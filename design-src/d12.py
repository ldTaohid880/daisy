from screen import *
_src = open('/home/claude/ds/layoutadv.py').read()
LA = {}
exec(_src[:_src.index('# ═════ A · ROW')], LA)
L = LA

S = Screen('Daisy · D-12 Text tool: editing')
S.remove_h1_overlay()
S.remove_parent_outline()
set_tool(S, 'Text (T)')

P['sup'] = ('stroke', 'M2.5 5l6 7M8.5 5l-6 7M11 2.5a1.5 1.5 0 1 1 3 .6L11 6.5h3')
P['sub'] = ('stroke', 'M2.5 4l6 7M8.5 4l-6 7M11 10.5a1.5 1.5 0 1 1 3 .6L11 14.5h3')
P['code-i'] = ('stroke', 'M5.5 4.5L2 8l3.5 3.5M10.5 4.5L14 8l-3.5 3.5')
P['clear'] = ('stroke', 'M4 3h8M8 3l-2 10M3 13h5M10 9l4 4M14 9l-4 4')
P['list-ul'] = ('stroke', 'M6 4h8M6 8h8M6 12h8M2.5 4h.01M2.5 8h.01M2.5 12h.01')
P['list-ol'] = ('stroke', 'M6.5 4h7.5M6.5 8h7.5M6.5 12h7.5M2 3l1-.5V6M2 9.5a1 1 0 1 1 1.6.8L2 12h2')
P['al-l'] = ('stroke', 'M2.5 4h11M2.5 8h7M2.5 12h9')
P['al-c'] = ('stroke', 'M2.5 4h11M4.5 8h7M3.5 12h9')
P['al-r'] = ('stroke', 'M2.5 4h11M6.5 8h7M4.5 12h9')
P['al-j'] = ('stroke', 'M2.5 4h11M2.5 8h11M2.5 12h11')
P['highlight'] = ('stroke', 'M9.5 2.5l4 4-6 6H3.5v-4zM2 14.5h12')
P['lh'] = ('stroke', 'M2 2.5h12M2 13.5h12M8 5v6M6 6.5L8 4.5l2 2M6 9.5l2 2 2-2')
P['ls'] = ('stroke', 'M2.5 3v10M13.5 3v10M5.5 11l2.5-6 2.5 6M6.3 9h3.4')
P['case'] = ('stroke', 'M1.5 12l3-8 3 8M2.6 9.5h3.8M10 8.5a2 2 0 1 1 0 3.5M12 7.5v4.5')
P['indent'] = ('stroke', 'M6 4h8M6 8h8M6 12h8M2 6l2 2-2 2')
P['quote'] = ('stroke', 'M3 11c0-3 1-5 3-6M9 11c0-3 1-5 3-6M3 11h2.5v-2.5H3zM9 11h2.5v-2.5H9z')

# ---------------- canvas: paragraph editing + floating toolbar ----------------
mini = lambda html, on=False, label='': f'<button aria-label="{label}" style="width: 30px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 4px; {"background: #3a3a3a; color: #ffffff;" if on else "color: #c8c8c8;"}">{html}</button>'
msep = '<span style="width: 1px; height: 18px; background: #3a3a3a; margin: 0 2px"></span>'
float_bar = (f'<span aria-label="Inline marks" style="position: absolute; left: 70px; top: -54px; height: 40px; display: flex; align-items: center; gap: 2px; padding: 0 6px; border-radius: 8px; background: #262626; border: 1px solid #454545; box-shadow: 0 10px 28px rgba(0,0,0,0.35); font: 500 15px/1 \'Inter\', sans-serif; color: #e8e8e8; white-space: nowrap; z-index: 6">'
             + mini('<b>B</b>', True, 'Bold · strong') + mini('<i style="font-family: Georgia, serif">I</i>', False, 'Italic · em') + mini('<u>U</u>', False, 'Underline') + mini('<s>S</s>', False, 'Strikethrough') + msep
             + mini(icon('code-i', 16), False, 'Inline code') + mini(icon('link', 16), False, 'Link · Ctrl+K')
             + mini(f'<span style="display: flex; flex-direction: column; align-items: center; gap: 2px">{icon("highlight", 13)}<span style="width: 14px; height: 3px; border-radius: 1px; background: #f2d78a"></span></span>', False, 'Highlight · mark') + msep
             + mini(icon('more', 16), False, 'More: superscript, subscript, clear formatting') + '</span>')
S.rep('<p style="margin: 0; font-size: 18px; line-height: 1.6; color: #4a443c; max-width: 480px">Each piece is wheel-thrown, glazed and fired in our studio by the river. Made slowly, used daily.</p>',
      '<p style="position: relative; margin: 0; font-size: 18px; line-height: 1.6; color: #4a443c; max-width: 480px">Each piece is '
      '<strong style="font-weight: 600; color: #1d1a16; background: rgba(47,128,237,0.32)">wheel-thrown</strong>, glazed and fired in our studio by the river. Made slowly, used daily.'
      '<span aria-hidden="true" style="position: absolute; inset: -4px -6px; border: 1.18px solid #2f80ed; pointer-events: none"></span>'

      + float_bar + '</p>')
