import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
P['r-all'] = ('stroke', 'M3 6a3 3 0 0 1 3-3h4a3 3 0 0 1 3 3v4a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3z')
P['r-pairs'] = ('stroke', 'M3 6a3 3 0 0 1 3-3h4a3 3 0 0 1 3 3v7H3z')
P['r-each'] = ('stroke', 'M3 6a3 3 0 0 1 3-3h2M11 3h2v2M13 11v2h-2M5 13H3v-2')
M_ = "font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 11px"
POPS = 'width: 328px; box-sizing: border-box; padding: 0 12px 12px; display: flex; flex-direction: column; gap: 10px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); font-size: 12px; line-height: 16px'
cap = lambda t, d: f'<div style="margin-bottom: 10px"><div style="font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{d}</div></div>'
def hdr(t, sub):
    return f'''<div style="height: 40px; margin: 0 -12px; padding: 0 8px 0 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a">
<span style="font-weight: 600">{t}</span><span style="flex: 1; font-size: 11px; color: #939393">{sub}</span>{icon("keep", 14, "#939393")}<span style="width: 6px"></span>{icon("close", 14, "#a8a8a8")}</div>'''
css = lambda t: f'<div style="display: flex; align-items: flex-start; gap: 8px; padding-top: 10px; border-top: 1px solid #333333"><code style="flex: 1; {M_}; color: #939393; white-space: pre-wrap">{t}</code><button style="font-size: 11px; color: #a8a8a8">Copy CSS</button></div>'
def modes(sel):
    items = [('r-all', 'All'), ('r-pairs', 'Top · Bottom'), ('r-each', 'Each')]
    return '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 2px; padding: 2px; border-radius: 4px; background: #1f1f1f; font-size: 11px">' + ''.join(
        f'<button style="height: 24px; display: flex; align-items: center; justify-content: center; gap: 6px; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #a8a8a8;"}">{icon(ic, 13)}{t}</button>' for i, (ic, t) in enumerate(items)) + '</div>'
fld = lambda inner, focus=False, w='': f'<span style="{w} height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px; box-sizing: border-box; border-radius: 2px; background: #2a2a2a; {"box-shadow: inset 0 0 0 1px #2f80ed;" if focus else ""}">{inner}</span>'
tokchip = lambda n: f'<span style="height: 16px; display: inline-flex; align-items: center; gap: 4px; padding: 0 5px; border-radius: 3px; background: #333333; font-size: 10px; color: #c8c8c8">{icon("link", 10, "#a8a8a8")}{n}</span>'
def tokens(sel):
    T = [('none', 0), ('sm', 4), ('md', 12), ('lg', 20), ('pill', 999)]
    return '<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 4px">' + ''.join(
        f'<button style="height: 44px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; border-radius: 4px; background: #2a2a2a; {"box-shadow: inset 0 0 0 1px #2f80ed;" if n == sel else ""}"><span style="width: 24px; height: 16px; border: 1.5px solid #c8c8c8; border-radius: {min(r, 8)}px"></span><span style="font-size: 10px; color: {"#e8e8e8" if n == sel else "#a8a8a8"}">{n} <span style="color: #939393">{r if r < 999 else ""}</span></span></button>' for n, r in T) + '</div>'
advbtn = lambda pressed=False: f'<button style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; font-size: 11px; {"background: #3a3a3a; box-shadow: 0 0 0 1px #2f80ed; color: #e8e8e8;" if pressed else "color: #a8a8a8;"}">{icon("sliders", 12)}Advanced</button>'
preview = lambda radius, extra='': f'<div style="position: relative; height: 96px; display: flex; align-items: center; justify-content: center; border-radius: 4px; background: #1f1f1f">{extra}<span style="width: 140px; height: 64px; background: #3a3a3a; box-shadow: inset 0 0 0 1px #6b6b6b; border-radius: {radius}"></span></div>'
slider = lambda pct: f'<div style="position: relative; flex: 1; height: 16px"><span style="position: absolute; left: 0; right: 0; top: 7px; height: 2px; background: #454545"></span><span style="position: absolute; left: 0; width: {pct}%; top: 7px; height: 2px; background: #2f80ed"></span><span style="position: absolute; left: calc({pct}% - 6px); top: 2px; width: 12px; height: 12px; border-radius: 6px; background: #e8e8e8"></span></div>'

# A · All corners
A = f'''<section style="{POPS}">{hdr('Corner roundness', 'Card 1')}{modes(0)}{preview('12px')}
<div style="display: flex; align-items: center; gap: 10px">{fld('<span style="flex: 1">12</span><span style="font-size: 10px; color: #939393">px</span>', True, 'width: 84px;')}{slider(30)}</div>
<div style="display: flex; align-items: center; gap: 8px; font-size: 11px; color: #a8a8a8"><span>From the design system</span><span style="flex: 1"></span>{tokchip('radius-md')}</div>{tokens('md')}
<div style="display: flex; align-items: center">{advbtn()}<span style="flex: 1"></span><span style="font-size: 11px; color: #939393">Drag a corner handle on the canvas too</span></div>
{css('border-radius: var(--radius-md);')}</section>'''

