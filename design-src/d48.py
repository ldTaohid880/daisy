import sys
sys.path.insert(0, '/home/claude/ds')
_src = open('/home/claude/ds/d38.py').read(); G = {}; exec(_src[:_src.index('FILE = [')], G)
from lib import *
mi, SEP, menu, cap_, POP = G['mi'], G['SEP'], G['menu'], G['cap_'], G['POP']
P.update({k: v for k, v in G['P'].items()})
P['target'] = ('stroke', 'M8 1.5v3M8 11.5v3M1.5 8h3M11.5 8h3M8 5.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5z')
P['palette'] = ('stroke', 'M8 1.5a6.5 6.5 0 1 0 0 13c1 0 1.5-.6 1.5-1.4 0-1.2-1-1.3-1-2.3 0-.8.6-1.3 1.5-1.3h1.6a2.9 2.9 0 0 0 2.9-2.9C14.5 4 11.6 1.5 8 1.5z')
cap = lambda t, d: f'<div style="margin-bottom: 10px"><div style="font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{d}</div></div>'
ptr = '<svg width="16" height="20" viewBox="0 0 16 20" aria-hidden="true" style="position: absolute"><path d="M2 1v15l4-4 3 6 2-1-3-6h5z" fill="#fff" stroke="#1d1a16" stroke-width="1.4"/></svg>'
head = lambda t: f'<div style="padding: 6px 8px 4px; display: flex; align-items: center; gap: 6px; font-size: 11px; color: #939393; border-bottom: 1px solid #3a3a3a; margin: -4px -4px 4px; padding-left: 12px">{t}</div>'

# 1 · element on the canvas (Hero title), with Select layer submenu
EL = [head('Heading · h1 · Hero title'), mi('Cut', 'Ctrl X', 'scissors'), mi('Copy', 'Ctrl C', 'copy'), mi('Paste', 'Ctrl V', 'paste'), mi('Paste inside', 'Ctrl Shift V', dis=True), mi('Duplicate', 'Ctrl D'), SEP,
      mi('Copy style', 'Ctrl Alt C'), mi('Paste style', 'Ctrl Alt V'), SEP, mi('Wrap in', 'Ctrl G', 'box', sub=True), mi('Wrap in link', 'Ctrl K', 'link'), SEP,
      mi('Select layer', sub=True, hov=True), mi('Add state', sub=True, ic='target'), mi('Placement', sub=True, note='In flow'), SEP,
      mi('Rename', 'F2'), mi('Lock', 'Ctrl L', 'lock'), mi('Hide', 'Ctrl Shift H', 'eye-off'), mi('Show code', 'Ctrl `', 'code'), SEP, mi('Delete', 'Del', 'trash', danger=True)]
SEL = [cap_('UNDER THE POINTER · DEEPEST FIRST'), mi('Hero title', 'h1', 't-heading', chk=True), mi('Hero text', 'div', 't-stack'), mi('Hero grid', 'div', 't-grid'), mi('Hero', 'section', 't-section'), mi('Page', 'body', 'file')]
def canvas_cell():
    page = '''<div style="position: absolute; left: 20px; top: 20px; width: 520px; height: 600px; background: #f6f1ea; color: #1d1a16; overflow: hidden">
<div style="position: absolute; left: 30px; top: 70px; width: 300px; font: 600 38px/1.05 'Fraunces', serif; outline: 1.5px solid #2f80ed; outline-offset: 3px">Hand-thrown ceramics for everyday tables</div></div>'''
    return f'''<div style="position: relative; width: 880px; height: 760px; border-radius: 6px; overflow: hidden; background: #2a2a2a; box-shadow: 0 0 0 1px #303030">{page}
<div style="position: absolute; left: 170px; top: 130px">{ptr}</div>
<div style="position: absolute; left: 182px; top: 140px">{menu(EL, 268)}</div>
<div style="position: absolute; left: 446px; top: {140 + 4 + 28 * 10 + 9 * 3 - 4}px">{menu(SEL, 230)}</div></div>'''

# 2 · empty workspace
WS = [head('Workspace'), mi('Paste', 'Ctrl V', 'paste'), mi('Select all', 'Ctrl A'), SEP, mi('Fit width', 'Shift 1'), mi('100%', 'Shift 0'), mi('Screen size', sub=True, note='Desktop'), SEP,
      mi('Rulers', 'Ctrl R', chk=True), mi('Guides', 'Ctrl ;', chk=True), mi('Layout grid', "Ctrl '"), SEP, mi('Page settings…', '', 'gear')]
