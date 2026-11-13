"""New project setup flow (Visual Studio-style steps), 1200 x 760 window."""
import sys, colorsys
sys.path.insert(0, '/home/claude/ds')
from lib import *

P['palette'] = ('stroke', 'M8 1.5a6.5 6.5 0 1 0 0 13c1 0 1.5-.6 1.5-1.4 0-1.2-1-1.3-1-2.3 0-.8.6-1.3 1.5-1.3h1.6a2.9 2.9 0 0 0 2.9-2.9C14.5 4 11.6 1.5 8 1.5z')
P['type'] = ('stroke', 'M3 4V3h10v1M8 3v10M6 13h4')
P['grid'] = ('stroke', 'M2.5 2.5h11v11h-11zM6.2 2.5v11M9.8 2.5v11')
P['layers2'] = ('stroke', 'M8 2l6 3-6 3-6-3zM2 8l6 3 6-3M2 11l6 3 6-3')
P['review'] = ('stroke', 'M3 2.5h10v11H3zM5.5 6h5M5.5 8.5h5M5.5 11h3')
P['import'] = ('stroke', 'M8 2v8M5 7l3 3 3-3M3 12.5h10')
P['skip'] = ('stroke', 'M3 3.5l6 4.5-6 4.5zM11.5 3.5v9')
P['sparkle'] = ('stroke', 'M8 2v3M8 11v3M2 8h3M11 8h3M4 4l1.8 1.8M10.2 10.2L12 12M12 4l-1.8 1.8M5.8 10.2L4 12')
MONO_ = "font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 11px"

# ── the example: Mossbank Tea ──
T = dict(name='Mossbank Tea', primary='#4f6b3a', secondary='#c08a3e', head="'Fraunces', serif", head_name='Fraunces', body='Inter', radius=8, shadow=True)

def scale(hexc, n=11):
    r, g, b = (int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5))
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    out = []
    for i, L in enumerate([0.97, 0.93, 0.86, 0.76, 0.64, 0.52, 0.42, 0.34, 0.26, 0.19, 0.13][:n]):
        ss = s * (0.55 + 0.45 * (1 - abs(L - 0.5) * 1.6))
        rr, gg, bb = colorsys.hls_to_rgb(h, L, max(0, min(1, ss)))
        out.append('#%02x%02x%02x' % (round(rr * 255), round(gg * 255), round(bb * 255)))
    return out
STEPS = ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900', '950']
NEUTRAL = scale('#6f6a60')

# ── small controls ──
lbl = lambda t, extra='': f'<span style="font-size: 11px; color: #a8a8a8; {extra}">{t}</span>'
def fld(inner, focus=False, w=None):
    return f'<span style="{f"width: {w}px;" if w else ""} height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 8px; box-sizing: border-box; background: #2a2a2a; border-radius: 2px; {"box-shadow: inset 0 0 0 1px #2f80ed;" if focus else ""}">{inner}</span>'
def field(name, inner, focus=False, hint=''):
    return f'<label style="display: flex; flex-direction: column; gap: 6px; min-width: 0">{lbl(name)}{fld(inner, focus)}{f"<span style=\"font-size: 11px; line-height: 15px; color: #939393\">{hint}</span>" if hint else ""}</label>'
fieldr = lambda name, ctl: f'<div style="display: flex; flex-direction: column; gap: 6px; min-width: 0">{lbl(name)}{ctl}</div>'
dd = lambda v, sub='': f'<span style="flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{v}</span>{f"<span style=\"{MONO_}; color: #939393\">{sub}</span>" if sub else ""}' + icon('chev-down', 10, '#939393', 1.75)
num = lambda v, u='px': f'<span style="flex: 1">{v}</span><span style="font-size: 10px; color: #939393">{u}</span>'
sw = lambda c, s=14: f'<span style="width: {s}px; height: {s}px; flex: none; border-radius: 2px; background: {c}; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.1)"></span>'
def seg(items, sel, full=True):
    return (f'<div role="group" style="display: {"grid" if full else "inline-grid"}; grid-template-columns: repeat({len(items)}, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #1f1f1f; border-radius: 4px">'
            + ''.join(f'<button aria-pressed="{str(i == sel).lower()}" style="height: 24px; padding: 0 8px; white-space: nowrap; display: flex; align-items: center; justify-content: center; gap: 6px; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #939393;"}">{t}</button>' for i, t in enumerate(items)) + '</div>')
