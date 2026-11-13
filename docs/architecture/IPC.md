# IPC contracts

All main ↔ renderer communication is declared in `packages/ipc/src`. A channel is

```ts
export const projectOpen = channel('project.open', z.object({ path: z.string() }), ProjectSnapshot);
```

- Names are `area.action` (`project.open`, `project.save`, `export.write`, `mcp.request`).
- Request and response are Zod schemas; the preload validates requests, the main process
  validates both directions (apps/desktop/src/main/ipc.ts).
- Main → renderer events (outside file change, MCP change request, update ready) use `event()`
  definitions in the same package and are delivered through one subscription API.
- Paths: the renderer may only pass paths that came from a main-process dialog or from the open
  project. The main process re-checks every path is inside an allowed root.
- Add a channel with the `daisy-ipc-channel` skill.
