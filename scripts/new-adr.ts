#!/usr/bin/env node
// Creates docs/adr/NNNN-title.md from the template. Usage: pnpm new:adr "Use X for Y"
import { readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { Repo } from './lib/Repo.ts';

class AdrWriter {
  readonly #dir = Repo.path('docs/adr');

  create(title: string): string {
    const number = String(this.#nextNumber()).padStart(4, '0');
    const slug = title
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-|-$/g, '');
    const file = join(this.#dir, `${number}-${slug}.md`);
    const body = readFileSync(join(this.#dir, '0000-template.md'), 'utf8')
      .replace('NNNN', number)
      .replace('TITLE', title)
      .replace('YYYY-MM-DD', new Date().toISOString().slice(0, 10));
    writeFileSync(file, body);
    return file;
  }

  #nextNumber(): number {
    const used = readdirSync(this.#dir)
      .map((f) => parseInt(f, 10))
      .filter(Number.isFinite);
    return Math.max(0, ...used) + 1;
  }
}

const title = process.argv.slice(2).join(' ').trim();
if (!title) {
  console.error('Usage: pnpm new:adr "Decision title"');
  process.exitCode = 1;
} else {
  console.warn(`Created ${new AdrWriter().create(title)}`);
}
