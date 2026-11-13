#!/usr/bin/env node
// Fails when a workspace package depends on, or imports, a Daisy package the graph does not allow.
// Graph: docs/architecture/dependencies.json. Run: node scripts/check-deps.ts
import { readdirSync, readFileSync } from 'node:fs';
import { join, relative } from 'node:path';
import { Repo } from './lib/Repo.ts';

interface Graph {
  readonly packages: Readonly<Record<string, readonly string[]>>;
  readonly devOnly: readonly string[];
}
interface Manifest {
  readonly name: string;
  readonly dependencies?: Readonly<Record<string, string>>;
}

class DependencyBoundaryChecker {
  readonly #graph = Repo.readJson(Repo.path('docs/architecture/dependencies.json')) as Graph;
  readonly #errors: string[] = [];

  run(): number {
    for (const dir of this.#packageDirs()) this.#checkPackage(dir);
    if (this.#errors.length > 0) {
      console.error('Package boundary violations:\n' + this.#errors.map((e) => '  - ' + e).join('\n'));
      return 1;
    }
    console.warn('check-deps: all package boundaries respected');
    return 0;
  }

  #packageDirs(): string[] {
    return ['apps', 'packages'].flatMap((d) => readdirSync(Repo.path(d)).map((n) => Repo.path(d, n)));
  }

  #checkPackage(dir: string): void {
    let manifest: Manifest;
    try {
      manifest = Repo.readJson(join(dir, 'package.json')) as Manifest;
    } catch {
      return;
    }
    const allowed = this.#graph.packages[manifest.name];
    if (!allowed) {
      this.#errors.push(`${manifest.name}: not listed in docs/architecture/dependencies.json`);
      return;
    }
    for (const dep of Object.keys(manifest.dependencies ?? {})) {
      if (dep.startsWith('@daisy/') && !allowed.includes(dep))
        this.#errors.push(`${manifest.name}: dependency ${dep} is not allowed`);
    }
    const ok = new Set([...allowed, ...this.#graph.devOnly, manifest.name]);
    for (const file of Repo.listFiles(join(dir, 'src'), /\.(ts|tsx)$/))
      this.#checkImports(file, manifest.name, ok);
  }

  #checkImports(file: string, owner: string, ok: ReadonlySet<string>): void {
    const isTest = /\.test\.tsx?$/.test(file);
    for (const m of readFileSync(file, 'utf8').matchAll(/from\s+['"](@daisy\/[a-z-]+)/g)) {
      const target = m[1] ?? '';
      if (!ok.has(target) || (!isTest && this.#graph.devOnly.includes(target))) {
        this.#errors.push(`${relative(Repo.root, file)}: imports ${target}, which ${owner} may not use`);
      }
    }
  }
}

process.exitCode = new DependencyBoundaryChecker().run();
