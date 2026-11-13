import { Token } from '@daisy/di';
import type { DaisyApi } from '@daisy/ipc';
import type { VersionService } from './services/VersionService.js';

export const EditorTokens = {
  Platform: new Token<DaisyApi>('editor.Platform'),
  VersionService: new Token<VersionService>('editor.VersionService'),
} as const;
