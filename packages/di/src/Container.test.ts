import { describe, expect, it } from 'vitest';
import { Container, ContainerError, Token } from './index.js';

class Clock {
  now(): number {
    return 42;
  }
}
const ClockToken = new Token<Clock>('Clock');

class Greeter {
  static readonly inject = [ClockToken] as const;
  readonly #clock: Clock;
  constructor(clock: Clock) {
    this.#clock = clock;
  }
  greet(): string {
    return `hello at ${String(this.#clock.now())}`;
  }
}
const GreeterToken = new Token<Greeter>('Greeter');

describe('Container', () => {
  it('builds classes with their declared dependencies', () => {
    const c = new Container().bindClass(ClockToken, Clock).bindClass(GreeterToken, Greeter);
    expect(c.resolve(GreeterToken).greet()).toBe('hello at 42');
  });

  it('returns one instance for singletons and new ones for transients', () => {
    const c = new Container().bindClass(ClockToken, Clock).bindClass(GreeterToken, Greeter, 'transient');
    expect(c.resolve(ClockToken)).toBe(c.resolve(ClockToken));
    expect(c.resolve(GreeterToken)).not.toBe(c.resolve(GreeterToken));
  });

  it('lets a child scope override a binding', () => {
    const parent = new Container().bindClass(ClockToken, Clock).bindClass(GreeterToken, Greeter, 'transient');
    const child = parent.createChild().bindValue(ClockToken, { now: () => 7 });
    expect(child.resolve(GreeterToken).greet()).toBe('hello at 7');
  });

  it('reports missing bindings and cycles', () => {
    const A = new Token<unknown>('A');
    const B = new Token<unknown>('B');
    const c = new Container().bindFactory(A, (x) => x.resolve(B)).bindFactory(B, (x) => x.resolve(A));
    expect(() => c.resolve(A)).toThrow(/Circular dependency: A → B → A/);
    expect(() => new Container().resolve(A)).toThrow(ContainerError);
  });

  it('refuses a class whose inject list is shorter than its constructor', () => {
    class Needy {
      readonly clock: Clock;
      constructor(clock: Clock) {
        this.clock = clock;
      }
    }
    expect(() => new Container().bindClass(new Token<Needy>('Needy'), Needy)).toThrow(/static inject/);
  });

  it('disposes created instances newest first', async () => {
    const order: string[] = [];
    class R {
      static count = 0;
      readonly id = `r${String(++R.count)}`;
      dispose(): void {
        order.push(this.id);
      }
    }
    const R1 = new Token<R>('R1');
    const R2 = new Token<R>('R2');
    const c = new Container().bindClass(R1, R).bindClass(R2, R);
    c.resolve(R1);
    c.resolve(R2);
    await c.dispose();
    expect(order).toEqual(['r2', 'r1']);
  });
});
