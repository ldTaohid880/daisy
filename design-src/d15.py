from screen import *
_src = open('/home/claude/ds/layoutadv.py').read()
LA = {}
exec(_src[:_src.index('# ═════ A · ROW')], LA)
L = LA

S = Screen('Daisy · D-15 Spacing tool on the Hero section')
S.remove_h1_overlay()
S.remove_parent_outline()
set_tool(S, 'Spacing (P)')

G, GE, OR = 'rgba(63,185,80,0.30)', '#3fb950', 'rgba(240,136,62,0.40)'
lab = lambda x, y, t, col='#1d5b27': f'<span aria-hidden="true" style="position: absolute; left: {x}; top: {y}; transform: translate(-50%, -50%); font: 600 15px/1 \'Inter\', sans-serif; color: {col}; z-index: 4">{t}</span>'
bands = f'''<!-- Spacing tool: space inside the Hero section -->
<div aria-hidden="true" style="position: absolute; left: 0; right: 0; top: 0; height: 72px; background: rgba(63,185,80,0.42); box-shadow: inset 0 -2.35px 0 #2f80ed; z-index: 3"></div>
<div aria-hidden="true" style="position: absolute; left: 0; width: 64px; top: 72px; bottom: 96px; background: {G}; z-index: 3"></div>
<div aria-hidden="true" style="position: absolute; right: 0; width: 64px; top: 72px; bottom: 96px; background: {G}; z-index: 3"></div>
<div aria-hidden="true" style="position: absolute; left: 0; right: 0; bottom: 0; height: 96px; background: {G}; z-index: 3"></div>
<div aria-hidden="true" style="position: absolute; left: 64px; right: 64px; top: 72px; bottom: 96px; box-shadow: 0 0 0 1.18px {GE}; z-index: 3"></div>
{lab('50%', '36px', '72')}{lab('32px', '50%', '64')}{lab('calc(100% - 32px)', '50%', '64')}{lab('50%', 'calc(100% - 48px)', '96')}
<span aria-hidden="true" style="position: absolute; left: calc(50% + 40px); top: 60px; height: 22px; padding: 0 8px; display: flex; align-items: center; border-radius: 11px; background: #237a33; color: #fff; font: 500 13px/1 'Inter', sans-serif; z-index: 5">72 · 3xl</span>
<span aria-hidden="true" style="position: absolute; left: calc(50% + 40px); top: 90px; display: flex; align-items: center; gap: 2px; padding: 3px; border-radius: 13px; background: rgba(29,26,22,0.88); font: 500 12px/1 'Inter', sans-serif; color: #c8c8c8; white-space: nowrap; z-index: 5"><span style="padding: 4px 7px">48 xl</span><span style="padding: 4px 7px">64 2xl</span><span style="padding: 4px 8px; border-radius: 10px; background: #237a33; color: #fff">72 3xl</span><span style="padding: 4px 7px">96 4xl</span><span style="padding: 4px 7px 4px 4px; color: #939393">Halden spacing</span></span>
<svg aria-hidden="true" width="28" height="28" viewBox="0 0 20 20" style="position: absolute; left: calc(50% + 4px); top: 58px; overflow: visible; z-index: 6"><path d="M10 2l4 4h-2.5v8H14l-4 4-4-4h2.5V6H6z" fill="#1d1a16" stroke="#ffffff" stroke-width="1" stroke-linejoin="round"></path></svg>
<div aria-hidden="true" style="position: absolute; inset: 0; box-shadow: inset 0 0 0 1.18px #2f80ed; z-index: 3"><span style="position: absolute; left: 8px; top: 8px; height: 21px; padding: 0 5px; display: flex; align-items: center; background: #246bcb; color: #fff; font: 500 13px/1 'Inter', sans-serif">Section · Hero</span></div>
'''
S.rep('<div style="padding: 72px 64px 96px">', '<div style="position: relative; padding: 72px 64px 96px">' + bands)
assert contrast('#ffffff', '#237a33') >= 4.5
# the h1's space outside: zero, shown as a grab strip
S.rep('<h1 style="margin: 0; font-family: \'Fraunces\', serif; font-size: 64px; line-height: 1.05; font-weight: 600; color: #1d1a16">Hand-thrown ceramics for everyday tables</h1>',
      '<h1 style="margin: 0; font-family: \'Fraunces\', serif; font-size: 64px; line-height: 1.05; font-weight: 600; color: #1d1a16">Hand-thrown ceramics for everyday tables</h1>'
      f'<span aria-hidden="true" style="position: absolute; left: 0; right: 0; bottom: -5px; height: 5px; background: {OR}; box-shadow: inset 0 0 0 1px #f0883e"></span>'
      '<span aria-hidden="true" style="position: absolute; right: -54px; bottom: -14px; height: 18px; padding: 0 6px; display: flex; align-items: center; border-radius: 9px; background: #a8511a; color: #fff; font: 500 11px/1 \'Inter\', sans-serif">outside 0</span>')

