from screen import *
_src = open('/home/claude/ds/layoutadv.py').read()
LA = {}
exec(_src[:_src.index('# ═════ A · ROW')], LA)
L = LA

S = Screen('Daisy · D-18 Elements panel and Place tool')
S.remove_h1_overlay()
S.remove_parent_outline()
set_tool(S, 'Place (N)')
scroll(S, 700)
add_footer(S)

# footer: drop target + vertical insertion line (footer is a Row)
S.rep('<footer style="padding: 48px 64px; background: #1d1a16; color: #f6f1ea; display: flex; align-items: center; justify-content: space-between; font-size: 15px">\n<span>© 2026 Halden Studio</span><span style="color: #e7d9c7">Riverside Works, Unit 4</span>',
      '<footer style="position: relative; padding: 48px 64px; background: #1d1a16; color: #f6f1ea; display: flex; align-items: center; justify-content: space-between; font-size: 15px">\n'
      '<div aria-hidden="true" style="position: absolute; inset: 0; border: 1.18px solid #2f80ed; pointer-events: none"><span style="position: absolute; left: -1px; bottom: calc(100% + 2px); height: 21px; padding: 0 5px; display: flex; align-items: center; background: #246bcb; color: #fff; font: 500 13px/1 \'Inter\', sans-serif">into Footer</span></div>'
      '<span>© 2026 Halden Studio</span><span style="position: relative; color: #e7d9c7">Riverside Works, Unit 4'
      '<span aria-hidden="true" style="position: absolute; right: -150px; top: -14px; width: 2.35px; height: 48px; background: #4b93f1"><span style="position: absolute; left: -2.35px; top: -1.2px; width: 7px; height: 2.35px; background: #4b93f1"></span><span style="position: absolute; left: -2.35px; bottom: -1.2px; width: 7px; height: 2.35px; background: #4b93f1"></span></span>'
      '<span aria-hidden="true" style="position: absolute; left: calc(100% + 196px); top: -22px; width: 118px; padding: 6px 8px; box-sizing: border-box; display: flex; flex-direction: column; gap: 5px; border: 1.18px dashed #4b93f1; background: rgba(75,147,241,0.10); border-radius: 2px">' + ''.join('<span style="display: flex; align-items: center; gap: 6px; font-size: 12px; color: rgba(246,241,234,0.7)"><span style="width: 4px; height: 4px; border-radius: 50%; background: currentColor"></span>List item</span>' for _ in range(3)) + '</span>'
      '<svg aria-hidden="true" width="34" height="34" viewBox="0 0 20 20" style="position: absolute; right: -186px; top: -8px; overflow: visible"><path d="M7 1v5M7 8v5M1 7h5M8 7h5" stroke="#ffffff" stroke-width="1.6"></path><rect x="10" y="10" width="9" height="9" rx="1" fill="#1d1a16" stroke="#ffffff" stroke-width="1" stroke-dasharray="2 1.5"></rect><path d="M14.5 12v5M12 14.5h5" stroke="#ffffff" stroke-width="1.2"></path></svg></span>')
S.rep('<span aria-hidden="true" style="position: absolute; right: 3px; top: 250px;', '<span aria-hidden="true" style="position: absolute; right: 3px; top: 420px;')

# left dock: Elements tab
S.rep('<button role="tab" aria-selected="true" style="position: relative; font-weight: 500; color: #e8e8e8">Layers<span style="position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: #2f80ed"></span></button>\n<button role="tab" aria-selected="false" style="font-weight: 500; color: #a8a8a8">Elements</button>',
      '<button role="tab" aria-selected="false" style="font-weight: 500; color: #a8a8a8">Layers</button>\n<button role="tab" aria-selected="true" style="position: relative; font-weight: 500; color: #e8e8e8">Elements<span style="position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: #2f80ed"></span></button>')
er = lambda ic, name, tag, note='', armed=False: (f'<button style="width: 100%; height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 12px; box-sizing: border-box; {"background: rgba(47,128,237,0.18); box-shadow: inset 2px 0 0 #2f80ed;" if armed else ""}">'
                                                  f'{icon(ic, 16, "#e8e8e8" if armed else "#a8a8a8")}<span style="color: #e8e8e8">{name}</span>'
                                                  + (f'<span style="font-size: 11px; color: {"#a9c8f7" if armed else "#939393"}">{note}</span>' if note else '')
                                                  + f'<span style="flex: 1"></span><span style="font-family: {MONO}; font-size: 11px; color: #939393">{tag}</span></button>')
