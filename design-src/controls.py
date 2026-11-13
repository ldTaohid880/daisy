import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

HOVER_FILL = '#2c72d6'
PRESSED_FILL = '#1f5fb5'
for c in (HOVER_FILL, PRESSED_FILL, '#246bcb'):
    assert contrast('#ffffff', c) >= 4.5, (c, contrast('#ffffff', c))


def row(cid, name, anatomy, cells):
    cs = ''.join(f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 10px; min-width: 96px">
<div style="min-height: 56px; display: flex; align-items: center; justify-content: center">{inner}</div>
<span style="font-size: 10px; line-height: 14px; color: #939393; text-align: center">{lab}</span></div>''' for lab, inner in cells)
    return f'''<div style="display: grid; grid-template-columns: 260px 1fr; gap: 32px; padding: 20px 0; border-bottom: 1px solid #262626; align-items: center">
<div><div style="font-family: {MONO}; font-size: 11px; color: #939393">{cid}</div><div style="font-weight: 600; margin: 2px 0 4px">{name}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{anatomy}</div></div>
<div style="display: flex; flex-wrap: wrap; gap: 24px 28px; align-items: flex-start">{cs}</div>
</div>'''


# ---------- buttons ----------
def btn(kind, state, label='Export', h=24):
    base = f'height: {h}px; display: inline-flex; align-items: center; gap: 6px; padding: 0 12px; border-radius: 4px; font-weight: 500; white-space: nowrap;'
    if kind == 'primary':
        bg = {'rest': '#246bcb', 'hover': HOVER_FILL, 'pressed': PRESSED_FILL, 'focus': '#246bcb', 'disabled': '#2a2a2a'}[state]
        col = '#4f4f4f' if state == 'disabled' else '#ffffff'
        extra = f'background: {bg}; color: {col};'
    elif kind == 'secondary':
        bg = {'rest': '#2a2a2a', 'hover': '#323232', 'pressed': '#3a3a3a', 'focus': '#2a2a2a', 'disabled': '#232323'}[state]
        col = '#4f4f4f' if state == 'disabled' else '#e8e8e8'
        ring = 'inset 0 0 0 1px #454545' if state != 'disabled' else 'inset 0 0 0 1px #2e2e2e'
        extra = f'background: {bg}; color: {col}; box-shadow: {ring};'
    else:
        bg = {'rest': 'transparent', 'hover': '#323232', 'pressed': '#3a3a3a', 'focus': 'transparent', 'disabled': 'transparent'}[state]
        col = '#4f4f4f' if state == 'disabled' else ('#a8a8a8' if state == 'rest' else '#e8e8e8')
        extra = f'background: {bg}; color: {col};'
    if state == 'focus':
        extra = extra.replace('box-shadow: inset 0 0 0 1px #454545;', '') + FOCUS + ';'
    dis = ' disabled' if state == 'disabled' else ''
    return f'<button{dis} style="{base} {extra}">{label}</button>'


def btn_row(kind, label):
    return [(s, btn(kind, s, label)) for s in ('rest', 'hover', 'pressed', 'focus', 'disabled')]


def ibtn(state, ic='eye', size=24):
    st = {'rest': 'color: #a8a8a8;', 'hover': 'background: #323232; color: #e8e8e8;', 'pressed': 'background: #3a3a3a; color: #e8e8e8;',
          'active': 'background: rgba(47,128,237,0.18); color: #2f80ed;', 'focus': 'color: #e8e8e8; ' + FOCUS + ';',
          'disabled': 'color: #a8a8a8; opacity: 0.35;'}[state]
    return f'<button aria-label="{ic}" style="width: {size}px; height: {size}px; display: flex; align-items: center; justify-content: center; border-radius: 4px; {st}">{icon(ic)}</button>'


# ---------- fields ----------
def field(inner, state='rest', w=140, extra=''):
    ring = {'rest': '', 'hover': 'box-shadow: inset 0 0 0 1px #454545;', 'focus': 'box-shadow: inset 0 0 0 1px #2f80ed, 0 0 0 1px #1f1f1f, 0 0 0 3px rgba(47,128,237,0.45);',
            'invalid': 'box-shadow: inset 0 0 0 1px #f85149;', 'disabled': 'opacity: 0.5;', 'readonly': 'background: transparent; box-shadow: inset 0 0 0 1px #303030;'}.get(state, '')
    return f'<span style="width: {w}px; height: 24px; box-sizing: border-box; display: flex; align-items: center; gap: 6px; padding: 0 6px; background: #2a2a2a; border-radius: 2px; {ring} {extra}">{inner}</span>'


caret = '<span style="width: 1px; height: 14px; background: #e8e8e8; margin-left: -4px"></span>'
tf = [
    ('rest', field('<span>Hero title</span>')),
    ('hover', field('<span>Hero title</span>', 'hover')),
    ('focus', field(f'<span>Hero title</span>{caret}', 'focus')),
    ('filled', field('<span style="flex: 1; min-width: 0; overflow: hidden; white-space: nowrap; text-overflow: ellipsis">Hand-thrown ceramics for everyday tables</span>')),
    ('placeholder', field('<span style="color: #939393">Name this element</span>')),
    ('invalid', '<span style="display: flex; flex-direction: column; gap: 4px">' + field('<span>12qx</span>', 'invalid') + '<span style="font-size: 11px; color: #f85149">Not a valid width</span></span>'),
    ('disabled', field('<span style="color: #4f4f4f">Hero title</span>', 'disabled')),
    ('read-only', field(f'<span style="flex: 1; color: #a8a8a8">index.html</span><span style="color: #939393">{icon("lock", 12)}</span>', 'readonly')),
]


def lenf(state):
    lab_col = '#2f80ed' if state == 'scrubbing' else '#939393'
    if state == 'custom':
        inner = f'<span style="font-size: 11px; color: #939393">W</span><span style="flex: 1; min-width: 0; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; font-family: {MONO}; font-size: 11px">clamp(320px, 90vw…</span><span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 8px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">custom</span>'
    elif state == 'mixed':
        inner = '<span style="font-size: 11px; color: #939393">W</span><span style="flex: 1; font-style: italic; color: #939393">Mixed</span>'
    else:
        inner = f'<span style="width: 5px; height: 5px; border-radius: 3px; background: #2f80ed"></span><span style="font-size: 11px; color: {lab_col}">W</span><span style="flex: 1">560</span><span style="font-size: 10px; color: #939393">px</span>'
        if state == 'scrubbing':
            inner += f'<span style="position: absolute; left: 18px; top: 26px; color: #e8e8e8">{icon("swap", 12)}</span>'
    st = {'rest': 'rest', 'hover': 'hover', 'focus': 'focus', 'scrubbing': 'hover', 'custom': 'rest', 'mixed': 'rest', 'disabled': 'disabled'}[state]
    return f'<span style="position: relative">{field(inner, st, 150)}</span>'


lf = [(s, lenf(s)) for s in ('rest', 'hover', 'focus', 'scrubbing', 'custom', 'mixed', 'disabled')]
lf.append(('size-mode tag', field('<span style="font-size: 11px; color: #939393">W</span><span style="flex: 1">560</span><span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">Fixed</span>', 'rest', 150)))


def colf(state):
    sw = '<span style="width: 14px; height: 14px; box-sizing: border-box; border-radius: 2px; background: #b5532d; flex: none"></span>'
    if state == 'mixed':
        inner = '<span style="width: 14px; height: 14px; box-sizing: border-box; border-radius: 2px; background: conic-gradient(#b5532d 0 50%, #5f6b4e 0); flex: none"></span><span style="flex: 1; font-style: italic; color: #939393">Mixed</span>'
    elif state == 'from swatch':
        inner = sw + '<span style="flex: 1">brand</span><span style="color: #939393">100%</span>'
    else:
        inner = sw + f'<span style="flex: 1; font-family: {MONO}; font-size: 11px">B5532D</span><span style="color: #939393">100%</span>'
    return field(inner, {'rest': 'rest', 'hover': 'hover', 'focus': 'focus'}.get(state, 'rest'), 150)


cf = [(s, colf(s)) for s in ('rest', 'hover', 'focus', 'mixed', 'from swatch')]


def sel(state):
    chev = icon('chev-up' if state == 'open' else 'chev-down', 10, '#939393', 1.75)
    txt = '<span style="flex: 1; font-style: italic; color: #939393">Mixed</span>' if state == 'mixed' else f'<span style="flex: 1; {"color: #4f4f4f;" if state == "disabled" else ""}">Heading 1</span>'
    f = field(txt + chev, {'rest': 'rest', 'hover': 'hover', 'open': 'focus', 'focus': 'focus', 'disabled': 'disabled', 'mixed': 'rest'}[state], 140)
    if state == 'open':
        menu = '<span style="position: absolute; left: 0; top: 28px; width: 140px; padding: 4px; box-sizing: border-box; background: #262626; border: 1px solid #454545; border-radius: 4px; box-shadow: 0 8px 24px rgba(0,0,0,0.45); z-index: 2">' + ''.join(
            f'<span style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px; border-radius: 3px; {"background: #323232;" if i == 0 else ""}"><span style="width: 12px; color: #e8e8e8">{icon("check", 12) if i == 0 else ""}</span>{t}</span>' for i, t in enumerate(['Heading 1', 'Heading 2', 'Paragraph'])) + '</span>'
        return f'<span style="position: relative; display: block; height: 108px">{f}{menu}</span>'
    return f


sf = [(s, sel(s)) for s in ('rest', 'hover', 'open', 'focus', 'disabled', 'mixed')]


def seg(sel_i=0, hover_i=None, dis_i=None, focus=False, labels=('Show', 'Cut off', 'Scroll')):
    out = ''
    for i, l in enumerate(labels):
        st = 'color: #939393;'
        if i == sel_i:
            st = 'background: #3a3a3a; color: #e8e8e8; font-weight: 500;'
        elif i == hover_i:
            st = 'background: #2c2c2c; color: #e8e8e8;'
        elif i == dis_i:
            st = 'color: #4f4f4f;'
        out += f'<button style="height: 20px; padding: 0 10px; border-radius: 3px; {st}">{l}</button>'
    f = FOCUS + ';' if focus else ''
    return f'<span role="group" style="height: 24px; display: inline-flex; gap: 2px; padding: 2px; box-sizing: border-box; background: #262626; border-radius: 4px; {f}">{out}</span>'


segs = [('selected + rest', seg()), ('segment hover', seg(0, 1)), ('segment disabled', seg(0, None, 2)), ('whole: focus', seg(0, None, None, True)),
        ('capsule (options bar)', '<span style="height: 28px; display: inline-flex; align-items: center; gap: 2px; padding: 2px; box-sizing: border-box; background: #232323; border-radius: 6px">'
         f'<button style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; background: #333333; font-weight: 500">{icon("flow", 12)}In flow</button>'
         f'<button style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; color: #939393">{icon("free", 12)}Free</button></span>')]


def tog(state):
    on = state in ('on', 'on hover', 'focus')
    track = '#246bcb' if on else '#454545'
    if state == 'on hover':
        track = HOVER_FILL
    if state == 'off hover':
        track = '#555555'
    thumb = '#ffffff' if on else '#a8a8a8'
    pos = 'right: 2px' if on else 'left: 2px'
    f = FOCUS + ';' if state == 'focus' else ''
    o = 'opacity: 0.35;' if state == 'disabled' else ''
    return f'<button role="switch" aria-checked="{str(on).lower()}" style="position: relative; width: 28px; height: 16px; border-radius: 8px; background: {track}; {f} {o}"><span style="position: absolute; {pos}; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {thumb}"></span></button>'


tg = [(s, tog(s)) for s in ('off', 'on', 'off hover', 'on hover', 'focus', 'disabled')]


def chk(state):
    box = 'width: 14px; height: 14px; box-sizing: border-box; border-radius: 3px; display: flex; align-items: center; justify-content: center;'
    if state in ('on', 'focus'):
        s = box + 'background: #246bcb; color: #fff;'
        inner = icon('check', 12, '#ffffff', 2)
    elif state == 'mixed':
        s = box + 'background: #246bcb;'
        inner = '<span style="width: 8px; height: 2px; border-radius: 1px; background: #fff"></span>'
    elif state == 'disabled':
        s = box + 'box-shadow: inset 0 0 0 1px #4f4f4f;'
        inner = ''
    else:
        s = box + 'box-shadow: inset 0 0 0 1px #8a8a8a;'
        inner = ''
    if state == 'focus':
        s += FOCUS + ';'
    lab_col = '#4f4f4f' if state == 'disabled' else '#e8e8e8'
    return f'<label style="display: flex; align-items: center; gap: 8px"><span style="{s}">{inner}</span><span style="color: {lab_col}">Required</span></label>'


ck = [(s, chk(s)) for s in ('off', 'on', 'mixed', 'focus', 'disabled')]


def sld(state):
    pct = 40
    thumb = 12
    ring = ''
    pill = ''
    fill = '#2f80ed'
    if state == 'hover':
        ring = 'box-shadow: 0 0 0 4px rgba(232,232,232,0.12);'
    if state == 'dragging':
        thumb = 14
        ring = 'box-shadow: 0 0 0 5px rgba(47,128,237,0.25);'
        pill = f'<span style="position: absolute; left: calc({pct}% - 14px); top: -24px; height: 18px; padding: 0 6px; display: flex; align-items: center; border-radius: 3px; background: #246bcb; color: #fff; font-size: 10px">40%</span>'
    if state == 'focus':
        ring = FOCUS + ';'
    if state == 'disabled':
        fill = '#4f4f4f'
    o = 'opacity: 0.5;' if state == 'disabled' else ''
    return f'''<span style="display: flex; align-items: center; gap: 10px; {o}"><span style="position: relative; width: 120px; height: 16px">
<span style="position: absolute; left: 0; right: 0; top: 7px; height: 2px; border-radius: 1px; background: #454545"></span>
<span style="position: absolute; left: 0; width: {pct}%; top: 7px; height: 2px; border-radius: 1px; background: {fill}"></span>
<span style="position: absolute; left: calc({pct}% - {thumb // 2}px); top: {8 - thumb // 2}px; width: {thumb}px; height: {thumb}px; border-radius: 50%; background: #e8e8e8; {ring}"></span>{pill}</span>
{field('<span style="flex: 1">40</span><span style="font-size: 10px; color: #939393">%</span>', 'rest', 52)}</span>'''


sl = [(s, sld(s)) for s in ('rest', 'hover', 'dragging', 'focus', 'disabled')]


def agrid(active=4, hover=None, size=60, disabled=False):
    cells = ''
    for i in range(9):
        if i == active:
            bars = ''.join(f'<span style="width: {int(size*0.05)+2}px; height: {h}px; border-radius: 1px; background: #2f80ed"></span>' for h in (int(size*0.18), int(size*0.27), int(size*0.13)))
            cells += f'<span style="display: flex; align-items: center; justify-content: center; gap: 2px">{bars}</span>'
        else:
            col = '#e8e8e8' if i == hover else '#6b6b6b'
            sz = 5 if i == hover else 3
            cells += f'<span style="display: flex; align-items: center; justify-content: center"><span style="width: {sz}px; height: {sz}px; border-radius: 50%; background: {col}"></span></span>'
    o = 'opacity: 0.35;' if disabled else ''
    return f'<span style="width: {size}px; height: {size}px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); padding: 4px; box-sizing: border-box; background: #2a2a2a; border-radius: 4px; {o}">{cells}</span>'


ag = [('rest · centre active', agrid()), ('hover dot', agrid(4, 2)), ('active top-left', agrid(0)), ('disabled', agrid(4, None, 60, True)), ('mini · 36 (options bar)', agrid(4, None, 36)), ('focus', agrid(4).replace('border-radius: 4px; ">', 'border-radius: 4px; ' + FOCUS + ';">', 1))]


def boxsides(state):
    out_hi = 'rgba(240,136,62,0.10)'
    top_hi = ''
    if state == 'hover a side':
        top_hi = '<span style="position: absolute; left: 0; right: 0; top: 0; height: 18px; background: rgba(240,136,62,0.28); border-radius: 4px 4px 0 0"></span>'
    vals = {'rest': ('0', '0', '0', '0', '72', '64', '96', '64'), 'hover a side': ('0', '0', '0', '0', '72', '64', '96', '64'),
            'editing a side': ('0', '0', '0', '0', '72', '64', '96', '64'), 'linked': ('24', '24', '24', '24', '16', '16', '16', '16')}[state]
    ot, orr, ob, ol, it, ir, ib, il = vals
    edit = ''
    if state == 'editing a side':
        edit = '<span style="position: absolute; top: 20px; left: calc(50% - 22px); width: 44px; height: 18px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; background: #2a2a2a; border-radius: 2px; box-shadow: inset 0 0 0 1px #2f80ed; font-size: 11px">72</span>'
        it = ''
    link = ''
    if state == 'linked':
        link = f'<span style="position: absolute; right: 4px; top: 3px; color: #2f80ed">{icon("link", 12)}</span>'
    num = 'position: absolute; font-size: 11px; color: #a8a8a8'
    return f'''<span style="position: relative; width: 220px; height: 112px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; background: {out_hi}; box-shadow: inset 0 0 0 1px rgba(240,136,62,0.45); border-radius: 4px">{top_hi}{link}
<span style="position: absolute; left: 6px; top: 3px; font-size: 10px; color: #939393">Outside</span>
<span style="{num}; top: 3px; left: 0; right: 0; text-align: center">{ot}</span><span style="{num}; bottom: 3px; left: 0; right: 0; text-align: center">{ob}</span>
<span style="{num}; left: 10px; top: 48px">{ol}</span><span style="{num}; right: 10px; top: 48px">{orr}</span>
<span style="position: relative; width: 150px; height: 64px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; background: rgba(63,185,80,0.10); box-shadow: inset 0 0 0 1px rgba(63,185,80,0.45); border-radius: 3px">
<span style="position: absolute; left: 5px; top: 2px; font-size: 10px; color: #939393">Inside</span>
<span style="{num}; top: 2px; left: 0; right: 0; text-align: center">{it}</span><span style="{num}; bottom: 2px; left: 0; right: 0; text-align: center">{ib}</span>
<span style="{num}; left: 6px; top: 24px">{il}</span><span style="{num}; right: 6px; top: 24px">{ir}</span>
<span style="height: 18px; padding: 0 6px; display: flex; align-items: center; border-radius: 2px; background: #3a3a3a; font-size: 10px; color: #a8a8a8">Hero</span>
</span>{edit}</span>'''


bs = [(s, boxsides(s)) for s in ('rest', 'hover a side', 'editing a side', 'linked')] + [('focus · keyboard on a side', boxsides('rest').replace('<span style="position: absolute; font-size: 11px; color: #a8a8a8; top: 3px; left: 0; right: 0; text-align: center">0</span>', '<span style="position: absolute; top: 2px; left: calc(50% - 10px); width: 20px; height: 14px; display: flex; align-items: center; justify-content: center; font-size: 11px; border-radius: 2px; ' + FOCUS + '">0</span>', 1))]


def pin(on=(), hover=None):
    def side(pos, key):
        col = '#2f80ed' if key in on else ('#e8e8e8' if key == hover else '#6b6b6b')
        w = 2 if key in on else 1.5
        return f'<span style="position: absolute; {pos}; background: {col}; border-radius: 1px"></span>'.replace('background', f'background', 1) if False else f'<span style="position: absolute; {pos.format(w=w)}; background: {col}; border-radius: 1px"></span>'
    c_col = '#2f80ed' if 'c' in on else '#6b6b6b'
    return f'''<span style="position: relative; width: 40px; height: 40px; box-sizing: border-box; background: #2a2a2a; border-radius: 4px">
<span style="position: absolute; left: 12px; top: 12px; width: 16px; height: 16px; box-sizing: border-box; border: 1px dashed #6b6b6b"></span>
{side('left: 15px; top: 3px; width: 10px; height: {w}px', 't')}{side('left: 15px; bottom: 3px; width: 10px; height: {w}px', 'b')}
{side('top: 15px; left: 3px; height: 10px; width: {w}px', 'l')}{side('top: 15px; right: 3px; height: 10px; width: {w}px', 'r')}
<span style="position: absolute; left: 18px; top: 18px; width: 4px; height: 4px; border-radius: 2px; background: {c_col}"></span></span>'''


pw = [('all off', pin()), ('Right + Top on', pin(('r', 't'))), ('hover a side', pin(('r', 't'), 'l')), ('centre on', pin(('c',))), ('focus', pin(('r', 't')).replace('border-radius: 4px">', 'border-radius: 4px; ' + FOCUS + '">', 1))]


def rtrig(state):
    ring = 'box-shadow: inset 0 0 0 1px #2f80ed;' if state == 'open' else ''
    bg = '#333333' if state == 'open' else '#232323'
    val = {'rest': ('radius', '0'), 'open': ('radius', '12'), 'pairs': ('radius', '16 · 0'), 'mixed': ('corners', '<i style="color: #939393">Mixed</i>')}[state]
    btnbg = 'background: #3f3f3f; color: #e8e8e8;' if state == 'open' else 'color: #a8a8a8;'
    return f'''<span style="height: 28px; display: inline-flex; align-items: center; gap: 2px; padding: 2px; box-sizing: border-box; background: {bg}; border-radius: 6px; {ring}">
<span style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px">{icon(val[0], 14, '#939393')}<span>{val[1]}</span></span>
<span style="width: 1px; height: 14px; background: #333333"></span>
<button aria-label="Corner options" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; {btnbg}">{icon('corners', 14)}</button></span>'''


rt = [(s, rtrig(s)) for s in ('rest', 'open', 'pairs', 'mixed')] + [('focus', rtrig('rest').replace('border-radius: 6px; ">', f'border-radius: 6px; {FOCUS}">', 1))]

body = sheet_header('D-00c', 'Controls', 'Buttons, fields and inputs C-01 to C-15, plus the corner roundness trigger C-33. Every interactive control shows a visible 2 px focus ring.')
rows = ''
rows += row('C-01', 'Primary button', f'24 h in panels, 28 in the top bar · accent-fill · white 12 medium · radius 4 (6 in top bar). Hover {HOVER_FILL}, pressed {PRESSED_FILL}: both ≥ 4.5:1 with white', btn_row('primary', 'Export'))
rows += row('C-02', 'Secondary button', 'bg-control + 1 px inset line-strong ring', btn_row('secondary', 'Open…'))
rows += row('C-03', 'Ghost / text button', 'No fill until hover · text-secondary at rest', btn_row('ghost', 'Copy CSS'))
rows += row('C-04', 'Icon button', '24 square (28 in top bar) · 16 icon · radius 4', [(s, ibtn(s)) for s in ('rest', 'hover', 'pressed', 'active', 'focus', 'disabled')] + [('28 · top bar', ibtn('rest', 'undo', 28))])
rows += row('C-05', 'Text field', '24 h · bg-control · radius 2 · no border at rest · 6 px padding', tf)
rows += row('C-06', 'Length / number field', 'Inside label (scrub ↔), value, unit menu · accepts any CSS value', lf)
rows += row('C-07', 'Colour field', '14 swatch + hex + opacity · shows the swatch name when linked', cf)
rows += row('C-08', 'Select / dropdown', 'Field + chevron · opens a C-16 menu', sf)
rows += row('C-09', 'Segmented control', '24 h in panels, 28 capsule in the options bar · selected segment bg-control-active', segs)
rows += row('C-10', 'Toggle switch', '28 × 16 · on = accent-fill', tg)
rows += row('C-11', 'Checkbox', '14 square · radius 3 · off ring #8a8a8a (3:1 non-text)', ck)
rows += row('C-12', 'Slider', '2 px track, 12 thumb, value field beside', sl)
rows += row('C-13', 'Alignment grid', '3 × 3 in 60 × 60 (36 mini) · active cell shows 3 bars for child arrangement', ag)
rows += row('C-14', 'Box-sides diagram', 'Outer ring Outside (orange), inner Inside (green) · 4 numbers each · link toggle', bs)
rows += row('C-15', 'Pin widget', '40 × 40 · 4 side toggles + centre', pw)
rows += row('C-33', 'Corner roundness trigger', 'Value + corners button · opens the popover on D-35', rt)
body += rows

H = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
open('/home/claude/daisy/project/DS-Controls.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-00c Controls', 1920, H, body))
