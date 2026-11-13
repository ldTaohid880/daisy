# M03 · Projects on disk, saving and Home

- **Goal:** Work is never lost: projects are folders on disk with autosave, recovery and a Home screen.
- **Source:** new (not in PLAN.md)
- **Spec:** PLAN.md 12.3–12.7; ADR 0005
- **Designs:** D-01, D-02, D-02b, D-46, D-52
- **Packages:** project-fs, ipc, editor, desktop
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

## Acceptance criteria

- Edit, close the window within two seconds, reopen: the edit is there.
- Kill the app during editing: on restart the project reopens with the "restored" notice and at most the final gesture missing.
- A corrupted page file does not crash the app; the page is reported as damaged and the rest still opens (D-46).
- Opening the same project in a second window opens it read-only (D-46).
- Changing a page file outside Daisy shows the outside-change notice with Reload / Keep mine (D-46).

**Done when:** A user can create several projects in folders, leave, come back days later, and continue each exactly where it was.

## Tasks

### M03-T01 Project folder format and schemas

- **Status:** todo
- **Needs:** M01
- **Done when:** docs/architecture/PROJECT_FORMAT.md implemented as Zod schemas in model (manifest, page) with stable serialisation (sorted keys).

### M03-T02 project-fs: open, validate, migrate

- **Status:** todo
- **Needs:** M03-T01
- **Done when:** Open a folder: read manifest and pages, run migrations, validate schema + invariants; damaged pages are isolated, not fatal.

### M03-T03 project-fs: atomic writes and the lock

- **Status:** todo
- **Needs:** M03-T02
- **Done when:** Temp file + fsync + rename; `.daisy/lock` with pid/host/since, stale-lock detection; second window read-only.

### M03-T04 IPC channels for projects

- **Status:** todo
- **Needs:** M03-T02
- **Done when:** project.create, project.open, project.save (changed pages only), project.close, project.recent; validated both ways.

### M03-T05 Autosave scheduler and save status

- **Status:** todo
- **Needs:** M03-T04
- **Done when:** PLAN.md 12.3 timings; save on window blur and before quit; top-bar status (Saving… / ✓ Saved / Not saved) per D-04 and D-46.

### M03-T06 Crash recovery journal

- **Status:** todo
- **Needs:** M03-T05
- **Done when:** Transactions appended to `.daisy/recovery/`; clean-close flag; restored notice (PLAN.md 12.4).

### M03-T07 Outside-change watcher

- **Status:** todo
- **Needs:** M03-T03
- **Done when:** Watch the project folder; ignore own writes; D-46 notice with Reload / Keep mine.

### M03-T08 Home screen and recent projects

- **Status:** todo
- **Needs:** M03-T04
- **Done when:** D-01 (empty) and D-02 (projects): recent list with thumbnails, open folder, remove from list, Help links (D-52).

### M03-T09 New project steps

- **Status:** todo
- **Needs:** M03-T08
- **Done when:** D-02b: name and folder, starting point (blank or Halden sample), screen sizes; the design-system step offers "Set up later" until M18.

### M03-T10 Thumbnails

- **Status:** todo
- **Needs:** M03-T05
- **Done when:** Rendered from the edit frame at most once a minute while idle; written to `.daisy/thumbnail.png`.

### M03-T11 Per-project editor state and preferences store

- **Status:** todo
- **Needs:** M03-T04
- **Done when:** Viewport and selection per page in app data; preferences in app data (not localStorage).

### M03-T12 Write-failure path

- **Status:** todo
- **Needs:** M03-T05
- **Done when:** Disk full / permission denied → red "Not saved" with "Save a copy elsewhere…"; editing continues in memory (D-46).
