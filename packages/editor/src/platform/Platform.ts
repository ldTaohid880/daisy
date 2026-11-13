import type { DaisyApi } from '@daisy/ipc';

/** The desktop shell, as the editor sees it. Only this folder knows about `window.daisy`. */
export class ElectronPlatform implements DaisyApi {
  readonly #api: DaisyApi;

  constructor(api: DaisyApi) {
    this.#api = api;
  }

  appInfo(req: Parameters<DaisyApi['appInfo']>[0]): ReturnType<DaisyApi['appInfo']> {
    return this.#api.appInfo(req);
  }
}

/** Used when the editor runs outside Electron (unit tests, storybook-like harnesses). */
export class UnavailablePlatform implements DaisyApi {
  appInfo(): never {
    throw new Error('The desktop shell is not available: window.daisy is missing.');
  }
}
