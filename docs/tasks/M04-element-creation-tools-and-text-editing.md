# M04 · Element creation tools and text editing

- **Goal:** All core creation tools and proper rich text editing.
- **Source:** PLAN.md §16 Milestone 4
- **Spec:** PLAN.md 5, 8, 9.7
- **Designs:** D-12, D-13, D-17, D-18, D-41, D-42, D-43
- **Packages:** model, editor
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** Element registry (8.1) with definitions for section, box, divider, text, heading, button, link, list, image placeholder. `canContain` validation. Shared creation pipeline (click versus drag, insertion point, In flow default). Text editing per 9.7 with inline model nodes. Options bar framework. Tool flyouts and tool lock.

## Acceptance criteria

- Every tool creates the exact HTML and starting CSS specified in 5.3 and 8.2 (snapshot tests).
- Dropping a box into a paragraph is refused with the specified message.
- Typing a sentence, bolding one word and linking another produces `<p>… <strong>…</strong> … <a href>…</a></p>` in the model.
- Undo while typing removes a burst, not a single character and not the whole paragraph.
- Pasting formatted text from a word processor yields plain text only.

**Done when:** A user can build a text-and-buttons page with headings, paragraphs with inline formatting, links, dividers and multiple sections, using tools alone.

## Tasks

### M04-T01 Implement `ElementTypeDef` and the registry with the element types listed above and their starting styles.

- **Status:** todo

### M04-T02 Implement `canContain` and invalid-drop feedback (red insertion line and reason).

- **Status:** todo

### M04-T03 Refactor creation into one pipeline used by every creation tool; add insertion-point preview while hovering.

- **Status:** todo

### M04-T04 Implement the Section tool and the "+ Add section" bar.

- **Status:** todo

### M04-T05 Implement Box variants (Ellipse, Divider) and tool flyouts, cycling and tool lock.

- **Status:** todo

### M04-T06 Implement full text editing: caret placement at click, `beforeinput` handling, model sync, paste as plain text, `Enter` new paragraph, `Shift+Enter` line break.

- **Status:** todo

### M04-T07 Implement inline formatting commands (bold, italic, underline via span, link) on a selected range.

- **Status:** todo

### M04-T08 Implement typing-burst history grouping.

- **Status:** todo

### M04-T09 Implement the Heading variant with level selection.

- **Status:** todo

### M04-T10 Implement the Button tool with its starting styles and immediate label editing.

- **Status:** todo

### M04-T11 Implement the Link tool: popover, wrap element, link text range, link to section (creates the id).

- **Status:** todo

### M04-T12 Build the options bar framework and the options for each tool built so far, with the "More" popover.

- **Status:** todo

### M04-T13 Build the Elements panel (categories, search, click-to-arm, drag to canvas, double-click insert) and the Place tool.

- **Status:** todo

### M04-T14 Add tool tooltips and the status bar hints.

- **Status:** todo
