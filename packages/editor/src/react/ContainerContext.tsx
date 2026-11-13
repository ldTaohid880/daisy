/*
 * The bridge between the DI container and React. React views are the one place Daisy uses
 * functions (components and hooks, ADR 0011): they stay thin and get every service from here.
 */
import { createContext, useContext, type ReactNode } from 'react';
import type { Container, Token } from '@daisy/di';

const ContainerContext = createContext<Container | null>(null);

export function ContainerProvider({ container, children }: { container: Container; children: ReactNode }) {
  return <ContainerContext.Provider value={container}>{children}</ContainerContext.Provider>;
}

export function useService<T>(token: Token<T>): T {
  const container = useContext(ContainerContext);
  if (!container) throw new Error('useService needs a <ContainerProvider> above it');
  return container.resolve(token);
}
