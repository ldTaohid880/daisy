import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

s = open('/home/claude/daisy/project/Main.dc.html', encoding='utf-8').read()


def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:90], s.count(old))
    s = s.replace(old, new)


rep('<title>Daisy · D-04 Editor, heading selected</title>', '<title>Daisy · D-05 Hover vs selection vs scope</title>')

# 1. remove the h1 selection overlay
a = s.index('<!-- selection overlay (screen-constant thickness: values ÷ 0.85) -->')
b = s.index('</div>\n</div>\n<p style="margin: 0; font-size: 18px', a)
s = s[:a] + s[b + len('</div>\n'):]


def handles():
    pos = ['left: -5.6px; top: -5.6px', 'left: calc(50% - 4.7px); top: -5.6px', 'right: -5.6px; top: -5.6px', 'right: -5.6px; top: calc(50% - 4.7px)',
           'right: -5.6px; bottom: -5.6px', 'left: calc(50% - 4.7px); bottom: -5.6px', 'left: -5.6px; bottom: -5.6px', 'left: -5.6px; top: calc(50% - 4.7px)']
    h = ''.join(f'<span style="position: absolute; {p}; width: 9.4px; height: 9.4px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>' for p in pos)
    r = ''.join(f'<span style="position: absolute; {p}; width: 7px; height: 7px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 50%"></span>' for p in ['left: 8.3px; top: 8.3px', 'right: 8.3px; top: 8.3px', 'right: 8.3px; bottom: 8.3px', 'left: 8.3px; bottom: 8.3px'])
    return h + r


# 2. Hero text becomes the selection
rep('''<!-- parent-of-selection outline: Hero text -->
<div aria-hidden="true" style="position: absolute; top: -1px; left: -1px; right: -1px; bottom: -1px; border: 1.18px dashed rgba(47,128,237,0.6); pointer-events: none"></div>''',
    f'''<!-- selection: Hero text -->
<div aria-hidden="true" style="position: absolute; top: -1px; left: -1px; right: -1px; bottom: -1px; border: 1.76px solid #2f80ed; pointer-events: none">
<span style="position: absolute; left: -1.76px; bottom: calc(100% + 2px); height: 21px; padding: 0 5px; display: flex; align-items: center; background: #246bcb; color: #ffffff; font: 500 13px/1 'Inter', sans-serif; white-space: nowrap">Box · div</span>
{handles()}
</div>''')

# 3. scope outline on Hero grid + 4. hover on Hero image + pointer
rep('<div style="display: grid; grid-template-columns: 1.1fr 1fr; gap: 64px; align-items: center">',
    '<div style="position: relative; display: grid; grid-template-columns: 1.1fr 1fr; gap: 64px; align-items: center">')
img_open = '<div style="justify-self: end; width: 580px; height: 520px; border-radius: 12px; overflow: hidden; background: #e6dccd">'
a = s.index(img_open)
b = s.index('</svg>\n</div>', a) + len('</svg>\n</div>')
overlays = f'''
<!-- scope: Hero grid (entered by double-click) -->
<div aria-hidden="true" style="position: absolute; top: -12px; left: -12px; right: -12px; bottom: -12px; border: 1.18px dashed rgba(47,128,237,0.6); pointer-events: none">
<span style="position: absolute; right: -1px; bottom: calc(100% + 2px); height: 21px; padding: 0 5px; display: flex; align-items: center; gap: 4px; background: rgba(47,128,237,0.16); color: #1f5fb5; font: 500 13px/1 'Inter', sans-serif; white-space: nowrap; border: 1px dashed rgba(47,128,237,0.6)">Inside Hero grid · Esc to go up</span></div>
<!-- hover: Hero image (what a click would select) -->
<div aria-hidden="true" style="position: absolute; top: -1px; right: -1px; width: 582px; height: 522px; border: 1.18px solid #2f80ed; border-radius: 0; pointer-events: none">
<span style="position: absolute; left: -1.18px; bottom: calc(100% + 2px); height: 21px; padding: 0 5px; display: flex; align-items: center; background: #246bcb; color: #ffffff; font: 500 13px/1 'Inter', sans-serif; white-space: nowrap">Image · img</span></div>
<!-- pointer -->
<svg aria-hidden="true" width="24" height="24" viewBox="0 0 16 16" style="position: absolute; left: 1010px; top: 250px; overflow: visible"><path d="M4 2l9 6.2-4.1.9 2.4 4.4-1.7.9-2.4-4.4L4 13z" fill="#1d1a16" stroke="#ffffff" stroke-width="1.2" stroke-linejoin="round"></path></svg>'''
s = s[:b] + overlays + s[b:]

