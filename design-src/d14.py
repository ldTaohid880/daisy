from screen import *
_src = open('/home/claude/ds/layoutadv.py').read()
LA = {}
exec(_src[:_src.index('# ═════ A · ROW')], LA)

S = Screen('Daisy · D-14 Layout tool on the card grid')
S.remove_h1_overlay()
S.remove_parent_outline()
set_tool(S, 'Layout (G)')
scroll(S, 640)
add_footer(S)

PUR, PURF, PINK = '#1a9284', '#127a70', '#db61a2'
CW, GAP = (1312 - 64) / 3, 32
grid_open = '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 32px">'
badge = lambda x, t: f'<span style="position: absolute; left: {x}px; top: -34px; transform: translateX(-50%); height: 22px; padding: 0 7px; display: flex; align-items: center; border-radius: 3px; background: {PURF}; color: #fff; font: 500 12px/1 \'Inter\', sans-serif; white-space: nowrap">{t}</span>'
hatch = lambda op: f'repeating-linear-gradient(45deg, rgba(219,97,162,{op}) 0 2.4px, rgba(219,97,162,0.12) 2.4px 7px)'
over = f'<div aria-hidden="true" style="position: absolute; inset: -1px; border: 1.18px solid {PUR}; pointer-events: none; z-index: 3"></div>'
for i in range(3):
    over += badge(CW * i + CW / 2, '1fr')
over += f'<span aria-hidden="true" style="position: absolute; left: calc(100% + 10px); top: -34px; width: 22px; height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: #ffffff; box-shadow: inset 0 0 0 1.18px {PUR}; color: #127a70; font: 600 15px/1 \'Inter\', sans-serif">+</span>'
for i in (1, 2):
    x = CW * i + GAP * (i - 1)
    dragging = i == 1
    over += (f'<div aria-hidden="true" style="position: absolute; left: {x}px; top: 0; bottom: 0; width: {GAP}px; background: {hatch(0.85 if dragging else 0.55)}; {"box-shadow: 0 0 0 1.18px " + PINK + ";" if dragging else ""} z-index: 3"></div>'
             f'<div aria-hidden="true" style="position: absolute; left: {x + GAP / 2}px; top: -1px; bottom: -1px; border-left: 1.18px dashed {PUR}; z-index: 3"></div>')
over += f'<span aria-hidden="true" style="position: absolute; left: {CW + GAP / 2}px; top: 46%; transform: translateX(-50%); height: 22px; padding: 0 8px; display: flex; align-items: center; border-radius: 11px; background: #b93d82; color: #fff; font: 500 12px/1 \'Inter\', sans-serif; z-index: 4">32</span>'
over += f'<svg aria-hidden="true" width="30" height="30" viewBox="0 0 20 20" style="position: absolute; left: {CW + GAP / 2 - 15}px; top: 56%; overflow: visible; z-index: 5"><path d="M2 10l4-4v2.5h8V6l4 4-4 4v-2.5H6V14z" fill="#1d1a16" stroke="#ffffff" stroke-width="1" stroke-linejoin="round"></path></svg>'
over += f'<span aria-hidden="true" style="position: absolute; left: -1px; top: calc(100% + 6px); height: 21px; padding: 0 5px; display: flex; align-items: center; background: #127a70; color: #fff; font: 500 13px/1 \'Inter\', sans-serif; white-space: nowrap; z-index: 4">Grid 3 × 1 · Card grid</span>'
S.rep(grid_open, '<div style="position: relative; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 32px">' + over)
assert contrast('#ffffff', '#b93d82') >= 4.5 and contrast('#ffffff', '#127a70') >= 4.5

