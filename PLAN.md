# Daisy — Product, UX, Architecture and Development Plan

Daisy is a desktop-browser application for designing real web pages visually. This document is the single plan for building it. It is written so that a developer, or an AI coding agent, can implement Daisy one task at a time.

Conventions used in this document:

- "Decision" marks a choice that is final for this plan. Alternatives are only mentioned to explain why they were rejected.
- Keyboard shortcuts are written for Windows. On macOS, `Ctrl` becomes `Cmd` and `Alt` becomes `Option`.
- "Canvas" means the editing workspace. "Page" means the web page being designed. "Document" means the saved Daisy project.

---

## 1. Product Definition

### 1.1 What Daisy is

Daisy is a visual design environment whose material is HTML and CSS. The user draws, places, moves, resizes and styles elements with tools, the way they would in a creative application, and every one of those actions edits a real web page that is being rendered by the browser's own engine.

The product idea in one line: **the creative freedom of an image editor, applied to HTML and CSS.**

Daisy is not a website builder. It has no templates, no themes, no pre-made blocks and no hosting. It is the tool you use to make the page itself.

### 1.2 Who it is for

| User | What they need | How Daisy serves them |
|---|---|---|
| Beginner | Make a good-looking page without learning HTML or CSS | Tools with obvious default behaviour, plain-language labels, direct manipulation on the canvas, sensible defaults on every new element |
| Designer / developer | Full control of structure, layout, styling, responsive behaviour and custom code | Every property group and tool has its own advanced disclosure; any CSS value can be typed; real tags, classes and attributes are editable; custom CSS, HTML and JavaScript are supported |

Both use the same interface. There is no mode switch.

### 1.3 What Daisy produces

A folder of plain files: `index.html`, a stylesheet, optional scripts, and assets. The folder works on any static web server and has no dependency on Daisy.

### 1.4 What Daisy is not (for this plan)

- Not a hosting service, CMS or e-commerce platform.
- Not a collaborative tool. There are no accounts and no cloud.
- Not a template marketplace.
- Not a code editor with a preview. Code is available, but it is never required.

### 1.5 Design reasoning: nine questions answered

These answers drive every later chapter.

**1. What does it mean to design a webpage visually?**
It means changing a live web page by acting on what you see instead of on its source. Three things must hold: (a) what you see is the browser's real rendering, (b) every gesture maps to a specific, nameable change in HTML or CSS, and (c) the same gesture always produces the same change.

**2. What are the fundamental operations?**
Create an element. Select it. Put content in it. Place it (order it among siblings, nest it, or position it freely). Size it. Space it (padding, margin, gap). Arrange its children (stack, row, grid). Style it (type, fill, border, effects). Vary it (by screen size, by state, over time). Inspect and export it.

**3. Which operations deserve dedicated tools?**
An operation gets a tool when it is performed *on the canvas with the pointer* and needs its own pointer behaviour. Creating elements, selecting, editing spacing by dragging edges, editing layout tracks and gaps, transforming, drawing gradients, sampling colours, measuring, panning and zooming all qualify. Decision: 18 tools, listed in chapter 5.

**4. Which operations belong in property panels?**
Anything that is a *value* rather than a gesture: font family, line height, border style, shadow parameters, overflow, attributes, accessibility text. Also every value a tool edits, so that tools and panel are two views of the same data.

**5. How does advanced CSS stay accessible without overwhelming beginners?**
Three layers, always in the same place: (1) the simple controls of a group, (2) an "Advanced" disclosure inside that same group, (3) a raw value: every field accepts any valid CSS value, and every group ends with "Other properties" where any CSS property can be added. Nothing is hidden behind a mode; it is one click away, next to the thing it affects.

**6. How should the editor represent real HTML structure?**
Directly. The Layers panel is the DOM tree. Every layer is one HTML element. A "group" is a real `<div>`. A "section" is a real `<section>`. Friendly names sit on top of real tags, and the tag is always visible in the General group.

**7. How do users build complex layouts without templates?**
From one primitive: a box that can contain other boxes, plus one control on every box, "Arrange children" (Stack, Row, Grid). The Layout tool makes rows, columns, gaps and grid tracks draggable on the canvas. Any layout on the web is a composition of these.

**8. How does the editor communicate responsive behaviour?**
The canvas is always showing one named screen size. A persistent chip says which. Every property shows whether its value is set at this size, inherited from a larger size, or overridden at a smaller one. Changing a value writes only to the current size.

**9. How is the relationship between editing and exported code kept predictable?**
Styles are stored as real CSS declarations (property and value strings). The canvas and the export are generated by the *same* CSS generator from the same data. There is no translation layer that could drift.

---

## 2. Product Principles

These are constraints. A feature that breaks one is wrong.

| # | Principle | What it means in practice |
|---|---|---|
| P1 | Progressive complexity at every level | Every tool and property group works with its defaults, and carries its own Advanced disclosure. No global Simple/Advanced switch. |
| P2 | Clean start | A new document is one empty `<section>`. No templates, presets or pre-built blocks anywhere in the product. |
| P3 | Real web output | The document is HTML elements and CSS declarations. Export is plain files with no Daisy runtime. |
| P4 | Tools first | The canvas is edited by tools, handles and guides. The Properties panel is for values, not the main way to work. |
| P5 | One source of truth | The document model is the truth. The canvas DOM and the export are both derived from it. |
| P6 | What you see is what you export | Daisy adds no editor-only layout CSS. If something has a size on the canvas, that size is in the stylesheet. The few unavoidable exceptions are listed in 9.9. |
| P7 | Never restrict, never force | Any valid CSS value can be entered anywhere. No user is ever required to type code. |
| P8 | Explicit over silent | Daisy never changes a value the user did not act on without saying so (for example, setting `position: relative` on a parent is reported and is part of the same undo step). |
| P9 | Plain language first, real names nearby | Labels are plain words ("Space inside"). The CSS name (`padding`) is shown in the tooltip and in the Advanced area. |
| P10 | Local first | Everything runs and saves in the browser. No server. |

### 2.1 The disclosure pattern (used everywhere)

Every property group and every tool's options follow the same four-level structure. Implement it once as a shared component.

```
▾ Spacing                                   ← group header (click to collapse)
   [ simple controls: always visible ]
   ▸ Advanced                               ← per-group disclosure, remembers its state
        [ advanced controls ]
        ▸ Other properties                  ← add any CSS property that belongs to this group
```

Rules:

- The Advanced disclosure state is remembered per group, per user (not per element). A professional opens "Advanced" in Spacing once and it stays open.
- If an element has a value that only an advanced control can show (for example a negative margin), the Advanced header shows a small dot so nothing set is ever invisible.
- If a simple control cannot represent the current value (for example `width: clamp(200px, 50%, 600px)`), it shows the raw value as text with a "custom" tag instead of pretending. It stays editable as text.
- Every field tooltip shows: plain description, CSS property name, current CSS value.

---

## 3. User Experience and Core Workflows

### 3.1 Opening Daisy

Daisy opens to the **Home** screen: a plain list of the user's documents (thumbnail, name, last modified) and one primary button, **New document**. If there are no documents, the screen shows only that button and one sentence: "A document starts as one empty section. You build everything else."

If Daisy was closed unexpectedly, the most recent document opens directly with a notice (see 12.4).

### 3.2 Document creation

1. Click **New document** (`Alt+N`).
2. A small dialog asks for a name (default "Untitled") and nothing else. Press Enter.
3. The editor opens.

What the user sees:

- A neutral dark-grey workspace.
- A white page, 1440 px wide, centred, with a thin drop edge so the page boundary is clear.
- Inside the page, one empty section 400 px tall. Because it is empty it shows a dashed inner outline and a centred hint: "Empty section — pick a tool and click here."
- Below the section, in the workspace (not on the page), a thin **+ Add section** bar.
- The Select tool is active. The section is selected, so its properties are visible.

Decision: the first section is a real `<section>` with exactly one declaration: `min-height: 400px`. That value is visible and editable in the Size group. It is the only style a new document contains.

**Document dimensions.** A web page has no fixed size. Daisy therefore has these page settings, not "canvas size":

| Setting | Default | Meaning |
|---|---|---|
| Canvas width per screen size | Desktop 1440, Tablet 768, Mobile 390 | The width of the simulated browser window when editing that size |
| Simulated window height | 900 | Used for `vh` units and to draw the "fold" line |
| Page background | `#ffffff` | `background-color` on `<body>` |
| Base text | system sans-serif, 16px, `#111111` | `font-family`, `font-size`, `color` on `<body>` |
| Language | `en` | `<html lang>` |
| Title, description, favicon, social image | empty | `<head>` metadata |

Page height always follows content.

**Adding sections.** Three ways: the **+ Add section** bar at the bottom of the page; the Section tool (`S`), which shows an insertion line between sections where a click inserts one; and Layers panel → right-click a section → "Add section below".

**Managing documents.**

| Action | How |
|---|---|
| Rename | Click the document name in the top bar and type; or rename on Home |
| Save | Automatic (see 12.3). `Ctrl+S` forces a save and creates a version |
| Duplicate | File → Duplicate, or Home → document menu → Duplicate |
| Delete | Home → document menu → Delete (asks for confirmation; goes to a "Recently deleted" list for 30 days) |
| Save to disk | File → Save a copy… writes a `.daisy` file |
| Open from disk | File → Open… or drop a `.daisy` file on Home |

### 3.3 Building a page: a worked example

This sequence shows the editing loop. Every step names the real change.

| # | User action | What Daisy does | Model change |
|---|---|---|---|
| 1 | Press `T` | Text tool active. Options bar shows Kind (Text / Heading), font, size, weight, colour, alignment | none |
| 2 | Move over the section | Section gets a blue outline. A horizontal insertion line shows where the text will go | none |
| 3 | Click | A paragraph is created at the insertion point, in flow, and enters text editing with a blinking caret | new `<p>` child of the section |
| 4 | Type "Hello" and press `Esc` | Text is committed. Tool returns to Select with the paragraph selected | text node value |
| 5 | Drag the right-middle handle | Width follows the pointer; a size label shows `320 × 24` | `width: 320px` |
| 6 | In the options bar, set size 48 and weight Bold | Text re-renders live | `font-size: 48px; font-weight: 700` |
| 7 | Press `P` (Spacing tool), drag the top edge of the section inward | A green band grows showing padding; label shows `64` | section `padding-top: 64px` |
| 8 | Press `V`, select the section, click "Center" in the alignment widget | Children centre horizontally | section `display: flex; flex-direction: column; align-items: center` (explained in 7.2) |
| 9 | Press `R`, drag out a rectangle below the text | A box 240 × 160 with a grey fill appears, in flow, after the paragraph | new `<div>`, `width`, `height`, `background-color` |
| 10 | Drag the box above the paragraph | Blue insertion line appears above the paragraph; drop reorders | section `children` order |

### 3.4 Element operations

**Selecting**

| Operation | Interaction |
|---|---|
| Select | Click with Select tool. Selects the element under the pointer *within the current scope* (see below) |
| Go deeper | Double-click a selected container to enter it; then clicks select its children. Double-click on text enters text editing |
| Select deepest directly | `Ctrl+click`, or use the Direct Select tool (`A`) |
| Select parent | `Esc`, or `Shift+Enter`, or click a name in the breadcrumb |
| Select first child | `Enter` |
| Next / previous sibling | `Tab` / `Shift+Tab` |
| Add / remove from selection | `Shift+click` |
| Marquee select | Drag from empty space of a container: selects children of that container the marquee touches |
| Select all siblings | `Ctrl+A` |
| Deselect | Click the workspace outside the page, or `Esc` at the top level |
| Select what is underneath | Right-click → "Select layer" lists every element under the pointer |

*Scope* rule (Decision): the scope starts at the page. A click selects the outermost element under the pointer that is a child of the current scope. Double-clicking moves the scope into that element. Selecting anything outside the scope resets the scope to the nearest common ancestor. This lets beginners select big things first and drill in, while `Ctrl+click` gives professionals instant deep selection.

**Moving**

Elements are either *in flow* (the default) or *free* (absolutely positioned). The two move differently, and Daisy makes the difference visible instead of hiding it.

| Element is | Drag does | Arrow keys do |
|---|---|---|
| In flow | Reorders or re-parents. A blue insertion line shows the drop position; the target container gets a blue outline. The element follows the pointer as a translucent ghost | Nothing. The status bar hints: "In flow: drag to reorder, or switch to Free to place anywhere". `Ctrl+[` and `Ctrl+]` move it earlier or later |
| Free | Moves it. Writes `left` / `top` (or whichever sides are pinned). Snaps to guides | Nudge 1 px; `Shift` 10 px |

The Select tool's options bar always shows a two-way switch for the selection: **In flow | Free**. Switching to Free keeps the element visually where it is (Daisy measures it and writes matching offsets). See 7.4.

**Other operations**

| Operation | Interaction | Result in the model |
|---|---|---|
| Resize | Drag any of 8 handles. `Shift` keeps proportions. `Alt` resizes from the centre (free elements) | `width`, `height` |
| Reorder | Drag in canvas (flow) or drag in Layers. `Ctrl+]` later, `Ctrl+[` earlier, add `Shift` for last / first | parent `children` order |
| Nest | Drag onto a container. Hovering a container for 400 ms "opens" it as the drop target; the insertion line shows the position inside | `parent` and `children` |
| Un-nest | Drag out to another container, or Layers drag | same |
| Duplicate | `Ctrl+D` (inserts after the original), or `Alt+drag` | cloned subtree with new ids and class names |
| Copy / cut / paste | `Ctrl+C` / `X` / `V`. Paste goes after the selection, or inside it if it is an empty container. `Ctrl+Shift+V` pastes inside | cloned subtree |
| Copy / paste style | `Ctrl+Alt+C` / `Ctrl+Alt+V` | style declarations only |
| Delete | `Delete` or `Backspace` | subtree removed. The last section cannot be deleted; it is emptied instead |
| Group | `Ctrl+G` wraps the selected siblings in a new `<div>` named "Group" | new real element |
| Ungroup | `Ctrl+Shift+G` replaces a container with its children. If the container has styles, Daisy warns that they will be lost | element removed |
| Lock | `Ctrl+Shift+L`, or lock icon in Layers. Locked elements cannot be selected on the canvas (only in Layers) | editor flag `locked` |
| Hide | `Ctrl+Shift+H`, or eye icon in Layers | `display: none` at the current screen size. This is real output |
| Move between sections | Drag across the section boundary; the destination section outlines | re-parent |
| Align (multi-selection or within parent) | Options bar buttons: left, centre, right, top, middle, bottom | see 7.2: for flow children this sets the *parent's* alignment or the child's `align-self`; for free elements it sets offsets |
| Distribute | Options bar: horizontal / vertical spacing | free elements: offsets. Flow children: Daisy offers "Space evenly", which sets the parent's `justify-content` |
| Undo / redo | `Ctrl+Z` / `Ctrl+Shift+Z` (also `Ctrl+Y`) | see 12.1 |

Grouping note: because a group is a real `<div>`, grouping can change layout in a row or grid parent (several items become one). Daisy shows a one-line notice the first time: "Group creates a container. In a row, the group becomes one item."

### 3.5 Snapping and guides

| Guide | When it appears | Looks like |
|---|---|---|
| Insertion line | Dragging a flow element or creating with a tool | 2 px blue line, horizontal in stacks and columns, vertical in rows |
| Drop target outline | Same | 1 px blue outline on the container that will receive the element |
| Alignment guides | Moving or resizing a free element; resizing any element | 1 px magenta lines when an edge or centre matches a sibling's or the parent's edge or centre |
| Equal-spacing guides | Moving a free element between two others | magenta bars with the distance |
| Size match | Resizing to the same width or height as a sibling | magenta tick marks on both elements |
| Distance readout | Hold `Alt` with something selected and hover another element | red lines with pixel distances between the two |
| Fold line | Always | faint dashed line at the simulated window height, labelled "Fold · 900" |
| Rulers and manual guides | Advanced scope: View → Rulers (`Ctrl+R`); drag from a ruler to make a guide | cyan lines. Editor-only, saved with the document |

Snap distance is 6 screen pixels. Hold `Ctrl` while dragging to disable snapping.

### 3.6 Canvas behaviour

| Aspect | Specification |
|---|---|
| Workspace background | Flat neutral grey `#2a2a2a` (dark theme) or `#e4e4e4` (light theme). No pattern |
| Page boundary | The page is a rectangle with a 1 px border in a slightly lighter tone. A label above the top-left corner shows `Desktop · 1440` |
| Section boundaries | Invisible by default. On hover with a tool that cares, a 1 px dashed line. In Layers they are the top level |
| Hover | 1 px blue outline on the element that a click would select, plus a small name tag (`Text · p`) |
| Selection | 1.5 px blue outline, 8 square handles (white fill, blue stroke), a name tag at top-left, a size label at bottom-centre while resizing |
| Parent of selection | 1 px dashed blue outline, so nesting is always visible |
| Multi-selection | Each element gets a thin outline; one bounding box with handles surrounds all |
| Locked element | Hovering shows a small lock glyph and no outline |
| Hidden element | Not rendered. Selecting it in Layers shows a notice in Properties: "Hidden at this screen size · Show" |
| Empty container | Dashed inner outline (drawn by the overlay, not CSS). If its real size is under 8 px in either direction, a small marker flag is drawn so it stays selectable |
| Text editing | Element outline turns solid thin blue with no handles; caret and selection are the browser's own |
| Dragging | Ghost at 60% opacity follows pointer; original stays in place dimmed until drop; insertion line and target outline update live |
| Resizing | Live. Size label near the handle. Layout around the element reflows live because it is the real page |
| Zoom | `Ctrl+wheel` or pinch zooms about the pointer. `Ctrl+=` / `Ctrl+-` step. `Shift+1` fit page width, `Shift+0` 100%, `Shift+2` zoom to selection. Range 5%–6400% |
| Pan | Wheel scrolls vertically, `Shift+wheel` horizontally, `Space+drag` or middle-drag pans, Hand tool |
| Context menu | Right-click. Contents below |
| Nesting indication | Breadcrumb in the status bar (`Page › Section 1 › Box › Text`), dashed parent outline, and Layers highlight |

**Context menu (element):** Cut, Copy, Paste, Paste inside, Duplicate · Copy style, Paste style · Group, Ungroup, Wrap in link · Move earlier, Move later · Placement ▸ (In flow, Free, Fixed to screen, Sticky) · Lock, Hide · Select layer ▸ · Rename · Show code · Delete.

**Context menu (empty workspace):** Paste, Select all, Zoom to fit, Show rulers, Page settings.

### 3.7 Beginner-friendly language

Decision: Daisy uses plain labels with the CSS name one hover away. This table is the vocabulary. Use it consistently in every panel, tooltip and menu.

| Concept | Label in Daisy | Shown in tooltip / Advanced |
|---|---|---|
| width / height | Width / Height, with choices **Fill**, **Fit content**, **Fixed** | `width: auto`, `fit-content`, a length |
| padding | Space inside | `padding` |
| margin | Space outside | `margin` |
| gap | Space between | `gap` |
| display: block flow | Arrange children: **Stack** | `display: block` |
| display: flex | Arrange children: **Row** (with a direction arrow → or ↓) | `display: flex`, `flex-direction` |
| display: grid | Arrange children: **Grid** | `display: grid` |
| justify / align | A 3×3 alignment dot grid, plus "Spread" options | `justify-content`, `align-items` |
| flex-grow | "Grow to fill" toggle on a child | `flex-grow: 1` |
| position: static | Placement: **In flow** | `position: static` |
| position: relative | Placement: **Nudged** | `position: relative` |
| position: absolute | Placement: **Free** | `position: absolute` |
| position: fixed | Placement: **Fixed to screen** | `position: fixed` |
| position: sticky | Placement: **Sticks when scrolling** | `position: sticky` |
| z-index | Stack order | `z-index` |
| breakpoint | Screen size | `@media (max-width: …)` |
| :hover / :active / :focus | Mouse over / Pressed / Focused | the selector |
| border-radius | Corner roundness | `border-radius` |
| box-shadow | Shadow | `box-shadow` |
| overflow | Content that doesn't fit: Show / Cut off / Scroll | `overflow` |
| line-height | Line spacing | `line-height` |
| letter-spacing | Letter spacing | `letter-spacing` |
| opacity | Transparency (shown as Opacity %) | `opacity` |

Discoverability rules:

- Every new element gets explicit, sensible starting styles so the first result looks intentional (see 8.2).
- The first time a concept appears, the control carries a one-line inline explanation that can be dismissed forever ("Row places children side by side").
- The Spacing and Layout tools draw the concept on the canvas (coloured bands for padding and margin, hatched bars for gaps), which teaches the box model without text.
- The Code panel shows the HTML and CSS of the selection at any time, so a curious beginner can watch code change as they drag.

### 3.8 Preview and export

- **Preview** (`Ctrl+Shift+Enter`) replaces the canvas with a live, interactive rendering built from the export output, running in a sandbox (chapter 13). Links, hover, forms, animation and custom JavaScript all work. A width selector and a "rotate" toggle test screen sizes. `Esc` returns to editing.
- **Export** (`Ctrl+Shift+E`) opens a dialog with a file tree preview and options (chapter 14), then downloads a `.zip` or writes into a chosen folder.

---

## 4. Application Interface and Screen Layout

### 4.1 Overall layout

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ Top bar: ☰ menus │ Doc name · Saved │ ↶ ↷ │      [Desktop▾][Tablet][Mobile] │ 100%▾ │ ▶ Preview │ Export │ 32px
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ Options bar: (changes with the active tool)                                               │ 36px
├────┬──────────────┬─────────────────────────────────────────────────┬────────────────────┤
│ T  │ Left dock    │                                                 │ Right dock         │
│ o  │ ┌──────────┐ │                                                 │ ┌────────────────┐ │
│ o  │ │Layers    │ │                    CANVAS                       │ │ Properties     │ │
│ l  │ │Elements  │ │                                                 │ │                │ │
│ s  │ │Assets    │ │                                                 │ │                │ │
│    │ └──────────┘ │                                                 │ ├────────────────┤ │
│44px│    260px     │                                                 │ │ Swatches│History│ │
│    │              │                                                 │ └────────────────┘ │
│    │              ├─────────────────────────────────────────────────┤       300px        │
│    │              │ Bottom drawer (collapsed): Code │ Timeline       │                    │
├────┴──────────────┴─────────────────────────────────────────────────┴────────────────────┤
│ Status bar: Page › Section 1 › Box › Text        hint text                  1440 × 2310  │ 24px
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

Visual style (Decision): dark neutral theme by default with a light theme option. 12 px UI text, 24 px control height, 4 px grid, 2 px corner radius on controls, 1 px separators, one accent colour (blue `#2f80ed`) used only for selection and active states. No cards, no shadows on panels, no gradients, no decorative icons. Panels are flat regions separated by lines.

Dock behaviour: both docks can be resized by dragging their inner edge, and collapsed with `Tab` (hides all panels for a clear canvas). Panels cannot be floated or rearranged in the first version; the layout is fixed so that documentation and muscle memory stay stable.

### 4.2 Top bar

| Item | Behaviour |
|---|---|
| Menus | **File** (New, Open…, Save version, Save a copy…, Duplicate, Versions…, Page settings…, Export…, Back to Home) · **Edit** (Undo, Redo, Cut, Copy, Paste, Paste inside, Duplicate, Delete, Select all, Copy style, Paste style, Preferences…) · **Element** (Group, Ungroup, Wrap in link, Lock, Hide, Move earlier/later, Placement) · **View** (Zoom items, Rulers, Guides, Fold line, Outline view, Panels, Theme) · **Help** (Keyboard shortcuts, About) |
| Document name | Click to rename inline |
| Save status | Text only: "Saved", "Saving…", "Not saved — storage full" (red). Hover shows the time of the last save |
| Undo / Redo | Two icon buttons; tooltip names the action ("Undo Resize Box") |
| Screen size selector | Segmented control listing the document's screen sizes, widest first. Clicking switches the canvas. A `+` opens the screen size editor (7.3). `Alt+1`, `Alt+2`, `Alt+3` switch |
| Zoom | Shows the percentage; menu with Fit, 50, 100, 200, Zoom to selection |
| Preview | Toggles preview mode |
| Export | Opens the export dialog |
| Page settings | Gear icon; opens the Page settings dialog (3.2) |

### 4.3 Tool strip

A single vertical column of 28 px icon buttons, in four groups separated by lines:

1. **Select group:** Select, Direct Select
2. **Create group:** Section, Box, Text, Media, Button, Link, Form, Place
3. **Shape group:** Layout, Spacing, Transform, Gradient
4. **Inspect group:** Eyedropper, Measure, Hand, Zoom

Behaviour:

- One tool is active at a time; it is highlighted with the accent colour.
- Tools with variants (Box, Text, Media, Form) show a small corner triangle. Press and hold, or right-click, to open a flyout. The last used variant becomes the button's face.
- Pressing a tool's shortcut again cycles its variants.
- After creating an element, a creation tool returns to Select. Double-clicking a creation tool "locks" it for repeated use (a small lock dot appears) until another tool is chosen.
- Holding `Space` gives the Hand temporarily; holding `Ctrl` gives Direct Select temporarily; holding `Alt` with Select shows distances.
- Hovering a tool for 500 ms shows a tooltip: name, shortcut, one-sentence description.

### 4.4 Options bar

One horizontal row under the top bar. Its content is defined by the active tool (chapter 5). Layout is always:

`[tool icon + name] │ [primary options] │ [▸ More]`

"More" opens the tool's advanced options as a popover anchored to the bar. This is the tool-level equivalent of the Advanced disclosure in property groups. When something is selected, the Select tool's options bar shows the most-used values of that element (X, Y, W, H, placement switch, alignment buttons).

When a screen size other than the base is active, or a state other than Normal, the far left of the options bar shows a coloured chip: `Editing: Tablet and smaller` or `Editing: Mouse over`. This chip is the constant reminder of where edits are going.

### 4.5 Left dock

Three tabs. Layers is the default.

**Layers** — the real document tree.

