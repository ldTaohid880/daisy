from screen import *
_src = open('/home/claude/ds/layoutadv.py').read(); LA = {}; exec(_src[:_src.index('# ═════ A · ROW')], LA); L = LA
P['bolt'] = ('stroke', 'M9 1.5L3.5 9H8l-1 5.5L12.5 7H8z')
P['menu3'] = ('stroke', 'M2.5 4.5h11M2.5 8h11M2.5 11.5h11')
P['tabs'] = ('stroke', 'M1.5 5.5h13v8h-13zM1.5 5.5V3h4v2.5M5.5 3h4v2.5')
P['accordion'] = ('stroke', 'M2 3h12v3H2zM2 7.5h12v3H2zM2 12h12v1.5H2z')
P['dialog'] = ('stroke', 'M2 2.5h12v11H2zM4.5 5.5h7M4.5 8h5M9.5 11h2.5')
P['slider'] = ('stroke', 'M1.5 4h13v8h-13zM4 14h1M7.5 14h1M11 14h1')
P['toggle'] = ('stroke', 'M4.5 4.5h7a3.5 3.5 0 0 1 0 7h-7a3.5 3.5 0 0 1 0-7zM11 6.5a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3z')
P['crosshair'] = ('stroke', 'M8 1.5v3M8 11.5v3M1.5 8h3M11.5 8h3M8 6a2 2 0 1 1 0 4 2 2 0 0 1 0-4z')
S = Screen('Daisy · D-56 Interactive parts: mobile menu')
S.remove_h1_overlay(); S.remove_parent_outline(); S.unselect_h1_row()
POP = 'background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5);'

# ── canvas: Mobile 390 shown twice, Closed and Open, with the interaction drawn between ──
def phone(open_):
    burger = f'''<span style="position: relative; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 20px; {"background: #1d1a16;" if open_ else "background: transparent;"}">
<svg width="20" height="20" viewBox="0 0 20 20"><path d="{"M5 5l10 10M15 5L5 15" if open_ else "M3 6h14M3 10h14M3 14h14"}" stroke="{"#f6f1ea" if open_ else "#1d1a16"}" stroke-width="2" stroke-linecap="round"/></svg>
{"" if open_ else '<span aria-hidden="true" style="position: absolute; inset: -4px; border: 1.5px solid #2f80ed"><span style="position: absolute; right: -1.5px; top: calc(100% + 3px); height: 18px; padding: 0 5px; display: flex; align-items: center; gap: 4px; background: #246bcb; color: #fff; font: 500 11px/1 Inter, sans-serif; white-space: nowrap">Menu button<span style="opacity: 0.8">⚡</span></span>' + ''.join(f'<span style="position: absolute; {p}; width: 7px; height: 7px; box-sizing: border-box; background: #fff; border: 1px solid #2f80ed"></span>' for p in ["left: -4px; top: -4px", "right: -4px; top: -4px", "left: -4px; bottom: -4px", "right: -4px; bottom: -4px"]) + '</span>'}</span>'''
    menu = '' if not open_ else '''<div style="position: absolute; left: 0; right: 0; top: 64px; bottom: 0; padding: 24px 20px; display: flex; flex-direction: column; gap: 4px; background: #1d1a16; color: #f6f1ea; outline: 1.5px dashed rgba(47,128,237,0.8); outline-offset: -1.5px">
<span style="position: absolute; right: 8px; top: 8px; height: 18px; padding: 0 6px; display: flex; align-items: center; background: rgba(47,128,237,0.25); color: #d6e6fb; font: 500 11px/1 Inter, sans-serif">Mobile menu · target</span>''' + ''.join(f'<span style="padding: 12px 0; border-bottom: 1px solid rgba(246,241,234,0.15); font: 600 26px/1.1 Fraunces, serif">{t}</span>' for t in ['Work', 'Shop', 'Journal', 'Visit']) + '''
<span style="margin-top: 20px; align-self: flex-start; padding: 12px 22px; border-radius: 999px; background: #b5532d; font-size: 15px; font-weight: 500">Book a visit</span></div>'''
    hero = '' if open_ else '''<div style="padding: 28px 20px; display: flex; flex-direction: column; gap: 14px"><span style="font-size: 11px; letter-spacing: 0.08em; color: #5f6b4e">SMALL-BATCH STONEWARE</span>
<span style="font: 600 36px/1.05 Fraunces, serif">Hand-thrown ceramics for everyday tables</span><span style="font-size: 15px; line-height: 1.55; color: #4a443c">Each piece is wheel-thrown, glazed and fired in our studio by the river.</span>
<span style="align-self: flex-start; padding: 12px 22px; border-radius: 999px; background: #b5532d; color: #fff; font-size: 15px">Shop the collection</span><span style="height: 220px; border-radius: 10px; background: #e6dccd"></span></div>'''
    return f'''<div style="position: relative; width: 390px; height: 820px; overflow: hidden; background: #f6f1ea; color: #1d1a16; font-family: Inter, sans-serif; outline: 1px solid #3c3c3c">
<div style="height: 64px; display: flex; align-items: center; justify-content: space-between; padding: 0 16px 0 20px; {"background: #1d1a16; color: #f6f1ea;" if open_ else ""}"><span style="font: 600 22px/1 Fraunces, serif">Halden</span>{burger}</div>{menu}{hero}</div>'''
lab = lambda t, on=False: f'<span style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: {"#a9c8f7" if on else "#939393"}">{t}</span>'
canvas = f'''<span style="position: absolute; left: 60px; top: 13px; display: flex; align-items: center; gap: 6px; font-size: 11px; line-height: 11px; color: #939393">{icon('phone', 12, '#d29922')}Mobile · 390</span>
<div style="position: absolute; left: 60px; top: 32px; display: flex; gap: 150px; align-items: flex-start">
<div style="display: flex; flex-direction: column; gap: 6px">{lab("Closed · as the page loads")}{phone(False)}</div>
<div style="display: flex; flex-direction: column; gap: 6px">{lab(icon("bolt", 11, "#a9c8f7") + "Open · after a click", True)}{phone(True)}</div></div>
<svg style="position: absolute; left: 420px; top: 60px" width="200" height="80" aria-hidden="true"><path d="M6 34 C 60 -6, 140 -6, 186 34" fill="none" stroke="#2f80ed" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M180 26l7 8-10 3" fill="none" stroke="#2f80ed" stroke-width="1.5"/></svg>
<span style="position: absolute; left: 468px; top: 52px; height: 22px; padding: 0 8px; display: flex; align-items: center; gap: 6px; border-radius: 11px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #2f80ed; color: #e8e8e8; font-size: 11px; white-space: nowrap">{icon("bolt", 11, "#a9c8f7")}Click → open / close</span>
'''
S.cut('<span style="position: absolute; left: 46px; top: 13px;', '<!-- vertical scroll indicator', canvas)

