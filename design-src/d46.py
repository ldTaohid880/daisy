import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *
P['cloud-off'] = ('stroke', 'M4.5 12h7a3 3 0 0 0 .6-5.9A4.5 4.5 0 0 0 4 6.5a2.8 2.8 0 0 0 .5 5.5zM2 2l12 12')
P['disk'] = ('stroke', 'M2.5 2.5h9l2 2v9h-11zM5 2.5v3.5h5V2.5M5 13.5V9.5h6v4')
P['history'] = ('stroke', 'M3 8a5 5 0 1 0 1.5-3.5M3 2.5v3h3M8 5.5V8l2 1.5')
P['img-off'] = ('stroke', 'M2.5 3h11v10h-11zM2.5 10.5l3-3 3 3 2-2 3 3M2 2l12 12')
W = 880
POP = 'background: #262626; border: 1px solid #454545; border-radius: 8px; box-shadow: 0 12px 32px rgba(0,0,0,0.5);'
btn = lambda t, kind='sec': f'<button style="height: 26px; padding: 0 12px; border-radius: 4px; white-space: nowrap; font-size: 12px; {"background: #246bcb; color: #fff; font-weight: 500;" if kind == "pri" else ("color: #a8a8a8;" if kind == "ghost" else "box-shadow: inset 0 0 0 1px #454545; color: #e8e8e8;")}">{t}</button>'
mono = lambda t, c='#c8c8c8': f'<span style="font-family: {MONO}; font-size: 11px; color: {c}">{t}</span>'
cap = lambda t, d: f'<div style="margin-bottom: 10px"><div style="font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{d}</div></div>'

def topbar(status):
    return f'''<div style="height: 40px; display: flex; align-items: center; gap: 8px; padding: 0 8px; background: #141414; border-bottom: 1px solid #262626">
<span style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 6px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #2e2e2e">{daisy(16)}</span>
<span style="display: flex; gap: 14px; margin-left: 6px; color: #a8a8a8">File Edit Element View Help</span><span style="flex: 1"></span>
{status}{icon("undo", 14, "#a8a8a8")}{icon("redo", 14, "#4f4f4f")}
<span style="height: 26px; padding: 0 10px; display: flex; align-items: center; border-radius: 6px; box-shadow: inset 0 0 0 1px #3a3a3a">Preview</span><span style="height: 26px; padding: 0 10px; display: flex; align-items: center; border-radius: 6px; background: #246bcb; color: #fff">Export</span></div>'''
def tabs(items):
    return '<div style="height: 32px; display: flex; background: #181818; border-bottom: 1px solid #2a2a2a">' + ''.join(
        f'<span style="position: relative; height: 32px; display: flex; align-items: center; gap: 8px; padding: 0 12px; border-right: 1px solid #262626; {"background: #2a2a2a; color: #e8e8e8;" if on else "color: #a8a8a8;"}">{"<span style=\"position: absolute; left: 0; right: 0; top: 0; height: 2px; background: #2f80ed\"></span>" if on else ""}{n}{mono(fn, "#939393")}{extra}</span>' for n, fn, on, extra in items) + '</div>'
canvas = lambda h, inner='': f'<div style="position: relative; height: {h}px; background: #2a2a2a">{inner}</div>'
frame = lambda inner: f'<div style="width: {W}px; border-radius: 6px; overflow: hidden; box-shadow: 0 0 0 1px #303030; font-size: 12px; line-height: 16px">{inner}</div>'

# 1 · save status in the top bar
pill = lambda ic, t, c, bg='transparent', extra='': f'<span style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; background: {bg}; color: {c}; font-size: 11px; white-space: nowrap">{ic}{t}{extra}</span>'
spinner = '<span style="width: 10px; height: 10px; box-sizing: border-box; border-radius: 5px; border: 1.5px solid #454545; border-top-color: #a8a8a8"></span>'
states = [('Saved', pill(icon('check', 11, '#3fb950', 2), 'Saved', '#939393'), 'Every change is written to the folder within 2 s. Hover: “Saved to D:\\Sites\\halden · 12:04”.'),
          ('Saving', pill(spinner, 'Saving…', '#a8a8a8'), 'Shown only if a save takes longer than 1 s.'),
          ('Waiting', pill(icon('disk', 11, '#d29922'), '3 changes not saved', '#e3b34a', 'rgba(210,153,34,0.12)'), 'Kept safe in this browser until the folder can be written.'),
          ('Failed', pill(icon('warning', 11, '#ff938c'), 'Couldn’t save', '#ff938c', 'rgba(248,81,73,0.14)', ' · <span style="text-decoration: underline">Fix</span>'), 'Click opens the reason and the way out (cell 2).')]
