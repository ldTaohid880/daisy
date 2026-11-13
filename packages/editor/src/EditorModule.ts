import type { Container, Module } from '@daisy/di';
import type { DaisyApi } from '@daisy/ipc';
import { ElectronPlatform, UnavailablePlatform } from './platform/Platform.js';
import { VersionService } from './services/VersionService.js';
import { EditorTokens } from './tokens.js';

/** Registers the editor's services. The renderer entry loads it into the root container. */
export class EditorModule implements Module {
  readonly #api: DaisyApi | undefined;

  constructor(api: DaisyApi | undefined) {
    this.#api = api;
  }

  register(container: Container): void {
    container
      .bindValue(
        EditorTokens.Platform,
        this.#api ? new ElectronPlatform(this.#api) : new UnavailablePlatform(),
      )
      .bindClass(EditorTokens.VersionService, VersionService);
  }
}
