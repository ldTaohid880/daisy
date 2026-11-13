import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

A = '#2f80ed'
PANEL = 'width: 320px; box-sizing: border-box; padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 10px; background: #1f1f1f; border: 1px solid #303030; border-radius: 4px'


def title(t, adv_open=True):
    st = 'background: #3a3a3a; color: #e8e8e8;' if adv_open else 'color: #939393;'
    return f'''<div style="height: 28px; margin-bottom: -2px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">{t}</span>
<button aria-label="{t} · Advanced" aria-expanded="{str(adv_open).lower()}" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; {st}">{icon('sliders', 14)}</button></div>'''


def lab(t, css=''):
    c = f' <span style="font-family: {MONO}; font-size: 10px; color: #939393">{css}</span>' if css else ''
    return f'<div style="font-size: 11px; color: #a8a8a8">{t}{c}</div>'


def seg(items, sel, cols=None):
    cols = cols or len(items)
    out = ''
    for i, it in enumerate(items):
        on = i == sel
        st = 'background: #3a3a3a; color: #e8e8e8;' if on else 'color: #939393;'
        lbl, tip = it if isinstance(it, tuple) else (it, it)
        out += f'<button aria-pressed="{str(on).lower()}" title="{tip}" style="height: 22px; display: flex; align-items: center; justify-content: center; gap: 4px; border-radius: 3px; font-size: 11px; {st}">{lbl}</button>'
    return f'<div role="group" style="display: grid; grid-template-columns: repeat({cols}, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #262626; border-radius: 4px">{out}</div>'


# mini diagrams for justify / align buttons (16 x 12 drawings)
def jd(kind, axis='main'):
    """three child bars inside a 18x12 frame showing justify-content or align-items."""
    bars = ''
    if axis == 'main':
        pos = {'start': [1, 5, 9], 'center': [4, 8, 12], 'end': [7, 11, 15], 'between': [1, 8, 15], 'around': [2.5, 8, 13.5], 'evenly': [3, 8, 13]}[kind]
        for x in pos:
            bars += f'<span style="position: absolute; left: {x}px; top: 2px; width: 3px; height: 8px; border-radius: 1px; background: currentColor"></span>'
    else:
        spec = {'start': [(0, 5), (0, 8), (0, 4)], 'center': [(3.5, 5), (2, 8), (4, 4)], 'end': [(7, 5), (4, 8), (8, 4)],
                'stretch': [(0, 12), (0, 12), (0, 12)], 'baseline': [(4, 5), (1, 8), (5, 4)]}[kind]
        for i, (y, h) in enumerate(spec):
            bars += f'<span style="position: absolute; left: {2 + i * 5}px; top: {y}px; width: 3px; height: {h}px; border-radius: 1px; background: currentColor"></span>'
        if kind == 'baseline':
            bars += '<span style="position: absolute; left: 0; right: 0; top: 9px; border-top: 1px dashed currentColor; opacity: 0.6"></span>'
    edge = '<span style="position: absolute; left: 0; top: 0; bottom: 0; border-left: 1px solid currentColor; opacity: 0.4"></span>' if axis == 'main' else '<span style="position: absolute; left: 0; right: 0; top: 0; border-top: 1px solid currentColor; opacity: 0.4"></span>'
    return f'<span aria-hidden="true" style="position: relative; width: 18px; height: 12px; display: block">{edge}{bars}</span>'


def iconseg(kinds, sel, axis, names):
    items = [(jd(k, axis), n) for k, n in zip(kinds, names)]
    return seg(items, sel)


def fieldv(label, val, unit='', w=None, dot=False, focus=False):
    d = '<span style="width: 5px; height: 5px; border-radius: 3px; background: #2f80ed; flex: none"></span>' if dot else ''
    f = 'box-shadow: inset 0 0 0 1px #2f80ed;' if focus else ''
    ws = f'width: {w}px;' if w else ''
    u = f'<span style="font-size: 10px; color: #939393">{unit}</span>' if unit else ''
    return f'<label style="{ws} height: 24px; box-sizing: border-box; display: flex; align-items: center; gap: 6px; padding: 0 6px; background: #2a2a2a; border-radius: 2px; {f}">{d}<span style="font-size: 11px; color: #939393; white-space: nowrap">{label}</span><span style="flex: 1; text-align: right">{val}</span>{u}</label>'


