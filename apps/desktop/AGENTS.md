# @daisy/desktop

The Electron app. It wires packages together; it holds almost no logic of its own.

- `src/main/` — main process (Node): windows, menus, IPC handlers, project-fs, MCP server, updates.
- `src/preload/` — exposes `window.daisy` from `@daisy/ipc` channels. Nothing else crosses.
- `src/renderer/` — mounts `@daisy/editor`. Keep it to the entry file.
- `e2e/` — Playwright tests against the built app (`pnpm build` then `pnpm test:e2e`).

**Rules:** keep `contextIsolation`, `sandbox`, `nodeIntegration: false` and the CSP exactly as they are unless an ADR changes them (docs/architecture/SECURITY.md). Every IPC handler validates input and output with the channel's Zod schemas. Main-process code never imports React or editor packages.

**Packaging:** `pnpm package` builds installers into `release/<version>/` for the current OS. Releases are made by CI from tags (docs/engineering/RELEASING.md).
