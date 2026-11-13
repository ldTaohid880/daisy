P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
sep = '<div style="height: 1px; background: #333333"></div>'
def pin(sym, v, name, on=False, vis=True):
    return (f'<div style="height: 26px; display: flex; align-items: center; gap: 8px; padding: 0 6px; border-radius: 3px; {"background: rgba(201,48,44,0.16); box-shadow: inset 0 0 0 1px #c9302c;" if on else "background: #2a2a2a;"}">'
            f'<span style="width: 46px; white-space: nowrap; color: #ff7b72; font-variant-numeric: tabular-nums">{sym} {v}</span><span style="flex: 1; font-size: 11px; color: #c8c8c8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{name}</span>'
            f'<span style="color: {"#a8a8a8" if vis else "#6b6b6b"}">{icon("eye" if vis else "eye-off", 12)}</span></div>')
sz = lambda ic, n, v, note='', on=False: f'<div style="display: grid; grid-template-columns: 16px 1fr auto; gap: 8px; align-items: center; font-size: 11px"><span style="color: #939393">{icon(ic, 12)}</span><span style="color: {"#e8e8e8" if on else "#a8a8a8"}">{n}<span style="color: #939393"> {note}</span></span><span style="color: #ff7b72; font-variant-numeric: tabular-nums">{v}</span></div>'
cbtn = lambda t: f'<button style="height: 22px; padding: 0 8px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #c8c8c8">{t}</button>'
mpop = f'''<!-- POPOVER: Measure · Advanced -->
<section role="dialog" aria-label="Measure advanced" style="position: absolute; left: 1282px; top: 136px; width: 328px; box-sizing: border-box; padding: 0 12px 12px; display: flex; flex-direction: column; gap: 9px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); font-variant-numeric: tabular-nums; z-index: 30">
<span aria-hidden="true" style="position: absolute; right: -6px; top: 14px; width: 10px; height: 10px; background: #262626; border-right: 1px solid #454545; border-top: 1px solid #454545; transform: rotate(45deg)"></span>
<div style="height: 40px; margin: 0 -12px; padding: 0 8px 0 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a">
<span style="font-weight: 600">Measure · Advanced</span><span style="flex: 1; font-size: 11px; color: #939393">Text → image</span>
<button aria-label="Pin open" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #939393">{icon("keep", 14)}</button>
<button aria-label="Close" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon("close", 14)}</button></div>
<div style="display: flex; align-items: center; justify-content: space-between">{L['lab']('Pinned on the canvas')}<button style="height: 22px; padding: 0 6px; border-radius: 3px; font-size: 11px; color: #a8a8a8">+ Pin this one</button></div>
{pin('↔', 78, 'Hero text → Hero image · live', True)}{pin('↕', 62, 'Top edges offset')}{pin('↔', 64, 'Grid gap · Hero grid', vis=False)}
<div style="margin-top: -4px; font-size: 10px; line-height: 14px; color: #939393">Pins stay while you edit and update live · Shift+click on the canvas adds one.</div>
{sep}
{L['lab']('Across screen sizes', 'this gap')}
{sz('desktop', 'Desktop', '78 px', '1440', True)}{sz('tablet' if 'tablet' in P else 'desktop', 'Tablet', '40 px', '768')}{sz('phone', 'Mobile', '—', '390 · stacked, ↕ 32 px')}
{sep}
{L['lab']('Why 78')}
<div style="font-size: 11px; line-height: 16px; color: #c8c8c8">Grid gap 64 + 14 px left over in the image's column (the image is fixed at 580 in a 594 column).</div>
<div style="display: flex; gap: 6px; flex-wrap: wrap">{cbtn('Make it 64 · image fills its column')}{cbtn('Snap to 72 · 3xl')}</div>
{sep}
{L['lab']('Copy as')}
<div style="display: flex; gap: 6px; margin-top: -3px">{cbtn('Value')}{cbtn('CSS')}{cbtn('Spec note')}{cbtn('Image with redlines')}</div>
</section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', mpop + '\n<!-- ═══════════ TOP BAR v3')
old_btn = f'<button aria-label="Measure · Advanced" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; color: #939393">{icon("sliders", 14)}</button>'
S.rep(old_btn, f'<button aria-label="Measure · Advanced" aria-expanded="true" aria-haspopup="dialog" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; background: #3a3a3a; color: #e8e8e8; box-shadow: 0 0 0 1px #2f80ed">{icon("sliders", 14)}</button>')
