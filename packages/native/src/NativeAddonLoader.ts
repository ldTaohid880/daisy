import { existsSync } from 'node:fs';
import { createRequire } from 'node:module';
import type { DaisyNativeAddon, NativeStatus } from './DaisyNativeAddon.js';

/** The addon is required (AGENTS.md 3c: no fallbacks). Daisy does not start without it. */
export class NativeAddonError extends Error {
  override readonly name = 'NativeAddonError';
}

/**
 * Loads daisy_native.node from the first candidate path that exists (packaged location, then the dev
 * prebuild). Throws when none exists or the one found fails to load; there is no pure-Node fallback.
 */
export class NativeAddonLoader {
  readonly addon: DaisyNativeAddon;
  readonly status: NativeStatus;

  constructor(candidatePaths: readonly string[]) {
    const path = candidatePaths.find((candidate) => existsSync(candidate));
    if (path === undefined) {
      throw new NativeAddonError(
        `daisy_native.node not found. Build it with "pnpm --filter @daisy/native build". Looked in:\n  ${candidatePaths.join('\n  ')}`,
      );
    }
    const require = createRequire(import.meta.url);
    try {
      this.addon = require(path) as DaisyNativeAddon;
    } catch (error) {
      throw new NativeAddonError(`daisy_native.node at ${path} failed to load`, { cause: error });
    }
    this.status = { version: this.addon.version(), path };
  }
}