tog = lambda t, on, c='rgba(63,185,80,0.22)', tc='#8ddb98': f'<button aria-pressed="{str(on).lower()}" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; white-space: nowrap; {f"background: {c}; color: {tc};" if on else "color: #a8a8a8;"}">{t}</button>'
olab = lambda t: f'<span style="font-size: 11px; color: #939393; padding: 0 4px 0 8px; white-space: nowrap">{t}</span>'
sb = lambda t, on=False: f'<button aria-pressed="{str(on).lower()}" style="height: 24px; display: flex; align-items: center; padding: 0 8px; border-radius: 4px; white-space: nowrap; {"background: #333333; color: #e8e8e8; font-weight: 500;" if on else "color: #939393;"}">{t}</button>'
opts = (cap(olab('Show') + tog('Inside', True) + tog('Outside', True, 'rgba(240,136,62,0.22)', '#f5b183') + tog('Between', False))
        + cap(olab('A drag changes') + sb('One side', True) + sb('Opposite') + sb('All four'))
        + cap(tog('Snap to Halden spacing', True, 'rgba(47,128,237,0.18)', '#a9c8f7') + capdiv() + tog('Allow negative', False))
        + '<span style="font-size: 11px; color: #939393; white-space: nowrap; padding-left: 4px">Values: in Properties</span>')
options_left(S, opts)
set_tree(S, hero_tree('Hero'))

diag = f'''<div style="position: relative; height: 112px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; background: rgba(240,136,62,0.10); box-shadow: inset 0 0 0 1px rgba(240,136,62,0.45); border-radius: 4px">
<span style="position: absolute; left: 6px; top: 3px; font-size: 10px; color: #939393">Outside</span>
<span style="position: absolute; top: 3px; left: 0; right: 0; text-align: center; font-size: 11px; color: #939393">0</span><span style="position: absolute; bottom: 3px; left: 0; right: 0; text-align: center; font-size: 11px; color: #939393">0</span>
<span style="position: absolute; left: 10px; top: 48px; font-size: 11px; color: #939393">0</span><span style="position: absolute; right: 10px; top: 48px; font-size: 11px; color: #939393">0</span>
<span style="position: relative; width: 190px; height: 64px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; background: rgba(63,185,80,0.12); box-shadow: inset 0 0 0 1px rgba(63,185,80,0.5); border-radius: 3px">
<span style="position: absolute; left: 5px; top: 2px; font-size: 10px; color: #939393">Inside</span>
<span style="position: absolute; top: 1px; left: calc(50% - 15px); width: 30px; height: 16px; display: flex; align-items: center; justify-content: center; border-radius: 2px; background: #2a2a2a; box-shadow: inset 0 0 0 1px #2f80ed; font-size: 11px">72</span>
<span style="position: absolute; bottom: 2px; left: 0; right: 0; text-align: center; font-size: 11px">96</span>
<span style="position: absolute; left: 6px; top: 24px; font-size: 11px">64</span><span style="position: absolute; right: 6px; top: 24px; font-size: 11px">64</span>
<span style="height: 18px; padding: 0 6px; display: flex; align-items: center; border-radius: 2px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">1440 × 688</span></span></div>'''
def sp_group(body):
    t = f'''<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">Spacing</span>
<button aria-label="Spacing · Advanced" aria-expanded="true" aria-haspopup="dialog" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; background: #3a3a3a; color: #e8e8e8; box-shadow: 0 0 0 1px #2f80ed">{icon("sliders", 14)}</button></div>'''
    return f'<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">{t}{body}</div><div style="height: 1px; background: #303030"></div>'
