from screen import *

# take the live page markup from the editor shell, without selection overlays
S = Screen('tmp')
S.remove_h1_overlay()
S.remove_parent_outline()
s = S.s
a = s.index('<!-- Header -->', s.index('<!-- page frame')); b = s.index('<!-- fold line at 900 -->', a)
pg = s[a:b]
pg = pg.replace('<a href="#visit" style="background: #b5532d; color: #ffffff; border-radius: 999px; padding: 10px 20px; font-size: 15px; font-weight: 500; line-height: 20px">Book a visit</a>',
                '<a href="#visit" style="position: relative; background: #9b4424; color: #ffffff; border-radius: 999px; padding: 10px 20px; font-size: 15px; font-weight: 500; line-height: 20px; box-shadow: 0 4px 12px rgba(155,68,36,0.25)">Book a visit'
                '<svg aria-hidden="true" width="22" height="22" viewBox="0 0 16 16" style="position: absolute; left: 62%; top: 58%; overflow: visible"><path d="M6 2.5a1 1 0 0 1 2 0V7l3.8.8a1.5 1.5 0 0 1 1.2 1.7l-.6 3.8a1.5 1.5 0 0 1-1.5 1.2H7.6a1.5 1.5 0 0 1-1.2-.6L3.3 9.7a1 1 0 0 1 1.5-1.3L6 9.6z" fill="#ffffff" stroke="#1d1a16" stroke-width="1" stroke-linejoin="round"></path></svg></a>')
pg = pg.replace('<div style="justify-self: end; width: 580px; height: 520px;', '<div style="justify-self: end; width: 100%; max-width: 580px; height: 520px;')
head = s[:s.index('<body>')]
head = head.replace('<title>tmp</title>', '<title>Daisy · D-29 Preview mode</title>')

W = 1280
PAGE_L = (1920 - W) // 2
RESP = '#d29922'
tb = lambda inner, on=False, label='': f'<button aria-label="{label}" aria-pressed="{str(on).lower()}" style="height: 26px; display: flex; align-items: center; gap: 6px; padding: 0 9px; border-radius: 5px; white-space: nowrap; {"background: #333333; color: #e8e8e8;" if on else "color: #a8a8a8;"}">{inner}</button>'
cap = lambda inner: f'<div style="height: 30px; display: flex; align-items: center; gap: 2px; padding: 2px; box-sizing: border-box; background: #232323; border-radius: 6px">{inner}</div>'
tog = lambda t, on: f'<button aria-pressed="{str(on).lower()}" style="height: 26px; display: flex; align-items: center; gap: 6px; padding: 0 9px; border-radius: 5px; white-space: nowrap; {"background: rgba(47,128,237,0.18); color: #a9c8f7;" if on else "color: #a8a8a8;"}">{t}</button>'
P['rotate'] = ('stroke', 'M3 8a5 5 0 1 0 1.5-3.5M3 2.5v3h3')
P['external'] = P.get('external', ('stroke', 'M9 2.5h4.5V7M13.5 2.5L7 9M11 9.5v4H2.5V5H6'))
P['back'] = ('stroke', 'M10 3L5 8l5 5')
P['share'] = ('stroke', 'M10.5 4.5L8 2 5.5 4.5M8 2v8M3.5 8v5.5h9V8')
bar = f'''<!-- PREVIEW BAR (h44) -->
<div style="height: 44px; flex: none; box-sizing: border-box; display: flex; align-items: center; gap: 10px; padding: 0 12px; background: #141414; border-bottom: 1px solid #2a2a2a">
<button style="height: 30px; display: flex; align-items: center; gap: 8px; padding: 0 12px 0 8px; border-radius: 6px; background: #2a2a2a; color: #e8e8e8; font-weight: 500">{icon('back', 14, 'currentColor', 1.75)}Back to editing<span style="height: 18px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #3a3a3a; font-size: 10px; color: #c8c8c8">Esc</span></button>
<span style="width: 1px; height: 18px; background: #2e2e2e"></span>
<button style="height: 30px; display: flex; align-items: center; gap: 8px; padding: 0 10px; border-radius: 6px; background: #232323; color: #e8e8e8">{icon('file', 13, '#a8a8a8')}Home<span style="font-family: {MONO}; font-size: 11px; color: #939393">index.html</span>{icon('chev-down', 10, '#939393', 1.75)}</button>
<span style="font-size: 11px; color: #939393">Links work · click to visit other pages</span>
<span style="flex: 1"></span>
{cap(tb(icon('desktop', 14), False, 'Desktop 1440') + tb(icon('tablet', 14), False, 'Tablet 768') + tb(icon('phone', 14), False, 'Mobile 390') + '<span style="width: 1px; height: 14px; background: #333333; margin: 0 2px"></span>'
     + f'<label style="height: 26px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 5px; background: rgba(47,128,237,0.18); box-shadow: inset 0 0 0 1px #2f80ed"><span style="font-size: 11px; color: #a9c8f7">Width</span><b style="font-weight: 600; font-variant-numeric: tabular-nums">{W}</b><span style="font-size: 10px; color: #939393">px</span></label>'
     + tb(icon('rotate', 13), False, 'Rotate'))}
<span style="font-size: 11px; color: #939393; white-space: nowrap">100%</span>
<span style="flex: 1"></span>
{cap(tog('Less motion', False) + tog('Dark preference', False) + tog('Slow network', False))}
<span style="width: 1px; height: 18px; background: #2e2e2e"></span>
{tb(icon('share', 13) + 'Share link')}{tb(icon('external', 13) + 'Open in new tab')}
</div>'''

