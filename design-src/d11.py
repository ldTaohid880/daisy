from screen import *

S = Screen('Daisy · D-11 Multi-selection and context menu')
S.remove_h1_overlay()
S.remove_parent_outline()

SCROLL = 640
S.rep('<div style="position: relative; width: 1440px; transform: scale(0.85); transform-origin: 0 0;',
      f'<div style="position: relative; width: 1440px; transform: scale(0.85) translateY(-{SCROLL}px); transform-origin: 0 0;')
fold_y = 32 + (900 - SCROLL) * 0.85
S.rep('right: 54px; top: 800px;', f'right: 54px; top: {fold_y + 3:.0f}px;')
S.rep('<span aria-hidden="true" style="position: absolute; right: 3px; top: 4px; width: 4px; height: 470px;',
      '<span aria-hidden="true" style="position: absolute; right: 3px; top: 250px; width: 4px; height: 470px;')

# third card has a different fill -> Mixed
S.rep('<div style="aspect-ratio: 4 / 3; border-radius: 8px; background: #ddd2c2"></div>', '<div style="aspect-ratio: 4 / 3; border-radius: 8px; background: #ddd2c2"></div>')
cards_open = '<div style="background: #ffffff; border-radius: 12px; padding: 16px; display: flex; flex-direction: column; gap: 8px">'
assert S.s.count(cards_open) == 3
outline = '<div aria-hidden="true" style="position: absolute; inset: -1px; border: 1.18px solid #2f80ed; border-radius: 0; pointer-events: none"></div>'
parts = S.s.split(cards_open)
bgs = ['#ffffff', '#ffffff', '#fbf6ef']
S.s = parts[0] + ''.join(f'<div style="position: relative; background: {bgs[i]}; border-radius: 12px; padding: 16px; display: flex; flex-direction: column; gap: 8px">{outline}' + parts[i + 1] for i in range(3))
grid_open = '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 32px">'
hpos = ['left: -5.6px; top: -5.6px', 'left: calc(50% - 4.7px); top: -5.6px', 'right: -5.6px; top: -5.6px', 'right: -5.6px; top: calc(50% - 4.7px)',
        'right: -5.6px; bottom: -5.6px', 'left: calc(50% - 4.7px); bottom: -5.6px', 'left: -5.6px; bottom: -5.6px', 'left: -5.6px; top: calc(50% - 4.7px)']
handles = ''.join(f'<span style="position: absolute; {p}; width: 9.4px; height: 9.4px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>' for p in hpos)
S.rep(grid_open, '<div style="position: relative; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 32px">'
      f'<div aria-hidden="true" style="position: absolute; inset: -6px; border: 1.76px solid #2f80ed; pointer-events: none; z-index: 2"><span style="position: absolute; left: -1.76px; bottom: calc(100% + 2px); height: 21px; padding: 0 5px; display: flex; align-items: center; background: #246bcb; color: #ffffff; font: 500 13px/1 \'Inter\', sans-serif; white-space: nowrap">3 selected · Box</span>{handles}</div>')


# footer (page content below This season)
S.rep('<!-- fold line at 900 -->', '''<!-- Footer -->
<div style="padding: 48px 64px; background: #1d1a16; color: #f6f1ea; display: flex; align-items: center; justify-content: space-between; font-size: 15px">
<span>© 2026 Halden Studio</span><span style="color: #e7d9c7">Riverside Works, Unit 4</span><span style="display: flex; gap: 24px"><a href="#ig">Instagram</a><a href="#news">Newsletter</a></span></div>
<!-- fold line at 900 -->''')