# inset: the same tool on a Row container
S.rep('<!-- vertical scroll indicator -->', f'''<!-- INSET: Layout tool on a Row -->
<div aria-label="Inset: Layout tool on a Row" style="position: absolute; left: 56px; top: 700px; width: 440px; padding: 12px; box-sizing: border-box; background: #1f1f1f; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 8px 24px rgba(0,0,0,0.45); z-index: 10">
<div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 11px"><span style="font-weight: 600">Inset · same tool on a Row</span><span style="color: #939393">Hero buttons</span></div>
<div style="position: relative; height: 112px; padding: 24px 16px 16px; box-sizing: border-box; background: #f6f1ea; border-radius: 2px">
<div style="position: relative; height: 64px; display: flex; align-items: center; gap: 16px; padding: 0 10px; box-shadow: inset 0 0 0 1px {PUR}">
<span style="position: absolute; left: 4px; top: -20px; display: flex; align-items: center; gap: 4px; color: #127a70; font-size: 10px">{icon('chev-right', 14, '#127a70', 2)}Row → · click to flip</span>
<span style="position: relative; flex: none; width: 128px; height: 36px; border-radius: 18px; background: #b5532d"><span style="position: absolute; left: 50%; bottom: -14px; transform: translateX(-50%); width: 16px; height: 8px; border-radius: 4px; background: #c8c8c8" title="grow off"></span></span>
<span style="width: 16px; flex: none; align-self: stretch; background: {hatch(0.55)}"></span>
<span style="position: relative; flex: 1; height: 28px; border-radius: 3px; background: #e7d9c7; display: flex; align-items: center; justify-content: center; font-size: 11px; color: #4a443c">Our process →<span style="position: absolute; left: 50%; bottom: -18px; transform: translateX(-50%); width: 16px; height: 8px; border-radius: 4px; background: #2f80ed" title="grow on"></span></span>
</div></div>
<div style="margin-top: 8px; font-size: 11px; line-height: 16px; color: #939393">Direction arrow at the start · grow toggles under each child (blue = grows to fill) · hatched bar = space between.</div>
</div>
<!-- vertical scroll indicator -->''')

tog = lambda t, on: f'<button aria-pressed="{str(on).lower()}" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; white-space: nowrap; {"background: rgba(26,146,132,0.18); color: #9fe5dc;" if on else "color: #a8a8a8;"}">{t}</button>'
lab = lambda t: f'<span style="font-size: 11px; color: #939393; padding: 0 4px 0 8px; white-space: nowrap">{t}</span>'
opts = (cap(lab('Show') + tog('Tracks', True) + tog('Gaps', True) + tog('Space inside', False) + tog('Track sizes', True))
        + cap(capfield('Drag steps', '8', 'px') + capdiv() + capfield('Alt+drag', 'all gaps'))
        + cap(f'<button style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; color: #c8c8c8; white-space: nowrap">{icon("t-grid", 12)}Make columns equal</button>')
        + '<span style="font-size: 11px; color: #939393; white-space: nowrap; padding-left: 4px">Layout values: in Properties</span>')
options_left(S, opts)

set_tree(S, season_tree(sel=('Card grid',)))
chip = lambda v: f'<button style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 6px 0 8px; border-radius: 3px; background: rgba(26,146,132,0.14); font-family: {MONO}; font-size: 11px; color: #9fe5dc">{v}{icon("chev-down", 10, "#6fd3c6", 1.75)}</button>'
lay_title = f'''<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">Layout</span>
<button aria-label="Layout · Advanced" aria-expanded="true" aria-haspopup="dialog" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; background: #3a3a3a; color: #e8e8e8; box-shadow: 0 0 0 1px #2f80ed">{icon("sliders", 14)}</button></div>'''
lay = f'''<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">{lay_title}
{seg([icon('t-stack', 12) + 'Stack', icon('t-row', 12) + 'Row', icon('t-grid', 12) + 'Grid'], 2)}
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">{LA['stepper']('Columns', 3)}{LA['stepper']('Rows', 1)}</div>
{f(DOT + '<span style="font-size: 11px; color: #939393">Gap</span><span style="flex: 1">32</span><span style="font-size: 10px; color: #939393">px</span>', 'box-shadow: inset 0 0 0 1px #2f80ed')}
<div style="font-size: 10px; line-height: 14px; color: #939393">Tracks, separate gaps, fill order and areas: Advanced</div></div>
<div style="height: 1px; background: #303030"></div>'''
S.props(panel(header('t-grid', 'Card grid', 'Box', 'div') + lay
              + group('Size', pair(f('<span style="font-size: 11px; color: #939393; padding-left: 11px">W</span><span style="flex: 1; color: #939393">1312</span>' + tagc('Fill')), f('<span style="font-size: 11px; color: #939393; padding-left: 11px">H</span><span style="flex: 1; color: #939393">380</span>' + tagc('Fit'))))
              + more([mp('Placement', 'In flow'), mp('Spacing', '0'), mp('Fill', 'none'), mp('Border', 'none'), mp('Effects'), mp('Visibility', 'All sizes'), mp('Accessibility'), mp('Attributes &amp; Custom CSS')])))