S.props(panel(header('t-section', 'Hero', 'Section', 'section')
              + sp_group(diag + f'<div style="display: flex; align-items: center; justify-content: space-between; font-size: 11px; color: #939393"><span>Centre horizontally</span><button role="switch" aria-checked="false" aria-label="Centre horizontally" style="position: relative; width: 28px; height: 16px; border-radius: 8px; background: #454545"><span style="position: absolute; left: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: #a8a8a8"></span></button></div>')
              + group('Size', pair(f('<span style="font-size: 11px; color: #939393; padding-left: 11px">W</span><span style="flex: 1; color: #939393">1440</span>' + tagc('Fill')), f('<span style="font-size: 11px; color: #939393; padding-left: 11px">H</span><span style="flex: 1; color: #939393">688</span>' + tagc('Fit'))))
              + more([mp('Layout', 'Stack'), mp('Placement', 'In flow'), mp('Fill', 'none'), mp('Border', 'none'), mp('Effects'), mp('Visibility', 'All sizes'), mp('Accessibility', 'Landmark'), mp('Attributes &amp; Custom CSS')])))
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
tok = lambda t, on=False: f'<span style="height: 18px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; font-size: 10px; {"background: rgba(47,128,237,0.22); color: #a9c8f7;" if on else "background: #333333; color: #a8a8a8;"}">{t}</span>'
def siderow(name, v, t, focus=False):
    ring = 'box-shadow: inset 0 0 0 1px #2f80ed;' if focus else ''
    return (f'<div style="display: grid; grid-template-columns: 52px minmax(0, 1fr) 46px 44px; gap: 6px; align-items: center"><span style="font-size: 11px; color: #a8a8a8">{name}</span>'
            f'<label style="height: 24px; display: flex; align-items: center; padding: 0 6px; background: #2a2a2a; border-radius: 2px; {ring}"><span style="flex: 1; text-align: right">{v}</span></label>'
            f'<button style="height: 24px; display: flex; align-items: center; justify-content: space-between; padding: 0 5px 0 7px; background: #2a2a2a; border-radius: 2px; font-size: 11px; color: #a8a8a8">px{icon("chev-down", 10, "#939393", 1.5)}</button>{tok(t, focus)}</div>')
