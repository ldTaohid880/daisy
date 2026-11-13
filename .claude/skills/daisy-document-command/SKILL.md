---
name: daisy-document-command
description: Add or change a model command (insert, move, set styles…) in @daisy/model with its inverse, invariants and tests.
---

# Document command

Spec: PLAN.md 10.2 (types and invariants), 10.6 (commands and history).

1. Put the command in `packages/model/src/commands/<Name>Command.ts` as a class implementing `Command<Args>`
   (`readonly id`, `readonly argsSchema`, `apply(draft, args): void` mutating an Immer draft). Register it in
   `ModelModule` (the command registry is injected into the store). The store wraps `apply` in
   `produceWithPatches`, so inverse patches come for free — but write a semantic inverse test anyway.
2. Validate args with the command's `argsSchema` at the boundary; trust them inside.
3. Keep invariants: run `assertInvariants(doc)` in tests after the command.
4. Tests in `<name>.test.ts`: result; apply + undo returns the identical document; invalid input is rejected; the
   property-based sequence test (`commands/sequence.test.ts`) includes the new command.
5. Export from `packages/model/src/index.ts`. Never add derived data to the document.
6. If the change alters stored shape: bump `SCHEMA_VERSION`, add a migration and a fixture saved in the previous version.
