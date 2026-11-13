/** Composition root of the renderer (ADR 0011). */
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { Container } from '@daisy/di';
import type { DaisyApi } from '@daisy/ipc';
import { App, ContainerProvider, EditorModule } from '@daisy/editor';
import '@daisy/ui';

class RendererBootstrap {
  readonly #container: Container;

  constructor(api: DaisyApi | undefined) {
    this.#container = new Container().load(new EditorModule(api));
  }

  mount(rootId: string): void {
    const root = document.getElementById(rootId);
    if (!root) throw new Error(`#${rootId} missing from index.html`);
    createRoot(root).render(
      <StrictMode>
        <ContainerProvider container={this.#container}>
          <App />
        </ContainerProvider>
      </StrictMode>,
    );
  }
}

declare global {
  interface Window {
    daisy?: DaisyApi;
  }
}

new RendererBootstrap(window.daisy).mount('root');
