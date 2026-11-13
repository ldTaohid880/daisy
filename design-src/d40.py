from screen import *
P['history'] = ('stroke', 'M3 8a5 5 0 1 0 1.5-3.5M3 2.5v3h3M8 5.5V8l2 1.5')
P['palette'] = ('stroke', 'M8 1.5a6.5 6.5 0 1 0 0 13c1 0 1.5-.6 1.5-1.4 0-1.2-1-1.3-1-2.3 0-.8.6-1.3 1.5-1.3h1.6a2.9 2.9 0 0 0 2.9-2.9C14.5 4 11.6 1.5 8 1.5z')
P['enter'] = ('stroke', 'M13 3v5a2 2 0 0 1-2 2H3M6 7l-3 3 3 3')
S = Screen('Daisy · D-40 Search results')
POP = 'background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5);'
kb = lambda t: f'<span style="height: 18px; box-sizing: border-box; display: inline-flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #2a2a2a; box-shadow: inset 0 -1px 0 #3a3a3a; font-size: 10px; font-weight: 500; color: #a8a8a8">{t}</span>'
hl = lambda t, q='Shop': t.replace(q, f'<b style="font-weight: 600; color: #e8e8e8; background: rgba(47,128,237,0.25); border-radius: 2px">{q}</b>', 1)

# ── search field, focused, with the query ──
a = S.s.index('<!-- centre: search / command centre -->'); b = S.s.index('<!-- right: history + run/ship -->')
field = f'''<!-- centre: search / command centre (focused) -->
<div role="combobox" aria-expanded="true" aria-label="Search Halden" style="width: 440px; height: 28px; box-sizing: border-box; display: flex; align-items: center; gap: 8px; padding: 0 6px 0 10px; border-radius: 6px; background: #262626; box-shadow: inset 0 0 0 1px #2f80ed, 0 0 0 3px rgba(47,128,237,0.25)">
{icon('search', 13, '#a8a8a8', 1.75)}<span style="flex: 1; color: #e8e8e8">shop<span style="display: inline-block; width: 1px; height: 13px; margin-left: 1px; vertical-align: -2px; background: #e8e8e8"></span></span>
<span style="font-size: 11px; color: #939393">9 results</span><button aria-label="Clear" style="color: #939393">{icon('close', 11)}</button></div>

'''
S.s = S.s[:a] + field + S.s[b:]

def row(ic, title, sub, right='', on=False, mono_sub=False):
    return (f'<div role="option" aria-selected="{str(on).lower()}" style="height: 32px; display: flex; align-items: center; gap: 10px; padding: 0 10px; border-radius: 4px; {"background: rgba(47,128,237,0.18);" if on else ""}">'
            f'{ic}<span style="min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; color: #c8c8c8">{title}</span>'
            f'<span style="flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-size: 11px; color: #939393; {"font-family: " + MONO + ";" if mono_sub else ""}">{sub}</span>'
            f'<span style="flex: none; font-size: 11px; color: #939393">{right}</span>{icon("enter", 12, "#a9c8f7") if on else ""}</div>')
grp = lambda t, n, more='': f'<div style="height: 24px; display: flex; align-items: center; gap: 8px; padding: 6px 10px 0"><span style="font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393">{t}</span><span style="font-size: 10px; color: #6b6b6b">{n}</span><span style="flex: 1"></span>{more}</div>'
ic = lambda n, c='#a8a8a8': icon(n, 14, c)
moreb = lambda t: f'<button style="font-size: 11px; color: #a9c8f7">{t}</button>'
tabs = '<div role="tablist" style="display: flex; gap: 2px; padding: 8px 10px 6px; border-bottom: 1px solid #333333">' + ''.join(
    f'<button role="tab" aria-selected="{str(i == 0).lower()}" style="height: 22px; display: flex; align-items: center; gap: 5px; padding: 0 8px; border-radius: 3px; font-size: 11px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == 0 else "color: #a8a8a8;"}">{t}<span style="color: #939393">{n}</span>{f"<span style=\"font-family: {MONO}; font-size: 10px; color: #6b6b6b\">{k}</span>" if k else ""}</button>'
    for i, (t, n, k) in enumerate([('All', 9, ''), ('Pages', 1, '/'), ('Layers', 5, '@'), ('Tokens', 0, '#'), ('Assets', 2, ''), ('Commands', 1, '>')])) + '</div>'
