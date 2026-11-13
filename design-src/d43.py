from screen import *
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
S = Screen('Daisy · D-43 Section tool and Direct Select')
S.remove_h1_overlay(); S.remove_parent_outline(); S.unselect_h1_row()
set_tool(S, 'Section (S)')
POP = 'background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5);'
S.rep('transform: scale(0.85); transform-origin: 0 0;', 'transform: scale(0.85) translateY(-430px); transform-origin: 0 0;')
S.rep('right: 54px; top: 800px;', 'right: 54px; top: 1000px;')

# ── canvas: a new section being drawn between Hero and This season ──
ghost = '''<!-- NEW SECTION being drawn (Section tool) -->
<div aria-hidden="true" style="position: relative; height: 240px; background: repeating-linear-gradient(135deg, rgba(47,128,237,0.06) 0 12px, rgba(47,128,237,0.12) 12px 24px); border-top: 2.35px solid #2f80ed; border-bottom: 2.35px solid #2f80ed">
<span style="position: absolute; left: 64px; right: 64px; top: 0; bottom: 0; border-left: 1.18px dashed rgba(47,128,237,0.6); border-right: 1.18px dashed rgba(47,128,237,0.6)"></span>
<span style="position: absolute; left: 0; top: -1px; height: 21px; padding: 0 6px; display: flex; align-items: center; gap: 6px; background: #246bcb; color: #fff; font: 500 13px/1 'Inter', sans-serif; white-space: nowrap">+ Section · section<span style="opacity: 0.75">after Hero</span></span>
<span style="position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); display: flex; flex-direction: column; align-items: center; gap: 6px; font: 500 15px/1.3 'Inter', sans-serif; color: #1f5fb5">Release to add the section<span style="font-size: 13px; color: #4a6fa5">Content width 1312 · from the Desktop grid</span></span>
<span style="position: absolute; left: calc(50% - 46px); bottom: -15px; height: 26px; padding: 0 10px; display: flex; align-items: center; border-radius: 13px; background: #1f1f1f; color: #e8e8e8; font: 500 13px/1 'Inter', sans-serif; white-space: nowrap">Min H 240</span>
<svg style="position: absolute; left: calc(50% + 70px); bottom: -14px" width="26" height="26" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v18M7 8l5-5 5 5M7 16l5 5 5-5" fill="none" stroke="#1d1a16" stroke-width="2.4"/><path d="M12 3v18M7 8l5-5 5 5M7 16l5 5 5-5" fill="none" stroke="#fff" stroke-width="0.9"/></svg>
</div>
'''
S.rep('<!-- This season -->\n<div style="padding: 96px 64px; background: #e7d9c7">', ghost + '<!-- This season -->\n<div style="padding: 96px 64px; background: #e7d9c7">')

# ── variants flyout? Kind lives in the options bar ──
lab = lambda t: f'<span style="font-size: 11px; color: #939393; padding: 0 4px 0 8px; white-space: nowrap">{t}</span>'
sb = lambda t, on=False: f'<button aria-pressed="{str(on).lower()}" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; white-space: nowrap; {"background: #333333; color: #e8e8e8; font-weight: 500;" if on else "color: #939393;"}">{t}</button>'
tog = lambda ic, t, on: f'<button aria-pressed="{str(on).lower()}" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; white-space: nowrap; {"background: rgba(47,128,237,0.18); color: #a9c8f7;" if on else "color: #a8a8a8;"}">{icon(ic, 13)}{t}</button>'
opts = (cap(lab('Kind') + '<span style="padding: 0 6px; font-weight: 500">Section</span><span style="font-family: ' + MONO + '; font-size: 10px; color: #939393; padding-right: 4px">section</span>' + icon('chev-down', 10, '#939393', 1.75), 'padding: 0 6px 0 0')
        + cap(lab('Content') + sb('Contained', True) + sb('Full width'))
        + cap(tog('keep', 'Keep tool', False))
        + '<span style="font-size: 11px; color: #939393; white-space: nowrap; padding-left: 4px">Click between sections to add one · drag down to set its height</span>')
