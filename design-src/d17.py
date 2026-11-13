from screen import *
_src = open('/home/claude/ds/layoutadv.py').read()
LA = {}
exec(_src[:_src.index('# ═════ A · ROW')], LA)
L = LA

S = Screen('Daisy · D-17 Media placed, describe-image prompt, Link popover')
S.remove_h1_overlay()
S.remove_parent_outline()
set_tool(S, 'Media (I)')
scroll(S, 640)
add_footer(S)

# Card 2 gets a freshly placed image: placeholder + selection
old = '<div style="aspect-ratio: 4 / 3; border-radius: 8px; background: #cfb9a3"></div>'
hpos = ['left: -5.6px; top: -5.6px', 'left: calc(50% - 4.7px); top: -5.6px', 'right: -5.6px; top: -5.6px', 'right: -5.6px; top: calc(50% - 4.7px)',
        'right: -5.6px; bottom: -5.6px', 'left: calc(50% - 4.7px); bottom: -5.6px', 'left: -5.6px; bottom: -5.6px', 'left: -5.6px; top: calc(50% - 4.7px)']
handles = ''.join(f'<span style="position: absolute; {p}; width: 9.4px; height: 9.4px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>' for p in hpos)
handles += ''.join(f'<span style="position: absolute; {p}; width: 7px; height: 7px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 50%"></span>' for p in ['left: 10px; top: 10px', 'right: 10px; top: 10px', 'right: 10px; bottom: 10px', 'left: 10px; bottom: 10px'])
new = (f'<div style="position: relative; aspect-ratio: 4 / 3; border-radius: 8px; background: #d9d9d9; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; color: #6b6b6b">'
       f'{icon("t-image", 48, "#8a8a8a", 1.25)}<span style="font-size: 14px">Drop a file here · or pick a source in Properties</span>'
       f'<div aria-hidden="true" style="position: absolute; inset: -1px; border: 1.76px solid #2f80ed; pointer-events: none">'
       f'<span style="position: absolute; left: -1.76px; bottom: calc(100% + 2px); height: 21px; padding: 0 5px; display: flex; align-items: center; background: #2f80ed; box-shadow: 0 0 0 3px rgba(47,128,237,0.35); color: #fff; font: 500 13px/1 \'Inter\', sans-serif">Image · img</span>{handles}</div></div>')
S.rep(old, new)

# INSET: Link popover over "Our process →"
FLOAT = 'background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 8px 24px rgba(0,0,0,0.45);'
opt = lambda t, on=False, hv=False: f'<button style="width: 100%; height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 8px; box-sizing: border-box; border-radius: 3px; {"background: #323232;" if hv else ""}"><span style="width: 12px">{icon("check", 12) if on else ""}</span>{icon("t-section", 14, "#a8a8a8")}<span style="flex: 1; text-align: left">{t}</span><span style="font-family: {MONO}; font-size: 11px; color: #939393">#{t.lower().replace(" ", "-")}</span></button>'
inset = f'''<!-- INSET: Link tool popover -->
<div aria-label="Inset: Link popover" style="position: absolute; left: 56px; top: 290px; width: 420px; padding: 12px; box-sizing: border-box; background: #1f1f1f; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 8px 24px rgba(0,0,0,0.45); z-index: 10">
<div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 11px"><span style="font-weight: 600">Inset · Link tool on “Our process →”</span><span style="color: #939393">Ctrl+K while editing text</span></div>
<div style="position: relative; height: 330px; padding: 20px 16px; box-sizing: border-box; background: #f6f1ea; border-radius: 2px; color: #1d1a16">
<div style="display: flex; align-items: center; justify-content: flex-end; gap: 20px"><span style="padding: 10px 20px; border-radius: 999px; background: #b5532d; color: #fff; font-size: 14px; font-weight: 500">Shop the collection</span>
<span style="position: relative; font-size: 14px; font-weight: 500">Our process →<span aria-hidden="true" style="position: absolute; inset: -4px -6px; border: 1px solid #2f80ed"></span></span></div>
<div role="dialog" aria-label="Link" style="position: absolute; left: 12px; top: 64px; width: 360px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px; {FLOAT} color: #e8e8e8; font-size: 12px">
<div style="display: flex; justify-content: space-between; align-items: center"><span style="font-weight: 600">Where should this go?</span><button aria-label="Remove link" style="font-size: 11px; color: #a8a8a8">Remove</button></div>
<div role="group" style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #1f1f1f; border-radius: 4px; font-size: 11px">
<button style="height: 22px; border-radius: 3px; color: #939393">Web</button><button aria-pressed="true" style="height: 22px; border-radius: 3px; background: #3a3a3a; font-weight: 500">Section</button><button style="height: 22px; border-radius: 3px; color: #939393">Email</button><button style="height: 22px; border-radius: 3px; color: #939393">Phone</button><button style="height: 22px; border-radius: 3px; color: #939393">File</button></div>
<div style="padding: 4px; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #2f80ed">{opt('Hero')}{opt('This season', True, True)}{opt('Footer')}</div>
<label style="display: flex; align-items: center; gap: 8px; font-size: 11px; color: #a8a8a8"><span style="width: 14px; height: 14px; box-sizing: border-box; border-radius: 3px; box-shadow: inset 0 0 0 1px #8a8a8a"></span>Open in new tab</label>
<div style="display: flex; justify-content: space-between; align-items: center; padding-top: 8px; border-top: 1px solid #333333"><code style="font-family: {MONO}; font-size: 11px; color: #939393">href="#this-season"</code><button style="height: 24px; padding: 0 12px; border-radius: 4px; background: #246bcb; color: #fff; font-weight: 500">Done</button></div>
</div></div></div>'''
S.rep('<!-- vertical scroll indicator -->', inset + '\n<!-- vertical scroll indicator -->')

