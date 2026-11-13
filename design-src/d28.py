from screen import *

S = Screen('Daisy · D-28 Timeline')
S.remove_h1_overlay()
S.unselect_h1_row()
S.remove_parent_outline()
P['pause'] = ('fill', 'M4 3h3v10H4zM9 3h3v10H9z')
P['loop'] = ('stroke', 'M3 7a4 4 0 0 1 4-4h5l-2-2M13 9a4 4 0 0 1-4 4H4l2 2')
P['tostart'] = ('fill', 'M3 3h2v10H3zM13 3v10L6 8z')
P['prevkey'] = ('stroke', 'M10 3L5 8l5 5M4 8h0')
P['nextkey'] = ('stroke', 'M6 3l5 5-5 5')
P['max'] = ('stroke', 'M3 6V3h3M10 3h3v3M13 10v3h-3M6 13H3v-3')
P['magnet'] = ('stroke', 'M4 2.5v6a4 4 0 0 0 8 0v-6M4 5.5h3M9 5.5h3')
P['marker'] = ('stroke', 'M8 2v12M8 2h5l-1.5 2L13 6H8')
P['eye'] = P.get('eye', ('stroke', 'M1.5 8S4 3.5 8 3.5 14.5 8 14.5 8 12 12.5 8 12.5 1.5 8 1.5 8z'))

T = 0.40                                       # playhead
# ---------------- canvas: hero at the playhead frame (staggered) ----------------
def frame_at(start, dur=0.6, dy=16):
    p = max(0.0, min(1.0, (T - start) / dur))
    e = 1 - (1 - p) ** 3                     # smooth (ease-out)
    return round(e, 2), round(dy * (1 - e), 1)
st = {}
for name, start in [('eyebrow', 0.0), ('title', 0.08), ('lede', 0.16), ('buttons', 0.24)]:
    st[name] = frame_at(start)
sty = lambda k: f'opacity: {st[k][0]}; transform: translateY({st[k][1]}px);'
S.rep('<p style="margin: 0; font-size: 13px; line-height: 20px; text-transform: uppercase; letter-spacing: 0.08em; color: #5f6b4e; font-weight: 500">',
      f'<p style="margin: 0; font-size: 13px; line-height: 20px; text-transform: uppercase; letter-spacing: 0.08em; color: #5f6b4e; font-weight: 500; {sty("eyebrow")}">')
S.rep('<h1 style="margin: 0; font-family: \'Fraunces\', serif; font-size: 64px; line-height: 1.05; font-weight: 600; color: #1d1a16">',
      f'<h1 style="margin: 0; font-family: \'Fraunces\', serif; font-size: 64px; line-height: 1.05; font-weight: 600; color: #1d1a16; {sty("title")} filter: blur(1px)">')
S.rep('<p style="margin: 0; font-size: 18px; line-height: 1.6; color: #4a443c; max-width: 480px">',
      f'<p style="margin: 0; font-size: 18px; line-height: 1.6; color: #4a443c; max-width: 480px; {sty("lede")}">')
S.rep('<div style="display: flex; align-items: center; gap: 24px">', f'<div style="display: flex; align-items: center; gap: 24px; {sty("buttons")}">')
# h1 selection outline (stays full strength) + end-position ghost
hpos = ['left: -5.6px; top: -5.6px', 'right: -5.6px; top: -5.6px', 'right: -5.6px; bottom: -5.6px', 'left: -5.6px; bottom: -5.6px']
handles = ''.join(f'<span style="position: absolute; {p}; width: 9.4px; height: 9.4px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>' for p in hpos)
S.rep('<div style="position: relative; width: 560px">',
      f'<div style="position: relative; width: 560px"><div aria-hidden="true" style="position: absolute; inset: -1px; border: 1.18px dashed #8a8a8a; pointer-events: none"><span style="position: absolute; right: 0; top: calc(100% + 3px); font: 500 11px/1 \'Inter\', sans-serif; color: #6b6b6b">end</span></div>'
      f'<div aria-hidden="true" style="position: absolute; inset: -1px; transform: translateY({st["title"][1]}px); border: 1.76px solid #2f80ed; pointer-events: none; z-index: 4">{handles}<span style="position: absolute; left: -1.76px; bottom: calc(100% + 2px); height: 21px; padding: 0 6px; display: flex; align-items: center; background: #246bcb; color: #fff; font: 500 13px/1 \'Inter\', sans-serif; white-space: nowrap">Heading · h1 · ▶ {T:.2f} s · {int(st["title"][0] * 100)}%</span></div>')
