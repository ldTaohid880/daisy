import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

W = 1920

dark = [
    ('Surfaces', [
        ('bg-titlebar', '#141414', 'Top bar'), ('bg-toolbar', '#1b1b1b', 'Options bar'),
        ('bg-chrome', '#181818', 'Tool strip, tabs, status'), ('bg-panel', '#1f1f1f', 'Docks, drawer'),
        ('bg-capsule', '#232323', 'Control holders'), ('bg-popover', '#262626', 'Menus, popovers'),
        ('bg-workspace', '#2a2a2a', 'Canvas'), ('bg-control', '#2a2a2a', 'Fields'),
        ('bg-control-hover', '#323232', 'Hover'), ('bg-control-active', '#3a3a3a', 'Pressed, selected'),
    ]),
    ('Lines', [
        ('line-subtle', '#262626', 'Indent guides, bar borders'), ('line', '#303030', 'Panel separators'),
        ('line-strong', '#454545', 'Hover borders, dashed bars'), ('page-edge', '#3c3c3c', 'Page frame'),
    ]),
    ('Text', [
        ('text-primary', '#e8e8e8', 'Main text'), ('text-secondary', '#a8a8a8', 'Labels, icons'),
        ('text-muted', '#939393', 'Tags, captions, placeholders'), ('text-disabled', '#4f4f4f', 'Disabled only'),
    ]),
    ('Accent', [
        ('accent', '#2f80ed', 'Selection, active, focus'), ('accent-hover', '#4b93f1', 'Primary hover'),
        ('accent-fill', '#246bcb', 'Behind white text'), ('accent-subtle', 'rgba(47,128,237,0.18)', 'Selected rows, tool chip'),
    ]),
    ('Meaning', [
        ('resp', '#d29922', 'Screen-size edits'), ('state', '#a371f7', 'State edits'),
        ('info', '#58a6ff', 'Hints, notices'), ('success', '#3fb950', 'Saved, done'),
        ('warning', '#d29922', 'Accessibility'), ('danger', '#f85149', 'Errors, delete'),
    ]),
    ('Brand', [('brand-daisy', '#f2b84b', 'Brand mark centre only')]),
]

light = [
    ('bg-titlebar', '#f3f3f3'), ('bg-toolbar', '#f7f7f7'), ('bg-chrome', '#f3f3f3'), ('bg-panel', '#fafafa'),
    ('bg-capsule', '#efefef'), ('bg-workspace', '#e4e4e4'), ('bg-control', '#ffffff'), ('bg-control-hover', '#f0f0f0'),
    ('bg-control-active', '#e6e6e6'), ('bg-popover', '#ffffff'), ('line-subtle', '#ececec'), ('line', '#e1e1e1'),
    ('line-strong', '#c9c9c9'), ('page-edge', '#cfcfcf'), ('text-primary', '#1c1c1c'), ('text-secondary', '#555555'),
    ('text-muted', '#6b6b6b'), ('text-disabled', '#b5b5b5'),
]


def swatch(name, val, use):
    is_text = name.startswith('text-')
    if is_text and val.startswith('#'):
        r = contrast(val, '#1f1f1f')
        ok = 'AA' if r >= 4.5 else ('decor' if name == 'text-disabled' else 'fail')
        badge_col = '#3fb950' if ok == 'AA' else '#939393'
        chip = f'<span style="width: 64px; height: 48px; flex: none; display: flex; align-items: center; justify-content: center; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #303030; color: {val}; font-size: 18px; font-weight: 500">Aa</span>'
        extra = f'<span style="font-size: 10px; color: {badge_col}">{r:.2f}:1 on bg-panel · {ok}</span>'
    else:
        chip = f'<span style="width: 64px; height: 48px; flex: none; border-radius: 4px; background: {val}; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.08)"></span>'
        extra = ''
        if name == 'accent-fill':
            extra = f'<span style="font-size: 10px; color: #3fb950">white {contrast("#ffffff", val):.2f}:1 · AA</span>'
        if name == 'accent':
            extra = f'<span style="font-size: 10px; color: #939393">white {contrast("#ffffff", val):.2f}:1 · not for text fills</span>'
    return f'''<div style="display: flex; gap: 12px; align-items: center">
{chip}
<div style="min-width: 0; display: flex; flex-direction: column; gap: 2px">
<span style="font-family: {MONO}; font-size: 11px; color: #e8e8e8">{name}</span>
<span style="font-family: {MONO}; font-size: 11px; color: #a8a8a8">{val}</span>
<span style="font-size: 11px; color: #939393">{use}</span>
{extra}
</div>
</div>'''


