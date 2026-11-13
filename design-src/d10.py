from screen import *

S = Screen('Daisy · D-10 Free element with guides')
S.remove_h1_overlay()
S.remove_parent_outline()
S.unselect_h1_row()

MAG, MAGF = '#e535ab', '#c21f8f'
BW, BH, TOP, RIGHT = 88, 36, 62, 24
GRID_W = 1312
bx = GRID_W - RIGHT - BW   # 1200

pill = lambda x, y, t: f'<span style="position: absolute; left: {x}px; top: {y}px; height: 20px; padding: 0 7px; display: flex; align-items: center; border-radius: 10px; background: {MAGF}; color: #fff; font: 500 12px/1 \'Inter\', sans-serif; white-space: nowrap; z-index: 4">{t}</span>'
overlays = f'''
<!-- the Free element itself (part of the page) -->
<span style="position: absolute; right: {RIGHT}px; top: {TOP}px; width: {BW}px; height: {BH}px; display: flex; align-items: center; justify-content: center; border-radius: 999px; background: #b5532d; color: #ffffff; font-size: 15px; font-weight: 600; letter-spacing: 0.02em; z-index: 2">New</span>
<!-- anchor: Hero grid -->
<div aria-hidden="true" style="position: absolute; top: -1px; left: -1px; right: -1px; bottom: -1px; border: 1.18px dashed rgba(47,128,237,0.6); pointer-events: none"></div>
<!-- alignment guide: badge top = Hero text top -->
<div aria-hidden="true" style="position: absolute; left: 0; width: {bx + BW}px; top: {TOP}px; border-top: 1.18px solid {MAG}; pointer-events: none; z-index: 3"></div>
<span aria-hidden="true" style="position: absolute; left: 690px; top: {TOP - 24}px; height: 20px; padding: 0 7px; display: flex; align-items: center; border-radius: 10px; background: {MAGF}; color: #fff; font: 500 12px/1 'Inter', sans-serif; white-space: nowrap; z-index: 4">aligned · Hero text top</span>
<!-- pin lines to the anchor -->
<div aria-hidden="true" style="position: absolute; left: {bx + BW / 2}px; top: 0; height: {TOP}px; border-left: 1.18px dashed {MAG}; pointer-events: none; z-index: 3"></div>
{pill(bx + BW / 2 - 36, 16, str(TOP))}
<div aria-hidden="true" style="position: absolute; left: {bx + BW}px; width: {RIGHT}px; top: {TOP + BH / 2}px; border-top: 1.18px dashed {MAG}; pointer-events: none; z-index: 3"></div>
{pill(bx + BW + 2, TOP + BH / 2 + 6, str(RIGHT))}
<!-- selection on the badge -->
{overlay_box(bx - 1, TOP - 1, BW + 2, BH + 2, 'Box · New ◇', extra='z-index: 4')}
<svg aria-hidden="true" width="26" height="26" viewBox="0 0 16 16" style="position: absolute; left: {bx + 30}px; top: {TOP + 14}px; overflow: visible; z-index: 5"><path d="M5 8V5.5a1 1 0 0 1 2 0V8M7 7.5V5a1 1 0 0 1 2 0v2.5M9 7.5V5.5a1 1 0 0 1 2 0V8M11 8V7a1 1 0 0 1 2 0v3a4 4 0 0 1-4 4H8.5a4 4 0 0 1-3.3-1.7L3.5 9.8a1 1 0 0 1 1.5-1.3L5 9V8z" fill="#ffffff" stroke="#1d1a16" stroke-width="1.1" stroke-linejoin="round"></path></svg>
'''
S.rep('<div style="display: grid; grid-template-columns: 1.1fr 1fr; gap: 64px; align-items: center">',
      '<div style="position: relative; display: grid; grid-template-columns: 1.1fr 1fr; gap: 64px; align-items: center">')
s = S.s
img_open = '<div style="justify-self: end; width: 580px; height: 520px; border-radius: 12px; overflow: hidden; background: #e6dccd">'
a = s.index(img_open)
b = s.index('</svg>\n</div>', a) + len('</svg>\n</div>')
S.s = s[:b] + overlays + s[b:]

# options bar: Free selected + pin widget
S.rep('<button aria-pressed="true" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; background: #333333; color: #e8e8e8; font-weight: 500">',
      '<button aria-pressed="false" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; color: #939393">')
S.rep('<button aria-pressed="false" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; color: #939393">\n<svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" aria-hidden="true"><path d="M8 1.5l6.5 6.5L8 14.5 1.5 8z"></path></svg>Free\n</button>',
      '<button aria-pressed="true" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; background: #333333; color: #e8e8e8; font-weight: 500">\n<svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" aria-hidden="true"><path d="M8 1.5l6.5 6.5L8 14.5 1.5 8z"></path></svg>Free\n</button>\n'
      '<span style="width: 1px; height: 14px; background: #333333; margin: 0 2px"></span>'
      '<button aria-label="Pinned to Top and Right" title="Pinned to Top and Right of Hero grid" style="position: relative; width: 24px; height: 24px; border-radius: 4px; background: #2a2a2a">'
      '<span style="position: absolute; left: 7px; top: 7px; width: 10px; height: 10px; box-sizing: border-box; border: 1px dashed #6b6b6b"></span>'
      '<span style="position: absolute; left: 9px; top: 2px; width: 6px; height: 2px; border-radius: 1px; background: #2f80ed"></span>'
      '<span style="position: absolute; left: 9px; bottom: 2px; width: 6px; height: 1.5px; border-radius: 1px; background: #6b6b6b"></span>'
      '<span style="position: absolute; top: 9px; left: 2px; width: 1.5px; height: 6px; border-radius: 1px; background: #6b6b6b"></span>'
      '<span style="position: absolute; top: 9px; right: 2px; width: 2px; height: 6px; border-radius: 1px; background: #2f80ed"></span></button>')
