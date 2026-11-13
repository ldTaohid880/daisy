from screen import *

S = Screen('Daisy · D-25 Layers outline view and accessibility')
S.remove_h1_overlay()
S.remove_parent_outline()
S.unselect_h1_row()
WARN = '#d29922'

# ---------------- canvas: outline badges + Hero image selected with a warning tag ----------------
hb = lambda t, extra='': f'<span aria-hidden="true" style="position: absolute; {extra} height: 20px; padding: 0 6px; display: flex; align-items: center; border-radius: 3px; background: #1d1a16; color: #f6f1ea; font: 600 11px/1 \'JetBrains Mono\', monospace; white-space: nowrap; z-index: 5">{t}</span>'
S.rep('<h1 style="margin: 0; font-family: \'Fraunces\', serif; font-size: 64px; line-height: 1.05; font-weight: 600; color: #1d1a16">',
      hb('H1', 'left: -46px; top: 8px;') + '<h1 style="margin: 0; font-family: \'Fraunces\', serif; font-size: 64px; line-height: 1.05; font-weight: 600; color: #1d1a16">')
S.rep('<div style="height: 80px; box-sizing: border-box; padding: 0 64px; display: flex; align-items: center; justify-content: space-between">',
      '<div style="position: relative; height: 80px; box-sizing: border-box; padding: 0 64px; display: flex; align-items: center; justify-content: space-between">' + hb('banner', 'left: 6px; top: 6px; background: #5f6b4e;'))
S.rep('<h2 style="margin: 0; font-family: \'Fraunces\', serif; font-size: 40px; line-height: 1.2; font-weight: 600">This season</h2>',
      '<h2 style="position: relative; margin: 0; font-family: \'Fraunces\', serif; font-size: 40px; line-height: 1.2; font-weight: 600">' + hb('H2', 'left: -46px; top: 12px;') + 'This season</h2>')
img_open = '<div style="justify-self: end; width: 580px; height: 520px; border-radius: 12px; overflow: hidden; background: #e6dccd">'
hpos = ['left: -5.6px; top: -5.6px', 'right: -5.6px; top: -5.6px', 'right: -5.6px; bottom: -5.6px', 'left: -5.6px; bottom: -5.6px']
handles = ''.join(f'<span style="position: absolute; {p}; width: 9.4px; height: 9.4px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>' for p in hpos)
S.rep(img_open, '<div style="position: relative; justify-self: end; width: 580px; height: 520px"><div aria-hidden="true" style="position: absolute; inset: -1px; border: 1.76px solid #2f80ed; z-index: 4">' + handles
      + f'<span style="position: absolute; left: -1.76px; bottom: calc(100% + 2px); height: 21px; padding: 0 6px; display: flex; align-items: center; gap: 5px; background: #246bcb; color: #fff; font: 500 13px/1 \'Inter\', sans-serif; white-space: nowrap">Image · img<span style="display: flex; align-items: center; gap: 3px; padding-left: 6px; border-left: 1px solid rgba(255,255,255,0.35); color: #ffd27a">{icon("warning", 12, "#ffd27a", 1.5)}no description</span></span></div>'
      + '<div style="width: 580px; height: 520px; border-radius: 12px; overflow: hidden; background: #e6dccd">')
s = S.s
a = s.index('<div style="width: 580px; height: 520px; border-radius: 12px; overflow: hidden; background: #e6dccd">'); b = s.index('</svg>\n</div>', a) + len('</svg>\n</div>')
S.s = s[:b] + '</div>' + s[b:]

# ---------------- layers: outline view ----------------
def orow(pad, badge, name, kind='h', sel=False, warn=''):
    bg = 'background-color: rgba(47,128,237,0.18);' if sel else ''
    tagbg = {'h': '#3a3a3a', 'l': 'rgba(95,107,78,0.35)', 'i': 'rgba(210,153,34,0.16)'}[kind]
    tagc_ = {'h': '#e8e8e8', 'l': '#c5d1b0', 'i': '#e3b34a'}[kind]
    return (f'<div role="treeitem"{" aria-selected=\"true\"" if sel else ""} style="height: 26px; display: flex; align-items: center; gap: 8px; padding: 0 12px 0 {pad}px; {bg}">'
            f'<span style="min-width: 22px; height: 16px; padding: 0 4px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: {tagbg}; color: {tagc_}; font: 600 10px/1 {MONO}">{badge}</span>'
            f'<span style="flex: 1; min-width: 0; color: #e8e8e8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{name}</span>{warn}</div>')
