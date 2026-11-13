import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *
P['palette'] = ('stroke', 'M8 1.5a6.5 6.5 0 1 0 0 13c1 0 1.5-.6 1.5-1.4 0-1.2-1-1.3-1-2.3 0-.8.6-1.3 1.5-1.3h1.6a2.9 2.9 0 0 0 2.9-2.9C14.5 4 11.6 1.5 8 1.5z')
P['arrow'] = ('stroke', 'M3 8h10M9 4l4 4-4 4')
M_ = "font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 11px"
POP = 'background: #262626; border: 1px solid #454545; border-radius: 8px; box-shadow: 0 12px 32px rgba(0,0,0,0.5);'
cap = lambda t, d: f'<div style="margin-bottom: 10px"><div style="font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{d}</div></div>'
btn = lambda t, k='sec': f'<button style="height: 26px; padding: 0 12px; border-radius: 4px; white-space: nowrap; {"background: #246bcb; color: #fff; font-weight: 500;" if k == "pri" else ("color: #a8a8a8;" if k == "ghost" else ("box-shadow: inset 0 0 0 1px #454545; color: #ff938c;" if k == "danger" else "box-shadow: inset 0 0 0 1px #454545;"))}">{t}</button>'
fld = lambda inner, focus=False: f'<div style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 6px; box-sizing: border-box; background: #2a2a2a; border-radius: 2px; {"box-shadow: inset 0 0 0 1px #2f80ed;" if focus else ""}">{inner}</div>'
lab = lambda t, w=44: f'<span style="font-size: 11px; color: #939393; width: {w}px; flex: none">{t}</span>'
pair = lambda a, b: f'<div style="display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 8px">{a}{b}</div>'
U = lambda n: f'<span style="font-size: 11px; color: #939393; white-space: nowrap">{n} uses</span>' if n else '<span style="height: 16px; padding: 0 6px; border-radius: 3px; background: #333333; font-size: 10px; line-height: 16px; color: #a8a8a8">Unused</span>'
sw = lambda c, s=24: f'<span style="width: {s}px; height: {s}px; flex: none; border-radius: 4px; background: {c}; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.1)"></span>'
def crow(n, c, uses, sel=False, extra=''):
    return (f'<div style="height: 34px; display: grid; grid-template-columns: 24px 120px 170px 80px minmax(0, 1fr); align-items: center; gap: 10px; padding: 0 10px; border-radius: 4px; {"background: rgba(47,128,237,0.18); box-shadow: inset 0 0 0 1px #2f80ed;" if sel else ""}">'
            f'{sw(c)}<span style="font-weight: 500">{n}</span><span style="{M_}; color: #939393">--color-{n}</span><span style="{M_}">{c[1:].upper()}</span><span style="justify-self: end">{extra or U(uses)}</span></div>')
def props(title, sub, body, w=300):
    return f'''<div style="width: {w}px; flex: none; border-left: 1px solid #303030; background: #1f1f1f">
<div style="padding: 10px 12px; border-bottom: 1px solid #303030"><div style="font-weight: 500">{title}</div><div style="font-size: 11px; color: #939393; margin-top: 3px">{sub}</div></div>
<div style="padding: 10px 12px; display: flex; flex-direction: column; gap: 8px">{body}</div></div>'''
frame = lambda inner, h=360: f'<div style="width: 880px; height: {h}px; display: flex; border-radius: 6px; overflow: hidden; background: #1f1f1f; box-shadow: 0 0 0 1px #303030; position: relative">{inner}</div>'
left = lambda inner: f'<div style="flex: 1; min-width: 0; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; gap: 2px">{inner}</div>'
sec = lambda t, n, r='': f'<div style="height: 30px; display: flex; align-items: center; gap: 8px; padding: 0 10px"><span style="font-weight: 600">{t}</span><span style="font-size: 11px; color: #939393">{n}</span><span style="flex: 1"></span>{r}</div>'

# 1 · edit a text style
def trow(n, ff, fw, px, spec, uses, sel=False):
    return (f'<div style="height: 46px; display: grid; grid-template-columns: 250px minmax(0, 1fr) 60px; align-items: center; gap: 12px; padding: 0 10px; border-radius: 4px; {"background: rgba(47,128,237,0.18); box-shadow: inset 0 0 0 1px #2f80ed;" if sel else ""}">'
            f'<span style="font-family: {ff}; font-weight: {fw}; font-size: {px}px; line-height: 1.1; white-space: nowrap; overflow: hidden">Hand-thrown ceramics</span><span style="display: flex; flex-direction: column"><span style="font-weight: 500">{n}</span><span style="font-size: 11px; color: #939393">{spec}</span></span><span style="justify-self: end">{U(uses)}</span></div>')
