#!/usr/bin/env node
// Builds daisy_native.node with cmake-js into prebuilds/<platform>-<arch>/.
// The addon is required (AGENTS.md 3c, ADR 0015): without CMake or a compiler this fails the build.
// DAISY_NATIVE_ARCHS="x64,arm64" builds several architectures; on macOS one universal binary is built.
import { spawnSync } from 'node:child_process';
import { copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

class NativeBuilder {
  static readonly #fileName = 'daisy_native.node';

  readonly #root = join(dirname(fileURLToPath(import.meta.url)), '..');
  readonly #archs = (process.env['DAISY_NATIVE_ARCHS'] ?? process.arch)
    .split(',')
    .map((a) => a.trim())
    .filter(Boolean);

  run(): number {
    if (!this.#hasCmake()) return this.#fail('CMake was not found on PATH');
    if (process.platform === 'darwin') return this.#buildMacUniversal();
    for (const arch of this.#archs) {
      const status = this.#build(arch, []);
      if (status !== 0) return this.#fail(`cmake-js failed for ${arch}`);
    }
    return 0;
  }

  #buildMacUniversal(): number {
    const status = this.#build('universal', ['--CDCMAKE_OSX_ARCHITECTURES=arm64;x86_64']);
    if (status !== 0) return this.#fail('cmake-js failed for the macOS universal build');
    const built = join(this.#root, 'build', 'darwin-universal', 'Release', NativeBuilder.#fileName);
    for (const arch of ['arm64', 'x64']) this.#publish(built, `darwin-${arch}`);
    return 0;
  }

  #build(arch: string, extra: readonly string[]): number {
    const out = join('build', `${process.platform}-${arch}`);
    const archArgs = arch === 'universal' ? [] : ['--arch', arch];
    // Run cmake-js's CLI with this Node directly: no shell, so arguments are never re-parsed.
    const result = spawnSync(
      process.execPath,
      [
        this.#cmakeJsBin(),
        'compile',
        '--directory',
        'cpp',
        '--out',
        out,
        '--config',
        'Release',
        ...archArgs,
        '--CDDAISY_BUILD_TESTS=OFF',
        ...extra,
      ],
      { cwd: this.#root, stdio: 'inherit' },
    );
    if (result.status === 0 && arch !== 'universal') {
      this.#publish(join(this.#root, out, 'Release', NativeBuilder.#fileName), `${process.platform}-${arch}`);
    }
    return result.status ?? 1;
  }

  #publish(builtFile: string, key: string): void {
    if (!existsSync(builtFile)) throw new Error(`Expected build output missing: ${builtFile}`);
    const dir = join(this.#root, 'prebuilds', key);
    mkdirSync(dir, { recursive: true });
    copyFileSync(builtFile, join(dir, NativeBuilder.#fileName));
    console.warn(`@daisy/native: built prebuilds/${key}/${NativeBuilder.#fileName}`);
  }

  #cmakeJsBin(): string {
    const require = createRequire(join(this.#root, 'package.json'));
    return join(dirname(require.resolve('cmake-js/package.json')), 'bin', 'cmake-js');
  }

  #hasCmake(): boolean {
    return spawnSync('cmake', ['--version'], { stdio: 'ignore' }).status === 0;
  }

  #fail(reason: string): number {
    console.error(`@daisy/native: ${reason}. The addon is required; install CMake and a C++ compiler.`);
    return 1;
  }
}

process.exitCode = new NativeBuilder().run();
