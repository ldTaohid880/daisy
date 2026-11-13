from screen import *
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
P['textarea'] = ('stroke', 'M2 3h12v10H2zM4.5 6h7M4.5 8.5h7M4.5 11h4')
P['dropdown'] = ('stroke', 'M2 5h12v6H2zM10 7.2l1.3 1.3 1.3-1.3')
P['checkbox'] = ('stroke', 'M3 3h10v10H3zM5.5 8l2 2 3.5-4')
P['radio'] = ('stroke', 'M8 2.5a5.5 5.5 0 1 1 0 11 5.5 5.5 0 0 1 0-11zM8 6.2a1.8 1.8 0 1 1 0 3.6 1.8 1.8 0 0 1 0-3.6z')
P['label'] = ('stroke', 'M2.5 4h7l4 4-4 4h-7zM5 8h2')
P['send'] = ('stroke', 'M2 8l12-5-5 12-2-5z')
S = Screen('Daisy · D-42 Form tool')
set_tool(S, 'Form (F)')
FLOAT = 'background: #262626; border: 1px solid #454545; box-shadow: 0 8px 24px rgba(0,0,0,0.45);'
POP = 'background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5);'

# ── page tab and project: the Visit page ──
S.rep('<span style="font-weight: 500; color: #e8e8e8">Home</span>', '<span style="font-weight: 500; color: #e8e8e8">Visit</span>')
S.rep('index.html @ 85%', 'visit.html @ 85%')
S.rep('<div role="treeitem" aria-current="page" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 44px; background: #2a2a2a">', '<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 44px">')
S.rep('<span style="flex: 1; color: #e8e8e8; font-weight: 500">Home</span>', '<span style="flex: 1">Home</span>')
S.rep('<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 44px; color: #a8a8a8">\n<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#757575"',
      '<div role="treeitem" aria-current="page" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 44px; background: #2a2a2a; color: #e8e8e8">\n<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#e8e8e8"')
S.rep('<span style="flex: 1">Visit</span>', '<span style="flex: 1; font-weight: 500">Visit</span>')