L1 = left(sec('Text styles', '5') + trow('Display', "'Fraunces', serif", 600, 28, 'Fraunces 44–64 · 600', 4) + trow('Heading 2', "'Fraunces', serif", 600, 23, 'Fraunces 32–40 · 600 · changed', 7, True)
          + trow('Heading 3', "'Fraunces', serif", 400, 18, 'Fraunces 20 · 400', 12) + trow('Body', "'Inter', sans-serif", 400, 15, 'Inter 16 / 1.5', 38))
fluid = f'''<div style="display: flex; flex-direction: column; gap: 4px">{pair(fld(lab('Min') + '<span style="flex: 1">32</span><span style="font-size: 10px; color: #939393">px</span>', True), fld(lab('Max') + '<span style="flex: 1">40</span><span style="font-size: 10px; color: #939393">px</span>'))}
<div style="position: relative; height: 18px"><span style="position: absolute; left: 0; right: 0; top: 8px; height: 2px; background: #333333"></span><span style="position: absolute; left: 0; right: 0; top: 8px; height: 2px; background: linear-gradient(90deg, #2f80ed, #a9c8f7)"></span>
<span style="position: absolute; left: 0; top: 11px; font-size: 9px; color: #939393">390</span><span style="position: absolute; right: 0; top: 11px; font-size: 9px; color: #939393">1440</span></div></div>'''
P1 = props('Heading 2', 'Text style · used 7 times · h2', fld(lab('Font') + '<span style="flex: 1">Fraunces</span>') + pair(fld(lab('Weight') + '<span>600</span>'), fld(lab('Case') + '<span>As typed</span>'))
           + '<span style="font-size: 11px; color: #a8a8a8">Size · fluid</span>' + fluid + pair(fld(lab('Line') + '<span>1.2</span>'), fld(lab('Letter') + '<span>−0.5%</span>'))
           + '<div style="padding: 8px; border-radius: 4px; background: rgba(47,128,237,0.12); font-size: 11px; line-height: 15px; color: #c8c8c8">Changed from 40 → 32–40. <b style="font-weight: 600">7 headings on 3 pages</b> update. 1 heading on Shop overrides the size and keeps it.</div>'
           + f'<div style="display: flex; gap: 6px">{btn("Revert", "ghost")}<span style="flex: 1"></span><span style="font-size: 11px; color: #939393; align-self: center">Ctrl Z undoes</span></div>')
c1 = frame(L1 + P1)

# 2 · add a colour token
new_row = f'''<div style="padding: 8px 10px; display: flex; flex-direction: column; gap: 8px; border-radius: 4px; background: rgba(47,128,237,0.12); box-shadow: inset 0 0 0 1px #2f80ed">
<div style="display: grid; grid-template-columns: 24px 120px 170px 80px minmax(0, 1fr); align-items: center; gap: 10px">{sw('#c08a3e')}
<span style="height: 24px; display: flex; align-items: center; padding: 0 6px; border-radius: 2px; background: #1b1b1b; box-shadow: inset 0 0 0 1px #2f80ed">honey<span style="width: 1px; height: 12px; background: #e8e8e8; margin-left: 1px"></span></span>
<span style="{M_}; color: #939393">--color-honey</span><span style="{M_}">C08A3E</span><span style="justify-self: end; font-size: 11px; color: #a9c8f7">new</span></div>
<div style="display: flex; align-items: center; gap: 10px; font-size: 11px; color: #a8a8a8"><span>Picked from</span><span style="color: #c8c8c8">Shop › Sale badge</span><span style="flex: 1"></span><span style="display: flex; align-items: center; gap: 6px">Also make a scale (50–950)<span style="width: 14px; height: 14px; border-radius: 3px; box-shadow: inset 0 0 0 1px #6b6b6b"></span></span></div>
<div style="display: flex; gap: 6px; align-items: center"><span style="font-size: 11px; color: #939393">Enter adds · Esc cancels · names use lowercase and dashes</span><span style="flex: 1"></span>{btn("Cancel", "ghost")}{btn("Add colour", "pri")}</div></div>'''
L2 = left(sec('Colours', '8', '<span style="font-size: 11px; color: #a9c8f7">+ Colour</span>') + crow('brand', '#b5532d', 18) + crow('ink', '#1d1a16', 42) + crow('sand', '#f6f1ea', 4) + crow('moss', '#5f6b4e', 9) + new_row)
c2 = frame(L2, 330)

