import sys
sys.path.insert(0, '/home/claude/ds')
_src = open('/home/claude/ds/d38.py').read(); G = {}; exec(_src[:_src.index('FILE = [')], G)
from lib import *
mi, SEP, menu = G['mi'], G['SEP'], G['menu']
P.update(G['P'])
P['restore'] = ('stroke', 'M3 8a5 5 0 1 0 1.5-3.5M3 2.5v3h3')
P['drop'] = ('stroke', 'M8 2v8M5 7l3 3 3-3M2.5 11v2.5h11V11')
P['bulb'] = ('stroke', 'M6 12.5h4M6.5 14.5h3M8 1.5a4.5 4.5 0 0 0-2.5 8.2V11h5V9.7A4.5 4.5 0 0 0 8 1.5z')
POP = 'background: #262626; border: 1px solid #454545; border-radius: 8px; box-shadow: 0 12px 32px rgba(0,0,0,0.5);'
M_ = "font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 11px"
cap = lambda t, d: f'<div style="margin-bottom: 10px"><div style="font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{d}</div></div>'
btn = lambda t, k='sec': f'<button style="height: 26px; padding: 0 12px; border-radius: 4px; white-space: nowrap; {"background: #246bcb; color: #fff; font-weight: 500;" if k == "pri" else ("color: #a8a8a8;" if k == "ghost" else ("box-shadow: inset 0 0 0 1px #454545; color: #ff938c;" if k == "danger" else "box-shadow: inset 0 0 0 1px #454545;"))}">{t}</button>'
frame = lambda inner, h: f'<div style="position: relative; width: 880px; height: {h}px; border-radius: 6px; overflow: hidden; background: #1f1f1f; box-shadow: 0 0 0 1px #303030; font-size: 12px; line-height: 16px">{inner}</div>'
def pcard(name, sub, bg, ink, acc, hover=False):
    return f'''<div style="width: 200px; border-radius: 6px; overflow: hidden; background: #1a1a1a; box-shadow: inset 0 0 0 1px {"#454545" if hover else "#2a2a2a"}">
<div style="height: 120px; display: flex; align-items: flex-end; justify-content: center; background: #2a2a2a"><div style="width: 164px; height: 104px; background: {bg}; padding: 8px; box-sizing: border-box; display: flex; flex-direction: column; gap: 4px"><span style="width: 60%; height: 6px; background: {ink}"></span><span style="width: 40%; height: 6px; background: {ink}"></span><span style="margin-top: 6px; width: 30px; height: 8px; border-radius: 4px; background: {acc}"></span></div></div>
<div style="display: flex; align-items: center; gap: 8px; padding: 8px 8px 8px 10px"><div style="flex: 1"><div style="font-weight: 500">{name}</div><div style="font-size: 11px; color: #939393">{sub}</div></div>
<span style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; {"background: #3a3a3a;" if hover else ""}">{icon("more", 12, "#e8e8e8" if hover else "#a8a8a8")}</span></div></div>'''

# 1 · project card menu
PM = [mi('Open', 'Enter'), mi('Open in a new window'), SEP, mi('Rename…', 'F2'), mi('Duplicate'), mi('Project settings…', '', 'gear'), SEP, mi('Show in folder', ic='folder'), mi('Export all pages…', '', 'external'), mi('Copy as a starting point…', note='tokens only'), SEP, mi('Delete…', 'Del', 'trash', danger=True)]
c1 = frame(f'''<div style="padding: 20px 24px; display: flex; gap: 16px">{pcard("Halden", "4 pages · Edited 12 minutes ago", "#f6f1ea", "#1d1a16", "#b5532d", True)}{pcard("Riverside Café", "2 pages · Edited yesterday", "#fffaf2", "#2b2118", "#c9822b")}{pcard("Portfolio 2026", "6 pages · 3 days ago", "#111318", "#e9ecf1", "#7aa2ff")}</div>
<div style="position: absolute; left: 200px; top: 200px">{menu(PM, 260)}</div>''', 580)

# 2 · recently deleted
drow = lambda ic, n, sub, left: f'<div style="height: 40px; display: grid; grid-template-columns: 20px minmax(0, 1fr) 210px 190px; align-items: center; gap: 12px; padding: 0 12px; border-bottom: 1px solid #262626">{icon(ic, 14, "#a8a8a8")}<span style="display: flex; flex-direction: column"><span>{n}</span><span style="font-size: 11px; color: #939393">{sub}</span></span><span style="font-size: 11px; color: #939393">{left}</span><span style="justify-self: end; display: flex; gap: 6px">{btn("Restore")}{btn("Delete forever", "ghost")}</span></div>'
c2 = frame(f'''<div style="padding: 20px 24px; display: flex; flex-direction: column; gap: 10px">
<div style="display: flex; align-items: center; gap: 10px"><button style="font-size: 11px; color: #a8a8a8">← Your projects</button><span style="flex: 1"></span></div>
<div style="display: flex; align-items: baseline; gap: 10px"><span style="font-size: 16px; font-weight: 600">Recently deleted</span><span style="font-size: 11px; color: #939393">Kept for 30 days, then removed for good. Files stay in your folders until then.</span></div>
<div style="border-top: 1px solid #262626">{drow("folder", "Old portfolio", "Project · 5 pages · D:\\Sites\\portfolio-2024", "Deleted 3 days ago · 27 days left")}{drow("file", "summer-sale.html", "Single file · Downloads", "Deleted 2 weeks ago · 16 days left")}</div>
<div style="display: flex; justify-content: flex-end">{btn("Empty now", "danger")}</div></div>''', 280)

