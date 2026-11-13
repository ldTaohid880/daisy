import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

H_ACT = int(sys.argv[1]) if len(sys.argv) > 1 else 134  # measured h1 height at 654 wide
s = open('/home/claude/daisy/project/Main.dc.html', encoding='utf-8').read()


def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:90], s.count(old))
    s = s.replace(old, new)


rep('<title>Daisy · D-04 Editor, heading selected</title>', '<title>Daisy · D-07 Resize limited by layout</title>')

# h1 is as wide as the column allows (654); its overlay grows with it
rep('<div style="position: relative; width: 560px">\n<h1', '<div id="h1wrap" style="position: relative; width: 654px">\n<h1')
# right-middle handle is the one being dragged
rep('<span style="position: absolute; right: -5.6px; top: calc(50% - 4.7px); width: 9.4px; height: 9.4px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>',
    '<span style="position: absolute; right: -5.6px; top: calc(50% - 4.7px); width: 9.4px; height: 9.4px; box-sizing: border-box; background: #2f80ed; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>'
    # requested width beyond the limit: dashed neutral extension to the pointer (+106 = 760)
    '<span style="position: absolute; left: 100%; top: -1px; bottom: -1px; width: 106px; box-sizing: border-box; border: 1.18px dashed #a8a8a8; border-left: 0; background: repeating-linear-gradient(135deg, rgba(168,168,168,0.14) 0 4px, transparent 4px 9px)"></span>'
    '<span style="position: absolute; left: calc(100% + 26px); top: -28px; height: 22px; padding: 0 7px; display: flex; align-items: center; border-radius: 11px; background: #3a3a3a; color: #e8e8e8; font: 500 12px/1 \'Inter\', sans-serif; white-space: nowrap">wants 760</span>'
    # size label: neutral pill = limited
    f'<span style="position: absolute; left: calc(50% - 118px); top: calc(100% + 9px); height: 21px; padding: 0 9px; display: flex; align-items: center; gap: 6px; border-radius: 11px; background: #3a3a3a; color: #e8e8e8; font: 500 13px/1 \'Inter\', sans-serif; white-space: nowrap; font-variant-numeric: tabular-nums; z-index: 3">654 × {H_ACT} <span style="color: #a8a8a8">· limited by column</span></span>')

# column edge marker on Hero grid (col 1 ends at 654)
rep('<div style="display: grid; grid-template-columns: 1.1fr 1fr; gap: 64px; align-items: center">',
    '<div style="position: relative; display: grid; grid-template-columns: 1.1fr 1fr; gap: 64px; align-items: center">'
    '<div aria-hidden="true" style="position: absolute; left: 653.7px; top: -24px; bottom: -24px; border-left: 1.18px dashed #1a9284; pointer-events: none; z-index: 2">'
    '<span style="position: absolute; left: -1px; top: -22px; transform: translateX(-50%); height: 20px; padding: 0 6px; display: flex; align-items: center; border-radius: 3px; background: #127a70; color: #fff; font: 500 11px/1 \'Inter\', sans-serif; white-space: nowrap">column edge · 654</span></div>')

# limited cursor near the dragged handle (page coords inside hero text area)
rep('<!-- parent-of-selection outline: Hero text -->',
    '<svg aria-hidden="true" width="34" height="26" viewBox="0 0 22 16" style="position: absolute; left: 744px; top: 99px; overflow: visible; z-index: 4">'
    '<path d="M1 8l4-4v2.5h6V4l4 4-4 4V9.5H5V12z" fill="#1d1a16" stroke="#ffffff" stroke-width="1" stroke-linejoin="round"></path>'
    '<circle cx="18" cy="12" r="3.6" fill="#ffffff" stroke="#c9302c" stroke-width="1.3"></circle><path d="M15.6 14.4l4.8-4.8" stroke="#c9302c" stroke-width="1.3"></path></svg>\n'
    '<!-- parent-of-selection outline: Hero text -->')

# options bar: W live, shows the dragged value
rep('<label title="Width · 560px" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px 0 8px; box-sizing: border-box; border-radius: 4px">',
    '<label title="Width · 760 set, 654 shown (limited by column)" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px 0 8px; box-sizing: border-box; border-radius: 4px; background: rgba(47,128,237,0.18); box-shadow: inset 0 0 0 1px #2f80ed">')
rep('<span style="width: 30px">560</span>', '<span style="width: 30px">760</span>')
rep('<span style="width: 30px; color: #a8a8a8">202</span>', f'<span style="width: 30px; color: #a8a8a8">{H_ACT}</span>')

# Properties: W ringed + real-size note
rep('<label title="Width · width: 560px" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px; background: #2a2a2a; border-radius: 2px">',
    '<label title="Width · width: 760px" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px; background: #2a2a2a; border-radius: 2px; box-shadow: inset 0 0 0 1px #2f80ed">')
rep('<span style="font-size: 11px; color: #939393">W</span><span style="flex: 1">560</span>', '<span style="font-size: 11px; color: #939393">W</span><span style="flex: 1">760</span>')
rep('<span style="font-size: 11px; color: #939393">H</span><span style="flex: 1; color: #939393">202</span>', f'<span style="font-size: 11px; color: #939393">H</span><span style="flex: 1; color: #939393">{H_ACT}</span>')
a = s.index('<!-- Size -->')
b = s.index('<div style="height: 1px; background: #303030"></div>', a)
end = s.rindex('</div>', a, b)
note = f'''<div style="display: flex; align-items: flex-start; gap: 6px; margin-top: 8px; font-size: 11px; line-height: 16px; color: #939393">{icon('info', 12, '#939393', 1.25)}<span style="flex: 1">Shown 654 — limited by Hero grid column</span><button style="color: #a8a8a8; text-decoration: underline; text-underline-offset: 2px">Use 654</button></div>
'''
s = s[:end] + note + s[end:]

# status bar
rep('<span style="flex: 1; text-align: center; color: #939393; white-space: nowrap">Drag a handle to resize · Shift keeps proportions</span>',
    '<span style="flex: 1; text-align: center; color: #939393; white-space: nowrap">Hero grid column limits the width to 654 · widen the column, or set Max width in Size → Advanced</span>')
rep('x 612 &#160;y 288', 'x 1004 &#160;y 226')

s = s.replace('class="mp-row mp-hover"', 'class="mp-row"')
open('/home/claude/daisy/project/D07-Limited.dc.html', 'w', encoding='utf-8').write(s)
print('ok')
