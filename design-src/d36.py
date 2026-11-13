import re
from screen import *

S = Screen('Daisy · D-36 Design system editor')
P['palette'] = ('stroke', 'M8 1.5a6.5 6.5 0 1 0 0 13c1 0 1.5-.6 1.5-1.4 0-1.2-1-1.3-1-2.3 0-.8.6-1.3 1.5-1.3h1.6a2.9 2.9 0 0 0 2.9-2.9C14.5 4 11.6 1.5 8 1.5z')
MONO_ = "font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 11px"
U = lambda n: f'<span style="font-size: 11px; color: #939393; font-variant-numeric: tabular-nums">{n} uses</span>' if n else '<span style="height: 16px; padding: 0 6px; border-radius: 3px; background: #333333; font-size: 10px; line-height: 16px; color: #a8a8a8">Unused</span>'

# ── page tabs: Home inactive, Design system tab active ──
S.rep('<button role="tab" aria-selected="true" style="position: relative; height: 32px; box-sizing: border-box; display: flex; align-items: center; gap: 8px; padding: 0 8px 0 12px; background: #2a2a2a; border-right: 1px solid #303030; margin-bottom: -1px">\n<span style="position: absolute; left: 0; right: 0; top: 0; height: 2px; background: #2f80ed"></span>\n<span style="font-weight: 500; color: #e8e8e8">Home</span>',
      '<button role="tab" aria-selected="false" style="height: 32px; box-sizing: border-box; display: flex; align-items: center; gap: 8px; padding: 0 8px 0 12px; border-right: 1px solid #262626; color: #a8a8a8">\n<span>Home</span>')
S.rep('index.html @ 85%', 'index.html')
a = S.s.index('<span aria-label="Close Home"'); b = S.s.index('</button>', a)
S.s = S.s[:a] + '<span style="width: 18px; height: 18px"></span>\n' + S.s[b:]
ds_tab = f'''<button role="tab" aria-selected="true" style="position: relative; height: 32px; box-sizing: border-box; display: flex; align-items: center; gap: 8px; padding: 0 8px 0 12px; background: #1f1f1f; border-right: 1px solid #303030; margin-bottom: -1px">
<span style="position: absolute; left: 0; right: 0; top: 0; height: 2px; background: #2f80ed"></span>{icon('palette', 13, '#e8e8e8')}
<span style="font-weight: 500; color: #e8e8e8">Design system</span><span style="{MONO_}; color: #939393">tokens.css</span>
<span aria-label="Close Design system" style="width: 18px; height: 18px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon('close', 10, 'currentColor', 2)}</span></button>
'''
i = S.s.index('<button role="tab" aria-selected="false" title="Shop · unsaved changes"')
S.s = S.s[:i] + ds_tab + S.s[i:]

# ── options bar: token tools only (no page view controls here) ──
find = f'<label style="width: 260px; height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 10px; box-sizing: border-box; border-radius: 6px; background: #232323; color: #939393">{icon("search", 13)}Find a token<span style="flex: 1"></span><span style="font-size: 10px; padding: 0 4px; border-radius: 3px; box-shadow: inset 0 0 0 1px #454545">Ctrl F</span></label>'
opt = (find + capseg(['All', 'Used', 'Unused · 1'], 0)
       + '\n<span style="flex: 1"></span>\n'
       + cap(f'<button style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; color: #e8e8e8">{icon("eyedropper", 13, "#a8a8a8")}Collect from pages…</button>{capdiv()}<button style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; color: #e8e8e8">{icon("upload", 13, "#a8a8a8")}Import</button>')
       + '\n<button aria-label="More options" style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 6px; color: #a8a8a8; background: #232323">' + icon('more', 14) + '</button>\n')
a = S.s.index('<!-- position + size capsule -->'); b = S.s.index('</div>\n\n<!-- ═══════════ MAIN ROW')
S.s = S.s[:a] + opt + S.s[b:]

# ── tool strip: page tools do not apply in this tab ──
S.rep('<div role="toolbar" aria-label="Tools" aria-orientation="vertical" style="', '<div role="toolbar" aria-label="Tools · page tools are off in the design system" aria-orientation="vertical" style="opacity: 0.35; ')