def pair(a, b, link=False):
    lk = f'<button aria-label="Link" style="width: 20px; height: 24px; display: flex; align-items: center; justify-content: center; color: {"#a9c8f7" if link else "#939393"}">{icon("link", 12)}</button>'
    return f'<div style="display: grid; grid-template-columns: minmax(0, 1fr) 20px minmax(0, 1fr); gap: 4px; align-items: center">{a}{lk}{b}</div>'


def stepper(label, n):
    return f'''<div style="height: 24px; display: flex; align-items: center; background: #2a2a2a; border-radius: 2px">
<span style="padding: 0 6px; font-size: 11px; color: #939393">{label}</span>
<button aria-label="Fewer" style="width: 22px; height: 24px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon("minus", 12)}</button>
<span style="flex: 1; text-align: center">{n}</span>
<button aria-label="More" style="width: 22px; height: 24px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon("plus", 12)}</button></div>'''


def css_line(t):
    return f'''<div style="display: flex; align-items: flex-start; gap: 8px; padding-top: 10px; border-top: 1px solid #333333">
<code style="flex: 1; min-width: 0; font-family: {MONO}; font-size: 11px; line-height: 16px; color: #939393; white-space: pre-wrap">{t}</code>
<button style="height: 22px; padding: 0 8px; border-radius: 4px; font-size: 11px; color: #a8a8a8; flex: none">Copy CSS</button></div>'''


def advdiv():
    return '<div style="display: flex; align-items: center; gap: 8px; margin-top: 2px"><span style="font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393">ADVANCED</span><span style="flex: 1; height: 1px; background: #333333"></span></div>'


def preview(inner, h=96):
    return f'<div aria-hidden="true" style="position: relative; height: {h}px; padding: 8px; box-sizing: border-box; background: #262626; border-radius: 4px; box-shadow: inset 0 0 0 1px #303030">{inner}</div>'


def chip_track(v, sel=False):
    st = 'box-shadow: inset 0 0 0 1px #2f80ed; background: rgba(26,146,132,0.18);' if sel else 'background: rgba(26,146,132,0.14);'
    return f'<button style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 6px 0 8px; border-radius: 3px; {st} font-family: {MONO}; font-size: 11px; color: #9fe5dc">{v}{icon("chev-down", 10, "#6fd3c6", 1.75)}</button>'


assert contrast('#9fe5dc', '#2b2633') >= 4.5

# ═════ A · ROW (flex container) ═════
kid = lambda w, h, c='#5b5b5b': f'<span style="width: {w}px; height: {h}px; border-radius: 2px; background: {c}; flex: none"></span>'
prevA = preview(f'<div style="height: 100%; display: flex; flex-direction: row; flex-wrap: wrap; justify-content: space-between; align-items: center; align-content: center; gap: 8px 12px; outline: 1px dashed #4f4f4f; outline-offset: 2px">{kid(44, 30, "#4a6fa5")}{kid(64, 44)}{kid(36, 24)}{kid(52, 36)}</div>')
A_panel = f'''<section aria-label="Layout · Row" style="{PANEL}">
{title('Layout')}
{seg(['Stack', 'Row', 'Grid'], 1)}
<div style="display: grid; grid-template-columns: 60px 1fr; gap: 10px; align-items: start">
<span style="width: 60px; height: 60px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); padding: 4px; box-sizing: border-box; background: #2a2a2a; border-radius: 4px">{''.join(f'<span style="display: flex; align-items: center; justify-content: center">' + (f'<span style="display: flex; gap: 2px; align-items: center"><span style="width: 3px; height: 7px; background: {A}; border-radius: 1px"></span><span style="width: 3px; height: 11px; background: {A}; border-radius: 1px"></span><span style="width: 3px; height: 5px; background: {A}; border-radius: 1px"></span></span>' if i == 4 else '<span style="width: 3px; height: 3px; border-radius: 50%; background: #6b6b6b"></span>') + '</span>' for i in range(9))}</span>
<div style="display: flex; flex-direction: column; gap: 6px">{fieldv('Spread', 'Space between', '', None)}{fieldv('Gap', '12', 'px', None, True)}</div>
</div>
{advdiv()}
{lab('Direction', 'flex-direction')}
{seg([(icon('chev-right', 12, 'currentColor', 1.75) + 'Row', 'row'), (icon('chev-down', 12, 'currentColor', 1.75) + 'Column', 'column'), (icon('chev-left', 12, 'currentColor', 1.75) + 'Reverse', 'row-reverse'), (icon('chev-up', 12, 'currentColor', 1.75) + 'Reverse', 'column-reverse')], 0)}
{lab('Main axis', 'justify-content')}
{iconseg(['start', 'center', 'end', 'between', 'around', 'evenly'], 3, 'main', ['Start', 'Centre', 'End', 'Space between', 'Space around', 'Space evenly'])}
{lab('Cross axis', 'align-items')}
{iconseg(['start', 'center', 'end', 'stretch', 'baseline'], 1, 'cross', ['Start', 'Centre', 'End', 'Stretch', 'Text baseline'])}
{lab('Wrap', 'flex-wrap')}
{seg(['No wrap', 'Wrap', 'Wrap reverse'], 1)}
{lab('Lines (when wrapping)', 'align-content')}
{iconseg(['start', 'center', 'end', 'between', 'around', 'evenly'], 1, 'main', ['Start', 'Centre', 'End', 'Space between', 'Space around', 'Space evenly'])}
{lab('Gaps', 'row-gap · column-gap')}
{pair(fieldv('Row', '8', 'px', None, True), fieldv('Column', '12', 'px', None, True), False)}
{prevA}
{css_line('display: flex; flex-wrap: wrap;\njustify-content: space-between;\nalign-items: center; align-content: center;\ngap: 8px 12px;')}
</section>'''

