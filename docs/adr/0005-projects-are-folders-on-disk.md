# 0005. Projects are folders on disk

- **Status:** Accepted
- **Date:** 2026-11-13
- **Supersedes in PLAN.md / UI_DESIGN_PLAN.md:** PLAN.md 12.2 storage layout, 12.4 (lock mechanism), 19.1 D16 and D20, 19.2 R8, R9; Milestone 3 tasks.

## Context

Designs (UI_DESIGN_PLAN.md D-02b, D-46, D-32) save to real folders, have several pages, and users want to keep sites in Git. PLAN.md 12.2 used IndexedDB with one page per document (D20).

## Decision

A project is a folder (docs/architecture/PROJECT_FORMAT.md): manifest, one JSON per page, content-addressed assets, and a `.daisy/` folder for lock, recovery and versions. project-fs writes atomically from the main process. The `.daisy` single-file format stays for sharing.

## Consequences

Git-friendly, inspectable, no browser-eviction risk (PLAN R8/R9 retired). Requires a file lock instead of Web Locks, a watcher for outside edits, and path checks. Autosave timings and recovery behaviour from PLAN.md 12.3–12.4 are kept.