tog = lambda t, on: f'<button aria-pressed="{str(on).lower()}" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; white-space: nowrap; {"background: rgba(47,128,237,0.18); color: #a9c8f7;" if on else "color: #a8a8a8;"}">{t}</button>'
olab = lambda t: f'<span style="font-size: 11px; color: #939393; padding: 0 4px 0 8px; white-space: nowrap">{t}</span>'
opts = (cap(olab('New media') + tog('Ask for a description', True) + tog('Load when scrolled to', True))
        + cap(olab('Uploads') + tog('Optimise · WebP', True) + tog('Max 2560 px', True))
        + cap(tog('Keep tool', False))
        + '<span style="font-size: 11px; color: #939393; white-space: nowrap; padding-left: 4px">Source, fit and description: in Properties</span>')
options_left(S, opts)

set_tree(S, season_tree(extra=()) if False else [r if r[3] != 'Card 2' else (32, 'open', 't-stack', 'Card 2', 'div', False, (14, 26), '') for r in season_tree()])
s = S.s
k = s.index('>Card 2</span>'); end = s.index('</div>', k) + 6
row = tree_rows([(44, None, 't-image', 'Image', 'img', True, (14, 26, 38), icon('warning', 12, '#d29922', 1.25, 'Needs a description')), (44, None, 't-para', '“Ember mug”', 'p', False, (14, 26, 38), ''), (44, None, 't-para', '“€26”', 'p', False, (14, 26, 38), '')])
row = row[row.index('<div role="treeitem"'):row.rindex('</div>\n</div>')] + '</div>'
S.s = s[:end] + row + s[end:]

