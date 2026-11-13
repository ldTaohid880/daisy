import colorsys
from screen import *
_src = open('/home/claude/ds/layoutadv.py').read(); LA = {}; exec(_src[:_src.index('# ═════ A · ROW')], LA); L = LA
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
P['unlink'] = ('stroke', 'M6.5 9.5l-1.8 1.8a2.3 2.3 0 0 1-3.2-3.2L3.3 6.3M9.5 6.5l1.8-1.8a2.3 2.3 0 0 0-3.2-3.2L6.3 3.3M2 2l12 12')

S = Screen('Daisy · D-39 Colour picker')
S.remove_h1_overlay(); S.remove_parent_outline(); S.unselect_h1_row()
BR = '#b5532d'

# ── canvas: the button selected ──
hpos = ['left: -5.6px; top: -5.6px', 'right: -5.6px; top: -5.6px', 'right: -5.6px; bottom: -5.6px', 'left: -5.6px; bottom: -5.6px']
handles = ''.join(f'<span style="position: absolute; {p}; width: 9.4px; height: 9.4px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>' for p in hpos)
old = '<a href="#shop" style="background: #b5532d; color: #ffffff; border-radius: 999px; padding: 12px 24px; font-size: 16px; font-weight: 500; line-height: 20px">Shop the collection</a>'
S.rep(old, f'<a href="#shop" style="position: relative; background: {BR}; color: #ffffff; border-radius: 999px; padding: 12px 24px; font-size: 16px; font-weight: 500; line-height: 20px">Shop the collection'
      f'<span aria-hidden="true" style="position: absolute; inset: -4px; border: 1.76px solid #2f80ed; border-radius: 4px">{handles}'
      f'<span style="position: absolute; left: -1.76px; bottom: calc(100% + 3px); height: 21px; padding: 0 6px; display: flex; align-items: center; background: #246bcb; color: #fff; font: 500 13px/1 \'Inter\', sans-serif; white-space: nowrap">Button · a</span></span></a>')
S.options('0', '0', '187', 'Fit', '44', 'Fit')
set_tree(S, hero_tree('Hero buttons', ('Hero buttons', [(56, None, 't-button', 'Shop the collection', 'a', True, (14, 26, 38, 50), ''), (56, None, 't-link', 'Our process →', 'a', False, (14, 26, 38, 50), '')])))

# ── Properties: Fill open, its colour field pressed (opens the picker) ──
chip = f'<span style="height: 16px; display: flex; align-items: center; gap: 4px; padding: 0 5px; border-radius: 3px; background: #333333; font-size: 10px; color: #c8c8c8">{icon("link", 10, "#a8a8a8")}brand</span>'
fill_row = f(DOT + swatch(BR) + '<span style="flex: 1">brand</span>' + '<span style="color: #939393">100%</span>', 'background: #3a3a3a; box-shadow: inset 0 0 0 1px #2f80ed')
fill = fill_row + f'<button style="align-self: flex-start; height: 22px; display: flex; align-items: center; gap: 6px; padding: 0 4px; font-size: 11px; color: #a8a8a8">{icon("plus", 11, "currentColor", 1.75)}Add a fill layer</button>'
typo = f(swatch('#ffffff', True) + '<span style="flex: 1">white</span>') + pair(f('<span style="flex: 1">Inter</span>'), f('<span style="flex: 1">Medium</span><span style="color: #939393">16</span>'))
S.props(panel(header('t-button', 'Shop the collection', 'Button', 'a') + group('Fill', fill) + group('Typography', typo)
              + more([mp('Size', '187 × 44 Fit'), mp('Spacing', '12 24'), mp('Border', 'radius pill'), mp('Effects'), mp('Link', '#shop'), mp('Accessibility')])))

# ── the colour picker popover ──
TOK = [('brand', BR), ('brand-deep', '#9e4626'), ('brand-light', '#c86a43'), ('ink', '#1d1a16'), ('ink-soft', '#4a443c'), ('sand', '#f6f1ea'), ('clay', '#e7d9c7'), ('moss', '#5f6b4e')]
PAGE = [('#e6dccd', 'hero image box'), ('#6b6358', 'View all link'), ('#d8cbb8', 'card image')]
tile = lambda c, on=False, title='': (f'<button title="{title}" style="width: 30px; height: 30px; box-sizing: border-box; border-radius: 4px; background: {c}; '
    f'{"outline: 2px solid #2f80ed; outline-offset: 2px;" if on else ""} box-shadow: inset 0 0 0 1px rgba(255,255,255,0.10)"></button>')
