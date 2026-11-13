# @daisy/project-fs

Project folders on disk: open, save, autosave, versions, recovery, watching, writing exports.

**Owns:** Project folder format, atomic writes, autosave writer, versions store, crash recovery journal, file watcher for outside edits, export writer.

**Specification:** docs/adr/0005-projects-are-folders-on-disk.md (replaces PLAN.md 12.2 IndexedDB); PLAN.md 12.3–12.7; UI_DESIGN_PLAN.md D-46, D-32

**May import:** @daisy/di, @daisy/model, @daisy/ipc, @daisy/export. The full graph is in `docs/architecture/dependencies.json` and is checked by `pnpm check:deps`.

**Rules:** Never write outside the project folder or a folder the user picked. Writes are atomic (temp file + rename).

**Tests:** `pnpm --filter @daisy/project-fs test`. Test files sit next to the code as `*.test.ts`.
