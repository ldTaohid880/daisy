import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

P['restore'] = ('stroke', 'M3 8a5 5 0 1 0 1.5-3.5M3 2.5v3h3')
P['pin'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
pop = 'background: #2a2a2a; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 10px 28px rgba(0,0,0,0.5);'
cap = lambda t, desc: f'<div style="display: flex; flex-direction: column; gap: 2px; margin-bottom: 10px"><div style="font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{desc}</div></div>'
btn = lambda t, primary=False, ic='': f'<button style="height: 26px; display: flex; align-items: center; gap: 6px; padding: 0 12px; border-radius: 5px; font-size: 11px; {"background: #246bcb; color: #fff; font-weight: 600;" if primary else "color: #e8e8e8; box-shadow: inset 0 0 0 1px #454545;"}">{ic}{t}</button>'
def ver(time, title, sub, kind='auto', on=False, extra=''):
    dot = {'now': 'background: #3fb950;', 'named': 'background: #e8e8e8;', 'auto': 'box-shadow: inset 0 0 0 1.5px #6b6b6b;'}[kind]
    return (f'<div style="position: relative; padding: 7px 8px; display: flex; gap: 8px; border-radius: 5px; {"background: rgba(47,128,237,0.16); box-shadow: inset 0 0 0 1px #2f80ed;" if on else ""}">'
            f'<span style="width: 7px; height: 7px; margin-top: 5px; flex: none; border-radius: 4px; {dot}"></span>'
            f'<span style="flex: 1; min-width: 0"><span style="display: flex; gap: 6px"><span style="flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; {"font-weight: 600;" if kind == "named" else ""}">{title}</span><span style="font-size: 10px; color: #939393">{time}</span></span>'
            f'<span style="display: block; font-size: 10px; line-height: 14px; color: #939393; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{sub}</span></span>{extra}</div>')
day = lambda t: f'<div style="padding: 8px 8px 3px; font-size: 9px; font-weight: 600; letter-spacing: 0.06em; color: #6b6b6b">{t}</div>'
base_list = lambda sel=3, extra_rows=None: (day('TODAY') + ver('now', 'Current', 'Unsaved · Hero title, Book a visit', 'now', sel == 0)
    + ver('13:05', 'Before the Tablet pass', 'Named · 14 changes', 'named', sel == 1) + ver('11:20', 'Autosave', '6 changes · season cards', on=sel == 2)
    + day('YESTERDAY') + ver('16:40', 'Autosave', '3 changes · headline, button', on=sel == 3) + ver('14:02', 'First full draft', 'Named · 4 pages', 'named', sel == 4))
def dlg(list_html, detail, h=330, footer=None, head_right=''):
    foot = footer if footer is not None else f'<span style="font-size: 10px; color: #939393">The current state is saved first</span><span style="flex: 1"></span>{btn("Restore as a copy")}{btn("Restore", True)}'
    return f'''<div style="height: {h}px; display: flex; flex-direction: column; background: #262626; border: 1px solid #454545; border-radius: 10px; overflow: hidden; box-shadow: 0 12px 32px rgba(0,0,0,0.45); font-size: 12px; position: relative">
<div style="height: 40px; flex: none; display: flex; align-items: center; gap: 10px; padding: 0 12px 0 16px; border-bottom: 1px solid #3a3a3a"><b style="font-weight: 600">Versions</b><span style="font-size: 11px; color: #939393">Halden</span><span style="flex: 1"></span>{head_right}{icon('close', 13, '#a8a8a8')}</div>
<div style="flex: 1; min-height: 0; display: flex"><div style="width: 250px; flex: none; padding: 4px 6px; box-sizing: border-box; border-right: 1px solid #3a3a3a; background: #222222; overflow: hidden">{list_html}</div>
<div style="flex: 1; min-width: 0; padding: 12px 14px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px; position: relative">{detail}</div></div>
<div style="height: 44px; flex: none; display: flex; align-items: center; gap: 8px; padding: 0 14px; border-top: 1px solid #3a3a3a; background: #222222">{foot}</div></div>'''
mini = lambda title, btn_c='#b5532d', w=200, extra='': f'''<div style="position: relative; width: {w}px; height: 130px; border-radius: 5px; overflow: hidden; background: #f6f1ea; box-shadow: 0 0 0 1px #3a3a3a">
<span style="position: absolute; left: 8px; top: 6px; font: 600 7px/1 Georgia, serif; color: #1d1a16">Halden</span><span style="position: absolute; right: 8px; top: 4px; width: 22px; height: 7px; border-radius: 4px; background: #b5532d"></span>
<span style="position: absolute; left: 8px; top: 30px; width: 46%; font: 600 13px/1.05 Georgia, serif; color: #1d1a16">{title}</span>
<span style="position: absolute; left: 8px; top: 86px; width: 34px; height: 8px; border-radius: 4px; background: {btn_c}"></span>
<span style="position: absolute; right: 8px; top: 24px; width: 44%; height: 76px; border-radius: 4px; background: #e6dccd"></span>
<span style="position: absolute; left: 0; right: 0; bottom: 0; height: 24px; background: #e7d9c7"></span>{extra}</div>'''
ptabs = lambda sel, notes: '<div style="display: flex; gap: 2px; padding: 2px; border-radius: 5px; background: #1f1f1f; font-size: 11px">' + ''.join(f'<span style="height: 22px; display: flex; align-items: center; gap: 5px; padding: 0 9px; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #a8a8a8;"}">{t}{f"<span style=\"height: 14px; padding: 0 4px; border-radius: 7px; background: #2f80ed; color: #fff; font-size: 9px; line-height: 14px\">{n}</span>" if n else ""}</span>' for i, (t, n) in enumerate(notes)) + '</div>'
pages = [('Home', 2), ('Shop', 1), ('Journal', 0), ('Visit', 0)]

# 1 · This version (one page, full width)
d1 = (f'<div style="display: flex; align-items: center; gap: 8px"><b style="font-weight: 600">Autosave · Yesterday 16:40</b><span style="flex: 1"></span>{ptabs(0, pages)}</div>'
      + f'<div style="flex: 1; display: flex; justify-content: center">{mini("Ceramics made by the river", "#1d1a16", 520).replace("height: 130px", "height: 196px")}</div>')
S1 = dlg(base_list(), d1)

# 2 · Naming the current version
name_row = (f'<div style="padding: 7px 8px; border-radius: 5px; background: rgba(47,128,237,0.16); box-shadow: inset 0 0 0 1px #2f80ed; display: flex; flex-direction: column; gap: 6px">'
            f'<div style="height: 24px; display: flex; align-items: center; padding: 0 8px; border-radius: 3px; background: #1b1b1b; box-shadow: inset 0 0 0 1px #2f80ed">Ready for the client review<span style="display: inline-block; width: 1px; height: 12px; margin-left: 1px; background: #e8e8e8"></span></div>'
            f'<div style="height: 36px; padding: 4px 8px; box-sizing: border-box; border-radius: 3px; background: #1b1b1b; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; color: #939393">Add a note (optional)</div>'
            f'<div style="display: flex; gap: 6px; justify-content: flex-end"><span style="font-size: 10px; color: #939393; margin-right: auto; align-self: center">Enter saves · Esc cancels</span>{btn("Save", True)}</div></div>')
S2 = dlg(day('TODAY') + name_row + ver('13:05', 'Before the Tablet pass', 'Named · 14 changes', 'named') + ver('11:20', 'Autosave', '6 changes · season cards'),
         f'<div style="font-size: 11px; line-height: 16px; color: #c8c8c8">Naming the current state keeps it for good. Autosaves are removed after 30 days.</div>{mini("Hand-thrown ceramics for everyday tables", w=360).replace("height: 130px", "height: 170px")}',
         head_right=f'<span style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; background: #333333; box-shadow: inset 0 0 0 1px #2f80ed; font-size: 11px; color: #e8e8e8">{icon("pin", 11)}Name the current version</span>')

# 3 · Confirm restore
confirm = f'''<div style="position: absolute; left: 14px; right: 14px; bottom: 12px; padding: 12px 14px; display: flex; align-items: center; gap: 12px; border-radius: 6px; {pop}">
{icon('restore', 16, '#a9c8f7')}<div style="flex: 1; font-size: 11px; line-height: 16px"><b style="font-weight: 600; color: #e8e8e8">Restore Yesterday 16:40?</b><div style="color: #a8a8a8">All 4 pages go back to this version. The current state is saved first as “Before restore · 13:38”.</div></div>{btn('Cancel')}{btn('Restore', True)}</div>'''
S3 = dlg(base_list(), mini('Ceramics made by the river', '#1d1a16', 420).replace('height: 130px', 'height: 150px') + confirm, footer='<span style="font-size: 10px; color: #939393">Confirming…</span>')

# 4 · After restore (toast in the editor)
toast_scene = f'''<div style="position: relative; height: 330px; border-radius: 10px; overflow: hidden; background: #2a2a2a; box-shadow: 0 0 0 1px #3a3a3a">
<div style="position: absolute; left: 30px; top: 24px; right: 30px; bottom: 60px; border-radius: 4px; background: #f6f1ea; overflow: hidden">
<span style="position: absolute; left: 24px; top: 40px; width: 50%; font: 600 28px/1.05 Georgia, serif; color: #1d1a16">Ceramics made by the river</span>
<span style="position: absolute; left: 24px; top: 150px; width: 90px; height: 22px; border-radius: 11px; background: #1d1a16"></span>
<span style="position: absolute; right: 24px; top: 30px; width: 40%; height: 160px; border-radius: 6px; background: #e6dccd"></span></div>
<div role="status" style="position: absolute; left: 50%; bottom: 16px; transform: translateX(-50%); height: 36px; display: flex; align-items: center; gap: 12px; padding: 0 8px 0 14px; border-radius: 8px; background: #262626; border: 1px solid #454545; box-shadow: 0 10px 28px rgba(0,0,0,0.5); white-space: nowrap">
{icon('check', 13, '#3fb950', 2)}<span>Restored <b style="font-weight: 600">Yesterday 16:40</b> · 4 pages</span><button style="height: 24px; padding: 0 10px; border-radius: 4px; background: #333333; color: #a9c8f7; font-weight: 500">Undo</button><button style="height: 24px; padding: 0 8px; color: #a8a8a8">Versions</button></div></div>'''

# 5 · Row menu
mi = lambda t, kb='', danger=False, sep=False, dim=False: ('<div style="height: 1px; background: #3a3a3a; margin: 4px 0"></div>' if sep else f'<div style="height: 26px; display: flex; align-items: center; padding: 0 8px; border-radius: 3px; color: {"#ff938c" if danger else ("#6b6b6b" if dim else "#e8e8e8")}"><span style="flex: 1">{t}</span><span style="font-size: 10px; color: #939393">{kb}</span></div>')
menu = (f'<div style="position: absolute; left: 200px; top: 124px; width: 220px; padding: 4px; {pop} z-index: 3">'
        + mi('Rename') + mi('Edit note') + mi('', sep=True) + mi('Restore as a copy') + mi('Download as .daisy') + mi('', sep=True) + mi('Delete', danger=True) + '</div>')
more_btn = '<span style="position: absolute; right: 6px; top: 9px; width: 18px; height: 18px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: #3a3a3a">' + icon('more', 11, '#e8e8e8') + '</span>'
l5 = (day('TODAY') + ver('now', 'Current', 'Unsaved · Hero title, Book a visit', 'now') + ver('13:05', 'Before the Tablet pass', 'Named · 14 changes', 'named', True, more_btn)
      + ver('11:20', 'Autosave', '6 changes · season cards') + day('YESTERDAY') + ver('16:40', 'Autosave', '3 changes · headline, button'))
S5 = dlg(l5, '<div style="font-size: 11px; line-height: 16px; color: #939393">Named versions can be renamed or deleted. Autosaves have no Delete; they go after 30 days.</div>' + mini('Hand-thrown ceramics for everyday tables', w=360).replace('height: 130px', 'height: 160px')) .replace('<div style="flex: 1; min-height: 0; display: flex">', '<div style="flex: 1; min-height: 0; display: flex">' + menu, 1)

# 6 · Named filter, empty
seg = lambda items, sel: '<div style="display: grid; grid-template-columns: repeat(' + str(len(items)) + ', minmax(0, 1fr)); gap: 2px; padding: 2px; margin: 6px 2px; background: #1f1f1f; border-radius: 4px; font-size: 11px">' + ''.join(f'<span style="height: 20px; display: flex; align-items: center; justify-content: center; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #a8a8a8;"}">{t}</span>' for i, t in enumerate(items)) + '</div>'
l6 = seg(['All', 'Named'], 1) + f'<div style="padding: 24px 12px; display: flex; flex-direction: column; align-items: center; gap: 8px; text-align: center"><span style="width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; border-radius: 8px; background: #2a2a2a">{icon("pin", 15, "#a8a8a8")}</span><b style="font-weight: 600">No named versions yet</b><span style="font-size: 11px; line-height: 15px; color: #939393">Name a version before a big change, so it is easy to find and kept for good.</span>{btn("Name the current version", True)}</div>'
S6 = dlg(l6, '<div style="flex: 1; display: flex; align-items: center; justify-content: center; font-size: 11px; color: #6b6b6b">Pick a version to see it</div>', footer='<span style="font-size: 10px; color: #939393">12 autosaves in the last 30 days · switch to All to see them</span>')

# 7 · No changes on this page
d7 = (f'<div style="display: flex; align-items: center; gap: 8px"><b style="font-weight: 600">Autosave · Yesterday 16:40</b><span style="flex: 1"></span>{ptabs(2, pages)}</div>'
      f'<div style="flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px; text-align: center"><span style="width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; border-radius: 8px; background: #2a2a2a">{icon("check", 15, "#3fb950", 2)}</span><b style="font-weight: 600">Journal is the same as now</b><span style="font-size: 11px; color: #939393">Changes in this version are on Home (2) and Shop (1)</span>{btn("Go to Home")}</div>')
S7 = dlg(base_list(), d7)

# 8 · Older versions
l8 = (base_list(4) + day('EARLIER') + ver('10 Nov', 'Project created', 'From the Shop template', 'named')
      + '<div style="margin: 6px 4px; padding: 8px; border-radius: 5px; background: #1f1f1f; font-size: 10px; line-height: 14px; color: #939393">Autosaves older than 30 days were removed · named versions always stay</div>')
S8 = dlg(l8, f'<div style="display: flex; align-items: center; gap: 8px"><b style="font-weight: 600">First full draft</b><span style="font-size: 11px; color: #939393">Named by you · Yesterday 14:02</span></div><div style="padding: 8px 10px; border-radius: 5px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; line-height: 16px; color: #c8c8c8">“All four pages in place, before the photo shoot.”</div>{mini("Hand-thrown ceramics", w=360).replace("height: 130px", "height: 150px")}', h=510)

cells = [
    ('1 · This version', 'One page at full size; page tabs show how many changes each page has', S1),
    ('2 · Naming a version', 'Inline name and optional note; named versions are kept for good', S2),
    ('3 · Confirm restore', 'Says what happens to all pages and the name of the safety version saved first', S3),
    ('4 · After restore', 'A toast in the editor with Undo, and a way back to Versions', toast_scene),
    ('5 · Version menu', 'Rename, note, restore as a copy, download; only named versions can be deleted', S5),
    ('6 · No named versions', 'Empty Named filter with the one useful action', S6),
    ('7 · Page with no changes', 'Journal is the same as now; points to the pages that did change', S7),
    ('8 · Older versions', 'A named version with its note; autosaves after 30 days are gone, named ones stay', S8),
]
body = sheet_header('D-32b', 'Versions · states', 'The states of the Versions dialog, drawn compact: one page at full size, naming, confirming and undoing a restore, the version menu, an empty filter, a page without changes and older versions. Read with D-32.')
body += '<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 48px 64px; align-items: start">' + ''.join(f'<div>{cap(t, dsc)}{c}</div>' for t, dsc, c in cells) + '</div>'
H = int(sys.argv[1]) if len(sys.argv) > 1 else 1900
open('/home/claude/daisy/project/D32b-Versions-States.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-32b Versions states', 1920, H, body))
print('ok')
