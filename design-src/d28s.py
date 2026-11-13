import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

REC = '#e5534b'
P['pause'] = ('fill', 'M4 3h3v10H4zM9 3h3v10H9z')
P['loop'] = ('stroke', 'M3 7a4 4 0 0 1 4-4h5l-2-2M13 9a4 4 0 0 1-4 4H4l2 2')
P['tostart'] = ('fill', 'M3 3h2v10H3zM13 3v10L6 8z')
P['rec'] = ('fill', 'M8 3a5 5 0 1 1 0 10A5 5 0 0 1 8 3z')
P['scroll'] = ('stroke', 'M5 2h6v12H5zM8 5v3')
pop = 'background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 10px 28px rgba(0,0,0,0.5);'
tb = lambda ic, l, on=False, c=None: f'<button aria-label="{l}" style="width: 24px; height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 4px; {"background: #333333; color: #e8e8e8;" if on else "color: #a8a8a8;"}">{icon(ic, 12, c or "currentColor", 1.75)}</button>'
chip = lambda t, extra='': f'<span style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 8px; border-radius: 4px; background: #262626; font-size: 11px; color: #c8c8c8; white-space: nowrap; {extra}">{t}</span>'

def frame(body, hdr_mid='', h=300, strip=None, rec=False, playing=False):
    trans = tb('tostart', 'Start') + tb('pause' if playing else 'play', 'Play', playing) + tb('loop', 'Loop') + tb('rec', 'Record keyframes', rec, REC if rec else '#a8a8a8')
    return f'''<div style="height: {h}px; display: flex; flex-direction: column; background: #1f1f1f; border: 1px solid {"#7a2f2b" if rec else "#303030"}; border-radius: 6px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.35)">
<div style="height: 30px; flex: none; display: flex; align-items: center; gap: 10px; padding: 0 8px 0 12px; border-bottom: 1px solid #303030">
<span style="display: flex; align-items: center; gap: 6px; color: #a8a8a8">{icon('code', 12)}Code</span>
<span style="position: relative; height: 30px; display: flex; align-items: center; gap: 6px; font-weight: 500">{icon('play', 10)}Timeline<span style="position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: #2f80ed"></span></span>
<span style="width: 1px; height: 14px; background: #333333"></span><div style="display: flex; gap: 1px">{trans}</div>{hdr_mid}</div>
<div style="flex: 1; min-height: 0; display: flex; position: relative">{body}</div>
{strip if strip is not None else ''}</div>'''
def stripbar(inner):
    return f'<div style="height: 22px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 12px; border-top: 1px solid #2c2c2c; font-size: 11px; color: #939393; white-space: nowrap">{inner}</div>'