options_left(S, opts)

# Kind menu shown open under the capsule
mi = lambda t, tag, d, on=False: f'<div style="height: 34px; display: flex; align-items: center; gap: 8px; padding: 0 8px; border-radius: 3px; {"background: #333333;" if on else ""}"><span style="width: 12px">{icon("check", 12) if on else ""}</span><span style="flex: 1; display: flex; flex-direction: column"><span>{t}</span><span style="font-size: 10px; line-height: 13px; color: #939393">{d}</span></span><span style="font-family: {MONO}; font-size: 10px; color: #939393">{tag}</span></div>'
kind = f'''<div role="menu" aria-label="Section kind" style="position: absolute; left: 52px; top: 74px; width: 310px; padding: 4px; box-sizing: border-box; {POP} border-radius: 4px; z-index: 40">
{mi('Section', 'section', 'A part of the page with its own heading', True)}{mi('Header', 'header', 'Top of the page: logo, navigation')}{mi('Navigation', 'nav', 'A set of links')}{mi('Main', 'main', 'The main content, once per page')}
{mi('Article', 'article', 'Stands on its own: a post, a product')}{mi('Sidebar', 'aside', 'Related, beside the main content')}{mi('Footer', 'footer', 'Bottom of the page')}
<div style="padding: 4px 8px; font-size: 10px; line-height: 14px; color: #939393">Screen readers use the kind to move around the page.</div></div>'''

# ── layers ──
rows = [(8, 'closed', 't-section', 'Header', 'header', False, (), ''), (8, 'closed', 't-section', 'Hero', 'section', False, (), ''),
        (8, None, 't-section', 'Section 1', 'section', True, (), '<span style="margin-left: 6px; font-size: 10px; color: #a9c8f7">adding</span>'),
        (8, 'closed', 't-section', 'This season', 'section', False, (), ''), (8, 'closed', 't-section', 'Footer', 'footer', False, (), '')]
set_tree(S, rows)

# ── properties: next section ──
small = lambda t: f'<span style="font-size: 11px; color: #939393">{t}</span>'
row2 = lambda l, c: f'<div style="display: grid; grid-template-columns: 84px minmax(0, 1fr); gap: 8px; align-items: center"><span style="font-size: 11px; color: #a8a8a8">{l}</span>{c}</div>'
dd = lambda v, sub='': f('<span style="flex: 1">' + v + '</span>' + (f'<span style="font-family: {MONO}; font-size: 10px; color: #939393">{sub}</span>' if sub else '') + icon('chev-down', 10, '#939393', 1.75))
tile = lambda c, n, on=False: f'<button title="{n}" style="height: 34px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3px; border-radius: 4px; background: #2a2a2a; {"box-shadow: inset 0 0 0 1px #2f80ed;" if on else ""}"><span style="width: 22px; height: 12px; border-radius: 2px; background: {c}; box-shadow: inset 0 0 0 1px rgba(0,0,0,0.15)"></span><span style="font-size: 9px; color: #a8a8a8">{n}</span></button>'
hdr = f'''<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{icon('t-section', 16, '#a9c8f7')}<span style="flex: 1; font-weight: 500">Next section</span><button style="height: 22px; padding: 0 6px; border-radius: 3px; font-size: 11px; color: #a8a8a8">Reset</button></div>
<div style="padding-left: 24px; font-size: 11px; color: #939393">After Hero · before This season</div></div>'''
gen = (row2('Name', f('<span style="flex: 1">Our story</span>', 'box-shadow: inset 0 0 0 1px #2f80ed'))
       + row2('Link id', f(f'<span style="flex: 1; font-family: {MONO}; font-size: 11px">#our-story</span><span style="font-size: 10px; color: #939393">from name</span>'))
       + row2('Min height', f('<span style="flex: 1">240</span><span style="font-size: 10px; color: #939393">px</span>')))