# ── Project tree: Design system is the open item ──
S.rep('<div role="treeitem" aria-current="page" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 44px; background: #2a2a2a">\n<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#e8e8e8"',
      '<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 44px">\n<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#a8a8a8"')
S.rep('<span style="flex: 1; color: #e8e8e8; font-weight: 500">Home</span>', '<span style="flex: 1">Home</span>')
S.rep('<div role="treeitem" aria-expanded="false" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 20px">\n<svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="#a8a8a8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 4l4 4-4 4"></path></svg>\n<span style="flex: 1; color: #a8a8a8">Design system</span>',
      f'<div role="treeitem" aria-current="page" aria-expanded="false" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 20px; background: #2a2a2a">\n<span style="width: 12px"></span>{icon("palette", 13, "#e8e8e8")}\n<span style="flex: 1; color: #e8e8e8; font-weight: 500">Design system</span>')

# ── Layers: nothing to show for this tab ──
a = S.s.index('<div style="display: flex; gap: 4px; padding: 8px 12px 4px">\n<label style="flex: 1; height: 24px;')
b = S.s.index('</aside>', a)
S.s = S.s[:a] + '''<div style="padding: 28px 24px; display: flex; flex-direction: column; align-items: center; gap: 6px; text-align: center">
<span style="font-weight: 500; color: #a8a8a8">No layers here</span>
<span style="font-size: 11px; line-height: 16px; color: #939393">Layers show the page in the active tab. Open a page to see where a token is used.</span></div>
''' + S.s[b:]

# ── main: the token editor ──
COL = [('brand', '#b5532d', 'Buttons, links, highlights', 18, True), ('brand-deep', '#9e4626', 'Button hover', 6, False),
       ('brand-light', '#c86a43', '', 0, False), ('ink', '#1d1a16', 'Headings and body text', 42, False),
       ('ink-soft', '#4a443c', 'Secondary text', 11, False), ('sand', '#f6f1ea', 'Page background', 4, False),
       ('clay', '#e7d9c7', 'Section background', 5, False), ('moss', '#5f6b4e', 'Labels and prices', 9, False)]
def crow(n, c, note, uses, sel):
    light = contrast(c, '#ffffff') < 3
    return (f'<div role="row" aria-selected="{str(sel).lower()}" style="height: 36px; display: grid; grid-template-columns: 28px 150px 190px 92px minmax(0, 1fr) 90px; align-items: center; gap: 12px; padding: 0 12px; border-radius: 4px; {"background: rgba(47,128,237,0.18); box-shadow: inset 0 0 0 1px #2f80ed;" if sel else ""}">'
            f'<span style="width: 24px; height: 24px; border-radius: 4px; background: {c}; {"box-shadow: inset 0 0 0 1px rgba(0,0,0,0.25);" if light else "box-shadow: inset 0 0 0 1px rgba(255,255,255,0.08);"}"></span>'
            f'<span style="font-weight: 500; color: #e8e8e8">{n}</span><span style="{MONO_}; color: #939393">--color-{n}</span>'
            f'<span style="{MONO_}; color: #c8c8c8">{c.upper()}</span><span style="font-size: 11px; color: #939393; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{note}</span>'
            f'<span style="justify-self: end">{U(uses)}</span></div>')
sec = lambda title, n, right='': f'<div style="height: 32px; display: flex; align-items: center; gap: 8px; padding: 0 12px"><span style="font-weight: 600">{title}</span><span style="font-size: 11px; color: #939393">{n}</span><span style="flex: 1"></span>{right}</div>'
addb = lambda t: f'<button style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; color: #a8a8a8">{icon("plus", 11, "currentColor", 1.75)}{t}</button>'
colours = sec('Colours', '8', addb('Colour')) + ''.join(crow(*r) for r in COL)

TS = [('Display', "'Fraunces', serif", 600, 30, 'Fraunces 64 / 1.05 · Semibold', 'h1', 4), ('Heading 2', "'Fraunces', serif", 600, 24, 'Fraunces 40 / 1.2 · Semibold', 'h2', 7),
      ('Heading 3', "'Fraunces', serif", 400, 18, 'Fraunces 20 / 1.3 · Regular', 'h3', 12), ('Body', "'Inter', sans-serif", 400, 15, 'Inter 16 / 1.5 · Regular', 'p', 38),
      ('Eyebrow', "'Inter', sans-serif", 500, 11, 'Inter 13 / 20 · Medium · caps · 0.08em', 'p', 5)]
