# Handoff — where Daisy stands (2026-11-13)

Read this once at the start of the first Claude Code session, then follow AGENTS.md.

## Done

- Product spec (`PLAN.md`) and every screen designed (`UI_DESIGN_PLAN.md`, design canvas "Daisy — UI Design").
- Monorepo scaffold: Electron app, 13 packages, class-based TypeScript with DI (`@daisy/di`), ADRs 0001–0014.
- `@daisy/native`: C++ core + Node-API addon (SHA-256 / file hashing) (required, no fallback — ADR 0015); C++ tests and
  addon parity were verified on Linux (GCC and Clang). Windows build via cmake-js not yet run.
- Agent setup: AGENTS.md, CLAUDE.md, `.claude/` skills, subagents, commands, hooks; CI/CD in `.github/`.
- Roadmap M00–M24 with tasks in `docs/tasks/`.

## Not done yet (start here)

1. **M00-T01** — `pnpm install`, fix any version range that does not resolve (watch electron-vite ↔ Vite 8,
   @vitejs/plugin-react, typescript-eslint ↔ TypeScript), commit `pnpm-lock.yaml`, record pins in ADR 0008.
2. **M00-T02/T03** — make `pnpm check` green; `pnpm dev` opens the window; `pnpm build && pnpm test:e2e` passes.
   Also `pnpm --filter @daisy/native build && pnpm --filter @daisy/native test` on Windows.
3. **M00-T04/T05** — `git init`, create the GitHub repo, replace `OWNER_PLACEHOLDER`
   (apps/desktop/electron-builder.yml, .github/CODEOWNERS), protect `main`, first green CI.
4. Then M01 (`/plan-milestone M01`, then `/next-task`).

## Known gaps to check first

- Nothing has been installed or run on Windows yet; expect small fixes in configs.
- ESLint class-first rule (ADR 0011) was written but not yet run against the code.
- `.claude/hooks/*.ts` run with `node file.ts` (Node 24 type stripping); confirm they work in your shell.

Delete this file when M00 is done.
