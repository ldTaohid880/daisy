// electron-builder beforePack hook. The native addon is required (ADR 0015), but electron-builder silently
// skips a missing `extraResources` folder, so a build for an arch without a prebuild would ship an app that
// cannot start. Fail the package step instead.
import { existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { Arch } from 'electron-builder';

class RequireNativePrebuild {
  static #prebuilds = join(
    dirname(fileURLToPath(import.meta.url)),
    '..',
    '..',
    '..',
    'packages',
    'native',
    'prebuilds',
  );

  /** @param {import('electron-builder').BeforePackContext} context */
  static check(context) {
    const key = `${context.electronPlatformName}-${Arch[context.arch]}`;
    const file = join(RequireNativePrebuild.#prebuilds, key, 'daisy_native.node');
    if (!existsSync(file)) {
      throw new Error(
        `Native addon missing for ${key}: ${file}. Build it with DAISY_NATIVE_ARCHS=<arch> pnpm --filter @daisy/native build.`,
      );
    }
  }
}

export default (context) => RequireNativePrebuild.check(context);