c1 = frame('<div style="padding: 14px; display: flex; flex-direction: column; gap: 10px; background: #1f1f1f">' + ''.join(
    f'<div style="display: grid; grid-template-columns: 80px 220px minmax(0, 1fr); align-items: center; gap: 12px"><span style="font-size: 11px; color: #939393">{n}</span><span style="height: 36px; display: flex; align-items: center; justify-content: flex-end; gap: 8px; padding: 0 10px; border-radius: 4px; background: #141414">{p}{icon("undo", 13, "#a8a8a8")}</span><span style="font-size: 11px; line-height: 15px; color: #a8a8a8">{d}</span></div>' for n, p, d in states) + '</div>')

# 2 · couldn't save
banner = f'''<div role="alert" style="display: flex; align-items: center; gap: 10px; padding: 10px 12px; background: rgba(248,81,73,0.12); border-bottom: 1px solid rgba(248,81,73,0.35)">
{icon('warning', 15, '#ff938c')}<span style="flex: 1; line-height: 16px"><b style="font-weight: 600">Couldn’t save shop.html.</b> <span style="color: #c8c8c8">Daisy no longer has permission to write to {mono("D:\\Sites\\halden")}. Your 3 changes are kept in this browser.</span></span>
{btn('Allow again', 'pri')}{btn('Save a copy elsewhere…')}{btn('Details', 'ghost')}</div>'''
c2 = frame(topbar(pill(icon('warning', 11, '#ff938c'), 'Couldn’t save', '#ff938c', 'rgba(248,81,73,0.14)')) + banner + tabs([('Home', 'index.html', False, ''), ('Shop', 'shop.html', True, '<span style="width: 7px; height: 7px; border-radius: 4px; background: #e3b34a"></span>')]) + canvas(110, '<div style="position: absolute; left: 24px; right: 24px; top: 16px; bottom: 0; background: #f6f1ea"></div>'))

# 3 · offline
off = f'''<div style="display: flex; align-items: center; gap: 10px; padding: 8px 12px; background: #1f1f1f; border-bottom: 1px solid #303030; font-size: 11px">
{icon('cloud-off', 14, '#a8a8a8')}<span style="flex: 1; color: #c8c8c8"><b style="font-weight: 600; color: #e8e8e8">Offline.</b> Saving to your folder still works. Google Fonts and web images can’t load until you are back online.</span>{btn('Dismiss', 'ghost')}</div>'''
fallback = f'''<div style="position: absolute; left: 24px; right: 24px; top: 14px; bottom: 0; padding: 16px 20px; background: #f6f1ea; color: #1d1a16">
<div style="font: 600 26px/1.1 Georgia, serif">Hand-thrown ceramics</div>
<span style="position: absolute; left: 20px; top: 56px; height: 20px; padding: 0 8px; display: flex; align-items: center; gap: 6px; border-radius: 3px; background: #1f1f1f; color: #c8c8c8; font-size: 11px">{icon('info', 11, '#58a6ff', 1.25)}Fraunces is not loaded · showing its fallback, Georgia</span>
<div style="position: absolute; right: 20px; top: 14px; width: 220px; height: 86px; border-radius: 6px; background: #e6dccd; display: flex; align-items: center; justify-content: center; gap: 6px; font-size: 11px; color: #6b6358">{icon('img-off', 14, '#6b6358')}unsplash.com image · offline</div></div>'''
c3 = frame(topbar(pill(icon('check', 11, '#3fb950', 2), 'Saved', '#939393')) + off + tabs([('Home', 'index.html', True, '')]) + canvas(140, fallback))

