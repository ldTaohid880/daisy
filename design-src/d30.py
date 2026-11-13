from screen import *
_src = open('/home/claude/ds/layoutadv.py').read()
LA = {}
exec(_src[:_src.index('# ═════ A · ROW')], LA)
L = LA

S = Screen('Daisy · D-30 Export dialog')
P['zip'] = ('stroke', 'M4 2h8v12H4zM8 2v2M8 5v1M8 7v1M7 9h2v2H7z')
P['folder-out'] = ('stroke', 'M1.5 4V13h13V5.5H8L6.5 3.5h-5zM8 7.5v4M6 9.5l2-2 2 2')
P['globe'] = ('stroke', 'M8 1.5a6.5 6.5 0 1 1 0 13 6.5 6.5 0 0 1 0-13zM1.5 8h13M8 1.5c2 2 2 11 0 13M8 1.5c-2 2-2 11 0 13')
sw = lambda on: f'<button role="switch" aria-checked="{str(on).lower()}" style="position: relative; width: 28px; height: 16px; flex: none; border-radius: 8px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {"#fff" if on else "#a8a8a8"}"></span></button>'
row = lambda label, sub, ctl: f'<div style="display: flex; align-items: center; gap: 10px; min-height: 30px; margin-bottom: 8px"><div style="flex: 1; min-width: 0"><div style="color: #e8e8e8">{label}</div>{f"<div style=\"font-size: 11px; line-height: 15px; color: #939393\">{sub}</div>" if sub else ""}</div>{ctl}</div>'
gh = lambda t, right='': f'<div style="display: flex; align-items: center; margin: 4px 0 2px; font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393"><span style="flex: 1">{t}</span>{right}</div>'
dd = lambda v, w=120: f'<button style="width: {w}px; height: 24px; display: flex; align-items: center; justify-content: space-between; padding: 0 8px; box-sizing: border-box; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #e8e8e8">{v}{icon("chev-down", 10, "#939393", 1.75)}</button>'

# ---------------- left: what you get ----------------
def fi(depth, ic, name, size='', note='', folder=False, on=False, tag=''):
    return (f'<div style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 10px 0 {10 + depth * 14}px; border-radius: 3px; {"background: rgba(47,128,237,0.16);" if on else ""}">'
            f'{icon("chev-down", 10, "#939393", 1.75) if folder else "<span style=\"width: 10px\"></span>"}{icon(ic, 13, "#a8a8a8")}'
            f'<span style="font-family: {MONO}; font-size: 11px; color: {"#e8e8e8" if folder or on else "#c8c8c8"}">{name}</span>{tag}<span style="flex: 1"></span>'
            f'<span style="font-size: 10px; color: #939393">{note}</span><span style="width: 52px; text-align: right; font-size: 11px; color: #a8a8a8; font-variant-numeric: tabular-nums">{size}</span></div>')
chg = lambda t, c='#3fb950': f'<span style="height: 14px; padding: 0 4px; border-radius: 3px; background: rgba(63,185,80,0.14); color: {c}; font-size: 9px; font-weight: 600; line-height: 14px">{t}</span>'
tree = (fi(0, 'folder', 'halden-site/', '640 KB', '', True)
        + fi(1, 'file', 'index.html', '18 KB', 'Home', on=True) + fi(1, 'file', 'shop.html', '14 KB', 'Shop', tag=chg('CHANGED', '#e3b34a').replace('rgba(63,185,80,0.14)', 'rgba(210,153,34,0.14)'))
        + fi(1, 'file', 'journal.html', '12 KB', 'Journal') + fi(1, 'file', 'visit.html', '9 KB', 'Visit')
        + fi(1, 'file', 'styles.css', '22 KB', 'all pages') + fi(1, 'file', 'animate.js', '3 KB', '2 sequences')
        + fi(1, 'folder', 'assets/', '', '', True) + fi(2, 'folder', 'images/', '512 KB', '6 · WebP', True) + fi(2, 'folder', 'fonts/', '58 KB', '2 · subset', True)
        + fi(1, 'file', 'sitemap.xml', '1 KB', '') + fi(1, 'file', 'robots.txt', '1 KB', ''))
