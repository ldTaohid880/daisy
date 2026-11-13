/** @daisy/ipc — typed contracts between the main process and the renderer. */
import { z } from 'zod';
import { Channel, type RequestOf, type ResponseOf } from './Channel.js';

export { Channel, type RequestOf, type ResponseOf } from './Channel.js';

/** Every channel, by API name. The preload exposes exactly these as `window.daisy`. */
export const channels = {
  /** Help › About shows the version. */
  appInfo: new Channel(
    'app.info',
    z.object({}),
    z.object({
      version: z.string(),
      platform: z.enum(['win32', 'darwin', 'linux']),
      /** Version of the C++ addon (ADR 0013), for Help › About and diagnostics. */
      nativeVersion: z.string(),
    }),
  ),
} as const;

export type Channels = typeof channels;

/** The API the preload script exposes as `window.daisy`. */
export type DaisyApi = {
  readonly [K in keyof Channels]: (req: RequestOf<Channels[K]>) => Promise<ResponseOf<Channels[K]>>;
};