S.options('0', '64', '560', 'Fixed', '202', 'Fit')
set_tree(S, hero_tree('Hero title'))

# ---------------- timeline geometry ----------------
LW, IW = 232, 288          # track list and inspector widths
PX, X0, END = 460, 14, 1.6  # px per second, left pad inside the time area, sequence end
t2x = lambda t: X0 + t * PX
ROW = 24
sel_keys = {('Hero title', 'Opacity', 0.68), ('Hero title', 'Move Y', 0.68)}
tracks = [  # (kind, label, sub, clip(start,end) or keys, extra)
    ('seq', 'Hero entrance', '5 elements · stagger 0.08 s', (0.0, 1.4)),
    ('el', 'Eyebrow', 'p', (0.0, 0.6)),
    ('el', 'Hero title', 'h1', (0.08, 0.68), 'open'),
    ('prop', 'Opacity', '0 → 100%', [0.08, 0.68]),
    ('prop', 'Move Y', '16 → 0 px', [0.08, 0.68]),
    ('prop', 'Blur', '6 → 0 px', [0.08, 0.38]),
    ('el', 'Lede', 'p', (0.16, 0.76)),
    ('el', 'Buttons', 'div', (0.24, 0.84)),
    ('el', 'Hero image', 'img · scale 1.04 → 1', (0.0, 1.4)),
]
def left_row(i, kind, label, sub, extra=''):
    pad = {'seq': 10, 'el': 22, 'prop': 44}[kind]
    chev = icon('chev-down', 10, '#a8a8a8', 1.75) if kind == 'seq' or extra == 'open' else (icon('chev-right', 10, '#6b6b6b', 1.75) if kind == 'el' else '<span style="width: 10px"></span>')
    on = label == 'Hero title'
    name_style = 'font-weight: 600; color: #e8e8e8;' if kind == 'seq' else ('color: #e8e8e8;' if kind == 'el' else 'color: #c8c8c8;')
    tools = '' if kind == 'seq' else f'<span style="display: flex; gap: 4px; color: #6b6b6b">{icon("eye", 11)}{icon("lock", 11)}</span>'
    kf = f'<span title="Add keyframe at playhead" style="width: 9px; height: 9px; transform: rotate(45deg); box-sizing: border-box; border: 1.25px solid #8a8a8a; border-radius: 1px; margin-right: 2px"></span>' if kind == 'prop' else ''
    return (f'<div style="height: {ROW}px; display: flex; align-items: center; gap: 6px; padding: 0 8px 0 {pad}px; box-sizing: border-box; border-bottom: 1px solid #262626; {"background: rgba(47,128,237,0.12);" if on else ""}">'
            f'{chev}<span style="{name_style} font-size: 11px; white-space: nowrap">{label}</span><span style="flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-size: 10px; color: #939393">{sub}</span>{kf}{tools}</div>')
def dia(t, on=False, ghost=False):
    st_ = 'background: #2f80ed; box-shadow: 0 0 0 2px #1b1b1b, 0 0 0 3.5px #2f80ed;' if on else ('background: transparent; border: 1.25px solid #8a8a8a;' if ghost else 'background: #c8c8c8;')
    return f'<span style="position: absolute; left: {t2x(t) - 5:.0f}px; top: 7px; width: 10px; height: 10px; box-sizing: border-box; transform: rotate(45deg); border-radius: 1.5px; {st_} z-index: 2"></span>'
def ease_seg(t1, t2, label=''):
    w = (t2 - t1) * PX
    return (f'<svg aria-hidden="true" style="position: absolute; left: {t2x(t1):.0f}px; top: 4px" width="{w:.0f}" height="16" viewBox="0 0 {w:.0f} 16"><path d="M0 14 C {w * 0.2:.0f} 14, {w * 0.2:.0f} 2, {w:.0f} 2" fill="none" stroke="rgba(47,128,237,0.7)" stroke-width="1.25"></path></svg>'
            + (f'<span style="position: absolute; left: {t2x(t1) + 10:.0f}px; top: 5px; font-size: 9px; color: #939393">{label}</span>' if label else ''))
