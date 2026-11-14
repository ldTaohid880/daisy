from daisy_tools.icons.app_icon import AppIconSvg, DaisyGlyph, MarkTokens


class TestAppIconSvg:
    def setup_method(self) -> None:
        tokens = MarkTokens()
        self.svg = AppIconSvg(DaisyGlyph(tokens), tokens).render()

    def test_has_eight_petals_and_a_brand_centre(self) -> None:
        assert self.svg.count("<ellipse") == 8
        assert 'fill="#f2b84b"' in self.svg

    def test_tile_keeps_the_mark_proportions(self) -> None:
        tile = AppIconSvg.CANVAS - 2 * AppIconSvg.MARGIN
        assert f'rx="{6 * tile / 28:.2f}"' in self.svg
        assert 'fill="#1f1f1f"' in self.svg
        assert 'stroke="#303030"' in self.svg

    def test_is_square_1024(self) -> None:
        assert 'viewBox="0 0 1024 1024"' in self.svg
