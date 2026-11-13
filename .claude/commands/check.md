---
description: Run the full local gate and fix what fails
---

Run `pnpm check`. If anything fails, fix the cause (not the test), rerun until green, and summarise what changed. Also run `pnpm test:browser` if css or renderer changed.