img_title = f'''<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">Image</span>{adv('Image')}</div>'''
src = f'''<div role="group" aria-label="Source" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #262626; border-radius: 4px; font-size: 11px">
<button style="height: 22px; display: flex; align-items: center; justify-content: center; gap: 6px; border-radius: 3px; color: #939393">{icon('upload', 12)}Upload</button>
<button aria-pressed="true" aria-expanded="true" aria-haspopup="dialog" style="height: 22px; display: flex; align-items: center; justify-content: center; gap: 4px; border-radius: 3px; background: #3a3a3a; color: #e8e8e8; font-weight: 500; box-shadow: 0 0 0 1px #2f80ed">Assets{icon('chev-left', 10, '#a8a8a8', 1.75)}</button>
<button style="height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 3px; color: #939393">URL</button></div>'''
img_grp = f'''<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">{img_title}{src}
{f('<span style="font-size: 11px; color: #939393">Fit</span><span style="flex: 1">Fill frame</span><span style="font-family: ' + MONO + '; font-size: 10px; color: #939393">cover</span>' + icon('chev-down', 10, '#939393', 1.5))}
<label style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 11px; color: #e3b34a; display: flex; align-items: center; gap: 6px">{icon("warning", 12, "#e3b34a", 1.25)}Describe this image<span style="flex: 1"></span><span style="color: #939393">required</span></span>
<span style="height: 24px; display: flex; align-items: center; padding: 0 6px; background: #2a2a2a; border-radius: 2px; box-shadow: inset 0 0 0 1px #2f80ed; color: #939393">e.g. Ember mug, matte black glaze</span></label>
<div style="font-size: 11px; line-height: 16px; color: #939393">Picking an asset fills this in from its saved description.</div>
<div style="display: flex; align-items: center; justify-content: space-between; font-size: 11px; color: #a8a8a8"><span>Decorative (screen readers skip it)</span><button role="switch" aria-checked="false" aria-label="Decorative" style="position: relative; width: 28px; height: 16px; border-radius: 8px; background: #454545"><span style="position: absolute; left: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: #a8a8a8"></span></button></div></div>
<div style="height: 1px; background: #303030"></div>'''
S.props(panel(header('t-image', 'Image', 'Image', 'img') + img_grp
              + group('Size', pair(f('<span style="font-size: 11px; color: #939393; padding-left: 11px">W</span><span style="flex: 1; color: #939393">384</span>' + tagc('Fill')), f('<span style="font-size: 11px; color: #939393; padding-left: 11px">H</span><span style="flex: 1; color: #939393">288</span>' + tagc('4:3'))))
              + more([mp('Placement', 'In flow'), mp('Spacing', '0'), mp('Border', 'radius 8'), mp('Effects'), mp('Visibility', 'All sizes'), mp('Attributes &amp; Custom CSS')])))

# Assets picker popover
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
def thumb(name, bg, shape, meta, on=False, desc=True):
    ring = 'box-shadow: 0 0 0 2px #2f80ed;' if on else ''
    warn = '' if desc else f'<span title="No saved description" style="position: absolute; right: 4px; top: 4px; width: 16px; height: 16px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: rgba(29,26,22,0.8)">{icon("warning", 10, "#e3b34a", 1.25)}</span>'
    return (f'<button aria-pressed="{str(on).lower()}" style="display: flex; flex-direction: column; gap: 4px; text-align: left; min-width: 0">'
            f'<span style="position: relative; height: 66px; border-radius: 3px; background: {bg}; overflow: hidden; {ring}">{shape}{warn}</span>'
            f'<span style="font-size: 11px; color: {"#e8e8e8" if on else "#c8c8c8"}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{name}</span><span style="margin-top: -3px; font-size: 10px; color: #939393">{meta}</span></button>')
bowl = lambda c: f'<span style="position: absolute; left: 22%; right: 22%; top: 40%; height: 34%; border-radius: 0 0 50% 50% / 0 0 100% 100%; background: {c}"></span>'
mug = '<span style="position: absolute; left: 34%; width: 26%; top: 30%; height: 46%; border-radius: 2px 2px 6px 6px; background: #1d1a16"></span><span style="position: absolute; left: 58%; width: 12%; top: 40%; height: 20%; border: 3px solid #1d1a16; border-left: 0; border-radius: 0 8px 8px 0"></span>'
plates = '<span style="position: absolute; left: 18%; right: 18%; top: 34%; height: 30%; border-radius: 50%; background: #efe7da; box-shadow: 0 5px 0 #d8cbb8, 0 10px 0 #c9bba8"></span>'
wheel = '<span style="position: absolute; left: 25%; right: 25%; top: 52%; height: 14%; border-radius: 50%; background: #6b5a48"></span><span style="position: absolute; left: 38%; right: 38%; top: 30%; height: 26%; border-radius: 40% 40% 10% 10%; background: #a88a6e"></span>'
tiles = ''.join(f'<span style="position: absolute; left: {8 + (i % 4) * 22}%; top: {18 + (i // 4) * 34}%; width: 18%; height: 28%; border-radius: 2px; background: {c}"></span>' for i, c in enumerate(['#b5532d', '#6b7d5a', '#1d1a16', '#d8cbb8', '#8a6e9e', '#c9a24a', '#4a6fa5', '#efe7da']))
river = '<span style="position: absolute; left: 0; right: 0; top: 58%; bottom: 0; background: #7c95a8"></span><span style="position: absolute; left: 0; right: 0; top: 46%; height: 14%; background: #6b7d5a"></span>'
grid = (thumb('tide-bowl.jpg', '#e6dccd', bowl('#6b7d5a'), '2400 × 1800') + thumb('ember-mug.jpg', '#d8c6b0', mug, '2400 × 1800', True) + thumb('linen-plates.jpg', '#e9e1d4', plates, '2400 × 1800')
        + thumb('studio-wheel.jpg', '#cbb79f', wheel, '3000 × 2000') + thumb('glaze-tests.jpg', '#efe7da', tiles, '2000 × 2000', desc=False) + thumb('river-view.jpg', '#c9d4da', river, '3200 × 1800'))
