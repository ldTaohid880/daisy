from screen import *

S = Screen('Daisy · D-13 Box tool: drawing in flow')
S.remove_h1_overlay()
S.remove_parent_outline()
set_tool(S, 'Box (R)')
scroll(S, 760)
add_footer(S)

PINK = '#c2255c'          # smart-guide colour (snaps, matched spacing)
assert contrast('#ffffff', PINK) >= 4.5
INTER = "'Inter', sans-serif"

# ---------------- canvas: This season (section coordinates) ----------------
GRID_BOTTOM = 96 + 48 + 40 + 380          # 564
COL = (1312 - 2 * 32) // 3                # 416, one grid column
BT = GRID_BOTTOM + 32                     # band top: 32 below the grid = the grid's own gap
BH = 160
S.rep('<div style="padding: 96px 64px; background: #e7d9c7">',
      f'<div style="position: relative; padding: 96px 64px {32 + BH + 96}px; background: #e7d9c7">')  # live reflow

IL = GRID_BOTTOM + 16
pill = lambda t, bg='#246bcb', extra='': f'<span style="height: 21px; padding: 0 8px; display: inline-flex; align-items: center; gap: 6px; border-radius: 11px; background: {bg}; color: #fff; font: 500 13px/1 {INTER}; font-variant-numeric: tabular-nums; white-space: nowrap; {extra}">{t}</span>'

slots = ''.join(  # snap slots: the grid's three columns, ghosted on the new row
    f'<div aria-hidden="true" style="position: absolute; left: {64 + i * (COL + 32)}px; top: {BT}px; width: {COL}px; height: {BH}px; box-sizing: border-box; border: 1.18px dashed rgba(47,128,237,0.45); border-radius: 12px; z-index: 2"></div>'
    for i in (1, 2))

band = f'''<!-- target container -->
<div aria-hidden="true" style="position: absolute; inset: 0; border: 1.18px solid #2f80ed; pointer-events: none; z-index: 2"><span style="position: absolute; left: -1px; top: 4px; height: 21px; padding: 0 5px; display: flex; align-items: center; background: #246bcb; color: #fff; font: 500 13px/1 {INTER}">into This season</span></div>
<!-- insertion line: after Card grid -->
<div aria-hidden="true" style="position: absolute; left: 64px; width: 1312px; top: {IL - 1.2}px; height: 2.35px; background: #2f80ed; z-index: 3"><span style="position: absolute; left: -1.2px; top: -2.35px; width: 2.35px; height: 7px; background: #2f80ed"></span><span style="position: absolute; right: -1.2px; top: -2.35px; width: 2.35px; height: 7px; background: #2f80ed"></span></div>
<!-- snap slots -->
{slots}
<span aria-hidden="true" style="position: absolute; left: {64 + COL + 32 + 12}px; top: {BT + 10}px; font: 500 12px/1 {INTER}; color: #2a5fa8; z-index: 2">2 columns</span>
<span aria-hidden="true" style="position: absolute; left: {64 + 2 * (COL + 32) + 12}px; top: {BT + 10}px; font: 500 12px/1 {INTER}; color: #2a5fa8; z-index: 2">Full width</span>
<!-- smart guide: right edge lines up with Card 1 -->
<div aria-hidden="true" style="position: absolute; left: {64 + COL - 0.6}px; top: {96 + 48 + 40 - 12}px; width: 0; height: {BT + BH - (96 + 48 + 40) + 24}px; border-left: 1.18px dashed {PINK}; z-index: 4"></div>
<div aria-hidden="true" style="position: absolute; left: {64 - 0.6}px; top: {96 + 48 + 40 - 12}px; width: 0; height: {BT + BH - (96 + 48 + 40) + 24}px; border-left: 1.18px dashed {PINK}; z-index: 4"></div>
<!-- matched spacing: 32 = the grid's gap -->
<div aria-hidden="true" style="position: absolute; left: {64 + COL / 2 - 0.6}px; top: {GRID_BOTTOM}px; width: 1.18px; height: 32px; background: {PINK}; z-index: 4"><span style="position: absolute; left: -4px; top: 0; width: 9px; height: 1.18px; background: {PINK}"></span><span style="position: absolute; left: -4px; bottom: 0; width: 9px; height: 1.18px; background: {PINK}"></span></div>
<span aria-hidden="true" style="position: absolute; left: {64 + COL / 2 + 10}px; top: {GRID_BOTTOM + 6}px; z-index: 5">{pill('32 · grid gap', PINK)}</span>
<!-- rubber band: previews the look it will get (Card preset) -->
<div aria-hidden="true" style="position: absolute; left: 64px; top: {BT}px; width: {COL}px; height: {BH}px; box-sizing: border-box; padding: 16px; display: flex; flex-direction: column; gap: 8px; background: rgba(255,255,255,0.88); border-radius: 12px; box-shadow: 0 0 0 1.18px #2f80ed; z-index: 3">
<span style="height: 28px; border-radius: 4px; border: 1.18px dashed #b9c9de"></span><span style="width: 60%; height: 14px; border-radius: 3px; background: #ece6dd"></span>
<span style="position: absolute; left: 50%; transform: translateX(-50%); top: calc(100% + 9px); display: flex; gap: 4px">{pill('416 × 160')}{pill('1 column', '#1d1a16')}</span></div>
<svg aria-hidden="true" width="30" height="30" viewBox="0 0 20 20" style="position: absolute; left: {64 + COL - 15}px; top: {BT + BH - 15}px; overflow: visible; z-index: 6"><path d="M10 1v7M10 12v7M1 10h7M12 10h7" stroke="#1d1a16" stroke-width="1.5"></path><path d="M10 1v7M10 12v7M1 10h7M12 10h7" stroke="#ffffff" stroke-width="0.6"></path><rect x="13" y="13" width="6" height="5" fill="#ffffff" stroke="#1d1a16" stroke-width="1"></rect></svg>
'''
S.rep('<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 40px">',
      band + '<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 40px">')