cat = lambda n, c, open_=False: f'<div style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px; color: #a8a8a8">{icon("chev-down" if open_ else "chev-right", 12)}<span style="flex: 1; font-size: 11px; font-weight: 500">{n}</span><span style="font-size: 11px; color: #939393">{c}</span></div>'
panel_html = f'''<div style="padding: 8px 12px 6px">
<label style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 4px 0 6px; box-sizing: border-box; background: #2a2a2a; border-radius: 2px; box-shadow: inset 0 0 0 1px #2f80ed">{icon('search', 12, '#939393', 1.75)}<span style="flex: 1">list</span><span style="width: 1px; height: 14px; background: #e8e8e8"></span><button aria-label="Clear search" style="width: 18px; height: 18px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon('close', 10, 'currentColor', 1.75)}</button></label>
</div>
<div style="padding: 2px 12px 6px; font-size: 10px; line-height: 14px; color: #939393">3 matches · click to arm the Place tool, drag onto the page, or double-click to insert after the selection</div>
{cat('Lists', 3, True)}
{er('t-list', 'Bulleted list', 'ul', '· 3 items', True)}
{er('t-list', 'Numbered list', 'ol', '· 3 items')}
{er('t-table', 'Description list', 'dl', '· 2 pairs')}
<div style="height: 1px; background: #262626; margin: 6px 12px"></div>
<div style="padding: 0 12px 4px; font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393">ALSO MATCHES</div>
{er('t-row', 'Navigation', 'nav', '· links in a list')}
<div style="height: 1px; background: #262626; margin: 6px 12px"></div>
{cat('Structure', 9)}{cat('Text', 8)}{cat('Media', 6)}{cat('Links &amp; buttons', 3)}{cat('Tables', 2)}{cat('Forms', 9)}{cat('Embeds', 3)}{cat('Custom', 0)}
'''
S.cut('<div style="display: flex; gap: 4px; padding: 8px 12px 4px">', '</aside>', panel_html)

olab = lambda t: f'<span style="font-size: 11px; color: #939393; padding: 0 4px 0 8px; white-space: nowrap">{t}</span>'
sb = lambda t, on=False: f'<button aria-pressed="{str(on).lower()}" style="height: 24px; display: flex; align-items: center; padding: 0 8px; border-radius: 4px; white-space: nowrap; {"background: #333333; color: #e8e8e8; font-weight: 500;" if on else "color: #939393;"}">{t}</button>'
tog = lambda t, on: f'<button aria-pressed="{str(on).lower()}" style="height: 24px; display: flex; align-items: center; padding: 0 8px; border-radius: 4px; white-space: nowrap; {"background: rgba(47,128,237,0.18); color: #a9c8f7;" if on else "color: #a8a8a8;"}">{t}</button>'
opts = (capseg([icon('flow', 12) + 'In flow', icon('free', 12) + 'Free'], 0)
        + cap(olab('After placing') + sb('Select it', True) + sb('Stay armed'))
        + cap(tog('Show preview', True) + tog('Only valid spots', True))
        + '<span style="font-size: 11px; color: #939393; white-space: nowrap; padding-left: 4px">Element settings: in Properties</span>')
options_left(S, opts)

S.props(panel(f'''<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{icon('t-list', 16, '#a8a8a8')}<span style="flex: 1; font-weight: 500">Bulleted list</span><span style="font-family: {MONO}; font-size: 11px; color: #939393">ul</span></div>
<div style="padding-left: 24px; font-size: 11px; color: #939393">Armed · what you place gets these settings</div></div>'''
              + group('What gets created', pair(f('<span style="font-size: 11px; color: #939393">Items</span><span style="flex: 1; text-align: right">3</span>'), f('<span style="font-size: 11px; color: #939393">Marker</span><span style="flex: 1; text-align: right">Disc</span>' + icon('chev-down', 10, '#939393', 1.5)))
                      + f('<span style="font-size: 11px; color: #939393">Item text</span><span style="flex: 1; text-align: right; color: #939393">List item</span>')
                      + '<div style="font-size: 11px; line-height: 16px; color: #939393">The smallest valid structure. Text style comes from Halden · Body. Plain, Links or Inline row: in the element card.</div>')
              + '<div style="padding: 8px 12px; font-size: 11px; line-height: 16px; color: #939393">Tag, where it goes, wrapping, every match, accessible name, id, class and style: Advanced</div>'))