def switch(on): return f'<span role="switch" aria-checked="{str(on).lower()}" style="position: relative; width: 28px; height: 16px; flex: none; border-radius: 8px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {"#fff" if on else "#a8a8a8"}"></span></span>'
def check(on, t): return f'<span style="display: flex; align-items: center; gap: 8px"><span style="width: 14px; height: 14px; border-radius: 3px; display: flex; align-items: center; justify-content: center; {"background: #246bcb;" if on else "box-shadow: inset 0 0 0 1px #6b6b6b;"}">{icon("check", 10, "#fff", 2) if on else ""}</span>{t}</span>'
def h2(t, d=''): return f'<div style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 16px; line-height: 22px; font-weight: 600">{t}</span>{f"<span style=\"font-size: 12px; line-height: 18px; color: #a8a8a8\">{d}</span>" if d else ""}</div>'
def group(t, body, right=''): return f'<section style="display: flex; flex-direction: column; gap: 10px; padding-top: 14px; border-top: 1px solid #303030"><div style="display: flex; align-items: center; gap: 8px"><span style="font-weight: 600">{t}</span><span style="flex: 1"></span>{right}</div>{body}</section>'
def grid(cols, *cells, gap=10): return f'<div style="display: grid; grid-template-columns: {cols}; gap: {gap}px; align-items: end">' + ''.join(cells) + '</div>'
adv = lambda t='Advanced': f'<button style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 6px; border-radius: 3px; font-size: 11px; color: #a8a8a8">{icon("sliders", 11)}{t}</button>'

# ── rail ──
RAIL = [('Project', 'folder', 0), ('Design system', 'palette', 0), ('Colours', None, 1), ('Typography', None, 1), ('Spacing & layout', None, 1), ('Shape & depth', None, 1), ('Review', 'review', 0)]
def rail(cur, ds_on=True):
    out = ''
    for i, (t, ic, sub) in enumerate(RAIL):
        if sub and not ds_on: continue
        done, on = i < cur, i == cur
        mark = (icon('check', 11, '#3fb950', 2) if done else f'<span style="width: 6px; height: 6px; border-radius: 3px; {"background: #2f80ed;" if on else "box-shadow: inset 0 0 0 1.5px #6b6b6b;"}"></span>')
        out += (f'<div role="tab" aria-selected="{str(on).lower()}" style="height: {30 if not sub else 26}px; display: flex; align-items: center; gap: 10px; padding: 0 12px 0 {32 if sub else 12}px; border-radius: 4px; '
                f'{"background: rgba(47,128,237,0.18); color: #e8e8e8; font-weight: 500;" if on else ("color: #c8c8c8;" if done else "color: #a8a8a8;")} {"font-size: 12px;" if not sub else ""}">'
                f'<span style="width: 14px; display: flex; justify-content: center">{mark}</span><span style="flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{t}</span></div>')
    return f'''<nav aria-label="Setup steps" style="width: 220px; flex: none; padding: 16px 10px; box-sizing: border-box; display: flex; flex-direction: column; gap: 2px; background: #222222; border-right: 1px solid #303030">{out}
<span style="flex: 1"></span><div style="padding: 10px 12px; font-size: 11px; line-height: 16px; color: #939393">Every value can be changed later in Project › Design system.</div></nav>'''

