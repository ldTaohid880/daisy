#!/usr/bin/env node
// Scaffolds packages/<name>. Usage: pnpm new:package <name> <pure|dom|react|node>
// Afterwards: add it to docs/architecture/dependencies.json and record why in an ADR.
import { existsSync, mkdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { Repo } from './lib/Repo.ts';

type Env = 'pure' | 'dom' | 'react' | 'node';

class PackageScaffolder {
  static readonly #libs: Readonly<Record<Env, readonly string[]>> = {
    pure: ['ES2024'],
    node: ['ES2024'],
    dom: ['ES2024', 'DOM', 'DOM.Iterable'],
    react: ['ES2024', 'DOM', 'DOM.Iterable'],
  };

  readonly #name: string;
  readonly #env: Env;
  readonly #dir: string;

  constructor(name: string, env: Env) {
    this.#name = name;
    this.#env = env;
    this.#dir = Repo.path('packages', name);
  }

  create(): void {
    if (existsSync(this.#dir)) throw new Error(`${this.#dir} exists`);
    mkdirSync(join(this.#dir, 'src'), { recursive: true });
    this.#json('package.json', {
      name: `@daisy/${this.#name}`,
      version: '0.0.0',
      private: true,
      type: 'module',
      exports: { '.': './src/index.ts' },
      scripts: {
        typecheck: 'tsc -p tsconfig.json',
        test: 'vitest run --passWithNoTests',
        clean: 'node ../../scripts/clean.ts .',
      },
      dependencies: { '@daisy/di': 'workspace:*' },
    });
    this.#json('tsconfig.json', {
      extends: '../../tsconfig.base.json',
      compilerOptions: {
        lib: PackageScaffolder.#libs[this.#env],
        types: this.#env === 'node' ? ['node'] : [],
        ...(this.#env === 'react' ? { jsx: 'react-jsx' } : {}),
      },
      include: ['src'],
    });
    this.#text(
      'vitest.config.ts',
      `import { defineConfig } from 'vitest/config';\n\nexport default defineConfig({ test: { name: '${this.#name}', include: ['src/**/*.test.{ts,tsx}'] } });\n`,
    );
    this.#text('src/index.ts', `/** @daisy/${this.#name} */\nexport {};\n`);
    this.#text(
      'AGENTS.md',
      `# @daisy/${this.#name}\n\nWhat it owns, its spec sections, what it may import, its rules and how to test it.\n`,
    );
  }

  #json(file: string, value: unknown): void {
    this.#text(file, JSON.stringify(value, null, 2) + '\n');
  }

  #text(file: string, value: string): void {
    writeFileSync(join(this.#dir, file), value);
  }
}

const [name, env = 'pure'] = process.argv.slice(2);
if (!name || !/^[a-z][a-z-]*$/.test(name) || !['pure', 'dom', 'react', 'node'].includes(env)) {
  console.error('Usage: pnpm new:package <name> <pure|dom|react|node>');
  process.exitCode = 1;
} else {
  new PackageScaffolder(name, env as Env).create();
  console.warn(
    `Created packages/${name}. Next: add it to docs/architecture/dependencies.json, then pnpm install.`,
  );
}
