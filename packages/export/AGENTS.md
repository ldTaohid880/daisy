# @daisy/export

Builds the exported site as an in-memory file map; writing to disk is project-fs's job.

**Owns:** exportSite(project) → Map<path, bytes>; asset rewriting; .daisy archive pack/unpack; export reports.

**Specification:** PLAN.md 14 (export), 12.6 (.daisy files); UI_DESIGN_PLAN.md D-30, D-55

**May import:** @daisy/di, @daisy/model, @daisy/css, @daisy/html · fflate. The full graph is in `docs/architecture/dependencies.json` and is checked by `pnpm check:deps`.

**Rules:** Never touch the file system. Exports must be byte-identical for the same input.

**Tests:** `pnpm --filter @daisy/export test`. Test files sit next to the code as `*.test.ts`.
