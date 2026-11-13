# @daisy/model

The Daisy document: types, Zod schema, commands with inverses, invariants, migrations, selectors.

**Owns:** DaisyDocument / Project types; commands (insertNode, removeNode, setStyles, moveNode…); transaction and patch helpers; invariant checker; schema migrations; selectors (effective styles, origins).

**Specification:** PLAN.md 10 (data architecture), 12.7 (schema versioning), 7 (layout model); UI_DESIGN_PLAN.md 6.4 (vocabulary)

**May import:** @daisy/di · zod, immer, nanoid. The full graph is in `docs/architecture/dependencies.json` and is checked by `pnpm check:deps`.

**Rules:** Never import React, the DOM, Node or Electron. Never store derived data. Every command needs a tested inverse.

**Tests:** `pnpm --filter @daisy/model test`. Test files sit next to the code as `*.test.ts`.
