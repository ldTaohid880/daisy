# Contributing to Daisy

Thank you for helping. Daisy is built by people and AI agents together; the same rules apply to both.

1. **Pick a task** from `docs/tasks/` (`pnpm check:tasks --next`), or open an issue first for anything not planned.
2. **Branch** from `main`: `m01/t04-doc-store` (milestone/task-short-name).
3. **Read the spec** the task points to (PLAN.md / UI_DESIGN_PLAN.md sections and design boards). The spec wins; if it is wrong, change the spec first in the same PR and say why.
4. **Write tests first or alongside** (docs/engineering/TESTING.md). A visual edit is tested by its exported code.
5. **Run `pnpm check`** — it must pass locally before you push.
6. **Open a PR** with a Conventional Commit title (`feat(model): add moveNode command`) and fill in the template. Mark the task `done` in its task file in the same PR.

Code style: docs/engineering/CODING_STANDARDS.md. Workflow details: docs/engineering/WORKFLOW.md.
By contributing you agree your work is released under the MIT licence.
