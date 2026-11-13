# @daisy/html

HTML generation for export and preview.

**Owns:** generateHtml per page, element registry output rules, attributes, accessibility attributes.

**Specification:** PLAN.md 14.2, 8 (HTML element system)

**May import:** @daisy/di, @daisy/model, @daisy/css. The full graph is in `docs/architecture/dependencies.json` and is checked by `pnpm check:deps`.

**Rules:** Never emit data-d-\* attributes, daisy-asset:// URLs or editor-only markup.

**Tests:** `pnpm --filter @daisy/html test`. Test files sit next to the code as `*.test.ts`.
