import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

TAG, STR, NUM, PROP, PUN, COM, ERR = '#7fb0f0', '#9cc58a', '#d9a66b', '#c8c8c8', '#8a8a8a', '#7a7a7a', '#f47067'
assert contrast(ERR, '#1b1b1b') >= 4.5
sp = lambda c, t: f'<span style="color: {c}">{t}</span>'
P['max'] = ('stroke', 'M3 6V3h3M10 3h3v3M13 10v3h-3M6 13H3v-3')
P['min'] = ('stroke', 'M6 3v3H3M13 6h-3V3M10 13v-3h3M3 10h3v3')
P['regex'] = ('stroke', 'M11 2v6M8.5 3.5l5 3M8.5 6.5l5-3M3 11h3v3H3z')
P['replace'] = ('stroke', 'M3 5h8l-2-2M13 11H5l2 2')
P['sync'] = ('stroke', 'M3 8a5 5 0 0 1 9-3l1-1v4H9l1.5-1.5A3 3 0 0 0 5 8M13 8a5 5 0 0 1-9 3l-1 1V8h4l-1.5 1.5A3 3 0 0 0 11 8')
d = lambda p, v, end=';': f'  {sp(PROP, p)}{sp(PUN, ":")} {v}{sp(PUN, end)}'

def lines(rows, start=1, hl=None, marks=None, extra=None):
    marks = marks or {}; extra = extra or {}
    out = ''
    for i, r in enumerate(rows):
        n = start + i
        m = marks.get(n, '')
        g = {'mod': '<span style="position: absolute; left: 0; top: 2px; bottom: 2px; width: 2px; background: #2f80ed"></span>',
             'err': f'<span style="position: absolute; left: 1px; top: 4px">{icon("close", 9, ERR, 2.5)}</span>',
             'warn': f'<span style="position: absolute; left: 1px; top: 4px">{icon("warning", 9, "#d29922", 1.75)}</span>'}.get(m, '')
        bg = 'background: rgba(47,128,237,0.14);' if n == hl else ('background: rgba(244,112,103,0.10);' if m == 'err' else '')
        out += (f'<div style="position: relative; display: flex; {bg}"><span style="position: relative; width: 34px; flex: none; padding-right: 8px; box-sizing: border-box; text-align: right; color: {"#c8c8c8" if n == hl else "#5b5b5b"}">{g}{n}</span>'
                f'<span style="position: relative; flex: 1; min-width: 0; white-space: pre; overflow: visible">{r}{extra.get(n, "")}</span></div>')
    return f'<div style="font: 11px/17px {MONO}; color: {PROP}; padding: 6px 0">{out}</div>'

hdrbtn = lambda ic, l: f'<button aria-label="{l}" style="width: 22px; height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 3px; color: #a8a8a8">{icon(ic, 12, "currentColor", 1.75)}</button>'
def mode(two_way=False):
    a = f'<button style="display: flex; align-items: center; gap: 4px; padding: 0 7px; border-radius: 3px; {"color: #939393;" if two_way else "background: #3a3a3a; color: #e8e8e8; font-weight: 500;"}">{icon("lock", 10)}Read-only</button>'
    b = f'<button style="display: flex; align-items: center; gap: 4px; padding: 0 7px; border-radius: 3px; {"background: #246bcb; color: #fff; font-weight: 500;" if two_way else "color: #939393;"}">{icon("sync", 10) if two_way else ""}Edit two-way</button>'
    return f'<div style="height: 22px; display: flex; gap: 2px; padding: 2px; box-sizing: border-box; background: #262626; border-radius: 4px; font-size: 11px">{a}{b}</div>'
