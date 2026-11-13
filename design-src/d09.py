from screen import *

S = Screen('Daisy · D-09 Invalid drop')
S.remove_h1_overlay()
S.remove_parent_outline()

RED, REDF = '#f85149', '#c9302c'
BTN = ('<a href="#shop" style="background: #b5532d; color: #ffffff; border-radius: 999px; padding: 12px 24px; font-size: 16px; font-weight: 500; line-height: 20px">Shop the collection</a>'
       '<a href="#process" style="font-size: 16px; font-weight: 500; color: #1d1a16">Our process →</a>')

# original row dimmed
S.rep('<div style="display: flex; align-items: center; gap: 24px">\n<a href="#shop" style="background: #b5532d;',
      '<div style="display: flex; align-items: center; gap: 24px; opacity: 0.3">\n<a href="#shop" style="background: #b5532d;')

# red overlay on the h1 (in its wrapper), red insertion line between its lines
S.rep('<h1 style="margin: 0; font-family: \'Fraunces\', serif; font-size: 64px; line-height: 1.05; font-weight: 600; color: #1d1a16">Hand-thrown ceramics for everyday tables</h1>',
      '<h1 style="margin: 0; font-family: \'Fraunces\', serif; font-size: 64px; line-height: 1.05; font-weight: 600; color: #1d1a16">Hand-thrown ceramics for everyday tables</h1>'
      + overlay_box(-1, -1, 562, 204, 'Heading · h1', REDF, f'1.18px solid {RED}', False)
      + f'<div aria-hidden="true" style="position: absolute; left: 0; width: 560px; top: 66px; height: 2.35px; background: {RED}"><span style="position: absolute; left: -1.2px; top: -2.35px; width: 2.35px; height: 7px; background: {RED}"></span><span style="position: absolute; right: -1.2px; top: -2.35px; width: 2.35px; height: 7px; background: {RED}"></span></div>')

# ghost + pointer + reason pill (Hero text coordinates)
S.rep('<!-- position + size capsule -->', '<!-- position + size capsule -->')  # sanity
ghost = f'''<!-- ghost (60%) on a solid card -->
<div aria-hidden="true" style="position: absolute; left: 236px; top: 128px; display: flex; align-items: center; gap: 24px; padding: 8px 12px; background: #f6f1ea; box-shadow: 0 0 0 1.18px rgba(248,81,73,0.6), 0 10px 26px rgba(29,26,22,0.25); border-radius: 6px; pointer-events: none; z-index: 3"><div style="display: flex; align-items: center; gap: 24px; opacity: 0.6">{BTN}</div></div>
<svg aria-hidden="true" width="26" height="26" viewBox="0 0 16 16" style="position: absolute; left: 312px; top: 140px; overflow: visible; z-index: 5"><circle cx="8" cy="8" r="6.2" fill="#ffffff" stroke="{REDF}" stroke-width="1.8"></circle><path d="M3.7 12.3l8.6-8.6" stroke="{REDF}" stroke-width="1.8"></path></svg>
<span aria-hidden="true" style="position: absolute; left: 350px; top: 96px; height: 26px; padding: 0 10px; display: flex; align-items: center; gap: 6px; border-radius: 13px; background: {REDF}; color: #ffffff; font: 500 14px/1 'Inter', sans-serif; white-space: nowrap; box-shadow: 0 4px 12px rgba(0,0,0,0.2); z-index: 5">Text can't contain boxes</span>
'''
S.rep('<p style="margin: 0; font-size: 13px; line-height: 20px; text-transform: uppercase;', ghost + '<p style="margin: 0; font-size: 13px; line-height: 20px; text-transform: uppercase;')
assert contrast('#ffffff', REDF) >= 4.5

# Layers: h1 row invalid (red outline), Hero buttons selected
S.unselect_h1_row()
S.rep('<span style="flex: 1; overflow: hidden; white-space: nowrap; text-overflow: ellipsis">Hero title</span><span style="font-size: 11px; color: #939393">h1</span>',
      '<span style="flex: 1; overflow: hidden; white-space: nowrap; text-overflow: ellipsis">Hero title</span><span style="font-size: 11px; color: #ff7b72">can’t drop here</span>')
s = S.s
i = s.index('>Hero title</span>')
j = s.rindex('<div role="treeitem" style="', 0, i)
S.s = s[:j] + '<div role="treeitem" style="box-shadow: inset 0 0 0 1px #f85149; ' + s[j + len('<div role="treeitem" style="'):]
s = S.s
k = s.index('<span style="flex: 1">Hero buttons</span>')
j = s.rindex('<div role="treeitem" aria-expanded="false" style="', 0, k)
S.s = s[:j] + '<div role="treeitem" aria-expanded="false" aria-selected="true" style="background-color: rgba(47,128,237,0.18); ' + s[j + len('<div role="treeitem" aria-expanded="false" style="'):]
S.rep('<span style="flex: 1">Hero buttons</span>', '<span style="flex: 1; color: #e8e8e8">Hero buttons</span>')

S.options('0', '380', '298', 'Fit', '44', 'Fit')
S.props(panel(header('t-row', 'Hero buttons', 'Box', 'div')
              + group('Size', pair(f('<span style="font-size: 11px; color: #939393; padding-left: 11px">W</span><span style="flex: 1; color: #939393">298</span>' + tagc('Fit')),
                                   f('<span style="font-size: 11px; color: #939393; padding-left: 11px">H</span><span style="flex: 1; color: #939393">44</span>' + tagc('Fit'))))
              + group('Layout', seg([icon('t-stack', 12) + 'Stack', icon('t-row', 12) + 'Row', icon('t-grid', 12) + 'Grid'], 1)
                      + f(DOT + '<span style="font-size: 11px; color: #939393">Gap</span><span style="flex: 1">24</span><span style="font-size: 10px; color: #939393">px</span>'))
              + more([mp('Placement', 'In flow'), mp('Spacing', '0'), mp('Fill', 'none'), mp('Border', 'none'), mp('Effects'), mp('Transform'), mp('Visibility', 'All sizes'), mp('Transition &amp; Animation'), mp('Accessibility'), mp('Attributes &amp; Custom CSS')])))
S.rep('<span style="flex: 1; text-align: center; color: #939393; white-space: nowrap">Drag a handle to resize · Shift keeps proportions</span>',
      '<span role="status" style="flex: 1; display: flex; align-items: center; justify-content: center; gap: 6px; color: #ff7b72; white-space: nowrap">' + icon('warning', 12, '#ff7b72', 1.25) + 'Text can’t contain boxes · drop above or below the heading instead · Esc cancels</span>')
s = S.s
a = s.index('<nav aria-label="Selection path"'); b = s.index('</nav>', a) + 6
S.s = s[:a] + '<nav aria-label="Selection path" style="flex: 1; display: flex; align-items: center; gap: 6px; color: #a8a8a8; white-space: nowrap"><button>Page</button><span aria-hidden="true">›</span><button>Section · Hero</button><span aria-hidden="true">›</span><button>Box · Hero grid</button><span aria-hidden="true">›</span><button>Box · Hero text</button><span aria-hidden="true">›</span><button aria-current="true" style="color: #e8e8e8">Box · Hero buttons</button></nav>' + s[b:]
S.rep('x 612 &#160;y 288', 'x 384 &#160;y 302')
S.save('D09-InvalidDrop.dc.html')
print('ok')