# B · Each corner
cf = lambda v, pos, focus=False: f'<span style="position: absolute; {pos}">{fld(f"<span style=\"flex: 1\">{v}</span>", focus, "width: 56px;")}</span>'
eachprev = f'''<div style="position: relative; height: 130px; border-radius: 4px; background: #1f1f1f">
{cf('20', 'left: 8px; top: 8px', True)}{cf('20', 'right: 8px; top: 8px')}{cf('0', 'left: 8px; bottom: 8px')}{cf('0', 'right: 8px; bottom: 8px')}
<span style="position: absolute; left: calc(50% - 70px); top: 33px; width: 140px; height: 64px; background: #3a3a3a; box-shadow: inset 0 0 0 1px #6b6b6b; border-radius: 20px 20px 0 0"></span>
<button title="Link all four" style="position: absolute; left: calc(50% - 12px); top: calc(50% - 12px); width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; background: #262626; color: #a8a8a8">{icon("link", 12)}</button></div>'''
B = f'''<section style="{POPS}">{hdr('Corner roundness', 'Hero image')}{modes(2)}{eachprev}
<div style="display: flex; gap: 6px; flex-wrap: wrap">{''.join(f'<button style="height: 22px; padding: 0 8px; border-radius: 3px; background: #2a2a2a; font-size: 11px; color: #c8c8c8">{t}</button>' for t in ['Top only', 'Bottom only', 'Left only', 'Swap', 'Make equal'])}</div>
<div style="display: flex; align-items: center; gap: 8px; font-size: 11px; color: #a8a8a8"><span>Top corners use</span>{tokchip('radius-lg · 20')}<span style="flex: 1"></span>{advbtn()}</div>
{css('border-radius: var(--radius-lg) var(--radius-lg) 0 0;')}</section>'''

# C · Advanced popover, opened from A's Advanced button
Asmall = f'''<section style="{POPS}; opacity: 0.55">{hdr('Corner roundness', 'Card 1')}{modes(0)}
<div style="display: flex; align-items: center; gap: 10px">{fld('<span style="flex: 1">12</span>', False, 'width: 84px;')}{slider(30)}</div>
<div style="display: flex; align-items: center">{advbtn(True)}</div></section>'''
shape = '<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 4px">' + ''.join(
    f'<button style="height: 46px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; border-radius: 4px; background: #2a2a2a; {"box-shadow: inset 0 0 0 1px #2f80ed;" if i == 1 else ""}"><svg width="22" height="16" viewBox="0 0 22 16"><path d="{d}" fill="none" stroke="#c8c8c8" stroke-width="1.5"/></svg><span style="font-size: 10px; color: {"#e8e8e8" if i == 1 else "#a8a8a8"}">{t}</span></button>'
    for i, (t, d) in enumerate([('Round', 'M1 15V7a6 6 0 0 1 6-6h14'), ('Squircle', 'M1 15V8C1 2 3 1 9 1h12'), ('Bevel', 'M1 15V7l6-6h14'), ('Notch', 'M1 15V7h6V1h14')])) + '</div>'
sw_ = lambda on: f'<span style="position: relative; width: 28px; height: 16px; border-radius: 8px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {"#fff" if on else "#a8a8a8"}"></span></span>'
C = f'''<section style="{POPS}; position: relative">
<span aria-hidden="true" style="position: absolute; left: -6px; top: 116px; width: 10px; height: 10px; background: #262626; border-left: 1px solid #454545; border-bottom: 1px solid #454545; transform: rotate(45deg)"></span>
{hdr('Corner roundness · Advanced', 'Card 1')}
<span style="font-size: 11px; color: #a8a8a8">Corner shape</span>{shape}
<span style="font-size: 11px; line-height: 15px; color: #939393">Squircle uses corner-shape; browsers without it show round corners.</span>
<div style="display: flex; align-items: center; gap: 8px"><span style="flex: 1">Elliptical corners</span>{sw_(False)}</div>
<span style="margin-top: -6px; font-size: 11px; color: #939393">Different across and down, e.g. 24 / 12</span>
<div style="display: flex; align-items: center; gap: 8px"><span style="flex: 1">Grow with the screen</span>{sw_(True)}</div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">{fld('<span style="font-size: 11px; color: #939393">Mobile</span><span style="flex: 1; text-align: right">8</span>')}{fld('<span style="font-size: 11px; color: #939393">Desktop</span><span style="flex: 1; text-align: right">12</span>')}</div>
{css('border-radius: clamp(8px, 0.4vw + 6.5px, 12px);' + chr(10) + 'corner-shape: squircle;')}</section>'''