def trow(n, ff, fw, px, spec, tag, uses):
    sample = 'SMALL-BATCH STONEWARE' if n == 'Eyebrow' else 'Hand-thrown ceramics'
    ls = 'letter-spacing: 0.08em;' if n == 'Eyebrow' else ''
    return (f'<div role="row" style="height: 48px; display: grid; grid-template-columns: 340px 220px 60px minmax(0, 1fr) 90px; align-items: center; gap: 12px; padding: 0 12px; border-radius: 4px">'
            f'<span style="font-family: {ff}; font-weight: {fw}; font-size: {px}px; line-height: 1.1; color: #e8e8e8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; {ls}">{sample}</span>'
            f'<span style="display: flex; flex-direction: column"><span style="font-weight: 500">{n}</span><span style="font-size: 11px; color: #939393">{spec}</span></span>'
            f'<span style="{MONO_}; color: #939393">{tag}</span><span style="font-size: 11px; color: #939393">{"Fluid 44–64" if n == "Display" else ""}</span><span style="justify-self: end">{U(uses)}</span></div>')
texts = sec('Text styles', '5', addb('Text style')) + ''.join(trow(*r) for r in TS)

RAD = [('radius-sm', 4, 6), ('radius-md', 12, 14), ('radius-lg', 20, 3), ('pill', 999, 9)]
rad = sec('Radius', '4', addb('Radius')) + '<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; padding: 0 12px">' + ''.join(
    f'<div style="padding: 10px; display: flex; align-items: center; gap: 10px; border-radius: 6px; background: #262626"><span style="width: 34px; height: 24px; flex: none; border: 1.5px solid #a8a8a8; border-radius: {min(r, 12)}px {min(r, 12)}px {min(r, 12)}px {min(r, 12)}px"></span>'
    f'<span style="display: flex; flex-direction: column; min-width: 0"><span style="font-weight: 500">{n}</span><span style="font-size: 11px; color: #939393">{r} px · {u} uses</span></span></div>' for n, r, u in RAD) + '</div>'
SP = [('xs', 8), ('sm', 16), ('md', 24), ('lg', 32), ('xl', 48), ('2xl', 64), ('3xl', 72), ('4xl', 96)]
space = sec('Spacing', '8', addb('Space')) + '<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 2px 24px; padding: 0 12px">' + ''.join(
    f'<div style="height: 22px; display: grid; grid-template-columns: 40px 44px minmax(0, 1fr); align-items: center; gap: 8px"><span style="font-weight: 500">{n}</span><span style="font-size: 11px; color: #939393; text-align: right; font-variant-numeric: tabular-nums">{v} px</span>'
    f'<span style="height: 8px; width: {round(v * 1.1)}px; border-radius: 2px; background: rgba(26,146,132,0.55)"></span></div>' for n, v in SP) + '</div>'

