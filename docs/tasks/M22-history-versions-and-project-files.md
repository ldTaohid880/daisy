# M22 · History, versions and project files

- **Goal:** Complete safety net and portability for documents.
- **Source:** PLAN.md §16 Milestone 17
- **Spec:** PLAN.md 12.5–12.6; ADR 0005
- **Designs:** D-32, D-32b
- **Packages:** project-fs, export, editor
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** History panel over the existing stack; entry coalescing and limits. `versions` store with retention. Zip-based `.daisy` format with validation (12.6). Corruption handling path. Storage is the project folder (ADR 0005): versions in `.daisy/versions/`, `.daisy` files are zips of the folder. "Recently deleted" applies to projects in Home.

## Acceptance criteria

- Clicking any History entry puts the document in exactly that state; continuing to edit from there discards later entries.
- Saving a `.daisy` file, deleting the document, and opening the file restores it identically, including assets.
- A truncated or tampered `.daisy` file is rejected with a message and does not create a broken document.
- Restoring a version first preserves the current state as another version.

**Done when:** A user can review and rewind their session, keep milestones of their design, back up documents as files and open them on another computer.

## Tasks

### M22-T01 Build the History panel with jump-to-entry.

- **Status:** todo

### M22-T02 Implement entry coalescing and the 300-entry / 50 MB limit.

- **Status:** todo

### M22-T03 Restore screen size, state, selection and scroll position on undo and redo.

- **Status:** todo

### M22-T04 Implement automatic versions (interval and pre-risk) with retention of 20.

- **Status:** todo

### M22-T05 Implement manual versions on `Ctrl+S` with labels.

- **Status:** todo

### M22-T06 Build the Versions dialog: list, thumbnail, restore, open as copy.

- **Status:** todo

### M22-T07 Implement `.daisy` export (a zip of the project folder, ADR 0005) with assets and thumbnail; save through the native dialog with re-save.

- **Status:** todo

### M22-T08 Implement `.daisy` import with full validation and the untrusted-file rules (remote content off, script prompt).

- **Status:** todo

### M22-T09 Implement the damaged-document path: offer last valid version and raw download.

- **Status:** todo

### M22-T10 Implement "Recently deleted" for projects in Home and the unused-asset clean-up action.

- **Status:** todo

### M22-T11 Add a migration fixture test for every schema version so far.

- **Status:** todo