# compact timeline renderer
def tl(rows, PX=300, X0=10, ticks=None, play=None, extra='', LW=150, tint=''):
    t2x = lambda t: X0 + t * PX
    ticks = ticks or [(i / 5, f'{i / 5:.1f}s') for i in range(0, 8)]
    ruler = ''.join(f'<span style="position: absolute; left: {t2x(t):.0f}px; bottom: 0; width: 1px; height: 6px; background: #555"></span><span style="position: absolute; left: {t2x(t) + 3:.0f}px; top: 3px; font-size: 9px; color: #939393">{lab}</span>' for t, lab in ticks)
    lrows, rrows = '', ''
    for r in rows:
        kind, name, sub = r[0], r[1], r[2]
        pad = {'seq': 8, 'el': 18, 'prop': 32}[kind]
        lrows += f'<div style="height: 22px; display: flex; align-items: center; gap: 6px; padding: 0 6px 0 {pad}px; border-bottom: 1px solid #262626; font-size: 11px; {r[4] if len(r) > 4 else ""}"><span style="color: {"#e8e8e8" if kind != "prop" else "#c8c8c8"}; {"font-weight: 600;" if kind == "seq" else ""} white-space: nowrap">{name}</span><span style="flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-size: 10px; color: #939393">{sub}</span></div>'
        body = ''
        for item in r[3]:
            if item[0] == 'clip':
                _, a, b, on = item
                body += f'<span style="position: absolute; left: {t2x(a):.0f}px; width: {(b - a) * PX:.0f}px; top: 4px; height: 13px; border-radius: 3px; {"background: rgba(47,128,237,0.30); box-shadow: inset 0 0 0 1px #2f80ed;" if on else "background: rgba(47,128,237,0.16); box-shadow: inset 0 0 0 1px rgba(47,128,237,0.45);"}"></span>'
            elif item[0] == 'seqbar':
                _, a, b = item
                body += f'<span style="position: absolute; left: {t2x(a):.0f}px; width: {(b - a) * PX:.0f}px; top: 5px; height: 12px; border-radius: 3px; background: #2a2f38; box-shadow: inset 0 0 0 1px #3d4757"></span>'
            elif item[0] == 'key':
                _, t, st = item
                s = {'on': 'background: #2f80ed; box-shadow: 0 0 0 2px #1b1b1b, 0 0 0 3.5px #2f80ed;', 'rec': f'background: {REC}; box-shadow: 0 0 0 2px #1b1b1b, 0 0 0 4px rgba(229,83,75,0.55);', 'off': 'background: #c8c8c8;', 'hold': 'background: #c8c8c8; border-radius: 0; transform: none;'}[st]
                body += f'<span style="position: absolute; left: {t2x(t) - 5:.0f}px; top: 6px; width: 9px; height: 9px; box-sizing: border-box; transform: rotate(45deg); border-radius: 1.5px; {s}"></span>'
            elif item[0] == 'line':
                _, a, b = item
                body += f'<span style="position: absolute; left: {t2x(a):.0f}px; width: {(b - a) * PX:.0f}px; top: 10px; height: 1.25px; background: rgba(47,128,237,0.6)"></span>'
        rrows += f'<div style="position: relative; height: 22px; border-bottom: 1px solid #262626; {r[4] if len(r) > 4 else ""}">{body}</div>'
    ph = f'<div style="position: absolute; left: {LW + t2x(play) - 0.5:.0f}px; top: 0; bottom: 0; width: 1px; background: #e8e8e8; z-index: 3"></div>' if play is not None else ''
    return (f'<div style="width: {LW}px; flex: none; border-right: 1px solid #2c2c2c"><div style="height: 22px; border-bottom: 1px solid #2c2c2c"></div>{lrows}</div>'
            f'<div style="position: relative; flex: 1; min-width: 0; background: #1b1b1b {tint}"><div style="position: relative; height: 22px; border-bottom: 1px solid #2c2c2c; background: #1f1f1f">{ruler}</div>{rrows}</div>{ph}{extra}')
cap = lambda t, desc: f'<div style="display: flex; flex-direction: column; gap: 2px; margin-bottom: 10px"><div style="font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{desc}</div></div>'
base_rows = lambda sel=True: [
    ('seq', 'Hero entrance', '5 elements', [('seqbar', 0, 1.4)]),
    ('el', 'Eyebrow', 'p', [('clip', 0, 0.6, False)]),
    ('el', 'Hero title', 'h1', [('clip', 0.08, 0.68, sel)], 'background: rgba(47,128,237,0.08);' if sel else ''),
    ('prop', 'Opacity', '0 → 100%', [('line', 0.08, 0.68), ('key', 0.08, 'off'), ('key', 0.68, 'off')]),
    ('prop', 'Move Y', '16 → 0 px', [('line', 0.08, 0.68), ('key', 0.08, 'off'), ('key', 0.68, 'on')]),
    ('el', 'Lede', 'p', [('clip', 0.16, 0.76, False)]),
]