# 4 · file changed outside Daisy
diff = f'''<div style="padding: 8px 10px; border-radius: 4px; background: #1b1b1b; box-shadow: inset 0 0 0 1px #303030; font-family: {MONO}; font-size: 11px; line-height: 17px">
<div style="color: #939393">styles.css · 2 lines</div>
<div style="color: #ff938c">−  .hero-title {{ font-size: 64px; }}</div><div style="color: #7ee2a8">+  .hero-title {{ font-size: clamp(44px, 5vw, 64px); }}</div>
<div style="color: #939393; margin-top: 4px">index.html · no change</div></div>'''
dlg4 = f'''<div style="position: absolute; left: 140px; top: 18px; width: 600px; padding: 16px; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px; {POP}">
<div style="display: flex; align-items: center; gap: 10px">{icon('info', 16, '#58a6ff', 1.5)}<b style="font-size: 14px; font-weight: 600">styles.css changed outside Daisy</b><span style="flex: 1"></span><span style="font-size: 11px; color: #939393">by another app · 12:10</span></div>
<span style="font-size: 12px; line-height: 18px; color: #c8c8c8">You also changed this file in Daisy since 12:02 (2 changes). Choose which version to keep.</span>
{diff}
<div style="display: flex; gap: 8px">{btn('Compare in Code')}<span style="flex: 1"></span>{btn('Keep mine', 'sec')}{btn('Use theirs', 'pri')}</div>
<span style="font-size: 11px; color: #939393">Either way, the other version is saved in Versions.</span></div>'''
c4 = frame(topbar(pill(icon('disk', 11, '#d29922'), '2 changes not saved', '#e3b34a', 'rgba(210,153,34,0.12)')) + tabs([('Home', 'index.html', True, '')]) + canvas(296, '<div style="position: absolute; inset: 0; background: rgba(0,0,0,0.45)"></div>' + dlg4))

# 5 · file missing
miss_tab = '<span style="text-decoration: line-through; color: #939393">Journal</span>'
miss = f'''<div style="position: absolute; left: 24px; right: 24px; top: 16px; bottom: 16px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; border-radius: 4px; border: 1px dashed #454545; text-align: center">
{icon('file', 22, '#a8a8a8')}<b style="font-size: 13px; font-weight: 600">journal.html is no longer in the folder</b>
<span style="font-size: 11px; color: #a8a8a8">It was moved, renamed or deleted outside Daisy. The last version is kept here.</span>
<div style="display: flex; gap: 8px">{btn('Find it…', 'pri')}{btn('Save it here again')}{btn('Remove from project', 'ghost')}</div></div>'''
c5 = frame(topbar(pill(icon('check', 11, '#3fb950', 2), 'Saved', '#939393')) + tabs([('Home', 'index.html', False, ''), (miss_tab, 'journal.html', True, icon('warning', 11, '#d29922', 1.5))]) + canvas(200, miss))

# 6 · recovery after a crash (on Home)
rec = lambda n, fn, d: f'<div style="height: 32px; display: flex; align-items: center; gap: 10px; padding: 0 10px; border-radius: 4px; background: #2a2a2a">{icon("file", 13, "#a8a8a8")}<span>{n}</span>{mono(fn, "#939393")}<span style="flex: 1"></span><span style="font-size: 11px; color: #a8a8a8">{d}</span><button style="font-size: 11px; color: #a9c8f7">View</button></div>'
dlg6 = f'''<div style="position: absolute; left: 160px; top: 20px; width: 560px; padding: 16px; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px; {POP}">
<div style="display: flex; align-items: center; gap: 10px">{icon('history', 16, '#a8a8a8')}<b style="font-size: 14px; font-weight: 600">Daisy closed before saving</b></div>
<span style="font-size: 12px; line-height: 18px; color: #c8c8c8">Unsaved changes from 12:31 were recovered in <b style="font-weight: 600">Halden</b>.</span>
<div style="display: flex; flex-direction: column; gap: 4px">{rec('Home', 'index.html', '4 changes')}{rec('Shop', 'shop.html', '1 change')}</div>
<div style="display: flex; gap: 8px">{btn('Discard', 'ghost')}<span style="flex: 1"></span>{btn('Open without them')}{btn('Restore changes', 'pri')}</div>
<span style="font-size: 11px; color: #939393">Discarded changes stay in Versions for 30 days.</span></div>'''
home_bg = '<div style="position: absolute; inset: 0; padding: 20px 24px; background: #1f1f1f"><div style="font-size: 16px; font-weight: 600; margin-bottom: 12px">Your projects</div><div style="display: flex; gap: 12px">' + ''.join('<span style="width: 160px; height: 120px; border-radius: 6px; background: #2a2a2a"></span>' for _ in range(4)) + '</div></div><div style="position: absolute; inset: 0; background: rgba(0,0,0,0.5)"></div>'
c6 = frame(f'<div style="height: 40px; display: flex; align-items: center; gap: 8px; padding: 0 8px; background: #141414; border-bottom: 1px solid #262626"><span style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 6px; background: #1f1f1f">{daisy(16)}</span><span style="color: #a8a8a8">Daisy</span></div>' + canvas(270, home_bg + dlg6))

