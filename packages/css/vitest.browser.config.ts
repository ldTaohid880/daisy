import { defineConfig } from 'vitest/config';
import { playwright } from '@vitest/browser-playwright';

// Tests that need a real CSS engine (PLAN.md 17.1 "Browser unit"). Chromium is the
// engine Electron ships, so it is the one that must pass.
export default defineConfig({
  test: {
    name: 'css-browser',
    include: ['src/**/*.browser.test.ts'],
    browser: { enabled: true, provider: playwright(), headless: true, instances: [{ browser: 'chromium' }] },
  },
});