# 3 · open and drop
c3 = frame(f'''<div style="padding: 20px 24px"><div style="font-size: 16px; font-weight: 600; margin-bottom: 14px">Your projects</div><div style="display: flex; gap: 16px">{pcard("Halden", "4 pages", "#f6f1ea", "#1d1a16", "#b5532d")}{pcard("Riverside Café", "2 pages", "#fffaf2", "#2b2118", "#c9822b")}</div></div>
<div style="position: absolute; inset: 10px; display: flex; align-items: center; justify-content: center; border-radius: 8px; border: 2px dashed #2f80ed; background: rgba(31,31,31,0.88)">
<div style="display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center">{icon('drop', 28, '#a9c8f7')}<b style="font-size: 15px; font-weight: 600">Drop to open</b>
<span style="max-width: 420px; font-size: 12px; line-height: 18px; color: #c8c8c8">A folder opens as a project. An <span style="{M_}">.html</span> file opens on its own, or drop it on a project card to add it there.</span>
<span style="display: flex; align-items: center; gap: 8px; padding: 6px 10px; border-radius: 4px; background: #262626; box-shadow: inset 0 0 0 1px #3a3a3a">{icon("folder", 13, "#a8a8a8")}<span style="{M_}">old-site/</span><span style="font-size: 11px; color: #939393">12 html files · will be a new project</span></span></div></div>''', 300)

# 4 · tips on first use
tip = f'''<div style="position: absolute; left: 330px; top: 92px; width: 300px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; gap: 8px; {POP}">
<span aria-hidden="true" style="position: absolute; left: 24px; top: -6px; width: 10px; height: 10px; background: #262626; border-left: 1px solid #454545; border-top: 1px solid #454545; transform: rotate(45deg)"></span>
<div style="display: flex; align-items: center; gap: 8px">{icon('bulb', 14, '#f2b84b')}<b style="font-weight: 600">Go inside a box</b><span style="flex: 1"></span><span style="font-size: 11px; color: #939393">2 of 6</span></div>
<span style="font-size: 12px; line-height: 18px; color: #c8c8c8">You picked Hero grid. <b style="font-weight: 600">Double-click</b> to select what is inside it, or press <b style="font-weight: 600">Enter</b>. Esc goes back out.</span>
<div style="display: flex; gap: 6px; align-items: center"><button style="font-size: 11px; color: #a8a8a8">Turn tips off</button><span style="flex: 1"></span>{btn("Got it", "pri")}</div></div>'''
c4 = frame(f'''<div style="position: absolute; left: 24px; top: 24px; width: 600px; height: 300px; background: #f6f1ea; color: #1d1a16">
<div style="position: absolute; left: 30px; top: 40px; width: 520px; height: 200px; outline: 1.5px solid #2f80ed; outline-offset: 2px"><span style="position: absolute; left: -2px; top: -22px; height: 18px; padding: 0 6px; display: flex; align-items: center; background: #246bcb; color: #fff; font-size: 10px">Box · Hero grid</span>
<div style="padding: 20px; font: 600 26px/1.1 'Fraunces', serif; width: 240px">Hand-thrown ceramics</div></div></div>{tip}
<div style="position: absolute; right: 24px; top: 24px; width: 210px; display: flex; flex-direction: column; gap: 8px; font-size: 11px; line-height: 16px; color: #a8a8a8">
<b style="font-size: 12px; font-weight: 600; color: #e8e8e8">How tips work</b><span>One tip at a time, the first time something happens, next to it.</span><span>Never over the selection, never in a dialog.</span><span>Help › Show tips again brings them back.</span></div>''', 360)

