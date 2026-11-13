# M16 · Full element library and accessibility

- **Goal:** Complete the HTML element set and build accessibility guidance into the workflow.
- **Source:** PLAN.md §16 Milestone 16
- **Spec:** PLAN.md 8
- **Designs:** D-18, D-42, D-25
- **Packages:** model, html, editor
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** Remaining registry entries (8.2). Compound creators and structure-specific editing (table row/column controls, list `Enter` behaviour, dropdown options editor). The model-based checker (8.4). Contrast calculation with culori.

## Acceptance criteria

- Creating a text field produces a `<label for>` and `<input id>` pair that match; a checkbox is wrapped in its label.
- A table can gain and lose rows and columns from the canvas and always exports valid table markup.
- An image without a description, an empty link and a skipped heading level each produce the specified warning, and none blocks export.
- Outline view lists headings and landmarks in document order.
- Exported fixtures for every element type pass html-validate.

**Done when:** A user can build a complete contact page with a labelled form, a pricing table, lists and proper landmarks, and be told about accessibility problems as they work.

## Tasks

### M16-T01 Add registry entries and starting styles for all form elements; implement the Form tool with automatic labels and ids.

- **Status:** todo

### M16-T02 Implement field settings in General (kind, placeholder, required, name) and advanced attributes.

- **Status:** todo

### M16-T03 Implement the dropdown options editor and radio grouping.

- **Status:** todo

### M16-T04 Implement lists: creation, `Enter`/`Backspace` item behaviour, auto-wrapping of dropped elements in `li`.

- **Status:** todo

### M16-T05 Implement tables: creation, canvas row/column controls, header cells, shared cell selectors.

- **Status:** todo

### M16-T06 Add remaining elements: figure, blockquote, pre/code, details, dialog, description list, picture.

- **Status:** todo

### M16-T07 Complete the Kind dropdown and landmark choices for containers.

- **Status:** todo

### M16-T08 Implement the accessibility checker rules and severity.

- **Status:** todo

### M16-T09 Implement the Accessibility group (contextual simple questions; advanced ARIA).

- **Status:** todo

### M16-T10 Add issue badges in Layers and the summary in the Export dialog.

- **Status:** todo

### M16-T11 Implement Outline view in Layers.

- **Status:** todo

### M16-T12 Add "Allow invalid nesting" override with warning badge.

- **Status:** todo
