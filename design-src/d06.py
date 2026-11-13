import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

s = open('/home/claude/daisy/project/Main.dc.html', encoding='utf-8').read()


def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:90], s.count(old))
    s = s.replace(old, new)


rep('<title>Daisy · D-04 Editor, heading selected</title>', '<title>Daisy · D-06 Resize in progress</title>')

# remove h1 overlay and Hero text parent outline
a = s.index('<!-- selection overlay (screen-constant thickness: values ÷ 0.85) -->')
b = s.index('</div>\n</div>\n<p style="margin: 0; font-size: 18px', a)
s = s[:a] + s[b + len('</div>\n'):]
a = s.index('<!-- parent-of-selection outline: Hero text -->')
b = s.index('</div>', a) + len('</div>')
s = s[:a] + s[b:]

# grid reflows live: image now 624 wide -> both columns 624
rep('<div style="display: grid; grid-template-columns: 1.1fr 1fr; gap: 64px; align-items: center">',
    '<div style="position: relative; display: grid; grid-template-columns: 624px 624px; gap: 64px; align-items: center">')
img_open = '<div style="justify-self: end; width: 580px; height: 520px; border-radius: 12px; overflow: hidden; background: #e6dccd">'
rep(img_open, '<div style="justify-self: start; width: 624px; height: 540px; border-radius: 12px; overflow: hidden; background: #e6dccd">')
rep('<svg width="580" height="520" viewBox="0 0 580 520" role="img" aria-label="Stacked bowls and a cup on linen">',
    '<svg width="624" height="540" viewBox="0 0 580 520" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Stacked bowls and a cup on linen">')

H = lambda pos, active=False: f'<span style="position: absolute; {pos}; width: 9.4px; height: 9.4px; box-sizing: border-box; background: {"#2f80ed" if active else "#fff"}; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>'
R = lambda pos: f'<span style="position: absolute; {pos}; width: 7px; height: 7px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 50%"></span>'
handles = ''.join(H(p, i == 4) for i, p in enumerate(['left: -5.6px; top: -5.6px', 'left: calc(50% - 4.7px); top: -5.6px', 'right: -5.6px; top: -5.6px', 'right: -5.6px; top: calc(50% - 4.7px)',
                                                       'right: -5.6px; bottom: -5.6px', 'left: calc(50% - 4.7px); bottom: -5.6px', 'left: -5.6px; bottom: -5.6px', 'left: -5.6px; top: calc(50% - 4.7px)']))
handles += ''.join(R(p) for p in ['left: 18px; top: 18px', 'right: 18px; top: 18px', 'right: 18px; bottom: 18px', 'left: 18px; bottom: 18px'])

a = s.index('<div style="justify-self: start; width: 624px; height: 540px;')
b = s.index('</svg>\n</div>', a) + len('</svg>\n</div>')
overlay = f'''
<!-- parent of selection: Hero grid -->
<div aria-hidden="true" style="position: absolute; top: -1px; left: -1px; right: -1px; bottom: -1px; border: 1.18px dashed rgba(47,128,237,0.6); pointer-events: none"></div>
<!-- ghost: size before the drag (580 × 520, right-aligned in its column) -->
<div aria-hidden="true" style="position: absolute; left: 732px; top: 10px; width: 580px; height: 520px; box-sizing: border-box; border: 1.18px dashed #8a8a8a; border-radius: 12px; pointer-events: none"></div>
<!-- selection: Hero image, resizing from the bottom-right handle -->
<div aria-hidden="true" style="position: absolute; left: 687px; top: -1px; width: 626px; height: 542px; box-sizing: border-box; border: 1.76px solid #2f80ed; pointer-events: none">
<span style="position: absolute; left: -1.76px; bottom: calc(100% + 2px); height: 21px; padding: 0 5px; display: flex; align-items: center; background: #246bcb; color: #ffffff; font: 500 13px/1 'Inter', sans-serif; white-space: nowrap">Image · img</span>
{handles}
<span style="position: absolute; left: calc(50% - 46px); top: calc(100% + 9px); height: 21px; padding: 0 9px; display: flex; align-items: center; border-radius: 11px; background: #246bcb; color: #ffffff; font: 500 13px/1 'Inter', sans-serif; white-space: nowrap; font-variant-numeric: tabular-nums">624 × 540</span>
</div>
<!-- size match: both grid columns are now 624 (magenta = guide) -->
<div aria-hidden="true" style="position: absolute; left: 0; top: -30px; width: 624px; height: 12px; pointer-events: none">
<span style="position: absolute; left: 0; right: 0; top: 6px; border-top: 1.18px solid #e535ab"></span><span style="position: absolute; left: 0; top: 1px; height: 11px; border-left: 1.18px solid #e535ab"></span><span style="position: absolute; right: 0; top: 1px; height: 11px; border-left: 1.18px solid #e535ab"></span>
<span style="position: absolute; left: calc(50% - 22px); top: -4px; height: 20px; padding: 0 7px; display: flex; align-items: center; border-radius: 10px; background: #c21f8f; color: #fff; font: 500 12px/1 'Inter', sans-serif">= 624</span></div>
<div aria-hidden="true" style="position: absolute; left: 688px; top: -30px; width: 624px; height: 12px; pointer-events: none">
<span style="position: absolute; left: 0; right: 0; top: 6px; border-top: 1.18px solid #e535ab"></span><span style="position: absolute; left: 0; top: 1px; height: 11px; border-left: 1.18px solid #e535ab"></span><span style="position: absolute; right: 0; top: 1px; height: 11px; border-left: 1.18px solid #e535ab"></span>
<span style="position: absolute; left: calc(50% - 22px); top: -4px; height: 20px; padding: 0 7px; display: flex; align-items: center; border-radius: 10px; background: #c21f8f; color: #fff; font: 500 12px/1 'Inter', sans-serif">= 624</span></div>
<!-- cursor: diagonal resize -->
<svg aria-hidden="true" width="26" height="26" viewBox="0 0 16 16" style="position: absolute; left: 1316px; top: 544px; overflow: visible"><path d="M3 3h5L6.3 4.7l5 5L13 8v5H8l1.7-1.7-5-5L3 8z" fill="#1d1a16" stroke="#ffffff" stroke-width="1" stroke-linejoin="round"></path></svg>'''
s = s[:b] + overlay + s[b:]
assert contrast('#ffffff', '#c21f8f') >= 4.5