def frame(body, target='Hero title <span style="font-family: ' + MONO + '; color: #939393">h1.hero-title</span>', two_way=False, strip='', h=300, extra_hdr=''):
    return f'''<div style="height: {h}px; display: flex; flex-direction: column; background: #1f1f1f; border: 1px solid #303030; border-radius: 6px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.35)">
<div style="height: 30px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 6px 0 12px; border-bottom: 1px solid #303030">
<span style="position: relative; height: 30px; display: flex; align-items: center; gap: 6px; font-weight: 500">{icon('code', 12)}Code<span style="position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: #2f80ed"></span></span>
<span style="display: flex; align-items: center; gap: 6px; color: #a8a8a8">{icon('play', 10)}Timeline</span>
<span style="width: 1px; height: 14px; background: #333333"></span><span style="font-size: 11px; color: #c8c8c8; white-space: nowrap">{target}</span>
<span style="flex: 1"></span>{extra_hdr}{mode(two_way)}{hdrbtn('max', 'Maximise')}{hdrbtn('chev-down', 'Collapse')}</div>
<div style="flex: 1; min-height: 0; display: flex; position: relative">{body}</div>
<div style="height: 22px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 12px; border-top: 1px solid #2c2c2c; font-size: 11px; color: #939393; white-space: nowrap">{strip or '<span style="display: flex; align-items: center; gap: 5px">' + icon("check", 11, "#3fb950", 2) + 'No problems</span><span style="flex: 1"></span><span>UTF-8</span>'}</div></div>'''
pane = lambda tabs, body, w=None, border=True: f'<section style="{f"width: {w}px; flex: none;" if w else "flex: 1; min-width: 0;"} display: flex; flex-direction: column; background: #1b1b1b; {"border-left: 1px solid #2c2c2c;" if border else ""}"><div style="height: 26px; flex: none; display: flex; align-items: stretch; background: #1f1f1f; border-bottom: 1px solid #262626">{tabs}</div><div style="flex: 1; min-height: 0; overflow: hidden">{body}</div></section>'
etab = lambda name, on=True, mod=False: f'<span style="display: flex; align-items: center; gap: 6px; padding: 0 10px; font-family: {MONO}; font-size: 11px; {"background: #1b1b1b; color: #e8e8e8; box-shadow: inset 0 2px 0 #2f80ed;" if on else "color: #939393;"}">{name}{"<span style=\"width: 6px; height: 6px; border-radius: 3px; background: #c8c8c8\"></span>" if mod else ""}</span>'
itab = lambda items, sel: '<span style="display: flex; align-items: center; gap: 14px; padding: 0 10px">' + ''.join(f'<span style="position: relative; height: 26px; display: flex; align-items: center; font-size: 11px; font-weight: 500; color: {"#e8e8e8" if i == sel else "#939393"}">{t}' + ('<span style="position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: #2f80ed"></span>' if i == sel else '') + '</span>' for i, t in enumerate(items)) + '</span>'
css_base = [sp(TAG, '.hero-title') + ' ' + sp(PUN, '{'), d('font-family', sp(STR, 'var(--font-display)')), None, d('line-height', sp(NUM, '1.05')), d('font-weight', sp(NUM, '600')), d('color', sp(STR, 'var(--ink)')), sp(PUN, '}')]
def css(line14, **kw):
    rows = list(css_base); rows[2] = line14
    return lines(rows, 12, **kw)
cap = lambda t, desc: f'<div style="display: flex; flex-direction: column; gap: 2px; margin-bottom: 10px"><div style="font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{desc}</div></div>'
pop = 'background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 10px 28px rgba(0,0,0,0.5);'

# 1 · Edit two-way with autocomplete
ac_item = lambda name, val, on=False, sw='': f'<div style="height: 24px; display: flex; align-items: center; gap: 8px; padding: 0 8px; border-radius: 3px; {"background: #2f4a6e;" if on else ""}">{sw}<span style="font-family: {MONO}; font-size: 11px; color: {"#e8e8e8" if on else "#c8c8c8"}">{name}</span><span style="flex: 1"></span><span style="font-size: 10px; color: #a8a8a8">{val}</span></div>'
ac = (f'<div style="position: absolute; left: 140px; top: 17px; width: 290px; padding: 4px; {pop} z-index: 3">'
      + ac_item('var(--text-display)', '64px · Halden', True) + ac_item('var(--text-h1)', '56px · Halden') + ac_item('var(--text-h2)', '40px · Halden') + ac_item('clamp()', 'fluid size')
      + '<div style="padding: 4px 8px 2px; font-size: 10px; color: #939393">Design-system sizes first · Tab accepts · Esc closes</div></div>')