# ── live preview (tokens applied to a sample) ──
def preview(t=T, focus=None, dark=False):
    P_ = scale(t['primary']); S_ = scale(t['secondary']); N = NEUTRAL
    bg, surf, ink, mut, line = (N[10], N[9], N[0], N[3], N[8]) if dark else ('#fbfaf7', '#ffffff', N[9], N[6], N[2])
    r = t['radius']; sh = '0 1px 2px rgba(0,0,0,0.06), 0 4px 12px rgba(0,0,0,0.08)' if t['shadow'] else 'none'
    ring = lambda k: 'outline: 1.5px solid #2f80ed; outline-offset: 3px;' if focus == k else ''
    return f'''<aside aria-label="Live preview" style="width: 320px; flex: none; padding: 16px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px; border-left: 1px solid #303030; background: #262626">
<div style="display: flex; align-items: center; gap: 8px"><span style="font-size: 10px; font-weight: 500; letter-spacing: 0.06em; color: #939393">LIVE PREVIEW</span><span style="flex: 1"></span>{seg(["Light", "Dark"], 1 if dark else 0, False)}</div>
<div style="flex: 1; padding: 16px; display: flex; flex-direction: column; gap: 12px; border-radius: 4px; background: {bg}; color: {ink}; overflow: hidden">
<span style="display: flex; justify-content: space-between; align-items: center"><span style="font: 600 13px/1 {t['head']}">{t['name']}</span><span style="display: flex; gap: 8px; font-size: 9px; color: {mut}"><span>Teas</span><span>Journal</span><span>Visit</span></span></span>
<span style="font-size: 8px; letter-spacing: 0.08em; color: {P_[7] if not dark else P_[3]}; {ring('text')}">SINGLE-ESTATE · SINCE 2019</span>
<span style="font: 600 24px/1.1 {t['head']}; {ring('text')}">Slow-grown tea from the hills</span>
<span style="font-size: 11px; line-height: 1.6; color: {mut}; {ring('text')}">Picked by hand, rolled in small batches and shipped the week it is made.</span>
<span style="display: flex; gap: 8px; {ring('space')}"><span style="height: 28px; display: flex; align-items: center; padding: 0 14px; border-radius: {r}px; background: {P_[6]}; color: #fff; font-size: 11px; font-weight: 500; {ring('colour')}">Shop teas</span>
<span style="height: 28px; display: flex; align-items: center; padding: 0 14px; border-radius: {r}px; box-shadow: inset 0 0 0 1px {line}; font-size: 11px">Our garden</span></span>
<span style="padding: 10px; display: flex; gap: 10px; border-radius: {r + 4}px; background: {surf}; box-shadow: {sh}{", inset 0 0 0 1px " + line if not t["shadow"] else ""}; {ring('shape')}">
<span style="width: 52px; height: 52px; flex: none; border-radius: {r}px; background: {S_[2] if not dark else S_[8]}"></span>
<span style="display: flex; flex-direction: column; gap: 4px; min-width: 0"><span style="font: 600 12px/1.2 {t['head']}">First flush</span><span style="font-size: 10px; color: {mut}">Darjeeling style · 50 g</span><span style="font-size: 11px; font-weight: 600; color: {P_[7] if not dark else P_[3]}">€14</span></span></span>
<span style="height: 28px; display: flex; align-items: center; padding: 0 10px; border-radius: {max(r - 2, 0)}px; background: {surf}; box-shadow: inset 0 0 0 1px {line}; font-size: 11px; color: {mut}">Your email</span>
<span style="display: flex; gap: 6px; flex-wrap: wrap; font-size: 9px; font-weight: 500">{''.join(f'<span style="padding: 3px 7px; border-radius: 999px; background: {b}; color: {c}">{x}</span>' for x, b, c in [('In stock', '#e3f3e6', '#1a7f37'), ('Low stock', '#fbf0d9', '#8a5a00'), ('Sold out', '#fbe3e3', '#b42318')])}</span>
</div></aside>'''

# ── window ──
def window(cur, content, prev=None, ds_on=True, next_label='Next', footer_note=''):
    total = 7 if ds_on else 3
    pos = cur + 1 if ds_on else {0: 1, 1: 2, 6: 3}[cur]
    return f'''<div role="dialog" aria-label="Create a new project" style="width: 1200px; height: 760px; display: flex; flex-direction: column; border-radius: 6px; overflow: hidden; background: #262626; border: 1px solid #454545; box-shadow: 0 8px 24px rgba(0,0,0,0.45); font-size: 12px; line-height: 16px; color: #e8e8e8">
<div style="height: 48px; flex: none; display: flex; align-items: center; gap: 10px; padding: 0 10px 0 16px; border-bottom: 1px solid #303030; background: #1f1f1f"><span style="width: 22px; height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 5px; background: #2a2a2a">{daisy(14)}</span><span style="font-size: 14px; font-weight: 600">Create a new project</span><span style="flex: 1"></span><button aria-label="Close" style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon("close", 12)}</button></div>
<div style="flex: 1; min-height: 0; display: flex">{rail(cur, ds_on)}
<div style="flex: 1; min-width: 0; padding: 20px 24px; box-sizing: border-box; display: flex; flex-direction: column; gap: 14px; overflow: hidden">{content}</div>
{prev or ''}</div>
<div style="height: 56px; flex: none; display: flex; align-items: center; gap: 8px; padding: 0 16px; border-top: 1px solid #303030; background: #1f1f1f">
<span style="font-size: 11px; color: #939393">Step {pos} of {total}</span><span style="margin-left: 12px; font-size: 11px; color: #939393">{footer_note}</span><span style="flex: 1"></span>
<button style="height: 28px; padding: 0 12px; border-radius: 4px; color: #a8a8a8">Cancel</button>
<button {"disabled" if cur == 0 else ""} style="height: 28px; padding: 0 12px; border-radius: 4px; box-shadow: inset 0 0 0 1px #454545; {"color: #4f4f4f;" if cur == 0 else ""}">Back</button>
{"" if cur == 6 or not ds_on else f'<button style="height: 28px; padding: 0 12px; border-radius: 4px; box-shadow: inset 0 0 0 1px #454545" title="Uses the suggested values for the steps left">Create with defaults</button>'}
<button style="height: 28px; padding: 0 16px; border-radius: 4px; background: #246bcb; color: #fff; font-weight: 500">{next_label}</button></div></div>'''