- One row per element: disclosure arrow, type icon, name, and on hover an eye and a lock.
- Top-level rows are sections. Text content is not a separate row; a text element shows its first words as its default name.
- Click selects (synchronised with the canvas both ways; selecting on the canvas scrolls the row into view and expands its ancestors).
- `Shift+click` range-selects, `Ctrl+click` toggles.
- Double-click the name to rename. Renaming also updates the exported class name (11.3).
- Drag to reorder or nest. A line shows "between"; a highlighted row shows "inside".
- Right-click gives the same context menu as the canvas.
- Small badges at the right of a row: a monitor glyph if the element has overrides at smaller screen sizes; a cursor glyph if it has state styles; a bolt if it is animated; a link glyph if it is or contains a link; `</>` if it has custom CSS.
- Filter field at the top: type to filter by name or tag. A toggle switches to **Outline view**, which lists only headings and landmarks in order with their levels. This is the document outline; it does not need its own panel.
- Rows are virtualised so thousands of elements stay fast.

**Elements** — every HTML element Daisy supports, as a searchable list. Not a template library: each entry is one bare element.

- Categories (collapsible): Structure, Text, Media, Links & buttons, Lists, Tables, Forms, Embeds, Custom.
- Each row: icon, friendly name, and the tag in muted text (`Paragraph  p`).
- Search matches friendly name, tag and synonyms ("picture" finds Image).
- Click an entry: arms the **Place** tool with that element; the next click or drag on the canvas creates it.
- Drag an entry onto the canvas or onto a Layers row: creates it at the drop position.
- Double-click an entry: inserts it after the current selection (or inside it if it is an empty container).

**Assets** — files stored in the document.

- Tabs inside: Images, Video & audio, Fonts, Other.
- Upload button, or drop files on the panel or anywhere on the canvas.
- Each asset: thumbnail, file name, dimensions, size, and a usage count. Clicking the count selects the elements that use it.
- Drag an image asset onto the canvas to create an image; drag onto an existing element to set it as that element's image (for `<img>`) or as a fill (for anything else, with `Alt`).
- Replace, rename, delete (blocked with a message if the asset is in use, with "Delete anyway").

### 4.6 Right dock

**Properties** (top, always visible, takes most of the height).

- Header: element icon, editable name, tag in muted text, and a **State** selector (Normal ▾).
- Below the header, a one-line context strip that appears only when relevant: `Tablet and smaller · 3 values set here` with a menu to review or clear them.
- Then the property groups (chapter 6), each collapsible, each with its own Advanced disclosure.
- With nothing selected, the panel shows Page properties (background, base text, title, language).
- With several elements selected, it shows the groups they have in common; differing values show "Mixed".

**Swatches** (bottom-right tab). The document's reusable colours and text styles. This merges "colour library" and "typography library" into one panel because both are named values.

- Colours: a grid of named swatches. Each is a CSS custom property (`--brand: #2f80ed`). Click applies to the selected element's fill; `Shift+click` applies to text colour. Editing a swatch updates every use.
- Text styles: a list of named font settings (family, size, weight, line spacing). Each field is a custom property; applying a text style sets the element's typography values to those variables.
- "Add from selection" creates a swatch from the selected element's current value.

**History** (bottom-right tab). A list of the session's actions, newest at the bottom, with the current position highlighted. Clicking an entry jumps to that state. Future (undone) entries are greyed.

### 4.7 Bottom drawer

Collapsed to a 24 px tab strip by default.

**Code** (`Ctrl+E`). Three sub-tabs:

- *Element*: read-only HTML and generated CSS for the current selection, updating live. Under it, an editable "Custom CSS for this element" box (declarations only).
- *Page CSS*: an editor for free-form custom CSS appended after the generated stylesheet.
- *Page JavaScript*: an editor for custom JavaScript and for custom `<head>` content.

This panel merges "CSS inspector" and "code editor". Beginners never need to open it.

**Timeline**. Appears as a tab only once the document has at least one animation, or when the user clicks "Edit on timeline" in the Animation group. It shows keyframes for the selected element's animation (chapter 6, Animation).

### 4.8 Panels considered and the decision

| Candidate | Decision | Reason |
|---|---|---|
| Assets | Included (left dock) | Images, video and fonts need a home and usage tracking |
| Colour library | Merged into Swatches | One panel for named values |
| Typography library | Merged into Swatches | Same |
| Document outline | A view toggle inside Layers | Same data as Layers, filtered |
| CSS inspector | Merged into Code → Element | It is the read-only side of the code panel |
| Code editor | Included (bottom drawer) | Required for custom CSS and JS |
| Animation timeline | Included, appears on demand | Keyframes need a time axis; nothing else does |
| History | Included (right dock tab) | Cheap to build on the history stack and valuable for trust |
| Export settings | A dialog, not a panel | Used once per export |

### 4.9 Status bar

Left: the breadcrumb path of the selection; each part is clickable and hovering one highlights that element on the canvas. Centre: a context hint for the active tool ("Click to add text · Drag to set width"). Right: page size in pixels and pointer position in page coordinates.

### 4.10 Dialogs

Only five: New document, Page settings, Screen sizes, Export, Versions. Everything else is inline or a popover.

---

## 5. Tool System

### 5.1 How features were sorted

The brief lists about seventy candidate features. Each was assigned by one test: *does it need its own pointer behaviour on the canvas?*

| Outcome | Features |
|---|---|
| **Dedicated tool** (18) | Select, Direct Select, Section, Box, Text, Media, Button, Link, Form, Place, Layout, Spacing, Transform, Gradient, Eyedropper, Measure, Hand, Zoom |
| **Variant of a tool** | Heading (Text), Ellipse and Divider (Box), Video / Audio / Embed / Icon (Media), Input / Textarea / Select / Checkbox / Radio (Form), Flexbox and Grid and Gap (Layout), Padding and Margin (Spacing) |
| **Placed through the Place tool from the Elements panel** | List, Navigation, Table, semantic landmarks, custom HTML element, everything else |
| **Contextual operation of Select** | Move, multi-select, alignment, distribution, positioning, corner radius handles |
| **Property group only** | Fill colour, border, shadow, effects, filters, blend modes, opacity, all typography values, transitions, attributes, custom CSS |
| **Panel** | States (selector in Properties), responsive (top bar + indicators), animation (Timeline), custom JavaScript (Code) |

Why not more tools: a Shadow tool, a Border tool or a Font tool would only be a button that opens a panel. That is a property group, and making it a tool would add count without adding a gesture.

### 5.2 Shared tool rules

- Every creation tool supports two gestures. **Click** creates the element with default size at the insertion point. **Drag** draws a rectangle and creates the element with that width and height.
- Creation is *in flow* by default. The insertion line shows where in the parent's order the new element will go; the drawn rectangle sets size, not position. Holding `Alt` while drawing creates the element as **Free** at exactly the drawn rectangle. The options bar of every creation tool has the same switch: `Place: In flow | Free`.
- The parent of a new element is the innermost container under the pointer. Elements that cannot contain others (text, image, input) are never chosen as parents; the insertion point falls before or after them.
- `Esc` cancels a gesture in progress; a second `Esc` returns to Select.
- All tools write through the same command layer (10.6), so every tool action is undoable and identical to the equivalent panel edit.

### 5.3 Tool specifications

#### Select

| Field | Specification |
|---|---|
| Tool | Select |
| Shortcut | `V` |
| Icon concept | Solid arrow pointer |
| Purpose | Choose elements, move them, resize them, round their corners |
| Beginner interaction | Click an element to select it. Drag to move it. Drag a handle to resize |
| Advanced options | Options bar: X, Y, W, H fields with units; placement switch (In flow / Free); alignment and distribution buttons; "Auto-select: Scoped / Deepest". More: snap settings (on/off, distance, snap to siblings / parent / guides), "Resize keeps unit" (keep `%` or `rem` instead of converting to `px`), nudge distance |
| Canvas behaviour | Hover outline and name tag. Selection outline with 8 handles. Four small round corner handles inside the box edit corner roundness (`Alt` edits one corner). Flow drag shows insertion line; free drag shows alignment guides. Marquee from empty space |
| Output | `width`, `height`, `left`/`top`/`right`/`bottom`, `border-radius`, child order, parent changes |
| Dependencies | Hit testing, overlay, measurement, snapping engine, command layer |

#### Direct Select

| Field | Specification |
|---|---|
| Tool | Direct Select |
| Shortcut | `A` (or hold `Ctrl` with Select) |
| Icon concept | Hollow arrow pointer |
| Purpose | Reach deeply nested elements in one click, ignoring the scope rule |
| Beginner interaction | Click exactly the thing you want, however deep it is |
| Advanced options | "Click through locked", "Select inline text parts" (lets a click select a `<strong>` or `<a>` inside a paragraph) |
| Canvas behaviour | Hover always outlines the deepest element. Repeated clicks at the same point walk up through ancestors. Otherwise identical to Select |
| Output | Same as Select |
| Dependencies | Same as Select |

#### Section

| Field | Specification |
|---|---|
| Tool | Section |
| Shortcut | `S` |
| Icon concept | A wide rectangle with a horizontal line through the page |
| Purpose | Add a full-width structural band to the page |
| Beginner interaction | Move between two sections (or to the top or bottom of the page); a full-width insertion line appears; click to add an empty section |
| Advanced options | Options bar: Kind (Section, Header, Footer, Main content, Navigation, Article, Sidebar), starting min-height. More: tag override, "Add id for linking" |
| Canvas behaviour | Only shows insertion lines between top-level sections. Drag vertically after clicking to set the min-height |
| Output | `<section>` (or `<header>`, `<footer>`, `<main>`, `<nav>`, `<article>`, `<aside>`) with `min-height: 400px` |
| Dependencies | Document model, renderer |

#### Box

| Field | Specification |
|---|---|
| Tool | Box (variants: Box, Ellipse, Divider) |
| Shortcut | `R` |
| Icon concept | Rectangle outline |
| Purpose | Create the universal building block: a rectangle that is both a shape and a container |
| Beginner interaction | Drag to draw a box. Click for a default 160 × 160 box. Then drop other things into it |
| Advanced options | Options bar: fill colour, border, corner roundness, place In flow / Free. More: tag (`div`, `section`, `article`, `aside`, `header`, `footer`, `nav`, `main`, `figure`, `span`), "Create empty (no fill, fill width)", `Shift` constrains to a square |
| Canvas behaviour | Live rubber-band rectangle with size label. Insertion line shows the flow position |
| Output | Box: `<div>` with `width`, `height`, `background-color: #d9d9d9`. Ellipse: same plus `border-radius: 50%`. Divider: `<hr>` with `border: 0; border-top: 1px solid #cccccc; width: 100%` |
| Dependencies | Creation pipeline, insertion-point finder |

A box drawn inside another box nests in it. A box becomes a layout container the moment it has children; nothing needs converting.

#### Text

| Field | Specification |
|---|---|
| Tool | Text (variants: Text, Heading) |
| Shortcut | `T` |
| Icon concept | Capital "T" |
| Purpose | Create and edit text |
| Beginner interaction | Click and type. Click existing text to edit it. `Esc` to finish |
| Advanced options | Options bar: Kind (Text / Heading with level 1–6), font, weight, size, colour, alignment, bold, italic, underline, link. More: tag (`p`, `h1`–`h6`, `span`, `blockquote`, `pre`, `label`, `figcaption`, `li`), line spacing, letter spacing, "Paste as plain text" |
| Canvas behaviour | Click creates a text element that fills the parent's width (auto width); drag creates one with a fixed width. Clicking existing text places the caret there. While editing, selecting a range and using bold / italic / link wraps it in `<strong>` / `<em>` / `<a>`. `Enter` makes a new paragraph element after the current one; `Shift+Enter` inserts `<br>` |
| Output | `<p>` or `<hN>` with text nodes and inline children. Text: `margin: 0; font-size: 16px; line-height: 1.5`. Heading 2: `margin: 0; font-size: 32px; line-height: 1.2; font-weight: 700` (sizes per level in 8.2) |
| Dependencies | Rich text editing (9.7), font system, Typography group |

#### Media

| Field | Specification |
|---|---|
| Tool | Media (variants: Image, Video, Audio, Embed, Icon) |
| Shortcut | `I` |
| Icon concept | Picture frame with a mountain and sun |
| Purpose | Place images, video, audio, embedded pages and SVG icons |
| Beginner interaction | Click or drag on the canvas; a file picker opens; the chosen image appears. Or drop a file straight onto the canvas with any tool |
| Advanced options | Options bar: source (Upload / From assets / URL), Fit (Fill, Fit inside, Stretch, Original), alt text field. More: `loading` (lazy / eager), `srcset` and `sizes`, `<picture>` sources, video controls / autoplay / loop / muted / poster, embed URL and sandbox flags, inline SVG versus `<img>` |
| Canvas behaviour | Drag defines a frame; the image fills it using `object-fit: cover`. Click places at natural size, capped to the parent's width. Until a source is chosen, shows a grey placeholder with an icon. Embeds show a static placeholder in the editor and run only in Preview |
| Output | `<img src alt width height>` with `max-width: 100%; height: auto` (click) or explicit size plus `object-fit` (drag). `<video controls>`, `<audio controls>`, `<iframe>`, inline `<svg>` or `<img>` for icons |
| Dependencies | Asset store, file import, sanitiser for SVG |

Alt text: after an image is placed, the options bar shows an "Describe this image" field with focus. It can be skipped; skipping marks the image as needing attention in the accessibility check.

#### Button

| Field | Specification |
|---|---|
| Tool | Button |
| Shortcut | `B` |
| Icon concept | Rounded rectangle with a short line in it |
| Purpose | Create a clickable button |
| Beginner interaction | Click; a button labelled "Button" appears with its text selected for typing |
| Advanced options | Options bar: label, link target (turns it into a link styled as a button), fill, text colour, corner roundness. More: element (`button` or `a`), `type` (button / submit / reset), disabled, "Add mouse-over style" shortcut that switches the state selector to Mouse over |
| Canvas behaviour | Click creates a fit-content button. Drag creates a fixed-size one |
| Output | `<button type="button">Button</button>` with explicit styles: `padding: 12px 20px; border: 0; border-radius: 6px; background-color: #111111; color: #ffffff; font: inherit; cursor: pointer`. With a link target: `<a href>` with the same styles plus `display: inline-block; text-decoration: none` |
| Dependencies | Text editing, States, Link system |

#### Link

| Field | Specification |
|---|---|
| Tool | Link |
| Shortcut | `L` |
| Icon concept | Two chain links |
| Purpose | Make things clickable and set where they go |
| Beginner interaction | Click any element; a small popover asks "Where should this go?" with choices: Web address, Section on this page, Email, Phone, File |
| Advanced options | Open in new tab, `rel` values, `download`, custom `href`, "Link the whole element / only the selected text" |
| Canvas behaviour | Hover highlights linkable elements. Clicking existing text with a text range selected links that range. Clicking an element wraps it in `<a>` (or converts it if it is a button). Clicking empty space creates a new text link. Elements that are links show a small link badge on hover |
| Output | `<a href="…">`. "Section on this page" adds an `id` to the target section and uses `href="#id"`. New tab adds `target="_blank" rel="noopener"` |
| Dependencies | Document model (wrap / unwrap), section ids, asset store for File links |

Validity rule: a link cannot contain another link or a button. Daisy refuses the wrap and explains why.

#### Form

| Field | Specification |
|---|---|
| Tool | Form (variants: Text field, Text area, Dropdown, Checkbox, Radio, Label, Form container) |
| Shortcut | `F` |
| Icon concept | A text field outline with a caret |
| Purpose | Create form controls |
| Beginner interaction | Pick a control, click on the canvas. A field appears together with a label reading "Label" ready to type |
| Advanced options | Options bar: field kind (text, email, password, number, tel, url, date, search, file, range, color), placeholder, required. More: `name`, `value`, `autocomplete`, `min` / `max` / `step` / `pattern`, options editor for dropdowns, radio group name, form `action` and `method`, "Create without label" |
| Canvas behaviour | Controls render as real controls but do not react to typing in the editor; double-click edits the placeholder or label text. Dropping a control outside a form is allowed (a notice suggests a Form container) |
| Output | `<label for="id">Label</label><input id="id" type="text" name="field-1">` with explicit starting styles (padding, 1 px border, radius, `font: inherit`). Checkbox and radio are wrapped inside their `<label>` |
| Dependencies | Attribute system, id generator, Accessibility checks |

#### Place

| Field | Specification |
|---|---|
| Tool | Place |
| Shortcut | `N` |
| Icon concept | A plus sign inside a dashed square |
| Purpose | Put any element from the Elements panel on the canvas |
| Beginner interaction | Click an element in the Elements panel, then click where it should go |
| Advanced options | Options bar: the armed element (click to change via a searchable dropdown), tag field accepting any tag name including custom elements, place In flow / Free. More: starting attributes, starting class |
| Canvas behaviour | Same click and drag behaviour as Box. Compound elements create their minimum valid structure: List makes `<ul>` with three `<li>`; Table makes a 3 × 3 `<table>` with `<thead>` and `<tbody>`; Navigation makes `<nav>` containing `<ul>` with three linked items |
| Output | The chosen element with its starting styles (8.2) |
| Dependencies | Element registry, Elements panel |

Those compound structures are not templates: they are the smallest valid HTML for the element, unstyled except for explicit defaults.

#### Layout

| Field | Specification |
|---|---|
| Tool | Layout |
| Shortcut | `G` |
| Icon concept | A square split into a tall cell and two stacked cells |
| Purpose | Control how a container arranges its children, directly on the canvas |
| Beginner interaction | Click a container. Choose Stack, Row or Grid in the options bar. Drag the space between children to change the gap. Click a dot in the 3 × 3 alignment grid |
| Advanced options | Options bar: Arrange (Stack / Row / Grid), direction, wrap, alignment grid, gap. For Grid: columns and rows counters. More: `display` raw value, `justify-content`, `align-items`, `align-content`, `justify-items`, row and column gap separately, track editor (`1fr`, `minmax()`, `repeat()`, `auto-fit`), named areas, `grid-auto-flow`, auto track sizes, reverse directions |
| Canvas behaviour | **Row/Stack:** hatched bars appear between children; dragging one changes `gap`. A direction arrow sits at the container's start; clicking flips row and column. Dragging a child reorders. Each child shows a small "grow" toggle. **Grid:** track lines are drawn across the container with a size badge on each track (`1fr`, `200px`); drag a line to resize the tracks next to it; click `+` at the end of a row or column of badges to add a track; right-click a badge to delete or change its unit. Drag a child to another cell to place it; drag a child's edge to span cells; drag across empty cells to mark an area for the next created element |
| Output | `display`, `flex-direction`, `flex-wrap`, `justify-content`, `align-items`, `gap`, `grid-template-columns`, `grid-template-rows`, and on children `grid-column`, `grid-row`, `flex-grow`, `align-self`, `order` |
| Dependencies | Layout read/write helpers (7.2), measurement of flex lines and grid tracks, Layout property group |

#### Spacing

| Field | Specification |
|---|---|
| Tool | Spacing |
| Shortcut | `P` |
| Icon concept | A square inside a larger dashed square |
| Purpose | Edit space inside, outside and between by dragging |
| Beginner interaction | Hover an element: green bands show space inside, orange bands show space outside. Drag any band's edge |
| Advanced options | Options bar: four inside values and four outside values with a link toggle each, gap. More: unit, "Drag affects: one side / opposite sides / all sides", allow negative outside space, set outside to `auto` (centring), logical properties (`padding-inline`, `margin-block`), step size |
| Canvas behaviour | Bands are drawn translucent with the value written in them. `Alt+drag` changes the opposite side too; `Shift+drag` changes all four. Dragging between two siblings in a Row/Grid container edits the parent's gap. Double-click a band to type a value. Zero-size bands have a 4 px grab strip so they can be pulled open |
| Output | `padding-*`, `margin-*`, `gap` |
| Dependencies | Box-model measurement (`getComputedStyle`), overlay |

#### Transform

| Field | Specification |
|---|---|
| Tool | Transform |
| Shortcut | `Q` |
| Icon concept | A square with a curved rotation arrow at one corner |
| Purpose | Rotate, scale, skew and shift an element visually without changing layout |
| Beginner interaction | Click an element. Drag outside a corner to rotate. Drag a corner to scale |
| Advanced options | Options bar: rotate, scale X / Y, move X / Y, skew X / Y, origin (9-point picker). More: 3D rotate, perspective, raw `transform` list editor, "Use individual properties" (`rotate`, `scale`, `translate`), reset |
| Canvas behaviour | The bounding box rotates with the element. The origin point is a draggable crosshair. `Shift` snaps rotation to 15°. A ghost outline shows the untransformed layout box, which teaches that transforms do not affect neighbours |
| Output | `transform`, `transform-origin` |
| Dependencies | Matrix maths for overlay drawing, Transform property group |

Decision: Transform is separate from Select's resize because they are different things on the web. Resize changes `width` and `height` and reflows the page. Transform scales the painted result only. Mixing them in one gesture would make output unpredictable.

#### Gradient

| Field | Specification |
|---|---|
| Tool | Gradient |
| Shortcut | `D` |
| Icon concept | A square fading from dark to light |
| Purpose | Draw gradients directly on an element |
| Beginner interaction | Drag across an element. A gradient from the current fill colour to a lighter tint appears along the drag line |
| Advanced options | Options bar: type (Linear, Radial, Conic), stop list, angle. More: repeating gradients, colour interpolation space, stop positions with units, apply to text (background-clip), add as a new fill layer versus replace |
| Canvas behaviour | After drawing, a line with stop handles stays on the element. Drag endpoints to change angle and extent; click the line to add a stop; drag a stop off to remove it; double-click a stop to pick its colour |
| Output | `background-image: linear-gradient(…)` (or `radial-gradient`, `conic-gradient`) as a layer in the Fill stack |
| Dependencies | Fill layer model, colour picker |

#### Eyedropper

