# Daisy — UI/UX Design Plan

**Stage 1 of 2: product UX and visual design.**
**Status:** Draft v0.2. D-04 and the corner roundness component are designed and in review. Not approved.
**Date:** 2026-11-11 · **Updated:** 2026-11-12 (see change log 13.2)

This document is the source of truth for how Daisy looks and behaves. It describes screens, components, states and interactions. It does not describe code, data structures or architecture. Those belong to Stage 2 (`PLAN.md`), which is written only after this design is approved.

---

## 0. How this document is used

### 0.1 The workflow

| Step | What happens | Output | Who |
|---|---|---|---|
| 1 | This specification is reviewed as text | Comments on this file | Owner |
| 2 | The **design system sheet** is built in Claude Design (chapter 12, phase A) | Design system screen | Claude Design |
| 3 | The **workspace shell** and the **key editor screen** are built and reviewed | Screens D-01 to D-03 | Claude Design, Owner |
| 4 | Interaction states are built in batches, each reviewed before the next (phases C–G) | Screens D-04 to D-34 | Claude Design, Owner |
| 5 | Every change requested during review is written back into this document (chapter 13) | Updated spec + change log | Claude |
| 6 | **Approval gate:** the owner signs off the checklist in 13.3 | Status becomes "Approved v1.0" | Owner |
| 7 | Only then is the Stage 2 technical plan written, with every task referencing a screen ID (D-xx) and a section of this document | `PLAN.md` | Claude |
| 8 | Code is written last | Application | — |

Rule: design first, approve second, architect third, code last. No step starts before the previous one is finished.

### 0.2 Note about the existing `PLAN.md`

`D:\Mine\daisy\PLAN.md` exists already. It is an early engineering draft that was written before this gate was put in place. Its product and UX chapters (1–8) were used as input to this document. Where the two documents disagree, **this document wins**. The draft is not approved, and it must be rewritten in Stage 2 against the approved design.

### 0.3 Screen IDs

Every designed screen has an ID (`D-01`, `D-02`, …), listed in chapter 11. Stage 2 tasks and later change requests refer to these IDs.

### 0.4 Conventions

- Shortcuts are for Windows. On macOS `Ctrl` becomes `Cmd` and `Alt` becomes `Option`.
- **Canvas** means the editing workspace. **Page** means the web page being designed. **Document** means the saved Daisy project.
- All sizes are in CSS pixels at 100% UI scale. The reference design frame is **1920 × 1080**. A secondary check frame is **1440 × 900** (13.3).

---

## 1. Product UX Architecture

### 1.1 What Daisy is, in one line

**The creative freedom of an image editor, applied to real HTML and CSS.** You use tools to draw, place, move, resize and style elements. Every action edits a real web page rendered by the browser. The output is a folder of plain files.

### 1.2 Design pillars

These are the tests every screen is checked against during review.

| # | Pillar | What the reviewer should see |
|---|---|---|
| U1 | **It feels like a professional creative tool** | A dense, calm, dark workspace. The canvas dominates the screen. Chrome is flat, precise and quiet. Nothing looks like a marketing site or a website builder. |
| U2 | **Tools first, panels second** | The tool strip and canvas handles are the main way to work. Panels show and accept values. |
| U3 | **Progressive complexity everywhere** | Every tool and every property group works with simple controls, and has its own **Advanced** disclosure in the same place. There is no global beginner or pro mode. |
| U4 | **The web is visible, not hidden** | Real tags, flow, nesting and screen sizes are always visible: name tags show `Text · p`, Layers is the DOM tree, and a chip shows which screen size is being edited. |
| U5 | **Plain words first, CSS names one hover away** | Labels say "Space inside". Tooltips say `padding`. |
| U6 | **Clean start** | A new document is one empty section. There are no templates or starter blocks anywhere. |
| U7 | **Nothing changes silently** | When Daisy changes something the user did not touch, it says so in a status-bar notice, and the change is part of the same undo step. |
| U8 | **One consistent vocabulary of components** | The same field, disclosure, chip and menu look and behave the same in every panel, popover and dialog. |

### 1.3 Users

| User | Needs | How the design serves them |
|---|---|---|
| Beginner | A good-looking page without knowing HTML/CSS | Obvious defaults, plain labels, direct manipulation, inline one-line hints that can be dismissed for good |
| Designer / developer | Full control of structure, layout, responsive behaviour and code | Advanced disclosures, raw CSS values in any field, editable tags and attributes, Code drawer |

Both users see the same interface.

### 1.4 Application map

```
Home ──┬── New project dialog ──► Editor (project open, first page in a tab)
       ├── Open project… ────────► Editor
       ├── Open file… ───────────► Editor (single file in a tab)
       └── Recently deleted

Editor (one window, pages open as tabs)
 ├── Top bar ─── brand mark, menus, search (Ctrl+P), undo/redo, Preview, Export ▾
 ├── Options bar ─── active tool's options · screen size switcher · page settings · Snap · More
 ├── Tool strip ─── 18 tools in 4 groups
 ├── Left dock ─── Project (top) · Layers | Elements | Assets (bottom)
 ├── Page tabs ─── one tab per open page or single file
 ├── Canvas ─── page + overlay (selection, guides, handles)
 ├── Right dock ─── Properties (top) · Swatches | History (bottom)
 ├── Bottom drawer ─── Code | Timeline (collapsed by default)
 ├── Status bar ─── breadcrumb, hint, zoom field, page size, pointer position
 ├── Modes ─── Edit (default) · Text editing · Preview (full canvas)
 └── Dialogs ─── New project · Page settings · Screen sizes · Export · Versions
```

Daisy has only five dialogs. Everything else is inline, a popover or a menu.

### 1.5 Editor modes

| Mode | Entered by | Visual signal | Exit |
|---|---|---|---|
| Edit | Default | Normal chrome | — |
| Text editing | Double-click text, or click with the Text tool | Thin solid blue outline with no handles, browser caret, options bar shows text formatting | `Esc`, or click outside |
| Preview | `Ctrl+Shift+Enter` or the ▶ Preview button | Left and right docks and the tool strip collapse. A slim preview bar replaces the options bar. The page becomes interactive. | `Esc`, or the "Back to editing" button |
| Panels hidden | `Tab` | Docks, tool strip and options bar hide. Only the canvas and a 24 px top strip remain | `Tab` |

### 1.6 Projects, pages and single files

Daisy works like a code editor such as Code::Blocks: you can open **one file** and edit it, or create a **project** that holds many pages. Open pages show as **tabs** above the canvas, like documents in Photoshop.

| Concept | What it is | Where it shows |
|---|---|---|
| Project | A folder of pages that share one design system and one asset library | Project panel (3.1), search bar placeholder ("Search Halden") |
| Page | One HTML page inside a project (`index.html`, `shop.html`, …) | Project panel → Pages; a page tab when open |
| Design system | The project's colours, text styles, radius and spacing tokens. Every page in the project uses it | Project panel → Design system; Swatches ("From Halden design system"); token links in fields (C-33) |
| Collection | A list of items with the same fields (products, posts), kept as a file in the project; repeats a designed card and can make one page per item | Project panel → Collections (D-57) |
| MCP | Model Context Protocol, the open standard AI apps use to reach tools. Daisy is an MCP server: apps such as Claude Code or Cursor read and edit the open project | Preferences › AI tools and MCP (D-59) |
| Component | A reusable piece with variants and options; editing it updates every use | Project panel → Components (D-58) |
| Shared part | A piece used on several pages (header, footer). Edited once, it changes on every page; a page can keep its own changes | Project panel → Shared parts; diamond icon in Layers and on the canvas (D-53) |
| Single file | An HTML file opened on its own, outside any project. It has no shared design system | Project panel → Single files; a page tab with a file icon and the tooltip "Single file · not part of a project" |

Rules:
- Each tab keeps its own screen size, zoom, scroll position, selection and undo history.
- Switching tabs never changes another page.
- Closing a tab with unsaved changes asks to save. An unsaved tab shows a dot in place of its ×.
- A single file can be added to a project later (Project panel ⋯ → Add file to project).

---

## 2. Complete Application Screen Layout

### 2.1 Editor layout at 1920 × 1080

```
y=0    ┌────────────────────────────────────────────────────────────────────────────────────────────┐
       │ TOP BAR                                                                              h 40  │
y=40   ├────────────────────────────────────────────────────────────────────────────────────────────┤
       │ OPTIONS BAR                                                                          h 36  │
y=76   ├──────┬───────────────┬─────────────────────────────────────────────────┬───────────────────┤
       │ TOOL │ LEFT DOCK     │ PAGE TABS [Home][Shop●][Journal][promo…][+] ⌄          h 32 │ RIGHT DOCK │
       │ STRIP│ w 260         ├─────────────────────────────────────────────────┤ w 300             │
       │ w 44 │ Project       │ CANVAS                                          │ Properties        │
       │      │ ───────────── │ w 1316 (fills)                                  │                   │
       │      │ Layers        │      ┌──────── page 1440 @ 85% ──────────┐      │                   │
       │      │ Elements      │      │                                    │      ├───────────────────┤
       │      │ Assets        │      │                                    │      │ Swatches│History  │
       │      │               ├──────┴────────────────────────────────────┴──────┤ h 220 (resizable) │
       │      │               │ BOTTOM DRAWER tabs (collapsed)              h 28 │                   │
y=1056 ├──────┴───────────────┴─────────────────────────────────────────────────┴───────────────────┤
       │ STATUS BAR                                                                           h 24  │
y=1080 └────────────────────────────────────────────────────────────────────────────────────────────┘
```

| Region | Size | Background token | Notes |
|---|---|---|---|
| Top bar | full width × 40 | `bg-titlebar` | Bottom border 1 px `line-subtle` |
| Options bar | full width × 36 | `bg-toolbar` | Bottom border 1 px `line-subtle` |
| Tool strip | 44 × fill | `bg-chrome` | Right border 1 px `line` |
| Left dock | 260 (min 200, max 420) × fill | `bg-panel` | Right border 1 px `line`; resize by dragging the edge. Project panel on top, Layers / Elements / Assets below |
| Page tabs | canvas width × 32 | `bg-chrome` | Sits over the canvas only, like Photoshop document tabs (2.7) |
| Canvas | fills the rest | `bg-workspace` | Contains the page frame and overlay |
| Right dock | 300 (min 260, max 480) × fill | `bg-panel` | Left border 1 px `line` |
| Bottom drawer | canvas width × 28 collapsed, 280 open (resizable 160–60%) | `bg-panel` | Sits under the canvas only, not under the docks |
| Status bar | full width × 24 | `bg-chrome` | Top border 1 px `line` |

The canvas area at the reference frame is 1316 × 920 px with the drawer collapsed. "Fit width" zoom shows the 1440 px Desktop page at **85%**, so it is 1224 px wide on screen with 46 px of workspace on each side.

### 2.2 Top bar (h 40)

The top bar holds **app-level** controls only. Anything that belongs to one page (screen size, zoom, page settings) lives in the page tab row (2.7).

```
┌─[✿]─File Edit Element View Help──────────[ ⌕ Search Halden            Ctrl P ]──────────↶ ↷ │ [▶ Preview] [⇪ Export ▾]─┐
```

Three-column grid (left `1fr` · centre `auto` · right `1fr`), 8 px side padding, 16 px column gap.

| Item | Spec |
|---|---|
| Brand mark | 28 × 28 tile, radius 6, `bg-panel` with a 1 px inner `line` ring. 18 px daisy glyph: eight petals in `text-primary`, centre `brand-daisy`. The only brand colour in the chrome. Click goes to Home |
| Menus | Text buttons, 12 px, `text-secondary`, 8 px horizontal padding, height 28, radius 4 |
| Search bar | Centred. 440 × 28, radius 6, `bg-panel`, 1 px inner `line` ring. Search icon (13), then "Search **Halden**" (project name in `text-primary` 500; for a single file, the file name), and two key badges "Ctrl" "P" on the right (18 h, radius 3, `bg-control`, 1 px bottom inset `bg-control-active`, 10 px medium). Searches pages, layers, assets and settings; typing `>` switches to commands, like VS Code. Replaces the document name and save status |
| Undo / Redo | 28 × 28 icon buttons, radius 4. Disabled at 35% opacity. Tooltip names the action: "Undo Resize · Heading · Ctrl+Z" |
| Separator | 1 × 16 px `line` |
| Preview | Outline button: 28 h, radius 6, 1 px inner `bg-control-active` ring, play icon (12) + "Preview" (12 px medium) |
| Export | Split primary button: 28 h, radius 6, `accent-fill` with white text. Left: upload icon + "Export". 1 px white-25% divider. Right: 24 px ▾ opening Zip download / Write to folder |

Save state: no permanent indicator in the top bar. An unsaved page shows a dot on its tab (2.7). Errors such as "Not saved — storage full" appear as a `danger` notice in the status bar.

### 2.3 Options bar (h 36)

The options bar shows **only the active tool's options**. It does not repeat the tool name or the selection: the tool strip already shows the active tool, and the Properties header, Layers and the status bar breadcrumb already show the selection.

Structure, always in this order:

```
[context chip] │ capsules of primary options … ──────── [🖥 Desktop 1440 | ▭ | ▯ | +] [⚙] │ [Snap] [⋯]
```

- **Start**: the first capsule lines up with the left dock's content (52 px from the window edge: 44 px tool strip + 8 px).
- **Capsules**: related controls sit together in a holder: 28 h, radius 6, 2 px padding, `bg-capsule`. Inside, controls are 24 h, radius 4, with no field fill at rest; hover shows `bg-control-hover`. 6 px between capsules; 1 × 14 `bg-control-active` dividers split groups inside a capsule. Capsules replace the old separator lines. Order for Select: X · Y | W · H, then Placement (In flow / Free with icons), then Align (3 | 3), then Distribute (horizontal, vertical; disabled until 3 or more are selected, tooltip says so), then Corner roundness.
- **Size modes** (Fixed / Fit / Fill) show as a small tag after the value: 16 h, padding 0 5, radius 3, `bg-control-active`, 10 px `text-secondary`. The same tag is used in Properties.
- **Corner roundness** uses the corner roundness control (C-33).
- **Context chip**: a pill, 20 px high, 11 px medium text. Responsive uses `resp` colours: "Editing: Tablet and smaller". State uses `state` colours: "Editing: Mouse over". When both apply there are two chips. A chip has a × that returns to Desktop or Normal.
- **Screen size switcher and Page settings** sit at the right, before a 1 × 16 divider, so the size being edited is always in view next to the tool options. Switcher: capsule 28 h, active segment icon + name + muted width ("Desktop 1440") on `bg-control-active`, inactive segments icon only (tooltip "Tablet · 768"), `+` opens the Screen sizes dialog. Page settings: 28 × 28 gear, radius 6, `bg-capsule`. Both apply to the page in the active tab and change when you switch tabs.
- **Snap** toggle and **⋯ More** (28 × 28, radius 6, `bg-capsule`) sit at the far right. More opens a popover with the tool's advanced options (6.1).
- If the options do not fit, the lowest-priority capsules move into More. Every tool has a defined priority order (chapter 4).

### 2.4 Tool strip (w 44)

- Tool buttons are 32 × 32, centred, with 2 px between buttons and 8 px plus a 20 px separator line between groups.
- The icon is 16 px in `text-secondary`. Hover: `bg-control-hover` and `text-primary`. Active: `accent-subtle` background, accent icon and a 2 px accent bar on the left edge of the strip.
- Tools with variants have a 4 px triangle in the bottom-right corner. Press and hold (300 ms), or right-click, to open a flyout. The flyout lists each variant with its icon, name and shortcut, and a check mark on the current one.
- A tool locked for repeated use (double-click) shows a 4 px accent dot in its top-right corner.
- At the bottom of the strip are two 20 × 20 overlapping swatches (fill and text colour of the selection, or the defaults) and a small ⇄ swap.

### 2.5 Status bar (h 24)

```
Page › Section · Hero › Box · Hero text › Heading · h1        Drag a handle to resize · Shift keeps proportions        [85% ▾] │ 1440 × 3120 · x 612  y 288
```

- **Zoom field** on the right, just before the page size and pointer position, separated from them by a 1 × 12 `line` divider, so all the "where am I" readouts sit together: 18 h, `bg-control`, radius 2, 11 px tabular value. Type a value (e.g. `150`) and press Enter, or open ▾: Zoom in, Zoom out, Fit width (`Shift+1`), 50%, 100% (`Shift+0`), 200%, Zoom to selection (`Shift+2`). The value updates live while zooming.

- The breadcrumb is 11 px. Each segment is clickable, and hovering one outlines that element on the canvas. The last segment is `text-primary` and the rest are `text-secondary`. Long paths collapse the middle into "…".
- The hint is centred, 11 px, in `text-muted`.
- **Notices** (pillar U7) temporarily replace the hint. They have an info icon, `info` text colour, an "Undo" link, and last 6 seconds or until the next action. Example: "ⓘ Changed Hero to Column so its children can be aligned · Undo".
- The right side shows page size and pointer position in page coordinates, in tabular numerals.

### 2.6 Bottom drawer

- Collapsed, it is a 28 px tab strip: "Code" and, when available, "Timeline", plus a ▴ expand control on the right.
- Open, it is 280 px. The tab strip stays on top, and the area underneath is the active tab's content. Drag its top edge to resize.

### 2.7 Page tabs (h 32)

Open pages and single files show as tabs over the canvas, like documents in Photoshop. The active tab's name shows its zoom ("@ 85%"); the zoom control itself is in the status bar (2.5).

```
[▔Home index.html @ 85% ×][Shop shop.html ●][Journal journal.html][🗋 promo-banner.html] [+] [⌄] ────── [🖥 Desktop 1440 | ▭ | ▯ | +] 85% ▾ ⚙
```

| Item | Spec |
|---|---|
| Tab | Height 32, padding 0 8 0 12, 8 px gap, 1 px right divider `line-subtle`. Page name (12 px), then file name in mono 11 `text-muted`; the active tab adds "@ 85%" |
| Active tab | `bg-workspace` (joins the canvas, no bottom border), 2 px accent line on top, name `text-primary` 500, × close button (18 px, radius 3) |
| Inactive tab | Transparent on `bg-chrome`, `text-secondary`. × appears on hover |
| Unsaved | A 7 px dot in `text-secondary` replaces the ×; tooltip "Unsaved changes" |
| Single file | 12 px file icon before the name; tooltip "Single file · not part of a project" |
| New tab | 32 × 32 `+` (New page, `Ctrl+N`) after the last tab |
| Overflow | ⌄ lists all open tabs; tabs shrink to a 120 px minimum first |
| Reorder | Drag a tab; drag it out to the Project panel to close it |

---

## 3. Navigation and Panel Organization

### 3.1 Left dock: Project (top) · Layers | Elements | Assets (bottom)

#### Project

A management tree like Code::Blocks, always visible at the top of the left dock (its height fits its content; drag the divider to resize).

```
┌ Project ─────────────────────── 🗋+ ⋯ ┐
│ ▾ 🗀 Halden                            │
│   ▾ Pages                          4  │
│       🗋 Home            index.html   │  ← page in the active tab: bg-control, text-primary 500
│       🗋 Shop             shop.html   │
│       🗋 Journal       journal.html   │
│       🗋 Visit           visit.html   │  ← closed page: dimmer icon
│   ▸ Design system         ■■■■■      │  ← 8 px mini swatches of the project colours
│   ▸ Assets                       12   │
│ ───────────────────────────────────── │
│ SINGLE FILES                          │  ← 10 px caps caption, text-muted
│   🗋 promo-banner.html                │
└───────────────────────────────────────┘
```

- Header 32 px: "Project" (12 px medium), New page button (`Ctrl+N`), ⋯ menu (New project, Open file…, Add file to project, Project settings).
- Rows are 24 px, same tree rules as Layers. File names in mono 11 `text-muted`, right-aligned.
- Double-click a page to open it in a tab. Opening Design system opens the design system editor (D-36).

#### Layers | Elements | Assets

The tab header is 32 px high with tabs as text (12 px medium). The active tab is `text-primary` with a 2 px accent underline. Inactive tabs are `text-secondary`. Layers is the default tab.

#### Layers

```
┌ Layers ────────────────────── ⌕ ☰ ┐
│ [ Filter layers…            ] [≡] │   ← filter field; [≡] toggles Outline view
│ Top of page ↑                      │   ← 10 px muted caption
│ ▾ ▭ Header                 header │
│   ▸ ▭ Nav bar                  div │
│ ▾ ▭ Hero                  section │
│   ▾ ▦ Hero grid                div │  ⊞ ← grid icon because it arranges as grid
│     ▾ ▭ Hero text              div │
│       ▪ T Hand-thrown ceramics… h1 │  ← selected row
│         ¶ Small-batch stoneware… p │
│         ◉ Shop the collection button│
│       ▣ Hero image             img │  ⚠
│ ▸ ▭ This season           section │  🖥
│ ▸ ▭ Footer                 footer │
└────────────────────────────────────┘
```

| Element of a row | Spec |
|---|---|
| Height | 24 px. Indentation is 12 px per level. Indent guides are 1 px `line-subtle` vertical lines |
| Disclosure | 12 px chevron, only for elements with children |
| Type icon | 14 px. Different icons for stack, row (horizontal bars), grid (2×2), text (¶), heading (T), image, button, link, form field, list, table, embed, section |
| Name | 12 px `text-primary`. Text elements show their first words in quotes when they have no custom name |
| Tag | 11 px `text-muted`, right-aligned |
| Hover actions | Eye and lock icons (14 px) appear at the right and replace the tag while hovering |
| Badges | 12 px glyphs after the name. 🖥 = overrides at smaller screen sizes, ⌖ = state styles, ⚡ = animation, 🔗 = link, `</>` = custom CSS, ⚠ = accessibility issue (`warning` colour), ◇ = Free placement |
| Selected | `accent-subtle` background, `text-primary`. When the canvas does not have focus, `bg-control-active` |
| Ancestor of selection | Its name is shown in `text-primary` and it is not dimmed |
| Hidden at this size | Row at 45% opacity, with a crossed-out eye that stays visible |
| Locked | Lock icon stays visible |
| Drop "between" | A 2 px accent line at the target indent, with a 6 px circle at its start |
| Drop "inside" | Row background `accent-subtle` with a 1 px accent outline |
| Invalid drop | A 2 px `danger` line and a tooltip with the reason |
| Rename | Double-click the name and it becomes an inline field |

Outline view (toggle [≡]): lists only headings and landmarks as `H1 Hand-thrown ceramics…`, `H2 This season`, `main`, `nav`, with level indentation. A skipped level is shown with a ⚠.

#### Elements

- Search field at the top ("Search elements… e.g. picture, list, nav").
- Collapsible categories: Structure, Text, Media, Links & buttons, Lists, Tables, Forms, Embeds, Custom.
- Each row is 28 px with an 16 px icon, a friendly name and a muted tag: `Paragraph   p`.
- Click arms the Place tool, and the row stays highlighted. Drag it onto the canvas or Layers. Double-click inserts it after the selection.
- No row is a pre-built block. Compound elements (List, Table, Navigation) create the smallest valid structure, and the row says so in muted text: "List · 3 items".

#### Assets

- Sub-tabs: Images · Video & audio · Fonts · Other. "Upload" is a secondary button, and the panel accepts files dropped on it.
- Images use a 2-column thumbnail grid (118 × 88 thumbnails with 4 px gaps). Under each are the file name (11 px), the dimensions and size (10 px muted), and a usage count chip ("2 uses"). Clicking the chip selects those elements.
- Fonts show as rows with the font name in its own face, the weights available, and a usage count.
- Empty state: an icon, "Drop images, video or fonts here", and an Upload button.

### 3.2 Right dock: Properties (top) · Swatches | History (bottom)

The Properties panel is described in chapter 5.

#### Swatches

- **Colours**: a grid of 24 × 24 swatches with 6 px gaps. Hovering shows the name and value ("brand · #b5532d"). Click applies to the fill, Shift+click to text colour. A dashed `+` tile at the end ("Add from selection").
- **Text styles**: rows with a 28 px sample "Ag" in the style, the name, and "Fraunces 48 / 1.1" in muted text.
- Right-click a swatch: Edit, Rename, Copy CSS variable (`var(--brand)`), Delete (shows how many uses).
- In a project the header reads "Colours · From Halden design system" (10 px `text-muted`, right-aligned): swatches belong to the project, not the page. A single file has its own page-level swatches.
- Text style rows are 32 px high.

#### History

- One row per action, newest at the bottom: a 14 px icon, the action name ("Resize · Heading") and a muted time.
- The current position is highlighted with `accent-subtle`. Undone entries below it are at 40% opacity. Click an entry to jump there.
- Saved versions appear inline as a divider: "— Version: Before mobile pass · 21:40 —".

### 3.3 Menus (complete contents)

Drawn on **D-38** (v0.2). "▸" opens a submenu; ✓ marks an item that is on; a muted note after a label shows the current value.