def right_row(kind, label, sub, data, extra=''):
    body = ''
    if kind == 'seq':
        a, b = data
        body = f'<span style="position: absolute; left: {t2x(a):.0f}px; width: {(b - a) * PX:.0f}px; top: 5px; height: 14px; border-radius: 3px; background: #2a2f38; box-shadow: inset 0 0 0 1px #3d4757"></span>'
    elif kind == 'el':
        a, b = data
        on = label == 'Hero title'
        body = (f'<span style="position: absolute; left: {t2x(a):.0f}px; width: {(b - a) * PX:.0f}px; top: 5px; height: 14px; box-sizing: border-box; border-radius: 3px; '
                f'{"background: rgba(47,128,237,0.30); box-shadow: inset 0 0 0 1px #2f80ed;" if on else "background: rgba(47,128,237,0.16); box-shadow: inset 0 0 0 1px rgba(47,128,237,0.45);"}">'
                f'<span style="position: absolute; left: 0; top: 0; bottom: 0; width: 4px; border-radius: 3px 0 0 3px; background: rgba(255,255,255,0.25)"></span><span style="position: absolute; right: 0; top: 0; bottom: 0; width: 4px; border-radius: 0 3px 3px 0; background: rgba(255,255,255,0.25)"></span></span>')
    else:
        a, b = data
        body = ease_seg(a, b, 'Smooth' if label == 'Opacity' else '') + dia(a) + dia(b, ('Hero title', label, b) in sel_keys)
    return f'<div style="position: relative; height: {ROW}px; border-bottom: 1px solid #262626; {"background: rgba(47,128,237,0.06);" if label == "Hero title" else ""}">{body}</div>'
left = ''.join(left_row(i, *tr[:3], *(tr[4:] or [''])) for i, tr in enumerate(tracks))
right = ''.join(right_row(tr[0], tr[1], tr[2], tr[3], *(tr[4:] or [''])) for tr in tracks)
ruler = ''
for i in range(0, 17):
    t = i / 10
    major = i % 2 == 0
    ruler += f'<span style="position: absolute; left: {t2x(t):.0f}px; bottom: 0; width: 1px; height: {9 if major else 4}px; background: #555555"></span>'
    if major:
        ruler += f'<span style="position: absolute; left: {t2x(t) + 4:.0f}px; top: 4px; font-size: 10px; color: #939393">{t:.1f}s</span>'
marker = f'<span style="position: absolute; left: {t2x(0.84) - 0.5:.0f}px; top: 0; height: 26px; border-left: 1px solid #f2b84b"><span style="position: absolute; left: 3px; top: 12px; height: 12px; padding: 0 4px; border-radius: 3px; background: rgba(242,184,75,0.18); color: #f2cf7f; font-size: 9px; line-height: 12px; white-space: nowrap">Buttons ready</span></span>'
workarea = f'<span style="position: absolute; left: {t2x(0):.0f}px; width: {1.4 * PX:.0f}px; bottom: 0; height: 3px; background: rgba(47,128,237,0.5)"></span>'
playhead = f'<div aria-hidden="true" style="position: absolute; left: {t2x(T) - 0.5:.0f}px; top: 0; bottom: 0; width: 1px; background: #e8e8e8; z-index: 5"><span style="position: absolute; left: -6px; top: 13px; width: 13px; height: 13px; background: #e8e8e8; clip-path: polygon(0 0, 100% 0, 100% 55%, 50% 100%, 0 55%)"></span></div>'
marquee = f'<div aria-hidden="true" style="position: absolute; left: {t2x(0.68) - 12:.0f}px; top: {26 + ROW * 3 + 1}px; width: 24px; height: {ROW * 2 - 2}px; border: 1px dashed #2f80ed; background: rgba(47,128,237,0.08); border-radius: 2px; z-index: 1"></div>'
stagger = f'<div aria-hidden="true" style="position: absolute; left: {t2x(0) - 2:.0f}px; top: {26 + ROW + 4}px; height: {ROW * 7 - 8}px; width: 1px; border-left: 1px dashed #6b6b6b"></div>'
endline = f'<div aria-hidden="true" style="position: absolute; left: {t2x(1.4):.0f}px; top: 26px; bottom: 0; width: 1px; background: #454545"></div>'
timeline = f'''<div style="position: relative; flex: 1; min-width: 0; background: #1b1b1b; overflow: hidden">
<div style="position: relative; height: 26px; border-bottom: 1px solid #2c2c2c; background: #1f1f1f">{ruler}{workarea}{marker}</div>
<div style="position: relative">{right}</div>
<div style="position: relative; height: {ROW}px"><span style="position: absolute; left: {t2x(0):.0f}px; top: 4px; font-size: 10px; color: #6b6b6b">Drag a clip to move · drag its ends to change its length · Shift+drag keeps the stagger</span></div>
{playhead}{marquee}{stagger}{endline}</div>'''
track_list = f'''<div style="width: {LW}px; flex: none; display: flex; flex-direction: column; border-right: 1px solid #2c2c2c; background: #1f1f1f">
<div style="height: 26px; flex: none; display: flex; align-items: center; gap: 6px; padding: 0 8px 0 10px; border-bottom: 1px solid #2c2c2c; font-size: 11px">
<button style="display: flex; align-items: center; gap: 4px; color: #e8e8e8; font-weight: 500">Hero entrance{icon('chev-down', 10, '#939393', 1.75)}</button><span style="flex: 1"></span><button style="color: #a9c8f7; font-size: 11px">+ Sequence</button></div>
{left}
<div style="height: {ROW}px; display: flex; align-items: center; padding-left: 22px"><button style="font-size: 11px; color: #a8a8a8">+ Add element</button></div></div>'''

