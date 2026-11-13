from screen import *
P['type'] = ('stroke', 'M3 4V3h10v1M8 3v10M6 13h4')
P['keyboard'] = ('stroke', 'M1.5 4.5h13v7h-13zM4 7h1M7 7h1M10 7h1M5 9.5h6')
P['cursor'] = ('stroke', 'M3 2l9 5-4 1.5L6.5 13z')
P['disk'] = ('stroke', 'M2.5 2.5h9l2 2v9h-11zM5 2.5v3.5h5V2.5M5 13.5V9.5h6v4')
P['shield'] = ('stroke', 'M8 1.5l5 2v4c0 3.2-2.2 5.6-5 7-2.8-1.4-5-3.8-5-7v-4z')
P['palette'] = ('stroke', 'M8 1.5a6.5 6.5 0 1 0 0 13c1 0 1.5-.6 1.5-1.4 0-1.2-1-1.3-1-2.3 0-.8.6-1.3 1.5-1.3h1.6a2.9 2.9 0 0 0 2.9-2.9C14.5 4 11.6 1.5 8 1.5z')
P['regex'] = ('stroke', 'M10 2.5v5M7.8 3.8l4.4 2.4M7.8 6.2l4.4-2.4M3.5 11.5h2v2h-2z')
P['plug'] = ('stroke', 'M5.5 1.5v3M10.5 1.5v3M3.5 4.5h9v2.5a4.5 4.5 0 0 1-9 0zM8 11.5v3')
P['replace'] = ('stroke', 'M3 5h7l-2-2M13 11H6l2 2')
sw = lambda on: f'<span role="switch" aria-checked="{str(on).lower()}" style="position: relative; width: 28px; height: 16px; flex: none; border-radius: 8px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {"#fff" if on else "#a8a8a8"}"></span></span>'
segm = lambda items, sel: '<div role="group" style="display: inline-grid; grid-template-columns: repeat(' + str(len(items)) + ', auto); gap: 2px; padding: 2px; background: #1f1f1f; border-radius: 4px; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px">' + ''.join(f'<button style="height: 24px; padding: 0 10px; white-space: nowrap; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #a8a8a8;"}">{t}</button>' for i, t in enumerate(items)) + '</div>'
dd = lambda v, w=180: f'<button style="width: {w}px; height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 10px; box-sizing: border-box; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; color: #e8e8e8"><span style="flex: 1; text-align: left">{v}</span>{icon("chev-down", 10, "#939393", 1.75)}</button>'
num = lambda v, u='px': f'<span style="width: 80px; height: 28px; display: flex; align-items: center; gap: 6px; padding: 0 10px; box-sizing: border-box; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a"><span style="flex: 1">{v}</span><span style="font-size: 10px; color: #939393">{u}</span></span>'
chk = lambda on, t: f'<span style="display: flex; align-items: center; gap: 8px"><span style="width: 14px; height: 14px; border-radius: 3px; display: flex; align-items: center; justify-content: center; {"background: #246bcb;" if on else "box-shadow: inset 0 0 0 1px #6b6b6b;"}">{icon("check", 10, "#fff", 2) if on else ""}</span>{t}</span>'
kb = lambda t: f'<span style="min-width: 18px; height: 20px; box-sizing: border-box; display: inline-flex; align-items: center; justify-content: center; padding: 0 6px; border-radius: 3px; background: #2a2a2a; box-shadow: inset 0 -1px 0 #454545; font-size: 11px; font-weight: 500; color: #c8c8c8">{t}</span>'
keys = lambda *ks: '<span style="display: inline-flex; gap: 3px">' + ''.join(kb(k) for k in ks) + '</span>'
def vtab(ic, t, on=False):
    return (f'<button role="tab" aria-selected="{str(on).lower()}" style="width: 100%; height: 34px; display: flex; align-items: center; gap: 10px; padding: 0 12px; box-sizing: border-box; border-radius: 6px; text-align: left; {"background: #333333; color: #e8e8e8; font-weight: 500;" if on else "color: #a8a8a8;"}">'
            f'{icon(ic, 15, "#e8e8e8" if on else "#939393")}<span style="flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{t}</span></button>')