caret = '<span style="display: inline-block; width: 1px; height: 13px; margin-left: 1px; vertical-align: -2px; background: #e8e8e8"></span>'
s1_body = (pane(etab('styles.css', True, True), css(d('font-size', sp(STR, 'var(--te') + caret + sp(PUN, ''), end=''), hl=14, marks={14: 'mod'}, extra={14: ac}), border=False)
           + f'''<aside style="width: 250px; flex: none; padding: 10px 12px; box-sizing: border-box; display: flex; flex-direction: column; gap: 8px; border-left: 1px solid #2c2c2c">
<div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a9c8f7">{icon('sync', 12, '#58a6ff')}Live: canvas and Properties follow</div>
<div style="padding: 8px; border-radius: 4px; background: #262626; font-size: 11px; line-height: 16px; color: #c8c8c8">Typography › Size shows <b style="font-weight: 600">var(--text-display)</b> with the token chip once you accept.</div>
<div style="font-size: 10px; line-height: 14px; color: #939393">Changes are kept as you type · Ctrl+Z undoes them in the same history as the canvas</div></aside>''')
S1 = frame(s1_body, two_way=True, strip=f'<span style="display: flex; align-items: center; gap: 5px; color: #a9c8f7">{icon("sync", 11, "#58a6ff")}Editing two-way · synced</span><span style="flex: 1"></span><span>Ln 14, Col 20</span><span>UTF-8</span>')

# 2 · Invalid code
squig = f'<span style="text-decoration: underline wavy {ERR}; text-underline-offset: 3px">64pz</span>'
tip = f'<span style="position: absolute; left: 160px; top: 18px; width: 280px; padding: 8px 10px; {pop} font-family: Inter, sans-serif; font-size: 11px; line-height: 16px; white-space: normal; z-index: 3"><b style="color: {ERR}; font-weight: 600">Unknown unit “pz”.</b> <span style="color: #c8c8c8">Did you mean <b style="font-weight: 600">px</b>?</span><span style="display: flex; gap: 6px; margin-top: 6px"><button style="height: 20px; padding: 0 8px; border-radius: 3px; background: #246bcb; color: #fff">Use 64px</button><button style="height: 20px; padding: 0 8px; border-radius: 3px; background: #333333; color: #c8c8c8">Ignore</button></span></span>'
s2_body = (pane(etab('styles.css', True, True), css(d('font-size', squig), hl=None, marks={14: 'err'}, extra={14: tip}), border=False)
           + f'''<aside style="width: 250px; flex: none; padding: 10px 12px; box-sizing: border-box; display: flex; flex-direction: column; gap: 8px; border-left: 1px solid #2c2c2c">
<div style="font-size: 11px; font-weight: 600">Canvas keeps the last good value</div>
<div style="display: flex; align-items: center; gap: 8px; padding: 8px; border-radius: 4px; background: #262626; font-size: 11px"><span style="font: 600 18px/1 Georgia, serif">Aa</span><span style="color: #c8c8c8">64px</span><span style="color: #939393">· until the line is valid</span></div>
<div style="font-size: 10px; line-height: 14px; color: #939393">Nothing breaks on the page while you type · invalid lines are never exported</div></aside>''')
S2 = frame(s2_body, two_way=True, strip=f'<span style="display: flex; align-items: center; gap: 5px; color: {ERR}">{icon("close", 10, ERR, 2.5)}1 error</span><span>· Unknown unit on line 14</span><span style="flex: 1"></span><span>Ln 14, Col 16</span>')