# options bar: Mobile size active, interaction chip
S.rep('<span style="font-weight: 500">Desktop</span>', '<span style="font-weight: 500">Mobile</span>')
S.rep('<span style="font-size: 11px; color: #a8a8a8; font-variant-numeric: tabular-nums">1440</span>', '<span style="font-size: 11px; color: #a8a8a8; font-variant-numeric: tabular-nums">390</span>')
S.options('342', '12', '40', 'Fixed', '40', 'Fixed')
S.rep('index.html @ 85%', 'index.html @ 100%')

# layers
rows = [(8, 'open', 't-section', 'Site header', 'header', False, (), ''), (20, None, 't-para', 'Wordmark “Halden”', 'p', False, (14,), ''),
        (20, 'closed', 't-row', 'Nav links', 'nav', False, (14,), icon('eye-off', 11, '#d29922', 1.25, 'Hidden at Mobile')),
        (20, None, 't-button', 'Menu button', 'button', True, (14,), '<span style="margin-left: 6px">' + icon('bolt', 11, '#a9c8f7', 1.5) + '</span>'),
        (20, 'open', 'menu3', 'Mobile menu', 'nav', False, (14,), '<span style="margin-left: 6px; font-size: 10px; color: #939393">closed</span>'),
        (32, None, 't-link', 'Work', 'a', False, (14, 26), ''), (32, None, 't-link', 'Shop', 'a', False, (14, 26), ''), (32, None, 't-link', 'Journal', 'a', False, (14, 26), ''), (32, None, 't-link', 'Visit', 'a', False, (14, 26), ''),
        (8, 'closed', 't-section', 'Hero', 'section', False, (), ''), (8, 'closed', 't-section', 'This season', 'section', False, (), ''), (8, 'closed', 't-section', 'Site footer', 'footer', False, (), '')]
set_tree(S, rows)