preview = f'''<div style="padding: 8px 10px; border-radius: 4px; background: #1b1b1b; box-shadow: inset 0 0 0 1px #2c2c2c; font: 10.5px/16px {MONO}; color: #a8a8a8">
<div style="display: flex; justify-content: space-between; font-family: Inter, sans-serif; font-size: 10px; color: #939393; margin-bottom: 4px"><span>index.html · first lines</span><span>readable</span></div>
<span style="color: #8a8a8a">&lt;!</span><span style="color: #7fb0f0">doctype html</span><span style="color: #8a8a8a">&gt;</span><br>
<span style="color: #8a8a8a">&lt;</span><span style="color: #7fb0f0">html</span> lang=<span style="color: #9cc58a">"en"</span><span style="color: #8a8a8a">&gt;</span><br>
<span style="color: #8a8a8a">&lt;</span><span style="color: #7fb0f0">title</span><span style="color: #8a8a8a">&gt;</span>Halden — Hand-thrown ceramics<span style="color: #8a8a8a">&lt;/</span><span style="color: #7fb0f0">title</span><span style="color: #8a8a8a">&gt;</span><br>
<span style="color: #8a8a8a">&lt;</span><span style="color: #7fb0f0">link</span> rel=<span style="color: #9cc58a">"stylesheet"</span> href=<span style="color: #9cc58a">"styles.css"</span><span style="color: #8a8a8a">&gt;</span></div>'''
left = f'''<div style="width: 400px; flex: none; padding: 16px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px; border-right: 1px solid #3a3a3a; background: #222222">
<div style="display: flex; align-items: center; gap: 8px"><b style="font-weight: 600">What you get</b><span style="flex: 1"></span><span style="font-size: 11px; color: #939393">12 files</span></div>
{L['seg'](['This page', 'Changed pages · 1', 'All 4 pages'], 2)}
<div style="display: flex; flex-direction: column; gap: 1px">{tree}</div>
{preview}
<div style="font-size: 10px; line-height: 14px; color: #939393">Plain HTML, CSS and a small script · no Daisy runtime · opens straight from the folder</div></div>'''

# ---------------- right: where + how ----------------
dest = lambda ic, name, sub, on=False: (f'<button aria-pressed="{str(on).lower()}" style="flex: 1; display: flex; flex-direction: column; gap: 4px; padding: 10px; border-radius: 6px; text-align: left; {"background: rgba(47,128,237,0.14); box-shadow: inset 0 0 0 1px #2f80ed;" if on else "background: #2a2a2a;"}">'
                                        f'<span style="display: flex; align-items: center; gap: 6px; color: #e8e8e8">{icon(ic, 14, "#a9c8f7" if on else "#a8a8a8")}{name}</span><span style="font-size: 10px; line-height: 14px; color: #939393">{sub}</span></button>')
