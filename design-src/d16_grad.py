# INSET: Gradient tool — behaviour bar + canvas stops + Gradient editor popover
FLOAT = 'background: #1f1f1f; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 8px 24px rgba(0,0,0,0.45);'
stop = lambda x, c, sel=False: f'<span style="position: absolute; left: {x}; top: 50%; transform: translate(-50%, -50%); width: 14px; height: 14px; box-sizing: border-box; border-radius: 50%; background: {c}; box-shadow: 0 0 0 2px #ffffff, 0 0 0 {"4px #2f80ed" if sel else "3px rgba(0,0,0,0.35)"}"></span>'
GRAD = 'linear-gradient(90deg in oklch, #b5532d 0%, #c8663a 50%, #d97a4e 100%)'
gtog = lambda t, on: f'<button aria-pressed="{str(on).lower()}" style="height: 22px; display: flex; align-items: center; padding: 0 7px; border-radius: 4px; white-space: nowrap; font-size: 11px; {"background: rgba(47,128,237,0.18); color: #a9c8f7;" if on else "color: #a8a8a8;"}">{t}</button>'
gbar = (f'<div style="height: 30px; display: flex; align-items: center; gap: 4px; padding: 0 4px; margin-bottom: 10px; background: #1b1b1b; border-radius: 4px">'
        f'<span style="font-size: 11px; color: #939393; padding: 0 4px">Click the line</span>{gtog("adds a stop", True)}<span style="width: 1px; height: 14px; background: #333333"></span>'
        f'{gtog("Snap stops to 25%", True)}{gtog("Show stop labels", True)}{gtog("Edit every fill layer", False)}<span style="flex: 1"></span><span style="font-size: 11px; color: #939393; padding-right: 4px">Values: in the gradient editor</span></div>')
srow = lambda c, name, pos, sel=False: (f'<div style="height: 26px; display: grid; grid-template-columns: 16px minmax(0, 1fr) 58px 18px; gap: 6px; align-items: center; padding: 0 6px; border-radius: 3px; {"background: rgba(47,128,237,0.14); box-shadow: inset 0 0 0 1px #2f80ed;" if sel else "background: #2a2a2a;"}">'
                                        f'<span style="width: 14px; height: 14px; border-radius: 2px; background: {c}; box-shadow: inset 0 0 0 1px rgba(0,0,0,0.25)"></span><span style="font-size: 11px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{name}</span>'
                                        f'<span style="display: flex; align-items: center; justify-content: flex-end; gap: 3px; font-size: 11px">{pos}<span style="font-size: 10px; color: #939393">%</span></span><button aria-label="Remove stop" style="color: #939393">{icon("close", 10)}</button></div>')
chips = ''.join(f'<button style="height: 20px; padding: 0 7px; border-radius: 3px; background: #2a2a2a; font-size: 10px; color: #a8a8a8">{t}</button>' for t in ['Repeat', 'Reverse', '⋯'])
editor = f'''<div role="dialog" aria-label="Gradient editor" style="width: 344px; flex: none; padding: 0 10px 10px; box-sizing: border-box; display: flex; flex-direction: column; gap: 7px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 10px 28px rgba(0,0,0,0.5); font-variant-numeric: tabular-nums">
<div style="height: 32px; margin: 0 -10px; padding: 0 8px 0 10px; display: flex; align-items: center; gap: 6px; border-bottom: 1px solid #3a3a3a"><span style="font-weight: 600; font-size: 12px">Gradient</span><span style="flex: 1; font-size: 11px; color: #939393">Fill layer 1 · Book a visit</span>{icon("close", 12, "#a8a8a8")}</div>
<div style="display: grid; grid-template-columns: minmax(0, 1fr) 84px; gap: 6px">{L['seg'](['Linear', 'Radial', 'Conic'], 0)}{L['fieldv']('Angle', '90', '°')}</div>
<span style="position: relative; height: 18px; margin: 2px 7px; border-radius: 3px; background: {GRAD}">{stop("0%", "#b5532d")}{stop("50%", "#c8663a", True)}{stop("100%", "#d97a4e")}</span>
{srow('#b5532d', 'terracotta · brand token', '0')}{srow('#c8663a', '#C8663A · just added', '50', True)}{srow('#d97a4e', '#D97A4E', '100')}
<div style="display: flex; gap: 6px; align-items: center"><span style="font-size: 11px; color: #a8a8a8; white-space: nowrap">Blend <span style="font-family: {MONO}; font-size: 10px; color: #939393">oklch</span></span><span style="width: 124px; flex: none">{L['seg'](['sRGB', 'Smooth'], 1)}</span><span style="flex: 1"></span>{chips}</div>
<code style="font-family: {MONO}; font-size: 10px; line-height: 14px; color: #939393">linear-gradient(90deg in oklch, #b5532d, #c8663a 50%, #d97a4e)</code>
</div>'''
line_stops = ''.join(f'<span aria-hidden="true" style="position: absolute; left: calc(14px + (100% - 28px) * {p / 100}); top: calc(100% + 16px); width: 0; height: 0">{stop("0", c, sel)}<span style="position: absolute; left: 0; top: 12px; transform: translateX(-50%); font: 500 10px/1 Inter, sans-serif; color: #4a443c">{p}%</span></span>' for p, c, sel in [(0, '#b5532d', False), (50, '#c8663a', True), (100, '#d97a4e', False)])
inset = f'''<!-- INSET: Gradient tool -->
<div aria-label="Inset: Gradient tool on Book a visit" style="position: absolute; left: 60px; top: 548px; width: 880px; padding: 12px; box-sizing: border-box; {FLOAT} z-index: 10">
<div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 11px"><span style="font-weight: 600">Inset · Gradient tool: its options bar, the canvas, and the gradient editor it opens</span><span style="color: #939393">Book a visit · a</span></div>
{gbar}
<div style="display: flex; gap: 12px; align-items: stretch">
<div style="position: relative; flex: 1; min-width: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 48px; background: #f6f1ea; border-radius: 2px">
<span style="position: relative; height: 44px; padding: 0 34px; display: flex; align-items: center; border-radius: 999px; background: {GRAD}; color: #ffffff; font-size: 16px; font-weight: 500">Book a visit
<span aria-hidden="true" style="position: absolute; inset: -2px; border: 1.5px solid #2f80ed; border-radius: 999px"></span>
<span aria-hidden="true" style="position: absolute; left: 14px; right: 14px; top: calc(100% + 16px); border-top: 1.5px solid #2f80ed"></span>{line_stops}</span>
<span style="font-size: 11px; color: #6b6b6b; text-align: center; padding: 0 12px">Drag the line ends to set direction · drag a stop to move it (snaps at 25%) · click the line to add one</span>
</div>
{editor}
</div></div>'''