# ═════ B · GRID container ═════
cells = ''
areas = [('header', 2), ('text', 1), ('image', 1)]
prevB = preview(f'''<div style="height: 100%; display: grid; grid-template-columns: 1.1fr 1fr; grid-template-rows: 22px 1fr; grid-template-areas: 'h h' 't i'; gap: 6px 8px">
<span style="grid-area: h; border-radius: 2px; background: rgba(26,146,132,0.28); box-shadow: inset 0 0 0 1px #1a9284; display: flex; align-items: center; padding-left: 6px; font-family: {MONO}; font-size: 10px; color: #9fe5dc">header</span>
<span style="grid-area: t; border-radius: 2px; background: #4a6fa5; display: flex; align-items: flex-end; padding: 0 0 4px 6px; font-family: {MONO}; font-size: 10px; color: #e8e8e8">text</span>
<span style="grid-area: i; border-radius: 2px; background: #5b5b5b; display: flex; align-items: flex-end; padding: 0 0 4px 6px; font-family: {MONO}; font-size: 10px; color: #e8e8e8">image</span></div>''', 110)

area_grid = f'''<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #262626; border-radius: 4px; font-family: {MONO}; font-size: 11px">
<span style="grid-column: 1 / 3; height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: rgba(26,146,132,0.18); color: #9fe5dc; box-shadow: inset 0 0 0 1px #2f80ed">header</span>
<span style="height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: #2f2f2f">text</span>
<span style="height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: #2f2f2f">image</span></div>'''