# live preview: Halden home at 26%, uses of brand outlined
def mark(l, t, w, h): return f'<span style="position: absolute; left: {l}px; top: {t}px; width: {w}px; height: {h}px; outline: 1.5px solid #2f80ed; outline-offset: 2px; border-radius: 2px"></span>'
prev_page = f'''<div style="position: relative; width: 376px; height: 470px; border-radius: 4px; overflow: hidden; background: #f6f1ea; box-shadow: 0 0 0 1px #3c3c3c">
<span style="position: absolute; left: 17px; top: 14px; font: 600 11px/1 'Fraunces', serif; color: #1d1a16">Halden</span>
<span style="position: absolute; left: 160px; top: 15px; display: flex; gap: 10px; font-size: 6px; color: #1d1a16"><span>Work</span><span>Shop</span><span>Journal</span><span>Visit</span></span>
<span style="position: absolute; right: 17px; top: 10px; width: 50px; height: 15px; border-radius: 8px; background: #b5532d"></span>
<span style="position: absolute; left: 17px; top: 60px; font-size: 5px; letter-spacing: 0.08em; color: #5f6b4e">SMALL-BATCH STONEWARE · EST. 2014</span>
<span style="position: absolute; left: 17px; top: 72px; width: 160px; font: 600 19px/1.05 'Fraunces', serif; color: #1d1a16">Hand-thrown ceramics for everyday tables</span>
<span style="position: absolute; left: 17px; top: 142px; width: 140px; font-size: 6px; line-height: 1.5; color: #4a443c">Each piece is wheel-thrown, glazed and fired in our studio by the river.</span>
<span style="position: absolute; left: 17px; top: 168px; width: 66px; height: 16px; border-radius: 8px; background: #b5532d"></span>
<span style="position: absolute; left: 90px; top: 172px; font-size: 6px; color: #1d1a16">Our process →</span>
<span style="position: absolute; right: 17px; top: 52px; width: 152px; height: 140px; border-radius: 4px; background: #e6dccd"></span>
<span style="position: absolute; left: 0; right: 0; top: 230px; bottom: 0; background: #e7d9c7"></span>
<span style="position: absolute; left: 17px; top: 252px; font: 600 12px/1 'Fraunces', serif; color: #1d1a16">This season</span>
<span style="position: absolute; right: 17px; top: 254px; font-size: 6px; color: #b5532d">View all →</span>
{''.join(f'<span style="position: absolute; left: {17 + i * 116}px; top: 278px; width: 108px; height: 120px; border-radius: 4px; background: #ffffff"><span style="position: absolute; left: 6px; right: 6px; top: 6px; height: 78px; border-radius: 3px; background: {c}"></span><span style="position: absolute; left: 6px; top: 92px; font: 7px Fraunces, serif; color: #1d1a16">{t}</span><span style="position: absolute; left: 6px; top: 104px; font-size: 6px; color: #5f6b4e">{p}</span></span>' for i, (c, t, p) in enumerate([('#d8cbb8', 'Tide bowl', '€38'), ('#cfb9a3', 'Ember mug', '€26'), ('#ddd2c2', 'Linen plate set', '€84')]))}
{mark(309, 10, 50, 15)}{mark(17, 168, 66, 16)}{mark(326, 252, 33, 9)}
</div>'''
preview = f'''<aside aria-label="Live preview" style="width: 420px; flex: none; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px; padding: 14px 22px; border-left: 1px solid #303030; background: #262626">
<div style="display: flex; align-items: center; gap: 8px"><span style="font-size: 10px; font-weight: 500; letter-spacing: 0.06em; color: #939393">LIVE PREVIEW</span><span style="flex: 1"></span>
<button style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; box-shadow: inset 0 0 0 1px #454545; color: #e8e8e8">Home<span style="{MONO_}; color: #939393">index.html</span>{icon("chev-down", 10, "#939393", 1.75)}</button></div>
{prev_page}
<div style="display: flex; align-items: center; gap: 8px; font-size: 11px; line-height: 16px; color: #a8a8a8"><span style="width: 12px; height: 12px; flex: none; outline: 1.5px solid #2f80ed; outline-offset: -1px; border-radius: 2px"></span><span>Outlined: where <b style="font-weight: 600; color: #e8e8e8">brand</b> is used on this page. Edits show here at once.</span></div>
</aside>'''
editor = f'''<main aria-label="Design system editor" style="position: relative; flex: 1; min-height: 0; overflow: hidden; display: flex; background: #1f1f1f">
<div style="flex: 1; min-width: 0; padding: 12px 16px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px; overflow: hidden">
<div style="display: flex; align-items: center; gap: 10px; padding: 0 12px 4px"><span style="font-size: 14px; font-weight: 600">Halden design system</span><span style="font-size: 11px; color: #939393">Used by 4 pages · 25 tokens</span>
<span style="flex: 1"></span><nav aria-label="Jump to" style="display: flex; gap: 2px; font-size: 11px">{''.join(f'<button style="height: 22px; padding: 0 8px; border-radius: 3px; {"background: #333333; color: #e8e8e8; font-weight: 500;" if i == 0 else "color: #a8a8a8;"}">{t}</button>' for i, t in enumerate(['Colours', 'Text styles', 'Radius', 'Spacing']))}</nav></div>
<section>{colours}</section>
<div style="height: 1px; background: #2a2a2a; margin: 0 12px"></div>
<section>{texts}</section>
<div style="height: 1px; background: #2a2a2a; margin: 0 12px"></div>
<div style="display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 24px"><section>{rad}</section><section>{space}</section></div>
</div>
<span aria-hidden="true" style="position: absolute; right: 424px; top: 6px; width: 4px; height: 640px; border-radius: 2px; background: #454545"></span>
{preview}
</main>'''
a = S.s.index('<main aria-label="Canvas"'); b = S.s.index('</main>', a) + len('</main>')
S.s = S.s[:a] + editor + S.s[b:]

