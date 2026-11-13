from screen import *

S = Screen('Daisy · D-32 Versions')
# page markup for the thumbnails (no overlays)
T = Screen('tmp'); T.remove_h1_overlay(); T.remove_parent_outline()
src = T.s
a = src.index('<!-- Header -->', src.index('<!-- page frame')); b = src.index('<!-- fold line at 900 -->', a)
pg = src[a:b]
old_pg = (pg.replace('Hand-thrown ceramics for everyday tables', 'Ceramics made by the river')
          .replace('<a href="#shop" style="background: #b5532d;', '<a href="#shop" style="background: #1d1a16;'))

P['restore'] = ('stroke', 'M3 8a5 5 0 1 0 1.5-3.5M3 2.5v3h3')
P['pin'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
P['copy'] = P['copy']
SC = 0.2
H = 296
thumb = lambda html: f'<div style="width: {1440 * SC:.0f}px; height: {H}px; overflow: hidden"><div style="width: 1440px; transform: scale({SC}); transform-origin: 0 0; background: #f6f1ea; color: #1d1a16; font-family: Inter, sans-serif; font-size: 16px; line-height: 1.5">{html}</div></div>'
mark = lambda l, t, w, h, n: f'<span style="position: absolute; left: {l}px; top: {t}px; width: {w}px; height: {h}px; border: 1.5px solid #2f80ed; border-radius: 3px; background: rgba(47,128,237,0.10)"><span style="position: absolute; left: -8px; top: -8px; width: 16px; height: 16px; border-radius: 8px; background: #2f80ed; color: #fff; font-size: 10px; font-weight: 600; line-height: 16px; text-align: center">{n}</span></span>'
pane = lambda label, html, marks: f'<div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 11px; color: #a8a8a8">{label}</span><div style="position: relative; border-radius: 6px; overflow: hidden; box-shadow: 0 0 0 1px #3a3a3a">{thumb(html)}{marks}</div></div>'
compare = f'<div style="display: flex; gap: 16px; justify-content: center">{pane("Yesterday 16:40", old_pg, mark(9, 54, 126, 36, 1) + mark(9, 104, 46, 12, 2))}{pane("Now", pg, mark(9, 50, 126, 48, 1) + mark(9, 112, 46, 12, 2))}</div>'
def ver(time, title, sub, named=False, on=False, now=False):
    return (f'<button aria-pressed="{str(on).lower()}" style="width: 100%; padding: 8px 10px; box-sizing: border-box; display: flex; gap: 10px; border-radius: 6px; text-align: left; {"background: rgba(47,128,237,0.16); box-shadow: inset 0 0 0 1px #2f80ed;" if on else ""}">'
            f'<span style="width: 8px; height: 8px; margin-top: 5px; flex: none; border-radius: 4px; {"background: #3fb950;" if now else ("background: #e8e8e8;" if named else "box-shadow: inset 0 0 0 1.5px #6b6b6b;")}"></span>'
            f'<span style="flex: 1; min-width: 0"><span style="display: flex; gap: 8px"><span style="flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; color: #e8e8e8; {"font-weight: 600;" if named else ""}">{title}</span><span style="font-size: 11px; color: #939393; white-space: nowrap">{time}</span></span>'
            f'<span style="display: block; font-size: 11px; line-height: 15px; color: #939393; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{sub}</span></span></button>')
day = lambda t: f'<div style="padding: 10px 10px 4px; font-size: 10px; font-weight: 600; letter-spacing: 0.06em; color: #6b6b6b">{t}</div>'
seg = lambda items, sel: '<div role="group" style="display: grid; grid-template-columns: repeat(' + str(len(items)) + ', minmax(0, 1fr)); gap: 2px; padding: 2px; background: #1f1f1f; border-radius: 4px; font-size: 11px">' + ''.join(f'<button style="height: 22px; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #a8a8a8;"}">{t}</button>' for i, t in enumerate(items)) + '</div>'
listing = f'''<div style="width: 300px; flex: none; display: flex; flex-direction: column; border-right: 1px solid #3a3a3a; background: #222222">
<div style="padding: 12px 12px 6px; display: flex; flex-direction: column; gap: 8px">{seg(['All', 'Named'], 0)}</div>
<div style="flex: 1; padding: 0 8px; overflow: hidden">
{day('TODAY')}
{ver('now', 'Current', 'Unsaved changes · Hero title, Book a visit', now=True)}
{ver('13:05', 'Before the Tablet pass', 'Named by you · 14 changes', named=True)}
{ver('11:20', 'Autosave', '6 changes · This season cards')}
{day('YESTERDAY')}
{ver('16:40', 'Autosave', '3 changes · hero headline, button colour', on=True)}
{ver('14:02', 'First full draft', 'Named by you · 4 pages', named=True)}
{ver('10:15', 'Autosave', '9 changes · Footer, Nav links')}
{day('10 NOV')}
{ver('18:30', 'Project created', 'From the Shop template')}
</div>
<div style="padding: 10px 12px; border-top: 1px solid #3a3a3a; font-size: 11px; line-height: 15px; color: #939393">Autosaves every 10 minutes while you work · named versions are kept for good</div></div>'''
detail = f'''<div style="flex: 1; min-width: 0; padding: 16px 20px; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px">
<div style="display: flex; align-items: center; gap: 10px"><div style="flex: 1"><div style="font-size: 14px; font-weight: 600">Autosave · Yesterday 16:40</div><div style="font-size: 11px; color: #939393">Home · changed areas are outlined</div></div>
{seg(['Side by side', 'This version'], 0).replace('display: grid;', 'display: grid; width: 180px;', 1)}</div>
{compare}
<div style="display: flex; flex-direction: column; gap: 4px; padding: 10px 12px; border-radius: 6px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; line-height: 16px">
<div style="font-weight: 600; color: #e8e8e8">Different from now</div>
<div style="color: #c8c8c8"><b style="color: #a9c8f7">1</b> Hero title text · “Ceramics made by the river”</div>
<div style="color: #c8c8c8"><b style="color: #a9c8f7">2</b> Shop the collection · fill ink instead of terracotta</div>
<div style="color: #939393">+ 1 more on Shop · 0 on Journal and Visit</div></div></div>'''

dialog = f'''<!-- SCRIM + VERSIONS -->
<div aria-hidden="true" style="position: absolute; inset: 0; background: rgba(0,0,0,0.55); z-index: 50"></div>
<section role="dialog" aria-modal="true" aria-label="Versions" style="position: absolute; left: calc(50% - 470px); top: 110px; width: 940px; display: flex; flex-direction: column; background: #262626; border: 1px solid #454545; border-radius: 10px; box-shadow: 0 24px 64px rgba(0,0,0,0.6); overflow: hidden; z-index: 51">
<div style="height: 52px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 12px 0 20px; border-bottom: 1px solid #3a3a3a">
<span style="font-size: 15px; font-weight: 600">Versions</span><span style="font-size: 12px; color: #939393">Halden · all pages</span><span style="flex: 1"></span>
<button style="height: 28px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; background: #2a2a2a; font-size: 12px; color: #e8e8e8">{icon('pin', 12)}Name the current version</button>
<button aria-label="Close" style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon('close', 14)}</button></div>
<div style="display: flex; height: 560px">{listing}{detail}</div>
<div style="height: 56px; flex: none; display: flex; align-items: center; gap: 10px; padding: 0 20px; border-top: 1px solid #3a3a3a; background: #222222">
<span style="font-size: 11px; color: #939393">Restoring never deletes anything · the current state is saved as a version first</span><span style="flex: 1"></span>
<button style="height: 32px; display: flex; align-items: center; gap: 6px; padding: 0 14px; border-radius: 6px; color: #e8e8e8; box-shadow: inset 0 0 0 1px #454545">{icon('copy', 13)}Restore as a copy</button>
<button style="height: 32px; display: flex; align-items: center; gap: 6px; padding: 0 16px; border-radius: 6px; background: #246bcb; color: #fff; font-weight: 600">{icon('restore', 13, '#fff')}Restore this version</button></div></section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', dialog + '\n<!-- ═══════════ TOP BAR v3')
S.save('D32-Versions.dc.html')
print('ok')
