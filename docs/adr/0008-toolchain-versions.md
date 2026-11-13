# 0008. Toolchain versions

- **Status:** Accepted
- **Date:** 2026-11-13
- **Supersedes in PLAN.md / UI_DESIGN_PLAN.md:** PLAN.md 15 versions ("current stable").

## Context

Versions as of November 2026.

## Decision

Node 24 LTS for tooling (the same major Electron 45 embeds), pnpm 10, TypeScript 6.0 (move to the native TypeScript 7 when typescript-eslint supports it), Vite 8, Vitest 4.1, React 19, Zod 4, MCP SDK v2. Electron stays within the latest three majors.

## Consequences

One Node major for build and runtime avoids surprises. Task M00-T01 verifies every range resolves and works together, and records any pin here.

## Verified versions (M00-T01, 2026-11-13, Windows 11)

`pnpm install` with Node 24.22.3 and pnpm 10.20.0 resolved these; `pnpm check`, `pnpm build`, `pnpm test:e2e`
and the native addon build (MSVC 19.51, VS 2026, CMake 4.4) pass with them. `pnpm-lock.yaml` holds the exact tree.

| Package                             | Range                   | Resolved | Note                                                                                                                                                                                                              |
| ----------------------------------- | ----------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| typescript                          | ~6.0.2                  | 6.0.3    | Stay on 6.0: typescript-eslint 8.72 supports `<6.1.0`; TS 7 waits for it                                                                                                                                          |
| typescript-eslint                   | ^8.46.0                 | 8.72.2   |                                                                                                                                                                                                                   |
| eslint / @eslint/js                 | ^9.39.0                 | 9.39.5   | ESLint 10 is out; upgrade is a separate task                                                                                                                                                                      |
| vite                                | ^8.0.0                  | 8.3.8    |                                                                                                                                                                                                                   |
| electron-vite                       | **^6.0.0** (was ^5.0.0) | 6.0.0    | 5.x supports Vite ≤ 7 only. v6 renames `rollupOptions` → `rolldownOptions`, replaces `externalizeDepsPlugin` with `build.externalizeDeps`, and externalises deps in the preload by default (we set it to `false`) |
| @vitejs/plugin-react                | ^6.0.0                  | 6.3.0    | Requires Vite 8                                                                                                                                                                                                   |
| electron                            | ^45.2.0                 | 45.3.1   |                                                                                                                                                                                                                   |
| electron-builder                    | ^26.0.0                 | 26.18.0  |                                                                                                                                                                                                                   |
| vitest / @vitest/browser-playwright | ^4.1.0                  | 4.1.12   | Vitest 5 is out; stay on 4.1 for now                                                                                                                                                                              |
| @playwright/test / playwright       | ^1.57.0                 | 1.65.0   |                                                                                                                                                                                                                   |
| react / react-dom                   | ^19.2.0                 | 19.3.1   |                                                                                                                                                                                                                   |
| zod                                 | ^4.1.0                  | 4.6.7    |                                                                                                                                                                                                                   |
| @modelcontextprotocol/server        | ^2.4.0                  | 2.4.0    |                                                                                                                                                                                                                   |
| @modelcontextprotocol/node          | **^2.1.2** (was ^2.4.0) | 2.1.2    | 2.4 does not exist; 2.1.2 is the latest and peers on server ^2.4.0                                                                                                                                                |
| cmake-js                            | ^7.3.1                  | 7.4.0    |                                                                                                                                                                                                                   |
| turbo                               | ^2.6.0                  | 2.11.11  |                                                                                                                                                                                                                   |
| prettier                            | ^3.6.0                  | 3.10.1   |                                                                                                                                                                                                                   |
