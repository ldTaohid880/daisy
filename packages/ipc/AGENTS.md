# @daisy/ipc

Typed contracts between the Electron main process and the renderer.

**Owns:** Channel definitions (name, request schema, response schema), event definitions, the DaisyApi type the preload exposes.

**Specification:** docs/architecture/ARCHITECTURE.md "Process model"; docs/architecture/IPC.md

**May import:** @daisy/di, @daisy/model · zod. The full graph is in `docs/architecture/dependencies.json` and is checked by `pnpm check:deps`.

**Rules:** Every channel has a Zod schema for both directions. No channel may pass file paths the user did not choose.

**Tests:** `pnpm --filter @daisy/ipc test`. Test files sit next to the code as `*.test.ts`.
