import { Token } from '@daisy/di';
import type { ContentHasher } from './ContentHasher.js';
import type { NativeStatus } from './DaisyNativeAddon.js';
import type { NativeAddonLoader } from './NativeAddonLoader.js';

export const NativeTokens = {
  Loader: new Token<NativeAddonLoader>('native.Loader'),
  Status: new Token<NativeStatus>('native.Status'),
  ContentHasher: new Token<ContentHasher>('native.ContentHasher'),
} as const;
