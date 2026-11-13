# @daisy/editor

The editor application: shell, panels, tools, stores.

**Owns:** docStore (Immer + history), editorStore, tools (one file each), panels (layers, properties, assets…), shell (top bar, options bar, tool strip, status bar, dialogs), Home.

**Specification:** PLAN.md 3–6 (UX, interface, tools, properties); UI_DESIGN_PLAN.md (every screen D-01…D-59)

**May import:** @daisy/di, @daisy/model, @daisy/css, @daisy/html, @daisy/export, @daisy/ipc, @daisy/renderer, @daisy/ui · react, react-dom, zustand, immer, @tanstack/react-virtual, culori. The full graph is in `docs/architecture/dependencies.json` and is checked by `pnpm check:deps`.

**Rules:** Tools and panels change the document only through store commands. Never call window.daisy outside src/platform/.

**Tests:** `pnpm --filter @daisy/editor test`. Test files sit next to the code as `*.test.ts`.
