from screen import *
P['arrow'] = ('stroke', 'M3 8h10M9 4l4 4-4 4')
S = Screen('Daisy · D-45 Import an HTML page')
POP = 'background: #262626; border: 1px solid #454545; border-radius: 6px;'
sw_ = lambda on: f'<span role="switch" aria-checked="{str(on).lower()}" style="position: relative; width: 28px; height: 16px; flex: none; border-radius: 8px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {"#fff" if on else "#a8a8a8"}"></span></span>'
chk = lambda on: f'<span style="width: 14px; height: 14px; flex: none; border-radius: 3px; display: flex; align-items: center; justify-content: center; {"background: #246bcb;" if on else "box-shadow: inset 0 0 0 1px #6b6b6b;"}">{icon("check", 10, "#fff", 2) if on else ""}</span>'
h3 = lambda t, right='': f'<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px"><span style="font-weight: 600">{t}</span><span style="flex: 1"></span>{right}</div>'
mono = lambda t, c='#c8c8c8': f'<span style="font-family: {MONO}; font-size: 11px; color: {c}">{t}</span>'
swc = lambda c: f'<span style="width: 16px; height: 16px; flex: none; border-radius: 3px; background: {c}; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.12)"></span>'
fld = lambda inner: f'<span style="height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 10px; box-sizing: border-box; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a">{inner}</span>'

# left: preview of the incoming page
thumb = '''<div style="height: 360px; border-radius: 6px; overflow: hidden; background: #fbf9f6; box-shadow: 0 0 0 1px #3a3a3a; position: relative; color: #2b2622">
<div style="height: 30px; display: flex; align-items: center; justify-content: space-between; padding: 0 14px; background: #2b2622; color: #f3ede4; font: 600 11px/1 Georgia, serif">Halden Pottery<span style="display: flex; gap: 10px; font: 9px Arial">Home · About · Shop · Contact</span></div>
<div style="padding: 18px 14px 0; font: 600 20px/1.15 Georgia, serif">About the studio</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 10px 14px">
<div style="display: flex; flex-direction: column; gap: 5px">''' + ''.join('<span style="height: 5px; border-radius: 1px; background: #c8bfb3"></span>' for _ in range(8)) + '''</div>
<div style="height: 96px; border-radius: 3px; background: #d8cbb8"></div></div>
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; padding: 10px 14px">''' + ''.join(f'<span style="height: 64px; border-radius: 3px; background: {c}"></span>' for c in ['#cfb9a3', '#e6dccd', '#c9b89f']) + '''</div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 44px; background: #b4542e; color: #fff; display: flex; align-items: center; justify-content: center; font: 11px Arial">Visit us on Saturdays · Riverside Works</div></div>'''
left = f'''<div style="width: 300px; flex: none; padding: 18px; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px; border-right: 1px solid #3a3a3a; background: #222222">
{thumb}
<div style="display: flex; flex-direction: column; gap: 4px; font-size: 11px; line-height: 16px; color: #a8a8a8">
<span style="color: #e8e8e8; font-weight: 500">{mono('about.html', '#e8e8e8')} · 48 KB</span><span>{mono('D:\\Mine\\old-site\\', '#939393')}</span>
<span>142 elements · 2 stylesheets · 6 images · 1 script · 1 font</span></div></div>'''

# middle: settings and the report
opt = lambda t, d, on=False, tag='': (f'<div role="radio" aria-checked="{str(on).lower()}" style="display: flex; gap: 10px; padding: 10px 12px; border-radius: 6px; {"background: rgba(47,128,237,0.14); box-shadow: inset 0 0 0 1px #2f80ed;" if on else "background: #2a2a2a;"}">'
    f'<span style="width: 14px; height: 14px; margin-top: 1px; flex: none; box-sizing: border-box; border-radius: 7px; {"border: 4px solid #2f80ed;" if on else "border: 1.5px solid #6b6b6b;"}"></span>'
    f'<span style="display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 500">{t}{f"<span style=\"margin-left: 6px; padding: 1px 5px; border-radius: 3px; background: #333333; font-size: 10px; font-weight: 400; color: #a8a8a8\">{tag}</span>" if tag else ""}</span><span style="font-size: 11px; line-height: 15px; color: #a8a8a8">{d}</span></span></div>')
how = (h3('How to bring it in') + '<div style="display: flex; flex-direction: column; gap: 6px">'
       + opt('Keep it as it is', 'Same HTML and CSS. Edit it as it is; nothing is linked to the design system.')
       + opt('Tidy it up', 'Same look. Inline styles become classes, unused CSS is removed (Bootstrap 160 KB → 9 KB), colours and sizes are linked to tokens where they match.', True, 'Recommended')
       + opt('Rebuild with Daisy layouts', 'Floats and Bootstrap columns become Row and Grid. Best for pages you will keep editing; check the result.') + '</div>')
match = lambda found, arrow, token, note, tc='#c8c8c8', on=True: (f'<div style="height: 30px; display: grid; grid-template-columns: 16px 16px 86px 16px minmax(0, 1fr) auto; align-items: center; gap: 8px; padding: 0 8px; border-radius: 4px; background: #2a2a2a">'
    f'{chk(on)}{swc(found)}{mono(found.upper())}{icon("arrow", 12, "#6b6b6b")}<span style="display: flex; align-items: center; gap: 6px; min-width: 0; color: {tc}">{token}</span><span style="font-size: 10px; color: #939393; white-space: nowrap">{note}</span></div>')
