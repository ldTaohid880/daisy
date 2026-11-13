import { expect, test } from '@playwright/test';
import { DaisyAppDriver } from './support/DaisyAppDriver.js';

test('the app starts and shows its version', async () => {
  const driver = new DaisyAppDriver();
  const window = await driver.launch();
  await expect(window.getByRole('heading', { name: 'Daisy' })).toBeVisible();
  await expect(window.getByText(/^Version /)).toBeVisible();
  await driver.close();
});
