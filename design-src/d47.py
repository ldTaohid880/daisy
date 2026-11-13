from screen import *
_src = open('/home/claude/ds/layoutadv.py').read(); LA = {}; exec(_src[:_src.index('# ═════ A · ROW')], LA); L = LA
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
P['grip2'] = ('fill', 'M6 4h1.5v1.5H6zM8.5 4H10v1.5H8.5zM6 7.25h1.5v1.5H6zM8.5 7.25H10v1.5H8.5zM6 10.5h1.5V12H6zM8.5 10.5H10V12H8.5z')
S = Screen('Daisy · D-47 Fill, Border and Effects')
S.remove_h1_overlay(); S.remove_parent_outline(); S.unselect_h1_row()
scroll(S, 700, 330)
SH = '0 4px 12px rgba(29,26,22,0.10), 0 1px 2px rgba(29,26,22,0.08)'

# ── canvas: Card 1 selected, with its fill, border and shadow ──
hpos = ['left: -5.6px; top: -5.6px', 'right: -5.6px; top: -5.6px', 'right: -5.6px; bottom: -5.6px', 'left: -5.6px; bottom: -5.6px', 'left: calc(50% - 4.7px); top: -5.6px', 'left: calc(50% - 4.7px); bottom: -5.6px', 'left: -5.6px; top: calc(50% - 4.7px)', 'right: -5.6px; top: calc(50% - 4.7px)']
handles = ''.join(f'<span style="position: absolute; {p}; width: 9.4px; height: 9.4px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>' for p in hpos)
old = '<div style="background: #ffffff; border-radius: 12px; padding: 16px; display: flex; flex-direction: column; gap: 8px">'
assert S.s.count(old) == 3
S.s = S.s.replace(old, f'<div style="position: relative; background: linear-gradient(180deg, rgba(246,241,234,0.6), rgba(246,241,234,0) 45%), #ffffff; border: 1px solid #d9cbb7; border-radius: 12px; padding: 16px; display: flex; flex-direction: column; gap: 8px; box-shadow: {SH}">'
                  f'<span aria-hidden="true" style="position: absolute; inset: -2px; border: 1.76px solid #2f80ed; pointer-events: none">{handles}<span style="position: absolute; left: -1.76px; bottom: calc(100% + 3px); height: 21px; padding: 0 6px; display: flex; align-items: center; background: #246bcb; color: #fff; font: 500 13px/1 \'Inter\', sans-serif; white-space: nowrap">Card 1 · div</span></span>', 1)
S.s = S.s.replace(old, f'<div style="background: #ffffff; border: 1px solid #d9cbb7; border-radius: 12px; padding: 16px; display: flex; flex-direction: column; gap: 8px; box-shadow: {SH}">')
S.options('0', '0', '419', 'Fill', '412', 'Fit')
set_tree(S, season_tree(sel=('Card 1',)))

# ── Properties: Fill, Border, Effects open ──
sm = lambda t, c='#939393': f'<span style="font-size: 11px; color: {c}">{t}</span>'
ib = lambda ic, lab, c='#a8a8a8': f'<button aria-label="{lab}" style="width: 20px; height: 20px; display: flex; align-items: center; justify-content: center; color: {c}">{icon(ic, 12)}</button>'
def layer(prev, name, val, on=True, sel=False, token=False):
    return (f'<div style="height: 28px; display: flex; align-items: center; gap: 6px; padding: 0 2px 0 0; border-radius: 2px; {"background: #3a3a3a; box-shadow: inset 0 0 0 1px #2f80ed;" if sel else ""}">'
            f'<span style="color: #6b6b6b">{icon("grip2", 12, "#6b6b6b")}</span>{prev}<span style="flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; {"" if on else "color: #6b6b6b;"}">{name}</span>'
            f'{sm(val)}{ib("eye" if on else "eye-off", "Show or hide")}{ib("minus", "Remove")}</div>')
