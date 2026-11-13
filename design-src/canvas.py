import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

B = '#2f80ed'
P['b-state'] = ('stroke', 'M8 1.5v3M8 11.5v3M1.5 8h3M11.5 8h3M11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0z')


def mini(inner, w=300, h=180):
    return f'<div style="position: relative; width: {w}px; height: {h}px; overflow: hidden; border-radius: 2px; background: #f6f1ea; box-shadow: 0 0 0 1px #3c3c3c; color: #1d1a16">{inner}</div>'


def ex(label, inner, note=''):
    n = f'<div style="font-size: 10px; line-height: 14px; color: #939393">{note}</div>' if note else ''
    return f'<div style="display: flex; flex-direction: column; gap: 8px">{inner}<div style="font-size: 11px; color: #e8e8e8">{label}</div>{n}</div>'


def box(x, y, w, h, bg='#e7d9c7', extra=''):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; background: {bg}; {extra}"></div>'


def tag(x, y, text, bg='#246bcb'):
    return f'<span style="position: absolute; left: {x}px; top: {y}px; height: 18px; padding: 0 4px; display: flex; align-items: center; gap: 4px; background: {bg}; color: #fff; font-size: 11px; font-weight: 500; white-space: nowrap; font-family: Inter, sans-serif">{text}</span>'


def outline(x, y, w, h, wpx=1.5, col=B, style='solid'):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; box-sizing: border-box; border: {wpx}px {style} {col}"></div>'


def handles(x, y, w, h, radius=True, state='rest'):
    out = ''
    pts = [(x, y), (x + w / 2, y), (x + w, y), (x + w, y + h / 2), (x + w, y + h), (x + w / 2, y + h), (x, y + h), (x, y + h / 2)]
    for i, (px, py) in enumerate(pts):
        st = 'background: #fff; border: 1px solid #2f80ed;'
        if state == 'hover' and i == 4:
            st = 'background: #2f80ed; border: 1px solid #2f80ed;'
        out += f'<span style="position: absolute; left: {px - 4}px; top: {py - 4}px; width: 8px; height: 8px; box-sizing: border-box; border-radius: 1px; {st}"></span>'
    if radius and w >= 48 and h >= 48:
        for px, py in [(x + 10, y + 10), (x + w - 10, y + 10), (x + w - 10, y + h - 10), (x + 10, y + h - 10)]:
            out += f'<span style="position: absolute; left: {px - 3}px; top: {py - 3}px; width: 6px; height: 6px; box-sizing: border-box; border-radius: 50%; background: #fff; border: 1px solid #2f80ed"></span>'
    return out


def pill(x, y, text, bg='#246bcb', col='#fff'):
    return f'<span style="position: absolute; left: {x}px; top: {y}px; height: 18px; padding: 0 6px; display: flex; align-items: center; border-radius: 9px; background: {bg}; color: {col}; font-size: 10px; font-weight: 500; white-space: nowrap; font-family: Inter, sans-serif">{text}</span>'


def text_lines(x, y, n=3, w=150):
    return ''.join(box(x, y + i * 14, w - (i == n - 1) * 50, 6, '#c9bba6', 'border-radius: 2px;') for i in range(n))


