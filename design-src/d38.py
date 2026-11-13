import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

P['palette'] = ('stroke', 'M8 1.5a6.5 6.5 0 1 0 0 13c1 0 1.5-.6 1.5-1.4 0-1.2-1-1.3-1-2.3 0-.8.6-1.3 1.5-1.3h1.6a2.9 2.9 0 0 0 2.9-2.9C14.5 4 11.6 1.5 8 1.5z')
P['history'] = ('stroke', 'M3 8a5 5 0 1 0 1.5-3.5M3 2.5v3h3M8 5.5V8l2 1.5')
P['folder-open'] = ('stroke', 'M1.5 4V13h11l2-6H4l-2.5 6M1.5 4h4.5l1.5 1.5h5V7')
P['keyboard'] = ('stroke', 'M1.5 4.5h13v7h-13zM4 7h1M7 7h1M10 7h1M5 9.5h6')
P['book'] = ('stroke', 'M2.5 3h4a1.5 1.5 0 0 1 1.5 1.5V13a1.5 1.5 0 0 0-1.5-1.5h-4zM13.5 3h-4A1.5 1.5 0 0 0 8 4.5V13a1.5 1.5 0 0 1 1.5-1.5h4z')
P['bug'] = ('stroke', 'M5.5 5.5h5v5a2.5 2.5 0 0 1-5 0zM6 5.5a2 2 0 0 1 4 0M2.5 8h3M10.5 8h3M3 4.5l2.5 1.5M13 4.5l-2.5 1.5M3 12l2.5-1.5M13 12l-2.5-1.5')
P['scissors'] = ('stroke', 'M5 4.5a1.8 1.8 0 1 1-3.6 0 1.8 1.8 0 0 1 3.6 0zM5 11.5a1.8 1.8 0 1 1-3.6 0 1.8 1.8 0 0 1 3.6 0zM4.5 5.8L14 12M4.5 10.2L14 4')
P['paste'] = ('stroke', 'M5.5 2.5h5v2h-5zM4 3.5H3v10h10v-10h-1')

POP = 'background: #262626; border: 1px solid #454545; border-radius: 4px; box-shadow: 0 8px 24px rgba(0,0,0,0.45);'
def mi(t, kb='', ic=None, sub=False, dis=False, chk=None, hov=False, danger=False, note=''):
    col = '#4f4f4f' if dis else ('#ff938c' if danger else '#e8e8e8')
    lead = icon('check', 12, '#e8e8e8', 2) if chk else (icon(ic, 14, '#4f4f4f' if dis else '#a8a8a8') if ic else '')
    return (f'<div role="menuitem"{" aria-disabled=\"true\"" if dis else ""} style="height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 8px; border-radius: 3px; {"background: #333333;" if hov else ""} color: {col}">'
            f'<span style="width: 16px; display: flex; justify-content: center">{lead}</span><span style="flex: 1; white-space: nowrap">{t}{f"<span style=\"margin-left: 6px; color: #939393\">{note}</span>" if note else ""}</span>'
            f'<span style="font-size: 11px; color: {"#4f4f4f" if dis else "#939393"}; white-space: nowrap">{kb}</span>{icon("chev-right", 10, "#939393", 1.75) if sub else ""}</div>')
SEP = '<div role="separator" style="height: 1px; margin: 4px 0; background: #3a3a3a"></div>'
cap_ = lambda t: f'<div style="padding: 6px 8px 2px 32px; font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393">{t}</div>'
menu = lambda items, w=280, extra='': f'<div role="menu" style="width: {w}px; padding: 4px; box-sizing: border-box; {POP} {extra}">{"".join(items)}</div>'

FILE = [mi('New project…', 'Ctrl Alt N', 'folder'), mi('New page', 'Ctrl N', 'new-page'), mi('Open…', 'Ctrl O', 'folder-open'), mi('Open recent', sub=True, hov=True), SEP,
        mi('Save version…', 'Ctrl S', note='autosaved'), mi('Versions…', 'Ctrl Alt S', 'history'), SEP,
        mi('Import', sub=True, ic='upload'), mi('Export…', 'Ctrl Shift E', 'external'), SEP,
        mi('Page settings…', '', 'gear'), mi('Project settings…'), SEP, mi('Close page', 'Ctrl W'), mi('Close project'), mi('Back to Home', 'Ctrl Shift H')]
