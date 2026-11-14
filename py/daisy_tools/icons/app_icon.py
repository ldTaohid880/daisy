"""App icon from the Daisy brand mark (UI_DESIGN_PLAN.md 4.2 "Brand mark", task M00-T06).

The mark is a 28 x 28 tile, radius 6, ``bg-panel`` with a 1 px inner ``line`` ring, and an 18 px daisy
glyph: eight petals in ``text-primary`` and a ``brand-daisy`` centre. The app icon is that tile scaled
up on a 1024 canvas with a margin. Run: ``python -m daisy_tools.icons.app_icon`` from ``py/``.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MarkTokens:
    """Token values from UI_DESIGN_PLAN.md chapter 9 (dark theme)."""

    bg_panel: str = "#1f1f1f"
    line: str = "#303030"
    text_primary: str = "#e8e8e8"
    brand_daisy: str = "#f2b84b"


class DaisyGlyph:
    """The 18-unit daisy glyph, identical to design-src/lib.py ``daisy()``."""

    VIEWBOX = 18.0

    def __init__(self, tokens: MarkTokens) -> None:
        self._tokens = tokens

    def petals(self) -> list[str]:
        straight = [(9, 4, 1.9, 3), (9, 14, 1.9, 3), (4, 9, 3, 1.9), (14, 9, 3, 1.9)]
        diagonal = [(5.5, 5.5, -45), (12.5, 12.5, -45), (12.5, 5.5, 45), (5.5, 12.5, 45)]
        out = [f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}"/>' for x, y, rx, ry in straight]
        out += [
            f'<ellipse cx="{x}" cy="{y}" rx="1.7" ry="2.7" transform="rotate({a} {x} {y})"/>'
            for x, y, a in diagonal
        ]
        return out

    def svg_group(self) -> str:
        petals = "".join(self.petals())
        return (
            f'<g fill="{self._tokens.text_primary}">{petals}</g>'
            f'<circle cx="9" cy="9" r="2.6" fill="{self._tokens.brand_daisy}"/>'
        )


class AppIconSvg:
    """The brand-mark tile at app-icon size."""

    CANVAS = 1024
    MARK = 28.0  # mark tile size in the editor
    MARGIN = 72  # canvas edge to tile, so the icon sits with other platform icons

    def __init__(self, glyph: DaisyGlyph, tokens: MarkTokens) -> None:
        self._glyph = glyph
        self._tokens = tokens

    def render(self) -> str:
        tile = self.CANVAS - 2 * self.MARGIN
        unit = tile / self.MARK
        radius = 6 * unit
        ring = 1 * unit
        glyph_size = 18 * unit
        glyph_scale = glyph_size / DaisyGlyph.VIEWBOX
        offset = (self.CANVAS - glyph_size) / 2
        inset = self.MARGIN + ring / 2
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.CANVAS}" height="{self.CANVAS}" '
            f'viewBox="0 0 {self.CANVAS} {self.CANVAS}">'
            f'<rect x="{self.MARGIN}" y="{self.MARGIN}" width="{tile}" height="{tile}" '
            f'rx="{radius:.2f}" fill="{self._tokens.bg_panel}"/>'
            f'<rect x="{inset:.2f}" y="{inset:.2f}" width="{tile - ring:.2f}" height="{tile - ring:.2f}" '
            f'rx="{radius - ring / 2:.2f}" fill="none" stroke="{self._tokens.line}" '
            f'stroke-width="{ring:.2f}"/>'
            f'<g transform="translate({offset:.2f} {offset:.2f}) scale({glyph_scale:.4f})">'
            f"{self._glyph.svg_group()}</g></svg>\n"
        )


class IconRenderer:
    """Writes icon.svg and renders icon.png and icon.ico with ImageMagick 7 (``magick``).

    No icon.icns: ImageMagick cannot write it, and electron-builder builds it from icon.png on macOS.
    """

    ICO_SIZES = (256, 128, 64, 48, 32, 24, 16)

    def __init__(self, svg: AppIconSvg, out_dir: Path) -> None:
        self._svg = svg
        self._out = out_dir

    def run(self) -> None:
        magick = shutil.which("magick")
        if magick is None:
            raise RuntimeError("ImageMagick 7 ('magick') is required to render the app icon.")
        self._out.mkdir(parents=True, exist_ok=True)
        source = self._out / "icon.svg"
        source.write_text(self._svg.render(), encoding="utf-8", newline="\n")
        png = self._out / "icon.png"
        self._magick(
            magick,
            "-background",
            "none",
            "-density",
            "96",
            str(source),
            "-resize",
            "1024x1024",
            "-depth",
            "8",
            str(png),
        )
        sizes = ",".join(str(s) for s in self.ICO_SIZES)
        self._magick(magick, str(png), "-define", f"icon:auto-resize={sizes}", str(self._out / "icon.ico"))

    @staticmethod
    def _magick(*args: str) -> None:
        subprocess.run(args, check=True)


class AppIconCli:
    @staticmethod
    def main() -> int:
        tokens = MarkTokens()
        out = Path(__file__).resolve().parents[3] / "apps" / "desktop" / "build"
        IconRenderer(AppIconSvg(DaisyGlyph(tokens), tokens), out).run()
        return 0


if __name__ == "__main__":
    sys.exit(AppIconCli.main())
