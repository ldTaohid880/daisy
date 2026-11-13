import type { Container, Module } from '@daisy/di';
import { app } from 'electron';
import { McpModule } from '@daisy/mcp-server';
import { NativeModule, NativePaths } from '@daisy/native';
import { DaisyApplication } from './DaisyApplication.js';
import { AppInfoHandler } from './ipc/AppInfoHandler.js';
import { IpcRouter } from './ipc/IpcRouter.js';
import { MainWindowFactory } from './MainWindowFactory.js';
import { SessionSecurity } from './SessionSecurity.js';
import { MainTokens } from './tokens.js';
import { UpdateService } from './UpdateService.js';

/** Main-process registrations. Add a new IPC handler class to the handler list below. */
export class MainModule implements Module {
  readonly #isDev: boolean;

  constructor(isDev: boolean) {
    this.#isDev = isDev;
  }

  register(container: Container): void {
    container
      .load(new McpModule(), new NativeModule(NativePaths.forApp(process.resourcesPath, app.getAppPath())))
      .bindValue(MainTokens.IsDev, this.#isDev)
      .bindClass(MainTokens.WindowFactory, MainWindowFactory)
      .bindClass(MainTokens.IpcRouter, IpcRouter)
      .bindClass(MainTokens.AppInfoHandler, AppInfoHandler)
      .bindFactory(MainTokens.IpcHandlers, (c) => [c.resolve(MainTokens.AppInfoHandler)])
      .bindClass(MainTokens.SessionSecurity, SessionSecurity)
      .bindClass(MainTokens.Updates, UpdateService)
      .bindClass(MainTokens.Application, DaisyApplication);
  }
}
