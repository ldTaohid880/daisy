# M15 · Custom code and attributes

- **Goal:** Safe support for custom HTML, CSS and JavaScript.
- **Source:** PLAN.md §16 Milestone 15
- **Spec:** PLAN.md 13
- **Designs:** D-27, D-27b
- **Packages:** model, editor, renderer
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** `CustomCode` in the model; script files in export; DOMPurify for canvas rendering of HTML blocks; CSP assembly from the document's external hosts; import trust prompts; heartbeat; "Disable scripts" and "Disable custom CSS on canvas" switches.

## Acceptance criteria

- An HTML block containing a script shows its markup on the canvas, runs nothing while editing, runs in Preview, and exports verbatim.
- A script calling `indexedDB.open`, `parent.document` or `top.location` from Preview fails and the editor is unaffected.
- Custom page CSS that sets `* { display: none }` leaves the editor fully usable.
- An exported page with a custom script runs it exactly as written.
- A user who never opens the Code drawer or the collapsed groups sees no code anywhere.

**Done when:** A developer can add tracking snippets, third-party embeds, web components and their own scripts and styles, test them in Preview, and export them unchanged, without any risk to their saved work.

## Tasks

### M15-T01 Implement the Attributes group with validation, boolean attributes, `data-*` helper, "runs script" tagging and "Copy selector".

- **Status:** todo

### M15-T02 Implement the HTML block element: code popover, sanitised canvas rendering, verbatim export.

- **Status:** todo

### M15-T03 Implement custom elements through the Place tool's tag field.

- **Status:** todo

### M15-T04 Build the Page CSS editor; append to generated CSS; "Disable custom CSS on canvas".

- **Status:** todo

### M15-T05 Complete "Also styled by Page CSS" notes in Properties.

- **Status:** todo

### M15-T06 Build the Page JavaScript editor: multiple scripts, placement, defer/async/module, external URLs, enable toggles, head HTML.

- **Status:** todo

### M15-T07 Export scripts as files and tags; inline them in Preview.

- **Status:** todo

### M15-T08 Build the CSP from document settings; implement "Allow network requests in preview".

- **Status:** todo

### M15-T09 Implement the preview heartbeat, "not responding" notice and safe-start after a crash.

- **Status:** todo

### M15-T10 Implement the remote content setting for the edit frame.

- **Status:** todo

### M15-T11 Write the security test suite (17.2, custom code isolation).

- **Status:** todo

### M15-T12 Warn when a renamed class still appears in custom code.

- **Status:** todo
