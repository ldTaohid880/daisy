from screen import *
P['repeat'] = ('stroke', 'M2.5 5.5h9l-2-2M13.5 10.5h-9l2 2M2.5 5.5v2M13.5 10.5v-2')
P['table'] = ('stroke', 'M2 3h12v10H2zM2 6.5h12M2 10h12M6.5 3v10')
P['field'] = ('stroke', 'M3 4.5h10v7H3zM5.5 7h3M5.5 9h5')
S = Screen('Daisy · D-57 Repeating content: collections')
S.remove_h1_overlay(); S.remove_parent_outline(); S.unselect_h1_row()
scroll(S, 700, 330)
POP = 'background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5);'
chip = lambda t: f'<span style="position: absolute; right: 4px; top: 50%; transform: translateY(-50%); height: 19px; padding: 0 6px; display: flex; align-items: center; border-radius: 3px; background: #246bcb; color: #fff; font: 500 12px/1 \'JetBrains Mono\', monospace; white-space: nowrap">{t}</span>'
bound = lambda inner, name: f'<span style="position: relative; display: block; outline: 1.2px dashed rgba(47,128,237,0.75); outline-offset: 3px">{inner}{chip(name)}</span>'
items = [('#d8cbb8', 'Tide bowl', '€38'), ('#cfb9a3', 'Ember mug', '€26'), ('#ddd2c2', 'Linen plate set', '€84')]
def card(i, bg, n, p):
    first = i == 0
    img = f'<div style="aspect-ratio: 4 / 3; border-radius: 8px; background: {bg}"></div>'
    nm = f'<p style="margin: 8px 0 0; font-family: \'Fraunces\', serif; font-size: 20px">{n}</p>'
    pr = f'<p style="margin: 0; font-size: 15px; color: #5f6b4e">{p}</p>'
    if first:
        img, nm, pr = bound(img, '{image}'), bound(nm, '{name}'), bound(pr, '{price}')
    return (f'<div style="position: relative; background: #ffffff; border-radius: 12px; padding: 16px; display: flex; flex-direction: column; gap: 14px; {"" if first else "opacity: 0.72;"}">{img}{nm}{pr}'
            + (f'<span aria-hidden="true" style="position: absolute; inset: -3px; border: 2.35px solid #2f80ed; border-radius: 14px"><span style="position: absolute; left: 0; bottom: calc(100% + 4px); height: 22px; padding: 0 7px; display: flex; align-items: center; gap: 6px; background: #246bcb; color: #fff; font: 500 14px/1 Inter, sans-serif; white-space: nowrap; border-radius: 2px">Card · repeated for each product</span></span>' if first else
               '<span aria-hidden="true" style="position: absolute; inset: -3px; border: 1.18px solid rgba(47,128,237,0.35); border-radius: 14px"></span>') + '</div>')
grid = ('<div style="position: relative; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 32px">' + ''.join(card(i, *it) for i, it in enumerate(items))
        + '<span aria-hidden="true" style="position: absolute; inset: -14px; border: 1.18px dashed rgba(47,128,237,0.6); border-radius: 4px"><span style="position: absolute; right: 0; top: calc(100% + 6px); height: 22px; padding: 0 8px; display: flex; align-items: center; gap: 6px; background: rgba(47,128,237,0.14); border: 1.18px dashed rgba(47,128,237,0.6); color: #1f5fb5; font: 500 14px/1 Inter, sans-serif; white-space: nowrap">Card grid · Products · 3 of 12 · newest first</span></span></div>')
a = S.s.index('<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 32px">')
endm = '<p style="margin: 0; font-size: 15px; color: #5f6b4e">€84</p>\n</div>\n</div>'
b = S.s.index(endm, a) + len(endm)
S.s = S.s[:a] + grid + S.s[b:]

# Project panel: Collections group
grp = f'''<div role="treeitem" aria-expanded="true" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 20px">{icon('chev-down', 12, '#a8a8a8')}<span style="flex: 1; color: #a8a8a8">Collections</span><span style="font-size: 11px; color: #939393">2</span></div>
<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 44px; background: rgba(47,128,237,0.12)">{icon('table', 13, '#a9c8f7')}<span style="flex: 1; color: #e8e8e8">Products</span><span style="font-size: 11px; color: #939393">12</span></div>
<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 44px">{icon('table', 13, '#a8a8a8')}<span style="flex: 1">Journal posts</span><span style="font-size: 11px; color: #939393">6</span></div>
'''
k = S.s.index('<div role="treeitem" aria-expanded="false" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 20px">\n<svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="#a8a8a8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 4l4 4-4 4"></path></svg>\n<span style="flex: 1; color: #a8a8a8">Design system</span>')
S.s = S.s[:k] + grp + S.s[k:]