# 1 · Scroll-linked
s1_ticks = [(i * 0.25, f'{i * 25}%') for i in range(0, 5)]
mini_page = f'''<div style="width: 120px; flex: none; padding: 8px; box-sizing: border-box; border-left: 1px solid #2c2c2c; display: flex; flex-direction: column; gap: 6px">
<div style="font-size: 10px; color: #939393">Page scroll</div>
<div style="position: relative; height: 170px; border-radius: 3px; background: #2a2a2a; box-shadow: inset 0 0 0 1px #3a3a3a">
<span style="position: absolute; left: 6px; right: 6px; top: 40px; height: 52px; border-radius: 2px; background: rgba(47,128,237,0.25); box-shadow: inset 0 0 0 1px #2f80ed"></span>
<span style="position: absolute; left: 0; right: 0; top: 70px; height: 1px; background: #e8e8e8"></span>
<span style="position: absolute; left: 6px; top: 44px; font-size: 9px; color: #a9c8f7">This season</span>
<span style="position: absolute; left: 6px; bottom: 6px; right: 6px; font-size: 9px; line-height: 12px; color: #939393">enters → leaves the screen</span></div></div>'''
S1 = frame(tl([('seq', 'Season cards', 'scroll-linked', [('seqbar', 0, 1.0)]),
               ('el', 'Card 1', 'div', [('clip', 0, 0.6, True)]), ('el', 'Card 2', 'div', [('clip', 0.1, 0.7, False)]), ('el', 'Card 3', 'div', [('clip', 0.2, 0.8, False)]),
               ('prop', 'Move Y', '40 → 0', [('line', 0, 0.6), ('key', 0, 'off'), ('key', 0.6, 'on')])], PX=420, ticks=s1_ticks, play=0.55) + mini_page,
           hdr_mid=chip(icon('scroll', 11) + 'Scroll-linked: This season enters → leaves') + '<span style="flex: 1"></span>' + chip('55% scrolled'),
           strip=stripbar('<span>The ruler is scroll progress, not seconds · scrub by scrolling the canvas</span><span style="flex: 1"></span><span>animation-timeline: view()</span>'))

# 2 · Recording keyframes
rec_rows = base_rows()
rec_rows[4] = ('prop', 'Move Y', '16 → 0 px', [('line', 0.08, 0.68), ('key', 0.08, 'off'), ('key', 0.68, 'off')])
rec_rows.append(('prop', 'Rotate', 'new · 0 → −2°', [('key', 0.08, 'off'), ('key', 0.52, 'rec')], f'background: rgba(229,83,75,0.08);'))
S2 = frame(tl(rec_rows, play=0.52, tint='; box-shadow: inset 0 0 0 1px rgba(229,83,75,0.5)'),
           rec=True, hdr_mid=f'<span style="display: flex; align-items: center; gap: 6px; height: 22px; padding: 0 8px; border-radius: 4px; background: rgba(229,83,75,0.16); color: #ff938c; font-size: 11px; font-weight: 500">{icon("rec", 9, REC)}Recording</span><span style="font-size: 11px; color: #c8c8c8">Change anything on the canvas to key it at <b style="font-weight: 600">0.52 s</b></span><span style="flex: 1"></span>' + chip('Esc stops'),
           strip=stripbar(f'<span style="color: #ff938c">● 1 new keyframe</span><span>· Rotate −2° at 0.52 s on Hero title</span><span style="flex: 1"></span><span>R toggles recording</span>'))

# 3 · Keyframe tab
fld = lambda lab, val, unit='', focus=False: f'<label style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; background: #2a2a2a; border-radius: 2px; {"box-shadow: inset 0 0 0 1px #2f80ed;" if focus else ""}"><span style="font-size: 11px; color: #939393">{lab}</span><span style="flex: 1; text-align: right">{val}</span><span style="font-size: 10px; color: #939393">{unit}</span></label>'
segm = lambda items, sel: '<div style="display: grid; grid-template-columns: repeat(' + str(len(items)) + ', minmax(0, 1fr)); gap: 2px; padding: 2px; background: #262626; border-radius: 4px; font-size: 11px">' + ''.join(f'<span style="height: 20px; display: flex; align-items: center; justify-content: center; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #939393;"}">{t}</span>' for i, t in enumerate(items)) + '</div>'
insp3 = f'''<aside style="width: 270px; flex: none; padding: 10px 12px; box-sizing: border-box; display: flex; flex-direction: column; gap: 8px; border-left: 1px solid #2c2c2c">
<div style="display: flex; gap: 14px; font-size: 11px; font-weight: 500"><span style="color: #939393">Easing</span><span style="color: #e8e8e8; box-shadow: 0 2px 0 #2f80ed">Keyframe</span><span style="color: #939393">Sequence</span></div>
<div style="font-size: 11px"><b style="font-weight: 600">Move Y</b> <span style="color: #939393">· Hero title · end</span></div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px">{fld('At', '0.68', 's')}{fld('Value', '0', 'px', True)}</div>
<div style="font-size: 11px; color: #a8a8a8">Into this keyframe</div>{segm(['Smooth', 'Snappy', 'Linear', 'Hold'], 0)}
<div style="font-size: 11px; color: #a8a8a8">Value from</div>{segm(['Typed', 'Current on canvas', 'Token'], 0)}
<div style="font-size: 10px; line-height: 14px; color: #939393">Hold keeps the value until the next keyframe (a step) · Token uses a spacing or size from Halden</div></aside>'''
S3 = frame(tl(base_rows(), play=0.68) + insp3, hdr_mid='<span style="flex: 1"></span>' + chip('0.68 / 1.40 s'))