# ── canvas: the Visit page with a booking form; a Phone field about to be placed ──
lab = lambda t, req=False: f'<span style="font-size: 14px; font-weight: 500; color: #1d1a16">{t}{"<span style=\"color: #b5532d\"> *</span>" if req else ""}</span>'
inp = lambda v, ph=False, h=48: f'<span style="height: {h}px; display: flex; align-items: {"flex-start" if h > 48 else "center"}; padding: {"14px" if h > 48 else "0"} 16px; box-sizing: border-box; border-radius: 8px; background: #fbf8f3; box-shadow: inset 0 0 0 1px #d9cbb7; font-size: 16px; color: {"#8a8174" if ph else "#1d1a16"}">{v}</span>'
fieldp = lambda l, c, req=False: f'<div style="display: flex; flex-direction: column; gap: 8px">{lab(l, req)}{c}</div>'
ins_line = f'''<div style="position: relative; height: 0">
<span aria-hidden="true" style="position: absolute; left: -8px; right: -8px; top: -11px; height: 2.35px; background: #2f80ed"><span style="position: absolute; left: -3.5px; top: -3.5px; width: 9.4px; height: 9.4px; border-radius: 5px; background: #2f80ed"></span><span style="position: absolute; right: -3.5px; top: -3.5px; width: 9.4px; height: 9.4px; border-radius: 5px; background: #2f80ed"></span>
<span style="position: absolute; left: 12px; top: 6px; height: 21px; padding: 0 6px; display: flex; align-items: center; gap: 6px; background: #246bcb; color: #fff; font: 500 13px/1 'Inter', sans-serif; white-space: nowrap; border-radius: 2px">+ Label and text field · after Email</span></span>
<svg style="position: absolute; left: 330px; top: -6px" width="26" height="26" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v18M3 12h18" stroke="#1d1a16" stroke-width="2"/><path d="M12 3v18M3 12h18" stroke="#fff" stroke-width="0.8"/></svg></div>'''
form = f'''<form style="position: relative; width: 560px; padding: 32px; box-sizing: border-box; display: flex; flex-direction: column; gap: 22px; border-radius: 12px; background: #ffffff">
<span aria-hidden="true" style="position: absolute; inset: -6px; border: 1.18px dashed rgba(47,128,237,0.6); border-radius: 14px"><span style="position: absolute; right: 8px; top: -26px; height: 21px; padding: 0 7px; display: flex; align-items: center; background: rgba(47,128,237,0.14); border: 1.18px dashed rgba(47,128,237,0.6); color: #1f5fb5; font: 500 13px/1 'Inter', sans-serif; white-space: nowrap">Form · adding inside</span></span>
{fieldp('Your name', inp('Ingrid Holm'), True)}
{fieldp('Email', inp('ingrid@example.com'), True)}
{ins_line}
{fieldp('Day', inp('Saturday 21 November<span style="flex: 1"></span><span style="font-size: 14px">▾</span>'))}
{fieldp('Anything we should know?', inp('Two of us, around 11. We would love to see the kiln.', h=96))}
<span style="display: flex; align-items: center; gap: 10px; font-size: 15px; color: #4a443c"><span style="width: 20px; height: 20px; border-radius: 4px; background: #1d1a16; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 13px">✓</span>Send me the studio letter, four times a year</span>
<span style="align-self: flex-start; padding: 13px 26px; border-radius: 999px; background: #b5532d; color: #fff; font-size: 16px; font-weight: 500">Request a visit</span>
</form>'''
header_html = S.s[S.s.index('<!-- Header -->', S.s.index('<!-- page frame')):S.s.index('<!-- Hero -->', S.s.index('<!-- page frame'))]
page_new = f'''<!-- page frame: 1440 @ 85% = 1224 · Visit page -->
<div style="position: absolute; left: 46px; top: 32px; bottom: 0; width: 1224px; overflow: hidden; outline: 1px solid #3c3c3c; background: #f6f1ea">
<div style="position: relative; width: 1440px; transform: scale(0.85); transform-origin: 0 0; background: #f6f1ea; color: #1d1a16; font-family: 'Inter', sans-serif; font-size: 16px; line-height: 1.5">
{header_html}
<div style="padding: 56px 64px 96px; display: grid; grid-template-columns: 1fr 560px; gap: 96px; align-items: start">
<div style="display: flex; flex-direction: column; gap: 22px; padding-top: 24px">
<p style="margin: 0; font-size: 13px; letter-spacing: 0.08em; text-transform: uppercase; color: #5f6b4e; font-weight: 500">Riverside Works, Unit 4</p>
<h1 style="margin: 0; font-family: 'Fraunces', serif; font-size: 56px; line-height: 1.05; font-weight: 600">Book a studio visit</h1>
<p style="margin: 0; max-width: 460px; font-size: 18px; line-height: 1.6; color: #4a443c">Saturdays from 10 to 4. See the wheels and the kiln, and choose pieces straight from the shelves.</p>
<div style="margin-top: 12px; height: 260px; border-radius: 12px; background: #e6dccd"></div>
</div>
{form}
</div>
<div aria-hidden="true" style="position: absolute; left: 0; right: 0; top: 900px; border-top: 1.18px dashed rgba(47,128,237,0.35)"></div>
</div>
</div>

'''
S.cut('<!-- page frame', '<!-- vertical scroll indicator', page_new)

# ── tool variants flyout (Form) ──
item = lambda ic, n, k, d, on=False: (f'<button role="menuitemradio" aria-checked="{str(on).lower()}" style="width: 100%; min-height: 36px; display: flex; align-items: center; gap: 8px; padding: 3px 8px; box-sizing: border-box; border-radius: 3px; {"background: #323232;" if on else ""}">'
    f'<span style="width: 12px">{icon("check", 12) if on else ""}</span>{icon(ic, 16, "#e8e8e8" if on else "#a8a8a8")}'
    f'<span style="flex: 1; text-align: left"><span style="display: block">{n}</span><span style="display: block; font-size: 10px; line-height: 14px; color: #939393">{d}</span></span><span style="font-size: 11px; color: #939393; font-family: {MONO}">{k}</span></button>')
fly = f'''<div role="menu" aria-label="Form tool variants" style="position: absolute; left: 46px; top: 360px; width: 272px; padding: 4px; box-sizing: border-box; border-radius: 4px; {FLOAT} z-index: 20">
{item('t-field', 'Text field', 'input', 'One line: text, email, phone', True)}{item('textarea', 'Text area', 'textarea', 'Several lines')}{item('dropdown', 'Dropdown', 'select', 'Pick one from a list')}
{item('checkbox', 'Checkbox', 'checkbox', 'On or off')}{item('radio', 'Radio group', 'radio', 'Pick one, all options shown')}{item('label', 'Label', 'label', 'Text tied to a field')}
<div style="height: 1px; background: #3a3a3a; margin: 4px 0"></div>{item('form', 'Form', 'form', 'Container that sends the fields')}
<div style="padding: 2px 8px 4px; font-size: 10px; line-height: 14px; color: #939393">Outside a form, the first field also makes one.</div></div>'''

