from screen import *
P['shared'] = ('stroke', 'M8 1.8l6.2 6.2L8 14.2 1.8 8z M8 5.2L10.8 8 8 10.8 5.2 8z')
P['detach'] = ('stroke', 'M8 1.8l6.2 6.2L8 14.2 1.8 8zM2 2l12 12')
S = Screen('Daisy · D-53 Shared parts')
S.remove_h1_overlay(); S.remove_parent_outline(); S.unselect_h1_row()
POP = 'background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5);'
SH = lambda s=12, c='#a9c8f7': icon('shared', s, c, 1.4)

# ── canvas: the shared header selected ──
hpos = ['left: -5.6px; top: -5.6px', 'right: -5.6px; top: -5.6px', 'right: -5.6px; bottom: -5.6px', 'left: -5.6px; bottom: -5.6px']
handles = ''.join(f'<span style="position: absolute; {p}; width: 9.4px; height: 9.4px; box-sizing: border-box; background: #fff; border: 1.18px solid #2f80ed; border-radius: 1.2px"></span>' for p in hpos)
old = '<!-- Header -->\n<div style="height: 80px; box-sizing: border-box; padding: 0 64px; display: flex; align-items: center; justify-content: space-between">'
i = S.s.index('<!-- page frame'); j = S.s.index(old, i)
S.s = S.s[:j] + ('<!-- Header (shared part) -->\n<div style="position: relative; height: 80px; box-sizing: border-box; padding: 0 64px; display: flex; align-items: center; justify-content: space-between">'
                 f'<span aria-hidden="true" style="position: absolute; inset: 0; border: 1.76px solid #2f80ed; pointer-events: none; background: repeating-linear-gradient(135deg, rgba(47,128,237,0.04) 0 10px, transparent 10px 20px)">{handles}'
                 '<span style="position: absolute; left: 6px; top: calc(100% + 4px); height: 21px; padding: 0 7px; display: flex; align-items: center; gap: 6px; background: #246bcb; color: #fff; font: 500 13px/1 \'Inter\', sans-serif; white-space: nowrap">'
                 + icon('shared', 13, '#fff', 1.6) + 'Site header · shared · 4 pages</span></span>') + S.s[j + len(old):]
S.rep('<a href="#work">Work</a><a href="#shop">Shop</a><a href="#journal">Journal</a><a href="#visit">Visit</a>',
      '<a href="#work">Work</a><a href="#shop">Shop</a><a href="#journal" style="position: relative">Journal<span title="Changed on this page" style="position: absolute; right: -10px; top: -4px; width: 7px; height: 7px; border-radius: 4px; background: #2f80ed; box-shadow: 0 0 0 2px #f6f1ea"></span></a><a href="#visit">Visit</a>')

# mode chip in the options bar
chip = (f'<span style="height: 22px; display: flex; align-items: center; gap: 6px; padding: 0 4px 0 9px; border-radius: 11px; background: rgba(47,128,237,0.14); color: #a9c8f7; font-size: 11px; font-weight: 500; white-space: nowrap">{SH(12)}Shared part · edits apply to 4 pages'
        f'<button aria-label="Change on this page only" style="height: 16px; padding: 0 6px; border-radius: 8px; background: rgba(47,128,237,0.25); color: #d6e6fb; font-size: 10px">This page only</button></span>')
S.options('0', '0', '1440', 'Fill', '80', 'Fit')
S.rep('<!-- position + size capsule -->', chip + '\n<!-- position + size capsule -->')

