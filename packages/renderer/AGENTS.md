# @daisy/renderer

The imperative CanvasRenderer that writes real DOM into the sandboxed edit frame, plus hit testing and measurement.

**Owns:** Edit-frame setup (sandbox, CSP), initial render, patch → DOM/CSSOM updates, id maps, hitTest, measure, snapping maths, insertion finder.

**Specification:** PLAN.md 9 (rendering and canvas architecture), 13.3 (edit frame never executes)

**May import:** @daisy/di, @daisy/model, @daisy/css · dompurify. The full graph is in `docs/architecture/dependencies.json` and is checked by `pnpm check:deps`.

**Rules:** Never use React here. Never let user code execute in the edit frame. Never read the DOM to learn what the document is.

**Tests:** `pnpm --filter @daisy/renderer test` · `pnpm --filter @daisy/renderer test:browser` for real-engine tests. Test files sit next to the code as `*.test.ts`.
