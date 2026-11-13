import type { ContentHasher } from './ContentHasher.js';
import type { DaisyNativeAddon } from './DaisyNativeAddon.js';

export class NativeContentHasher implements ContentHasher {
  readonly #addon: DaisyNativeAddon;

  constructor(addon: DaisyNativeAddon) {
    this.#addon = addon;
  }

  hashBytes(data: Uint8Array | string): string {
    return this.#addon.sha256(data);
  }

  hashFile(path: string): Promise<string> {
    return this.#addon.hashFile(path);
  }
}
