# 0009. Agent-native development

- **Status:** Accepted
- **Date:** 2026-11-13
- **Supersedes in PLAN.md / UI_DESIGN_PLAN.md:** —

## Context

Most code will be written by AI agents working in parallel, reviewed by people and other agents.

## Decision

AGENTS.md is the canonical guide (CLAUDE.md imports it); every package has its own AGENTS.md; repeatable work is captured as skills in `.claude/skills`; reviews use subagents in `.claude/agents`; work is broken into task files with IDs; `pnpm check` is the single gate and runs in hooks and CI.

## Consequences

Agents find the spec, the rules and the next task without asking. The cost is keeping these files current — a task is not done until its docs are.