# ── Properties: the selected token ──
inp = lambda inner, focus=False: f'<div style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px; box-sizing: border-box; background: #2a2a2a; border-radius: 2px; {"box-shadow: inset 0 0 0 1px #2f80ed;" if focus else ""}">{inner}</div>'
def crow2(label, ratio, ok, note):
    c = '#3fb950' if ok == 'AA' else '#d29922'
    return (f'<div style="height: 26px; display: flex; align-items: center; gap: 8px">{label}<span style="flex: 1"></span>'
            f'<span style="font-size: 11px; color: #c8c8c8; font-variant-numeric: tabular-nums">{ratio}</span>'
            f'<span style="width: 78px; display: flex; align-items: center; gap: 4px; font-size: 10px; white-space: nowrap; color: {c}">{icon("check" if ok == "AA" else "warning", 11, c, 1.75)}{note}</span></div>')
chip = lambda fg, bg: f'<span style="width: 34px; height: 18px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: {bg}; color: {fg}; font: 600 10px/1 Inter, sans-serif; box-shadow: inset 0 0 0 1px rgba(0,0,0,0.15)">Aa</span>'
r1 = contrast('#ffffff', '#b5532d'); r2 = contrast('#b5532d', '#f6f1ea'); r3 = contrast('#b5532d', '#e7d9c7')
page_use = lambda n, c: f'<div style="height: 24px; display: flex; align-items: center; gap: 8px">{icon("file", 13, "#a8a8a8")}<span>{n}</span><span style="flex: 1"></span><span style="font-size: 11px; color: #939393; font-variant-numeric: tabular-nums">{c}</span>{icon("chev-right", 10, "#6b6b6b", 1.75)}</div>'
props = f'''<!-- Properties: colour token -->
<section aria-label="Properties" style="position: relative; flex: 1; min-height: 0; overflow: hidden; font-variant-numeric: tabular-nums">
<div style="padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px"><span style="width: 16px; height: 16px; border-radius: 3px; background: #b5532d"></span><span style="flex: 1; font-weight: 500">brand</span>
<button aria-label="Token menu" style="width: 22px; height: 22px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon("more", 13)}</button></div>
<div style="padding-left: 24px; font-size: 11px; color: #a8a8a8">Colour token<span style="color: #454545"> · </span><span style="{MONO_}; color: #939393">--color-brand</span></div></div>
<div style="padding: 4px 12px 12px; border-bottom: 1px solid #303030">
<div style="height: 28px; display: flex; align-items: center"><span style="font-weight: 600">Token</span></div>
<div style="display: flex; flex-direction: column; gap: 8px">
{inp('<span style="font-size: 11px; color: #939393; width: 40px">Name</span><span>brand</span>')}
{inp(f'<span style="font-size: 11px; color: #939393; width: 40px">Value</span><span style="width: 14px; height: 14px; border-radius: 2px; background: #b5532d"></span><span style="{MONO_}">B5532D</span><span style="flex: 1"></span><span style="font-size: 11px; color: #939393">100%</span>', True)}
{inp('<span style="font-size: 11px; color: #939393; width: 40px">Note</span><span>Buttons, links, highlights</span>')}
</div></div>
<div style="padding: 4px 12px 10px; border-bottom: 1px solid #303030">
<div style="height: 28px; display: flex; align-items: center"><span style="font-weight: 600">Contrast</span><span style="flex: 1"></span><span style="font-size: 11px; color: #939393">text 4.5 · large 3</span></div>
{crow2(chip('#ffffff', '#b5532d') + '<span>White on brand</span>', f'{r1:.1f}:1', 'AA', 'AA')}
{crow2(chip('#b5532d', '#f6f1ea') + '<span>Brand on sand</span>', f'{r2:.1f}:1', 'AA' if r2 >= 4.5 else 'L', 'AA' if r2 >= 4.5 else 'Large only')}
{crow2(chip('#b5532d', '#e7d9c7') + '<span>Brand on clay</span>', f'{r3:.1f}:1', 'AA' if r3 >= 4.5 else 'L', 'AA' if r3 >= 4.5 else 'Large only')}
<div style="margin-top: 2px; font-size: 11px; line-height: 15px; color: #939393">Small text (“View all →”) needs 4.5. <b style="font-weight: 500; color: #c8c8c8">brand-deep</b> passes on both (4.5 and 5.6). <button style="font-size: 11px; color: #a9c8f7">Use it for links</button></div>
</div>
<div style="padding: 4px 12px 10px; border-bottom: 1px solid #303030">
<div style="height: 28px; display: flex; align-items: center"><span style="font-weight: 600">Used on</span><span style="flex: 1"></span><span style="font-size: 11px; color: #939393">18 uses · 4 pages</span></div>
{page_use('Home', 3)}{page_use('Shop', 9)}{page_use('Journal', 4)}{page_use('Visit', 2)}
</div>
<div style="padding: 10px 12px; display: flex; gap: 8px">
<button style="height: 24px; padding: 0 10px; border-radius: 4px; box-shadow: inset 0 0 0 1px #454545; color: #e8e8e8">Duplicate</button>
<button title="brand is used 18 times: pick a token to use instead" style="height: 24px; padding: 0 10px; border-radius: 4px; box-shadow: inset 0 0 0 1px #454545; color: #ff938c">Replace and delete…</button></div>
</section>
'''
S.cut('<!-- Properties v2 (decluttered) -->', '<!-- Swatches | History (h220) -->', props)