dark_html = ''
for gname, items in dark:
    dark_html += f'<div style="grid-column: 1 / -1; font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393; margin-top: 8px">{gname.upper()}</div>'
    dark_html += ''.join(swatch(*i) for i in items)
dark_block = grid(5, dark_html, gap=20)

light_html = ''.join(f'''<div style="display: flex; gap: 10px; align-items: center">
<span style="width: 40px; height: 32px; flex: none; border-radius: 4px; background: {v}; box-shadow: inset 0 0 0 1px rgba(0,0,0,0.12)"></span>
<span style="display: flex; flex-direction: column; gap: 1px"><span style="font-family: {MONO}; font-size: 11px; color: #1c1c1c">{n}</span><span style="font-family: {MONO}; font-size: 11px; color: #555555">{v}</span></span>
</div>''' for n, v in light)
light_note = f'<div style="grid-column: 1 / -1; font-size: 11px; color: #555555">Accent, meaning and overlay colours are the same in both themes. <span style="color: #1c1c1c">text-muted #6b6b6b = {contrast("#6b6b6b", "#f3f3f3"):.2f}:1 on bg-chrome</span>. New light values (titlebar, toolbar, capsule, line-subtle) are proposals to confirm on D-33.</div>'
light_block = f'<div style="padding: 24px; border-radius: 8px; background: #fafafa; box-shadow: inset 0 0 0 1px #e1e1e1">{grid(6, light_html + light_note, gap=16)}</div>'

# ---- overlay key ----
def mini(inner):
    return f'<div style="position: relative; width: 100%; height: 104px; border-radius: 4px; background: #f6f1ea; overflow: hidden">{inner}</div>'