# Layers: Hero image selected, Hero title normal
rep('<div role="treeitem" aria-selected="true" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 44px; background-color: rgba(47,128,237,0.18); background-image: linear-gradient(#303030,#303030), linear-gradient(#303030,#303030), linear-gradient(#303030,#303030);',
    '<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 44px; background-image: linear-gradient(#262626,#262626), linear-gradient(#262626,#262626), linear-gradient(#262626,#262626);')
rep('<span style="flex: 1; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; color: #e8e8e8">Hero title</span><span style="font-size: 11px; color: #a8a8a8">h1</span>',
    '<span style="flex: 1; overflow: hidden; white-space: nowrap; text-overflow: ellipsis">Hero title</span><span style="font-size: 11px; color: #939393">h1</span>')
rep('<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#e8e8e8" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M3 3.5h10M8 3.5V13"></path></svg>',
    '<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#a8a8a8" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M3 3.5h10M8 3.5V13"></path></svg>')
rep('<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 32px; background-image: linear-gradient(#262626,#262626), linear-gradient(#262626,#262626); background-size: 1px 100%, 1px 100%; background-position: 14px 0, 26px 0; background-repeat: no-repeat">\n<span style="width: 12px"></span>\n<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#a8a8a8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 3.5h11v9h-11z',
    '<div role="treeitem" aria-selected="true" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 32px; background-color: rgba(47,128,237,0.18); background-image: linear-gradient(#303030,#303030), linear-gradient(#303030,#303030); background-size: 1px 100%, 1px 100%; background-position: 14px 0, 26px 0; background-repeat: no-repeat">\n<span style="width: 12px"></span>\n<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#e8e8e8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 3.5h11v9h-11z')

# options bar: live W / H highlighted
rep('<span style="font-size: 11px; color: #939393">X</span><span>0</span>', '<span style="font-size: 11px; color: #939393">X</span><span>688</span>')
rep('<span style="font-size: 11px; color: #939393">Y</span><span>64</span>', '<span style="font-size: 11px; color: #939393">Y</span><span>0</span>')
LIVE = 'background: rgba(47,128,237,0.18); box-shadow: inset 0 0 0 1px #2f80ed;'
rep('<label title="Width · 560px" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px 0 8px; box-sizing: border-box; border-radius: 4px">',
    f'<label title="Width · updating live" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px 0 8px; box-sizing: border-box; border-radius: 4px; {LIVE}">')
rep('<span style="width: 30px">560</span>', '<span style="width: 30px">624</span>')
rep('<label title="Height · fit-content" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px 0 8px; box-sizing: border-box; border-radius: 4px">',
    f'<label title="Height · updating live" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px 0 8px; box-sizing: border-box; border-radius: 4px; {LIVE}">')
rep('<span style="width: 30px; color: #a8a8a8">202</span><span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">Fit</span>',
    '<span style="width: 30px">540</span><span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">Fixed</span>')

