import sys, re
sys.path.insert(0, '/home/claude/ds')
from lib import *
import wiz as WZ
PR = WZ.scale(WZ.T['primary']); SE = WZ.scale(WZ.T['secondary']); NE = WZ.NEUTRAL

s = open('/home/claude/daisy/project/Main.dc.html', encoding='utf-8').read()


def between(start, end, new, include_end=False):
    global s
    a = s.index(start)
    b = s.index(end, a)
    if include_end:
        b += len(end)
    s = s[:a] + new + s[b:]


def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:80], s.count(old))
    s = s.replace(old, new)


rep('<title>Daisy · D-04 Editor, heading selected</title>', '<title>Daisy · D-03 Editor, fresh project</title>')

# ---- top bar search ----
rep('aria-label="Search Halden: pages, layers, assets and commands"', 'aria-label="Search Mossbank Tea: pages, layers, assets and commands"')
rep('Search <span style="color: #e8e8e8; font-weight: 500">Halden</span>', 'Search <span style="color: #e8e8e8; font-weight: 500">Mossbank Tea</span>')

# ---- options bar ----
rep('<span style="font-size: 11px; color: #939393">Y</span><span>64</span>', '<span style="font-size: 11px; color: #939393">Y</span><span>0</span>')
rep('<label title="Width · 560px"', '<label title="Width · fills the page"')
rep('<span style="width: 30px">560</span><span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">Fixed</span>',
    '<span style="width: 30px; color: #a8a8a8">1440</span><span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">Fill</span>')
rep('<span style="width: 30px; color: #a8a8a8">202</span>', '<span style="width: 30px; color: #a8a8a8">400</span>')

# ---- project tree ----
pt_row = lambda pad, inner, extra='': f'<div role="treeitem" {extra} style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 {pad}px">{inner}</div>'
project_tree = '<div role="tree" aria-label="Project files" style="padding-top: 4px">\n' + \
    pt_row(8, icon('chev-down', 12, '#a8a8a8') + icon('folder', 14, '#e8e8e8') + '<span style="flex: 1; font-weight: 600">Mossbank Tea</span>', 'aria-expanded="true"') + \
    pt_row(20, '<span style="color: #a8a8a8; display: flex">' + icon('chev-down', 12) + '</span><span style="flex: 1; color: #a8a8a8">Pages</span><span style="font-size: 11px; color: #939393">1</span>', 'aria-expanded="true"') + \
    f'<div role="treeitem" aria-current="page" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 44px; background: #2a2a2a">{icon("file", 14, "#e8e8e8")}<span style="flex: 1; font-weight: 500">Home</span><span style="font-family: {MONO}; font-size: 11px; color: #939393">index.html</span></div>' + \
    pt_row(20, '<span style="color: #a8a8a8; display: flex">' + icon('chev-right', 12) + '</span><span style="flex: 1; color: #a8a8a8">Design system</span><span style="display: flex; gap: 2px" aria-label="Mossbank Tea colours">' + ''.join(f'<span style="width: 8px; height: 8px; border-radius: 2px; background: {c}; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.1)"></span>' for c in [PR[6], SE[5], NE[9], NE[0], NE[2]]) + '</span>', 'aria-expanded="false"') + \
    pt_row(20, '<span style="color: #a8a8a8; display: flex">' + icon('chev-right', 12) + '</span><span style="flex: 1; color: #a8a8a8">Assets</span><span style="font-size: 11px; color: #939393">0</span>', 'aria-expanded="false"') + \
    '\n</div>\n'
between('<div role="tree" aria-label="Project files"', '</section>', project_tree)

# ---- layers tree ----
layers = f'''<div role="tree" aria-label="Layers" style="display: flex; flex-direction: column; font-size: 12px">
<div role="treeitem" aria-selected="true" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 8px; background: rgba(47,128,237,0.18)">
<span style="width: 12px"></span>{icon('t-section', 14, '#e8e8e8')}<span style="flex: 1">Section</span><span style="font-size: 11px; color: #a8a8a8">section</span>
</div>
</div>
'''
between('<div role="tree" aria-label="Layers"', '</aside>', layers)

