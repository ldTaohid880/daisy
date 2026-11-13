import { _electron as electron, type ElectronApplication, type Page } from '@playwright/test';
import { join } from 'node:path';

/** Starts the built app and gives tests a page object. Run `pnpm build` first. */
export class DaisyAppDriver {
  #app: ElectronApplication | undefined;

  async launch(): Promise<Page> {
    // Launch the app folder (package.json "main" → out/main/index.js) so app.getAppPath() matches `pnpm dev`.
    this.#app = await electron.launch({ args: [join(import.meta.dirname, '../..')] });
    return this.#app.firstWindow();
  }

  async close(): Promise<void> {
    await this.#app?.close();
  }
}
