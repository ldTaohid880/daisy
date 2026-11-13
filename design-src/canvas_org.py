import json, sys
sys.path.insert(0, '/home/claude/ds')
from lib import *
P_ = '/home/claude/daisy/project/'
c = json.load(open(P_ + 'canvas.json'))
B = c['boards']
ROWS = [
 ('01', 'Reference', 'The key editor screen and the shared component sheets', ['Main.dc.html', 'Radius.dc.html', 'Layout-Advanced.dc.html']),
 ('02', 'Home and new project', 'First run, projects, the setup steps, a fresh project, Home and Help', ['D01-Home.dc.html', 'D02-Home-Projects.dc.html', 'D02b-NewProject-Steps.dc.html', 'D03-Editor-Fresh.dc.html', 'D52-HomeHelp.dc.html']),
 ('03', 'Selecting and moving', 'Hover, scope, resize, drag, drop, free elements, multi-select', ['D05-Scope.dc.html', 'D06-Resize.dc.html', 'D07-Limited.dc.html', 'D08-FlowDrag.dc.html', 'D09-InvalidDrop.dc.html', 'D10-Free.dc.html', 'D11-MultiSelect.dc.html']),
 ('04', 'Creation tools', 'Text, Box, Section, Button, Link, Form, Media, Elements, Place and interactive parts', ['D12-TextEditing.dc.html', 'D13-BoxDraw.dc.html', 'D43-Section-DirectSelect.dc.html', 'D41-ButtonLink.dc.html', 'D42-Form.dc.html', 'D17-Media.dc.html', 'D18-Elements.dc.html', 'D56-Interactive.dc.html', 'D56b-Interactive-States.dc.html']),
 ('05', 'Shape and inspect tools', 'Layout, Spacing, Transform and Gradient, Measure and Eyedropper', ['D14-LayoutTool.dc.html', 'D15-SpacingTool.dc.html', 'D16-Transform.dc.html', 'D19-Measure.dc.html']),
 ('06', 'Properties', 'Advanced values, colour picker, fill, border and effects, states', ['D20-Advanced.dc.html', 'D39-ColourPicker.dc.html', 'D47-FillBorderEffects.dc.html', 'D21-State.dc.html']),
 ('07', 'Screen sizes, views and themes', 'Tablet, Mobile, Preview, light theme and the compact frame', ['D22-Tablet.dc.html', 'D23-Mobile.dc.html', 'D29-Preview.dc.html', 'D33-Light.dc.html', 'D33b-Light-Picker.dc.html', 'D33c-Light-Menus.dc.html', 'D33d-Light-Dialogs.dc.html', 'D34-Compact.dc.html']),
 ('08', 'Panels', 'Layers, outline and accessibility, Assets', ['D24-Layers.dc.html', 'D25-Outline.dc.html', 'D26-Assets.dc.html']),
 ('09', 'Reusable content', 'Shared parts, components with variants, collections of repeating content', ['D53-SharedParts.dc.html', 'D58-Components.dc.html', 'D58b-Components-States.dc.html', 'D57-Collections.dc.html', 'D57b-Collections-States.dc.html']),
 ('10', 'Code and Timeline', 'The two pro workspaces and their states', ['D27-Code.dc.html', 'D27b-Code-States.dc.html', 'D28-Timeline.dc.html', 'D28b-Timeline-States.dc.html']),
 ('11', 'Design system', 'The editor, opting in later, and its states', ['D36-DesignSystem.dc.html', 'D36b-DesignSystem-Setup.dc.html', 'D36c-DesignSystem-States.dc.html']),
 ('12', 'Pages and settings', 'Page settings, Project settings and the page dialogs', ['D31-PageSettings.dc.html', 'D31b-PageSettings-States.dc.html', 'D44-ProjectSettings.dc.html', 'D44b-ProjectSettings-Tabs.dc.html', 'D54-PageDialogs.dc.html']),
 ('13', 'Files, versions and export', 'Import, versions, export, saving and file problems', ['D45-ImportPage.dc.html', 'D32-Versions.dc.html', 'D32b-Versions-States.dc.html', 'D30-Export.dc.html', 'D55-ExportHistory.dc.html', 'D46-SaveFileStates.dc.html']),
 ('14', 'Menus, search and preferences', 'Menu bar, right-click menus, search, preferences, shortcuts, find and replace', ['D38-Menus.dc.html', 'D48-ContextMenus.dc.html', 'D40-Search.dc.html', 'D49-Preferences.dc.html', 'D50-Shortcuts.dc.html', 'D51-FindReplace.dc.html']),
]
screens = [k for k, v in B.items() if v.get('page') == 'screens' and not k.startswith('SEC-')]
placed = [f for r in ROWS for f in r[3]]
missing = [k for k in screens if k not in placed]; extra = [f for f in placed if f not in B]
assert not missing and not extra, (missing, extra)
for k in [k for k in B if k.startswith('SEC-')]: del B[k]
GAP_X, HEAD_H, HEAD_GAP, ROW_GAP = 160, 280, 80, 360
y = 0; order = []
for code, title, desc, files in ROWS:
    names = []
    for f in files:
        t = B[f]['title']; names.append(t.split(' · ')[0] if ' · ' in t else t)
    sec = f'SEC-{code}.dc.html'
    body = f'''<div style="display: flex; align-items: center; gap: 28px; height: 100%">
<span style="width: 96px; height: 96px; flex: none; display: flex; align-items: center; justify-content: center; border-radius: 20px; background: #246bcb; color: #fff; font-size: 44px; font-weight: 600">{code}</span>
<div style="display: flex; flex-direction: column; gap: 8px"><div style="font-size: 44px; line-height: 52px; font-weight: 600">{title}</div>
<div style="font-size: 18px; line-height: 26px; color: #a8a8a8">{desc}</div><div style="font-size: 15px; color: #6b6b6b; font-family: 'JetBrains Mono', monospace">{' · '.join(names)}</div></div></div>'''
    html = page(f'Daisy · Section {code} · {title}', 1920, HEAD_H, body).replace('padding: 64px;', 'padding: 32px 40px;')
    open(P_ + sec, 'w', encoding='utf-8').write(html)
    B[sec] = {'x': 0, 'y': y, 'w': 1920, 'h': HEAD_H, 'title': f'{code} · {title}', 'page': 'screens'}
    order.append(sec)
    y += HEAD_H + HEAD_GAP
    x = 0; hmax = 0
    for f in files:
        B[f]['x'] = x; B[f]['y'] = y; x += B[f]['w'] + GAP_X; hmax = max(hmax, B[f]['h']); order.append(f)
    y += hmax + ROW_GAP
ds = [k for k in c['order'] if B.get(k, {}).get('page') == 'ds']
c['order'] = order + ds
json.dump(c, open(P_ + 'canvas.json', 'w'), ensure_ascii=False, indent=2)
print('rows', len(ROWS), 'height', y, 'boards', len(B))