# 4 · Stagger popover
st_bar = lambda i, d: f'<span style="position: absolute; left: {10 + i * d}px; top: {5 + i * 9}px; width: 80px; height: 6px; border-radius: 2px; background: rgba(47,128,237,0.45)"></span>'
stag = f'''<div style="position: absolute; left: 230px; top: 6px; width: 300px; padding: 10px; box-sizing: border-box; display: flex; flex-direction: column; gap: 8px; {pop} z-index: 4">
<div style="display: flex; align-items: center; justify-content: space-between"><b style="font-weight: 600">Stagger</b><span style="font-size: 11px; color: #939393">Hero entrance · 5 elements</span></div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px">{fld('Each', '0.08', 's', True)}{fld('Total', '0.32', 's')}</div>
<div style="font-size: 11px; color: #a8a8a8">Order</div>{segm(['In order', 'Reverse', 'From centre', 'Random'], 0)}
<div style="font-size: 11px; color: #a8a8a8">Spread</div>{segm(['Even', 'Ease out', 'Ease in'], 1)}
<div style="position: relative; height: 52px; border-radius: 3px; background: #1b1b1b">{''.join(st_bar(i, [0, 16, 28, 36, 40][i]) for i in range(5))}</div>
</div>'''
S4 = frame(tl(base_rows(False), play=0.0) + stag, hdr_mid='<span style="flex: 1"></span>' + chip('Opened from the sequence bar'))

# 5 · Sequence tab
insp5 = f'''<div style="flex: 1; padding: 12px 16px; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px 24px; align-content: start">
<div style="grid-column: 1 / 3; display: flex; gap: 14px; font-size: 11px; font-weight: 500"><span style="color: #939393">Easing</span><span style="color: #939393">Keyframe</span><span style="color: #e8e8e8; box-shadow: 0 2px 0 #2f80ed">Sequence</span></div>
<div style="display: flex; flex-direction: column; gap: 6px">{fld('Name', 'Hero entrance')}<div style="font-size: 11px; color: #a8a8a8">Starts</div>{segm(['On load', 'Scroll into view', 'Hover', 'Click'], 1)}
{fld('When', '20% visible')}{fld('Delay', '0', 's')}</div>
<div style="display: flex; flex-direction: column; gap: 6px"><div style="font-size: 11px; color: #a8a8a8">Plays</div>{segm(['Once', 'Every time', 'Loop'], 0)}
<div style="font-size: 11px; color: #a8a8a8">On screen sizes</div>{segm(['All', 'Desktop', 'Tablet', 'Mobile'], 0)}
<div style="font-size: 11px; color: #a8a8a8">Less motion</div>{segm(['Fade only', 'Skip', 'Same'], 0)}</div></div>'''
S5 = frame(insp5, hdr_mid='<span style="flex: 1"></span>' + chip('Hero entrance ▾'))

# 6 · Empty: add animation
pre = lambda name, sub, glyph: f'<button style="display: flex; flex-direction: column; gap: 6px; padding: 10px; border-radius: 6px; background: #262626; text-align: left"><span style="height: 34px; display: flex; align-items: center; justify-content: center; border-radius: 4px; background: #1b1b1b">{glyph}</span><span style="font-size: 11px; color: #e8e8e8">{name}</span><span style="margin-top: -4px; font-size: 10px; color: #939393">{sub}</span></button>'
g = lambda style: f'<span style="width: 22px; height: 14px; border-radius: 2px; background: #7fb0f0; {style}"></span>'
s6 = (f'<div style="flex: 1; padding: 14px 16px; display: flex; flex-direction: column; gap: 10px">'
      '<div><b style="font-weight: 600">Shop the collection has no animation</b><div style="font-size: 11px; color: #939393; margin-top: 2px">Pick a start, then tweak it on the timeline · or record your own</div></div>'
      '<div style="display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 8px">'
      + pre('Fade in', '0.4 s', g('opacity: 0.4')) + pre('Fade in up', '0.6 s', g('transform: translateY(4px); opacity: 0.6')) + pre('Slide in', 'from left', g('transform: translateX(-6px)'))
      + pre('Scale in', '0.95 → 1', g('transform: scale(0.8)')) + pre('Blur in', '6 → 0 px', g('filter: blur(2px)')) + pre('Pulse', 'loops · hover', g('box-shadow: 0 0 0 3px rgba(127,176,240,0.35)'))
      + '</div><div style="display: flex; gap: 8px"><button style="height: 24px; padding: 0 10px; border-radius: 4px; background: #333333; font-size: 11px; color: #e8e8e8">Add to “Hero entrance”</button>'
      f'<button style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; font-size: 11px; color: #ff938c; box-shadow: inset 0 0 0 1px rgba(229,83,75,0.5)">{icon("rec", 8, REC)}Record your own</button></div></div>')
