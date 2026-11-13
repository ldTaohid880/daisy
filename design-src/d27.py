from screen import *

S = Screen('Daisy · D-27 Code workspace')

# muted syntax: accent tags/selectors, green strings/values, orange numbers; neutral rest
TAG, STR, NUM, PROP, PUN, COM = '#7fb0f0', '#9cc58a', '#d9a66b', '#c8c8c8', '#8a8a8a', '#7a7a7a'
assert all(contrast(c, '#1b1b1b') >= 4.5 for c in (TAG, STR, NUM, PROP))
sp = lambda c, t: f'<span style="color: {c}">{t}</span>'
tg = lambda name, cls=None, close=False: (sp(PUN, '&lt;/' if close else '&lt;') + sp(TAG, name) + (f' {sp(PROP, "class")}{sp(PUN, "=")}{sp(STR, chr(34) + cls + chr(34))}' if cls else '') + sp(PUN, '&gt;'))
P['split'] = ('stroke', 'M2 3h12v10H2zM8 3v10')
P['wrap'] = ('stroke', 'M2 4h12M2 8h9a2 2 0 0 1 0 4H8l1.5-1.5M8 12l1.5 1.5M2 12h3')
P['fold'] = ('stroke', 'M4 6l4 4 4-4')
P['max'] = ('stroke', 'M3 6V3h3M10 3h3v3M13 10v3h-3M6 13H3v-3')
P['files'] = ('stroke', 'M4 2h5l3 3v9H4zM9 2v3h3')

def editor(rows, start=1, hl=None, gutter=None, fold=(), dim=(), wrap=True):
    gutter = gutter or {}
    out = ''
    for i, r in enumerate(rows):
        n = start + i
        g = gutter.get(n, '')
        mark = {'mod': '<span style="position: absolute; left: 0; top: 2px; bottom: 2px; width: 2px; background: #2f80ed"></span>',
                'resp': f'<span title="Tablet and smaller" style="position: absolute; left: 2px; top: 4px">{icon("tablet", 9, "#d29922", 1.75)}</span>',
                'warn': f'<span title="1 problem" style="position: absolute; left: 2px; top: 4px">{icon("warning", 9, "#d29922", 1.75)}</span>'}.get(g, '')
        bg = 'background: rgba(47,128,237,0.14);' if n == hl else ''
        fd = f'<span style="width: 12px; flex: none; color: #6b6b6b">{icon("fold", 9, "#6b6b6b", 1.75) if n in fold else ""}</span>'
        out += (f'<div style="position: relative; display: flex; {bg} {"opacity: 0.5;" if n in dim else ""}"><span style="position: relative; width: 38px; flex: none; padding-right: 6px; box-sizing: border-box; text-align: right; color: {"#c8c8c8" if n == hl else "#5b5b5b"}">{mark}{n}</span>{fd}'
                f'<span style="flex: 1; min-width: 0; {"white-space: pre-wrap;" if wrap else "white-space: pre; overflow: hidden; text-overflow: ellipsis;"}">{r}</span></div>')
    return out
html_rows = [
    tg('section', 'hero'),
    '  ' + tg('div', 'hero-grid'),
    '    ' + tg('div', 'hero-text'),
    '      ' + tg('p', 'eyebrow') + sp(PROP, 'Small-batch stoneware · Est. 2014') + tg('p', close=True),
    '      ' + tg('h1', 'hero-title') + sp(PROP, 'Hand-thrown ceramics for everyday tables') + tg('h1', close=True),
    '      ' + tg('p', 'hero-lede') + sp(PROP, 'Each piece is wheel-thrown…') + tg('p', close=True),
    '      ' + tg('div', 'hero-buttons') + sp(PUN, '…') + tg('div', close=True),
    '    ' + tg('div', close=True),
    '    ' + sp(PUN, '&lt;') + sp(TAG, 'img') + f' {sp(PROP, "src")}{sp(PUN, "=")}{sp(STR, chr(34) + "assets/hero-bowls.svg" + chr(34))} {sp(PROP, "alt")}{sp(PUN, "=")}{sp(STR, chr(34) + chr(34))}' + sp(PUN, '&gt;'),
    '  ' + tg('div', close=True),
]
d = lambda p, v: f'  {sp(PROP, p)}{sp(PUN, ":")} {v}{sp(PUN, ";")}'
css_rows = [
    sp(TAG, '.hero-title') + ' ' + sp(PUN, '{'),
    d('font-family', sp(STR, 'var(--font-display)')),
    d('font-size', sp(NUM, '64px')),
    d('line-height', sp(NUM, '1.05')),
    d('font-weight', sp(NUM, '600')),
    d('color', sp(STR, 'var(--ink)')),
    d('max-width', sp(NUM, '560px')),
    d('text-wrap', sp(STR, 'balance')) + f' {sp(COM, "/* custom */")}',
    sp(PUN, '}'),
    '',
    sp(TAG, '@media') + ' ' + sp(PUN, '(') + sp(PROP, 'max-width') + sp(PUN, ':') + ' ' + sp(NUM, '1024px') + sp(PUN, ')') + ' ' + sp(PUN, '{'),
    '  ' + sp(TAG, '.hero-title') + ' ' + sp(PUN, '{') + ' ' + sp(PROP, 'font-size') + sp(PUN, ':') + ' ' + sp(NUM, '48px') + sp(PUN, '; }'),
    sp(PUN, '}'),
]

