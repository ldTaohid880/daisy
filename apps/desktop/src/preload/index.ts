/**
 * Preload: the only bridge between the renderer and Node. Exposes `window.daisy` with one function
 * per channel in @daisy/ipc, and nothing else (no ipcRenderer, no Node).
 */
import { contextBridge, ipcRenderer } from 'electron';
import { channels, type DaisyApi } from '@daisy/ipc';

class PreloadBridge {
  expose(): void {
    contextBridge.exposeInMainWorld('daisy', this.#buildApi());
  }

  #buildApi(): DaisyApi {
    const entries = Object.entries(channels).map(([key, channel]) => [
      key,
      (request: unknown) => ipcRenderer.invoke(channel.name, channel.request.parse(request)),
    ]);
    return Object.fromEntries(entries) as DaisyApi;
  }
}

new PreloadBridge().expose();