B_panel = f'''<section aria-label="Layout · Grid" style="{PANEL}">
{title('Layout')}
{seg(['Stack', 'Row', 'Grid'], 2)}
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">{stepper('Columns', 2)}{stepper('Rows', 2)}</div>
{fieldv('Gap', '64', 'px', None, True)}
{advdiv()}
{lab('Columns', 'grid-template-columns')}
<div style="display: flex; flex-wrap: wrap; gap: 4px; align-items: center">{chip_track('1.1fr', True)}{chip_track('1fr')}<button aria-label="Add column" style="width: 22px; height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 3px; box-shadow: inset 0 0 0 1px #454545; color: #a8a8a8">{icon('plus', 12)}</button></div>
<div style="padding: 8px; display: flex; flex-direction: column; gap: 6px; background: #262626; border-radius: 4px; box-shadow: inset 0 0 0 1px #3a3a3a">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 11px; color: #e8e8e8">Column 1</span><span style="font-family: {MONO}; font-size: 10px; color: #939393">track</span></div>
{seg(['fr', 'px', 'auto', 'min–max', 'fit'], 0)}
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px">{fieldv('Share', '1.1', 'fr', None, True, True)}{fieldv('Min', '0', 'px')}</div>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 4px">
<button style="height: 22px; padding: 0 8px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #a8a8a8">Equal</button>
<button title="240px 1fr" style="height: 22px; padding: 0 8px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #a8a8a8">Sidebar + main</button>
<button title="repeat(auto-fit, minmax(200px, 1fr))" style="height: 22px; padding: 0 8px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #a8a8a8">Auto-fit cards</button>
<button title="repeat(12, 1fr)" style="height: 22px; padding: 0 8px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #a8a8a8">12 columns</button>
</div>
{lab('Rows', 'grid-template-rows')}
<div style="display: flex; gap: 4px; align-items: center">{chip_track('auto')}{chip_track('1fr')}<button aria-label="Add row" style="width: 22px; height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 3px; box-shadow: inset 0 0 0 1px #454545; color: #a8a8a8">{icon('plus', 12)}</button></div>
{lab('Gaps', 'row-gap · column-gap')}
{pair(fieldv('Row', '24', 'px', None, True), fieldv('Column', '64', 'px', None, True))}
{lab('Fill order', 'grid-auto-flow')}
{seg(['Row', 'Column', 'Row · dense', 'Col · dense'], 0)}
{lab('Items inside cells', 'justify-items · align-items')}
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px">{iconseg(['start', 'center', 'end', 'stretch'], 3, 'cross', ['Start', 'Centre', 'End', 'Stretch'])}{iconseg(['start', 'center', 'end', 'stretch'], 1, 'cross', ['Start', 'Centre', 'End', 'Stretch'])}</div>
<div style="display: flex; align-items: center; justify-content: space-between">{lab('Named areas', 'grid-template-areas')}<button role="switch" aria-checked="true" aria-label="Named areas" style="position: relative; width: 28px; height: 16px; border-radius: 8px; background: #246bcb"><span style="position: absolute; right: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: #ffffff"></span></button></div>
{area_grid}
<div style="font-size: 10px; line-height: 14px; color: #939393">Drag across cells to merge them into one area; type to rename.</div>
{prevB}
{css_line("display: grid;\ngrid-template-columns: 1.1fr 1fr;\ngrid-template-rows: auto 1fr;\ngrid-template-areas: 'header header' 'text image';\ngap: 24px 64px; align-items: center;")}
</section>'''

# ═════ C · CHILD of a Row / Grid ═════
C_row = f'''<section aria-label="In Row" style="{PANEL}">
{title('In Row', True)}
<div style="font-size: 11px; color: #939393; margin-top: -4px">Shown when the parent arranges as a Row</div>
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 11px; color: #e8e8e8">Grow to fill</span><button role="switch" aria-checked="true" aria-label="Grow to fill" style="position: relative; width: 28px; height: 16px; border-radius: 8px; background: #246bcb"><span style="position: absolute; right: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: #ffffff"></span></button></div>
{advdiv()}
{lab('Size in the row', 'flex-grow · flex-shrink · flex-basis')}
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 6px">{fieldv('Grow', '1', '', None, True)}{fieldv('Shrink', '1')}{fieldv('Basis', 'auto')}</div>
<div style="display: flex; flex-wrap: wrap; gap: 4px">
<button style="height: 22px; padding: 0 8px; border-radius: 4px; background: rgba(47,128,237,0.22); font-size: 11px; color: #a9c8f7">Fill space</button>
<button style="height: 22px; padding: 0 8px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #a8a8a8">Keep size</button>
<button style="height: 22px; padding: 0 8px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #a8a8a8">Equal share</button>
</div>
{lab('Align this item', 'align-self')}
{iconseg(['start', 'center', 'end', 'stretch', 'baseline'], 3, 'cross', ['Start', 'Centre', 'End', 'Stretch', 'Text baseline'])}
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px">{fieldv('Order', '0')}<div style="display: flex; gap: 2px">
<button style="flex: 1; height: 24px; border-radius: 2px; background: #2a2a2a; font-size: 11px; color: #a8a8a8">First</button><button style="flex: 1; height: 24px; border-radius: 2px; background: #2a2a2a; font-size: 11px; color: #a8a8a8">Last</button></div></div>
{css_line('flex: 1 1 auto; align-self: stretch;')}
</section>'''

# grid cell picker 4x3, item spans col 1-2, row 2
picker = ''
for r in range(3):
    for c in range(4):
        on = (r == 1 and c in (0, 1))
        st = 'background: rgba(47,128,237,0.35); box-shadow: inset 0 0 0 1px #2f80ed;' if on else 'background: #2a2a2a;'
        picker += f'<span style="height: 20px; border-radius: 2px; {st}"></span>'
