from screen import *
P['type'] = ('stroke', 'M3 4V3h10v1M8 3v10M6 13h4')
P['redirect'] = ('stroke', 'M2 5h8a3 3 0 0 1 0 6H6M9 8l3-3-3-3')
P['devices'] = ('stroke', 'M1.5 3h9v7h-9zM4 12.5h4M12 6h2.5v7.5H12z')
P['upload2'] = ('stroke', 'M8 11V3M5 6l3-3 3 3M3 13h10')
S = Screen('Daisy · D-44 Project settings')
sw = lambda on: f'<span role="switch" aria-checked="{str(on).lower()}" style="position: relative; width: 28px; height: 16px; flex: none; border-radius: 8px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {"#fff" if on else "#a8a8a8"}"></span></span>'
segm = lambda items, sel: '<div role="group" style="display: grid; grid-template-columns: repeat(' + str(len(items)) + ', minmax(0, 1fr)); gap: 2px; padding: 2px; background: #1f1f1f; border-radius: 4px; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px">' + ''.join(f'<button aria-pressed="{str(i == sel).lower()}" style="height: 24px; padding: 0 8px; white-space: nowrap; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #a8a8a8;"}">{t}</button>' for i, t in enumerate(items)) + '</div>'
dd = lambda v, sub='': f'<button style="width: 100%; height: 30px; display: flex; align-items: center; gap: 8px; padding: 0 10px; box-sizing: border-box; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; color: #e8e8e8"><span>{v}</span><span style="flex: 1; text-align: left; font-family: {MONO}; font-size: 11px; color: #939393">{sub}</span>{icon("chev-down", 10, "#939393", 1.75)}</button>'
field = lambda label, ctl, help_='': f'<div style="min-width: 0"><div style="margin-bottom: 6px; font-size: 12px">{label}</div>{ctl}{f"<div style=\"margin-top: 4px; font-size: 11px; line-height: 15px; color: #939393\">{help_}</div>" if help_ else ""}</div>'
def vtab(ic, t, on=False, n=''):
    return (f'<button role="tab" aria-selected="{str(on).lower()}" style="width: 100%; height: 34px; display: flex; align-items: center; gap: 10px; padding: 0 12px; box-sizing: border-box; border-radius: 6px; text-align: left; {"background: #333333; color: #e8e8e8; font-weight: 500;" if on else "color: #a8a8a8;"}">'
            f'{icon(ic, 15, "#e8e8e8" if on else "#939393")}<span style="flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis" title="{t}">{t}</span><span style="font-size: 11px; color: #939393">{n}</span></button>')
nav = f'''<nav aria-label="Project settings" style="width: 210px; flex: none; padding: 12px 10px; box-sizing: border-box; display: flex; flex-direction: column; gap: 2px; border-right: 1px solid #3a3a3a; background: #222222">
{vtab('gear', 'General')}{vtab('type', 'Fonts', True, '3')}{vtab('devices', 'Screen sizes', n='3')}{vtab('redirect', 'Redirects', n='2')}{vtab('code', 'Site-wide code')}{vtab('external', 'Export defaults')}
<div style="flex: 1"></div>
<div style="padding: 8px 10px; font-size: 11px; line-height: 15px; color: #939393">Colours, type sizes and spacing are tokens: <button style="color: #a9c8f7; font-size: 11px">Design system</button></div></nav>'''

def font_row(name, ff, src, weights, used, kb, on=False, warn=''):
    chips = ''.join(f'<span style="height: 18px; padding: 0 6px; border-radius: 3px; background: {"#333333" if w[1] else "transparent"}; box-shadow: inset 0 0 0 1px {"#454545" if w[1] else "#333333"}; font-size: 10px; line-height: 18px; color: {"#e8e8e8" if w[1] else "#6b6b6b"}">{w[0]}</span>' for w in weights)
    return (f'<div style="display: grid; grid-template-columns: 200px minmax(0, 1fr) 70px 20px; align-items: center; gap: 14px; padding: 10px 12px; border-radius: 6px; {"background: rgba(47,128,237,0.12); box-shadow: inset 0 0 0 1px #2f80ed;" if on else "background: #2a2a2a;"}">'
            f'<div style="display: flex; flex-direction: column; gap: 4px; min-width: 0"><span style="font-family: {ff}; font-size: 22px; line-height: 1.1; white-space: nowrap">Hand-thrown</span><span style="font-size: 11px; color: #939393"><b style="font-weight: 600; color: #e8e8e8">{name}</b> · {src}</span></div>'
            f'<div style="display: flex; flex-direction: column; gap: 6px; min-width: 0"><span style="display: flex; flex-wrap: wrap; gap: 4px">{chips}</span><span style="font-size: 11px; color: #939393; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{used}</span></div>'
            f'<span style="font-size: 11px; color: {"#e3b34a" if warn else "#c8c8c8"}; text-align: right; font-variant-numeric: tabular-nums">{kb}</span>{icon("more", 13, "#a8a8a8")}</div>')
fonts = (font_row('Fraunces', "'Fraunces', serif", 'Google Fonts · variable', [('300', False), ('400', True), ('600', True), ('Italic', False), ('opsz', True)], 'Display, Heading 2, Heading 3 · --font-heading', '62 KB', True)
         + font_row('Inter', "'Inter', sans-serif", 'Google Fonts · variable', [('400', True), ('500', True), ('600', True), ('700', False)], 'Body, Eyebrow, buttons · --font-body', '48 KB')
         + font_row('JetBrains Mono', "'JetBrains Mono', monospace", 'Google Fonts', [('400', True)], 'Code blocks · not used on any page yet', '22 KB'))