S.options('1200', '62', '88', 'Fit', '36', 'Fit')

# Layers: new Free row under Hero grid, selected
s = S.s
k = s.index('<span style="color: #e8e8e8">Hero image</span>')
end = s.index('</div>', k) + len('</div>')
row = f'''
<div role="treeitem" aria-selected="true" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 32px; background-color: rgba(47,128,237,0.18); background-image: linear-gradient(#303030,#303030), linear-gradient(#303030,#303030); background-size: 1px 100%, 1px 100%; background-position: 14px 0, 26px 0; background-repeat: no-repeat">
<span style="width: 12px"></span>{icon('box', 14, '#e8e8e8')}<span style="color: #e8e8e8">New badge</span>{icon('free', 12, '#a8a8a8', 1.25, 'Free placement')}<span style="flex: 1"></span><span style="font-size: 11px; color: #a8a8a8">div</span></div>'''
S.s = s[:end] + row + s[end:]

# Properties
pinw = ('<span style="position: relative; width: 56px; height: 56px; flex: none; box-sizing: border-box; background: #2a2a2a; border-radius: 4px">'
        '<span style="position: absolute; left: 18px; top: 18px; width: 20px; height: 20px; box-sizing: border-box; border: 1px dashed #6b6b6b; border-radius: 2px"></span>'
        '<span style="position: absolute; left: 22px; top: 5px; width: 12px; height: 2.5px; border-radius: 1px; background: #2f80ed"></span>'
        '<span style="position: absolute; left: 22px; bottom: 5px; width: 12px; height: 1.5px; border-radius: 1px; background: #6b6b6b"></span>'
        '<span style="position: absolute; top: 22px; left: 5px; width: 1.5px; height: 12px; border-radius: 1px; background: #6b6b6b"></span>'
        '<span style="position: absolute; top: 22px; right: 5px; width: 2.5px; height: 12px; border-radius: 1px; background: #2f80ed"></span>'
        '<span style="position: absolute; left: 26px; top: 26px; width: 4px; height: 4px; border-radius: 2px; background: #6b6b6b"></span></span>')
placement = (seg(['In flow', 'Free', 'Fixed', 'Sticky'], 1)
             + f'<div style="display: flex; gap: 10px; align-items: center">{pinw}<div style="flex: 1; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px">'
             + f('<span style="width: 5px; height: 5px; border-radius: 3px; background: #2f80ed; flex: none"></span><span style="font-size: 11px; color: #939393">Top</span><span style="flex: 1; text-align: right">62</span>')
             + f('<span style="width: 5px; height: 5px; border-radius: 3px; background: #2f80ed; flex: none"></span><span style="font-size: 11px; color: #939393">Right</span><span style="flex: 1; text-align: right">24</span>')
             + f('<span style="font-size: 11px; color: #939393; padding-left: 11px">Bottom</span><span style="flex: 1; text-align: right; color: #939393">auto</span>')
             + f('<span style="font-size: 11px; color: #939393; padding-left: 11px">Left</span><span style="flex: 1; text-align: right; color: #939393">auto</span>')
             + '</div></div>'
             + f'<div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #939393">Positioned relative to <button style="display: flex; align-items: center; gap: 3px; color: #a9c8f7">Hero grid{icon("external", 10, "currentColor", 1.5)}</button></div>')
fill = f('<span style="width: 14px; height: 14px; border-radius: 2px; background: #b5532d; flex: none"></span><span style="flex: 1">brand</span><span style="color: #939393">100%</span>')
S.props(panel(header('box', 'New badge', 'Box', 'div')
              + group('Placement', placement)
              + group('Size', pair(f('<span style="font-size: 11px; color: #939393; padding-left: 11px">W</span><span style="flex: 1; color: #939393">88</span>' + tagc('Fit')),
                                   f('<span style="font-size: 11px; color: #939393; padding-left: 11px">H</span><span style="flex: 1; color: #939393">36</span>' + tagc('Fit'))))
              + group('Fill', fill)
              + more([mp('Spacing', '8 20'), mp('Border', 'radius Pill'), mp('Typography', 'Inter 15 / 600'), mp('Effects'), mp('Transform'), mp('Visibility', 'All sizes'), mp('Accessibility'), mp('Attributes &amp; Custom CSS')])))

S.status(['Page', 'Section · Hero', 'Box · Hero grid', 'Box · New badge'],
         'Hero grid is now the anchor for New badge · <button style="color: #e8e8e8; text-decoration: underline; text-underline-offset: 2px">Undo</button>',
         'x 1236 &#160;y 210', notice=True)
S.save('D10-Free.dc.html')
print('ok')