# 5. layers selection
rep('<span style="flex: 1; color: #e8e8e8">Hero text</span><span style="font-size: 11px; color: #939393">div</span>\n</div>',
    '<span style="flex: 1; color: #e8e8e8">Hero text</span><span style="font-size: 11px; color: #a8a8a8">div</span>\n</div>')
rep('<div role="treeitem" aria-expanded="true" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 32px; background-image:',
    '<div role="treeitem" aria-expanded="true" aria-selected="true" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 32px; background-color: rgba(47,128,237,0.18); background-image:')
rep('<div role="treeitem" aria-selected="true" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 44px; background-color: rgba(47,128,237,0.18); background-image: linear-gradient(#303030,#303030), linear-gradient(#303030,#303030), linear-gradient(#303030,#303030);',
    '<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 44px; background-image: linear-gradient(#262626,#262626), linear-gradient(#262626,#262626), linear-gradient(#262626,#262626);')
rep('<span style="flex: 1; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; color: #e8e8e8">Hero title</span><span style="font-size: 11px; color: #a8a8a8">h1</span>',
    '<span style="flex: 1; overflow: hidden; white-space: nowrap; text-overflow: ellipsis">Hero title</span><span style="font-size: 11px; color: #939393">h1</span>')
rep('<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#e8e8e8" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M3 3.5h10M8 3.5V13"></path></svg>',
    '<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#a8a8a8" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M3 3.5h10M8 3.5V13"></path></svg>')
# hover row in Layers for Hero image (canvas hover mirrors in Layers)
rep('<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 32px; background-image: linear-gradient(#262626,#262626), linear-gradient(#262626,#262626); background-size: 1px 100%, 1px 100%; background-position: 14px 0, 26px 0; background-repeat: no-repeat">\n<span style="width: 12px"></span>\n<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#a8a8a8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 3.5h11v9h-11z',
    '<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 32px; background-color: #262626; background-image: linear-gradient(#303030,#303030), linear-gradient(#303030,#303030); background-size: 1px 100%, 1px 100%; background-position: 14px 0, 26px 0; background-repeat: no-repeat">\n<span style="width: 12px"></span>\n<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#a8a8a8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 3.5h11v9h-11z')

# 6. options bar values
rep('<span style="font-size: 11px; color: #939393">Y</span><span>64</span>', '<span style="font-size: 11px; color: #939393">Y</span><span>48</span>')
rep('<label title="Width · 560px"', '<label title="Width · fills its grid column"')
rep('<span style="width: 30px">560</span><span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">Fixed</span>',
    '<span style="width: 30px; color: #a8a8a8">654</span><span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">Fill</span>')
rep('<span style="width: 30px; color: #a8a8a8">202</span>', '<span style="width: 30px; color: #a8a8a8">424</span>')

