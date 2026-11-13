---
description: Review the current branch before a PR
---

Run the spec-reviewer, code-reviewer and (for UI changes) ui-fidelity-reviewer subagents on `git diff main...HEAD`; run security-reviewer if Electron, IPC, files, frames or MCP changed. Fix blocking items, then list what remains.