# 3 · Find and replace
hlf = lambda t, cur=False: f'<span style="border-radius: 2px; {"background: rgba(242,184,75,0.45); box-shadow: 0 0 0 1px #f2b84b;" if cur else "background: rgba(242,184,75,0.22);"}">{t}</span>'
optb = lambda ic, l, on=False: f'<button aria-label="{l}" aria-pressed="{str(on).lower()}" style="width: 22px; height: 20px; display: flex; align-items: center; justify-content: center; border-radius: 3px; font: 600 10px/1 {MONO}; {"background: #2f4a6e; color: #e8e8e8;" if on else "color: #a8a8a8;"}">{ic}</button>'
field = lambda val, ph='': f'<label style="flex: 1; height: 24px; display: flex; align-items: center; padding: 0 8px; background: #1b1b1b; border-radius: 3px; box-shadow: inset 0 0 0 1px {"#2f80ed" if val else "#3a3a3a"}; font-family: {MONO}; font-size: 11px; color: {"#e8e8e8" if val else "#939393"}">{val or ph}</label>'
findbox = f'''<div style="position: absolute; right: 12px; top: 8px; width: 380px; padding: 6px; box-sizing: border-box; display: flex; flex-direction: column; gap: 4px; {pop} z-index: 3">
<div style="display: flex; align-items: center; gap: 4px">{field('hero-title')}{optb('Aa', 'Match case')}{optb('ab', 'Whole word', True)}{optb('.*', 'Regex')}<span style="width: 56px; text-align: right; font-size: 11px; color: #c8c8c8">2 of 5</span>{hdrbtn('chev-up', 'Previous')}{hdrbtn('chev-down', 'Next')}</div>
<div style="display: flex; align-items: center; gap: 4px">{field('', 'Replace with')}<button style="height: 22px; padding: 0 8px; border-radius: 3px; background: #333333; font-size: 11px; color: #c8c8c8">Replace</button><button style="height: 22px; padding: 0 8px; border-radius: 3px; background: #333333; font-size: 11px; color: #c8c8c8">All</button></div>
<div style="display: flex; gap: 10px; padding: 2px 2px 0; font-size: 10px; color: #939393"><span>In: <b style="color: #c8c8c8; font-weight: 500">Project</b> ▾</span><span>index.html 3 · styles.css 2</span></div></div>'''
s3 = lines([sp(PUN, '&lt;') + sp(TAG, 'h1') + ' ' + sp(PROP, 'class') + sp(PUN, '=') + sp(STR, '"') + hlf(sp(STR, 'hero-title')) + sp(STR, '"') + sp(PUN, '&gt;') + 'Hand-thrown ceramics…',
            '', sp(TAG, '.') + hlf(sp(TAG, 'hero-title'), True) + ' ' + sp(PUN, '{'), d('font-size', sp(NUM, '64px')), sp(PUN, '}'), '', sp(TAG, '@media') + ' (max-width: 1024px) {', '  ' + sp(TAG, '.') + hlf(sp(TAG, 'hero-title')) + ' { font-size: 48px; }', '}'], 1, hl=3)
S3 = frame(pane(etab('styles.css', True) + etab('index.html', False), s3 + findbox, border=False), extra_hdr='')

# 4 · Computed
def crow(p, v, src, set_=True):
    return f'<div style="display: grid; grid-template-columns: 130px 1fr auto; gap: 8px; align-items: center; height: 22px; padding: 0 12px; font: 11px/1 {MONO}"><span style="color: #c8c8c8">{p}</span><span style="color: {"#e8e8e8" if set_ else "#939393"}">{v}</span><span style="font-family: Inter, sans-serif; font-size: 10px; color: #a9c8f7">{src}</span></div>'
ghd = lambda t: f'<div style="height: 22px; display: flex; align-items: center; padding: 0 12px; font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393; background: #1f1f1f">{t}</div>'
comp = (f'<div style="display: flex; align-items: center; gap: 8px; padding: 6px 12px"><label style="flex: 1; height: 22px; display: flex; align-items: center; gap: 6px; padding: 0 8px; background: #262626; border-radius: 3px; font-size: 11px; color: #939393">{icon("search", 11, "#939393", 1.75)}Filter properties</label>'
        + f'<div style="height: 22px; display: flex; gap: 2px; padding: 2px; box-sizing: border-box; background: #262626; border-radius: 4px; font-size: 11px"><span style="padding: 0 8px; border-radius: 3px; background: #3a3a3a; color: #e8e8e8; font-weight: 500">Set here</span><span style="padding: 0 8px; color: #939393">All 312</span></div></div>'
        + ghd('TYPOGRAPHY') + crow('font-family', 'Fraunces, serif', '→ Typography') + crow('font-size', '64px', '→ Typography') + crow('line-height', '67.2px · 1.05', '→ Typography') + crow('color', '#1d1a16 · ink', 'inherited')
        + ghd('SIZE') + crow('width', '560px', '→ Size') + crow('height', '202px · fit', 'auto', False))