# ═════ steps ═════
def step_project():
    c = h2('Configure your new project', 'Name it and choose where its files live. Pages, assets and the design system are kept in this folder.')
    c += grid('minmax(0, 1fr)', field('Project name', '<span style="background: rgba(47,128,237,0.35)">Mossbank Tea</span>', True))
    c += grid('minmax(0, 1fr) auto', field('Location', f'<span style="{MONO_}">D:\\Sites</span>'), '<button style="height: 28px; padding: 0 12px; border-radius: 4px; box-shadow: inset 0 0 0 1px #454545">Browse…</button>')
    c += f'<div style="font-size: 11px; color: #939393">Files go to <span style="{MONO_}; color: #c8c8c8">D:\\Sites\\mossbank-tea\\</span></div>'
    c += group('First page', grid('minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr)', field('Page name', 'Home'), field('File', f'<span style="{MONO_}">index.html</span>'), field('Language', dd('English', 'en'))))
    c += group('Site', grid('minmax(0, 1fr) minmax(0, 1fr)', field('Address (optional)', f'<span style="{MONO_}; color: #939393">https://</span><span style="{MONO_}">mossbank.tea</span>'), field('Favicon', dd('Daisy mark in the brand colour'))))
    c += '<span style="flex: 1"></span><div style="font-size: 11px; line-height: 16px; color: #939393">The project starts with one page holding one empty section. Screen sizes are set in Spacing &amp; layout.</div>'
    return window(0, c)