sec = lambda t, right='': f'<div style="display: flex; align-items: center; gap: 8px; margin-top: 2px"><span style="font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393">{t}</span><span style="flex: 1"></span>{right}</div>'
h, s_, v = colorsys.rgb_to_hsv(*(int(BR[i:i + 2], 16) / 255 for i in (1, 3, 5)))
SVW, SVH = 304, 150
hue_hex = '#%02x%02x%02x' % tuple(round(x * 255) for x in colorsys.hsv_to_rgb(h, 1, 1))
sv = f'''<div style="position: relative; width: {SVW}px; height: {SVH}px; border-radius: 4px; background: linear-gradient(to top, #000, transparent), linear-gradient(to right, #fff, {hue_hex}); box-shadow: inset 0 0 0 1px rgba(255,255,255,0.08)">
<span style="position: absolute; left: {s_ * SVW - 7:.0f}px; top: {(1 - v) * SVH - 7:.0f}px; width: 14px; height: 14px; box-sizing: border-box; border-radius: 7px; border: 2px solid #fff; box-shadow: 0 0 0 1px rgba(0,0,0,0.4); background: {BR}"></span></div>'''
hue = f'''<div style="position: relative; height: 12px; border-radius: 6px; background: linear-gradient(to right, #f00, #ff0, #0f0, #0ff, #00f, #f0f, #f00)">
<span style="position: absolute; left: {h * 100:.1f}%; top: -2px; width: 16px; height: 16px; margin-left: -8px; box-sizing: border-box; border-radius: 8px; border: 2px solid #fff; box-shadow: 0 0 0 1px rgba(0,0,0,0.4); background: {hue_hex}"></span></div>'''
alpha = f'''<div style="position: relative; height: 12px; border-radius: 6px; background: linear-gradient(to right, rgba(181,83,45,0), {BR}), repeating-conic-gradient(#555 0 25%, #888 0 50%) 0 0 / 8px 8px">
<span style="position: absolute; right: -2px; top: -2px; width: 16px; height: 16px; box-sizing: border-box; border-radius: 8px; border: 2px solid #fff; box-shadow: 0 0 0 1px rgba(0,0,0,0.4); background: {BR}"></span></div>'''
eyedrop = f'<button aria-label="Pick from the screen · I" title="Pick from the screen · I" style="width: 30px; height: 30px; flex: none; display: flex; align-items: center; justify-content: center; border-radius: 4px; box-shadow: inset 0 0 0 1px #454545; color: #c8c8c8">{icon("eyedropper", 14)}</button>'
sliders = f'<div style="display: flex; align-items: center; gap: 10px">{eyedrop}<div style="flex: 1; display: flex; flex-direction: column; gap: 8px">{hue}{alpha}</div><span style="width: 30px; height: 30px; flex: none; border-radius: 4px; background: {BR}; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.1)" title="Current colour"></span></div>'
fmt = f'<button style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 6px 0 8px; border-radius: 2px; background: #2a2a2a; font-size: 11px; color: #c8c8c8">HEX{icon("chev-down", 9, "#939393", 1.75)}</button>'
vals = (f'<div style="display: grid; grid-template-columns: 64px minmax(0, 1fr) 72px; gap: 6px">{fmt}'
        + f('<span style="flex: 1; font-family: ' + MONO + '; font-size: 11px">B5532D</span>')
        + f('<span style="flex: 1">100</span><span style="font-size: 10px; color: #939393">%</span>') + '</div>')
tabs = '<div role="tablist" style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #1f1f1f; border-radius: 4px; font-size: 11px">' + ''.join(
    f'<button role="tab" aria-selected="{str(i == 0).lower()}" style="height: 22px; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == 0 else "color: #a8a8a8;"}">{t}</button>' for i, t in enumerate(['Solid', 'Linear', 'Radial', 'Image'])) + '</div>'
