import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *
import wiz as WZ
cap = lambda t, d: f'<div style="display: flex; flex-direction: column; gap: 2px; margin-bottom: 12px"><div style="font-size: 13px; font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{d}</div></div>'
cells = [
 ('2 · Design system', 'Choose how to start. Build new is the default; the four detail steps appear in the rail only for Build new and Import.', WZ.step_start(0)),
 ('3 · Colours', 'Base colours make 11-step scales (OKLCH). Roles map steps to what pages use; a dark theme can be made from the same scales.', WZ.step_colours()),
 ('4 · Typography', 'Heading, body and code fonts; a modular scale with a smaller ratio on small screens, written as fluid clamp() sizes.', WZ.step_type()),
 ('5 · Spacing & layout', 'Spacing scale from a 4 px base, and the screen sizes with columns, margins, gutters and max content width.', WZ.step_space()),
 ('6 · Shape & depth', 'Corner radius scale, borders, shadow levels and motion timings.', WZ.step_shape()),
 ('7 · Review', 'Summary with Edit links, token naming, output files and a tokens.css preview. Create project.', WZ.step_review()),
 ('2 · Copy from a project', 'Pick one of your projects; its values fill the detail steps, so they can be changed before creating.', WZ.step_start(1)),
 ('2 · Import tokens', 'Drop a W3C, CSS or Figma variables file; the detail steps open with the imported values to check.', WZ.step_start(2)),
 ('2 · Skip for now', 'The rail drops the detail steps: Project, Design system, Review.', WZ.step_start(3)),
]
body = sheet_header('D-02b', 'New project · setup steps', 'Step-by-step setup like a professional IDE: a rail of steps, one decision per step, a live preview of the tokens, and Create with defaults at any point. Step 1 (Project) is on D-02. Every value stays editable in D-36.')
body += '<div style="display: grid; grid-template-columns: 1200px 1200px; gap: 56px 64px">' + ''.join(f'<div>{cap(t, d)}{c}</div>' for t, d, c in cells) + '</div>'
H = int(sys.argv[1]) if len(sys.argv) > 1 else 4500
open('/home/claude/daisy/project/D02b-NewProject-Steps.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-02b New project setup steps', 2592, H, body))
print('ok')