checks = f'''<div style="display: flex; flex-direction: column; gap: 6px; padding: 10px; border-radius: 6px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a">
<div style="display: flex; align-items: center; gap: 8px"><b style="font-weight: 600">Before you export</b><span style="flex: 1"></span><span style="font-size: 10px; color: #939393">nothing here blocks export</span></div>
<div style="display: flex; align-items: center; gap: 8px; font-size: 11px">{icon('warning', 12, '#d29922', 1.25)}<span style="flex: 1; color: #c8c8c8"><b style="font-weight: 600; color: #e8e8e8">1 needs attention</b> · Hero image has no description</span><button style="height: 20px; padding: 0 8px; border-radius: 3px; background: #333333; color: #e8e8e8">Fix</button></div>
<div style="display: flex; align-items: center; gap: 8px; font-size: 11px">{icon('info', 12, '#58a6ff', 1.25)}<span style="flex: 1; color: #c8c8c8">2 suggestions · add a focus style · social image missing</span><button style="height: 20px; padding: 0 8px; border-radius: 3px; color: #a9c8f7">Review</button></div>
<div style="display: flex; align-items: center; gap: 8px; font-size: 11px">{icon('check', 12, '#3fb950', 2)}<span style="color: #a8a8a8">All 23 links work · every page has a title · no unused images</span></div></div>'''
right = f'''<div style="flex: 1; min-width: 0; padding: 16px 20px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px">
<b style="font-weight: 600">Where it goes</b>
<div style="display: flex; gap: 8px">{dest('zip', 'Zip download', 'halden-site.zip · to your Downloads')}{dest('folder-out', 'Write to a folder', 'Keep a folder in sync · overwrites changed files', True)}{dest('globe', 'Publish', 'Coming later · connect a host')}</div>
<label style="height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 6px 0 10px; border-radius: 4px; background: #2a2a2a"><span style="font-family: {MONO}; font-size: 11px; flex: 1">D:\\Sites\\halden-site</span><span style="font-size: 10px; color: #3fb950">last export 2 days ago</span><button style="height: 22px; padding: 0 8px; border-radius: 3px; background: #333333; font-size: 11px; color: #c8c8c8">Change…</button></label>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0 28px">
<div>{gh('CODE')}
{row('Minify', 'Smaller files, harder to read', dd('CSS + JS', 96))}
{row('Class names', 'Readable keeps names like hero-title', L['seg'](['Readable', 'Short'], 0).replace('<div role="group"', '<div role="group" style="width: 140px;"', 1) if False else dd('Readable', 96))}
{row('CSS files', '', dd('One shared file', 130))}
{gh('EXTRAS')}
{row('sitemap.xml and robots.txt', 'For search engines', sw(True))}
{row('Include the .daisy source', 'Re-open and edit this export later', sw(False))}</div>
<div>{gh('IMAGES')}
{row('Format', 'Falls back to the original for old browsers', dd('WebP', 96))}
{row('Quality', '', '<span style="display: flex; align-items: center; gap: 8px; width: 140px"><span style="position: relative; flex: 1; height: 3px; border-radius: 2px; background: #454545"><span style="position: absolute; left: 0; width: 82%; height: 3px; border-radius: 2px; background: #2f80ed"></span><span style="position: absolute; left: calc(82% - 6px); top: -5px; width: 12px; height: 12px; border-radius: 6px; background: #e8e8e8"></span></span><span style="width: 22px; text-align: right; font-size: 11px">82</span></span>')}
{row('Make sizes for each screen', 'srcset · 640, 1024, 1440 wide', sw(True))}
{row('Inline images under 4 KB', 'Fewer requests', sw(False))}
{gh('FONTS')}
{row('Only the letters you use', 'Fraunces, Inter · −71%', sw(True))}</div></div>
{checks}</div>'''

dialog = f'''<!-- SCRIM + EXPORT DIALOG -->
<div aria-hidden="true" style="position: absolute; inset: 0; background: rgba(0,0,0,0.55); z-index: 50"></div>
<section role="dialog" aria-modal="true" aria-label="Export" style="position: absolute; left: calc(50% - 520px); top: 96px; width: 1040px; display: flex; flex-direction: column; background: #262626; border: 1px solid #454545; border-radius: 10px; box-shadow: 0 24px 64px rgba(0,0,0,0.6); overflow: hidden; z-index: 51">
<div style="height: 52px; flex: none; display: flex; align-items: center; gap: 10px; padding: 0 12px 0 20px; border-bottom: 1px solid #3a3a3a">
<span style="font-size: 15px; font-weight: 600">Export</span><span style="font-size: 12px; color: #939393">Halden · a static website you can host anywhere</span><span style="flex: 1"></span>
<button aria-label="Close" style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon('close', 14)}</button></div>
<div style="display: flex">{left}{right}</div>
<div style="height: 60px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 20px; border-top: 1px solid #3a3a3a; background: #222222">
<div style="display: flex; flex-direction: column"><span style="font-size: 13px; font-weight: 600; font-variant-numeric: tabular-nums">640 KB <span style="font-weight: 400; color: #939393">· from 1.8 MB</span></span><span style="font-size: 11px; color: #939393">Images and fonts are optimised · about 0.4 s on 4G</span></div>
<span style="flex: 1"></span>
<label style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a8a8a8"><span style="width: 14px; height: 14px; border-radius: 3px; background: #246bcb; display: flex; align-items: center; justify-content: center">{icon('check', 10, '#fff', 2.25)}</span>Open the folder after</label>
<button style="height: 32px; padding: 0 16px; border-radius: 6px; color: #e8e8e8; box-shadow: inset 0 0 0 1px #454545">Cancel</button>
<button style="height: 32px; padding: 0 18px; border-radius: 6px; background: #246bcb; color: #fff; font-weight: 600">Export 12 files</button></div></section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', dialog + '\n<!-- ═══════════ TOP BAR v3')
S.save('D30-Export.dc.html')
print('ok')
