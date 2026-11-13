# 0003. Internal packages are consumed as TypeScript source

- **Status:** Accepted
- **Date:** 2026-11-13
- **Supersedes in PLAN.md / UI_DESIGN_PLAN.md:** —

## Context

Building every package separately slows development and complicates debugging.

## Decision

Packages export `./src/index.ts`. Vite/electron-vite bundle them; `tsc --noEmit` type-checks each package. Only `apps/desktop` has a build. No package is published to npm.

## Consequences

Instant changes across packages, simple source maps. If a package is ever published (for example a CLI), it gets its own build then.