link = f'''<div style="display: flex; align-items: center; gap: 8px; padding: 8px; border-radius: 4px; background: #2a2a2a">
{icon('link', 13, '#a9c8f7')}<span style="flex: 1; min-width: 0; display: flex; flex-direction: column"><span>Linked to <b style="font-weight: 600">brand</b></span><span style="font-size: 10px; line-height: 14px; color: #939393">Changing the colour here unlinks this fill. To change brand on all 18 uses, <button style="font-size: 10px; color: #a9c8f7">edit the token</button>.</span></span>
<button title="Unlink · keep #B5532D as a plain value" style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 8px; border-radius: 4px; box-shadow: inset 0 0 0 1px #454545; font-size: 11px; color: #c8c8c8">{icon("unlink", 11)}Unlink</button></div>'''
r = contrast('#ffffff', BR)
con = f'<div style="display: flex; align-items: center; gap: 8px; font-size: 11px"><span style="width: 34px; height: 18px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: {BR}; color: #fff; font: 600 10px/1 Inter, sans-serif">Aa</span><span style="flex: 1; color: #a8a8a8">Text on this fill (white)</span><span style="color: #c8c8c8">{r:.1f}:1</span><span style="display: flex; align-items: center; gap: 3px; color: #3fb950">{icon("check", 11, "#3fb950", 1.75)}AA</span></div>'
pop = f'''<!-- POPOVER: Colour picker · Fill -->
<section role="dialog" aria-label="Fill colour · Shop the collection" style="position: absolute; left: 1282px; top: 118px; width: 328px; box-sizing: border-box; padding: 0 12px 12px; display: flex; flex-direction: column; gap: 10px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); font-variant-numeric: tabular-nums; z-index: 30">
<span aria-hidden="true" style="position: absolute; right: -6px; top: 62px; width: 10px; height: 10px; background: #262626; border-right: 1px solid #454545; border-top: 1px solid #454545; transform: rotate(45deg)"></span>
<div style="height: 40px; margin: 0 -12px; padding: 0 8px 0 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a">
<span style="font-weight: 600">Fill</span><span style="flex: 1; font-size: 11px; color: #939393">Shop the collection</span>
<button aria-label="Pin open" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #939393">{icon("keep", 14)}</button>
<button aria-label="Close" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon("close", 14)}</button></div>
{tabs}
{sec('HALDEN DESIGN SYSTEM', f'<button aria-label="Find a colour" style="color: #939393">{icon("search", 12)}</button>')}
<div style="display: grid; grid-template-columns: repeat(8, 30px); justify-content: space-between">{''.join(tile(c, n == 'brand', n) for n, c in TOK)}</div>
{sec('ON THIS PAGE · NOT TOKENS', '<button style="font-size: 10px; color: #a9c8f7">Save as token…</button>')}
<div style="display: flex; gap: 8px">{''.join(tile(c, False, t) for c, t in PAGE)}</div>
<div style="height: 1px; margin: 2px 0; background: #333333"></div>
{sv}{sliders}{vals}
{link}{con}
{L['css_line']('background-color: var(--color-brand);')}
</section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', pop + '\n<!-- ═══════════ TOP BAR v3')
S.status(['Page', 'Section · Hero', 'Box · Hero grid', 'Box · Hero text', 'Box · Hero buttons', 'Button · a'],
         'I picks a colour from the screen · Alt-click a token to see where it is used', 'x 612 &#160;y 288')
S.rep('<button aria-label="ink · #1d1a16" aria-pressed="true" style="width: 24px; height: 24px; box-sizing: border-box; border-radius: 2px; background: #1d1a16; outline: 2px solid #2f80ed; outline-offset: 1px; border: 1px solid #454545"></button>', '<button aria-label="ink · #1d1a16" style="width: 24px; height: 24px; box-sizing: border-box; border-radius: 2px; background: #1d1a16; border: 1px solid #454545"></button>')
S.rep('<button aria-label="brand · #b5532d" style="width: 24px; height: 24px; border-radius: 2px; background: #b5532d"></button>', '<button aria-label="brand · #b5532d" aria-pressed="true" style="width: 24px; height: 24px; border-radius: 2px; background: #b5532d; outline: 2px solid #2f80ed; outline-offset: 1px"></button>')
S.save('D39-ColourPicker.dc.html')
print('ok')