# breakpoint ruler above the page: shows which screen size's styles apply at this width
rx = lambda w: PAGE_L + (w / 1440) * W * (1440 / W) * (W / 1440) if False else None
RL, RW = PAGE_L, W  # ruler drawn across the page width, scale: 0..1600 px
sc = RW / 1600
seg_ = lambda a, b, name, ic, on=False: f'<div style="position: absolute; left: {a * sc:.0f}px; width: {(b - a) * sc:.0f}px; top: 0; height: 22px; display: flex; align-items: center; gap: 6px; padding-left: 8px; box-sizing: border-box; border-left: 1px solid #3a3a3a; font-size: 11px; {"background: rgba(47,128,237,0.12); color: #e8e8e8;" if on else "color: #939393;"}">{icon(ic, 12, RESP if on else "#6b6b6b", 1.5)}{name}</div>'
ruler = (f'<div aria-label="Screen sizes" style="position: absolute; left: {RL}px; top: 14px; width: {RW}px; height: 22px; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #303030; overflow: hidden">'
         + seg_(0, 640, 'Mobile ≤ 640', 'phone') + seg_(640, 1024, 'Tablet ≤ 1024', 'tablet') + seg_(1024, 1600, 'Desktop styles · base', 'desktop', True)
         + f'<span style="position: absolute; left: {W * sc - 1:.0f}px; top: 0; bottom: 0; width: 2px; background: #2f80ed"></span>'
         + f'<span style="position: absolute; left: {1440 * sc:.0f}px; top: 0; bottom: 0; border-left: 1px dashed #6b6b6b"></span><span style="position: absolute; left: {1440 * sc + 4:.0f}px; top: 4px; font-size: 10px; color: #939393">1440 canvas</span></div>'
         + f'<span style="position: absolute; left: {RL + W * sc - 26:.0f}px; top: 38px; height: 16px; padding: 0 6px; border-radius: 8px; background: #246bcb; color: #fff; font-size: 10px; font-weight: 600; line-height: 16px">{W}</span>')
handle = lambda side: f'<div aria-label="Drag to resize" style="position: absolute; {side}: -18px; top: calc(50% - 32px); width: 10px; height: 64px; border-radius: 5px; background: #3a3a3a; box-shadow: inset 0 0 0 1px #4a4a4a; display: flex; align-items: center; justify-content: center"><span style="width: 2px; height: 26px; border-left: 1px solid #8a8a8a; border-right: 1px solid #8a8a8a"></span></div>'
canvas = f'''<main aria-label="Preview" style="position: relative; flex: 1; min-height: 0; overflow: hidden; background: #2a2a2a">
{ruler}
<div style="position: absolute; left: {PAGE_L}px; top: 62px; bottom: 0; width: {W}px">
{handle('left')}{handle('right')}
<div style="position: absolute; inset: 0; overflow: hidden; background: #f6f1ea; box-shadow: 0 0 0 1px #3c3c3c, 0 16px 48px rgba(0,0,0,0.45); border-radius: 6px 6px 0 0">
<div style="position: relative; width: {W}px; background: #f6f1ea; color: #1d1a16; font-family: 'Inter', sans-serif; font-size: 16px; line-height: 1.5">
{pg}
</div></div></div>
<div style="position: absolute; right: 18px; bottom: 16px; display: flex; align-items: center; gap: 8px; height: 26px; padding: 0 10px; border-radius: 13px; background: rgba(20,20,20,0.85); color: #c8c8c8; font-size: 11px">{icon('info', 11, '#58a6ff', 1.25)}Hover, links and animations behave as on the live site · Esc goes back</div>
</main>'''

html = head + f'''<body>
<x-dc>
<helmet>
''' + s[s.index('<helmet>') + len('<helmet>'):s.index('</helmet>')] + f'''</helmet>
<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden; background: #2a2a2a; color: #e8e8e8; font-family: 'Inter', system-ui, sans-serif; font-size: 12px; line-height: 16px">
{bar}
{canvas}
</div>
</x-dc>
''' + s[s.index('<script type="text/x-dc"'):]
open('/home/claude/daisy/project/D29-Preview.dc.html', 'w', encoding='utf-8').write(html)
print('ok')
