#!/usr/bin/env node
// PreToolUse: refuse edits to generated or managed files. Exit code 2 blocks the tool and shows the reason.
import { readFileSync } from 'node:fs';

interface HookInput {
  readonly tool_input?: { readonly file_path?: string };
}

class ProtectedFilesGuard {
  static readonly #rules: readonly (readonly [RegExp, string])[] = [
    [/(^|\/)pnpm-lock\.yaml$/, 'pnpm-lock.yaml is managed by pnpm. Run pnpm install instead.'],
    [/\/(dist|out|release|coverage|node_modules)\//, 'Build output is generated. Change the source instead.'],
    [/(^|\/)CHANGELOG\.md$/, 'CHANGELOG.md is written by release-please.'],
    [/(^|\/)\.env(\.|$)/, 'Secrets files are never edited by agents.'],
  ];

  check(input: HookInput): number {
    const file = (input.tool_input?.file_path ?? '').replaceAll('\\', '/');
    for (const [pattern, reason] of ProtectedFilesGuard.#rules) {
      if (pattern.test(file)) {
        console.error(`Blocked: ${file}\n${reason}`);
        return 2;
      }
    }
    return 0;
  }
}

const raw = readFileSync(0, 'utf8');
process.exitCode = new ProtectedFilesGuard().check(raw ? (JSON.parse(raw) as HookInput) : {});