sw = lambda on, label: f'<button role="switch" aria-checked="{str(on).lower()}" aria-label="{label}" style="position: relative; width: 28px; height: 16px; border-radius: 8px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {"#fff" if on else "#a8a8a8"}"></span></button>'
swrow = lambda lab_html, on, label: f'<div style="display: flex; align-items: center; justify-content: space-between">{lab_html}{sw(on, label)}</div>'
pop = f'''<!-- POPOVER: Spacing · Advanced, anchored to Properties › Spacing -->
<section role="dialog" aria-label="Spacing advanced · Hero" style="position: absolute; left: 1282px; top: 136px; width: 328px; box-sizing: border-box; padding: 0 12px 12px; display: flex; flex-direction: column; gap: 9px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); font-variant-numeric: tabular-nums; z-index: 30">
<span aria-hidden="true" style="position: absolute; right: -6px; top: 14px; width: 10px; height: 10px; background: #262626; border-right: 1px solid #454545; border-top: 1px solid #454545; transform: rotate(45deg)"></span>
<div style="height: 40px; margin: 0 -12px; padding: 0 8px 0 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a">
<span style="font-weight: 600">Spacing · Advanced</span><span style="flex: 1; font-size: 11px; color: #939393">Hero · section</span>
<button aria-label="Pin open" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #939393">{icon("keep", 14)}</button>
<button aria-label="Close" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon("close", 14)}</button></div>
<div style="display: flex; align-items: center; justify-content: space-between">{L['lab']('Inside', 'padding')}<span style="font-size: 10px; color: #939393">value · unit · token</span></div>
{L['seg'](['Each side', 'Pairs', 'All'], 0)}
{siderow('Top', '72', '3xl', True)}{siderow('Right', '64', '2xl')}{siderow('Bottom', '96', '4xl')}{siderow('Left', '64', '2xl')}
<div style="margin-top: -3px; font-size: 10px; color: #8ddb98">Top follows your drag on the canvas</div>
<div style="height: 1px; background: #333333"></div>
<div style="display: flex; align-items: center; justify-content: space-between">{L['lab']('Outside', 'margin')}<span style="font-size: 10px; color: #939393">All sides · linked</span></div>
{L['fieldv']('All', '0', 'px')}
<div style="height: 1px; background: #333333"></div>
{swrow(L['lab']('Shrink on small screens', 'clamp()'), True, 'Fluid spacing')}
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px">{L['fieldv']('Mobile', '40', 'px')}{L['fieldv']('Desktop', '72', 'px')}</div>
<code style="font-family: {MONO}; font-size: 10px; color: #939393">top: clamp(40px, 5vw, 72px)</code>
{swrow(L['lab']('Follow text direction', 'logical sides'), False, 'Logical sides')}
{swrow(L['lab']('Offset when linked to', 'scroll-margin-top'), True, 'Scroll offset')}
<div style="display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 6px; align-items: center">{L['fieldv']('Offset', '68', 'px')}<span style="font-size: 10px; color: #939393">= header height</span></div>
{L['css_line']('padding: clamp(40px, 5vw, 72px) 64px 96px;\nmargin: 0; scroll-margin-top: 68px;')}
</section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', pop + '\n<!-- ═══════════ TOP BAR v3')

# inset: Space between on a Stack
hatch = 'repeating-linear-gradient(45deg, rgba(219,97,162,0.55) 0 2.4px, rgba(219,97,162,0.12) 2.4px 7px)'
bar = lambda w, h: f'<span style="width: {w}px; height: {h}px; border-radius: 2px; background: #8b7b66"></span>'
gapb = lambda v, on=False: f'<span style="position: relative; height: {int(v) // 2 + 2}px; background: {hatch}; {"box-shadow: 0 0 0 1.18px #db61a2;" if on else ""}"><span style="position: absolute; right: -44px; top: -2px; height: 18px; padding: 0 6px; display: flex; align-items: center; border-radius: 9px; background: #b93d82; color: #fff; font: 500 11px/1 Inter, sans-serif">{v}</span></span>'
S.rep('<!-- vertical scroll indicator -->', f'''<!-- INSET: Space between in a Stack -->
<div aria-label="Inset: space between in a Stack" style="position: absolute; left: 56px; top: 742px; width: 420px; padding: 12px; box-sizing: border-box; background: #1f1f1f; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 8px 24px rgba(0,0,0,0.45); z-index: 10">
<div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 11px"><span style="font-weight: 600">Inset · Between on, over Hero text</span><span style="color: #939393">Stack · 3 gaps</span></div>
<div style="padding: 12px 64px 12px 16px; background: #f6f1ea; border-radius: 2px"><div style="display: flex; flex-direction: column; box-shadow: 0 0 0 1px #3fb950">
{bar(150, 8)}{gapb('16')}{bar(260, 26)}{gapb('24', True)}{bar(220, 12)}{gapb('32')}{bar(120, 18)}</div></div>
<div style="margin-top: 8px; font-size: 11px; line-height: 16px; color: #939393">Each gap can differ: the tool writes margins on the child below, or one gap on the Stack when all are equal (Alt+drag).</div>
</div>
<!-- vertical scroll indicator -->''')
S.status(['Page', 'Section · Hero'], 'Drag a band to change the space · Alt: opposite side too · Shift: all four · Ctrl: ignore the spacing snap · double-click to type', 'x 720 &#160;y 136')
S.save('D15-SpacingTool.dc.html')
print('ok')
