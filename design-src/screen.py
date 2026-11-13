"""Helpers for deriving editor screens from Main.dc.html (D-04)."""
import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *


class Screen:
    def __init__(self, title):
        self.s = open('/home/claude/daisy/project/Main.dc.html', encoding='utf-8').read()
        self.rep('<title>Daisy · D-04 Editor, heading selected</title>', f'<title>{title}</title>')

    def rep(self, old, new, count=1):
        assert self.s.count(old) == count, (old[:100], self.s.count(old))
        self.s = self.s.replace(old, new)

    def cut(self, start, end, new='', include_end=False):
        a = self.s.index(start)
        b = self.s.index(end, a) + (len(end) if include_end else 0)
        self.s = self.s[:a] + new + self.s[b:]

    def remove_h1_overlay(self):
        a = self.s.index('<!-- selection overlay (screen-constant thickness: values ÷ 0.85) -->')
        b = self.s.index('</div>\n</div>\n<p style="margin: 0; font-size: 18px', a)
        self.s = self.s[:a] + self.s[b + len('</div>\n'):]

    def remove_parent_outline(self):
        self.cut('<!-- parent-of-selection outline: Hero text -->', '</div>', '', include_end=True)

    def unselect_h1_row(self):
        self.rep('<div role="treeitem" aria-selected="true" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 44px; background-color: rgba(47,128,237,0.18); background-image: linear-gradient(#303030,#303030), linear-gradient(#303030,#303030), linear-gradient(#303030,#303030);',
                 '<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 44px; background-image: linear-gradient(#262626,#262626), linear-gradient(#262626,#262626), linear-gradient(#262626,#262626);')
        self.rep('<span style="flex: 1; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; color: #e8e8e8">Hero title</span><span style="font-size: 11px; color: #a8a8a8">h1</span>',
                 '<span style="flex: 1; overflow: hidden; white-space: nowrap; text-overflow: ellipsis">Hero title</span><span style="font-size: 11px; color: #939393">h1</span>')
        self.rep('<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#e8e8e8" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M3 3.5h10M8 3.5V13"></path></svg>',
                 '<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#a8a8a8" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M3 3.5h10M8 3.5V13"></path></svg>')

    def options(self, x, y, w, wmode, h, hmode):
        s = self.s
        a = s.index('<!-- position + size capsule -->')
        b = s.index('<!-- placement -->', a)
        tag = lambda t: f'<span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">{t}</span>'
        val = lambda v, mode: f'<span style="width: 30px; {"" if mode == "Fixed" else "color: #a8a8a8;"} {"font-style: italic; color: #939393;" if v == "Mixed" else ""}">{v}</span>'
        cap = f'''<!-- position + size capsule -->
<div style="height: 28px; display: flex; align-items: center; gap: 2px; padding: 2px; box-sizing: border-box; background: #232323; border-radius: 6px">
<label title="X · left" style="height: 24px; width: 64px; display: flex; align-items: center; gap: 6px; padding: 0 8px; box-sizing: border-box; border-radius: 4px"><span style="font-size: 11px; color: #939393">X</span><span style="{"font-style: italic; color: #939393" if x == "Mixed" else ""}">{x}</span></label>
<label title="Y · top" style="height: 24px; width: 64px; display: flex; align-items: center; gap: 6px; padding: 0 8px; box-sizing: border-box; border-radius: 4px"><span style="font-size: 11px; color: #939393">Y</span><span>{y}</span></label>
<span style="width: 1px; height: 14px; background: #333333"></span>
<label title="Width" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px 0 8px; box-sizing: border-box; border-radius: 4px"><span style="font-size: 11px; color: #939393">W</span>{val(w, wmode)}{tag(wmode)}</label>
<label title="Height" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px 0 8px; box-sizing: border-box; border-radius: 4px"><span style="font-size: 11px; color: #939393">H</span>{val(h, hmode)}{tag(hmode)}</label>
</div>

'''
        self.s = s[:a] + cap + s[b:]

    def props(self, html):
        a = self.s.index('<!-- Properties v2 (decluttered) -->')
        b = self.s.index('<!-- Swatches | History (h220) -->')
        self.s = self.s[:a] + html + '\n' + self.s[b:]

    def status(self, crumbs, hint, xy, notice=False):
        a = self.s.index('<nav aria-label="Selection path"')
        b = self.s.index('</nav>', a) + len('</nav>')
        parts = []
        for i, c in enumerate(crumbs):
            last = i == len(crumbs) - 1
            parts.append(f'<button{" aria-current=\"true\" style=\"color: #e8e8e8\"" if last else ""}>{c}</button>')
        nav = '<nav aria-label="Selection path" style="flex: 1; display: flex; align-items: center; gap: 6px; color: #a8a8a8; white-space: nowrap">\n' + '<span aria-hidden="true">›</span>'.join(parts) + '\n</nav>'
        self.s = self.s[:a] + nav + self.s[b:]
        old = '<span style="flex: 1; text-align: center; color: #939393; white-space: nowrap">Drag a handle to resize · Shift keeps proportions</span>'
        if notice:
            new = f'<span role="status" style="flex: 1; display: flex; align-items: center; justify-content: center; gap: 6px; color: #58a6ff; white-space: nowrap">{icon("info", 12, "#58a6ff", 1.25)}{hint}</span>'
        else:
            new = f'<span style="flex: 1; text-align: center; color: #939393; white-space: nowrap">{hint}</span>'
        self.rep(old, new)
        self.rep('x 612 &#160;y 288', xy)

    def save(self, name):
        self.s = self.s.replace('class="mp-row mp-hover"', 'class="mp-row"')
        open(f'/home/claude/daisy/project/{name}', 'w', encoding='utf-8').write(self.s)


