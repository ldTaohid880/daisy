#!/usr/bin/env node
// Removes build output. Usage: node scripts/clean.ts [dir] [extra folders…]
import { rmSync } from 'node:fs';
import { join, resolve } from 'node:path';

class BuildCleaner {
  static readonly #standard = ['dist', 'out', 'coverage', '.turbo'];

  clean(dir: string, extra: readonly string[]): void {
    for (const name of [...BuildCleaner.#standard, ...extra])
      rmSync(join(resolve(dir), name), { recursive: true, force: true });
  }
}

const [dir = '.', ...extra] = process.argv.slice(2);
new BuildCleaner().clean(dir, extra);
