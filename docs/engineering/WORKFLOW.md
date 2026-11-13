# Workflow

## Branches and commits

- `main` is always releasable and protected: PRs only, CI must pass, one approving review.
- Branch names: `m03/t05-autosave`, `fix/<short>`, `docs/<short>`.
- PR titles follow Conventional Commits; scope = package (`feat(css): …`, `fix(desktop): …`).
  They become the changelog (release-please). Squash-merge.

## The task loop (people and agents)

1. `pnpm check:tasks --next` → read the task file entry and the milestone header.
2. Read every spec section and design board the task lists. Use the `daisy-spec-lookup` skill.
3. Plan in the PR description: files to touch, tests to add, risks.
4. Implement with tests (docs/engineering/TESTING.md). Keep the change to the task.
5. `pnpm check` green. For UI work, compare with the design board (`ui-fidelity-reviewer`).
6. Update the task's status to `done`, and any docs the change affects.
7. Open the PR. Reviews: `code-reviewer` and `spec-reviewer` subagents, then a person.

## Parallel work

Tasks inside a milestone list their dependencies (`Needs:`). Agents may take independent tasks in
parallel, each in its own branch or worktree. Never edit another task's files without saying so in
the PR.

## When the spec is wrong

Change PLAN.md / UI_DESIGN_PLAN.md first (with a change-log row), or add an ADR when it is an
architectural choice, in the same PR. Code never silently diverges from the spec.