grad = '<span style="width: 16px; height: 16px; flex: none; border-radius: 2px; background: linear-gradient(180deg, #f6f1ea, #ffffff); box-shadow: inset 0 0 0 1px rgba(255,255,255,0.15)"></span>'
add = lambda t: f'<button style="align-self: flex-start; height: 22px; display: flex; align-items: center; gap: 6px; padding: 0 2px; font-size: 11px; color: #a8a8a8">{icon("plus", 11, "currentColor", 1.75)}{t}</button>'
fill = (layer(grad, 'Linear · sand → clear', '60%') + layer(swatch('#ffffff', True), 'white', '100%', token=True)
        + add('Add a fill layer') + '<div style="font-size: 10px; line-height: 14px; color: #939393">Top layer paints first · drag to reorder</div>')

sides = f'''<div style="display: grid; grid-template-columns: 56px minmax(0, 1fr); gap: 10px; align-items: center">
<div title="Click a side to edit only that side" style="position: relative; width: 56px; height: 44px; border-radius: 3px; background: #262626">
<span style="position: absolute; left: 10px; right: 10px; top: 8px; height: 2px; background: #a9c8f7"></span><span style="position: absolute; left: 10px; right: 10px; bottom: 8px; height: 2px; background: #a9c8f7"></span>
<span style="position: absolute; top: 8px; bottom: 8px; left: 10px; width: 2px; background: #a9c8f7"></span><span style="position: absolute; top: 8px; bottom: 8px; right: 10px; width: 2px; background: #a9c8f7"></span></div>
<div style="display: flex; flex-direction: column; gap: 6px">{pair(f('<span style="flex: 1">1</span><span style="font-size: 10px; color: #939393">px</span>'), f('<span style="flex: 1">Solid</span>' + icon('chev-down', 10, '#939393', 1.5)))}
{f(DOT + swatch('#d9cbb7') + '<span style="flex: 1">clay-line</span><span style="color: #939393">100%</span>')}</div></div>'''
corners = f(icon('radius', 12, '#939393') + '<span style="flex: 1">12</span>' + '<span style="height: 16px; display: flex; align-items: center; gap: 4px; padding: 0 5px; border-radius: 3px; background: #333333; font-size: 10px; color: #c8c8c8">' + icon('link', 10, '#a8a8a8') + 'radius-md</span>' + icon('corners', 12, '#939393'))
border = (sm('All sides') + sides + '<div style="display: grid; grid-template-columns: 56px minmax(0, 1fr); gap: 10px; align-items: center">' + sm('Corners') + corners + '</div>'
          + '<div style="display: grid; grid-template-columns: 56px minmax(0, 1fr); gap: 10px; align-items: center">' + sm('Outline') + f('<span style="flex: 1; color: #939393">Focus ring only</span>' + icon('chev-down', 10, '#939393', 1.5)) + '</div>')

shadow_prev = '<span style="width: 16px; height: 16px; flex: none; border-radius: 3px; background: #3a3a3a; box-shadow: 0 2px 4px rgba(0,0,0,0.6)"></span>'
blur_prev = '<span style="width: 16px; height: 16px; flex: none; border-radius: 3px; background: radial-gradient(#a8a8a8, transparent 70%)"></span>'
effects = (layer(shadow_prev, 'Drop shadow · shadow-2', '', sel=True) + layer(blur_prev, 'Background blur', '8', on=False)
           + add('Add an effect') + pair(f('<span style="font-size: 11px; color: #939393">Opacity</span><span style="flex: 1; text-align: right">100</span><span style="font-size: 10px; color: #939393">%</span>'), f('<span style="flex: 1">Normal</span><span style="font-size: 10px; color: #939393">blend</span>' + icon('chev-down', 10, '#939393', 1.5))))
hdr = f'''<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{icon('t-stack', 16, '#a8a8a8')}<span style="flex: 1; font-weight: 500">Card 1</span><button style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 6px; color: #a8a8a8">Normal{icon('chev-down', 10, 'currentColor', 1.5)}</button></div>
<div style="padding-left: 24px; font-size: 11px; color: #a8a8a8">Box · <span style="font-family: {MONO}; color: #939393">div.card</span> · same as Card 2, Card 3</div></div>'''
grp = lambda t, body, pressed=False: f'''<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">
<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">{t}</span><button aria-label="{t} · Advanced" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; {"background: #3a3a3a; box-shadow: 0 0 0 1px #2f80ed; color: #e8e8e8;" if pressed else "color: #939393;"}">{icon("sliders", 14)}</button></div>
{body}</div><div style="height: 1px; background: #303030"></div>'''
S.props(panel(hdr + grp('Fill', fill) + grp('Border', border) + grp('Effects', effects, True)
              + more([mp('Size', 'Fill × Fit'), mp('Layout', 'Stack'), mp('Spacing', '16'), mp('Transform')])))