| Menu | Items |
|---|---|
| File | New project… `Ctrl Alt N` · New page `Ctrl N` · Open… `Ctrl O` · Open recent ▸ (Projects; Single files; Clear recent) · — · Save version… `Ctrl S` (note "autosaved") · Versions… `Ctrl Alt S` · — · Import ▸ (images and media, HTML page, tokens) · Export… `Ctrl Shift E` · — · Page settings… · Project settings… · — · Close page `Ctrl W` · Close project · Back to Home `Ctrl Shift H` |
| Edit | Undo `Ctrl Z` (names the change, e.g. "Change fill") · Redo `Ctrl Shift Z` · History · — · Cut · Copy · Copy as ▸ (HTML, CSS `Ctrl Alt C`, CSS variables used, Style, Image PNG) · Paste · Paste inside `Ctrl Shift V` · Paste style `Ctrl Alt V` · Duplicate `Ctrl D` · Delete · — · Select all `Ctrl A` · Select same ▸ (tag, class, fill, text style) · Find and replace… `Ctrl H` · — · Preferences… `Ctrl ,` |
| Element | Wrap in ▸ `Ctrl G` (Box, Row, Grid, Link, Section) · Unwrap `Ctrl Shift G` · Wrap in link `Ctrl K` · — · Move earlier `Ctrl [` · Move later `Ctrl ]` · Placement ▸ (In flow ✓, Free, Fixed to screen, Sticks when scrolling, Placement options…) · — · Add state ▸ · Animate… · Save as preset… · — · Rename `F2` · Lock `Ctrl L` · Hide `Ctrl Shift H` · — · Show code `` Ctrl ` `` · Delete element (danger) |
| View | Zoom in · Zoom out · Fit width `Shift 1` · 100% `Shift 0` · Zoom to selection `Shift 2` · — · Screen size ▸ (Desktop 1440 ✓, Tablet 768, Mobile 390, Rotate, Screen sizes…) · Preview `Ctrl Enter` · Outline view `Ctrl Y` · — · Rulers ✓ · Guides ✓ · Layout grid · Fold line ✓ · Snap ✓ · — · Panels ▸ · Code · Timeline · Hide panels `Tab` · — · Theme ▸ (Dark, Light, System) |
| Help | Search commands `Ctrl P` · Keyboard shortcuts `Ctrl /` · Getting started · Show tips again · — · What's new · Report a problem… · Check for updates · — · About Daisy |

**Behaviour.** Click a name to open its menu; while one is open, hovering another name switches to it. Click outside or `Esc` closes. `Alt` or `F10` focuses the bar; ← → between menus, ↑ ↓ through items, → opens a submenu, Enter runs. Submenus open after 150 ms and stay open while the pointer moves towards them. Items that do not apply are **disabled, not hidden**, with a tooltip that says why ("Redo · nothing to redo"). Every command is also in the search bar (`Ctrl P`) with the same name and shortcut. In the Design system tab, Element is disabled, and so are the canvas items in View.

Menu visuals are in component C-16 (chapter 9).

---

## 4. Tool Inventory and Contextual Options Bar

### 4.1 Inventory

There are 18 tools in four groups. A feature gets a tool only if it needs its own pointer behaviour on the canvas. Everything else is a property group.

| Group | Tool | Key | Variants | Icon concept (16 px, outline) |
|---|---|---|---|---|
| Select | Select | `V` | — | Solid arrow pointer |
| | Direct Select | `A` | — | Hollow arrow pointer |
| Create | Section | `S` | Section, Header, Footer, Main, Navigation, Article, Sidebar (as Kind option) | Wide rectangle spanning the frame |
| | Box | `R` | Box, Ellipse, Divider | Rectangle |
| | Text | `T` | Text, Heading | Capital T |
| | Media | `I` | Image, Video, Audio, Embed, Icon | Frame with mountain and sun |
| | Button | `B` | — | Rounded rectangle with a line |
| | Link | `L` | — | Two chain links |
| | Form | `F` | Text field, Text area, Dropdown, Checkbox, Radio, Label, Form container | Field with caret |
| | Place | `N` | (armed element) | Plus in a dashed square |
| Shape | Layout | `G` | — | Square split into one tall and two stacked cells |
| | Spacing | `P` | — | Square inside a dashed square |
| | Transform | `Q` | — | Square with a rotation arrow |
| | Gradient | `D` | — | Square fading dark to light |
| Inspect | Eyedropper | `E` | — | Pipette |
| | Measure | `M` | — | Ruler |
| | Hand | `H` / hold `Space` | — | Open hand |
| | Zoom | `Z` | — | Magnifier |

Temporary tools: hold `Space` for Hand, hold `Ctrl` for Direct Select, hold `Alt` with Select to show distances. Releasing the key returns to the previous tool. While a temporary tool is held, the tool strip shows it with a dashed outline instead of a filled highlight.

### 4.2 Shared tool behaviour (shown on every creation tool)

- **Click** creates at the default size at the insertion point. **Drag** draws the size.
- Placement defaults to **In flow**. Every creation tool's options bar has the same segmented control, `Place: In flow | Free`. Holding `Alt` while drawing creates a Free element at exactly the drawn rectangle.
- After creating, the tool returns to Select (unless it is locked).
- `Esc` cancels the current gesture. A second `Esc` returns to Select.

### 4.3 Options bar per tool

Each row lists the clusters in priority order (1 is kept longest when space is short). "More" lists what lives in the popover.

| Tool | Primary options (in order) | More ▸ popover |
|---|---|---|
| Select (nothing selected) | Auto-select: Scoped / Deepest · Snap ☐ | Snap distance, snap to siblings / parent / guides, nudge distance, "Resize keeps unit" |
| Select (element selected) | 1 X · Y · W · H fields (W/H show mode: Fill/Fit/Fixed) · 2 `Place: In flow | Free` · 3 align ⫷ ⫿ ⫸ ⊤ ⊥ ⊥ · 4 distribute · 5 corner roundness (C-33) | Same as above, plus lock proportions and pin widget for Free |
| Direct Select | Same as Select | Click through locked · Select inline text parts |
| Section | Kind ▾ (Section, Header, Navigation, Main, Article, Sidebar, Footer) · Content Contained / Full width · Keep tool (name, id, min height, background in Properties, D-43) | Tag override · Add id for linking |
| Box | Variant (Box / Ellipse / Divider) · Fill swatch · Border · Roundness · Place | Tag ▾ (div, section, article, aside, header, footer, nav, main, figure, span) · Create empty (no fill, fill width) |
| Text | Kind (Text / Heading 1–6) · Font ▾ · Weight ▾ · Size · Colour · Align ⫷⫿⫸≡ · **B** *I* U · 🔗 | Tag ▾ · Line spacing · Letter spacing · Paste as plain text |
| Media | Variant · Source (Upload / Assets / URL) · Fit ▾ · Describe this image [field] | Loading lazy/eager · srcset & sizes · picture sources · video: controls/autoplay/loop/muted/poster · embed sandbox flags · inline SVG vs img |
| Button | In flow / Free · The button: Goes somewhere (`a`) / Runs an action (`button`) · Keep tool (look and destination are in Properties, D-41) | Type ▾ (for `button`) · Disabled · Add mouse-over style |
| Link | Destination type (Web address / Section / Email / Phone / File) · [value] · Open in new tab ☐ | rel · download · Link whole element / selected text |
| Form | Variant ▾ · Type ▾ · With label · Keep tool (Label, Placeholder, Required and Data are in Properties, D-42) | name · value · autocomplete · min/max/step/pattern · options editor · radio group · action/method · Create without label |
| Place | In flow / Free · After placing: Select it / Stay armed · Show preview · Only valid spots (the armed element shows in the Elements panel, the element card and the Properties header) | **Place Advanced popover** from Properties › What gets created: Tag (`ul` · `ol` · `menu`, same-meaning tags only) · Where it goes (Before · Inside start · Inside end · After, keyboard Tab cycles) · Wrap the selection · Place into every match · Accessible name `aria-label` · id · class · + Attribute · Style (From design system / Bare HTML) · Save as preset (to Elements › Custom) |
| Layout | Arrange: Stack / Row / Grid · Row: direction, 3×3 alignment grid, Spread ▾, Wrap, Space between · Grid: Columns ±, Rows ±, Space between, alignment grid · "Edit on canvas" link | **C-38 (D-37)**. Row: Direction incl. reverse (picture buttons) · Main axis (`justify-content`: start, centre, end, between, around, evenly) · Cross axis (`align-items`: start, centre, end, stretch, baseline) · Wrap (no wrap, wrap, reverse) · Lines (`align-content`) · separate Row/Column gap with link · live preview · CSS line + Copy CSS. Grid: column and row **track chips** with a per-track editor (fr, px, auto, min–max, fit-content) · presets (Equal, Sidebar + main, Auto-fit cards, 12 columns) · gaps · Fill order (`grid-auto-flow`, dense) · Items inside cells (`justify-items`, `align-items`) · Named areas (drag across cells to merge, type to rename) · live preview · CSS line. Other display values (`inline`, `inline-flex`, `contents`…) in `display ▾`. Multi-column text |
| Spacing | Inside: T R B L + link · Outside: T R B L + link · Space between | Unit · Drag affects: one / opposite / all sides · Allow negative · Outside auto · Logical properties · Step size |
| Transform | Rotate ° · Scale % · Move X · Y · Origin (9-point) · Flip H/V | Skew · 3D rotate · Perspective · Raw function list · Use individual properties · Reset |
| Gradient | Type (Linear / Radial / Conic) · Stop strip (inline mini) · Angle ° | Repeating · Interpolation space · Stop units · Apply to text · New layer / Replace |
| Eyedropper | Apply to: Fill / Text / Border · Sample: Pixel / Element colour | Pick up full style · Add to swatches |
| Measure | Units: px / rem / % · Measure from: border / content / outside · All four sides · To parent edges · Keep pins | **Measure Advanced popover** from Properties › Measure: pinned measurements (eye, live update, Shift+click adds) · the same gap across screen sizes · "Why" explanation with fixes (match the grid gap, snap to a spacing token) · Copy as Value / CSS / Spec note / Image with redlines |
| Hand | Scroll to section ▾ | — |
| Zoom | − 85% + · Fit · 100% · Selection | Scrubby zoom |

**Text editing mode** replaces the bar with: `Text editing` · Kind ▾ · Font ▾ · Weight ▾ · Size · Colour · **B** *I* U S · 🔗 · Align · `Done (Esc)` on the right.

---

## 5. Properties Panel Structure

### 5.1 Anatomy

The panel shows **only what the element actually uses**. Groups with values are open; everything else is one quiet line in "More properties".

```
┌ Properties ────────────────────────────────┐
│ T  Hero title                     Normal ▾ │ ← header, two lines
│    Heading 1 ▾ · h1                        │
├────────────────────────────────────────────┤
│ Size                                    ⚙︎ │ ← group title + Advanced icon
│ [• W 560   Fixed] [  H 202     Fit]        │ ← paired fields, labels inside
├────────────────────────────────────────────┤
│ Typography                              ⚙︎ │
│ [• Fraunces                          ▾]    │
│ [• Semibold      ▾] [• 64           px]    │
│ [■ ink             ] [↕ 1.05           ]   │
│ [≡][≡][≡]                       I  U  S    │
├────────────────────────────────────────────┤
│ MORE PROPERTIES                            │
│ Placement                         In flow  │
│ Spacing                                 0  │
│ Fill                                 none  │
│ Effects                               [+]  │ ← hover: row highlights, + appears
│ …                                          │
└────────────────────────────────────────────┘
```

| Part | Spec |
|---|---|
| Header | Padding 10 12, 4 px between lines. Line 1: element icon (16), editable name (12 px medium), State selector on the right (ghost dropdown 22 h; when not Normal it is pressed with an accent ring and a small violet ⌖ icon). Line 2, indented 24: Kind dropdown (11 px `text-secondary`) · tag in mono 11 `text-muted`. Replaces the General group's Name and Kind rows |
| Context strip | 24 px with a `resp-subtle` background, a device icon and the text "Tablet and smaller · 2 values set here", plus a ⋯ menu: Review values, Clear all at this size |
| Group | Padding 4 12 12, 8 px between rows. Title row 28 px: group name (12 px semibold) and a 24 px **Advanced** icon button (sliders glyph, `text-muted`; accent dot when something is set inside). 1 px `line` divider between groups |
| Fields | 24 h, `bg-control`, radius 2, **no border at rest**, 1 px `line-strong` on hover, accent ring on focus, 6 px padding, 6 px inner gap. Short label inside the field (W, H) in 11 px `text-muted`; the full name and CSS property in the tooltip. Related values pair up in a 2-column grid with 8 px gap |
| Origin marker | A 5 px dot at the start of the field (inside it). **Solid accent** = set at this size or state. **Hollow `resp`** = inherited from another screen size (tooltip: "From Desktop: 48px"). **Hollow `text-muted`** = from parent element (Typography only). **None** = not set |
| Size mode | A tag after the value (Fixed / Fit / Fill), the same as the options bar (2.3) |
| Toggles | Align and I / U / S are plain 24 px icon buttons without boxes; the active one gets `bg-control-active`, radius 2 |
| More properties | 10 px caps caption "MORE PROPERTIES" (medium, 0.04em tracking, `text-muted`), then one 28 px row per group that has nothing set: name in `text-secondary`, its current value on the right in 11 px `text-muted` ("In flow", "0", "none"). **Hover**: row `#262626`, name `text-primary`, and an 18 px `+` button (radius 3, `bg-control-active`) appears on the right. Click opens the group above the list (C-37) |
| Unset value | The field shows the computed value in `text-muted` |
| Group dividers | 1 px `line` between groups. No cards and no boxes around groups |

### 5.2 Groups shown per selection

| Selection | Groups in order |
|---|---|
| Section / Box | General, Size, Placement, Layout, Spacing, Fill, Border, Effects, Transform, Visibility, Transition, Animation, Attributes, Accessibility, Custom CSS |
| Text / Heading | General, Size, Placement, Spacing, Typography, Fill, Border, Effects, Transform, Visibility, Transition, Animation, Attributes, Accessibility, Custom CSS |
| Image / Video | General (with Source), Size (with Fit), Placement, Spacing, Border, Effects, Transform, Visibility, Transition, Animation, Attributes, Accessibility, Custom CSS |
| Button / Link | General (with Link), Size, Placement, Layout (only if it has element children), Spacing, Typography, Fill, Border, Effects, Transform, Visibility, Transition, Animation, Attributes, Accessibility, Custom CSS |
| Form control | General (with Field settings), Size, Placement, Spacing, Typography, Fill, Border, Effects, Visibility, Transition, Attributes, Accessibility, Custom CSS |
| Several elements | Only the groups they share. Values that differ show "Mixed" in italic `text-muted` |
| Nothing | **Page**: Background, Base text, Metadata (title, description, language, favicon, social image) |

Groups with values set are shown open at the top in the order above. Size and the one group most relevant to the element type (Typography for text, Layout for containers, Fill for boxes with a fill) are always open. Every other group with nothing set goes into the "More properties" list (5.1). General has no group of its own: Name and Kind are in the header, and its other fields are in the header's Advanced (Tag, Class, id, Language).

### 5.3 Group contents (simple / advanced)

| Group | Simple controls | Advanced disclosure |
|---|---|---|
| General | Name · Kind ▾ · element basics (image Source + Description, link Destination, button Label, field Placeholder + Required) | Tag (free text) · Class name · Extra classes · id · Language |
| Size | Width [mode ▾][value] · Height [mode ▾][value] · lock ⛓ · Content that doesn't fit (Show / Cut off / Scroll) · media Fit · in Row: Grow to fill | Min/max W/H · Units · Aspect ratio · Box sizing · Overflow X/Y · Object position · **In Row** group (C-38 C): Grow to fill switch; Advanced: Grow · Shrink · Basis with presets (Fill space, Keep size, Equal share), Align this item (`align-self`), Order + First/Last · **In Grid** group (C-38 D): cell picker to place and span by dragging, Column/Row + Span fields; Advanced: Area, Align in cell (`justify-self`, `align-self`) |
| Placement | Segmented: In flow / Free / Fixed to screen / Sticks when scrolling · for Free/Fixed: pin widget + X/Y · Sticky: Stick at Top [value] · Bring forward / Send back | Nudged · four offsets · inset view · z-index · "Positioned relative to: Hero grid ↗" · Float/clear · Isolation |
| Layout | Arrange: Stack / Row / Grid · Row: direction, 3×3 alignment grid, Spread ▾, Wrap, Space between · Grid: Columns ±, Rows ±, Space between, alignment grid · "Edit on canvas" link | display ▾ · direction incl. reverse · justify/align/align-content · row & column gap · track list editor (chips: `1fr` `minmax(200px,1fr)` `+`) · auto-flow · auto rows/cols · template areas (text grid) · justify items · Multi-column text |
| Spacing | Box diagram (outer ring Outside, inner ring Inside; 4 numbers each; link toggle) · Center horizontally toggle | Units per side · auto · negative · logical props · shorthand preview · scroll margin/padding |
| Typography | Font ▾ (with previews) · Weight ▾ · Size · Colour · Align · Line spacing · B I U S toggles · Text style ▾ | Letter/word spacing · Case · decoration style/colour/thickness/offset · Indent · Wrapping (balance, pretty, nowrap) · Truncate (1 line / N lines) · Vertical align · Direction/writing mode · Font features · variable axes · Text shadow · Fluid size helper |
| Fill | Layer list (top first): each row = 20 px preview, type, value, eye, ⋯ · `+ Add fill` ▾ (Colour, Gradient, Image) | Per layer: size, position, repeat, attachment, origin, clip (incl. text), blend mode · colour format · raw `background` view |
| Border | Border on/off (switch in the group title) · Colour + Thickness (paired) · Style (Solid / Dashed / Dotted) · **Corners**: the corner roundness control (C-33), opening the same popover as the options bar | Per side · all styles · Outline (colour, thickness, style, offset) · Border image. Elliptical corners and corner shape live in the C-33 popover's Advanced |
| Effects | Opacity slider + % · Shadows list (`+`, each: X Y Blur Spread Colour Inside) · Blur | Blend mode · Filters list · Backdrop filters · Clip path · Mask · Cursor · Pointer events |
| Transform | Rotate · Scale · Move X/Y · Flip H/V · "Edit on canvas" | Skew · Scale X/Y · Origin · 3D · Raw list |
| Visibility | Row of screen-size icon toggles (🖥 ▭ ▯), each on/off | visibility · content-visibility · Hide from screen readers · Visually hidden |
| Transition | Animate changes toggle · Duration · Feel (Smooth / Snappy / Gentle / Linear) · ▶ preview | Per-property list · delay · cubic-bezier curve editor (120 × 120) · steps |
| Animation | `+ Add animation` ▾ (Fade in, Move in, Scale in, Spin, Custom) · Duration · Delay · Repeat · Starts (Page load / Scrolled into view) · "Edit on timeline" | Keyframes (opens Timeline) · Direction · Fill mode · Multiple · Scroll-driven · Respect reduced motion (on) |
| Attributes | Key/value list · `+ Add attribute` | data-* helper · boolean toggles · Copy selector · id/title/tabindex/hidden/inert |
| Accessibility | Only relevant questions: "Describe this image" / Decorative; "Name for screen readers"; field Label; heading Level (with skip warning); Landmark | role · aria-* · tabindex |
| Custom CSS | One line: "For anything the controls don't cover." | Declarations editor (mono 11 px, 6 visible lines) scoped to this element, size and state · More selectors list (`::before`, `:nth-child`, `> li`) |

### 5.4 Field behaviour (visual rules)

- **Length field** (C-06): accepts a number, a number with a unit, a keyword, arithmetic (`100% - 40px` becomes `calc(…)`), `var(--x)`, or any valid value. The unit sits inside the field at the right as a 10 px muted clickable unit menu. Non-simple values show the raw text plus a `custom` tag.
- **Scrubbing**: the cursor turns into ↔ over a field label, and dragging changes the value (1 per 2 px; `Shift` ×10; `Alt` ×0.1).
- **Arrow keys** step by 1, with `Shift` 10 and `Alt` 0.1.
- **Invalid value**: 1 px `danger` border and an 11 px message under the row ("Not a valid width"). The previous value stays.
- **Hovering a field** highlights the matching thing on the canvas, such as the width dimension line, the padding band or the gap bars.
- **Real size differs**: a muted note under the row, for example "Shown 280 — limited by Max width".
- **Right-click a label**: Reset · Set for all sizes · Copy CSS.

---

## 6. Beginner and Advanced Interaction Patterns

### 6.1 The four-level disclosure (used by every group and every tool)

```
▾ Spacing                     ← Level 1: group header (collapse/expand)
   simple controls            ← Level 2: always visible
   ▸ Advanced  •              ← Level 3: per-group disclosure; dot if anything set inside
       advanced controls
       ▸ Other properties     ← Level 4: add any CSS property this group owns
           [property ▾] [value        ] [×]
           + Add property
```

- The **Advanced** row is 24 px with an 11 px medium label in `text-secondary`, a chevron, and a 5 px accent dot when values are set inside.
- When open, the advanced controls are indented 0 px (the same column as simple controls) with a 1 px `line-subtle` line above them. They are not boxed.
- Disclosure state is remembered **per group, per user**, not per element.
- The "Other properties" property field autocompletes from CSS properties this group owns, and then all properties.
- The tool equivalent is the **More ▸** popover in the options bar (width 320, the same internal layout).
- In the Properties panel, Level 3 is opened by the **Advanced icon button** in the group's title row (5.1), not a separate "▸ Advanced" row. The advanced controls open in a 328 px popover to the left of the Properties panel, anchored to that button (pressed, with an accent ring), with Pin open, Close, a CSS line and Copy CSS (v0.2, D-14 to D-20).
- Level 1 for empty groups is the "More properties" list: one line per group, with a `+` on hover (5.1).

### 6.2 Beginner aids

| Aid | Look | Behaviour |
|---|---|---|
| First-use hint | One line under a control in 11 px `info` text with a ⓘ and a × ("Row places children side by side.") | Shown the first time the concept appears. × dismisses it forever. Help → Show tips again restores all hints |
| Plain labels | See the vocabulary in 6.4 | CSS names are in tooltips |
| Canvas teaching visuals | Coloured bands for space inside/outside, hatched bars for gaps, track badges for grid | Shown by Spacing and Layout tools, and when hovering fields |
| Empty section hint | Dashed inner outline and centred text "Empty section — pick a tool and click here" in 13 px `#9a9a9a` on the page | Drawn by the overlay, never part of the page |
| Status bar hint | One sentence per tool and state | Always present |
| Explain refusals | Invalid drop: red insertion line + reason beside the pointer | Never silent |

### 6.3 Advanced aids

| Aid | Where |
|---|---|
| Raw values anywhere | Every field |
| `custom` tag | Any field that holds a value its simple control can't represent |
| Inactive tag | Properties of an old arrangement (e.g. grid values after switching to Row), with a "Clean up" button |
| Code drawer | Live HTML/CSS of the selection, Page CSS, Page JavaScript |
| Direct Select and `Ctrl+click` | Deep selection without drilling in |
| Alt+drop in Layers | Allow invalid nesting (the element gets a ⚠ badge) |
| Copy CSS / Copy selector | Right-click labels; Attributes group |

### 6.4 Vocabulary (use exactly these words in the design)

| Concept | Label | Tooltip / Advanced name |
|---|---|---|
| width / height | Width / Height: **Fill**, **Fit content**, **Fixed** | `width: auto`, `fit-content`, length |
| padding | Space inside | `padding` |
| margin | Space outside | `margin` |
| gap | Space between | `gap` |
| block / flex / grid | Arrange children: **Stack**, **Row** (→ or ↓), **Grid** | `display` |
| justify / align | Alignment grid, Spread | `justify-content`, `align-items` |
| flex-grow | Grow to fill | `flex-grow: 1` |
| position | Placement: **In flow**, **Nudged**, **Free**, **Fixed to screen**, **Sticks when scrolling** | `static`, `relative`, `absolute`, `fixed`, `sticky` |
| z-index | Stack order | `z-index` |
| breakpoint | Screen size | `@media (max-width: …)` |
| :hover / :active / :focus-visible | Mouse over / Pressed / Focused | selector |
| border-radius | Corner roundness | `border-radius` |
| box-shadow | Shadow | `box-shadow` |
| overflow | Content that doesn't fit: Show / Cut off / Scroll | `overflow` |
| line-height | Line spacing | `line-height` |
| opacity | Opacity % | `opacity` |

---

## 7. Canvas Interaction Specifications

### 7.1 Canvas visuals

| Aspect | Spec |
|---|---|
| Workspace | Flat `bg-workspace`. No pattern or grid |
| Page frame | The page renders white (or the page background). A 1 px `page-edge` border sits outside it. Above the top-left corner is the label "Desktop · 1440" (11 px `text-muted`, 8 px above). There is no shadow |
| Fold line | A dashed 1 px `rgba(47,128,237,.35)` line across the page at 900 px, with a 10 px label "Fold · 900" in `#666666` **just below the line, inside the page's right edge** (8 px in). It never sits outside the page, where the 46 px workspace margin is too narrow |
| Add section bar | Under the page, 8 px gap, full page width, 32 px high, dashed 1 px `line-strong` border, centred "+ Add section" (12 px `text-secondary`). Hover: `text-primary`, solid border |
| Hover | 1 px accent outline on the element a click would select, and a name tag above its top-left |
| Name tag | 18 px high, 4 px horizontal padding, `accent-fill`, white 11 px medium text: `Heading · h1`. A free element adds a ◇. Locked shows 🔒 and no outline |
| Selection | A 1.5 px accent outline and 8 handles (8 × 8, white fill, 1 px accent stroke, 1 px radius). Inside each corner, 10 px in, are 4 round corner-radius handles (6 px, white with accent stroke), which appear only when the element is at least 48 px in both dimensions |
| Size label | While resizing, an accent pill centred 8 px below the box: `720 × 116`. It shows "Fill" or "Fit" words when a mode is not fixed |
| Parent of selection | A 1 px dashed accent outline at 60% opacity |
| Multi-selection | A thin 1 px outline on each element, plus one bounding box with handles |
| Empty container | A dashed inner outline in `#c8c8c8` on the page. If it is under 8 px in one dimension, a 12 px marker flag is drawn |
| Hidden element (selected in Layers) | Not rendered. Properties shows the notice "Hidden at this screen size · Show" |
| Text editing | 1 px solid accent outline, no handles, browser caret and selection colour |

### 7.2 Overlay colour code (fixed meaning across the whole product)

| Colour | Token | Meaning |
|---|---|---|
| Blue `#2f80ed` | `ov-select` | Selection, hover, insertion line, drop target |
| Green `#3fb950` at 30% fill, 100% edges | `ov-inside` | Space inside (padding) |
| Orange `#f0883e` at 30% fill | `ov-outside` | Space outside (margin) |
| Pink `#db61a2` hatched 45° | `ov-gap` | Space between (gap) |
| Magenta `#e535ab` | `ov-guide` | Alignment guides, equal spacing, size match |
| Red `#f85149` | `ov-measure` | Measure tool and distance readout. Also invalid drop |
| Teal `#1a9284` | `ov-track` | Grid tracks, column edges, track badges, the transform origin and dial (lines 3.4:1 on the page, 4.3:1 on the dark editor). Badge fill `ov-track-fill` `#127a70` (white text 5.2:1); subtle `ov-track-subtle` `rgba(26,146,132,0.14)`; text on dark `#9fe5dc`. Violet is reserved for states only |
| Cyan `#22c5e0` | `ov-ruler` | Manual ruler guides |

The overlay is always drawn at fixed screen thickness, whatever the zoom.

### 7.3 Gestures and their visual feedback

| Gesture | Visual feedback |
|---|---|
| Drag an **in-flow** element | Ghost at 60% opacity follows the pointer. The original stays in place at 30% opacity. A 2 px blue insertion line, with 6 px end caps, shows the drop position; it is horizontal in stacks and vertical in rows. The target container gets a 1 px blue outline and a name tag "into Hero text" |
| Hover a container during a drag for 400 ms | The container "opens" and the insertion line moves inside it |
| Invalid drop | The insertion line turns red, and a red pill beside the pointer gives the reason ("Text can't contain boxes") |
| Drag a **Free** element | The element moves. Magenta guide lines appear on matching edges and centres, with the gap distances in magenta pills. Pin lines run from the pinned sides to the anchor with distances |
| Resize | Live reflow. A size label is shown. When the size is limited by layout, a "limited" cursor and the label "280 × 116 · limited by Max width" appear |
| Marquee | 1 px blue rectangle with 8% blue fill. Elements it touches get a hover outline |
| Alt-hover distances | Red lines with red value pills between the selection and the hovered element |
| Snap | When an edge snaps, the guide flashes to full opacity. Snap distance is 6 screen px. Hold `Ctrl` to disable snapping |
| Zoom/pan | Smooth. The zoom percentage in the top bar updates live |

### 7.4 Cursors

