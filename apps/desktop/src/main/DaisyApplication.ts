import { app, BrowserWindow } from 'electron';
import type { IpcRouter } from './ipc/IpcRouter.js';
import type { IpcHandler } from './ipc/IpcHandler.js';
import type { MainWindowFactory } from './MainWindowFactory.js';
import type { SessionSecurity } from './SessionSecurity.js';
import type { UpdateService } from './UpdateService.js';
import { MainTokens } from './tokens.js';

/** Lifecycle of the desktop app. Built by the container in `index.ts`. */
export class DaisyApplication {
  static readonly inject = [
    MainTokens.WindowFactory,
    MainTokens.IpcRouter,
    MainTokens.IpcHandlers,
    MainTokens.SessionSecurity,
    MainTokens.Updates,
    MainTokens.IsDev,
  ] as const;

  readonly #windows: MainWindowFactory;
  readonly #router: IpcRouter;
  readonly #handlers: readonly IpcHandler[];
  readonly #security: SessionSecurity;
  readonly #updates: UpdateService;
  readonly #isDev: boolean;

  constructor(
    windows: MainWindowFactory,
    router: IpcRouter,
    handlers: readonly IpcHandler[],
    security: SessionSecurity,
    updates: UpdateService,
    isDev: boolean,
  ) {
    this.#windows = windows;
    this.#router = router;
    this.#handlers = handlers;
    this.#security = security;
    this.#updates = updates;
    this.#isDev = isDev;
  }

  async start(): Promise<void> {
    app.on('window-all-closed', () => {
      if (process.platform !== 'darwin') app.quit();
    });
    await app.whenReady();
    this.#security.apply();
    this.#router.registerAll(this.#handlers);
    this.#windows.create();
    if (!this.#isDev) this.#updates.start();
    app.on('activate', () => {
      if (BrowserWindow.getAllWindows().length === 0) this.#windows.create();
    });
  }
}
