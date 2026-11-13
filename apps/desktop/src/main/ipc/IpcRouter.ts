import { ipcMain } from 'electron';
import type { IpcHandler } from './IpcHandler.js';

export class IpcRouter {
  registerAll(handlers: readonly IpcHandler[]): void {
    for (const handler of handlers) this.register(handler);
  }

  register(handler: IpcHandler): void {
    const { channel } = handler;
    ipcMain.handle(channel.name, async (_event, raw: unknown) => {
      const request = channel.request.parse(raw);
      return channel.response.parse(await handler.handle(request));
    });
  }
}