bg = ('<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 4px">' + tile('transparent', 'none') + tile('#f6f1ea', 'sand', True) + tile('#e7d9c7', 'clay') + tile('#1d1a16', 'ink') + tile('#5f6b4e', 'moss') + '</div>'
      + small('Sections alternate sand and clay; this one keeps sand.'))
inside = (row2('Width', dd('Contained', '1312')) + row2('Padding', dd('Section · 96 / 64', 'space-9')) + row2('Arrange', dd('Stack')))
S.props(panel(hdr + group('Section', gen) + group('Background', bg) + group('Inside', inside)
              + more([mp('Accessibility', 'Heading needed'), mp('Visibility', 'All sizes'), mp('Effects')])))

# ── INSET: Direct Select ──
card = f'''<div style="position: relative; width: 170px; padding: 8px; box-sizing: border-box; border-radius: 8px; background: #ffffff; outline: 1px dashed rgba(47,128,237,0.45); outline-offset: 2px">
<div style="height: 90px; border-radius: 5px; background: #d8cbb8"></div><div style="margin-top: 8px; font: 14px 'Fraunces', serif; color: #1d1a16">Tide bowl</div>
<div style="position: relative; width: max-content; font-size: 12px; color: #5f6b4e; outline: 1.5px solid #2f80ed; outline-offset: 2px">€38
<svg style="position: absolute; left: 22px; top: 6px" width="16" height="20" viewBox="0 0 16 20" aria-hidden="true"><path d="M2 1v15l4-4 3 6 2-1-3-6h5z" fill="none" stroke="#1d1a16" stroke-width="1.6"/><path d="M2 1v15l4-4 3 6 2-1-3-6h5z" fill="#fff"/></svg></div>
<span style="position: absolute; left: -4px; top: -24px; height: 18px; padding: 0 6px; display: flex; align-items: center; background: #246bcb; color: #fff; font-size: 10px; white-space: nowrap; border-radius: 2px">Text · p</span></div>'''
cmp_ = lambda t, d, c: f'<div style="display: flex; gap: 8px; font-size: 11px; line-height: 16px"><span style="width: 92px; flex: none; color: {c}; font-weight: 500">{t}</span><span style="color: #a8a8a8">{d}</span></div>'
inset = f'''<!-- INSET: Direct Select -->
<div style="position: absolute; left: 330px; bottom: 44px; width: 640px; display: flex; flex-direction: column; gap: 8px; z-index: 35">
<span style="width: max-content; height: 20px; display: flex; align-items: center; padding: 0 8px; border-radius: 3px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; color: #a8a8a8">Inset · Direct Select (A, or hold Ctrl) clicking a price</span>
<div style="display: flex; gap: 20px; align-items: center; padding: 26px 16px 14px; {POP}">
<div style="padding: 14px; border-radius: 6px; background: #e7d9c7">{card}</div>
<div style="flex: 1; display: flex; flex-direction: column; gap: 8px">
<span style="font-weight: 600">Picks the deepest element under the pointer</span>
{cmp_('Select (V)', 'First click picks Card grid; double-click goes inside, one level at a time.', '#c8c8c8')}
{cmp_('Direct Select (A)', 'Picks “€38” at once, through Card grid and Card 1. The scope moves to Card 1, so the next click picks its neighbours.', '#a9c8f7')}
<div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #939393; font-family: {MONO}">This season › Card grid › Card 1 › <span style="color: #e8e8e8">p</span></div>
<span style="font-size: 11px; color: #939393">Alt + click with Direct Select picks the parent instead.</span></div></div></div>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', kind + '\n' + inset + '\n<!-- ═══════════ TOP BAR v3')
S.status(['Page', 'Section · Our story'], 'Drag to set the height · Shift snaps to the spacing scale · Esc cancels', 'x 720 &#160;y 820')
S.save('D43-Section-DirectSelect.dc.html')
print('ok')