# ---------- selection ----------
sel = []
sel.append(ex('Hover', mini(box(60, 60, 180, 60) + outline(60, 60, 180, 60, 1) + tag(59, 40, 'Box · Hero text')), '1 px accent outline + name tag on what a click would select'))
sel.append(ex('Selection', mini(box(60, 60, 180, 70) + outline(60, 60, 180, 70) + tag(59, 40, 'Heading · h1') + handles(60, 60, 180, 70)), '1.5 px outline · 8 handles 8 × 8 · radius handles 10 in, only ≥ 48 px'))
sel.append(ex('Parent of selection', mini(box(30, 30, 240, 120, '#efe6da') + outline(30, 30, 240, 120, 1, 'rgba(47,128,237,0.6)', 'dashed') + box(50, 60, 140, 40) + outline(50, 60, 140, 40) + handles(50, 60, 140, 40, False) + tag(49, 40, 'Text · p')), 'Dashed 1 px accent at 60%'))
sel.append(ex('Multi-selection', mini(''.join(box(30 + i * 85, 60, 70, 70, '#fff', 'border-radius: 6px;') + outline(30 + i * 85, 60, 70, 70, 1) for i in range(3)) + outline(30, 60, 240, 70, 1.5) + handles(30, 60, 240, 70, False)), 'Thin outline on each + one bounding box'))
sel.append(ex('Size label', mini(box(60, 50, 180, 60) + outline(60, 50, 180, 60) + handles(60, 50, 180, 60, False, 'hover') + pill(112, 120, '720 × 116')), 'Accent pill 8 px below while resizing'))
sel.append(ex('Limited by layout', mini(box(60, 50, 180, 60) + outline(60, 50, 180, 60) + handles(60, 50, 180, 60, False) + pill(56, 120, '560 × 202 · limited by column', '#3a3a3a', '#e8e8e8')), 'Neutral pill + "limited" cursor'))
sel.append(ex('Text editing', mini(f'<div style="position: absolute; left: 50px; top: 60px; width: 200px; font-size: 13px; line-height: 18px; font-family: Inter, sans-serif">Each piece is <span style="background: rgba(47,128,237,0.3)">wheel-thrown</span>, glazed and fired<span style="display: inline-block; width: 1px; height: 14px; background: #1d1a16; vertical-align: middle"></span></div>' + outline(46, 56, 208, 44, 1)), '1 px solid outline, no handles, browser caret'))
sel.append(ex('Empty container / section', mini(outline(24, 24, 252, 132, 1, '#c8c8c8', 'dashed') + '<span style="position: absolute; left: 0; right: 0; top: 82px; text-align: center; font-size: 13px; color: #9a9a9a; font-family: Inter, sans-serif">Empty section — pick a tool and click here</span>'), 'Drawn by the overlay, never part of the page'))
sel.append(ex('Marquee', mini(box(40, 40, 70, 50) + box(150, 70, 90, 60) + outline(40, 40, 70, 50, 1) + f'<div style="position: absolute; left: 24px; top: 28px; width: 160px; height: 80px; box-sizing: border-box; border: 1px solid {B}; background: rgba(47,128,237,0.08)"></div>'), '1 px rect, 8% fill; touched elements get hover outlines'))
sel.append(ex('Free element', mini(box(60, 50, 180, 90) + box(196, 40, 54, 24, '#b5532d', 'border-radius: 999px;') + outline(196, 40, 54, 24, 1.5) + tag(195, 20, 'Box · New ◇')), 'Name tag adds ◇'))

# ---------- name tags ----------
tags = ''.join(f'<div style="display: flex; flex-direction: column; gap: 8px; align-items: flex-start"><div style="position: relative; height: 22px">{t}</div><span style="font-size: 10px; color: #939393">{l}</span></div>' for l, t in [
    ('element', tag(0, 0, 'Heading · h1').replace('position: absolute; left: 0px; top: 0px;', 'position: relative;')),
    ('free', tag(0, 0, 'Box · New ◇').replace('position: absolute; left: 0px; top: 0px;', 'position: relative;')),
    ('locked (no outline)', tag(0, 0, f'{icon("lock", 11, "#fff", 1.5)} Footer · footer', '#4f4f4f').replace('position: absolute; left: 0px; top: 0px;', 'position: relative;')),
    ('state badge', tag(0, 0, f'Book a visit · a {icon("b-state", 11, "#fff", 1.5) if "b-state" in P else "⌖"}', '#7c4ed8').replace('position: absolute; left: 0px; top: 0px;', 'position: relative;')),
    ('invalid', tag(0, 0, 'Box · div', '#c9302c').replace('position: absolute; left: 0px; top: 0px;', 'position: relative;')),
    ('just created (600 ms)', tag(0, 0, 'Box · div', '#2f80ed').replace('position: absolute; left: 0px; top: 0px;', 'position: relative; box-shadow: 0 0 0 3px rgba(47,128,237,0.35);')),
])
for c in ('#246bcb', '#4f4f4f', '#7c4ed8', '#c9302c'):
    assert contrast('#ffffff', c) >= 4.5, (c, contrast('#ffffff', c))
