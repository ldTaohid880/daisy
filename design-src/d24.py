from screen import *

S = Screen('Daisy · D-24 Layers interactions')
S.remove_h1_overlay()
S.unselect_h1_row()

# ---------------- canvas: Hero text is the drop target ----------------
S.rep('<!-- parent-of-selection outline: Hero text -->\n<div aria-hidden="true" style="position: absolute; top: -1px; left: -1px; right: -1px; bottom: -1px; border: 1.18px dashed rgba(47,128,237,0.6); pointer-events: none"></div>',
      '<!-- drop target: Hero text -->\n<div aria-hidden="true" style="position: absolute; top: -1px; left: -1px; right: -1px; bottom: -1px; border: 1.76px solid #2f80ed; background: rgba(47,128,237,0.06); pointer-events: none">'
      '<span style="position: absolute; left: -1.76px; bottom: calc(100% + 2px); height: 21px; padding: 0 5px; display: flex; align-items: center; background: #246bcb; color: #fff; font: 500 13px/1 \'Inter\', sans-serif; white-space: nowrap">into Hero text · last</span>'
      '<span style="position: absolute; left: 0; right: 0; bottom: 6px; height: 2.35px; background: #2f80ed"><span style="position: absolute; left: -1.2px; top: -2.35px; width: 2.35px; height: 7px; background: #2f80ed"></span><span style="position: absolute; right: -1.2px; top: -2.35px; width: 2.35px; height: 7px; background: #2f80ed"></span></span></div>')

# ---------------- layers: drag in progress ----------------
G = lambda *x: x
rows = [
    (8, 'closed', 't-section', 'Header', 'header', False, (), ''),
    (8, 'open', 't-section', 'Hero', 'section', False, (), ''),
    (20, 'open', 't-grid', 'Hero grid', 'div', False, G(14), ''),
    (32, 'open', 't-stack', 'Hero text', 'div', False, G(14, 26), ''),
    (44, None, 't-para', '“Small-batch stoneware…”', 'p', False, G(14, 26, 38), ''),
    (44, None, 't-heading', 'Hero title', 'h1', False, G(14, 26, 38), ''),
    (44, None, 't-para', '“Each piece is…”', 'p', False, G(14, 26, 38), ''),
    (44, 'closed', 't-row', 'Hero buttons', 'div', False, G(14, 26, 38), ''),
    (32, None, 't-image', 'Hero image', 'img', False, G(14, 26), icon('warning', 12, '#d29922', 1.25, 'Accessibility issue')),
    (8, 'open', 't-section', 'This season', 'section', False, (), ''),
    (20, 'open', 't-grid', 'Card grid', 'div', False, G(14), ''),
    (32, 'closed', 't-stack', 'Card 1', 'div', False, G(14, 26), ''),
    (32, 'closed', 't-stack', 'Card 2', 'div', True, G(14, 26), ''),
    (32, 'closed', 't-stack', 'Card 3', 'div', False, G(14, 26), ''),
    (8, 'closed', 't-section', 'Footer', 'footer', False, (), ''),
]
set_tree(S, rows)
s = S.s
# Hero text row: drop-inside highlight
k = s.index('>Hero text</span>'); a = s.rindex('<div role="treeitem"', 0, k)
s = s[:a] + s[a:].replace('<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 32px; ',
                          '<div role="treeitem" aria-label="Drop inside Hero text" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 32px; background-color: rgba(47,128,237,0.16); box-shadow: inset 0 0 0 1.5px #2f80ed; ', 1)
# insertion line after Hero buttons (last child of Hero text)
k = s.index('>Hero buttons</span>'); e = s.index('</div>', k) + 6
s = s[:e] + '<div aria-hidden="true" style="position: relative; height: 0"><span style="position: absolute; left: 56px; right: 12px; top: -1px; height: 2px; background: #2f80ed"><span style="position: absolute; left: -4px; top: -3px; width: 8px; height: 8px; box-sizing: border-box; border-radius: 50%; border: 2px solid #2f80ed; background: #1f1f1f"></span></span></div>' + s[e:]
# Card 2: the dragged source, dimmed
k = s.index('>Card 2</span>'); a = s.rindex('<div role="treeitem"', 0, k)
s = s[:a] + s[a:].replace('<div role="treeitem" aria-selected="true" style="', '<div role="treeitem" aria-selected="true" style="opacity: 0.45; ', 1)
S.s = s
# ghost of the dragged row under the pointer
ghost = f'''<!-- drag ghost -->
<div aria-hidden="true" style="position: absolute; left: 176px; top: 556px; height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 10px 0 8px; border-radius: 4px; background: #2f80ed; color: #fff; font-size: 12px; box-shadow: 0 6px 16px rgba(0,0,0,0.45); z-index: 40">{icon('t-stack', 13, '#fff')}Card 2<span style="font-size: 11px; opacity: 0.8">div</span></div>
<svg aria-hidden="true" width="18" height="18" viewBox="0 0 16 16" style="position: absolute; left: 170px; top: 548px; z-index: 41"><path d="M3 2l9.5 6.5-4.2 1 2.4 4.4-1.8 1-2.4-4.4-3.5 2.7z" fill="#fff" stroke="#1d1a16" stroke-width="1.1" stroke-linejoin="round"></path></svg>'''