# ---------------- inspector: Easing curve editor ----------------
CW, CH = 256, 150
cx = lambda x: 16 + x * (CW - 32)
cy = lambda y: CH - 18 - y * (CH - 36)
p1, p2 = (0.2, 0.8), (0.2, 1.0)
grid_lines = ''.join(f'<line x1="{cx(i / 4):.0f}" y1="{cy(0):.0f}" x2="{cx(i / 4):.0f}" y2="{cy(1):.0f}" stroke="#2a2a2a"></line><line x1="{cx(0):.0f}" y1="{cy(i / 4):.0f}" x2="{cx(1):.0f}" y2="{cy(i / 4):.0f}" stroke="#2a2a2a"></line>' for i in range(5))
curve = f'''<svg aria-label="Easing curve cubic-bezier(0.2, 0.8, 0.2, 1)" width="{CW}" height="{CH}" viewBox="0 0 {CW} {CH}" style="display: block; background: #1b1b1b; border-radius: 4px; box-shadow: inset 0 0 0 1px #2c2c2c">
{grid_lines}
<line x1="{cx(0)}" y1="{cy(0)}" x2="{cx(1)}" y2="{cy(1)}" stroke="#3a3a3a" stroke-dasharray="3 3"></line>
<path d="M{cx(0)} {cy(0)} C {cx(p1[0]):.1f} {cy(p1[1]):.1f}, {cx(p2[0]):.1f} {cy(p2[1]):.1f}, {cx(1)} {cy(1)}" fill="none" stroke="#2f80ed" stroke-width="2"></path>
<line x1="{cx(0)}" y1="{cy(0)}" x2="{cx(p1[0]):.1f}" y2="{cy(p1[1]):.1f}" stroke="#8a8a8a"></line><line x1="{cx(1)}" y1="{cy(1)}" x2="{cx(p2[0]):.1f}" y2="{cy(p2[1]):.1f}" stroke="#8a8a8a"></line>
<circle cx="{cx(p1[0]):.1f}" cy="{cy(p1[1]):.1f}" r="5" fill="#1b1b1b" stroke="#e8e8e8" stroke-width="1.5"></circle><circle cx="{cx(p2[0]):.1f}" cy="{cy(p2[1]):.1f}" r="5" fill="#2f80ed" stroke="#ffffff" stroke-width="1.5"></circle>
<circle cx="{cx(0)}" cy="{cy(0)}" r="3" fill="#8a8a8a"></circle><circle cx="{cx(1)}" cy="{cy(1)}" r="3" fill="#8a8a8a"></circle>
<circle cx="{cx(0.33):.0f}" cy="{cy(0.83):.0f}" r="3.5" fill="#e8e8e8"></circle>
<text x="{cx(0) + 2}" y="{CH - 4}" font-family="Inter, sans-serif" font-size="9" fill="#6b6b6b">time →</text><text x="4" y="14" font-family="Inter, sans-serif" font-size="9" fill="#6b6b6b">value</text></svg>'''
preset = lambda name, path, on=False: (f'<button aria-pressed="{str(on).lower()}" style="display: flex; flex-direction: column; align-items: center; gap: 3px; padding: 4px 0; border-radius: 4px; {"background: rgba(47,128,237,0.18); box-shadow: inset 0 0 0 1px #2f80ed;" if on else "background: #262626;"}">'
                                       f'<svg width="34" height="18" viewBox="0 0 34 18"><path d="{path}" fill="none" stroke="{"#7fb0f0" if on else "#a8a8a8"}" stroke-width="1.5"></path></svg><span style="font-size: 10px; color: {"#e8e8e8" if on else "#a8a8a8"}">{name}</span></button>')
