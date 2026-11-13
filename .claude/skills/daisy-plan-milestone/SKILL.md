---
name: daisy-plan-milestone
description: Refine a roadmap milestone into ready tasks (needs, done-when, packages, tests) from PLAN.md and the design boards before starting it.
---

# Plan a milestone

1. Open `docs/tasks/Mxx-*.md`, its PLAN.md milestone section, and every listed board.
2. For each task: add **Needs** (task ids), **Done when** (observable, testable), and the package(s). Split tasks larger
   than one PR. Add missing tasks the boards or acceptance criteria imply (states sheets!).
3. Map every acceptance criterion to at least one task and one test.
4. Note risks from PLAN.md 19.2 that apply.
5. Commit the refined file as its own PR (`docs(tasks): plan Mxx`) before implementation starts.