def step_start(sel=0):
    opts = [('sparkle', 'Build a new design system', 'Set colours, type, spacing and shape in four short steps. Every value has a suggested default.', 'Recommended'),
            ('copy', 'Copy from a project', 'Start from the tokens of one of your projects. Copied once; the projects are not linked.', ''),
            ('import', 'Import tokens', 'W3C Design Tokens (.json), CSS variables (.css) or Figma variables (.json).', ''),
            ('skip', 'Skip for now', 'Pages use plain values. Set the design system up later from the Project panel.', '')]
    def opt(i, ic, t, d, tag):
        on = i == sel
        return (f'<div role="radio" aria-checked="{str(on).lower()}" style="display: flex; gap: 14px; padding: 14px 16px; border-radius: 6px; {"background: rgba(47,128,237,0.14); box-shadow: inset 0 0 0 1px #2f80ed;" if on else "background: #2a2a2a;"}">'
                f'<span style="width: 36px; height: 36px; flex: none; display: flex; align-items: center; justify-content: center; border-radius: 8px; background: {"#246bcb" if on else "#333333"}">{icon(ic, 17, "#fff" if on else "#c8c8c8")}</span>'
                f'<span style="flex: 1; display: flex; flex-direction: column; gap: 4px"><span style="display: flex; align-items: center; gap: 8px"><span style="font-size: 13px; font-weight: 600">{t}</span>{f"<span style=\"height: 16px; padding: 0 6px; border-radius: 3px; background: #333333; font-size: 10px; line-height: 16px; color: #a8a8a8\">{tag}</span>" if tag else ""}</span>'
                f'<span style="font-size: 12px; line-height: 18px; color: #a8a8a8">{d}</span></span></div>')
    c = h2('Design system', 'The colours, type, spacing and shape every page in Mossbank Tea will share, written to tokens.css.')
    c += '<div style="display: flex; flex-direction: column; gap: 8px">' + ''.join(opt(i, *o) for i, o in enumerate(opts)) + '</div>'
    if sel == 1:
        projs = [('Halden', ['#b5532d', '#9e4626', '#1d1a16', '#4a443c', '#f6f1ea', '#e7d9c7', '#5f6b4e'], '25 tokens · Fraunces, Inter · edited today', True),
                 ('North Pier Coffee', ['#0f3d3e', '#e2b04a', '#1c1c1c', '#f7f4ee', '#d9d2c3'], '19 tokens · Inter', False),
                 ('Studio Lumen', ['#111111', '#ff5a36', '#f2f2f2', '#8a8a8a'], '14 tokens · Space Grotesk', False)]
        chips = lambda cs: '<span style="display: flex; gap: 3px">' + ''.join(sw(c) for c in cs) + '</span>'
        c += '<div style="display: flex; flex-direction: column; gap: 2px; padding: 6px; border-radius: 6px; background: #1f1f1f">' + ''.join(
            f'<div style="height: 40px; display: flex; align-items: center; gap: 12px; padding: 0 10px; border-radius: 4px; {"background: rgba(47,128,237,0.18);" if on else ""}"><span style="width: 14px; height: 14px; box-sizing: border-box; border-radius: 7px; {"border: 4px solid #2f80ed;" if on else "border: 1.5px solid #6b6b6b;"}"></span><span style="flex: 1; display: flex; flex-direction: column"><span style="font-weight: 500">{n}</span><span style="font-size: 11px; color: #939393">{d}</span></span>{chips(cs)}</div>' for n, cs, d, on in projs) + '</div>'
        c += f'<div style="font-size: 11px; color: #939393">The detail steps open with Halden’s values, so you can change them before creating.</div>'
    elif sel == 3:
        c += f'<div style="display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 4px; background: #1f1f1f; font-size: 11px; line-height: 16px; color: #a8a8a8">{icon("info", 13, "#58a6ff", 1.25)}The project starts without tokens. Later, Project › Design system › Set up opens these same steps and can collect the colours and fonts the pages already use.</div>'
    elif sel == 2:
        c += f'''<div style="height: 96px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; border-radius: 6px; border: 1px dashed #454545; color: #a8a8a8">{icon("import", 18)}<span>Drop a tokens file here, or <button style="color: #a9c8f7">browse</button></span><span style="font-size: 11px; color: #939393">.json (W3C or Figma variables) · .css (custom properties)</span></div>'''
    else:
        c += f'<div style="display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 4px; background: #1f1f1f; font-size: 11px; line-height: 16px; color: #a8a8a8">{icon("info", 13, "#58a6ff", 1.25)}Not a template: no pages or content are added. Only tokens are made, from the values you choose.</div>'
    return window(1, c, None, sel != 3, next_label='Next' if sel != 3 else 'Next: Review')

def step_colours():
    P_ = scale(T['primary']); S_ = scale(T['secondary'])
    def role_row(name, base, sc, note, sel=False, lock=''):
        strip = '<span style="display: grid; grid-template-columns: repeat(11, minmax(0, 1fr)); height: 22px; border-radius: 3px; overflow: hidden; flex: 1; min-width: 0">' + ''.join(f'<span style="background: {c}; {"box-shadow: inset 0 0 0 1.5px #ffffff;" if i == 5 else ""}"></span>' for i, c in enumerate(sc)) + '</span>'
        return (f'<div style="display: grid; grid-template-columns: 82px 108px minmax(0, 1fr) 96px; align-items: center; gap: 10px; padding: 4px 6px; border-radius: 4px; {"background: rgba(47,128,237,0.14);" if sel else ""}">'
                f'<span style="font-weight: 500">{name}</span>{fld(sw(base) + f"<span style=\"{MONO_}\">{base[1:].upper()}</span>", sel)}{strip}<span style="font-size: 11px; color: #939393; text-align: right; white-space: nowrap">{note}</span></div>')
    roles = (role_row('Primary', T['primary'], P_, 'brand, buttons', True) + role_row('Secondary', T['secondary'], S_, 'highlights')
             + role_row('Neutral', '#6f6a60', NEUTRAL, 'text, surfaces')
             + role_row('Success', '#2f8a4c', scale('#2f8a4c'), 'auto') + role_row('Warning', '#b7791f', scale('#b7791f'), 'auto') + role_row('Danger', '#c4352b', scale('#c4352b'), 'auto'))
    steps_hdr = '<div style="display: grid; grid-template-columns: 82px 108px minmax(0, 1fr) 96px; gap: 10px; padding: 0 6px; font-size: 10px; color: #6b6b6b"><span></span><span></span><span style="display: grid; grid-template-columns: repeat(11, minmax(0, 1fr)); text-align: center">' + ''.join(f'<span>{s}</span>' for s in STEPS) + '</span><span></span></div>'
    gen = grid('minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr)', field('Scale method', dd('OKLCH · even lightness')), field('Neutral tint', dd('Warm · from Primary')), field('Contrast target', dd('AA · 4.5 text, 3 large')))
    roles_map = [('Background', 'neutral-50'), ('Surface', 'white'), ('Text', 'neutral-900'), ('Text muted', 'neutral-600'), ('Border', 'neutral-200'), ('Link', 'primary-700'), ('Button', 'primary-600'), ('Focus ring', 'primary-400')]
    mapping = '<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px">' + ''.join(f'<span style="height: 26px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 3px; background: #2a2a2a"><span style="flex: 1; font-size: 11px; color: #a8a8a8; white-space: nowrap">{a}</span><span style="{MONO_}; color: #e8e8e8; white-space: nowrap">{b}</span></span>' for a, b in roles_map) + '</div>'
    c = h2('Colours', 'Pick the base colours. Daisy makes an 11-step scale for each and maps them to roles the pages use.')
    c += f'<div style="display: flex; flex-direction: column; gap: 4px">{steps_hdr}{roles}<button style="align-self: flex-start; height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px; color: #a8a8a8">{icon("plus", 11, "currentColor", 1.75)}Add a colour role</button></div>'
    c += group('Generation', gen, adv())
    c += group('Roles · light theme', mapping, f'<span style="display: flex; align-items: center; gap: 8px; font-size: 11px; color: #a8a8a8">Also make a dark theme{switch(True)}</span>')
    return window(2, c, preview(focus='colour'), footer_note='6 roles · 66 colours · 16 role tokens')