# properties: Interaction group
sm = lambda t, c='#939393': f'<span style="font-size: 11px; color: {c}">{t}</span>'
row2 = lambda l, c: f'<div style="display: grid; grid-template-columns: 64px minmax(0, 1fr); gap: 8px; align-items: center"><span style="font-size: 11px; color: #a8a8a8">{l}</span>{c}</div>'
dd = lambda v, extra='': f(f'<span style="flex: 1">{v}</span>{extra}' + icon('chev-down', 10, '#939393', 1.5))
chk = lambda on, t: f'<div style="height: 22px; display: flex; align-items: center; gap: 8px; font-size: 11px"><span style="width: 13px; height: 13px; border-radius: 3px; display: flex; align-items: center; justify-content: center; {"background: #246bcb;" if on else "box-shadow: inset 0 0 0 1px #6b6b6b;"}">{icon("check", 9, "#fff", 2) if on else ""}</span>{t}</div>'
inter = (row2('When', dd('Clicked or tapped')) + row2('Do', dd('Open and close')) + row2('Target', f(icon('menu3', 12, '#a9c8f7') + '<span style="flex: 1">Mobile menu</span>' + icon('crosshair', 12, '#939393'), 'box-shadow: inset 0 0 0 1px #2f80ed'))
         + row2('Starts', '<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #262626; border-radius: 4px; font-size: 11px"><span style="height: 20px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: #3a3a3a">Closed</span><span style="height: 20px; display: flex; align-items: center; justify-content: center; color: #939393">Open</span></div>')
         + row2('Motion', dd('Slide down · 240 ms', '<span style="font-size: 10px; color: #939393; margin-right: 4px">Timeline</span>'))
         + chk(True, 'Close with Esc and when a link is chosen') + chk(True, 'Keep focus inside while open') + chk(True, 'Stop the page scrolling behind it')
         + f'<div style="display: flex; align-items: center; gap: 6px; padding: 6px 8px; border-radius: 4px; background: #262626; font-size: 10px; line-height: 14px; color: #a8a8a8">{icon("check", 10, "#3fb950", 2)}Screen readers hear “Menu, collapsed”. aria-expanded is set for you.</div>')
view = (sm('Show on the canvas') + '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #262626; border-radius: 4px; font-size: 11px"><span style="height: 20px; display: flex; align-items: center; justify-content: center; color: #939393">Closed</span><span style="height: 20px; display: flex; align-items: center; justify-content: center; color: #939393">Open</span><span style="height: 20px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: #3a3a3a">Both</span></div>'
        + sm('Click Open on the canvas to edit the menu as it looks when open.'))
hdr = f'''<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{icon('t-button', 16, '#a8a8a8')}<span style="flex: 1; font-weight: 500">Menu button</span><button style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 6px; color: #a8a8a8">Normal{icon('chev-down', 10, 'currentColor', 1.5)}</button></div>
<div style="padding-left: 24px; font-size: 11px; color: #a8a8a8">Button · <span style="font-family: {MONO}; color: #939393">button</span> · shown at Tablet and Mobile</div></div>'''
S.props(panel(hdr + group('Interaction', inter) + group('Preview', view)
              + more([mp('Accessibility', 'Menu'), mp('Size', '40 × 40'), mp('Fill', 'none · ink when open'), mp('Visibility', 'Tablet, Mobile')])))

# INSET: interactive parts in Elements
part = lambda ic, n, d, tag: f'<div style="height: 40px; display: grid; grid-template-columns: 30px minmax(0, 1fr) auto; align-items: center; gap: 10px; padding: 0 10px; border-radius: 4px; background: #2a2a2a"><span style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 6px; background: #333333">{icon(ic, 15, "#e8e8e8")}</span><span style="display: flex; flex-direction: column; min-width: 0"><span style="font-weight: 500">{n}</span><span style="font-size: 10px; color: #939393; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{d}</span></span><span style="font-family: {MONO}; font-size: 10px; color: #939393">{tag}</span></div>'
inset = f'''<!-- INSET: Elements › Interactive -->
<div style="position: absolute; left: 1306px; top: 130px; width: 306px; display: flex; flex-direction: column; gap: 8px; z-index: 35">
<span style="width: max-content; height: 20px; display: flex; align-items: center; padding: 0 8px; border-radius: 3px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; color: #a8a8a8">Inset · Elements › Interactive</span>
<div style="padding: 10px; display: flex; flex-direction: column; gap: 4px; {POP}">
{part('menu3', 'Menu for phones', 'Button + panel, opens and closes', 'button nav')}{part('tabs', 'Tabs', 'One panel at a time, arrow keys move', 'tablist')}{part('accordion', 'Accordion', 'Questions that open in place', 'details')}
{part('dialog', 'Pop-up', 'Opens over the page, Esc closes', 'dialog')}{part('slider', 'Image slider', 'Swipe and arrows, pauses on hover', 'section')}{part('toggle', 'Show and hide', 'Any button shows or hides any part', 'button')}
<div style="padding: 4px 4px 0; font-size: 10px; line-height: 14px; color: #939393">Built on native HTML where it exists; a few lines of script otherwise. Keyboard and screen-reader rules are included. Any element can get its own interaction in Properties.</div></div></div>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', inset + '\n<!-- ═══════════ TOP BAR v3')
S.status(['Page', 'Shared · Site header', 'Button · Menu button'], 'Alt-click the button on the canvas to try the interaction · Preview runs it for real', 'x 342 &#160;y 12')
S.rep('<span style="width: 28px">85%</span>', '<span style="width: 28px">100%</span>')
S.save('D56-Interactive.dc.html')
print('ok')