def ws_cell():
    return f'''<div style="position: relative; width: 420px; height: 470px; border-radius: 6px; overflow: hidden; background: #2a2a2a; box-shadow: 0 0 0 1px #303030">
<div style="position: absolute; left: 260px; top: 0; bottom: 0; width: 200px; background: #f6f1ea"></div>
<div style="position: absolute; left: 30px; top: 30px">{ptr}</div><div style="position: absolute; left: 42px; top: 40px">{menu(WS, 240)}</div></div>'''

# 3 · Layers row
LY = [head('Card 1 · div · 3 children'), mi('Rename', 'F2'), mi('Select children'), mi('Select same', sub=True, note='class .card'), SEP,
      mi('Collapse all inside'), mi('Expand all inside'), SEP, mi('Wrap in', 'Ctrl G', 'box', sub=True), mi('Unwrap', 'Ctrl Shift G'), mi('Duplicate', 'Ctrl D'), SEP,
      mi('Lock', 'Ctrl L', 'lock'), mi('Hide', 'Ctrl Shift H', 'eye-off'), mi('Show on canvas', 'Shift 2', 'zoom'), SEP, mi('Delete', 'Del', 'trash', danger=True)]
def tree_row(pad, name, tag, sel=False):
    return f'<div style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 {pad}px; {"background: rgba(47,128,237,0.18); box-shadow: inset 0 0 0 1px #2f80ed;" if sel else ""}">{icon("t-stack", 13, "#a8a8a8")}<span style="flex: 1">{name}</span><span style="font-size: 11px; color: #939393">{tag}</span></div>'
def layers_cell():
    rows = ''.join(tree_row(20 + 12 * d, n, t, s) for d, n, t, s in [(0, 'This season', 'section', False), (1, 'Card grid', 'div', False), (2, 'Card 1', 'div', True), (2, 'Card 2', 'div', False), (2, 'Card 3', 'div', False)])
    return f'''<div style="position: relative; width: 420px; height: 600px; border-radius: 6px; overflow: hidden; background: #1f1f1f; box-shadow: 0 0 0 1px #303030">
<div style="height: 32px; display: flex; align-items: center; gap: 16px; padding: 0 12px; border-bottom: 1px solid #303030; font-weight: 500">Layers<span style="color: #a8a8a8">Elements</span><span style="color: #a8a8a8">Assets</span></div>
<div style="width: 260px; padding-top: 6px">{rows}</div>
<div style="position: absolute; left: 110px; top: 88px">{ptr}</div><div style="position: absolute; left: 122px; top: 98px">{menu(LY, 280)}</div></div>'''

# 4 · page tab
TB = [head('Shop · shop.html · unsaved'), mi('Save version…', 'Ctrl S'), mi('Page settings…', '', 'gear'), mi('Preview', 'Ctrl Enter', 'play'), SEP,
      mi('Duplicate page'), mi('Rename page…'), mi('Copy address', note='halden.studio/shop'), mi('Show in Project'), SEP,
      mi('Close', 'Ctrl W'), mi('Close others'), mi('Close tabs to the right'), mi('Close saved tabs')]
def tab_cell():
    tab = lambda n, fn, on=False: f'<span style="height: 32px; display: flex; align-items: center; gap: 8px; padding: 0 12px; border-right: 1px solid #262626; {"background: #333333; color: #e8e8e8;" if on else "color: #a8a8a8;"}">{n}<span style="font-family: {MONO}; font-size: 11px; color: #939393">{fn}</span>{"<span style=\"width: 7px; height: 7px; border-radius: 4px; background: #a8a8a8\"></span>" if on else ""}</span>'
    return f'''<div style="position: relative; width: 420px; height: 470px; border-radius: 6px; overflow: hidden; background: #2a2a2a; box-shadow: 0 0 0 1px #303030">
<div style="height: 32px; display: flex; background: #181818; border-bottom: 1px solid #2a2a2a">{tab('Home', 'index.html')}{tab('Shop', 'shop.html', True)}</div>
<div style="position: absolute; left: 150px; top: 14px">{ptr}</div><div style="position: absolute; left: 162px; top: 24px">{menu(TB, 248)}</div></div>'''

# 5 · Project panel row (a page)
PJ = [head('Journal · journal.html'), mi('Open', 'Enter'), mi('Open in a new tab'), SEP, mi('New page', 'Ctrl N', 'new-page'), mi('Duplicate'), mi('Rename…', 'F2'), mi('Set as home page', note='index.html is now'), SEP,
      mi('Page settings…', '', 'gear'), mi('Export this page…', '', 'external'), mi('Show in folder', ic='folder'), SEP, mi('Delete page…', 'Del', 'trash', danger=True)]