# ---------------- options bar: full text editing bar ----------------
B = lambda t, on=False, label='': f'<button aria-label="{label}" aria-pressed="{str(on).lower()}" style="width: 26px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; {"background: #333333; color: #e8e8e8;" if on else "color: #a8a8a8;"}">{t}</button>'
dd = lambda label, w=None, prefix='': f'<button style="height: 24px; {f"width: {w}px;" if w else ""} display: flex; align-items: center; justify-content: space-between; gap: 6px; padding: 0 6px 0 8px; box-sizing: border-box; border-radius: 4px; white-space: nowrap">{prefix}<span style="flex: 1; text-align: left; overflow: hidden; text-overflow: ellipsis">{label}</span>{icon("chev-down", 10, "#939393", 1.75)}</button>'
num = lambda ic, v, unit='', w=58: f'<label style="height: 24px; width: {w}px; display: flex; align-items: center; gap: 5px; padding: 0 6px; box-sizing: border-box; border-radius: 4px">{icon(ic, 13, "#939393")}<span style="flex: 1">{v}</span><span style="font-size: 10px; color: #939393">{unit}</span></label>'
opts = (mode_chip('Text editing')
        + cap(B(icon('al-l', 14), True, 'Align left') + B(icon('al-c', 14), False, 'Align centre') + B(icon('al-r', 14), False, 'Align right') + B(icon('al-j', 14), False, 'Justify'))
        + cap(B(icon('list-ul', 14), False, 'Bulleted list') + B(icon('list-ol', 14), False, 'Numbered list') + B(icon('quote', 14), False, 'Quote') + capdiv() + B(icon('indent', 14), False, 'Indent'))
        + '<span style="font-size: 11px; color: #939393; white-space: nowrap; padding-left: 4px">Marks: on the selection · Kind, style and values: in Properties</span>'
        + '<span style="flex: 1"></span>'
        + '<button style="height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 8px 0 12px; border-radius: 6px; color: #e8e8e8; font-weight: 500; box-shadow: inset 0 0 0 1px #3a3a3a">Done<span style="height: 18px; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #333333; font-size: 10px; color: #a8a8a8">Esc</span></button>'
        + '<span style="width: 1px; height: 16px; background: #2e2e2e; margin: 0 2px"></span>')
options_left(S, opts, spacer=False)
# give the bar room: hide screen-size switcher label while text editing? keep, but compact: remove Snap (not used in text editing)

set_tree(S, hero_tree('“Each piece is…”'))

# ---------------- properties: deep typography ----------------
small = lambda t: f'<span style="font-size: 11px; color: #939393">{t}</span>'
segm = lambda items, sel: '<div role="group" style="display: grid; grid-template-columns: repeat(' + str(len(items)) + ', minmax(0, 1fr)); gap: 2px; padding: 2px; background: #262626; border-radius: 4px; font-size: 11px">' + ''.join(
    f'<button aria-pressed="{str(i == sel).lower()}" style="height: 20px; display: flex; align-items: center; justify-content: center; gap: 4px; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #939393;"}">{t}</button>' for i, t in enumerate(items)) + '</div>'
row2 = lambda lab, ctl: f'<div style="display: grid; grid-template-columns: 76px minmax(0, 1fr); gap: 8px; align-items: center"><span style="font-size: 11px; color: #a8a8a8">{lab}</span>{ctl}</div>'
slider = lambda pct, val: f'<div style="display: flex; align-items: center; gap: 8px"><span style="position: relative; flex: 1; height: 14px"><span style="position: absolute; left: 0; right: 0; top: 6px; height: 2px; background: #454545; border-radius: 1px"></span><span style="position: absolute; left: 0; width: {pct}%; top: 6px; height: 2px; background: #2f80ed; border-radius: 1px"></span><span style="position: absolute; left: calc({pct}% - 6px); top: 1px; width: 12px; height: 12px; border-radius: 50%; background: #e8e8e8"></span></span><span style="width: 30px; text-align: right; font-size: 11px">{val}</span></div>'
toggle = lambda on: f'<button role="switch" aria-checked="{str(on).lower()}" style="position: relative; width: 28px; height: 16px; border-radius: 8px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {"#fff" if on else "#a8a8a8"}"></span></button>'

scope = f'''<div style="padding: 8px 12px; display: flex; flex-direction: column; gap: 6px; background: rgba(47,128,237,0.08); border-bottom: 1px solid #303030">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 11px; color: #a9c8f7">Changes apply to</span><span style="font-family: {MONO}; font-size: 10px; color: #939393">&lt;strong&gt; · 12 chars</span></div>
{segm(['Selected words', 'Whole paragraph'], 0)}</div>'''

