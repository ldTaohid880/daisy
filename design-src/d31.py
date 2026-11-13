from screen import *

S = Screen('Daisy · D-31 Page settings')
P['palette'] = ('stroke', 'M8 1.5a6.5 6.5 0 1 0 0 13c1 0 1.5-.6 1.5-1.4 0-1.2-1-1.3-1-2.3 0-.8.6-1.3 1.5-1.3h1.6a2.9 2.9 0 0 0 2.9-2.9C14.5 4 11.6 1.5 8 1.5z')
P['share'] = ('stroke', 'M10.5 4.5L8 2 5.5 4.5M8 2v8M3.5 8v5.5h9V8')
sw = lambda on: f'<button role="switch" aria-checked="{str(on).lower()}" style="position: relative; width: 28px; height: 16px; flex: none; border-radius: 8px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {"#fff" if on else "#a8a8a8"}"></span></button>'
cnt = lambda n, mx: f'<span style="font-size: 10px; color: {"#939393" if n <= mx else "#e3b34a"}; font-variant-numeric: tabular-nums">{n} / {mx}</span>'
inp = lambda v, focus=False, mono=False, h=30: f'<div style="min-height: {h}px; display: flex; align-items: center; padding: 6px 10px; box-sizing: border-box; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px {"#2f80ed" if focus else "#3a3a3a"}; line-height: 18px; {"font-family: " + MONO + "; font-size: 11px;" if mono else ""}">{v}</div>'
dd = lambda v, sub='': f'<button style="width: 100%; height: 30px; display: flex; align-items: center; gap: 8px; padding: 0 10px; box-sizing: border-box; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; color: #e8e8e8"><span>{v}</span><span style="flex: 1; text-align: left; font-family: {MONO}; font-size: 11px; color: #939393">{sub}</span>{icon("chev-down", 10, "#939393", 1.75)}</button>'
segm = lambda items, sel: '<div role="group" style="display: grid; grid-template-columns: repeat(' + str(len(items)) + ', minmax(0, 1fr)); gap: 2px; padding: 2px; background: #1f1f1f; border-radius: 4px; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px">' + ''.join(f'<button aria-pressed="{str(i == sel).lower()}" style="height: 24px; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #a8a8a8;"}">{t}</button>' for i, t in enumerate(items)) + '</div>'
field = lambda label, ctl, help_='', right='': f'<div><div style="display: flex; align-items: baseline; gap: 8px; margin-bottom: 6px"><span style="font-size: 12px; color: #e8e8e8">{label}</span><span style="flex: 1"></span>{right}</div>{ctl}{f"<div style=\"margin-top: 4px; font-size: 11px; line-height: 15px; color: #939393\">{help_}</div>" if help_ else ""}</div>'

def vtab(ic, t, on=False, warn=False):
    return (f'<button role="tab" aria-selected="{str(on).lower()}" style="width: 100%; height: 34px; display: flex; align-items: center; gap: 10px; padding: 0 12px; box-sizing: border-box; border-radius: 6px; text-align: left; {"background: #333333; color: #e8e8e8; font-weight: 500;" if on else "color: #a8a8a8;"}">'
            f'{icon(ic, 15, "#e8e8e8" if on else "#939393")}<span style="flex: 1">{t}</span>{icon("warning", 12, "#d29922", 1.25) if warn else ""}</button>')
nav = f'''<nav aria-label="Page settings" style="width: 200px; flex: none; padding: 12px 10px; box-sizing: border-box; display: flex; flex-direction: column; gap: 2px; border-right: 1px solid #3a3a3a; background: #222222">
{vtab('file', 'General', True)}{vtab('share', 'Search and social', warn=True)}{vtab('palette', 'Appearance')}{vtab('code', 'Code')}{vtab('sliders', 'Advanced')}
<div style="flex: 1"></div>
<div style="padding: 8px 10px; font-size: 11px; line-height: 15px; color: #939393">Fonts, screen sizes, redirects and site-wide code: <button style="color: #a9c8f7; font-size: 11px">Project settings</button></div></nav>'''

general = f'''<div style="flex: 1; min-width: 0; padding: 18px 22px; box-sizing: border-box; display: flex; flex-direction: column; gap: 16px">
{field('Page title', inp('Halden — Hand-thrown ceramics for everyday tables', True), 'The browser tab and the headline in search results', cnt(50, 60))}
{field('Description', inp('Small-batch stoneware, wheel-thrown and fired in our studio by the river. Shop bowls, mugs and plates made slowly and used daily.', h=56), 'The text under the headline in search results', cnt(138, 160) + '<button style="margin-left: 8px; font-size: 11px; color: #a9c8f7">Use first paragraph</button>')}
<div style="display: grid; grid-template-columns: minmax(0, 1.3fr) minmax(0, 1fr); gap: 14px">
{field('Address', f'<div style="height: 30px; display: flex; align-items: center; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-family: {MONO}; font-size: 11px"><span style="padding: 0 2px 0 10px; color: #939393">halden.studio</span><span>/</span><span style="flex: 1"></span><span style="margin-right: 6px; padding: 0 6px; border-radius: 3px; background: #333333; font-family: Inter, sans-serif; font-size: 10px; line-height: 18px; color: #c8c8c8">home</span></div>', 'Saved as index.html')}
{field('Language', dd('English', 'en'), 'Read by screen readers')}</div>
{field('Status', segm(['Draft', 'Published'], 1), 'Drafts are left out of exports')}
</div>'''

