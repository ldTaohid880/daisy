import type { Channel, RequestOf, ResponseOf } from '@daisy/ipc';
import type { z } from 'zod';

/** One class per channel. The router validates input and output with the channel's schemas. */
export interface IpcHandler<C extends Channel<z.ZodType, z.ZodType> = Channel<z.ZodType, z.ZodType>> {
  readonly channel: C;
  handle(request: RequestOf<C>): Promise<ResponseOf<C>> | ResponseOf<C>;
}