pop = f'''<!-- POPOVER: Assets picker, anchored to Properties › Image › Source: Assets -->
<section role="dialog" aria-label="Pick an image from Assets" style="position: absolute; left: 1282px; top: 136px; width: 328px; box-sizing: border-box; padding: 0 12px 12px; display: flex; flex-direction: column; gap: 10px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); z-index: 30">
<span aria-hidden="true" style="position: absolute; right: -6px; top: 46px; width: 10px; height: 10px; background: #262626; border-right: 1px solid #454545; border-top: 1px solid #454545; transform: rotate(45deg)"></span>
<div style="height: 40px; margin: 0 -12px; padding: 0 8px 0 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a">
<span style="font-weight: 600">Assets</span><span style="flex: 1; font-size: 11px; color: #939393">Halden · 12 files</span>
<button aria-label="Pin open" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #939393">{icon("keep", 14)}</button>
<button aria-label="Close" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon("close", 14)}</button></div>
<label style="height: 26px; display: flex; align-items: center; gap: 8px; padding: 0 8px; background: #1f1f1f; border-radius: 4px; box-shadow: inset 0 0 0 1px #3a3a3a">{icon('search', 12, '#939393')}<span style="flex: 1; color: #939393">Search names and descriptions</span></label>
{L['seg'](['Images 9', 'Icons 2', 'Video 1', 'Unused'], 0)}
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px 8px">{grid}</div>
<div style="padding: 8px; display: flex; flex-direction: column; gap: 6px; background: #1f1f1f; border-radius: 4px; box-shadow: inset 0 0 0 1px #3a3a3a">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 11px; color: #e8e8e8">ember-mug.jpg</span><span style="font-size: 10px; color: #939393">412 KB · WebP 96 KB · used 1×</span></div>
<div style="display: flex; gap: 6px; align-items: flex-start; font-size: 11px; line-height: 16px"><span style="flex: none; margin-top: 2px">{icon('check', 12, '#3fb950', 2)}</span><span style="color: #c8c8c8">“Ember mug in matte black glaze on a linen cloth”</span></div>
<div style="font-size: 10px; color: #939393">Saved description · it fills in the image's alt text</div></div>
<div style="display: flex; align-items: center; gap: 6px"><button style="height: 26px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #c8c8c8">{icon('upload', 12)}Upload</button><span style="flex: 1; font-size: 10px; color: #939393">⚠ = no saved description</span>
<button style="height: 26px; padding: 0 14px; border-radius: 4px; background: #246bcb; color: #fff; font-weight: 500">Use image</button></div>
</section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', pop + '\n<!-- ═══════════ TOP BAR v3')
S.status(['Page', 'Section · This season', 'Box · Card grid', 'Box · Card 2', 'Image · img'], 'Drop a file on the frame · pick an asset in Properties · Enter uses the picked asset · Esc keeps the empty frame', 'x 940 &#160;y 1060')
S.save('D17-Media.dc.html')
print('ok')