# Element info popover beside the Elements panel
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
var = lambda t, on=False: f'<button aria-pressed="{str(on).lower()}" style="flex: 1; display: flex; flex-direction: column; gap: 4px; padding: 6px; border-radius: 4px; text-align: left; {"background: rgba(47,128,237,0.14); box-shadow: inset 0 0 0 1px #2f80ed;" if on else "background: #2a2a2a;"}">{t}</button>'
dots = lambda n, row=False, link=False: (f'<span style="display: flex; {"flex-direction: row; gap: 8px" if row else "flex-direction: column; gap: 3px"}">' + ''.join(f'<span style="display: flex; align-items: center; gap: 4px"><span style="width: 3px; height: 3px; border-radius: 50%; background: #a8a8a8"></span><span style="width: {18 if row else 34}px; height: 3px; border-radius: 1px; background: {"#4b93f1" if link else "#6b6b6b"}"></span></span>' for _ in range(n)) + '</span>')
pop = f'''<!-- POPOVER: Element info, beside the Elements panel -->
<section role="dialog" aria-label="Bulleted list" style="position: absolute; left: 312px; top: 336px; width: 320px; box-sizing: border-box; padding: 0 12px 12px; display: flex; flex-direction: column; gap: 9px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); z-index: 30">
<span aria-hidden="true" style="position: absolute; left: -6px; top: 188px; width: 10px; height: 10px; background: #262626; border-left: 1px solid #454545; border-bottom: 1px solid #454545; transform: rotate(45deg)"></span>
<div style="height: 40px; margin: 0 -12px; padding: 0 8px 0 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a">{icon('t-list', 14, '#a8a8a8')}
<span style="font-weight: 600">Bulleted list</span><span style="flex: 1; font-family: {MONO}; font-size: 11px; color: #939393">ul</span>
<button aria-label="Pin open" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #939393">{icon("keep", 14)}</button></div>
<div style="padding: 12px 14px; background: #f6f1ea; border-radius: 3px; color: #1d1a16; font-size: 13px; line-height: 20px"><ul style="margin: 0; padding-left: 18px"><li>Hand-thrown in small batches</li><li>Fired in our riverside kiln</li><li>Safe for dishwasher and oven</li></ul></div>
<div style="font-size: 11px; line-height: 16px; color: #a8a8a8">A list where order does not matter. Screen readers announce “list, 3 items”.</div>
{L['lab']('Starts as')}
<div style="display: flex; gap: 6px">{var(dots(3) + '<span style="font-size: 10px; color: #c8c8c8">Plain</span>', True)}{var(dots(3, link=True) + '<span style="font-size: 10px; color: #c8c8c8">Links</span>')}{var(dots(3, row=True) + '<span style="font-size: 10px; color: #c8c8c8">Inline row</span>')}</div>
<div style="display: flex; align-items: flex-start; gap: 6px; padding: 8px; background: #1f1f1f; border-radius: 4px; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; line-height: 16px"><span style="margin-top: 2px">{icon('check', 12, '#3fb950', 2)}</span><span style="color: #c8c8c8">Fits in <b style="font-weight: 600; color: #e8e8e8">Footer</b>. Footer is a Row, so the list sits beside the address as one item.</span></div>
<code style="font-family: {MONO}; font-size: 11px; line-height: 16px; color: #939393">&lt;ul&gt; &lt;li&gt;…&lt;/li&gt; ×3 &lt;/ul&gt;</code>
<div style="display: flex; gap: 6px; align-items: center"><span style="flex: 1"></span><span style="font-size: 10px; color: #939393">Enter places after the selection</span></div>
</section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', pop + '\n<!-- ═══════════ TOP BAR v3')
exec(open('/home/claude/ds/d18_adv.py').read())
S.status(['Page', 'Footer'], 'Click to place Bulleted list after “Riverside Works, Unit 4” · Alt to place Free · Esc disarms', 'x 1130 &#160;y 1678')
S.save('D18-Elements.dc.html')
print('ok')
