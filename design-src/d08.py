import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

s = open('/home/claude/daisy/project/Main.dc.html', encoding='utf-8').read()


def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:90], s.count(old))
    s = s.replace(old, new)


rep('<title>Daisy · D-04 Editor, heading selected</title>', '<title>Daisy · D-08 Flow drag: reorder</title>')

# remove h1 selection overlay
a = s.index('<!-- selection overlay (screen-constant thickness: values ÷ 0.85) -->')
b = s.index('</div>\n</div>\n<p style="margin: 0; font-size: 18px', a)
s = s[:a] + s[b + len('</div>\n'):]

# original button row dimmed to 30%
rep('<div style="display: flex; align-items: center; gap: 24px">\n<a href="#shop" style="background: #b5532d;',
    '<div style="display: flex; align-items: center; gap: 24px; opacity: 0.3">\n<a href="#shop" style="background: #b5532d;')

# target outline + insertion line + ghost + grabbing hand (Hero text coordinates)
BTN = ('<a href="#shop" style="background: #b5532d; color: #ffffff; border-radius: 999px; padding: 12px 24px; font-size: 16px; font-weight: 500; line-height: 20px">Shop the collection</a>'
       '<a href="#process" style="font-size: 16px; font-weight: 500; color: #1d1a16">Our process →</a>')
INS_Y = 20 + 24 + 202 + 12  # eyebrow + gap + h1 + half gap
rep('''<!-- parent-of-selection outline: Hero text -->
<div aria-hidden="true" style="position: absolute; top: -1px; left: -1px; right: -1px; bottom: -1px; border: 1.18px dashed rgba(47,128,237,0.6); pointer-events: none"></div>''',
    f'''<!-- drop target: Hero text -->
<div aria-hidden="true" style="position: absolute; top: -1px; left: -1px; right: -1px; bottom: -1px; border: 1.18px solid #2f80ed; pointer-events: none">
<span style="position: absolute; left: -1.18px; bottom: calc(100% + 2px); height: 21px; padding: 0 5px; display: flex; align-items: center; background: #246bcb; color: #ffffff; font: 500 13px/1 'Inter', sans-serif; white-space: nowrap">into Hero text</span></div>
<!-- insertion line: after the heading, before the paragraph (2 px, 6 px end caps) -->
<div aria-hidden="true" style="position: absolute; left: 0; width: 560px; top: {INS_Y - 1.2}px; height: 2.35px; background: #2f80ed; pointer-events: none">
<span style="position: absolute; left: -1.2px; top: -2.35px; width: 2.35px; height: 7px; background: #2f80ed"></span><span style="position: absolute; right: -1.2px; top: -2.35px; width: 2.35px; height: 7px; background: #2f80ed"></span></div>
<!-- ghost following the pointer (60%) -->
<div aria-hidden="true" style="position: absolute; left: 150px; top: {INS_Y + 26}px; display: flex; align-items: center; gap: 24px; padding: 8px 12px; background: #f6f1ea; box-shadow: 0 0 0 1.18px rgba(47,128,237,0.5), 0 10px 26px rgba(29,26,22,0.25); border-radius: 6px; pointer-events: none; z-index: 3"><div style="display: flex; align-items: center; gap: 24px; opacity: 0.6">{BTN}</div></div>
<svg aria-hidden="true" width="26" height="26" viewBox="0 0 16 16" style="position: absolute; left: 228px; top: {INS_Y + 42}px; overflow: visible; z-index: 4"><path d="M5 8V5.5a1 1 0 0 1 2 0V8M7 7.5V5a1 1 0 0 1 2 0v2.5M9 7.5V5.5a1 1 0 0 1 2 0V8M11 8V7a1 1 0 0 1 2 0v3a4 4 0 0 1-4 4H8.5a4 4 0 0 1-3.3-1.7L3.5 9.8a1 1 0 0 1 1.5-1.3L5 9V8z" fill="#ffffff" stroke="#1d1a16" stroke-width="1.1" stroke-linejoin="round"></path></svg>''')

# Layers: Hero buttons selected (the dragged element); h1 back to normal
rep('<div role="treeitem" aria-selected="true" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 44px; background-color: rgba(47,128,237,0.18); background-image: linear-gradient(#303030,#303030), linear-gradient(#303030,#303030), linear-gradient(#303030,#303030);',
    '<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 44px; background-image: linear-gradient(#262626,#262626), linear-gradient(#262626,#262626), linear-gradient(#262626,#262626);')
rep('<span style="flex: 1; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; color: #e8e8e8">Hero title</span><span style="font-size: 11px; color: #a8a8a8">h1</span>',
    '<span style="flex: 1; overflow: hidden; white-space: nowrap; text-overflow: ellipsis">Hero title</span><span style="font-size: 11px; color: #939393">h1</span>')
rep('<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#e8e8e8" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M3 3.5h10M8 3.5V13"></path></svg>',
    '<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#a8a8a8" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M3 3.5h10M8 3.5V13"></path></svg>')
# Hero buttons row selected
old_hb = s[s.index('<div role="treeitem" aria-expanded="false" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 44px;'):]
old_hb = old_hb[:old_hb.index('</div>') + 6]
assert 'Hero buttons' in old_hb
new_hb = old_hb.replace('aria-expanded="false" style="', 'aria-expanded="false" aria-selected="true" style="background-color: rgba(47,128,237,0.18); ', 1).replace('<span style="flex: 1">Hero buttons</span>', '<span style="flex: 1; color: #e8e8e8">Hero buttons</span>')
s = s.replace(old_hb, new_hb, 1)
# drop-target mirror in Layers: Hero text row outlined
rep('<span style="flex: 1; color: #e8e8e8">Hero text</span><span style="font-size: 11px; color: #939393">div</span>\n</div>',
    '<span style="flex: 1; color: #e8e8e8">Hero text</span><span style="font-size: 11px; color: #939393">div</span>\n</div>')