# 7. properties for Hero text
f = lambda inner: f'<label style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px; background: #2a2a2a; border-radius: 2px">{inner}</label>'
dot = '<span style="width: 5px; height: 5px; border-radius: 3px; background: #2f80ed; flex: none"></span>'
tagc = lambda t: f'<span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">{t}</span>'
adv = lambda t: f'<button aria-label="{t} · Advanced" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; color: #939393">{icon("sliders", 14)}</button>'
mp = lambda n, v='': f'<button class="mp-row" aria-label="Open {n}" style="width: 100%; height: 28px; display: flex; align-items: center; padding: 0 8px 0 12px; box-sizing: border-box; border-radius: 0; color: #a8a8a8"><span style="flex: 1; text-align: left">{n}</span>' + (f'<span style="font-size: 11px; color: #939393">{v}</span>' if v else '') + f'<span class="mp-add" aria-hidden="true" style="width: 18px; height: 18px; margin-left: 8px; display: flex; align-items: center; justify-content: center; border-radius: 3px; color: #e8e8e8">{icon("plus", 12, "currentColor", 1.75)}</span></button>'
agrid = '<span style="width: 60px; height: 60px; flex: none; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); padding: 4px; box-sizing: border-box; background: #2a2a2a; border-radius: 4px">' + ''.join(
    '<span style="display: flex; align-items: center; justify-content: center">' + ('<span style="display: flex; flex-direction: column; gap: 2px; align-items: flex-start"><span style="width: 9px; height: 3px; background: #2f80ed; border-radius: 1px"></span><span style="width: 13px; height: 3px; background: #2f80ed; border-radius: 1px"></span><span style="width: 7px; height: 3px; background: #2f80ed; border-radius: 1px"></span></span>' if i == 3 else '<span style="width: 3px; height: 3px; border-radius: 50%; background: #6b6b6b"></span>') + '</span>' for i in range(9)) + '</span>'

props = f'''<!-- Properties: Hero text -->
<section aria-label="Properties" style="position: relative; flex: 1; min-height: 0; overflow: hidden; font-variant-numeric: tabular-nums">
<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{icon('t-stack', 16, '#a8a8a8')}<span style="flex: 1; font-weight: 500">Hero text</span>
<button aria-label="State: Normal" style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 6px; border-radius: 2px; color: #a8a8a8">Normal{icon('chev-down', 10, 'currentColor', 1.5)}</button></div>
<div style="display: flex; align-items: center; gap: 6px; padding-left: 24px; font-size: 11px; color: #a8a8a8"><button style="display: flex; align-items: center; gap: 3px">Box{icon('chev-down', 10, 'currentColor', 1.5)}</button><span style="color: #454545">·</span><span style="font-family: {MONO}; color: #939393">div</span></div>
</div>
<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">
<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">Size</span>{adv('Size')}</div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">
{f('<span style="font-size: 11px; color: #939393; padding-left: 11px">W</span><span style="flex: 1; color: #939393">654</span>' + tagc('Fill'))}
{f('<span style="font-size: 11px; color: #939393; padding-left: 11px">H</span><span style="flex: 1; color: #939393">424</span>' + tagc('Fit'))}
</div></div>
<div style="height: 1px; background: #303030"></div>
<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">
<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">Layout</span>{adv('Layout')}</div>
<div role="group" aria-label="Arrange children" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #262626; border-radius: 4px; font-size: 11px">
<button aria-pressed="false" style="height: 22px; display: flex; align-items: center; justify-content: center; gap: 6px; border-radius: 3px; color: #939393">{icon('t-stack', 12)}Stack</button>
<button aria-pressed="true" style="height: 22px; display: flex; align-items: center; justify-content: center; gap: 6px; border-radius: 3px; background: #3a3a3a; color: #e8e8e8; font-weight: 500">{icon('t-row', 12)}Row</button>
<button aria-pressed="false" style="height: 22px; display: flex; align-items: center; justify-content: center; gap: 6px; border-radius: 3px; color: #939393">{icon('t-grid', 12)}Grid</button></div>
<div style="display: flex; gap: 10px">{agrid}
<div style="flex: 1; display: flex; flex-direction: column; gap: 6px">
<div role="group" aria-label="Direction" style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #262626; border-radius: 4px; font-size: 11px">
<button aria-pressed="false" style="height: 20px; display: flex; align-items: center; justify-content: center; gap: 4px; border-radius: 3px; color: #939393">{icon('chev-right', 10, 'currentColor', 1.75)}Across</button>
<button aria-pressed="true" style="height: 20px; display: flex; align-items: center; justify-content: center; gap: 4px; border-radius: 3px; background: #3a3a3a; color: #e8e8e8">{icon('chev-down', 10, 'currentColor', 1.75)}Down</button></div>
{f(dot + '<span style="font-size: 11px; color: #939393">Gap</span><span style="flex: 1">24</span><span style="font-size: 10px; color: #939393">px</span>')}
</div></div></div>
<div style="height: 1px; background: #303030"></div>
<div style="padding: 8px 0 0">
<div style="padding: 0 12px 4px; font-size: 10px; line-height: 14px; font-weight: 500; letter-spacing: 0.04em; color: #939393">MORE PROPERTIES</div>
{mp('Placement', 'In flow')}{mp('Spacing', '0')}{mp('Fill', 'none')}{mp('Border', 'none')}{mp('Effects')}{mp('Transform')}{mp('Visibility', 'All sizes')}{mp('Transition &amp; Animation')}{mp('Accessibility')}{mp('Attributes &amp; Custom CSS')}
</div>
</section>
'''
a = s.index('<!-- Properties v2 (decluttered) -->')
b = s.index('<!-- Swatches | History (h220) -->')
s = s[:a] + props + '\n' + s[b:]

