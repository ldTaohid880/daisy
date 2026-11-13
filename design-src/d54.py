import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *
P['shared'] = ('stroke', 'M8 1.8l6.2 6.2L8 14.2 1.8 8z M8 5.2L10.8 8 8 10.8 5.2 8z')
P['arrow'] = ('stroke', 'M3 8h10M9 4l4 4-4 4')
M_ = "font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 11px"
POP = 'background: #262626; border: 1px solid #454545; border-radius: 10px; box-shadow: 0 16px 48px rgba(0,0,0,0.55);'
cap = lambda t, d: f'<div style="margin-bottom: 10px"><div style="font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{d}</div></div>'
btn = lambda t, k='sec': f'<button style="height: 30px; padding: 0 14px; border-radius: 5px; white-space: nowrap; {"background: #246bcb; color: #fff; font-weight: 600;" if k == "pri" else ("color: #a8a8a8;" if k == "ghost" else ("background: #b62324; color: #fff; font-weight: 600;" if k == "danger" else "box-shadow: inset 0 0 0 1px #454545;"))}">{t}</button>'
fld = lambda inner, focus=False: f'<span style="height: 30px; display: flex; align-items: center; gap: 8px; padding: 0 10px; box-sizing: border-box; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px {"#2f80ed" if focus else "#3a3a3a"}">{inner}</span>'
field = lambda l, c, h='': f'<label style="display: flex; flex-direction: column; gap: 6px; min-width: 0"><span style="font-size: 11px; color: #a8a8a8">{l}</span>{c}{f"<span style=\"font-size: 11px; color: #939393\">{h}</span>" if h else ""}</label>'
chk = lambda on, t, d='': f'<div style="min-height: 26px; display: flex; align-items: center; gap: 8px"><span style="width: 14px; height: 14px; flex: none; border-radius: 3px; display: flex; align-items: center; justify-content: center; {"background: #246bcb;" if on else "box-shadow: inset 0 0 0 1px #6b6b6b;"}">{icon("check", 10, "#fff", 2) if on else ""}</span><span>{t}</span><span style="flex: 1"></span><span style="font-size: 11px; color: #939393; text-align: right">{d}</span></div>'
radio = lambda on, t, d='': f'<div style="display: flex; gap: 10px; padding: 9px 10px; border-radius: 5px; {"background: rgba(47,128,237,0.14); box-shadow: inset 0 0 0 1px #2f80ed;" if on else "background: #2a2a2a;"}"><span style="width: 14px; height: 14px; margin-top: 1px; flex: none; box-sizing: border-box; border-radius: 7px; {"border: 4px solid #2f80ed;" if on else "border: 1.5px solid #6b6b6b;"}"></span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 500">{t}</span>{f"<span style=\"font-size: 11px; color: #a8a8a8\">{d}</span>" if d else ""}</span></div>'
sec = lambda t: f'<div style="font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393; margin-top: 2px">{t}</div>'
def dialog(title, body, foot, w=600):
    return f'''<div style="width: {w}px; display: flex; flex-direction: column; font-size: 12px; line-height: 16px; {POP}">
<div style="height: 48px; display: flex; align-items: center; padding: 0 10px 0 18px; border-bottom: 1px solid #3a3a3a"><span style="flex: 1; font-size: 14px; font-weight: 600">{title}</span>{icon("close", 12, "#a8a8a8")}</div>
<div style="padding: 16px 18px; display: flex; flex-direction: column; gap: 12px">{body}</div>
<div style="height: 56px; display: flex; align-items: center; gap: 8px; padding: 0 18px; border-top: 1px solid #3a3a3a; background: #222222; border-radius: 0 0 10px 10px">{foot}</div></div>'''
sp = lambda n: f'<span style="display: inline-flex; align-items: center; gap: 4px">{icon("shared", 11, "#a9c8f7", 1.4)}{n}</span>'
link = lambda where, text, note='', shared=False: f'<div style="height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 8px; border-radius: 3px; background: #2a2a2a">{icon("shared", 12, "#a9c8f7", 1.4) if shared else icon("link", 12, "#a8a8a8")}<span style="color: #a8a8a8; white-space: nowrap">{where}</span><span style="flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">“{text}”</span><span style="font-size: 11px; color: #939393; white-space: nowrap">{note}</span></div>'

# 1 · New page
new = dialog('New page', grid := (
    f'<div style="display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 12px">{field("Page name", fld("<span style=\"background: rgba(47,128,237,0.35)\">Workshops</span>", True))}{field("File", fld(f"<span style=\"{M_}\">workshops.html</span><span style=\"flex: 1\"></span><span style=\"font-size: 10px; color: #3fb950\">free</span>"), "from the name")}</div>'
    + sec('START WITH') + '<div style="display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 8px">'
    + radio(True, 'One empty section', 'Like every new page') + radio(False, 'The layout of a page ▾', 'Sections and boxes, no text or images') + '</div>'
    + sec('SHARED PARTS') + chk(True, sp('Site header'), 'on 4 pages') + chk(True, sp('Site footer'), 'on 4 pages')
    + sec('NAVIGATION') + chk(True, 'Add “Workshops” to the Site header nav', 'after Journal · all pages')
    + '<div style="font-size: 11px; color: #939393">Title “Workshops — Halden” and description are set in Page settings; Ctrl N skips this dialog with the last choices.</div>'),
    '<span style="flex: 1; font-size: 11px; color: #939393">Opens in a new tab</span>' + btn('Cancel', 'ghost') + btn('Create page', 'pri'))

