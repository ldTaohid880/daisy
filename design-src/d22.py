from screen import *
_src = open('/home/claude/ds/layoutadv.py').read()
LA = {}
exec(_src[:_src.index('# ═════ A · ROW')], LA)
L = LA
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')

S = Screen('Daisy · D-22 Responsive: Tablet')
RESP, RESPS = '#d29922', 'rgba(210,153,34,0.14)'

# ---------------- canvas: the page at Tablet 768, 100% ----------------
src = S.s
a = src.index('<div style="justify-self: end; width: 580px; height: 520px'); b = src.index('</svg>', a) + 6
art = src[a:b]
art = art[art.index('<svg'):].replace('<svg width="580" height="520" viewBox="0 0 580 520"', '<svg width="100%" height="100%" viewBox="0 70 580 330" preserveAspectRatio="xMidYMid slice"')
hpos = ['left: -5px; top: -5px', 'left: calc(50% - 4px); top: -5px', 'right: -5px; top: -5px', 'right: -5px; top: calc(50% - 4px)',
        'right: -5px; bottom: -5px', 'left: calc(50% - 4px); bottom: -5px', 'left: -5px; bottom: -5px', 'left: -5px; top: calc(50% - 4px)']
handles = ''.join(f'<span style="position: absolute; {p}; width: 8px; height: 8px; box-sizing: border-box; background: #fff; border: 1px solid #2f80ed; border-radius: 1px"></span>' for p in hpos)
card = lambda bg, name, price: f'<div style="background: #ffffff; border-radius: 12px; padding: 16px; display: flex; flex-direction: column; gap: 8px"><div style="aspect-ratio: 4 / 3; border-radius: 8px; background: {bg}"></div><p style="margin: 8px 0 0; font-family: \'Fraunces\', serif; font-size: 20px; line-height: 1.2">{name}</p><p style="margin: 0; font-size: 14px; color: #6b6358">{price}</p></div>'
page = f'''<!-- page frame: Tablet 768 @ 100% -->
<span style="position: absolute; left: 200px; top: 13px; display: flex; align-items: center; gap: 6px; font-size: 11px; line-height: 11px; color: #939393">{icon('tablet', 12, RESP)}Tablet · 768 · applies up to 1024</span>
<div style="position: absolute; left: 200px; top: 32px; bottom: 0; width: 768px; overflow: hidden; outline: 1px solid #3c3c3c; background: #f6f1ea">
<div style="position: relative; width: 768px; background: #f6f1ea; color: #1d1a16; font-family: 'Inter', sans-serif; font-size: 16px; line-height: 1.5">
<div style="height: 72px; box-sizing: border-box; padding: 0 32px; display: flex; align-items: center; justify-content: space-between">
<p style="margin: 0; font-family: 'Fraunces', serif; font-size: 22px; font-weight: 600; line-height: 1">Halden</p>
<nav style="display: flex; gap: 24px; font-size: 15px"><a href="#work">Work</a><a href="#shop">Shop</a><a href="#journal">Journal</a><a href="#visit">Visit</a></nav>
<a href="#visit" style="background: #b5532d; color: #ffffff; border-radius: 999px; padding: 9px 18px; font-size: 14px; font-weight: 500; line-height: 20px">Book a visit</a></div>
<div style="padding: 32px 32px 48px; display: grid; grid-template-columns: 1fr; gap: 28px">
<div style="position: relative; display: flex; flex-direction: column; gap: 20px">
<p style="margin: 0; font-size: 13px; line-height: 20px; text-transform: uppercase; letter-spacing: 0.08em; color: #5f6b4e; font-weight: 500">Small-batch stoneware · Est. 2014</p>
<div style="position: relative">
<h1 style="margin: 0; font-family: 'Fraunces', serif; font-size: 48px; line-height: 1.05; font-weight: 600; color: #1d1a16">Hand-thrown ceramics for everyday tables</h1>
<div aria-hidden="true" style="position: absolute; inset: -1px; border: 1.5px solid #2f80ed; pointer-events: none">{handles}
<span style="position: absolute; left: -1.5px; bottom: calc(100% + 2px); height: 20px; padding: 0 5px; display: flex; align-items: center; gap: 5px; background: #246bcb; color: #ffffff; font: 500 12px/1 'Inter', sans-serif; white-space: nowrap">Heading · h1<span style="display: flex; align-items: center; padding-left: 5px; border-left: 1px solid rgba(255,255,255,0.35)">{icon('tablet', 11, '#ffd27a', 1.5)}</span></span></div></div>
<p style="margin: 0; font-size: 17px; line-height: 1.6; color: #4a443c; max-width: 520px">Each piece is wheel-thrown, glazed and fired in our studio by the river. Made slowly, used daily.</p>
<div style="display: flex; align-items: center; gap: 24px"><a href="#shop" style="background: #b5532d; color: #ffffff; border-radius: 999px; padding: 12px 24px; font-size: 16px; font-weight: 500; line-height: 20px">Shop the collection</a><a href="#process" style="font-size: 16px; font-weight: 500">Our process →</a></div></div>
<div style="height: 180px; border-radius: 12px; overflow: hidden; background: #e6dccd">{art}</div></div>
<div style="padding: 40px 32px; background: #e7d9c7">
<div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 20px"><h2 style="margin: 0; font-family: 'Fraunces', serif; font-size: 32px; line-height: 1.2; font-weight: 600">This season</h2><a href="#shop" style="font-size: 15px; color: #6b6358">View all →</a></div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px">{card('#d8cbb8', 'Tide bowl', '€38')}{card('#cfb9a3', 'Ember mug', '€26')}</div></div>
</div></div>
'''
a = src.index('<span style="position: absolute; left: 46px; top: 13px; font-size: 11px; line-height: 11px; color: #939393">Desktop · 1440</span>')
b = src.index('<span aria-hidden="true" style="position: absolute; right: 54px; top: 800px;')
b = src.index('<!-- vertical scroll indicator -->', b)
S.s = src[:a] + page + src[b:]