style_row = f'''<div style="display: flex; align-items: center; gap: 8px; padding: 6px 8px; background: #2a2a2a; border-radius: 4px">
<span style="font: 600 15px/1 Inter; width: 22px">Ag</span><span style="flex: 1; min-width: 0"><span style="display: block">Body <span style="color: #e3b34a">· modified</span></span><span style="display: block; font-size: 10px; color: #939393">Inter 18 / 1.6 · from Halden design system</span></span>
<button style="height: 22px; padding: 0 6px; border-radius: 3px; font-size: 11px; color: #a8a8a8">Update style</button>{icon("chev-down", 10, "#939393", 1.5)}</div>'''

typo = (style_row
        + f('<span style="flex: 1; font-family: Inter">Inter</span><span style="font-size: 10px; color: #939393">variable</span>' + icon('chev-down', 10, '#939393', 1.5))
        + pair(f(DOT + '<span style="flex: 1">Semibold</span>' + icon('chev-down', 10, '#939393', 1.5)), f('<span style="font-size: 11px; color: #939393; padding-left: 11px">Size</span><span style="flex: 1; text-align: right">18</span><span style="font-size: 10px; color: #939393">px</span>'))
        + pair(f(icon('lh', 12, '#939393') + '<span style="flex: 1">1.6</span>'), f(icon('ls', 12, '#939393') + '<span style="flex: 1">0</span><span style="font-size: 10px; color: #939393">%</span>'))
        + f(DOT + swatch('#1d1a16') + '<span style="flex: 1">ink</span><span style="color: #939393">100%</span>'))
advanced = f'''<div style="display: flex; align-items: center; gap: 8px; margin-top: 2px"><span style="font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393">ADVANCED</span><span style="flex: 1; height: 1px; background: #333333"></span></div>
{row2('Optical size', slider(30, 'auto'))}
{row2('Case', segm(['Aa', 'AA', 'aa', 'Ab'], 0))}
{row2('Line style', segm(['Solid', 'Dotted', 'Wavy', 'Double'], 0))}
{row2('Wrap', segm(['Normal', 'Balance', 'Pretty', 'No wrap'], 2))}
{row2('Truncate', segm(['Off', '1 line', 'Lines'], 0))}
{row2('Numbers', segm(['Default', 'Tabular', 'Old-style'], 0))}
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 11px; color: #a8a8a8">Ligatures</span>{toggle(True)}</div>
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 11px; color: #a8a8a8">Small caps</span>{toggle(False)}</div>
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 11px; color: #a8a8a8">Fluid size <span style="font-family: {MONO}; font-size: 10px; color: #939393">clamp()</span></span>{toggle(False)}</div>
<div style="display: flex; gap: 6px"><button style="height: 22px; padding: 0 8px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #a8a8a8">+ Text shadow</button><button style="height: 22px; padding: 0 8px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #a8a8a8">+ Other property</button></div>'''

typo_group = f'''<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px">
<div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">Typography</span>
<button aria-label="Typography · Advanced" aria-expanded="true" aria-haspopup="dialog" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; background: #3a3a3a; color: #e8e8e8; box-shadow: 0 0 0 1px #2f80ed">{icon("sliders", 14)}</button></div>
{typo}
<div style="font-size: 10px; line-height: 14px; color: #939393">Optical size, case, wrap, truncate, numbers and more: Advanced</div></div>'''

S.props(panel(header('t-para', '“Each piece is…”', 'Paragraph', 'p') + scope + typo_group))
# Typography · Advanced popover
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
adv_body = advanced.replace('''<div style="display: flex; align-items: center; gap: 8px; margin-top: 2px"><span style="font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393">ADVANCED</span><span style="flex: 1; height: 1px; background: #333333"></span></div>''', '')
pop = f'''<!-- POPOVER: Typography · Advanced -->
<section role="dialog" aria-label="Typography advanced · selected words" style="position: absolute; left: 1282px; top: 208px; width: 328px; box-sizing: border-box; padding: 0 12px 12px; display: flex; flex-direction: column; gap: 9px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); font-variant-numeric: tabular-nums; z-index: 30">
<span aria-hidden="true" style="position: absolute; right: -6px; top: 14px; width: 10px; height: 10px; background: #262626; border-right: 1px solid #454545; border-top: 1px solid #454545; transform: rotate(45deg)"></span>
<div style="height: 40px; margin: 0 -12px; padding: 0 8px 0 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a">
<span style="font-weight: 600">Typography · Advanced</span><span style="flex: 1; font-size: 11px; color: #939393">Selected words</span>
<button aria-label="Pin open" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #939393">{icon("keep", 14)}</button>
<button aria-label="Close" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon("close", 14)}</button></div>
{adv_body}
{L['css_line']('text-wrap: pretty;\nfont-variant-ligatures: common-ligatures;')}
</section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', pop + '\n<!-- ═══════════ TOP BAR v3')

S.status(['Page', 'Section · Hero', 'Box · Hero grid', 'Box · Hero text', 'Text · p', 'strong'],
         'Esc to finish · Shift+Enter for a line break · Ctrl+B / I / U · Ctrl+K link · Ctrl+Shift+V paste as plain text', 'x 496 &#160;y 410')
S.save('D12-TextEditing.dc.html')
print('ok')