# ---- page tabs: only Home ----
a = s.index('<button role="tab" aria-selected="false" title="Shop · unsaved changes"')
b = s.index('<button aria-label="New page" title="New page · Ctrl+N" style="width: 32px; height: 32px;')
s = s[:a] + s[b:]

ds_tab = f'''<button role="tab" aria-selected="false" title="Opened after creating · 142 tokens" style="height: 32px; box-sizing: border-box; display: flex; align-items: center; gap: 8px; padding: 0 8px 0 12px; border-right: 1px solid #262626; color: #a8a8a8">{icon('palette', 12)}<span>Design system</span><span style="font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 11px; color: #939393">tokens.css</span><span style="width: 18px; height: 18px"></span></button>
'''
s = s.replace('<button aria-label="New page" title="New page · Ctrl+N" style="width: 32px; height: 32px;', ds_tab + '<button aria-label="New page" title="New page · Ctrl+N" style="width: 32px; height: 32px;', 1)

# ---- canvas page ----
new_canvas = f'''<span style="position: absolute; left: 46px; top: 13px; font-size: 11px; line-height: 11px; color: #939393">Desktop · 1440</span>

<!-- page frame: 1440 @ 85% = 1224 · fresh page: one empty section, 400 high (340 on screen) -->
<div style="position: absolute; left: 46px; top: 32px; width: 1224px; height: 340px; overflow: visible; outline: 1px solid #3c3c3c; background: #fbfaf7">
<div style="position: relative; width: 1440px; transform: scale(0.85); transform-origin: 0 0; background: #fbfaf7; color: #2a2824; font-family: 'Inter', sans-serif; font-size: 16px; line-height: 1.5">
<section style="position: relative; height: 400px">
<!-- empty-section hint (overlay, not part of the page) -->
<div aria-hidden="true" style="position: absolute; left: 9.4px; top: 9.4px; right: 9.4px; bottom: 9.4px; border: 1.18px dashed #c8c8c8; display: flex; align-items: center; justify-content: center">
<span style="font-size: 15.3px; color: #9a9a9a">Empty section — pick a tool and click here</span></div>
<!-- selection overlay -->
<div aria-hidden="true" style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; border: 1.76px solid #2f80ed; pointer-events: none">
<span style="position: absolute; left: -1.76px; top: 4px; height: 21px; padding: 0 5px; display: flex; align-items: center; background: #246bcb; color: #ffffff; font: 500 13px/1 'Inter', sans-serif; white-space: nowrap">Section · section</span>
{''.join(f'<span style="position: absolute; {pos}; width: 9.4px; height: 9.4px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>' for pos in ['left: -5.6px; top: -5.6px', 'left: calc(50% - 4.7px); top: -5.6px', 'right: -5.6px; top: -5.6px', 'right: -5.6px; top: calc(50% - 4.7px)', 'right: -5.6px; bottom: -5.6px', 'left: calc(50% - 4.7px); bottom: -5.6px', 'left: -5.6px; bottom: -5.6px', 'left: -5.6px; top: calc(50% - 4.7px)'])}
{''.join(f'<span style="position: absolute; {pos}; width: 7px; height: 7px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 50%"></span>' for pos in ['left: 8.3px; top: 30px', 'right: 8.3px; top: 30px', 'right: 8.3px; bottom: 8.3px', 'left: 8.3px; bottom: 8.3px'])}
</div>
</section>
</div>
</div>
<!-- add section bar: 8 px under the page, page width, 32 high -->
<button style="position: absolute; left: 46px; top: 380px; width: 1224px; height: 32px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; gap: 6px; border: 1px dashed #454545; color: #a8a8a8">{icon('plus', 12, 'currentColor', 1.75)}Add section</button>
</main>'''
between('<span style="position: absolute; left: 46px; top: 13px;', '</main>', new_canvas, include_end=True)