# Layers
rp = '<span style="margin-left: 6px">' + icon('repeat', 11, '#a9c8f7', 1.5) + '</span>'
rows = [(8, 'closed', 't-section', 'Header', 'header', False, (), ''), (8, 'closed', 't-section', 'Hero', 'section', False, (), ''), (8, 'open', 't-section', 'This season', 'section', False, (), ''),
        (20, 'closed', 't-row', 'Season heading', 'div', False, (14,), ''), (20, 'open', 't-grid', 'Card grid', 'div', True, (14,), rp + '<span style="margin-left: 4px; font-size: 10px; color: #a9c8f7">Products</span>'),
        (32, 'open', 't-stack', 'Card', 'div', False, (14, 26), '<span style="margin-left: 6px; font-size: 10px; color: #939393">× 3</span>'),
        (44, None, 't-image', 'Image', 'img', False, (14, 26, 38), '<span style="margin-left: 6px; font-family: ' + MONO + '; font-size: 10px; color: #a9c8f7">{image}</span>'),
        (44, None, 't-para', 'Name', 'p', False, (14, 26, 38), '<span style="margin-left: 6px; font-family: ' + MONO + '; font-size: 10px; color: #a9c8f7">{name}</span>'),
        (44, None, 't-para', 'Price', 'p', False, (14, 26, 38), '<span style="margin-left: 6px; font-family: ' + MONO + '; font-size: 10px; color: #a9c8f7">{price}</span>'),
        (8, 'closed', 't-section', 'Footer', 'footer', False, (), '')]
set_tree(S, rows)

# Properties: Repeat group
row2 = lambda l, c: f'<div style="display: grid; grid-template-columns: 64px minmax(0, 1fr); gap: 8px; align-items: center"><span style="font-size: 11px; color: #a8a8a8">{l}</span>{c}</div>'
dd = lambda v, extra='': f(f'<span style="flex: 1">{v}</span>{extra}' + icon('chev-down', 10, '#939393', 1.5))
fmap = lambda el, fld_: f'<div style="height: 24px; display: flex; align-items: center; gap: 8px; font-size: 11px"><span style="width: 56px; color: #a8a8a8">{el}</span>{icon("chev-right", 10, "#6b6b6b", 1.5)}<span style="flex: 1; height: 22px; display: flex; align-items: center; gap: 6px; padding: 0 6px; border-radius: 2px; background: #2a2a2a">{icon("field", 11, "#a9c8f7")}<span style="font-family: {MONO}">{fld_}</span></span></div>'
rep = (row2('Repeat', f(icon('table', 12, '#a9c8f7') + '<span style="flex: 1">Products</span><span style="font-size: 10px; color: #939393">12 items</span>', 'box-shadow: inset 0 0 0 1px #2f80ed'))
       + row2('Show', pair(f('<span style="flex: 1">3</span><span style="font-size: 10px; color: #939393">items</span>'), dd('Newest first')))
       + row2('Only', dd('Season is Winter', '<span style="font-size: 10px; color: #939393; margin-right: 4px">5 match</span>'))
       + row2('When none', dd('Hide the section'))
       + '<div style="font-size: 10px; letter-spacing: 0.04em; color: #939393; margin-top: 2px">FIELDS IN THE CARD</div>' + fmap('Image', 'photo') + fmap('Name', 'name') + fmap('Price', 'price · €') + fmap('Link', 'shop/{slug}.html'))
item_pg = (row2('Item page', f(icon('file', 12, '#a8a8a8') + f'<span style="flex: 1; font-family: {MONO}; font-size: 11px">shop/tide-bowl.html</span><span style="font-size: 10px; color: #939393">+11</span>'))
           + '<div style="font-size: 10px; line-height: 14px; color: #939393">One page per product from the Product page design. Export writes them all; no server needed.</div>')
hdr = f'''<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{icon('t-grid', 16, '#a8a8a8')}<span style="flex: 1; font-weight: 500">Card grid</span><button style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 6px; color: #a8a8a8">Normal{icon('chev-down', 10, 'currentColor', 1.5)}</button></div>
<div style="padding-left: 24px; font-size: 11px; color: #a8a8a8">Grid · <span style="font-family: {MONO}; color: #939393">div</span> · repeats a card for each product</div></div>'''
S.props(panel(hdr + group('Repeat', rep) + group('Item pages', item_pg) + more([mp('Layout', 'Grid · 3 columns'), mp('Spacing', '32'), mp('Visibility', 'All sizes')])))
S.options('0', '0', '1312', 'Fill', 'Fit', 'Fit')

