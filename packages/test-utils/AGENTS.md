# @daisy/test-utils

Fixtures and builders shared by tests.

**Owns:** Document builders, the Halden sample project (PLAN.md 10 / UI_DESIGN_PLAN.md 10), golden-file helpers.

**Specification:** PLAN.md 17 (testing), UI_DESIGN_PLAN.md 10 (sample content)

**May import:** @daisy/di, @daisy/model. The full graph is in `docs/architecture/dependencies.json` and is checked by `pnpm check:deps`.

**Rules:** Never import from apps. Fixtures are plain data.

**Tests:** `pnpm --filter @daisy/test-utils test`. Test files sit next to the code as `*.test.ts`.
