from screen import *
_src = open('/home/claude/ds/layoutadv.py').read()
LA = {}
exec(_src[:_src.index('# ═════ A · ROW')], LA)
L = LA
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')

S = Screen('Daisy · D-20 Properties: Advanced and custom values')
S.remove_h1_overlay()
S.remove_parent_outline()
S.unselect_h1_row()

PUR = '#a371f7'
C1 = (1312 - 64) * 1.1 / 2.1   # 653.7
# ---------------- canvas: Hero grid selected, tracks shown while the popover is open ----------------
hpos = ['left: -5.6px; top: -5.6px', 'left: calc(50% - 4.7px); top: -5.6px', 'right: -5.6px; top: -5.6px', 'right: -5.6px; top: calc(50% - 4.7px)',
        'right: -5.6px; bottom: -5.6px', 'left: calc(50% - 4.7px); bottom: -5.6px', 'left: -5.6px; bottom: -5.6px', 'left: -5.6px; top: calc(50% - 4.7px)']
handles = ''.join(f'<span style="position: absolute; {p}; width: 9.4px; height: 9.4px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>' for p in hpos)
badge = lambda x, t, on=False: f'<span style="position: absolute; left: {x}px; top: -32px; transform: translateX(-50%); height: 21px; padding: 0 7px; display: flex; align-items: center; border-radius: 3px; background: {"#7c4ed8" if on else "#8a5cf0"}; {"box-shadow: 0 0 0 2px #fff, 0 0 0 3.5px #7c4ed8;" if on else ""} color: #fff; font: 500 12px/1 \'Inter\', sans-serif; white-space: nowrap">{t}</span>'
over = f'''
<!-- Hero grid: selected; tracks drawn while Layout · Advanced is open -->
<div aria-hidden="true" style="position: absolute; left: 0; top: 0; width: {C1:.1f}px; bottom: 0; background: rgba(163,113,247,0.07); box-shadow: inset 0 0 0 1.18px rgba(163,113,247,0.6); z-index: 3"></div>
<div aria-hidden="true" style="position: absolute; left: {C1:.1f}px; width: 64px; top: 0; bottom: 0; background: repeating-linear-gradient(45deg, rgba(219,97,162,0.35) 0 2.4px, rgba(219,97,162,0.08) 2.4px 7px); z-index: 3"></div>
<div aria-hidden="true" style="position: absolute; right: 0; top: 0; width: {1312 - C1 - 64:.1f}px; bottom: 0; box-shadow: inset 0 0 0 1.18px rgba(163,113,247,0.6); z-index: 3"></div>
<div aria-hidden="true" style="position: absolute; inset: -1px; border: 1.76px solid #2f80ed; z-index: 4">{handles}
<span style="position: absolute; left: -1.76px; top: calc(100% + 4px); height: 21px; padding: 0 5px; display: flex; align-items: center; background: #246bcb; color: #fff; font: 500 13px/1 'Inter', sans-serif; white-space: nowrap">Box · Hero grid · Grid 2 × 1</span>
{badge(C1 / 2, '1.1fr', True)}{badge(C1 + 64 + (1312 - C1 - 64) / 2, '1fr')}</div>
'''
S.rep('<div style="display: grid; grid-template-columns: 1.1fr 1fr; gap: 64px; align-items: center">',
      '<div style="position: relative; display: grid; grid-template-columns: 1.1fr 1fr; gap: 64px; align-items: center">')
s = S.s
img_open = '<div style="justify-self: end; width: 580px; height: 520px; border-radius: 12px; overflow: hidden; background: #e6dccd">'
a = s.index(img_open); b = s.index('</svg>\n</div>', a) + len('</svg>\n</div>')
S.s = s[:b] + over + s[b:]

# options bar: Select tool (unchanged) but for a box: keep shell's capsule with Hero grid numbers
S.options('64', '72', '1312', 'Fill', '520', 'Fit')
set_tree(S, hero_tree('Hero grid'))

