# Architecture

This document is the map. The specification is PLAN.md (behaviour, data, rendering, export) and
UI_DESIGN_PLAN.md (every screen). Where this map and PLAN.md disagree, the ADRs in `docs/adr/`
say which wins.

## 1. Process model (Electron, ADR 0001)

```
┌──────────────────────── Main process (Node 24) ────────────────────────┐
│ app lifecycle · windows · native dialogs · auto-update                 │
│ @daisy/project-fs  — project folders, autosave writer, versions, lock  │
│ @daisy/mcp-server  — MCP over HTTP 127.0.0.1 (+ stdio bridge)          │
│ IPC handlers (apps/desktop/src/main/ipc.ts), validated by @daisy/ipc   │
└──────────────▲───────────────────────────────────────▲─────────────────┘
               │ contextBridge: window.daisy (typed)   │ change requests / results
┌──────────────┴──────────── Renderer (Chromium) ──────┴─────────────────┐
│ @daisy/editor — React chrome, tools, panels, stores                    │
│   docStore (Zustand + Immer patches) = the ONE source of truth         │
│ @daisy/renderer — writes real DOM into the edit frame                  │
│ ┌ edit frame (iframe, sandbox without scripts, CSP) ┐ ┌ preview frame ┐│
│ │ the user's page, never executes anything          │ │ isolated, runs││
│ └────────────────────────────────────────────────────┘ │ scripts       ││
│                                                        └───────────────┘│
└─────────────────────────────────────────────────────────────────────────┘
```

- The **renderer owns the open document**. The main process never edits it; it loads and saves
  serialised snapshots and forwards MCP change requests as commands for the renderer to apply.
- The **edit frame** follows PLAN.md 9.2 and 13.3: real DOM, no script execution. The **preview
  frame** follows PLAN.md 13.4, adapted in ADR 0010.

## 2. Packages and the dependency rule

| Package        | Runs in                  | Depends on                                  |
| -------------- | ------------------------ | ------------------------------------------- |
| `di`           | anywhere (pure)          | —                                           |
| `model`        | anywhere (pure)          | di                                          |
| `css`          | anywhere                 | model                                       |
| `html`         | anywhere                 | model, css                                  |
| `export`       | anywhere                 | model, css, html                            |
| `ipc`          | anywhere                 | model                                       |
| `renderer`     | renderer (DOM, no React) | model, css                                  |
| `ui`           | renderer (React)         | —                                           |
| `editor`       | renderer (React)         | model, css, html, export, ipc, renderer, ui |
| `project-fs`   | main (Node)              | model, ipc, export, native                  |
| `mcp-server`   | main (Node)              | model, ipc                                  |
| `native`       | main (Node + C++ addon)  | — (ADR 0013)                                |
| `test-utils`   | tests                    | model                                       |
| `apps/desktop` | all three                | wires everything                            |

Every package also depends on `di` (left out of the table for brevity).

Rules (enforced by `pnpm check:deps` and ESLint):

1. Pure packages never touch the DOM, Node, React or Electron. They are where the hard logic
   lives, so they must be testable in milliseconds.
2. Renderer packages never import Node, Electron, `project-fs` or `mcp-server`; they reach the
   main process only through `packages/editor/src/platform/`.
3. Main-process code never imports React or renderer packages.
4. Adding an edge to the graph needs an ADR.

## 2a. Classes, modules and composition roots (ADR 0011)

```
packages/<pkg>/src/tokens.ts      Token<T> per service
packages/<pkg>/src/<Pkg>Module.ts  class XModule implements Module { register(container) }
apps/desktop/src/main/index.ts     new Container().load(new MainModule(...)) → Application.start()
apps/desktop/src/preload/index.ts  new PreloadBridge().expose()
apps/desktop/src/renderer/main.tsx new RendererBootstrap(window.daisy).mount('root')
tests                              new Container().load(module).createChild().bindValue(token, fake)
```

Services take collaborators in their constructors (`static readonly inject`). Commands, tools, generators,
renderers, adapters and handlers are all classes. React components are thin functions that call
`useService(Token)`.

C++ enters only as the Node addon in `packages/native`, behind DI tokens; the addon is required, with no fallback (ADRs 0013, 0014, 0015).

## 3. Data flow of one edit (PLAN.md 10.6)

```
pointer → Tool (editor/tools) → store.run(command)   ← MCP change request (approved) joins here
        → model command produces Immer patches + inverse patches
        → history entry
        → @daisy/renderer applies patches to edit-frame DOM/CSSOM (via @daisy/css)
        → overlay re-measures
        → autosave scheduler → window.daisy.project.save(snapshot) → project-fs (atomic write)
```

Export runs the same `@daisy/css` and `@daisy/html` generators the canvas uses (PLAN.md 11.1),
then `project-fs` writes the file map from `@daisy/export`.

## 4. Where each part of the specification lives in code

| Specification                                     | Package / folder                                                                               |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| PLAN 10 data architecture, 12.7 schema versions   | `packages/model`                                                                               |
| PLAN 11 CSS generation                            | `packages/css`                                                                                 |
| PLAN 8 element system, 14.2 HTML                  | `packages/html` (+ element registry in `packages/model/src/registry`)                          |
| PLAN 9 rendering and canvas                       | `packages/renderer`, `packages/editor/src/canvas`                                              |
| PLAN 5 tools                                      | `packages/editor/src/tools` (one file per tool)                                                |
| PLAN 6 properties                                 | `packages/editor/src/panels/properties` (+ registry in model)                                  |
| PLAN 12 persistence                               | `packages/project-fs` (ADR 0005 replaces IndexedDB)                                            |
| PLAN 13 security                                  | `packages/renderer` (edit frame), `packages/editor/src/preview`, docs/architecture/SECURITY.md |
| PLAN 14 export                                    | `packages/export` + `project-fs` writer                                                        |
| UI_DESIGN_PLAN 9 design system (the editor's own) | `packages/ui/src/tokens.css` and primitives                                                    |
| UI_DESIGN_PLAN screens D-xx                       | `packages/editor/src/**` — each component names its board in a comment                         |
| UI_DESIGN_PLAN Phase I MCP                        | `packages/mcp-server`, `apps/desktop/src/main`, `packages/editor/src/mcp`                      |

## 5. Things that are deliberately not here

A global event bus, a plugin system, a rich-text framework, a drag-and-drop library, a UI kit,
server-side rendering, a backend (PLAN.md 15). Daisy as an MCP client and backend-as-a-service
integration are deferred (UI_DESIGN_PLAN.md Phase I).
