import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *
import dsetup as DS

P['palette'] = ('stroke', 'M8 1.5a6.5 6.5 0 1 0 0 13c1 0 1.5-.6 1.5-1.4 0-1.2-1-1.3-1-2.3 0-.8.6-1.3 1.5-1.3h1.6a2.9 2.9 0 0 0 2.9-2.9C14.5 4 11.6 1.5 8 1.5z')
cap = lambda t, d: f'<div style="display: flex; flex-direction: column; gap: 2px; margin-bottom: 10px"><div style="font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{d}</div></div>'
btn = lambda t, primary=False: f'<button style="height: 28px; padding: 0 {14 if primary else 12}px; border-radius: 4px; font-weight: 500; {"background: #246bcb; color: #fff;" if primary else "background: #2a2a2a; box-shadow: inset 0 0 0 1px #454545;"}">{t}</button>'
def dialog(body, create='Create'):
    return f'''<div style="width: 680px; display: flex; flex-direction: column; border-radius: 4px; background: #262626; border: 1px solid #454545; box-shadow: 0 8px 24px rgba(0,0,0,0.45)">
<div style="height: 44px; display: flex; align-items: center; justify-content: space-between; padding: 0 8px 0 16px; border-bottom: 1px solid #333333"><span style="font-size: 14px; font-weight: 600">New project</span>{icon("close", 12, "#a8a8a8")}</div>
<div style="display: flex; flex-direction: column; gap: 16px; padding: 16px">
<label style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 11px; color: #a8a8a8">Name</span><span style="height: 28px; display: flex; align-items: center; padding: 0 8px; background: #2a2a2a; border-radius: 2px">Mossbank Tea</span></label>
{body}</div>
<div style="height: 52px; display: flex; align-items: center; gap: 8px; padding: 0 16px; border-top: 1px solid #333333"><span style="flex: 1; font-size: 11px; color: #939393">Enter to create</span>{btn("Cancel")}{btn(create, True)}</div></div>'''
dshead = lambda sel: f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="display: flex; align-items: baseline; gap: 8px"><span style="font-weight: 600">Design system</span><span style="font-size: 11px; color: #939393">Shared by every page. You can change it any time in Project › Design system.</span></div>{DS.choice(sel)}</div>'

# A · Copy from a project
projs = [('Halden', ['#b5532d', '#9e4626', '#1d1a16', '#4a443c', '#f6f1ea', '#e7d9c7', '#5f6b4e'], '25 tokens · Fraunces, Inter', True),
         ('North Pier Coffee', ['#0f3d3e', '#e2b04a', '#1c1c1c', '#f7f4ee', '#d9d2c3'], '19 tokens · Inter', False),
         ('Studio Lumen', ['#111111', '#ff5a36', '#f2f2f2', '#8a8a8a'], '14 tokens · Space Grotesk', False)]
prow = lambda n, cs, sub, on: (f'<div style="height: 44px; display: flex; align-items: center; gap: 12px; padding: 0 10px; border-radius: 4px; {"background: rgba(47,128,237,0.18); box-shadow: inset 0 0 0 1px #2f80ed;" if on else ""}">'
    f'<span style="width: 14px; height: 14px; border-radius: 7px; box-sizing: border-box; {"border: 4px solid #2f80ed;" if on else "border: 1.5px solid #6b6b6b;"}"></span>'
    f'<span style="flex: 1; display: flex; flex-direction: column"><span style="font-weight: 500">{n}</span><span style="font-size: 11px; color: #939393">{sub}</span></span>{DS.chips(cs)}</div>')
A = dialog(dshead(1) + '<div style="display: flex; flex-direction: column; gap: 2px">' + ''.join(prow(*p) for p in projs) + '</div>'
           + '<div style="display: flex; align-items: center; gap: 8px; font-size: 11px; line-height: 16px; color: #939393">' + icon('info', 12, '#58a6ff', 1.25) + 'Copies the tokens only, not pages or content. The two projects do not stay linked.</div>')

# B · Skip for now
B = dialog(dshead(2) + f'''<div style="padding: 14px; display: flex; gap: 12px; border-radius: 4px; background: #1f1f1f">{icon("palette", 16, "#a8a8a8")}
<div style="font-size: 11px; line-height: 16px; color: #a8a8a8"><b style="font-weight: 600; color: #e8e8e8">The project starts without tokens.</b><br>Pages use plain values. Set the design system up later from Project › Design system; Daisy can collect the colours and sizes your pages already use.</div></div>''')