# ── Project panel: Shared parts group ──
grp = f'''<div role="treeitem" aria-expanded="true" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 20px">{icon('chev-down', 12, '#a8a8a8')}<span style="flex: 1; color: #a8a8a8">Shared parts</span><span style="font-size: 11px; color: #939393">2</span></div>
<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 44px; background: rgba(47,128,237,0.12)">{SH(13, '#a9c8f7')}<span style="flex: 1; color: #e8e8e8">Site header</span><span style="font-size: 11px; color: #939393">4 pages</span></div>
<div role="treeitem" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 44px">{SH(13, '#a8a8a8')}<span style="flex: 1">Site footer</span><span style="font-size: 11px; color: #939393">4 pages</span></div>
'''
k = S.s.index('<div role="treeitem" aria-expanded="false" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px 0 20px">\n<svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="#a8a8a8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 4l4 4-4 4"></path></svg>\n<span style="flex: 1; color: #a8a8a8">Design system</span>')
S.s = S.s[:k] + grp + S.s[k:]

# ── Layers ──
rows = hero_tree()
rows = [tuple(r) for r in rows]
new = []
for r in rows:
    r = list(r)
    if r[3] == 'Header':
        r[2] = 'shared'; r[3] = 'Site header'; r[5] = True; r[7] = '<span style="margin-left: 6px; height: 14px; padding: 0 5px; border-radius: 7px; background: rgba(47,128,237,0.2); color: #a9c8f7; font-size: 10px; line-height: 14px">4</span>'
    if r[3] == 'Nav links':
        r[1] = 'open'
        new.append(tuple(r))
        for n, ov in [('Work', False), ('Shop', False), ('Journal', True), ('Visit', False)]:
            new.append((32, None, 't-link', n, 'a', False, (14, 26), '<span title="Changed on this page" style="margin-left: 6px; width: 6px; height: 6px; border-radius: 3px; background: #2f80ed"></span>' if ov else ''))
        continue
    if r[3] in ('Hero grid', 'Hero text') or r[0] >= 32 and r[3] not in ('Work',):
        if r[0] >= 32: continue
    if r[3] == 'Hero': r[1] = 'closed'
    if r[3] == 'Hero grid': continue
    if r[3] == 'Footer':
        r[2] = 'shared'; r[3] = 'Site footer'; r[7] = '<span style="margin-left: 6px; height: 14px; padding: 0 5px; border-radius: 7px; background: #333333; color: #a8a8a8; font-size: 10px; line-height: 14px">4</span>'
    new.append(tuple(r))
set_tree(S, new)

# ── Properties ──
sm = lambda t, c='#939393': f'<span style="font-size: 11px; color: {c}">{t}</span>'
hdr = f'''<div style="box-sizing: border-box; padding: 10px 12px; border-bottom: 1px solid #303030; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 8px">{SH(16, '#a9c8f7')}<span style="flex: 1; font-weight: 500">Site header</span><button style="height: 22px; display: flex; align-items: center; gap: 4px; padding: 0 6px; color: #a8a8a8">Normal{icon('chev-down', 10, 'currentColor', 1.5)}</button></div>
<div style="padding-left: 24px; font-size: 11px; color: #a8a8a8">Shared part · <span style="font-family: {MONO}; color: #939393">header</span></div></div>'''
seg_ = lambda items, sel: '<div style="display: grid; grid-template-columns: repeat(' + str(len(items)) + ', minmax(0, 1fr)); gap: 2px; padding: 2px; background: #262626; border-radius: 4px; font-size: 11px">' + ''.join(f'<button style="height: 22px; border-radius: 3px; white-space: nowrap; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #939393;"}">{t}</button>' for i, t in enumerate(items)) + '</div>'
pg = lambda n, note='', cur=False: f'<div style="height: 24px; display: flex; align-items: center; gap: 8px">{icon("file", 12, "#a8a8a8")}<span style="{"color: #e8e8e8; font-weight: 500;" if cur else ""}">{n}</span><span style="flex: 1"></span>{sm(note, "#a9c8f7" if "change" in note else "#939393")}</div>'
shared = (sm('Edits apply to') + seg_(['All 4 pages', 'This page only'], 0)
          + '<div style="display: flex; flex-direction: column">' + pg('Home', '1 change here', True) + pg('Shop') + pg('Journal') + pg('Visit') + '</div>')