ok = icon('check', 12, '#3fb950', 2)
tree = f'''<div style="display: flex; align-items: center; gap: 6px; padding: 0 12px 6px">
<span style="height: 20px; display: flex; align-items: center; gap: 4px; padding: 0 4px 0 8px; border-radius: 10px; background: #333333; font-size: 11px; color: #e8e8e8">Outline view<button aria-label="Turn off outline view" style="width: 14px; height: 14px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon('close', 9)}</button></span>
<span style="flex: 1"></span><span style="font-size: 10px; color: #939393">Alt+O</span></div>
<div role="tree" aria-label="Outline" style="display: flex; flex-direction: column; font-size: 12px">
{orow(12, 'banner', 'Header', 'l')}
{orow(24, 'nav', 'Navigation · 4 links', 'l')}
{orow(12, 'main', 'Main content', 'l')}
{orow(24, 'H1', 'Hand-thrown ceramics for everyday tables')}
{orow(24, 'img', 'Hero image', 'i', True, icon('warning', 12, WARN, 1.25, 'No description'))}
{orow(24, 'H2', 'This season')}
{orow(36, 'H3', 'Tide bowl')}{orow(36, 'H3', 'Ember mug')}{orow(36, 'H3', 'Linen plate set')}
{orow(12, 'footer', 'Footer · contentinfo', 'l')}
</div>
<div style="margin: 10px 12px 0; padding: 8px 10px; border-radius: 4px; background: #262626; display: flex; flex-direction: column; gap: 6px; font-size: 11px; line-height: 16px">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600; color: #e8e8e8">Page check</span><span style="color: #939393">updates as you edit</span></div>
<div style="display: flex; gap: 6px"><span style="margin-top: 2px">{icon('warning', 12, WARN, 1.25)}</span><span style="color: #c8c8c8">1 image has no description</span></div>
<div style="display: flex; gap: 6px"><span style="margin-top: 2px">{ok}</span><span style="color: #a8a8a8">One H1 · headings in order</span></div>
<div style="display: flex; gap: 6px"><span style="margin-top: 2px">{ok}</span><span style="color: #a8a8a8">Text contrast passes (lowest 6.1 : 1)</span></div>
</div>
'''
S.cut('<div role="tree" aria-label="Layers"', '</aside>', tree)

# ---------------- properties ----------------
img_grp = f'''<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">
<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">Image</span>{adv('Image')}</div>
{f('<span style="font-size: 11px; color: #939393">Source</span><span style="flex: 1; font-family: ' + MONO + '; font-size: 11px">hero-bowls.svg</span>' + icon('chev-down', 10, '#939393', 1.5))}
<label style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 11px; color: #e3b34a; display: flex; align-items: center; gap: 6px">{icon("warning", 12, "#e3b34a", 1.25)}Describe this image<span style="flex: 1"></span><span style="color: #939393">required</span></span>
<span style="height: 24px; display: flex; align-items: center; padding: 0 6px; background: #2a2a2a; border-radius: 2px; box-shadow: inset 0 0 0 1px #2f80ed; color: #939393">e.g. Stacked bowls and a black mug on linen</span></label>
<div role="alert" style="font-size: 11px; line-height: 16px; color: #e3b34a">Images need a description, or mark it Decorative.</div>
<div style="display: flex; align-items: center; justify-content: space-between; font-size: 11px; color: #a8a8a8"><span>Decorative (screen readers skip it)</span><button role="switch" aria-checked="false" aria-label="Decorative" style="position: relative; width: 28px; height: 16px; border-radius: 8px; background: #454545"><span style="position: absolute; left: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: #a8a8a8"></span></button></div>
</div><div style="height: 1px; background: #303030"></div>'''
acc = (f'<div style="display: grid; grid-template-columns: 1fr auto; gap: 6px 12px; font-size: 11px"><span style="color: #a8a8a8">Read as</span><span style="color: #c8c8c8">image, <i style="color: #e3b34a">no name</i></span>'
       f'<span style="color: #a8a8a8">Role</span><span style="color: #939393">img (automatic)</span>'
       f'<span style="color: #a8a8a8">In reading order</span><span style="color: #939393">after “Our process →”</span></div>'
       '<div style="font-size: 10px; line-height: 14px; color: #939393">The description is set in Image above · Hide from screen readers and roles: Advanced</div>')
S.props(panel(header('t-image', 'Hero image', 'Image', 'img') + img_grp + group('Accessibility', acc)
              + group('Size', pair(f('<span style="font-size: 11px; color: #939393; padding-left: 11px">W</span><span style="flex: 1; color: #939393">580</span>' + tagc('Fixed')), f('<span style="font-size: 11px; color: #939393; padding-left: 11px">H</span><span style="flex: 1; color: #939393">520</span>' + tagc('Fixed'))))
              + more([mp('Placement', 'In flow'), mp('Border', 'radius 12'), mp('Effects'), mp('Visibility', 'All sizes')])))
S.options('—', '—', '580', 'Fixed', '520', 'Fixed')
S.status(['Page', 'Section · Hero', 'Box · Hero grid', 'Image · Hero image'], 'Outline view · headings and landmarks only · click a row to select it · Alt+O returns to all layers', 'x 1180 &#160;y 330')
S.save('D25-Outline.dc.html')
print('ok')