rep('<div role="treeitem" aria-expanded="true" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 32px; background-image:',
    '<div role="treeitem" aria-expanded="true" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 32px; box-shadow: inset 0 0 0 1px #2f80ed; background-image:')

# options bar
rep('<span style="font-size: 11px; color: #939393">Y</span><span>64</span>', '<span style="font-size: 11px; color: #939393">Y</span><span>380</span>')
rep('<label title="Width · 560px"', '<label title="Width · fit content"')
rep('<span style="width: 30px">560</span><span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">Fixed</span>',
    '<span style="width: 30px; color: #a8a8a8">298</span><span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">Fit</span>')
rep('<span style="width: 30px; color: #a8a8a8">202</span>', '<span style="width: 30px; color: #a8a8a8">44</span>')

# Properties: Hero buttons (Row across, gap 24)
f = lambda inner: f'<label style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px; background: #2a2a2a; border-radius: 2px">{inner}</label>'
dot = '<span style="width: 5px; height: 5px; border-radius: 3px; background: #2f80ed; flex: none"></span>'
tagc = lambda t: f'<span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">{t}</span>'
adv = lambda t: f'<button aria-label="{t} · Advanced" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; color: #939393">{icon("sliders", 14)}</button>'
mp = lambda n, v='': f'<button class="mp-row" aria-label="Open {n}" style="width: 100%; height: 28px; display: flex; align-items: center; padding: 0 8px 0 12px; box-sizing: border-box; border-radius: 0; color: #a8a8a8"><span style="flex: 1; text-align: left">{n}</span>' + (f'<span style="font-size: 11px; color: #939393">{v}</span>' if v else '') + f'<span class="mp-add" aria-hidden="true" style="width: 18px; height: 18px; margin-left: 8px; display: flex; align-items: center; justify-content: center; border-radius: 3px; color: #e8e8e8">{icon("plus", 12, "currentColor", 1.75)}</span></button>'
agrid = '<span style="width: 60px; height: 60px; flex: none; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); padding: 4px; box-sizing: border-box; background: #2a2a2a; border-radius: 4px">' + ''.join(
    '<span style="display: flex; align-items: center; justify-content: center">' + ('<span style="display: flex; gap: 2px; align-items: center"><span style="width: 3px; height: 9px; background: #2f80ed; border-radius: 1px"></span><span style="width: 3px; height: 13px; background: #2f80ed; border-radius: 1px"></span><span style="width: 3px; height: 7px; background: #2f80ed; border-radius: 1px"></span></span>' if i == 3 else '<span style="width: 3px; height: 3px; border-radius: 50%; background: #6b6b6b"></span>') + '</span>' for i in range(9)) + '</span>'
props = f'''<!-- Properties: Hero buttons (being dragged) -->
<section aria-label="Properties" style="position: relative; flex: 1; min-height: 0; overflow: hidden; font-variant-numeric: tabular-nums">
<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{icon('t-row', 16, '#a8a8a8')}<span style="flex: 1; font-weight: 500">Hero buttons</span>
<button aria-label="State: Normal" style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 6px; border-radius: 2px; color: #a8a8a8">Normal{icon('chev-down', 10, 'currentColor', 1.5)}</button></div>
<div style="display: flex; align-items: center; gap: 6px; padding-left: 24px; font-size: 11px; color: #a8a8a8"><button style="display: flex; align-items: center; gap: 3px">Box{icon('chev-down', 10, 'currentColor', 1.5)}</button><span style="color: #454545">·</span><span style="font-family: {MONO}; color: #939393">div</span></div>
</div>
<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">
<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">Size</span>{adv('Size')}</div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">
{f('<span style="font-size: 11px; color: #939393; padding-left: 11px">W</span><span style="flex: 1; color: #939393">298</span>' + tagc('Fit'))}
{f('<span style="font-size: 11px; color: #939393; padding-left: 11px">H</span><span style="flex: 1; color: #939393">44</span>' + tagc('Fit'))}
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
<button aria-pressed="true" style="height: 20px; display: flex; align-items: center; justify-content: center; gap: 4px; border-radius: 3px; background: #3a3a3a; color: #e8e8e8">{icon('chev-right', 10, 'currentColor', 1.75)}Across</button>
<button aria-pressed="false" style="height: 20px; display: flex; align-items: center; justify-content: center; gap: 4px; border-radius: 3px; color: #939393">{icon('chev-down', 10, 'currentColor', 1.75)}Down</button></div>
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

# status bar
a = s.index('<nav aria-label="Selection path"')
b = s.index('</nav>', a) + len('</nav>')
s = s[:a] + '''<nav aria-label="Selection path" style="flex: 1; display: flex; align-items: center; gap: 6px; color: #a8a8a8; white-space: nowrap">
<button>Page</button><span aria-hidden="true">›</span>
<button>Section · Hero</button><span aria-hidden="true">›</span>
<button>Box · Hero grid</button><span aria-hidden="true">›</span>
<button>Box · Hero text</button><span aria-hidden="true">›</span>
<button aria-current="true" style="color: #e8e8e8">Box · Hero buttons</button>
</nav>''' + s[b:]
rep('<span style="flex: 1; text-align: center; color: #939393; white-space: nowrap">Drag a handle to resize · Shift keeps proportions</span>',
    '<span style="flex: 1; text-align: center; color: #939393; white-space: nowrap">Release to move · Esc cancels · Ctrl to disable snapping</span>')
rep('x 612 &#160;y 288', 'x 296 &#160;y 492')

open('/home/claude/daisy/project/D08-FlowDrag.dc.html', 'w', encoding='utf-8').write(s)
print('ok')