presets = ('<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 4px">'
           + preset('Smooth', 'M2 16 C 9 16, 9 2, 32 2', True) + preset('Snappy', 'M2 16 C 4 2, 12 2, 32 2') + preset('Gentle', 'M2 16 C 14 16, 20 2, 32 2')
           + preset('Linear', 'M2 16 L32 2') + preset('Spring', 'M2 16 C 8 -4, 14 6, 20 1 S 28 3, 32 2') + '</div>')
itab = lambda items, sel: '<div role="tablist" style="height: 26px; flex: none; display: flex; align-items: center; gap: 14px; padding: 0 12px; border-bottom: 1px solid #2c2c2c">' + ''.join(f'<span style="position: relative; height: 26px; display: flex; align-items: center; font-size: 11px; font-weight: 500; color: {"#e8e8e8" if i == sel else "#939393"}">{t}' + ('<span style="position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: #2f80ed"></span>' if i == sel else '') + '</span>' for i, t in enumerate(items)) + '</div>'
inspector = f'''<aside aria-label="Timeline inspector" style="width: {IW}px; flex: none; display: flex; flex-direction: column; border-left: 1px solid #2c2c2c; background: #1f1f1f">
{itab(['Easing', 'Keyframe', 'Sequence'], 0)}
<div style="flex: 1; padding: 10px 12px; display: flex; flex-direction: column; gap: 8px; overflow: hidden">
<div style="display: flex; align-items: center; gap: 6px; font-size: 11px"><span style="width: 8px; height: 8px; transform: rotate(45deg); border-radius: 1px; background: #2f80ed"></span><b style="font-weight: 600">2 keyframes</b><span style="color: #939393">· Opacity, Move Y at 0.68 s</span></div>
{curve}
{presets}
<div style="display: flex; align-items: center; gap: 6px"><code style="flex: 1; font-family: {MONO}; font-size: 10px; color: #939393">cubic-bezier(0.2, 0.8, 0.2, 1)</code><button style="height: 20px; padding: 0 6px; border-radius: 3px; background: #2a2a2a; font-size: 10px; color: #c8c8c8">Copy</button></div>
<button style="height: 24px; border-radius: 4px; background: #246bcb; color: #fff; font-size: 11px; font-weight: 500">Apply to 2 selected</button></div></aside>'''