# ── Effects · Advanced popover: the shadow editor ──
num = lambda l, v, u='': f('<span style="font-size: 11px; color: #939393; width: 30px">' + l + '</span><span style="flex: 1">' + v + '</span>' + (f'<span style="font-size: 10px; color: #939393">{u}</span>' if u else ''))
lab = lambda t: f'<span style="font-size: 11px; color: #a8a8a8">{t}</span>'
seg_ = lambda items, sel: '<div style="display: grid; grid-template-columns: repeat(' + str(len(items)) + ', minmax(0, 1fr)); gap: 2px; padding: 2px; background: #1f1f1f; border-radius: 4px; font-size: 11px">' + ''.join(f'<button style="height: 22px; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #a8a8a8;"}">{t}</button>' for i, t in enumerate(items)) + '</div>'
tokens = '<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px">' + ''.join(
    f'<button style="height: 46px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; border-radius: 4px; background: #e7d9c7; {"box-shadow: inset 0 0 0 1.5px #2f80ed;" if n == "2" else ""}"><span style="width: 26px; height: 16px; border-radius: 3px; background: #fff; box-shadow: {s}"></span><span style="font-size: 10px; color: #4a443c">{"none" if n == "0" else "shadow-" + n}</span></button>'
    for n, s in [('0', 'none'), ('1', '0 1px 2px rgba(29,26,22,0.15)'), ('2', SH), ('3', '0 12px 28px rgba(29,26,22,0.18)')]) + '</div>'
layers2 = (f'<div style="display: flex; flex-direction: column; gap: 4px">'
           + f'<div style="display: flex; align-items: center; gap: 6px">{lab("Layer 1")}<span style="flex: 1"></span>{sm("of 2")}</div>'
           + f'<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px">{num("X", "0")}{num("Y", "4")}{num("Blur", "12")}{num("Grow", "0")}</div>'
           + f(DOT + swatch('#1d1a16') + '<span style="flex: 1">ink</span><span style="color: #939393">10%</span>') + '</div>')
pop = f'''<!-- POPOVER: Effects · Advanced (shadow) -->
<section role="dialog" aria-label="Effects advanced · Card 1" style="position: absolute; left: 1282px; top: 470px; width: 328px; box-sizing: border-box; padding: 0 12px 12px; display: flex; flex-direction: column; gap: 10px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); font-variant-numeric: tabular-nums; z-index: 30">
<span aria-hidden="true" style="position: absolute; right: -6px; top: 70px; width: 10px; height: 10px; background: #262626; border-right: 1px solid #454545; border-top: 1px solid #454545; transform: rotate(45deg)"></span>
<div style="height: 40px; margin: 0 -12px; padding: 0 8px 0 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a">
<span style="font-weight: 600">Effects · Advanced</span><span style="flex: 1; font-size: 11px; color: #939393">Drop shadow</span>
<button aria-label="Pin open" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; color: #939393">{icon("keep", 14)}</button><button aria-label="Close" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon("close", 14)}</button></div>
{seg_(['Drop', 'Inner'], 0)}
{lab('From the design system')}{tokens}
<div style="display: flex; align-items: center; gap: 8px; font-size: 11px"><span style="color: #a8a8a8">Linked to</span><b style="font-weight: 600">shadow-2</b><span style="flex: 1"></span><button style="font-size: 11px; color: #a9c8f7">Unlink to edit</button></div>
<div style="padding: 10px; border-radius: 4px; background: #2a2a2a; opacity: 0.6">{layers2}</div>
<div style="font-size: 10px; line-height: 14px; color: #939393">Values come from shadow-2 (2 layers). Unlink to change them for this card only, or edit the token in Design system.</div>
{L['css_line']('box-shadow: var(--shadow-2);')}
</section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', pop + '\n<!-- ═══════════ TOP BAR v3')
S.status(['Page', 'Section · This season', 'Grid · Card grid', 'Box · Card 1'], 'Card 2 and Card 3 share the class .card · edits apply to all three', 'x 300 &#160;y 1180')
S.save('D47-FillBorderEffects.dc.html')
print('ok')
