import { describe, expect, it } from 'vitest';
import { z } from 'zod';
import { Channel, channels } from './index.js';

describe('Channel', () => {
  it('validates names', () => {
    expect(() => new Channel('Bad Name', z.object({}), z.object({}))).toThrow();
  });
  it('parses the app.info response', () => {
    const info = { version: '0.0.0', platform: 'win32', nativeVersion: '0.1.0' };
    expect(channels.appInfo.response.parse(info)).toEqual(info);
  });
});