# ---------------- left: explorer ----------------
fileitem = lambda ic, name, note='', on=False, badge='': (f'<button style="width: 100%; height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px 0 12px; box-sizing: border-box; {"background: rgba(47,128,237,0.16);" if on else ""}">'
                                                         f'{icon(ic, 13, "#a8a8a8")}<span style="flex: 1; text-align: left; font-family: {MONO}; font-size: 11px; color: {"#e8e8e8" if on else "#c8c8c8"}">{name}</span>{badge}<span style="font-size: 10px; color: #939393">{note}</span></button>')
ruleitem = lambda name, note, on=False, dim=False: (f'<button style="width: 100%; min-height: 24px; display: flex; align-items: center; gap: 6px; padding: 2px 8px 2px 24px; box-sizing: border-box; {"background: rgba(47,128,237,0.16);" if on else ""} {"opacity: 0.55;" if dim else ""}">'
                                                    f'<span style="flex: 1; text-align: left; font-family: {MONO}; font-size: 11px; color: #c8c8c8">{name}</span><span style="font-size: 10px; color: #939393">{note}</span></button>')
hd = lambda t, right='': f'<div style="height: 24px; display: flex; align-items: center; padding: 0 8px 0 12px; font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393"><span style="flex: 1">{t}</span>{right}</div>'
dot = '<span style="width: 6px; height: 6px; border-radius: 3px; background: #c8c8c8"></span>'
explorer = f'''<aside aria-label="Code explorer" style="width: 188px; flex: none; display: flex; flex-direction: column; border-right: 1px solid #2c2c2c; background: #1f1f1f; overflow: hidden">
{hd('SHOW CODE FOR')}
<div style="padding: 0 8px 6px">{seg(['Element', 'Page', 'Project'], 0)}</div>
{hd('FILES')}
{fileitem('file', 'index.html', 'page')}{fileitem('file', 'styles.css', '', True, dot)}{fileitem('lock', 'tokens.css', 'design system')}{fileitem('file', 'animate.js', 'generated')}
{hd('RULES FOR h1.hero-title', '<button style="font-size: 10px; color: #a9c8f7">+ Rule</button>')}
{ruleitem('.hero-title', 'base', True)}{ruleitem('@media ≤ 1024', 'Tablet')}{ruleitem('h1', 'design system')}{ruleitem(':hover', 'none yet', dim=True)}
<div style="flex: 1"></div>
<div style="padding: 8px 12px; border-top: 1px solid #2c2c2c; font-size: 10px; line-height: 14px; color: #939393">Generated from the page · edits in Properties update this live</div>
</aside>'''

# ---------------- centre: editors ----------------
etab = lambda name, on=False, mod=False, extra='': (f'<button role="tab" aria-selected="{str(on).lower()}" style="height: 28px; display: flex; align-items: center; gap: 6px; padding: 0 10px; box-sizing: border-box; font-family: {MONO}; font-size: 11px; {"background: #1b1b1b; color: #e8e8e8; box-shadow: inset 0 2px 0 #2f80ed;" if on else "color: #939393;"}">'
                                                    f'{name}{extra}{dot if mod else ""}</button>')