| Situation | Cursor |
|---|---|
| Select over element | Default arrow |
| Over handle | Resize arrows by direction |
| Over a radius handle | Arrow with a small rounded-corner glyph |
| Dragging in flow | Grabbing hand |
| Creation tools | Crosshair with a small tool glyph |
| Text tool over text | I-beam |
| Spacing band / gap bar | Resize arrow perpendicular to the band |
| Transform outside corner | Curved rotate arrow |
| Not allowed | Circle-slash |
| Value uses a formula (can't drag) | Arrow with a lock glyph |

### 7.5 Context menus

Drawn on **D-48**. Every menu starts with a header line naming what was clicked; rows, names and shortcuts are the same as the menu bar (3.3, C-16). Right-click selects what is under the pointer first (unless it is already in the selection); `Shift F10` or the Menu key opens the menu for the selection; menus open at the pointer and flip to stay on screen; with several elements selected the header reads "3 elements" and only shared actions show (D-11).

**Element:** Cut · Copy · Paste · Paste inside · Duplicate — Copy style · Paste style — Wrap in ▸ · Wrap in link — **Select layer ▸** (every element under the pointer, deepest first; hovering a row outlines it) · Add state ▸ · Placement ▸ — Rename · Lock · Hide · Show code — Delete (`danger`)

**Empty workspace:** Paste · Select all — Fit width · 100% · Screen size ▸ — Rulers · Guides · Layout grid — Page settings…

**Layers row:** Rename · Select children · Select same ▸ (class) — Collapse all inside · Expand all inside — Wrap in ▸ · Unwrap · Duplicate — Lock · Hide · Show on canvas — Delete

**Page tab:** Save version… · Page settings… · Preview — Duplicate page · Rename page… · Copy address · Show in Project — Close · Close others · Close tabs to the right · Close saved tabs

**Project page row:** Open · Open in a new tab — New page · Duplicate · Rename… · Set as home page — Page settings… · Export this page… · Show in folder — Delete page… (asks first)

**Swatch or token:** Apply to fill · Apply to text colour (Alt-click) · Apply to border — Select all uses · Edit token… · Copy ▸ (hex, var()) — Replace and delete…

---

## 8. Document Hierarchy and Layers Interactions

### 8.1 Hierarchy as the user sees it

- The page is a vertical stack of **sections**. Sections are the top-level rows in Layers.
- Every layer is one real HTML element. A group is a real `<div>`. Text content is not its own row.
- Order in Layers equals order on the page, **first at the top** ("Top of page ↑" caption). This is the reverse of an image editor, and the caption says so.
- Inline parts (`strong`, `a` inside a paragraph) are hidden by default. Layers ☰ → "Show inline parts" reveals them as 20 px rows in muted text.

### 8.2 Selection scope (shown in D-05 and D-06)

- A click selects the outermost element under the pointer within the current scope. The scope starts at the page.
- Double-click enters a container: the scope moves in, and the container gets the dashed parent outline.
- `Ctrl+click` or Direct Select picks the deepest element.
- `Esc` selects the parent. `Enter` selects the first child. `Tab` / `Shift+Tab` move to the next or previous sibling.

### 8.3 Layers interactions

| Action | Interaction | Visual |
|---|---|---|
| Select | Click a row | Synced with the canvas: canvas selection scrolls the row into view and expands its ancestors |
| Range / toggle | `Shift+click` / `Ctrl+click` | Multiple highlighted rows |
| Rename | Double-click the name | Inline field |
| Reorder / nest | Drag a row | Between line, or inside highlight (3.1). Hovering a collapsed row for 600 ms expands it |
| Hide / lock | Eye / lock on hover | Icons stay visible when active |
| Context menu | Right-click | Same as canvas, plus "Add section below" for sections and "Add item" for lists |
| Filter | Type in the filter | Matching rows with ancestors kept and dimmed. Matching text is highlighted |
| Hover row | — | Canvas outlines that element |

### 8.4 Nesting rules as the user experiences them

| Rule | Message shown |
|---|---|
| Image, field, divider can't have children | "Images can't contain other elements. Use a Box and put both inside." |
| Text and headings hold only text | "Text can't contain boxes." |
| Link/button can't hold clickable things | "A link can't contain another clickable element." |
| List holds only items | Auto-wraps in a list item, with the notice "Wrapped in a list item" |
| Form in form | "A form can't be inside another form." |
| Section dropped into a box | Converted to a Box, with the notice "Sections live at the top of the page, so this became a Box · Undo" |

---

## 9. Design System

### 9.1 Colour tokens: dark theme (default)

| Token | Value | Use |
|---|---|---|
| `bg-titlebar` | `#141414` | Top bar |
| `bg-toolbar` | `#1b1b1b` | Options bar |
| `bg-chrome` | `#181818` | Tool strip, page tab row, status bar |
| `bg-capsule` | `#232323` | Control holders in the options bar |
| `bg-panel` | `#1f1f1f` | Docks, options bar, drawer |
| `bg-workspace` | `#2a2a2a` | Canvas background |
| `bg-control` | `#2a2a2a` | Field and button fill |
| `bg-control-hover` | `#323232` | Hover |
| `bg-control-active` | `#3a3a3a` | Pressed and active segment |
| `bg-popover` | `#262626` | Menus, popovers, dialogs, tooltips |
| `line-subtle` | `#262626` | Indent guides, advanced divider |
| `line` | `#303030` | Panel separators |
| `line-strong` | `#454545` | Control borders, dashed add-bar |
| `page-edge` | `#3c3c3c` | Page frame border |
| `text-primary` | `#e8e8e8` | Main text |
| `text-secondary` | `#a8a8a8` | Labels, inactive icons |
| `text-muted` | `#939393` | Placeholders, tags, captions. 5.37:1 on `bg-panel`, 4.67:1 on `bg-control`, 6.0:1 on `bg-titlebar`. (v0.1 used `#757575`, which measured only 3.58:1 on `bg-panel`, not the 4.6:1 stated, and failed AA) |
| `text-disabled` | `#4f4f4f` | Disabled |
| `accent` | `#2f80ed` | Selection outlines, handles, active states, focus ring. Not for fills behind white text (3.87:1) |
| `accent-fill` | `#246bcb` | Fills behind white text: primary button, canvas name tag, switches that are on. 5.2:1 with white |
| `accent-fill-hover` | `#2c72d6` | Primary button hover (4.7:1 with white; `accent-hover` #4b93f1 is too light for white text) |
| `accent-fill-pressed` | `#1f5fb5` | Primary button pressed (6.4:1 with white) |
| `accent-hover` | `#4b93f1` | Primary hover |
| `accent-pressed` | `#246bcb` | Primary pressed |
| `accent-subtle` | `rgba(47,128,237,0.18)` | Selected rows, active tool background |
| `on-accent` | `#ffffff` | Text on accent |
| `resp` | `#d29922` | **Mode cues only**: the responsive chip, the active screen-size icon, the small tablet/phone icons on name tags, Layers badges and the Properties context strip. Value markers in Properties are accent (set here) or hollow grey (inherited) |
| `resp-subtle` | `rgba(210,153,34,0.14)` | Context strip |
| `state` | `#a371f7` | **Mode cues only**: the state context chip in the options bar, the canvas name tag (fill `#7c4ed8`), the ⌖ badge in Layers and the small ⌖ icon in the State button. Properties panels and popovers never use it: they use the normal `accent` (pressed button with accent ring, accent dot and ring for overrides, accent suggestion box) |
| `state-subtle` | `rgba(163,113,247,0.16)` | State strip |
| `rec` | `#e5534b` | **Mode cue only**: Timeline recording (record button, border, badge, new keyframe halo). Subtle `rgba(229,83,75,0.16)`, text on dark `#ff938c` |
| `info` | `#58a6ff` | Hints, notices |
| `success` | `#3fb950` | Saved, export done |
| `warning` | `#d29922` | Accessibility warnings |
| `danger` | `#f85149` | Errors, delete, invalid |
| `brand-daisy` | `#f2b84b` | Centre of the daisy brand mark only. Never used for UI states |

Overlay colours are listed in 7.2 and are the same in both themes.

### 9.2 Colour tokens: light theme

Checked on D-33 (D-04 redrawn in light). Values marked † changed in that check.

| Token | Value | Token | Value |
|---|---|---|---|
| `bg-titlebar` | `#eeeeee` † (new) | `text-primary` | `#1c1c1c` |
| `bg-toolbar` | `#f7f7f7` † (new) | `text-secondary` | `#555555` |
| `bg-chrome` | `#f3f3f3` | `text-muted` | `#6b6b6b` (4.6:1 on titlebar, 4.68:1 on control, 5.1:1 on panel) |
| `bg-capsule` | `#ececec` † (new) | `text-disabled` | `#b5b5b5` |
| `bg-panel` | `#fafafa` | `line-subtle` | `#ebebeb` † (new) |
| `bg-workspace` | `#e4e4e4` | `line` | `#e1e1e1` |
| `bg-control` | `#f0f0f0` † (was `#ffffff`, which vanished on `bg-panel` at 1.04:1) | `line-strong` | `#c9c9c9` |
| `bg-control-hover` | `#e8e8e8` † | `page-edge` | `#cfcfcf` |
| `bg-control-active` | `#dcdcdc` † | `accent-subtle` | `rgba(47,128,237,0.12)` † (0.18 read too heavy on white) |
| `bg-popover` | `#ffffff` | Shadow | `0 8px 24px rgba(0,0,0,0.10)` + 1 px `line-strong` |

**Floating surfaces and text colours in light** († from D-33b–d): popovers, menus and dialogs are `#ffffff` with a 1 px `#d4d4d4` border and shadow `0 8px 24px rgba(0,0,0,0.16)`; dialog scrims drop to 28 % (insets 22 %). Text that is light-on-dark in the dark theme has light equivalents: link and info blue `#1f5fb5`, info icon `#0969da`, danger text `#cf222e`, warning text `#9a6700`, secondary text `#3d3d3d`; code colours tag `#0550ae`, string `#116329`, number `#953800`. Selected rows use `accent-subtle` at 12 %, pressed tabs 10 %.

**Status colours in light** †: the dark values are too pale on light surfaces (amber `#d29922` is 2.4:1), so light uses ink versions: `warning` / `resp` `#9a6700` (4.7:1), `success` `#1a7f37` (4.9:1), `danger` `#cf222e` (5.1:1). Mode-cue fills (`state` name tag `#7c4ed8`, `rec`), accent `#2f80ed` and `accent-fill` `#246bcb` stay the same. Accent used as **text** (links in panels) uses `accent-fill` `#246bcb` in light, since `#2f80ed` is 3.7:1 on `bg-panel`. Overlay colours do not change.

### 9.3 Typography

| Token | Font | Size / line | Weight | Use |
|---|---|---|---|---|
| `ui-xs` | Inter, system-ui | 10 / 14 | 500 | Badges, units, fold label |
| `ui-sm` | Inter | 11 / 16 | 400 | Labels, tags, status bar, captions |
| `ui-base` | Inter | 12 / 16 | 400 | Default UI text, fields, menus |
| `ui-medium` | Inter | 12 / 16 | 500 | Tabs, tool name, buttons, doc name |
| `ui-strong` | Inter | 12 / 16 | 600 | Group headers |
| `ui-title` | Inter | 14 / 20 | 600 | Dialog titles |
| `ui-display` | Inter | 20 / 28 | 600 | Home title |
| `mono-sm` | JetBrains Mono, ui-monospace | 11 / 16 | 400 | Tags in Properties, CSS values, Code drawer |

Numbers in fields and readouts use tabular figures (`font-feature-settings: "tnum"`). There is no text smaller than 10 px.

### 9.4 Spacing, sizing and grid

- Base unit is 4 px. Spacing scale: 2, 4, 8, 12, 16, 24, 32.
- **Control height: 24 px.** Row height: 28 px in Properties, 24 px in Layers, 28 px in menus.
- Icon buttons are 24 × 24 (in panels) or 28 × 28 (top bar), and tool buttons are 32 × 32.
- Panel padding is 12 px horizontal. Gaps between controls in a row are 4 px for tightly related controls (value + unit, W + H) and 8 px otherwise.
- Popover widths: 240 (menus, min), 328 (Advanced popovers, colour picker), 360 (link popover).
- Dialog widths: 560 (Screen sizes), 940 (Versions), 1040 (Export), 1100 (Page settings). The New project setup is a 1200 × 760 window.

### 9.5 Borders, radius, elevation

| Item | Value |
|---|---|
| Field radius (panels) | 2 px |
| Buttons, segments, inner capsule controls | 4 px |
| Capsules / holders, brand tile, Preview and Export, search bar, popovers | 6 px |
| Menu, tooltip, dialog radius | 4 px |
| Key badges, size-mode tags, tab close | 3 px |
| Chips / pills | 10 px (fully rounded at 20 px height) |
| Panels, docks | 0 px; separated by 1 px lines only |
| Control border | Fields: no border at rest, 1 px `line-strong` on hover, accent on focus. Buttons have no border except outline (Preview) and secondary buttons, drawn as a 1 px inner ring (`box-shadow: inset 0 0 0 1px`) |
| Elevation | Only floating layers have it: `0 8px 24px rgba(0,0,0,0.45)` + 1 px `line-strong` border. Panels are never elevated |
| Focus ring | 2 px `accent` outside, 1 px offset. Keyboard focus only (`:focus-visible`) |

### 9.6 Iconography

- Grid is 16 × 16 with a 1.5 px stroke, round caps and joins, outline style, and `currentColor`. Small badge glyphs are 12 px on a 1.25 px stroke.
- Tool icons are a custom set drawn to the concepts in 4.1. Generic glyphs (chevrons, eye, lock, plus, trash, gear, play) use the Lucide style for consistency.
- No filled or duotone icons, except the active-tool state, which uses the accent colour only.
- Device icons: monitor, tablet, phone and wide monitor, all at 14 px.

### 9.7 Motion

| Use | Duration | Easing |
|---|---|---|
| Hover, press colour changes | 80 ms | linear |
| Disclosure expand / collapse | 140 ms | ease-out |
| Popover / menu open | 120 ms fade + 4 px slide | ease-out |
| Dialog open | 160 ms fade + scale 0.98 → 1 | ease-out |
| Notice in status bar | 160 ms fade | — |
| Canvas zoom (button/keyboard) | 160 ms | ease-in-out |

Canvas overlay feedback (outlines, handles, guides) is never animated. It follows the pointer at once. All motion turns off when the system asks for reduced motion.

### 9.8 Component library and states

Every component is shown on the design system sheet (D-00) in **all** listed states.

| ID | Component | Anatomy | States |
|---|---|---|---|
| C-01 | Primary button | 24 h (28 in top bar), 12 px padding, `accent-fill` (hover `accent-fill-hover`, pressed `accent-fill-pressed`), `ui-medium` | rest, hover, pressed, focus, disabled |
| C-02 | Secondary button | `bg-control` + 1 px `line-strong` border | rest, hover, pressed, focus, disabled |
| C-03 | Ghost / text button | No fill until hover | rest, hover, pressed, focus, disabled |
| C-04 | Icon button | 24 or 28 square, 16 px icon | rest, hover, pressed, active (toggled on), focus, disabled |
| C-05 | Text field | 24 h, `bg-control`, no border at rest, 6 px padding, optional inside label | rest, hover (1 px `line-strong`), focus (accent border + ring), filled, placeholder, invalid, disabled, read-only |
| C-06 | Length / number field | Text field plus a unit menu at the right and a scrubbable label | as C-05, plus scrubbing (↔ cursor, accent label), `custom` tag, mixed |
| C-07 | Colour field | 16 px swatch + hex + opacity % | rest, hover, focus, mixed, from swatch (shows the swatch name in place of hex) |
| C-08 | Select / dropdown | Field with chevron. Opens C-16 | rest, hover, open, focus, disabled, mixed |
| C-09 | Segmented control | 24 h, equal or content-width segments, 1 px outer border | each segment: rest, hover, selected, disabled; whole: focus |
| C-10 | Toggle switch | 28 × 16 | off, on, hover, focus, disabled |
| C-11 | Checkbox | 14 px square | off, on, mixed, focus, disabled |
| C-12 | Slider | 2 px track, 12 px thumb, value field beside it | rest, hover, dragging, focus, disabled |
| C-13 | Alignment grid | 3×3 dots in a 60 × 60 square (36 px mini in the options bar). Active dot is accent with 3 bars showing the child arrangement | rest, hover dot, active dot, disabled |
| C-14 | Box-sides diagram | Two nested rounded rectangles (outer orange tint, inner green tint) with 4 inline number fields each and a centre element chip | rest, hover a side (canvas band highlights), editing a side, linked |
| C-15 | Pin widget | 40 × 40 square with 4 side toggles and a centre toggle | each side on/off/hover |
| C-16 | Menu / context menu | `bg-popover`, 4 px padding, 28 px rows, icon column 16, shortcut right-aligned in `text-muted`, submenu chevron | row: rest, hover, disabled, checked, danger |
| C-17 | Popover | `bg-popover`, 12 px padding, optional title row | — |
| C-18 | Tooltip | `bg-popover`, 6 × 8 padding, max 260 px. Line 1: description. Line 2: `mono-sm` CSS name and current value. 500 ms delay | — |
| C-19 | Dialog | Title bar 44 px (title + ×), body 16 px padding, footer 52 px with buttons right-aligned (secondary, primary) | — |
| C-20 | Tabs | Text tabs, 2 px accent underline on active | rest, hover, active, focus |
| C-21 | Group header + Advanced disclosure | 6.1 | collapsed, expanded, hover, with dot, with warning |
| C-22 | Origin marker | 6 px dot | set here, inherited from size, inherited from parent, none |
| C-23 | Chip / tag | 20 h pill (`custom`, `inactive`, `runs script`, context chips) | neutral, resp, state, warning, danger |
| C-24 | Tree row (Layers) | 3.1 | rest, hover, selected, selected-unfocused, hidden, locked, drop-between, drop-inside, invalid, renaming |
| C-25 | Breadcrumb | 11 px segments with › | rest, hover, current |
| C-26 | Notice (status bar) | ⓘ + text + action link | info, warning |
| C-27 | Inline hint | ⓘ + one line + × | — |
| C-28 | Swatch tile | 24 square, 2 px radius, inner 1 px border for light colours | rest, hover, selected, add tile |
| C-29 | Canvas name tag | 7.1. Fills keep white text ≥ 4.5:1: element `accent-fill`, state `#7c4ed8`, invalid `#c9302c`, locked `#4f4f4f` | element, free, locked, state badge, invalid (red), just created |
| C-30 | Canvas handles | Resize handle, radius handle, gradient stop, transform origin, grid track badge, gap bar | rest, hover, dragging, disabled (limited) |
| C-31 | Layer / fill list row | 28 h, preview, label, eye, ⋯, drag grip on hover | rest, hover, dragging, hidden |
| C-32 | Empty state | 32 px icon, one sentence, optional button | — |
| C-33 | Corner roundness control | Trigger: capsule with value (or "16 · 0", or *Mixed*) + a corners button. Popover 320: mode row (All · Top/Bottom · Left/Right · Each), live preview shape with fields on the corners, value + px menu + slider (All), presets (0 4 8 12 24 Pill Circle; pair shortcuts Swap · Top only · Bottom only · Tab · Make equal), design-system token link, CSS line + Copy CSS. Advanced: Elliptical corners (H / V per corner), Corner shape (Round · Squircle · Bevel · Notch via `corner-shape`, round fallback), Fluid value (`clamp()` etc. with `custom` tag), link opposite corners. Used in the options bar and in Properties → Border | All, pairs, each, each + advanced; trigger rest / open / mixed |
| C-34 | Page tab | 2.7 | active, inactive, hover (× shows), unsaved (dot), single file, dragging |
| C-35 | Search bar | 2.2 | rest, hover, focus (opens results: recent pages, matching layers and assets, `>` commands) |
| C-37 | More properties row | 5.1 | rest, hover (+ visible), with value summary |
| C-38 | Layout advanced (Row / Grid / item) | D-37. Same pattern as C-33: plain label + CSS name beside it, picture buttons for alignment, live preview, CSS line + Copy CSS. Raw CSS accepted in every field and chip; unsupported syntax gets the `custom` tag. Mirrors the Layout tool on canvas (12.4) | Row container, Grid container (track editor open), child in Row, child in Grid |

### 9.9 Token reference for other tools and for code

Use these exact values everywhere: Claude Design, other design tools, and the Stage 2 code. The names match the tokens above; in CSS they are custom properties with a `--d-` prefix.

```css
:root, [data-theme="dark"] {
  /* surfaces */
  --d-bg-titlebar: #141414;  --d-bg-toolbar: #1b1b1b;  --d-bg-chrome: #181818;
  --d-bg-panel: #1f1f1f;     --d-bg-capsule: #232323;  --d-bg-workspace: #2a2a2a;
  --d-bg-control: #2a2a2a;   --d-bg-control-hover: #323232; --d-bg-control-active: #3a3a3a;
  --d-bg-popover: #262626;
  /* lines */
  --d-line-subtle: #262626;  --d-line: #303030;  --d-line-strong: #454545;  --d-page-edge: #3c3c3c;
  /* text */
  --d-text-primary: #e8e8e8; --d-text-secondary: #a8a8a8; --d-text-muted: #939393; --d-text-disabled: #4f4f4f;
  /* accent */
  --d-accent: #2f80ed; --d-accent-hover: #4b93f1; --d-accent-pressed: #246bcb;
  --d-accent-fill: #246bcb; --d-accent-fill-hover: #2c72d6; --d-accent-fill-pressed: #1f5fb5;
  --d-accent-subtle: rgba(47,128,237,0.18); --d-on-accent: #ffffff;
  --d-tag-state: #7c4ed8; --d-tag-invalid: #c9302c; --d-tag-locked: #4f4f4f;
  /* meaning */
  --d-resp: #d29922; --d-resp-subtle: rgba(210,153,34,0.14);
  --d-state: #a371f7; --d-state-subtle: rgba(163,113,247,0.16);
  --d-info: #58a6ff; --d-success: #3fb950; --d-warning: #d29922; --d-danger: #f85149;
  --d-brand-daisy: #f2b84b;
  /* overlay (both themes) */
  --d-ov-select: #2f80ed; --d-ov-inside: #3fb950; --d-ov-outside: #f0883e; --d-ov-gap: #db61a2;
  --d-ov-guide: #e535ab;  --d-ov-measure: #f85149; --d-ov-track: #1a9284; --d-ov-track-fill: #127a70; --d-ov-track-subtle: rgba(26,146,132,0.14); --d-ov-track-text: #9fe5dc; --d-ov-ruler: #22c5e0;
  /* type */
  --d-font-ui: "Inter", system-ui, sans-serif;  --d-font-mono: "JetBrains Mono", ui-monospace, monospace;
  /* size, radius, elevation */
  --d-space-1: 2px; --d-space-2: 4px; --d-space-3: 8px; --d-space-4: 12px; --d-space-5: 16px; --d-space-6: 24px; --d-space-7: 32px;
  --d-control-h: 24px; --d-capsule-h: 28px; --d-row-h: 28px; --d-tree-row-h: 24px;
  --d-radius-field: 2px; --d-radius-badge: 3px; --d-radius-control: 4px; --d-radius-capsule: 6px; --d-radius-menu: 4px; --d-radius-chip: 10px;
  --d-shadow-float: 0 8px 24px rgba(0,0,0,0.45);
  --d-focus-ring: 0 0 0 1px var(--d-bg-panel), 0 0 0 3px var(--d-accent);
}
[data-theme="light"] {
  --d-bg-titlebar: #f3f3f3; --d-bg-toolbar: #f7f7f7; --d-bg-chrome: #f3f3f3; --d-bg-panel: #fafafa;
  --d-bg-capsule: #efefef;  --d-bg-workspace: #e4e4e4; --d-bg-control: #ffffff; --d-bg-control-hover: #f0f0f0;
  --d-bg-control-active: #e6e6e6; --d-bg-popover: #ffffff;
  --d-line-subtle: #ececec; --d-line: #e1e1e1; --d-line-strong: #c9c9c9; --d-page-edge: #cfcfcf;
  --d-text-primary: #1c1c1c; --d-text-secondary: #555555; --d-text-muted: #6b6b6b; --d-text-disabled: #b5b5b5;
}
```

Component style summary (what to copy when rebuilding the shell elsewhere):

| Pattern | Recipe |
|---|---|
| Field | 24 h · `bg-control` · radius 2 · no border at rest · hover 1 px `line-strong` · focus accent border + `focus-ring` · 12 px text · inside label 11 px `text-muted` |
| Capsule (holder) | 28 h · `bg-capsule` · radius 6 · padding 2 · children 24 h radius 4 · 1 × 14 dividers |
| Segmented control | Capsule holder · selected segment `bg-control-active` + `text-primary` 500 · others `text-muted` |
| Primary button | 28 h (top bar) / 24 h (panels) · `accent-fill` · white 12 px medium · radius 6 (top bar) / 4 (panels) |
| Outline button | Transparent · inset 1 px `bg-control-active` ring · `text-primary` 12 px medium |
| Tag (size mode, `custom`) | 16 h · padding 0 5 · radius 3 · `bg-control-active` · 10 px `text-secondary` |
| Key badge | 16–18 h · padding 0 4–5 · radius 3 · 10 px medium |
| Popover | `bg-popover` · 1 px `line-strong` · radius 6 · `shadow-float` · padding 12 · 12 px gap |
| Section caption | 10 px medium caps · 0.04em tracking · `text-muted` |
| Dividers | 1 px `line` between groups and panels; 1 px `line-subtle` inside the top two bars |

Light-theme values for `bg-titlebar`, `bg-toolbar`, `bg-capsule` and `line-subtle` are first proposals and must be checked on D-33.


---

## 10. Sample Content for the Designs

Every editor screen shows the **same** document, so the screens read as one product. The page is mock content for design purposes only. It is not a template, and nothing like it ships in Daisy.

### 10.1 Document "Halden landing" — a small ceramics studio

Page settings: background `#f6f1ea`. Base text Inter 16 / 1.5 `#1d1a16`. Headings in **Fraunces** (serif). Brand terracotta `#b5532d`. Swatches: `brand #b5532d`, `ink #1d1a16`, `sand #f6f1ea`, `clay #e7d9c7`, `moss #5f6b4e`.

| Section | Content and layout at Desktop 1440 |
|---|---|
| **Header** (`header`) | 80 px high, padding 0 64. Arranged as a Row with Spread: Space between. On the left, the wordmark "Halden" (Fraunces 24, 600). In the middle, a nav row of links: Work · Shop · Journal · Visit (Inter 15, gap 32). On the right, a button "Book a visit" (terracotta fill, white text, radius 999, padding 10 20) |
| **Hero** (`section`) | Padding 72 64 96. **Grid**, 2 columns `1.1fr 1fr`, gap 64, items centred vertically. Left "Hero text" box (Column, gap 24): eyebrow "Small-batch stoneware · Est. 2014" (13 px, uppercase, letter spacing .08em, moss). **h1** "Hand-thrown ceramics for everyday tables" (Fraunces 64 / 1.05, ink, width 560). Paragraph "Each piece is wheel-thrown, glazed and fired in our studio by the river. Made slowly, used daily." (18 / 1.6, `#4a443c`, max width 480). Buttons row: "Shop the collection" (terracotta) and "Our process →" (text link). Right "Hero image": a photo of stacked bowls and cups on linen, 580 × 520, radius 12, object-fit cover |
| **This season** (`section`) | Padding 96 64, background clay `#e7d9c7`. h2 "This season" (Fraunces 40) with a muted "View all →" link, in a Row with Space between. Then a **Grid** of 3 columns, gap 32, of 3 "Card" boxes. Each card has white fill, radius 12 and padding 16: an image (radius 8, aspect 4/3), a name (Fraunces 20) and a price (15, moss). The cards are "Tide bowl — €38", "Ember mug — €26" and "Linen plate set — €84" |
| **Footer** (`footer`) | Padding 48 64, ink background, sand text. Row: "© 2026 Halden Studio", an address, and Instagram and Newsletter links |

Total page height at Desktop is about 2,050 px. The fold line at 900 cuts through the top of "This season".

### 10.2 Layers tree (exact)

```
▾ Header                    header
   Wordmark "Halden"        p
  ▸ Nav links               nav
   Book a visit             a
▾ Hero                      section
  ▾ Hero grid               div      (Grid)
    ▾ Hero text             div      (Column)
       "Small-batch…"       p
       "Hand-thrown…"       h1
       "Each piece is…"     p
      ▸ Hero buttons        div      (Row)
     Hero image             img
▸ This season               section
▸ Footer                    footer
```

### 10.3 Responsive versions (for D-20 to D-23)

| Size | Canvas width | Overrides shown |
|---|---|---|
| Tablet (≤ 1024) | 768 | Hero grid becomes 1 column. h1 goes to 48 px. Card grid becomes 2 columns. Header padding 0 32 |
| Mobile (≤ 640) | 390 | h1 goes to 36 px. Nav links are hidden (Visibility). Card grid becomes 1 column. Section padding 48 20. Hero image height 320 |

---

## 11. Screen-by-Screen Design Requirements

Every screen is 1920 × 1080 in the dark theme unless stated. Each screen lists **what it must show** and its **review checks**. Each builds on an earlier screen, so only the differences are described.

### Canvas map (v0.2)

The Screens page is laid out in 14 numbered rows, top to bottom, each starting with a section title board (`SEC-01` … `SEC-14`). Inside a row, boards run left to right with their state sheets right after them. This map replaces the "at x, y" positions given in the screen notes below.

| Row | Section | Boards, left to right |
|---|---|---|
| 01 | **Reference** · The key editor screen and the shared component sheets | D-04 · D-35 · D-37 |
| 02 | **Home and new project** · First run, projects, the setup steps, a fresh project, Home and Help | D-01 · D-02 · D-02b · D-03 · D-52 |
| 03 | **Selecting and moving** · Hover, scope, resize, drag, drop, free elements, multi-select | D-05 · D-06 · D-07 · D-08 · D-09 · D-10 · D-11 |
| 04 | **Creation tools** · Text, Box, Section, Button, Link, Form, Media, Elements, Place and interactive parts | D-12 · D-13 · D-43 · D-41 · D-42 · D-17 · D-18 · D-56 · D-56b |
| 05 | **Shape and inspect tools** · Layout, Spacing, Transform and Gradient, Measure and Eyedropper | D-14 · D-15 · D-16 · D-19 |
| 06 | **Properties** · Advanced values, colour picker, fill, border and effects, states | D-20 · D-39 · D-47 · D-21 |
| 07 | **Screen sizes, views and themes** · Tablet, Mobile, Preview, light theme and the compact frame | D-22 · D-23 · D-29 · D-33 · D-33b · D-33c · D-33d · D-34 |
| 08 | **Panels** · Layers, outline and accessibility, Assets | D-24 · D-25 · D-26 |
| 09 | **Reusable content** · Shared parts, components with variants, collections of repeating content | D-53 · D-58 · D-58b · D-57 · D-57b |
| 10 | **Code and Timeline** · The two pro workspaces and their states | D-27 · D-27b · D-28 · D-28b |
| 11 | **Design system** · The editor, opting in later, and its states | D-36 · D-36b · D-36c |
| 12 | **Pages and settings** · Page settings, Project settings and the page dialogs | D-31 · D-31b · D-44 · D-44b · D-54 |
| 13 | **Files, versions and export** · Import, versions, export, saving and file problems | D-45 · D-32 · D-32b · D-30 · D-55 · D-46 |
| 14 | **Menus, search and preferences** · Menu bar, right-click menus, search, preferences, shortcuts, find and replace | D-38 · D-48 · D-40 · D-49 · D-50 · D-51 |
| 15 | **AI tools and MCP** · Apps working in Daisy through MCP | D-59 · D-59b · D-59c |

The design system sheets (D-00 a–e) stay on their own page, "D-00 Design system".

### Phase A — Design system

**D-00 Design system sheet** (may be taller than 1080)
- Colour tokens for both themes as labelled swatches.
- The type scale with real UI examples.
- Spacing scale, sizes and radii.
- Icons: all 18 tool icons plus the generic glyph set.
- Every component C-01 to C-32 in every state listed in 9.8.
- Overlay colour key (7.2) with a mini example of each.
- *Checks:* all states present; contrast of `text-muted` on `bg-panel` is at least 4.5:1; there is a visible focus ring on every interactive component.

### Phase B — Shell and first run

**D-01 Home, first run** (v0.2, project model)
- `bg-panel` full screen, with a 40 px top bar (`bg-titlebar`): brand mark tile, "Daisy" (12 semibold), Preferences gear on the right.
- Centred column 480 wide, slightly above centre: title "Your projects" (`ui-display`), the sentence "A project holds your pages and one design system they all share. Every new page starts as one empty section. You build everything else." (13 / 20, `text-secondary`).
- Two buttons, 32 h, radius 6: **New project** (primary, key badges `Alt` `N`) and **Open file…** (outline, file icon, `Ctrl` `O`).
- Under a 1 px `line` divider, one info line (11 px `text-muted`): Open file edits one HTML page on its own, without a project, and can be added to a project later; an `.html` file can also be dropped anywhere in the window.
- Nothing else. No templates or suggestions.

**D-02 Home with projects, plus the New project dialog** (v0.2, project model)
- Top bar as D-01, plus the search bar centred: "Search projects and files" `Ctrl P`.
- Content column 1488 wide, 48 px from the top. Title row: "Your projects" (`ui-display`), then a sort menu "Last edited ▾", **Open file…** (outline) and **New project** (primary, + icon), all 28 h.
- **Project cards**: 240 wide, 6 per row, 16 gap, radius 6, `#1a1a1a` with a 1 px `bg-workspace` ring (hover: `line-strong` ring). Thumbnail 240 × 150 on `bg-workspace` showing the project's Home page. Under it: name (12 medium) and "4 pages · Edited 12 minutes ago" (11 `text-muted`), and a ⋯ menu: Open, Rename, Duplicate, Save a copy, Delete.
- **Recent files**: heading (14 semibold) + "Single pages opened without a project". Rows 36 h: file icon, file name (mono 12), folder (mono 11 `text-muted`), "Opened 2 hours ago", and an "Add to project" ghost button.
- "Recently deleted (2)" link with a trash icon at the bottom.
- **New project setup** (1200 × 760 window over a 50% scrim, Visual Studio-style steps; full steps on D-02b). Left rail of steps: **Project** · **Design system** (with Colours · Typography · Spacing & layout · Shape & depth nested under it) · **Review**; done steps get a green check, the current one an accent dot and tint. Footer: "Step 1 of 7", Cancel, Back, **Create with defaults** (uses suggested values for the remaining steps), Next. Rail footnote: "Every value can be changed later in Project › Design system." D-02 shows **Step 1 · Project**: "Configure your new project"; Project name (Mossbank Tea, selected); Location `D:\Sites` + Browse…, "Files go to D:\Sites\mossbank-tea\"; First page: Page name Home · File `index.html` · Language English en; Site: Address (optional) · Favicon. Note: the project starts with one page holding one empty section; screen sizes are set in Spacing & layout.

**D-02b New project · setup steps** (v0.2, sheet `D02b-NewProject-Steps.dc.html`, 2592 × 4520, at 0, 15600). Each step is the 1200 × 760 window; steps 3–7 have a 320 **Live preview** (Light / Dark) of a sample page (nav, eyebrow, heading, body, two buttons, a product card, a field, status chips) that applies the tokens and outlines what the step changes.
- **2 · Design system**: four choices as large radio rows: **Build a new design system** (Recommended; four short steps, each with defaults) · **Copy from a project** (copied once, not linked) · **Import tokens** (W3C Design Tokens .json, CSS variables .css, Figma variables .json) · **Skip for now**. Note: "Not a template: no pages or content are added." Variants: Copy shows a radio list of projects with token counts, fonts and colour chips, and fills the detail steps with that project's values; Import shows a drop zone; Skip removes the detail steps from the rail (Step 2 of 3, "Next: Review", no Create with defaults).
- **3 · Colours**: roles Primary, Secondary, Neutral, Success, Warning, Danger (+ Add a colour role), each a base hex field and an **11-step scale** 50–950 with the base marked. Generation: Scale method (OKLCH, even lightness) · Neutral tint (Warm, from Primary) · Contrast target (AA) · Advanced. **Roles · light theme**: Background neutral-50, Surface white, Text neutral-900, Text muted neutral-600, Border neutral-200, Link primary-700, Button primary-600, Focus ring primary-400; "Also make a dark theme" switch. Footer: 6 roles · 66 colours · 16 role tokens.
- **4 · Typography**: Headings Fraunces (variable) · Body Inter (variable) · Code JetBrains Mono; Google Fonts, self-hosted on export; Upload a font…. **Scale**: Base 16, Ratio Major third 1.25, On small screens Minor third 1.2, Base on small 15, "Fluid between 390 and 1440" on. Table of 8 styles (Display, H1–H4, Body, Small, Caption) with live samples, min → max size and line height. Advanced: letter spacing, weights per style, text case.
- **5 · Spacing & layout**: Base unit 4 / 8, Steps (base × 0.5 … 24), Names (space-1 … space-10), 11 chips 0–96 (+). **Screen sizes and grid**: Desktop 1440 · 12 col · margin 64 · gutter 24 · max 1280; Tablet 768 · 8 · 32 · 20 · fluid; Mobile 390 · 4 · 20 · 16 · fluid; + Screen size; a 12-column grid strip. These become the editor's screen sizes.
- **6 · Shape & depth**: Corners Sharp / Soft / Round, Buttons use md · 8, radius scale none 0 · sm 4 · md 8 · lg 16 · xl 24 · full 999; Borders thin 1, thick 2, colour neutral-200; Shadows levels None / 2 / 3, tint neutral-900 8%, previews shadow-1…3; Motion fast 120 · base 200 · slow 320 ms, easing Standard (off for reduced motion).
- **7 · Review**: one row per area with a summary and Edit; Output: Naming (role and step, `--color-primary-600`), Prefix; a `tokens.css` preview; files tokens.css ✓, tokens.json (W3C Design Tokens) ✓, Figma variables; "Open the design system after creating" ✓; primary **Create project** (142 tokens).

**D-03 Editor, fresh project** (v0.2, after the setup steps of D-02 / D-02b with Build new)
- The full editor layout (2.1) built from D-04, with the Select tool active. Search reads "Search **Mossbank Tea**".
- Page tabs: "Home index.html @ 85%" (active) and **Design system tokens.css** (opened by "Open the design system after creating", behind Home).
- Project panel: Mossbank Tea → Pages (1) → Home `index.html` (open); Design system with mini chips of primary, secondary and neutrals; Assets "0". No Single files group. (If the person chose Skip, the row shows **Set up**, D-36b B.)
- The canvas shows the 1440 page at 85% on the **Background** role (neutral-50 `#fbfaf7`) with one empty section 400 high: dashed inner outline, the hint text "Empty section — pick a tool and click here", and the section selected (1.5 px outline, handles, radius handles, name tag "Section · section" drawn inside the top edge because there is no room above). The "+ Add section" bar sits 8 px under the page.
- Options bar: Select chip › Section `section` · X 0 · Y 0 · W 1440 `Fill` · H 400 `Fit` · In flow.
- Layers has one row, "Section", selected.
- Properties: header "Section" / "Section ▾ · section"; Size (W 1440 Fill, H 400 Fit, **Min H 400** with a solid origin dot); **Layout** open with **Stack** selected and the first-use hint "Stack places children one under another. Choose Row or Grid to align and space them."; every other group in More properties (Accessibility shows "Landmark").
- Swatches: "From Mossbank Tea design system": primary-600, secondary-500, neutral-900, neutral-600, neutral-200, neutral-50, success, danger; Text styles Display (Fraunces 37–49), H1 (Fraunces 31–39), Body (Inter 15–16).
- Status bar: `Page › Section`, notice "✓ Mossbank Tea created · 142 tokens · Pick a tool and click inside the section", "1440 × 400".
- *Checks:* clean start, no content pre-made, only the tokens chosen in setup; the canvas dominates; chrome is quiet.

### Phase C — The key editor screen

**D-04 Editor, populated page, heading selected (the reference screen)**
- The Halden page at Desktop 85%, scrolled to the top. The fold line is visible.
- The h1 "Hand-thrown ceramics…" is selected: outline, handles, name tag "Heading · h1". The dashed parent outline is on "Hero text".
- Options bar: the Select tool, with X 0 · Y 64 · W 560 Fixed · H Fit, Place In flow, and the align buttons.
- Layers is expanded to the h1 row, which is selected. The Hero grid row has its grid icon. Hero image has a ⚠ badge (missing description). "This season" has a 🖥 badge.
- Properties shows Heading: General (Name "Hero title", Kind Heading 1), Size (Width Fixed 560 with a solid dot, Height Fit), Spacing (zero), and **Typography expanded** (Fraunces, 600, 64, ink swatch "ink", line spacing 1.05) with Advanced collapsed. Other groups are collapsed with summaries.
- Swatches tab is visible in the lower right dock.
- Status bar: the full breadcrumb.
- v0.2 additions: page tabs (Home active, Shop unsaved, Journal, `promo-banner.html` as a single file); Project panel above Layers; the redesigned top bar (search "Search Halden"), options bar (capsules only, starting at 52 px, with Distribute and the C-33 trigger) and Properties (5.1: only Size and Typography open, the rest in More properties with Effects shown hovered).
- *Checks:* this screen alone should make the product's identity clear: a professional tool, real HTML visible everywhere, and a believable web page.

**D-35 Corner roundness control** (v0.2, rebuilt in the shared popover pattern; sheet `Radius.dc.html`, 1600 × 1120, moved to 5000, 0)
- **A · All corners**: 328 popover "Corner roundness · Card 1" with Pin open and Close; modes **All** · Top · Bottom · Each; preview; value 12 px with a slider; **From the design system** none 0 · sm 4 · **md 12** · lg 20 · pill, linked chip `radius-md`; Advanced button; CSS line `border-radius: var(--radius-md);`.
- **B · Each corner**: four fields around the shape (20 · 20 · 0 · 0 on the Hero image) with a link button in the middle to set them together; quick actions Top only · Bottom only · Left only · Swap · Make equal; "Top corners use radius-lg · 20"; CSS line.
- **C · Advanced**: its own popover beside A, anchored to A's pressed Advanced button (A dims): Corner shape Round · **Squircle** · Bevel · Notch (with the corner-shape fallback note); Elliptical corners (across / down); **Grow with the screen** Mobile 8 → Desktop 12; CSS line with `clamp()` and `corner-shape`.
- **D · On the canvas**: round handles inside each corner; dragging shows "18 → snaps to lg 20"; all four move together, Alt moves one, Shift stops snapping to tokens.
- **E · Triggers**: the options bar capsule (Select tool; in More on the compact frame) and Properties › Border › Corners both show "12 · radius-md" and open the same popover. One control: values are edited only in the popover or on the canvas.

**D-37 Layout advanced for Row and Grid** (component sheet, 1600 × 1470)
- A Row container with Advanced open (wrap, space between, centre, gaps 8 / 12); B Grid container with the Column 1 track editor open, presets, named areas `header header / text image`; C a child In Row (grow 1, stretch); D a child In Grid (column 1 span 2, row 2).

**D-36 Design system editor** (v0.2, `D36-DesignSystem.dc.html`, at 4000, 14000)
- Opened from Project → Design system. It opens as its own **tab**, "Design system · tokens.css" (palette icon), beside the page tabs; the Project row is marked current. Edits the project's colours, text styles, radius and spacing tokens used by every page.
- **Options bar** (this tab only): Find a token (`Ctrl F`) · All / Used / Unused · 1 · Collect from pages… (finds colours and sizes used on pages but not yet tokens) · Import · More. The page view controls are not shown; the tool strip is dimmed (page tools are off).
- **Editor** (one scrolling list, header "Halden design system · Used by 4 pages · 25 tokens", jump links Colours · Text styles · Radius · Spacing):
  - **Colours** (8): swatch · name · CSS variable `--color-…` · hex · note · uses (or an Unused tag). Shown: brand (selected), brand-deep, brand-light (Unused), ink, ink-soft, sand, clay, moss.
  - **Text styles** (5): a live specimen in the style, name and spec, tag, fluid range where set, uses. Display (Fluid 44–64), Heading 2, Heading 3, Body, Eyebrow.
  - **Radius** (4): radius-sm 4 · radius-md 12 · radius-lg 20 · pill 999, with uses.
  - **Spacing** (8): xs 8 … 4xl 96 as bars (teal, layout colour).
  - Each section has its own + add button.
- **Live preview** (420 wide, right of the list): the chosen page (Home ▾) at a small scale; uses of the selected token are outlined in accent. Edits show at once.
- **Properties** shows the selected token, and is the only place it is edited: name, value (colour field, focused), note; **Contrast** checks against white and the background tokens (text 4.5, large 3), with a hint and a one-click fix (brand on sand 4.4 and on clay 3.6 are large-only; brand-deep passes, "Use it for links"); **Used on** with uses per page (opens the page with the uses selected); Duplicate and **Replace and delete…** (a used token must be replaced first).
- Swatches are not shown in this tab (they would repeat the colour list); the dock shows **History** of token edits, with use counts.
- Layers says "No layers here", since layers belong to pages.
- Status bar: Design system › Colours › brand · "Changes apply to every page · Ctrl+Z undoes" · 25 tokens · brand · 18 uses.

**D-36b Design system · opting in later** (v0.2, sheet `D36b-DesignSystem-Setup.dc.html`, 1920 × 820, at 6000, 14000)
- Rule: a design system is made in the New project steps (D-02, D-02b), or skipped there. A skipped project **opts in later**; every token stays editable in D-36.
- A **Set up later**: the Design system tab reads "not set up": "Mossbank Tea has no design system yet", a "Found on your pages" bar (6 colours, 2 fonts, 4 text sizes, with chips), and three choices: **Start from what the pages use** (recommended; fills the steps with the found values and links them), Build a new design system, Copy from a project or import tokens. Each opens the D-02b steps without the Project step.
- B **Project panel row**: with tokens, mini colour chips; skipped, a **Set up** button. Swatches read "No design system yet · Set up".

**D-36c Design system editor · states** (v0.2, sheet `D36c-DesignSystem-States.dc.html`, 1920 × 1480, at 36000, 14000; read with D-36).
1. **Editing a text style**: Heading 2 selected in the list ("changed"); Properties edits the style: Font, Weight, Case, **fluid size** Min 32 / Max 40 over 390 → 1440, Line, Letter; a note "Changed from 40 → 32–40. 7 headings on 3 pages update. 1 heading on Shop overrides the size and keeps it." Revert.
2. **Adding a colour**: + Colour opens an inline row with the name field focused (`honey` → `--color-honey`, `C08A3E`, "new"), "Picked from Shop › Sale badge", "Also make a scale (50–950)", "Enter adds · Esc cancels · names use lowercase and dashes", Add colour.
3. **Deleting a used token**: "Delete brand-deep? It is used 6 times on 2 pages." Choose **Use another token** (brand, closest ΔE 6, suggested) or Keep the colour as a plain value; a before → after preview of an affected element; Select the 6 uses; **Replace and delete** (danger). An unused token is deleted at once with Undo.
4. **Collect from pages**: values on pages that are not tokens, by kind (Colours 5 · Text sizes 3 · Spacing 6 · Radius 2); each row: value, uses and pages, the nearest token with ΔE, and **Map** / **New token**; "20 uses change"; Apply 5.
5. **Renaming a token**: `--color-terracotta` → `--color-brand` updates 18 uses, tokens.css and Custom CSS in 2 places; "Keep the old name working" (on) writes `--color-terracotta: var(--color-brand);` for CSS outside Daisy.

### Phase D — Selection and manipulation states

**D-05 Hover vs selection vs scope** (v0.2)
- Built from D-04. **Hero text is selected** after a double-click into Hero grid, so the scope is Hero grid: 1.5 px outline, handles and the tag "Box · div" on Hero text.
- **Scope**: a dashed accent outline (60%) drawn 12 px outside Hero grid, with a scope tag on its top-right, "Inside Hero grid · Esc to go up" (accent-subtle fill, dashed border, `accent-fill-pressed` text). The breadcrumb segment for the scope container is tinted accent (`#a9c8f7`).
- **Hover**: the pointer is over Hero image: 1 px outline and the name tag "Image · img". The Layers row for Hero image shows the hover background at the same time.
- Layers: Hero text selected. Properties: header "Hero text" / "Box ▾ · div"; Size W 654 `Fill`, H 424 `Fit`; Layout open with **Row** and direction **Down**, Gap 24, alignment grid left-centre; the rest in More properties. Options bar: X 0 · Y 48 · W 654 Fill · H 424 Fit.
- Status bar hint: "Click to select Hero image · Double-click to go inside · Esc to go up to Hero grid". Pointer position x 948 y 262.
- A yellow **design note** (annotation, not part of the app UI) states the rule: a click selects the outermost element inside the current scope; Esc goes up; Ctrl+click picks the deepest element.

**D-06 Resize in progress** (v0.2)
- Built from D-04. The Hero image is being resized from the **bottom-right handle** (that handle is filled accent). Size label pill `624 × 540`, centred 8 px below.
- The page **reflows live**: Hero grid's columns follow the image, so the text column narrows from 654 to 624. A grey dashed **ghost** shows the image's size before the drag (580 × 520).
- **Size match**: magenta measure lines with end ticks over both columns, each with a pill "= 624", because the image snapped to make the two columns equal. (v0.1 said the image matches the card width; the cards are 416 wide, so the snap target was changed to the equal-columns case, which is a real snap.)
- Parent of selection: dashed outline on Hero grid. Cursor ↘ at the handle.
- Options bar: X 688 · Y 0, and the **W and H fields highlighted** (accent-subtle fill + accent ring) while they update: W 624 `Fixed`, H 540 `Fixed`. Properties Size shows the same two fields ringed, plus the note "Hero grid columns follow: both are now 624". Properties also show the Image group (file `bowls-on-linen.jpg`, Fit: Fill frame / Fit inside / Stretch) and Accessibility "⚠ needs a description" in More properties.
- Status bar: `… › Box · Hero grid › Image · img`, hint "Shift keeps proportions · Alt resizes from the centre · Ctrl turns off snapping · Esc cancels".

**D-07 Resize limited by layout** (v0.2)
- Built from D-04. The h1 is dragged wider by its **right-middle handle** (filled accent). The box stops at the **column edge**: it is 654 wide (the text rewraps to two lines), and a teal dashed line on Hero grid marks the edge with the badge "column edge · 654".
- Past the edge, the width the pointer asks for is drawn as a **hatched grey extension** to 760 with a neutral pill "wants 760". The size label turns **neutral** (`bg-control-active`): `654 × 134 · limited by column`. The cursor is the resize arrow with a small red not-allowed badge ("limited" cursor).
- Options bar W is live-highlighted and shows the value being set, `760 Fixed`; H `134 Fit`.
- Properties Size: W 760 ringed, H 134, and under the row the muted note **"Shown 654 — limited by Hero grid column"** with a **Use 654** link that sets the field to what is shown.
- Status hint: "Hero grid column limits the width to 654 · widen the column, or set Max width in Size → Advanced".
- (v0.1 numbers said 560 × 202; the Hero text column is 654 wide, so the limit is 654.)

**D-08 Flow drag: reorder** (v0.2)
- Built from D-04. The **Hero buttons** row ("Shop the collection" · "Our process →") is being dragged **above the paragraph**.
- The original stays in place at **30%**. The **ghost** follows the pointer: the row at 60% on a solid page-colour card with a faint accent ring and a soft shadow, so it reads over text. Grabbing-hand cursor.
- A **2 px blue insertion line** with 6 px end caps sits between the h1 and the paragraph (the drop position), as wide as the h1. (v0.1 put the line between the eyebrow and the h1, which contradicted "above the paragraph".)
- The target container **Hero text** gets a 1 px blue outline and the tag "into Hero text"; its Layers row gets the same 1 px outline while Hero buttons is the selected row.
- Properties show Hero buttons (Box · div, Row Across, Gap 24); options bar X 0 · Y 380 · W 298 Fit · H 44 Fit.
- Status hint: "Release to move · Esc cancels · Ctrl to disable snapping".

**D-09 Invalid drop** (v0.2)
- Built from D-04. The **Hero buttons** box is dragged onto the h1. The h1 gets a 1 px `danger` outline and a red name tag (`#c9302c`), and a **red 2 px insertion line** with end caps sits between its first and second lines, where the pointer is.
- A red pill **"Text can't contain boxes"** sits beside the pointer; the cursor is the not-allowed circle. The ghost card gets a red ring instead of the blue one. The original row stays at 30%.
- Layers: the Hero title row shows a red inset outline and "can't drop here" in place of its tag; Hero buttons stays the selected row.
- Status bar: a red warning line replaces the hint — "Text can't contain boxes · drop above or below the heading instead · Esc cancels".

**D-10 Free element with guides** (v0.2)
- A **"New" badge** (terracotta pill, 88 × 36) is placed **Free** inside Hero grid over the top-right of the Hero image and is being dragged (grabbing hand). Its name tag reads "Box · New ◇".
- **Pin lines** (dashed magenta) run from its top edge to the top of Hero grid and from its right edge to the grid's right edge, with pills **62** and **24**. The anchor, Hero grid, has the dashed accent outline.
- A solid magenta **alignment guide** runs across the grid at the badge's top edge with the pill "aligned · Hero text top" (v0.1 said "aligned to the image's top edge", which can't hold with a 24 px top pin; aligning to Hero text's top is a real snap).
- Options bar: Place **Free** selected, followed by a 24 px **pin widget** with Top and Right on; X 1200 · Y 62 · W 88 Fit · H 36 Fit.
- Layers: a new row "New badge ◇" under Hero grid, selected.
- Properties: **Placement** open — segmented In flow / Free / Fixed / Sticky (Free on), a 56 px pin widget with Top + Right on, offset fields Top 62 · Right 24 · Bottom auto · Left auto, and "Positioned relative to Hero grid ↗"; Size 88 × 36 Fit; Fill brand; Border radius Pill in More properties.
- Status notice (info, replaces the hint): "ⓘ Hero grid is now the anchor for New badge · Undo".

**D-11 Multi-selection and context menu** (v0.2)
- The canvas is scrolled to **This season** (the fold line is near the top). The three cards are selected: a 1 px outline on each card and one bounding box with handles and the tag "3 selected · Box".
- Properties show only shared groups: header "3 elements · Card 1 · 2 · 3" / "Box · div · only shared groups shown"; Size 416 Fill × 380 Fit; **Fill "Mixed"** (italic, half-and-half swatch, because Card 3's fill differs); Border Corners 12; the rest in More properties.
- Options bar: X **Mixed** · Y 952 · W 416 Fill · H 380 Fit, and **Distribute is enabled** now that 3 are selected.
- Layers: This season expanded → Season heading, Card grid → Card 1, Card 2, Card 3 all selected.
- The **element context menu** (7.5) is open at the pointer with every item, dividers and shortcuts; Paste inside, Ungroup and Rename disabled; Delete in `danger`; **Placement ▸** highlighted with its submenu open (In flow ✓, Nudged, Free (hover), Fixed to screen, Sticks when scrolling).
- Status: `Page › Section · This season › Box · Card grid › 3 selected`, hint "Shift-click to add or remove · right-click for actions · Ctrl+G to group".

### Phase E — Creation and tool-specific states

**D-12 Text tool: editing** (v0.2, redesigned after review: "very basic"; deduplicated: "one control, one place")
- The Text tool is active; the paragraph is in text editing mode (thin solid accent outline, no handles). The range "wheel-thrown" is selected and is already `strong`.
- **Rule: each control lives in exactly one place.** The floating toolbar holds inline marks, the options bar holds paragraph structure, and Properties holds kind, text style and every typography value. Nothing is repeated across the three.
- **Floating inline toolbar** on the canvas, just above the selection (40 h, radius 8, `bg-popover`, `shadow-float`), labelled "Inline marks": **B** (active) · I · U · S · inline code · link (Ctrl+K) · highlight · ⋯ (superscript, subscript, clear formatting). It follows the selection. It has no style or colour controls.
- **Options bar — text editing bar** (left to right): "Text editing" mode chip · Align L C R Justify · bulleted list · numbered list · quote · indent · hint "Marks: on the selection · Kind, style and values: in Properties" · **Done · Esc** on the right, then the usual screen-size switcher, page settings, Snap and More.
- **Properties**:
  - Header "“Each piece is…” · Paragraph ▾ · p". The kind menu (Paragraph, H1–H6, Quote, Code, List item) lives here.
  - A **scope switch** "Changes apply to: **Selected words** / Whole paragraph" with the range info (`<strong>` · 12 chars).
  - **Typography**: the **text style row** ("Ag Body · modified · Inter 18 / 1.6 · from Halden design system" + **Update style**); Font (variable); Weight + Size; Line spacing + Letter spacing; Colour. Align and highlight are not repeated here.
  - Under the Typography values, the note "Optical size, case, wrap, truncate, numbers and more: Advanced". The Typography **Advanced button is pressed** (accent ring) and opens the popover. Nothing expands inline.
- **Typography Advanced popover** (328 w, same frame as C-38, arrow on the button, Pin open and Close). Header "Typography · Advanced · Selected words".
  - Optical size slider (auto).
  - Case: Aa · AA · aa · Ab.
  - Line style for underline and strike: Solid · Dotted · Wavy · Double.
  - Wrap: Normal · Balance · **Pretty** · No wrap.
  - Truncate: Off · 1 line · Lines.
  - Numbers: Default · Tabular · Old-style.
  - Ligatures (on) · Small caps · Fluid size `clamp()`.
  - + Text shadow · + Other property.
  - The CSS line `text-wrap: pretty; font-variant-ligatures: common-ligatures;` with Copy CSS.
  - The Weight axis slider was removed: the Weight field in Properties already sets any weight (one control, one place).
- Breadcrumb ends `Text · p › strong`; hint "Esc to finish · Shift+Enter for a line break · Ctrl+B / I / U · Ctrl+K link · Ctrl+Shift+V paste as plain text".

**D-13 Box tool: drawing in flow** (v0.2, improved after review: "needs to improve")
- **Rule: one control, one place.** The tool-strip flyout picks the variant, the options bar sets how drawing behaves, and Properties sets how the new box looks. The options bar no longer repeats the variants.
- The Box tool is active; the canvas is scrolled to This season. The section gets the target outline and the tag "into This season". A 2 px insertion line after **Card grid** shows where the box goes, and the section opens room while drawing (live reflow).
- **Rubber band previews the result**: it is drawn with the chosen preset (Card: white, radius 12, space inside 16), with a dashed content hint inside, a 1 px accent ring, and a crosshair cursor with a box glyph. Under it sit two pills: `416 × 160` and a dark `1 column` pill.
- **Snapping**:
  - **Snap slots**: the grid's columns are ghosted on the new row as dashed accent outlines labelled "2 columns" and "Full width", so the width snaps to 1, 2 or 3 columns.
  - **Smart guides** (`#c2255c`, white text 4.5:1): dashed verticals show both edges lining up with Card 1.
  - **Matched spacing**: a measure with the pill "32 · grid gap" shows the 32 px gap to the grid, which equals the grid's own gap.
- **Tool-strip flyout** (248 w), each item with a one-line description:
  - Box ✓ (R) · A container `div`
  - Ellipse (Shift+R) · A fully rounded box
  - Section band (Alt+R) · Full width, a new section
  - Divider · A line `hr`
  - Spacer · Empty room in a stack or row
  - Footer: "Hold the tool 300 ms or right-click · the strip shows the last one used".
- **Options bar**, left to right:
  - In flow / Free.
  - Width Fixed / Fill · Height Fixed / Hug: how the box sizes when you let go.
  - **Wrap what I draw over** (on) · **Keep tool** (off): Keep tool stays in Box after drawing instead of returning to Select.
  - The hint "Look of the new box: in Properties", then the usual screen-size switcher, page settings, Snap and More.
- **Properties → "Next box"**: "Look for what you draw · page not selected", with a Reset button.
  - **Start from**: presets from the Halden design system, in a 3 × 2 grid with thumbnails: Plain, **Card** (like Card 1, selected), Outline, Tinted, Pill, Ink. Below them, "Match an element on the page…" with an eyedropper.
  - **Look**: Fill white 100%, Corners 12, Border none, Shadow none.
  - **Inside**: Arrange (**Stack**, Row, Grid, None), Space inside 16, Between 8.
  - **Element**: Name "Box 1" (auto), Tag `div` (suggests article or aside).
  - Buttons: Save as preset · Use for this project.
- **Layers**: a ghost row "Box 1 · drawing" (italic, accent icon, 2 px accent line on top) after Card 3, inside This season, before Footer.
- **Inset: drawing over elements wraps them**: a band over Card 1 and Card 2 rings both and shows the pill "Wrap 2 in a box"; Card 3 stays out. Caption: "Let go to wrap Card 1 and Card 2 in a new box that keeps their place in the grid · hold Ctrl to draw on top instead · Ctrl+Alt+G does the same on a selection."
- Status: `Page › Section · This season`; hint "Drag to draw · Shift square · Alt places it Free · Ctrl from the centre · Space moves while drawing · Esc cancels"; `x 480  y 1556`.

**D-14 Layout tool on the card grid** (v0.2, reworked: Layout Advanced shown as a popover; one control, one place)
- **Rule: one control, one place.**
  - The options bar sets how the tool behaves.
  - Properties → Layout holds the simple values.
  - The **Layout Advanced popover (C-38)** holds the advanced values.
  - The canvas handles edit the same values live.
- **Canvas**: the Layout tool is active on **Card grid**.
  - A teal outline and teal dashed track lines.
  - Track badges `1fr` `1fr` `1fr` above the columns, and a `+` after the last.
  - Pink hatched gap bars between the cards. The first gap bar is being dragged (stronger hatch, pink ring, pill `32`, ↔ cursor).
  - The tag "Grid 3 × 1 · Card grid" under the grid.
- **Options bar**, tool behaviour only:
  - Show: **Tracks** · **Gaps** · Space inside · **Track sizes**, as toggles in teal when on.
  - Drag steps 8 px · Alt+drag: all gaps.
  - **Make columns equal**.
  - The hint "Layout values: in Properties".
  - Arrange, Columns, Rows and Gap are no longer repeated here.
- **Properties → Layout** (simple):
  - Stack · Row · **Grid**.
  - Columns − 3 + · Rows − 1 +.
  - Gap 32, ringed while dragging.
  - The note "Tracks, separate gaps, fill order and areas: Advanced".
  - The group's **Advanced button is pressed** (accent ring) and opens the popover. Size and More properties follow.
- **Layout Advanced popover** (C-38 Grid, 328 w, `bg-popover`, `shadow-float`, radius 6). It sits to the left of the Properties panel, with an arrow pointing at the Advanced button.
  - Header: "Layout · Advanced · Card grid · Grid", Pin open, Close.
  - Columns `grid-template-columns`: track chips `1fr` (selected) `1fr` `1fr` and `+`.
    - The track editor for "Column 1 · Tide bowl": fr · px · auto · min–max · fit, with Share 1 fr (focused) and Min 0 px.
  - Presets: **Equal** (active, `repeat(3, 1fr)`) · Sidebar + main · Auto-fit cards · 12 columns.
  - Rows `grid-template-rows`: `auto` and `+`.
  - Gaps `row-gap · column-gap`: Row 32 and Column 32 (linked). Column is ringed, with "Column gap follows your drag on the canvas".
  - Fill order `grid-auto-flow`: **Row**, Column, Row · dense, Col · dense.
  - Items inside cells `justify-items · align-items`: Stretch and Stretch, as picture buttons.
  - Named areas `grid-template-areas`: off.
  - A live preview of 3 cells, with Column 1 highlighted.
  - CSS line `display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px;` and Copy CSS.
- **Popover rule** (applies to 5.1 Level 3): a group whose Advanced is a full editor opens it as a 320–328 popover beside the Properties panel, anchored to the group's Advanced button. This covers Layout (C-38) and Corners (C-33). The popover can be pinned open and stays in sync with canvas drags. (Superseded in D-20: every group's Advanced opens as a popover; nothing opens inline.)
- **Inset** (bottom left): the same tool on a Row (Hero buttons).
  - The direction arrow "Row → · click to flip" and a hatched gap.
  - Grow toggles under each child (blue = grows to fill).
- Status: `Page › Section · This season › Box · Card grid`; hint "Drag a gap bar to change the space between · drag a track line to resize columns · + adds a column · Alt+drag sets every gap".

**D-15 Spacing tool on the Hero section** (v0.2, reworked: Spacing Advanced popover; one control, one place)
- **Rule: one control, one place.**
  - The options bar sets how the tool behaves.
  - Properties → Spacing holds the simple box diagram.
  - The **Spacing Advanced popover** holds per-side units, tokens and the advanced CSS.
  - The canvas bands edit the same values live.
- **Canvas**: the Spacing tool on the Hero section.
  - Green bands for space inside, with values written in them (72 top, 64 sides, 96 bottom).
  - The top band is being dragged: accent bottom edge, ↕ cursor, green pill `72 · 3xl` in `#237a33`.
  - A **snap ladder** under the pill shows the nearby Halden spacing tokens, `48 xl · 64 2xl · **72 3xl** · 96 4xl · Halden spacing`, with the current stop in green.
  - The h1's space outside is 0, shown as a 5 px orange grab strip with the pill "outside 0".
- **Options bar**, tool behaviour only:
  - Show: **Inside** (green) · **Outside** (orange) · Between.
  - A drag changes: **One side** · Opposite · All four.
  - **Snap to Halden spacing** · Allow negative.
  - The hint "Values: in Properties".
  - The four-side value fields, Space between and Unit are no longer repeated here.
- **Properties → Spacing** (simple):
  - The box-sides diagram, with the inside top value ringed.
  - Centre horizontally.
  - The group's Advanced button is pressed (accent ring) and opens the popover.
  - Size and More properties follow.
- **Spacing Advanced popover** (328 w, same frame as C-38: arrow pointing at the Advanced button, Pin open, Close). Header "Spacing · Advanced · Hero · section".
  - Inside `padding`:
    - A mode switch: **Each side** · Pairs · All.
    - Rows Top / Right / Bottom / Left, each with a value, a unit menu (px, rem, %, vw) and a **design-system token chip**: 72 `3xl` (focused, follows the drag), 64 `2xl`, 96 `4xl`, 64 `2xl`.
  - Outside `margin`: All 0 px, linked.
  - **Shrink on small screens** `clamp()` (on): Mobile 40 · Desktop 72, which writes `top: clamp(40px, 5vw, 72px)`.
  - Follow text direction (logical sides): off.
  - **Offset when linked to** `scroll-margin-top` (on): 68 px, "= header height".
  - A CSS line with Copy CSS.
- **Inset** (bottom left): Between turned on over Hero text, a Stack with 3 gaps.
  - Pink hatched gaps 16 · **24** (being dragged) · 32, sized to their values.
  - Caption: each gap can differ. The tool writes a margin on the child below, or one gap on the Stack when all gaps are equal (Alt+drag).
- Halden spacing tokens used here (sample project): xs 8 · sm 16 · md 24 · lg 32 · xl 48 · 2xl 64 · 3xl 72 · 4xl 96.
- Status: hint "Drag a band to change the space · Alt: opposite side too · Shift: all four · Ctrl: ignore the spacing snap · double-click to type".

**D-16 Transform and Gradient tools** (one screen, Gradient as an inset; reworked: Transform Advanced popover, rotation dial, one control, one place)
- **Rule: one control, one place.**
  - The options bar sets what the corners do, plus actions.
  - Properties → Transform holds Rotate, Scale and Move.
  - The **Transform Advanced popover** holds origin, separate scale, skew, 3D and order.
- **Canvas**: the "New" badge, placed Free at the top left of the hero image, is rotated **−8°**.
  - The bounding box and handles rotate with it, and a grey dashed ghost shows the untransformed box.
  - A small teal origin dot sits at the centre. It no longer covers the label.
  - A **rotation dial** is drawn behind the element: a dashed teal circle around the origin with ticks every 15° (longer at 45°), a dashed 0° reference line, the teal −8° line and a teal wedge between them.
  - The rotate cursor is at the top-right corner. Pills under the badge: `−8°` and "Shift snaps to 15°".
- **Options bar**, behaviour and actions:
  - Corners drag to: **Rotate** · Scale · Skew · Move.
  - **Angle snap 15°** · **Show dial** · **Origin draggable**, as toggles.
  - Flip H / V · Reset all.
  - The hint "Values: in Properties".
  - Rotate, Scale, Move and Origin are no longer repeated here.
- **Properties → Transform** (simple):
  - Rotate −8° (ringed) · Scale 100% · Move X 0 · Y 0.
  - The note "Origin, separate scale, skew, 3D and order: Advanced".
  - The Advanced button is pressed and opens the popover.
  - Placement follows (Free), then More properties.
- **Transform Advanced popover** (328 w, same frame as C-38, with Pin open and Close). Header "Transform · Advanced · New badge · div".
  - Origin `transform-origin`: a 9-point picker (centre) with X 50% and Y 50%.
  - Scale `scale`: X 100% and Y 100%, linked.
  - Skew `skew()`: X 0° and Y 0°.
  - 3D (`rotateX · rotateY · perspective`): off, so X 0°, Y 0° and Persp. 800 are dimmed.
  - Order (transform list) with + Add:
    - Draggable rows `rotate -8deg` (highlighted) and `translate 0 0`, each with a remove button.
    - The note "Drag to reorder: rotate then move is not the same as move then rotate."
  - **Use separate properties** (`rotate · scale · translate`): on.
  - A CSS line `rotate: -8deg; transform-origin: 50% 50%;` with Copy CSS.
- **Inset: the Gradient tool** on "Book a visit" (880 w). It shows the tool's options bar, the canvas and the gradient editor it opens, so its values also follow one control, one place:
  - **Options bar** (behaviour only):
    - Click the line **adds a stop**.
    - **Snap stops to 25%** · **Show stop labels** · Edit every fill layer (off).
    - The hint "Values: in the gradient editor". Type, stops and angle are no longer in the bar.
  - **Canvas**:
    - The gradient line runs **under** the button (so it never strikes through the label).
    - Three stops labelled 0% · **50%** (just added, ringed in accent) · 100%, with a faint 25% snap tick.
    - Caption: "Drag the line ends to set direction · drag a stop to move it (snaps at 25%) · click the line to add one".
  - **Gradient editor popover** (344 w, opened from Properties › Fill › gradient layer, or by double-clicking a stop). Header "Gradient · Fill layer 1 · Book a visit".
    - Linear · Radial · Conic, and Angle 90°.
    - A stop strip.
    - Stop rows, each with swatch, name, position % and remove: `terracotta · brand token` 0 · `#C8663A · just added` 50 (selected) · `#D97A4E` 100.
    - **Blend** `oklch`: sRGB · **Smooth**.
    - Repeat · Reverse · ⋯ (Apply to text, Save to design system).
    - The CSS line `linear-gradient(90deg in oklch, #b5532d, #c8663a 50%, #d97a4e)`.
- Status: hint "Drag outside a corner to rotate · Shift snaps to 15° · Alt rotates around the opposite corner · drag the origin to move it · Esc cancels"; `x 838  y 196`.

**D-17 Media placed + describe prompt; Link popover** (v0.2, reworked: Assets picker popover; one control, one place)
- **Rule: one control, one place.**
  - The options bar sets how the Media tool behaves.
  - Properties → Image holds the source, fit and description.
  - The **Assets picker popover** holds browsing.
  - The media kind (Image, Video, Audio, Embed, Icon) is chosen in the tool-strip flyout and the header's kind menu, not in the options bar.
- **Canvas**: the Media tool placed a new image in Card 2.
  - A grey placeholder `#d9d9d9` with an image icon and "Drop a file here · or pick a source in Properties".
  - It is selected, with the just-created tag glow ("Image · img").
- **Options bar**, behaviour only:
  - New media: **Ask for a description** · **Load when scrolled to**.
  - Uploads: **Optimise · WebP** · **Max 2560 px**.
  - Keep tool.
  - The hint "Source, fit and description: in Properties".
  - Kind, Source, Fit and the describe field are no longer repeated here.
- **Properties → Image**:
  - Source Upload · **Assets** · URL. Assets is pressed with an accent ring and opens the popover.
  - Fit "Fill frame" `cover`.
  - **Describe this image** (warning, "required", focused field) with "Picking an asset fills this in from its saved description."
  - Decorative switch.
  - Then Size 384 Fill × 288 `4:3` and More properties. Layers: Card 2 expanded with the new Image row (⚠).
- **Assets picker popover** (328 w, same frame as C-38, arrow pointing at the Assets button, Pin open and Close). Header "Assets · Halden · 12 files".
  - A search field "Search names and descriptions".
  - Tabs **Images 9** · Icons 2 · Video 1 · Unused.
  - A 3 × 2 thumbnail grid with name and size: tide-bowl, **ember-mug** (selected, accent ring), linen-plates, studio-wheel, glaze-tests (⚠ no saved description), river-view.
  - A details box: "ember-mug.jpg · 412 KB · WebP 96 KB · used 1×", with the **saved description** ✓ "Ember mug in matte black glaze on a linen cloth" and the note "Saved description · it fills in the image's alt text".
  - Footer: Upload · the legend "⚠ = no saved description" · **Use image** (primary).
- **Assets keep a saved description** per file. Picking one fills the image's `alt`. Editing the alt offers to update the saved one.
- Inset (moved to the left, over Card 1): the **Link popover** (360) over "Our process →": "Where should this go?" with Web · **Section** · Email · Phone · File, a section list (Hero, **This season ✓**, Footer, with their `#ids`), Open in new tab, the resulting `href="#this-season"`, Remove and Done.
- Status: hint "Drop a file on the frame · pick an asset in Properties · Enter uses the picked asset · Esc keeps the empty frame".

**D-18 Elements panel and Place tool** (v0.2, reworked: element card popover, ghost preview; one control, one place)
- **Rule: one control, one place.**
  - The Elements panel picks and arms an element.
  - The **element card popover** shows what it is and which variant it starts as.
  - Properties holds the settings for what gets created.
  - The options bar sets how placing behaves.
- **Elements panel** (left dock):
  - Search "list" (focused, with a clear ×), and "3 matches · click to arm…".
  - Category Lists: **Bulleted list · 3 items `ul`** (armed: accent-subtle row with a 2 px accent left edge), Numbered list `ol`, Description list `dl`.
  - "Also matches": Navigation `nav`.
  - The other categories collapsed with counts.
- **Element card popover** (320 w, same frame as C-38, arrow pointing at the armed row, Pin open). Header "Bulleted list `ul`".
  - A live preview in the Halden style with three sample items.
  - A plain description: "A list where order does not matter. Screen readers announce “list, 3 items”."
  - **Starts as**: **Plain** · Links · Inline row, as picture buttons.
  - A fit check ✓ "Fits in **Footer**. Footer is a Row, so the list sits beside the address as one item." If the element doesn't fit, it shows a warning with the reason instead.
  - The structure line `<ul> <li>…</li> ×3 </ul>`.
  - Save to Custom, and the hint "Enter places after the selection". It opens on hover or arm, and Pin keeps it open.
- **Canvas**:
  - The canvas is scrolled to the footer, with the target tag "into Footer".
  - The Place cursor (crosshair + dashed-square plus) and a vertical insertion line after "Riverside Works, Unit 4" (the footer is a Row).
  - A **ghost preview** of the list (dashed accent outline, 10% fill, three "List item" rows) shows where it lands and how big it will be.
- **Options bar**, behaviour only:
  - In flow / Free.
  - After placing: **Select it** · Stay armed.
  - **Show preview** · **Only valid spots**, as toggles.
  - The hint "Element settings: in Properties".
  - The armed element and its tag are no longer repeated here: they show in the panel, the card and the Properties header.
- **Properties → "What gets created"**:
  - Items 3 · Marker Disc · Item text "List item".
  - "The smallest valid structure. Text style comes from Halden · Body. Plain, Links or Inline row: in the element card."
  - The note "Tag, where it goes, wrapping, every match, accessible name, id, class and style: Advanced".
  - The group's **Advanced button is pressed** and opens the popover.
- **Place Advanced popover** (328 w, same frame as C-38, arrow pointing at the Advanced button, Pin open and Close). Header "Place · Advanced · Bulleted list".
  - **Tag**: **`ul`** · `ol` · `menu`, with "Only tags that mean the same kind of thing are offered."
  - **Where it goes** (relative to "Riverside Works, Unit 4"): Before · Inside ↑ · Inside ↓ · **After**, with "The pointer picks this on the canvas · Tab cycles it from the keyboard."
  - **Wrap the selection** (off): "Places the list around what is selected instead of beside it. Off: nothing is selected."
  - **Place into every match** (off): "Adds it to every container like Footer at once · 1 match on this page."
  - **Accessible name** `aria-label` (placeholder "e.g. Opening hours"), id —, class `footer-list`, + Attribute.
  - **Style**: **From Halden** · Bare HTML.
  - The structure line `<ul class="footer-list"> … </ul>` and **Save as preset** (to Elements › Custom). The element card no longer has its own Save button.
- Status: hint "Click to place Bulleted list after “Riverside Works, Unit 4” · Alt to place Free · Esc disarms".

**D-19 Measure and Eyedropper** (one screen, Eyedropper as an inset)
- Measure: Hero text is selected and the pointer hovers Hero image (red outline). Red lines with end ticks show **78** horizontally (Hero text's right edge to the image) and a dashed pair with **62** for the offset between their top edges. (v0.1 said 64 and 0; 64 is the grid gap, and the image sits at the end of its column, so the real distance is 78. Properties explain this.)
- **Rule: one control, one place.**
  - The canvas pills and Properties → Measure show the live values.
  - The options bar sets how measuring behaves.
  - The **Measure Advanced popover** holds pins, other screen sizes, the explanation and copy.
- **Options bar**, behaviour only:
  - Units px · rem · %.
  - From Border · Content · Outside.
  - All four sides · **To parent edges** · **Keep pins**, as red toggles when on.
  - The hint "Values: in Properties".
  - The live readout and Copy value are no longer in the bar.
- **Properties → Measure**:
  - To Hero image, horizontally **78 px** · Top edges offset **62 px**.
  - The note "Live while you hover · pins, other screen sizes, why 78 and copy: Advanced".
  - The Advanced button is pressed and opens the popover.
- **Measure Advanced popover** (328 w, same frame as C-38, with Pin open and Close). Header "Measure · Advanced · Text → image".
  - **Pinned on the canvas**, with + Pin this one:
    - ↔ 78 Hero text → Hero image · live (highlighted).
    - ↕ 62 Top edges offset.
    - ↔ 64 Grid gap · Hero grid (hidden).
    - Each row has an eye. The note: "Pins stay while you edit and update live · Shift+click on the canvas adds one."
  - **Across screen sizes** (this gap): Desktop 1440 **78 px** · Tablet 768 **40 px** · Mobile 390 "stacked, ↕ 32 px" —.
  - **Why 78**: "Grid gap 64 + 14 px left over in the image's column (the image is fixed at 580 in a 594 column)." Two actions:
    - **Make it 64 · image fills its column**.
    - **Snap to 72 · 3xl**.
  - **Copy as**: Value · CSS · Spec note · Image with redlines.
- Inset (moved bottom left so the popover has room): the **Eyedropper** loupe (120 px circle, 10× pixels, centre pixel outlined) over "Book a visit", with the label "#B5532D · brand" (matched to the swatch name); options Apply to Fill · Text · Border, Sample Pixel · Element colour.
- Status: hint "Hover another element to measure · Shift+click pins it · Alt with Select does the same · C copies the value".

### Phase F — Properties depth, states and responsive

**D-20 Properties: Size Advanced and custom values** (v0.2, reworked: Advanced as a popover; one control, one place)
- **Rule: every group's Advanced opens as a popover.** No group expands inline any more. Properties holds the simple values; the popover holds limits, custom values and rarely used settings; a value appears in only one of them.
- **Canvas**: Hero grid is selected (blue outline, handles, tag "Grid · Hero grid"). Select tool, standard options bar (X 0 · Y 0 · W 1312 Fill · H 520 Fit).
- **Properties → Layout** (simple): Stack · Row · **Grid**, Columns − 2 +, Rows − 1 +, Gap 64.
  - A **tooltip** over the Gap label (dotted underline): "Space between · `gap` · 64px".
  - An amber `custom tracks` tag with "Column sizes are set in Advanced". The track values (`1.1fr 1fr`) live only in the Layout Advanced popover (C-38, shown in D-14), so they are not repeated here.
- **Properties → Size** (simple): W 1312 Fill · H 520 Fit. An amber `limits` tag with "Max width is a custom value · Advanced". The **Advanced button is pressed** and opens the popover.
- **Other properties** (open, count 1): one row `isolation` `isolate` with a remove ×, "+ Add property", and the note "CSS that no group covers. Typing a property a group owns (e.g. gap) moves it to that group."
- More properties follow (Placement, Spacing, Fill, Border, Effects, Visibility, Accessibility, Attributes).
- **Size Advanced popover** (328 w, same frame as C-38, arrow on the Size Advanced button). Header "Size · Advanced · Hero grid", Pin open, Close.
  - **Width limits** `min-width · max-width`: Min 0 px · Max `clamp(320px, 92vw, 1312px)` (focused) with the amber `custom` tag.
  - **Custom value editor** for `clamp()`, "Grows with the window": Min 320 px · Ideal 92 vw (focused) · Max 1312 px. **Resolves to**: Desktop 1440 → 1312 px · at most; Tablet 768 → 707 px; Mobile 390 → 359 px. Actions **Edit as text** · **Back to a fixed value**.
  - **Height limits** `min-height · max-height`: Min auto · Max none.
  - **Aspect ratio**: **Auto** · 1 : 1 · 4 : 3 · 16 : 9 · Custom.
  - **Content that does not fit** `overflow`: **Show** · Clip · Scroll · Auto.
  - **Size includes** `box-sizing`: **Border and padding** · Content only.
  - CSS line `max-width: clamp(320px, 92vw, 1312px);` and Copy CSS.
  - (v0.1 used `clamp(320px, 90vw, 1280px)`; that caps the grid at 1280, but it is 1312 wide in the 1440 page, so the value was changed to match.)
- Status: hint "Hover a label to see its CSS name · Advanced holds limits and custom values".

**D-21 State editing: Mouse over** (v0.2, with the States popover)
- **Subject**: the hero button **"Shop the collection"**. v0.1 used "Book a visit", but that button sits under the popover area at the top right.
- **Canvas**: the button is held in its hover state (darker terracotta `#9b4424`, white text 6.5:1).
  - Selection outline and corner handles.
  - The name tag in the state fill `#7c4ed8` with ⌖: "Shop the collection · Mouse over".
- **Options bar**: the state chip "⌖ Editing: Mouse over ×" (`state-subtle` fill, × goes back to Normal), then the normal Select capsules (X 0 · Y 0 · W 187 Fit · H 44 Fit …).
- **Layers**: Hero buttons expanded. The **Shop the collection** row is selected, with a ⌖ badge (has a Mouse over state).
- **Properties**:
  - **Header**: the State button "⌖ Mouse over ▾" (pressed, accent ring, only the ⌖ icon violet) opens the States popover. Line 2: Button · `a` · "1 change in this state" in accent text.
  - **Fill**: the override `#9B4424` 100% with the accent dot and accent ring. Below it: "Normal: terracotta · Reset · + Save as swatch". The colour is not in the design system yet.
  - **Typography**: muted values from Normal (Inter, Medium, 16, white), with "Grey values come from Normal · change one to set it for Mouse over only."
  - **Transition**: the inline suggestion "▶ Animate this change? Fill · 200 ms · Smooth" with **Add** (`accent-fill`) and a dismiss ×, in an accent-tinted box.
  - More properties: Size, Spacing, Border, Effects, Link `#shop`, Accessibility.
- **States popover** (328 w, same frame as C-38, arrow on the State button, Pin open and Close). Header "States · Shop the collection · a".
  - Rows, each with its CSS selector and change count:
    - Normal (base).
    - **Mouse over** `:hover` · 1 change (checked).
    - Pressed `:active` · 0.
    - Focused `:focus-visible` · 0 ⚠.
    - Disabled `[disabled]` · 0.
  - A warning box: "Focused only has the browser's default ring. **Add a focus style**".
  - + More: Visited link · Focus within · Placeholder…
  - Switches: **Hold the state on the canvas** (on) · **Show all states side by side** (on) · Apply to every "Shop" button (off).
  - The CSS line `a:hover { background: #9b4424; }` with Copy CSS.
- **Inset: all states side by side** (bottom left, 700 w): Normal · **Mouse over** (ringed in accent, "1 change") · Pressed (dimmed, "same as Normal") · Focused ⚠ (browser ring).
  - Caption: "States without changes are dimmed · ⚠ Focused shows only the browser ring." Clicking one edits that state.
- Status: hint "Editing Mouse over · only changes are saved · Esc or × goes back to Normal · selecting another element resets to Normal".

**D-22 Responsive: Tablet** (v0.2, with the size-compare popover; amber only for mode cues)
- **Screen-size switcher** (options bar, right): **Tablet 768** active (amber tablet icon, pressed), Desktop and Mobile as icons.
- **Canvas**: the 768-wide page at **100%**, with the label "▯ Tablet · 768 · applies up to 1024".
  - The page shifts left so the popover does not cover it.
  - Header padding 32 · Hero one column (h1 48 px, image 704 × 180) · This season with the cards in **2 columns**.
  - The h1 is selected. Its name tag "Heading · h1" has a small amber tablet icon: it has Tablet overrides.
  - The tab reads `index.html @ 100%`. The status shows 100% and `768 × 2480`.
- **Options bar**: the amber chip "▯ Editing: Tablet and smaller ×" (× returns to Desktop), then the normal Select capsules (X 0 · Y 0 · W 704 Fill · H 101 Fit …).
- **Layers**: tablet badges (amber icon) on Hero grid, Hero title, Hero image and This season, the elements with Tablet overrides.
- **Properties** (accent only; amber appears only as small tablet icons):
  - The context strip (neutral `bg #232323`) "▯ Tablet and smaller · 2 values set here" with **Show only these**.
  - **Size**: W 704 Fill (solid accent dot, set here) · H 101 Fit (hollow grey dot, from Desktop), with "Width: Fixed 560 on Desktop · Fill here".
  - **Typography**: Fraunces, Semibold, Line 1.05 and ink with **hollow grey dots** (from Desktop) · **Size 48** with the solid accent dot and accent ring (set here).
  - A legend: "● set here · ○ from Desktop".
  - The hollow dots are grey, not amber, so the panel stays one colour.
- **Font size popover** (opened by clicking the Size field's dot; 328 w, same frame as C-38). Header "Font size · Hero title · across screen sizes".
  - Rows:
    - Desktop 1440 · base **64 px**.
    - **Tablet and smaller ≤ 1024 · set here 48 px** (selected).
    - Mobile ≤ 640 · from Tablet 48 px (dimmed).
  - Actions: Reset to Desktop · Use 48 everywhere.
  - **Or make it fluid** `clamp()` ("one value, no breakpoints"): Min 36 px · Ideal 5 vw · Max 64 px.
    - A preview of "Aa" at 390 · 36, 768 · 38 and 1440 · 64.
    - **Use fluid** (primary).
  - The CSS line `@media (max-width: 1024px) { h1 { font-size: 48px; } }` with Copy CSS.
  - This replaces v0.1's tooltip.
- Status: hint "Editing Tablet and smaller · changes apply up to 1024 px · hollow dots come from Desktop · click a dot to compare sizes".

**D-23 Responsive: Mobile + Visibility + Screen sizes dialog** (v0.2)
- **Screen-size switcher**: **Mobile 390** active (amber phone icon). Tab `index.html @ 100%`; status 100% · `390 × 3120`.
- **Canvas**: the 390-wide page at 100%, labelled "▯ Mobile · 390 · applies up to 640".
  - The h1 is 48 px (from Tablet), and the buttons and the image stack.
  - In the header, the hidden **Nav links** show as a dashed accent placeholder "⊘ Nav links hidden", visible only while the element is selected.
- **Options bar**: the amber chip "▯ Editing: Mobile ×", then the Select capsules showing — (the element is not rendered at this size).
- **Layers**: **Nav links** selected and dimmed (struck through, with a crossed-out eye) and an amber phone badge. Tablet badges stay on Hero grid and Hero title.
- **Properties** (accent only):
  - Header "Nav links · Row · nav".
  - A neutral context strip "▯ Mobile · 1 value set here · Show only these".
  - **Visibility**: three large toggles, Desktop and Tablet **on**, **Mobile off** (crossed-out eye, accent ring), with "● Hidden at 640 px and smaller · `display: none`".
    - An info box: "The site has no way to reach these links on Mobile." with **Add a menu button** (primary).
  - Layout: Row, Gap 32 (hollow dot, from Desktop).
  - More properties.
- **Inset: Screen sizes dialog** (560, opened from + in the screen-size switcher or Page settings › Screen sizes). Header "Screen sizes · Halden · all pages".
  - Columns ICON · NAME · APPLIES UP TO · CANVAS, with a ⋯ menu per row:
    - Desktop — base, above 1024 · 1440 px.
    - Tablet ≤ 1024 px · 768 px.
    - **Mobile ≤ 640 px · 390 px** (current row, accent).
    - Icon pickers with a chevron.
  - **+ Add screen size**, and Common presets: Wide 1920 · Laptop 1280 · iPad 834 · Phone 375.
  - **Mobile-first** switch (off), explained in plain words: "Off: Desktop is the base and smaller sizes change it (`max-width`). On: Mobile is the base and bigger sizes change it (`min-width`)."
  - The impact note "Changing a size moves every value set for it · 14 values use Tablet, 6 use Mobile".
  - Cancel · **Save**.
- Status: hint "Hidden on Mobile · shown as a dashed placeholder while selected · turn Mobile back on in Visibility to show it".

### Phase G — Panels, drawer, modes and dialogs

**D-24 Layers interactions** (v0.2)
- **Layers**: **Card 2** (This season › Card grid) is being dragged into **Hero text**.
  - The source row is dimmed (45%).
  - A blue ghost "▤ Card 2 div" follows the pointer.
  - The Hero text row has the **drop-inside highlight** (16% accent fill + 1.5 px accent ring).
  - A 2 px accent insertion line with a ring end sits after Hero buttons, its last child.
- **Canvas**: the matching target. Hero text has a solid accent outline with 6% fill, the tag "into Hero text · last" and an insertion line at its bottom.
- **Properties** (Card 2): a neutral strip "ⓘ Moving to **Hero text** · last child. It will take Hero text's width.", then Size and More properties.
- **Inset: ☰ Layers menu** (at rest, bottom left), with one-line descriptions:
  - Show inline parts (bold words, links and line breaks inside text) · off.
  - Outline view (only headings and landmarks, Alt+O) · off.
  - Show hidden elements (dimmed, with a crossed-out eye) · ✓.
  - Expand to selection (Alt+→) · Collapse all (Alt+←).
  - Show tags (div, p, h1 on the right) · ✓.
  - The menu is an inset so it does not cover the drag target.
- Status: hint "Drop inside Hero text · move up or down to drop before or after · Alt drops beside instead of inside · Esc cancels".

**D-25 Layers outline view and accessibility** (v0.2)
- **Layers in Outline view**: a removable "Outline view ×" chip (Alt+O).
  - Rows with mono badges: `banner` Header · `nav` Navigation · 4 links · `main` Main content · `H1` Hand-thrown ceramics… · **`img` Hero image ⚠** (selected) · `H2` This season · `H3` ×3 (Tide bowl, Ember mug, Linen plate set) · `footer` Footer · contentinfo.
  - Landmarks have olive badges, headings neutral badges and the image an amber badge.
  - A **Page check** box that updates as you edit: ⚠ 1 image has no description · ✓ One H1 · headings in order · ✓ Text contrast passes (lowest 6.1 : 1).
- **Canvas**: while outline view is on, small dark badges show `banner`, `H1` and `H2` beside the elements. Hero image is selected, and its tag is "Image · img | ⚠ no description".
- **Properties**:
  - **Image**: Source `hero-bowls.svg`, then **Describe this image** (warning label, "required", focused field). Under it, the warning message "Images need a description, or mark it Decorative." and the Decorative switch.
  - **Accessibility**: a read-out, not a second description field (one control, one place): Read as "image, *no name*" · Role img (automatic) · In reading order "after “Our process →”". The note: "The description is set in Image above · Hide from screen readers and roles: Advanced".
  - Then Size and More properties.
- Status: hint "Outline view · headings and landmarks only · click a row to select it · Alt+O returns to all layers".

**D-26 Assets panel** (v0.2)
- **Left dock on Assets**:
  - Search "Search assets", with an Upload button.
  - Tabs **Images 6** · Icons 2 · Video 1 · Fonts 2. "Recently added ▾ · 4.1 MB".
  - A 2-column grid with **usage chips**: tide-bowl (used 1×), **ember-mug** (used 1×, being dragged: ringed and dimmed), linen-plates (used 1×), studio-wheel (used 2×), glaze-tests (unused, ⚠ no saved description), river-view (unused).
  - A dashed drop zone "Drop files here to upload · or paste an image", and the hint "Drag onto an image to replace it · onto empty space to place a new one".
- **Canvas** (scrolled to This season): the ember-mug thumbnail is dragged onto Card 1's image.
  - The image shows the **replace highlight**: 22% accent fill, 2.35 px accent inset ring, and a centred pill "⇄ Replace image".
  - The tag "Image · Tide bowl photo". The tilted ghost thumbnail sits at the pointer.
- **Properties → On drop**:
  - Now (tide-bowl) › After (ember-mug) thumbnails.
  - ✓ "Description comes too: “Ember mug in matte black glaze on a linen cloth”".
  - "Size, fit and corners stay as they are · Alt+drop places it as a new image instead".
- Status: hint "Drop to replace this image · Alt+drop to place a new one beside it · Esc cancels".

**D-27 Code workspace** (v0.2, rebuilt as a pro tool: explorer · split editors · cascade inspector)
- The drawer opens at **420** (drag handle on top; **Maximise** fills the canvas area, Ctrl+Shift+M). Three columns plus a status strip.
- **Header**:
  - Tabs **Code** · Timeline, and the target "Hero title `h1.hero-title`".
  - The editing mode **🔒 Read-only** · Edit two-way. Two-way lets typed code update the canvas and Properties.
  - **Find in code** (Ctrl F), Maximise and Collapse.
- **Explorer** (188, left):
  - **Show code for**: **Element** · Page · Project.
  - **Files**: `index.html` (page), `styles.css` (● changed), `tokens.css` (🔒 design system), `animate.js` (generated).
  - **Rules for h1.hero-title**, with **+ Rule**: `.hero-title` (base, selected) · `@media ≤ 1024` (Tablet) · `h1` (design system) · `:hover` (none yet, dimmed).
  - Footer: "Generated from the page · edits in Properties update this live".
- **Editors** (split, centre). Each pane has file tabs, a tool cluster (Wrap lines, Split, Copy) and a breadcrumb.
  - **HTML** `index.html`: breadcrumb `… › div.hero-grid › div.hero-text › h1.hero-title`.
    - Lines 41–50, with fold chevrons on the containers.
    - Line **45** (the h1) highlighted, with bright line numbers.
    - A ⚠ in the gutter on line 49 (`alt=""`).
    - Wrap is off, so long lines end with an ellipsis.
  - **CSS** `styles.css ●` and a **Custom CSS 1** tab (custom CSS lives here now, not in a box under the panes).
    - Breadcrumb `styles.css › .hero-title › font-size`.
    - Line 14 `font-size: 64px` highlighted, with a blue change bar in the gutter (just edited in Properties).
    - Lines 22–24 (`@media (max-width: 1024px)`) marked with amber tablet icons.
    - `text-wrap: balance; /* custom */` shows where custom CSS lands.
- **Inspector** (284, right) with tabs **Cascade** · Computed · Box, context "Desktop".
  - **Cascade** lists every rule that applies, in order, each with its source:
    - `.hero-title` (styles.css:12): font-family, font-size 64px, line-height, font-weight, text-wrap "balance · custom".
    - `@media ≤ 1024` (styles.css:22, dimmed): "Not active at Desktop · Tablet and smaller".
    - `h1` (tokens.css · Halden): font-size 40px and line-height 1.2 **struck through** (overridden), margin 0.
    - `body` (inherited): color, font smoothing.
  - Footer: "Struck-through values are overridden · click any value to jump to its field".
- **Status strip** (24):
  - ⚠ **1 problem** · "img on line 49 has an empty alt" (click to jump).
  - Ln 45, Col 9 · 2 spaces · UTF-8.
  - **Copy as: HTML + CSS ▾** (also HTML only, CSS only, one file with inline styles).
- **Syntax colours**, muted and few: accent-blue `#7fb0f0` tags and selectors · green `#9cc58a` strings and values · orange `#d9a66b` numbers · neutral `#c8c8c8` · grey punctuation and comments. All are ≥ 4.5:1 on `#1b1b1b`, and there is no purple.
- **Properties**: "Attributes & Custom CSS" became **Attributes** and **Custom CSS** "1 line · in Code ↓", which opens the Custom CSS tab.
- Status: hint "Code follows the selection · click a CSS value to jump to its field · Ctrl+` toggles the drawer · Ctrl+Shift+M maximises it".

**D-27b Code workspace · states** (sheet, 1920 × 2180; read with D-27, which shows the default Read-only state). Ten states, each drawn as a real drawer.
1. **Edit two-way**:
   - The mode switch is blue, with ⟳.
   - Typing `font-size: var(--te` opens autocomplete, design-system sizes first: `var(--text-display)` 64px · Halden (selected), `--text-h1`, `--text-h2`, `clamp()`. "Tab accepts · Esc closes".
   - A side note: "Live: canvas and Properties follow", and Typography › Size will show the token chip. Undo shares the canvas history.
   - Strip: "Editing two-way · synced".
2. **Invalid code**:
   - `64pz` gets a red wavy underline (`#f47067`, 4.5:1), a red ✕ in the gutter and a tinted line.
   - A tooltip: "Unknown unit “pz”. Did you mean **px**?" with **Use 64px** · Ignore.
   - A side note: "Canvas keeps the last good value · 64px". Invalid lines are never exported.
   - Strip: "✕ 1 error · Unknown unit on line 14".
3. **Find and replace** (Ctrl F):
   - The query `hero-title` with Match case · **Whole word** · Regex, and "2 of 5" with previous/next.
   - A Replace field with Replace and All.
   - "In: **Project** ▾ · index.html 3 · styles.css 2".
   - Matches have an amber tint, the current one ringed.
4. **Computed** tab:
   - A filter field, and **Set here** · All 312.
   - Groups like Properties (TYPOGRAPHY, SIZE). Each row: property, final value (e.g. `line-height 67.2px · 1.05`) and a jump link "→ Typography". Unset values are muted.
5. **Box** tab:
   - Nested margin (orange), border (amber), padding (green) and content (accent, `560 × 202`) with real numbers, each clickable to Spacing or Size.
   - Position and box-sizing notes. "85% zoom does not change the numbers".
6. **Page scope**:
   - The target "Page · index.html · 212 lines".
   - A document outline (`<head>` "title, meta, 2 fonts", `<body>`, header "4 links", **section.hero**, section.season "3 cards", footer) beside the full file, with the selected section highlighted.
7. **Copy as** (from the status strip):
   - HTML + CSS (two blocks) · HTML only · CSS only (media queries included) · One file, inline styles (for an email or a CMS).
   - Include design tokens (adds the `--variables` it uses).
8. **Nothing selected**: an empty state, "Select something to see its code · Click an element on the canvas or in Layers", with **Show the page code** · Open styles.css.
9. **Conflict** (two-way):
   - An amber banner under the tabs: "**font-size** changed in Properties (56px) while you were typing here (60px)." with **Keep 60px** · Use 56px. Nothing is lost.
   - Strip: "⚠ 1 conflict".
10. **Collapsed and maximised**:
    - The collapsed bar keeps an amber "⚠ 1" problem badge, or a blue "⟳ editing" badge while in two-way.
    - Maximised covers the canvas area. Restore with the restore button or Ctrl+Shift+M.

**D-28 Timeline** (v0.2, rebuilt as a motion tool: sequences · tracks · curve editor)
- **Model**: animations live in named **sequences** (here "Hero entrance") with one trigger. A sequence holds element **clips**, and a clip holds **property tracks** with keyframes. Several elements can share one sequence with a **stagger**.
- **Canvas**: the frame at the playhead (t = 0.40 s), staggered:
  - The eyebrow almost in.
  - The **h1 at 90%** (6 px blur fading out), with its outline drawn at the current offset and a grey dashed "end" ghost.
  - The lede and buttons less far along.
  - The h1 tag reads "Heading · h1 · ▶ 0.40 s · 90%".
- **Drawer** at 420 (drag handle, Maximise).
  - **Header**: Code · **Timeline**, then the transport:
    - To start · previous keyframe · **Pause** (playing) · next keyframe · **Loop** (on).
    - The editable time **0.40** / 1.40 s, speed 1×, "Starts: On scroll into view ▾" (also On load, On hover, On click, Scroll-linked).
    - On the right: **Snap** to keyframes and markers (on), Add marker, a zoom slider, Maximise and Collapse.
  - **Track list** (232):
    - The sequence picker "Hero entrance ▾" with + Sequence.
    - Rows: the sequence "Hero entrance · 5 elements · stagger 0.08 s", then Eyebrow `p`, **Hero title `h1`** (expanded, highlighted) with its property rows (Opacity 0 → 100%, Move Y 16 → 0 px, Blur 6 → 0 px; each with an add-keyframe diamond), Lede `p`, Buttons `div` and Hero image `img · scale 1.04 → 1`.
    - Each element row has show and lock buttons. + Add element.
  - **Time area**:
    - A ruler 0–1.6 s (labels every 0.2 s), a blue work-area bar to 1.4 s, and a marker "Buttons ready" at 0.84 s.
    - The sequence bar, then element **clips** (accent tint, darker ends to drag, staggered 0.00 / 0.08 / 0.16 / 0.24 s). The Hero title clip is selected.
    - Property rows show diamond keyframes joined by a **curve line** that draws the easing, with the label "Smooth".
    - **Two keyframes selected** (Opacity and Move Y at 0.68 s) inside a dashed marquee.
    - A dashed stagger guide, the end line at 1.4 s, and the white playhead with its head.
    - Hint: "Drag a clip to move · drag its ends to change its length · Shift+drag keeps the stagger".
  - **Inspector** (288), tabs **Easing** · Keyframe · Sequence. Header "◆ 2 keyframes · Opacity, Move Y at 0.68 s".
    - A **curve editor** (256 × 150): grid, dashed linear reference, the blue curve, two draggable handles, and a dot at the playhead position.
    - **Presets** with mini curves: **Smooth** · Snappy · Gentle · Linear · Spring.
    - `cubic-bezier(0.2, 0.8, 0.2, 1)` with Copy, and **Apply to 2 selected**.
  - **Strip**:
    - "Less motion: **fade only, no movement** ▾" (what plays when the visitor prefers reduced motion).
    - "5 elements · 14 keyframes · 1.40 s".
    - Shortcuts (Space play · K keyframe · ← → 1 frame · Shift ← → 0.1 s) and **Copy as CSS @keyframes**.
- **Properties → Animation** (summary only): In sequence "Hero entrance · 2 of 5" · Starts at 0.08 s · Length 0.6 s · Animates Opacity · Move Y · Blur, with "Keyframes, easing and the sequence are edited in the Timeline below".
- Status: hint "Timeline · the canvas shows the frame at the playhead · drag the playhead to scrub · Shift+drag clips keeps the stagger".

**D-28b Timeline · states** (sheet, 1920 × 2180; read with D-28). Ten states, each drawn as a real drawer.
1. **Scroll-linked**:
   - The trigger chip "Scroll-linked: This season enters → leaves".
   - The ruler becomes **scroll progress 0–100%**. Card 1–3 clips are staggered, with a Move Y track.
   - A **page-scroll map** shows the section and the current position at 55%.
   - Strip: "The ruler is scroll progress, not seconds" · `animation-timeline: view()`.
2. **Recording keyframes**:
   - The record button is red, with a red border and a "● Recording" badge: "Change anything on the canvas to key it at **0.52 s**".
   - The time area has a red inset line. A new Rotate track gets a red keyframe with a halo.
   - Strip: "● 1 new keyframe · Rotate −2° at 0.52 s on Hero title".
   - **Red `#e5534b` is the recording mode colour only.**
3. **Keyframe tab**:
   - At 0.68 s · Value 0 px (focused).
   - Into this keyframe: Smooth · Snappy · Linear · **Hold** (a step).
   - Value from: Typed · Current on canvas · **Token** (a Halden spacing or size).
4. **Stagger** (popover from the sequence bar):
   - Each 0.08 s (focused) · Total 0.32 s.
   - Order: **In order** · Reverse · From centre · Random.
   - Spread: Even · **Ease out** · Ease in.
   - A live preview of the five offset bars.
5. **Sequence tab**:
   - Name.
   - Starts: On load · **Scroll into view** · Hover · Click, then When "20% visible" and Delay 0 s.
   - Plays: **Once** · Every time · Loop.
   - On screen sizes: **All** · Desktop · Tablet · Mobile.
   - Less motion: **Fade only** · Skip · Same.
6. **No animation yet**:
   - "Shop the collection has no animation".
   - Six presets with tiny previews: Fade in, Fade in up, Slide in, Scale in, Blur in, Pulse (loops · hover).
   - **Add to “Hero entrance”** · ● Record your own.
7. **Keyframe menu** (right-click): Copy (Ctrl C) · Paste at playhead (Ctrl V) · Ease: Smooth ▸ · Hold until next · Select all on this track (Ctrl A) · **Delete** (red, Del).
8. **Conflict**:
   - "**Move Y** and the hover **Scale** both write `transform`; one would cancel the other."
   - **Use separate properties** fixes it by writing `translate` and `scale` separately.
   - Header chip "⚠ 1 conflict".
9. **Performance hint** (while playing, loop):
   - The Blur track is tinted amber. A popover "● Heavy on phones · 52 fps": "Blur on a 64 px heading is costly. Move and fade are cheap."
   - **Remove blur** · Keep.
10. **Collapsed**:
    - The **mini player** (pause, "Hero entrance · 0.40 s", progress bar) while playing.
    - The red "● Recording" badge while recording.
    - A note on colours: violet = states, amber = screen sizes, red = recording. Everything else uses the accent.

**D-29 Preview mode** (v0.2)
- **No editor chrome**: the top bar, options bar, tool strip, docks, drawer and status bar are hidden. Only a 44 h **preview bar** and the page remain.
- **Preview bar**:
  - **Back to editing (Esc)**.
  - A page picker "Home `index.html` ▾", with "Links work · click to visit other pages".
  - Centre: the screen sizes Desktop · Tablet · Mobile, a custom **Width 1280 px** field (active, accent ring), Rotate, and the zoom 100%.
  - Simulation toggles: **Less motion** · **Dark preference** · **Slow network** (all off), which mimic `prefers-reduced-motion`, `prefers-color-scheme` and a slow connection.
  - **Share link** · **Open in new tab**.
- **Screen-size ruler** above the page (0–1600 px):
  - Segments Mobile ≤ 640 · Tablet ≤ 1024 · **Desktop styles · base** (highlighted, so you can see which styles apply at this width).
  - The current width marked by a 2 px accent line and the pill `1280`, and a dashed "1440 canvas" mark.
- **Page** at 1280 × 100%, centred, with a soft shadow and **drag handles on both edges** to change the width live.
  - The real hover state on **Book a visit** (darker `#9b4424` with a lift shadow) under a hand cursor.
  - The hero image shrinks to fit its column at this width.
- A corner toast: "Hover, links and animations behave as on the live site · Esc goes back".

**D-30 Export dialog** (v0.2, 1040 wide over a 55% scrim)
- **Header**: "Export · Halden · a static website you can host anywhere" and Close.
- **Left · What you get** (400): scope **This page** · Changed pages · 1 · **All 4 pages** (selected), "12 files".
  - A file tree with notes and sizes:
    - `halden-site/` 640 KB, holding `index.html` (Home, selected), `shop.html` (amber CHANGED), `journal.html`, `visit.html`, `styles.css` (all pages), `animate.js` (2 sequences).
    - `assets/images/` (6 · WebP, 512 KB) and `assets/fonts/` (2 · subset, 58 KB).
    - `sitemap.xml` and `robots.txt`.
  - A first-lines preview of the selected file (readable code).
  - "Plain HTML, CSS and a small script · no Daisy runtime · opens straight from the folder".
- **Right · Where it goes**:
  - Three cards: Zip download (halden-site.zip · to your Downloads) · **Write to a folder** (keep a folder in sync · overwrites changed files) · Publish (coming later).
  - The folder field `D:\Sites\halden-site`, with "last export 2 days ago" and Change….
  - Options in two columns, each a plain label with a one-line explanation:
    - **CODE**: Minify (CSS + JS ▾) · Class names (Readable ▾) · CSS files (One shared file ▾).
    - **EXTRAS**: sitemap.xml and robots.txt (on) · Include the .daisy source (off).
    - **IMAGES**: Format WebP with a fallback for old browsers · Quality 82 · Make sizes for each screen (srcset 640 / 1024 / 1440, on) · Inline images under 4 KB (off).
    - **FONTS**: Only the letters you use (Fraunces, Inter · −71%, on).
  - **Before you export** (non-blocking checks):
    - ⚠ 1 needs attention · Hero image has no description · **Fix**.
    - ⓘ 2 suggestions (add a focus style · social image missing) · Review.
    - ✓ All 23 links work · every page has a title · no unused images.
- **Footer**:
  - "**640 KB** · from 1.8 MB · Images and fonts are optimised · about 0.4 s on 4G".
  - ☑ Open the folder after.
  - Cancel · **Export 12 files** (primary).

**D-31 Page settings** (v0.2, lean: a 1100-wide panel over a 55% scrim; opened from the gear in the options bar or Ctrl+,)
- **Rule: only what a single page needs.**
  - Anything shared by all pages (fonts, screen sizes, redirects, site-wide code, performance and accessibility defaults) lives in **Project settings**.
  - Issues show only as a ⚠ on the section that needs attention. There are no score cards (they would repeat the Export checks).
- **Header**: "Page settings", the page switcher "Home `index.html` ▾", **Find a setting** (jumps to the field), Close.
- **Sections** (200): **General** · Search and social ⚠ · Appearance · Code · Advanced.
  - Footer note: "Fonts, screen sizes, redirects and site-wide code: **Project settings**".
- **General**:
  - **Page title** 50 / 60 (focused): "The browser tab and the headline in search results".
  - **Description** 138 / 160 · Use first paragraph: "The text under the headline in search results". Counters turn amber past the limit.
  - **Address** `halden.studio/` with the tag "home" (saved as index.html) · **Language** English `en` (read by screen readers).
  - **Status** Draft · **Published** ("Drafts are left out of exports").
- **Preview** (340), with tabs **Search** · Share · **Tab**:
  - One realistic search result that updates as you type.
  - Under it, **In the browser tab**: the favicon and the title, cut at the tab width.
  - The note: "put the important words first, tabs show about 25 characters".
- **The other sections**:
  - **Search and social**: Show in search results, social image (from Hero, an asset or an upload) and an optional shorter title and description for sharing. The Share tab of the preview shows the card.
  - **Appearance**: page background, base text font, size and colour (tokens), browser bar colour.
  - **Code**: custom code in `<head>` for this page.
  - **Advanced** (collapsed groups): canonical address, sitemap, follow links, text direction, meta tags, preload of the hero image, html and body attributes.
- **Footer**: "Changes apply as you type · Ctrl+Z undoes them" and **Done**.

**D-31b Page settings · states** (sheet, 1920 × 3050; read with D-31). Twelve compact panels with the lean sections (General · Search and social · Appearance · Code · Advanced).
1. **Search and social**:
   - The social image `share-hero.jpg` with "1200 × 630 ✓" and Replace · Crop · Remove.
   - Same title and description as search (on).
   - Previews: a link card and a chat message.
2. **Search and social · no image**:
   - An amber note: shared links will use the first image, cropped by each app.
   - Three ways to add one: From the Hero · Pick an asset · Upload. The section shows ⚠.
3. **Appearance**: page background `sand` and base text Inter 16 `ink` (tokens) · browser bar colour (phones) · simulated window height 900 · smooth scrolling.
4. **Advanced**:
   - Canonical address · In the sitemap · Text direction (Left to right / Right to left).
   - **Business details** (on), with its structured-data preview filled from the footer.
   - Also here: follow links, meta tags, preload of the hero image, html and body attributes.
5. **Code**:
   - Code in `<head>` for **this page only**. Site-wide code points to Project settings.
   - Scripts run only in Preview and the export; scripts from other sites go into the export checks.
6. **Too long and empty**:
   - Title 74 / 60 in amber · description empty, with **Use the first paragraph**.
   - The search preview shows the cut-off and borrowed text. **The tab preview** shows the long title cut off.
7. **Another page's address** (Shop):
   - `/shop` with its links updated automatically, and the old `/store` redirecting.
   - The taken name `journal` in red.
8. **Hidden from search** (Visit): **Show in search results** off (noindex, left out of the sitemap). The preview is covered by "Hidden from search results", and the section shows a crossed-out eye.
9. **Page switcher**: every page with what it is missing, and **Fill missing descriptions on all pages…**
10. **Single file** (`promo-banner.html`): no address or sitemap, and **Move into Halden…**
11. **Page title in the browser** (the preview's **Tab** tab):
    - One tab open (the full title fits).
    - Many tabs open (about 25 characters show).
    - Pinned (favicon only) and a bookmark chip.
    - Hint: "Put the words people need first · tabs show about 25 characters". The icon comes from Project settings › Favicon.
12. **Draft** (Journal):
    - A "DRAFT" strip: left out of exports and the sitemap, but you can still open it in Preview.
    - Status **Draft** · Published. Links to a draft page are flagged in the export checks.

**D-32 Versions dialog** (v0.2, 940 wide over a 55% scrim)
- **Header**: "Versions · Halden · all pages", **Name the current version**, Close.
- **List** (300):
  - A filter: **All** · Named.
  - Grouped by day (TODAY, YESTERDAY, 10 NOV). Each row has a dot, a title, a time and a one-line summary:
    - **Current** (green dot): "Unsaved changes · Hero title, Book a visit" · now.
    - Named versions (white dot, bold): **Before the Tablet pass** 13:05 · 14 changes, and **First full draft** 14:02 · 4 pages.
    - Autosaves (hollow dot): "6 changes · This season cards", **Yesterday 16:40** (selected) "3 changes · hero headline, button colour", and so on.
    - "Project created · From the Shop template".
  - Footer: "Autosaves every 10 minutes while you work · named versions are kept for good".
- **Detail**: "Autosave · Yesterday 16:40 · Home · changed areas are outlined", with a switch **Side by side** · This version.
  - Two page thumbnails, **Yesterday 16:40** and **Now**. Numbered accent outlines mark what changed: **1** the hero title, **2** the Shop button.
  - **Different from now**:
    - 1 Hero title text “Ceramics made by the river”.
    - 2 Shop the collection, fill ink instead of terracotta.
    - "+ 1 more on Shop · 0 on Journal and Visit".
- **Footer**:
  - "Restoring never deletes anything · the current state is saved as a version first".
  - **Restore as a copy** (opens it as a new page or project) · **Restore this version** (primary).

**D-32b Versions states** (v0.2, sheet `D32b-Versions-States.dc.html`, read with D-32)
1. **This version**: one page at full size; the page tabs carry a count of the changes on each page.
2. **Naming a version**: inline name field with an optional note on the Current row; Enter saves, Esc cancels. Named versions are kept for good; autosaves go after 30 days.
3. **Confirm restore**: an inline bar says that all pages go back and names the safety version saved first ("Before restore · 13:38"); Cancel or Restore.
4. **After restore**: a toast in the editor, "Restored Yesterday 16:40 · 4 pages", with Undo and a link back to Versions.
5. **Version menu**: Rename, Edit note, Restore as a copy, Download as .daisy, Delete. Only named versions can be deleted.
6. **No named versions**: the Named filter is empty, with one action, Name the current version; the footer counts the autosaves under All.
7. **Page with no changes**: "Journal is the same as now", pointing to the pages that did change, with Go to Home.
8. **Older versions**: an EARLIER group (Project created) and a note that autosaves older than 30 days were removed; a named version shows its note above the thumbnail.

**D-33 Light theme** (v0.2, `D33-Light.dc.html`, at 0, 14000)
- D-04 redrawn in the light theme from the same markup. Only token values change, and the page in the frame is untouched.
- Findings, now in 9.2: fields needed a fill (`bg-control` `#f0f0f0`), the chrome needed its own titlebar, toolbar and capsule greys, `accent-subtle` dropped to 0.12, and status colours use darker ink versions.
- **D-33b · c · d** (v0.2, at 3000 / 5000 / 7000, 16000): the colour picker over the editor, the menus sheet (D-38) and the page dialogs sheet (D-54) redrawn in light from the same markup to check popovers, menus and dialogs; the page in the frame is untouched. Findings are in 9.2 (floating surfaces and text colours).

**D-34 Compact frame check** (v0.2, `D34-Compact.dc.html`, 1440 × 900, at 2000, 14000)
- D-04 at 1440 × 900. The tool strip (44) and the docks (260 and 300) keep their widths, so the canvas column is 836 wide.
- **Zoom:** 70% does not fit (1440 × 0.7 = 1008 > 836). The canvas opens at **Fit, 55%** (page 792 wide, 22 px margin). The page tab and the status bar read "55%" and "Fit 55%". Overlay lines, handles and the name tag keep their screen sizes, so they are counted for 55%.
- **Options bar:** Distribute and Corner roundness go into More (its tooltip lists them). Corner roundness is also in Properties › Border. Everything else fits with room to spare.
- **Right dock:** Swatches | History drops from 220 to 188 high below 1000 px window height, so the whole Properties list (down to Attributes & Custom CSS) shows without scrolling.
- Left dock, top bar and page tabs work unchanged; Layers scrolls as usual. *Result:* usable and not cramped.

---

### Phase H — Gaps found in the project audit

**D-38 Menus** (v0.2, sheet `D38-Menus.dc.html`, 1920 × 1740, at 8000, 14000). Contents and behaviour are in 3.3.

**D-39 Colour picker** (v0.2, `D39-ColourPicker.dc.html`, at 10000, 14000). Built from D-04: the **Shop the collection** button is selected (outline, handles, tag "Button · a"); Layers shows it under Hero buttons.
- Properties: Fill is open; its colour field "brand 100%" is pressed (`#3a3a3a`, accent ring) because it opened the picker; "+ Add a fill layer" below. Swatches mark brand as the current colour.
- The **colour picker** is a 328-wide popover at left 1282, anchored to the field (arrow), with the shared header "Fill · Shop the collection", Pin open and Close. From top to bottom:
  - Type tabs **Solid** · Linear · Radial · Image (Linear and Radial open the gradient editor of D-16).
  - **Halden design system**: the eight colour tokens as 30 px tiles, the current one ringed in accent; Find a colour (search).
  - **On this page · not tokens**: colours the page uses that are not tokens (hero image box, View all link, card image), with **Save as token…**.
  - The picker: saturation/brightness area 304 × 150 with the cursor, hue slider, opacity slider on a checkerboard, **eyedropper** (`I`, picks from the screen) and a current-colour chip.
  - Values: format menu **HEX** (also RGB, HSL, OKLCH) · `B5532D` · 100 %.
  - **Token link**: "Linked to brand. Changing the colour here unlinks this fill. To change brand on all 18 uses, edit the token." with **Unlink** (keeps #B5532D as a plain value).
  - **Contrast** of the text on this fill (white 5.0:1, AA ✓); for a text colour it checks against the background behind it.
  - CSS line `background-color: var(--color-brand);` with Copy CSS.
- Status bar: path to Button · a; hint "I picks a colour from the screen · Alt-click a token to see where it is used".
- The same picker opens from every colour field (text, border, shadow, gradient stops, design system values); only the header and the contrast pair change.

**D-40 Search results** (v0.2, `D40-Search.dc.html`, at 12000, 14000). Built from D-04; the search bar is focused (accent ring and 3 px glow) with the query **shop**, "9 results" and Clear.
- A 760-wide results panel drops from the bar. Scope tabs with counts: **All 9** · Pages 1 · Layers 5 · Tokens 0 · Assets 2 · Commands 1; each shows its typed prefix (`/` pages, `@` layers, `#` tokens, `>` commands).
- Results are grouped: **Pages** (Shop `shop.html`, "open in a tab · unsaved") · **Layers · Home** (Shop the collection, highlighted; Shop nav link; View all →, matched on its href) with "All 5" · **Layers · other pages** (Shop grid, Shop by season) · **Assets** (`shop-hero.jpg`, used on Shop; `shop-icon.svg`, not used) · **Commands** (Export page "Shop", with its shortcut). Each row: icon, name with the match highlighted, path or detail, tag, and ↵ on the highlighted row.
- A 248 preview pane for the highlighted result: thumbnail with the element outlined, name, kind · tag · page, key properties (fill brand, text white, link, Mouse over state) and actions: **Select on the page** Enter, Reveal in Layers Ctrl Enter, Show code, Copy CSS.
- Footer: ↑ ↓ move · Enter open · Tab next group · Esc close · "Type / @ # > for pages, layers, tokens, commands".
- Inset **command mode** (typing `>`): a "Commands" chip in the field, "Backspace to leave", and the matching commands (Show code, Show tips again, Show rulers, Show hidden layers, Show history) with their menu and shortcut. These are the same names and shortcuts as the menus (3.3).
- Results on other pages open that page in a tab and select the element. Searching never changes the selection until Enter.

**D-41 Button and Link tools** (v0.2, `D41-ButtonLink.dc.html`, at 14000, 14000). Built from D-04 with the **Button** tool (`B`) active.
- Canvas: a new **Secondary** button "Gift cards" was placed after "Our process →" in Hero buttons; its label is being typed (accent caret), outline + handles, tag "Button · a · new".
- Options bar (how the tool places; the look is in Properties): In flow / Free · **The button: Goes somewhere (`a`) / Runs an action (`button`)** · Keep tool · hint "Click a row or stack to add · drag to set the size · look and destination: in Properties". This replaces the v0.1 row in 4.3 that put Label, Fill, Text colour and Roundness in the options bar (one control, one place).
- Layers: "Gift cards" under Hero buttons, selected, with a "new" badge.
- Properties: header Gift cards · Button · a. **Button** group: Style presets from the design system (Primary · **Secondary** · Text · Plain, shown as small samples) with a one-line summary of the style and **Edit style**; **Goes to** Visit `visit.html` ▾; Section (Top) ▾; New tab switch. **Accessibility**: Name "Gift cards" (from label). More properties show "from style" where the preset sets them (Spacing, Fill, Border, Typography).
- Status: "Type the label · Enter to finish · Esc removes the new button".
- **Inset · Link tool (`L`) on a whole element**: clicking a product card shows "Link the whole card"; the Link popover has destination tabs **Page** · Section · Web address · Email · Phone · File, a search ("tide") listing pages and their sections (Shop › Tide bowl `#tide-bowl` chosen), Open in a new tab, the check "Nothing clickable inside the card, so it can be one link" (otherwise the 8.x rule message), and the resulting `<a href="shop.html#tide-bowl">`. Text links are in D-17.

**D-42 Form tool** (v0.2, `D42-Form.dc.html`, at 16000, 14000). The **Visit** page (`visit.html` tab, Project row current) with a booking form; the **Form** tool (`F`) is active with its variants flyout open.
- Canvas: "Book a studio visit" with a white form card (Your name *, Email *, Day dropdown, a textarea, a checkbox, Request a visit). The form shows a dashed accent scope outline with the tag "Form · adding inside". Between Email and Day an **insertion line** with end dots and the tag "+ Label and text field · after Email", and the crosshair pointer.
- **Variants flyout** (hold the tool or right-click): Text field `input` ✓ · Text area · Dropdown `select` · Checkbox · Radio group · Label · Form `form` ("Outside a form, the first field also makes one").
- Options bar (behaviour): current variant **Text field** ▾ · Type **Phone** `tel` ▾ · **With label** (on) · **Keep tool** (on) · hint "Click in a form to add · fields line up with the ones around them".
- Layers: Booking form `form` with its fields; "Phone" shown italic in accent with "adding" where it will land.
- Properties, **Next field** (into Booking form · after Email): **Field** Label "Phone" (focused), Type Phone `tel`, Placeholder, Help text, Required switch (optional fields say "optional"); **Data** Name `phone` (from label), Autofill Phone number `tel`, Check Phone format; **Look** "Matches the fields around it · Form field · Halden". More: States, Accessibility (label tied), Size.
- **Inset · the form's own settings** (form selected → Properties › Form): **When someone sends it** Email it to me / Send to a web address / Design only; To, Subject with field placeholders, After (thank-you message), Spam check (hidden field); **Field states from the design system**: Rest, Focus, Error, Disabled.
- Status: "Click to add after Email · Alt adds without a label · Esc cancels".

**D-43 Section tool and Direct Select** (v0.2, `D43-Section-DirectSelect.dc.html`, at 18000, 14000). Built from D-04, scrolled so Hero meets This season; the **Section** tool (`S`) is active.
- Canvas: a new section is being dragged open **between Hero and This season**: a full-width band with accent top and bottom lines, a light hatch, dashed lines at the content width, the tag "+ Section · section · after Hero", the centre text "Release to add the section · Content width 1312 · from the Desktop grid", the size pill "Min H 240" and a vertical-resize pointer. This season moves down live.
- Options bar (behaviour): **Kind** Section `section` ▾ (menu open: Section, Header `header`, Navigation `nav`, Main `main`, Article `article`, Sidebar `aside`, Footer `footer`, each with a one-line meaning; "Screen readers use the kind to move around the page.") · **Content** Contained / Full width · Keep tool · hint "Click between sections to add one · drag down to set its height".
- Layers: "Section 1 · adding" between Hero and This season.
- Properties, **Next section** (after Hero · before This season): **Section** Name "Our story" (focused), Link id `#our-story` (from name), Min height 240; **Background** none / **sand** / clay / ink / moss tokens with the note that sections alternate; **Inside** Width Contained 1312, Padding Section 96 / 64 (`space-9`), Arrange Stack. More: Accessibility "Heading needed", Visibility, Effects.
- Status: "Drag to set the height · Shift snaps to the spacing scale · Esc cancels".
- **Inset · Direct Select** (`A`, or hold Ctrl): clicking the price "€38" in a card picks the text at once (tag "Text · p"), with the comparison: Select picks Card grid first and goes in one level per double-click; Direct Select picks the deepest element and moves the scope to Card 1. Path `This season › Card grid › Card 1 › p`; Alt-click picks the parent.

**D-44 Project settings** (v0.2, `D44-ProjectSettings.dc.html`, at 20000, 14000). A 1200-wide panel over a 55% scrim, the same frame as Page settings (D-31): title "Project settings · Halden · 4 pages", Find a setting, Close; footer "Applies to every page · Ctrl+Z undoes · one page only: Page settings" and Done. Opened from File › Project settings…, the Project ⋯ menu and Page settings' link.
- Sections (vertical tabs): General · **Fonts** 3 · Screen sizes 3 · Redirects 2 · Site-wide code · Export defaults; a note that colours, type sizes and spacing are tokens, with a link to Design system. Screen sizes is the same list as D-23's dialog and the setup step; Site-wide code holds head and body snippets for every page; Redirects are from → to (301 / 302); Export defaults hold folder layout, clean URLs, minify and image optimisation.
- **Fonts** (shown): Upload… and **Add from Google Fonts**; one row per font with a live sample, name and source (Fraunces · Google Fonts · variable, selected; Inter; JetBrains Mono), weight chips (used ones filled, unused dimmed, axes such as `opsz`), where it is used (text styles and the `--font-…` token, or "not used on any page yet") and its exported size; a **Fonts per page** bar (110 KB on Home · budget 300 KB). Settings: Load fonts **Self-host on export** / From Google (faster and private); While loading **Fallback, then swap** (`font-display: swap`); Characters Latin + Latin Ext.
- **Fallback** column for the selected font: switch on; Fraunces drawn over its adjusted fallback (Georgia) to show the match; Fallback ▾, Size 97.5 %, Ascent 92 %; "Matched so the page does not jump when Fraunces arrives · Layout shift 0.01"; the generated `@font-face` rule.

**D-44b Project settings · the other tabs** (v0.2, sheet `D44b-ProjectSettings-Tabs.dc.html`, 1920 × 1700, at 46000, 14000; read with D-44). Same panel frame and row pattern.
- **General**: Project name · Site address (`https://halden.studio`, used for search and social previews) · Language (pages can override) · Home page ▾ · Favicon (Daisy mark in brand, or Upload…) · Social image (default 1200 × 630 for pages without their own).
- **Screen sizes**: reorderable rows with icon, name, width and range, columns, and an on/off switch: **Desktop 1440** (design here first, from 1025, 12 columns) · Tablet 768 (641–1024, 8) · Mobile 390 (up to 640, 4) · Wide 1920 (off); + Add a screen size; grid columns and margins live in the design system. **Write CSS as** Desktop first (max-width) / Mobile first (min-width): changes the media queries, not the design.
- **Redirects**: From → To, Kind (Moved / Temporary) and where it came from ("added by Rename · today", "added by you", "checks: reachable"); a redirect to a deleted page is flagged amber; + Add a redirect · Import from a file…; exported as `_redirects`, `.htaccess` or `vercel.json`.
- **Site-wide code**: In `<head>` (every page, after Daisy's own tags; e.g. an analytics script) and Before `</body>`; "Run it in the editor and Preview" off by default; one page only: Page settings › Code.
- **Export defaults**: Export to (folder, .zip or a host) · Addresses `/shop.html` / **`/shop`** / `/shop/` · CSS one file / one per page, remove unused and minify · Images resized to the largest size used, WebP with fallback · Check links and accessibility before exporting (never blocks) · Also write sitemap.xml, robots.txt, 404.html.

**D-45 Import a page** (v0.2, `D45-ImportPage.dc.html`, at 22000, 14000). A 1240-wide dialog over a 55% scrim, opened by File › Import › HTML page or by dropping an `.html` file on the Project panel. Title "Import a page · into Halden", Choose another file…, Close.
- **Left**: a preview of the incoming page (`about.html` · 48 KB · `D:\Mine\old-site\`) and what it holds: 142 elements · 2 stylesheets · 6 images · 1 script · 1 font.
- **Middle**: Page name (About) and File in Halden (`about.html`, "free"). **How to bring it in**: Keep it as it is (same HTML and CSS, nothing linked) · **Tidy it up** (Recommended: inline styles become classes, unused CSS is removed, e.g. Bootstrap 160 KB → 9 KB, values linked to tokens where they match) · Rebuild with Daisy layouts (floats and Bootstrap columns become Row and Grid). **Colours · 9 found** (4 same · 3 close · 2 new): each with a checkbox, found value → token (ink same; `#B4542E` → brand, close ΔE 0.4; `#F3EDE4` → sand, ΔE 1.9; `#6A6A6A` kept as a plain value, new), "+ 5 more · Review all · new colours can be saved as tokens". **Also**: copy 6 images into Assets (2 resized on export) · add the font Lora · map 7 text sizes to text styles · use its header and footer on every page (off; Halden already has them).
- **Right · Before you import**: notes for positioned elements (become Free), Bootstrap columns (kept unless Rebuild), a script (kept and exported, not run in the editor), images without a description (listed in Accessibility). "The original file is not changed. Undo removes the imported page."
- Footer: drop/menu hint, Cancel, **Import page**.

**D-46 Saving and file problems** (v0.2, sheet `D46-SaveFileStates.dc.html`, 1920 × 1760, at 24000, 14000). Rule: never lose work, say what happened, offer the fix.
1. **Save status** in the top bar, left of Undo (new element for every editor screen): **Saved** (quiet, ✓ green; hover "Saved to D:\Sites\halden · 12:04"; changes are written within 2 s) · **Saving…** (only if it takes over 1 s) · **3 changes not saved** (amber tint; kept in this browser until the folder can be written) · **Couldn't save · Fix** (red tint; opens 2).
2. **Couldn't save**: a banner under the top bar, "Couldn't save shop.html. Daisy no longer has permission to write to D:\Sites\halden. Your 3 changes are kept in this browser." · **Allow again** · Save a copy elsewhere… · Details. The page tab keeps its unsaved dot.
3. **Offline**: a quiet notice, "Saving to your folder still works. Google Fonts and web images can't load until you are back online." Web fonts show their fallback with a small note on the canvas; web images show a placeholder.
4. **Changed outside Daisy**: a dialog when another app changed a file you also changed: what changed (a short diff per file), Compare in Code, **Keep mine** / **Use theirs**; the version not kept is saved in Versions. With no local changes, the file reloads silently with a status notice.
5. **File missing**: the page tab is struck through with a warning icon; the page shows "journal.html is no longer in the folder" with **Find it…**, Save it here again, Remove from project. The last version is kept.
6. **Recovered after a crash**: on the next start, Home shows "Daisy closed before saving", the recovered changes per page (with View), Discard / Open without them / **Restore changes**; discarded changes stay in Versions for 30 days.
7. **Missing image**: the image keeps its size with a hatched placeholder, the file name, **Relink…** and Pick from Assets; the status bar counts missing items with "Show in Assets". Missing fonts behave like 3.
8. **Folder permission**: before the browser's own prompt, "Let Daisy edit the Halden folder?" explains that Daisy saves straight into the folder and never uploads files; Open read-only / **Continue**.

**D-47 Fill, Border and Effects** (v0.2, `D47-FillBorderEffects.dc.html`, at 26000, 14000). Built from D-04, scrolled to This season; **Card 1** is selected (outline, eight handles, tag "Card 1 · div"); the three cards share `.card`, so the status bar says edits apply to all three.
- Properties header: Card 1 · Box · `div.card` · "same as Card 2, Card 3".
- **Fill** (layer list): one row per layer with a drag grip, preview, name, opacity, show/hide and remove: "Linear · sand → clear 60%" above "white 100%"; + Add a fill layer; "Top layer paints first · drag to reorder". Gradient rows open the gradient editor (D-16), colour rows the colour picker (D-39).
- **Border**: All sides with a **sides diagram** (click one side to edit only it) · width 1 px · style Solid · colour clay-line (token); **Corners** 12 linked to `radius-md`, with the corner control of D-35; **Outline** Focus ring only.
- **Effects** (layer list): Drop shadow · shadow-2 (selected) · Background blur 8 (hidden, dimmed); + Add an effect (drop shadow, inner shadow, layer blur, background blur); Opacity 100 % and Blend Normal on one line. The group's Advanced button is pressed.
- **Effects · Advanced popover** (328, anchored to the shadow row; Pin open, Close): Drop / Inner; **From the design system** previews none, shadow-1, **shadow-2**, shadow-3 on the page colour; "Linked to shadow-2 · Unlink to edit"; the layer values (X 0 · Y 4 · Blur 12 · Grow 0 · ink 10 %, layer 1 of 2) shown dimmed while linked; CSS line `box-shadow: var(--shadow-2);`.

**D-48 Right-click menus** (v0.2, sheet `D48-ContextMenus.dc.html`, 1920 × 2030, at 28000, 14000). The six menus of 7.5, each drawn where it opens with the pointer: the Hero title on the canvas (with the **Select layer** submenu open: Hero title ✓ h1 · Hero text · Hero grid · Hero · Page), the empty workspace, a Layers row (Card 1), a page tab (Shop, unsaved), a Project page row (Journal) and a swatch (brand). Plus the behaviour note.

**D-49 Preferences** (v0.2, `D49-Preferences.dc.html`, at 30000, 14000). Edit › Preferences… (`Ctrl ,`). A 1000-wide panel in the Project settings frame, titled "Preferences · for you on this computer"; footer "Changes apply at once" and Done. Sections: General · Appearance (theme, interface size, reduced motion) · **Canvas and editing** (shown) · Code (font size, tab size, wrap, format on save) · Keyboard shortcuts (opens D-50) · Files and saving (versions kept, recovery, default folder) · AI tools and MCP (D-59) · Privacy and updates. Note: "These are yours on this computer. Project choices are in Project settings."
- Canvas and editing: **Selecting** A click selects The outer element first / The deepest element · Show outlines on hover (with the name). **Moving and snapping** Nudge 1, with Shift 10 · Snap distance 6 (on screen, at any zoom) · Snap to Layout grid ✓, Other elements ✓, Spacing scale ✓, Whole pixels only. **Units and names** Show sizes in px / rem / As written · Show CSS names (off). **Zoom** Mouse wheel Scrolls · Ctrl zooms / Zooms · Open pages at Fit width. Reset this section.

**D-50 Keyboard shortcuts** (v0.2, `D50-Shortcuts.dc.html`, at 32000, 14000). Help › Keyboard shortcuts (`Ctrl /`). A 1180-wide panel with Find a shortcut; filters All / Yours · 1 / Most used; key sets **Daisy** / Like Figma / Like Photoshop; columns Tools · Selection · View · Editing · Files and panels with key caps. Click a shortcut to change it: the row shows "Press keys…", and a conflict bar says "Ctrl J is already Timeline · Replace · Cancel". Changed ones carry "yours". Footer: Reset all to Daisy · Print a cheat sheet · Done.

**D-51 Find and replace** (v0.2, `D51-FindReplace.dc.html`, at 34000, 14000). Edit › Find and replace… (`Ctrl H`). A 400-wide panel at the top right of the canvas: Find "Halden" with Match case, **Whole word** (on), Regular expression, "1 of 9" with previous / next and Close; Replace "Halden Studio" with Replace and **Replace all**; scope This page / **All pages** / Selection; what Text and alt text ▾. Results "9 matches · 4 pages" grouped by page with context and kind (wordmark, footer, text, alt text, h1); "+ 4 more · 1 already reads Halden Studio, skipped". Also search Links · Classes · Colours · Code. On the canvas, matches are tinted amber and the current one is outlined in accent and selected (Layers and Properties follow). Replace all is one undo step.

**D-52 Home and Help · small screens** (v0.2, sheet `D52-HomeHelp.dc.html`, 1920 × 1920, at 38000, 14000).
1. **Project card menu** (⋯ or right-click): Open · Open in a new window — Rename… · Duplicate · Project settings… — Show in folder · Export all pages… · Copy as a starting point… (tokens only) — Delete… (danger; goes to Recently deleted).
2. **Recently deleted**: back link, "Kept for 30 days, then removed for good. Files stay in your folders until then."; rows for projects and single files with where they were, when deleted and days left, Restore and Delete forever; Empty now (danger).
3. **Open and drop**: File › Open… takes a folder (a project) or an `.html` file (a single file). Dragging over Home shows a dashed accent drop zone, "Drop to open", what the drop will do, and a chip for the item ("old-site/ · 12 html files · will be a new project"); dropping on a project card adds the file to it.
4. **A tip on first use**: a popover next to what it explains ("Go inside a box · 2 of 6": double-click or Enter, Esc goes out), Turn tips off · Got it. One tip at a time, the first time something happens; never over the selection, never in a dialog; Help › Show tips again.
5. **Getting started**: an optional checklist from Help (3 of 6 with a progress bar): Add a section · Write a heading · Use a colour from the design system · Make it work on phones · Preview the page · Export your site; steps tick themselves as you work and each opens a 30-second guide on your own page.
6. **About Daisy** (version, "up to date", What's new, Licences, Copy version info) and **What's new** (opens once after an update and from Help; three items and All release notes).
7. **Couldn't check for updates** (*proposed 2026-11-14, awaiting owner approval*). Rule from D-46: say what happened, offer the fix; never silent.
   - **About Daisy** (and Help › Check for updates, which opens it): the status line "up to date" becomes ⚠ **Couldn't check for updates** (amber, the warning ink), one plain reason under it — "You're offline." · "GitHub didn't answer." · "The update file is missing from this install." — and **Try again** · Details (the error text, copyable, for Report a problem).
   - **Automatic check at start** fails: a quiet notice, like D-46 3: "Couldn't check for updates. Daisy will try again next time you start it." · Details · ✕. Once per start, never over a dialog; nothing blocks editing.
   - **Update failed to download or install**: the same notice in red (danger ink), "The update to 0.2.0 didn't finish downloading. Your version still works." · **Try again** · Details.

**D-53 Shared parts** (v0.2, `D53-SharedParts.dc.html`, at 40000, 14000). A **shared part** is a piece used on several pages (header, footer, a newsletter block); editing it once changes it everywhere. It is stored once in the project and placed on each page. Cue: a diamond icon in accent (no new colour); never violet (states) or amber (responsive).
- Canvas (Home): the header is selected with a faint accent hatch over it and the tag "◇ Site header · shared · 4 pages" under its bottom edge. The nav link "Journal" has a small accent dot: changed on this page only.
- Options bar: a chip "◇ Shared part · edits apply to 4 pages" with **This page only** (switches edits to local changes).
- Project panel: a new group **Shared parts** (Site header · 4 pages, Site footer · 4 pages) between Pages and Design system.
- Layers: "Site header" and "Site footer" carry the diamond icon and a page-count badge; changed children carry the dot.
- Properties: header "Site header · Shared part · header". **Shared part**: Edits apply to **All 4 pages** / This page only, and the pages using it (Home "1 change here", Shop, Journal, Visit). **Changes on this page · 1**: "Nav › Journal · text (shared: “Stories”)" with Reset; Apply to all pages · Reset all here. Actions: **Open in its own tab** (edit with no page around it) · **Detach** ("makes this page's header a normal copy; the other pages keep the shared one").
- Status: "Editing the shared header · changes appear on Shop, Journal and Visit too".
- **Inset · Make shared** (right-click › Make shared, `Ctrl Alt K`): Name "Site footer"; Use it on, page by page: Home (this page), Shop (same footer found · will be replaced), Journal (similar footer · 2 differences), Visit (has its own footer, kept); "New pages get it automatically"; Make shared.
- Rules: deleting a shared part asks which pages keep a copy; Undo covers all pages at once; Export writes the part into every page (plain HTML, nothing extra needed to host).

**D-54 Pages · new, rename, delete, duplicate** (v0.2, sheet `D54-PageDialogs.dc.html`, 1920 × 1630, at 42000, 14000). Rule: links between pages keep working.
1. **New page** (`Ctrl N`, Project ⋯, File): Page name (Workshops, selected) and File `workshops.html` (from the name, "free"); **Start with** One empty section (like every new page) / The layout of a page ▾ (sections and boxes, no text or images); **Shared parts** Site header ✓ · Site footer ✓; **Navigation** "Add Workshops to the Site header nav · after Journal · all pages" ✓; title and description go to Page settings; `Ctrl N` again skips the dialog with the last choices. Opens in a new tab · Create page.
2. **Rename page**: Page name Stories (was Journal), File `stories.html`; **7 links point to this page** (Site header › Nav, shared · 4 pages; Home › This season "Read the journal"; Shop › Tide bowl "How we glaze" `#tide`; + 4 more · Show all); Update all 7 links ✓ · Change link text that says "Journal" to "Stories" (2 of 7) ✓ · Keep the old address working (adds a redirect in Project settings) ✓. One undo step.
3. **Delete page**: "Delete Visit? It goes to Recently deleted for 30 days. 5 links point to it." with the list; **What happens to them** Point them to another page (Home ▾) / Remove the links, keep the text / Leave them (shown as broken in the page check); Remove "Visit" from the Site header nav ✓; Delete page (danger).
4. **Duplicate page**: Shop · Winter `shop-winter.html`; Copy the content ✓ · Copy page settings ✓ (title gets "· Winter") · Add to the Site header nav; shared parts stay shared, and this page's own changes to them are copied as changes.

**D-55 Export progress and History** (v0.2, sheet `D55-ExportHistory.dc.html`, 1920 × 1600, at 44000, 14000).
1. **Exporting**: "Exporting Halden to D:\Sites\halden-export", progress 68 % · about 6 s, steps with status: Pages 4 of 4 ✓ · CSS combined, unused rules removed (184 KB → 21 KB) ✓ · Images resized and converted to WebP (9 of 12, running) · Fonts self-hosted, only weights in use · Check links and accessibility. "You can keep working; the export uses a snapshot from 14:02" · Run in background · Cancel.
2. **Exported**: "4 pages, 1.8 MB · was 6.2 MB in the editor · images 71 % smaller"; **2 things to look at · not blocking** (an image with no description · Fix; a link to a missing `#process` · Show); Copy summary · Open in browser · **Open folder**.
3. **Export stopped**: "Can't write to D:\Sites\halden-export. The folder is read-only or another app is using it. Nothing was changed."; Details · Download as .zip · Choose another folder… · **Try again**.
4. **In the background**: the Export button reads "Exporting 68 %" with a spinner; when done, a toast "Exported 4 pages · 1.8 MB · 2 things to look at" with Open folder and Report.
5. **History panel** (right dock, tab beside Swatches; "This page ▾" / All pages): newest at the top; each step with what changed, page, time and detail; the current step has an accent dot and left bar; undone steps above it are greyed ("Redo: …"); named versions appear as pins. Click a step to go back to it (the canvas shows that moment); a new change from there drops the greyed steps. Hover shows the change; right-click: Save version here · Copy as CSS change · Show on canvas.

**Save status on every editor screen** (v0.2): the D-46 save status ("✓ Saved", hover "Saved to D:\Sites\halden · 12:04") is now in the top bar of D-04 (Main) and every screen built from it, left of Undo, including D-33 (light: `#6b6b6b` text, `#1a7f37` check) and D-34.

**D-56 Interactive parts · mobile menu** (v0.2, `D56-Interactive.dc.html`, row 04). Any element can **do something when used**; common patterns come ready-made. Cue: a small lightning icon in accent on interactive elements (Layers, name tag).
- Canvas: Home at **Mobile 390, 100 %**, drawn twice side by side: **Closed · as the page loads** (the menu button selected, tag "Menu button ⚡") and **Open · after a click** (the dark Mobile menu panel with Work, Shop, Journal, Visit and Book a visit, outlined as "Mobile menu · target"). A dashed accent arrow joins them, labelled "⚡ Click → open / close".
- Layers: Site header › Nav links (hidden at Mobile), **Menu button** `button` ⚡ (selected), **Mobile menu** `nav` ("closed") with its links.
- Properties › **Interaction**: When **Clicked or tapped** ▾ · Do **Open and close** ▾ (also Show, Hide, Go to, Scroll to, Play animation) · Target **Mobile menu** (pick on canvas with the crosshair) · Starts Closed / Open · Motion "Slide down · 240 ms" (edits in Timeline) · ✓ Close with Esc and when a link is chosen · ✓ Keep focus inside while open · ✓ Stop the page scrolling behind it · note "Screen readers hear ‘Menu, collapsed’. aria-expanded is set for you." **Preview**: show Closed / Open / **Both** on the canvas; click Open to edit the menu as it looks when open.
- Status: "Alt-click the button on the canvas to try the interaction · Preview runs it for real".
- **Inset · Elements › Interactive**: Menu for phones (button + panel) · Tabs (`tablist`, arrow keys) · Accordion (`details`) · Pop-up (`dialog`, Esc closes) · Image slider (swipe and arrows, pauses on hover) · Show and hide (any button, any part). Built on native HTML where it exists, a few lines of script otherwise; keyboard and screen-reader behaviour included.
- Export writes the HTML attributes and a small script only for pages that use interactions.

**D-57 Repeating content · collections** (v0.2, `D57-Collections.dc.html`, row 09). A **collection** is a list of items with the same fields (Products, Journal posts), stored in the project as a file (`products.json`). Elements can repeat once per item and show its fields. Everything is written out as plain pages on export; no server or database.
- Canvas (Home › This season): the Card grid is linked to **Products** (dashed scope, tag "Card grid · Products · 3 of 12 · newest first"). The first card is the one you design (outline, tag "Card · repeated for each product"), with field chips `{image}`, `{name}`, `{price}` on its parts; the other cards follow it and are dimmed slightly.
- Project panel: a **Collections** group (Products 12 · Journal posts 6). Layers: Card grid with the repeat icon and "Products"; Card "× 3"; its parts show their field.
- Properties › **Repeat**: Repeat **Products** (12 items) · Show 3, Newest first · Only "Season is Winter" (5 match) · When none: Hide the section · **Fields in the card**: Image → photo, Name → name, Price → price (€), Link → `shop/{slug}.html`. **Item pages**: one page per product from a Product page design (`shop/tide-bowl.html` + 11), all written on export.
- Status: "Design the first card; the others follow · drag a field from the collection onto an element to link it".
- **Inset · the collection's own tab** (Project › Collections › Products): a table with photo, name, price, glaze, season, in stock; Import CSV… · + Field · + Product; field kinds listed (image, text, number with currency, choice, yes/no, slug from name).

**D-58 Components and variants** (v0.2, `D58-Components.dc.html`, row 09). A **component** is a reusable piece (Product card, Button, Section heading) used many times; each use can choose a **variant** and set **options**, and editing the component updates every use. Shared parts (D-53) are the page-level case of the same idea. Cue: a four-diamond icon in accent.
- Canvas: the third card (Linen plate set) is selected; tag "◈ Product card · Sold out"; it shows the Sold out variant (dimmed photo, dark "Sold out" badge, struck price).
- Project panel: a **Components** group (Product card · 3 variants, Button · 4 variants, Section heading · 2 variants). Layers: the three cards as Product card uses with their variant.
- Properties › **Component**: header "Product card · Component · used 9 times · this one: Linen plate set"; Variant Default / **Sold out** / Featured; "Chosen by the data: in stock is off → Sold out · Edit rule" (a variant can follow a collection field); **Options** Badge (from variant), Size Regular / Compact, Show price; **Content · from Products** Image photo, Name name, Price price. Actions: **Edit component** · No changes here (or "Changes here · n" with reset) · Detach.
- Status: "Double-click to edit this use · Edit component changes all 9".
- **Inset · the component's own tab**: its variants side by side on the page colour (Default 4 uses, Sold out 1, Featured 4, with the selected one outlined) and its options (Variant, Badge text, Size, Show price); + Variant · + Option; "Variants only differ where they need to."

**D-56b Interactive parts · states** (v0.2, sheet `D56b-Interactive-States.dc.html`, row 04).
1. **Picking the target**: Target "Pick on the canvas…" (focused); the crosshair highlights what will be chosen, including parts hidden until opened ("Mobile menu · nav · hidden until opened"); Esc cancels; Layers works too.
2. **Editing the Open view**: a chip "⚡ Editing: Open view · changes apply only while open"; edited parts get an accent dot in Layers; Esc or the chip's × returns to Closed.
3. **Tabs**: tabs listed in Properties (reorder, rename, "shown first"), + Tab, Opens on Click, arrow keys move between tabs, optional remember last tab; built as tablist / tab / tabpanel.
4. **Accordion**: native `details` items; Only one open at a time; First item open; Expand 160 ms; works without script.
5. **When it cannot run**: hidden at this screen size (amber note, expected for a phone menu); target deleted (red note "Target missing · Pick another or remove the interaction", listed in the page check).
6. **In Preview**: Enter opens the menu, focus moves to the first link, Tab stays inside, Esc closes and returns focus, the page behind does not scroll.

**D-57b Collections · states** (v0.2, sheet `D57b-Collections-States.dc.html`, row 09).
1. **Empty collection**: "Products has no items yet" with the fields listed, Import CSV… · + Product; linked cards show one sample card while designing.
2. **Importing a CSV**: each column → a field with its detected kind (name text, price number €, photo image, glaze text, season choice, in stock yes / no) and a sample; problems are listed (2 image files not found; row 9 price not a number, imported empty); Import 13 items.
3. **Filter and sort**: "Which products · 4 of 12 match": conditions (season is Winter · and · in stock is yes), + Condition, Sort price Low to high; opened from Repeat › Only.
4. **Editing an item on the canvas**: double-clicking text in a repeated card edits that item's data; chip "Editing data: Products › Ember mug · name"; styling still goes through Properties.
5. **A deleted field**: the linked part keeps its place with a hatched placeholder "{glaze} · field deleted" on every card; Link to another field · Use plain text · Remove label.
6. **Item page template**: the Product page tab `shop/{slug}.html` with a switcher "‹ Showing Tide bowl · 1 of 12 ›" to check each item.

**D-58b Components · states** (v0.2, sheet `D58b-Components-States.dc.html`, row 09).
1. **Making a component** (right-click › Make component, `Ctrl Alt M`; Make shared is `Ctrl Alt K`): name, which parts become options (image, name text, price text; not the corner radius), "Card 2 and Card 3 look the same · they will use it too".
2. **Changes on one use**: tag "Product card · 2 changes here"; the changes listed with Reset; **Make this a variant…** (e.g. "On sale") · Reset all.
3. **Editing a variant** (component tab): Sold out selected among Default · Sold out · Featured; Properties lists where it differs from Default (badge shown, photo greyed 55 %, price struck through); everything else follows Default.
4. **Swapping**: replace with another component (Product row keeps image, name, price; Journal card keeps image, name); what does not fit is listed first; Swap this one · Swap all 9.
5. **Deleting or detaching**: "Delete Product card? It is used 9 times": Keep the uses as plain copies (default) or Replace them with another component; Detach one use works the same for a single card; Undo brings it back.

### Phase I — AI tools and MCP

Daisy is an **MCP server**: it lets AI apps on the same computer read and edit the open project through the same model the user edits (elements, properties, design-system tokens, components), never by rewriting files behind the editor. Setup is personal (Preferences), not part of the project.

**Deferred (later):** Daisy as an MCP client (using other MCP servers for Assets and Collections) and backend-as-a-service integration (Supabase, Firebase). Nothing in v0.2 depends on them.

Rules:
- Off until the user turns it on. Local only: stdio, or HTTP on `127.0.0.1`.
- Each app has an access level: **Read only**, **Ask before changes** (default), **Change freely**; and a reach: the open project (default) or all recent projects.
- Every change an app makes is one named step in Undo and History ("Claude Code · 3 changes"). Changes are applied whole or not at all.
- An app's activity is shown in accent blue (it is an active state, not a mode; violet stays for states, amber for screen sizes).
- A Read only app that tries to change something is refused, and the user is told once.

**D-59 AI tools and MCP** (v0.2, `D59-MCP.dc.html`, row 15). Preferences gains a tab **AI tools and MCP**, between Files and saving and Privacy and updates; the same tab is added to D-49. Section **Let AI apps work in Daisy**: Daisy MCP server switch with status ("Running · 1 app connected"); Connect by (Local app (stdio) · Address (HTTP)) with the copyable address `http://127.0.0.1:7341/mcp`, "Only this computer can reach it"; Quick setup buttons that copy the settings for Claude Code, Cursor, VS Code or as JSON; New apps may (Read only · **Ask before changes** · Change freely); Apps can see (The open project · All recent projects). Connected apps listed with status, their own access level and Disconnect / Remove.

**D-59b An AI app working in Daisy** (v0.2, `D59b-MCP-Live.dc.html`, row 15). Top bar, before the save status: an accent chip "Claude Code is working · Pause · Stop". On the canvas, the element an app proposes to change gets a dashed accent outline with the tag "Claude Code · proposed change" and a small Was / Now card. The request opens as an anchored popover (328 wide at left 1282, with Pin and Close): the app's own words, the list of changes (each can be unticked; the first is shown on the canvas), "Allow changes without asking until I close Daisy", **Allow 3 changes** / Deny, and the note that allowed changes become one undo step. Status bar: "Claude Code is connected through MCP · it can read this project and asks before changing it".

**D-59c MCP · states** (v0.2, sheet `D59c-MCP-States.dc.html`, row 15).
1. **An app asks to connect** (first time only): access level and reach chosen here; Don't allow / Allow.
2. **A read-only app tries to change something**: "Cursor tried to change “Hero heading”"; nothing changed; Keep read only / Allow it to ask.
3. **An app stops mid-task**: each change is listed as done or not started; Undo the 2 changes / Keep.
4. **History shows app steps**: named and grouped, undoable; reads are listed too ("Cursor · read only · read Home and Shop").

## 12. Interaction and State Specifications for Important Tools

Each table is the state machine the designs must illustrate. "Overlay" is what is drawn. "Panels" is what changes in the chrome.

### 12.1 Select tool

| State | Enter | Overlay | Panels | Exit |
|---|---|---|---|---|
| Idle | Default | Selection (if any) | Options show selection values | — |
| Hover | Pointer over a selectable element | Hover outline + name tag | Status hint "Click to select · Double-click to go inside" | Pointer leaves |
| Pressed | Pointer down on an element | Selection moves to it | Properties updates | Move 3 px (drag) or up (click) |
| Drag flow | Drag an in-flow element | Ghost, dimmed original, insertion line, target outline | Status "Release to move" | Up = move (one undo step); `Esc` = cancel |
| Drag free | Drag a Free element | Moves the element, guides, pin lines | X/Y update live | Up / `Esc` |
| Resize | Drag a handle | Live size, size label, guides, size-match ticks | W/H update live | Up / `Esc` restores |
| Radius | Drag a radius handle | Corner arcs, radius readout `12` | Border → Roundness updates | Up / `Esc` |
| Marquee | Drag from empty space of a container | Marquee rect, hover outlines on hits | — | Up selects the hits |
| Alt-distance | Hold `Alt`, hover another element | Red distance lines | — | Release `Alt` |
| Formula-locked | Drag an element whose offset uses a formula | Lock cursor, no movement | Notice "Position uses a formula… · Replace" | Up |

### 12.2 Text tool and text editing

| State | Enter | Overlay / visuals | Panels |
|---|---|---|---|
| Armed | Press `T` | Crosshair+T cursor. Hovering a container shows the insertion line; hovering text shows the I-beam | Options show text defaults |
| Created | Click | New `p` with a blinking caret, solid thin outline | Options switch to text editing |
| Editing | Typing | Native caret/selection | History groups one typing burst |
| Range selected | Select text | Native selection | B/I/U/link reflect the range; Typography edits the range |
| Linking | `Ctrl+K` or 🔗 | Link popover anchored to the range | — |
| Finished | `Esc` / click outside | Normal selection outline + handles | Tool returns to Select |

`Enter` makes a new paragraph after the current one. `Shift+Enter` inserts a line break. Pasted text is plain by default.

### 12.3 Box and other creation tools

| State | Visuals |
|---|---|
| Armed | Crosshair with a tool glyph. Hovering shows the target container outline and the insertion line |
| Drawing | Rubber band (1 px blue, 8% fill), size label, insertion line stays visible |
| Drawing + `Alt` | The insertion line disappears. The rubber band shows a ◇ "Free" tag. Guides appear |
| Drawing + `Shift` | Constrained square/circle, label shows "160 × 160 ⛓" |
| Created | New element selected, name tag shows briefly in a highlighted colour (600 ms), tool returns to Select |
| Invalid parent | Insertion falls before/after a non-container, never inside it |

### 12.4 Layout tool

| State | Visuals |
|---|---|
| Hover container | Outline + the arrangement badge ("Grid 3 × 1", "Row →", "Stack") |
| Container selected · Stack | Children outlined thinly, gap bars hidden, hint "Choose Row or Grid to control alignment and spacing" |
| · Row | Hatched gap bars, direction arrow at the start (click flips), grow toggles (12 px) on children, alignment grid in options |
| · Grid | Teal track lines, track badges, `+` add-track buttons, gap bars, cell highlight on hover |
| Drag gap bar | Bar highlights, value pill, all gaps update together |
| Drag track line | Both adjacent badges update live, keeping their units (`1fr` → `1.2fr`) |
| Drag child to a cell | Target cell fills with 15% teal, ghost child |
| Drag child edge across cells | Span highlight, badge "span 2" |
| Alignment on a Stack | Daisy switches it to Column; status notice "Changed to Column so children can be aligned · Undo" |
| Track uses unsupported syntax | Tracks drawn dashed and read-only, badge "edit in Properties" |

### 12.5 Spacing tool

| State | Visuals |
|---|---|
| Hover element | Green inside bands and orange outside bands with values. Zero-size bands show a 4 px grab strip on hover |
| Drag band edge | Band grows/shrinks, value pill, opposite side unchanged |
| `Alt+drag` | Opposite side mirrored (both bands highlighted) |
| `Shift+drag` | All four sides (all bands highlighted) |
| Between siblings in Row/Grid | Hatched gap bars, which edit the parent's gap |
| Double-click a band | Inline numeric field in the band |
| Collapsed margins | The smaller band is tagged "merged with neighbour" |

### 12.6 Responsive editing flow

| Step | What the user sees |
|---|---|
| Switch to Tablet | The canvas animates to 768 wide (160 ms). The page label reads "Tablet · 768". The amber chip "Editing: Tablet and smaller" appears in the options bar |
| Edit a value | The field's marker turns solid. The Layers row gains 🖥. The context strip counts "1 value set here" |
| Look at an inherited value | A hollow amber dot with the tooltip "From Desktop: 64px" |
| Structural edit at Tablet | First time per session: notice "Adding, removing and reordering applies to all screen sizes." |
| Right-click label | Reset (back to inherited) · Set for all sizes (promote) · Copy CSS |
| Back to Desktop | The chip disappears. Values show the base |

### 12.7 State editing flow

| Step | What the user sees |
|---|---|
| Choose Mouse over | The State selector shows "⌖ Mouse over" (pressed, accent ring). The chip "Editing: Mouse over" appears. The canvas shows the element in that state, and the name tag gets a ⌖ |
| Edit | Only differences are stored. Normal values are muted until overridden |
| Select another element | The state resets to Normal automatically |

---

## 13. Review Process and Approval Gate

### 13.1 How the owner reviews

1. Each phase (A–G) is delivered as a set of Claude Design screens with their IDs.
2. The owner comments per screen ID: "D-14: gap bars too strong" or "D-04: right dock too narrow".
3. Claude updates **this document first** (spec text, tokens or component), adds a change log entry, and then the screen is revised in Claude Design.
4. A phase is accepted when all its screens are marked ✓ in 13.4. The next phase begins only after that.

### 13.2 Change log

| Version | Date | Screen / section | Change | Requested by |
|---|---|---|---|---|
| 0.1 | 2026-11-11 | All | First draft of the design specification | — |
| 0.2 | 2026-11-12 | 5.1, 5.2, 5.3, 6.1, C-05, C-37 | Properties panel decluttered: two-line header replaces General; only used groups open; paired fields with inside labels; borderless fields at rest; Advanced as a header icon; empty groups in a "More properties" list with + on hover | Owner (D-04 review: "cluttered") |
| 0.2 | 2026-11-12 | 2.2, 2.3, 9.1, 9.5, C-35, C-36 | Top bar and options bar redesigned: daisy brand mark, centred VS Code-style search replacing document name and save status, split Export; tool chip with key badge, selection label, capsules; softer radii (3 / 4 / 6 px) | Owner (D-04 review: "not giving any feeling") |
| 0.2 | 2026-11-12 | 1.4, 1.6, 2.1, 2.7, 3.1, 3.2, C-34 | Project model: projects with many pages and one design system, or single-file editing; Photoshop-style page tabs; Code::Blocks-style Project panel; screen size, zoom and page settings moved from the top bar to the page tab row | Owner |
| 0.2 | 2026-11-12 | 7.1, 9.1, 9.2 | Review fixes: fold label moved inside the page; `text-muted` #757575 → #939393 (dark) and #767676 → #6b6b6b (light) to pass 4.5:1; new `accent-fill` #246bcb for white text on blue; consistent Fixed/Fit tags; real gear icon | Claude review, approved by owner |
| 0.2 | 2026-11-12 | 4.3, 5.3, C-33, D-35 | Corner roundness control: all corners, two pairs, each corner, elliptical corners, corner shape, fluid values, design-system tokens; shared by the options bar and Properties → Border | Owner |
| 0.2 | 2026-11-12 | D-00, 9.1, 9.8, 9.9 | D-00 design system sheet built as five artboards; added `accent-fill-hover` / `accent-fill-pressed` and name-tag fills so all white text passes 4.5:1; focus states shown for every interactive component | Claude, D-00 build |
| 0.2 | 2026-11-12 | 5.3, C-38, D-37 | Layout Advanced made visual for flex and grid (direction, axes, wrap, lines, gaps, track chips with editor and presets, fill order, named areas) and the In Row / In Grid child groups. A separate display control was considered and dropped: Stack / Row / Grid plus `display ▾` already cover it | Owner |
| 0.2 | 2026-11-12 | D-01 | Home first run redesigned for projects: New project (Alt+N) and Open file… (Ctrl+O), with one line explaining single-file editing and drag-and-drop | Claude, D-01 build |
| 0.2 | 2026-11-12 | D-02, 1.4 | Home with projects: project cards with page counts, a Recent files list for single pages with Add to project, search; New document dialog became New project with an optional design system copied from another project | Claude, D-02 build |
| 0.2 | 2026-11-12 | D-03 | Fresh-project editor derived from the v0.2 shell: single Home tab, Untitled project tree, empty design system in Swatches, Layout Stack with first-use hint, name tag inside the top edge of a full-width section | Claude, D-03 build |
| 0.2 | 2026-11-12 | 3.3, D-38 | Menus designed: File, Edit, Element, View, Help with one submenu each (Open recent, Copy as, Placement, Screen size); contents updated for projects, versions, design system, Code, Timeline, Preview and Outline; menu bar behaviour and keyboard access | Owner ("what will happen when user will click file, edit, view, help?") |
| 0.2 | 2026-11-12 | 9.4, 13 | Status table brought up to date (F and G were still "Not started"; D-02b, D-36b, D-38 added); dialog widths in 9.4 corrected | Claude, project audit |
| 0.2 | 2026-11-12 | D-39 | Colour picker popover: Solid/Linear/Radial/Image, design-system tokens first, page colours not yet tokens with Save as token, SV area + hue + opacity + eyedropper, HEX/RGB/HSL/OKLCH, token link with Unlink and edit-the-token, contrast check, CSS line | Owner ("okay go ahead") |
| 0.2 | 2026-11-12 | D-40, C-35 | Search results: scope tabs with prefixes, grouped results across pages, layers on other pages, assets and commands, match highlighting, preview pane with actions, keyboard footer; command mode inset | Owner ("yes go ahead") |
| 0.2 | 2026-11-12 | D-41, 4.3 | Button tool: new Secondary button placed in a row with the label typed in place; options bar only says how it places and whether it is a link or an action; Properties Button group with design-system style presets, Goes to, Section, New tab. Link tool on a whole card with page/section search and the nothing-clickable-inside check | Owner ("okay go ahead") |
| 0.2 | 2026-11-12 | D-42 | Form tool: variants flyout, insertion of a labelled Phone field into a form, behaviour-only options bar, Next field properties (field, data, look), form send settings and design-system field states | Owner ("go ahead") |
| 0.2 | 2026-11-12 | D-43 | Section tool: drag a new section open between two, Kind menu with meanings, contained/full width from the grid, Next section properties with link id and background tokens; Direct Select inset compared with Select | Owner ("go ahead.") |
| 0.2 | 2026-11-12 | D-44 | Project settings panel (General, Fonts, Screen sizes, Redirects, Site-wide code, Export defaults); Fonts tab with weights in use, sizes, per-page budget, self-hosting, swap, subsets and a matched fallback to avoid layout shift | Owner ("go ahead") |
| 0.2 | 2026-11-12 | D-45 | Import an HTML page: preview and inventory, Keep / Tidy (recommended) / Rebuild with Daisy layouts, colour matching to tokens with ΔE, images, fonts and text-style mapping, notes on positioned elements, Bootstrap, scripts and missing descriptions | Owner ("go ahead") |
| 0.2 | 2026-11-12 | D-46 | Saving and file problems: save status in the top bar (Saved, Saving, not saved, Couldn't save), save-failure banner, offline, changed outside Daisy with diff and Keep mine / Use theirs, missing file, crash recovery, missing image, folder permission | Owner ("yes please") |
| 0.2 | 2026-11-12 | D-47 | Fill, Border and Effects groups open: fill and effect layer lists with reorder, visibility and remove; border sides diagram, token colour, corners linked to radius-md, outline; Effects Advanced popover with shadow tokens and linked values | Owner ("okay go ahead.") |
| 0.2 | 2026-11-12 | 7.5, D-48 | Right-click menus for element, empty workspace, Layers row, page tab, Project page and swatch; header line, Select layer submenu, keyboard access and flip rules | Owner ("go ahead.") |
| 0.2 | 2026-11-12 | D-49, D-50, D-51 | Preferences (Canvas and editing shown: click behaviour, hover outlines, nudge, snapping, units, zoom); Keyboard shortcuts (columns by area, key sets, edit in place with conflict check); Find and replace across pages with scope, kinds, whole word / regex and grouped results | Owner ("go ahead") |
| 0.2 | 2026-11-12 | D-36c | Design system editor states: edit a text style with fluid size and override note, add a colour inline, delete a used token by replacing it, collect values from pages (map or new token), rename with an alias for outside CSS | Owner ("go ahead") |
| 0.2 | 2026-11-12 | D-52 | Home and Help small screens: project card menu, Recently deleted, open and drop, first-use tip rules, Getting started checklist, About and What's new | Owner ("go ahead.") |
| 0.2 | 2026-11-12 | D-35, C-33 | Corner roundness rebuilt in the shared popover pattern: tokens first, Advanced as its own anchored popover (shape, elliptical, grow with the screen), canvas handles snapping to tokens, both triggers open one popover | Owner ("yes please") |
| 0.2 | 2026-11-12 | D-53, 1.4 | Shared parts: one header/footer used on many pages; diamond accent cue, Shared parts group in Project, edit for all pages or this page only, per-page changes with reset/apply, open in its own tab, detach; Make shared with page-by-page matching | Owner ("go ahead", second audit) |
| 0.2 | 2026-11-12 | D-54 | Page dialogs: New page with shared parts and nav entry, Rename with link updates and redirect, Delete with what broken links become, Duplicate keeping shared parts | Owner ("go ahead") |
| 0.2 | 2026-11-12 | D-04 and derived screens, D-55 | Save status added to the top bar of D-04 and all 43 screens built from it (light version on D-33); Export progress, done with non-blocking report, stopped with ways out, background progress and toast; History panel with undone steps, current marker, version pins | Owner ("go ahead") |
| 0.2 | 2026-11-12 | D-44b | Project settings tabs: General, Screen sizes (with CSS direction), Redirects (origin and flags), Site-wide code, Export defaults | Owner ("go ahead") |
| 0.2 | 2026-11-12 | 9.2, D-33b–d | Light theme check of popovers, menus and dialogs: white floating surfaces with light border and softer shadow, lighter scrims, light versions of link, warning, danger and code colours | Owner ("yes plz") |
| 0.2 | 2026-11-12 | 11 (Canvas map) | Screens page reorganised into 13 rows with section title boards; state sheets follow their screens; positions now listed in the canvas map | Owner ("need proper reordering") |
| 0.2 | 2026-11-12 | D-56 | Interactive parts: interaction model (when, do, target, start, motion, accessibility rules), Closed/Open shown side by side on the canvas, mobile menu as the example, ready-made Menu, Tabs, Accordion, Pop-up, Slider, Show and hide | Owner ("go for one by one (1-3)") |
| 0.2 | 2026-11-12 | D-57, D-58, canvas map | Collections (repeat a designed card from Products, filters and sorting, field mapping, item pages, collection table tab); Components with variants and options (variant chosen by data, edit component tab, detach); new canvas row 09 "Reusable content" (14 rows) | Owner ("complete them both 2,3 one by one") |
| 0.2 | 2026-11-12 | D-56b, D-57b, D-58b | States for interactive parts (target picking, open view, tabs, accordion, cannot run, preview), collections (empty, CSV import, filter, edit data on canvas, deleted field, item page), components (make, local changes, variant editing, swap, delete/detach); Make component shortcut Ctrl Alt M | Owner ("add states for these 3 new features") |
| 0.2 | 2026-11-13 | D-59, D-59b, D-59c, D-49, 6.4, canvas map | MCP support: Daisy as an MCP server for AI apps (access levels, local only, changes as one undo step, approvals) and as an MCP client for Assets and Collections; Preferences tab "AI tools and MCP"; live AI editing screen; states sheet; canvas row 15 | Owner ("add mcp support, mcp connection its ui") |
| 0.2 | 2026-11-13 | D-59, D-59c, Phase I | Scope cut: Daisy as an MCP client (servers for Assets and Collections) and backend-as-a-service integration deferred; D-59 keeps only "Let AI apps work in Daisy"; D-59c now: connect request, read-only refusal, stop mid-task, History | Owner ("dropped the baas feature … think about that later") |
| 0.2 | 2026-11-12 | 2.3, C-36, D-03, D-04, D-00d | Options bar no longer repeats the active tool (tool chip removed, C-36 retired) or the selection label; it starts at 52 px aligned with the left dock and regains the Distribute capsule | Owner ("duplicated below the top bar") |
| 0.2 | 2026-11-12 | 1.4, 2.3, 2.7, D-03, D-04 | Screen size switcher and Page settings moved from the page tab row to the right of the options bar for visibility; zoom stays in the tab row | Owner |
| 0.2 | 2026-11-12 | 1.4, 2.5, 2.7, D-03, D-04 | Zoom moved from the page tab row to an editable field at the left of the status bar, like Photoshop | Owner |
| 0.2 | 2026-11-12 | 2.5 | Zoom field moved to the right of the status bar, placed just before the page size and pointer position | Owner |
| 0.2 | 2026-11-12 | D-05, 8.2 | Hover vs selection vs scope designed; scope gets a visible tag ("Inside Hero grid · Esc to go up") and an accent-tinted breadcrumb segment, and canvas hover mirrors in Layers | Claude, D-05 build |
| 0.2 | 2026-11-12 | D-06, 7.3 | Resize in progress designed: live reflow, ghost of the original size, live-highlighted W/H in options bar and Properties; size-match target changed to equal grid columns (= 624) because the card width (416) could not match | Claude, D-06 build |
| 0.2 | 2026-11-12 | D-07, 5.4, 7.3 | Resize limited by layout designed: box stops at the column edge, requested width shown as a hatched extension with "wants 760", neutral limited size label, limited cursor, "Use 654" action on the real-size note; numbers corrected to the 654 column | Claude, D-07 build |
| 0.2 | 2026-11-12 | D-08, 7.3 | Flow drag designed: insertion line placed above the paragraph to match the described move; ghost on a solid card so it stays legible over text; drop target mirrored in Layers | Claude, D-08 build |
| 0.2 | 2026-11-12 | D-09, D-10, D-11 | Phase D completed: invalid drop (red tag, line, pill, Layers mirror, red status line); Free badge with pin lines, alignment guide to Hero text top (v0.1's image-top alignment was impossible with a 24 px pin), pin widget in options bar, anchor notice; multi-selection with Mixed fill, enabled Distribute, full context menu with Placement submenu | Claude, Phase D build |
| 0.2 | 2026-11-12 | D-12 – D-19 | Phase E designed (text editing bar with a mode chip and Done; Box drawing with live reflow and the variants flyout; Layout and Spacing tool visuals; Transform with Gradient inset; Media describe prompt with Link popover inset; Elements panel with Place tool; Measure with Eyedropper inset). Numbers corrected where v0.1's were impossible (measure 78/62). Green value pill darkened to `#237a33` for 4.5:1 | Claude, Phase E build |
| 0.2 | 2026-11-12 | D-12, 4.3 | Text editing redesigned: floating inline toolbar on the selection; full text editing bar (style with modified dot, font, weight, size stepper, line and letter spacing, colour, highlight, B I U S, super/subscript, inline code, link, clear, align, lists, quote, case); Properties with a Selected words / Whole paragraph scope switch, text style row with Update style, and deep Advanced typography (variable axes, case, decoration, wrap, truncate, numbers, ligatures, small caps, fluid size) | Owner ("very basic") |
| 0.2 | 2026-11-12 | D-12, 4.3 | Text editing deduplicated, one control in one place: floating toolbar = inline marks (B I U S, code, link, highlight, ⋯); options bar = paragraph structure (align, lists, quote, indent, Done); Properties = kind, text style with Update style, and typography values. Removed from the options bar: kind, style, font, weight, size, spacing, colour, marks, case. Removed from the floating toolbar: style and colour. Removed from Properties: align and highlight. Decoration in Advanced became Line style | Owner ("repeated some options in multiple places") |
| 0.2 | 2026-11-12 | D-13 | Box tool improved, one control in one place: variants only in the flyout (added Section band, Spacer, with descriptions); options bar = drawing behaviour (In flow/Free, Width Fixed/Fill, Height Fixed/Hug, Wrap what I draw over, Keep tool); Properties = "Next box" with design-system presets (Plain, Card, Outline, Tinted, Pill, Ink), match-an-element, Look, Inside, Element, Save as preset. Rubber band previews the preset; column snap slots, smart guides `#c2255c` and matched spacing; Layers ghost row; Wrap inset | Owner ("needs to improve") |
| 0.2 | 2026-11-12 | D-14, 5.1, C-38 | Layout tool reworked: the Layout Advanced popover (C-38 Grid) opens from Properties › Layout's Advanced button and stays in sync with canvas drags (track chips + editor, presets, rows, split gaps, fill order, items in cells, named areas, preview, CSS). Options bar now tool behaviour only (Show Tracks/Gaps/Space inside/Track sizes, Drag steps, Alt+drag all gaps, Make columns equal); Arrange/Columns/Rows/Gap no longer repeated there. Track chips moved from Properties to the popover. New popover rule for full-editor Advanced (Layout, Corners). Row inset moved bottom left | Owner ("include our designed properties popup") |
| 0.2 | 2026-11-12 | D-15, 5.3, 12.5 | Spacing tool reworked: Spacing Advanced popover from Properties › Spacing (per-side value + unit + token chip, Each/Pairs/All, margin, clamp() fluid spacing, logical sides, scroll-margin-top offset, CSS); options bar now behaviour only (Show Inside/Outside/Between, A drag changes One/Opposite/All, Snap to Halden spacing, Allow negative); snap ladder of design-system tokens on the drag pill; Between inset with per-gap values. Halden sample spacing tokens defined | Owner ("Yes", continuing the dedupe) |
| 0.2 | 2026-11-12 | D-16, 5.3 | Transform tool reworked: Transform Advanced popover from Properties › Transform (origin 9-point + X/Y, scale X/Y, skew, 3D, reorderable transform list, separate properties, CSS); options bar now behaviour and actions (Corners drag to Rotate/Scale/Skew/Move, Angle snap 15°, Show dial, Origin draggable, Flip, Reset all); rotation dial with 15° ticks behind the element; origin dot no longer covers the label; badge moved to the image's top left so the popover does not hide it; Origin removed from simple Transform | Owner ("Yes", continuing the dedupe) |
| 0.2 | 2026-11-12 | D-16, 5.3 Fill | Gradient inset reworked: Gradient tool options bar is behaviour only (click adds a stop, snap stops to 25%, show stop labels, edit every fill layer); new Gradient editor popover (type, angle, stop strip, stop rows with token names and positions, oklch Smooth blend, Repeat, Reverse, ⋯, CSS line); third stop added at 50% with labels on canvas | Owner ("improve d16 first") |
| 0.2 | 2026-11-12 | D-18, 4.4 | Elements and Place tool reworked: element card popover beside the panel (live preview, description, Starts as Plain/Links/Inline row, fit check for the target, structure, Save to Custom, Pin); ghost preview on canvas at the insertion point; options bar now behaviour only (In flow/Free, After placing Select it/Stay armed, Show preview, Only valid spots); armed chip and Tag removed from the bar; code block moved out of Properties | Owner ("Yes", continuing the dedupe) |
| 0.2 | 2026-11-12 | D-18, 6.1 Place | Place Advanced popover added (Tag ul/ol/menu, Where it goes Before/Inside start/Inside end/After, Wrap the selection, Place into every match, Accessible name, id, class, + Attribute, Style From design system/Bare HTML, Save as preset); tool-options table row for Place updated to the new behaviour bar and Advanced; element card Save button removed (one save, in Advanced) | Owner ("What is the advance tools for d18?" → "Yes") |
| 0.2 | 2026-11-12 | D-19, 6.1 Measure | Measure tool reworked: Measure Advanced popover (pins with visibility, across screen sizes, Why 78 with Make it 64 / Snap to 72 fixes, Copy as Value/CSS/Spec note/Image with redlines); options bar now behaviour only (Units, From, All four sides, To parent edges, Keep pins); live readout and Copy value removed from the bar; Properties › Measure trimmed to the live values; Eyedropper inset moved bottom left; tool-options row for Measure updated | Owner ("Ok", continuing the dedupe) |
| 0.2 | 2026-11-12 | D-20, 5.1, 6.x Level 3 | D-20 reworked for the popover pattern: every group's Advanced now opens as a 328 px popover (rule extended from Layout and Corners to all groups). Size Advanced popover with width and height limits, a clamp() custom value editor (Min · Ideal · Max, resolved per screen size, Edit as text, Back to a fixed value), aspect ratio, overflow and box-sizing; Properties keeps simple values with amber `custom tracks` / `limits` tags instead of repeating values; Other properties group (isolation: isolate); label tooltip "Space between · gap · 64px"; max-width corrected to clamp(320px, 92vw, 1312px) to match the 1312 grid | Owner (popover rule), Claude D-20 build |
| 0.2 | 2026-11-12 | D-12 | Typography Advanced moved from inline into a popover to follow the every-Advanced-is-a-popover rule (Optical size, Case, Line style, Wrap, Truncate, Numbers, Ligatures, Small caps, Fluid size, + Text shadow, + Other property, CSS line); Weight axis removed as a duplicate of Weight; panel scrollbar removed | Owner ("Fix d12 issue first") |
| 0.2 | 2026-11-12 | D-21, 12.7 | D-21 designed: States popover from the header State button (Normal, Mouse over, Pressed, Focused, Disabled with selectors and change counts, focus-style warning, more states, hold state, all side by side, apply to every matching button, CSS); Fill override with Normal value, Reset and Save as swatch; muted Normal values; Transition suggestion; all-states inset; subject moved to Shop the collection so the popover does not cover it | Owner ("Move on") |
| 0.2 | 2026-11-12 | 9.x tokens, D-07, D-14, D-16, D-37, D-00a, D-00e | Violet now means states only. Layout and transform visuals moved to teal: `ov-track` #1a9284 (was #a371f7), badge fill #127a70, subtle rgba(26,146,132,0.14), text on dark #9fe5dc; track chips in the Layout Advanced popover, column edge, track badges, transform origin and dial, Layout tool toggles. State colours unchanged | Owner ("Why used violet colours?" → option 1) |
| 0.2 | 2026-11-12 | 5.1 header, 9.x `state`, D-21, 12.7 | Violet limited to mode cues (options-bar chip, canvas name tag, Layers ⌖ badge, ⌖ icon). Properties and popovers use the normal accent: State button pressed with accent ring, override dot and ring, Transition suggestion and Add, selected state row, change counts, inset ring | Owner ("should be accent colour rather than make the app rainbow") |
| 0.2 | 2026-11-12 | D-22, 9.x `resp` | D-22 designed: Tablet at 100% (one-column hero, 2-column cards), amber chip and icons as mode cues only, neutral context strip with Show only these, accent dots for values set here and hollow grey dots for inherited ones, Font size popover comparing Desktop/Tablet/Mobile with Reset, Use everywhere and a fluid clamp() option; replaces the v0.1 tooltip | Owner ("go for next") |
| 0.2 | 2026-11-12 | D-23 | D-23 designed: Mobile 390 at 100%, hidden Nav links as a dashed placeholder while selected, dimmed Layers row with eye-off, Visibility with large device toggles and a missing-menu suggestion (Add a menu button), Screen sizes dialog (icon, name, applies up to, canvas, presets, Mobile-first explained, impact count, Save) | Owner ("Next") |
| 0.2 | 2026-11-12 | D-24 – D-26 | Phase G started: Layers drag into Hero text with drop-inside highlight, insertion line, ghost and Properties move note, Layers menu as an inset with described options; Outline view with landmark and heading badges, live Page check, canvas outline badges, Accessibility group as a read-out (description stays in Image); Assets panel with usage chips, no-description badge, upload zone, replace highlight on drop and an On drop before/after preview that carries the saved description | Owner ("Go ahead") |
| 0.2 | 2026-11-12 | D-27, D-28 | Code drawer at 330 with Element/Page/Design system CSS, read-only HTML and CSS panes with Copy, CSS lines that jump to their field, editable Custom CSS with a move-to-group hint, muted 3-colour syntax (purple dropped); Properties Custom CSS row now points to the drawer. Timeline with transport, trigger, ruler, playhead, clip, keyframe rows, keyframe inspector with feel and curve, canvas frame at the playhead, Animation summary with reduced-motion switch | Owner ("Next") |
| 0.2 | 2026-11-12 | D-27 | Code drawer rebuilt as a pro workspace: 420 h with Maximise, Read-only / Edit two-way, Find; Explorer (Element/Page/Project, files with changed and locked states, rules for the element with + Rule); split HTML/CSS editors with file tabs, breadcrumbs, folding, gutter markers (changed, Tablet, problem), wrap/split/copy; Custom CSS as its own tab; Cascade/Computed/Box inspector with sources and struck-through overrides; status strip with problems, cursor, encoding and Copy as | Owner ("massive tool… more advanced, clean, organized") |
| 0.2 | 2026-11-12 | D-27b | Code workspace states sheet: edit two-way with token autocomplete and live sync, invalid code with fix suggestion and last-good-value, find and replace with scope and counts, Computed and Box tabs, Page scope with document outline, Copy as menu, empty state, two-way conflict, collapsed and maximised bars | Owner ("Design states for d27 first") |
| 0.2 | 2026-11-12 | D-28 | Timeline rebuilt as a motion tool: named sequences with one trigger, element clips with stagger, property tracks with keyframes and drawn easing, multi-select marquee, markers, work area, snap and zoom; full transport; curve editor with presets and Apply to selected; reduced-motion choice; Copy as CSS @keyframes; canvas shows the staggered frame at the playhead; Properties Animation reduced to a summary | Owner ("Yes go for next") |
| 0.2 | 2026-11-12 | D-28b, 9.x `rec` | Timeline states sheet: scroll-linked mode with progress ruler and page map, recording keyframes (new `rec` mode colour), Keyframe tab with Hold and Token values, stagger popover with order and spread, Sequence tab (trigger, threshold, plays, screen sizes, less motion), empty state with presets, keyframe menu, transform conflict with split fix, performance hint while playing, collapsed mini player and recording badge | Owner ("Yes") |
| 0.2 | 2026-11-12 | D-29 | Preview mode: chrome hidden, 44 h preview bar (Back to editing, page picker with working links, screen sizes, custom width, rotate, Less motion / Dark preference / Slow network simulation, Share link, Open in new tab), screen-size ruler showing which styles apply at the current width, page with drag handles on both edges, real hover state | Owner ("Go for next") |
| 0.2 | 2026-11-12 | D-30 | Export dialog at 1040: scope (this page / changed / all), file tree with notes, sizes and changed tags, code preview; destinations (Zip, Write to a folder with sync, Publish later) with folder path; grouped options with plain explanations (code, extras, images incl. srcset and quality, font subsetting); non-blocking pre-export checks with Fix; size before and after with load time; Export N files | Owner ("Yes go for next") |
| 0.2 | 2026-11-12 | D-31 | Page settings at 960 with side tabs (General, Social sharing with warning, Appearance, Search engines, Code in head) and a page switcher; General with counted title and description, use-first-paragraph, address with home tag, language, show-in-search toggle; live search-result and share-card previews; changes apply live with Done | Owner ("go ahead") |
| 0.2 | 2026-11-12 | D-31b | Page settings states sheet: social sharing set and empty (three ways to add an image), Appearance, Search engines with business details, Code in head with script safety note, too-long and empty validation with cut-off preview, another page address with auto-updated links and a taken-name error, hidden-from-search, page switcher with per-page gaps, single file without address or sitemap | Owner ("create states for D-31") |
| 0.2 | 2026-11-12 | D-31 | Page settings redesigned as a full-screen workspace: search across settings, page card and status, 11 sections in Page / Quality / Behaviour groups with statuses, health cards with one-click fixes, General (title, description, address, language, direction, status, menu) and Search engines cards, live preview of desktop and phone results, sitelinks and browser tab; adds Performance, Accessibility, Scripts, Redirects, Access and Advanced sections. D-31b marked for redo | Owner ("most important page… most advanced configurations") |
| 0.2 | 2026-11-12 | D-31 | Page settings trimmed back after review: 1100 panel, five sections (General, Search and social, Appearance, Code, Advanced), one Search/Share preview, ⚠ on sections only, no score cards; site-wide items moved to Project settings | Owner ("we over done things here") |
| 0.2 | 2026-11-12 | D-31, D-31b | Page title preview added (Tab tab and an In the browser tab strip under the search preview); D-31b redone for the lean sections with two new states: the title in the browser (one tab, many tabs, pinned, bookmark) and a Draft page | Owner ("states now for 31 · show the page title preview") |
| 0.2 | 2026-11-12 | D-32 | Versions dialog: list grouped by day with current, named and autosave versions and change summaries; side-by-side thumbnails with numbered change outlines and a Different from now list; Name the current version; Restore as a copy and Restore, with the current state saved first | Owner ("go for next") |
| 0.2 | 2026-11-12 | D-32b | Versions states sheet: this version, naming, confirm restore, after-restore toast with Undo, version menu, no named versions, page with no changes, older versions | Owner ("what about its states ?") |
| 0.2 | 2026-11-12 | D-33 | Light theme check on D-04. 9.2 updated: new titlebar, toolbar, capsule and line-subtle tokens; bg-control #f0f0f0 (white fields vanished); accent-subtle 0.12; ink versions of warning, success and danger; accent text uses accent-fill | Owner ("go for 33 now") |
| 0.2 | 2026-11-12 | D-34 | Compact frame 1440 × 900: docks keep widths; canvas opens at Fit 55% (70% does not fit 836); Distribute and Corner roundness move into More; Swatches/History 188 high below 1000 px so Properties fits | Owner ("yes") |
| 0.2 | 2026-11-12 | D-36 | Design system editor as its own tab: token list (colours, text styles, radius, spacing) with uses, live preview with uses outlined, token Properties with contrast checks and fix, Used on per page, Replace and delete; History replaces Swatches in this tab | Owner ("go for 36") |
| 0.2 | 2026-11-12 | D-02, D-03, D-36b | Design system is created with the project: New project dialog (680) with Set up now (brand, text, background colours, fonts, text size, corners, spacing, live preview) / Copy from a project / Skip for now; a skipped project opts in later from the Design system tab (same form, colours collected from pages); Project row shows Set up when skipped | Owner ("design system should be created at time of project creation… opt… modify it later") |
| 0.2 | 2026-11-12 | D-02, D-02b, D-36b | New project became a step-by-step setup (Visual Studio style): rail Project · Design system (Colours, Typography, Spacing & layout, Shape & depth) · Review, live token preview, Create with defaults. Pro design system steps: OKLCH 11-step scales and roles with dark theme, fluid modular type scale, spacing scale and screen-size grids, radius/border/shadow/motion, token naming and outputs (CSS, W3C JSON, Figma). Start choices Build new / Copy / Import / Skip; D-36b reduced to opting in later (start from what pages use) | Owner ("setup … should be like … visual studio … advance enough for professional users") |
| 0.2 | 2026-11-12 | D-03 | Fresh project redrawn as the result of the setup steps: Mossbank Tea, Design system tab opened behind Home, tree chips, page on the Background role, Swatches with the generated colours and fluid text styles, "created · 142 tokens" notice; Skip path noted (Set up button) | Owner ("please update D-03") |
| 0.2 | 2026-11-12 | D-17, 5.3 | Media tool reworked: Assets picker popover from Properties › Image › Source (search, tabs, thumbnail grid, details with saved description that fills alt, Upload, Use image); options bar now behaviour only (Ask for a description, Load when scrolled to, Optimise WebP, Max 2560 px, Keep tool); Kind, Source, Fit and describe field no longer repeated in the bar; Fit moved into Properties › Image; assets carry saved descriptions; Link inset moved left | Owner ("Yes", continuing the dedupe) |
| 0.2 | 2026-11-12 | 9.9, 14 | Token reference as CSS custom properties and a component style summary, so other tools and the Stage 2 code use the same styles; Claude Design brief updated | Owner |
| 0.2 | 2026-11-14 | D-52 (7) | **Proposed:** "Couldn't check for updates" states in About Daisy, a quiet notice for a failed automatic check, and a red notice for a failed download or install (Try again, Details). Awaiting owner approval and a Claude Design screen | Owner ("Show error in the app") |

### 13.3 Approval checklist (all must be ✓ before Stage 2)

- [ ] The design system sheet (D-00) is complete and every component state is present.
- [ ] The workspace layout, panel sizes and density are approved at 1920 × 1080 and still usable at 1440 × 900 (D-34).
- [ ] The tool strip, all 18 tool icons and the options bar for each tool are approved.
- [ ] Selection, hover, scope, resize, flow drag, free drag and invalid-drop states are approved.
- [ ] The Properties panel structure, the disclosure pattern and the origin markers are approved.
- [ ] The Layers, Elements and Assets panels are approved.
- [ ] Responsive editing (Desktop, Tablet, Mobile, Screen sizes dialog) is approved.
- [ ] State editing, Code drawer, Timeline, Preview and all five dialogs are approved.
- [ ] Dark and light themes are approved.
- [ ] All change requests are reflected in this document and the change log.
- [ ] The owner has written "Design approved v1.0" with a date in 13.4.

### 13.4 Screen status

| Phase | Screens | Status |
|---|---|---|
| A | D-00 (a Foundations · b Icons · c Controls · d Navigation, panels, overlays · e Canvas overlay) | In review (v0.2) |
| B | D-01 | In review (v0.2) |
| B | D-02, D-02b (setup steps) | In review (v0.2) |
| B | D-03 | In review (v0.2) |
| C | D-04 | In review (v0.2) |
| C+ | D-35 | In review (v0.2) |
| C+ | D-36, D-36b (opt in later), D-36c (states) | In review (v0.2) |
| C+ | D-37 | In review (v0.2) |
| D | D-05 | In review (v0.2) |
| D | D-06 | In review (v0.2) |
| D | D-07 | In review (v0.2) |
| D | D-08 | In review (v0.2) |
| D | D-09 – D-11 | In review (v0.2) |
| E | D-12 – D-19 | In review (v0.2) |
| F | D-20 – D-23 | In review (v0.2) |
| G | D-24 – D-34 (with D-27b, D-28b, D-31b, D-32b) | In review (v0.2) |
| H | D-38 Menus, D-39 Colour picker, D-40 Search results, D-41 Button and Link, D-42 Form, D-43 Section and Direct Select, D-44 Project settings (D-44b tabs), D-45 Import a page, D-46 Saving and file problems, D-47 Fill, Border and Effects, D-48 Right-click menus, D-49 Preferences, D-50 Keyboard shortcuts, D-51 Find and replace, D-52 Home and Help, D-53 Shared parts, D-54 Page dialogs, D-55 Export progress and History, D-56 Interactive parts, D-57 Collections, D-58 Components | In review (v0.2) |
| I | D-59 AI tools and MCP, D-59b An AI app working in Daisy, D-59c MCP states | In review (v0.2) |

**Approval:** _not yet approved_

---

## 14. Brief for Claude Design

Paste this at the start of each Claude Design session, followed by the screen section from chapter 11.

> You are designing **Daisy**, a professional desktop-browser application for visually designing real HTML/CSS web pages. It should feel like a precise creative tool (in the family of pro design and image-editing apps), not a website builder. Use the design system in Daisy's `UI_DESIGN_PLAN.md` chapter 9 exactly: tokens in 9.9 exactly: dark theme `#141414` top bar, `#1b1b1b` options bar, `#181818` / `#1f1f1f` chrome, `#2a2a2a` workspace, one blue accent `#2f80ed` used only for selection and active states (`#246bcb` behind white text), `text-muted` `#939393`, Inter 12 px UI text, 24 px controls in 28 px capsules, a 4 px grid, 2 px field radius with 3–6 px badges, buttons and capsules, borderless fields at rest, flat panels separated by 1 px lines, and no cards, shadows or gradients in the chrome. The top bar is app-level only (brand mark, menus, centred search, undo/redo, Preview, Export); pages open as Photoshop-style tabs over the canvas with screen size and zoom on the right of the tab row; the left dock starts with the Project panel; Properties opens only the groups in use and lists the rest under "More properties". The canvas shows a real-looking web page (the "Halden landing" ceramics page, chapter 10) at the stated zoom, with the editor overlay (selection outlines, handles, guides) drawn on top in the colours of 7.2. Build one screen at a time at 1920 × 1080. Keep every component consistent with the design system sheet (D-00). Use real labels from the vocabulary in 6.4, never lorem ipsum in the chrome. When a screen shows an interaction, show it frozen mid-gesture with the pointer visible.

Order of work: D-00 → D-03 → D-04, then await review. After that, one phase at a time.

Build the editor shell once (D-03/D-04) and derive each later screen from it, changing only what the screen requires. This keeps the whole set one coherent product.
