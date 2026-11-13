# @daisy/css

CSS generation: one generator for canvas and export.

**Owns:** generateCss (base, responsive, states), normalisation, shorthand expansion/collapse, rule order, base stylesheet, class naming.

**Specification:** PLAN.md 11 (CSS generation), 7.3 (responsive), 6.5 (states)

**May import:** @daisy/di, @daisy/model. The full graph is in `docs/architecture/dependencies.json` and is checked by `pnpm check:deps`.

**Rules:** Never produce CSS the plan does not specify for a gesture. Output must be deterministic (golden tests).

**Tests:** `pnpm --filter @daisy/css test` · `pnpm --filter @daisy/css test:browser` for real-engine tests. Test files sit next to the code as `*.test.ts`.
