from screen import *
import math
_src = open('/home/claude/ds/layoutadv.py').read()
LA = {}
exec(_src[:_src.index('# ═════ A · ROW')], LA)
L = LA

S = Screen('Daisy · D-16 Transform and Gradient tools')
S.remove_h1_overlay()
S.remove_parent_outline()
set_tool(S, 'Transform (Q)')

BW, BH, TOP, RIGHT = 88, 36, 62, 24
bx = 1312 - 580 + RIGHT
PUR = '#1a9284'
hpos = ['left: -5.6px; top: -5.6px', 'left: calc(50% - 4.7px); top: -5.6px', 'right: -5.6px; top: -5.6px', 'right: -5.6px; top: calc(50% - 4.7px)',
        'right: -5.6px; bottom: -5.6px', 'left: calc(50% - 4.7px); bottom: -5.6px', 'left: -5.6px; bottom: -5.6px', 'left: -5.6px; top: calc(50% - 4.7px)']
handles = ''.join(f'<span style="position: absolute; {p}; width: 9.4px; height: 9.4px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>' for p in hpos)
R = 66
cx, cy = bx + BW / 2, TOP + BH / 2
ticks = ''
for d in range(-180, 180, 15):
    r1 = R - (8 if d % 45 == 0 else 5)
    t = math.radians(d)
    ticks += f'<line x1="{R + 4 + r1 * math.cos(t):.1f}" y1="{R + 4 + r1 * math.sin(t):.1f}" x2="{R + 4 + R * math.cos(t):.1f}" y2="{R + 4 + R * math.sin(t):.1f}" stroke="#127a70" stroke-width="{1.5 if d % 45 == 0 else 1}"></line>'
c = R + 4
ang = math.radians(-8)
wedge = f'M{c} {c} L{c + R} {c} A {R} {R} 0 0 0 {c + R * math.cos(ang):.1f} {c + R * math.sin(ang):.1f} Z'
dial = (f'<svg aria-hidden="true" width="{2 * c}" height="{2 * c}" viewBox="0 0 {2 * c} {2 * c}" style="position: absolute; left: {cx - c}px; top: {cy - c}px; overflow: visible; z-index: 2">'
        f'<circle cx="{c}" cy="{c}" r="{R}" fill="rgba(26,146,132,0.06)" stroke="#1a9284" stroke-width="1" stroke-dasharray="2 3"></circle>{ticks}'
        f'<path d="{wedge}" fill="rgba(124,78,216,0.28)"></path>'
        f'<line x1="{c}" y1="{c}" x2="{c + R + 10}" y2="{c}" stroke="#8a8a8a" stroke-width="1" stroke-dasharray="3 3"></line>'
        f'<line x1="{c}" y1="{c}" x2="{c + (R + 10) * math.cos(ang):.1f}" y2="{c + (R + 10) * math.sin(ang):.1f}" stroke="#127a70" stroke-width="1.5"></line>'
        f'<text x="{c + R + 14}" y="{c + 4}" font-family="Inter, sans-serif" font-size="11" fill="#5b5b5b">0°</text></svg>')
over = f'''
<!-- ghost of the untransformed box -->
<div aria-hidden="true" style="position: absolute; left: {bx}px; top: {TOP}px; width: {BW}px; height: {BH}px; box-sizing: border-box; border: 1.18px dashed #8a8a8a; border-radius: 999px; z-index: 2"></div>
<!-- the element, rotated -8deg -->
<span style="position: absolute; left: {bx}px; top: {TOP}px; width: {BW}px; height: {BH}px; display: flex; align-items: center; justify-content: center; border-radius: 999px; background: #b5532d; color: #ffffff; font-size: 15px; font-weight: 600; letter-spacing: 0.02em; transform: rotate(-8deg); z-index: 3">New</span>
<!-- rotated bounding box -->
<div aria-hidden="true" style="position: absolute; left: {bx - 1}px; top: {TOP - 1}px; width: {BW + 2}px; height: {BH + 2}px; box-sizing: border-box; border: 1.76px solid #2f80ed; transform: rotate(-8deg); z-index: 4">{handles}
<span style="position: absolute; left: calc(50% - 4px); top: calc(50% - 4px); width: 8px; height: 8px; box-sizing: border-box; border-radius: 50%; background: #fff; border: 1.5px solid {PUR}"></span></div>
<!-- rotation dial around the origin -->
{dial}
<span aria-hidden="true" style="position: absolute; left: {bx + BW / 2 - 70}px; top: {TOP + BH / 2 + 78}px; display: flex; gap: 4px; z-index: 6"><span style="height: 22px; padding: 0 9px; display: flex; align-items: center; border-radius: 11px; background: #246bcb; color: #fff; font: 500 13px/1 'Inter', sans-serif">−8°</span><span style="height: 22px; padding: 0 9px; display: flex; align-items: center; border-radius: 11px; background: rgba(29,26,22,0.88); color: #e8e8e8; font: 500 12px/1 'Inter', sans-serif; white-space: nowrap">Shift snaps to 15°</span></span>
<svg aria-hidden="true" width="26" height="26" viewBox="0 0 16 16" style="position: absolute; left: {bx + BW + 4}px; top: {TOP - 30}px; overflow: visible; z-index: 6"><path d="M3 9a5 5 0 0 1 9-3l1-2v5H8l2-1.5A3 3 0 0 0 5 9z" fill="#1d1a16" stroke="#ffffff" stroke-width="1" stroke-linejoin="round"></path></svg>
'''
S.rep('<div style="display: grid; grid-template-columns: 1.1fr 1fr; gap: 64px; align-items: center">',
      '<div style="position: relative; display: grid; grid-template-columns: 1.1fr 1fr; gap: 64px; align-items: center">')
