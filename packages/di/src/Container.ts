import type { Token } from './Token.js';

/** A class the container can build: its constructor parameters are listed, in order, in `inject`. */
export interface InjectableClass<T> {
  new (...args: never[]): T;
  readonly inject?: readonly Token<unknown>[];
}

/** Anything with resources to release when its container is disposed. */
export interface Disposable {
  dispose(): void | Promise<void>;
}

/** A package's registrations, applied at a composition root (main process, renderer, tests). */
export interface Module {
  register(container: Container): void;
}

export type Lifetime = 'singleton' | 'transient';

type Provider<T> =
  | { readonly kind: 'class'; readonly lifetime: Lifetime; readonly ctor: InjectableClass<T> }
  | { readonly kind: 'value'; readonly value: T }
  | { readonly kind: 'factory'; readonly lifetime: Lifetime; readonly create: (container: Container) => T };

export class ContainerError extends Error {
  override readonly name = 'ContainerError';
}

/**
 * Small, explicit dependency-injection container (ADR 0011). No decorators, no reflection:
 * a class declares `static readonly inject = [TokenA, TokenB] as const` matching its constructor.
 */
export class Container {
  readonly #parent: Container | undefined;
  readonly #providers = new Map<Token<unknown>, Provider<unknown>>();
  readonly #singletons = new Map<Token<unknown>, unknown>();
  readonly #created: unknown[] = [];
  readonly #resolving: Token<unknown>[] = [];

  constructor(parent?: Container) {
    this.#parent = parent;
  }

  bindClass<T>(token: Token<T>, ctor: InjectableClass<T>, lifetime: Lifetime = 'singleton'): this {
    const needed = ctor.length;
    const given = ctor.inject?.length ?? 0;
    if (given < needed) {
      throw new ContainerError(
        `${ctor.name} takes ${String(needed)} constructor arguments but declares ${String(given)} in static inject`,
      );
    }
    return this.#set(token, { kind: 'class', lifetime, ctor });
  }

  bindValue<T>(token: Token<T>, value: T): this {
    return this.#set(token, { kind: 'value', value });
  }

  bindFactory<T>(
    token: Token<T>,
    create: (container: Container) => T,
    lifetime: Lifetime = 'singleton',
  ): this {
    return this.#set(token, { kind: 'factory', lifetime, create });
  }

  load(...modules: readonly Module[]): this {
    for (const module of modules) module.register(this);
    return this;
  }

  has(token: Token<unknown>): boolean {
    return this.#providers.has(token) || (this.#parent?.has(token) ?? false);
  }

  /**
   * Builds or returns the service for a token. Singletons belong to the container that registered
   * them (built from its bindings, cached there). Transients are built in the asking container, so a
   * child scope's overrides apply to them.
   */
  resolve<T>(token: Token<T>): T {
    const found = this.#find(token);
    if (!found) throw new ContainerError(`Nothing is bound to ${token.description}`);
    const { provider, owner } = found;
    if (provider.kind === 'value') return provider.value;
    if (provider.lifetime === 'singleton' && owner !== this) return owner.resolve(token);
    if (provider.lifetime === 'singleton' && this.#singletons.has(token))
      return this.#singletons.get(token) as T;
    if (this.#resolving.includes(token)) {
      const chain = [...this.#resolving, token].map((t) => t.description).join(' → ');
      throw new ContainerError(`Circular dependency: ${chain}`);
    }
    this.#resolving.push(token);
    try {
      const instance = provider.kind === 'class' ? this.#construct(provider.ctor) : provider.create(this);
      if (provider.lifetime === 'singleton') this.#singletons.set(token, instance);
      this.#created.push(instance);
      return instance;
    } finally {
      this.#resolving.pop();
    }
  }

  /** A scope that sees this container's bindings and can override them (tests, per-window services). */
  createChild(): Container {
    return new Container(this);
  }

  /** Disposes everything this container created, newest first. */
  async dispose(): Promise<void> {
    for (const instance of this.#created.reverse()) {
      if (Container.#isDisposable(instance)) await instance.dispose();
    }
    this.#created.length = 0;
    this.#singletons.clear();
  }

  #find<T>(token: Token<T>): { provider: Provider<T>; owner: Container } | undefined {
    const provider = this.#providers.get(token) as Provider<T> | undefined;
    if (provider) return { provider, owner: this };
    return this.#parent ? this.#parent.#find(token) : undefined;
  }

  #set<T>(token: Token<T>, provider: Provider<T>): this {
    this.#providers.set(token, provider);
    this.#singletons.delete(token);
    return this;
  }

  #construct<T>(ctor: InjectableClass<T>): T {
    const args = (ctor.inject ?? []).map((dep) => this.resolve(dep));
    return new ctor(...(args as never[]));
  }

  static #isDisposable(value: unknown): value is Disposable {
    return (
      typeof value === 'object' &&
      value !== null &&
      typeof (value as Partial<Disposable>).dispose === 'function'
    );
  }
}