budget = f'''<div style="display: flex; align-items: center; gap: 10px; font-size: 11px; color: #a8a8a8"><span>Fonts per page</span>
<span style="flex: 1; height: 6px; border-radius: 3px; background: #1f1f1f; overflow: hidden; display: flex"><span style="width: 37%; background: #2f80ed"></span><span style="width: 18%; background: rgba(47,128,237,0.45)"></span></span>
<span style="color: #c8c8c8">110 KB on Home</span><span>· budget 300 KB</span></div>'''
main = f'''<div style="flex: 1; min-width: 0; padding: 18px 22px; box-sizing: border-box; display: flex; flex-direction: column; gap: 14px">
<div style="display: flex; align-items: center; gap: 10px"><span style="font-size: 14px; font-weight: 600">Fonts</span><span style="font-size: 11px; color: #939393">Only the weights in use are exported</span><span style="flex: 1"></span>
<button style="height: 28px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; white-space: nowrap; box-shadow: inset 0 0 0 1px #454545">{icon("upload2", 12, "#a8a8a8")}Upload…</button>
<button style="height: 28px; display: flex; align-items: center; gap: 6px; padding: 0 12px; border-radius: 4px; white-space: nowrap; background: #246bcb; color: #fff; font-weight: 500">{icon("plus", 11, "currentColor", 2)}Add from Google Fonts</button></div>
<div style="display: flex; flex-direction: column; gap: 6px">{fonts}</div>
{budget}
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; padding-top: 12px; border-top: 1px solid #333333">
{field('Load fonts', segm(['Self-host on export', 'From Google'], 0), 'Self-hosting is faster and keeps visitors private')}
{field('While loading', dd('Fallback, then swap'), 'font-display: swap · text is never invisible')}
{field('Characters', dd('Latin + Latin Ext.'), 'Add Cyrillic, Greek or others if a page needs them')}
</div></div>'''

# right column: fallback match for the selected font
preview = f'''<aside style="width: 320px; flex: none; padding: 18px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px; border-left: 1px solid #3a3a3a; background: #222222">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 11px; font-weight: 500; letter-spacing: 0.04em; color: #939393">FALLBACK · FRAUNCES</span>{sw(True)}</div>
<div style="position: relative; padding: 14px; border-radius: 6px; background: #f6f1ea; color: #1d1a16">
<div style="font: 600 24px/1.05 'Fraunces', serif; white-space: nowrap">Hand-thrown pots</div>
<div style="position: absolute; left: 14px; top: 14px; font: 600 23.4px/1.05 Georgia, serif; white-space: nowrap; color: rgba(181,83,45,0.55)">Hand-thrown pots</div></div>
<div style="display: flex; gap: 12px; font-size: 11px; color: #a8a8a8"><span style="display: flex; align-items: center; gap: 6px"><span style="width: 10px; height: 10px; border-radius: 2px; background: #1d1a16"></span>Fraunces</span><span style="display: flex; align-items: center; gap: 6px"><span style="width: 10px; height: 10px; border-radius: 2px; background: rgba(181,83,45,0.55)"></span>Georgia, adjusted</span></div>
{field('Fallback', dd('Georgia', 'serif'))}
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; font-size: 11px">
{f('<span style="color: #939393">Size</span><span style="flex: 1; text-align: right">97.5%</span>')}{f('<span style="color: #939393">Ascent</span><span style="flex: 1; text-align: right">92%</span>')}</div>
<div style="font-size: 11px; line-height: 15px; color: #939393">Matched so the page does not jump when Fraunces arrives. <span style="color: #3fb950">Layout shift 0.01</span></div>
<code style="margin-top: auto; font-family: {MONO}; font-size: 10px; line-height: 15px; color: #939393; white-space: pre">@font-face {{ font-family: "Fraunces fallback";
  src: local("Georgia"); size-adjust: 97.5%; }}</code></aside>'''

dialog = f'''<!-- SCRIM + PROJECT SETTINGS -->
<div aria-hidden="true" style="position: absolute; inset: 0; background: rgba(0,0,0,0.55); z-index: 50"></div>
<section role="dialog" aria-modal="true" aria-label="Project settings" style="position: absolute; left: calc(50% - 600px); top: 120px; width: 1200px; display: flex; flex-direction: column; background: #262626; border: 1px solid #454545; border-radius: 10px; box-shadow: 0 16px 48px rgba(0,0,0,0.55); z-index: 51; overflow: hidden">
<div style="height: 52px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 12px 0 20px; border-bottom: 1px solid #3a3a3a">
<span style="font-size: 15px; font-weight: 600">Project settings</span><span style="font-size: 12px; color: #939393">Halden · 4 pages</span><span style="flex: 1"></span>
<label style="width: 260px; height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 10px; box-sizing: border-box; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; color: #939393">{icon('search', 12, '#939393')}Find a setting</label>
<button aria-label="Close" style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon('close', 14)}</button></div>
<div style="display: flex; min-height: 520px">{nav}{main}{preview}</div>
<div style="height: 54px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 20px; border-top: 1px solid #3a3a3a; background: #222222">
<span style="font-size: 11px; color: #939393">Applies to every page · Ctrl+Z undoes · one page only: Page settings</span><span style="flex: 1"></span>
<button style="height: 32px; padding: 0 18px; border-radius: 6px; background: #246bcb; color: #fff; font-weight: 600">Done</button></div></section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', dialog + '\n<!-- ═══════════ TOP BAR v3')
S.save('D44-ProjectSettings.dc.html')
print('ok')
