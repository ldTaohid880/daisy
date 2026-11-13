from screen import *
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
P['section'] = P.get('section', ('stroke', 'M1.5 4h13M1.5 12h13M3 7h10M3 9h7'))
S = Screen('Daisy · D-41 Button and Link tools')
S.remove_h1_overlay(); S.remove_parent_outline(); S.unselect_h1_row()
set_tool(S, 'Button (B)')
POP = 'background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5);'

# ── canvas: a new Secondary button placed after "Our process →", label being typed ──
hpos = ['left: -5.6px; top: -5.6px', 'right: -5.6px; top: -5.6px', 'right: -5.6px; bottom: -5.6px', 'left: -5.6px; bottom: -5.6px']
handles = ''.join(f'<span style="position: absolute; {p}; width: 9.4px; height: 9.4px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>' for p in hpos)
old = '<a href="#process" style="font-size: 16px; font-weight: 500; color: #1d1a16">Our process →</a>'
new_btn = (f'<a href="visit.html" style="position: relative; border-radius: 999px; padding: 11px 23px; border: 1px solid #1d1a16; font-size: 16px; font-weight: 500; line-height: 20px; color: #1d1a16">Gift cards<span style="display: inline-block; width: 1.5px; height: 18px; margin-left: 1px; vertical-align: -3px; background: #2f80ed"></span>'
           f'<span aria-hidden="true" style="position: absolute; inset: -4px; border: 1.76px solid #2f80ed; border-radius: 4px">{handles}'
           f'<span style="position: absolute; left: -1.76px; bottom: calc(100% + 3px); height: 21px; padding: 0 6px; display: flex; align-items: center; gap: 6px; background: #246bcb; color: #fff; font: 500 13px/1 \'Inter\', sans-serif; white-space: nowrap">Button · a<span style="opacity: 0.75">new</span></span></span></a>')
S.rep(old, old + '\n' + new_btn)

# ── options bar: how the tool places (look lives in Properties) ──
lab = lambda t: f'<span style="font-size: 11px; color: #939393; padding: 0 4px 0 8px; white-space: nowrap">{t}</span>'
sb = lambda t, on=False: f'<button aria-pressed="{str(on).lower()}" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; white-space: nowrap; {"background: #333333; color: #e8e8e8; font-weight: 500;" if on else "color: #939393;"}">{t}</button>'
tog = lambda ic, t, on: f'<button aria-pressed="{str(on).lower()}" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; white-space: nowrap; {"background: rgba(47,128,237,0.18); color: #a9c8f7;" if on else "color: #a8a8a8;"}">{icon(ic, 13)}{t}</button>'
opts = (capseg([icon('flow', 12) + 'In flow', icon('free', 12) + 'Free'], 0)
        + cap(lab('The button') + sb('Goes somewhere <span style="font-family: ' + MONO + '; font-size: 10px; color: #939393">a</span>', True) + sb('Runs an action <span style="font-family: ' + MONO + '; font-size: 10px; color: #939393">button</span>'))
        + cap(tog('keep', 'Keep tool', False))
        + '<span style="font-size: 11px; color: #939393; white-space: nowrap; padding-left: 4px">Click a row or stack to add · drag to set the size · look and destination: in Properties</span>')
options_left(S, opts)

# ── layers ──
set_tree(S, hero_tree('Hero buttons', ('Hero buttons', [(56, None, 't-button', 'Shop the collection', 'a', False, (14, 26, 38, 50), ''), (56, None, 't-link', 'Our process →', 'a', False, (14, 26, 38, 50), ''),
                                                       (56, None, 't-button', 'Gift cards', 'a', True, (14, 26, 38, 50), '<span style="margin-left: 6px; font-size: 10px; color: #a9c8f7">new</span>')])))

# ── properties: the new button ──
def preset(name, sample, on=False):
    return (f'<button aria-pressed="{str(on).lower()}" style="height: 52px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 5px; border-radius: 4px; background: #2a2a2a; {"box-shadow: inset 0 0 0 1px #2f80ed;" if on else ""}">'
            f'{sample}<span style="font-size: 10px; color: {"#e8e8e8" if on else "#a8a8a8"}">{name}</span></button>')
pill = lambda st: f'<span style="height: 16px; padding: 0 10px; border-radius: 8px; font-size: 9px; line-height: 16px; {st}">Label</span>'
presets = '<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px">' + preset('Primary', pill('background: #b5532d; color: #fff')) + preset('Secondary', pill('box-shadow: inset 0 0 0 1px #e8e8e8; color: #e8e8e8'), True) + preset('Text', pill('color: #e8e8e8; text-decoration: underline')) + preset('Plain', pill('color: #a8a8a8; box-shadow: inset 0 0 0 1px #454545; border-radius: 2px')) + '</div>'
lab2 = lambda t: f'<span style="font-size: 11px; color: #939393">{t}</span>'
dest = f(lab2('Goes to') + f'<span style="flex: 1">Visit</span><span style="font-family: {MONO}; font-size: 11px; color: #939393">visit.html</span>' + icon('chev-down', 10, '#939393', 1.75), 'box-shadow: inset 0 0 0 1px #3a3a3a')
dest2 = pair(f(lab2('Section') + '<span style="flex: 1; color: #939393; white-space: nowrap">Top</span>' + icon('chev-down', 10, '#939393', 1.75)), f('<span style="flex: 1">New tab</span><span role="switch" aria-checked="false" style="position: relative; width: 24px; height: 14px; border-radius: 7px; background: #454545"><span style="position: absolute; left: 2px; top: 2px; width: 10px; height: 10px; border-radius: 5px; background: #a8a8a8"></span></span>'))
btn_group = (lab2('Style · from Halden design system') + presets
             + '<div style="font-size: 11px; line-height: 15px; color: #939393">Secondary: outline ink 1 px · pill · Inter Medium 16 · Mouse over fills sand. <button style="font-size: 11px; color: #a9c8f7">Edit style</button></div>'
             + dest + dest2)