# D · on the canvas
D = f'''<div style="position: relative; width: 480px; height: 300px; border-radius: 6px; background: #e7d9c7; box-shadow: 0 0 0 1px #3a3a3a">
<div style="position: absolute; left: 90px; top: 50px; width: 300px; height: 200px; border-radius: 18px; background: #ffffff; outline: 1.5px solid #2f80ed; outline-offset: 0px">
<span style="position: absolute; left: 10px; top: 10px; width: 9px; height: 9px; box-sizing: border-box; border-radius: 5px; background: #2f80ed; border: 1.5px solid #fff"></span>
{''.join(f'<span style="position: absolute; {p}; width: 7px; height: 7px; box-sizing: border-box; border-radius: 4px; background: #fff; border: 1.2px solid #2f80ed"></span>' for p in ['right: 10px; top: 10px', 'right: 10px; bottom: 10px', 'left: 10px; bottom: 10px'])}
<svg style="position: absolute; left: 0; top: 0" width="40" height="40"><path d="M1 30V18A17 17 0 0 1 18 1h12" fill="none" stroke="#2f80ed" stroke-width="1" stroke-dasharray="3 2"/></svg>
<span style="position: absolute; left: 24px; top: 24px; height: 22px; padding: 0 8px; display: flex; align-items: center; gap: 6px; border-radius: 11px; background: #1f1f1f; color: #e8e8e8; font-size: 11px; white-space: nowrap">18 → snaps to <b style="font-weight: 600">lg 20</b></span>
<svg style="position: absolute; left: 12px; top: 18px" width="16" height="20" viewBox="0 0 16 20"><path d="M2 1v15l4-4 3 6 2-1-3-6h5z" fill="#fff" stroke="#1d1a16" stroke-width="1.4"/></svg></div></div>
<div style="margin-top: 8px; font-size: 11px; line-height: 16px; color: #a8a8a8">Drag a round handle inside a corner. All four move together; <b style="font-weight: 500; color: #e8e8e8">Alt</b> moves one corner, <b style="font-weight: 500; color: #e8e8e8">Shift</b> turns snapping to tokens off.</div>'''

# E · the triggers
cap_ob = f'''<div style="display: flex; align-items: center; gap: 2px; height: 28px; padding: 2px; box-sizing: border-box; border-radius: 6px; background: #232323; width: max-content">
<span style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; background: #3a3a3a; box-shadow: 0 0 0 1px #2f80ed">{icon("radius", 13, "#a8a8a8")}12<span style="font-size: 10px; color: #939393">md</span>{icon("chev-down", 9, "#939393", 1.75)}</span></div>'''
border_row = f'''<div style="width: 276px; padding: 10px 12px; border-radius: 4px; background: #1f1f1f; display: flex; flex-direction: column; gap: 8px">
<div style="display: flex; justify-content: space-between"><b style="font-weight: 600">Border</b>{icon("sliders", 13, "#939393")}</div>
<div style="display: grid; grid-template-columns: 60px minmax(0, 1fr); gap: 8px; align-items: center"><span style="font-size: 11px; color: #939393">Corners</span>{fld(icon("radius", 12, "#939393") + '<span style="flex: 1">12</span>' + tokchip('radius-md'))}</div></div>'''
E = f'''<div style="display: flex; flex-direction: column; gap: 16px">
<div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 11px; color: #939393">Options bar (Select tool · in More on the compact frame, D-34)</span>{cap_ob}</div>
<div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 11px; color: #939393">Properties › Border</span>{border_row}</div>
<div style="max-width: 300px; font-size: 11px; line-height: 16px; color: #a8a8a8">One control: both are triggers that show the value and open the same popover (A). The value is edited only in the popover or by dragging on the canvas.</div></div>'''

body = sheet_header('D-35', 'Corner roundness', 'Rebuilt in the shared popover pattern: header with Pin and Close, design-system tokens first, CSS line, and Advanced as its own popover. border-radius · corner-shape.')
body += f'''<div style="display: grid; grid-template-columns: 328px 328px 700px; gap: 48px 56px; align-items: start">
<div>{cap('A · All corners', 'One value, token presets, slider. Linked to radius-md.')}{A}</div>
<div>{cap('B · Each corner', 'Four values around the shape, link to set them together, quick actions.')}{B}</div>
<div>{cap('C · Advanced (from A)', 'Its own popover beside the first, anchored to the pressed Advanced button.')}<div style="display: flex; gap: 14px; align-items: flex-start">{Asmall}{C}</div></div>
<div style="grid-column: span 2">{cap('D · On the canvas', 'Round handles inside each corner; the readout snaps to tokens.')}{D}</div>
<div>{cap('E · Where it opens from', 'Same popover from both places.')}{E}</div></div>'''
H = int(sys.argv[1]) if len(sys.argv) > 1 else 1300
open('/home/claude/daisy/project/Radius.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-35 Corner roundness', 1600, H, body))
print('ok')