# 8. status bar
a = s.index('<nav aria-label="Selection path"')
b = s.index('</nav>', a) + len('</nav>')
s = s[:a] + '''<nav aria-label="Selection path" style="flex: 1; display: flex; align-items: center; gap: 6px; color: #a8a8a8; white-space: nowrap">
<button>Page</button><span aria-hidden="true">›</span>
<button>Section · Hero</button><span aria-hidden="true">›</span>
<button style="color: #a9c8f7">Box · Hero grid</button><span aria-hidden="true">›</span>
<button aria-current="true" style="color: #e8e8e8">Box · Hero text</button>
</nav>''' + s[b:]
rep('<span style="flex: 1; text-align: center; color: #939393; white-space: nowrap">Drag a handle to resize · Shift keeps proportions</span>',
    '<span style="flex: 1; text-align: center; color: #939393; white-space: nowrap">Click to select Hero image · Double-click to go inside · Esc to go up to Hero grid</span>')
rep('x 612 &#160;y 288', 'x 948 &#160;y 262')

# 9. annotation (designer note, not part of the app)
note = f'''<!-- DESIGNER ANNOTATION — not part of the app UI -->
<div role="note" aria-label="Design annotation" style="position: absolute; left: 640px; top: 640px; width: 420px; padding: 14px 16px; box-sizing: border-box; background: #fff4b8; color: #3b3200; border-radius: 4px; box-shadow: 0 8px 24px rgba(0,0,0,0.45); font-size: 12px; line-height: 18px; transform: rotate(-0.6deg)">
<div style="font-size: 10px; font-weight: 600; letter-spacing: 0.06em; color: #6b5a00; margin-bottom: 6px">DESIGN NOTE · SCOPE RULE</div>
<b>A click selects the outermost element inside the current scope.</b> Double-clicking Hero grid moved the scope inside it (dashed outline), so Hero text is selected and hovering shows that a click would pick <b>Hero image</b>, not the whole grid. <span style="white-space: nowrap">Esc</span> goes back up; Ctrl+click picks the deepest element.
</div>
</main>'''
a = s.index('<!-- vertical scroll indicator -->')
b = s.index('</main>', a) + len('</main>')
seg = s[a:b]
s = s[:a] + seg.replace('</main>', note) + s[b:]

open('/home/claude/daisy/project/D05-Scope.dc.html', 'w', encoding='utf-8').write(s)
print('ok')
