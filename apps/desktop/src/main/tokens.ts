import { Token } from '@daisy/di';
import type { DaisyApplication } from './DaisyApplication.js';
import type { AppInfoHandler } from './ipc/AppInfoHandler.js';
import type { IpcHandler } from './ipc/IpcHandler.js';
import type { IpcRouter } from './ipc/IpcRouter.js';
import type { MainWindowFactory } from './MainWindowFactory.js';
import type { SessionSecurity } from './SessionSecurity.js';
import type { UpdateService } from './UpdateService.js';

export const MainTokens = {
  Application: new Token<DaisyApplication>('main.Application'),
  WindowFactory: new Token<MainWindowFactory>('main.WindowFactory'),
  IpcRouter: new Token<IpcRouter>('main.IpcRouter'),
  IpcHandlers: new Token<readonly IpcHandler[]>('main.IpcHandlers'),
  AppInfoHandler: new Token<AppInfoHandler>('main.AppInfoHandler'),
  SessionSecurity: new Token<SessionSecurity>('main.SessionSecurity'),
  Updates: new Token<UpdateService>('main.Updates'),
  IsDev: new Token<boolean>('main.IsDev'),
} as const;