# ── Swatches | History → History (Swatches would repeat the editor) ──
a = S.s.index('<!-- Swatches | History (h220) -->'); b = S.s.index('</aside>', a)
hrow = lambda t, sub, on=False: f'<div style="height: 34px; display: flex; flex-direction: column; justify-content: center; padding: 0 12px; line-height: 15px; {"background: rgba(47,128,237,0.18);" if on else ""}"><span style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{t}</span><span style="font-size: 10px; line-height: 12px; color: #939393">{sub}</span></div>'
S.s = S.s[:a] + f'''<!-- History (Swatches hidden: the editor shows the tokens) -->
<section aria-label="History" style="height: 220px; flex: none; box-sizing: border-box; display: flex; flex-direction: column; border-top: 1px solid #303030">
<div role="tablist" style="height: 32px; flex: none; display: flex; align-items: stretch; gap: 16px; padding: 0 12px; border-bottom: 1px solid #303030">
<button role="tab" aria-selected="false" title="Swatches are the colours above in this tab" style="font-weight: 500; color: #6b6b6b">Swatches</button>
<button role="tab" aria-selected="true" style="position: relative; font-weight: 500">History<span style="position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: #2f80ed"></span></button></div>
<div style="padding-top: 4px">{hrow('brand · #B85A33 → #B5532D', 'Now · 18 uses on 4 pages', True)}{hrow('Renamed terracotta → brand', '13:12')}{hrow('Added brand-light', '13:10')}{hrow('Body · 15 → 16 px', '12:58 · 38 uses')}{hrow('Opened design system', '12:57')}</div>
</section>
''' + S.s[b:]

# ── status bar ──
S.status(['Design system', 'Colours', 'brand'], 'Changes apply to every page · Ctrl+Z undoes', '18 uses')
S.s = re.sub(r'<label title="Zoom · type a value[\s\S]*?</label>\s*<span aria-hidden="true" style="width: 1px; height: 12px; background: #303030"></span>', '', S.s, count=1)
S.rep('<span title="Page size at this screen size">1440 × 2050</span><span aria-hidden="true" style="color: #4f4f4f">·</span><span title="Pointer position on the page">18 uses</span>', '<span>25 tokens</span><span aria-hidden="true" style="color: #4f4f4f">·</span><span>brand · 18 uses</span>')
S.save('D36-DesignSystem.dc.html')
print('ok')