# 2 · Rename
ren = dialog('Rename page', (
    f'<div style="display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 12px">{field("Page name", fld("Stories", True), "was Journal")}{field("File", fld(f"<span style=\"{M_}\">stories.html</span>"), "was journal.html")}</div>'
    + sec('7 LINKS POINT TO THIS PAGE') + '<div style="display: flex; flex-direction: column; gap: 3px">'
    + link('Site header › Nav', 'Journal', 'shared · 4 pages', True) + link('Home › This season', 'Read the journal') + link('Shop › Tide bowl', 'How we glaze', '#tide') + '<div style="font-size: 11px; color: #939393; padding: 2px 8px">+ 4 more on Shop and Visit · <button style="font-size: 11px; color: #a9c8f7">Show all</button></div></div>'
    + chk(True, 'Update all 7 links to stories.html') + chk(True, 'Change link text that says “Journal” to “Stories”', '2 of 7')
    + chk(True, 'Keep the old address working', 'adds a redirect in Project settings')),
    '<span style="flex: 1; font-size: 11px; color: #939393">One undo step</span>' + btn('Cancel', 'ghost') + btn('Rename', 'pri'))

# 3 · Delete
dele = dialog('Delete Visit?', (
    '<span style="font-size: 12px; line-height: 18px; color: #c8c8c8">It goes to Recently deleted for 30 days. <b style="font-weight: 600; color: #e8e8e8">5 links</b> point to it.</span>'
    + '<div style="display: flex; flex-direction: column; gap: 3px">' + link('Site header', 'Book a visit', 'shared · 4 pages', True) + link('Site header › Nav', 'Visit', 'shared', True) + link('Home › Hero', 'Our process →', '#visit') + link('Shop › footer note', 'Come and see us') + '</div>'
    + sec('WHAT HAPPENS TO THEM') + radio(True, 'Point them to another page', f'{fld("Home · index.html " + icon("chev-down", 10, "#939393", 1.75))}'.replace('height: 30px', 'height: 26px; margin-top: 4px; width: 220px'))
    + radio(False, 'Remove the links, keep the text') + radio(False, 'Leave them', 'They will show as broken in the page check')
    + chk(True, 'Remove “Visit” from the Site header nav', 'all pages')),
    btn('Cancel', 'ghost') + '<span style="flex: 1"></span>' + btn('Delete page', 'danger'))

# 4 · Duplicate
dup = dialog('Duplicate Shop', (
    f'<div style="display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 12px">{field("Page name", fld("Shop · Winter", True))}{field("File", fld(f"<span style=\"{M_}\">shop-winter.html</span>"))}</div>'
    + chk(True, 'Copy the content', 'text and images') + chk(True, 'Copy page settings', 'title gets “· Winter”') + chk(False, 'Add to the Site header nav')
    + f'<div style="font-size: 11px; line-height: 16px; color: #939393">{sp("Site header")} and {sp("Site footer")} stay shared in the copy; changes made to them on Shop only are copied as changes.</div>'),
    '<span style="flex: 1"></span>' + btn('Cancel', 'ghost') + btn('Duplicate', 'pri'), w=560)

back = lambda d, h: f'<div style="position: relative; width: 880px; height: {h}px; border-radius: 6px; overflow: hidden; background: #181818; box-shadow: 0 0 0 1px #303030"><div style="position: absolute; inset: 0; background: linear-gradient(#141414 0 40px, #1b1b1b 40px 76px, #2a2a2a 76px); opacity: 0.6"></div><div style="position: absolute; inset: 0; background: rgba(0,0,0,0.45)"></div><div style="position: absolute; left: 50%; top: 24px; transform: translateX(-50%)">{d}</div></div>'
cells = [('1 · New page (Ctrl N)', 'Name and file, how it starts, which shared parts it gets and whether it joins the navigation. Opens in a new tab.', back(new, 560)),
         ('2 · Rename a page', 'Lists the links that point to the page and updates them, including the shared nav; the old address can keep working.', back(ren, 560)),
         ('3 · Delete a page', 'Shows the links that would break and what they become. The page goes to Recently deleted.', back(dele, 680)),
         ('4 · Duplicate a page', 'Copies content and settings; shared parts stay shared.', back(dup, 400))]
body = sheet_header('D-54', 'Pages · new, rename, delete, duplicate', 'Page dialogs from the Project panel, the page tab menu and File. Links between pages are kept working: renaming updates them, deleting asks what they become.')
body += '<div style="display: grid; grid-template-columns: repeat(2, 880px); gap: 48px 32px; align-items: start">' + ''.join(f'<div>{cap(t, d)}{c}</div>' for t, d, c in cells) + '</div>'
H = int(sys.argv[1]) if len(sys.argv) > 1 else 1700
open('/home/claude/daisy/project/D54-PageDialogs.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-54 Page dialogs', 1920, H, body))
print('ok')