# 3 · replace and delete
dlg = f'''<div style="position: absolute; left: 150px; top: 30px; width: 580px; padding: 16px; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px; {POP}">
<b style="font-size: 14px; font-weight: 600">Delete brand-deep?</b>
<span style="font-size: 12px; line-height: 18px; color: #c8c8c8">It is used <b style="font-weight: 600">6 times</b> on 2 pages (button hovers). Pick what those uses become.</span>
<div style="display: flex; flex-direction: column; gap: 4px">
<div style="height: 34px; display: flex; align-items: center; gap: 10px; padding: 0 10px; border-radius: 4px; background: rgba(47,128,237,0.18); box-shadow: inset 0 0 0 1px #2f80ed"><span style="width: 14px; height: 14px; box-sizing: border-box; border-radius: 7px; border: 4px solid #2f80ed"></span>Use another token{sw('#b5532d', 18)}<b style="font-weight: 600">brand</b><span style="flex: 1"></span><span style="font-size: 11px; color: #939393">closest · ΔE 6</span></div>
<div style="height: 34px; display: flex; align-items: center; gap: 10px; padding: 0 10px; border-radius: 4px; background: #2a2a2a"><span style="width: 14px; height: 14px; box-sizing: border-box; border-radius: 7px; border: 1.5px solid #6b6b6b"></span>Keep the colour as a plain value<span style="flex: 1"></span><span style="{M_}; color: #939393">#9E4626</span></div></div>
<div style="display: flex; align-items: center; gap: 10px; padding: 8px; border-radius: 4px; background: #1f1f1f"><span style="padding: 6px 14px; border-radius: 999px; background: #9e4626; color: #fff; font-size: 11px">Before</span>{icon('arrow', 14, '#6b6b6b')}<span style="padding: 6px 14px; border-radius: 999px; background: #b5532d; color: #fff; font-size: 11px">After</span><span style="font-size: 11px; color: #939393">Shop the collection · Mouse over</span></div>
<div style="display: flex; gap: 8px">{btn("Select the 6 uses", "ghost")}<span style="flex: 1"></span>{btn("Cancel", "ghost")}{btn("Replace and delete", "danger")}</div>
<span style="font-size: 11px; color: #939393">An unused token is deleted at once, with Undo in the status bar.</span></div>'''
L3 = left(sec('Colours', '8') + crow('brand', '#b5532d', 18) + crow('brand-deep', '#9e4626', 6, True) + crow('brand-light', '#c86a43', 0) + crow('ink', '#1d1a16', 42) + crow('sand', '#f6f1ea', 4))
c3 = frame(L3 + '<div style="position: absolute; inset: 0; background: rgba(0,0,0,0.45)"></div>' + dlg, 380)

# 4 · collect from pages
def found(c, uses, where, near, nc, act):
    return (f'<div style="height: 36px; display: grid; grid-template-columns: 16px 24px 80px 150px minmax(0, 1fr) 150px; align-items: center; gap: 10px; padding: 0 10px; border-radius: 4px; background: #2a2a2a">'
            f'<span style="width: 14px; height: 14px; border-radius: 3px; background: #246bcb; display: flex; align-items: center; justify-content: center">{icon("check", 10, "#fff", 2)}</span>{sw(c)}<span style="{M_}">{c[1:].upper()}</span>'
            f'<span style="font-size: 11px; color: #a8a8a8">{uses} uses · {where}</span><span style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #c8c8c8">{icon("arrow", 12, "#6b6b6b")}{sw(nc, 14) if nc else ""}{near}</span>'
            f'<span style="justify-self: end; display: flex; gap: 2px; padding: 2px; border-radius: 4px; background: #1f1f1f; font-size: 11px">{act}</span></div>')
