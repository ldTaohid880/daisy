from screen import *
P['comp'] = ('stroke', 'M8 1.5l2.5 2.5L8 6.5 5.5 4zM4 5.5l2.5 2.5L4 10.5 1.5 8zM12 5.5l2.5 2.5-2.5 2.5L9.5 8zM8 9.5l2.5 2.5L8 14.5 5.5 12z')
P['repeat'] = ('stroke', 'M2.5 5.5h9l-2-2M13.5 10.5h-9l2 2M2.5 5.5v2M13.5 10.5v-2')
P['detach'] = ('stroke', 'M8 1.8l6.2 6.2L8 14.2 1.8 8zM2 2l12 12')
P['field'] = ('stroke', 'M3 4.5h10v7H3zM5.5 7h3M5.5 9h5')
S = Screen('Daisy · D-58 Components and variants')
S.remove_h1_overlay(); S.remove_parent_outline(); S.unselect_h1_row()
scroll(S, 700, 330)
POP = 'background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5);'
CI = lambda s=12, c='#a9c8f7': icon('comp', s, c, 1.3)

def card_html(bg, n, p, variant='default', sel=False, scale=1):
    sold = variant == 'sold'; feat = variant == 'featured'
    badge = ('<span style="position: absolute; z-index: 1; left: 26px; top: 26px; padding: 4px 10px; border-radius: 999px; background: #1d1a16; color: #f6f1ea; font-size: 12px; font-weight: 500">Sold out</span>' if sold else
             '<span style="position: absolute; z-index: 1; left: 26px; top: 26px; padding: 4px 10px; border-radius: 999px; background: #b5532d; color: #fff; font-size: 12px; font-weight: 500">New</span>' if feat else '')
    over = (f'<span aria-hidden="true" style="position: absolute; inset: -3px; border: 2.35px solid #2f80ed; border-radius: 14px">'
            + ''.join(f'<span style="position: absolute; {q}; width: 11px; height: 11px; box-sizing: border-box; background: #fff; border: 1.4px solid #2f80ed"></span>' for q in ['left: -6px; top: -6px', 'right: -6px; top: -6px', 'left: -6px; bottom: -6px', 'right: -6px; bottom: -6px'])
            + '<span style="position: absolute; left: 0; bottom: calc(100% + 4px); height: 22px; padding: 0 7px; display: flex; align-items: center; gap: 6px; background: #246bcb; color: #fff; font: 500 14px/1 Inter, sans-serif; white-space: nowrap; border-radius: 2px">' + icon('comp', 14, '#fff', 1.5) + 'Product card · Sold out</span></span>') if sel else ''
    return (f'<div style="position: relative; background: #ffffff; border-radius: 12px; padding: 16px; display: flex; flex-direction: column; gap: 8px; {"box-shadow: inset 0 0 0 2px #b5532d;" if feat else ""}">{badge}'
            f'<div style="aspect-ratio: 4 / 3; border-radius: 8px; background: {bg}; {"filter: grayscale(0.7); opacity: 0.55;" if sold else ""}"></div>'
            f'<p style="margin: 8px 0 0; font-family: \'Fraunces\', serif; font-size: 20px; {"color: #8a8174;" if sold else ""}">{n}</p>'
            f'<p style="margin: 0; font-size: 15px; color: {"#8a8174; text-decoration: line-through" if sold else "#5f6b4e"}">{p}</p>{over}</div>')
items = [('#d8cbb8', 'Tide bowl', '€38', 'default', False), ('#cfb9a3', 'Ember mug', '€26', 'default', False), ('#ddd2c2', 'Linen plate set', '€84', 'sold', True)]
grid = '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 32px">' + ''.join(card_html(*it) for it in items) + '</div>'
a = S.s.index('<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 32px">')
endm = '<p style="margin: 0; font-size: 15px; color: #5f6b4e">€84</p>\n</div>\n</div>'
b = S.s.index(endm, a) + len(endm)
S.s = S.s[:a] + grid + S.s[b:]