# 7 · missing image or font on the page
miss_img = f'''<div style="position: absolute; left: 24px; right: 24px; top: 14px; bottom: 0; padding: 16px 20px; display: grid; grid-template-columns: 1fr 260px; gap: 20px; background: #f6f1ea; color: #1d1a16">
<div style="font: 600 26px/1.1 'Fraunces', serif">Hand-thrown ceramics for everyday tables</div>
<div style="height: 130px; border-radius: 8px; background: repeating-linear-gradient(135deg, #e6dccd 0 10px, #ddd2c2 10px 20px); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; outline: 1.5px solid #d29922; outline-offset: -1.5px">
{icon('img-off', 18, '#6b6358')}<span style="font-family: {MONO}; font-size: 11px; color: #4a443c">bowls.jpg not found</span><span style="display: flex; gap: 6px"><span style="height: 22px; padding: 0 8px; display: flex; align-items: center; border-radius: 3px; background: #1f1f1f; color: #e8e8e8; font-size: 11px">Relink…</span><span style="height: 22px; padding: 0 8px; display: flex; align-items: center; border-radius: 3px; background: #1f1f1f; color: #e8e8e8; font-size: 11px">Pick from Assets</span></span></div></div>'''
c7 = frame(topbar(pill(icon('check', 11, '#3fb950', 2), 'Saved', '#939393')) + tabs([('Home', 'index.html', True, '')]) + canvas(170, miss_img)
           + f'<div style="height: 24px; display: flex; align-items: center; justify-content: center; gap: 6px; background: #181818; border-top: 1px solid #303030; font-size: 11px; color: #e3b34a">{icon("warning", 11, "#d29922", 1.5)}1 image not found on this page · <span style="color: #a9c8f7">Show in Assets</span></div>')

# 8 · folder permission when opening
dlg8 = f'''<div style="position: absolute; left: 180px; top: 22px; width: 520px; padding: 16px; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px; {POP}">
<div style="display: flex; align-items: center; gap: 10px">{icon('folder', 16, '#a8a8a8')}<b style="font-size: 14px; font-weight: 600">Let Daisy edit the Halden folder?</b></div>
<span style="font-size: 12px; line-height: 18px; color: #c8c8c8">Your browser will ask next. Daisy saves straight into {mono("D:\\Sites\\halden")} and never uploads your files.</span>
<div style="display: flex; gap: 8px">{btn('Open read-only', 'ghost')}<span style="flex: 1"></span>{btn('Continue', 'pri')}</div>
<span style="font-size: 11px; color: #939393">Read-only shows the pages; saving asks again.</span></div>'''
c8 = frame(f'<div style="height: 40px; display: flex; align-items: center; gap: 8px; padding: 0 8px; background: #141414; border-bottom: 1px solid #262626"><span style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 6px; background: #1f1f1f">{daisy(16)}</span><span style="color: #a8a8a8">Daisy</span></div>' + canvas(200, home_bg + dlg8))

cells = [('1 · Save status', 'In the top bar, left of Undo. Quiet when all is well; colour only when something needs you.', c1),
         ('2 · Couldn’t save', 'A banner under the top bar with the reason, the fix and a way to keep working. Nothing is lost.', c2),
         ('3 · Offline', 'Local saving keeps working; web fonts fall back and web images show a placeholder.', c3),
         ('4 · Changed outside Daisy', 'Another app edited a file you also changed. Shows what changed; the version not kept goes to Versions.', c4),
         ('5 · File missing', 'A page file was moved or deleted outside Daisy; its tab is struck through and the page offers ways back.', c5),
         ('6 · Recovered after a crash', 'On the next start, Home offers the recovered changes, page by page.', c6),
         ('7 · Missing image', 'The image keeps its size with a placeholder and Relink; the status bar counts what is missing.', c7),
         ('8 · Folder permission', 'Before the browser’s own prompt, Daisy says why it needs the folder and offers read-only.', c8)]
body = sheet_header('D-46', 'Saving and file problems', 'How Daisy shows saving, and what it does when a save fails, the computer is offline, files change or disappear outside Daisy, or the app closed unexpectedly. The rule: never lose work, say what happened, offer the fix.')
body += '<div style="display: grid; grid-template-columns: repeat(2, 880px); gap: 48px 32px; align-items: start">' + ''.join(f'<div>{cap(t, d)}{c}</div>' for t, d, c in cells) + '</div>'
H = int(sys.argv[1]) if len(sys.argv) > 1 else 1900
open('/home/claude/daisy/project/D46-SaveFileStates.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-46 Saving and file problems', 1920, H, body))
print('ok')