# 5 · getting started
step = lambda done, t, d: f'<div style="display: flex; gap: 10px; align-items: flex-start; padding: 6px 0"><span style="width: 18px; height: 18px; flex: none; border-radius: 9px; display: flex; align-items: center; justify-content: center; {"background: #1a7f37;" if done else "box-shadow: inset 0 0 0 1.5px #6b6b6b;"}">{icon("check", 10, "#fff", 2) if done else ""}</span><span style="display: flex; flex-direction: column; gap: 2px"><span style="{"color: #939393; text-decoration: line-through;" if done else ""}">{t}</span><span style="font-size: 11px; color: #939393">{d}</span></span></div>'
gs = f'''<div style="position: absolute; right: 16px; top: 16px; width: 320px; padding: 14px; box-sizing: border-box; {POP}">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px"><b style="font-weight: 600">Getting started</b><span style="font-size: 11px; color: #939393">3 of 6</span><span style="flex: 1"></span>{icon("close", 11, "#a8a8a8")}</div>
<div style="height: 4px; border-radius: 2px; background: #333333; margin-bottom: 8px"><span style="display: block; width: 50%; height: 4px; border-radius: 2px; background: #2f80ed"></span></div>
{step(True, "Add a section", "Section tool · S")}{step(True, "Write a heading", "Text tool · T")}{step(True, "Use a colour from the design system", "Swatches")}
{step(False, "Make it work on phones", "Mobile screen size")}{step(False, "Preview the page", "Ctrl Enter")}{step(False, "Export your site", "Ctrl Shift E")}
<div style="margin-top: 6px; font-size: 11px; color: #939393">Each step opens a 30-second guide on your own page.</div></div>'''
c5 = frame('<div style="position: absolute; inset: 0; background: #2a2a2a"></div><div style="position: absolute; left: 24px; top: 24px; width: 470px; height: 440px; background: #f6f1ea"></div>' + gs, 490)

# 6 · about and what's new
about = f'''<div style="position: absolute; left: 24px; top: 24px; width: 360px; padding: 20px; box-sizing: border-box; display: flex; flex-direction: column; align-items: center; gap: 8px; text-align: center; {POP}">
<span style="width: 48px; height: 48px; display: flex; align-items: center; justify-content: center; border-radius: 12px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #2e2e2e">{daisy(30)}</span>
<b style="font-size: 16px; font-weight: 600">Daisy</b><span style="font-size: 11px; color: #a8a8a8">Version 0.9.2 · up to date</span>
<span style="font-size: 11px; line-height: 16px; color: #939393">Design real HTML and CSS, visually.</span>
<div style="display: flex; gap: 12px; font-size: 11px"><button style="color: #a9c8f7">What’s new</button><button style="color: #a9c8f7">Licences</button><button style="color: #a9c8f7">Copy version info</button></div></div>'''
wn = f'''<div style="position: absolute; left: 410px; top: 24px; width: 446px; padding: 16px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px; {POP}">
<div style="display: flex; align-items: center; gap: 8px"><b style="font-size: 14px; font-weight: 600">What’s new in 0.9</b><span style="flex: 1"></span>{icon("close", 11, "#a8a8a8")}</div>
{"".join(f'<div style="display: flex; gap: 10px"><span style="width: 6px; height: 6px; margin-top: 6px; border-radius: 3px; background: #2f80ed; flex: none"></span><span style="display: flex; flex-direction: column; gap: 2px"><b style="font-weight: 600">{t}</b><span style="font-size: 11px; line-height: 16px; color: #a8a8a8">{d}</span></span></div>' for t, d in [("Find and replace across pages", "Ctrl H. Text, alt text, links, classes and colours."), ("Import an HTML page", "Tidy it up and link its colours to your tokens."), ("Matched font fallbacks", "No more jumping text while fonts load.")])}
<button style="align-self: flex-start; font-size: 11px; color: #a9c8f7">All release notes</button></div>'''
c6 = frame('<div style="position: absolute; inset: 0; background: rgba(0,0,0,0.35)"></div>' + about + wn, 290)

cells = [('1 · Project card menu', 'The ⋯ on a project card (or right-click). Copy as a starting point takes only the tokens, never content.', c1),
         ('2 · Recently deleted', 'Projects and single files, with days left, Restore and Delete forever.', c2),
         ('3 · Open and drop', 'File › Open… takes a folder or an .html file. Dropping on Home shows what will happen before letting go.', c3),
         ('4 · A tip on first use', 'Shown once, next to what it explains, never over the selection.', c4),
         ('5 · Getting started', 'An optional checklist from Help; ticks itself as you work; each step opens a short guide on your own page.', c5),
         ('6 · About and What’s new', 'Help › About Daisy; What’s new opens once after an update and from Help.', c6)]
body = sheet_header('D-52', 'Home and Help · small screens', 'The project card menu, Recently deleted, opening and dropping files, first-use tips, Getting started, About and What’s new.')
body += '<div style="display: grid; grid-template-columns: repeat(2, 880px); gap: 48px 32px; align-items: start">' + ''.join(f'<div>{cap(t, d)}{c}</div>' for t, d, c in cells) + '</div>'
H = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
open('/home/claude/daisy/project/D52-HomeHelp.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-52 Home and Help', 1920, H, body))
print('ok')