S4 = frame(pane(itab(['Cascade', 'Computed', 'Box'], 1), comp, border=False))

# 5 · Box
def ring(label, val_t, val_r, val_b, val_l, bg, inner, color):
    sty = 'font: 11px/1 ' + MONO
    return (f'<div style="position: relative; padding: 22px 34px; background: {bg}; border: 1px dashed {color}; border-radius: 3px">'
            f'<span style="position: absolute; left: 6px; top: 4px; font-size: 10px; color: {color}">{label}</span>'
            f'<span style="position: absolute; left: 0; right: 0; top: 5px; text-align: center; {sty}; color: #e8e8e8">{val_t}</span><span style="position: absolute; left: 0; right: 0; bottom: 5px; text-align: center; {sty}; color: #e8e8e8">{val_b}</span>'
            f'<span style="position: absolute; left: 10px; top: calc(50% - 5px); {sty}; color: #e8e8e8">{val_l}</span><span style="position: absolute; right: 10px; top: calc(50% - 5px); {sty}; color: #e8e8e8">{val_r}</span>{inner}</div>')
content = '<div style="padding: 14px 24px; background: rgba(47,128,237,0.22); border: 1px solid #2f80ed; border-radius: 2px; text-align: center; font: 11px/1 ' + MONO + '; color: #e8e8e8">560 × 202</div>'
box = ring('margin', '0', '0', '0', '0', 'rgba(240,136,62,0.10)', ring('border', '0', '0', '0', '0', 'rgba(210,153,34,0.08)', ring('padding', '0', '0', '0', '0', 'rgba(63,185,80,0.12)', content, '#3fb950'), '#d29922'), '#f0883e')
s5 = (f'<div style="display: flex; gap: 20px; padding: 14px 16px; align-items: center"><div style="width: 330px">{box}</div>'
      f'<div style="flex: 1; display: flex; flex-direction: column; gap: 6px; font-size: 11px; line-height: 16px; color: #a8a8a8"><div><b style="color: #e8e8e8; font-weight: 600">Click a number</b> to jump to Spacing or Size.</div><div>Position: in flow · offset 0, 64 inside Hero text</div><div>Box sizing: border-box</div><div style="color: #939393">Rendered at Desktop 1440 · 85% zoom does not change the numbers</div></div></div>')
S5 = frame(pane(itab(['Cascade', 'Computed', 'Box'], 2), s5, border=False))

# 6 · Page scope
outline = lambda depth, t, cnt='', on=False: f'<div style="height: 22px; display: flex; align-items: center; gap: 6px; padding: 0 10px 0 {10 + depth * 12}px; font: 11px/1 {MONO}; {"background: rgba(47,128,237,0.16);" if on else ""}"><span style="color: {TAG}">{t}</span><span style="flex: 1"></span><span style="font-family: Inter, sans-serif; font-size: 10px; color: #939393">{cnt}</span></div>'
s6_left = pane(etab('Document outline'), outline(0, '&lt;head&gt;', 'title, meta, 2 fonts') + outline(0, '&lt;body&gt;') + outline(1, 'header', '4 links') + outline(1, 'section.hero', '', True) + outline(1, 'section.season', '3 cards') + outline(1, 'footer'), w=260, border=False)
s6_right = pane(etab('index.html', True), lines([sp(PUN, '&lt;!') + sp(TAG, 'doctype html') + sp(PUN, '&gt;'), tg_ := sp(PUN, '&lt;') + sp(TAG, 'html') + ' ' + sp(PROP, 'lang') + sp(PUN, '=') + sp(STR, '"en"') + sp(PUN, '&gt;'), sp(PUN, '&lt;') + sp(TAG, 'head') + sp(PUN, '&gt;') + ' ' + sp(PUN, '…') + ' ' + sp(PUN, '&lt;/') + sp(TAG, 'head') + sp(PUN, '&gt;'), sp(PUN, '&lt;') + sp(TAG, 'body') + sp(PUN, '&gt;'), '  ' + sp(PUN, '&lt;') + sp(TAG, 'header') + sp(PUN, '&gt;') + ' … ', '  ' + sp(PUN, '&lt;') + sp(TAG, 'section') + ' ' + sp(PROP, 'class') + sp(PUN, '=') + sp(STR, '"hero"') + sp(PUN, '&gt;')], 1, hl=6))
S6 = frame(s6_left + s6_right, target='Page · <span style="font-family: ' + MONO + '; color: #939393">index.html</span> · 212 lines')

