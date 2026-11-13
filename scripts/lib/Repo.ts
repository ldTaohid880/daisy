import { readdirSync, readFileSync, statSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

/** Paths and file helpers shared by the repository scripts. */
export class Repo {
  static readonly root = join(dirname(fileURLToPath(import.meta.url)), '..', '..');

  static path(...parts: string[]): string {
    return join(Repo.root, ...parts);
  }

  /** Parsed JSON; the caller states the shape it expects. */
  static readJson(path: string): unknown {
    return JSON.parse(readFileSync(path, 'utf8'));
  }

  static listFiles(
    dir: string,
    pattern: RegExp,
    skip: readonly string[] = ['node_modules', 'dist', 'out'],
  ): string[] {
    const out: string[] = [];
    let names: string[];
    try {
      names = readdirSync(dir);
    } catch {
      return out;
    }
    for (const name of names) {
      if (skip.includes(name)) continue;
      const p = join(dir, name);
      if (statSync(p).isDirectory()) out.push(...Repo.listFiles(p, pattern, skip));
      else if (pattern.test(name)) out.push(p);
    }
    return out;
  }
}