# top bar tab + status zoom/size
S.s = S.s.replace('@ 85%', '@ 100%', 1)
S.rep('>85%<', '>100%<')
S.rep('1440 × 2050', '768 × 2480')
# screen-size switcher: Tablet active
sw_old = S.s[S.s.index('<div role="group" aria-label="Screen size"'):S.s.index('<span style="width: 1px; height: 14px; background: #2e2e2e; margin: 0 2px"></span>', S.s.index('<div role="group" aria-label="Screen size"'))]
sw_new = (f'<div role="group" aria-label="Screen size" style="height: 28px; display: flex; align-items: center; gap: 2px; padding: 2px; box-sizing: border-box; background: #232323; border-radius: 6px">\n'
          f'<button aria-pressed="false" aria-label="Desktop 1440" title="Desktop · 1440" style="width: 32px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #939393">{icon("desktop", 14)}</button>\n'
          f'<button aria-pressed="true" style="height: 24px; display: flex; align-items: center; gap: 8px; padding: 0 10px; border-radius: 4px; background: #333333; color: #e8e8e8">{icon("tablet", 14, RESP)}<span style="font-weight: 500">Tablet</span><span style="font-size: 11px; color: #a8a8a8; font-variant-numeric: tabular-nums">768</span></button>\n'
          f'<button aria-pressed="false" aria-label="Mobile 390" title="Mobile · 390" style="width: 32px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #939393">{icon("phone", 14)}</button>\n')
S.s = S.s.replace(sw_old, sw_new, 1)

# ---------------- options bar: amber context chip + Select capsules ----------------
chip = (f'<span style="height: 22px; display: flex; align-items: center; gap: 6px; padding: 0 4px 0 9px; border-radius: 11px; background: {RESPS}; color: #f0c56a; font-size: 11px; font-weight: 500; white-space: nowrap">'
        f'{icon("tablet", 12, RESP, 1.5)}Editing: Tablet and smaller<button aria-label="Back to Desktop" style="width: 16px; height: 16px; display: flex; align-items: center; justify-content: center; border-radius: 8px; color: #f0c56a">{icon("close", 10)}</button></span>')