# Project panel: Components group
grp = f'''<div role="treeitem" aria-expanded="true" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 20px">{icon('chev-down', 12, '#a8a8a8')}<span style="flex: 1; color: #a8a8a8">Components</span><span style="font-size: 11px; color: #939393">3</span></div>
<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 44px; background: rgba(47,128,237,0.12)">{CI(13)}<span style="flex: 1; color: #e8e8e8">Product card</span><span style="font-size: 11px; color: #939393">3 variants</span></div>
<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 44px">{CI(13, '#a8a8a8')}<span style="flex: 1">Button</span><span style="font-size: 11px; color: #939393">4 variants</span></div>
<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 44px">{CI(13, '#a8a8a8')}<span style="flex: 1">Section heading</span><span style="font-size: 11px; color: #939393">2 variants</span></div>
'''
k = S.s.index('<div role="treeitem" aria-expanded="false" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 20px">\n<svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="#a8a8a8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 4l4 4-4 4"></path></svg>\n<span style="flex: 1; color: #a8a8a8">Design system</span>')
S.s = S.s[:k] + grp + S.s[k:]

# Layers
cb = lambda v: f'<span style="margin-left: 6px; font-size: 10px; color: #a9c8f7">{v}</span>'
rows = [(8, 'closed', 't-section', 'Header', 'header', False, (), ''), (8, 'closed', 't-section', 'Hero', 'section', False, (), ''), (8, 'open', 't-section', 'This season', 'section', False, (), ''),
        (20, 'closed', 't-row', 'Season heading', 'div', False, (14,), ''), (20, 'open', 't-grid', 'Card grid', 'div', False, (14,), '<span style="margin-left: 6px">' + icon('repeat', 11, '#a9c8f7', 1.5) + '</span>'),
        (32, 'closed', 'comp', 'Product card', 'div', False, (14, 26), cb('Default')), (32, 'closed', 'comp', 'Product card', 'div', False, (14, 26), cb('Default')),
        (32, 'closed', 'comp', 'Product card', 'div', True, (14, 26), cb('Sold out')), (8, 'closed', 't-section', 'Footer', 'footer', False, (), '')]
set_tree(S, rows)

# Properties
row2 = lambda l, c: f'<div style="display: grid; grid-template-columns: 64px minmax(0, 1fr); gap: 8px; align-items: center"><span style="font-size: 11px; color: #a8a8a8">{l}</span>{c}</div>'
seg_ = lambda items, sel: '<div style="display: grid; grid-template-columns: repeat(' + str(len(items)) + ', minmax(0, 1fr)); gap: 2px; padding: 2px; background: #262626; border-radius: 4px; font-size: 11px">' + ''.join(f'<button style="height: 22px; border-radius: 3px; white-space: nowrap; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #939393;"}">{t}</button>' for i, t in enumerate(items)) + '</div>'
swt = lambda on: f'<span style="position: relative; display: inline-block; width: 24px; height: 14px; flex: none; border-radius: 7px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 10px; height: 10px; border-radius: 5px; background: {"#fff" if on else "#a8a8a8"}"></span></span>'
comp = (row2('Variant', seg_(['Default', 'Sold out', 'Featured'], 1))
        + f'<div style="display: flex; align-items: center; gap: 6px; padding: 6px 8px; border-radius: 4px; background: rgba(47,128,237,0.12); font-size: 11px; line-height: 15px; color: #c8c8c8">{icon("field", 12, "#a9c8f7")}<span style="flex: 1">Chosen by the data: <b style="font-weight: 600; color: #e8e8e8">in stock</b> is off → Sold out</span><button style="font-size: 11px; color: #a9c8f7">Edit rule</button></div>'
        + '<div style="font-size: 10px; letter-spacing: 0.04em; color: #939393; margin-top: 2px">OPTIONS</div>'
        + row2('Badge', f('<span style="flex: 1">Sold out</span><span style="font-size: 10px; color: #939393">from variant</span>'))
        + row2('Size', seg_(['Regular', 'Compact'], 0))
        + row2('Show price', f('<span style="flex: 1"></span>' + swt(True)))
        + '<div style="font-size: 10px; letter-spacing: 0.04em; color: #939393; margin-top: 2px">CONTENT · FROM PRODUCTS</div>'
        + row2('Image', f(f'<span style="flex: 1; font-family: {MONO}; font-size: 11px">photo</span>')) + row2('Name', f(f'<span style="flex: 1; font-family: {MONO}; font-size: 11px">name</span>')) + row2('Price', f(f'<span style="flex: 1; font-family: {MONO}; font-size: 11px">price</span>')))