crumb = lambda parts: '<div style="height: 22px; flex: none; white-space: nowrap; overflow: hidden; display: flex; align-items: center; gap: 4px; padding: 0 10px; font-family: ' + MONO + '; font-size: 10px; color: #939393; border-bottom: 1px solid #262626">' + '<span style="color: #5b5b5b">›</span>'.join(f'<span style="{"color: #c8c8c8" if i == len(parts) - 1 else ""}">{p}</span>' for i, p in enumerate(parts)) + '</div>'
pane_tools = lambda wrap=True: f'<span style="flex: 1"></span><span style="display: flex; align-items: center; gap: 2px; padding-right: 6px; color: #939393">' + ''.join(f'<button aria-label="{l}" style="width: 22px; height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 3px; {"background: #2a2a2a; color: #e8e8e8;" if on else ""}">{icon(ic, 12)}</button>' for ic, l, on in [('wrap', 'Wrap lines', wrap), ('split', 'Split', True), ('copy', 'Copy', False)]) + '</span>'
html_pane = f'''<section aria-label="HTML" style="flex: 1; min-width: 0; display: flex; flex-direction: column; background: #1b1b1b">
<div role="tablist" style="height: 28px; flex: none; display: flex; align-items: stretch; background: #1f1f1f; border-bottom: 1px solid #262626">{etab('index.html', True)}{pane_tools(False)}</div>
{crumb(['…', 'div.hero-grid', 'div.hero-text', 'h1.hero-title'])}
<div style="flex: 1; padding: 6px 8px 6px 0; font: 11px/17px {MONO}; color: {PROP}; overflow: hidden">{editor(html_rows, 41, hl=45, gutter={49: 'warn'}, fold=(41, 42, 43), wrap=False)}</div></section>'''
css_pane = f'''<section aria-label="CSS" style="flex: 1; min-width: 0; display: flex; flex-direction: column; background: #1b1b1b; border-left: 1px solid #2c2c2c">
<div role="tablist" style="height: 28px; flex: none; display: flex; align-items: stretch; background: #1f1f1f; border-bottom: 1px solid #262626">{etab('styles.css', True, True)}{etab('Custom CSS', extra='<span style="height: 14px; padding: 0 4px; border-radius: 7px; background: #333333; font-family: Inter, sans-serif; font-size: 10px; line-height: 14px; color: #c8c8c8">1</span>')}{pane_tools()}</div>
{crumb(['styles.css', '.hero-title', 'font-size'])}
<div style="flex: 1; padding: 6px 8px 6px 0; font: 11px/17px {MONO}; color: {PROP}; overflow: hidden">{editor(css_rows, 12, hl=14, gutter={14: 'mod', 22: 'resp', 23: 'resp', 24: 'resp'}, fold=(12, 22))}</div></section>'''

# ---------------- right: inspector (Cascade / Computed) ----------------
def rule(sel, src, decls, active=True, note=''):
    rows = ''
    for p, v, state in decls:
        style = {'on': 'color: #c8c8c8;', 'over': 'color: #6b6b6b; text-decoration: line-through;', 'inh': 'color: #a8a8a8;'}[state]
        rows += f'<div style="display: flex; gap: 6px; font: 11px/17px {MONO}; {style}"><span style="width: 92px; flex: none; overflow: hidden; text-overflow: ellipsis">{p}</span><span style="flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap">{v}</span></div>'
    return (f'<div style="padding: 6px 10px 8px; border-bottom: 1px solid #262626; {"opacity: 0.55;" if not active else ""}">'
            f'<div style="display: flex; align-items: center; gap: 6px; margin-bottom: 3px"><span style="font: 600 11px/16px {MONO}; color: {TAG}">{sel}</span><span style="flex: 1"></span><span style="font-size: 10px; color: #939393">{src}</span></div>'
            f'{rows}{f"<div style=\"font-size: 10px; color: #939393; margin-top: 2px\">{note}</div>" if note else ""}</div>')
itab = lambda t, on=False: f'<button role="tab" aria-selected="{str(on).lower()}" style="position: relative; height: 28px; padding: 0 2px; font-size: 11px; font-weight: 500; color: {"#e8e8e8" if on else "#939393"}">{t}' + ('<span style="position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: #2f80ed"></span>' if on else '') + '</button>'
inspector = f'''<aside aria-label="Cascade" style="width: 284px; flex: none; display: flex; flex-direction: column; border-left: 1px solid #2c2c2c; background: #1f1f1f; overflow: hidden">
<div role="tablist" style="height: 28px; flex: none; display: flex; align-items: center; gap: 14px; padding: 0 10px; border-bottom: 1px solid #262626">{itab('Cascade', True)}{itab('Computed')}{itab('Box')}<span style="flex: 1"></span><span style="font-size: 10px; color: #939393; white-space: nowrap">Desktop</span></div>
<div style="flex: 1; overflow: hidden">
{rule('.hero-title', 'styles.css:12', [('font-family', 'var(--font-display)', 'on'), ('font-size', '64px', 'on'), ('line-height', '1.05', 'on'), ('font-weight', '600', 'on'), ('text-wrap', 'balance · custom', 'on')])}
{rule('@media ≤ 1024', 'styles.css:22', [('font-size', '48px', 'on')], active=False, note='Not active at Desktop · Tablet and smaller')}
{rule('h1', 'tokens.css · Halden', [('font-size', '40px', 'over'), ('line-height', '1.2', 'over'), ('margin', '0', 'on')])}
{rule('body', 'inherited', [('color', 'var(--ink) #1d1a16', 'inh'), ('-webkit-font-smoothing', 'antialiased', 'inh')])}
</div>
<div style="padding: 6px 10px; border-top: 1px solid #2c2c2c; font-size: 10px; line-height: 14px; color: #939393">Struck-through values are overridden · click any value to jump to its field</div>
</aside>'''

