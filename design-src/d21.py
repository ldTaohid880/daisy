from screen import *
_src = open('/home/claude/ds/layoutadv.py').read()
LA = {}
exec(_src[:_src.index('# ═════ A · ROW')], LA)
L = LA
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
P['target'] = ('stroke', 'M8 1.5v3M8 11.5v3M1.5 8h3M11.5 8h3M8 5.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5z')

S = Screen('Daisy · D-21 State editing: Mouse over')
S.remove_h1_overlay()
S.remove_parent_outline()
S.unselect_h1_row()

ST, STF, STS = '#a371f7', '#7c4ed8', 'rgba(163,113,247,0.16)'
HOV = '#9b4424'
assert contrast('#ffffff', HOV) >= 4.5 and contrast('#ffffff', STF) >= 4.5

# ---------------- canvas: the button shown in its Mouse over state ----------------
hpos = ['left: -5.6px; top: -5.6px', 'right: -5.6px; top: -5.6px', 'right: -5.6px; bottom: -5.6px', 'left: -5.6px; bottom: -5.6px']
handles = ''.join(f'<span style="position: absolute; {p}; width: 9.4px; height: 9.4px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>' for p in hpos)
old = '<a href="#shop" style="background: #b5532d; color: #ffffff; border-radius: 999px; padding: 12px 24px; font-size: 16px; font-weight: 500; line-height: 20px">Shop the collection</a>'
S.rep(old, f'<a href="#shop" style="position: relative; background: {HOV}; color: #ffffff; border-radius: 999px; padding: 12px 24px; font-size: 16px; font-weight: 500; line-height: 20px">Shop the collection'
      f'<span aria-hidden="true" style="position: absolute; inset: -4px; border: 1.76px solid #2f80ed; border-radius: 4px">{handles}'
      f'<span style="position: absolute; left: -1.76px; bottom: calc(100% + 3px); height: 21px; padding: 0 6px; display: flex; align-items: center; gap: 5px; background: {STF}; color: #fff; font: 500 13px/1 \'Inter\', sans-serif; white-space: nowrap">{icon("target", 12, "#fff", 1.5)}Shop the collection · Mouse over</span></span></a>')

# ---------------- options bar: state chip + normal Select capsules ----------------
chip = (f'<span style="height: 22px; display: flex; align-items: center; gap: 6px; padding: 0 4px 0 9px; border-radius: 11px; background: {STS}; color: #d2bbfb; font-size: 11px; font-weight: 500; white-space: nowrap">'
        f'{icon("target", 12, ST, 1.5)}Editing: Mouse over<button aria-label="Back to Normal" style="width: 16px; height: 16px; display: flex; align-items: center; justify-content: center; border-radius: 8px; color: #d2bbfb">{icon("close", 10)}</button></span>')
S.options('0', '0', '187', 'Fit', '44', 'Fit')
S.rep('<!-- position + size capsule -->', chip + '\n<!-- position + size capsule -->')
set_tree(S, hero_tree('Hero buttons', ('Hero buttons', [(56, None, 't-button', 'Shop the collection', 'a', True, (14, 26, 38, 50), icon('target', 12, ST, 1.5, 'Has a Mouse over state')), (56, None, 't-link', 'Our process →', 'a', False, (14, 26, 38, 50), '')])))
S.rep('<div role="treeitem" aria-selected="true" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 44px; background-color: rgba(47,128,237,0.18);',
      '<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 44px;') if 'padding: 0 12px 0 44px; background-color: rgba(47,128,237,0.18);' in S.s and S.s.count('aria-selected="true"') > 1 else None

