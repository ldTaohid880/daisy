#!/usr/bin/env node
// PostToolUse: run Prettier on the file that was just written, quietly. Never blocks.
import { spawnSync } from 'node:child_process';
import { readFileSync } from 'node:fs';

interface HookInput {
  readonly tool_input?: { readonly file_path?: string };
}

class FormatOnWrite {
  static readonly #formattable = /\.(ts|tsx|js|mjs|cjs|json|css|md|ya?ml|html)$/;

  run(input: HookInput): void {
    const file = input.tool_input?.file_path;
    if (!file || !FormatOnWrite.#formattable.test(file)) return;
    spawnSync('pnpm', ['exec', 'prettier', '--write', '--log-level', 'warn', file], {
      stdio: 'ignore',
      shell: process.platform === 'win32',
    });
  }
}

const raw = readFileSync(0, 'utf8');
new FormatOnWrite().run(raw ? (JSON.parse(raw) as HookInput) : {});