seg2 = lambda a, b, sel: f'<span style="height: 20px; padding: 0 8px; line-height: 20px; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8;" if sel == 0 else "color: #a8a8a8;"}">{a}</span><span style="height: 20px; padding: 0 8px; line-height: 20px; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8;" if sel == 1 else "color: #a8a8a8;"}">{b}</span>'
L4 = left(f'<div style="display: flex; align-items: center; gap: 10px; padding: 4px 10px 8px"><b style="font-weight: 600">Collect from pages</b><span style="font-size: 11px; color: #939393">Values used on pages that are not tokens · 4 pages scanned</span><span style="flex: 1"></span>{segm if False else ""}</div>'
          + '<div style="display: flex; gap: 14px; padding: 0 10px 8px; font-size: 11px"><span style="color: #e8e8e8; font-weight: 500; border-bottom: 2px solid #2f80ed; padding-bottom: 4px">Colours 5</span><span style="color: #a8a8a8">Text sizes 3</span><span style="color: #a8a8a8">Spacing 6</span><span style="color: #a8a8a8">Radius 2</span></div>'
          + '<div style="display: flex; flex-direction: column; gap: 4px">'
          + found('#9b4424', 3, 'Home', 'like brand-deep · ΔE 1.1', '#9e4626', seg2('Map', 'New token', 0))
          + found('#6b6358', 5, 'Home, Shop', 'like ink-soft · ΔE 4.0', '#4a443c', seg2('Map', 'New token', 1))
          + found('#e6dccd', 4, 'Home, Journal', 'like clay · ΔE 2.2', '#e7d9c7', seg2('Map', 'New token', 0))
          + found('#c08a3e', 2, 'Shop', 'nothing close', '', seg2('Map', 'New token', 1))
          + found('#d8cbb8', 6, 'all pages', 'like clay · ΔE 3.1', '#e7d9c7', seg2('Map', 'New token', 0)) + '</div>'
          + f'<div style="display: flex; align-items: center; gap: 8px; padding: 10px 10px 0"><span style="font-size: 11px; color: #939393">Map links those uses to the token; New token adds it and links them. 20 uses change.</span><span style="flex: 1"></span>{btn("Apply 5", "pri")}</div>')
c4 = frame(L4, 340)

# 5 · rename
L5 = left(sec('Colours', '8') + crow('brand', '#b5532d', 18, True))
P5 = props('Rename terracotta', 'Colour token', fld(lab('Name') + '<span style="flex: 1">brand</span>', True)
           + f'<div style="font-size: 11px; line-height: 16px; color: #c8c8c8"><span style="{M_}; color: #ff938c; text-decoration: line-through">--color-terracotta</span> → <span style="{M_}; color: #7ee2a8">--color-brand</span></div>'
           + '<div style="font-size: 11px; line-height: 15px; color: #a8a8a8">Updates 18 uses, tokens.css and Custom CSS in 2 places.</div>'
           + f'<div style="display: flex; align-items: center; gap: 8px; font-size: 11px"><span style="flex: 1; color: #c8c8c8">Keep the old name working</span><span style="position: relative; width: 28px; height: 16px; border-radius: 8px; background: #246bcb"><span style="position: absolute; right: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: #fff"></span></span></div>'
           + f'<code style="{M_}; font-size: 10px; color: #939393">--color-terracotta: var(--color-brand);</code><div style="font-size: 10px; line-height: 14px; color: #939393">For CSS outside Daisy that still uses the old name.</div>', 380)
c5 = frame(L5 + P5, 260)

cells = [('1 · Editing a text style', 'Heading 2 selected; Properties edits the style. Fluid size as min–max over the screen range; the note says what updates and what keeps an override.', c1),
         ('2 · Adding a colour', 'A new row opens inline with the name focused; the value comes from the eyedropper or the picker. Optional scale.', c2),
         ('3 · Deleting a used token', 'Delete asks what the uses become: another token (closest suggested, with before and after) or a plain value.', c3),
         ('4 · Collect from pages', 'Values that are on pages but not tokens, by kind. Each is mapped to a near token or made a new one; one Apply.', c4),
         ('5 · Renaming a token', 'Renaming updates every use and tokens.css; the old name can keep working as an alias.', c5)]
body = sheet_header('D-36c', 'Design system editor · states', 'Editing a text style, adding, deleting and renaming tokens, and collecting values from the pages. Read with D-36.')
body += '<div style="display: grid; grid-template-columns: repeat(2, 880px); gap: 48px 32px; align-items: start">' + ''.join(f'<div>{cap(t, d)}{c}</div>' for t, d, c in cells) + '</div>'
H = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
open('/home/claude/daisy/project/D36c-DesignSystem-States.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-36c Design system editor states', 1920, H, body))
print('ok')