def modal(S, title, sub, body, w, h_min, foot, top=120):
    dialog = f'''<div aria-hidden="true" style="position: absolute; inset: 0; background: rgba(0,0,0,0.55); z-index: 50"></div>
<section role="dialog" aria-modal="true" aria-label="{title}" style="position: absolute; left: calc(50% - {w // 2}px); top: {top}px; width: {w}px; display: flex; flex-direction: column; background: #262626; border: 1px solid #454545; border-radius: 10px; box-shadow: 0 16px 48px rgba(0,0,0,0.55); z-index: 51; overflow: hidden">
<div style="height: 52px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 12px 0 20px; border-bottom: 1px solid #3a3a3a">
<span style="font-size: 15px; font-weight: 600">{title}</span><span style="font-size: 12px; color: #939393">{sub}</span><span style="flex: 1"></span>
<label style="width: 260px; height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 10px; box-sizing: border-box; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; color: #939393">{icon('search', 12, '#939393')}Find a {"shortcut" if "Keyboard" in title else "setting"}</label>
<button aria-label="Close" style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon('close', 14)}</button></div>
<div style="display: flex; min-height: {h_min}px">{body}</div>
<div style="height: 54px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 20px; border-top: 1px solid #3a3a3a; background: #222222">{foot}</div></section>'''
    S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
          '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
    S.rep('<!-- ═══════════ TOP BAR v3', dialog + '\n<!-- ═══════════ TOP BAR v3')
done = '<span style="flex: 1"></span><button style="height: 32px; padding: 0 18px; border-radius: 6px; background: #246bcb; color: #fff; font-weight: 600">Done</button>'

# ═════ D-49 Preferences ═════
S = Screen('Daisy · D-49 Preferences')
nav = f'''<nav style="width: 210px; flex: none; padding: 12px 10px; box-sizing: border-box; display: flex; flex-direction: column; gap: 2px; border-right: 1px solid #3a3a3a; background: #222222">
{vtab('gear', 'General')}{vtab('palette', 'Appearance')}{vtab('cursor', 'Canvas and editing', True)}{vtab('code', 'Code')}{vtab('keyboard', 'Keyboard shortcuts')}{vtab('disk', 'Files and saving')}{vtab('plug', 'AI tools and MCP')}{vtab('shield', 'Privacy and updates')}
<div style="flex: 1"></div><div style="padding: 8px 10px; font-size: 11px; line-height: 15px; color: #939393">These are yours on this computer. Project choices are in Project settings.</div></nav>'''
row = lambda label, ctl, d='': f'<div style="display: grid; grid-template-columns: 240px minmax(0, 1fr); gap: 16px; align-items: center; padding: 8px 0"><div style="display: flex; flex-direction: column; gap: 2px"><span>{label}</span>{f"<span style=\"font-size: 11px; line-height: 15px; color: #939393\">{d}</span>" if d else ""}</div><div style="display: flex; align-items: center; gap: 10px">{ctl}</div></div>'
sec = lambda t: f'<div style="margin-top: 10px; padding-top: 12px; border-top: 1px solid #333333; font-size: 11px; font-weight: 500; letter-spacing: 0.04em; color: #939393">{t}</div>'
main = f'''<div style="flex: 1; min-width: 0; padding: 18px 26px; box-sizing: border-box; display: flex; flex-direction: column">
<div style="display: flex; align-items: center"><span style="font-size: 14px; font-weight: 600">Canvas and editing</span><span style="flex: 1"></span><button style="font-size: 11px; color: #a8a8a8">Reset this section</button></div>
<div style="font-size: 11px; font-weight: 500; letter-spacing: 0.04em; color: #939393; margin-top: 12px">SELECTING</div>
{row('A click selects', segm(['The outer element first', 'The deepest element'], 0), 'Outer first: double-click goes in. Deepest is like Direct Select.')}
{row('Show outlines on hover', sw(True) + '<span style="font-size: 11px; color: #939393">with the element’s name</span>')}
{sec('MOVING AND SNAPPING')}
{row('Nudge with arrow keys', num('1') + '<span style="font-size: 11px; color: #939393">with Shift</span>' + num('10'))}
{row('Snap distance', num('6') + '<span style="font-size: 11px; color: #939393">on screen, at any zoom</span>')}
{row('Snap to', chk(True, 'Layout grid') + chk(True, 'Other elements') + chk(True, 'Spacing scale') + chk(False, 'Whole pixels only'))}
{sec('UNITS AND NAMES')}
{row('Show sizes in', segm(['px', 'rem', 'As written'], 0), 'rem uses the project base, 16 px')}
{row('Show CSS names', sw(False) + '<span style="font-size: 11px; color: #939393">e.g. “Space inside” also shows padding</span>')}
{sec('ZOOM')}
{row('Mouse wheel', segm(['Scrolls · Ctrl zooms', 'Zooms'], 0))}
{row('Open pages at', dd('Fit width'))}
</div>'''
modal(S, 'Preferences', 'for you on this computer', nav + main, 1000, 600, '<span style="font-size: 11px; color: #939393">Changes apply at once</span>' + done, top=110)
S.save('D49-Preferences.dc.html')