tags_block = f'<div style="display: flex; gap: 40px; padding: 20px; background: #f6f1ea; border-radius: 4px">{tags}</div><div style="margin-top: 8px; font-size: 11px; color: #939393">18 h · 4 px padding · 11 px medium white. Fills are darkened tints of their meaning so white text stays ≥ 4.5:1 (state #7c4ed8, invalid #c9302c, locked #4f4f4f).</div>'

# ---------- handles ----------
def hcell(label, inner):
    return f'<div style="display: flex; flex-direction: column; align-items: center; gap: 8px"><div style="position: relative; width: 64px; height: 48px; background: #f6f1ea; border-radius: 2px; display: flex; align-items: center; justify-content: center">{inner}</div><span style="font-size: 10px; color: #939393; text-align: center">{label}</span></div>'


rh = lambda st: {'rest': 'background: #fff; border: 1px solid #2f80ed;', 'hover': 'background: #2f80ed; border: 1px solid #2f80ed;', 'dragging': 'background: #2f80ed; border: 1px solid #2f80ed; box-shadow: 0 0 0 3px rgba(47,128,237,0.3);', 'limited': 'background: #fff; border: 1px solid #a8a8a8;'}[st]
hrow = ''
groups = [
    ('Resize handle · 8 × 8', lambda st: f'<span style="width: 8px; height: 8px; box-sizing: border-box; border-radius: 1px; {rh(st)}"></span>'),
    ('Radius handle · 6', lambda st: f'<span style="width: 6px; height: 6px; box-sizing: border-box; border-radius: 50%; {rh(st)}"></span>'),
    ('Gradient stop', lambda st: f'<span style="width: 12px; height: 12px; box-sizing: border-box; border-radius: 50%; background: #b5532d; box-shadow: 0 0 0 2px {"#fff" if st != "dragging" else "#2f80ed"}, 0 0 0 3px {"#2f80ed" if st != "limited" else "#a8a8a8"}"></span>'),
    ('Transform origin', lambda st: f'<span style="position: relative; width: 14px; height: 14px"><span style="position: absolute; left: 6px; top: 0; width: 2px; height: 14px; background: {"#1a9284" if st != "limited" else "#a8a8a8"}"></span><span style="position: absolute; top: 6px; left: 0; height: 2px; width: 14px; background: {"#1a9284" if st != "limited" else "#a8a8a8"}"></span><span style="position: absolute; left: 4px; top: 4px; width: 6px; height: 6px; box-sizing: border-box; border-radius: 50%; background: {"#1a9284" if st in ("hover", "dragging") else "#fff"}; border: 1.5px solid #1a9284"></span></span>'),
    ('Grid track badge · limited = syntax only editable in Properties', lambda st: f'<span style="height: 18px; padding: 0 5px; display: flex; align-items: center; border-radius: 3px; background: {"#127a70" if st in ("hover", "dragging") else ("#a8a8a8" if st == "limited" else "#127a70")}; color: #fff; font-size: 10px; font-weight: 500; {"box-shadow: 0 0 0 3px rgba(26,146,132,0.35);" if st == "dragging" else ""}">{"1.2fr" if st == "dragging" else ("auto" if st == "limited" else "1fr")}</span>'),
    ('Gap bar', lambda st: f'<span style="width: 14px; height: 40px; background: repeating-linear-gradient(45deg, rgba(219,97,162,{0.8 if st in ("hover", "dragging") else 0.55}) 0 2px, rgba(219,97,162,0.12) 2px 6px); {"box-shadow: 0 0 0 1px #db61a2;" if st == "dragging" else ""} {"filter: grayscale(1);" if st == "limited" else ""}"></span>'),
]
for gname, fn in groups:
    cells = ''.join(hcell(st, fn(st)) for st in ('rest', 'hover', 'dragging', 'limited'))
    hrow += f'<div style="display: flex; flex-direction: column; gap: 10px; padding: 14px; background: #1a1a1a; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a"><span style="font-weight: 500">{gname}</span><div style="display: flex; gap: 10px">{cells}</div></div>'