over = (f'<div style="display: flex; align-items: center; gap: 8px; padding: 6px 8px; border-radius: 4px; background: #2a2a2a"><span style="width: 6px; height: 6px; border-radius: 3px; background: #2f80ed"></span><span style="flex: 1; font-size: 11px">Nav › Journal · text <span style="color: #939393">(shared: “Stories”)</span></span><button style="font-size: 11px; color: #a8a8a8">Reset</button></div>'
        + '<div style="display: flex; gap: 8px"><button style="font-size: 11px; color: #a9c8f7">Apply to all pages</button><span style="flex: 1"></span><button style="font-size: 11px; color: #a8a8a8">Reset all here</button></div>')
acts = f'<div style="display: flex; gap: 6px"><button style="height: 24px; padding: 0 10px; border-radius: 4px; box-shadow: inset 0 0 0 1px #454545; font-size: 11px">Open in its own tab</button><button style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; font-size: 11px; color: #a8a8a8">{icon("detach", 12)}Detach</button></div>'
S.props(panel(hdr + group('Shared part', shared) + group('Changes on this page · 1', over)
              + '<div style="padding: 10px 12px">' + acts + '<div style="margin-top: 6px; font-size: 10px; line-height: 14px; color: #939393">Detach makes this page’s header a normal copy; the other pages keep the shared one.</div></div>'
              + more([mp('Layout', 'Row'), mp('Spacing', '0 64'), mp('Fill', 'none'), mp('Visibility', 'All sizes'), mp('Accessibility', 'Banner')])))

# ── INSET: Make shared (on the footer) ──
chk = lambda on, t, d='': f'<div style="height: 28px; display: flex; align-items: center; gap: 8px"><span style="width: 14px; height: 14px; border-radius: 3px; display: flex; align-items: center; justify-content: center; {"background: #246bcb;" if on else "box-shadow: inset 0 0 0 1px #6b6b6b;"}">{icon("check", 10, "#fff", 2) if on else ""}</span><span>{t}</span><span style="flex: 1"></span><span style="font-size: 11px; color: #939393">{d}</span></div>'
inset = f'''<!-- INSET: Make shared -->
<div style="position: absolute; left: 330px; bottom: 44px; width: 540px; display: flex; flex-direction: column; gap: 8px; z-index: 35">
<span style="width: max-content; height: 20px; display: flex; align-items: center; padding: 0 8px; border-radius: 3px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; color: #a8a8a8">Inset · Footer selected → right-click › Make shared (Ctrl Alt K)</span>
<div style="padding: 14px; display: flex; flex-direction: column; gap: 10px; {POP}">
<div style="display: flex; align-items: center; gap: 8px">{SH(15)}<b style="font-weight: 600">Make the footer a shared part</b></div>
<div style="display: grid; grid-template-columns: 60px minmax(0, 1fr); gap: 8px; align-items: center"><span style="font-size: 11px; color: #939393">Name</span><span style="height: 26px; display: flex; align-items: center; padding: 0 8px; border-radius: 2px; background: #2a2a2a; box-shadow: inset 0 0 0 1px #2f80ed">Site footer</span></div>
<div><span style="font-size: 11px; color: #939393">Use it on</span>{chk(True, 'Home', 'this page')}{chk(True, 'Shop', 'same footer found · will be replaced')}{chk(True, 'Journal', 'similar footer · 2 differences')}{chk(False, 'Visit', 'has its own footer, kept')}</div>
<div style="display: flex; align-items: center; gap: 8px"><span style="font-size: 11px; color: #939393">New pages get it automatically</span><span style="flex: 1"></span><button style="height: 26px; padding: 0 12px; color: #a8a8a8">Cancel</button><button style="height: 26px; padding: 0 12px; border-radius: 4px; background: #246bcb; color: #fff; font-weight: 500">Make shared</button></div></div></div>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', inset + '\n<!-- ═══════════ TOP BAR v3')
S.status(['Page', 'Shared · Site header'], 'Editing the shared header · changes appear on Shop, Journal and Visit too', 'x 640 &#160;y 40')
S.save('D53-SharedParts.dc.html')
print('ok')