# ---- property panel pieces ----
def f(inner, extra=''):
    return f'<label style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px; background: #2a2a2a; border-radius: 2px; {extra}">{inner}</label>'


DOT = '<span style="width: 5px; height: 5px; border-radius: 3px; background: #2f80ed; flex: none"></span>'


def tagc(t):
    return f'<span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">{t}</span>'


def adv(t):
    return f'<button aria-label="{t} · Advanced" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; color: #939393">{icon("sliders", 14)}</button>'


def mp(n, v='', vc='#939393'):
    val = f'<span style="font-size: 11px; color: {vc}">{v}</span>' if v else ''
    return (f'<button class="mp-row" aria-label="Open {n}" style="width: 100%; height: 28px; display: flex; align-items: center; padding: 0 8px 0 12px; box-sizing: border-box; border-radius: 0; color: #a8a8a8"><span style="flex: 1; text-align: left">{n}</span>{val}'
            f'<span class="mp-add" aria-hidden="true" style="width: 18px; height: 18px; margin-left: 8px; display: flex; align-items: center; justify-content: center; border-radius: 3px; color: #e8e8e8">{icon("plus", 12, "currentColor", 1.75)}</span></button>')


def header(ic, name, kind, tag):
    return f'''<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{icon(ic, 16, '#a8a8a8')}<span style="flex: 1; font-weight: 500">{name}</span>
<button aria-label="State: Normal" style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 6px; border-radius: 2px; color: #a8a8a8">Normal{icon('chev-down', 10, 'currentColor', 1.5)}</button></div>
<div style="display: flex; align-items: center; gap: 6px; padding-left: 24px; font-size: 11px; color: #a8a8a8"><button style="display: flex; align-items: center; gap: 3px">{kind}{icon('chev-down', 10, 'currentColor', 1.5)}</button><span style="color: #454545">·</span><span style="font-family: {MONO}; color: #939393">{tag}</span></div>
</div>'''


def group(title, body):
    return f'''<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">
<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">{title}</span>{adv(title)}</div>
{body}</div>
<div style="height: 1px; background: #303030"></div>'''


def pair(a, b):
    return f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">{a}{b}</div>'


def more(rows):
    return f'''<div style="padding: 8px 0 0">
<div style="padding: 0 12px 4px; font-size: 10px; line-height: 14px; font-weight: 500; letter-spacing: 0.04em; color: #939393">MORE PROPERTIES</div>
{''.join(rows)}</div>'''


def panel(inner):
    return f'''<!-- Properties -->
<section aria-label="Properties" style="position: relative; flex: 1; min-height: 0; overflow: hidden; font-variant-numeric: tabular-nums">
{inner}
</section>
'''


def seg(items, sel):
    out = ''.join(f'<button aria-pressed="{str(i == sel).lower()}" style="height: 22px; display: flex; align-items: center; justify-content: center; gap: 6px; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #939393;"}">{t}</button>' for i, t in enumerate(items))
    return f'<div role="group" style="display: grid; grid-template-columns: repeat({len(items)}, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #262626; border-radius: 4px; font-size: 11px">{out}</div>'