tok = lambda c, n: f'{swc(c)}<span style="font-weight: 500">{n}</span>'
colours = (h3('Colours · 9 found', '<span style="font-size: 11px; color: #939393">4 same · 3 close · 2 new</span>')
           + '<div style="display: flex; flex-direction: column; gap: 3px">'
           + match('#1d1a16', '', tok('#1d1a16', 'ink'), 'same') + match('#b4542e', '', tok('#b5532d', 'brand'), 'close · ΔE 0.4')
           + match('#f3ede4', '', tok('#f6f1ea', 'sand'), 'close · ΔE 1.9') + match('#6a6a6a', '', '<span style="color: #a8a8a8">Keep as a plain value</span>', 'new · 3 uses', on=False)
           + '<div style="font-size: 11px; color: #939393; padding: 4px 2px">+ 5 more · <button style="font-size: 11px; color: #a9c8f7">Review all</button> · new colours can be <button style="font-size: 11px; color: #a9c8f7">saved as tokens</button></div></div>')
other = (h3('Also')
         + '<div style="display: flex; flex-direction: column; gap: 6px; font-size: 12px">'
         + f'<span style="display: flex; align-items: center; gap: 8px">{chk(True)}Copy 6 images into Assets <span style="color: #939393; font-size: 11px">(2 are larger than needed · resized on export)</span></span>'
         + f'<span style="display: flex; align-items: center; gap: 8px">{chk(True)}Add the font Lora to the project <span style="color: #939393; font-size: 11px">(Google Fonts)</span></span>'
         + f'<span style="display: flex; align-items: center; gap: 8px">{chk(True)}Map 7 text sizes to text styles <span style="color: #939393; font-size: 11px">(h1 → Display, p → Body …)</span></span>'
         + f'<span style="display: flex; align-items: center; gap: 8px">{chk(False)}Use its header and footer on every page <span style="color: #939393; font-size: 11px">(Halden already has them)</span></span></div>')
mid = f'''<div style="flex: 1; min-width: 0; padding: 18px 22px; box-sizing: border-box; display: flex; flex-direction: column; gap: 16px">
<div style="display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 12px">
<div><div style="margin-bottom: 6px; font-size: 11px; color: #a8a8a8">Page name</div>{fld("About")}</div>
<div><div style="margin-bottom: 6px; font-size: 11px; color: #a8a8a8">File in Halden</div>{fld(mono("about.html", "#e8e8e8") + '<span style="flex: 1"></span><span style="font-size: 10px; color: #3fb950">free</span>')}</div></div>
{how}{colours}{other}</div>'''

# right: notes
note = lambda ic, c, t, d: f'<div style="display: flex; gap: 10px; padding: 10px; border-radius: 4px; background: #2a2a2a">{icon(ic, 14, c, 1.5)}<span style="display: flex; flex-direction: column; gap: 2px; font-size: 11px; line-height: 15px"><span style="color: #e8e8e8; font-weight: 500">{t}</span><span style="color: #a8a8a8">{d}</span></span></div>'
right = f'''<aside style="width: 300px; flex: none; padding: 18px; box-sizing: border-box; display: flex; flex-direction: column; gap: 8px; border-left: 1px solid #3a3a3a; background: #222222">
<span style="font-size: 11px; font-weight: 500; letter-spacing: 0.04em; color: #939393">BEFORE YOU IMPORT · 4 NOTES</span>
{note('info', '#58a6ff', '2 positioned elements', 'They become Free elements; everything else stays in flow.')}
{note('info', '#58a6ff', 'Bootstrap columns', 'Kept as they are. Choose Rebuild to turn them into Grid.')}
{note('warning', '#d29922', '1 script (jquery.min.js)', 'Kept in the file and exported, but not run in the editor.')}
{note('warning', '#d29922', '3 images have no description', 'Listed in Accessibility after import.')}
<span style="flex: 1"></span>
<span style="font-size: 11px; line-height: 15px; color: #939393">The original file is not changed. Undo removes the imported page.</span></aside>'''

dialog = f'''<!-- SCRIM + IMPORT -->
<div aria-hidden="true" style="position: absolute; inset: 0; background: rgba(0,0,0,0.55); z-index: 50"></div>
<section role="dialog" aria-modal="true" aria-label="Import a page" style="position: absolute; left: calc(50% - 620px); top: 96px; width: 1240px; display: flex; flex-direction: column; background: #262626; border: 1px solid #454545; border-radius: 10px; box-shadow: 0 16px 48px rgba(0,0,0,0.55); z-index: 51; overflow: hidden">
<div style="height: 52px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 12px 0 20px; border-bottom: 1px solid #3a3a3a">
<span style="font-size: 15px; font-weight: 600">Import a page</span><span style="font-size: 12px; color: #939393">into Halden</span><span style="flex: 1"></span>
<button style="height: 26px; padding: 0 10px; border-radius: 4px; box-shadow: inset 0 0 0 1px #454545; font-size: 11px">Choose another file…</button>
<button aria-label="Close" style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon('close', 14)}</button></div>
<div style="display: flex; min-height: 640px">{left}{mid}{right}</div>
<div style="height: 56px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 20px; border-top: 1px solid #3a3a3a; background: #222222">
<span style="font-size: 11px; color: #939393">Also: drop .html files on the Project panel, or File › Import › HTML page</span><span style="flex: 1"></span>
<button style="height: 32px; padding: 0 14px; border-radius: 6px; color: #a8a8a8">Cancel</button>
<button style="height: 32px; padding: 0 18px; border-radius: 6px; background: #246bcb; color: #fff; font-weight: 600">Import page</button></div></section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', dialog + '\n<!-- ═══════════ TOP BAR v3')
S.save('D45-ImportPage.dc.html')
print('ok')