| Field | Specification |
|---|---|
| Tool | Eyedropper |
| Shortcut | `E` |
| Icon concept | Pipette |
| Purpose | Pick up a colour (or a whole style) from anything visible |
| Beginner interaction | Select an element, press `E`, click a colour anywhere on the page. The selected element's fill becomes that colour |
| Advanced options | Options bar: Apply to (Fill, Text, Border), Sample (Pixel / Element's own colour). More: "Pick up full style" (copies all appearance declarations), "Add to swatches" |
| Canvas behaviour | A magnifier loupe follows the pointer showing the colour and its hex value. `Shift+click` applies to text colour, `Alt+click` to border |
| Output | `background-color`, `color` or `border-color` |
| Dependencies | The browser `EyeDropper` API where available; otherwise reads computed styles of the element under the pointer |

#### Measure

| Field | Specification |
|---|---|
| Tool | Measure |
| Shortcut | `M` |
| Icon concept | Ruler |
| Purpose | Read distances and sizes |
| Beginner interaction | Click one element then hover another: the distances between them are drawn. Or drag anywhere to measure a length |
| Advanced options | Units (px, rem, % of parent), "Measure from: border edge / content edge / outside edge", copy value |
| Canvas behaviour | Red lines with number labels. Nothing in the document changes |
| Output | None |
| Dependencies | Measurement |

#### Hand

| Field | Specification |
|---|---|
| Tool | Hand |
| Shortcut | `H` (or hold `Space`) |
| Icon concept | Open hand |
| Purpose | Move the view |
| Beginner interaction | Drag the canvas |
| Advanced options | "Scroll to section" dropdown |
| Canvas behaviour | Cursor becomes a hand; grabbing hand while dragging |
| Output | None |
| Dependencies | Viewport transform |

#### Zoom

| Field | Specification |
|---|---|
| Tool | Zoom |
| Shortcut | `Z` |
| Icon concept | Magnifying glass |
| Purpose | Change magnification |
| Beginner interaction | Click to zoom in, `Alt+click` to zoom out |
| Advanced options | Drag a rectangle to zoom into it; buttons for Fit, 100%, Selection; "Scrubby zoom" (drag left/right) |
| Canvas behaviour | Zoom is centred on the pointer |
| Output | None |
| Dependencies | Viewport transform |

### 5.4 Shortcut summary

| Key | Tool | Key | Tool |
|---|---|---|---|
| `V` | Select | `G` | Layout |
| `A` | Direct Select | `P` | Spacing |
| `S` | Section | `Q` | Transform |
| `R` | Box | `D` | Gradient |
| `T` | Text | `E` | Eyedropper |
| `I` | Media | `M` | Measure |
| `B` | Button | `H` | Hand |
| `L` | Link | `Z` | Zoom |
| `F` | Form | `N` | Place |

Shortcuts avoid combinations a browser reserves and will not release (`Ctrl+N`, `Ctrl+T`, `Ctrl+W`, `Ctrl+1`–`9`). Single-letter shortcuts are disabled while typing in any field or editing text.

---

## 6. Properties System

### 6.1 Architecture

The Properties panel is generated from a **property registry**. Nothing in the panel is hand-wired per element.

```ts
interface PropertyGroupDef {
  id: string;                         // "spacing"
  label: string;                      // "Spacing"
  appliesTo: (el: ElementNode, ctx: ElementContext) => boolean;
  simple: ControlDef[];               // always visible
  advanced: ControlDef[];             // inside the Advanced disclosure
  ownedProps: string[];               // CSS properties this group owns ("Other properties" suggestions
                                      // and where unknown-but-related props are listed)
}

interface ControlDef {
  id: string;
  label: string;                      // plain language
  css: string[];                      // properties it reads and writes
  control: 'length' | 'color' | 'select' | 'toggle' | 'segmented' | 'box-sides'
         | 'align-grid' | 'layers' | 'text' | 'font' | 'custom';
  read: (decls: StyleDecls, computed: ComputedInfo) => ControlValue; // CSS → control
  write: (value: ControlValue) => StyleDecls;                        // control → CSS
  visibleWhen?: (el: ElementNode, ctx: ElementContext) => boolean;
  help: string;                       // one-sentence tooltip
}
```

`ElementContext` carries what the group needs to adapt: the element's tag, whether it has children, the parent's arrangement (stack / row / grid), the element's placement, and the active screen size and state.

Rules that apply to every control:

1. **Reads are layered.** A control shows the value set at the current screen size and state if there is one; otherwise the inherited value from a wider screen size; otherwise the browser's computed value in muted text as a placeholder.
2. **Writes go to exactly one place:** the active screen size and the active state.
3. **Origin marker.** A small dot left of each label: solid blue = set here; hollow = inherited from another screen size (tooltip names it); none = not set (browser default or inherited from a parent element). Right-click a label: "Reset" (removes the value here), "Set for all sizes" (moves it to the base), "Copy CSS".
4. **Length fields** accept a number (uses the field's current unit), a number with a unit, a keyword (`auto`, `fit-content`), arithmetic (`100% - 40px` becomes `calc(100% - 40px)`), a variable (`var(--gap)`), or any other valid value, which is kept as typed and shown with a "custom" tag. Arrow keys step by 1; `Shift` by 10; `Alt` by 0.1. Dragging the label scrubs the value.
5. **Validation** uses the browser: `CSS.supports(property, value)`. Invalid input is rejected with the field outlined red and the previous value kept.
6. **Unit change** converts the value so the element does not visibly change, using the measured size (for example `320px` in a 1280 px parent becomes `25%`).

### 6.2 How groups adapt

| Selection | Groups shown, in order |
|---|---|
| Section or Box (container) | General, Size, Placement, Layout, Spacing, Fill, Border, Effects, Transform, Visibility, Transition, Animation, Attributes, Accessibility, Custom CSS |
| Text / Heading | General, Size, Placement, Spacing, Typography, Fill, Border, Effects, Transform, Visibility, Transition, Animation, Attributes, Accessibility, Custom CSS |
| Image / Video | General (with Source), Size (with Fit), Placement, Spacing, Border, Effects, Transform, Visibility, Transition, Animation, Attributes, Accessibility, Custom CSS |
| Button / Link | General (with Link), Size, Placement, Layout (if it has element children), Spacing, Typography, Fill, Border, Effects, Transform, Visibility, Transition, Animation, Attributes, Accessibility, Custom CSS |
| Form control | General (with Field settings), Size, Placement, Spacing, Typography, Fill, Border, Effects, Visibility, Transition, Attributes, Accessibility, Custom CSS |
| Nothing selected | Page: Background, Base text, Metadata |

Extra adaptation inside groups:

- A **child of a Row** gains "In row" controls in Size (Grow to fill, Shrink, Align self, Order). A **child of a Grid** gains "In grid" controls (column and row start, span).
- **Layout** is hidden for elements that cannot have children.
- **Typography** is shown on containers too, collapsed and labelled "Text (passed to children)", because text values are inherited and setting them on a container is a legitimate, common technique.
- Groups with no values set start collapsed, except General, Size and the group most relevant to the element type.

### 6.3 Evaluation of the 21 candidate groups

| Candidate | Decision |
|---|---|
| General, Size, Spacing, Layout, Typography, Border, Effects, Transform, Attributes, Accessibility, Custom CSS | Kept as groups |
| Position | Kept, named **Placement** |
| Fill + Background | Merged into **Fill**. On the web a fill *is* a background; two groups would duplicate each other |
| Visibility | Kept (small) |
| Overflow | Moved into Size, where the question "what if content doesn't fit?" naturally arises |
| Animation, Transitions | Kept as two groups: **Transition** and **Animation** |
| Responsive | Not a group. It is a dimension of every property (origin markers, top bar selector, context strip) |
| States | Not a group. It is the State selector in the Properties header |
| Custom JavaScript | Not an element property. It lives in Code → Page JavaScript. The element's Attributes group offers "Copy selector" for use in scripts |

### 6.4 Group specifications

For every group: "Inherited" answers whether children receive the value automatically. "Responsive" is always yes (every CSS value can differ per screen size) unless stated.

#### General

| | |
|---|---|
| Simple | Name (layer name). Kind (friendly name of the tag, e.g. "Section", with a dropdown of sensible alternatives for this element). Element-specific basics: image Source and Description; link Destination; button Label; field Placeholder and Required |
| Advanced | Tag (free text, any valid tag name). Class name (auto-generated from the name; editable). Extra classes. `id`. Language override |
| Defaults | Name from element type and a counter ("Box 3"). Class from the name (`box-3`) |
| Supported | All elements |
| Output | The tag itself, `class`, `id`, element attributes (`src`, `alt`, `href`, …). No CSS |
| Inherited | No |
| Responsive | No. Structure and attributes are the same at every size |
| Feedback | Changing the tag updates the name tag on the canvas and the Layers icon immediately |

#### Size

| | |
|---|---|
| Simple | Width and Height, each with a mode: **Fill**, **Fit content**, **Fixed** (with a value). Lock-proportions toggle. "Content that doesn't fit": Show / Cut off / Scroll. For images and video: Fit (Fill frame, Fit inside, Stretch, Original). In a Row: "Grow to fill" toggle |
| Advanced | Min and max width and height. Units (px, %, rem, em, vw, vh, ch). Aspect ratio. Box sizing. Separate horizontal and vertical overflow. `object-position`. In a Row: `flex-grow`, `flex-shrink`, `flex-basis`, `align-self`, `order`. In a Grid: `grid-column`, `grid-row`, `justify-self`, `align-self` |
| Defaults | Blocks: width Fill (`auto`), height Fit content (`auto`). Inline elements: fit content both ways. Overflow Show |
| Supported | All. Width and height are disabled, with an explanation, for inline text parts (`span`, `strong`) unless their display is changed |
| Output | `width`, `height`, `min-*`, `max-*`, `aspect-ratio`, `overflow-x`, `overflow-y`, `object-fit`, `flex-*`, `grid-*` |
| Inherited | No |
| Feedback | Hovering a field highlights that dimension on the canvas with a labelled line. If the real size differs from the set size (because the parent row is shrinking it, or a max is clamping it), a muted note shows the real size and the reason: "Shown 280 — limited by Max width" |

Mode mapping: Fill = `width: auto` for blocks in a Stack, `flex-grow: 1` along a Row's direction, `align-self: stretch` across it, `width: 100%` for free elements. Daisy picks the right one for the context and shows which in the tooltip. Fit content = `fit-content`. Fixed = a length.

#### Placement

| | |
|---|---|
| Simple | Placement: **In flow**, **Free**, **Fixed to screen**, **Sticks when scrolling**. For Free and Fixed: a pin widget (a square with four side toggles) and X / Y fields. For Sticky: "Stick at: Top" with a distance. Stack order: Bring forward / Send back buttons |
| Advanced | **Nudged** (`relative`) placement. All four offsets with units. `inset` shorthand view. `z-index` numeric. "Positioned relative to:" (shows which ancestor is the anchor; click to select it). Float and clear. `isolation` |
| Defaults | In flow, no offsets, stack order auto |
| Supported | All except the page body |
| Output | `position`, `top`, `right`, `bottom`, `left`, `z-index`, `float`, `clear` |
| Inherited | No |
| Feedback | For Free elements the canvas draws thin lines from the pinned sides to the anchor's edges with the distances. The anchor ancestor gets a dotted outline |

#### Layout

| | |
|---|---|
| Simple | Arrange children: **Stack / Row / Grid**. For Row: direction (→ ↓), 3 × 3 alignment grid, Spread (Packed / Space between / Space around / Space evenly), Wrap toggle, Space between. For Grid: Columns and Rows counters, Space between, alignment grid |
| Advanced | `display` (block, flex, inline-flex, grid, inline-grid, inline, inline-block, flow-root, contents, none, list-item, table values). `flex-direction` including reverse, `flex-wrap`, `justify-content`, `align-items`, `align-content`, `row-gap`, `column-gap`. Grid: track list editors for columns and rows with `fr`, `minmax()`, `repeat()`, `auto-fill` / `auto-fit`; `grid-auto-flow`, `grid-auto-rows`, `grid-auto-columns`, `grid-template-areas` as an editable text grid, `justify-items`. Multi-column text (`columns`, `column-gap`) |
| Defaults | Stack |
| Supported | Elements that can have children |
| Output | `display`, `flex-*`, `justify-*`, `align-*`, `gap`, `grid-template-*`, `grid-auto-*` |
| Inherited | No |
| Feedback | Hovering Space between highlights gaps on the canvas. Changing the arrangement re-lays out live. The button "Edit on canvas" switches to the Layout tool |

#### Spacing

| | |
|---|---|
| Simple | A box diagram: an inner ring for Space inside and an outer ring for Space outside, each with four editable numbers and a link toggle (all sides / horizontal + vertical / independent). A "Center horizontally" toggle |
| Advanced | Units per side. `auto` on any outside side. Negative outside values. Logical properties toggle (`padding-inline-start`, etc.). Shorthand preview (`padding: 16px 24px`). `scroll-margin` and `scroll-padding` |
| Defaults | All zero (Daisy's base stylesheet zeroes default margins on text elements; see 11.6) |
| Supported | All. Vertical outside space on inline elements is disabled with an explanation |
| Output | `padding-top/right/bottom/left`, `margin-top/right/bottom/left` (stored as longhands, collapsed on export) |
| Inherited | No |
| Feedback | Hovering or focusing a field draws that band on the canvas in green (inside) or orange (outside) |

"Center horizontally" sets `margin-left: auto; margin-right: auto` and is enabled only when the element has a width that is not Fill; otherwise the control explains: "Give this a width or max width first."

#### Typography

| | |
|---|---|
| Simple | Font (searchable dropdown with previews). Weight. Size. Colour. Alignment (left / centre / right / justify). Line spacing. Bold, italic, underline, strikethrough toggles. Text style (apply a swatch) |
| Advanced | Letter spacing. Word spacing. Case (`text-transform`). Decoration style, colour, thickness and offset. Indent. Wrapping (`white-space`, `text-wrap: balance / pretty`, `overflow-wrap`, `word-break`, `hyphens`). Truncate with ellipsis (one line or N lines). Vertical align. Direction and writing mode. Font features (`font-feature-settings`, `font-variant-*`), variable font axes. Text shadow. Font stretch. List style (for lists). Fluid size helper (builds a `clamp()` from a min and max size) |
| Defaults | Inherited from the page: system sans-serif, 16 px, `#111111`, line spacing 1.5 |
| Supported | Text elements, buttons, links, form controls, and containers (to pass values down) |
| Output | `font-family`, `font-size`, `font-weight`, `font-style`, `line-height`, `letter-spacing`, `color`, `text-align`, `text-decoration-*`, `text-transform`, and the others listed |
| Inherited | **Yes** for almost all. The origin marker has an extra state here: "from parent *Section 1*" with a click-through to that parent |
| Feedback | Live. When a text range is selected during editing, the group edits that range (creating a `<span>` when needed) instead of the whole element |

#### Fill

| | |
|---|---|
| Simple | A list of fill layers, top first. Each layer is a Colour, a Gradient or an Image. Add, remove, reorder, toggle. Colour picker with hex, opacity, and document swatches. Image layer: source, Size (Cover / Contain / Original / Tile) and a 9-point position picker |
| Advanced | Per layer: `background-size` with lengths, `background-position` with offsets, `background-repeat`, `background-attachment`, `background-origin`, `background-clip` (including `text`), `background-blend-mode`. Colour formats (hex, rgb, hsl, oklch). Multiple gradients. Raw `background` shorthand view |
| Defaults | None (transparent), except the Box tool's `#d9d9d9` |
| Supported | All except replaced media where it would be invisible |
| Output | `background-color` plus comma-separated `background-image`, `background-size`, `background-position`, `background-repeat` |
| Inherited | No |
| Feedback | Live. "Edit on canvas" on a gradient layer switches to the Gradient tool |

Text colour lives in Typography, not here, because on the web it is `color`, a different property.

#### Border

| | |
|---|---|
| Simple | Border on/off. Colour, thickness, style (solid, dashed, dotted). Corner roundness with a link toggle for all four corners |
| Advanced | Each side separately (colour, thickness, style). All border styles. Elliptical radii. Outline (colour, thickness, style, offset). Border image. Logical corners |
| Defaults | No border, roundness 0 |
| Supported | All |
| Output | `border-*-width/style/color`, `border-*-radius`, `outline-*` |
| Inherited | No |
| Feedback | Corner handles on the canvas mirror the roundness fields |

#### Effects

| | |
|---|---|
| Simple | Opacity slider. Shadow list (add; each has X, Y, blur, spread, colour, and an Inside toggle). Blur |
| Advanced | Blend mode (`mix-blend-mode`). Filters list in order: blur, brightness, contrast, grayscale, hue-rotate, invert, saturate, sepia, drop-shadow. Backdrop filters. `clip-path` (preset shapes and raw value). Mask image. Cursor. Pointer events. `will-change` |
| Defaults | Opacity 100%, no shadows, no filters |
| Supported | All |
| Output | `opacity`, `box-shadow`, `filter`, `backdrop-filter`, `mix-blend-mode`, `clip-path`, `mask-*`, `cursor`, `pointer-events` |
| Inherited | No (`cursor` and `pointer-events` are; noted in their tooltips) |
| Feedback | Live |

#### Transform

| | |
|---|---|
| Simple | Rotate. Scale. Move X / Y. Flip horizontal / vertical buttons |
| Advanced | Skew X / Y. Scale X and Y separately. Origin picker and values. 3D: rotate X / Y / Z, translate Z, perspective, `transform-style`, `backface-visibility`. Ordered raw function list |
| Defaults | None |
| Supported | All block-like elements |
| Output | `transform`, `transform-origin`, `perspective` |
| Inherited | No |
| Feedback | "Edit on canvas" switches to the Transform tool. The untransformed outline is drawn while a field is focused |

#### Visibility

| | |
|---|---|
| Simple | Shown / Hidden at this screen size, displayed as a row of screen-size icons, each toggleable, so "hide on mobile" is one click |
| Advanced | `visibility` (visible / hidden, keeps the space), `content-visibility`, "Hidden from screen readers" (`aria-hidden`), "Visually hidden but readable by screen readers" (applies the standard clip pattern) |
| Defaults | Shown everywhere |
| Supported | All |
| Output | `display: none` in the relevant screen size; `visibility` |
| Inherited | `visibility` yes; `display` no |
| Feedback | Layers eye icon mirrors the current screen size's value |

Showing an element again at a smaller size needs a display value. Daisy restores the element's own arrangement value from the base (`flex`, `grid`, `block`), never a blind `block`.

#### Transition

| | |
|---|---|
| Simple | "Animate changes" toggle with Duration and Feel (Smooth, Snappy, Gentle, Linear). Applies to all properties that change between states |
| Advanced | Per-property transitions list: property, duration, delay, easing with a cubic-bezier curve editor, `steps()`. `transition-behavior` |
| Defaults | Off. When the user first adds a Mouse over style, Daisy offers "Animate this change? 200 ms" as an inline suggestion (not automatic) |
| Supported | All |
| Output | `transition-property`, `transition-duration`, `transition-timing-function`, `transition-delay` on the Normal state |
| Inherited | No |
| Feedback | A play button previews the transition between Normal and the chosen state on the canvas |

#### Animation

| | |
|---|---|
| Simple | Add animation → choose what changes: Fade in, Move in (with direction), Scale in, Spin, or Custom. Duration, Delay, Repeat (Once / N times / Forever). Starts: When page loads / When scrolled into view |
| Advanced | Timeline panel with keyframes at any percentage and any properties per keyframe. Easing per keyframe. Direction, fill mode, play state. Multiple animations per element. Scroll-driven (`animation-timeline: view()` / `scroll()`). "Respect reduced motion" toggle (on by default) |
| Defaults | None |
| Supported | All |
| Output | `@keyframes <name> { … }` plus `animation-*` properties. "When scrolled into view" adds a `data-animate` attribute and a 15-line standalone script using `IntersectionObserver` (14.4). Reduced-motion wrapping via `@media (prefers-reduced-motion: no-preference)` |
| Inherited | No |
| Feedback | Play / pause / scrub on the canvas through the Timeline |

The choices in the simple list are starting keyframes for one element, each fully editable in the Timeline. They are not page templates.

#### Attributes

| | |
|---|---|
| Simple | Hidden for beginners by being collapsed; contains a plain key/value list of the element's HTML attributes with "Add attribute" |
| Advanced | `data-*` helper, boolean attribute toggles, "Copy selector" (`.box-3`), `id`, `title`, `tabindex`, `contenteditable`, `draggable`, `hidden`, `inert` |
| Defaults | Only what the element type needs |
| Supported | All |
| Output | Attributes on the tag |
| Inherited | No |
| Responsive | No |
| Feedback | Attribute names are validated; `on*` event attributes are accepted but flagged with a "runs script" tag and never active on the editing canvas |

#### Accessibility

| | |
|---|---|
| Simple | Only the questions relevant to this element, in plain words: image "Describe this image" (or "Decorative"); link / button "Name for screen readers" (only if it has no text); field "Label" (shows the associated label or offers to create one); heading "Level" with a note if a level is skipped; section "Landmark" |
| Advanced | `role`, `aria-label`, `aria-labelledby`, `aria-describedby`, `aria-hidden`, `aria-live`, `aria-expanded` and other state attributes, `tabindex`, focus order notes |
| Defaults | None |
| Supported | All |
| Output | `alt`, `aria-*`, `role` |
| Inherited | No |
| Responsive | No |
| Feedback | Inline warnings (missing description, contrast below 4.5:1 for text, empty link). A small warning dot on the group header and on the Layers row |

#### Custom CSS

| | |
|---|---|
| Simple | Collapsed. One sentence: "For anything the controls don't cover." |
| Advanced | A declarations editor (`property: value;` lines) with autocomplete and validation, scoped to this element, this screen size and this state. Below it, a "More selectors" list for pseudo-elements and custom suffixes (`::before`, `::after`, `::placeholder`, `:nth-child(2n)`, `> li`), each with its own declarations box |
| Defaults | Empty |
| Supported | All |
| Output | Declarations are merged into the element's rule. If a declaration's property is one a visual control understands, it *becomes* that control's value (there is one store, not two). Extra selectors emit `.class<suffix> { … }` |
| Inherited | Depends on the property |
| Feedback | Live. Invalid lines are underlined and not applied |

Decision: custom declarations are not a separate layer that fights the visual controls. Typing `padding-top: 20px` in Custom CSS and dragging the padding band are the same edit to the same stored declaration. This is what keeps the relationship between visual editing and code predictable.

### 6.5 States

The State selector in the Properties header lists: **Normal**, **Mouse over** (`:hover`), **Pressed** (`:active`), **Focused** (`:focus-visible`), and when relevant **Disabled**, **Checked**, **Visited**, **Placeholder text** (`::placeholder`). "Add custom…" accepts any selector suffix.

- Choosing a state makes the canvas show the element *in that state* and routes all edits to it. The options bar chip shows `Editing: Mouse over`.
- Only the differences are stored. Controls show the Normal value in muted text until overridden.
- States combine with screen sizes: a hover style can be set for Mobile only.
- Selecting another element returns the selector to Normal, so a state is never left on by accident.

---

## 7. Layout Engine

Daisy does not have its own layout engine. The browser lays out the page; Daisy's job is to give precise, visual control over the CSS that drives it. This chapter fixes exactly which CSS Daisy writes for each user action.

### 7.1 Default layout behaviour

**Decision: normal document flow is the default for everything.** A new element goes into its parent's flow at the insertion point. Nothing is absolutely positioned unless the user asks for it.

Reason: flow is what makes a page adapt to content and screen width. A design made of absolutely positioned boxes looks right at one width and breaks at every other. Daisy gives creative freedom through fast, visual control of flow (and a one-click escape to Free placement), not by abandoning it.

| Topic | Behaviour in Daisy |
|---|---|
| Page | `<body>` is a Stack. Its children are the sections, top to bottom |
| New section | `<section>`, a block: full width, height from content, `min-height: 400px`. Arrangement Stack |
| Block elements (`div`, `p`, headings, lists, `section`, `form`, …) | Take the full available width (Width: Fill) and the height of their content (Height: Fit content). Stack vertically in source order |
| Inline elements (`span`, `a`, `strong`, `em`) | Sit inside a line of text and wrap with it. They ignore width and height. Daisy shows them in Layers only when the "Show inline parts" toggle is on, and selects them with Direct Select |
| Inline-block elements (`button`, `input`, `select`, and `img` by default) | Sit on a line like text but accept width and height. Two buttons created one after another appear side by side, as on the web. Daisy sets `img` to `display: block` in its base stylesheet to avoid the baseline gap, so images stack |
| Default stacking | Later elements paint over earlier ones when they overlap. Layers lists elements in source order, first at the top. (This is the reverse of an image editor's layer stack; the Layers header says "Top of page ↑" to make it clear) |
| Width and height | Unset by default (`auto`). Drag-resizing writes pixel values. See Size (6.4) |
| Content sizing | Height always grows with content unless the user fixes it. If the user fixes a height and content exceeds it, the overflow is visible on the canvas and the Size group shows a warning: "Content is taller than this box" with choices Show / Cut off / Scroll / Remove fixed height |
| Parent-child | Every element has exactly one parent. A child is laid out by its parent's arrangement. Percent sizes refer to the parent's content box |
| Overflow | Visible by default |
| Nesting | Unlimited depth, subject to HTML validity rules (8.3) |
| Vertical margins | Adjacent vertical margins of blocks in a Stack collapse (the larger wins). The Spacing tool shows the collapsed result and tags the smaller band "merged with neighbour" |

**Flow versus positioned.** An in-flow element takes up space and pushes its neighbours. A Free (absolute) or Fixed element takes up no space; neighbours behave as if it were not there, and it is placed by distances from the edges of an anchor. Daisy shows the difference constantly: flow elements show insertion lines when dragged; free elements show pin lines to their anchor and a small "free" glyph on their name tag and Layers row.

### 7.2 Visual layout manipulation

Everything starts from one control on a container: **Arrange children**.

| Choice | CSS written | Children behave |
|---|---|---|
| Stack | `display: block` (removed if it is the tag's default) | Normal flow |
| Row → | `display: flex; flex-direction: row` | Side by side |
| Row ↓ (Column) | `display: flex; flex-direction: column` | Top to bottom, with alignment and gap control |
| Grid | `display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px` on first use | Fill cells in order |

**User actions and the CSS they produce**

| User action | CSS |
|---|---|
| Click Row in the options bar or Layout group | `display: flex` |
| Click the direction arrow on the canvas | toggles `flex-direction` |
| Click a dot in the 3 × 3 alignment grid (Row →: columns of the grid are main axis) | `justify-content` and `align-items` set to `flex-start` / `center` / `flex-end` |
| Choose Spread: Space between | `justify-content: space-between` |
| Drag a hatched gap bar | `gap` |
| Toggle Wrap | `flex-wrap: wrap` |
| Toggle "Grow to fill" on a child | child `flex-grow: 1; flex-basis: 0` |
| Drag a child in a Row | reorders the DOM (not the `order` property; `order` is an Advanced control because it separates visual order from reading order) |
| "Create columns": select a container, choose Grid, set Columns 3 | `grid-template-columns: repeat(3, 1fr)` |
| Drag a grid line | converts that template to an explicit list and changes the two adjacent tracks, keeping their units (`fr` stays `fr`, `px` stays `px`) |
| Click `+` after the last column badge | appends `1fr` to the template |
| Drag a child to another cell | child `grid-column-start` / `grid-row-start` |
| Drag a child's edge across cells | child `grid-column: 1 / span 2` |
| Use the alignment grid on a **Stack** | Stack cannot align blocks on both axes. Daisy changes the container to Row ↓ and applies the alignment, in one undo step, and says so in the status bar: "Changed to Column so children can be aligned" (principle P8) |
| Align buttons on a single flow child | child `align-self` in a Row or Grid; in a Stack, `margin-left/right: auto` (needs a non-Fill width; otherwise the control is disabled with the reason) |
| Switch Row to Grid or back | Only `display` and the properties of the new arrangement are written. Properties of the old one are kept but inactive, shown in Advanced with an "inactive" tag and a "Clean up" button. Switching back restores the previous setup |

**Layout read/write helpers.** All layout controls go through two functions so the tool, the options bar and the panel cannot disagree:

```ts
interface LayoutConfig {
  mode: 'stack' | 'row' | 'grid' | 'other';     // 'other' = a display value the simple UI does not model
  direction?: 'row' | 'column';
  reverse?: boolean;
  wrap?: boolean;
  justify?: string;                              // raw justify-content
  align?: string;                                // raw align-items
  gap?: { row: string; column: string };
  columns?: TrackList;                           // parsed grid-template-columns
  rows?: TrackList;
}
type TrackList = { raw: string; tracks: { size: string; repeat?: number }[]; editable: boolean };

function readLayout(effective: StyleDecls): LayoutConfig;          // CSS → config
function writeLayout(change: Partial<LayoutConfig>): StyleDecls;   // config change → minimal CSS
```

`TrackList.editable` is false when the template uses something the drag handles cannot represent safely (for example `subgrid` or line names). The canvas then shows tracks read-only and the Advanced text field remains the editor. Nothing is ever rewritten into a simpler form without the user asking.

**Complex layouts without templates.** A typical "navigation bar, two-column hero, three cards" page is built as: Section → Arrange: Row, Spread: Space between (logo box and a row of links). Section → Arrange: Grid, 2 columns (text box, image). Section → Arrange: Grid, 3 columns (three boxes). The user needs only the Box, Text and Media tools and the Arrange control.

### 7.3 Responsive design

**Model (Decision): desktop-first cascade with `max-width` media queries.**

- Every document has a **base** style set that applies at all widths, edited at the widest screen size ("Desktop").
- Each additional screen size has a maximum width. Default set: **Tablet** (`max-width: 1024px`), **Mobile** (`max-width: 640px`).
- A value set at Tablet applies to Tablet and everything narrower, unless Mobile sets its own.

Why desktop-first: the user starts designing on a wide desktop canvas, so "what I design first is the base, and smaller screens adjust it" matches what they see. A mobile-first option exists per document (below) for professionals who want it.

**Screen sizes dialog** (top bar `+`):

| Field | Meaning |
|---|---|
| Name | Shown in the selector |
| Applies up to (max width) | The media query boundary |
| Canvas width | The width the canvas uses when editing this size (default: Tablet 768, Mobile 390) |
| Icon | Monitor, tablet, phone, wide |

- Add custom screen sizes at any width. Add a **larger** one ("Wide", applies from 1600 px up) which uses `min-width` and sits above the base in the selector.
- Advanced: switch the document to **mobile-first**. Daisy then recomputes nothing silently; it shows a preview of how many values would move and requires confirmation, and creates a version first.
- Deleting a screen size asks what to do with its values: discard them, or merge them into the next narrower size.

**What happens when the user changes a property at one screen size**

1. The canvas is at Tablet. The options bar chip reads `Editing: Tablet and smaller`.
2. The user drags the heading's font size from 48 to 36.
3. Daisy writes `font-size: 36px` into the heading's **Tablet** declarations only. The base value `48px` is untouched.
4. The Size field's origin marker turns solid blue. Its tooltip reads "Set for Tablet and smaller. Desktop: 48px".
5. Switching to Desktop shows 48. Switching to Mobile shows 36 with a hollow marker: "From Tablet".

**Guarantees**

- An edit writes to the active screen size only. No other size's stored values are ever modified by it.
- Structure (which elements exist, their order, their text and attributes) is shared by all sizes. This is how the web works: one HTML document.
- If the user performs a *structural* edit while at a non-base size (adds, deletes, re-parents or reorders an element), Daisy shows a non-blocking notice the first time in each session: "Adding, removing and reordering elements applies to all screen sizes. To change order on this size only, use Visual order." Styles applied to a newly created element at a non-base size go to the base, because the element needs a starting appearance everywhere; the notice says so.

| Topic | Behaviour |
|---|---|
| Inherited styles | Shown with hollow markers and the source size in the tooltip |
| Overrides | Shown with solid markers. The Properties context strip counts them and can list or clear them |
| Reset an override | Right-click the label → Reset. The inherited value returns |
| Promote | Right-click → "Set for all sizes" moves the value to the base and removes the override |
| Visibility | Visibility group's per-size toggles write `display: none` at that size |
| Responsive typography | Set a different size per screen size, or use the fluid size helper (Typography → Advanced) to generate `clamp(min, preferred, max)` once at the base |
| Responsive spacing | Same: per-size values, or any fluid value typed in |
| Element reordering | "Visual order" control (Size → In row / In grid → Advanced → Order) writes `order` at that size. Daisy shows an accessibility note that reading order does not change |
| Flex and grid changes | Arrange children and all its values are ordinary per-size properties. A 3-column grid at the base can be 1 column at Mobile by setting Columns to 1 there |
| Preview | Preview mode has a draggable width handle and the same size selector, so in-between widths can be tested |
| Canvas | The canvas frame is really that width, so the browser's own media queries decide what applies. Daisy does not simulate the cascade |

Changing the canvas width by dragging the page's right edge is allowed for testing; the selector then shows the size whose range contains the current width.

### 7.4 Positioning and visual editing

| Placement | CSS | How the user edits it on the canvas | What Daisy guarantees |
|---|---|---|---|
| **In flow** | `position: static` (not written) | Drag reorders / re-parents. Resize changes size. Spacing tool adjusts its distance from neighbours | No offsets are ever written to a static element |
| **Nudged** (Advanced) | `position: relative; top; left` | Drag moves it visually from its flow position; a ghost outline shows the space it still occupies | Neighbours do not move. Offsets are relative to its own flow position |
| **Free** | `position: absolute` + offsets | Drag moves it. Pin lines show distances to the anchor. Resize works from any handle | See conversion rules below |
| **Fixed to screen** | `position: fixed` + offsets | Drag moves it within the "first screen" frame (the area from the page top to the fold line), which stands in for the browser window | Canvas rendering is an approximation (9.9); Preview shows the true behaviour |
| **Sticks when scrolling** | `position: sticky; top: 0` | It stays in flow, so drag reorders. A dashed line shows the stick distance, draggable to change `top`. A bracket shows the range (its parent) within which it will stick | Daisy warns if an ancestor has `overflow` set, which prevents sticking |

**Converting In flow → Free**

1. Measure the element's current border box relative to its anchor (the nearest ancestor that is positioned).
2. If the direct parent is not positioned, set `position: relative` on the parent so the parent becomes the anchor. This is reported ("Box 2 is now the anchor for Text 5") and is part of the same undo step.
3. Write `position: absolute; left: Xpx; top: Ypx; width: Wpx` where W is the measured width (an absolute element would otherwise shrink to its content). Height stays auto unless it was fixed.
4. The element does not visibly move. Its former neighbours close the gap, which is the true consequence and is visible immediately.

**Converting Free → In flow.** Remove `position` and all offsets. Insert the element in its parent's order at the position nearest to where it was visually. Keep the width.

**Pins.** A Free element stores offsets from the sides it is pinned to. The pin widget toggles each side:

| Pins | CSS written when dragged | Behaviour when the anchor resizes |
|---|---|---|
| Left + Top (default) | `left`, `top` | Stays at the same distance from top-left |
| Right + Top | `right`, `top` | Follows the right edge |
| Left + Right | `left`, `right`, no `width` | Stretches with the anchor |
| Centre (advanced) | `left: 50%; translate: -50% 0` | Stays centred |

Dragging always rewrites only the pinned sides, in their existing units. An element pinned by `right: 5%` stays in percent after a drag.

**Stack order.** "Bring forward" on a positioned element first tries to reorder among siblings; if the overlap involves elements in different parents, it sets `z-index`. The Placement group shows the numeric value in Advanced.

**Values Daisy cannot drag.** If an offset is an expression the drag cannot solve safely (for example `left: calc(50% - var(--w) / 2)`), the element is still selectable and resizable, but dragging shows a lock cursor and the message "Position uses a formula. Edit it in Placement, or replace it with a fixed value." with a "Replace" button. Daisy never overwrites a formula as a side effect of a drag.

---

## 8. HTML Element System

### 8.1 Rules

- Every element in a Daisy document is a standard HTML element. There are no Daisy-specific tags.
- Every element type is described by one entry in an **element registry**. Tools, the Elements panel, the Properties panel, validation and export all read the registry.

```ts
interface ElementTypeDef {
  type: string;                    // "heading"
  label: string;                   // "Heading"
  category: ElementCategory;
  tag: string;                     // default tag: "h2"
  altTags?: string[];              // allowed in the Kind dropdown: ["h1","h3","h4","h5","h6"]
  content: 'none' | 'text' | 'children' | 'text-and-inline' | 'raw';
  allowedChildren?: (childTag: string) => boolean;
  allowedParents?: (parentTag: string) => boolean;
  defaultAttrs: Record<string, string>;
  defaultStyles: StyleDecls;       // explicit starting CSS
  defaultSize?: { width: string; height: string };  // used on click-create
  create?: (ctx: CreateContext) => NodeSeed[];      // for compound elements (list, table)
  a11y: A11yRule[];
  icon: string;
}
```

### 8.2 Element library

Starting styles are deliberately minimal and always explicit, so nothing on the canvas depends on a particular browser's defaults.

**Structural**

| Element | Tag | Created by | Starting styles | Children | Accessibility | Export |
|---|---|---|---|---|---|---|
| Section | `section` | Section tool, + Add section | `min-height: 400px` | Anything | Should have a heading; else flagged as a suggestion | `<section class>` |
| Header / Footer / Main / Navigation / Article / Sidebar | `header`, `footer`, `main`, `nav`, `article`, `aside` | Section tool Kind, or General → Kind | as Section, without min-height when created inside another element | Anything | One `main` per page. `nav` needs a label if there is more than one | the tag |
| Box | `div` | Box tool | `width`, `height`, `background-color: #d9d9d9` | Anything | None | `<div class>` |
| Group | `div` | `Ctrl+G` | none | The grouped elements | None | `<div class>` |
| Divider | `hr` | Box tool variant | `border: 0; border-top: 1px solid #cccccc; margin: 0` | None | Decorative by default | `<hr class>` |

**Text**

| Element | Tag | Created by | Starting styles | Children | Accessibility | Export |
|---|---|---|---|---|---|---|
| Text | `p` | Text tool | `margin: 0` (font values inherited from the page) | Text and inline parts | None | `<p class>` |
| Heading | `h1`–`h6` (default `h2`) | Text tool variant | `margin: 0; font-weight: 700; line-height: 1.2`; size by level: 48, 32, 24, 20, 16, 14 px | Text and inline parts | One `h1` per page; levels should not skip. Warnings, never blocks | `<h2 class>` |
| Inline parts | `strong`, `em`, `span`, `a`, `br`, `code`, `sub`, `sup`, `mark`, `small` | Formatting during text editing | none (`span` gets a class only if it has styles) | Text and inline parts | None | inline tags |
| Quote | `blockquote` | Elements panel | `margin: 0` | Anything | Optional `cite` | `<blockquote>` |
| Preformatted / Code | `pre`, `code` | Elements panel | `margin: 0; font-family: monospace; white-space: pre-wrap` | Text | None | the tags |

**Media**

| Element | Tag | Created by | Starting styles | Children | Accessibility | Export |
|---|---|---|---|---|---|---|
| Image | `img` | Media tool, file drop, Assets drag | click: `max-width: 100%; height: auto`. drag: `width; height; object-fit: cover` | None | `alt` required: a description, or empty with "Decorative" | `<img src="assets/images/…" alt width height loading="lazy">` (intrinsic width/height attributes prevent layout shift) |
| Picture | `picture` > `source`, `img` | Media → More → Sources | as Image | `source`, `img` | as Image | the structure |
| Video | `video` | Media tool variant | `max-width: 100%` | `source`, `track` | Captions track suggested; autoplay requires muted | `<video controls src poster>` |
| Audio | `audio` | Media tool variant | none | `source` | Transcript suggested | `<audio controls src>` |
| Icon / SVG | inline `svg` or `img` | Media tool variant | `width: 24px; height: 24px` | None editable (SVG internals are kept as raw markup) | `aria-hidden="true"` if decorative; else a `<title>` | sanitised inline SVG or `<img>` |
| Figure | `figure` > content, `figcaption` | Elements panel | `margin: 0` | Anything plus one caption | Caption describes content | the tags |

**Links and buttons**

| Element | Tag | Created by | Starting styles | Children | Accessibility | Export |
|---|---|---|---|---|---|---|
| Link | `a` | Link tool, text formatting | text link: `color: inherit; text-decoration: underline`. Wrapper link: `display: block; color: inherit; text-decoration: none` | Anything except links, buttons and form controls | Needs discernible text or a screen-reader name | `<a href>`; new tab adds `rel="noopener"` |
| Button | `button` | Button tool | see 5.3 Button | Text and inline parts, images, icons | Needs text or a name. `type` always written | `<button type="button">` |

**Lists**

| Element | Tag | Created by | Starting styles | Children | Accessibility | Export |
|---|---|---|---|---|---|---|
| Bulleted / Numbered list | `ul` / `ol` > `li` | Place tool | `margin: 0; padding-left: 24px` | Only `li` (enforced) | None. If bullets are removed, `role="list"` is added for Safari | the tags |
| List item | `li` | `Enter` at the end of an item, or Layers "Add item" | none | Anything | None | `<li>` |
| Description list | `dl` > `dt`, `dd` | Elements panel | `margin: 0` | `dt`, `dd`, grouping `div` | None | the tags |

**Tables**

| Element | Tag | Created by | Starting styles | Children | Accessibility | Export |
|---|---|---|---|---|---|---|
| Table | `table` > `thead`/`tbody` > `tr` > `th`/`td` | Place tool (3 × 3) | `border-collapse: collapse; width: 100%`; cells `padding: 8px; border: 1px solid #cccccc; text-align: left` | Strict table structure (enforced) | Header cells get `scope`. Optional `caption` | the structure |

Table editing: selecting a table shows row and column headers on the canvas with `+` buttons and a right-click menu (insert, delete, make header). Cell styles are shared through the selectors `.table-1 th` and `.table-1 td` (stored as extra selectors on the table, see Custom CSS in 6.4) so a table is not hundreds of separate rules; an individual cell can still be styled on its own.

**Forms**

| Element | Tag | Created by | Starting styles | Children | Accessibility | Export |
|---|---|---|---|---|---|---|
| Form | `form` | Form tool variant | none | Anything except another form | None | `<form action method>` |
| Text field | `input` | Form tool | `padding: 8px 12px; border: 1px solid #999999; border-radius: 4px; font: inherit; width: 240px` | None | Must have a label (`for`/`id`) or an `aria-label` | `<input type name id>` |
| Text area | `textarea` | Form tool | as Text field plus `min-height: 96px; resize: vertical` | Text | Label | `<textarea>` |
| Dropdown | `select` > `option` | Form tool | as Text field | `option`, `optgroup` (edited in an options list, not on canvas) | Label | `<select>` |
| Checkbox / Radio | `label` > `input` + text | Form tool | label: `display: inline-flex; align-items: center; gap: 8px` | Fixed structure | Label is built in. Radios share a `name` | the structure |
| Label | `label` | Form tool variant, or automatic | `display: block` | Text and inline | `for` matches a field | `<label for>` |
| Field group | `fieldset` > `legend` | Elements panel | `border: 0; margin: 0; padding: 0` | Anything | Legend names the group | the tags |
| Submit button | `button type="submit"` | Button tool → More → type | as Button | as Button | as Button | `<button type="submit">` |

Daisy does not process form submissions. The Form's General group has an Action field (a URL) and explains: "Daisy designs the form. Sending it needs a service or server; paste its address here."

**Embeds and custom**

| Element | Tag | Created by | Behaviour in editor | Export |
|---|---|---|---|---|
| Embedded page | `iframe` | Media tool variant | Static placeholder showing the URL. Runs only in Preview | `<iframe src title loading="lazy">`; `title` is required |
| HTML block | `div` wrapping raw markup | Elements panel → Custom → HTML block | A code popover holds the markup. The canvas renders a sanitised copy (scripts and event attributes removed). Its internals are not individually selectable | The raw markup verbatim inside the wrapper |
| Custom element | any tag name containing a hyphen, or any tag typed in the Place tool | Place tool tag field | Rendered as an unknown element (acts like an inline box until given a display value; Daisy starts it with `display: block`) | The tag as typed. Its definition script goes in Page JavaScript |
| Details | `details` > `summary` | Elements panel | Rendered open in the editor so content is editable | `<details>` (closed unless `open` is set) |
| Dialog | `dialog` | Elements panel | Rendered open in the editor with a "dialog" badge | `<dialog>`; opening it needs custom JS or `popover` attributes, both available in Attributes |

### 8.3 Nesting rules

Validity is enforced when creating, dropping and pasting, by one function:

```ts
function canContain(parentTag: string, childTag: string, ancestors: string[]): { ok: boolean; reason?: string };
```

| Rule | Reason shown to the user |
|---|---|
| `img`, `input`, `hr`, `br`, `source`, `track` have no children | "Images can't contain other elements. Use a Box and put both inside." |
| `p` and headings contain only text and inline parts | "Text can't contain boxes." |
| `a` cannot contain `a`, `button`, or form controls | "A link can't contain another clickable element." |
| `button` cannot contain interactive elements | same |
| `ul` / `ol` contain only `li` | The dropped element is automatically wrapped in a new `li` (reported) |
| Table parts follow table structure | "Add rows and cells with the table controls." |
| `form` cannot contain `form` | "A form can't be inside another form." |
| `label` cannot contain `label` | same pattern |
| Sections stay at the top level of the page | A section dragged into a box is converted to a Box, with a notice |

When a drop is invalid, the insertion line turns red and the reason appears beside the pointer. Professionals can override most rules in Layers with `Alt+drop` ("Allow invalid nesting"), because browsers are forgiving and some advanced patterns need it; the element then carries a warning badge.

### 8.4 Accessibility checks

A single checker runs over the document model (not the DOM) and produces a list of issues with severity "needs attention" or "suggestion". It powers the Accessibility group's inline warnings, Layers badges, and the summary shown in the Export dialog. Checks: missing image description, empty link or button, field without a label, missing page title or language, more than one `h1`, skipped heading level, no `main` landmark, text contrast below 4.5:1, `iframe` without title, autoplaying media with sound. Export is never blocked by these.

---

## 9. Rendering and Canvas Architecture

### 9.1 Strategy

**Decision: the page is rendered as real DOM inside an `<iframe>`. The editor's selection graphics are drawn in a separate overlay in the editor window, on top of the iframe.**

Rejected alternatives:

| Alternative | Why rejected |
|---|---|
| Draw the page on an HTML canvas / WebGL | Would require re-implementing CSS layout and text. Can never match browsers exactly. Violates P3 and P6 |
| Render the page as DOM directly in the editor document | Editor CSS and page CSS would leak into each other; media queries would respond to the editor window, not the simulated width; no isolation |
| Draw selection graphics inside the iframe | They would be part of the page (affecting `:hover`, `nth-child`, overflow, stacking) and would scale with zoom |

### 9.2 Structure

```
Editor window (trusted)
└─ CanvasViewport            div, overflow hidden, receives all pointer and wheel events
   ├─ World                  div, transform: translate(panX, panY) scale(zoom), transform-origin 0 0
   │   └─ PageFrame          <iframe sandbox="allow-same-origin">, width = canvas width (CSS px),
   │                          height = page content height
   └─ Overlay                absolutely positioned SVG + a few HTML elements, NOT transformed:
                              outlines, handles, guides, bands, labels, insertion lines
```

There are two different frames in Daisy, with different security settings:

| Frame | Used for | Sandbox | Scripts | Editor can reach its DOM |
|---|---|---|---|---|
| **Edit frame** | The editing canvas | `sandbox="allow-same-origin"` | Never run | Yes, directly |
| **Preview frame** | Preview mode | `sandbox="allow-scripts"` (no `allow-same-origin`) | Run | No. Messages only |

The edit frame can be same-origin *because* nothing executes in it. The preview frame executes user code, so it is isolated. Chapter 13 covers this in full.

### 9.3 From document to DOM

A `CanvasRenderer` class (plain TypeScript, not React) owns the edit frame's DOM.

- **Initial render:** walks the document model and creates elements with `document.createElement`, never by parsing HTML strings. Each element gets its `class` and a `data-d-id` attribute with its node id. It keeps a `Map<NodeId, HTMLElement>` and a `WeakMap<HTMLElement, NodeId>`.
- **Styles:** one `<style>` element in the frame's head holds a stylesheet generated by the same CSS generator that export uses (chapter 11). The renderer keeps a `Map` from `(nodeId, screen size, state)` to the live `CSSStyleRule` object, so a single value change is one `rule.style.setProperty()` call.
- **Updates:** the store emits patches for every change (10.6). The renderer translates each patch into the smallest DOM operation: set a style property, set or remove an attribute, set text, insert, remove or move a node. There is no full re-render during editing.
- **Attribute allow-list:** in the edit frame the renderer does not set `on*` attributes, does not set `javascript:` URLs, does not create `<script>` elements, and renders `<iframe>` elements as placeholders. These things exist in the model and in export; they are simply not materialised on the editing canvas.

**Mapping in both directions**

- Selection → DOM: `nodeMap.get(id)`.
- DOM → document: from any element, walk up to the nearest ancestor with `data-d-id`, then `WeakMap` lookup. Children of an HTML block or inline SVG resolve to their wrapper.

### 9.4 Pointer interaction

All pointer events are handled by `CanvasViewport` in the editor window. The iframe never receives pointer events during normal editing (`pointer-events: none` on the iframe), so links do not navigate, buttons do not press and inputs do not focus.

**Hit testing**

```ts
function hitTest(clientX: number, clientY: number): NodeId[] {
  const r = pageFrame.getBoundingClientRect();           // already includes pan and zoom
  const x = (clientX - r.left) / zoom;                   // page CSS pixels
  const y = (clientY - r.top) / zoom;
  return frameDoc.elementsFromPoint(x, y)                 // front-to-back
    .map(el => idOf(el)).filter(Boolean).filter(unique);
}
```

Because the frame is as tall as the page and never scrolls internally, page coordinates equal frame viewport coordinates. The active tool decides which id in the returned list to use (Select applies the scope rule; Direct Select takes the first; locked elements are skipped).

**Tool dispatch.** Each tool implements one interface. `CanvasViewport` forwards normalised events to the active tool.

```ts
interface Tool {
  id: ToolId;
  cursor(ctx: ToolContext): string;
  onPointerDown?(e: CanvasPointerEvent, ctx: ToolContext): void;
  onPointerMove?(e: CanvasPointerEvent, ctx: ToolContext): void;
  onPointerUp?(e: CanvasPointerEvent, ctx: ToolContext): void;
  onKeyDown?(e: KeyboardEvent, ctx: ToolContext): boolean;   // true = handled
  onCancel?(ctx: ToolContext): void;
  overlay?(ctx: ToolContext): OverlayItem[];                 // what to draw
  optionsBar: React.ComponentType;
}
interface CanvasPointerEvent { page: Point; screen: Point; hits: NodeId[]; buttons: number;
                               shift: boolean; alt: boolean; ctrl: boolean; }
```

A drag starts after the pointer moves 3 screen pixels. Pointer capture is taken on `CanvasViewport` so drags continue outside it.

### 9.5 Measurement

All geometry comes from the browser, never from Daisy's own calculation of layout.

| Need | Source |
|---|---|
| Element box (for outlines and handles) | `el.getBoundingClientRect()` in the frame, then `screen = rect × zoom + frameOrigin` |
| Padding, border, margin bands | `getComputedStyle(el)` used values, applied to the border box |
| Content box of a parent (for percent conversion and snapping) | border box minus computed border and padding |
| Flex gaps | Difference between adjacent children's rects along the main axis |
| Grid tracks | `getComputedStyle(el).gridTemplateColumns` / `Rows`, which the browser returns as resolved pixel sizes, plus computed gaps and the container's content box |
| Text caret position | The browser (native editing) |
| Transformed elements | The oriented box is computed from `offsetWidth` / `offsetHeight` and the accumulated `transform` matrices (`DOMMatrix`) of the element and its ancestors |

**Layout synchronisation.** The overlay must be redrawn whenever layout might have changed:

1. After the renderer applies patches, it schedules one `requestAnimationFrame` measurement pass.
2. A `ResizeObserver` on the frame's `<body>` and on currently selected and hovered elements catches changes caused by content (image loads, font loads, wrapping).
3. `document.fonts` `loadingdone` and image `load` events trigger a pass.
4. Pan and zoom changes trigger a redraw without re-measuring (rects are cached in page coordinates).

In each pass all reads happen first, then all overlay writes, so there is at most one forced layout per frame. Only elements the overlay needs (selection, hover, drag targets, current container's children) are measured, never the whole page.

The frame's height is kept equal to the page's content height by observing `<body>`; this is what lets the whole page be visible and pannable without internal scrolling.

### 9.6 Drag and resize calculations

**Resize.** On pointer down, record the start rect and the element's current width and height declarations. On each move:

1. Convert the pointer delta to page pixels (`delta / zoom`).
2. Compute the new border-box size from the handle direction, applying `Shift` (proportion) and snapping.
3. Convert to the stored unit: if the existing value is in `%`, divide by the parent's content box; if `rem`, by the root font size; otherwise `px`. (Option "Resize keeps unit" off = always `px`.)
4. Dispatch one `setStyles` command inside the open transaction. The renderer applies it; the browser lays out; the overlay re-measures.

For a **flow** element, any handle changes size only; where the element ends up is decided by layout (a centred element grows from both sides, which the user sees live). For a **free** element, the left and top handles also adjust the pinned offsets so the opposite edge stays still.

If the element's measured size does not follow the pointer (because a max-width, a shrinking row, or a grid track is controlling it), the size label shows the real size and a one-line reason, and the handle shows a "limited" cursor. Daisy does not fight the layout.

**Flow drag (reorder / re-parent).** While dragging:

1. Hit-test to find the innermost valid container under the pointer (`canContain` must pass; the dragged subtree is excluded).
2. Read the container's arrangement to get its main axis.
3. Among the container's in-flow children, find the insertion index by comparing the pointer to each child's midpoint along the main axis (per line, for wrapped rows and grids).
4. Draw the insertion line at that gap and outline the container.
5. On drop, dispatch one `moveNode` command.

**Free drag.** New offsets = start offsets + delta, expressed for the pinned sides and in their units, then adjusted by the snapping engine, which compares the moving rect's edges and centres with the cached rects of siblings and the anchor.

### 9.7 Text editing

Decision: text is edited with the browser's own editing (`contenteditable`) inside the edit frame, and the result is parsed back into the model.

1. On entering edit mode, the renderer sets `contenteditable="true"` on the text element, makes the iframe accept pointer events, focuses it and places the caret at the click point (`caretPositionFromPoint` / `caretRangeFromPoint`).
2. Listeners attached from the editor window handle `beforeinput`, `input`, `keydown`, `paste` and `blur` on the frame document.
3. `beforeinput` is used to block or redirect anything that would create markup outside the allowed inline set. Formatting commands (bold, italic, link) are performed by Daisy on the selection range, not by the browser's `execCommand`.
4. Paste is always converted: plain text by default; "keep basic formatting" maps to the allowed inline tags only.
5. After each `input`, the element's child nodes are read and converted to model nodes (text nodes and allowed inline elements; everything else is unwrapped to its text). The result is committed with a `setInlineContent` command, grouped into one history entry per typing burst (12.1).
6. `Esc` or clicking outside ends editing, removes `contenteditable`, and re-renders the element from the model so the DOM is exactly what the model says.

### 9.8 Zoom, pan and viewport simulation

- Zoom and pan are a CSS transform on `World`. The frame itself always lays out at 100%, so layout is identical at every zoom level.
- The overlay is not transformed; it converts page coordinates to screen coordinates itself. Outlines stay 1.5 px and handles stay 8 px at any zoom.
- Wheel zoom keeps the page point under the pointer fixed: `pan' = pointer − (pointer − pan) × (zoom' / zoom)`.
- Changing screen size sets the frame's width to that size's canvas width. Real media queries in the generated stylesheet then apply. Nothing else changes.
- The device pixel ratio is the user's own; Daisy does not emulate DPR.

### 9.9 Canvas versus export: the complete list of differences

The editing canvas and the exported page use the same HTML structure, the same class names and the same generated CSS. The differences are limited to this list. Adding to it requires a written reason.

| # | Difference in the edit frame | Why | Effect on fidelity |
|---|---|---|---|
| 1 | `data-d-id` attribute on every element | Mapping | None |
| 2 | Scripts, event attributes and `javascript:` URLs are not materialised; iframes and HTML-block scripts are placeholders | Safety and stable editing | Script-driven content appears only in Preview |
| 3 | An editor stylesheet sets `animation: none !important` and `transition: none !important`, except on an element being previewed from the Timeline | Elements must be measurable and visible while editing | Animations are seen in Timeline playback and Preview |
| 4 | State rules get an extra selector so a state can be shown without a real pointer: `.btn:hover, .btn[data-d-state~="hover"]` | Editing states | None |
| 5 | `vh`, `svh`, `lvh`, `dvh` units are generated as `calc(var(--d-vh) * N)` where `--d-vh` is 1% of the simulated window height | The frame is as tall as the page, so real `vh` would be wrong | Numerically identical to a window of the simulated height |
| 6 | `position: fixed` elements are rendered as absolutely positioned inside a box representing the first screen | Same reason | Approximation; badge on the element; true behaviour in Preview |
| 7 | `details` and `dialog` are forced open | So their content can be edited | Open/closed state follows the attribute in export |
| 8 | `pointer-events` is forced to `auto` for hit testing | Elements with `pointer-events: none` must stay selectable | None (pointer events never reach the page while editing) |
| 9 | Media `autoplay` is ignored | Stability | Plays in Preview |

Empty-element outlines, hidden-element indicators and every other editing aid are drawn in the overlay and never in page CSS.

**Preventing drift.** The CSS generator has one implementation with a `target: 'edit' | 'export'` flag that controls only items 4–6. An automated test (chapter 17) renders every test document both ways and compares element geometry.

### 9.10 CSS that visual controls cannot manipulate

| Situation | Handling |
|---|---|
| A property with no dedicated control | Listed under "Other properties" in its owning group (or in Custom CSS if no group owns it) as an editable name/value row |
| A value a control cannot represent (`clamp()`, `calc()`, `var()`, `min()`) | The control shows the raw text with a "custom" tag. Still editable as text. Handles and bands still display the *computed* result |
| A value a drag cannot safely rewrite | Drag is disabled for that property with an explanation and a "Replace with fixed value" option (7.4) |
| Pseudo-elements, complex selectors | Custom CSS → More selectors |
| At-rules other than screen sizes (`@supports`, `@container`, `@font-face`, `@layer`) | Page CSS in the Code panel |
| Anything set in Page CSS that affects an element | The Properties panel shows a note "Also styled by Page CSS" when the computed value differs from Daisy's generated value for a property the user is hovering |

### 9.11 Performance

| Technique | Detail |
|---|---|
| Patch-based rendering | A style change is one CSSOM call; a move is one `insertBefore` |
| One transaction per gesture | A drag updates the model on each pointer move (throttled to animation frames) but produces one history entry |
| Minimal measurement | Only overlay-relevant elements, once per frame |
| Overlay in SVG | Few nodes (tens), redrawn from state |
| Virtualised Layers | Only visible rows exist in the DOM |
| Derived data memoised | Effective styles per element/size/state are cached and invalidated by patch path |
| Lazy modules | Code editor, Timeline, export and zip code load on first use |
| Asset handling | Images are shown through object URLs, never data URLs, in the edit frame; large images get a downscaled thumbnail for the Assets panel |

Budgets (enforced by tests in chapter 17): open a 2,000-element document in under 1 s; drag and resize at 60 fps on a 2,000-element page on a mid-range laptop; a single property edit reflected on canvas in under 16 ms; memory stable over 500 undo steps.

---

## 10. Document and Data Architecture

### 10.1 Source of truth

**Decision: one normalised, JSON-serialisable document object held in the store is the only source of truth.** The edit frame's DOM, the Layers panel, the Properties panel, the preview and the export are all derived from it. The DOM is never read to find out what the document *is*; it is read only to find out where things *are* (measurement) and, during text editing, what the user typed (which is immediately written back to the model).

**Decision: styles are stored as real CSS declarations**: longhand property names in kebab-case mapped to value strings exactly as they will appear in the stylesheet. There is no abstract style schema.

Why: any CSS that exists or will exist is representable with no schema change; controls become small read/write adapters over CSS; exported code is predictable because it *is* the stored data; and the professional's custom CSS and the beginner's dragged values are literally the same records.

### 10.2 Core types

```ts
// ---------- identifiers ----------
type NodeId = string;          // nanoid(10), unique within a document
type PageId = string;
type AssetId = string;         // content hash (SHA-256, first 16 hex chars)
type BreakpointId = string;    // "base" is reserved

// ---------- document ----------
interface DaisyDocument {
  schemaVersion: number;                       // for migrations
  id: string;
  name: string;
  createdAt: number;
  updatedAt: number;
  settings: DocumentSettings;
  breakpoints: Breakpoint[];                   // excluding the implicit base
  tokens: Token[];                             // colours and text values → CSS custom properties
  fonts: FontSource[];
  assets: Record<AssetId, AssetMeta>;          // metadata only; bytes live in the asset store
  keyframes: Record<string, KeyframesDef>;     // by animation name
  pages: Page[];                               // first version of the UI uses pages[0] only
  nodes: Record<NodeId, DNode>;                // every node of every page, flat
  customCode: CustomCode;
  guides: Guide[];                             // editor-only ruler guides
}

interface DocumentSettings {
  cascade: 'desktop-first' | 'mobile-first';
  baseCanvasWidth: number;                     // 1440
  simulatedViewportHeight: number;             // 900
  classPrefix: string;                         // "" by default
}

interface Breakpoint {
  id: BreakpointId;
  name: string;                                // "Tablet"
  query: { type: 'max-width' | 'min-width'; px: number };
  canvasWidth: number;                         // 768
  icon: 'wide' | 'desktop' | 'tablet' | 'phone';
}

// ---------- page ----------
interface Page {
  id: PageId;
  name: string;                                // "Home"
  fileName: string;                            // "index.html"
  rootId: NodeId;                              // the <body> node
  meta: { title: string; description: string; lang: string;
          favicon?: AssetId; socialImage?: AssetId };
}

// ---------- nodes ----------
type DNode = ElementNode | TextNode;

interface NodeBase {
  id: NodeId;
  parent: NodeId | null;                       // null only for a page's body node
}

interface TextNode extends NodeBase {
  type: 'text';
  value: string;
}

interface ElementNode extends NodeBase {
  type: 'element';
  elementType: string;                         // registry key: "section", "box", "text", "image", ...
  tag: string;                                 // "section", "div", "p", "img", ...
  name: string;                                // layer name: "Hero title"
  className: string;                           // generated from name, unique: "hero-title"
  extraClasses: string[];
  attrs: Record<string, string>;               // real HTML attributes (boolean attrs use "")
  children: NodeId[];                          // ordered; element and text nodes
  styles: ResponsiveStyles;                    // the element's own rule
  extraRules: ExtraRule[];                     // suffix selectors: "::before", " > li", ":nth-child(2n)"
  rawHtml?: string;                            // only for HTML blocks and inline SVG
  locked: boolean;                             // editor-only
  motion?: MotionTrigger;                      // "on scroll into view" trigger settings
}

// A Section is not a separate kind of object. It is an ElementNode whose parent is the body node.
type SectionNode = ElementNode & { tag: 'section' | 'header' | 'footer' | 'main' | 'nav' | 'article' | 'aside' | 'div' };
```

**Parent and child references.** Each node stores its `parent` id and, for elements, an ordered `children` id array. Both directions are stored because both are read constantly (walk up for breadcrumbs and anchors; walk down for rendering). They are kept consistent by allowing structural changes only through four commands (`insertNode`, `removeNode`, `moveNode`, `replaceChildren`), and a development-mode invariant check runs after every transaction:

- every id in `children` exists and has `parent` equal to this node;
- every node except page roots has a parent that lists it exactly once;
- there are no cycles; every node is reachable from exactly one page root;
- a body node's children are all elements.

### 10.3 Styles, responsive styles and states

```ts
type StyleDecls = Record<string, string>;      // { "padding-top": "24px", "color": "var(--ink)" }

/** "" is the normal state. Others are selector suffixes appended to the class. */
type StateKey = '' | ':hover' | ':active' | ':focus-visible' | ':focus' | ':disabled'
              | ':checked' | ':visited' | '::placeholder' | (string & {});

type StateStyles = Partial<Record<StateKey, StyleDecls>>;

/** Keyed by "base" and by each breakpoint id. Missing keys mean "nothing set there". */
type ResponsiveStyles = Record<BreakpointId, StateStyles>;

interface ExtraRule {
  id: string;
  suffix: string;                              // appended to ".className": "::before", " > li"
  styles: ResponsiveStyles;
}
```

Example: a heading that is 48 px, 36 px on tablet and smaller, and blue on hover:

```ts
styles: {
  base:   { '': { 'font-size': '48px', 'font-weight': '700', 'margin-top': '0px' },
            ':hover': { 'color': '#2f80ed' } },
  tablet: { '': { 'font-size': '36px' } },
}
```

**Normalisation rules** (applied by the `setStyles` command, in this order):

1. Property names are lower-cased. Vendor prefixes and custom properties (`--x`) are kept as typed.
2. Shorthands are expanded to longhands using the browser: the value is assigned to a detached element's `style` and the resulting longhands are read back. So `padding: 8px 16px` is stored as four entries. Shorthands that cannot be expanded reliably when they contain `var()` are stored as typed and flagged `opaque`; the related visual controls then show them as custom values.
3. Values are trimmed; a value of empty string removes the declaration.
4. Values are validated with `CSS.supports`. Invalid values are rejected.
5. Zero lengths are stored as `0px` for lengths (so unit fields behave), colours are stored as typed.

**Effective styles.** What an element "has" at a given screen size and state is computed, never stored:

```ts
function effectiveDecls(el: ElementNode, bp: BreakpointId, state: StateKey, doc: DaisyDocument): {
  decls: StyleDecls;
  origin: Record<string, { bp: BreakpointId; state: StateKey }>;   // where each value comes from
};
```

It merges, in cascade order, the base and each breakpoint that applies at `bp`'s canvas width, normal state first and then the requested state. The `origin` map drives the origin markers in the Properties panel.

### 10.4 Layout, attributes, tokens, assets, code

```ts
// Layout is not stored separately. LayoutConfig (7.2) is a read model derived from StyleDecls.

interface Token {
  id: string;
  kind: 'color' | 'font-family' | 'font-size' | 'length' | 'other';
  name: string;                                // "Brand"
  cssName: string;                             // "--brand"
  value: string;                               // "#2f80ed"
  group?: string;                              // "Text styles/Heading"
}

interface FontSource {
  id: string;
  family: string;                              // "Inter"
  kind: 'system' | 'uploaded' | 'remote';
  faces: { weight: string; style: 'normal' | 'italic'; asset?: AssetId; url?: string }[];
  fallback: string;                            // "system-ui, sans-serif"
}

interface AssetMeta {
  id: AssetId;
  kind: 'image' | 'video' | 'audio' | 'font' | 'file';
  fileName: string;                            // export name, unique within the document
  mime: string;
  bytes: number;
  width?: number; height?: number; duration?: number;
  createdAt: number;
}

interface KeyframesDef {
  name: string;                                // "fade-in-1"
  steps: { offset: number; decls: StyleDecls; easing?: string }[];   // offset 0..100
}

interface MotionTrigger { type: 'load' | 'in-view'; threshold: number; once: boolean; }

interface CustomCode {
  css: string;                                 // appended after generated CSS
  headHtml: string;                            // inserted at the end of <head>
  scripts: CustomScript[];
}
interface CustomScript {
  id: string;
  name: string;                                // "main.js"
  placement: 'head' | 'body-end';
  kind: 'inline-file' | 'external-url';
  code?: string;
  url?: string;
  attrs: { defer?: boolean; async?: boolean; module?: boolean };
  enabled: boolean;
}

interface Guide { axis: 'x' | 'y'; position: number; }
```

In styles and attributes, an asset is referenced by a stable URL form: `daisy-asset://<AssetId>`. The edit renderer resolves it to an object URL; export resolves it to a relative file path. Because references are plain strings in a known form, "where is this asset used" is a simple scan.

### 10.5 Editor state

Editor state is everything that is not part of the document. It is kept in a separate store slice and is never undoable (except selection, which is restored by undo for orientation).

```ts
interface Selection {
  ids: NodeId[];                               // in selection order; last is the "key" element
  scopeId: NodeId;                             // current drill-in scope (3.4)
  textEdit?: { nodeId: NodeId };               // set while editing text
}

interface EditorState {
  docId: string;
  pageId: PageId;
  tool: { active: ToolId; variant: Record<ToolId, string>; locked: boolean;
          options: Record<ToolId, unknown> };
  selection: Selection;
  hoverId: NodeId | null;
  breakpoint: BreakpointId;                    // where edits are written
  state: StateKey;                             // which state edits are written to
  viewport: { zoom: number; panX: number; panY: number };
  mode: 'edit' | 'preview';
  gesture: GestureState | null;                // live drag / resize / draw info for the overlay
  panels: { leftTab: 'layers' | 'elements' | 'assets'; rightTab: 'swatches' | 'history';
            drawer: 'closed' | 'code' | 'timeline'; leftWidth: number; rightWidth: number;
            collapsedGroups: Record<string, boolean>; advancedOpen: Record<string, boolean> };
  save: { status: 'saved' | 'saving' | 'error'; lastSavedAt: number | null; error?: string };
  clipboard: ClipboardPayload | null;
}
```

`panels`, tool options and theme are user preferences and persist in `localStorage`. Viewport and selection persist per document so reopening returns to the same place.

### 10.6 Commands and history operations

All document changes go through **commands**. A command is a plain function that mutates an Immer draft of the document. The store wraps it to capture patches.

```ts
// Low-level commands (the only code allowed to touch doc.nodes structure or styles)
insertNode(parentId, index, subtree: NodeSeed)
removeNode(id)
moveNode(id, newParentId, index)
replaceChildren(id, children: NodeSeed[])            // used by text editing
setStyles(id, bp, state, decls: StyleDecls)          // "" value removes a property
setExtraRuleStyles(id, ruleId, bp, state, decls)
setAttrs(id, attrs: Record<string, string | null>)   // null removes
setNodeProps(id, { name?, tag?, className?, locked?, ... })
setDocProps(...), setToken(...), setBreakpoint(...), setKeyframes(...), setCustomCode(...)

// Store API
interface DocStore {
  doc: DaisyDocument;
  run(label: string, fn: (d: Draft<DaisyDocument>) => void): void;   // one history entry
  begin(label: string): void;                                        // open a transaction
  commit(): void;                                                    // close → one history entry
  rollback(): void;                                                  // cancel (Esc during drag)
  undo(): void;
  redo(): void;
}

interface HistoryEntry {
  id: number;
  label: string;                          // "Resize Box 3", shown in menus and the History panel
  patches: Patch[];                       // Immer patches: forward
  inverse: Patch[];                       // Immer patches: backward
  selectionBefore: Selection;
  selectionAfter: Selection;
  breakpoint: BreakpointId;               // editor returns to where the change was made
  state: StateKey;
  time: number;
}
```

Higher-level actions (group, duplicate, convert to Free, wrap in link) are compositions of low-level commands inside a single `run`, so they are one undo step automatically.

The renderer, the autosave and the Layers panel subscribe to the patch stream rather than diffing the document.

---

## 11. CSS Generation

### 11.1 One generator

```ts
function generateCss(doc: DaisyDocument, page: Page, opts: {
  target: 'edit' | 'export';
  minify?: boolean;
  assetUrl: (id: AssetId) => string;
}): string;
```

The same function output is used by the edit frame, the preview and the export. `target` affects only the three items listed in 9.9 (forced-state selectors, `vh` rewriting, fixed positioning).

### 11.2 Output order

```
1. Base stylesheet            (fixed, 11.6)
2. @font-face rules           (uploaded fonts in use)
3. :root { tokens }           (custom properties)
4. body rule                  (page background and base text)
5. Element rules, base        (document order; each element: normal state, then states,
                               then its extra rules)
6. @keyframes                 (those referenced)
7. One @media block per breakpoint, in cascade order
     desktop-first: min-width breakpoints ascending, then max-width breakpoints descending
     inside each block: same order as step 5
8. Reduced-motion block       (if any animation opts in)
9. Custom page CSS            (verbatim)
```

Because every element rule is a single class selector, all generated rules have the same specificity, and the cascade is decided purely by order. That makes the result easy to reason about: later screen sizes override earlier ones, and custom page CSS, coming last, can override anything with an equal-specificity selector.

### 11.3 Selectors and class names

- Each element's rule is `.className`. `className` is the layer name converted to kebab-case, restricted to `[a-z0-9-]`, prefixed with `el-` if it would start with a digit, and made unique in the document by appending `-2`, `-3`, …. "Hero Title" → `.hero-title`.
- Renaming a layer renames the class, unless the user has edited the class by hand (then it is "detached" and kept). References in custom page CSS and scripts are *not* rewritten; Daisy warns if the old name appears there.
- Elements with no styles and no extra classes get no `class` attribute in export.
- State selectors append the state key: `.cta:hover`. States are emitted in a fixed order so later ones win as authors expect: normal, `:visited`, `:hover`, `:focus`, `:focus-visible`, `:active`, `:disabled`, `:checked`, then pseudo-elements, then custom suffixes in creation order.
- Nesting in HTML does not create nested or descendant selectors. Every rule is flat. (Only extra rules such as `.list-1 > li` use combinators, because the user wrote them.)

### 11.4 Property mapping, units and inheritance

| Topic | Rule |
|---|---|
| Property mapping | None needed. Stored declarations are emitted as `property: value;` |
| Shorthand collapsing | On export, complete longhand sets with compatible values are collapsed: four paddings → `padding`, four margins → `margin`, border sides when identical → `border`, radii → `border-radius`, `overflow-x/y` → `overflow`, gaps → `gap`, `inset`, flex and grid placement pairs. A set is only collapsed when all its members are present in the same rule, so a collapse can never reset a value inherited from another screen size |
| Property order inside a rule | Fixed and grouped: position, display and layout, size, spacing, typography, fill, border, effects, transform, transition, animation, others alphabetically |
| Units | Emitted as stored. `0px` is written as `0`. No unit conversion at export |
| Inheritance | Not flattened. If a section sets `color`, children do not get their own `color` declarations. The Properties panel explains inherited values; the stylesheet stays small |
| Tokens | `:root { --brand: #2f80ed; }` and uses are `var(--brand)`. A token that is unused is still exported (it is part of the design); an option removes unused ones |
| Asset URLs | `daisy-asset://id` → `url("../assets/images/hero.jpg")` relative to the CSS file |
| Empty rules | Skipped |
| Identical rules | Not merged by default (one element = one rule keeps the output predictable and diff-friendly). Export option "Merge identical rules" groups selectors |
| Minify | Optional. Off by default; the default output is formatted with two-space indentation |

### 11.5 Responsive and state output example

```css
.hero-title {
  margin: 0;
  font-size: 48px;
  font-weight: 700;
}
.hero-title:hover {
  color: #2f80ed;
}

@media (max-width: 1024px) {
  .hero-title {
    font-size: 36px;
  }
}
```

### 11.6 Base stylesheet

A fixed, short block, identical in canvas and export, so pages do not depend on browser-specific defaults:

```css
*, *::before, *::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; }
img, video, svg { display: block; }
h1, h2, h3, h4, h5, h6, p, figure, blockquote, dl, dd, pre { margin: 0; }
button, input, select, textarea { font: inherit; color: inherit; }
```

Everything else an element needs is written as explicit, visible, editable declarations on that element when it is created (8.2). The base stylesheet is not editable in the UI; anything in it can be overridden per element or in Page CSS.

---

## 12. Undo, Redo and Persistence

### 12.1 History

| Topic | Design |
|---|---|
| Unit | One `HistoryEntry` per user-meaningful action (10.6) |
| Individual operations | `store.run(label, fn)` records one entry |
| Grouped operations | `begin` … many commands … `commit` records one entry containing all patches, with consecutive patches to the same path compressed to the last one |
| Drag grouping | Pointer down → `begin("Move Box 3")`; each pointer move runs commands inside the transaction; pointer up → `commit`; `Esc` → `rollback` (applies the inverse patches and discards) |
| Text editing grouping | Typing extends the current entry while the pause between keystrokes is under 1 s and the caret has not jumped. A pause, a formatting command, or leaving edit mode starts a new entry. Leaving text editing with no change records nothing |
| Field scrubbing and sliders | Same as drag: one entry from pointer down to up |
| Coalescing repeated edits | Two consecutive entries with the same label, target and property within 1 s (arrow-key stepping in a field, nudging) are merged |
| Undo | Apply `inverse`, restore `selectionBefore`, switch the editor to the entry's screen size and state, scroll the affected element into view if off-screen, move the pointer in the stack |
| Redo | Apply `patches`, restore `selectionAfter` |
| New action after undo | Discards the redo tail |
| Limit | 300 entries or 50 MB of patch data, whichever comes first; oldest dropped |
| What is not in history | Selection changes on their own, zoom, pan, tool changes, panel state, screen size switching |
| Asset changes | Uploading an asset is not undoable (the bytes stay in the store); the element that uses it is. Unused assets are cleaned up only by explicit user action |
| Persistence of history | The undo stack lives for the session. It is not saved. Long-term safety comes from versions (12.5) |

### 12.2 Storage layout

> **Superseded (2026-11-13):** projects are folders on disk, not IndexedDB — see `docs/adr/0005-projects-are-folders-on-disk.md` and `docs/architecture/PROJECT_FORMAT.md`. Timings and recovery behaviour in 12.3–12.4 still apply.


**Decision: IndexedDB, accessed through the small `idb` wrapper.** No server.

| Object store | Key | Value |
|---|---|---|
| `documents` | doc id | `{ id, name, createdAt, updatedAt, thumbnail: Blob, sizeBytes, deletedAt? }` for the Home list |
| `docData` | doc id | The serialised `DaisyDocument` (structured clone of the plain object) |
| `assets` | `docId + ":" + assetId` | `{ blob: Blob, meta }` |
| `versions` | auto id, indexed by doc id | `{ docId, time, label, kind: 'auto' or 'manual', data: DaisyDocument }` |
| `session` | doc id | `{ openedAt, cleanClose: boolean, tabId }` for crash detection |

Assets are stored once per document by content hash, so uploading the same file twice does not duplicate it. Documents reference assets by id only; the JSON never contains binary data.

On first save Daisy calls `navigator.storage.persist()` to ask the browser not to evict the data, and shows the remaining quota (`navigator.storage.estimate()`) in Home.

### 12.3 Autosave

1. Every committed history entry marks the document dirty and schedules a save 800 ms later (debounced; forced after at most 5 s of continuous editing).
2. A save writes `docData` and updates `documents` in one IndexedDB transaction. Assets are written at upload time, not during saves.
3. Saves are also triggered on `visibilitychange` to hidden and on `pagehide`.
4. The top bar shows "Saving…" then "Saved". If a write fails (quota, private mode), it shows a persistent red "Not saved" with a "Save a copy to disk" button, and editing continues in memory.
5. The thumbnail for Home is regenerated at most once a minute while idle.

One document is open per browser tab. If the same document is opened in a second tab, the second tab opens read-only with a notice (detected with the Web Locks API), which avoids silent overwrites without building a merge system.

### 12.4 Recovery after unexpected closure

- When a document opens, `session.cleanClose` is set to `false`. It is set to `true` on a normal close (`pagehide` after a successful save, or returning to Home).
- If Daisy starts and finds a session with `cleanClose: false` that no live tab holds a lock for, it reopens that document and shows: "Daisy closed unexpectedly. Restored your work from 14:32:05." with a "View versions" link.
- Because autosave lags editing by under a second, at most the last gesture can be lost.
- If the saved document fails validation on load (schema check plus the structural invariants in 10.2), Daisy does not open it for editing. It offers the most recent version that validates and a download of the raw data.

### 12.5 Versions

- **Automatic versions:** one every 10 minutes of active editing and one before any risky operation (import, cascade direction change, bulk delete of a screen size). The newest 20 automatic versions per document are kept.
- **Manual versions:** `Ctrl+S` or File → Save version, with an optional label. Kept until deleted.
- The Versions dialog lists them with time and label, shows a thumbnail, and offers "Restore" (which first saves the current state as a version) and "Open as copy".

### 12.6 Document files: import and export of Daisy documents

A `.daisy` file is a ZIP archive:

```
document.json        the DaisyDocument, including schemaVersion
assets/<assetId>     raw bytes of each asset
thumbnail.png
```

- **Save a copy** uses the File System Access API where available (so the user picks a location and later saves overwrite the same file) and falls back to a normal download.
- **Open** validates the archive: size limits, JSON schema, structural invariants, that every referenced asset exists, and that asset bytes match their declared type. The opened file becomes a *new* local document; it never overwrites an existing one.
- An opened file is untrusted input. Custom code inside it is inert on the canvas like all custom code; the first Preview of an imported document that contains scripts shows a notice naming them and asks before running (13.6).

### 12.7 Schema versioning

`schemaVersion` is an integer. A `migrations` array holds one pure function per version step (`v1 → v2`, …). On load, migrations run in order until the document reaches the current version, then it is validated. A document from a newer version than the app understands is refused with a clear message. Every schema change requires a migration and a fixture test with a document saved in the previous version.

---

### 12.8 App updates

Daisy updates itself from GitHub Releases (electron-updater in the main process; ADR 0004, docs/engineering/RELEASING.md). An automatic check runs once at start in packaged builds; Help › Check for updates runs one on demand. Downloads happen in the background and install when Daisy quits.

Update problems are never silent (AGENTS.md 3c; design UI_DESIGN_PLAN.md D-52 item 7):

- The main process sends every update result to the editor as an IPC event: checking, up to date, available (version), downloaded, and **failed** with a kind (`offline`, `server`, `missing-config`, `download`, `install`) and the error text.
- A failed **automatic** check shows the quiet notice once per start; it never blocks editing or covers a dialog. A failed **on-demand** check shows the warning state in About Daisy with Try again and Details. A failed **download or install** shows the red notice with Try again; the running version keeps working.
- Details shows the raw error text, copyable for Report a problem. Nothing is retried in the background without the user pressing Try again; the next automatic check is the next start.



### 13.1 What users can add

| Capability | Where | Who sees it |
|---|---|---|
| HTML attributes | Properties → Attributes | Collapsed by default |
| Extra classes and ids | Properties → General → Advanced | Advanced only |
| Element-level CSS and extra selectors | Properties → Custom CSS | Collapsed by default |
| Page CSS | Code → Page CSS | Only if the drawer is opened |
| Raw HTML | HTML block element | Only if placed |
| `<head>` content | Code → Page JavaScript → Head | Only if the drawer is opened |
| JavaScript files and external script URLs | Code → Page JavaScript | Only if the drawer is opened |

A beginner who never opens these never meets code.

### 13.2 Threat model

Daisy has no accounts and no server, so the valuable things to protect are: the user's other documents and assets in IndexedDB, the integrity of the editor (it must not be frozen, defaced or made to save corrupted data), and the user's browser session on Daisy's origin. Threats come from code the user pasted without understanding it, and from `.daisy` files received from someone else.

### 13.3 Layer 1: the editing canvas never executes anything

- The edit frame is created with `sandbox="allow-same-origin"` and **without** `allow-scripts`. With that flag absent the browser will not run scripts, event-handler attributes or `javascript:` URLs in the frame.
- Independently of the sandbox, the renderer never materialises executable content (9.3): no `<script>`, no `on*` attributes, no `javascript:` URLs, embeds as placeholders, HTML blocks and SVG passed through a sanitiser (DOMPurify) before insertion.
- The frame's document also carries `<meta http-equiv="Content-Security-Policy" content="script-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'">`.

Three independent layers are used because each has known gaps on its own (sanitisers have had bypasses; sandbox behaviour differs slightly between browsers; meta CSP applies only from the point it is parsed).

Custom CSS *is* applied on the canvas. CSS cannot run script, but it can load remote resources (`url()`), which can reveal that the document was opened, and it can hide or restyle page content. It cannot reach outside the frame, so it cannot restyle the editor. Remote loading is governed by the asset policy in 13.5.

### 13.4 Layer 2: Preview runs code in an isolated frame

> **Adapted (2026-11-13):** in the Electron app Preview runs in an isolated session — `docs/adr/0010-preview-in-an-isolated-electron-session.md`.


- The preview frame is `<iframe sandbox="allow-scripts allow-forms allow-popups" srcdoc="…">`. There is **no `allow-same-origin`**, so the frame has an opaque origin: it cannot read Daisy's IndexedDB, `localStorage`, cookies, service workers or the editor's DOM, and requests it makes are cross-origin without credentials for Daisy's origin.
- There is no `allow-top-navigation`, so the page cannot navigate the editor away. Popups opened from the preview inherit the sandbox.
- The preview document is built by the export pipeline into a single self-contained HTML string: CSS inlined, scripts inlined, and assets embedded as `data:` URLs (object URLs from the editor's origin are not usable from an opaque origin).
- A Content Security Policy is included as the first element of `<head>`:

```
default-src 'none';
img-src data: https:;  media-src data: https:;  font-src data: https:;
style-src 'unsafe-inline' https:;
script-src 'unsafe-inline' <hosts of external scripts the user added>;
frame-src https:;
connect-src <none by default; "Allow network requests in preview" adds https:>;
form-action 'none';  base-uri 'none';
```

- Forms do not submit in preview (`form-action 'none'`); the preview shows a toast "Form would be sent to …" instead.

**Communication.** A small bridge script is placed first in the preview document. It forwards uncaught errors, console output and link clicks to the editor with `postMessage`. The editor:

- accepts messages only when `event.source === previewFrame.contentWindow`;
- treats every message as untrusted data, validates its shape against a fixed schema, limits sizes and rate, and renders any strings as text only;
- never executes, evaluates, or uses message content as HTML, and never lets a message trigger a document change;
- sends only two message types into the frame: "scroll to element" and "set width". No document data beyond what is already in the frame.

User scripts run in the same frame as the bridge and can therefore forge or suppress its messages. That is acceptable only because nothing the editor does with those messages is privileged: the worst outcome is a misleading entry in the preview console.

### 13.5 Asset and network policy

| Context | Allowed sources |
|---|---|
| Edit frame | Document assets (object URLs), `data:`, and `https:` images, media and fonts. A per-document setting "Load remote content while editing" (on by default for documents created locally, **off** for imported files until the user turns it on) |
| Preview frame | As set by the CSP above |
| Uploaded SVG | Sanitised on import. Used through `<img>` by default (where scripts in SVG never run); inlined only on request, sanitised again |
| Uploaded fonts, images, video | Type checked by signature (magic bytes), not by file extension |

### 13.6 Broken or hostile code

| Problem | Handling |
|---|---|
| Syntax error in custom CSS | The editor marks the line; the browser ignores the invalid rule; the rest applies |
| CSS that hides everything or covers the page | The canvas overlay and Layers still work, since they are outside the frame. View → "Disable custom CSS on canvas" turns page CSS off for editing |
| JavaScript error | Shown in the preview console with line number; preview continues |
| Infinite loop or heavy script | A sandboxed frame may run in the same process as the editor, in which case a tight loop freezes the tab. Mitigations: the document is saved before preview starts; the bridge sends a heartbeat and the editor shows "Preview is not responding — Stop" when it can; the next launch after a crash opens the document in edit mode (never straight into preview) and offers "Disable scripts" |
| Script that alters or deletes the page | Affects only the preview's copy. The document is untouched; leaving preview discards the frame |
| Script that redirects or opens windows | Top navigation is blocked by the sandbox; popups are sandboxed |
| Imported document with scripts | First preview shows the list of scripts and their sizes and asks "Run scripts from this file?" with "Preview without scripts" as the default button |
| Data exfiltration by script | The script can only see the preview page itself. `connect-src` is closed by default |

### 13.7 Limitations and trade-offs (stated plainly)

- **A sandboxed iframe is not a complete security boundary for arbitrary JavaScript.** It reliably blocks access to Daisy's storage and DOM. It does not protect against browser vulnerabilities, does not guarantee a separate process, and cannot stop CPU or memory exhaustion.
- **Preview is close to, but not identical to, a hosted page.** Opaque origin means `localStorage`, cookies and some APIs throw or are unavailable; relative URL navigation between pages is simulated; `data:` assets make very large media slow to preview. The true final test is the exported folder on a real server, and the Export dialog says so.
- **Stronger isolation is possible later** by serving the preview from a separate registrable domain (for example a `daisy-preview` domain) so the browser gives it its own process and a real origin. This requires hosting a second static site and is deferred until there is evidence it is needed. The message-only bridge is designed so that this change would not affect the editor.
- **Exported sites run the user's code with no sandbox**, as any website does. Daisy preserves custom code exactly and does not claim to make it safe.
- **Safari note.** Some WebKit versions have not dispatched event listeners registered from the parent into a frame that lacks `allow-scripts`. Milestone 1 includes a check for this. If it fails on a target browser, that browser's edit frame drops the sandbox attribute and relies on the renderer allow-list plus the `script-src 'none'` policy. Primary target browsers are Chromium-based; see chapter 19.

---

## 14. Export System

### 14.1 Output structure

```
my-site/
├── index.html
├── css/
│   └── style.css
├── js/
│   ├── motion.js          only if "start when scrolled into view" is used
│   └── main.js            only if the user wrote custom JavaScript (one file per custom script)
└── assets/
    ├── images/
    │   ├── hero.jpg
    │   └── logo.svg
    ├── media/
    │   └── intro.mp4
    └── fonts/
        └── inter-400.woff2
```

All references are relative, so the folder works from any path on any static server, from a subfolder, or opened directly from disk.

### 14.2 HTML generation

`generateHtml(doc, page, opts)` walks the node tree and serialises it.

- `<!doctype html>`, `<html lang>`, a `<head>` with charset, viewport, title, description, optional social tags and favicon, font preloads, the stylesheet link, custom head HTML, then scripts with `placement: 'head'`.
- `<body>` contains the sections in order. Scripts with `placement: 'body-end'` come last.
- Tags and attributes are written exactly as stored. Attribute order is fixed: `class`, `id`, element-specific (`href`, `src`, `alt`, `type`, `name`, …), `aria-*`, `data-*`, others alphabetically.
- Text is HTML-escaped. Attribute values are escaped and double-quoted. Void elements are written without a closing slash.
- Output is indented with two spaces. Inline content (text with `strong`, `a`, …) is kept on one line so whitespace does not change rendering. `pre` and `textarea` content is never re-indented.
- No `data-d-*` attributes, no editor classes, no comments mentioning Daisy other than one optional generator meta tag (off by default).
- HTML blocks and inline SVG are written verbatim.
- Elements hidden at every screen size are still exported (they may be shown by script); the Export dialog lists them so the user can delete them instead.

### 14.3 CSS generation

Chapter 11 with `target: 'export'`. File name `css/style.css`. Options: minify, merge identical rules, remove unused tokens, include a source comment header (off).

### 14.4 JavaScript generation

**Daisy generates no JavaScript for layout, styling, responsive behaviour, states or ordinary animations.** Those are all CSS. There are two cases where a script file is written:

1. `js/motion.js`, only when at least one element uses the "When scrolled into view" animation start. It is a fixed, dependency-free script of about 15 lines:

```js
(() => {
  const els = document.querySelectorAll('[data-animate]');
  if (!('IntersectionObserver' in window)) { els.forEach(el => el.classList.add('is-in-view')); return; }
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (e.isIntersecting) { e.target.classList.add('is-in-view'); io.unobserve(e.target); }
    }
  }, { threshold: 0.2 });
  els.forEach(el => io.observe(el));
})();
```

   The matching CSS pauses the animation until the class is present (`.card-1 { animation-play-state: paused } .card-1.is-in-view { animation-play-state: running }`). Where the user opts for a scroll-driven CSS timeline instead, no script is written.

2. Custom scripts, each written to its own file under `js/` with the name the user gave it, and referenced with the `defer`, `async` or `type="module"` attributes they chose. External script URLs are written as `<script src>` tags. Code is preserved byte for byte.

### 14.5 Assets

- Only assets that are referenced by the page are exported (option: "Include unused assets").
- File names come from the original names, lower-cased, spaces to hyphens, non-ASCII transliterated or removed, de-duplicated with a numeric suffix. Names are stable between exports of the same document.
- Images are exported as uploaded. Optional, off by default: "Also create WebP copies and use `<picture>`".
- Uploaded fonts produce `@font-face` rules with `font-display: swap` and are preloaded if used in the first screen.
- Remote fonts and remote images stay as remote URLs. The Export dialog lists every external dependency so the user knows the site is not fully self-contained when any exist.

### 14.6 Export dialog

Left: a file tree of what will be written, with sizes. Clicking a file shows its content read-only. Right: options (minify HTML/CSS, merge rules, unused assets, WebP copies), the accessibility summary (8.4), and the list of external dependencies. Buttons: **Download .zip** and, where the File System Access API exists, **Save to folder…** (remembers the folder per document so re-export is one click).

### 14.7 Example

Document: one section with padding, a heading and a button with a hover style, a smaller heading on mobile.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Daisy example</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <section class="intro">
    <h1 class="intro-title">Design the web, visually.</h1>
    <a class="start-button" href="#start">Get started</a>
  </section>
</body>
</html>
```

```css
*, *::before, *::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; }
img, video, svg { display: block; }
h1, h2, h3, h4, h5, h6, p, figure, blockquote, dl, dd, pre { margin: 0; }
button, input, select, textarea { font: inherit; color: inherit; }

:root {
  --brand: #2f80ed;
}

body {
  background-color: #ffffff;
  font-family: system-ui, sans-serif;
  font-size: 16px;
  line-height: 1.5;
  color: #111111;
}

.intro {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
  min-height: 400px;
  padding: 96px 24px;
}

.intro-title {
  font-size: 56px;
  font-weight: 700;
  line-height: 1.2;
  text-align: center;
}

.start-button {
  display: inline-block;
  padding: 12px 20px;
  border-radius: 6px;
  background-color: var(--brand);
  color: #ffffff;
  text-decoration: none;
  transition: background-color 200ms ease;
}
.start-button:hover {
  background-color: #1b5fc1;
}

@media (max-width: 640px) {
  .intro {
    padding: 56px 16px;
  }
  .intro-title {
    font-size: 36px;
  }
}
```

### 14.8 Hosting

The output is static files only. Any of these work with no changes: uploading the folder by FTP to shared hosting, any static host or object storage bucket, a local web server, or opening `index.html` from disk. There is no build step, no runtime library, and no reference to Daisy.

---

## 15. Technology Stack

> **Updated (2026-11-13):** Daisy is an Electron desktop app (ADR 0001) in a pnpm + Turborepo monorepo (ADR 0002), with class-based TypeScript and dependency injection (ADR 0011) and Go/C++/Python where they fit (ADR 0012). Current versions: ADR 0008. The source layout in 15.1 is replaced by `docs/architecture/ARCHITECTURE.md`.


| Area | Choice | Why |
|---|---|---|
| Language | **TypeScript**, strict mode | The document model, registries and commands are type-heavy; strictness catches whole classes of editor bugs |
| Build | **Vite** | Fast dev server, simple static build, no configuration burden |
| UI framework | **React** (current stable) for the editor chrome only | Panels, menus and forms are conventional component UI; React has the widest pool of maintained primitives. The canvas page is *not* rendered with React |
| Page rendering | **Own imperative `CanvasRenderer`** writing real DOM into an iframe | Needs exact control of DOM and CSSOM, patch-level updates and no framework artefacts in the page (chapter 9) |
| Overlay | React-rendered **SVG** in the editor window | Tens of shapes; declarative drawing from gesture state is simplest |
| State | **Zustand** with **Immer** (`produceWithPatches`) | Small, no boilerplate; Immer gives immutable updates plus the forward and inverse patches that history, rendering and autosave are built on |
| Document model | Plain JSON-serialisable objects (chapter 10), validated with **Zod** at load and import | Zod gives runtime validation and static types from one definition, used at the trust boundary only |
| Editor styling | **CSS Modules** with CSS custom properties for the theme | The UI is dense and custom; plain scoped CSS is the most direct way to get exact 24 px controls. No utility framework, no CSS-in-JS runtime |
| Accessible primitives | **Radix UI primitives** (unstyled): menu, context menu, popover, dialog, tooltip, select, tabs | Keyboard and screen-reader behaviour of these is hard to get right and not Daisy's specialty |
| Icons | Hand-drawn 16 px SVG set for tools; **Lucide** for generic UI glyphs | Tool icons need to be specific; generic ones do not |
| Canvas interaction | Own pointer handling with Pointer Events and pointer capture | Drag libraries assume list or DOM-drop models; Daisy's gestures (insertion points across a transformed iframe, snapping, bands) are specific |
| Ids | **nanoid** | Tiny, collision-safe |
| Persistence | **IndexedDB** via **idb** | Only browser store that handles large blobs; `idb` is a thin promise wrapper |
| Zip | **fflate** | Small, fast, streaming; used for `.daisy` files and export |
| Sanitising | **DOMPurify** | Mature sanitiser for HTML blocks and SVG |
| Colour | **culori** (tree-shaken) | Parsing and converting hex, rgb, hsl, oklch; contrast calculation |
| Code editor | **CodeMirror 6**, lazy-loaded | Modular and far lighter than alternatives; CSS, HTML and JS modes |
| CSS parsing | The browser: `CSSStyleSheet`, `element.style`, `CSS.supports` | No parser dependency; behaviour matches the engine that renders the page |
| Virtual list | **@tanstack/react-virtual** | Layers and Elements lists |
| Unit tests | **Vitest** | Same toolchain as Vite |
| Browser tests | **Playwright** | Real pointer gestures, screenshots, multi-browser |
| HTML checks | **html-validate** in tests | Validates exported markup |
| Lint / format | ESLint, Prettier | Standard |
| Backend | **None** | Nothing in scope needs one. The app is a static site |

Deliberately not used: a global event bus, a plugin system, a rich-text framework, a drag-and-drop library, a design-system component kit, server-side rendering, a monorepo.

### 15.1 Source layout

```
src/
  app/            App shell, routing between Home and Editor, theme
  model/          types.ts, schema.ts (Zod), commands.ts, invariants.ts, migrations.ts, selectors.ts
  registry/       elements/ (one file per category), properties/ (one file per group), tools.ts
  store/          docStore.ts (Immer + history), editorStore.ts, prefs.ts
  css/            generate.ts, normalize.ts, shorthands.ts, order.ts, base.css.ts
  html/           generate.ts
  canvas/         CanvasViewport.tsx, CanvasRenderer.ts, hitTest.ts, measure.ts, snapping.ts,
                  insertion.ts, textEdit.ts, overlay/
  tools/          one file per tool implementing the Tool interface
  panels/         layers/, elements/, assets/, properties/ (+ controls/), swatches/, history/,
                  code/, timeline/
  shell/          TopBar, OptionsBar, ToolStrip, StatusBar, dialogs/
  persistence/    db.ts, autosave.ts, versions.ts, daisyFile.ts, recovery.ts
  preview/        buildPreview.ts, bridge.ts, PreviewFrame.tsx
  export/         exportSite.ts, assets.ts, ExportDialog.tsx
  a11y/           checker.ts
tests/
  unit/  e2e/  fixtures/  visual/
```

Dependency rule: `model`, `css` and `html` import nothing from React or the DOM-specific folders, so they can be tested in isolation and reused by export. `tools` and `panels` talk to the document only through `store` commands.

---

## 16. Development Milestones

> **Updated (2026-11-13):** the live roadmap is `docs/tasks/ROADMAP.md` (M00–M24). CI exists from day one (ADR 0004). Milestone 3 is rewritten for project folders; milestones 17–19 here are M22–M24 there.


Nineteen milestones in dependency order. Each ends with something a person can use. Each task is sized to be implemented and verified on its own.

Sequencing notes:

- The history mechanism (transactions and patches) is built in Milestone 1, not later, because the renderer and every tool depend on the patch stream. The later history work is the History panel and hardening.
- Local saving comes third, as soon as there is work worth keeping.
- Preview and Export come before states, animation and custom code, so that every later feature is verified against real exported output from the day it is built.
- No CI, accounts, cloud or collaboration appear anywhere in this roadmap. A local test command is enough until there is more than one contributor.

Overview:

| # | Milestone | Main dependency |
|---|---|---|
| 1 | Clean document and core editor loop | — |
| 2 | Selection and manipulation | 1 |
| 3 | Local saving and documents | 1 |
| 4 | Element creation tools and text editing | 2 |
| 5 | Layers and document hierarchy | 2, 4 |
| 6 | Properties architecture | 4 |
| 7 | Layout and spacing | 6 |
| 8 | Typography and appearance | 6 |
| 9 | Assets and media | 3, 4 |
| 10 | Preview and export | 7, 8, 9 |
| 11 | Responsive editing | 6, 10 |
| 12 | States and transitions | 6, 10 |
| 13 | Advanced CSS and positioning | 7, 8, 12 |
| 14 | Animation | 12 |
| 15 | Custom code and attributes | 10 |
| 16 | Full element library and accessibility | 4, 6, 15 |
| 17 | History, versions and document files | 3 |
| 18 | Performance and editor accessibility | all above |
| 19 | Final polish | all above |

---

### Milestone 1: Clean document and core editor loop

- **Goal:** Open Daisy, see one empty section, add a box and a text element, change them, and see the real page update.
- **Why it is needed:** It proves the central architecture end to end: model → generated CSS → iframe DOM → overlay → tool → command → model.
- **User-visible result:** A working, if minimal, editor: canvas with a page, three tools, a small properties panel, undo and redo.
- **Technical implementation details:** Vite + React + TypeScript project. Types and commands from chapter 10 (nodes, styles for base only, `insertNode`, `removeNode`, `setStyles`). Zustand + Immer store with `run`, `begin`, `commit`, `rollback`, `undo`, `redo`. `generateCss` for base styles and the base stylesheet. `CanvasRenderer` with initial render and patch application. Edit frame with the sandbox settings of 9.2. `CanvasViewport` with hit testing and tool dispatch. SVG overlay for hover and selection outlines.
- **Dependencies:** None.

**Task checklist**

- [ ] Scaffold the project with strict TypeScript, ESLint, Prettier, Vitest.
- [ ] Define `DaisyDocument`, `ElementNode`, `TextNode`, `StyleDecls`, `ResponsiveStyles` and a `createEmptyDocument()` that returns one `<section>` with `min-height: 400px`.
- [ ] Implement `insertNode`, `removeNode`, `setStyles`, `replaceChildren` with the invariant checker.
- [ ] Implement the doc store with patch capture, transactions, undo and redo.
- [ ] Implement `generateCss` (base rules only) and the base stylesheet.
- [ ] Implement the edit frame and `CanvasRenderer` (initial render; patch → DOM/CSSOM updates; id maps).
- [ ] Verify that listeners attached from the editor window fire inside the script-less sandboxed frame in Chromium, Firefox and Safari; record the result and apply the fallback from 13.7 where needed.
- [ ] Implement `CanvasViewport`: pointer events, `hitTest`, the `Tool` interface, active-tool dispatch.
- [ ] Implement the overlay: hover outline, selection outline with name tag, empty-section hint.
- [ ] Implement the Select tool (click to select, `Delete` to remove).
- [ ] Implement the Box tool (click and drag to create, in flow, at the end of the section).
- [ ] Implement the Text tool (click to create a paragraph; plain-text inline editing with `contenteditable`; commit on `Esc` or blur).
- [ ] Build the minimal shell: tool strip with three tools, canvas, and a properties panel with Width, Height, Fill colour, Text colour and Font size wired through `setStyles`.
- [ ] Wire `Ctrl+Z` / `Ctrl+Shift+Z`.

**Acceptance criteria**

- A fresh load shows exactly one empty section on a white 1440 px page; the model contains one section node and one declaration.
- Drawing a box adds a `<div>` to the frame's DOM with a class, and a rule for that class to the frame's stylesheet.
- Changing Width in the panel changes the rule and the canvas within one frame.
- Typing in a text element updates the model's text node.
- Undo and redo step through every action, and the DOM matches the model after each.
- No script can run in the edit frame (test: a node with an `onclick` attribute and a `<script>` child in the model does nothing).

**Done when:** A user can open Daisy, click the section, draw two boxes and a line of text, recolour and resize them from the panel, and undo it all.

---

### Milestone 2: Selection and manipulation

- **Goal:** Direct manipulation on the canvas: move, resize, reorder, multi-select, duplicate, zoom and pan.
- **Why it is needed:** Without it Daisy is a form that edits a page. This milestone makes it a design tool.
- **User-visible result:** Handles, drag-to-reorder with insertion lines, drag-resize with size labels, marquee selection, zoom and pan.
- **Technical implementation details:** Measurement pass (9.5). Resize calculation and flow drag insertion finder (9.6) for Stack parents. `moveNode` command. World transform for zoom/pan with pointer-anchored zoom. Scope rule for selection. Clipboard as serialised subtrees.
- **Dependencies:** Milestone 1.

**Task checklist**

- [ ] Implement the measurement scheduler (rAF pass, `ResizeObserver` on body and selection, frame auto-height).
- [ ] Draw 8 resize handles; implement resize for flow elements writing `width` / `height` in px inside a transaction.
- [ ] Show the live size label; implement `Shift` proportional resize.
- [ ] Implement `moveNode` and flow drag: container detection, insertion index, insertion line, drop target outline, ghost.
- [ ] Implement nesting by dropping into a box, including the 400 ms hover-to-open rule.
- [ ] Implement the selection scope rule, double-click to enter, `Esc` to parent, `Ctrl+click` deep select.
- [ ] Implement multi-selection: `Shift+click`, marquee, bounding box, group move.
- [ ] Implement duplicate (`Ctrl+D`, `Alt+drag`), copy, cut, paste, paste inside, delete, with new ids and unique class names.
- [ ] Implement zoom (wheel, shortcuts, fit, 100%) and pan (wheel, `Space+drag`, middle drag), Hand and Zoom tools.
- [ ] Implement the status bar breadcrumb with click and hover behaviour.
- [ ] Implement the element context menu with the actions available so far.
- [ ] Implement alignment guides and size-match snapping during resize.

**Acceptance criteria**

- Dragging a box above another reorders the DOM and the model identically; one undo restores it.
- A whole drag or resize is a single history entry; `Esc` mid-drag leaves the document unchanged.
- Outlines and handles stay aligned with elements at every zoom from 10% to 800%, and stay the same screen size.
- Resizing an element taller pushes following elements down live.
- Pasting produces elements with class names not used elsewhere.

**Done when:** A user can lay out a simple stacked page by drawing boxes and text, dragging them into order and into each other, resizing by hand, and navigating with zoom and pan.

---

### Milestone 3: Local saving and documents

- **Goal:** Work is never lost and documents can be managed.
- **Why it is needed:** From this point users create things worth keeping; every later milestone assumes persistence.
- **User-visible result:** Home screen with documents, automatic saving with status, reopening after closing the browser.
- **Technical implementation details:** IndexedDB stores `documents`, `docData`, `session` (12.2). Debounced autosave driven by committed history entries. `schemaVersion` and the migration runner (even with zero migrations). Zod schema validation on load. Web Locks for single-tab ownership. Basic crash detection.
- **Dependencies:** Milestone 1.

**Task checklist**

- [ ] Implement `db.ts` with the object stores and typed accessors.
- [ ] Implement autosave (800 ms debounce, 5 s max wait, save on `visibilitychange` and `pagehide`) and the save status in the top bar.
- [ ] Implement the Zod schema for the document and validation plus invariant checks on load.
- [ ] Implement the migration runner and `schemaVersion`.
- [ ] Build Home: list, New document dialog, open, rename, duplicate, delete with "Recently deleted".
- [ ] Generate and store thumbnails.
- [ ] Persist per-document viewport and selection; persist preferences in `localStorage`.
- [ ] Implement the session record, clean-close flag and the "restored" notice.
- [ ] Implement the Web Lock and the read-only second-tab notice.
- [ ] Request persistent storage and show the quota on Home.
- [ ] Handle write failure with the red status and in-memory continuation.

**Acceptance criteria**

- Edit, close the tab within two seconds, reopen: the edit is there.
- Kill the browser process during editing: on restart Daisy reopens the document with the restored notice and at most the final gesture missing.
- A corrupted `docData` record does not crash the app; the document is reported as damaged and others still open.
- Opening the same document in a second tab does not allow editing there.

**Done when:** A user can create several documents, leave, come back days later, and continue each one exactly where it was.

---

### Milestone 4: Element creation tools and text editing

- **Goal:** All core creation tools and proper rich text editing.
- **Why it is needed:** A page needs more than boxes and plain text; the element registry is also the foundation for properties and validation.
- **User-visible result:** Section, Box (with variants), Text (with Heading), Button, Link, Place tools; the Elements panel; the options bar; bold, italic and links inside text.
- **Technical implementation details:** Element registry (8.1) with definitions for section, box, divider, text, heading, button, link, list, image placeholder. `canContain` validation. Shared creation pipeline (click versus drag, insertion point, In flow default). Text editing per 9.7 with inline model nodes. Options bar framework. Tool flyouts and tool lock.
- **Dependencies:** Milestone 2.

**Task checklist**

- [ ] Implement `ElementTypeDef` and the registry with the element types listed above and their starting styles.
- [ ] Implement `canContain` and invalid-drop feedback (red insertion line and reason).
- [ ] Refactor creation into one pipeline used by every creation tool; add insertion-point preview while hovering.
- [ ] Implement the Section tool and the "+ Add section" bar.
- [ ] Implement Box variants (Ellipse, Divider) and tool flyouts, cycling and tool lock.
- [ ] Implement full text editing: caret placement at click, `beforeinput` handling, model sync, paste as plain text, `Enter` new paragraph, `Shift+Enter` line break.
- [ ] Implement inline formatting commands (bold, italic, underline via span, link) on a selected range.
- [ ] Implement typing-burst history grouping.
- [ ] Implement the Heading variant with level selection.
- [ ] Implement the Button tool with its starting styles and immediate label editing.
- [ ] Implement the Link tool: popover, wrap element, link text range, link to section (creates the id).
- [ ] Build the options bar framework and the options for each tool built so far, with the "More" popover.
- [ ] Build the Elements panel (categories, search, click-to-arm, drag to canvas, double-click insert) and the Place tool.
- [ ] Add tool tooltips and the status bar hints.

**Acceptance criteria**

- Every tool creates the exact HTML and starting CSS specified in 5.3 and 8.2 (snapshot tests).
- Dropping a box into a paragraph is refused with the specified message.
- Typing a sentence, bolding one word and linking another produces `<p>… <strong>…</strong> … <a href>…</a></p>` in the model.
- Undo while typing removes a burst, not a single character and not the whole paragraph.
- Pasting formatted text from a word processor yields plain text only.

**Done when:** A user can build a text-and-buttons page with headings, paragraphs with inline formatting, links, dividers and multiple sections, using tools alone.

---

### Milestone 5: Layers and document hierarchy

- **Goal:** See and control the real structure of the page.
- **Why it is needed:** Nested structure cannot be managed from the canvas alone; locking, hiding, grouping and renaming need a home.
- **User-visible result:** The Layers panel, synchronised with the canvas, with rename, reorder, nest, lock, hide, group and ungroup.
- **Technical implementation details:** Virtualised tree over the node map. Drag and drop in the tree using `moveNode` and `canContain`. `locked` flag honoured by hit testing. Hide writes `display: none` to the base. Group and ungroup as composite commands. Class name generation from names (11.3).
- **Dependencies:** Milestones 2 and 4.

**Task checklist**

- [ ] Build the virtualised Layers tree with expand/collapse, icons and default names.
- [ ] Two-way selection sync, including auto-expand and scroll into view.
- [ ] Hovering a row highlights the element on the canvas, and the reverse.
- [ ] Inline rename with class name regeneration and uniqueness.
- [ ] Drag to reorder and nest within the tree, with between/inside indicators and validation.
- [ ] Lock: flag, icon, canvas hit-test skip, `Ctrl+Shift+L`.
- [ ] Hide: `display: none`, eye icon, hidden notice in Properties, `Ctrl+Shift+H`.
- [ ] Group (`Ctrl+G`) and Ungroup (`Ctrl+Shift+G`) with the style-loss warning.
- [ ] Layer context menu; "Select layer" submenu on the canvas context menu.
- [ ] Name/tag filter field.
- [ ] `Ctrl+[` / `Ctrl+]` reorder shortcuts and `Tab` / `Shift+Tab` sibling navigation.

**Acceptance criteria**

- The tree always equals the DOM structure of the edit frame (automated comparison after random operations).
- Renaming "Box 3" to "Price card" makes the exported class `price-card`.
- A locked element cannot be selected by clicking the canvas but can be from Layers.
- Grouping three siblings creates one `<div>` containing them in the same order; ungrouping restores the previous structure exactly.

**Done when:** A user can organise a page of fifty nested elements: name them, find them, restructure them and protect finished parts from accidental edits.

---

### Milestone 6: Properties architecture

- **Goal:** The registry-driven Properties panel with the disclosure pattern and robust value fields.
- **Why it is needed:** Every later styling feature is a set of registry entries. Building the framework once prevents twenty hand-made panels.
- **User-visible result:** A real Properties panel with General, Size, Placement (In flow / Free), Spacing (numbers), Fill (single colour) and Border, each with Advanced and "Other properties".
- **Technical implementation details:** `PropertyGroupDef` and `ControlDef` (6.1). `effectiveDecls` with origin tracking. Shared controls: length field (parsing, units, arithmetic, scrubbing, stepping), colour picker, select, segmented, toggle, box-sides. Style normalisation with shorthand expansion and `CSS.supports` validation (10.3). Free placement conversion (7.4). Mixed values for multi-selection.
- **Dependencies:** Milestone 4.

**Task checklist**

- [ ] Implement style normalisation: shorthand expansion via the browser, validation, zero handling.
- [ ] Implement `effectiveDecls` and its memoisation.
- [ ] Build the group container component: collapse, Advanced disclosure with remembered state, set-value dot, "Other properties" rows.
- [ ] Build the length field with units, keywords, arithmetic → `calc()`, custom-value fallback, scrub, arrow stepping, validation feedback.
- [ ] Implement unit conversion that preserves visual size.
- [ ] Build the colour picker (hex, alpha, hue/saturation area, eyedropper button stub).
- [ ] Build tooltips showing description, CSS property and current value.
- [ ] Implement General (name, kind, tag, class, id).
- [ ] Implement Size (modes Fill / Fit content / Fixed, min/max, overflow, aspect ratio) with the "real size differs" note.
- [ ] Implement Placement: In flow ↔ Free conversion with anchor handling, pins, offsets, stack order; free drag and nudge on the canvas with snapping.
- [ ] Implement Spacing box diagram (numeric only) and "Center horizontally".
- [ ] Implement single-colour Fill and simple Border with corner roundness; corner handles on the canvas.
- [ ] Implement group adaptation by element type and context (`appliesTo`, `visibleWhen`), and Mixed values.
- [ ] Show the selection's X, Y, W, H and placement switch in the Select options bar.

**Acceptance criteria**

- Typing `50%`, `12rem`, `auto`, `100% - 40px`, `clamp(1rem, 4vw, 3rem)` or `var(--x)` into a length field stores the correct CSS; typing `banana` is rejected.
- Typing `padding: 8px 16px` under Other properties results in four stored longhands and the Spacing diagram showing them.
- Switching an element to Free does not move it by more than 0.5 px, and is one undo step including the parent's `position: relative`.
- Selecting an image does not show Layout or Typography; selecting a paragraph does not show Layout.
- Advanced disclosure state survives selecting other elements and reloading.

**Done when:** A user can precisely control size, placement, spacing, colour and borders of any element, in simple terms or with any CSS value they choose.

---

### Milestone 7: Layout and spacing

- **Goal:** Visual control of arrangement: rows, columns, grids, gaps, padding and margin on the canvas.
- **Why it is needed:** This is how users build real layouts without templates; it is the heart of the product.
- **User-visible result:** The Arrange children control, the Layout tool and the Spacing tool.
- **Technical implementation details:** `readLayout` / `writeLayout` and the track-list parser (7.2). Insertion finder extended to rows, wrapped rows and grids. Gap, band and track overlays using computed styles. Child controls for rows and grids in Size. Alignment and distribution actions.
- **Dependencies:** Milestone 6.

**Task checklist**

- [ ] Implement `readLayout`, `writeLayout`, and the `TrackList` parser with the `editable` flag.
- [ ] Implement the Layout group: Stack / Row / Grid, direction, alignment grid, spread, wrap, gap; Advanced raw properties; inactive-property tags and "Clean up".
- [ ] Extend flow drag and creation insertion to row, wrapped row and grid parents.
- [ ] Implement the Stack → Column conversion when aligning, with the status message.
- [ ] Implement child controls: Grow to fill, shrink, basis, align self, order; grid column/row start and span.
- [ ] Implement the Layout tool for rows: gap bars (drag), direction arrow, per-child grow toggle, options bar.
- [ ] Implement the Layout tool for grids: track lines and badges, drag to resize tracks, add/remove tracks, drag child to cell, drag edge to span.
- [ ] Implement the Spacing tool: padding and margin bands, edge drag, `Alt`/`Shift` modifiers, gap drag between siblings, double-click to type, zero-size grab strips.
- [ ] Draw bands and gaps when hovering or focusing the matching fields in the panel.
- [ ] Implement alignment and distribution buttons for single flow children, multi-selections and free elements.
- [ ] Implement `Alt`-hover distance readouts and the Measure tool.
- [ ] Show the margin-collapse tag in the Spacing tool.

**Acceptance criteria**

- Choosing Row then dragging a gap bar writes `display: flex` and `gap` and nothing else.
- Setting Grid with 3 columns then dragging the first line produces a three-track template whose pixel result matches the pointer within 1 px.
- A grid template using `subgrid` or named lines is displayed but not draggable, and is never rewritten.
- Switching Row → Grid → Row restores the original row settings.
- Dragging the top padding band of a section 64 px writes `padding-top: 64px`.

**Done when:** A user can build a navigation bar, a two-column block and a three-card grid from empty boxes using only the Layout and Spacing tools.

---

### Milestone 8: Typography and appearance

- **Goal:** Full control of how things look: fonts, text styling, fills, gradients, borders, shadows and effects.
- **Why it is needed:** Layout without appearance is a wireframe.
- **User-visible result:** Typography, Fill (layers), Border (complete) and Effects groups; Eyedropper; Swatches panel.
- **Technical implementation details:** Font registry with system stacks; text options in the options bar; range-level typography during text editing. Fill layer model mapped to comma-separated background longhands. Shadow and filter list editors. Tokens as CSS custom properties with `var()` references. Eyedropper via the `EyeDropper` API with a computed-style fallback.
- **Dependencies:** Milestone 6.

**Task checklist**

- [ ] Implement the Typography group simple controls and wire the Text tool's options bar to them.
- [ ] Implement Typography advanced controls, including truncation and the fluid size helper.
- [ ] Show "from parent" origin for inherited text values with click-through.
- [ ] Apply typography to a selected text range (span creation and merging).
- [ ] Implement the font picker with system font stacks and previews.
- [ ] Implement the Fill layer list: colour and image layers, reorder, toggle; mapping to and from background longhands.
- [ ] Implement gradient layers with a stop editor in the panel.
- [ ] Complete Border: per-side values, all styles, elliptical radii, outline.
- [ ] Implement Effects: opacity, shadow list with inner shadows, blur; Advanced blend mode, filter list, backdrop filter, clip-path, cursor.
- [ ] Implement tokens and the Swatches panel: colours, text styles, apply, edit, "Add from selection", detach.
- [ ] Extend the colour picker with swatches, rgb / hsl / oklch input and a contrast readout against the background.
- [ ] Implement the Eyedropper tool and Copy style / Paste style.
- [ ] Implement Page properties (background, base text) when nothing is selected.

**Acceptance criteria**

- Two fill layers (gradient over colour) produce one `background-color` and one `background-image`, and reorder correctly.
- Editing a colour swatch changes every element using it without changing any element's stored declarations.
- Setting text colour on a section changes its children on the canvas, and their Typography group shows the value as coming from the section.
- A shadow list with two shadows round-trips through reload unchanged.

**Done when:** A user can produce a visually finished static page: styled type, colours from a shared palette, gradients, rounded bordered cards with shadows.

---

### Milestone 9: Assets and media

- **Goal:** Real images, video and fonts in documents.
- **Why it is needed:** Pages need media; fonts and images also drive export structure.
- **User-visible result:** The Media tool, the Assets panel, file drop on the canvas, image fills, uploaded fonts.
- **Technical implementation details:** `assets` store keyed by content hash; `AssetMeta`; `daisy-asset://` references resolved to object URLs in the edit frame with lifecycle management. Type detection by signature. SVG sanitising. `@font-face` generation. Usage scan.
- **Dependencies:** Milestones 3 and 4.

**Task checklist**

- [ ] Implement asset import: hashing, signature-based type check, metadata extraction (dimensions, duration), size limits with clear messages.
- [ ] Implement the asset URL resolver and object URL lifecycle in the renderer.
- [ ] Implement the Media tool: Image by click, drag and file drop; placeholder state; Fit options; alt text prompt.
- [ ] Implement Video, Audio and Icon variants; sanitise SVG on import.
- [ ] Implement the Embed variant with the editor placeholder.
- [ ] Build the Assets panel: tabs, upload, thumbnails, usage counts, select users, replace, rename, guarded delete.
- [ ] Support dragging assets to the canvas and onto elements (image source or fill).
- [ ] Add image layers from assets in Fill.
- [ ] Implement uploaded fonts: `FontSource`, weight/style detection, `@font-face` in the generator, availability in the font picker.
- [ ] Include asset blobs when duplicating a document.
- [ ] Write intrinsic `width` and `height` attributes on images.

**Acceptance criteria**

- Dropping a JPEG on a section creates an `<img>` that fits within the section and stores exactly one asset; dropping the same file again reuses it.
- An SVG containing a `<script>` is stored and displayed with the script removed.
- A file named `.png` that is not an image is rejected.
- Deleting an in-use asset is blocked unless confirmed; reloading the document shows all media correctly.

**Done when:** A user can build a page with photographs, a logo, a background image, a video and their own brand font.

---

### Milestone 10: Preview and export

- **Goal:** Turn the document into a real website and verify it interactively.
- **Why it is needed:** It is the product's core promise. From here on, every feature is tested against exported output.
- **User-visible result:** Preview mode and the Export dialog producing a working folder or zip.
- **Technical implementation details:** `generateHtml` (14.2). Export CSS with shorthand collapsing and property ordering (11.4). Asset naming and copying. Zip via fflate; File System Access where available. Preview frame with `sandbox="allow-scripts allow-forms allow-popups"`, self-contained `srcdoc`, CSP and bridge (13.4). The canvas-versus-export geometry test harness.
- **Dependencies:** Milestones 7, 8 and 9.

**Task checklist**

- [ ] Implement `generateHtml` with head metadata, escaping, attribute ordering and formatting rules.
- [ ] Implement export-target CSS: shorthand collapsing, property order, optional minify and rule merging.
- [ ] Implement asset file naming, de-duplication and reference rewriting in HTML and CSS.
- [ ] Implement `exportSite` producing an in-memory file map; zip download; "Save to folder".
- [ ] Build the Export dialog: file tree, file viewer, options, external dependency list.
- [ ] Build the Page settings dialog (title, description, language, favicon, social image).
- [ ] Implement `buildPreview` (single-document, `data:` assets, CSP) and the preview frame.
- [ ] Implement the bridge and validated message handling; preview console for errors.
- [ ] Implement preview width control, size selector and `Esc` to return.
- [ ] Build the fidelity harness: render fixtures in the edit frame and as exported files, compare bounding boxes of every element.
- [ ] Add html-validate checks on exported fixtures.

**Acceptance criteria**

- The exported folder of every fixture document opens from disk and from a static server and looks the same as the canvas (geometry difference ≤ 0.5 px per element).
- Exported HTML passes validation; exported files contain no `data-d-` attributes and no reference to Daisy.
- Links, buttons and form typing work in Preview and not on the editing canvas.
- The preview frame cannot read the editor's IndexedDB or DOM (automated test from inside the frame).

**Done when:** A user can design a page, preview it as a visitor would, export it, upload the folder to any web host, and have a working site.

---

### Milestone 11: Responsive editing

- **Goal:** Design for every screen size without overwriting anything by accident.
- **Why it is needed:** A page that works at one width is not a web page.
- **User-visible result:** Screen size selector, per-size editing, origin markers, per-size visibility, custom screen sizes.
- **Technical implementation details:** Breakpoints in the model; `setStyles` already takes a breakpoint id. Media query blocks in the generator in cascade order. Frame width switching. Origin markers from `effectiveDecls`. Reset and promote actions. `vh` rewriting and fold line.
- **Dependencies:** Milestones 6 and 10.

**Task checklist**

- [ ] Add default breakpoints (Tablet 1024/768, Mobile 640/390) to new documents and a migration for existing ones.
- [ ] Generate `@media` blocks in the correct order for desktop-first, including `min-width` sizes.
- [ ] Implement the top bar selector, `Alt+1..3`, and canvas width switching.
- [ ] Route all style writes to the active breakpoint; show the `Editing:` chip.
- [ ] Implement origin markers and tooltips on every control; Reset and "Set for all sizes".
- [ ] Implement the Properties context strip with the list of overrides and "Clear all here".
- [ ] Implement the Visibility group with per-size toggles and correct display restoration.
- [ ] Implement the structural-edit notice at non-base sizes and base routing for new elements' starting styles.
- [ ] Build the Screen sizes dialog: add, edit, delete with discard/merge choice; mobile-first conversion with preview and automatic version.
- [ ] Implement the Visual order control with its accessibility note.
- [ ] Implement edit-target `vh` rewriting and the fold line.
- [ ] Add Layers badges for elements with overrides; drag the page edge to test widths.

**Acceptance criteria**

- Changing font size at Tablet leaves the base declaration byte-for-byte unchanged and adds exactly one declaration under the Tablet key.
- Exported CSS contains the override inside `@media (max-width: 1024px)`, after all base rules.
- An element hidden on Mobile and shown elsewhere keeps its `display: flex` at larger sizes.
- Deleting a screen size never discards values without the user choosing.
- A 3-column grid set to 1 column at Mobile exports and behaves correctly when the browser window is resized.

**Done when:** A user can take a desktop design, switch to tablet and mobile, adjust type, spacing, columns and visibility for each, and export a site that adapts correctly.

---

### Milestone 12: States and transitions

- **Goal:** Interactive styling: hover, pressed, focus and smooth changes between them.
- **Why it is needed:** Buttons, links and fields feel broken without state feedback.
- **User-visible result:** The State selector, state editing on the canvas, the Transition group.
- **Technical implementation details:** State keys in `ResponsiveStyles` are already modelled. Forced-state selectors and `data-d-state` in the edit target. State-ordered rule output. Transition controls and a canvas play-through using a temporary class swap in the edit frame.
- **Dependencies:** Milestones 6 and 10.

**Task checklist**

- [ ] Implement the State selector with element-appropriate states and custom suffix entry.
- [ ] Route writes to the active state; show the chip; reset to Normal on selection change.
- [ ] Generate state rules in the fixed order; add forced-state selectors for the edit target.
- [ ] Show Normal values as muted placeholders while editing a state.
- [ ] Implement the Transition group simple controls and the inline suggestion on first hover style.
- [ ] Implement per-property transitions and the cubic-bezier editor.
- [ ] Implement the canvas transition preview button.
- [ ] Add Layers badges for state styles; add "Add mouse-over style" to the Button options.
- [ ] Support states combined with screen sizes.
- [ ] Implement `::placeholder` editing for fields.

**Acceptance criteria**

- A button with a hover fill exports `.name:hover { background-color: … }` after the normal rule; hovering in Preview changes the colour.
- With Mouse over selected, the canvas shows the hover appearance without the pointer being over the element.
- Enabling "Animate changes" adds transition longhands to the normal rule only.
- Focus styles are visible when tabbing in Preview.

**Done when:** A user can make buttons, links and fields respond to mouse over, press and keyboard focus with smooth transitions.

---

### Milestone 13: Advanced CSS and positioning

- **Goal:** Professional-level control: transforms, gradients on canvas, remaining placement modes, element-level custom CSS and code inspection.
- **Why it is needed:** Removes the ceiling for experienced users while leaving the beginner surface unchanged.
- **User-visible result:** Transform tool, Gradient tool, Fixed / Sticky / Nudged placement, Custom CSS group with extra selectors, Code panel (Element tab), rulers and guides.
- **Technical implementation details:** Matrix-based oriented overlay boxes. Gradient parsing and on-canvas stop editing. Fixed rendering in the first-screen box (9.9). `ExtraRule` editing and generation. Read-only code view generated from the same generators. CodeMirror lazy-loaded.
- **Dependencies:** Milestones 7, 8 and 12.

**Task checklist**

- [ ] Implement the Transform group and the Transform tool (rotate, scale, origin, skew) with oriented selection boxes and the untransformed ghost.
- [ ] Make hit testing, handles and snapping correct for transformed elements and transformed ancestors.
- [ ] Implement the Gradient tool with on-canvas line and stops for linear, radial and conic gradients.
- [ ] Implement Nudged, Fixed and Sticky placement with their canvas affordances and warnings.
- [ ] Implement the "position uses a formula" lock and "Replace with fixed value".
- [ ] Implement the Custom CSS group: declarations editor with autocomplete and validation, merged into the element's stored declarations.
- [ ] Implement extra selectors (`ExtraRule`): create, edit, generate, including `::before` / `::after`.
- [ ] Build the Code drawer with the Element tab: live HTML and CSS of the selection.
- [ ] Implement rulers and draggable guides with snapping; persist guides.
- [ ] Add multi-column text, `clip-path` presets and mask controls to their groups' Advanced areas.
- [ ] Add "Also styled by Page CSS" detection hook (used fully in Milestone 15).

**Acceptance criteria**

- Rotating an element 30° writes only `transform`; neighbours do not move; the selection box is drawn rotated and handles still work.
- Typing `padding-top: 20px` in Custom CSS updates the Spacing diagram, and dragging the padding band updates the Custom CSS text.
- A sticky header sticks in Preview and in the exported page; a fixed element is shown in the first-screen box on the canvas and fixed in Preview.
- A `::before` rule with `content` renders on the canvas and exports as `.name::before { … }`.

**Done when:** A professional can express essentially any single-element CSS in Daisy, by handle where one exists and by value where not, and inspect the code as they work.

---

### Milestone 14: Animation

- **Goal:** Keyframe animation with a timeline.
- **Why it is needed:** Motion is part of modern page design and is pure CSS, so it fits Daisy's output model.
- **User-visible result:** The Animation group, the Timeline panel, scroll-into-view starts.
- **Technical implementation details:** `KeyframesDef` in the model; `@keyframes` generation; `animation-*` longhands. Timeline scrubbing by setting a negative `animation-delay` with a paused play state on the edited element (exempted from the editor's animation-off rule). `motion.js` and `data-animate` output. Reduced-motion wrapping.
- **Dependencies:** Milestone 12.

**Task checklist**

- [ ] Implement keyframes commands and `@keyframes` generation with unique names.
- [ ] Implement the Animation group simple controls and the starting choices (Fade in, Move in, Scale in, Spin, Custom).
- [ ] Build the Timeline: tracks per animated property, keyframe add/move/delete, per-keyframe easing, duration and delay handles.
- [ ] Implement scrub, play and pause on the canvas.
- [ ] Record mode: while a keyframe is selected, canvas and panel edits write into that keyframe.
- [ ] Implement advanced controls: iteration, direction, fill mode, multiple animations.
- [ ] Implement "When scrolled into view": `MotionTrigger`, `data-animate`, paused-until-class CSS, `motion.js` export.
- [ ] Implement scroll-driven timelines as an Advanced option with a support note.
- [ ] Implement reduced-motion handling (on by default).
- [ ] Add Layers badges and Preview replay button.

**Acceptance criteria**

- A fade-in exports one `@keyframes` block and animation longhands (collapsed to `animation`), and plays on load in Preview.
- Scrubbing the timeline shows intermediate states on the canvas without altering the document.
- With "scrolled into view", the exported page includes `js/motion.js` and the element animates only when scrolled to; with scripts disabled the element is still visible.
- With the operating system set to reduce motion, the exported page shows no animation.

**Done when:** A user can make elements fade, slide and scale in on load or on scroll, fine-tune keyframes on a timeline, and export it as standard CSS.

---

### Milestone 15: Custom code and attributes

- **Goal:** Safe support for custom HTML, CSS and JavaScript.
- **Why it is needed:** Professionals need an escape hatch for behaviour Daisy does not model; it must not endanger the editor or burden beginners.
- **User-visible result:** Attributes group, HTML block element, custom elements, Page CSS and Page JavaScript editors, hardened Preview.
- **Technical implementation details:** `CustomCode` in the model; script files in export; DOMPurify for canvas rendering of HTML blocks; CSP assembly from the document's external hosts; import trust prompts; heartbeat; "Disable scripts" and "Disable custom CSS on canvas" switches.
- **Dependencies:** Milestone 10.

**Task checklist**

- [ ] Implement the Attributes group with validation, boolean attributes, `data-*` helper, "runs script" tagging and "Copy selector".
- [ ] Implement the HTML block element: code popover, sanitised canvas rendering, verbatim export.
- [ ] Implement custom elements through the Place tool's tag field.
- [ ] Build the Page CSS editor; append to generated CSS; "Disable custom CSS on canvas".
- [ ] Complete "Also styled by Page CSS" notes in Properties.
- [ ] Build the Page JavaScript editor: multiple scripts, placement, defer/async/module, external URLs, enable toggles, head HTML.
- [ ] Export scripts as files and tags; inline them in Preview.
- [ ] Build the CSP from document settings; implement "Allow network requests in preview".
- [ ] Implement the preview heartbeat, "not responding" notice and safe-start after a crash.
- [ ] Implement the remote content setting for the edit frame.
- [ ] Write the security test suite (17.2, custom code isolation).
- [ ] Warn when a renamed class still appears in custom code.

**Acceptance criteria**

- An HTML block containing a script shows its markup on the canvas, runs nothing while editing, runs in Preview, and exports verbatim.
- A script calling `indexedDB.open`, `parent.document` or `top.location` from Preview fails and the editor is unaffected.
- Custom page CSS that sets `* { display: none }` leaves the editor fully usable.
- An exported page with a custom script runs it exactly as written.
- A user who never opens the Code drawer or the collapsed groups sees no code anywhere.

**Done when:** A developer can add tracking snippets, third-party embeds, web components and their own scripts and styles, test them in Preview, and export them unchanged, without any risk to their saved work.

---

### Milestone 16: Full element library and accessibility

- **Goal:** Complete the HTML element set and build accessibility guidance into the workflow.
- **Why it is needed:** Forms, tables, lists and landmarks are needed for real sites; accessibility is part of producing proper web output.
- **User-visible result:** Form tool, tables, lists, all semantic elements, the Accessibility group, issue badges, Outline view.
- **Technical implementation details:** Remaining registry entries (8.2). Compound creators and structure-specific editing (table row/column controls, list `Enter` behaviour, dropdown options editor). The model-based checker (8.4). Contrast calculation with culori.
- **Dependencies:** Milestones 4, 6 and 15.

**Task checklist**

- [ ] Add registry entries and starting styles for all form elements; implement the Form tool with automatic labels and ids.
- [ ] Implement field settings in General (kind, placeholder, required, name) and advanced attributes.
- [ ] Implement the dropdown options editor and radio grouping.
- [ ] Implement lists: creation, `Enter`/`Backspace` item behaviour, auto-wrapping of dropped elements in `li`.
- [ ] Implement tables: creation, canvas row/column controls, header cells, shared cell selectors.
- [ ] Add remaining elements: figure, blockquote, pre/code, details, dialog, description list, picture.
- [ ] Complete the Kind dropdown and landmark choices for containers.
- [ ] Implement the accessibility checker rules and severity.
- [ ] Implement the Accessibility group (contextual simple questions; advanced ARIA).
- [ ] Add issue badges in Layers and the summary in the Export dialog.
- [ ] Implement Outline view in Layers.
- [ ] Add "Allow invalid nesting" override with warning badge.

**Acceptance criteria**

- Creating a text field produces a `<label for>` and `<input id>` pair that match; a checkbox is wrapped in its label.
- A table can gain and lose rows and columns from the canvas and always exports valid table markup.
- An image without a description, an empty link and a skipped heading level each produce the specified warning, and none blocks export.
- Outline view lists headings and landmarks in document order.
- Exported fixtures for every element type pass html-validate.

**Done when:** A user can build a complete contact page with a labelled form, a pricing table, lists and proper landmarks, and be told about accessibility problems as they work.

---

### Milestone 17: History, versions and document files

- **Goal:** Complete safety net and portability for documents.
- **Why it is needed:** Trust. Users must be able to go back, recover, and move their work between machines.
- **User-visible result:** History panel, named and automatic versions, `.daisy` save and open.
- **Technical implementation details:** History panel over the existing stack; entry coalescing and limits. `versions` store with retention. Zip-based `.daisy` format with validation (12.6). Corruption handling path.
- **Dependencies:** Milestone 3.

**Task checklist**

- [ ] Build the History panel with jump-to-entry.
- [ ] Implement entry coalescing and the 300-entry / 50 MB limit.
- [ ] Restore screen size, state, selection and scroll position on undo and redo.
- [ ] Implement automatic versions (interval and pre-risk) with retention of 20.
- [ ] Implement manual versions on `Ctrl+S` with labels.
- [ ] Build the Versions dialog: list, thumbnail, restore, open as copy.
- [ ] Implement `.daisy` export with assets and thumbnail; File System Access save with re-save.
- [ ] Implement `.daisy` import with full validation and the untrusted-file rules (remote content off, script prompt).
- [ ] Implement the damaged-document path: offer last valid version and raw download.
- [ ] Implement "Recently deleted" expiry and unused-asset clean-up action.
- [ ] Add a migration fixture test for every schema version so far.

**Acceptance criteria**

- Clicking any History entry puts the document in exactly that state; continuing to edit from there discards later entries.
- Saving a `.daisy` file, deleting the document, and opening the file restores it identically, including assets.
- A truncated or tampered `.daisy` file is rejected with a message and does not create a broken document.
- Restoring a version first preserves the current state as another version.

**Done when:** A user can review and rewind their session, keep milestones of their design, back up documents as files and open them on another computer.

---

### Milestone 18: Performance and editor accessibility

- **Goal:** Daisy stays fast on large pages and is usable by keyboard and assistive technology.
- **Why it is needed:** Professional tools are judged on responsiveness; an application that produces accessible pages should itself be accessible.
- **User-visible result:** Smooth editing on big documents; complete keyboard operation; screen-reader labelling.
- **Technical implementation details:** Profiling against the budgets in 9.11 with generated large fixtures. Measurement batching review, memoisation, virtualisation. Lazy loading of heavy modules. ARIA roles for tree, toolbar, tabs; focus management; keyboard equivalents for canvas operations.
- **Dependencies:** All previous milestones.

**Task checklist**

- [ ] Create fixture generators for 500, 2,000 and 5,000-element documents and automated timing tests.
- [ ] Profile and fix open time, drag frame rate, property edit latency, and memory over long undo sequences.
- [ ] Ensure only overlay-relevant elements are measured; remove any full-tree walks from hot paths.
- [ ] Lazy-load CodeMirror, Timeline, export, zip and sanitiser code; set a bundle size budget.
- [ ] Downscale thumbnails for large images in Assets and Home.
- [ ] Make every panel operable by keyboard with visible focus; implement roving focus in the tool strip and tree semantics in Layers.
- [ ] Provide keyboard equivalents for canvas actions: move in order, resize by keys in a "resize mode", change placement, enter and leave containers.
- [ ] Add accessible names to all controls; announce selection changes and operation results through a live region.
- [ ] Check editor colour contrast in both themes; respect the operating system's reduced-motion setting in editor animations.
- [ ] Build the keyboard shortcuts reference dialog.

**Acceptance criteria**

- All budgets in 9.11 are met in the automated performance tests.
- A complete simple page can be created, styled, saved and exported without a mouse.
- A screen reader announces tool changes, the selected element's name and type, and property labels with values.
- Initial load transfers under the bundle budget; the code editor is not loaded until the drawer opens.

**Done when:** A user can work comfortably on a long, complex page, and a keyboard-only user can use every feature that does not inherently require pointing.

---

### Milestone 19: Final polish

- **Goal:** Consistency, clarity and correctness across the whole product.
- **Why it is needed:** The sum of small rough edges is what separates a professional tool from a prototype.
- **User-visible result:** A coherent, predictable application ready for real use.
- **Technical implementation details:** Review passes against the vocabulary table (3.7), the disclosure pattern (2.1), and the design standards (4.1). Cross-browser test pass. Error boundaries. Offline support through a simple cache-first service worker for the app shell.
- **Dependencies:** All previous milestones.

**Task checklist**

- [ ] Audit every label, tooltip and message against the vocabulary table; fix inconsistencies.
- [ ] Audit every group and tool for the simple/advanced split and the "advanced value set" dot.
- [ ] Complete first-use inline explanations and their dismissal.
- [ ] Complete empty states for every panel.
- [ ] Add error boundaries around panels and the canvas with "copy details" and non-destructive recovery.
- [ ] Finish the light theme; verify visual standards (no stray radii, shadows or decorative colour).
- [ ] Full shortcut audit for conflicts with browsers on Windows and macOS.
- [ ] Cross-browser pass in current Chrome, Edge, Firefox and Safari; record and resolve differences or document them.
- [ ] Add the service worker for offline use of the app itself; confirm it never intercepts preview or asset logic.
- [ ] Run the full acceptance suite (chapter 17) and the end-to-end "build a real page" scripts.
- [ ] Write the in-app keyboard reference and a one-page "How Daisy maps to HTML and CSS" help page.

**Acceptance criteria**

- No interface string contradicts the vocabulary table.
- Every tool and group passes the progressive-complexity check: usable with defaults; advanced reachable in place; nothing set is invisible.
- The three end-to-end reference pages (17.3) can be rebuilt from an empty document and export identically to their stored expected output.
- Daisy loads and edits offline after the first visit.

**Done when:** A new user can open Daisy for the first time and produce and export a complete, responsive page unaided, and a professional can do the same using advanced CSS, without either encountering an inconsistency or a dead end.

---

## 17. Testing and Quality Assurance

### 17.1 Approach

Three layers, all runnable locally with one command each:

| Layer | Tool | Runs | Covers |
|---|---|---|---|
| Unit | Vitest (Node) | On every change, seconds | Model commands, invariants, selectors, HTML generation, CSS ordering, migrations, registries, the accessibility checker |
| Browser unit | Vitest browser mode (real Chromium) | On every change | Anything that needs a real CSS engine: style normalisation, shorthand expansion and collapsing, `readLayout` on computed styles, unit conversion |
| End-to-end | Playwright | Before finishing a milestone | Real pointer gestures on the canvas, panels, persistence, preview isolation, export output, visual and geometry comparisons, performance |

The rule that matters most: **a visual edit is tested by its exported code.** An end-to-end test performs a gesture, then asserts on the model *and* on the generated HTML and CSS, not only on what the canvas looks like.

### 17.2 What is tested, by area

| Area | Tests |
|---|---|
| **Document model correctness** | Each command has unit tests for its result and its inverse. A property-based test applies thousands of random valid command sequences and checks the invariants (10.2) after each, then undoes everything and expects the original document |
| **HTML validity** | Every element type and every fixture document is exported and run through html-validate. `canContain` is tested against a table of allowed and disallowed pairs |
| **CSS correctness** | Every generated stylesheet is loaded with `new CSSStyleSheet().replaceSync()` and must produce no dropped rules. Snapshot tests for rule order, state order and media query order. Shorthand collapsing is tested by computing styles before and after collapsing on a real element and requiring equality |
| **Visual rendering** | Screenshot comparison of fixture documents in the edit frame against stored baselines, per browser |
| **Canvas versus export** | The fidelity harness (Milestone 10): for each fixture and each screen size, the bounding box of every element in the edit frame must equal that of the exported page within 0.5 px, and selected computed styles must match. This test runs for every new feature |
| **Selection behaviour** | Scripted clicks at computed coordinates verify the scope rule, deep select, marquee, locked and hidden elements, selection sync with Layers, and overlay alignment at zoom levels 25%, 100% and 400% |
| **Drag and resize** | Scripted pointer sequences: reorder in stack, row, wrapped row and grid; nest and un-nest; resize in px and %; free move with pins; each asserts the exact declarations written and that one history entry was created. `Esc` mid-gesture must leave the document identical |
| **Undo and redo** | After every scripted scenario, undo to the start and compare to the initial document; redo to the end and compare to the final. Typing bursts and drags are checked to be single entries |
| **Responsive inheritance** | For each property type: set at base, override at Tablet, verify base bytes unchanged, verify effective values and origins at all three sizes, reset, promote. Deleting and merging a breakpoint. Verify exported media queries and their real effect by resizing the exported page |
| **Export consistency** | Golden-file tests: fixtures export to exactly the stored expected files. Exported pages are loaded from a static server in Playwright with no console errors and no failed requests. A scan confirms no `data-d-`, no `daisy-asset://`, no object URLs |
| **Browser persistence** | Save and reload round-trips equality. Simulated crash (close the context without `pagehide`) then reopen. Quota failure injected through a mocked store. Second-tab lock. `.daisy` round-trip. Each old-schema fixture migrates and validates |
| **Custom code isolation** | From inside the preview frame, scripts attempt: `parent.document`, `top.location = …`, `indexedDB.open`, `localStorage`, `document.cookie`, `fetch` to the editor origin, forged bridge messages with oversized and malformed payloads. Each must fail or be ignored, and the editor's document must be unchanged. In the edit frame: `<script>`, `onerror` attributes, `javascript:` links, SVG with script, and a hostile HTML block must execute nothing (a global flag they would set must stay unset) |
| **Performance** | Timed Playwright runs on generated documents against the budgets in 9.11; tests fail on regression beyond 20% |
| **Editor accessibility** | Automated axe checks on the editor shell; scripted keyboard-only scenarios |

### 17.3 Practical acceptance tests

These are end-to-end scripts that build something real from an empty document using only tool gestures and panel edits, then compare the export with a stored expected result. They are the definition of "Daisy works".

| # | Scenario | Proves |
|---|---|---|
| A1 | **Hello page.** New document → Text tool → type a heading → set size and colour → Spacing tool padding → export | The core loop. Expected: one `<section>` with one `<h2>`, four declarations |
| A2 | **Navigation bar.** Box → Arrange Row → Spread: Space between → logo image + three links → align centre | Row layout by gesture. Expected CSS contains `display: flex; justify-content: space-between; align-items: center` and no positioning properties |
| A3 | **Three cards.** Box → Grid 3 columns → three boxes each with image, heading, text → gap by dragging | Grid, nesting, duplication with unique classes |
| A4 | **Responsive cards.** A3, then Mobile → Columns 1, smaller padding, hide one decorative image | Exactly three declarations inside the mobile media query; base rules unchanged from A3's export |
| A5 | **Button with states.** Button → fill → Mouse over fill → Animate changes → Focused outline | State rules in the right order; transition on the normal rule; works in Preview by hover and by keyboard |
| A6 | **Free badge.** A box inside a card switched to Free, pinned top-right, dragged | `position: absolute; top; right` on the badge, `position: relative` on the card, nothing else changed |
| A7 | **Contact form.** Form container, three labelled fields, submit button | Valid, labelled form markup; passes html-validate and the accessibility checker with no "needs attention" issues |
| A8 | **Round trip.** Build A3, save as `.daisy`, delete, reopen, export | Byte-identical export before and after |
| A9 | **Undo marathon.** Run A1–A6 in one document, undo everything, redo everything | Empty document after undo; identical export after redo |
| A10 | **Hostile document.** Open a `.daisy` file whose custom code and HTML blocks attempt every attack in 17.2 | Editor state and stored data unchanged; nothing runs on the canvas; scripts need consent in Preview |
| A11 | **Pro CSS.** Set width to `clamp(280px, 50%, 640px)`, add `::before` with content, add a custom property, a container query in Page CSS | Values preserved exactly; controls show "custom" without altering them; export contains them verbatim |
| A12 | **Reference pages.** Three complete pages (a landing page, an article page, a product page) built by script | Full-page golden export and screenshot match at three widths |

### 17.4 Quality gates per milestone

A milestone is finished only when: all of its acceptance criteria have automated tests that pass; all earlier tests still pass; the fidelity harness passes for every fixture; and there are no known cases where a gesture writes CSS other than what this document specifies for it.

---

## 18. MVP vs Advanced vs Future Scope

### 18.1 Core MVP

The smallest version that is honestly a visual web design application: someone can design a responsive page from an empty section and publish it.

**Milestones 1 through 11.**

| Included | Detail |
|---|---|
| Clean document, Home, autosave, recovery | M1, M3 |
| Tools | Select, Direct Select, Section, Box, Text, Media, Button, Link, Place, Layout, Spacing, Eyedropper, Measure, Hand, Zoom |
| Elements | Section and landmarks, box, divider, text, heading, inline formatting, image, video, button, link, list |
| Panels | Layers, Elements, Assets, Properties, Swatches |
| Properties | General, Size, Placement (In flow and Free), Layout, Spacing, Typography, Fill, Border, Effects, Visibility |
| Responsive | Three default screen sizes plus custom ones, overrides, markers |
| Output | Preview and export of HTML, CSS and assets |
| History | Undo and redo (stack only) |

### 18.2 Advanced capabilities

Extend the editor for professional use. **Milestones 12 through 19.**

| Capability | Milestone |
|---|---|
| States and transitions | 12 |
| Transform and Gradient tools; Fixed, Sticky and Nudged placement; element Custom CSS; extra selectors; Code panel; rulers and guides | 13 |
| Keyframe animation, Timeline, scroll-into-view | 14 |
| Attributes, HTML block, custom elements, Page CSS, Page JavaScript, hardened Preview | 15 |
| Form tool, tables, remaining elements, Accessibility group and checker, Outline view | 16 |
| History panel, versions, `.daisy` files | 17 |
| Performance at scale, keyboard and screen-reader operation | 18 |
| Polish, light theme, offline | 19 |

### 18.3 Future capabilities

Not planned in this roadmap. Each is noted with what already exists in the architecture to support it.

| Capability | Architectural support already present | Not yet built |
|---|---|---|
| Multiple pages per document | `pages: Page[]`, one flat node map, per-page root, file names | Pages panel, cross-page links UI, shared header/footer |
| Reusable components (edit once, update everywhere) | Flat node map and subtree cloning | Component definitions, instances and overrides |
| Shared style classes | Styles are already class rules; tokens exist | Named classes applied to several elements, class manager |
| Web font catalogue browsing | `FontSource.kind: 'remote'` | Catalogue UI and font fetching |
| Container queries as a visual feature | Raw support through Page CSS and custom values | A UI parallel to screen sizes |
| Import of existing HTML/CSS | The model is real HTML and CSS declarations | A parser that maps arbitrary stylesheets to per-element rules |
| Image editing (crop, optimise, format conversion) | Asset store with metadata | Editing tools and codecs |
| Interactions without code (toggle a class on click, menus, tabs) | Attributes, states, `motion.js` precedent for tiny standalone scripts | An interactions model and its generated script |
| Separate-origin preview | Message-only bridge | Hosting a second origin |
| Accounts, cloud sync, sharing, collaboration | Patch-based changes are a suitable basis | Everything; requires a backend and a demonstrated need |
| Installable desktop app | Static, offline-capable build | Packaging |
| Learning / tutorial section | — | Out of scope; may later link to a separate learning project |

### 18.4 Architecture versus features

The following are built into the **architecture from Milestone 1** even though their features arrive later, because retrofitting them would mean rewriting core code:

- Styles keyed by screen size and state (features in M11 and M12).
- Patch-producing transactions (History panel in M17).
- The `target` flag in the CSS generator (export in M10).
- Asset references by id (assets in M9).
- `schemaVersion` and migrations (M3).
- `pages[]` in the model (multi-page is Future).
- The registry-driven Properties panel (M6), so that every later group is data, not new UI code.

The following are deliberately **not** built early: any plugin or extension system, any abstraction for multiple storage backends, any sync or conflict-resolution layer, and any generalised "component" concept.

---

## 19. Technical Decisions and Open Risks

### 19.1 Decision record

> **See also (2026-11-13):** `docs/adr/` records later decisions; D16, D17 and D20 are superseded by ADRs 0001, 0002, 0005 and 0011.


| # | Decision | Chosen | Main reason | Rejected |
|---|---|---|---|---|
| D1 | Default layout model | Normal flow; Free placement is explicit | Pages must adapt to content and width | Absolute positioning by default |
| D2 | Style storage | Real CSS longhand declarations as strings | Full CSS coverage, predictable export, one store for visual and code edits | Typed abstract style schema |
| D3 | Rendering | Real DOM in an iframe, overlay outside | Exact fidelity and isolation | Canvas drawing; in-document rendering |
| D4 | Source of truth | Normalised JSON document in the store | Undo, save, export and validation all need a model | DOM as truth |
| D5 | Canvas updates | Imperative renderer applying Immer patches | Minimal DOM work, no framework artefacts in the page | Rendering the page with React |
| D6 | Edit frame security | No script execution: sandbox without `allow-scripts`, allow-list renderer, CSP | Lets the editor measure the DOM directly and safely | Running user scripts while editing |
| D7 | Preview security | Sandboxed opaque-origin frame, CSP, message bridge | Isolation from storage and editor without a server | Same-origin preview; separate domain (deferred) |
| D8 | Responsive cascade | Desktop-first `max-width` by default, mobile-first optional | Matches what users see first | Mobile-first only; independent per-size styles |
| D9 | Selectors | One flat class per element, named from the layer | Equal specificity, readable, stable | Nested selectors; hashed class names; inline styles |
| D10 | Groups | A real `<div>` | Layers must equal the DOM | Editor-only virtual groups |
| D11 | Hide (eye) | Real `display: none` at the current screen size | Canvas must equal export | Editor-only hiding |
| D12 | Empty-element sizing | Real, visible starting sizes; outlines only in the overlay | No hidden editor CSS | Editor-only min sizes |
| D13 | Simple versus advanced | Per-group and per-tool disclosure; raw value always accepted | Progressive complexity without modes | Global mode switch; separate interfaces |
| D14 | Fill and Background | One group | They are the same CSS | Two groups |
| D15 | Resize versus transform | Separate gestures and tools | Different CSS, different effect on layout | One combined free-transform |
| D16 | Persistence | IndexedDB, autosave, versions, `.daisy` zip | Local-first with no backend | Server storage; `localStorage` |
| D17 | Stack | React + TypeScript + Vite, Zustand + Immer, CSS Modules, Radix primitives | Smallest set that covers the needs | Heavier frameworks and UI kits |
| D18 | Generated JavaScript | None, except a tiny optional scroll trigger | Output must not need a runtime | A Daisy runtime library |
| D19 | Panels | Fixed dock layout | Stability and simpler implementation | Free-floating, rearrangeable panels (could be added later) |
| D20 | Pages in first version | One page per document in the UI; model supports many | Keeps the first version focused | Multi-page from the start |

### 19.2 Open risks

| # | Risk | Impact | Mitigation | Checked in |
|---|---|---|---|---|
| R1 | Listeners from the editor may not fire inside a frame without `allow-scripts` in some WebKit versions | Text editing and frame-level events fail in Safari | Per-browser check; fallback to no sandbox attribute with allow-list rendering and `script-src 'none'`; Chromium is the primary target | M1 |
| R2 | `contenteditable` behaves differently across browsers and can produce unexpected markup | Corrupt inline content | `beforeinput` interception; Daisy performs formatting itself; DOM is re-rendered from the model after every commit; restricted inline set | M4 |
| R3 | Flow-first editing may feel restrictive to users expecting to drag anything anywhere | Beginners get confused when a drag reorders instead of moving | Clear insertion feedback; persistent In flow / Free switch; status hints; `Alt`-draw for free placement; validate with user testing after M2 and M7 | M2, M7 |
| R4 | Fixed elements and `vh` units are approximated on the canvas | Canvas differs from the real page in those cases | Explicit, documented exceptions (9.9); badges; Preview is exact | M11, M13 |
| R5 | Shorthand expansion with `var()` cannot be resolved reliably | Some controls show custom values instead of structured ones | Store as typed, flag opaque, never rewrite; controls degrade to text | M6 |
| R6 | A sandboxed preview can still freeze the tab or exploit a browser bug | Lost time; in the worst case, a compromised session | Save before preview; consent for imported scripts; safe start after crash; documented limitation; separate-origin preview as a later hardening step | M15 |
| R7 | Preview differs from a hosted page (opaque origin, `data:` assets) | Some scripts behave differently; large media is slow | Documented; Export dialog advises testing the exported folder; consider separate-origin preview | M10, M15 |
| R8 | Browser storage can be evicted or cleared by the user | Data loss | Request persistent storage; show quota; prompt periodic `.daisy` backup for documents not backed up in 14 days | M3, M17 |
| R9 | Storage quota exhausted by video assets | Saves fail | Per-file size limits with warnings; quota display; failed-save path keeps work in memory and offers a file save | M3, M9 |
| R10 | Grid track dragging cannot represent every template | Users with complex templates lose direct manipulation | `editable` flag; read-only display; text editing always available; never rewrite | M7 |
| R11 | Performance on very large pages (many thousands of elements) | Lag while dragging | Patch rendering, minimal measurement, virtualisation, budgets and regression tests | M18 |
| R12 | Transformed and nested-transformed elements complicate hit testing, handles and snapping | Misaligned overlays | Matrix-based overlay maths with dedicated tests; before M13, transformed elements show an axis-aligned box | M13 |
| R13 | Renaming layers changes class names used in custom code | Custom CSS or JS silently stops matching | Warn on rename when the old name appears in custom code; allow detaching the class from the name | M15 |
| R14 | Margin collapsing and other flow subtleties surprise users using the Spacing tool | "I added space and nothing happened" | Spacing tool shows computed result and the "merged with neighbour" tag | M7 |
| R15 | Scope growth in the properties system | Milestones stall | The registry makes each control independent; "Other properties" covers anything not yet given a control, so no control is ever a blocker | M6 onward |
| R16 | Browser-reserved shortcuts and differences between operating systems | Shortcuts that silently do nothing | Avoid reserved combinations; audit on Windows and macOS; every action is also reachable from a menu | M19 |

### 19.3 Questions intentionally left to the owner

These do not block implementation. Sensible defaults are already chosen in this plan.

| Question | Default in this plan |
|---|---|
| Should the default canvas width be 1440 or 1280? | 1440 |
| Dark or light theme by default? | Dark |
| Should Daisy show a "generated with" meta tag in exports? | No (option, off) |
| Is Safari a supported browser at first release or best-effort? | Best-effort; Chromium-based browsers and Firefox supported |
| Maximum single asset size? | 25 MB for images, 200 MB for video, with a warning above 50 MB |

### 19.4 How to use this plan

Implement milestones in order. Within a milestone, do tasks top to bottom; each is written to be completed and verified on its own. When a task touches behaviour specified in chapters 3 to 14, that chapter is the specification: implement exactly the CSS, HTML and interaction it states. If implementation reveals that a stated behaviour is wrong or impossible, change this document first, with the reason recorded in 19.1 or 19.2, and then change the code.