# 5. the Layout Advanced popover (C-38, Grid), anchored to the Advanced button
L = LA
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
plus = lambda n: f'<button aria-label="Add {n}" style="width: 22px; height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 3px; box-shadow: inset 0 0 0 1px #454545; color: #a8a8a8">{icon("plus", 12)}</button>'
pbtn = lambda t, tip, on=False: f'<button title="{tip}" aria-pressed="{str(on).lower()}" style="height: 22px; padding: 0 8px; border-radius: 4px; font-size: 11px; {"background: rgba(47,128,237,0.18); color: #a9c8f7; box-shadow: inset 0 0 0 1px #2f80ed;" if on else "background: #2a2a2a; color: #a8a8a8;"}">{t}</button>'
cellp = lambda: '<span style="border-radius: 2px; background: #5b5b5b"></span>'
prev = L['preview'](f'''<div style="height: 100%; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px">
<span style="border-radius: 2px; background: #4a6fa5; box-shadow: inset 0 0 0 1px #a9c8f7"></span>{cellp()}{cellp()}</div>''', 64)
pop = f'''<!-- POPOVER: Layout · Advanced (C-38, Grid) anchored to Properties › Layout -->
<section role="dialog" aria-label="Layout advanced · Card grid" style="position: absolute; left: 1282px; top: 136px; width: 328px; box-sizing: border-box; padding: 0 12px 12px; display: flex; flex-direction: column; gap: 9px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); font-variant-numeric: tabular-nums; z-index: 30">
<span aria-hidden="true" style="position: absolute; right: -6px; top: 14px; width: 10px; height: 10px; background: #262626; border-right: 1px solid #454545; border-top: 1px solid #454545; transform: rotate(45deg)"></span>
<div style="height: 40px; margin: 0 -12px; padding: 0 8px 0 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a">
<span style="font-weight: 600">Layout · Advanced</span><span style="flex: 1; font-size: 11px; color: #939393">Card grid · Grid</span>
<button aria-label="Pin open" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #939393">{icon("keep", 14)}</button>
<button aria-label="Close" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon("close", 14)}</button></div>
{L['lab']('Columns', 'grid-template-columns')}
<div style="display: flex; flex-wrap: wrap; gap: 4px; align-items: center">{L['chip_track']('1fr', True)}{L['chip_track']('1fr')}{L['chip_track']('1fr')}{plus('column')}</div>
<div style="padding: 8px; display: flex; flex-direction: column; gap: 6px; background: #1f1f1f; border-radius: 4px; box-shadow: inset 0 0 0 1px #3a3a3a">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 11px; color: #e8e8e8">Column 1 · Tide bowl</span><span style="font-family: {MONO}; font-size: 10px; color: #939393">track</span></div>
{L['seg'](['fr', 'px', 'auto', 'min–max', 'fit'], 0)}
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px">{L['fieldv']('Share', '1', 'fr', None, False, True)}{L['fieldv']('Min', '0', 'px')}</div></div>
<div style="display: flex; flex-wrap: wrap; gap: 4px">{pbtn('Equal', 'repeat(3, 1fr)', True)}{pbtn('Sidebar + main', '240px 1fr')}{pbtn('Auto-fit cards', 'repeat(auto-fit, minmax(200px, 1fr))')}{pbtn('12 columns', 'repeat(12, 1fr)')}</div>
{L['lab']('Rows', 'grid-template-rows')}
<div style="display: flex; gap: 4px; align-items: center">{L['chip_track']('auto')}{plus('row')}</div>
{L['lab']('Gaps', 'row-gap · column-gap')}
{L['pair'](L['fieldv']('Row', '32', 'px', None, True), L['fieldv']('Column', '32', 'px', None, True, True), True)}
<div style="margin-top: -4px; font-size: 10px; color: #6fd3c6">Column gap follows your drag on the canvas</div>
{L['lab']('Fill order', 'grid-auto-flow')}
{L['seg'](['Row', 'Column', 'Row · dense', 'Col · dense'], 0)}
{L['lab']('Items inside cells', 'justify-items · align-items')}
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px">{L['iconseg'](['start', 'center', 'end', 'stretch'], 3, 'cross', ['Start', 'Centre', 'End', 'Stretch'])}{L['iconseg'](['start', 'center', 'end', 'stretch'], 3, 'cross', ['Start', 'Centre', 'End', 'Stretch'])}</div>
<div style="display: flex; align-items: center; justify-content: space-between">{L['lab']('Named areas', 'grid-template-areas')}<button role="switch" aria-checked="false" aria-label="Named areas" style="position: relative; width: 28px; height: 16px; border-radius: 8px; background: #454545"><span style="position: absolute; left: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: #a8a8a8"></span></button></div>
{prev}
{L['css_line']('display: grid;\ngrid-template-columns: repeat(3, 1fr);\ngap: 32px;')}
</section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', pop + '\n<!-- ═══════════ TOP BAR v3')
S.status(['Page', 'Section · This season', 'Box · Card grid'], 'Drag a gap bar to change the space between · drag a track line to resize columns · + adds a column · Alt+drag sets every gap', 'x 512 &#160;y 1140')
S.save('D14-LayoutTool.dc.html')
print('ok')
