---
name: daisy-polyglot-component
description: Decide where non-TypeScript code goes in Daisy - C++ only as the Node addon, Python only for repository tooling, no Go (ADR 0014).
---

# Code in other languages (ADR 0014)

- **C++** → only as a function of the Node-API addon in `packages/native`. Use the `daisy-native-addon` skill.
  No standalone executables or sidecars.
- **Python** → only repository tooling in `py/daisy_tools/<area>/` (fixtures, sample projects, design-board
  generators, analysis). Classes first, type hints, ruff, pytest. Never shipped in the app.
- **Go** → not used. If a task seems to need it, write it in TypeScript or as an addon function and say why in the PR.