def project_cell():
    row = lambda n, fn, on=False: f'<div style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 44px; {"background: rgba(47,128,237,0.18); box-shadow: inset 0 0 0 1px #2f80ed;" if on else ""}">{icon("file", 13, "#a8a8a8")}<span style="flex: 1">{n}</span><span style="font-family: {MONO}; font-size: 11px; color: #939393">{fn}</span></div>'
    return f'''<div style="position: relative; width: 420px; height: 600px; border-radius: 6px; overflow: hidden; background: #1f1f1f; box-shadow: 0 0 0 1px #303030">
<div style="height: 32px; display: flex; align-items: center; padding: 0 12px; border-bottom: 1px solid #303030; font-weight: 500">Project</div>
<div style="width: 260px; padding-top: 4px"><div style="height: 24px; display: flex; align-items: center; padding: 0 12px 0 20px; color: #a8a8a8">Pages</div>{row('Home', 'index.html')}{row('Shop', 'shop.html')}{row('Journal', 'journal.html', True)}{row('Visit', 'visit.html')}</div>
<div style="position: absolute; left: 120px; top: 88px">{ptr}</div><div style="position: absolute; left: 132px; top: 98px">{menu(PJ, 272)}</div></div>'''

# 6 · Swatch / token
SW = [head('brand · #B5532D · token'), mi('Apply to fill', 'Click'), mi('Apply to text colour', 'Alt click'), mi('Apply to border'), SEP,
      mi('Select all uses', note='18'), mi('Edit token…', '', 'palette'), mi('Copy', sub=True, note='hex · var()'), SEP, mi('Replace and delete…', danger=True)]
def swatch_cell():
    tiles = ''.join(f'<span style="width: 24px; height: 24px; border-radius: 2px; background: {c}; {"outline: 2px solid #2f80ed; outline-offset: 1px;" if i == 0 else ""}"></span>' for i, c in enumerate(['#b5532d', '#1d1a16', '#f6f1ea', '#e7d9c7', '#5f6b4e']))
    return f'''<div style="position: relative; width: 420px; height: 320px; border-radius: 6px; overflow: hidden; background: #1f1f1f; box-shadow: 0 0 0 1px #303030">
<div style="height: 32px; display: flex; align-items: center; gap: 16px; padding: 0 12px; border-bottom: 1px solid #303030; font-weight: 500">Swatches<span style="color: #a8a8a8">History</span></div>
<div style="padding: 10px 12px; display: flex; gap: 6px">{tiles}</div>
<div style="position: absolute; left: 22px; top: 58px">{ptr}</div><div style="position: absolute; left: 34px; top: 68px">{menu(SW, 270)}</div></div>'''

cells = [('1 · Element on the canvas', 'Right-click the Hero title. Select layer lists every element under the pointer, deepest first; hovering a row outlines it on the canvas. Items that do not apply are disabled.', canvas_cell(), 'span'),
         ('2 · Empty workspace', 'Outside the page: paste, select all, zoom, screen size and canvas guides.', ws_cell(), ''),
         ('3 · Layers row', 'Tree actions first (select children, select same class, collapse and expand all inside), then the element actions.', layers_cell(), ''),
         ('4 · Page tab', 'Page actions and the usual tab closing commands.', tab_cell(), ''),
         ('5 · Project panel · page', 'Open, duplicate, rename, make it the home page, page settings, export and delete (asks first).', project_cell(), ''),
         ('6 · Swatch or token', 'Apply to fill, text or border; select every use; edit the token; delete only by replacing it.', swatch_cell(), '')]
body = sheet_header('D-48', 'Right-click menus', 'The context menus for the canvas, the empty workspace, a Layers row, a page tab, a Project page and a swatch. Same rows, names and shortcuts as the menu bar (D-38); a header line says what was clicked.')
body += '<div style="display: grid; grid-template-columns: 880px 420px 420px; gap: 48px 36px; align-items: start">'
body += f'<div style="grid-row: span 2">{cap(cells[0][0], cells[0][1])}{cells[0][2]}</div>'
body += ''.join(f'<div>{cap(t, d)}{c}</div>' for t, d, c, _ in cells[1:])
body += '<div style="padding-top: 26px; font-size: 12px; line-height: 18px; color: #c8c8c8; max-width: 420px"><b style="font-weight: 600; color: #e8e8e8">Behaviour</b><br>Right-click selects what is under the pointer first (unless it is already part of the selection). <code>Shift F10</code> or the Menu key opens the same menu for the selection. Menus open at the pointer and flip to stay on screen. With several elements selected, the header reads “3 elements” and only shared actions show (D-11).</div></div>'
H = int(sys.argv[1]) if len(sys.argv) > 1 else 1800
open('/home/claude/daisy/project/D48-ContextMenus.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-48 Right-click menus', 1920, H, body))
print('ok')