RECENT = [cap_('PROJECTS'), mi('Halden', ic='folder'), mi('Riverside Café', ic='folder'), mi('Portfolio 2026', ic='folder'), SEP, cap_('SINGLE FILES'), mi('promo-banner.html', ic='file'), mi('invite-card.html', ic='file'), SEP, mi('Clear recent')]
EDIT = [mi('Undo', 'Ctrl Z', 'undo', note='Change fill'), mi('Redo', 'Ctrl Shift Z', 'redo', dis=True), mi('History', '', 'history'), SEP,
        mi('Cut', 'Ctrl X', 'scissors'), mi('Copy', 'Ctrl C', 'copy'), mi('Copy as', sub=True, hov=True), mi('Paste', 'Ctrl V', 'paste'), mi('Paste inside', 'Ctrl Shift V'), mi('Paste style', 'Ctrl Alt V'), mi('Duplicate', 'Ctrl D'), mi('Delete', 'Del', 'trash'), SEP,
        mi('Select all', 'Ctrl A'), mi('Select same', sub=True), mi('Find and replace…', 'Ctrl H', 'search'), SEP, mi('Preferences…', 'Ctrl ,', 'gear')]
COPYAS = [mi('HTML'), mi('CSS', 'Ctrl Alt C'), mi('CSS variables used'), mi('Style', note='to paste on another element'), mi('Image (PNG)')]
ELEM = [mi('Wrap in', 'Ctrl G', 'box', sub=True), mi('Unwrap', 'Ctrl Shift G'), mi('Wrap in link', 'Ctrl K', 'link'), SEP,
        mi('Move earlier', 'Ctrl ['), mi('Move later', 'Ctrl ]'), mi('Placement', sub=True, hov=True, note='In flow'), SEP,
        mi('Add state', sub=True), mi('Animate…', ic='play'), mi('Save as preset…'), SEP,
        mi('Rename', 'F2'), mi('Lock', 'Ctrl L', 'lock'), mi('Hide', 'Ctrl Shift H', 'eye-off'), SEP, mi('Show code', 'Ctrl `', 'code'), mi('Delete element', 'Del', danger=True)]
PLACE = [mi('In flow', chk=True), mi('Free'), mi('Fixed to screen'), mi('Sticks when scrolling'), SEP, mi('Placement options…', ic='sliders')]
VIEW = [mi('Zoom in', 'Ctrl +', 'zoom'), mi('Zoom out', 'Ctrl −'), mi('Fit width', 'Shift 1'), mi('100%', 'Shift 0'), mi('Zoom to selection', 'Shift 2'), SEP,
        mi('Screen size', sub=True, hov=True, note='Desktop'), mi('Preview', 'Ctrl Enter', 'play'), mi('Outline view', 'Ctrl Y', 'outline'), SEP,
        mi('Rulers', 'Ctrl R', chk=True), mi('Guides', 'Ctrl ;', chk=True), mi('Layout grid', "Ctrl '"), mi('Fold line', chk=True), mi('Snap', 'Ctrl Shift ;', chk=True), SEP,
        mi('Panels', sub=True), mi('Code', 'Ctrl `', 'code'), mi('Timeline', 'Ctrl Alt T'), mi('Hide panels', 'Tab'), SEP, mi('Theme', sub=True, note='Dark')]
SCREEN = [mi('Desktop', '1440', 'desktop', chk=False), mi('Tablet', '768', 'tablet'), mi('Mobile', '390', 'phone'), SEP, mi('Rotate', 'Ctrl Alt R', dis=True), mi('Screen sizes…', ic='sliders')]
SCREEN[0] = SCREEN[0].replace('<span style="width: 16px; display: flex; justify-content: center">', '<span style="width: 16px; display: flex; justify-content: center">' + icon('check', 12, '#e8e8e8', 2) + '<!--', 1).replace('</span><span style="flex: 1; white-space: nowrap">Desktop', '--></span><span style="flex: 1; white-space: nowrap">Desktop', 1)
HELP = [mi('Search commands', 'Ctrl P', 'search'), mi('Keyboard shortcuts', 'Ctrl /', 'keyboard'), mi('Getting started', ic='book'), mi('Show tips again'), SEP,
        mi('What’s new', note='0.9'), mi('Report a problem…', ic='bug'), mi('Check for updates'), SEP, mi('About Daisy')]