# 7 · Copy as menu
mi = lambda t, sub, on=False: f'<div style="padding: 5px 8px; border-radius: 3px; {"background: #323232;" if on else ""}"><div style="color: #e8e8e8">{t}</div><div style="font-size: 10px; line-height: 14px; color: #939393">{sub}</div></div>'
menu = (f'<div style="position: absolute; right: 10px; bottom: 26px; width: 300px; padding: 4px; {pop} z-index: 3">'
        + mi('HTML + CSS', 'Two blocks, as in the files', True) + mi('HTML only', 'Markup for this element') + mi('CSS only', 'Its rules, media queries included')
        + mi('One file, inline styles', 'Paste into an email or a CMS') + '<div style="height: 1px; background: #3a3a3a; margin: 4px 0"></div>'
        + mi('Include design tokens', 'Adds the --variables it uses') + '</div>')
s7 = pane(etab('styles.css', True), css(d('font-size', sp(NUM, '64px')), hl=14) + menu, border=False)
S7 = frame(s7, strip=f'<span style="display: flex; align-items: center; gap: 5px">{icon("check", 11, "#3fb950", 2)}No problems</span><span style="flex: 1"></span><span style="padding: 0 6px; border-radius: 3px; background: #333333; color: #e8e8e8">Copy as: HTML + CSS ▴</span>')

# 8 · Nothing selected
s8 = (f'<div style="flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; background: #1b1b1b">'
      f'<span style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 8px; background: #262626">{icon("code", 18, "#a8a8a8")}</span>'
      '<div style="font-weight: 600">Select something to see its code</div><div style="font-size: 11px; color: #939393">Click an element on the canvas or in Layers</div>'
      '<div style="display: flex; gap: 6px"><button style="height: 24px; padding: 0 10px; border-radius: 4px; background: #333333; font-size: 11px; color: #e8e8e8">Show the page code</button><button style="height: 24px; padding: 0 10px; border-radius: 4px; font-size: 11px; color: #a8a8a8; box-shadow: inset 0 0 0 1px #3a3a3a">Open styles.css</button></div></div>')
S8 = frame(s8, target='<span style="color: #939393">Nothing selected</span>')

# 9 · Conflict while editing two-way
conf = f'''<div style="position: absolute; left: 12px; right: 12px; top: 34px; padding: 8px 10px; display: flex; align-items: center; gap: 10px; border-radius: 4px; background: rgba(210,153,34,0.12); box-shadow: inset 0 0 0 1px rgba(210,153,34,0.5); font-size: 11px; z-index: 3">
{icon('warning', 13, '#d29922', 1.5)}<span style="flex: 1; color: #c8c8c8"><b style="font-weight: 600; color: #e8e8e8">font-size</b> changed in Properties (56px) while you were typing here (60px).</span>
<button style="height: 22px; padding: 0 8px; border-radius: 3px; background: #246bcb; color: #fff">Keep 60px</button><button style="height: 22px; padding: 0 8px; border-radius: 3px; background: #333333; color: #c8c8c8">Use 56px</button></div>'''
s9 = pane(etab('styles.css', True, True), '<div style="height: 46px"></div>' + css(d('font-size', sp(NUM, '60px')), hl=14, marks={14: 'mod'}) + conf, border=False)
S9 = frame(s9, two_way=True, strip=f'<span style="display: flex; align-items: center; gap: 5px; color: #e3b34a">{icon("warning", 11, "#d29922", 1.5)}1 conflict</span><span style="flex: 1"></span><span>Ln 14</span>')

