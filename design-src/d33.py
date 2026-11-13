import re
src = open('/home/claude/daisy/project/Main.dc.html', encoding='utf-8').read()
# Canvas background (workspace) before generic mapping
src = src.replace('overflow: hidden; background: #2a2a2a">\n<span style="position: absolute; left: 46px; top: 13px', 'overflow: hidden; background: #e4e4e4">\n<span style="position: absolute; left: 46px; top: 13px', 1)
a = src.index('<!-- page frame'); b = src.index('<!-- vertical scroll indicator')
head, page, tail = src[:a], src[a:b], src[b:]
M = {  # dark -> light (9.2, plus the chrome tokens 9.2 did not list)
 '#141414': '#eeeeee', '#1b1b1b': '#f7f7f7', '#181818': '#f3f3f3', '#232323': '#ececec', '#1f1f1f': '#fafafa',
 '#2a2a2a': '#f0f0f0', '#262626': '#ebebeb', '#2e2e2e': '#e8e8e8', '#303030': '#e1e1e1', '#333333': '#e8e8e8',
 '#3a3a3a': '#dcdcdc', '#3c3c3c': '#cfcfcf', '#454545': '#c9c9c9', '#4f4f4f': '#b5b5b5', '#666666': '#8a8a8a',
 '#757575': '#c9c9c9', '#939393': '#6b6b6b', '#a8a8a8': '#555555', '#e8e8e8': '#1c1c1c',
 'rgba(255,255,255,0.04)': 'rgba(0,0,0,0.035)', 'rgba(255,255,255,0.25)': 'rgba(0,0,0,0.18)', 'rgba(0,0,0,0.25)': 'rgba(0,0,0,0.10)',
 '#d29922': '#9a6700', '#3fb950': '#1a7f37', '#f85149': '#cf222e',
 'rgba(47,128,237,0.18)': 'rgba(47,128,237,0.12)',
}
pat = re.compile('|'.join(re.escape(k) for k in sorted(M, key=len, reverse=True)) + r'(?![0-9a-fA-F])')
sw = lambda s: pat.sub(lambda m: M[m.group(0)], s)
head, tail = sw(head), sw(tail)
page = page.replace('outline: 1px solid #3c3c3c', 'outline: 1px solid #cfcfcf')
# Text in accent and amber needs darker ink on light surfaces
out = head + page + tail
out = out.replace('<title>Daisy · D-04 Editor, heading selected</title>', '<title>Daisy · D-33 Light theme</title>')
open('/home/claude/daisy/project/D33-Light.dc.html', 'w', encoding='utf-8').write(out)
print('ok', len(out))