ov = [
    ('ov-select', '#2f80ed', 'Selection, hover, insertion, drop target',
     mini('<div style="position: absolute; left: 40px; top: 30px; width: 120px; height: 44px; border: 1.5px solid #2f80ed"></div>'
          '<span style="position: absolute; left: 39px; top: 10px; height: 18px; padding: 0 4px; display: flex; align-items: center; background: #246bcb; color: #fff; font-size: 11px; font-weight: 500">Box · div</span>'
          + ''.join(f'<span style="position: absolute; left: {x}px; top: {y}px; width: 8px; height: 8px; box-sizing: border-box; background: #fff; border: 1px solid #2f80ed; border-radius: 1px"></span>' for x, y in [(36, 26), (96, 26), (156, 26), (36, 70), (96, 70), (156, 70), (36, 48), (156, 48)]))),
    ('ov-inside', '#3fb950', 'Space inside (padding)',
     mini('<div style="position: absolute; left: 40px; top: 18px; width: 140px; height: 68px; background: rgba(63,185,80,0.3); box-shadow: inset 0 0 0 1px #3fb950"></div><div style="position: absolute; left: 56px; top: 34px; width: 108px; height: 36px; background: #f6f1ea; box-shadow: 0 0 0 1px #3fb950"></div><span style="position: absolute; left: 104px; top: 19px; font-size: 10px; color: #1d5b27">16</span>')),
    ('ov-outside', '#f0883e', 'Space outside (margin)',
     mini('<div style="position: absolute; left: 40px; top: 16px; width: 140px; height: 24px; background: rgba(240,136,62,0.3)"></div><div style="position: absolute; left: 40px; top: 40px; width: 140px; height: 40px; background: #e7d9c7"></div><span style="position: absolute; left: 104px; top: 21px; font-size: 10px; color: #7a3d10">24</span>')),
    ('ov-gap', '#db61a2', 'Space between (gap), hatched 45°',
     mini('<div style="position: absolute; left: 28px; top: 26px; width: 60px; height: 52px; background: #e7d9c7"></div><div style="position: absolute; left: 88px; top: 26px; width: 32px; height: 52px; background: repeating-linear-gradient(45deg, rgba(219,97,162,0.55) 0 2px, rgba(219,97,162,0.12) 2px 6px)"></div><div style="position: absolute; left: 120px; top: 26px; width: 60px; height: 52px; background: #e7d9c7"></div><span style="position: absolute; left: 92px; top: 82px; padding: 0 4px; border-radius: 3px; background: #db61a2; color: #fff; font-size: 10px">32</span>')),
    ('ov-guide', '#e535ab', 'Alignment guides, equal spacing',
     mini('<div style="position: absolute; left: 20px; right: 20px; top: 30px; border-top: 1px solid #e535ab"></div><div style="position: absolute; left: 36px; top: 30px; width: 50px; height: 40px; background: #e7d9c7"></div><div style="position: absolute; left: 130px; top: 30px; width: 50px; height: 28px; background: #d8cbb8"></div><span style="position: absolute; left: 92px; top: 38px; padding: 0 4px; border-radius: 3px; background: #e535ab; color: #fff; font-size: 10px">44</span>')),
    ('ov-measure', '#f85149', 'Measure, distances, invalid drop',
     mini('<div style="position: absolute; left: 30px; top: 30px; width: 40px; height: 44px; background: #e7d9c7"></div><div style="position: absolute; left: 150px; top: 30px; width: 40px; height: 44px; background: #e7d9c7"></div><div style="position: absolute; left: 70px; width: 80px; top: 52px; border-top: 1px solid #f85149"></div><span style="position: absolute; left: 98px; top: 58px; padding: 0 4px; border-radius: 3px; background: #f85149; color: #fff; font-size: 10px">80</span>')),
    ('ov-track', '#1a9284', 'Grid tracks, badges, origin',
     mini('<div style="position: absolute; left: 24px; top: 30px; width: 172px; height: 56px; box-shadow: inset 0 0 0 1px #1a9284"></div><div style="position: absolute; left: 82px; top: 30px; height: 56px; border-left: 1px dashed #1a9284"></div><div style="position: absolute; left: 140px; top: 30px; height: 56px; border-left: 1px dashed #1a9284"></div>' + ''.join(f'<span style="position: absolute; left: {x}px; top: 10px; padding: 0 4px; border-radius: 3px; background: #1a9284; color: #fff; font-size: 10px">1fr</span>' for x in (40, 98, 156)))),
    ('ov-ruler', '#22c5e0', 'Manual ruler guides',
     mini('<div style="position: absolute; left: 0; right: 0; top: 0; height: 14px; background: #e4e4e4"></div><div style="position: absolute; left: 110px; top: 0; bottom: 0; border-left: 1px solid #22c5e0"></div><span style="position: absolute; left: 114px; top: 1px; font-size: 9px; color: #0b5d6b">640</span>')),
]
ov_html = ''.join(f'''<div style="display: flex; flex-direction: column; gap: 8px">{ex}
<div style="display: flex; align-items: center; gap: 8px"><span style="width: 12px; height: 12px; border-radius: 3px; background: {c}"></span><span style="font-family: {MONO}; font-size: 11px">{n}</span><span style="font-family: {MONO}; font-size: 11px; color: #939393">{c}</span></div>
<div style="font-size: 11px; color: #939393">{u}</div></div>''' for n, c, u, ex in ov)
ov_block = grid(4, ov_html, gap=24) + '<div style="margin-top: 12px; font-size: 11px; color: #939393">Overlay colours have a fixed meaning in both themes and are always drawn at fixed screen thickness, whatever the zoom. Overlay feedback is never animated.</div>'