# ---------------- inset: drawing over elements wraps them ----------------
mini_card = lambda x, hl: f'<span style="position: absolute; left: {x}px; top: 16px; width: 92px; height: 70px; border-radius: 6px; background: #ffffff; {"box-shadow: 0 0 0 1.5px #2f80ed;" if hl else ""}"><span style="position: absolute; left: 8px; right: 8px; top: 8px; height: 36px; border-radius: 3px; background: #d8cbb8"></span><span style="position: absolute; left: 8px; top: 52px; width: 44px; height: 6px; border-radius: 2px; background: #c9bba8"></span></span>'
S.rep('<!-- vertical scroll indicator -->', f'''<!-- INSET: drawing over elements wraps them -->
<div aria-label="Inset: drawing over elements wraps them" style="position: absolute; left: 640px; top: 690px; width: 560px; padding: 12px; box-sizing: border-box; background: #1f1f1f; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 8px 24px rgba(0,0,0,0.45); z-index: 10">
<div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 11px"><span style="font-weight: 600">Inset · draw over elements to wrap them</span><span style="color: #939393">Card grid</span></div>
<div style="position: relative; height: 100px; background: #e7d9c7; border-radius: 2px; overflow: hidden">
{mini_card(18, True)}{mini_card(122, True)}{mini_card(226, False)}
<span style="position: absolute; left: 10px; top: 8px; width: 216px; height: 86px; box-sizing: border-box; border: 1.18px solid #2f80ed; background: rgba(47,128,237,0.10)"></span>
<span style="position: absolute; left: 236px; top: 72px">{pill('Wrap 2 in a box', '#246bcb', 'font-size: 11px; height: 19px')}</span>
<span style="position: absolute; right: 10px; top: 10px; font: 500 10px/1 {INTER}; color: #4a443c">Card 3 stays out</span></div>
<div style="margin-top: 8px; font-size: 11px; line-height: 16px; color: #939393">Let go to wrap Card 1 and Card 2 in a new box that keeps their place in the grid · hold Ctrl to draw on top instead · Ctrl+Alt+G does the same on a selection.</div>
</div>
<!-- vertical scroll indicator -->''')