results = (grp('PAGES', '1') + row(ic('file'), hl('Shop'), 'shop.html', 'open in a tab · unsaved', mono_sub=True)
    + grp('LAYERS · HOME', '3', moreb('All 5')) + row(ic('t-button', '#e8e8e8'), hl('Shop the collection'), 'Hero › Hero text › Hero buttons', 'a', on=True)
    + row(ic('t-link'), hl('Shop'), 'Header › Nav links · links to #shop', 'a') + row(ic('t-link'), 'View all →', 'This season · href “#<b style="font-weight: 600; color: #e8e8e8">shop</b>”', 'a')
    + grp('LAYERS · OTHER PAGES', '2') + row(ic('t-grid'), hl('Shop grid'), 'Shop › Products', 'div') + row(ic('t-heading'), hl('Shop by season', 'Shop'), 'Journal › Feature', 'h2')
    + grp('ASSETS', '2') + row(ic('media'), f'<span style="font-family: {MONO}; font-size: 11px">{hl("shop-hero.jpg", "shop")}</span>', '2400 × 1600 · used on Shop', 'image') + row(ic('media'), f'<span style="font-family: {MONO}; font-size: 11px">{hl("shop-icon.svg", "shop")}</span>', 'not used', 'svg')
    + grp('COMMANDS', '1') + row(ic('external'), f'Export page “{hl("Shop")}”', 'File › Export…', kb('Ctrl') + ' ' + kb('Shift') + ' ' + kb('E')))
# preview of the highlighted result
prev = f'''<aside style="width: 248px; flex: none; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px; border-left: 1px solid #333333; background: #222222">
<div style="height: 92px; display: flex; align-items: center; justify-content: center; border-radius: 4px; background: #f6f1ea"><span style="padding: 10px 20px; border-radius: 999px; background: #b5532d; color: #fff; font-size: 12px; font-weight: 500; outline: 1.5px solid #2f80ed; outline-offset: 3px">Shop the collection</span></div>
<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 600">Shop the collection</span><span style="font-size: 11px; color: #939393">Button · <span style="font-family: {MONO}">a</span> · Home</span></div>
<div style="font-size: 11px; line-height: 16px; color: #a8a8a8">Fill <b style="font-weight: 500; color: #c8c8c8">brand</b> · Text <b style="font-weight: 500; color: #c8c8c8">white</b> · Links to <span style="font-family: {MONO}">#shop</span> · Mouse over state</div>
<div style="display: flex; flex-direction: column; gap: 2px; margin-top: auto">
{''.join(f'<div style="height: 26px; display: flex; align-items: center; gap: 8px; padding: 0 6px; border-radius: 3px; {"background: #333333;" if i == 0 else ""}"><span style="flex: 1">{t}</span><span style="display: flex; gap: 2px">{"".join(kb(k) for k in ks)}</span></div>' for i, (t, ks) in enumerate([('Select on the page', ['Enter']), ('Reveal in Layers', ['Ctrl', 'Enter']), ('Show code', ['Ctrl', '`']), ('Copy CSS', ['Ctrl', 'Alt', 'C'])]))}
</div></aside>'''
foot = f'<div style="height: 32px; display: flex; align-items: center; gap: 14px; padding: 0 12px; border-top: 1px solid #333333; font-size: 11px; color: #939393; white-space: nowrap"><span>{kb("↑")} {kb("↓")} move</span><span>{kb("Enter")} open</span><span>{kb("Tab")} next group</span><span>{kb("Esc")} close</span><span style="flex: 1"></span><span>Type <span style="font-family: {MONO}; color: #c8c8c8">/ @ # &gt;</span> for pages, layers, tokens, commands</span></div>'
panel_ = f'''<!-- SEARCH RESULTS -->
<div role="listbox" aria-label="Search results for shop" style="position: absolute; left: 580px; top: 38px; width: 760px; display: flex; flex-direction: column; {POP} z-index: 40">
{tabs}<div style="display: flex; min-height: 0"><div style="flex: 1; min-width: 0; padding: 0 6px 8px">{results}</div>{prev}</div>{foot}</div>'''

# command mode inset
cmd_rows = [('code', 'Show code', 'View', ['Ctrl', '`'], True), ('play', 'Show tips again', 'Help', [], False), ('measure', 'Show rulers', 'View', ['Ctrl', 'R'], False), ('eye', 'Show hidden layers', 'Layers', [], False), ('history', 'Show history', 'Edit', [], False)]
cmd = f'''<!-- INSET: command mode -->
<div style="position: absolute; left: 330px; bottom: 44px; width: 460px; display: flex; flex-direction: column; gap: 8px; z-index: 35">
<span style="width: max-content; height: 20px; display: flex; align-items: center; padding: 0 8px; border-radius: 3px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; color: #a8a8a8">Inset · Commands only, typing “&gt; sho”</span>
<div style="{POP}">
<div style="height: 36px; display: flex; align-items: center; gap: 8px; padding: 0 10px; border-bottom: 1px solid #333333"><span style="height: 18px; padding: 0 6px; border-radius: 3px; background: rgba(47,128,237,0.18); color: #a9c8f7; font-size: 11px; line-height: 18px">Commands</span><span style="color: #e8e8e8">sho</span><span style="flex: 1"></span><span style="font-size: 11px; color: #939393">Backspace to leave</span></div>
<div style="padding: 6px">{''.join(row(ic(i), hl(t, "Sho"), m, ' '.join(kb(k) for k in ks), on) for i, t, m, ks, on in cmd_rows)}</div></div></div>'''

S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', panel_ + '\n' + cmd + '\n<!-- ═══════════ TOP BAR v3')
S.save('D40-Search.dc.html')
print('ok')
