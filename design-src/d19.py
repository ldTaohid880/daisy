from screen import *
_src = open('/home/claude/ds/layoutadv.py').read()
LA = {}
exec(_src[:_src.index('# ═════ A · ROW')], LA)
L = LA

S = Screen('Daisy · D-19 Measure and Eyedropper')
S.remove_h1_overlay()
S.remove_parent_outline()
set_tool(S, 'Measure (M)')

RED, REDF = '#f85149', '#c9302c'
TT = 62   # Hero text top inside Hero grid (measured)
GAPX = 1312 - 580 - 653.7  # Hero text right edge -> image left = 78
pill = lambda x, y, t: f'<span aria-hidden="true" style="position: absolute; left: {x}px; top: {y}px; transform: translate(-50%, -50%); height: 22px; padding: 0 8px; display: flex; align-items: center; border-radius: 11px; background: {REDF}; color: #fff; font: 500 13px/1 \'Inter\', sans-serif; z-index: 6">{t}</span>'
over = f'''
<!-- Hero text: measured from (selected) -->
<div aria-hidden="true" style="position: absolute; left: -1px; top: {TT - 1}px; width: 655.7px; height: 397px; border: 1.5px solid #2f80ed; z-index: 4"></div>
<!-- Hero image: hovered, measured to -->
<div aria-hidden="true" style="position: absolute; right: -1px; top: -1px; width: 582px; height: 522px; border: 1.18px solid {RED}; z-index: 4"></div>
<!-- horizontal distance -->
<div aria-hidden="true" style="position: absolute; left: 653.7px; width: {GAPX:.1f}px; top: 260px; border-top: 1.5px solid {RED}; z-index: 5"></div>
<div aria-hidden="true" style="position: absolute; left: 653.7px; top: 252px; height: 16px; border-left: 1.5px solid {RED}; z-index: 5"></div>
<div aria-hidden="true" style="position: absolute; left: {653.7 + GAPX:.1f}px; top: 252px; height: 16px; border-left: 1.5px solid {RED}; z-index: 5"></div>
{pill(653.7 + GAPX / 2, 284, f"{GAPX:.0f}")}
<!-- vertical offset of the tops -->
<div aria-hidden="true" style="position: absolute; left: 700px; width: 40px; top: 0; border-top: 1.5px dashed {RED}; z-index: 5"></div>
<div aria-hidden="true" style="position: absolute; left: 620px; width: 40px; top: {TT}px; border-top: 1.5px dashed {RED}; z-index: 5"></div>
<div aria-hidden="true" style="position: absolute; left: 690px; top: 0; height: {TT}px; border-left: 1.5px solid {RED}; z-index: 5"></div>
{pill(690, TT / 2, str(TT))}
<svg aria-hidden="true" width="26" height="26" viewBox="0 0 16 16" style="position: absolute; left: 1010px; top: 300px; overflow: visible; z-index: 7"><path d="M1.5 5h13v6h-13zM4.5 5v2.5M7.5 5v1.5M10.5 5v2.5" fill="#ffffff" stroke="#1d1a16" stroke-width="1.2" stroke-linejoin="round"></path></svg>
'''
S.rep('<div style="display: grid; grid-template-columns: 1.1fr 1fr; gap: 64px; align-items: center">',
      '<div style="position: relative; display: grid; grid-template-columns: 1.1fr 1fr; gap: 64px; align-items: center">')
s = S.s
img_open = '<div style="justify-self: end; width: 580px; height: 520px; border-radius: 12px; overflow: hidden; background: #e6dccd">'
a = s.index(img_open); b = s.index('</svg>\n</div>', a) + len('</svg>\n</div>')
S.s = s[:b] + over + s[b:]

# INSET: Eyedropper loupe over the header button
px = ''
cols = ['#f6f1ea', '#f6f1ea', '#e9d3c6', '#c46a45', '#b5532d', '#b5532d', '#b5532d', '#b5532d', '#b5532d', '#b5532d', '#c46a45']
for r in range(11):
    for c in range(11):
        if r < 2:
            col = '#f6f1ea'
        elif r < 3:
            col = '#e9d3c6' if c > 2 else '#f6f1ea'
        elif c < 2:
            col = '#f6f1ea' if r < 5 else '#e9d3c6'
        elif r in (6, 7) and 4 <= c <= 8:
            col = '#ffffff' if (c + r) % 3 == 0 else '#b5532d'
        else:
            col = '#b5532d'
        px += f'<span style="background: {col}"></span>'