handles_block = grid(3, hrow, gap=16)
assert contrast('#ffffff', '#127a70') >= 4.0

# ---------- drag & drop ----------
def ins_h(x, y, w, col=B):
    return f'<div style="position: absolute; left: {x}px; top: {y - 1}px; width: {w}px; height: 2px; background: {col}"></div><div style="position: absolute; left: {x - 1}px; top: {y - 3}px; width: 2px; height: 6px; background: {col}"></div><div style="position: absolute; left: {x + w - 1}px; top: {y - 3}px; width: 2px; height: 6px; background: {col}"></div>'


def ins_v(x, y, h, col=B):
    return f'<div style="position: absolute; left: {x - 1}px; top: {y}px; width: 2px; height: {h}px; background: {col}"></div><div style="position: absolute; left: {x - 3}px; top: {y - 1}px; width: 6px; height: 2px; background: {col}"></div><div style="position: absolute; left: {x - 3}px; top: {y + h - 1}px; width: 6px; height: 2px; background: {col}"></div>'


drag = []
drag.append(ex('Flow drag · stack', mini(outline(30, 24, 240, 136, 1) + tag(29, 4, 'into Hero text') + box(46, 40, 160, 14, '#c9bba6') + box(46, 92, 200, 22, '#d8cbb8', 'opacity: 0.3;') + ins_h(46, 72, 208) + box(120, 120, 160, 22, '#d8cbb8', 'opacity: 0.6; box-shadow: 0 6px 16px rgba(0,0,0,0.18);')), 'Ghost 60% · original 30% · 2 px line, 6 px end caps · target outline + tag'))
drag.append(ex('Flow drag · row', mini(outline(20, 50, 260, 80, 1) + ''.join(box(36 + i * 82, 64, 66, 52, '#fff', 'border-radius: 6px;') for i in range(3)) + ins_v(110, 60, 60)), 'Vertical insertion line in rows'))
drag.append(ex('Invalid drop', mini(box(40, 60, 200, 50, '#efe6da') + text_lines(50, 70, 3, 180) + ins_h(40, 56, 200, '#f85149') + pill(150, 120, "Text can't contain boxes", '#c9302c')), 'Red line + reason pill beside the pointer · not-allowed cursor'))
drag.append(ex('Drop inside (hover 400 ms)', mini(box(40, 40, 220, 100, '#efe6da') + outline(40, 40, 220, 100, 1) + f'<div style="position: absolute; left: 40px; top: 40px; width: 220px; height: 100px; background: rgba(47,128,237,0.08)"></div>' + tag(39, 20, 'into Card') + ins_h(56, 90, 188)), 'Container opens; the line moves inside it'))

# ---------- layout + spacing ----------
lay = []
lay.append(ex('Layout tool · grid', mini(outline(16, 40, 268, 110, 1, '#1a9284') + ''.join(box(16 + i * 92, 40, 84, 110, '#fff', 'border-radius: 6px;') for i in range(3)) +
                                     ''.join(f'<div style="position: absolute; left: {100 + i * 92}px; top: 40px; width: 8px; height: 110px; background: repeating-linear-gradient(45deg, rgba(219,97,162,0.55) 0 2px, rgba(219,97,162,0.12) 2px 6px)"></div>' for i in range(2)) +
                                     ''.join(f'<span style="position: absolute; left: {44 + i * 92}px; top: 16px; height: 18px; padding: 0 5px; display: flex; align-items: center; border-radius: 3px; background: #127a70; color: #fff; font-size: 10px; font-family: Inter, sans-serif">1fr</span>' for i in range(3)) +
                                     '<span style="position: absolute; left: 270px; top: 16px; width: 18px; height: 18px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: #fff; box-shadow: inset 0 0 0 1px #1a9284; color: #127a70; font-size: 13px; font-family: Inter, sans-serif">+</span>' + pill(92, 156, 'gap 8', '#b93d82')), 'Purple tracks + badges · hatched pink gap bars · + adds a track'))