acc = f(lab2('Name') + '<span style="flex: 1; color: #939393">Gift cards</span><span style="font-size: 10px; color: #939393">from label</span>')
S.props(panel(header('t-button', 'Gift cards', 'Button', 'a') + group('Button', btn_group) + group('Accessibility', acc)
              + more([mp('Size', 'Fit'), mp('Spacing', 'from style'), mp('Fill', 'from style'), mp('Border', 'from style'), mp('Typography', 'from style'), mp('Effects'), mp('Transition &amp; Animation')])))

# ── INSET: Link tool on a whole card ──
card = f'''<div style="position: relative; width: 150px; flex: none; padding: 8px; box-sizing: border-box; border-radius: 8px; background: #ffffff; outline: 1.5px dashed #2f80ed; outline-offset: 3px">
<div style="height: 82px; border-radius: 5px; background: #d8cbb8"></div><div style="margin-top: 8px; font: 13px 'Fraunces', serif; color: #1d1a16">Tide bowl</div><div style="font-size: 11px; color: #5f6b4e">€38</div>
<span style="position: absolute; left: -4px; top: -26px; height: 18px; padding: 0 6px; display: flex; align-items: center; gap: 4px; background: #246bcb; color: #fff; font-size: 10px; white-space: nowrap; border-radius: 2px">{icon('link', 10, '#fff')}Link the whole card</span>
<span style="position: absolute; right: 20px; bottom: 30px">{icon('t-link', 18, '#1d1a16', 2)}</span></div>'''
dtabs = '<div role="tablist" style="display: grid; grid-template-columns: repeat(6, auto); gap: 2px; padding: 2px; background: #1f1f1f; border-radius: 4px; font-size: 11px">' + ''.join(
    f'<button role="tab" aria-selected="{str(i == 0).lower()}" style="height: 22px; padding: 0 7px; border-radius: 3px; white-space: nowrap; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == 0 else "color: #a8a8a8;"}">{t}</button>' for i, t in enumerate(['Page', 'Section', 'Web address', 'Email', 'Phone', 'File'])) + '</div>'
drow = lambda ic, t, sub, on=False: f'<div style="height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 8px; border-radius: 3px; {"background: rgba(47,128,237,0.18);" if on else ""}">{icon(ic, 13, "#a8a8a8")}<span>{t}</span><span style="flex: 1; font-size: 11px; color: #939393; font-family: {MONO}">{sub}</span>{icon("check", 11, "#a9c8f7", 2) if on else ""}</div>'
lpop = f'''<div style="flex: 1; min-width: 0; padding: 10px; display: flex; flex-direction: column; gap: 8px; {POP}">
<div style="display: flex; align-items: center; gap: 8px"><span style="font-weight: 600">Link</span><span style="flex: 1; font-size: 11px; color: #939393">Card · Tide bowl</span>{icon('close', 11, '#a8a8a8')}</div>
{dtabs}
<div style="height: 26px; display: flex; align-items: center; gap: 8px; padding: 0 8px; border-radius: 2px; background: #2a2a2a; box-shadow: inset 0 0 0 1px #2f80ed">{icon('search', 12, '#939393')}<span>tide</span></div>
<div>{drow('file', 'Shop', 'shop.html')}{drow('section', 'Shop › Tide bowl', '#tide-bowl', True)}{drow('section', 'Journal › Tide glaze notes', '#tide')}</div>
<div style="display: flex; align-items: center; gap: 8px; font-size: 11px; color: #a8a8a8"><span style="flex: 1">Open in a new tab</span><span style="position: relative; width: 24px; height: 14px; border-radius: 7px; background: #454545"><span style="position: absolute; left: 2px; top: 2px; width: 10px; height: 10px; border-radius: 5px; background: #a8a8a8"></span></span></div>
<div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #3fb950">{icon('check', 11, '#3fb950', 1.75)}<span style="color: #a8a8a8">Nothing clickable inside the card, so it can be one link.</span></div>
<code style="font-family: {MONO}; font-size: 11px; color: #939393">&lt;a href="shop.html#tide-bowl"&gt; … &lt;/a&gt;</code></div>'''
inset = f'''<!-- INSET: Link tool on a whole element -->
<div style="position: absolute; left: 330px; bottom: 44px; width: 600px; display: flex; flex-direction: column; gap: 8px; z-index: 35">
<span style="width: max-content; height: 20px; display: flex; align-items: center; padding: 0 8px; border-radius: 3px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; color: #a8a8a8">Inset · Link tool (L) clicked on a card · text links: D-17</span>
<div style="display: flex; gap: 22px; align-items: center; padding: 30px 14px 14px; border-radius: 6px; background: #e7d9c7; box-shadow: 0 0 0 1px #3a3a3a">{card}{lpop}</div></div>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', inset + '\n<!-- ═══════════ TOP BAR v3')
S.status(['Page', 'Section · Hero', 'Box · Hero grid', 'Box · Hero text', 'Box · Hero buttons', 'Button · a'],
         'Type the label · Enter to finish · Esc removes the new button', 'x 655 &#160;y 541')
S.save('D41-ButtonLink.dc.html')
print('ok')