# ── options bar ──
lab_ = lambda t: f'<span style="font-size: 11px; color: #939393; padding: 0 4px 0 8px; white-space: nowrap">{t}</span>'
tog = lambda ic, t, on: f'<button aria-pressed="{str(on).lower()}" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; white-space: nowrap; {"background: rgba(47,128,237,0.18); color: #a9c8f7;" if on else "color: #a8a8a8;"}">{icon(ic, 13)}{t}</button>'
opts = (cap(icon('t-field', 13, '#e8e8e8') + '<span style="padding: 0 6px; font-weight: 500">Text field</span>' + icon('chev-down', 10, '#939393', 1.75), 'padding: 0 8px')
        + cap(lab_('Type') + '<span style="padding: 0 6px">Phone <span style="font-family: ' + MONO + '; font-size: 10px; color: #939393">tel</span></span>' + icon('chev-down', 10, '#939393', 1.75))
        + cap(tog('label', 'With label', True) + capdiv() + tog('keep', 'Keep tool', True))
        + '<span style="font-size: 11px; color: #939393; white-space: nowrap; padding-left: 4px">Click in a form to add · fields line up with the ones around them</span>')
options_left(S, opts)

# ── layers ──
fr = lambda pad, ic, n, t, sel=False, badge='': (pad, None, ic, n, t, sel, (14, 26), badge)
rows = [(8, 'open', 't-section', 'Header', 'header', False, (), ''), (8, 'open', 't-section', 'Visit', 'section', False, (), ''),
        (20, 'closed', 't-stack', 'Intro', 'div', False, (14,), ''), (20, 'open', 'form', 'Booking form', 'form', False, (14,), ''),
        fr(32, 't-field', 'Your name', 'input'), fr(32, 't-field', 'Email', 'input'),
        (32, None, 't-field', 'Phone', 'input', False, (14, 26), '<span style="margin-left: 6px; font-size: 10px; color: #a9c8f7">adding</span>'),
        fr(32, 'dropdown', 'Day', 'select'), fr(32, 'textarea', 'Anything we should know?', 'textarea'), fr(32, 'checkbox', 'Studio letter', 'checkbox'), fr(32, 't-button', 'Request a visit', 'button'),
        (8, 'closed', 't-section', 'Footer', 'footer', False, (), '')]
set_tree(S, rows)
S.s = S.s.replace('<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 32px; ', '<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 4px; padding: 0 12px 0 32px; ', 1)
S.rep('<span style="color: #e8e8e8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">Phone</span>', '<span style="color: #a9c8f7; font-style: italic; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">Phone</span>')

# ── properties: the next field ──
small = lambda t: f'<span style="font-size: 11px; color: #939393">{t}</span>'
row2 = lambda l, c: f'<div style="display: grid; grid-template-columns: 84px minmax(0, 1fr); gap: 8px; align-items: center"><span style="font-size: 11px; color: #a8a8a8">{l}</span>{c}</div>'
sw_ = lambda on: f'<span role="switch" aria-checked="{str(on).lower()}" style="position: relative; width: 24px; height: 14px; flex: none; border-radius: 7px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 10px; height: 10px; border-radius: 5px; background: {"#fff" if on else "#a8a8a8"}"></span></span>'
dd = lambda v, sub='': f('<span style="flex: 1">' + v + '</span>' + (f'<span style="font-family: {MONO}; font-size: 10px; color: #939393">{sub}</span>' if sub else '') + icon('chev-down', 10, '#939393', 1.75))
hdr = f'''<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{icon('t-field', 16, '#a9c8f7')}<span style="flex: 1; font-weight: 500">Next field</span><button style="height: 22px; padding: 0 6px; border-radius: 3px; font-size: 11px; color: #a8a8a8">Reset</button></div>
<div style="padding-left: 24px; font-size: 11px; color: #939393">Into Booking form · after Email</div></div>'''
fieldg = (row2('Label', f('<span style="flex: 1">Phone</span>', 'box-shadow: inset 0 0 0 1px #2f80ed'))
          + row2('Type', dd('Phone', 'tel')) + row2('Placeholder', f('<span style="flex: 1; color: #939393">+47 …</span>'))
          + row2('Help text', f('<span style="flex: 1; color: #939393">Only if the day moves</span>'))
          + row2('Required', '<div style="display: flex; align-items: center; gap: 8px">' + sw_(False) + small('Optional fields say “optional”') + '</div>'))