serp = f'''<div style="padding: 12px 14px; border-radius: 8px; background: #ffffff; color: #202124; font-family: Arial, sans-serif">
<div style="display: flex; align-items: center; gap: 8px"><span style="width: 24px; height: 24px; border-radius: 12px; background: #f1f3f4; display: flex; align-items: center; justify-content: center">{daisy(13).replace('#e8e8e8', '#b5532d')}</span>
<span style="display: flex; flex-direction: column"><span style="font-size: 12px; line-height: 15px">Halden</span><span style="font-size: 11px; line-height: 14px; color: #4d5156">halden.studio</span></span></div>
<div style="margin-top: 6px; font-size: 17px; line-height: 22px; color: #1a0dab">Halden — Hand-thrown ceramics for everyday tables</div>
<div style="margin-top: 2px; font-size: 12px; line-height: 18px; color: #4d5156">Small-batch stoneware, wheel-thrown and fired in our studio by the river. Shop bowls, mugs and plates made slowly and used daily.</div></div>'''
ptab = '<div role="tablist" style="display: flex; gap: 2px; padding: 2px; border-radius: 5px; background: #1f1f1f; font-size: 11px"><button style="padding: 0 10px; height: 22px; border-radius: 3px; background: #3a3a3a; color: #e8e8e8; font-weight: 500">Search</button><button style="padding: 0 10px; height: 22px; color: #a8a8a8">Share</button><button style="padding: 0 10px; height: 22px; color: #a8a8a8">Tab</button></div>'
preview = f'''<aside style="width: 340px; flex: none; padding: 18px 18px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px; border-left: 1px solid #3a3a3a; background: #222222">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 11px; font-weight: 500; letter-spacing: 0.04em; color: #939393">PREVIEW</span>{ptab}</div>
{serp}
<span style="margin-top: 4px; font-size: 11px; font-weight: 500; letter-spacing: 0.04em; color: #939393">IN THE BROWSER TAB</span>
<div style="display: flex; align-items: flex-end; gap: 2px; padding: 6px 8px 0; border-radius: 8px 8px 0 0; background: #dee1e6"><span style="width: 240px; height: 30px; display: inline-flex; align-items: center; gap: 8px; padding: 0 10px; box-sizing: border-box; border-radius: 8px 8px 0 0; background: #ffffff; color: #202124; font: 12px/1 Arial, sans-serif">{daisy(12).replace('#e8e8e8', '#b5532d')}<span style="flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">Halden — Hand-thrown ceramics for everyday tables</span><span style="color: #5f6368">×</span></span><span style="padding: 0 6px 8px; color: #5f6368; font: 12px Arial">+</span></div>
<div style="font-size: 11px; line-height: 15px; color: #939393">Updates as you type · put the important words first, tabs show about 25 characters</div></aside>'''

dialog = f'''<!-- SCRIM + PAGE SETTINGS -->
<div aria-hidden="true" style="position: absolute; inset: 0; background: rgba(0,0,0,0.55); z-index: 50"></div>
<section role="dialog" aria-modal="true" aria-label="Page settings" style="position: absolute; left: calc(50% - 550px); top: 130px; width: 1100px; display: flex; flex-direction: column; background: #262626; border: 1px solid #454545; border-radius: 10px; box-shadow: 0 24px 64px rgba(0,0,0,0.6); overflow: hidden; z-index: 51">
<div style="height: 52px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 12px 0 20px; border-bottom: 1px solid #3a3a3a">
<span style="font-size: 15px; font-weight: 600">Page settings</span>
<button style="height: 26px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; background: #2a2a2a; font-size: 12px; color: #e8e8e8">Home <span style="font-family: {MONO}; font-size: 11px; color: #939393">index.html</span>{icon('chev-down', 10, '#939393', 1.75)}</button>
<span style="flex: 1"></span>
<label style="width: 260px; height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 10px; box-sizing: border-box; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; color: #939393">{icon('search', 12, '#939393', 1.75)}Find a setting</label>
<button aria-label="Close" style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon('close', 14)}</button></div>
<div style="display: flex; min-height: 440px">{nav}{general}{preview}</div>
<div style="height: 54px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 20px; border-top: 1px solid #3a3a3a; background: #222222">
<span style="font-size: 11px; color: #939393">Changes apply as you type · Ctrl+Z undoes them</span><span style="flex: 1"></span>
<button style="height: 32px; padding: 0 18px; border-radius: 6px; background: #246bcb; color: #fff; font-weight: 600">Done</button></div></section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', dialog + '\n<!-- ═══════════ TOP BAR v3')
S.save('D31-PageSettings.dc.html')
print('ok')