# ---- type ----
types = [
    ('ui-xs', '10 / 14 · 500', 'font-size: 10px; line-height: 14px; font-weight: 500', 'Badges · units · FOLD · 900'),
    ('ui-sm', '11 / 16 · 400', 'font-size: 11px; line-height: 16px', 'Labels, tags and the status bar hint'),
    ('ui-base', '12 / 16 · 400', 'font-size: 12px; line-height: 16px', 'Space inside · default UI text, fields and menus'),
    ('ui-medium', '12 / 16 · 500', 'font-size: 12px; line-height: 16px; font-weight: 500', 'Tabs, tool name, buttons'),
    ('ui-strong', '12 / 16 · 600', 'font-size: 12px; line-height: 16px; font-weight: 600', 'Group headers · Typography'),
    ('ui-title', '14 / 20 · 600', 'font-size: 14px; line-height: 20px; font-weight: 600', 'Dialog title · Export Halden'),
    ('ui-display', '20 / 28 · 600', 'font-size: 20px; line-height: 28px; font-weight: 600', 'Your projects'),
    ('mono-sm', '11 / 16 · JetBrains Mono', f'font-family: {MONO}; font-size: 11px; line-height: 16px', 'border-radius: 12px; · index.html · h1'),
]
type_rows = ''.join(f'''<div style="display: grid; grid-template-columns: 140px 220px 1fr; align-items: center; gap: 16px; padding: 12px 0; border-bottom: 1px solid #262626">
<span style="font-family: {MONO}; font-size: 11px">{n}</span><span style="font-size: 11px; color: #939393">{spec}</span><span style="{st}">{ex}</span></div>''' for n, spec, st, ex in types)
type_block = type_rows + f'<div style="margin-top: 12px; font-size: 11px; color: #939393">Inter for UI, JetBrains Mono for tags, CSS and code. Numbers use tabular figures (<code style="font-family: {MONO}">tnum</code>). No text below 10 px.</div>'

# ---- spacing / sizes / radii / elevation / focus ----
sp = ''.join(f'<div style="display: flex; flex-direction: column; align-items: center; gap: 6px"><span style="width: {v}px; height: 32px; background: #2f80ed; opacity: 0.6; border-radius: 1px"></span><span style="font-family: {MONO}; font-size: 11px">{v}</span></div>' for v in (2, 4, 8, 12, 16, 24, 32))
sp_block = f'<div style="display: flex; gap: 28px; align-items: flex-end; padding: 20px; background: #1a1a1a; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a">{sp}</div><div style="margin-top: 8px; font-size: 11px; color: #939393">Base unit 4 px. Tight pairs 4 · controls in a row 8 · panel padding 12.</div>'

sizes = [('Field / control', 24, 120), ('Capsule', 28, 120), ('Panel row', 28, 160), ('Tree row', 24, 160), ('Tool button', 32, 32), ('Page tab', 32, 140), ('Options bar', 36, 180), ('Top bar', 40, 180)]
sz = ''.join(f'<div style="display: flex; align-items: center; gap: 12px"><span style="width: {w}px; height: {h}px; border-radius: 2px; background: #2a2a2a; box-shadow: inset 0 0 0 1px #454545"></span><span style="font-size: 11px">{n}</span><span style="font-family: {MONO}; font-size: 11px; color: #939393">{h}</span></div>' for n, h, w in sizes)
sz_block = f'<div style="display: flex; flex-direction: column; gap: 10px">{sz}</div>'