# context menu (canvas coordinates)
def mrow(label, key='', ic=None, sub=False, state='rest', checked=False):
    bg = 'background: #323232;' if state == 'hover' else ''
    col = {'danger': '#f85149', 'disabled': '#4f4f4f'}.get(state, '#e8e8e8')
    left = icon('check', 12, '#e8e8e8') if checked else (icon(ic, 14, col if state == 'danger' else '#a8a8a8') if ic else '')
    right = icon('chev-right', 12, '#939393') if sub else f'<span style="font-size: 11px; color: #939393">{key}</span>'
    return f'<button role="menuitem" style="width: 100%; height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 8px; box-sizing: border-box; border-radius: 3px; color: {col}; {bg}"><span style="width: 16px; display: flex; justify-content: center">{left}</span><span style="flex: 1; text-align: left">{label}</span>{right}</button>'


sep = '<span role="separator" style="display: block; height: 1px; margin: 4px 0; background: #333333"></span>'
FLOAT = 'background: #262626; border: 1px solid #454545; box-shadow: 0 8px 24px rgba(0,0,0,0.45);'
menu = (mrow('Cut', 'Ctrl+X') + mrow('Copy', 'Ctrl+C', 'copy') + mrow('Paste', 'Ctrl+V') + mrow('Paste inside', 'Ctrl+Shift+V', state='disabled') + mrow('Duplicate', 'Ctrl+D') + sep
        + mrow('Copy style', 'Ctrl+Alt+C') + mrow('Paste style', 'Ctrl+Alt+V') + sep
        + mrow('Group', 'Ctrl+G') + mrow('Ungroup', 'Ctrl+Shift+G', state='disabled') + mrow('Wrap in link') + sep
        + mrow('Move earlier', 'Ctrl+[') + mrow('Move later', 'Ctrl+]') + sep
        + mrow('Placement', sub=True, state='hover') + sep
        + mrow('Lock') + mrow('Hide') + mrow('Select layer', sub=True) + sep
        + mrow('Rename', state='disabled') + mrow('Show code') + sep + mrow('Delete', 'Del', 'trash', state='danger'))
sub = mrow('In flow', checked=True) + mrow('Nudged') + mrow('Free', state='hover') + mrow('Fixed to screen') + mrow('Sticks when scrolling')
MX, MY = 692, 230
place_top = 4 + 5 * 28 + 9 + 2 * 28 + 9 + 3 * 28 + 9 + 2 * 28 + 9
ctx = f'''<!-- context menu on the selection -->
<div role="menu" aria-label="Element actions" style="position: absolute; left: {MX}px; top: {MY}px; width: 240px; padding: 4px; box-sizing: border-box; border-radius: 4px; {FLOAT} z-index: 10">{menu}</div>
<div role="menu" aria-label="Placement" style="position: absolute; left: {MX + 238}px; top: {MY + place_top - 4}px; width: 200px; padding: 4px; box-sizing: border-box; border-radius: 4px; {FLOAT} z-index: 11">{sub}</div>
<svg aria-hidden="true" width="22" height="22" viewBox="0 0 16 16" style="position: absolute; left: {MX - 12}px; top: {MY - 14}px; overflow: visible; z-index: 12"><path d="M4 2l9 6.2-4.1.9 2.4 4.4-1.7.9-2.4-4.4L4 13z" fill="#1d1a16" stroke="#ffffff" stroke-width="1.2" stroke-linejoin="round"></path></svg>
'''
S.rep('<!-- vertical scroll indicator -->', ctx + '<!-- vertical scroll indicator -->')

# Layers tree: This season expanded, three cards selected
def lrow(pad, chev, ic, name, tag, sel=False, guides=()):
    g = ''
    if guides:
        g = 'background-image: ' + ', '.join('linear-gradient(#303030,#303030)' if sel else 'linear-gradient(#262626,#262626)' for _ in guides) + '; background-size: ' + ', '.join('1px 100%' for _ in guides) + '; background-position: ' + ', '.join(f'{x}px 0' for x in guides) + '; background-repeat: no-repeat;'
    bg = 'background-color: rgba(47,128,237,0.18);' if sel else ''
    ch = icon('chev-down' if chev == 'open' else 'chev-right', 12, '#a8a8a8') if chev else '<span style="width: 12px"></span>'
    col = '#e8e8e8'
    return (f'<div role="treeitem"{" aria-selected=\"true\"" if sel else ""} style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 {pad}px; {bg} {g}">'
            f'{ch}{icon(ic, 14, "#e8e8e8" if sel else "#a8a8a8")}<span style="flex: 1; color: {col}">{name}</span><span style="font-size: 11px; color: {"#a8a8a8" if sel else "#939393"}">{tag}</span></div>')


