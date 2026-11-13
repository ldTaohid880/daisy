# Daisy

Daisy is a desktop app for visually designing real websites. You work on a real page made of
HTML and CSS — drag, resize, style — and Daisy writes clean, hand-quality code you own.

> Status: **pre-alpha**. The product is fully specified and designed; implementation starts at
> milestone M00 (docs/tasks/ROADMAP.md).

## Where things are

| You want                                | Read                                                                               |
| --------------------------------------- | ---------------------------------------------------------------------------------- |
| What Daisy is and how it behaves        | [`PLAN.md`](PLAN.md) — product, UX, architecture and development plan              |
| What every screen looks like            | [`UI_DESIGN_PLAN.md`](UI_DESIGN_PLAN.md) and the design canvas "Daisy — UI Design" |
| How the code is organised               | [`docs/architecture/ARCHITECTURE.md`](docs/architecture/ARCHITECTURE.md)           |
| Why a decision was made                 | [`docs/adr/`](docs/adr/)                                                           |
| What to build next                      | [`docs/tasks/ROADMAP.md`](docs/tasks/ROADMAP.md) and `pnpm check:tasks --next`     |
| How to work here (people and AI agents) | [`AGENTS.md`](AGENTS.md), [`CONTRIBUTING.md`](CONTRIBUTING.md)                     |

## Quick start

Requirements: Node.js 24 LTS, pnpm 10 (`corepack enable`), Git.

```sh
pnpm install
pnpm dev          # start the desktop app with hot reload
pnpm check        # format, lint, package boundaries, types, unit tests — run before every PR
pnpm test:e2e     # Electron end-to-end tests (after `pnpm build`)
pnpm package      # installers for this OS in apps/desktop/release/
```

## Repository layout

```
apps/desktop          Electron app: main process, preload, renderer entry, packaging, e2e
packages/di           Dependency injection: typed tokens and the container (ADR 0011)
packages/model        Document model: types, schema, commands, invariants, migrations
packages/css          The one CSS generator (canvas and export)
packages/html         HTML generation
packages/export       Builds the exported site as a file map; .daisy archives
packages/ipc          Typed main ↔ renderer contracts
packages/renderer     CanvasRenderer, hit testing, measurement (no React)
packages/ui           Editor UI kit: tokens and primitives
packages/editor       The editor app: shell, panels, tools, stores
packages/project-fs   Project folders on disk: save, autosave, versions, recovery
packages/mcp-server   Daisy's MCP server for AI apps
packages/native       C++ core as a Node-API addon (required, ADR 0015)
packages/test-utils   Fixtures (the Halden sample project) and builders
docs/                 Architecture, ADRs, engineering guides, roadmap and tasks
py/                   Python repository tooling (ADR 0014)
scripts/              Repository scripts — TypeScript classes run by Node
design-src/           Scripts that generated the design boards (reference only)
.claude/              Agent skills, subagents, commands, hooks
.github/              CI, release, security scanning, templates
```

## Licence

[MIT](LICENSE)
