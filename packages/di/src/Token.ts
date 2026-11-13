/**
 * A typed key for the container. Tokens are compared by identity, so declare each one once
 * (in the owning package's `tokens.ts`) and import it everywhere else.
 */
export class Token<T> {
  declare readonly __type: T;
  readonly description: string;

  constructor(description: string) {
    this.description = description;
  }

  toString(): string {
    return `Token(${this.description})`;
  }
}