# ---------------- properties ----------------
hdr = f'''<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{icon('t-button', 16, '#a8a8a8')}<span style="flex: 1; font-weight: 500">Shop the collection</span>
<button aria-label="State: Mouse over" aria-expanded="true" aria-haspopup="dialog" style="height: 22px; display: flex; align-items: center; gap: 5px; padding: 0 6px; border-radius: 3px; background: #3a3a3a; box-shadow: 0 0 0 1px #2f80ed; color: #e8e8e8; font-weight: 500">{icon('target', 12, ST, 1.5)}Mouse over{icon('chev-down', 10, 'currentColor', 1.5)}</button></div>
<div style="display: flex; align-items: center; gap: 6px; padding-left: 24px; font-size: 11px; color: #a8a8a8"><span>Button</span><span style="color: #454545">·</span><span style="font-family: {MONO}; color: #939393">a</span><span style="flex: 1"></span><span style="color: #a9c8f7">1 change in this state</span></div></div>'''
muted = 'color: #6b6b6b;'
mrow = lambda inner: f(inner, 'opacity: 0.75')
fill = (f(DOT + swatch(HOV) + f'<span style="flex: 1; font-family: {MONO}; font-size: 11px">#9B4424</span><span style="color: #939393">100%</span>', f'box-shadow: inset 0 0 0 1px #2f80ed')
        + '<div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #939393"><span>Normal:</span>' + swatch('#b5532d') + '<span>terracotta</span><span style="flex: 1"></span><button style="font-size: 11px; color: #a8a8a8">Reset</button><span style="color: #454545">·</span><button style="font-size: 11px; color: #a9c8f7">+ Save as swatch</button></div>')
typo = (mrow(f'<span style="flex: 1; {muted}">Inter</span>')
        + pair(mrow(f'<span style="flex: 1; {muted}">Medium</span>'), mrow(f'<span style="font-size: 11px; color: #6b6b6b">Size</span><span style="flex: 1; text-align: right; {muted}">16</span>'))
        + mrow(swatch('#ffffff', True) + f'<span style="flex: 1; {muted}">white</span>')
        + '<div style="font-size: 10px; line-height: 14px; color: #939393">Grey values come from Normal · change one to set it for Mouse over only.</div>')
trans = f'''<div style="display: flex; align-items: center; gap: 8px; padding: 8px; border-radius: 4px; background: rgba(47,128,237,0.12); box-shadow: inset 0 0 0 1px rgba(47,128,237,0.45)">
{icon('play', 12, '#58a6ff')}<span style="flex: 1; font-size: 11px; line-height: 15px; color: #e8e8e8">Animate this change?<span style="display: block; color: #a9c8f7">Fill · 200 ms · Smooth</span></span>
<button style="height: 22px; padding: 0 10px; border-radius: 4px; background: #246bcb; color: #fff; font-size: 11px; font-weight: 500">Add</button><button aria-label="Dismiss" style="color: #939393">{icon('close', 10)}</button></div>'''
S.props(panel(hdr + group('Fill', fill) + group('Typography', typo) + group('Transition', trans)
              + more([mp('Size', '187 × 44 Fit'), mp('Spacing', '12 24'), mp('Border', 'radius Pill'), mp('Effects'), mp('Link', '#shop'), mp('Accessibility')])))

# ---------------- States popover from the header's state button ----------------
def strow(name, css, n, on=False, warn=''):
    cnt = f'<span style="font-size: 10px; color: {"#a9c8f7" if n else "#6b6b6b"}">{n} change{"s" if n != 1 else ""}</span>' if n is not None else '<span style="font-size: 10px; color: #939393">base</span>'
    w = f'<span title="{warn}">{icon("warning", 12, "#e3b34a", 1.25)}</span>' if warn else ''
    return (f'<button aria-pressed="{str(on).lower()}" style="width: 100%; height: 30px; display: flex; align-items: center; gap: 8px; padding: 0 8px; box-sizing: border-box; border-radius: 3px; {"background: rgba(47,128,237,0.18); box-shadow: inset 0 0 0 1px #2f80ed;" if on else ""}">'
            f'<span style="width: 12px">{icon("check", 12, "#a9c8f7") if on else ""}</span><span style="color: {"#e8e8e8" if on else "#c8c8c8"}">{name}</span><span style="font-family: {MONO}; font-size: 10px; color: #939393">{css}</span><span style="flex: 1"></span>{w}{cnt}</button>')
