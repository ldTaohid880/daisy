import type { z } from 'zod';

/**
 * One main ↔ renderer request/response channel. Both directions are Zod schemas; the preload
 * validates requests and the main process validates both (docs/architecture/IPC.md).
 */
export class Channel<Req extends z.ZodType, Res extends z.ZodType> {
  static readonly #namePattern = /^[a-z]+(\.[a-z][a-zA-Z]*)+$/;

  readonly name: string;
  readonly request: Req;
  readonly response: Res;

  constructor(name: string, request: Req, response: Res) {
    if (!Channel.#namePattern.test(name)) {
      throw new Error(`IPC channel name must look like "area.action": ${name}`);
    }
    this.name = name;
    this.request = request;
    this.response = response;
  }
}

export type RequestOf<C> = C extends Channel<infer Req, z.ZodType> ? z.infer<Req> : never;
export type ResponseOf<C> = C extends Channel<z.ZodType, infer Res> ? z.infer<Res> : never;