# ---------------- drawer frame ----------------
tab = lambda t, on=False: f'<button role="tab" aria-selected="{str(on).lower()}" style="position: relative; height: 32px; display: flex; align-items: center; gap: 6px; font-weight: 500; color: {"#e8e8e8" if on else "#a8a8a8"}">{t}' + ('<span style="position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: #2f80ed"></span>' if on else '') + '</button>'
tb = lambda ic, l, on=False, big=False: f'<button aria-label="{l}" aria-pressed="{str(on).lower()}" style="width: {28 if big else 24}px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; {"background: #333333; color: #e8e8e8;" if on else "color: #a8a8a8;"}">{icon(ic, 13 if big else 12, "currentColor", 1.75)}</button>'
chipb = lambda t: f'<button style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 8px; border-radius: 4px; background: #262626; font-size: 11px; color: #c8c8c8; white-space: nowrap">{t}{icon("chev-down", 9, "#939393", 1.75)}</button>'
zoom = f'<span style="display: flex; align-items: center; gap: 6px; font-size: 10px; color: #939393">{icon("minus", 10)}<span style="position: relative; width: 60px; height: 3px; border-radius: 2px; background: #3a3a3a"><span style="position: absolute; left: 0; width: 26px; height: 3px; border-radius: 2px; background: #8a8a8a"></span><span style="position: absolute; left: 22px; top: -4px; width: 10px; height: 10px; border-radius: 5px; background: #e8e8e8"></span></span>{icon("plus", 10)}</span>'
hdr_bar = f'''<div role="tablist" aria-label="Bottom drawer" style="height: 34px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 6px 0 12px; border-bottom: 1px solid #303030">
{tab(icon('code', 13) + 'Code')}{tab(icon('play', 11) + 'Timeline', True)}
<span style="width: 1px; height: 14px; background: #333333"></span>
<div style="display: flex; align-items: center; gap: 1px">{tb('tostart', 'Back to start')}{tb('prevkey', 'Previous keyframe')}{tb('pause', 'Pause', True, True)}{tb('nextkey', 'Next keyframe')}{tb('loop', 'Loop', True)}</div>
<label style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 8px; border-radius: 4px; background: #262626; font-size: 11px; font-variant-numeric: tabular-nums"><b style="font-weight: 600; color: #e8e8e8">{T:.2f}</b><span style="color: #939393">/ 1.40 s</span></label>
{chipb('1×')}{chipb('Starts: On scroll into view')}
<span style="flex: 1"></span>
{tb('magnet', 'Snap to keyframes and markers', True)}{tb('marker', 'Add marker')}{zoom}
<button aria-label="Maximise" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon('max', 12, 'currentColor', 1.75)}</button>
<button aria-label="Collapse drawer" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon('chev-down', 13, 'currentColor', 1.75)}</button></div>'''
strip = f'''<div style="height: 24px; flex: none; display: flex; align-items: center; gap: 14px; padding: 0 12px; border-top: 1px solid #2c2c2c; font-size: 11px; color: #939393">
<span style="display: flex; align-items: center; gap: 6px">Less motion:<b style="font-weight: 500; color: #c8c8c8">fade only, no movement</b>{icon('chev-down', 9, '#939393', 1.75)}</span>
<span>· 5 elements · 14 keyframes · 1.40 s</span><span style="flex: 1"></span>
<span>Space play · K keyframe · ← → 1 frame · Shift ← → 0.1 s</span>
<button style="color: #c8c8c8">Copy as CSS @keyframes</button></div>'''
drawer = f'''<!-- BOTTOM DRAWER: Timeline (open, h420) -->
<div style="position: relative; height: 420px; flex: none; box-sizing: border-box; display: flex; flex-direction: column; background: #1f1f1f; border-top: 1px solid #303030">
<span aria-hidden="true" title="Drag to resize" style="position: absolute; left: calc(50% - 16px); top: -3px; width: 32px; height: 4px; border-radius: 2px; background: #454545"></span>
{hdr_bar}
<div style="flex: 1; min-height: 0; display: flex">{track_list}{timeline}{inspector}</div>
{strip}</div>'''
a = S.s.index('<!-- BOTTOM DRAWER (collapsed, h28) -->'); b = S.s.index('</div>\n</div>', a)
S.s = S.s[:a] + drawer + S.s[b + len('</div>'):]

# ---------------- properties: Animation (summary; editing happens in the Timeline) ----------------
anim = (f('<span style="font-size: 11px; color: #939393">In sequence</span><span style="flex: 1">Hero entrance</span><span style="font-size: 10px; color: #939393">2 of 5</span>' + icon('chev-down', 10, '#939393', 1.5))
        + pair(f('<span style="font-size: 11px; color: #939393">Starts at</span><span style="flex: 1; text-align: right">0.08</span><span style="font-size: 10px; color: #939393">s</span>'), f('<span style="font-size: 11px; color: #939393">Length</span><span style="flex: 1; text-align: right">0.6</span><span style="font-size: 10px; color: #939393">s</span>'))
        + f('<span style="font-size: 11px; color: #939393">Animates</span><span style="flex: 1">Opacity · Move Y · Blur</span>')
        + '<div style="font-size: 10px; line-height: 14px; color: #939393">Keyframes, easing and the sequence are edited in the Timeline below</div>')
S.props(panel(header('t-heading', 'Hero title', 'Heading 1', 'h1') + group('Animation', anim)
              + group('Typography', f('<span style="flex: 1; font-family: Georgia, serif">Fraunces</span>') + pair(f('<span style="flex: 1">Semibold</span>'), f('<span style="flex: 1; text-align: right">64</span><span style="font-size: 10px; color: #939393">px</span>')))
              + more([mp('Size', '560 Fixed'), mp('Placement', 'In flow'), mp('Spacing', '0'), mp('Transition'), mp('Visibility', 'All sizes')])))
S.status(['Page', 'Section · Hero', 'Box · Hero grid', 'Box · Hero text', 'Heading · Hero title'],
         'Timeline · the canvas shows the frame at the playhead · drag the playhead to scrub · Shift+drag clips keeps the stagger', 'x 612 &#160;y 288')
S.save('D28-Timeline.dc.html')
print('ok')
