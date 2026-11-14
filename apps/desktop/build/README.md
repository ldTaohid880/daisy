# Build resources

App icons, made from the Daisy brand mark (UI_DESIGN_PLAN.md 4.2 "Brand mark", task M00-T06):

- `icon.svg` — source: the brand-mark tile on a 1024 canvas
- `icon.png` — 1024 px; macOS (electron-builder converts it to `.icns`) and Linux
- `icon.ico` — Windows, 16–256 px

Do not edit them by hand. Regenerate from `py/` with ImageMagick 7 installed:

```sh
python -m daisy_tools.icons.app_icon
```

electron-builder picks them up automatically from this folder.