def step_type():
    ratio = 1.25
    names = [('Display', 5, 1.05), ('H1', 4, 1.1), ('H2', 3, 1.15), ('H3', 2, 1.2), ('H4', 1, 1.3), ('Body', 0, 1.6), ('Small', -1, 1.5), ('Caption', -2, 1.4)]
    def trow(n, k, lh):
        mx = 16 * ratio ** k; mn = 15 * 1.2 ** k
        head = k >= 1
        return (f'<div style="height: {max(22, min(44, mx * 0.62 + 8)):.0f}px; display: grid; grid-template-columns: 64px minmax(0, 1fr) 120px 48px; align-items: center; gap: 10px; padding: 0 6px; border-bottom: 1px solid #2a2a2a">'
                f'<span style="font-size: 11px; color: #a8a8a8">{n}</span><span style="font-family: {T["head"] if head else "Inter, sans-serif"}; font-weight: {600 if head else 400}; font-size: {min(mx * 0.62, 36):.1f}px; line-height: 1.1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">Slow-grown tea</span>'
                f'<span style="{MONO_}; color: #c8c8c8; text-align: right">{mn:.0f} → {mx:.0f} px</span><span style="{MONO_}; color: #939393; text-align: right">{lh}</span></div>')
    fonts = grid('minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr)', field('Headings', dd('Fraunces', 'variable')), field('Body', dd('Inter', 'variable')), field('Code', dd('JetBrains Mono')))
    c = h2('Typography', 'Choose the fonts and a scale. Sizes grow smoothly between the smallest and largest screen.')
    c += fonts + '<div style="display: flex; gap: 14px; font-size: 11px; color: #939393"><span>Source: Google Fonts · self-hosted on export</span><span>Weights: 400, 500, 600</span><button style="color: #a9c8f7; font-size: 11px">Upload a font…</button></div>'
    c += group('Scale', grid('minmax(0, 1fr) minmax(0, 1.4fr) minmax(0, 1fr) minmax(0, 1fr)', field('Base size', num('16')), field('Ratio', dd('Major third', '1.25')), field('On small screens', dd('Minor third', '1.2')), field('Base on small', num('15'))),
                f'<span style="display: flex; align-items: center; gap: 8px; font-size: 11px; color: #a8a8a8">Fluid between 390 and 1440{switch(True)}</span>')
    c += '<div style="display: flex; flex-direction: column">' + '<div style="display: grid; grid-template-columns: 64px minmax(0, 1fr) 120px 48px; gap: 10px; padding: 0 6px 4px; font-size: 10px; color: #6b6b6b"><span>Style</span><span>Sample</span><span style="text-align: right">Size</span><span style="text-align: right">Line</span></div>' + ''.join(trow(*x) for x in names) + '</div>'
    c += f'<div style="display: flex; gap: 8px">{adv("Letter spacing, weights per style, text case")}</div>'
    return window(3, c, preview(focus='text'), footer_note='3 fonts · 8 text styles · fluid')

