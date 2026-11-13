import type { Container, Module } from '@daisy/di';
import { NativeAddonLoader } from './NativeAddonLoader.js';
import { NativeContentHasher } from './NativeContentHasher.js';
import { NativeTokens } from './tokens.js';

/** Registers native services. Loading throws when the addon is missing: there is no fallback (AGENTS.md 3c). */
export class NativeModule implements Module {
  readonly #candidatePaths: readonly string[];

  constructor(candidatePaths: readonly string[]) {
    this.#candidatePaths = candidatePaths;
  }

  register(container: Container): void {
    const loader = new NativeAddonLoader(this.#candidatePaths);
    container
      .bindValue(NativeTokens.Loader, loader)
      .bindValue(NativeTokens.Status, loader.status)
      .bindValue(NativeTokens.ContentHasher, new NativeContentHasher(loader.addon));
  }
}