def overlay_box(left, top, w, h, tag_text=None, tag_bg='#246bcb', border='1.76px solid #2f80ed', handles=True, extra=''):
    """absolute selection box in page coordinates (relative to the positioned parent)."""
    hs = ''
    if handles:
        pos = ['left: -5.6px; top: -5.6px', 'left: calc(50% - 4.7px); top: -5.6px', 'right: -5.6px; top: -5.6px', 'right: -5.6px; top: calc(50% - 4.7px)',
               'right: -5.6px; bottom: -5.6px', 'left: calc(50% - 4.7px); bottom: -5.6px', 'left: -5.6px; bottom: -5.6px', 'left: -5.6px; top: calc(50% - 4.7px)']
        hs = ''.join(f'<span style="position: absolute; {p}; width: 9.4px; height: 9.4px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>' for p in pos)
    tg = f'<span style="position: absolute; left: -1.5px; bottom: calc(100% + 2px); height: 21px; padding: 0 5px; display: flex; align-items: center; gap: 4px; background: {tag_bg}; color: #ffffff; font: 500 13px/1 \'Inter\', sans-serif; white-space: nowrap">{tag_text}</span>' if tag_text else ''
    return f'<div aria-hidden="true" style="position: absolute; left: {left}px; top: {top}px; width: {w}px; height: {h}px; box-sizing: border-box; border: {border}; pointer-events: none; {extra}">{tg}{hs}</div>'


# ---------- Phase E helpers ----------
import re as _re


def set_tool(S, label):
    """Make `label` (e.g. 'Text (T)') the active tool in the tool strip."""
    s = S.s
    sel_open = '<button aria-label="Select (V)" aria-pressed="true" style="position: relative; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; border-radius: 2px; background: rgba(47,128,237,0.18); color: #2f80ed">\n<span style="position: absolute; left: -6px; top: 0; bottom: 0; width: 2px; background: #2f80ed"></span>'
    assert s.count(sel_open) == 1
    s = s.replace(sel_open, '<button aria-label="Select (V)" style="position: relative; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; border-radius: 2px">')
    m = _re.search(r'<button aria-label="' + _re.escape(label) + r'" style="([^"]*)">', s)
    assert m, label
    new = (f'<button aria-label="{label}" aria-pressed="true" style="position: relative; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; border-radius: 2px; background: rgba(47,128,237,0.18); color: #2f80ed">'
           '\n<span style="position: absolute; left: -6px; top: 0; bottom: 0; width: 2px; background: #2f80ed"></span>')
    S.s = s[:m.start()] + new + s[m.end():]


def options_left(S, html, spacer=True):
    """Replace everything in the options bar left of the page-view controls."""
    a = S.s.index('<!-- position + size capsule -->')
    b = S.s.index('<!-- page view:', a)
    S.s = S.s[:a] + html + ('\n<span style="flex: 1"></span>\n' if spacer else '\n') + S.s[b:]


def scroll(S, y, scroll_bar_top=250):
    S.rep('<div style="position: relative; width: 1440px; transform: scale(0.85); transform-origin: 0 0;',
          f'<div style="position: relative; width: 1440px; transform: scale(0.85) translateY(-{y}px); transform-origin: 0 0;')
    fy = 32 + (900 - y) * 0.85
    if fy < 32:
        S.rep('<span aria-hidden="true" style="position: absolute; right: 54px; top: 800px;', '<span aria-hidden="true" style="display: none; position: absolute; right: 54px; top: 800px;')
    else:
        S.rep('right: 54px; top: 800px;', f'right: 54px; top: {fy + 3:.0f}px;')
    S.rep('<span aria-hidden="true" style="position: absolute; right: 3px; top: 4px; width: 4px; height: 470px;',
          f'<span aria-hidden="true" style="position: absolute; right: 3px; top: {scroll_bar_top}px; width: 4px; height: 470px;')


def add_footer(S):
    S.rep('<!-- fold line at 900 -->', '''<!-- Footer -->
<footer style="padding: 48px 64px; background: #1d1a16; color: #f6f1ea; display: flex; align-items: center; justify-content: space-between; font-size: 15px">
<span>© 2026 Halden Studio</span><span style="color: #e7d9c7">Riverside Works, Unit 4</span><span style="display: flex; gap: 24px"><a href="#ig">Instagram</a><a href="#news">Newsletter</a></span></footer>
<!-- fold line at 900 -->''')


def cap(inner, extra=''):
    return f'<div style="height: 28px; display: flex; align-items: center; gap: 2px; padding: 2px; box-sizing: border-box; background: #232323; border-radius: 6px; {extra}">{inner}</div>'


def capseg(items, sel):
    return cap(''.join(f'<button aria-pressed="{str(i == sel).lower()}" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; {"background: #333333; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #939393;"}">{t}</button>' for i, t in enumerate(items)))


def capfield(label, val, unit='', w=None, extra=''):
    ws = f'width: {w}px;' if w else ''
    u = f'<span style="font-size: 10px; color: #939393">{unit}</span>' if unit else ''
    return f'<label style="height: 24px; {ws} display: flex; align-items: center; gap: 6px; padding: 0 8px; box-sizing: border-box; border-radius: 4px; {extra}"><span style="font-size: 11px; color: #939393; white-space: nowrap">{label}</span><span style="white-space: nowrap">{val}</span>{u}</label>'


def capdiv():
    return '<span style="width: 1px; height: 14px; background: #333333"></span>'