radii = [(2, 'radius-field', 'Fields in panels'), (3, 'radius-badge', 'Key badges, tags, tab ×'), (4, 'radius-control', 'Buttons, segments, menus'), (6, 'radius-capsule', 'Capsules, search, popovers'), (10, 'radius-chip', 'Chips, pills')]
rd = ''.join(f'<div style="display: flex; flex-direction: column; gap: 8px"><span style="width: 72px; height: 48px; border-radius: {r}px; background: #2a2a2a; box-shadow: inset 0 0 0 1.5px #a8a8a8"></span><span style="font-family: {MONO}; font-size: 11px">{n} · {r}</span><span style="font-size: 11px; color: #939393">{u}</span></div>' for r, n, u in radii)
rd_block = f'<div style="display: flex; gap: 24px">{rd}</div><div style="margin-top: 8px; font-size: 11px; color: #939393">Panels and docks: 0, separated by 1 px lines only.</div>'

elev_block = f'''<div style="display: flex; gap: 32px; align-items: flex-start">
<div style="display: flex; flex-direction: column; gap: 8px"><div style="width: 200px; height: 88px; border-radius: 6px; background: #262626; border: 1px solid #454545; box-shadow: 0 8px 24px rgba(0,0,0,0.45)"></div><span style="font-family: {MONO}; font-size: 11px">shadow-float</span><span style="font-size: 11px; color: #939393">0 8 24 rgba(0,0,0,.45) + 1 px line-strong<br>Menus, popovers, dialogs, tooltips only</span></div>
<div style="display: flex; flex-direction: column; gap: 8px"><div style="width: 200px; height: 88px; display: flex; align-items: center; justify-content: center; background: #1f1f1f; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a"><span style="height: 24px; display: flex; align-items: center; padding: 0 12px; border-radius: 4px; background: #2a2a2a; {FOCUS}">Focused</span></div><span style="font-family: {MONO}; font-size: 11px">focus-ring</span><span style="font-size: 11px; color: #939393">2 px accent, 1 px offset<br>Keyboard focus only (:focus-visible)</span></div>
</div>'''

motion = [('Hover, press colour', '80 ms', 'linear'), ('Disclosure', '140 ms', 'ease-out'), ('Popover / menu', '120 ms fade + 4 px', 'ease-out'), ('Dialog', '160 ms fade + scale .98→1', 'ease-out'), ('Status notice', '160 ms fade', '—'), ('Canvas zoom', '160 ms', 'ease-in-out'), ('Screen-size switch', '160 ms width', 'ease-in-out')]
mo = ''.join(f'<div style="display: grid; grid-template-columns: 1fr 1fr 90px; gap: 12px; padding: 8px 0; border-bottom: 1px solid #262626"><span>{a}</span><span style="font-family: {MONO}; font-size: 11px; color: #a8a8a8">{b}</span><span style="font-family: {MONO}; font-size: 11px; color: #939393">{c}</span></div>' for a, b, c in motion)
mo_block = mo + '<div style="margin-top: 8px; font-size: 11px; color: #939393">Canvas overlay is never animated. All motion stops under reduced motion.</div>'

body = sheet_header('D-00a', 'Foundations', 'Colour, type, space, size, radius, elevation and motion. Every value here is in UI_DESIGN_PLAN.md 9.9 as a CSS variable, so other tools and the code use exactly the same styles.')
body += section('9.1', 'Colour · dark theme (default)', 'Text tokens show contrast on bg-panel', dark_block)
body += section('9.2', 'Colour · light theme', 'Surfaces, lines and text that change', light_block)
body += section('7.2', 'Overlay colour key', 'Fixed meaning across the product', ov_block)
body += f'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 64px">'
body += section('9.3', 'Type scale', 'Inter · JetBrains Mono', type_block)
body += '<div>' + section('9.4', 'Spacing', '4 px grid', sp_block, mb=40) + section('9.4', 'Sizes', 'Heights in px', sz_block, mb=0) + '</div>'
body += '</div>'
body += f'<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 64px">'
body += section('9.5', 'Radius', '', rd_block, mb=0)
body += section('9.5', 'Elevation · focus', '', elev_block, mb=0)
body += section('9.7', 'Motion', '', mo_block, mb=0)
body += '</div>'

H = int(sys.argv[1]) if len(sys.argv) > 1 else 3200
open('/home/claude/daisy/project/DS-Foundations.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-00a Foundations', W, H, body))
