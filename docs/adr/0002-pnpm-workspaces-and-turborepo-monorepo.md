# 0002. pnpm workspaces and Turborepo monorepo

- **Status:** Accepted
- **Date:** 2026-11-13
- **Supersedes in PLAN.md / UI_DESIGN_PLAN.md:** PLAN.md 15 "Deliberately not used: … a monorepo".

## Context

Daisy has clear layers (model, generators, renderer, editor, file system, MCP) and many agents will work in parallel. PLAN.md 15 said "no monorepo".

## Decision

One repository with pnpm workspaces (`apps/*`, `packages/*`) and Turborepo for task running and caching. The allowed dependency graph lives in docs/architecture/dependencies.json and is enforced in CI.

## Consequences

Boundaries are enforced by package manifests, not only by convention, so an agent cannot accidentally make the model depend on React. Slightly more configuration.