# ═════ D-50 Keyboard shortcuts ═════
S = Screen('Daisy · D-50 Keyboard shortcuts')
def col(title, rows):
    return f'<div style="display: flex; flex-direction: column; gap: 2px"><div style="font-size: 11px; font-weight: 500; letter-spacing: 0.04em; color: #939393; margin-bottom: 6px">{title}</div>' + ''.join(
        f'<div style="height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 8px; border-radius: 3px; {"background: rgba(47,128,237,0.14); box-shadow: inset 0 0 0 1px #2f80ed;" if ed else ""}"><span style="flex: 1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{n}</span>{k}{f"<span style=\"font-size: 10px; color: #a9c8f7\">yours</span>" if mine else ""}</div>' for n, k, mine, ed in rows) + '</div>'
R = lambda n, *k, mine=False, ed=False: (n, keys(*k), mine, ed)
tools = col('TOOLS', [R('Select', 'V'), R('Direct Select', 'A'), R('Section', 'S'), R('Box', 'R'), R('Text', 'T'), R('Media', 'I'), R('Button', 'B'), R('Link', 'L'), R('Form', 'F'), R('Place', 'N'), R('Layout', 'G'), R('Spacing', 'P'), R('Measure', 'M'), R('Hand', 'Space')])
selc = col('SELECTION', [R('Go inside', 'Enter'), R('Go up a level', 'Esc'), R('Next element', 'Tab'), R('Select all', 'Ctrl', 'A'), R('Select same class', 'Ctrl', 'Shift', 'A', mine=True), R('Nudge', '←', '→'), R('Nudge 10', 'Shift', '→'), R('Show distances', 'Alt')]) + '<div style="height: 14px"></div>' + col('VIEW', [R('Fit width', 'Shift', '1'), R('Zoom to selection', 'Shift', '2'), R('100%', 'Shift', '0'), R('Preview', 'Ctrl', 'Enter'), R('Hide panels', 'Tab')])
edit = col('EDITING', [R('Undo', 'Ctrl', 'Z'), R('Redo', 'Ctrl', 'Shift', 'Z'), R('Duplicate', 'Ctrl', 'D'), R('Wrap in', 'Ctrl', 'G'), R('Wrap in link', 'Ctrl', 'K'), R('Copy style', 'Ctrl', 'Alt', 'C'), R('Paste style', 'Ctrl', 'Alt', 'V'), R('Rename', 'F2')])
rec = f'<span style="display: inline-flex; align-items: center; gap: 6px; height: 22px; padding: 0 8px; border-radius: 3px; background: #1b1b1b; box-shadow: inset 0 0 0 1px #2f80ed; font-size: 11px; color: #a9c8f7">Press keys…</span>'
edit += '<div style="height: 14px"></div>' + col('FILES AND PANELS', [R('Search', 'Ctrl', 'P'), ('Show code', rec, False, True), R('Versions', 'Ctrl', 'Alt', 'S'), R('Export', 'Ctrl', 'Shift', 'E'), R('This list', 'Ctrl', '/')])
conflict = f'''<div style="display: flex; align-items: center; gap: 10px; padding: 8px 10px; border-radius: 4px; background: rgba(210,153,34,0.12); font-size: 11px; color: #e3b34a">{icon('warning', 13, '#d29922', 1.5)}<span style="flex: 1; color: #c8c8c8">Editing <b style="font-weight: 600; color: #e8e8e8">Show code</b>. {keys('Ctrl', 'J')} is already Timeline.</span><button style="font-size: 11px; color: #a9c8f7">Replace</button><button style="font-size: 11px; color: #a8a8a8">Cancel</button></div>'''
body = f'''<div style="flex: 1; min-width: 0; padding: 16px 22px; box-sizing: border-box; display: flex; flex-direction: column; gap: 14px">
<div style="display: flex; align-items: center; gap: 10px">{segm(['All', 'Yours · 1', 'Most used'], 0)}<span style="flex: 1"></span><span style="font-size: 11px; color: #939393">Click a shortcut to change it</span>{segm(['Daisy', 'Like Figma', 'Like Photoshop'], 0)}</div>
{conflict}
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 28px">{tools}<div>{selc}</div><div>{edit}</div></div></div>'''
modal(S, 'Keyboard shortcuts', 'Ctrl /', body, 1180, 640, '<button style="font-size: 11px; color: #a8a8a8">Reset all to Daisy</button><button style="font-size: 11px; color: #a8a8a8">Print a cheat sheet</button>' + done, top=80)
S.save('D50-Shortcuts.dc.html')