# Properties: image
f = lambda inner, extra='': f'<label style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px; background: #2a2a2a; border-radius: 2px; {extra}">{inner}</label>'
dot = '<span style="width: 5px; height: 5px; border-radius: 3px; background: #2f80ed; flex: none"></span>'
tagc = lambda t: f'<span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">{t}</span>'
adv = lambda t: f'<button aria-label="{t} · Advanced" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; color: #939393">{icon("sliders", 14)}</button>'
mp = lambda n, v='', vc='#939393': f'<button class="mp-row" aria-label="Open {n}" style="width: 100%; height: 28px; display: flex; align-items: center; padding: 0 8px 0 12px; box-sizing: border-box; border-radius: 0; color: #a8a8a8"><span style="flex: 1; text-align: left">{n}</span>' + (f'<span style="font-size: 11px; color: {vc}">{v}</span>' if v else '') + f'<span class="mp-add" aria-hidden="true" style="width: 18px; height: 18px; margin-left: 8px; display: flex; align-items: center; justify-content: center; border-radius: 3px; color: #e8e8e8">{icon("plus", 12, "currentColor", 1.75)}</span></button>'
LIVEF = 'box-shadow: inset 0 0 0 1px #2f80ed;'
props = f'''<!-- Properties: Hero image while resizing -->
<section aria-label="Properties" style="position: relative; flex: 1; min-height: 0; overflow: hidden; font-variant-numeric: tabular-nums">
<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{icon('t-image', 16, '#a8a8a8')}<span style="flex: 1; font-weight: 500">Hero image</span>
<button aria-label="State: Normal" style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 6px; border-radius: 2px; color: #a8a8a8">Normal{icon('chev-down', 10, 'currentColor', 1.5)}</button></div>
<div style="display: flex; align-items: center; gap: 6px; padding-left: 24px; font-size: 11px; color: #a8a8a8"><button style="display: flex; align-items: center; gap: 3px">Image{icon('chev-down', 10, 'currentColor', 1.5)}</button><span style="color: #454545">·</span><span style="font-family: {MONO}; color: #939393">img</span></div>
</div>
<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">
<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">Size</span>{adv('Size')}</div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">
{f(dot + '<span style="font-size: 11px; color: #939393">W</span><span style="flex: 1">624</span>' + tagc('Fixed'), LIVEF)}
{f(dot + '<span style="font-size: 11px; color: #939393">H</span><span style="flex: 1">540</span>' + tagc('Fixed'), LIVEF)}
</div>
<div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #939393">{icon('info', 12, '#939393', 1.25)}Hero grid columns follow: both are now 624</div>
</div>
<div style="height: 1px; background: #303030"></div>
<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">
<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">Image</span>{adv('Image')}</div>
<div style="display: flex; align-items: center; gap: 8px"><span style="width: 40px; height: 32px; flex: none; border-radius: 3px; background: #c86a43"></span><span style="flex: 1; min-width: 0"><span style="display: block; font-family: {MONO}; font-size: 11px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">bowls-on-linen.jpg</span><span style="display: block; font-size: 10px; color: #939393">2400 × 2000 · 312 KB</span></span><button style="height: 22px; padding: 0 8px; border-radius: 4px; font-size: 11px; color: #a8a8a8">Replace</button></div>
<div role="group" aria-label="Fit" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #262626; border-radius: 4px; font-size: 11px">
<button aria-pressed="true" style="height: 22px; border-radius: 3px; background: #3a3a3a; color: #e8e8e8; font-weight: 500" title="object-fit: cover">Fill frame</button><button aria-pressed="false" style="height: 22px; border-radius: 3px; color: #939393" title="object-fit: contain">Fit inside</button><button aria-pressed="false" style="height: 22px; border-radius: 3px; color: #939393" title="object-fit: fill">Stretch</button></div>
</div>
<div style="height: 1px; background: #303030"></div>
<div style="padding: 8px 0 0">
<div style="padding: 0 12px 4px; font-size: 10px; line-height: 14px; font-weight: 500; letter-spacing: 0.04em; color: #939393">MORE PROPERTIES</div>
{mp('Placement', 'In flow')}{mp('Spacing', '0')}{mp('Border', 'radius 12')}{mp('Effects')}{mp('Transform')}{mp('Visibility', 'All sizes')}{mp('Transition &amp; Animation')}{mp('Accessibility', '⚠ needs a description', '#e3b34a')}{mp('Attributes &amp; Custom CSS')}
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
<button aria-current="true" style="color: #e8e8e8">Image · img</button>
</nav>''' + s[b:]
rep('<span style="flex: 1; text-align: center; color: #939393; white-space: nowrap">Drag a handle to resize · Shift keeps proportions</span>',
    '<span style="flex: 1; text-align: center; color: #939393; white-space: nowrap">Shift keeps proportions · Alt resizes from the centre · Ctrl turns off snapping · Esc cancels</span>')
rep('x 612 &#160;y 288', 'x 1312 &#160;y 692')

rep('right: 54px; top: 800px;', 'right: 54px; top: 781px;')  # hero grew 20 px: label above the line
open('/home/claude/daisy/project/D06-Resize.dc.html', 'w', encoding='utf-8').write(s)
print('ok')
