#!/usr/bin/env node
// Lists tasks from docs/tasks/*.md by status. Usage: node scripts/check-tasks.ts [--next]
import { readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { Repo } from './lib/Repo.ts';

interface TaskRow {
  readonly id: string;
  readonly title: string;
  readonly status: string;
  readonly file: string;
}

class TaskBoard {
  readonly #dir = Repo.path('docs/tasks');
  readonly #rows: TaskRow[];

  constructor() {
    this.#rows = this.#load();
  }

  printNext(): void {
    const next = this.#rows.find((r) => r.status === 'todo');
    console.warn(next ? `${next.id}  ${next.title}  (docs/tasks/${next.file})` : 'No todo tasks left.');
  }

  printAll(): void {
    for (const r of this.#rows) console.warn(`${r.status.padEnd(12)} ${r.id.padEnd(9)} ${r.title}`);
  }

  #load(): TaskRow[] {
    const rows: TaskRow[] = [];
    for (const file of readdirSync(this.#dir)
      .filter((f) => /^M\d+.*\.md$/.test(f))
      .sort()) {
      const text = readFileSync(join(this.#dir, file), 'utf8');
      for (const m of text.matchAll(/^### (M\d+-T\d+)\s+(.+)\n+- \*\*Status:\*\* (\w[\w -]*)/gm)) {
        rows.push({ id: m[1] ?? '', title: (m[2] ?? '').trim(), status: (m[3] ?? '').trim(), file });
      }
    }
    return rows;
  }
}

const board = new TaskBoard();
if (process.argv.includes('--next')) board.printNext();
else board.printAll();