loupe = f'''<div style="position: relative; width: 120px; height: 120px; border-radius: 50%; overflow: hidden; box-shadow: 0 0 0 2px #ffffff, 0 0 0 3px rgba(0,0,0,0.4), 0 8px 20px rgba(0,0,0,0.35)">
<div style="position: absolute; inset: 0; display: grid; grid-template-columns: repeat(11, minmax(0, 1fr)); grid-template-rows: repeat(11, minmax(0, 1fr)); gap: 1px; background: rgba(0,0,0,0.12)">{px}</div>
<span style="position: absolute; left: calc(50% - 6px); top: calc(50% - 6px); width: 12px; height: 12px; box-sizing: border-box; border: 1.5px solid #ffffff; box-shadow: 0 0 0 1px #1d1a16"></span></div>'''
inset = f'''<!-- INSET: Eyedropper -->
<div aria-label="Inset: Eyedropper" style="position: absolute; left: 60px; top: 590px; width: 460px; padding: 12px; box-sizing: border-box; background: #1f1f1f; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 8px 24px rgba(0,0,0,0.45); z-index: 10">
<div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 11px"><span style="font-weight: 600">Inset · Eyedropper over “Book a visit”</span><span style="color: #939393">E</span></div>
<div style="height: 36px; display: flex; align-items: center; gap: 6px; padding: 0 4px; margin-bottom: 10px; background: #1b1b1b; border-radius: 4px">
<span style="font-size: 11px; color: #939393; padding: 0 4px">Apply to</span>{capseg(['Fill', 'Text', 'Border'], 0)}{capseg(['Pixel', 'Element colour'], 0)}</div>
<div style="position: relative; height: 190px; background: #f6f1ea; border-radius: 2px; overflow: hidden">
<span style="position: absolute; right: 40px; top: 28px; height: 44px; padding: 0 24px; display: flex; align-items: center; border-radius: 999px; background: #b5532d; color: #fff; font-size: 16px; font-weight: 500">Book a visit</span>
<div style="position: absolute; left: 150px; top: 18px">{loupe}
<span style="position: absolute; left: 50%; top: calc(100% + 8px); transform: translateX(-50%); height: 22px; padding: 0 8px; display: flex; align-items: center; gap: 6px; border-radius: 4px; background: #262626; border: 1px solid #454545; color: #e8e8e8; font: 500 12px/1 {MONO}; white-space: nowrap"><span style="width: 12px; height: 12px; border-radius: 2px; background: #b5532d"></span>#B5532D · brand</span></div>
<svg aria-hidden="true" width="24" height="24" viewBox="0 0 16 16" style="position: absolute; left: 214px; top: 46px; overflow: visible"><path d="M10.5 2.5l3 3-2 2-3-3zM9 4.5l-6 6V13h2.5l6-6" fill="#ffffff" stroke="#1d1a16" stroke-width="1.2" stroke-linejoin="round"></path></svg>
</div>
<div style="margin-top: 8px; font-size: 11px; color: #939393">10× loupe · click to apply to the selection's fill · Alt+click picks up the whole style · matches a swatch by name</div>
</div>'''
S.rep('<!-- vertical scroll indicator -->', inset + '\n<!-- vertical scroll indicator -->')

opts = (cap('<span style="padding: 0 6px 0 8px; font-size: 11px; color: #939393">Units</span>' + ''.join(f'<button aria-pressed="{str(i == 0).lower()}" style="height: 24px; padding: 0 9px; border-radius: 4px; {"background: #333333; color: #e8e8e8; font-weight: 500;" if i == 0 else "color: #939393;"}">{t}</button>' for i, t in enumerate(['px', 'rem', '%'])))
        + cap('<span style="padding: 0 6px 0 8px; font-size: 11px; color: #939393">From</span>' + ''.join(f'<button aria-pressed="{str(i == 0).lower()}" style="height: 24px; padding: 0 9px; border-radius: 4px; {"background: #333333; color: #e8e8e8; font-weight: 500;" if i == 0 else "color: #939393;"}">{t}</button>' for i, t in enumerate(['Border', 'Content', 'Outside'])))
        + cap(''.join(f'<button aria-pressed="{str(on).lower()}" style="height: 24px; display: flex; align-items: center; padding: 0 8px; border-radius: 4px; white-space: nowrap; {"background: rgba(201,48,44,0.18); color: #ff9b94;" if on else "color: #a8a8a8;"}">{t}</button>' for t, on in [('All four sides', False), ('To parent edges', True), ('Keep pins', True)]))
        + '<span style="font-size: 11px; color: #939393; white-space: nowrap; padding-left: 4px">Values: in Properties</span>')
options_left(S, opts)
set_tree(S, hero_tree('Hero text'))
S.props(panel(header('t-stack', 'Hero text', 'Box', 'div')
              + group('Measure', f'''<div style="display: grid; grid-template-columns: 1fr auto; gap: 6px 12px; font-size: 11px">
<span style="color: #a8a8a8">To Hero image, horizontally</span><span style="color: #ff7b72; font-variant-numeric: tabular-nums">{GAPX:.0f} px</span>
<span style="color: #a8a8a8">Top edges offset</span><span style="color: #ff7b72; font-variant-numeric: tabular-nums">{TT} px</span>
</div>
<div style="font-size: 11px; line-height: 16px; color: #939393">Live while you hover · pins, other screen sizes, why 78 and copy: Advanced</div>''')
              + group('Size', pair(f('<span style="font-size: 11px; color: #939393; padding-left: 11px">W</span><span style="flex: 1; color: #939393">654</span>' + tagc('Fill')), f('<span style="font-size: 11px; color: #939393; padding-left: 11px">H</span><span style="flex: 1; color: #939393">395</span>' + tagc('Fit'))))
              + more([mp('Layout', 'Row ↓ · gap 24'), mp('Placement', 'In flow'), mp('Spacing', '0'), mp('Fill', 'none'), mp('Border', 'none'), mp('Effects'), mp('Visibility', 'All sizes'), mp('Attributes &amp; Custom CSS')])))
exec(open('/home/claude/ds/d19_adv.py').read())
S.status(['Page', 'Section · Hero', 'Box · Hero grid', 'Box · Hero text'], 'Hover another element to measure · Shift+click pins it · Alt with Select does the same · C copies the value', 'x 1010 &#160;y 360')
S.save('D19-Measure.dc.html')
print('ok')