# ---------------- properties ----------------
press = f'<button aria-label="Layout · Advanced" aria-expanded="true" aria-haspopup="dialog" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; background: #3a3a3a; color: #e8e8e8; box-shadow: 0 0 0 1px #2f80ed">{icon("sliders", 14)}</button>'
inline_on = f'<button aria-label="Size · Advanced" aria-expanded="true" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; background: #3a3a3a; color: #e8e8e8">{icon("sliders", 14)}</button>'
ttl = lambda t, btn: f'<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">{t}</span>{btn}</div>'
blk = lambda body: f'<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">{body}</div><div style="height: 1px; background: #303030"></div>'
custom = '<span style="height: 16px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: rgba(227,179,74,0.16); font-size: 10px; color: #e3b34a">custom</span>'
tip = (f'<span role="tooltip" style="position: absolute; left: 20px; bottom: calc(100% + 6px); height: 26px; display: flex; align-items: center; gap: 6px; padding: 0 9px; border-radius: 4px; background: #e8e8e8; color: #1b1b1b; font-size: 11px; white-space: nowrap; box-shadow: 0 6px 16px rgba(0,0,0,0.4); z-index: 5">'
       f'Space between · <span style="font-family: {MONO}">gap</span> · 64px<span style="position: absolute; left: 14px; top: 100%; border: 5px solid transparent; border-top-color: #e8e8e8"></span></span>')
layout = blk(ttl('Layout', press)
             + seg([icon('t-stack', 12) + 'Stack', icon('t-row', 12) + 'Row', icon('t-grid', 12) + 'Grid'], 2)
             + f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">{L["stepper"]("Columns", 2)}{L["stepper"]("Rows", 1)}</div>'
             + f'<div style="position: relative">{tip}' + f(DOT + '<span style="font-size: 11px; color: #e8e8e8; text-decoration: underline dotted #939393; text-underline-offset: 3px">Gap</span><span style="flex: 1">64</span><span style="font-size: 10px; color: #939393">px</span>') + '</div>'
             + '<div style="font-size: 10px; line-height: 14px; color: #939393">Tracks, separate gaps, fill order and areas: Advanced</div>')
size = blk(ttl('Size', inline_on)
           + pair(f('<span style="font-size: 11px; color: #939393; padding-left: 11px">W</span><span style="flex: 1; color: #939393">1312</span>' + tagc('Fill')), f('<span style="font-size: 11px; color: #939393; padding-left: 11px">H</span><span style="flex: 1; color: #939393">520</span>' + tagc('Fit')))
           + L['advdiv']()
           + pair(f('<span style="font-size: 11px; color: #939393">Min W</span><span style="flex: 1; text-align: right; color: #939393">0</span>'), f('<span style="font-size: 11px; color: #939393">Min H</span><span style="flex: 1; text-align: right; color: #939393">0</span>'))
           + f(DOT + f'<span style="font-size: 11px; color: #939393">Max W</span><span style="flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-family: {MONO}; font-size: 11px">clamp(320px, 90vw, 1280px)</span>' + custom)
           + pair(f('<span style="font-size: 11px; color: #939393">Ratio</span><span style="flex: 1; text-align: right; color: #939393">none</span>'), f('<span style="font-size: 11px; color: #939393">Overflow</span><span style="flex: 1; text-align: right; color: #939393">visible</span>')))
other = blk(ttl('Other properties', '')
            + f('<span style="font-family: ' + MONO + '; font-size: 11px; color: #e8e8e8">isolation</span><span style="flex: 1; text-align: right; font-family: ' + MONO + '; font-size: 11px">isolate</span>' + icon('close', 10, '#939393'))
            + '<button style="height: 22px; align-self: flex-start; padding: 0 8px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #a8a8a8">+ Other property</button>')
S.props(panel(header('t-grid', 'Hero grid', 'Box', 'div') + layout + size + other
              + more([mp('Placement', 'In flow'), mp('Spacing', '0'), mp('Fill', 'none'), mp('Border', 'none'), mp('Effects'), mp('Visibility', 'All sizes')])))