# ---- properties ----
f = lambda inner, extra='': f'<label style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px; background: #2a2a2a; border-radius: 2px; {extra}">{inner}</label>'
dot = '<span style="width: 5px; height: 5px; border-radius: 3px; background: #2f80ed; flex: none"></span>'
tagc = lambda t: f'<span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">{t}</span>'
adv = lambda t: f'<button aria-label="{t} · Advanced" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; color: #939393">{icon("sliders", 14)}</button>'
mp = lambda n, v='': f'<button class="mp-row" aria-label="Open {n}" style="width: 100%; height: 28px; display: flex; align-items: center; padding: 0 8px 0 12px; box-sizing: border-box; border-radius: 0; color: #a8a8a8"><span style="flex: 1; text-align: left">{n}</span>' + (f'<span style="font-size: 11px; color: #939393">{v}</span>' if v else '') + f'<span class="mp-add" aria-hidden="true" style="width: 18px; height: 18px; margin-left: 8px; display: flex; align-items: center; justify-content: center; border-radius: 3px; color: #e8e8e8">{icon("plus", 12, "currentColor", 1.75)}</span></button>'

props = f'''<!-- Properties: fresh section -->
<section aria-label="Properties" style="position: relative; flex: 1; min-height: 0; overflow: hidden; font-variant-numeric: tabular-nums">
<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{icon('t-section', 16, '#a8a8a8')}<span style="flex: 1; font-weight: 500">Section</span>
<button aria-label="State: Normal" style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 6px; border-radius: 2px; color: #a8a8a8">Normal{icon('chev-down', 10, 'currentColor', 1.5)}</button></div>
<div style="display: flex; align-items: center; gap: 6px; padding-left: 24px; font-size: 11px; color: #a8a8a8"><button style="display: flex; align-items: center; gap: 3px">Section{icon('chev-down', 10, 'currentColor', 1.5)}</button><span style="color: #454545">·</span><span style="font-family: {MONO}; color: #939393">section</span></div>
</div>

<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">
<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">Size</span>{adv('Size')}</div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">
{f('<span style="font-size: 11px; color: #939393; padding-left: 11px">W</span><span style="flex: 1; color: #939393">1440</span>' + tagc('Fill'), '')}
{f('<span style="font-size: 11px; color: #939393; padding-left: 11px">H</span><span style="flex: 1; color: #939393">400</span>' + tagc('Fit'), '')}
</div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">
<span></span>
{f(dot + '<span style="font-size: 11px; color: #939393">Min H</span><span style="flex: 1">400</span><span style="font-size: 10px; color: #939393">px</span>', '')}
</div>
</div>
<div style="height: 1px; background: #303030"></div>

<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">
<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">Layout</span>{adv('Layout')}</div>
<div role="group" aria-label="Arrange children" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #262626; border-radius: 4px; font-size: 11px">
<button aria-pressed="true" style="height: 22px; display: flex; align-items: center; justify-content: center; gap: 6px; border-radius: 3px; background: #3a3a3a; color: #e8e8e8; font-weight: 500">{icon('t-stack', 12)}Stack</button>
<button aria-pressed="false" style="height: 22px; display: flex; align-items: center; justify-content: center; gap: 6px; border-radius: 3px; color: #939393">{icon('t-row', 12)}Row</button>
<button aria-pressed="false" style="height: 22px; display: flex; align-items: center; justify-content: center; gap: 6px; border-radius: 3px; color: #939393">{icon('t-grid', 12)}Grid</button></div>
<div style="display: flex; align-items: flex-start; gap: 6px; font-size: 11px; line-height: 16px; color: #58a6ff">{icon('info', 12, '#58a6ff', 1.25)}<span style="flex: 1">Stack places children one under another. Choose Row or Grid to align and space them.</span><button aria-label="Dismiss hint for good" style="width: 16px; height: 16px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon('close', 10, 'currentColor', 1.75)}</button></div>
</div>
<div style="height: 1px; background: #303030"></div>

<div style="padding: 8px 0 0">
<div style="padding: 0 12px 4px; font-size: 10px; line-height: 14px; font-weight: 500; letter-spacing: 0.04em; color: #939393">MORE PROPERTIES</div>
{mp('Placement', 'In flow')}{mp('Spacing', '0')}{mp('Fill', 'none')}{mp('Border', 'none')}{mp('Effects')}{mp('Transform')}{mp('Visibility', 'All sizes')}{mp('Transition &amp; Animation')}{mp('Accessibility', 'Landmark')}{mp('Attributes &amp; Custom CSS')}
</div>
</section>
'''
between('<!-- Properties v2 (decluttered) -->', '<!-- Swatches | History (h220) -->', props + '\n')

