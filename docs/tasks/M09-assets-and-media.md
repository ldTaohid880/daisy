# M09 · Assets and media

- **Goal:** Real images, video and fonts in documents.
- **Source:** PLAN.md §16 Milestone 9
- **Spec:** PLAN.md 10.4, 13.5
- **Designs:** D-17, D-26
- **Packages:** model, project-fs, editor
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** `assets` store keyed by content hash; `AssetMeta`; `daisy-asset://` references resolved to object URLs in the edit frame with lifecycle management. Type detection by signature. SVG sanitising. `@font-face` generation. Usage scan.

## Acceptance criteria

- Dropping a JPEG on a section creates an `<img>` that fits within the section and stores exactly one asset; dropping the same file again reuses it.
- An SVG containing a `<script>` is stored and displayed with the script removed.
- A file named `.png` that is not an image is rejected.
- Deleting an in-use asset is blocked unless confirmed; reloading the document shows all media correctly.

**Done when:** A user can build a page with photographs, a logo, a background image, a video and their own brand font.

## Tasks

### M09-T01 Implement asset import: hashing, signature-based type check, metadata extraction (dimensions, duration), size limits with clear messages.

- **Status:** todo

### M09-T02 Implement the asset URL resolver and object URL lifecycle in the renderer.

- **Status:** todo

### M09-T03 Implement the Media tool: Image by click, drag and file drop; placeholder state; Fit options; alt text prompt.

- **Status:** todo

### M09-T04 Implement Video, Audio and Icon variants; sanitise SVG on import.

- **Status:** todo

### M09-T05 Implement the Embed variant with the editor placeholder.

- **Status:** todo

### M09-T06 Build the Assets panel: tabs, upload, thumbnails, usage counts, select users, replace, rename, guarded delete.

- **Status:** todo

### M09-T07 Support dragging assets to the canvas and onto elements (image source or fill).

- **Status:** todo

### M09-T08 Add image layers from assets in Fill.

- **Status:** todo

### M09-T09 Implement uploaded fonts: `FontSource`, weight/style detection, `@font-face` in the generator, availability in the font picker.

- **Status:** todo

### M09-T10 Include asset blobs when duplicating a document.

- **Status:** todo

### M09-T11 Write intrinsic `width` and `height` attributes on images.

- **Status:** todo
