import { describe, expect, it } from 'vitest';
import { Container } from '@daisy/di';
import { EditorModule } from '../EditorModule.js';
import { EditorTokens } from '../tokens.js';

describe('VersionService', () => {
  it('labels the version reported by the desktop shell', async () => {
    const api = {
      appInfo: () =>
        Promise.resolve({ version: '1.2.3', platform: 'linux' as const, nativeVersion: '0.1.0' }),
    };
    const c = new Container().load(new EditorModule(api));
    await expect(c.resolve(EditorTokens.VersionService).label()).resolves.toBe('Version 1.2.3');
  });
});