S.options('0', '0', '704', 'Fill', '101', 'Fit')
S.rep('<!-- position + size capsule -->', chip + '\n<!-- position + size capsule -->')
assert contrast('#f0c56a', '#2a2618') >= 4.5

# ---------------- layers: tablet badges on elements with overrides ----------------
tb = icon('tablet', 12, RESP, 1.25, 'Overrides at Tablet')
rows = []
for r in hero_tree('Hero title'):
    r = list(r)
    if r[3] in ('Hero grid', 'Hero title', 'Hero image', 'This season'):
        if r[3] == 'Hero image':
            r[7] = r[7] + tb
        elif r[3] == 'This season':
            r[7] = tb
        else:
            r[7] = tb
    rows.append(tuple(r))
set_tree(S, rows)

# ---------------- properties ----------------
HOLLOW = '<span title="From Desktop" style="width: 5px; height: 5px; box-sizing: border-box; border-radius: 3px; border: 1px solid #8a8a8a; flex: none"></span>'
strip = f'''<div style="padding: 8px 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #303030; background: #232323">
{icon('tablet', 14, RESP, 1.5)}<span style="flex: 1; font-size: 11px; color: #c8c8c8">Tablet and smaller<span style="color: #939393"> · 2 values set here</span></span><button style="font-size: 11px; color: #a9c8f7">Show only these</button></div>'''
fieldf = lambda dot, lab, val, unit='', extra='': f(dot + (f'<span style="font-size: 11px; color: #939393">{lab}</span>' if lab else '') + f'<span style="flex: 1; {"text-align: right;" if lab else ""}">{val}</span>' + (f'<span style="font-size: 10px; color: #939393">{unit}</span>' if unit else ''), extra)
size_grp = group('Size', pair(fieldf(DOT, 'W', '704', '') .replace('</label>', tagc('Fill') + '</label>'), fieldf(HOLLOW, 'H', '<span style="color: #939393">101</span>').replace('</label>', tagc('Fit') + '</label>'))
                 + '<div style="font-size: 10px; line-height: 14px; color: #939393">Width: Fixed 560 on Desktop · Fill here</div>')
typo_grp = group('Typography',
                 f(HOLLOW + '<span style="flex: 1; font-family: Georgia, serif; color: #a8a8a8">Fraunces</span>' + icon('chev-down', 10, '#939393', 1.5))
                 + pair(f(HOLLOW + '<span style="flex: 1; color: #a8a8a8">Semibold</span>'),
                        f(DOT + '<span style="font-size: 11px; color: #939393">Size</span><span style="flex: 1; text-align: right">48</span><span style="font-size: 10px; color: #939393">px</span>', 'box-shadow: inset 0 0 0 1px #2f80ed'))
                 + pair(f(HOLLOW + icon('lh', 12, '#939393') if 'lh' in P else HOLLOW + '<span style="font-size: 11px; color: #939393">Line</span>' + '<span style="flex: 1; text-align: right; color: #a8a8a8">1.05</span>'),
                        f(HOLLOW + swatch('#1d1a16') + '<span style="flex: 1; color: #a8a8a8">ink</span>'))
                 + f'<div style="display: flex; align-items: center; gap: 10px; font-size: 10px; color: #939393"><span style="display: flex; align-items: center; gap: 4px">{DOT}set here</span><span style="display: flex; align-items: center; gap: 4px">{HOLLOW}from Desktop</span></div>')
hdr = header('t-heading', 'Hero title', 'Heading 1', 'h1')
S.props(panel(hdr + strip + size_grp + typo_grp + more([mp('Placement', 'In flow'), mp('Spacing', '0'), mp('Fill', 'none'), mp('Effects'), mp('Visibility', 'All sizes'), mp('Accessibility')])))

