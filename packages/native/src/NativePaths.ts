import { join } from 'node:path';

/** Where the addon lives: packaged in resources/native, or built into packages/native/prebuilds in dev. */
export class NativePaths {
  static readonly fileName = 'daisy_native.node';

  static platformKey(platform: string = process.platform, arch: string = process.arch): string {
    return `${platform}-${arch}`;
  }

  /** Candidate paths for the Electron main process, packaged first. */
  static forApp(resourcesPath: string, appPath: string): string[] {
    return [
      join(resourcesPath, 'native', NativePaths.fileName),
      join(
        appPath,
        '..',
        '..',
        'packages',
        'native',
        'prebuilds',
        NativePaths.platformKey(),
        NativePaths.fileName,
      ),
    ];
  }

  /** Candidate path inside this package (tests). */
  static forPackage(packageRoot: string): string[] {
    return [join(packageRoot, 'prebuilds', NativePaths.platformKey(), NativePaths.fileName)];
  }
}