# ---------------- tool-strip flyout ----------------
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
FLOAT = 'background: #262626; border: 1px solid #454545; box-shadow: 0 8px 24px rgba(0,0,0,0.45);'
P['ellipse'] = ('stroke', 'M8 3c3.6 0 6 2.2 6 5s-2.4 5-6 5-6-2.2-6-5 2.4-5 6-5z')
P['divider'] = ('stroke', 'M2 8h12')
P['band'] = ('stroke', 'M1 5h14M1 11h14M4 8h8')
P['spacer'] = ('stroke', 'M8 2v12M5.5 4.5L8 2l2.5 2.5M5.5 11.5L8 14l2.5-2.5M3 8h2M11 8h2')
P['wrap'] = ('stroke', 'M2 2h12v12H2zM5 5h2.5v6H5zM9 5h2.5v6H9z')
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
item = lambda ic, n, k, d, on=False: (f'<button role="menuitemradio" aria-checked="{str(on).lower()}" style="width: 100%; min-height: 40px; display: flex; align-items: center; gap: 8px; padding: 4px 8px; box-sizing: border-box; border-radius: 3px; {"background: #323232;" if on else ""}">'
                                      f'<span style="width: 12px">{icon("check", 12) if on else ""}</span>{icon(ic, 16, "#e8e8e8" if on else "#a8a8a8")}'
                                      f'<span style="flex: 1; text-align: left"><span style="display: block">{n}</span><span style="display: block; font-size: 10px; line-height: 14px; color: #939393">{d}</span></span><span style="font-size: 11px; color: #939393">{k}</span></button>')
fly = f'''<div role="menu" aria-label="Box tool variants" style="position: absolute; left: 46px; top: 196px; width: 248px; padding: 4px; box-sizing: border-box; border-radius: 4px; {FLOAT} z-index: 20">
{item('box', 'Box', 'R', 'A container · div', True)}{item('ellipse', 'Ellipse', 'Shift+R', 'A fully rounded box')}{item('band', 'Section band', 'Alt+R', 'Full width, a new section')}{item('divider', 'Divider', '', 'A line · hr')}{item('spacer', 'Spacer', '', 'Empty room in a stack or row')}
<div style="height: 1px; background: #3a3a3a; margin: 4px 0"></div>
<div style="padding: 2px 8px 4px; font-size: 10px; line-height: 14px; color: #939393">Hold the tool 300 ms or right-click · the strip shows the last one used</div></div>'''
S.rep('<!-- ═══════════ TOP BAR v3', fly + '\n<!-- ═══════════ TOP BAR v3')

# ---------------- options bar: how drawing behaves (look lives in Properties) ----------------
lab = lambda t: f'<span style="font-size: 11px; color: #939393; padding: 0 4px 0 8px; white-space: nowrap">{t}</span>'
sb = lambda t, on=False: f'<button aria-pressed="{str(on).lower()}" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; white-space: nowrap; {"background: #333333; color: #e8e8e8; font-weight: 500;" if on else "color: #939393;"}">{t}</button>'
tog = lambda ic, t, on: f'<button aria-pressed="{str(on).lower()}" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; white-space: nowrap; {"background: rgba(47,128,237,0.18); color: #a9c8f7;" if on else "color: #a8a8a8;"}">{icon(ic, 13)}{t}</button>'
opts = (capseg([icon('flow', 12) + 'In flow', icon('free', 12) + 'Free'], 0)
        + cap(lab('Width') + sb('Fixed', True) + sb('Fill') + capdiv() + lab('Height') + sb('Fixed', True) + sb('Hug'))
        + cap(tog('wrap', 'Wrap what I draw over', True) + capdiv() + tog('keep', 'Keep tool', False))
        + '<span style="font-size: 11px; color: #939393; white-space: nowrap; padding-left: 4px">Look of the new box: in Properties</span>')
options_left(S, opts)

# ---------------- layers: the box shows where it lands ----------------
set_tree(S, season_tree(extra=[(20, None, 'box', 'Box 1', 'div', False, (14,), '<span style="margin-left: 6px; font-size: 10px; color: #a9c8f7">drawing</span>')]))
S.rep('<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 20px;  background-image: linear-gradient(#262626,#262626); background-size: 1px 100%; background-position: 14px 0; background-repeat: no-repeat;">' + '<span style="width: 12px"></span>' + icon('box', 14, '#a8a8a8'),
      '<div role="treeitem" aria-label="Box 1, being drawn" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 20px; background-color: rgba(47,128,237,0.08); box-shadow: inset 0 2px 0 #2f80ed; background-image: linear-gradient(#262626,#262626); background-size: 1px 100%; background-position: 14px 0; background-repeat: no-repeat; font-style: italic">' + '<span style="width: 12px"></span>' + icon('box', 14, '#a9c8f7'))

