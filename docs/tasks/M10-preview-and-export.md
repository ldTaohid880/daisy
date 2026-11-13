# M10 · Preview and export

- **Goal:** Turn the document into a real website and verify it interactively.
- **Source:** PLAN.md §16 Milestone 10
- **Spec:** PLAN.md 14; ADR 0010
- **Designs:** D-29, D-30, D-55
- **Packages:** html, export, project-fs, editor, desktop
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** `generateHtml` (14.2). Export CSS with shorthand collapsing and property ordering (11.4). Asset naming and copying. Zip via fflate; File System Access where available. Preview frame with `sandbox="allow-scripts allow-forms allow-popups"`, self-contained `srcdoc`, CSP and bridge (13.4). The canvas-versus-export geometry test harness.

## Acceptance criteria

- The exported folder of every fixture document opens from disk and from a static server and looks the same as the canvas (geometry difference ≤ 0.5 px per element).
- Exported HTML passes validation; exported files contain no `data-d-` attributes and no reference to Daisy.
- Links, buttons and form typing work in Preview and not on the editing canvas.
- The preview frame cannot read the editor's IndexedDB or DOM (automated test from inside the frame).

**Done when:** A user can design a page, preview it as a visitor would, export it, upload the folder to any web host, and have a working site.

## Tasks

### M10-T01 Implement `generateHtml` with head metadata, escaping, attribute ordering and formatting rules.

- **Status:** todo

### M10-T02 Implement export-target CSS: shorthand collapsing, property order, optional minify and rule merging.

- **Status:** todo

### M10-T03 Implement asset file naming, de-duplication and reference rewriting in HTML and CSS.

- **Status:** todo

### M10-T04 Implement `exportSite` producing an in-memory file map; write it to a chosen folder through project-fs; optional zip.

- **Status:** todo

### M10-T05 Build the Export dialog: file tree, file viewer, options, external dependency list.

- **Status:** todo

### M10-T06 Build the Page settings dialog (title, description, language, favicon, social image).

- **Status:** todo

### M10-T07 Implement Preview in an isolated session through the `daisy-preview://` protocol (ADR 0010) and the preview frame.

- **Status:** todo

### M10-T08 Implement the bridge and validated message handling; preview console for errors.

- **Status:** todo

### M10-T09 Implement preview width control, size selector and `Esc` to return.

- **Status:** todo

### M10-T10 Build the fidelity harness: render fixtures in the edit frame and as exported files, compare bounding boxes of every element.

- **Status:** todo

### M10-T11 Add html-validate checks on exported fixtures.

- **Status:** todo