# ---------------- Layout · Advanced popover (C-38, Grid) ----------------
plus = lambda n: f'<button aria-label="Add {n}" style="width: 22px; height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 3px; box-shadow: inset 0 0 0 1px #454545; color: #a8a8a8">{icon("plus", 12)}</button>'
pbtn = lambda t, tip_: f'<button title="{tip_}" style="height: 22px; padding: 0 8px; border-radius: 4px; font-size: 11px; background: #2a2a2a; color: #a8a8a8">{t}</button>'
prev = L['preview']('<div style="height: 100%; display: grid; grid-template-columns: 1.1fr 1fr; gap: 10px; align-items: center"><span style="height: 70%; border-radius: 2px; background: #4a6fa5; box-shadow: inset 0 0 0 1px #a9c8f7"></span><span style="height: 100%; border-radius: 2px; background: #5b5b5b"></span></div>', 64)
pop = f'''<!-- POPOVER: Layout · Advanced (C-38) for Hero grid -->
<section role="dialog" aria-label="Layout advanced · Hero grid" style="position: absolute; left: 1282px; top: 136px; width: 328px; box-sizing: border-box; padding: 0 12px 12px; display: flex; flex-direction: column; gap: 9px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); font-variant-numeric: tabular-nums; z-index: 30">
<span aria-hidden="true" style="position: absolute; right: -6px; top: 14px; width: 10px; height: 10px; background: #262626; border-right: 1px solid #454545; border-top: 1px solid #454545; transform: rotate(45deg)"></span>
<div style="height: 40px; margin: 0 -12px; padding: 0 8px 0 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a">
<span style="font-weight: 600">Layout · Advanced</span><span style="flex: 1; font-size: 11px; color: #939393">Hero grid · Grid</span>
<button aria-label="Pin open" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #939393">{icon("keep", 14)}</button>
<button aria-label="Close" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon("close", 14)}</button></div>
{L['lab']('Columns', 'grid-template-columns')}
<div style="display: flex; gap: 4px; align-items: center">{L['chip_track']('1.1fr', True)}{L['chip_track']('1fr')}{plus('column')}</div>
<div style="padding: 8px; display: flex; flex-direction: column; gap: 6px; background: #1f1f1f; border-radius: 4px; box-shadow: inset 0 0 0 1px #3a3a3a">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 11px; color: #e8e8e8">Column 1 · Hero text</span><span style="font-family: {MONO}; font-size: 10px; color: #939393">654 px now</span></div>
{L['seg'](['fr', 'px', 'auto', 'min–max', 'fit'], 0)}
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px">{L['fieldv']('Share', '1.1', 'fr', None, True, True)}{L['fieldv']('Min', '0', 'px')}</div></div>
<div style="display: flex; flex-wrap: wrap; gap: 4px">{pbtn('Equal', 'repeat(2, 1fr)')}{pbtn('Sidebar + main', '240px 1fr')}{pbtn('Auto-fit cards', 'repeat(auto-fit, minmax(200px, 1fr))')}</div>
{L['lab']('Rows', 'grid-template-rows')}
<div style="display: flex; gap: 4px; align-items: center">{L['chip_track']('auto')}{plus('row')}</div>
{L['lab']('Gaps', 'row-gap · column-gap')}
{L['pair'](L['fieldv']('Row', '0', 'px'), L['fieldv']('Column', '64', 'px', None, True), False)}
{L['lab']('Items inside cells', 'justify-items · align-items')}
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px">{L['iconseg'](['start', 'center', 'end', 'stretch'], 3, 'cross', ['Start', 'Centre', 'End', 'Stretch'])}{L['iconseg'](['start', 'center', 'end', 'stretch'], 1, 'cross', ['Start', 'Centre', 'End', 'Stretch'])}</div>
<div style="display: flex; gap: 6px; font-family: {MONO}; font-size: 10px; color: #939393"><span style="flex: 1">justify-items: stretch</span><span style="flex: 1">align-items: center</span></div>
<div style="display: flex; align-items: center; justify-content: space-between">{L['lab']('Fill order', 'grid-auto-flow')}<span style="font-size: 11px; color: #a8a8a8">Row</span></div>
{prev}
{L['css_line']('display: grid;\ngrid-template-columns: 1.1fr 1fr;\ncolumn-gap: 64px; align-items: center;')}
</section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', pop + '\n<!-- ═══════════ TOP BAR v3')

S.status(['Page', 'Section · Hero', 'Box · Hero grid'], 'Layout · Advanced is open · tracks show on the canvas while it is open · Esc closes it', 'x 1180 &#160;y 410')
S.save('D20-Advanced.dc.html')
print('ok')