# ☰ Layers menu, open
mi = lambda t, sub='', on=None, kb='': (f'<button role="menuitemcheckbox" aria-checked="{str(bool(on)).lower()}" style="width: 100%; min-height: 28px; display: flex; align-items: center; gap: 8px; padding: 4px 8px; box-sizing: border-box; border-radius: 3px; text-align: left">'
                                       f'<span style="width: 12px">{icon("check", 12) if on else ""}</span><span style="flex: 1"><span style="display: block">{t}</span>{f"<span style=\"display: block; font-size: 10px; line-height: 14px; color: #939393\">{sub}</span>" if sub else ""}</span><span style="font-size: 11px; color: #939393">{kb}</span></button>')
menu = f'''<!-- INSET: Layers ☰ menu -->
<div aria-label="Inset: Layers menu" style="position: absolute; left: 356px; top: 760px; width: 300px; padding: 12px; box-sizing: border-box; background: #1f1f1f; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 8px 24px rgba(0,0,0,0.45); z-index: 30">
<div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 11px"><span style="font-weight: 600">Inset · ☰ Layers menu</span><span style="color: #939393">at rest</span></div>
<div role="menu" aria-label="Layers options" style="padding: 4px; box-sizing: border-box; border-radius: 6px; background: #262626; border: 1px solid #454545">
{mi('Show inline parts', 'Bold words, links and line breaks inside text', False)}
{mi('Outline view', 'Only headings and landmarks', False, 'Alt+O')}
{mi('Show hidden elements', 'Dimmed, with a crossed-out eye', True)}
<div style="height: 1px; background: #3a3a3a; margin: 4px 0"></div>
{mi('Expand to selection', '', None, 'Alt+→')}{mi('Collapse all', '', None, 'Alt+←')}
<div style="height: 1px; background: #3a3a3a; margin: 4px 0"></div>
{mi('Show tags', 'div, p, h1 on the right', True)}
</div></div>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', ghost + menu + '\n<!-- ═══════════ TOP BAR v3')
# menu button pressed
S.rep('<button aria-label="Layers options"', '<button aria-label="Layers options" aria-expanded="true" data-pressed') if '<button aria-label="Layers options"' in S.s else None

S.options('—', '—', '416', 'Fill', '380', 'Fit')
S.props(panel(header('t-stack', 'Card 2', 'Box', 'div')
              + '<div style="padding: 8px 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #303030; background: #232323; font-size: 11px; color: #c8c8c8">' + icon('info', 12, '#58a6ff', 1.25) + '<span style="flex: 1">Moving to <b style="font-weight: 600; color: #e8e8e8">Hero text</b> · last child. It will take Hero text\'s width.</span></div>'
              + group('Size', pair(f('<span style="font-size: 11px; color: #939393; padding-left: 11px">W</span><span style="flex: 1; color: #939393">416</span>' + tagc('Fill')), f('<span style="font-size: 11px; color: #939393; padding-left: 11px">H</span><span style="flex: 1; color: #939393">380</span>' + tagc('Fit'))))
              + more([mp('Layout', 'Stack ↓ · gap 8'), mp('Placement', 'In flow'), mp('Spacing', '16'), mp('Fill', 'white'), mp('Border', 'radius 12'), mp('Effects')])))
S.status(['Page', 'This season', 'Card grid', 'Card 2'], 'Drop inside Hero text · move up or down to drop before or after · Alt drops beside instead of inside · Esc cancels', 'x 640 &#160;y 520')
S.save('D24-Layers.dc.html')
print('ok')
