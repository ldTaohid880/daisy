import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *
P['history'] = ('stroke', 'M3 8a5 5 0 1 0 1.5-3.5M3 2.5v3h3M8 5.5V8l2 1.5')
P['pin'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
P['zip'] = ('stroke', 'M3.5 1.5h6l3 3v10h-9zM7 3h1M7 5h1M7 7h1M6.5 9h2v2h-2z')
M_ = "font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 11px"
POP = 'background: #262626; border: 1px solid #454545; border-radius: 10px; box-shadow: 0 16px 48px rgba(0,0,0,0.55);'
cap = lambda t, d: f'<div style="margin-bottom: 10px"><div style="font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{d}</div></div>'
btn = lambda t, k='sec': f'<button style="height: 30px; padding: 0 14px; border-radius: 5px; white-space: nowrap; {"background: #246bcb; color: #fff; font-weight: 600;" if k == "pri" else ("color: #a8a8a8;" if k == "ghost" else "box-shadow: inset 0 0 0 1px #454545;")}">{t}</button>'
def dialog(title, sub, body, foot, w=640):
    return f'''<div style="width: {w}px; display: flex; flex-direction: column; font-size: 12px; line-height: 16px; {POP}">
<div style="height: 48px; display: flex; align-items: center; gap: 10px; padding: 0 10px 0 18px; border-bottom: 1px solid #3a3a3a"><span style="font-size: 14px; font-weight: 600">{title}</span><span style="flex: 1; font-size: 11px; color: #939393">{sub}</span>{icon("close", 12, "#a8a8a8")}</div>
<div style="padding: 16px 18px; display: flex; flex-direction: column; gap: 12px">{body}</div>
<div style="height: 56px; display: flex; align-items: center; gap: 8px; padding: 0 18px; border-top: 1px solid #3a3a3a; background: #222222; border-radius: 0 0 10px 10px">{foot}</div></div>'''
back = lambda d, h: f'<div style="position: relative; width: 880px; height: {h}px; border-radius: 6px; overflow: hidden; background: #181818; box-shadow: 0 0 0 1px #303030"><div style="position: absolute; inset: 0; background: linear-gradient(#141414 0 40px, #1b1b1b 40px 76px, #2a2a2a 76px); opacity: 0.6"></div><div style="position: absolute; inset: 0; background: rgba(0,0,0,0.45)"></div><div style="position: absolute; left: 50%; top: 24px; transform: translateX(-50%)">{d}</div></div>'
spin = '<span style="width: 12px; height: 12px; box-sizing: border-box; border-radius: 6px; border: 2px solid #454545; border-top-color: #2f80ed"></span>'
def stp(state, t, d):
    ic = {'done': icon('check', 12, '#3fb950', 2), 'run': spin, 'wait': '<span style="width: 8px; height: 8px; border-radius: 4px; box-shadow: inset 0 0 0 1.5px #6b6b6b"></span>'}[state]
    return f'<div style="height: 26px; display: flex; align-items: center; gap: 10px"><span style="width: 14px; display: flex; justify-content: center">{ic}</span><span style="{"color: #6b6b6b;" if state == "wait" else ""}">{t}</span><span style="flex: 1"></span><span style="font-size: 11px; color: #939393">{d}</span></div>'
bar = lambda pct: f'<div style="height: 6px; border-radius: 3px; background: #1f1f1f; overflow: hidden"><span style="display: block; width: {pct}%; height: 6px; background: #2f80ed"></span></div>'

# 1 · exporting
c1 = back(dialog('Exporting Halden', f'to <span style="{M_}">D:\\Sites\\halden-export</span>',
    f'<div style="display: flex; align-items: center; gap: 10px"><span style="flex: 1">{bar(68)}</span><span style="font-size: 11px; color: #c8c8c8">68% · about 6 s</span></div>'
    + stp('done', 'Pages', '4 of 4') + stp('done', 'CSS: combined, unused rules removed', '184 KB → 21 KB') + stp('run', 'Images: resized and converted to WebP', '9 of 12')
    + stp('wait', 'Fonts: self-hosted, only weights in use', '3') + stp('wait', 'Check links and accessibility', ''),
    '<span style="flex: 1; font-size: 11px; color: #939393">You can keep working; the export uses a snapshot from 14:02</span>' + btn('Run in background', 'ghost') + btn('Cancel')), 380)

# 2 · done
item = lambda ic, c, t, d, act='': f'<div style="display: flex; align-items: center; gap: 10px; padding: 8px 10px; border-radius: 4px; background: #2a2a2a">{icon(ic, 13, c, 1.5)}<span style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span>{t}</span><span style="font-size: 11px; color: #939393">{d}</span></span>{act}</div>'
c2 = back(dialog('Exported', '14:02 · 8 s',
    f'''<div style="display: flex; align-items: center; gap: 12px"><span style="width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border-radius: 18px; background: rgba(63,185,80,0.16)">{icon("check", 18, "#3fb950", 2)}</span>
<div style="display: flex; flex-direction: column; gap: 2px"><b style="font-size: 14px; font-weight: 600">4 pages, 1.8 MB</b><span style="font-size: 11px; color: #a8a8a8">was 6.2 MB in the editor · images 71% smaller</span></div></div>
<div style="font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393">2 THINGS TO LOOK AT · NOT BLOCKING</div>
{item('warning', '#d29922', 'Hero image has no description', 'Home · screen readers say nothing', '<button style="font-size: 11px; color: #a9c8f7">Fix</button>')}
{item('link', '#d29922', '“Our process →” links to #process, which is not on the page', 'Home › Hero', '<button style="font-size: 11px; color: #a9c8f7">Show</button>')}''',
    btn('Copy summary', 'ghost') + '<span style="flex: 1"></span>' + btn('Open in browser') + btn('Open folder', 'pri')), 440)

# 3 · could not export
c3 = back(dialog('Export stopped', 'at step 1 of 5',
    f'''<div style="display: flex; gap: 10px; padding: 10px 12px; border-radius: 5px; background: rgba(248,81,73,0.12); box-shadow: inset 0 0 0 1px rgba(248,81,73,0.35)">{icon("warning", 15, "#ff938c")}
<span style="display: flex; flex-direction: column; gap: 2px; line-height: 17px"><b style="font-weight: 600">Can’t write to {"<span style=\"" + M_ + "\">D:\\Sites\\halden-export</span>"}</b><span style="font-size: 11px; color: #c8c8c8">The folder is read-only or another app is using it. Nothing was changed.</span></span></div>
<span style="font-size: 11px; color: #939393">Your project is not affected. Pick another way to get the files:</span>''',
    btn('Details', 'ghost') + '<span style="flex: 1"></span>' + btn('Download as .zip') + btn('Choose another folder…') + btn('Try again', 'pri')), 300)

# 4 · toast in the editor
toast = f'''<div style="position: absolute; left: 50%; bottom: 38px; transform: translateX(-50%); height: 40px; display: flex; align-items: center; gap: 12px; padding: 0 8px 0 14px; border-radius: 8px; background: #262626; border: 1px solid #454545; box-shadow: 0 10px 28px rgba(0,0,0,0.5); white-space: nowrap; font-size: 12px">
{icon('check', 13, '#3fb950', 2)}<span>Exported 4 pages · 1.8 MB · 2 things to look at</span><button style="height: 26px; padding: 0 10px; border-radius: 4px; background: #333333; color: #a9c8f7">Open folder</button><button style="height: 26px; padding: 0 8px; color: #a8a8a8">Report</button></div>'''
c4 = f'''<div style="position: relative; width: 880px; height: 240px; border-radius: 6px; overflow: hidden; background: #2a2a2a; box-shadow: 0 0 0 1px #303030">
<div style="height: 40px; display: flex; align-items: center; justify-content: flex-end; gap: 10px; padding: 0 10px; background: #141414; border-bottom: 1px solid #262626; font-size: 11px">
<span style="display: flex; align-items: center; gap: 6px; color: #939393">{icon("check", 11, "#3fb950", 2)}Saved</span>
<span style="height: 26px; display: flex; align-items: center; gap: 8px; padding: 0 12px; border-radius: 6px; background: #246bcb; color: #fff; font-size: 12px">{spin.replace("#454545", "rgba(255,255,255,0.35)").replace("#2f80ed", "#ffffff")}Exporting 68%</span></div>
<div style="position: absolute; left: 30px; right: 30px; top: 60px; bottom: 0; background: #f6f1ea"></div>{toast}</div>'''

# 5 · History panel
def h(t, sub, state='past', big=False):
    col = {'past': '#c8c8c8', 'now': '#e8e8e8', 'future': '#6b6b6b'}[state]
    return (f'<div style="height: 32px; display: flex; align-items: center; gap: 8px; padding: 0 10px; {"background: rgba(47,128,237,0.18); box-shadow: inset 2px 0 0 #2f80ed;" if state == "now" else ""}">'
            f'<span style="width: 8px; height: 8px; flex: none; border-radius: 4px; {"background: #2f80ed;" if state == "now" else ("box-shadow: inset 0 0 0 1.5px #6b6b6b;" if state == "future" else "background: #6b6b6b;")}"></span>'
            f'<span style="flex: 1; min-width: 0; display: flex; flex-direction: column"><span style="color: {col}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{t}</span><span style="font-size: 10px; line-height: 12px; color: #6b6b6b">{sub}</span></span></div>')
mark = '<div style="height: 22px; display: flex; align-items: center; gap: 6px; padding: 0 10px; font-size: 10px; color: #a9c8f7">' + icon('pin', 11, '#a9c8f7') + 'Version “Before the Tablet pass” · 13:05</div>'
dock = f'''<div style="width: 300px; flex: none; display: flex; flex-direction: column; border-left: 1px solid #303030; background: #1f1f1f">
<div style="height: 32px; display: flex; align-items: stretch; gap: 16px; padding: 0 12px; border-bottom: 1px solid #303030"><span style="display: flex; align-items: center; font-weight: 500; color: #a8a8a8">Swatches</span><span style="position: relative; display: flex; align-items: center; font-weight: 500">History<span style="position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: #2f80ed"></span></span><span style="flex: 1"></span><span style="display: flex; align-items: center; font-size: 11px; color: #939393">This page ▾</span></div>
<div style="font-size: 12px; line-height: 16px">
{h('Redo: Move “Our process →” after the button', 'Home · 14:12', 'future')}{h('Redo: Hero gap 64 → 56', 'Home · 14:11', 'future')}
{h('Hero title size 64 → fluid 44–64', 'Home · 14:10 · Typography', 'now')}
{h('Change fill of Shop the collection', 'Home · 14:08 · brand-deep → brand', 'past')}{h('Add Gift cards button', 'Home · 14:06', 'past')}{mark}
{h('Edit text “Each piece is…”', 'Home · 13:02', 'past')}{h('Hero grid: Row → Grid', 'Home · 12:58', 'past')}
<div style="padding: 6px 10px; font-size: 10px; color: #6b6b6b">142 steps today · kept until the project closes</div></div></div>'''
side = f'''<div style="flex: 1; padding: 18px; display: flex; flex-direction: column; gap: 10px; font-size: 12px; line-height: 18px; color: #c8c8c8">
<b style="color: #e8e8e8">How History works</b>
<span>Newest at the top. The current step has a blue dot; steps above it are undone and greyed (Redo brings them back).</span>
<span>Click a step to go back to it; the canvas shows that moment. Making a change from there drops the greyed steps.</span>
<span>Hover shows what changed; right-click: <b style="font-weight: 500; color: #e8e8e8">Save version here</b>, Copy as CSS change, Show on canvas.</span>
<span>Named versions appear as pins in the list. “This page ▾” switches to All pages.</span></div>'''
c5 = f'<div style="width: 880px; height: 380px; display: flex; border-radius: 6px; overflow: hidden; background: #2a2a2a; box-shadow: 0 0 0 1px #303030">{side}{dock}</div>'

cells = [('1 · Exporting', 'Steps with progress; work can continue because the export uses a snapshot. Can run in the background.', c1),
         ('2 · Exported', 'Size and what got smaller, things to look at (not blocking) with Fix or Show, Open folder or Open in browser.', c2),
         ('3 · Export stopped', 'Says why and that nothing changed; Try again, another folder, or download a .zip.', c3),
         ('4 · In the background', 'The Export button shows progress; a toast says when it is done.', c4),
         ('5 · History panel', 'In the right dock beside Swatches; every step with page, time and detail.', c5)]
body = sheet_header('D-55', 'Export progress and History', 'What happens after Export (D-30), and the History panel for undo and redo.')
body += '<div style="display: grid; grid-template-columns: repeat(2, 880px); gap: 48px 32px; align-items: start">' + ''.join(f'<div>{cap(t, d)}{c}</div>' for t, d, c in cells) + '</div>'
H = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
open('/home/claude/daisy/project/D55-ExportHistory.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-55 Export progress and History', 1920, H, body))
print('ok')