s = S.s
img_open = '<div style="justify-self: end; width: 580px; height: 520px; border-radius: 12px; overflow: hidden; background: #e6dccd">'
a = s.index(img_open); b = s.index('</svg>\n</div>', a) + len('</svg>\n</div>')
S.s = s[:b] + over + s[b:]

exec(open('/home/claude/ds/d16_grad.py').read())
S.rep('<!-- vertical scroll indicator -->', inset + '\n<!-- vertical scroll indicator -->')

origin9 = '<span style="width: 24px; height: 24px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); padding: 4px; box-sizing: border-box; background: #2a2a2a; border-radius: 3px">' + ''.join(f'<span style="display: flex; align-items: center; justify-content: center"><span style="width: {4 if i == 4 else 2}px; height: {4 if i == 4 else 2}px; border-radius: 50%; background: {PUR if i == 4 else "#6b6b6b"}"></span></span>' for i in range(9)) + '</span>'
P['flip-h'] = ('stroke', 'M8 2v12M6 4L2 12h4zM10 4l4 8h-4z')
P['flip-v'] = ('stroke', 'M2 8h12M4 6l8-4v4zM4 10l8 4v-4z')
tog = lambda t, on: f'<button aria-pressed="{str(on).lower()}" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; white-space: nowrap; {"background: rgba(26,146,132,0.18); color: #9fe5dc;" if on else "color: #a8a8a8;"}">{t}</button>'
olab = lambda t: f'<span style="font-size: 11px; color: #939393; padding: 0 4px 0 8px; white-space: nowrap">{t}</span>'
opts = (cap(olab('Corners drag to') + ''.join(f'<button aria-pressed="{str(i == 0).lower()}" style="height: 24px; display: flex; align-items: center; padding: 0 8px; border-radius: 4px; {"background: #333333; color: #e8e8e8; font-weight: 500;" if i == 0 else "color: #939393;"}">{t}</button>' for i, t in enumerate(['Rotate', 'Scale', 'Skew', 'Move'])))
        + cap(tog('Angle snap 15°', True) + tog('Show dial', True) + tog('Origin draggable', True))
        + cap(f'<button aria-label="Flip horizontally" style="width: 26px; height: 24px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon("flip-h", 14)}</button><button aria-label="Flip vertically" style="width: 26px; height: 24px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon("flip-v", 14)}</button>' + capdiv() + '<button style="height: 24px; padding: 0 8px; border-radius: 4px; color: #a8a8a8; white-space: nowrap">Reset all</button>')
        + '<span style="font-size: 11px; color: #939393; white-space: nowrap; padding-left: 4px">Values: in Properties</span>')
options_left(S, opts)
set_tree(S, hero_tree('New badge', ('Hero image', [(32, None, 'box', 'New badge', 'div', True, (14, 26), icon('free', 12, '#a8a8a8', 1.25, 'Free placement'))])))
def tr_group(body):
    t = f'''<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">Transform</span>
<button aria-label="Transform · Advanced" aria-expanded="true" aria-haspopup="dialog" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; background: #3a3a3a; color: #e8e8e8; box-shadow: 0 0 0 1px #2f80ed">{icon("sliders", 14)}</button></div>'''
    return f'<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">{t}{body}</div><div style="height: 1px; background: #303030"></div>'