# C · Design system tab, not set up yet (opt in later)
hdr = '<div style="height: 32px; display: flex; align-items: stretch; background: #181818; border-bottom: 1px solid #2a2a2a"><span style="height: 32px; display: flex; align-items: center; gap: 8px; padding: 0 12px; color: #a8a8a8; border-right: 1px solid #262626">Home<span style="font-family: \'JetBrains Mono\', monospace; font-size: 11px; color: #939393">index.html</span></span><span style="position: relative; height: 32px; display: flex; align-items: center; gap: 8px; padding: 0 12px; background: #1f1f1f; border-right: 1px solid #303030"><span style="position: absolute; left: 0; right: 0; top: 0; height: 2px; background: #2f80ed"></span>' + icon('palette', 13, '#e8e8e8') + '<b style="font-weight: 500">Design system</b><span style="font-family: \'JetBrains Mono\', monospace; font-size: 11px; color: #939393">not set up</span></span></div>'
found = ['#4f6b3a', '#2d3a24', '#1e1e1e', '#6a6a6a', '#fbfaf6', '#efe9dc']
opt = lambda ic, t, d, primary=False: f'''<div style="display: flex; gap: 14px; padding: 14px 16px; border-radius: 6px; {"background: rgba(47,128,237,0.14); box-shadow: inset 0 0 0 1px #2f80ed;" if primary else "background: #2a2a2a;"}"><span style="width: 36px; height: 36px; flex: none; display: flex; align-items: center; justify-content: center; border-radius: 8px; background: {"#246bcb" if primary else "#333333"}">{icon(ic, 17, "#fff" if primary else "#c8c8c8")}</span><span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 13px; font-weight: 600">{t}</span><span style="font-size: 12px; line-height: 18px; color: #a8a8a8">{d}</span></span></div>'''
P['sparkle'] = ('stroke', 'M8 2v3M8 11v3M2 8h3M11 8h3M4 4l1.8 1.8M10.2 10.2L12 12M12 4l-1.8 1.8M5.8 10.2L4 12')
P['import'] = ('stroke', 'M8 2v8M5 7l3 3 3-3M3 12.5h10')
C = f'''<div style="width: 1316px; border-radius: 6px; overflow: hidden; box-shadow: 0 0 0 1px #303030">{hdr}
<div style="height: 470px; display: flex; justify-content: center; padding-top: 40px; box-sizing: border-box; background: #1f1f1f">
<div style="width: 640px; display: flex; flex-direction: column; gap: 12px">
<span style="font-size: 16px; font-weight: 600">Mossbank Tea has no design system yet</span>
<span style="font-size: 12px; line-height: 18px; color: #a8a8a8">Tokens are shared by all 3 pages. Values the pages already use stay as they are until you link them.</span>
<div style="display: flex; align-items: center; gap: 12px; padding: 10px 12px; border-radius: 4px; background: rgba(88,166,255,0.10); box-shadow: inset 0 0 0 1px rgba(88,166,255,0.35)">{icon("eyedropper", 14, "#58a6ff")}
<span style="flex: 1; font-size: 11px; line-height: 16px; color: #c8c8c8"><b style="font-weight: 600; color: #e8e8e8">Found on your pages:</b> 6 colours, 2 fonts (Lora, Inter), 4 text sizes</span>{DS.chips(found)}</div>
{opt("eyedropper", "Start from what the pages use", "Opens the setup steps filled with the colours, fonts and sizes found above, and links them to the new tokens.", True)}
{opt("sparkle", "Build a new design system", "The same steps as a new project: Colours, Typography, Spacing &amp; layout, Shape &amp; depth, Review.")}
{opt("import", "Copy from a project or import tokens", "Another project’s tokens, or a W3C, CSS or Figma variables file.")}
</div></div></div>'''

# D · Project panel row
row = lambda inner: f'<div style="width: 260px; height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 20px; box-sizing: border-box; background: #1f1f1f">{icon("chev-right", 12, "#a8a8a8")}{inner}</div>'
D = (f'<div style="display: flex; flex-direction: column; gap: 10px">'
     + '<span style="font-size: 11px; color: #939393">Set up</span>' + row('<span style="flex: 1; color: #a8a8a8">Design system</span><span style="display: flex; gap: 2px">' + ''.join(f'<span style="width: 8px; height: 8px; border-radius: 2px; background: {c}"></span>' for c in ['#b5532d', '#1d1a16', '#f6f1ea', '#e7d9c7', '#5f6b4e']) + '</span>')
     + '<span style="font-size: 11px; color: #939393">Skipped</span>' + row('<span style="flex: 1; color: #a8a8a8">Design system</span><button style="height: 18px; padding: 0 8px; border-radius: 3px; box-shadow: inset 0 0 0 1px #454545; font-size: 11px; color: #e8e8e8">Set up</button>')
     + '<span style="font-size: 11px; line-height: 16px; color: #939393; max-width: 300px">Swatches in the editor read "No design system yet · Set up" instead of the empty lists of D-03.</span></div>')

body = sheet_header('D-36b', 'Design system · creating and opting in', 'A design system is made in the New project steps (D-02, D-02b) or skipped there. A skipped project opts in later from the Design system tab; every token is edited later in D-36.')
body += f'''<div style="display: flex; gap: 64px; align-items: start">
<div>{cap('A · Set up later (Design system tab)', 'A skipped project opts in here. Each choice opens the setup steps of D-02b, without the Project step.')}{C}</div>
<div>{cap('B · Project panel', 'The tree row with tokens and without')}{D}</div></div>'''
H = int(sys.argv[1]) if len(sys.argv) > 1 else 1400
open('/home/claude/daisy/project/D36b-DesignSystem-Setup.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-36b Design system setup', 1920, H, body))
print('ok')
