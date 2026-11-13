import re
src = open('/home/claude/daisy/project/Main.dc.html', encoding='utf-8').read()
Z = 0.55; K = 0.85 / Z
R = lambda old, new, n=1: globals().__setitem__('src', src.replace(old, new, n)) if old in src else (_ for _ in ()).throw(KeyError(old[:60]))
R('<title>Daisy · D-04 Editor, heading selected</title>', '<title>Daisy · D-34 Compact frame 1440 × 900</title>')
R('width: 1920px; height: 1080px;', 'width: 1440px; height: 900px;')
R('index.html @ 85%', 'index.html @ 55%')
R('<span style="width: 28px">85%</span>', '<span style="width: 28px">Fit 55%</span>')
R('left: 46px; top: 13px;', 'left: 22px; top: 13px;')
R('<!-- page frame: 1440 @ 85% = 1224 -->', '<!-- page frame: 1440 @ 55% (Fit) = 792 -->')
R('left: 46px; top: 32px; bottom: 0; width: 1224px;', 'left: 22px; top: 32px; bottom: 0; width: 792px;')
R('transform: scale(0.85)', f'transform: scale({Z})')
# overlay: keep screen-constant thickness at the new zoom
a = src.index('<!-- selection overlay'); b = src.index('<!-- vertical scroll indicator')
seg = src[a:b]
def scale_overlay(s):
    s = s.replace('values ÷ 0.85', f'values ÷ {Z}')
    def f(m): return f'{float(m.group(1))*K:.2f}px'.replace('.00px', 'px')
    s = re.sub(r'(?<![\w.])(-?\d+\.\d+)px', f, s)            # decimals: 1.76, 9.4, 5.6, 4.7, 1.18, 8.3, 1.2
    s = s.replace('width: 7px; height: 7px', f'width: {7*K:.1f}px; height: {7*K:.1f}px')
    s = s.replace('bottom: calc(100% + 2px); height: 21px; padding: 0 5px', f'bottom: calc(100% + {2*K:.1f}px); height: {21*K:.1f}px; padding: 0 {5*K:.1f}px')
    s = s.replace("font: 500 13px/1 'Inter'", f"font: 500 {13*K:.1f}px/1 'Inter'")
    return s
# only the overlay pieces, not the page's own markup: overlay block, parent outline, fold line
ov_a = seg.index('<!-- selection overlay'); ov_b = seg.index('</div>\n</div>\n<p style="margin: 0; font-size: 18px') + len('</div>')
seg = seg[:ov_a] + scale_overlay(seg[ov_a:ov_b]) + seg[ov_b:]
seg = seg.replace('border: 1.18px dashed rgba(47,128,237,0.6)', f'border: {1.18*K:.2f}px dashed rgba(47,128,237,0.6)')
seg = seg.replace('border-top: 1.18px dashed rgba(47,128,237,0.35)', f'border-top: {1.18*K:.2f}px dashed rgba(47,128,237,0.35)')
seg = seg.replace('right: 54px; top: 800px;', f'left: {22+792-58}px; top: {32+int(900*Z)+5}px;')
seg = seg.replace('height: 470px; border-radius: 2px', 'height: 300px; border-radius: 2px')
src = src[:a] + seg + src[b:]
# options bar: Distribute and Corner roundness go into More (low priority; Corner stays in Properties > Border)
d_a = src.index('<!-- distribute (needs 3+ selected) -->'); d_b = src.index('<span style="flex: 1"></span>', d_a)
src = src[:d_a] + src[d_b:]
R('<button aria-label="More options" style="width: 28px; height: 28px;',
  '<button aria-label="More options · Distribute, Corner roundness" title="More · Distribute, Corner roundness" style="position: relative; width: 28px; height: 28px;')
R('<section aria-label="Swatches and History" style="height: 220px;', '<section aria-label="Swatches and History" style="height: 188px;')
import sys
open('/home/claude/daisy/project/D34-Compact.dc.html', 'w', encoding='utf-8').write(src)
print('ok')