lay.append(ex('Layout tool · row', mini(outline(16, 50, 268, 90, 1, '#1a9284') + ''.join(box(28 + i * 86, 62, 74, 66, '#fff', 'border-radius: 6px;') + f'<span style="position: absolute; left: {57 + i * 86}px; top: 117px; width: 16px; height: 8px; border-radius: 4px; background: {"#2f80ed" if i == 1 else "#c8c8c8"}"></span>' for i in range(3)) +
                                    f'<span style="position: absolute; left: 20px; top: 30px; color: #127a70">{icon("chev-right", 16, "#127a70", 2)}</span><span style="position: absolute; left: 38px; top: 32px; font-size: 10px; color: #127a70; font-family: Inter, sans-serif">Row → click to flip</span>'), 'Direction arrow at the start · grow toggles on children'))
lay.append(ex('Spacing tool', mini(f'<div style="position: absolute; left: 30px; top: 20px; width: 240px; height: 140px; background: rgba(63,185,80,0.3); box-shadow: inset 0 0 0 1px #3fb950"></div>' + box(62, 48, 176, 84, '#f6f1ea') +
                                   f'<div style="position: absolute; left: 62px; top: 104px; width: 176px; height: 12px; background: rgba(240,136,62,0.3)"></div>' + box(62, 60, 176, 44, '#e7d9c7') +
                                   '<span style="position: absolute; left: 140px; top: 24px; font-size: 10px; color: #1d5b27; font-family: Inter, sans-serif">72</span><span style="position: absolute; left: 36px; top: 84px; font-size: 10px; color: #1d5b27; font-family: Inter, sans-serif">64</span><span style="position: absolute; left: 132px; top: 104px; font-size: 9px; color: #7a3d10; font-family: Inter, sans-serif">24</span>' + pill(124, 4, '72', '#237a33')), 'Green inside, orange outside, values written in · dragging pill'))
lay.append(ex('Merged margins', mini(box(40, 30, 220, 40) + f'<div style="position: absolute; left: 40px; top: 70px; width: 220px; height: 24px; background: rgba(240,136,62,0.3)"></div><div style="position: absolute; left: 40px; top: 70px; width: 220px; height: 14px; background: rgba(240,136,62,0.15); box-shadow: inset 0 0 0 1px rgba(240,136,62,0.6)"></div>' + box(40, 94, 220, 40) + pill(170, 74, 'merged with neighbour', '#a8511a')), 'The smaller band is tagged'))

