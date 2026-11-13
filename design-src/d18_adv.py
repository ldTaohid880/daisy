# Place · Advanced popover, anchored to Properties › What gets created
sw = lambda on, label: f'<button role="switch" aria-checked="{str(on).lower()}" aria-label="{label}" style="position: relative; width: 28px; height: 16px; border-radius: 8px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {"#fff" if on else "#a8a8a8"}"></span></button>'
swrow = lambda l, on, label: f'<div style="display: flex; align-items: center; justify-content: space-between">{l}{sw(on, label)}</div>'
note = lambda t: f'<div style="margin-top: -4px; font-size: 10px; line-height: 14px; color: #939393">{t}</div>'
def pos_pick():
    cell = lambda t, on=False: f'<button aria-pressed="{str(on).lower()}" style="height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 3px; font-size: 11px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if on else "color: #939393;"}">{t}</button>'
    return (f'<div style="display: grid; grid-template-columns: 1fr 1.2fr 1fr; gap: 6px; align-items: stretch">'
            f'<div style="display: grid; gap: 2px; padding: 2px; background: #262626; border-radius: 4px">{cell("Before")}</div>'
            f'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2px; padding: 2px; background: #262626; border-radius: 4px; box-shadow: inset 0 0 0 1px #3a3a3a">{cell("Inside ↑")}{cell("Inside ↓")}</div>'
            f'<div style="display: grid; gap: 2px; padding: 2px; background: #262626; border-radius: 4px">{cell("After", True)}</div></div>')
adv_pop = f'''<!-- POPOVER: Place · Advanced -->
<section role="dialog" aria-label="Place advanced · Bulleted list" style="position: absolute; left: 1282px; top: 128px; width: 328px; box-sizing: border-box; padding: 0 12px 12px; display: flex; flex-direction: column; gap: 9px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); font-variant-numeric: tabular-nums; z-index: 30">
<span aria-hidden="true" style="position: absolute; right: -6px; top: 16px; width: 10px; height: 10px; background: #262626; border-right: 1px solid #454545; border-top: 1px solid #454545; transform: rotate(45deg)"></span>
<div style="height: 40px; margin: 0 -12px; padding: 0 8px 0 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a">
<span style="font-weight: 600">Place · Advanced</span><span style="flex: 1; font-size: 11px; color: #939393">Bulleted list</span>
<button aria-label="Pin open" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #939393">{icon("keep", 14)}</button>
<button aria-label="Close" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon("close", 14)}</button></div>
{L['lab']('Tag')}
{L['seg']([('<span style="font-family: ' + MONO + '">ul</span>', 'Unordered list'), ('<span style="font-family: ' + MONO + '">ol</span>', 'Numbered list'), ('<span style="font-family: ' + MONO + '">menu</span>', 'Toolbar of commands')], 0)}
{note('Only tags that mean the same kind of thing are offered.')}
<div style="display: flex; align-items: center; justify-content: space-between">{L['lab']('Where it goes')}<span style="font-size: 10px; color: #939393">relative to “Riverside Works, Unit 4”</span></div>
{pos_pick()}
{note('The pointer picks this on the canvas · Tab cycles it from the keyboard.')}
<div style="height: 1px; background: #333333"></div>
{swrow(L['lab']('Wrap the selection'), False, 'Wrap the selection')}
{note('Places the list around what is selected instead of beside it. Off: nothing is selected.')}
{swrow(L['lab']('Place into every match'), False, 'Place into every match')}
{note('Adds it to every container like Footer at once · 1 match on this page.')}
<div style="height: 1px; background: #333333"></div>
{L['lab']('Accessible name', 'aria-label')}
<label style="height: 24px; display: flex; align-items: center; padding: 0 6px; background: #2a2a2a; border-radius: 2px; color: #939393">e.g. Opening hours</label>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px">{L['fieldv']('id', '—')}{L['fieldv']('class', 'footer-list')}</div>
<button style="height: 22px; align-self: flex-start; padding: 0 8px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #a8a8a8">+ Attribute</button>
{L['lab']('Style')}
{L['seg'](['From Halden', 'Bare HTML'], 0)}
<div style="display: flex; align-items: flex-start; gap: 8px; padding-top: 10px; border-top: 1px solid #333333">
<code style="flex: 1; min-width: 0; font-family: {MONO}; font-size: 11px; line-height: 16px; color: #939393">&lt;ul class="footer-list"&gt; … &lt;/ul&gt;</code>
<button style="height: 22px; padding: 0 8px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #c8c8c8; flex: none">Save as preset</button></div>
</section>'''
S.rep('<!-- ═══════════ TOP BAR v3', adv_pop + '\n<!-- ═══════════ TOP BAR v3')
# group title: Advanced pressed
old_btn = f'<button aria-label="What gets created · Advanced" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; color: #939393">{icon("sliders", 14)}</button>'
S.rep(old_btn, f'<button aria-label="What gets created · Advanced" aria-expanded="true" aria-haspopup="dialog" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; background: #3a3a3a; color: #e8e8e8; box-shadow: 0 0 0 1px #2f80ed">{icon("sliders", 14)}</button>')
