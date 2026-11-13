import { BrowserWindow, shell } from 'electron';
import { join } from 'node:path';
import { MainTokens } from './tokens.js';

/**
 * Creates editor windows with the hardened settings of docs/architecture/SECURITY.md.
 * Do not relax a webPreferences value without an ADR.
 */
export class MainWindowFactory {
  static readonly inject = [MainTokens.IsDev] as const;

  readonly #isDev: boolean;

  constructor(isDev: boolean) {
    this.#isDev = isDev;
  }

  create(): BrowserWindow {
    const win = new BrowserWindow({
      width: 1600,
      height: 1000,
      minWidth: 1280,
      minHeight: 800,
      show: false,
      backgroundColor: '#1f1f1f',
      title: 'Daisy',
      webPreferences: {
        preload: join(import.meta.dirname, '../preload/index.cjs'),
        contextIsolation: true,
        nodeIntegration: false,
        sandbox: true,
        webSecurity: true,
        spellcheck: false,
      },
    });
    win.once('ready-to-show', () => {
      win.show();
    });
    this.#lockNavigation(win);
    this.#load(win);
    return win;
  }

  #lockNavigation(win: BrowserWindow): void {
    win.webContents.setWindowOpenHandler(({ url }) => {
      if (/^https?:\/\//.test(url)) void shell.openExternal(url);
      return { action: 'deny' };
    });
    win.webContents.on('will-navigate', (event, url) => {
      if (url !== win.webContents.getURL()) event.preventDefault();
    });
  }

  #load(win: BrowserWindow): void {
    const devUrl = process.env['ELECTRON_RENDERER_URL'];
    if (this.#isDev && devUrl) void win.loadURL(devUrl);
    else void win.loadFile(join(import.meta.dirname, '../renderer/index.html'));
  }
}
