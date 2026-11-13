---
name: daisy-adr
description: Record an architecture decision (and what it supersedes in the plans) as an ADR.
---

# ADR

1. `pnpm new:adr "Decision title"` creates the file from the template.
2. Fill Context, Decision, Consequences, and **Supersedes** (exact PLAN.md / UI_DESIGN_PLAN.md sections).
3. Add a one-line pointer at those sections in the plan.
4. If it changes the package graph, update `docs/architecture/dependencies.json` and ARCHITECTURE.md in the same PR.