# ---------------- drawer frame ----------------
tab = lambda t, on=False: f'<button role="tab" aria-selected="{str(on).lower()}" style="position: relative; height: 32px; display: flex; align-items: center; gap: 6px; font-weight: 500; color: {"#e8e8e8" if on else "#a8a8a8"}">{t}' + ('<span style="position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: #2f80ed"></span>' if on else '') + '</button>'
sbtn = lambda ic, l: f'<button aria-label="{l}" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon(ic, 13, "currentColor", 1.75)}</button>'
modeseg = ('<div role="group" aria-label="Editing" style="height: 22px; display: flex; gap: 2px; padding: 2px; box-sizing: border-box; background: #262626; border-radius: 4px; font-size: 11px">'
           f'<button aria-pressed="true" style="display: flex; align-items: center; gap: 4px; padding: 0 8px; border-radius: 3px; background: #3a3a3a; color: #e8e8e8; font-weight: 500">{icon("lock", 10)}Read-only</button>'
           '<button aria-pressed="false" style="padding: 0 8px; border-radius: 3px; color: #939393">Edit two-way</button></div>')
statusbar = f'''<div style="height: 24px; flex: none; display: flex; align-items: center; gap: 14px; padding: 0 12px; border-top: 1px solid #2c2c2c; background: #1f1f1f; font-size: 11px; color: #939393">
<button style="display: flex; align-items: center; gap: 5px; color: #c8c8c8">{icon('warning', 11, '#d29922', 1.5)}1 problem<span style="color: #939393">· img on line 49 has an empty alt</span></button>
<span style="flex: 1"></span><span>Ln 45, Col 9</span><span>2 spaces</span><span>UTF-8</span>
<button style="display: flex; align-items: center; gap: 4px; color: #c8c8c8">Copy as: HTML + CSS{icon('chev-down', 10, '#939393', 1.75)}</button></div>'''
drawer = f'''<!-- BOTTOM DRAWER: Code workspace (open, h420) -->
<div style="position: relative; height: 420px; flex: none; box-sizing: border-box; display: flex; flex-direction: column; background: #1f1f1f; border-top: 1px solid #303030">
<span aria-hidden="true" title="Drag to resize" style="position: absolute; left: calc(50% - 16px); top: -3px; width: 32px; height: 4px; border-radius: 2px; background: #454545"></span>
<div role="tablist" aria-label="Bottom drawer" style="height: 32px; flex: none; display: flex; align-items: center; gap: 16px; padding: 0 6px 0 12px; border-bottom: 1px solid #303030">
{tab(icon('code', 13) + 'Code', True)}{tab(icon('play', 11) + 'Timeline')}
<span style="width: 1px; height: 14px; background: #333333"></span>
<span style="font-size: 11px; color: #c8c8c8">Hero title <span style="font-family: {MONO}; color: #939393">h1.hero-title</span></span>
<span style="flex: 1"></span>{modeseg}
<label style="height: 22px; width: 180px; display: flex; align-items: center; gap: 6px; padding: 0 8px; box-sizing: border-box; background: #262626; border-radius: 4px; font-size: 11px; color: #939393">{icon('search', 11, '#939393', 1.75)}Find in code<span style="flex: 1"></span><span style="font-size: 10px">Ctrl F</span></label>
{sbtn('max', 'Maximise drawer')}{sbtn('chev-down', 'Collapse drawer')}</div>
<div style="flex: 1; min-height: 0; display: flex">{explorer}<div style="flex: 1; min-width: 0; display: flex">{html_pane}{css_pane}</div>{inspector}</div>
{statusbar}</div>'''
a = S.s.index('<!-- BOTTOM DRAWER (collapsed, h28) -->'); b = S.s.index('</div>\n</div>', a)
S.s = S.s[:a] + drawer + S.s[b + len('</div>'):]

# Properties: one home for custom CSS (it lives in Code)
i = S.s.index('<span style="flex: 1; text-align: left">Attributes &amp; Custom CSS</span>')
a0 = S.s.rindex('<button', 0, i); b0 = S.s.index('</button>', i) + len('</button>')
S.s = S.s[:a0] + mp('Attributes') + mp('Custom CSS', '1 line · in Code ↓', '#a9c8f7') + S.s[b0:]

S.status(['Page', 'Section · Hero', 'Box · Hero grid', 'Box · Hero text', 'Heading · Hero title'],
         'Code follows the selection · click a CSS value to jump to its field · Ctrl+` toggles the drawer · Ctrl+Shift+M maximises it', 'x 612 &#160;y 288')
S.save('D27-Code.dc.html')
print('ok')
