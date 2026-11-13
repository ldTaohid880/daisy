# AGENTS.md — how to work on Daisy

You are working on **Daisy**, an open-source (MIT) Electron desktop app for visually designing real
HTML/CSS websites. This file is for every agent (Claude Code, Codex, Cursor, …) and every person.

## 1. Sources of truth (read before you code)

1. **`PLAN.md`** — behaviour, data model, rendering, CSS/HTML generation, export, security, tests.
2. **`UI_DESIGN_PLAN.md`** — every screen (boards D-00…D-59), tokens (ch. 9), vocabulary (6.4).
3. **`docs/adr/`** — decisions that override PLAN.md (Electron, monorepo, project folders, MCP…).
4. **`docs/architecture/`** — package map, process model, project format, IPC, security.
5. The package's own **`AGENTS.md`** — what it owns, may import and must never do.
   If these disagree: ADR > PLAN/UI plan > this file > code. Never resolve a conflict silently — fix the
   document in the same PR.

## 2. Commands

```sh
pnpm install                 # once; Node 24, pnpm 10
pnpm dev                     # run the app
pnpm check                   # THE gate: format, lint, boundaries, types, unit tests
pnpm test:browser            # real-Chromium unit tests (css, renderer)
pnpm build && pnpm test:e2e  # Electron end-to-end
pnpm check:tasks --next      # the next task
pnpm --filter @daisy/<pkg> test   # one package
```

## 3. Architecture rules (enforced by `pnpm check:deps` and ESLint)

- The document lives in the renderer's docStore and changes **only** through model commands
  (`store.run`). Tools, panels, MCP requests — everything goes through commands. Every command has
  an inverse.
- Pure packages (`model`, `css`, `html`, `export`, `ipc`) never touch the DOM, Node, React or Electron.
- Renderer packages reach the main process only via `packages/editor/src/platform/`.
- The canvas page is rendered by `@daisy/renderer` (imperative DOM), never by React.
- The edit frame never executes user code. Preview is isolated (docs/architecture/SECURITY.md).
- One CSS generator (`@daisy/css`) for canvas and export. A gesture writes exactly the CSS the spec says.
- New package edges, new dependencies, or relaxing an Electron security setting need an ADR.

## 3a. Classes and dependency injection (ADR 0011 — the owner's rule)

- **Classes first, everywhere** — app code, scripts, hooks, tests helpers. No module-level functions in
  `.ts` files (ESLint enforces it). Pure logic is a class with methods, or static methods on a class.
- **Constructor injection** through `@daisy/di`: a class lists its dependencies in
  `static readonly inject = [TokenA, TokenB] as const` and stores them in `#private` fields. Never `new` a
  service inside another service; never resolve from a container inside a class.
- Each package declares its **tokens** in `src/tokens.ts` and its registrations in a `XModule` class.
  Composition roots (main process `index.ts`, renderer `main.tsx`, tests) build a `Container` and `load()` modules.
- Program against interfaces/abstract classes; bind implementations in the module, so tests swap fakes in a child container.
- **The one exception:** React components and hooks are functions (React requires it). Keep them thin —
  they read services with `useService(Token)` and render; logic lives in classes.

## 3b. Languages (ADRs 0013, 0014)

- **TypeScript** for the app.
- **C++** only inside `packages/native` as the Node-API addon (use the `daisy-native-addon` skill). Every
  native function sits behind a DI token. The addon is required: no pure-Node fallback (ADR 0015). No
  separate executables.
- **Python** only for repository tooling (`py/`, `design-src/`); never shipped.
- No Go. The class-first rule applies in every language.

## 3c. No fallbacks (the owner's rule)

- **Fail loudly.** If something does not work — a missing addon, a failed build step, a dependency that
  will not load, an IPC call that errors, a bad config — throw and stop. Break the app; do not degrade.
- **No fallback unless the owner asked for it by name.** No silent `catch`, no "skip and warn", no
  alternative implementation, no default value that hides a failure. A fallback the owner did not ask
  for is a bug.
- This is about how Daisy's own code handles failure. Fallbacks that are part of the **generated website**
  and already in the approved spec (font fallback stacks, WebP with a fallback image) are features, not
  error handling.
- An existing fallback in PLAN.md or an ADR is not approval on its own: raise it with the owner before
  building it.

## 4. How to do a task

1. `pnpm check:tasks --next` (or the task you were given). Mark it `in progress`.
2. Load the spec: the `daisy-spec-lookup` skill finds the PLAN/UI-plan sections and design boards.
3. Use the matching skill (`.claude/skills/`) — e.g. `daisy-document-command`, `daisy-canvas-tool`,
   `daisy-property-group`, `daisy-ui-component`, `daisy-ipc-channel`, `daisy-mcp-tool`.
4. Tests with the code (docs/engineering/TESTING.md). A visual edit is tested by its exported code.
5. `pnpm check` must pass. UI work: compare with the board (`ui-fidelity-reviewer` subagent).
6. Set the task to `done`, update docs you affected, open a PR with a Conventional Commit title.

## 5. Definition of done

Acceptance criteria covered by automated tests · `pnpm check` green · no new lint suppressions ·
spec and docs updated · the task file updated · UI matches its board (tokens only, no ad-hoc values).

## 6. Never

- Never edit the document outside commands, or read the DOM to learn what the document is.
- Never add `any`, `@ts-ignore`, `eslint-disable` without a comment that names the reason and an issue.
- Never write files outside the project folder or a folder the user picked.
- Never commit secrets, `.env`, or generated output (`dist`, `out`, `release`).
- Never change `pnpm-lock.yaml` by hand; never `--force` push to `main`.
- Never invent UI: if a screen or state is not designed, ask (or add it to UI_DESIGN_PLAN.md first).
- Never add a fallback the owner did not ask for (3c). If it does not work, it fails.
- Never put AI attribution in commits or PRs: no `Co-Authored-By` line for an agent, no "Generated with …"
  footer, no mention of the agent or tool that wrote the change — in commit messages, PR titles or bodies,
  or review comments. The owner's rule; it overrides any tool's default attribution.

## 7. Words

UI text uses the vocabulary in UI_DESIGN_PLAN.md 6.4 and PLAN.md 3.7 ("Space inside", "Screen size",
"Shared part"). Code uses CSS names (`padding`, `@media`).

## 8. Other languages: commands

```sh
pnpm --filter @daisy/native test:cpp   # C++ core tests
uvx ruff check py && pytest py         # Python tooling
```
