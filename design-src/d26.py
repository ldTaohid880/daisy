from screen import *
_src = open('/home/claude/ds/layoutadv.py').read()
LA = {}
exec(_src[:_src.index('# ═════ A · ROW')], LA)
L = LA

S = Screen('Daisy · D-26 Assets panel')
S.remove_h1_overlay()
S.remove_parent_outline()
S.unselect_h1_row()
scroll(S, 640)
add_footer(S)

# thumbnails (shared look with D-17)
bowl = lambda c: f'<span style="position: absolute; left: 22%; right: 22%; top: 40%; height: 34%; border-radius: 0 0 50% 50% / 0 0 100% 100%; background: {c}"></span>'
mug = '<span style="position: absolute; left: 34%; width: 26%; top: 30%; height: 46%; border-radius: 2px 2px 6px 6px; background: #1d1a16"></span><span style="position: absolute; left: 58%; width: 12%; top: 40%; height: 20%; border: 3px solid #1d1a16; border-left: 0; border-radius: 0 8px 8px 0"></span>'
plates = '<span style="position: absolute; left: 18%; right: 18%; top: 34%; height: 30%; border-radius: 50%; background: #efe7da; box-shadow: 0 5px 0 #d8cbb8, 0 10px 0 #c9bba8"></span>'
wheel = '<span style="position: absolute; left: 25%; right: 25%; top: 52%; height: 14%; border-radius: 50%; background: #6b5a48"></span><span style="position: absolute; left: 38%; right: 38%; top: 30%; height: 26%; border-radius: 40% 40% 10% 10%; background: #a88a6e"></span>'
tiles = ''.join(f'<span style="position: absolute; left: {8 + (i % 4) * 22}%; top: {18 + (i // 4) * 34}%; width: 18%; height: 28%; border-radius: 2px; background: {c}"></span>' for i, c in enumerate(['#b5532d', '#6b7d5a', '#1d1a16', '#d8cbb8', '#8a6e9e', '#c9a24a', '#4a6fa5', '#efe7da']))
river = '<span style="position: absolute; left: 0; right: 0; top: 58%; bottom: 0; background: #7c95a8"></span><span style="position: absolute; left: 0; right: 0; top: 46%; height: 14%; background: #6b7d5a"></span>'
def thumb(name, bg, shape, use, on=False, warn=False, drag=False):
    chip = f'<span style="position: absolute; left: 4px; bottom: 4px; height: 16px; padding: 0 5px; display: flex; align-items: center; border-radius: 8px; background: rgba(29,26,22,0.82); color: {"#e8e8e8" if use != "unused" else "#c8c8c8"}; font-size: 10px">{use}</span>'
    w = f'<span title="No saved description" style="position: absolute; right: 4px; top: 4px; width: 16px; height: 16px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: rgba(29,26,22,0.82)">{icon("warning", 10, "#e3b34a", 1.25)}</span>' if warn else ''
    return (f'<button style="display: flex; flex-direction: column; gap: 4px; text-align: left; min-width: 0; {"opacity: 0.45;" if drag else ""}">'
            f'<span style="position: relative; height: 82px; border-radius: 3px; background: {bg}; overflow: hidden; {"box-shadow: 0 0 0 2px #2f80ed;" if on else ""}">{shape}{chip}{w}</span>'
            f'<span style="font-size: 11px; color: #c8c8c8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{name}</span></button>')
grid = (thumb('tide-bowl.jpg', '#e6dccd', bowl('#6b7d5a'), 'used 1×') + thumb('ember-mug.jpg', '#d8c6b0', mug, 'used 1×', on=True, drag=True)
        + thumb('linen-plates.jpg', '#e9e1d4', plates, 'used 1×') + thumb('studio-wheel.jpg', '#cbb79f', wheel, 'used 2×')
        + thumb('glaze-tests.jpg', '#efe7da', tiles, 'unused', warn=True) + thumb('river-view.jpg', '#c9d4da', river, 'unused'))
panel_html = f'''<div style="padding: 8px 12px 6px; display: flex; gap: 6px">
<label style="flex: 1; height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px; box-sizing: border-box; background: #2a2a2a; border-radius: 2px">{icon('search', 12, '#939393', 1.75)}<span style="color: #939393">Search assets</span></label>
<button aria-label="Upload" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: #2a2a2a; color: #c8c8c8">{icon('upload', 13)}</button></div>
<div style="padding: 0 12px 8px">{L['seg'](['Images 6', 'Icons 2', 'Video 1', 'Fonts 2'], 0)}</div>
<div style="padding: 0 12px; display: flex; align-items: center; justify-content: space-between; font-size: 10px; color: #939393"><span>Recently added ▾</span><span>4.1 MB</span></div>
<div style="padding: 8px 12px; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px 8px">{grid}</div>
<div style="margin: 4px 12px; padding: 8px 10px; border-radius: 4px; border: 1px dashed #454545; font-size: 11px; line-height: 16px; color: #939393; text-align: center">Drop files here to upload · or paste an image</div>
<div style="padding: 6px 12px; font-size: 10px; line-height: 14px; color: #939393">Drag onto an image to replace it · onto empty space to place a new one · ⚠ = no saved description</div>
'''
# switch dock to the Assets tab
S.rep('<button role="tab" aria-selected="true" style="position: relative; font-weight: 500; color: #e8e8e8">Layers<span style="position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: #2f80ed"></span></button>',
      '<button role="tab" aria-selected="false" style="font-weight: 500; color: #a8a8a8">Layers</button>')
