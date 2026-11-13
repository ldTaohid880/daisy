import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

P['b-state'] = ('stroke', 'M8 1.5v3M8 11.5v3M1.5 8h3M11.5 8h3M11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0z')
P['b-anim'] = ('stroke', 'M9 1.5L3.5 9H8l-1 5.5L12.5 7H8z')

tools = [
    ('Select', [('select', 'Select', 'V', ''), ('direct', 'Direct Select', 'A', '')]),
    ('Create', [('section', 'Section', 'S', 'variants'), ('box', 'Box', 'R', 'variants'), ('text', 'Text', 'T', 'variants'),
                ('media', 'Media', 'I', 'variants'), ('button', 'Button', 'B', ''), ('link', 'Link', 'L', ''),
                ('form', 'Form', 'F', 'variants'), ('place', 'Place', 'N', '')]),
    ('Shape', [('layout', 'Layout', 'G', ''), ('spacing', 'Spacing', 'P', ''), ('transform', 'Transform', 'Q', ''), ('gradient', 'Gradient', 'D', '')]),
    ('Inspect', [('eyedropper', 'Eyedropper', 'E', ''), ('measure', 'Measure', 'M', ''), ('hand', 'Hand', 'H · Space', ''), ('zoom', 'Zoom', 'Z', '')]),
]

TRI = '<svg width="4" height="4" viewBox="0 0 4 4" aria-hidden="true" style="position: absolute; right: 3px; bottom: 3px"><path d="M4 0V4H0z" fill="#939393"></path></svg>'


def tbtn(ic, state, variants):
    tri = TRI if variants else ''
    if state == 'rest':
        st, col, bar = '', '#a8a8a8', ''
    elif state == 'hover':
        st, col, bar = 'background: #323232;', '#e8e8e8', ''
    elif state == 'active':
        st, col, bar = 'background: rgba(47,128,237,0.18);', '#2f80ed', '<span style="position: absolute; left: -6px; top: 0; bottom: 0; width: 2px; background: #2f80ed"></span>'
    elif state == 'temp':
        st, col, bar = 'box-shadow: inset 0 0 0 1px #2f80ed; outline: none; background-image: none; border: 1px dashed #2f80ed; box-sizing: border-box; box-shadow: none;', '#2f80ed', ''
    else:  # focus
        st, col, bar = FOCUS + ';', '#e8e8e8', ''
    return f'<span style="position: relative; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; border-radius: 2px; color: {col}; {st}">{bar}{icon(ic)}{tri}</span>'


cards = ''
for gname, items in tools:
    row = ''
    for ic, name, key, var in items:
        row += f'''<div style="display: flex; flex-direction: column; gap: 10px; padding: 16px; background: #1a1a1a; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a">
<div style="display: flex; align-items: center; justify-content: space-between">
<span style="color: #e8e8e8">{icon(ic, 32, sw=1.5 * 16 / 32 * 2)}</span>
<span style="height: 18px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #2a2a2a; box-shadow: inset 0 -1px 0 #3a3a3a; font-size: 10px; font-weight: 500; color: #a8a8a8">{key}</span>
</div>
<div style="font-weight: 500">{name}{' <span style="font-size: 10px; color: #939393">· has variants</span>' if var else ''}</div>
<div style="display: flex; gap: 10px; align-items: center; padding-left: 6px">{tbtn(ic, 'rest', var)}{tbtn(ic, 'hover', var)}{tbtn(ic, 'active', var)}{tbtn(ic, 'focus', var)}</div>
<div style="display: flex; gap: 10px; font-size: 10px; color: #939393; padding-left: 6px"><span style="width: 32px; text-align: center">rest</span><span style="width: 32px; text-align: center">hover</span><span style="width: 32px; text-align: center">active</span><span style="width: 32px; text-align: center">focus</span></div>
</div>'''
    cards += f'<div style="grid-column: 1 / -1; font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393; margin-top: 8px">{gname.upper()} · {len(items)}</div>' + row
tools_block = grid(8, cards, gap=12)
tools_block += f'''<div style="display: flex; gap: 32px; margin-top: 20px; align-items: center">
<div style="display: flex; align-items: center; gap: 10px">{tbtn('hand', 'temp', '')}<span style="font-size: 11px; color: #a8a8a8">Temporary tool (hold Space / Ctrl / Alt): dashed accent outline instead of a fill</span></div>
<div style="display: flex; align-items: center; gap: 10px"><span style="position: relative; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon('box')}<span style="position: absolute; right: 4px; top: 4px; width: 4px; height: 4px; border-radius: 2px; background: #2f80ed"></span></span><span style="font-size: 11px; color: #a8a8a8">Locked for repeated use (double-click): 4 px accent dot</span></div>
<div style="display: flex; align-items: center; gap: 10px"><span style="position: relative; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon('text')}{TRI}</span><span style="font-size: 11px; color: #a8a8a8">Has variants: 4 px corner triangle · hold 300 ms or right-click</span></div>
</div>'''

generic = ['chev-down', 'chev-right', 'chev-up', 'chev-left', 'close', 'plus', 'minus', 'check', 'eye', 'eye-off', 'lock', 'unlock',
           'trash', 'gear', 'play', 'search', 'more', 'undo', 'redo', 'warning', 'info', 'folder', 'file', 'new-page', 'code', 'sliders',
           'swap', 'upload', 'external', 'copy', 'grip', 'menu', 'outline', 'corners', 'radius', 'snap', 'flow', 'free']