def swatch(c, ring=False):
    r = 'box-shadow: inset 0 0 0 1px rgba(0,0,0,0.25);' if ring else ''
    return f'<span style="width: 14px; height: 14px; border-radius: 2px; background: {c}; flex: none; {r}"></span>'


def mode_chip(text):
    return f'<span style="height: 26px; display: flex; align-items: center; padding: 0 10px; border-radius: 6px; background: rgba(47,128,237,0.14); color: #a9c8f7; font-weight: 500; white-space: nowrap">{text}</span>'


def tree_rows(rows):
    """rows: (pad, chev, icon, name, tag, sel, guides, extra_badge)"""
    out = ''
    for pad, chev, ic, name, tag, sel, guides, badge in rows:
        g = ''
        if guides:
            g = 'background-image: ' + ', '.join(('linear-gradient(#303030,#303030)' if sel else 'linear-gradient(#262626,#262626)') for _ in guides) + '; background-size: ' + ', '.join('1px 100%' for _ in guides) + '; background-position: ' + ', '.join(f'{x}px 0' for x in guides) + '; background-repeat: no-repeat;'
        bg = 'background-color: rgba(47,128,237,0.18);' if sel else ''
        ch = icon('chev-down' if chev == 'open' else 'chev-right', 12, '#a8a8a8') if chev else '<span style="width: 12px"></span>'
        out += (f'<div role="treeitem"{" aria-selected=\"true\"" if sel else ""} style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 {pad}px; {bg} {g}">'
                f'{ch}{icon(ic, 14, "#e8e8e8" if sel else "#a8a8a8")}<span style="color: #e8e8e8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{name}</span>{badge}<span style="flex: 1"></span><span style="font-size: 11px; color: {"#a8a8a8" if sel else "#939393"}">{tag}</span></div>')
    return '<div role="tree" aria-label="Layers" style="display: flex; flex-direction: column; font-size: 12px">\n' + out + '\n</div>\n'


def set_tree(S, rows):
    S.cut('<div role="tree" aria-label="Layers"', '</aside>', tree_rows(rows))


def hero_tree(sel=None, extra_after=None):
    """Standard Halden tree with Hero expanded; sel = name to select."""
    G = lambda *x: x
    rows = [
        (8, 'open', 't-section', 'Header', 'header', False, (), ''),
        (20, None, 't-para', 'Wordmark “Halden”', 'p', False, G(14), ''),
        (20, 'closed', 't-row', 'Nav links', 'nav', False, G(14), ''),
        (20, None, 't-button', 'Book a visit', 'a', False, G(14), ''),
        (8, 'open', 't-section', 'Hero', 'section', False, (), ''),
        (20, 'open', 't-grid', 'Hero grid', 'div', False, G(14), ''),
        (32, 'open', 't-stack', 'Hero text', 'div', False, G(14, 26), ''),
        (44, None, 't-para', '“Small-batch stoneware…”', 'p', False, G(14, 26, 38), ''),
        (44, None, 't-heading', 'Hero title', 'h1', False, G(14, 26, 38), ''),
        (44, None, 't-para', '“Each piece is…”', 'p', False, G(14, 26, 38), ''),
        (44, 'closed', 't-row', 'Hero buttons', 'div', False, G(14, 26, 38), ''),
        (32, None, 't-image', 'Hero image', 'img', False, G(14, 26), icon('warning', 12, '#d29922', 1.25, 'Accessibility issue')),
        (8, 'closed', 't-section', 'This season', 'section', False, (), icon('desktop', 12, '#d29922', 1.25, 'Overrides at smaller sizes')),
        (8, 'closed', 't-section', 'Footer', 'footer', False, (), ''),
    ]
    out = []
    for r in rows:
        r = list(r)
        if r[3] == sel:
            r[5] = True
        out.append(tuple(r))
        if extra_after and r[3] == extra_after[0]:
            out.extend(extra_after[1])
    return out


def season_tree(sel=(), open_cards=False, extra=()):
    G = lambda *x: x
    rows = [(8, 'closed', 't-section', 'Header', 'header', False, (), ''),
            (8, 'closed', 't-section', 'Hero', 'section', False, (), ''),
            (8, 'open', 't-section', 'This season', 'section', False, (), ''),
            (20, 'closed', 't-row', 'Season heading', 'div', 'Season heading' in sel, G(14), ''),
            (20, 'open', 't-grid', 'Card grid', 'div', 'Card grid' in sel, G(14), '')]
    rows += [(32, 'closed', 't-stack', f'Card {i}', 'div', f'Card {i}' in sel, G(14, 26), '') for i in (1, 2, 3)]
    rows += list(extra)
    rows += [(8, 'closed', 't-section', 'Footer', 'footer', 'Footer' in sel, (), '')]
    return rows
