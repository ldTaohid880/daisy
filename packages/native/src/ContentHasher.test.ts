import { createHash } from 'node:crypto';
import { mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';
import { Container } from '@daisy/di';
import {
  AssetIds,
  NativeAddonError,
  NativeAddonLoader,
  NativeModule,
  NativePaths,
  NativeTokens,
} from './index.js';

// The addon must be built (turbo runs `build` before `test` here). A missing addon fails these tests.
const packageRoot = join(dirname(fileURLToPath(import.meta.url)), '..');
const loader = new NativeAddonLoader(NativePaths.forPackage(packageRoot));
const hasher = new Container()
  .load(new NativeModule(NativePaths.forPackage(packageRoot)))
  .resolve(NativeTokens.ContentHasher);
/** Test oracle only: node:crypto is never used by Daisy itself. */
const reference = (data: Uint8Array | string): string => createHash('sha256').update(data).digest('hex');

const VECTORS: readonly (readonly [string, string])[] = [
  ['', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'],
  ['abc', 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'],
];

describe('NativeAddonLoader', () => {
  it('throws when the addon is missing (no fallback)', () => {
    expect(() => new NativeAddonLoader(['/no/such/daisy_native.node'])).toThrow(NativeAddonError);
  });
  it('makes the container fail when the addon is missing', () => {
    expect(() => new Container().load(new NativeModule(['/no/such/daisy_native.node']))).toThrow(
      /daisy_native\.node not found/,
    );
  });
  it('reports the loaded addon', () => {
    expect(loader.status.version).toMatch(/^\d+\.\d+\.\d+/);
    expect(loader.status.path).toContain(NativePaths.fileName);
  });
});

describe('NativeContentHasher', () => {
  it.each(VECTORS)('hashes %j', (input, expected) => {
    expect(hasher.hashBytes(input)).toBe(expected);
  });
  it('makes 16-character asset ids', () => {
    expect(AssetIds.fromHash(hasher.hashBytes('abc'))).toBe('ba7816bf8f01cfea');
  });
  it('matches SHA-256 on buffers of many sizes', () => {
    for (const size of [1, 55, 56, 63, 64, 65, 1000, 65_537]) {
      const data = new Uint8Array(size).map((_, i) => (i * 131 + size) % 256);
      expect(hasher.hashBytes(data)).toBe(reference(data));
    }
  });
  it('hashes files off the main thread and rejects missing files', async () => {
    const dir = mkdtempSync(join(tmpdir(), 'daisy-native-'));
    const file = join(dir, 'asset.bin');
    const bytes = new Uint8Array(300_001).map((_, i) => i % 251);
    writeFileSync(file, bytes);
    try {
      await expect(hasher.hashFile(file)).resolves.toBe(reference(bytes));
      await expect(hasher.hashFile(join(dir, 'missing.bin'))).rejects.toThrow(/Cannot open file/);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });
  it('raises a TypeError for wrong arguments', () => {
    expect(() => loader.addon.sha256(42 as unknown as string)).toThrow(TypeError);
  });
});
