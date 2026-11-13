---
name: daisy-release
description: Cut, verify and publish a Daisy release, or debug the release pipeline.
---

# Release

Follow docs/engineering/RELEASING.md. In short: merge the release-please PR → tag builds installers on three OSes →
draft GitHub Release → install-test each artifact (open Halden, export, auto-update from previous) → publish.
Never publish a draft with a failed OS job. Never edit CHANGELOG.md by hand.
