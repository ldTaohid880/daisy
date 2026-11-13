"""Light-theme pass over popovers, menus and dialogs (D-33b, c, d)."""
import re
BASE = {
 '#141414': '#eeeeee', '#1b1b1b': '#f7f7f7', '#181818': '#f3f3f3', '#232323': '#ececec', '#1f1f1f': '#fafafa', '#1a1a1a': '#f7f7f7', '#222222': '#f5f5f5',
 '#2a2a2a': '#f0f0f0', '#262626': '#ebebeb', '#2e2e2e': '#e8e8e8', '#303030': '#e1e1e1', '#333333': '#e8e8e8',
 '#3a3a3a': '#dcdcdc', '#3c3c3c': '#cfcfcf', '#454545': '#c9c9c9', '#4f4f4f': '#b5b5b5', '#666666': '#8a8a8a', '#6b6b6b': '#8f8f8f',
 '#757575': '#c9c9c9', '#939393': '#6b6b6b', '#a8a8a8': '#555555', '#c8c8c8': '#3d3d3d', '#e8e8e8': '#1c1c1c',
 '#a9c8f7': '#1f5fb5', '#ff938c': '#cf222e', '#e3b34a': '#9a6700', '#d29922': '#9a6700', '#3fb950': '#1a7f37', '#f85149': '#cf222e', '#58a6ff': '#0969da',
 '#7fb0f0': '#0550ae', '#9cc58a': '#116329', '#d9a66b': '#953800', '#7ee2a8': '#116329', '#d6e6fb': '#1f5fb5',
 'rgba(255,255,255,0.04)': 'rgba(0,0,0,0.035)', 'rgba(255,255,255,0.08)': 'rgba(0,0,0,0.08)', 'rgba(255,255,255,0.1)': 'rgba(0,0,0,0.1)', 'rgba(255,255,255,0.10)': 'rgba(0,0,0,0.1)', 'rgba(255,255,255,0.12)': 'rgba(0,0,0,0.12)', 'rgba(255,255,255,0.15)': 'rgba(0,0,0,0.12)',
 'rgba(255,255,255,0.25)': 'rgba(0,0,0,0.18)', 'rgba(0,0,0,0.25)': 'rgba(0,0,0,0.10)',
 'rgba(0,0,0,0.45)': 'rgba(0,0,0,0.14)', 'rgba(0,0,0,0.5)': 'rgba(0,0,0,0.16)', 'rgba(0,0,0,0.55)': 'rgba(0,0,0,0.18)',
 'rgba(47,128,237,0.18)': 'rgba(47,128,237,0.12)', 'rgba(47,128,237,0.14)': 'rgba(47,128,237,0.10)',
}
pat = re.compile('|'.join(re.escape(k) for k in sorted(BASE, key=len, reverse=True)) + r'(?![0-9a-fA-F])')
def light(s):
    # floating surfaces (popovers, menus, dialogs) become white; scrims stay a little dark
    s = s.replace('background: #262626; border: 1px solid #454545', 'background: #ffffff; border: 1px solid #d4d4d4')
    s = s.replace('background: rgba(0,0,0,0.55); z-index: 50', 'background: rgba(0,0,0,0.28); z-index: 50')
    s = s.replace('background: rgba(0,0,0,0.45)"></div>', 'background: rgba(0,0,0,0.22)"></div>')
    return pat.sub(lambda m: BASE[m.group(0)], s)
def protect(s, start, end):
    a = s.index(start); b = s.index(end, a)
    return light(s[:a]) + s[a:b] + light(s[b:])
P = '/home/claude/daisy/project/'
# D-33b · colour picker over the editor (page content untouched)
s = open(P + 'D39-ColourPicker.dc.html', encoding='utf-8').read()
s = s.replace('overflow: hidden; background: #2a2a2a">\n<span style="position: absolute; left: 46px; top: 13px', 'overflow: hidden; background: #e4e4e4">\n<span style="position: absolute; left: 46px; top: 13px', 1)
s = protect(s, '<!-- page frame', '<!-- vertical scroll indicator').replace('Daisy · D-39 Colour picker', 'Daisy · D-33b Light theme · colour picker')
open(P + 'D33b-Light-Picker.dc.html', 'w', encoding='utf-8').write(s)
# D-33c · menus sheet, D-33d · page dialogs sheet
for src, dst, t in [('D38-Menus.dc.html', 'D33c-Light-Menus.dc.html', 'D-33c Light theme · menus'), ('D54-PageDialogs.dc.html', 'D33d-Light-Dialogs.dc.html', 'D-33d Light theme · dialogs')]:
    s = open(P + src, encoding='utf-8').read()
    s = re.sub(r'<title>[^<]*</title>', f'<title>Daisy · {t}</title>', light(s), 1)
    s = s.replace('D-38 · Daisy design system', 'D-33c · Daisy design system').replace('D-54 · Daisy design system', 'D-33d · Daisy design system')
    open(P + dst, 'w', encoding='utf-8').write(s)
print('ok')