# ---------------- properties: the next box ----------------
small = lambda t: f'<span style="font-size: 11px; color: #939393">{t}</span>'
row2 = lambda l, c: f'<div style="display: grid; grid-template-columns: 76px minmax(0, 1fr); gap: 8px; align-items: center"><span style="font-size: 11px; color: #a8a8a8">{l}</span>{c}</div>'
def preset(name, sub, look, on=False):
    return (f'<button aria-pressed="{str(on).lower()}" style="display: flex; flex-direction: column; gap: 5px; padding: 6px; border-radius: 4px; text-align: left; {"background: rgba(47,128,237,0.14); box-shadow: inset 0 0 0 1px #2f80ed;" if on else "background: #262626;"}">'
            f'<span style="height: 34px; border-radius: 3px; background: #e7d9c7; display: flex; align-items: center; justify-content: center"><span style="width: 54px; height: 22px; box-sizing: border-box; {look}"></span></span>'
            f'<span style="font-size: 11px; color: {"#e8e8e8" if on else "#c8c8c8"}; white-space: nowrap">{name}</span><span style="margin-top: -4px; font-size: 10px; color: #939393; white-space: nowrap">{sub}</span></button>')
presets = f'''<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 6px">
{preset('Plain', 'grey · 0', 'background: #d9d9d9')}{preset('Card', 'like Card 1', 'background: #fff; border-radius: 6px', True)}{preset('Outline', 'line · 6', 'border: 1px solid #1d1a16; border-radius: 3px')}
{preset('Tinted', 'sand · 6', 'background: #d8cbb8; border-radius: 3px')}{preset('Pill', 'full round', 'background: #b5532d; border-radius: 11px')}{preset('Ink', 'dark · 6', 'background: #1d1a16; border-radius: 3px')}</div>
<div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #939393">{icon('eyedropper', 12, '#939393')}<span style="flex: 1">Match an element on the page…</span><span>From Halden</span></div>'''

look = (pair(f(swatch('#ffffff', True) + '<span style="flex: 1">white</span><span style="color: #939393">100%</span>'), f(icon('radius', 12, '#939393') + '<span style="flex: 1">12</span><span style="font-size: 10px; color: #939393">px</span>'))
        + pair(f('<span style="font-size: 11px; color: #939393">Border</span><span style="flex: 1; text-align: right">none</span>'), f('<span style="font-size: 11px; color: #939393">Shadow</span><span style="flex: 1; text-align: right">none</span>')))
inside = (row2('Arrange', seg([icon('t-stack', 12) + 'Stack', icon('t-row', 12) + 'Row', icon('t-grid', 12) + 'Grid', 'None'], 0))
          + row2('Space inside', f('<span style="flex: 1">16</span><span style="font-size: 10px; color: #939393">px</span>'))
          + row2('Between', f('<span style="flex: 1">8</span><span style="font-size: 10px; color: #939393">px</span>')))
element = (row2('Name', f('<span style="flex: 1">Box 1</span><span style="font-size: 10px; color: #939393">auto</span>'))
           + row2('Tag', f(f'<span style="flex: 1; font-family: {MONO}">div</span><span style="font-size: 10px; color: #939393">or article · aside</span>' + icon('chev-down', 10, '#939393', 1.5))))
hdr = f'''<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{icon('box', 16, '#a9c8f7')}<span style="flex: 1; font-weight: 500">Next box</span><button style="height: 22px; padding: 0 6px; border-radius: 3px; font-size: 11px; color: #a8a8a8">Reset</button></div>
<div style="padding-left: 24px; font-size: 11px; color: #939393">Look for what you draw · page not selected</div></div>'''
S.props(panel(hdr + group('Start from', presets) + group('Look', look) + group('Inside', inside) + group('Element', element)
              + '<div style="padding: 10px 12px; display: flex; gap: 6px"><button style="height: 24px; padding: 0 10px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #c8c8c8">Save as preset</button><button style="height: 24px; padding: 0 10px; border-radius: 4px; font-size: 11px; color: #a8a8a8">Use for this project</button></div>'))

S.status(['Page', 'Section · This season'], 'Drag to draw · Shift square · Alt places it Free · Ctrl from the centre · Space moves while drawing · Esc cancels', 'x 480 &#160;y 1556')
S.save('D13-BoxDraw.dc.html')
print('ok')