# ═════ D-51 Find and replace ═════
S = Screen('Daisy · D-51 Find and replace')
S.remove_h1_overlay(); S.remove_parent_outline(); S.unselect_h1_row()
mark = lambda t, cur=False: f'<span style="background: {"rgba(47,128,237,0.35)" if cur else "rgba(227,179,74,0.45)"}; {"outline: 1.76px solid #2f80ed; outline-offset: 1px;" if cur else ""} border-radius: 2px">{t}</span>'
S.rep('<p style="margin: 0; font-family: \'Fraunces\', serif; font-size: 24px; font-weight: 600; line-height: 1">Halden</p>', f'<p style="margin: 0; font-family: \'Fraunces\', serif; font-size: 24px; font-weight: 600; line-height: 1">{mark("Halden", True)}</p>')
S.rep('<span style="color: #e7d9c7">Riverside Works, Unit 4</span>', '<span style="color: #e7d9c7">Riverside Works, Unit 4</span>') if '<span style="color: #e7d9c7">Riverside Works, Unit 4</span>' in S.s else None
fld = lambda v, focus=False, extra='': f'<span style="flex: 1; height: 28px; display: flex; align-items: center; gap: 6px; padding: 0 4px 0 8px; box-sizing: border-box; border-radius: 3px; background: #1f1f1f; box-shadow: inset 0 0 0 1px {"#2f80ed" if focus else "#3a3a3a"}">{v}<span style="flex: 1"></span>{extra}</span>'
opt = lambda t, on=False, title='': f'<button title="{title}" style="width: 22px; height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 3px; font-size: 11px; font-weight: 600; {"background: rgba(47,128,237,0.25); color: #a9c8f7;" if on else "color: #939393;"}">{t}</button>'
res = lambda page, ctx, kind, on=False: f'<div style="height: 30px; display: flex; align-items: center; gap: 8px; padding: 0 8px; border-radius: 3px; {"background: rgba(47,128,237,0.18);" if on else ""}"><span style="width: 56px; font-size: 11px; color: #939393">{page}</span><span style="flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{ctx}</span><span style="font-size: 10px; color: #939393">{kind}</span></div>'
hl = lambda t: t.replace('Halden', '<b style="font-weight: 600; background: rgba(227,179,74,0.35); color: #e8e8e8">Halden</b>')
panel_ = f'''<!-- FIND AND REPLACE -->
<section role="dialog" aria-label="Find and replace" style="position: absolute; left: 878px; top: 116px; width: 400px; display: flex; flex-direction: column; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); z-index: 40">
<div style="padding: 8px; display: flex; flex-direction: column; gap: 6px">
<div style="display: flex; gap: 6px">{fld('Halden', True, opt('Aa', False, 'Match case') + opt('W', True, 'Whole word') + opt(icon('regex', 12), False, 'Regular expression'))}
<span style="display: flex; align-items: center; gap: 2px; font-size: 11px; color: #c8c8c8; white-space: nowrap">1 of 9{icon('chev-up', 12, '#a8a8a8')}{icon('chev-down', 12, '#a8a8a8')}</span>{icon('close', 12, '#a8a8a8')}</div>
<div style="display: flex; gap: 6px">{fld('Halden Studio')}<button style="height: 28px; padding: 0 10px; border-radius: 3px; box-shadow: inset 0 0 0 1px #454545; font-size: 11px">Replace</button><button style="height: 28px; padding: 0 10px; border-radius: 3px; background: #246bcb; color: #fff; font-size: 11px; font-weight: 500">Replace all</button></div>
<div style="display: flex; align-items: center; gap: 6px; font-size: 11px">{segm(['This page', 'All pages', 'Selection'], 1)}<span style="flex: 1"></span>{dd('Text and alt text', 150)}</div></div>
<div style="padding: 4px 8px 8px; border-top: 1px solid #333333">
<div style="display: flex; align-items: center; padding: 6px 8px 4px; font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393">9 MATCHES · 4 PAGES<span style="flex: 1"></span><span style="font-weight: 400; letter-spacing: 0">Enter next · Ctrl Enter replace all</span></div>
{res('Home', hl('Halden'), 'wordmark', True)}{res('Home', hl('© 2026 Halden Studio'), 'footer')}{res('Shop', hl('Halden bowls are dishwasher safe'), 'text')}{res('Shop', hl('alt: “Halden mug on linen”'), 'alt text')}{res('Journal', hl('Inside the Halden kiln'), 'h1')}
<div style="padding: 4px 8px; font-size: 11px; color: #939393">+ 4 more · <span style="color: #e3b34a">1 already reads “Halden Studio”, skipped</span></div></div>
<div style="padding: 8px 10px; display: flex; gap: 8px; border-top: 1px solid #333333; font-size: 11px; color: #939393">Also search: <button style="font-size: 11px; color: #a9c8f7">Links</button><button style="font-size: 11px; color: #a9c8f7">Classes</button><button style="font-size: 11px; color: #a9c8f7">Colours</button><button style="font-size: 11px; color: #a9c8f7">Code</button></div></section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', panel_ + '\n<!-- ═══════════ TOP BAR v3')
set_tree(S, [(8, 'open', 't-section', 'Header', 'header', False, (), ''), (20, None, 't-para', 'Wordmark “Halden”', 'p', True, (14,), ''), (20, 'closed', 't-row', 'Nav links', 'nav', False, (14,), ''), (20, None, 't-button', 'Book a visit', 'a', False, (14,), ''),
             (8, 'closed', 't-section', 'Hero', 'section', False, (), ''), (8, 'closed', 't-section', 'This season', 'section', False, (), ''), (8, 'closed', 't-section', 'Footer', 'footer', False, (), '')])
S.props(panel(header('t-para', 'Wordmark “Halden”', 'Text', 'p') + group('Typography', f('<span style="flex: 1">Fraunces</span>') + pair(f('<span style="flex: 1">Semibold</span>'), f('<span style="flex: 1">24</span><span style="font-size: 10px; color: #939393">px</span>')))
              + more([mp('Size', 'Fit'), mp('Spacing'), mp('Link', 'none'), mp('Accessibility')])))
S.status(['Page', 'Section · Header', 'Text · Wordmark'], 'Find and replace · Ctrl H · replacing is one undo step', 'x 74 &#160;y 32')
S.save('D51-FindReplace.dc.html')
print('ok')
