import type { DaisyApi } from '@daisy/ipc';
import { EditorTokens } from '../tokens.js';

/** Supplies the app version for Help › About and the start screen. */
export class VersionService {
  static readonly inject = [EditorTokens.Platform] as const;

  readonly #platform: DaisyApi;

  constructor(platform: DaisyApi) {
    this.#platform = platform;
  }

  async label(): Promise<string> {
    const info = await this.#platform.appInfo({});
    return `Version ${info.version}`;
  }
}