# ---------------- popover: this value across screen sizes ----------------
def szrow(ic, name, v, note, on=False, dim=False):
    return (f'<div style="height: 30px; display: grid; grid-template-columns: 18px 1fr auto; gap: 8px; align-items: center; padding: 0 8px; border-radius: 3px; {"background: rgba(47,128,237,0.18); box-shadow: inset 0 0 0 1px #2f80ed;" if on else "background: #2a2a2a;"}">'
            f'<span style="color: {RESP if on else "#939393"}">{icon(ic, 13)}</span><span style="color: {"#e8e8e8" if on else "#c8c8c8"}">{name}<span style="font-size: 10px; color: #939393"> {note}</span></span>'
            f'<span style="font-variant-numeric: tabular-nums; {"color: #939393;" if dim else ""}">{v}</span></div>')
cbtn = lambda t, primary=False: f'<button style="height: 24px; padding: 0 9px; border-radius: 4px; font-size: 11px; {"background: #246bcb; color: #fff; font-weight: 500;" if primary else "background: #2a2a2a; color: #c8c8c8;"}">{t}</button>'
pop = f'''<!-- POPOVER: Font size across screen sizes (opened from the Size field's dot) -->
<section role="dialog" aria-label="Font size across screen sizes" style="position: absolute; left: 1282px; top: 268px; width: 328px; box-sizing: border-box; padding: 0 12px 12px; display: flex; flex-direction: column; gap: 9px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); z-index: 30">
<span aria-hidden="true" style="position: absolute; right: -6px; top: 70px; width: 10px; height: 10px; background: #262626; border-right: 1px solid #454545; border-top: 1px solid #454545; transform: rotate(45deg)"></span>
<div style="height: 40px; margin: 0 -12px; padding: 0 8px 0 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a">
<span style="font-weight: 600">Font size</span><span style="flex: 1; font-size: 11px; color: #939393">Hero title · across screen sizes</span>
<button aria-label="Close" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon("close", 14)}</button></div>
<div style="display: flex; flex-direction: column; gap: 2px">
{szrow('desktop', 'Desktop', '64 px', '1440 · base')}{szrow('tablet', 'Tablet and smaller', '48 px', '≤ 1024 · set here', True)}{szrow('phone', 'Mobile', '48 px', '≤ 640 · from Tablet', dim=True)}</div>
<div style="display: flex; gap: 6px; flex-wrap: wrap">{cbtn('Reset to Desktop')}{cbtn('Use 48 everywhere')}</div>
<div style="height: 1px; background: #333333"></div>
<div style="display: flex; align-items: center; justify-content: space-between">{L['lab']('Or make it fluid', 'clamp()')}<span style="font-size: 10px; color: #939393">one value, no breakpoints</span></div>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 6px">{L['fieldv']('Min', '36', 'px')}{L['fieldv']('Ideal', '5', 'vw')}{L['fieldv']('Max', '64', 'px')}</div>
<div style="display: flex; align-items: flex-end; gap: 10px; padding: 8px; background: #1f1f1f; border-radius: 4px; box-shadow: inset 0 0 0 1px #3a3a3a; font-family: Georgia, serif; color: #e8e8e8">
<span style="display: flex; flex-direction: column; align-items: center; gap: 4px"><span style="font-size: 26px; line-height: 1">Aa</span><span style="font: 10px Inter, sans-serif; color: #939393">390 · 36</span></span>
<span style="display: flex; flex-direction: column; align-items: center; gap: 4px"><span style="font-size: 32px; line-height: 1">Aa</span><span style="font: 10px Inter, sans-serif; color: #939393">768 · 38</span></span>
<span style="display: flex; flex-direction: column; align-items: center; gap: 4px"><span style="font-size: 44px; line-height: 1">Aa</span><span style="font: 10px Inter, sans-serif; color: #939393">1440 · 64</span></span>
<span style="flex: 1"></span>{cbtn('Use fluid', True)}</div>
{L['css_line']('@media (max-width: 1024px) {\n  h1 { font-size: 48px; }\n}')}
</section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', pop + '\n<!-- ═══════════ TOP BAR v3')

S.status(['Page', 'Section · Hero', 'Box · Hero grid', 'Box · Hero text', 'Heading · Hero title'],
         'Editing Tablet and smaller · changes apply up to 1024 px · hollow dots come from Desktop · click a dot to compare sizes', 'x 306 &#160;y 160')
S.save('D22-Tablet.dc.html')
print('ok')