sw = lambda on: f'<button role="switch" aria-checked="{str(on).lower()}" style="position: relative; width: 28px; height: 16px; border-radius: 8px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {"#fff" if on else "#a8a8a8"}"></span></button>'
pop = f'''<!-- POPOVER: States, from the header's state button -->
<section role="dialog" aria-label="States · Shop the collection" style="position: absolute; left: 1282px; top: 80px; width: 328px; box-sizing: border-box; padding: 0 12px 12px; display: flex; flex-direction: column; gap: 8px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); z-index: 30">
<span aria-hidden="true" style="position: absolute; right: -6px; top: 14px; width: 10px; height: 10px; background: #262626; border-right: 1px solid #454545; border-top: 1px solid #454545; transform: rotate(45deg)"></span>
<div style="height: 40px; margin: 0 -12px; padding: 0 8px 0 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a">
<span style="font-weight: 600">States</span><span style="flex: 1; font-size: 11px; color: #939393">Shop the collection · a</span>
<button aria-label="Pin open" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #939393">{icon("keep", 14)}</button>
<button aria-label="Close" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon("close", 14)}</button></div>
<div style="display: flex; flex-direction: column; gap: 2px">
{strow('Normal', '', None)}{strow('Mouse over', ':hover', 1, True)}{strow('Pressed', ':active', 0)}{strow('Focused', ':focus-visible', 0, warn='No visible focus style of its own')}{strow('Disabled', '[disabled]', 0)}</div>
<div style="display: flex; align-items: flex-start; gap: 6px; padding: 8px; border-radius: 4px; background: rgba(227,179,74,0.10); box-shadow: inset 0 0 0 1px rgba(227,179,74,0.35); font-size: 11px; line-height: 16px"><span style="margin-top: 2px">{icon('warning', 12, '#e3b34a', 1.25)}</span><span style="flex: 1; color: #c8c8c8">Focused only has the browser's default ring. <button style="color: #e3b34a; font-size: 11px">Add a focus style</button></span></div>
<button style="height: 24px; align-self: flex-start; display: flex; align-items: center; gap: 4px; padding: 0 8px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #a8a8a8">{icon('plus', 11)}More: Visited link · Focus within · Placeholder…</button>
<div style="height: 1px; background: #333333"></div>
<div style="display: flex; align-items: center; justify-content: space-between; font-size: 11px; color: #a8a8a8"><span>Hold the state on the canvas</span>{sw(True)}</div>
<div style="display: flex; align-items: center; justify-content: space-between; font-size: 11px; color: #a8a8a8"><span>Show all states side by side</span>{sw(True)}</div>
<div style="display: flex; align-items: center; justify-content: space-between; font-size: 11px; color: #a8a8a8"><span>Apply to every “Shop” button</span>{sw(False)}</div>
{L['css_line']('a:hover {\n  background: #9b4424;\n}')}
</section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', pop + '\n<!-- ═══════════ TOP BAR v3')

# ---------------- inset: all states side by side ----------------
btn = lambda bg, label, extra='', ring='': f'<div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 8px"><span style="position: relative; height: 36px; padding: 0 16px; display: flex; align-items: center; border-radius: 999px; background: {bg}; color: #fff; font-size: 13px; font-weight: 500; white-space: nowrap; {ring}">Shop the collection</span><span style="font-size: 11px; color: #4a443c">{label}</span>{extra}</div>'
S.rep('<!-- vertical scroll indicator -->', f'''<!-- INSET: all states side by side -->
<div aria-label="Inset: all states side by side" style="position: absolute; left: 56px; top: 700px; width: 700px; padding: 12px; box-sizing: border-box; background: #1f1f1f; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 8px 24px rgba(0,0,0,0.45); z-index: 10">
<div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 11px"><span style="font-weight: 600">Inset · Show all states side by side</span><span style="color: #939393">click one to edit it</span></div>
<div style="display: flex; gap: 8px; padding: 16px 8px 12px; background: #f6f1ea; border-radius: 2px">
{btn('#b5532d', 'Normal')}
{btn(HOV, '<b style="color: #1f5fb5">Mouse over</b> · 1 change', ring='box-shadow: 0 0 0 2px #f6f1ea, 0 0 0 3.5px #2f80ed')}
{btn('#b5532d', 'Pressed · same as Normal', '', 'opacity: 0.55')}
{btn('#b5532d', 'Focused ⚠', '', 'outline: 2px auto #4d90fe; outline-offset: 2px')}
</div>
<div style="margin-top: 8px; font-size: 11px; line-height: 16px; color: #939393">States without changes are dimmed · ⚠ Focused shows only the browser ring.</div>
</div>
<!-- vertical scroll indicator -->''')

S.status(['Page', 'Section · Hero', 'Box · Hero grid', 'Box · Hero text', 'Box · Hero buttons', 'Button · Shop the collection'],
         'Editing Mouse over · only changes are saved · Esc or × goes back to Normal · selecting another element resets to Normal', 'x 488 &#160;y 640')
S.save('D21-State.dc.html')
print('ok')
