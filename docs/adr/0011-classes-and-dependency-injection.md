# 0011. Classes and dependency injection

- **Status:** Accepted
- **Date:** 2026-11-13
- **Supersedes in PLAN.md / UI_DESIGN_PLAN.md:** PLAN.md 10.6 and 15.1 where they describe commands, tools and generators as functions: these become classes with the same responsibilities.

## Context

The owner requires all TypeScript to be written as classes with dependency injection, with classes preferred over functions everywhere, build scripts included. Many agents will extend the code; explicit dependencies keep it testable and replaceable.

## Decision

All TypeScript logic lives in classes. Dependencies are passed to constructors and declared in `static readonly inject = [...] as const`; the small `@daisy/di` container (typed tokens, singleton/transient/value/factory bindings, child scopes, disposal; no decorators or reflect-metadata) builds them at composition roots: the main process, the preload, the renderer and tests. Each package has `tokens.ts` and an `XModule` class. ESLint forbids module-level functions in `.ts` files. React components and hooks are the only functions, because React requires it; they stay thin and get services through `useService`. Repository scripts and hooks are TypeScript classes run by Node 24's type stripping.

## Consequences

Every collaborator can be swapped in tests through a child container. Slightly more ceremony per service; decorator-based libraries (InversifyJS, tsyringe) were rejected because they need legacy decorators and runtime reflection, which do not fit the native TypeScript 7 compiler or Node type stripping.
