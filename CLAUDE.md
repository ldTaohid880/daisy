@AGENTS.md

## Claude Code specifics

- Skills in `.claude/skills/` cover the repeatable kinds of work; load the matching one before starting.
- Every TypeScript change follows ADR 0011 (classes + DI); the `daisy-di-service` skill shows the pattern.
- Subagents in `.claude/agents/`: `spec-reviewer`, `code-reviewer`, `test-engineer`,
  `ui-fidelity-reviewer`, `security-reviewer`, `milestone-planner`. Use reviewers before opening a PR.
- Commands: `/next-task`, `/check`, `/review`, `/plan-milestone`.
- Hooks format every file you write and block edits to lockfiles and build output.
- The Playwright MCP server (`.mcp.json`) can drive a browser for UI checks of the renderer in dev.
