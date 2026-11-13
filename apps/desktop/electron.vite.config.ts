import { resolve } from 'node:path';
import { defineConfig } from 'electron-vite';
import react from '@vitejs/plugin-react';

// Workspace packages are TypeScript source; they are bundled, not externalised.
const workspace = [
  '@daisy/di',
  '@daisy/editor',
  '@daisy/export',
  '@daisy/ipc',
  '@daisy/mcp-server',
  '@daisy/model',
  '@daisy/native',
  '@daisy/project-fs',
  '@daisy/ui',
];

export default defineConfig({
  main: {
    build: {
      externalizeDeps: { exclude: workspace },
      rolldownOptions: {
        input: {
          index: resolve(import.meta.dirname, 'src/main/index.ts'),
          // Small Node script AI apps launch for MCP over stdio; it forwards to the running app.
          'mcp-stdio': resolve(import.meta.dirname, 'src/main/mcp-stdio.ts'),
        },
      },
    },
  },
  // Sandboxed preloads cannot load modules at run time: bundle everything into one CommonJS file.
  preload: {
    build: {
      externalizeDeps: false,
      rolldownOptions: { output: { format: 'cjs', entryFileNames: '[name].cjs' } },
    },
  },
  renderer: {
    plugins: [react()],
    root: resolve(import.meta.dirname, 'src/renderer'),
    build: { rolldownOptions: { input: resolve(import.meta.dirname, 'src/renderer/index.html') } },
  },
});