# ---- swatches: empty design system ----
a = s.index('<div style="padding: 10px 12px 0">', s.index('aria-label="Swatches and History"'))
b = s.index('</section>', a)
cols = [('primary-600', PR[6]), ('secondary-500', SE[5]), ('neutral-900', NE[9]), ('neutral-600', NE[6]), ('neutral-200', NE[2]), ('neutral-50', NE[0]), ('success', '#2f8a4c'), ('danger', '#c4352b')]
ts = [("'Fraunces', serif", 600, 22, 'Display', 'Fraunces 37–49'), ("'Fraunces', serif", 600, 18, 'H1', 'Fraunces 31–39'), ("'Inter', sans-serif", 400, 15, 'Body', 'Inter 15–16')]
sw = f'''<div style="padding: 10px 12px 0">
<div style="display: flex; align-items: center; justify-content: space-between; font-size: 11px; color: #a8a8a8; margin-bottom: 6px"><span>Colours</span><span style="font-size: 10px; color: #939393">From Mossbank Tea design system</span></div>
<div style="display: flex; gap: 6px">{''.join(f'<button aria-label="{n} · {c}" style="width: 24px; height: 24px; box-sizing: border-box; border-radius: 2px; background: {c}; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.1)"></button>' for n, c in cols)}</div>
<div style="font-size: 11px; color: #a8a8a8; margin: 10px 0 0">Text styles</div>
<div style="display: flex; flex-direction: column">{''.join(f'<div style="height: 32px; display: flex; align-items: center; gap: 10px"><span style="width: 28px; font-family: {ff}; font-size: {px}px; font-weight: {fw}; line-height: 1">Ag</span><span style="flex: 1">{n}</span><span style="font-size: 11px; color: #939393">{spec}</span></div>' for ff, fw, px, n, spec in ts)}</div>
</div>
'''
s = s[:a] + sw + s[b:]

# ---- status bar ----
a = s.index('<nav aria-label="Selection path"')
b = s.index('</footer>', a)
s = s[:a] + '''<nav aria-label="Selection path" style="flex: 1; display: flex; align-items: center; gap: 6px; color: #a8a8a8; white-space: nowrap">
<button>Page</button><span aria-hidden="true">›</span>
<button aria-current="true" style="color: #e8e8e8">Section</button>
</nav>
<span role="status" style="flex: 1; display: flex; align-items: center; justify-content: center; gap: 6px; white-space: nowrap">''' + icon("check", 12, "#3fb950", 2) + '''<span style="color: #c8c8c8">Mossbank Tea created · 142 tokens</span><span style="color: #454545">·</span><span style="color: #939393">Pick a tool and click inside the section</span></span>
<span style="flex: 1; display: flex; align-items: center; justify-content: flex-end; gap: 10px; color: #a8a8a8; white-space: nowrap">''' + open('/home/claude/ds/zoom_snip.html').read() + '''
<span aria-hidden="true" style="width: 1px; height: 12px; background: #303030"></span>
<span title="Page size at this screen size">1440 × 400</span></span>
''' + s[b:]

open('/home/claude/daisy/project/D03-Editor-Fresh.dc.html', 'w', encoding='utf-8').write(s)
print('ok')