tree = ('<div role="tree" aria-label="Layers" style="display: flex; flex-direction: column; font-size: 12px">\n'
        + lrow(8, 'closed', 't-section', 'Header', 'header')
        + lrow(8, 'closed', 't-section', 'Hero', 'section')
        + lrow(8, 'open', 't-section', 'This season', 'section')
        + lrow(20, 'closed', 't-row', 'Season heading', 'div', guides=(14,))
        + lrow(20, 'open', 't-grid', 'Card grid', 'div', guides=(14,))
        + ''.join(lrow(32, 'closed', 't-stack', f'Card {i}', 'div', True, (14, 26)) for i in (1, 2, 3))
        + lrow(8, 'closed', 't-section', 'Footer', 'footer')
        + '\n</div>\n')
S.cut('<div role="tree" aria-label="Layers"', '</aside>', tree)

# options: mixed X, distribute enabled
S.options('Mixed', '952', '416', 'Fill', '380', 'Fit')
S.rep('title="Distribute horizontally · select 3 or more" disabled style="width: 26px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; opacity: 0.35"',
      'title="Distribute horizontally" style="width: 26px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px"')
S.rep('title="Distribute vertically · select 3 or more" disabled style="width: 26px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; opacity: 0.35"',
      'title="Distribute vertically" style="width: 26px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px"')

mixed_fill = f('<span style="width: 14px; height: 14px; box-sizing: border-box; border-radius: 2px; background: conic-gradient(#ffffff 0 50%, #fbf6ef 0); box-shadow: inset 0 0 0 1px #6b6b6b; flex: none"></span><span style="flex: 1; font-style: italic; color: #939393">Mixed</span>')
hdr = f'''<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{icon('t-stack', 16, '#a8a8a8')}<span style="flex: 1; font-weight: 500">3 elements</span><span style="font-size: 11px; color: #939393">Card 1 · 2 · 3</span></div>
<div style="padding-left: 24px; font-size: 11px; color: #939393">Box · <span style="font-family: {MONO}">div</span> · only shared groups shown</div></div>'''
S.props(panel(hdr
              + group('Size', pair(f('<span style="font-size: 11px; color: #939393; padding-left: 11px">W</span><span style="flex: 1; color: #939393">416</span>' + tagc('Fill')),
                                   f('<span style="font-size: 11px; color: #939393; padding-left: 11px">H</span><span style="flex: 1; color: #939393">380</span>' + tagc('Fit'))))
              + group('Fill', mixed_fill)
              + group('Border', pair(f('<span style="font-size: 11px; color: #939393; padding-left: 11px">Colour</span><span style="flex: 1; color: #939393">none</span>'),
                                     f(DOT + '<span style="font-size: 11px; color: #939393">Corners</span><span style="flex: 1; text-align: right">12</span>')))
              + more([mp('Placement', 'In flow'), mp('Layout', 'Stack'), mp('Spacing', '16'), mp('Effects'), mp('Transform'), mp('Visibility', 'All sizes'), mp('Transition &amp; Animation'), mp('Attributes &amp; Custom CSS')])))
S.status(['Page', 'Section · This season', 'Box · Card grid', '3 selected'], 'Shift-click to add or remove · right-click for actions · Ctrl+G to group', 'x 812 &#160;y 1104')
S.save('D11-MultiSelect.dc.html')
print('ok', place_top)
