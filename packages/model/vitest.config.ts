import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    name: 'model',
    environment: 'node',
    include: ['src/**/*.test.{ts,tsx}'],
    exclude: ['src/**/*.browser.test.{ts,tsx}'],
  },
});
