# Tasks

- One file per milestone (`Mxx-name.md`). Each task has an id `Mxx-Tyy`, a status and optional _Needs_ and _Done when_.
- Statuses: `todo`, `in progress`, `in review`, `done`, `blocked`.
- `pnpm check:tasks` lists everything; `pnpm check:tasks --next` gives the first `todo` task.
- Change a task's status in the same PR that does the work. Add tasks freely inside a milestone; give them the next number.
- A task that is larger than one PR should be split before starting.