# 10 · Collapsed and maximised bars
bar = lambda inner: f'<div style="height: 28px; display: flex; align-items: center; gap: 14px; padding: 0 8px 0 12px; background: #1f1f1f; border: 1px solid #303030; border-radius: 6px; font-size: 12px">{inner}</div>'
badge = lambda t, c, bg: f'<span style="height: 16px; padding: 0 6px; display: flex; align-items: center; gap: 4px; border-radius: 8px; background: {bg}; color: {c}; font-size: 10px; font-weight: 500">{t}</span>'
S10 = f'''<div style="display: flex; flex-direction: column; gap: 10px">
{bar(f'<span style="display: flex; align-items: center; gap: 6px; color: #a8a8a8">{icon("code", 12)}Code</span>' + badge(icon("warning", 9, "#d29922", 1.75) + '1', '#e3b34a', 'rgba(210,153,34,0.16)') + f'<span style="color: #a8a8a8; display: flex; align-items: center; gap: 6px">{icon("play", 10)}Timeline</span><span style="flex: 1"></span>' + hdrbtn('chev-up', 'Expand'))}
<div style="font-size: 10px; color: #939393; margin: -4px 0 4px 4px">Collapsed · a problem badge stays visible · Ctrl+` opens</div>
{bar(f'<span style="display: flex; align-items: center; gap: 6px; color: #a8a8a8">{icon("code", 12)}Code</span>' + badge(icon("sync", 9, "#58a6ff") + 'editing', '#a9c8f7', 'rgba(47,128,237,0.18)') + '<span style="color: #a8a8a8">Timeline</span><span style="flex: 1"></span>' + hdrbtn('chev-up', 'Expand'))}
<div style="font-size: 10px; color: #939393; margin: -4px 0 4px 4px">Collapsed while editing two-way · changes are already applied</div>
<div style="position: relative; height: 150px; border-radius: 6px; background: #2a2a2a; box-shadow: inset 0 0 0 1px #303030; overflow: hidden">
<div style="position: absolute; left: 10px; right: 10px; top: 10px; height: 18px; border-radius: 3px; background: #333333; font-size: 10px; line-height: 18px; padding-left: 8px; color: #939393">options bar</div>
<div style="position: absolute; left: 10px; right: 10px; top: 34px; bottom: 10px; border-radius: 4px; background: #1f1f1f; border: 1px solid #303030; display: flex; align-items: center; justify-content: center; gap: 8px; color: #a8a8a8; font-size: 11px">{icon('max', 14)}Maximised · the drawer covers the canvas area · {icon('min', 14)} or Ctrl+Shift+M restores it</div></div></div>'''

cells = [
    ('1 · Edit two-way', 'Typing a value: design-system suggestions first; canvas and Properties follow live', S1),
    ('2 · Invalid code', 'Wavy underline, a fix suggestion, red mark in the gutter; the page keeps the last good value', S2),
    ('3 · Find and replace', 'Ctrl F · match case, whole word, regex · scope Element / Page / Project with counts per file', S3),
    ('4 · Computed', 'Final values grouped like Properties; “Set here” or all 312; each row jumps to its field', S4),
    ('5 · Box', 'Margin, border, padding and content with real numbers; click to edit', S5),
    ('6 · Page scope', 'Document outline beside the full file; the selected section is highlighted', S6),
    ('7 · Copy as', 'From the status strip · formats for real hand-offs, tokens optional', S7),
    ('8 · Nothing selected', 'Empty state with the two useful next steps', S8),
    ('9 · Conflict', 'Properties and code changed the same value: choose which wins; nothing is lost', S9),
    ('10 · Collapsed and maximised', 'Bars keep status visible; maximise trades the canvas for room', S10),
]
body = sheet_header('D-27b', 'Code workspace · states', 'Every state of the Code drawer drawn at real size: editing, errors, search, the inspector tabs, scopes, copying, empty, conflicts and the collapsed and maximised bars. Read with D-27, which shows the default Read-only state.')
body += '<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 48px 64px; align-items: start">' + ''.join(f'<div>{cap(t, dsc)}{c}</div>' for t, dsc, c in cells) + '</div>'
H = int(sys.argv[1]) if len(sys.argv) > 1 else 2300
open('/home/claude/daisy/project/D27b-Code-States.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-27b Code workspace states', 1920, H, body))
print('ok')
