import { defineConfig } from 'vitest/config';

// Root runner: `pnpm vitest` runs every package's unit tests in one process.
export default defineConfig({
  test: {
    projects: ['packages/*', 'apps/desktop'],
  },
});