# ---------- guides / measure / misc ----------
gm = []
gm.append(ex('Alignment guides', mini(box(30, 60, 90, 70) + box(170, 60, 100, 40, '#b5532d', 'border-radius: 999px;') + outline(170, 60, 100, 40) + f'<div style="position: absolute; left: 10px; right: 10px; top: 60px; border-top: 1px solid #e535ab"></div><div style="position: absolute; left: 120px; width: 50px; top: 80px; border-top: 1px solid #e535ab"></div>' + pill(128, 84, '50', '#c21f8f')), 'Magenta lines on matching edges/centres · gap pills'))
gm.append(ex('Pin lines (Free)', mini(outline(16, 16, 268, 148, 1, 'rgba(47,128,237,0.6)', 'dashed') + box(180, 40, 80, 28, '#b5532d', 'border-radius: 999px;') + outline(180, 40, 80, 28) + f'<div style="position: absolute; left: 220px; top: 16px; height: 24px; border-left: 1px dashed #e535ab"></div><div style="position: absolute; left: 260px; width: 24px; top: 54px; border-top: 1px dashed #e535ab"></div>' + pill(224, 18, '24', '#c21f8f') + pill(258, 60, '24', '#c21f8f')), 'From pinned sides to the anchor, with distances'))
gm.append(ex('Measure / Alt-distance', mini(box(30, 50, 80, 80) + box(190, 70, 80, 60) + f'<div style="position: absolute; left: 110px; width: 80px; top: 100px; border-top: 1px solid #f85149"></div><div style="position: absolute; left: 110px; top: 96px; height: 8px; border-left: 1px solid #f85149"></div><div style="position: absolute; left: 190px; top: 96px; height: 8px; border-left: 1px solid #f85149"></div>' + pill(136, 106, '64', '#c9302c') + f'<div style="position: absolute; left: 230px; top: 50px; height: 20px; border-left: 1px solid #f85149"></div>' + pill(236, 52, '20', '#c9302c')), 'Red lines, end ticks, value pills'))
gm.append(ex('Rotate', mini(box(110, 60, 80, 60, '#e7d9c7', 'opacity: 0.35; outline: 1px dashed #a8a8a8;') + f'<div style="position: absolute; left: 110px; top: 60px; width: 80px; height: 60px; background: #b5532d; transform: rotate(-8deg); box-shadow: 0 0 0 1.5px #2f80ed"></div><span style="position: absolute; left: 143px; top: 83px; width: 14px; height: 14px; color: #1a9284">{icon("plus", 14, "#127a70", 2)}</span>' + pill(128, 132, '−8°')), 'Ghost of the original · purple origin · readout'))
gm.append(ex('Fold line + label', mini(box(20, 20, 260, 140, '#e7d9c7') + f'<div style="position: absolute; left: 0; right: 0; top: 90px; border-top: 1px dashed rgba(47,128,237,0.35)"></div><span style="position: absolute; right: 8px; top: 94px; font-size: 10px; color: #666666; font-family: Inter, sans-serif">Fold · 900</span>'), 'Label below the line, inside the right edge'))
gm.append(ex('Add section bar', f'<div style="width: 300px; height: 180px; display: flex; flex-direction: column; justify-content: flex-end; gap: 8px; padding: 12px; box-sizing: border-box; background: #2a2a2a; border-radius: 2px"><div style="flex: 1; background: #f6f1ea; box-shadow: 0 0 0 1px #3c3c3c"></div><div style="height: 32px; display: flex; align-items: center; justify-content: center; box-sizing: border-box; border: 1px dashed #454545; color: #a8a8a8">+ Add section</div><div style="height: 32px; display: flex; align-items: center; justify-content: center; box-sizing: border-box; border: 1px solid #a8a8a8; color: #e8e8e8">+ Add section · hover</div></div>', '32 h, 8 px under the page'))

body = sheet_header('D-00e', 'Canvas overlay', 'Everything Daisy draws on top of the page: selection, handles, name tags, drag and drop, layout and spacing visuals, guides and measurement. Fixed screen thickness at any zoom; never animated.')
body += section('7.1', 'Selection and hover', '', grid(5, ''.join(sel), gap=24))
body += section('C-29', 'Canvas name tag', 'All states', tags_block)
body += section('C-30', 'Canvas handles', 'rest · hover · dragging · disabled (limited)', handles_block)
body += section('7.3', 'Drag and drop', '', grid(4, ''.join(drag), gap=24))
body += section('12.4 · 12.5', 'Layout and spacing tools', '', grid(4, ''.join(lay), gap=24))
body += section('7.3', 'Guides, measurement and page furniture', '', grid(5, ''.join(gm), gap=24), mb=0)

H = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
open('/home/claude/daisy/project/DS-Canvas.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-00e Canvas overlay', 1920, H, body))