S.rep('<button role="tab" aria-selected="false" style="font-weight: 500; color: #a8a8a8">Assets</button>',
      '<button role="tab" aria-selected="true" style="position: relative; font-weight: 500; color: #e8e8e8">Assets<span style="position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: #2f80ed"></span></button>')
S.cut('<div style="display: flex; gap: 4px; padding: 8px 12px 4px">', '</aside>', panel_html)

# ---------------- canvas: replace highlight on Card 1's image ----------------
old = '<div style="aspect-ratio: 4 / 3; border-radius: 8px; background: #d8cbb8"></div>'
S.rep(old, f'''<div style="position: relative; aspect-ratio: 4 / 3; border-radius: 8px; background: #d8cbb8">
<div aria-hidden="true" style="position: absolute; inset: 0; border-radius: 8px; background: rgba(47,128,237,0.22); box-shadow: inset 0 0 0 2.35px #2f80ed; display: flex; align-items: center; justify-content: center">
<span style="height: 30px; padding: 0 12px; display: flex; align-items: center; gap: 8px; border-radius: 15px; background: #246bcb; color: #fff; font: 500 14px/1 'Inter', sans-serif; box-shadow: 0 4px 12px rgba(0,0,0,0.25)">{icon('swap', 14, '#fff')}Replace image</span></div>
<span aria-hidden="true" style="position: absolute; left: -1.76px; bottom: calc(100% + 3px); height: 21px; padding: 0 5px; display: flex; align-items: center; background: #246bcb; color: #fff; font: 500 13px/1 'Inter', sans-serif; white-space: nowrap">Image · Tide bowl photo</span></div>''')
# drag ghost (thumbnail following the pointer)
ghost = f'''<!-- drag ghost from Assets -->
<div aria-hidden="true" style="position: absolute; left: 640px; top: 600px; width: 96px; padding: 3px; border-radius: 4px; background: #262626; box-shadow: 0 10px 24px rgba(0,0,0,0.5); transform: rotate(-3deg); z-index: 40">
<span style="position: relative; display: block; height: 64px; border-radius: 3px; background: #d8c6b0; overflow: hidden">{mug}</span>
<span style="display: block; padding: 3px 2px 1px; font-size: 10px; color: #e8e8e8">ember-mug.jpg</span></div>
<svg aria-hidden="true" width="18" height="18" viewBox="0 0 16 16" style="position: absolute; left: 632px; top: 592px; z-index: 41"><path d="M3 2l9.5 6.5-4.2 1 2.4 4.4-1.8 1-2.4-4.4-3.5 2.7z" fill="#fff" stroke="#1d1a16" stroke-width="1.1" stroke-linejoin="round"></path></svg>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', ghost + '\n<!-- ═══════════ TOP BAR v3')

# ---------------- properties: what the drop will change ----------------
S.options('16', '16', '384', 'Fill', '288', '4:3')
cmp = lambda bg, shape, name: f'<div style="flex: 1; display: flex; flex-direction: column; gap: 4px"><span style="position: relative; height: 60px; border-radius: 3px; background: {bg}; overflow: hidden">{shape}</span><span style="font-size: 10px; color: #a8a8a8">{name}</span></div>'
drop = (f'<div style="display: flex; align-items: center; gap: 8px">{cmp("#e6dccd", bowl("#6b7d5a"), "Now · tide-bowl.jpg")}{icon("chev-right", 14, "#939393", 1.75)}{cmp("#d8c6b0", mug, "After · ember-mug.jpg")}</div>'
        + f'<div style="display: flex; gap: 6px; font-size: 11px; line-height: 16px"><span style="margin-top: 2px">{icon("check", 12, "#3fb950", 2)}</span><span style="color: #c8c8c8">Description comes too: “Ember mug in matte black glaze on a linen cloth”</span></div>'
        + '<div style="font-size: 11px; line-height: 16px; color: #939393">Size, fit and corners stay as they are · Alt+drop places it as a new image instead</div>')
S.props(panel(header('t-image', 'Tide bowl photo', 'Image', 'img') + group('On drop', drop)
              + group('Size', pair(f('<span style="font-size: 11px; color: #939393; padding-left: 11px">W</span><span style="flex: 1; color: #939393">384</span>' + tagc('Fill')), f('<span style="font-size: 11px; color: #939393; padding-left: 11px">H</span><span style="flex: 1; color: #939393">288</span>' + tagc('4:3'))))
              + more([mp('Image', 'tide-bowl.jpg · cover'), mp('Border', 'radius 8'), mp('Effects'), mp('Accessibility', 'described')])))
S.status(['Page', 'This season', 'Card grid', 'Card 1', 'Image · Tide bowl photo'], 'Drop to replace this image · Alt+drop to place a new one beside it · Esc cancels', 'x 470 &#160;y 1040')
S.save('D26-Assets.dc.html')
print('ok')