datag = (row2('Name', f(f'<span style="flex: 1; font-family: {MONO}; font-size: 11px">phone</span><span style="font-size: 10px; color: #939393">from label</span>'))
         + row2('Autofill', dd('Phone number', 'tel'))
         + row2('Check', dd('Phone format')))
look = ('<div style="display: flex; align-items: center; gap: 8px; padding: 6px 8px; border-radius: 4px; background: #2a2a2a"><span style="flex: 1; font-size: 11px; color: #c8c8c8">Matches the fields around it</span>' + small('Form field · Halden') + '</div>')
S.props(panel(hdr + group('Field', fieldg) + group('Data', datag) + group('Look', look)
              + more([mp('States', 'focus, error, disabled'), mp('Accessibility', 'label tied'), mp('Size', 'Fill width')])))

# ── INSET: the form's own settings (select the form) ──
seg_ = lambda items, sel: '<div style="display: grid; grid-template-columns: repeat(' + str(len(items)) + ', minmax(0, 1fr)); gap: 2px; padding: 2px; background: #1f1f1f; border-radius: 4px; font-size: 11px">' + ''.join(f'<button style="height: 22px; border-radius: 3px; white-space: nowrap; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #a8a8a8;"}">{t}</button>' for i, t in enumerate(items)) + '</div>'
st = lambda n, look, c='#1d1a16': f'<div style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 10px; color: #939393">{n}</span><span style="height: 26px; display: flex; align-items: center; padding: 0 8px; border-radius: 5px; background: #fbf8f3; font-size: 11px; color: {c}; {look}">+47 912 34 567</span></div>'
states = ('<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; padding: 10px; border-radius: 4px; background: #f6f1ea">'
          + st('Rest', 'box-shadow: inset 0 0 0 1px #d9cbb7') + st('Focus', 'box-shadow: inset 0 0 0 2px #1d1a16') + st('Error', 'box-shadow: inset 0 0 0 2px #b42318', '#b42318') + st('Disabled', 'box-shadow: inset 0 0 0 1px #e2d8c8; opacity: 0.55') + '</div>')
inset = f'''<!-- INSET: Form settings -->
<div style="position: absolute; left: 330px; bottom: 44px; width: 560px; display: flex; flex-direction: column; gap: 8px; z-index: 35">
<span style="width: max-content; height: 20px; display: flex; align-items: center; padding: 0 8px; border-radius: 3px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; color: #a8a8a8">Inset · Booking form selected → Properties › Form</span>
<div style="padding: 12px; display: flex; flex-direction: column; gap: 10px; {POP}">
<div style="display: flex; align-items: center; gap: 8px"><span style="font-weight: 600">When someone sends it</span><span style="flex: 1"></span><span style="font-size: 11px; color: #939393">6 fields · 2 required</span></div>
{seg_(['Email it to me', 'Send to a web address', 'Design only'], 0)}
<div style="display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 8px">{f('<span style="font-size: 11px; color: #939393">To</span><span style="flex: 1">studio@halden.studio</span>')}{f('<span style="font-size: 11px; color: #939393">Subject</span><span style="flex: 1">Visit request · {{Your name}}</span>')}</div>
<div style="display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 8px">{f('<span style="font-size: 11px; color: #939393">After</span><span style="flex: 1">Show a thank-you message</span>' + icon('chev-down', 10, '#939393', 1.75))}{f('<span style="flex: 1">Spam check</span>' + small('hidden field') + sw_(True))}</div>
<div style="font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393">FIELD STATES · FROM THE DESIGN SYSTEM</div>{states}
</div></div>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', fly + '\n' + inset + '\n<!-- ═══════════ TOP BAR v3')
S.status(['Page', 'Section · Visit', 'Form · Booking form'], 'Click to add after Email · Alt adds without a label · Esc cancels', 'x 1012 &#160;y 402')
S.save('D42-Form.dc.html')
print('ok')