def step_space():
    vals = [0, 2, 4, 8, 12, 16, 24, 32, 48, 64, 96]
    chips = '<div style="display: flex; flex-wrap: wrap; gap: 6px">' + ''.join(f'<span style="height: 44px; min-width: 44px; padding: 0 6px; box-sizing: border-box; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; border-radius: 4px; background: #2a2a2a"><span style="height: 8px; width: {max(2, v * 0.4):.0f}px; border-radius: 1px; background: rgba(26,146,132,0.7)"></span><span style="{MONO_}; font-size: 10px; color: #c8c8c8">{v}</span></span>' for v in vals) + f'<span style="height: 44px; width: 44px; display: flex; align-items: center; justify-content: center; border-radius: 4px; border: 1px dashed #454545; color: #a8a8a8">{icon("plus", 11, "currentColor", 1.75)}</span></div>'
    bps = [('Desktop', 'desktop', 1440, '12', 64, 24, '1280'), ('Tablet', 'tablet', 768, '8', 32, 20, 'fluid'), ('Mobile', 'phone', 390, '4', 20, 16, 'fluid')]
    bp_rows = ''.join(f'<div style="display: grid; grid-template-columns: 24px 70px repeat(5, minmax(0, 1fr)); align-items: center; gap: 8px; padding: 4px 6px; border-radius: 4px; background: #2a2a2a">{icon(ic, 14, "#a8a8a8")}<span style="font-weight: 500">{n}</span>{fld(num(w))}{fld(num(c, "col"))}{fld(num(m))}{fld(num(g))}{fld(num(mx, "" if mx == "fluid" else "px"))}</div>' for n, ic, w, c, m, g, mx in bps)
    bp_hdr = '<div style="display: grid; grid-template-columns: 24px 70px repeat(5, minmax(0, 1fr)); gap: 8px; padding: 0 6px; font-size: 10px; color: #6b6b6b"><span></span><span></span><span>Width</span><span>Columns</span><span>Margin</span><span>Gutter</span><span>Max content</span></div>'
    gridviz = '<div style="height: 40px; display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 6px; padding: 0 22px; border-radius: 4px; background: #1f1f1f">' + '<span style="background: rgba(26,146,132,0.22)"></span>' * 12 + '</div>'
    c = h2('Spacing &amp; layout', 'A spacing scale for gaps and padding, and the screen sizes with their grids.')
    c += group('Spacing scale', grid('minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr)', fieldr('Base unit', seg(['4', '8'], 0)), field('Steps', dd('Base × 0.5 … 24')), field('Names', dd('Numbers · space-1 … space-10'))) + chips, adv())
    c += group('Screen sizes and grid', bp_hdr + '<div style="display: flex; flex-direction: column; gap: 4px">' + bp_rows + '</div>' + gridviz + '<span style="font-size: 11px; color: #939393">These become the page’s screen sizes (Desktop · Tablet · Mobile) in the editor.</span>',
                f'<button style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 6px; font-size: 11px; color: #a8a8a8">{icon("plus", 11, "currentColor", 1.75)}Screen size</button>')
    return window(4, c, preview(focus='space'), footer_note='11 spaces · 3 screen sizes')

