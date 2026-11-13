---
name: daisy-di-service
description: Create a class-based service with constructor injection: tokens, module registration, composition root and tests with fakes.
---

# Service with dependency injection (ADR 0011)

1. Write the class in its package: dependencies as constructor parameters, stored in `#private` fields, listed in
   `static readonly inject = [Tokens.A, Tokens.B] as const` in the same order. No module-level functions.
2. Add a token in the package's `src/tokens.ts`: `X: new Token<XInterface>('pkg.X')` — type it with an interface
   when there may be more than one implementation (e.g. a fake).
3. Register it in the package's `XModule.register(container)` with `bindClass` (singleton by default).
4. Consumers get it through their own constructor (never `container.resolve` inside a class). React views use
   `useService(Tokens.X)` and stay thin.
5. Test: `new Container().load(new XModule())`, then `createChild().bindValue(Tokens.Dep, fake)` to swap collaborators.
