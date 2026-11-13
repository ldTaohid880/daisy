# @daisy/di

Dependency injection: typed tokens and a small container. Every Daisy class gets its collaborators from here.

**Owns:** Token<T>, Container (singleton, transient, value, factory registrations; child scopes; disposal), the Injectable contract (`static readonly inject`).

**Specification:** docs/adr/0011-classes-and-dependency-injection.md

**May import:** no other Daisy package. The full graph is in `docs/architecture/dependencies.json` and is checked by `pnpm check:deps`.

**Rules:** Never use decorators or reflect-metadata. Never resolve from a global container inside a class: take dependencies in the constructor.

**Tests:** `pnpm --filter @daisy/di test`. Test files sit next to the code as `*.test.ts`.