S.props(panel(header('box', 'New badge', 'Box', 'div')
              + tr_group(pair(f(DOT + '<span style="font-size: 11px; color: #939393">Rotate</span><span style="flex: 1; text-align: right">−8</span><span style="font-size: 10px; color: #939393">°</span>', 'box-shadow: inset 0 0 0 1px #2f80ed'),
                                        f('<span style="font-size: 11px; color: #939393; padding-left: 11px">Scale</span><span style="flex: 1; text-align: right; color: #939393">100</span><span style="font-size: 10px; color: #939393">%</span>'))
                      + pair(f('<span style="font-size: 11px; color: #939393; padding-left: 11px">Move X</span><span style="flex: 1; text-align: right; color: #939393">0</span>'), f('<span style="font-size: 11px; color: #939393; padding-left: 11px">Y</span><span style="flex: 1; text-align: right; color: #939393">0</span>'))
                      + '<div style="font-size: 10px; line-height: 14px; color: #939393">Origin, separate scale, skew, 3D and order: Advanced</div>')
              + group('Placement', seg(['In flow', 'Free', 'Fixed', 'Sticky'], 1))
              + more([mp('Size', '88 × 36 Fit'), mp('Fill', 'brand'), mp('Border', 'radius Pill'), mp('Effects'), mp('Visibility', 'All sizes'), mp('Transition &amp; Animation'), mp('Accessibility'), mp('Attributes &amp; Custom CSS')])))
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
sw = lambda on, label: f'<button role="switch" aria-checked="{str(on).lower()}" aria-label="{label}" style="position: relative; width: 28px; height: 16px; border-radius: 8px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {"#fff" if on else "#a8a8a8"}"></span></button>'
swrow = lambda l, on, label: f'<div style="display: flex; align-items: center; justify-content: space-between">{l}{sw(on, label)}</div>'
fn = lambda name, val, on=False: (f'<div style="height: 28px; display: flex; align-items: center; gap: 6px; padding: 0 6px; border-radius: 3px; {"background: rgba(26,146,132,0.14); box-shadow: inset 0 0 0 1px #1a9284;" if on else "background: #2a2a2a;"}">'
                                  f'<span style="color: #6b6b6b">{icon("grip", 12, "#6b6b6b")}</span><span style="font-family: {MONO}; font-size: 11px; color: #9fe5dc">{name}</span><span style="flex: 1; text-align: right; font-family: {MONO}; font-size: 11px">{val}</span>'
                                  f'<button aria-label="Remove {name}" style="width: 18px; height: 18px; display: flex; align-items: center; justify-content: center; color: #939393">{icon("close", 10)}</button></div>')
o9 = '<span style="width: 60px; height: 60px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); padding: 6px; box-sizing: border-box; background: #2a2a2a; border-radius: 4px">' + ''.join(f'<span style="display: flex; align-items: center; justify-content: center"><span style="width: {7 if i == 4 else 4}px; height: {7 if i == 4 else 4}px; border-radius: 50%; background: {"#1a9284" if i == 4 else "#6b6b6b"}"></span></span>' for i in range(9)) + '</span>'
pop = f'''<!-- POPOVER: Transform · Advanced, anchored to Properties › Transform -->
<section role="dialog" aria-label="Transform advanced · New badge" style="position: absolute; left: 1282px; top: 136px; width: 328px; box-sizing: border-box; padding: 0 12px 12px; display: flex; flex-direction: column; gap: 9px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); font-variant-numeric: tabular-nums; z-index: 30">
<span aria-hidden="true" style="position: absolute; right: -6px; top: 14px; width: 10px; height: 10px; background: #262626; border-right: 1px solid #454545; border-top: 1px solid #454545; transform: rotate(45deg)"></span>
<div style="height: 40px; margin: 0 -12px; padding: 0 8px 0 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a">
<span style="font-weight: 600">Transform · Advanced</span><span style="flex: 1; font-size: 11px; color: #939393">New badge · div</span>
<button aria-label="Pin open" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #939393">{icon("keep", 14)}</button>
<button aria-label="Close" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon("close", 14)}</button></div>
{L['lab']('Origin', 'transform-origin')}
<div style="display: grid; grid-template-columns: 60px minmax(0, 1fr); gap: 10px; align-items: center">{o9}<div style="display: flex; flex-direction: column; gap: 6px">{L['fieldv']('X', '50', '%')}{L['fieldv']('Y', '50', '%')}</div></div>
{L['lab']('Scale', 'scale')}
{L['pair'](L['fieldv']('X', '100', '%'), L['fieldv']('Y', '100', '%'), True)}
{L['lab']('Skew', 'skew()')}
{L['pair'](L['fieldv']('X', '0', '°'), L['fieldv']('Y', '0', '°'))}
<div style="height: 1px; background: #333333"></div>
{swrow(L['lab']('3D', 'rotateX · rotateY · perspective'), False, '3D')}
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 6px; opacity: 0.55">{L['fieldv']('X', '0', '°')}{L['fieldv']('Y', '0', '°')}{L['fieldv']('Persp.', '800', '')}</div>
<div style="height: 1px; background: #333333"></div>
<div style="display: flex; align-items: center; justify-content: space-between">{L['lab']('Order', 'transform list')}<button style="height: 22px; padding: 0 6px; border-radius: 3px; font-size: 11px; color: #a8a8a8">+ Add</button></div>
{fn('rotate', '-8deg', True)}{fn('translate', '0 0')}
<div style="margin-top: -3px; font-size: 10px; line-height: 14px; color: #939393">Drag to reorder: rotate then move is not the same as move then rotate.</div>
{swrow(L['lab']('Use separate properties', 'rotate · scale · translate'), True, 'Individual properties')}
{L['css_line']('rotate: -8deg;\ntransform-origin: 50% 50%;')}
</section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', pop + '\n<!-- ═══════════ TOP BAR v3')
S.status(['Page', 'Section · Hero', 'Box · Hero grid', 'Box · New badge'], 'Drag outside a corner to rotate · Shift snaps to 15° · Alt rotates around the opposite corner · drag the origin to move it · Esc cancels', 'x 838 &#160;y 196')
S.save('D16-Transform.dc.html')
print('ok')
