# Project folder format (ADR 0005)

A Daisy project is a normal folder the user chooses (for example `D:\Sites\halden`). It is
designed to be readable, diff-friendly and safe to keep in Git.

```
halden/
  daisy.json             manifest: schemaVersion, id, name, page order, screen sizes, project settings
  pages/<pageId>.json    one page each: nodes, styles, page settings
  parts/<id>.json        shared parts and components (M19)
  collections/<id>.json  collection items (M19)
  design-system.json     the project's design system tokens (M18; absent if opted out)
  assets/<hash>.<ext>    content-addressed files (PLAN.md 10.4); never duplicated
  .daisy/
    lock                 { pid, host, since } — one editing window per project
    recovery/            journal of unsaved transactions for crash recovery
    versions/            automatic and manual versions (gzip JSON + manifest)
    thumbnail.png        for Home
```

Rules:

- JSON is written with sorted keys and 2-space indentation, so diffs are small and stable.
- Every write is atomic: write `name.tmp`, `fsync`, rename over the old file.
- Autosave follows PLAN.md 12.3 (800 ms debounce, 5 s max wait); only changed files are written.
- Validation on open: Zod schema + invariants (PLAN.md 10.2); migrations run first (12.7).
- Outside changes (a `git pull`, another editor) are detected with a watcher; the user chooses to
  reload or keep theirs (UI_DESIGN_PLAN.md D-46).
- Exported sites go to a folder the user picks (default `<project>/site`), never inside `.daisy/`.
- A `.daisy` file (PLAN.md 12.6) is a zip of the same folder without `.daisy/lock` and `recovery/`.