# INSET: the collection itself (opens as a tab like the design system)
hdrc = ['', 'photo', 'name', 'price', 'glaze', 'season', 'in stock']
rowsd = [('#d8cbb8', 'Tide bowl', '38', 'Sea green', 'Winter', True, True), ('#cfb9a3', 'Ember mug', '26', 'Iron red', 'Winter', True, False), ('#ddd2c2', 'Linen plate set', '84', 'Oat', 'Winter', False, False), ('#c9b89f', 'Moss cup', '22', 'Moss', 'Autumn', True, False)]
cell = lambda inner, extra='': f'<span style="height: 34px; display: flex; align-items: center; padding: 0 10px; border-right: 1px solid #303030; {extra}">{inner}</span>'
table = ('<div style="display: grid; grid-template-columns: 26px 60px minmax(0, 1.4fr) 70px minmax(0, 1fr) 80px 76px; border-top: 1px solid #303030">'
         + ''.join(f'<span style="height: 26px; display: flex; align-items: center; padding: 0 10px; border-right: 1px solid #303030; border-bottom: 1px solid #303030; font-family: {MONO}; font-size: 10px; color: #939393">{h}</span>' for h in hdrc)
         + ''.join(cell(f'<span style="font-size: 10px; color: #6b6b6b">{i + 1}</span>', 'border-bottom: 1px solid #2a2a2a;' + ('background: rgba(47,128,237,0.12);' if sel else '')) + cell(f'<span style="width: 34px; height: 24px; border-radius: 3px; background: {bg}"></span>', 'border-bottom: 1px solid #2a2a2a;' + ('background: rgba(47,128,237,0.12);' if sel else ''))
                   + cell(n, 'border-bottom: 1px solid #2a2a2a;' + ('background: rgba(47,128,237,0.12);' if sel else '')) + cell(f'€{p}', 'border-bottom: 1px solid #2a2a2a; justify-content: flex-end;' + ('background: rgba(47,128,237,0.12);' if sel else ''))
                   + cell(g, 'border-bottom: 1px solid #2a2a2a; color: #c8c8c8;' + ('background: rgba(47,128,237,0.12);' if sel else '')) + cell(se, 'border-bottom: 1px solid #2a2a2a; color: #c8c8c8;' + ('background: rgba(47,128,237,0.12);' if sel else ''))
                   + cell(f'<span style="width: 13px; height: 13px; border-radius: 3px; display: flex; align-items: center; justify-content: center; {"background: #246bcb;" if st else "box-shadow: inset 0 0 0 1px #6b6b6b;"}">{icon("check", 9, "#fff", 2) if st else ""}</span>', 'border-bottom: 1px solid #2a2a2a;' + ('background: rgba(47,128,237,0.12);' if sel else ''))
                   for i, (bg, n, p, g, se, st, sel) in enumerate(rowsd)) + '</div>')
inset = f'''<!-- INSET: Products collection -->
<div style="position: absolute; left: 330px; bottom: 44px; width: 640px; display: flex; flex-direction: column; gap: 8px; z-index: 35">
<span style="width: max-content; height: 20px; display: flex; align-items: center; padding: 0 8px; border-radius: 3px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; color: #a8a8a8">Inset · Project › Collections › Products (opens in its own tab)</span>
<div style="display: flex; flex-direction: column; {POP}; overflow: hidden">
<div style="height: 38px; display: flex; align-items: center; gap: 10px; padding: 0 12px">{icon('table', 14, '#a9c8f7')}<b style="font-weight: 600">Products</b><span style="font-size: 11px; color: #939393">12 items · products.json</span><span style="flex: 1"></span>
<button style="font-size: 11px; color: #a8a8a8">Import CSV…</button><button style="font-size: 11px; color: #a8a8a8">+ Field</button><button style="height: 24px; padding: 0 10px; border-radius: 4px; background: #246bcb; color: #fff; font-size: 11px; font-weight: 500">+ Product</button></div>
{table}<div style="height: 28px; display: flex; align-items: center; padding: 0 12px; font-size: 11px; color: #939393">+ 8 more · fields: photo (image), name (text), price (number, €), glaze (text), season (choice), in stock (yes / no), slug (from name)</div></div></div>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', inset + '\n<!-- ═══════════ TOP BAR v3')
S.status(['Page', 'Section · This season', 'Grid · Card grid'], 'Design the first card; the others follow · drag a field from the collection onto an element to link it', 'x 64 &#160;y 1180')
S.save('D57-Collections.dc.html')
print('ok')
