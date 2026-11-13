import { app } from 'electron';
import { channels, type ResponseOf } from '@daisy/ipc';
import { NativeTokens, type NativeStatus } from '@daisy/native';
import type { IpcHandler } from './IpcHandler.js';

export class AppInfoHandler implements IpcHandler<typeof channels.appInfo> {
  static readonly inject = [NativeTokens.Status] as const;

  readonly channel = channels.appInfo;
  readonly #native: NativeStatus;

  constructor(native: NativeStatus) {
    this.#native = native;
  }

  handle(): ResponseOf<typeof channels.appInfo> {
    return {
      version: app.getVersion(),
      platform: process.platform as 'win32' | 'darwin' | 'linux',
      nativeVersion: this.#native.version,
    };
  }
}