def step_shape():
    rads = [('none', 0), ('sm', 4), ('md', 8), ('lg', 16), ('xl', 24), ('full', 999)]
    rad = '<div style="display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 6px">' + ''.join(f'<div style="padding: 6px; display: flex; flex-direction: column; align-items: center; gap: 4px; border-radius: 4px; background: #2a2a2a; {"box-shadow: inset 0 0 0 1px #2f80ed;" if n == "md" else ""}"><span style="width: 36px; height: 20px; border: 1.5px solid #c8c8c8; border-radius: {min(r, 14)}px"></span><span style="font-size: 11px">{n} <span style="{MONO_}; font-size: 10px; color: #939393">{r}</span></span></div>' for n, r in rads) + '</div>'
    shs = [('1', '0 1px 2px rgba(0,0,0,.25)'), ('2', '0 2px 4px rgba(0,0,0,.25), 0 6px 14px rgba(0,0,0,.25)'), ('3', '0 4px 8px rgba(0,0,0,.3), 0 14px 30px rgba(0,0,0,.35)')]
    sh = '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; padding: 6px 4px 8px">' + ''.join(f'<div style="height: 36px; display: flex; align-items: center; justify-content: center; border-radius: 6px; background: #3a3a3a; box-shadow: {s}; font-size: 11px; color: #c8c8c8">shadow-{n}</div>' for n, s in shs) + '</div>'
    mot = grid('repeat(4, minmax(0, 1fr))', field('Fast', num('120', 'ms')), field('Base', num('200', 'ms')), field('Slow', num('320', 'ms')), field('Easing', dd('Standard')))
    c = h2('Shape &amp; depth', 'Corner radius, borders, shadows and motion for components.')
    c += group('Corners', grid('minmax(0, 1fr) minmax(0, 1fr)', fieldr('Style', seg(['Sharp', 'Soft', 'Round'], 1)), field('Buttons use', dd('md · 8'))) + rad)
    c += group('Borders', grid('repeat(3, minmax(0, 1fr))', field('Thin', num('1')), field('Thick', num('2')), field('Colour', sw(NEUTRAL[2]) + f'<span style="{MONO_}">neutral-200</span>')))
    c += group('Shadows', grid('minmax(0, 1fr) minmax(0, 1fr)', fieldr('Levels', seg(['None', '2', '3'], 2)), field('Tint', dd('Neutral-900 · 8%'))) + sh)
    c += group('Motion', mot, '<span style="font-size: 11px; color: #939393">Turned off for people who ask for reduced motion</span>')
    return window(5, c, preview(focus='shape'), footer_note='6 radii · 2 borders · 3 shadows · 4 motion')

def step_review():
    rows = [('palette', 'Colours', '6 roles · 66 steps · 16 role tokens · light and dark', 'Colours'), ('type', 'Typography', 'Fraunces, Inter, JetBrains Mono · 8 fluid styles · 390 → 1440', 'Typography'),
            ('grid', 'Spacing &amp; layout', '11 spaces (base 4) · Desktop 1440 · Tablet 768 · Mobile 390', 'Spacing & layout'), ('layers2', 'Shape &amp; depth', '6 radii · 2 borders · 3 shadows · 4 motion', 'Shape & depth')]
    summ = ''.join(f'<div style="height: 44px; display: flex; align-items: center; gap: 12px; padding: 0 12px; border-radius: 4px; background: #2a2a2a">{icon(ic, 15, "#a8a8a8")}<span style="width: 140px; font-weight: 500">{t}</span><span style="flex: 1; min-width: 0; font-size: 11px; color: #a8a8a8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{d}</span><button style="font-size: 11px; color: #a9c8f7">Edit</button></div>' for ic, t, d, _ in rows)
    code = f'''<pre style="margin: 0; padding: 12px; border-radius: 4px; background: #1b1b1b; box-shadow: inset 0 0 0 1px #303030; {MONO_}; line-height: 17px; color: #c8c8c8; white-space: pre; overflow: hidden"><span style="color: #7a7a7a">/* tokens.css · Mossbank Tea · 142 tokens */</span>
<span style="color: #7fb0f0">:root</span> {{
  --color-primary-600: <span style="color: #d9a66b">#4f6b3a</span>;
  --color-text: <span style="color: #9cc58a">var(--color-neutral-900)</span>;
  --font-heading: <span style="color: #9cc58a">"Fraunces", serif</span>;
  --text-h1: <span style="color: #9cc58a">clamp(2.07rem, 1.79rem + 1.2vw, 2.44rem)</span>;
  --space-4: <span style="color: #d9a66b">16px</span>;  --radius-md: <span style="color: #d9a66b">8px</span>;
}}</pre>'''
    out = grid('minmax(0, 1fr) minmax(0, 1fr)', field('Naming', dd('Role and step', '--color-primary-600')), field('Prefix', '<span style="color: #939393">none</span>'))
    c = h2('Review', 'Mossbank Tea will be created in D:\\Sites\\mossbank-tea with one page and this design system.')
    c += '<div style="display: flex; flex-direction: column; gap: 6px">' + summ + '</div>'
    c += group('Output', out + code + '<div style="display: flex; gap: 20px">' + check(True, 'tokens.css') + check(True, 'tokens.json <span style="color: #939393">(W3C Design Tokens)</span>') + check(False, 'Figma variables') + '</div>')
    c += '<span style="flex: 1"></span>' + check(True, 'Open the design system after creating')
    return window(6, c, preview(), next_label='Create project', footer_note='142 tokens')