def glyph(n, size=16, col='#e8e8e8'):
    return f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 14px 4px 10px; background: #1a1a1a; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a">
<span style="color: {col}">{icon(n, size)}</span><span style="font-family: {MONO}; font-size: 10px; color: #939393">{n}</span></div>'''


gen_block = grid(13, ''.join(glyph(n) for n in generic), gap=8)

devices = [('desktop', 'Desktop'), ('tablet', 'Tablet'), ('phone', 'Mobile'), ('wide', 'Wide')]
dev_block = '<div style="display: flex; gap: 8px">' + ''.join(
    f'<div style="width: 96px; display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 14px 4px 10px; background: #1a1a1a; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a"><span style="color: #e8e8e8">{icon(n, 14)}</span><span style="font-size: 10px; color: #939393">{l} · 14</span></div>'
    for n, l in devices) + '</div>'

types = [('t-section', 'section'), ('t-stack', 'stack'), ('t-row', 'row'), ('t-grid', 'grid'), ('t-para', 'text ¶'), ('t-heading', 'heading'),
         ('t-image', 'image'), ('t-button', 'button'), ('t-link', 'link'), ('t-field', 'form field'), ('t-list', 'list'), ('t-table', 'table'), ('t-embed', 'embed')]
type_block = grid(13, ''.join(
    f'<div style="display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 14px 4px 10px; background: #1a1a1a; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a"><span style="color: #a8a8a8">{icon(n, 14)}</span><span style="font-size: 10px; color: #939393">{l}</span></div>'
    for n, l in types), gap=8)

badges = [('desktop', '#d29922', 'Overrides at smaller sizes'), ('b-state', '#a371f7', 'State styles'), ('b-anim', '#a8a8a8', 'Animation'),
          ('link', '#a8a8a8', 'Link'), ('code', '#a8a8a8', 'Custom CSS'), ('warning', '#d29922', 'Accessibility issue'), ('free', '#a8a8a8', 'Free placement'),
          ('lock', '#a8a8a8', 'Locked'), ('eye-off', '#a8a8a8', 'Hidden at this size')]
badge_block = '<div style="display: flex; gap: 8px; flex-wrap: wrap">' + ''.join(
    f'<div style="width: 120px; display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 14px 4px 10px; background: #1a1a1a; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a">{icon(n, 12, c, 1.25)}<span style="font-size: 10px; color: #939393; text-align: center">{l}</span></div>'
    for n, c, l in badges) + '</div>'

rules = f'''<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px">
<div style="padding: 16px; background: #1a1a1a; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a; display: flex; gap: 16px; align-items: center">
<div style="position: relative; width: 96px; height: 96px; flex: none; background-image: linear-gradient(#2f80ed22 1px, transparent 1px), linear-gradient(90deg, #2f80ed22 1px, transparent 1px); background-size: 6px 6px; box-shadow: inset 0 0 0 1px #2f80ed55; display: flex; align-items: center; justify-content: center; color: #e8e8e8">{icon('media', 96, sw=1.5)}</div>
<div style="font-size: 11px; line-height: 16px; color: #a8a8a8"><b style="color: #e8e8e8">16 × 16 grid</b><br>1.5 px stroke, round caps and joins, outline, currentColor.</div></div>
<div style="padding: 16px; background: #1a1a1a; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a; font-size: 11px; line-height: 16px; color: #a8a8a8"><b style="color: #e8e8e8">Sizes</b><br>Tools and generic 16 · devices and tree types 14 · badges 12 on a 1.25 stroke · inline chevrons 10–12.</div>
<div style="padding: 16px; background: #1a1a1a; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a; font-size: 11px; line-height: 16px; color: #a8a8a8"><b style="color: #e8e8e8">No fills</b><br>Outline only. Exceptions: Select pointer, play, more dots, grip — and the active tool, which uses the accent colour only.</div>
<div style="padding: 16px; background: #1a1a1a; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a; font-size: 11px; line-height: 16px; color: #a8a8a8"><b style="color: #e8e8e8">Source</b><br>Tool icons are a custom set drawn to the concepts in 4.1. Generic glyphs follow the Lucide style. Never emoji.</div>
</div>'''

body = sheet_header('D-00b', 'Icons', 'All 18 tool icons with their states and shortcuts, the generic glyph set, device, element-type and badge icons. Same drawing rules everywhere (9.6).')
body += section('4.1', 'Tools · 18 in 4 groups', 'Shown at 32 for detail; the rows below each are the real 32 × 32 buttons with a 16 px icon', tools_block)
body += section('9.6', 'Generic glyphs · 16', 'Chevrons, actions, panels and controls', gen_block)
body += '<div style="display: grid; grid-template-columns: auto 1fr; gap: 64px">' + section('9.6', 'Devices · 14', '', dev_block, mb=40) + section('3.1', 'Element types · 14', 'Layers and Project tree', type_block, mb=40) + '</div>'
body += section('3.1', 'Badges · 12', 'After a layer name; colour only where it carries meaning', badge_block, mb=40)
body += section('9.6', 'Drawing rules', '', rules, mb=0)

H = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
open('/home/claude/daisy/project/DS-Icons.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-00b Icons', 1920, H, body))