picker = f'<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 3px; padding: 6px; background: #262626; border-radius: 4px">{picker}</div>'

C_grid = f'''<section aria-label="In Grid" style="{PANEL}">
{title('In Grid', True)}
<div style="font-size: 11px; color: #939393; margin-top: -4px">Shown when the parent arranges as a Grid</div>
{lab('Place in cells — drag to span')}
{picker}
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px">{fieldv('Column', '1', '')}{fieldv('Span', '2', 'cols', None, True)}{fieldv('Row', '2', '')}{fieldv('Span', '1', 'row')}</div>
{advdiv()}
{lab('Area', 'grid-area')}
{fieldv('Area', 'text ▾')}
{lab('Align in cell', 'justify-self · align-self')}
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px">{iconseg(['start', 'center', 'end', 'stretch'], 3, 'cross', ['Start', 'Centre', 'End', 'Stretch'])}{iconseg(['start', 'center', 'end', 'stretch'], 1, 'cross', ['Start', 'Centre', 'End', 'Stretch'])}</div>
{css_line('grid-column: 1 / span 2; grid-row: 2;\njustify-self: stretch; align-self: center;')}
</section>'''


def colhead(t, d):
    return f'<div><div style="font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{d}</div></div>'


body = sheet_header('D-37', 'Layout · Advanced for Row and Grid', 'Every flex and grid property gets a visual control with a plain name, the CSS name beside it, a live preview and a CSS line — the same pattern as the corner roundness control. Opened with the Advanced icon in the Layout group header.')
body += f'''<div style="display: grid; grid-template-columns: repeat(4, 320px); gap: 48px; align-items: start">
<div style="display: flex; flex-direction: column; gap: 12px">{colhead('A · Row container', 'Simple controls, then Advanced: direction incl. reverse, main and cross axis as picture buttons, wrap, line alignment, separate gaps')}{A_panel}</div>
<div style="display: flex; flex-direction: column; gap: 12px">{colhead('B · Grid container', 'Track chips with a per-track editor (fr, px, auto, min–max, fit), presets, rows, gaps, fill order, item alignment and named areas')}{B_panel}</div>
<div style="display: flex; flex-direction: column; gap: 12px">{colhead('C · Child in a Row', 'Grow / shrink / basis with one-click presets, align self, order')}{C_row}</div>
<div style="display: flex; flex-direction: column; gap: 12px">{colhead('D · Child in a Grid', 'Pick cells visually to place and span; area, align in cell')}{C_grid}</div>
</div>
<div style="margin-top: 32px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px">
<div style="padding: 14px; background: #1a1a1a; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a; font-size: 11px; line-height: 16px; color: #a8a8a8"><b style="color: #e8e8e8">Same on canvas.</b> Every control here has a canvas twin in the Layout tool (D-14): track lines, gap bars, direction arrow, grow toggles, cell drag. Changing one updates the other live.</div>
<div style="padding: 14px; background: #1a1a1a; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a; font-size: 11px; line-height: 16px; color: #a8a8a8"><b style="color: #e8e8e8">Raw values always work.</b> Any field or track chip accepts CSS directly (<code style="font-family: {MONO}">minmax(200px, 1fr)</code>, <code style="font-family: {MONO}">repeat(auto-fit, …)</code>). Syntax the pictures can't show gets the <span style="padding: 0 4px; border-radius: 6px; background: #3a3a3a">custom</span> tag and stays editable as text.</div>
<div style="padding: 14px; background: #1a1a1a; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a; font-size: 11px; line-height: 16px; color: #a8a8a8"><b style="color: #e8e8e8">Display stays simple.</b> Stack / Row / Grid covers block, flex and grid. Other display values (inline, inline-flex, contents…) stay in Advanced → <code style="font-family: {MONO}">display ▾</code>; hiding stays in Visibility so it can differ per screen size.</div>
</div>'''

H = int(sys.argv[1]) if len(sys.argv) > 1 else 1800
open('/home/claude/daisy/project/Layout-Advanced.dc.html', 'w', encoding='utf-8').write(page('Daisy · Layout advanced (Row and Grid)', 1600, H, body))