acts = f'<div style="padding: 10px 12px; display: flex; flex-wrap: wrap; gap: 6px; white-space: nowrap"><button style="height: 24px; padding: 0 10px; border-radius: 4px; box-shadow: inset 0 0 0 1px #454545; font-size: 11px">Edit component</button><button style="height: 24px; padding: 0 10px; border-radius: 4px; font-size: 11px; color: #a8a8a8">No changes here</button><button style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 8px; border-radius: 4px; font-size: 11px; color: #a8a8a8">{icon("detach", 11)}Detach</button></div>'
hdr = f'''<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{CI(16)}<span style="flex: 1; font-weight: 500">Product card</span><button style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 6px; color: #a8a8a8">Normal{icon('chev-down', 10, 'currentColor', 1.5)}</button></div>
<div style="padding-left: 24px; font-size: 11px; color: #a8a8a8">Component · used 9 times · this one: Linen plate set</div></div>'''
S.props(panel(hdr + group('Component', comp) + acts + more([mp('Size', 'Fill'), mp('Spacing', 'from component'), mp('Effects', 'from component')])))
S.options('912', '0', '416', 'Fill', 'Fit', 'Fit')

# INSET: the component's own tab (variants board)
mini = lambda v, label, note: f'''<div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 11px; color: #4a443c; font-weight: 500">{label} <span style="color: #6b6358; font-weight: 400">· {note}</span></span>
<div style="position: relative; width: 150px; padding: 8px; box-sizing: border-box; border-radius: 8px; background: #fff; {"box-shadow: inset 0 0 0 2px #b5532d;" if v == "featured" else ""} {"outline: 1.5px solid #2f80ed; outline-offset: 3px;" if v == "sold" else ""}">
<div style="height: 80px; border-radius: 5px; background: #d8cbb8; {"filter: grayscale(0.7); opacity: 0.55;" if v == "sold" else ""}"></div>
{"<span style=\"position: absolute; left: 14px; top: 14px; padding: 2px 7px; border-radius: 999px; background: #1d1a16; color: #f6f1ea; font-size: 9px\">Sold out</span>" if v == "sold" else ""}{"<span style=\"position: absolute; left: 14px; top: 14px; padding: 2px 7px; border-radius: 999px; background: #b5532d; color: #fff; font-size: 9px\">New</span>" if v == "featured" else ""}
<div style="margin-top: 6px; font: 13px Fraunces, serif; color: {"#8a8174" if v == "sold" else "#1d1a16"}">{{name}}</div><div style="font-size: 11px; color: {"#8a8174; text-decoration: line-through" if v == "sold" else "#5f6b4e"}">{{price}}</div></div></div>'''
inset = f'''<!-- INSET: Product card component tab -->
<div style="position: absolute; left: 330px; bottom: 44px; width: 860px; display: flex; flex-direction: column; gap: 8px; z-index: 35">
<span style="width: max-content; height: 20px; display: flex; align-items: center; padding: 0 8px; border-radius: 3px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; color: #a8a8a8">Inset · Edit component → the Product card opens in its own tab</span>
<div style="padding: 14px; display: flex; gap: 20px; {POP}">
<div style="display: flex; gap: 16px; padding: 12px; border-radius: 6px; background: #e7d9c7">{mini("default", "Default", "4 uses")}{mini("sold", "Sold out", "1 use")}{mini("featured", "Featured", "4 uses")}</div>
<div style="flex: 1; display: flex; flex-direction: column; gap: 6px; font-size: 11px">
<b style="font-size: 12px; font-weight: 600">Options</b>
{''.join(f'<div style="height: 24px; display: flex; align-items: center; gap: 8px; padding: 0 8px; border-radius: 3px; background: #2a2a2a"><span style="flex: 1">{a}</span><span style="color: #939393">{b}</span></div>' for a, b in [('Variant', 'Default · Sold out · Featured'), ('Badge', 'text'), ('Size', 'Regular · Compact'), ('Show price', 'on / off')])}
<div style="display: flex; gap: 10px; margin-top: 2px"><button style="font-size: 11px; color: #a9c8f7">+ Variant</button><button style="font-size: 11px; color: #a9c8f7">+ Option</button></div>
<span style="margin-top: auto; line-height: 15px; color: #939393">Edit a variant here and every use updates. Variants only differ where they need to.</span></div></div></div>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', inset + '\n<!-- ═══════════ TOP BAR v3')
S.status(['Page', 'Section · This season', 'Grid · Card grid', 'Component · Product card'], 'Double-click to edit this use · Edit component changes all 9', 'x 912 &#160;y 1180')
S.save('D58-Components.dc.html')
print('ok')
