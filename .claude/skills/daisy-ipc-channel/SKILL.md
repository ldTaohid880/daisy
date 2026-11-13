---
name: daisy-ipc-channel
description: Add a main↔renderer IPC channel or event with Zod contracts, a validated handler, and the platform wrapper.
---

# IPC channel

Spec: docs/architecture/IPC.md, SECURITY.md (Files).

1. Define in `packages/ipc/src/index.ts` (or `<area>.ts`) with `new Channel('area.action', Request, Response)`; add to `channels`.
2. Handler: a class in `apps/desktop/src/main/ipc/<Name>Handler.ts` implementing `IpcHandler<typeof channels.x>`, with its
   services injected; add it to `MainTokens.IpcHandlers` in `MainModule`. The `IpcRouter` validates both ways. Paths:
   resolve and check against the allowed roots before touching the disk.
3. The preload picks it up automatically from `channels`. Call it from the editor only via `platform` (packages/editor/src/platform).
4. Tests: schema tests in ipc; handler logic lives in a Node package (project-fs…) with its own unit tests.