S6 = frame(s6, hdr_mid='<span style="flex: 1"></span>' + chip('No sequence'))

# 7 · Keyframe context menu
mi = lambda t, kb='', danger=False, sep=False: ('<div style="height: 1px; background: #3a3a3a; margin: 4px 0"></div>' if sep else f'<div style="height: 26px; display: flex; align-items: center; padding: 0 8px; border-radius: 3px; color: {"#ff938c" if danger else "#e8e8e8"}"><span style="flex: 1">{t}</span><span style="font-size: 11px; color: #939393">{kb}</span></div>')
menu = (f'<div style="position: absolute; left: 400px; top: 32px; width: 230px; padding: 4px; {pop} z-index: 4; font-size: 12px">'
        + mi('Copy', 'Ctrl C') + mi('Paste at playhead', 'Ctrl V') + mi('', sep=True) + mi('Ease: Smooth ▸') + mi('Hold until next')
        + mi('Select all on this track', 'Ctrl A') + mi('', sep=True) + mi('Delete', 'Del', True) + '</div>')
S7 = frame(tl(base_rows(), play=0.4) + menu, hdr_mid='<span style="flex: 1"></span>' + chip('Right-click a keyframe'))

# 8 · Conflict: two tracks write transform
warn = f'''<div style="position: absolute; left: 160px; right: 12px; bottom: 8px; padding: 8px 10px; display: flex; align-items: center; gap: 10px; border-radius: 4px; background: rgba(210,153,34,0.12); box-shadow: inset 0 0 0 1px rgba(210,153,34,0.5); font-size: 11px; z-index: 3">
{icon('warning', 13, '#d29922', 1.5)}<span style="flex: 1; color: #c8c8c8"><b style="font-weight: 600; color: #e8e8e8">Move Y</b> and the hover <b style="font-weight: 600; color: #e8e8e8">Scale</b> both write <code style="font-family: {MONO}">transform</code>; one would cancel the other.</span>
<button style="height: 22px; padding: 0 8px; border-radius: 3px; background: #246bcb; color: #fff">Use separate properties</button></div>'''
S8 = frame(tl(base_rows()[:5], play=0.4) + warn, hdr_mid='<span style="flex: 1"></span>' + chip(icon('warning', 10, '#d29922', 1.75) + '1 conflict', 'color: #e3b34a;'))

# 9 · Performance hint while playing
perf = f'''<div style="position: absolute; right: 12px; top: 30px; width: 280px; padding: 10px; display: flex; flex-direction: column; gap: 6px; {pop} z-index: 4; font-size: 11px; line-height: 16px">
<div style="display: flex; align-items: center; gap: 6px"><span style="width: 8px; height: 8px; border-radius: 4px; background: #d29922"></span><b style="font-weight: 600">Heavy on phones</b><span style="flex: 1"></span><span style="color: #939393">52 fps</span></div>
<div style="color: #c8c8c8">Blur on a 64 px heading is costly. Move and fade are cheap.</div>
<div style="display: flex; gap: 6px"><button style="height: 22px; padding: 0 8px; border-radius: 3px; background: #246bcb; color: #fff">Remove blur</button><button style="height: 22px; padding: 0 8px; border-radius: 3px; background: #333333; color: #c8c8c8">Keep</button></div></div>'''
S9 = frame(tl(base_rows() + [('prop', 'Blur', '6 → 0 px', [('line', 0.08, 0.38), ('key', 0.08, 'off'), ('key', 0.38, 'off')], 'background: rgba(210,153,34,0.08);')], play=0.3) + perf,
           playing=True, hdr_mid='<span style="flex: 1"></span>' + chip('Playing · loop'))