daisy_btn = f'<span style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 6px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #2e2e2e">{daisy(18)}</span>'
NAMES = ['File', 'Edit', 'Element', 'View', 'Help']
X = {'File': 0, 'Edit': 37, 'Element': 75, 'View': 141, 'Help': 189}
def bar(open_, w):
    btns = ''.join(f'<button style="height: 28px; padding: 0 8px; border-radius: 4px; {"background: #333333; color: #e8e8e8;" if n == open_ else ""}">{n}</button>' for n in NAMES)
    return f'<div style="width: {w}px; height: 40px; display: flex; align-items: center; gap: 4px; padding: 0 8px; box-sizing: border-box; background: #141414; border-bottom: 1px solid #262626"> {daisy_btn}<nav style="display: flex; margin-left: 4px; color: #a8a8a8">{btns}</nav></div>'
def cell(open_, items, sub=None, sub_top=0, w=560, h=640, mw=280, sw=240):
    left = 40 + X[open_]
    subm = f'<div style="position: absolute; left: {left + mw - 4}px; top: {40 + 2 + sub_top}px">{menu(sub, sw)}</div>' if sub else ''
    return f'''<div style="position: relative; width: {w}px; height: {h}px; border-radius: 6px; background: #2a2a2a; box-shadow: 0 0 0 1px #303030">{bar(open_, w).replace("box-sizing: border-box;", "box-sizing: border-box; border-radius: 6px 6px 0 0;", 1)}
<div style="position: absolute; left: {left}px; top: 42px">{menu(items, mw)}</div>{subm}</div>'''
ROW = 28
cells = [
 ('File', 'Project and page files, versions, import and export. “Save version” names an autosave; work is never lost.', cell('File', FILE, RECENT, 3 * ROW, h=560)),
 ('Edit', 'Undo names the last change. Copy as gives HTML, CSS or the style; Select same picks every element with the same tag, class, fill or text style.', cell('Edit', EDIT, COPYAS, 6 * ROW + 8, h=560)),
 ('Element', 'Acts on the selection; items that do not apply are disabled, not hidden. Placement shows the current value.', cell("Element", ELEM, PLACE, 5 * ROW + 8, h=560, mw=260, sw=200)),
 ('View', 'Zoom, screen size, preview, canvas guides (ticked when on), panels and theme. Code and Timeline open the bottom drawer.', cell('View', VIEW, SCREEN, 5 * ROW + 8, h=760)),
 ('Help', 'Search commands opens the search bar on commands. Tips and getting started never block the canvas.', cell('Help', HELP, h=420)),
]
spec = '''<div style="display: flex; flex-direction: column; gap: 10px; font-size: 12px; line-height: 18px; color: #c8c8c8; max-width: 520px">
<div style="font-size: 13px; font-weight: 600; color: #e8e8e8">Behaviour</div>
<div>• <b style="font-weight: 600">Click</b> a menu name to open it; while one is open, <b style="font-weight: 600">moving the pointer</b> to another name opens that one. Click outside or <code>Esc</code> closes.</div>
<div>• <b style="font-weight: 600">Alt</b> (or F10) focuses the menu bar; ← → move between menus, ↑ ↓ through items, → opens a submenu, Enter runs.</div>
<div>• Submenus open after 150 ms of hover and stay open while the pointer moves diagonally towards them.</div>
<div>• Every command is also in the search bar (Ctrl P) with the same name and shortcut.</div>
<div>• Disabled items explain themselves in a tooltip, e.g. “Redo · nothing to redo”.</div>
<div>• In the Design system tab, Element is disabled, and the canvas items in View (zoom, screen size, guides) are disabled too.</div>
<div style="margin-top: 6px; font-size: 13px; font-weight: 600; color: #e8e8e8">Row anatomy (C-16)</div>
<div>28 high · 16 px icon column (icon, or ✓ when on) · label · optional muted note · shortcut right-aligned in <code>text-muted</code> · submenu chevron. Hover <code>#333333</code>. Danger items use <code>#ff938c</code>.</div></div>'''
body = sheet_header('D-38', 'Menus', 'What opens under File, Edit, Element, View and Help in the top bar, with one submenu each. Contents follow the project model and every tool designed so far.')
body += '<div style="display: grid; grid-template-columns: repeat(3, 560px); gap: 48px 56px; align-items: start">' + ''.join(f'<div><div style="margin-bottom: 10px"><div style="font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{d}</div></div>{c}</div>' for t, d, c in cells) + f'<div style="padding-top: 26px">{spec}</div></div>'
H = int(sys.argv[1]) if len(sys.argv) > 1 else 1700
open('/home/claude/daisy/project/D38-Menus.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-38 Menus', 1920, H, body))
print('ok')