# 10 · Collapsed with mini player
bar = lambda inner: f'<div style="height: 28px; display: flex; align-items: center; gap: 12px; padding: 0 8px 0 12px; background: #1f1f1f; border: 1px solid #303030; border-radius: 6px; font-size: 12px">{inner}</div>'
S10 = f'''<div style="display: flex; flex-direction: column; gap: 10px">
{bar(f'<span style="display: flex; align-items: center; gap: 6px; color: #a8a8a8">{icon("code", 12)}Code</span><span style="display: flex; align-items: center; gap: 6px; color: #e8e8e8">{icon("play", 10)}Timeline</span><span style="width: 1px; height: 14px; background: #333333"></span>{tb("pause", "Pause", True)}<span style="font-size: 11px; color: #c8c8c8">Hero entrance · 0.40 s</span><span style="position: relative; width: 160px; height: 3px; border-radius: 2px; background: #3a3a3a"><span style="position: absolute; left: 0; width: 46px; height: 3px; border-radius: 2px; background: #2f80ed"></span></span><span style="flex: 1"></span>{tb("chev-up", "Expand")}')}
<div style="font-size: 10px; color: #939393; margin: -4px 0 4px 4px">Collapsed while playing · a mini player keeps play, time and progress</div>
{bar(f'<span style="display: flex; align-items: center; gap: 6px; color: #a8a8a8">{icon("code", 12)}Code</span><span style="display: flex; align-items: center; gap: 6px; color: #e8e8e8">{icon("play", 10)}Timeline</span><span style="display: flex; align-items: center; gap: 5px; height: 16px; padding: 0 6px; border-radius: 8px; background: rgba(229,83,75,0.16); color: #ff938c; font-size: 10px; font-weight: 500">{icon("rec", 7, REC)}Recording</span><span style="flex: 1"></span>{tb("chev-up", "Expand")}')}
<div style="font-size: 10px; color: #939393; margin: -4px 0 4px 4px">Collapsed while recording · the red badge never hides</div>
<div style="padding: 10px 12px; border-radius: 6px; background: #1a1a1a; box-shadow: inset 0 0 0 1px #2a2a2a; font-size: 11px; line-height: 16px; color: #a8a8a8"><b style="color: #e8e8e8">Red is only for recording.</b> Like violet for states and amber for screen sizes, it marks a mode; everything else in the Timeline uses the normal accent.</div></div>'''

cells = [
    ('1 · Scroll-linked', 'The ruler becomes scroll progress (0–100%) of a section passing through the screen; a page map shows where you are', S1),
    ('2 · Recording keyframes', 'Record on: change anything on the canvas and it is keyed at the playhead; red border and badge', S2),
    ('3 · Keyframe tab', 'Exact time and value, how to arrive (Smooth, Snappy, Linear, Hold), and where the value comes from', S3),
    ('4 · Stagger', 'From the sequence bar: gap between elements, order and spread, with a live preview', S4),
    ('5 · Sequence tab', 'Name, trigger and threshold, delay, how often it plays, on which screen sizes, and what “less motion” does', S5),
    ('6 · No animation yet', 'Presets to start from, added into a sequence, or record your own', S6),
    ('7 · Keyframe menu', 'Copy, paste at playhead, ease, hold, select all on the track, delete', S7),
    ('8 · Conflict', 'Two animations writing the same CSS property; one click splits them into separate properties', S8),
    ('9 · Performance hint', 'While playing: frame rate and a fix when something is heavy on phones', S9),
    ('10 · Collapsed', 'Mini player while playing; recording badge while recording', S10),
]
body = sheet_header('D-28b', 'Timeline · states', 'Every state of the Timeline drawn at real size: scroll-linked mode, recording, the Keyframe and Sequence tabs, stagger, empty, the keyframe menu, conflicts, performance and the collapsed bars. Read with D-28, which shows the default editing state.')
body += '<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 48px 64px; align-items: start">' + ''.join(f'<div>{cap(t, dsc)}{c}</div>' for t, dsc, c in cells) + '</div>'
H = int(sys.argv[1]) if len(sys.argv) > 1 else 2300
open('/home/claude/daisy/project/D28b-Timeline-States.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-28b Timeline states', 1920, H, body))
print('ok')
