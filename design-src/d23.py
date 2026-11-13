from screen import *
_src = open('/home/claude/ds/layoutadv.py').read()
LA = {}
exec(_src[:_src.index('# ═════ A · ROW')], LA)
L = LA
P['menu3'] = ('stroke', 'M2.5 4h11M2.5 8h11M2.5 12h11')

S = Screen('Daisy · D-23 Responsive: Mobile, Visibility, Screen sizes')
RESP, RESPS = '#d29922', 'rgba(210,153,34,0.14)'

# ---------------- canvas: the page at Mobile 390, 100% ----------------
src = S.s
a = src.index('<div style="justify-self: end; width: 580px; height: 520px'); b = src.index('</svg>', a) + 6
art = src[a:b]
art = art[art.index('<svg'):].replace('<svg width="580" height="520" viewBox="0 0 580 520"', '<svg width="100%" height="100%" viewBox="40 80 500 320" preserveAspectRatio="xMidYMid slice"')
page = f'''<!-- page frame: Mobile 390 @ 100% -->
<span style="position: absolute; left: 60px; top: 13px; display: flex; align-items: center; gap: 6px; font-size: 11px; line-height: 11px; color: #939393">{icon('phone', 12, RESP)}Mobile · 390 · applies up to 640</span>
<div style="position: absolute; left: 60px; top: 32px; bottom: 0; width: 390px; overflow: hidden; outline: 1px solid #3c3c3c; background: #f6f1ea">
<div style="position: relative; width: 390px; background: #f6f1ea; color: #1d1a16; font-family: 'Inter', sans-serif; font-size: 16px; line-height: 1.5">
<div style="position: relative; height: 64px; box-sizing: border-box; padding: 0 20px; display: flex; align-items: center; justify-content: space-between">
<p style="margin: 0; font-family: 'Fraunces', serif; font-size: 22px; font-weight: 600; line-height: 1">Halden</p>
<span aria-hidden="true" style="position: absolute; left: 100px; top: 19px; height: 26px; padding: 0 6px; display: flex; align-items: center; gap: 5px; border: 1.5px dashed #2f80ed; border-radius: 3px; background: rgba(47,128,237,0.08); color: #1f5fb5; font: 500 10px/1 'Inter', sans-serif; white-space: nowrap">{icon('eye-off', 11, '#1f5fb5')}Nav links hidden</span>
<a href="#visit" style="background: #b5532d; color: #ffffff; border-radius: 999px; padding: 8px 14px; font-size: 13px; font-weight: 500; line-height: 18px">Book a visit</a></div>
<div style="padding: 24px 20px 40px; display: flex; flex-direction: column; gap: 18px">
<p style="margin: 0; font-size: 12px; line-height: 18px; text-transform: uppercase; letter-spacing: 0.08em; color: #5f6b4e; font-weight: 500">Small-batch stoneware · Est. 2014</p>
<h1 style="margin: 0; font-family: 'Fraunces', serif; font-size: 48px; line-height: 1.05; font-weight: 600">Hand-thrown ceramics for everyday tables</h1>
<p style="margin: 0; font-size: 16px; line-height: 1.6; color: #4a443c">Each piece is wheel-thrown, glazed and fired in our studio by the river. Made slowly, used daily.</p>
<div style="display: flex; flex-direction: column; align-items: flex-start; gap: 14px"><a href="#shop" style="background: #b5532d; color: #ffffff; border-radius: 999px; padding: 12px 22px; font-size: 15px; font-weight: 500; line-height: 20px">Shop the collection</a><a href="#process" style="font-size: 15px; font-weight: 500">Our process →</a></div>
<div style="height: 200px; border-radius: 12px; overflow: hidden; background: #e6dccd">{art}</div></div>
<div style="padding: 36px 20px; background: #e7d9c7"><h2 style="margin: 0 0 16px; font-family: 'Fraunces', serif; font-size: 28px; line-height: 1.2; font-weight: 600">This season</h2>
<div style="background: #ffffff; border-radius: 12px; padding: 14px"><div style="aspect-ratio: 4 / 3; border-radius: 8px; background: #d8cbb8"></div></div></div>
</div></div>
'''
a = src.index('<span style="position: absolute; left: 46px; top: 13px; font-size: 11px; line-height: 11px; color: #939393">Desktop · 1440</span>')
b = src.index('<!-- vertical scroll indicator -->', src.index('<span aria-hidden="true" style="position: absolute; right: 54px; top: 800px;'))
S.s = src[:a] + page + src[b:]
S.s = S.s.replace('@ 85%', '@ 100%', 1)
S.rep('>85%<', '>100%<')
S.rep('1440 × 2050', '390 × 3120')
sw_old = S.s[S.s.index('<div role="group" aria-label="Screen size"'):S.s.index('<span style="width: 1px; height: 14px; background: #2e2e2e; margin: 0 2px"></span>', S.s.index('<div role="group" aria-label="Screen size"'))]
sw_new = (f'<div role="group" aria-label="Screen size" style="height: 28px; display: flex; align-items: center; gap: 2px; padding: 2px; box-sizing: border-box; background: #232323; border-radius: 6px">\n'
          f'<button aria-label="Desktop 1440" style="width: 32px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #939393">{icon("desktop", 14)}</button>\n'
          f'<button aria-label="Tablet 768" style="width: 32px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #939393">{icon("tablet", 14)}</button>\n'
          f'<button aria-pressed="true" style="height: 24px; display: flex; align-items: center; gap: 8px; padding: 0 10px; border-radius: 4px; background: #333333; color: #e8e8e8">{icon("phone", 14, RESP)}<span style="font-weight: 500">Mobile</span><span style="font-size: 11px; color: #a8a8a8; font-variant-numeric: tabular-nums">390</span></button>\n')
S.s = S.s.replace(sw_old, sw_new, 1)

chip = (f'<span style="height: 22px; display: flex; align-items: center; gap: 6px; padding: 0 4px 0 9px; border-radius: 11px; background: {RESPS}; color: #f0c56a; font-size: 11px; font-weight: 500; white-space: nowrap">'
        f'{icon("phone", 12, RESP, 1.5)}Editing: Mobile<button aria-label="Back to Desktop" style="width: 16px; height: 16px; display: flex; align-items: center; justify-content: center; border-radius: 8px; color: #f0c56a">{icon("close", 10)}</button></span>')
S.options('—', '—', '—', 'Fit', '—', 'Fit')
S.rep('<!-- position + size capsule -->', chip + '\n<!-- position + size capsule -->')

# ---------------- layers: Nav links selected, dimmed with eye-off ----------------
pb = icon('phone', 12, RESP, 1.25, 'Overrides at Mobile')
rows = []
for r in hero_tree('Nav links'):
    r = list(r)
    if r[3] == 'Nav links':
        r[7] = pb
    if r[3] in ('Hero grid', 'Hero title'):
        r[7] = icon('tablet', 12, RESP, 1.25, 'Overrides at Tablet')
    rows.append(tuple(r))
set_tree(S, rows)
S.rep('<span style="color: #e8e8e8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">Nav links</span>',
      f'<span style="color: #939393; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; text-decoration: line-through; text-decoration-color: #6b6b6b">Nav links</span>{icon("eye-off", 12, "#939393", 1.25, "Hidden on Mobile")}')

# ---------------- properties ----------------
strip = f'''<div style="padding: 8px 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #303030; background: #232323">
{icon('phone', 14, RESP, 1.5)}<span style="flex: 1; font-size: 11px; color: #c8c8c8">Mobile<span style="color: #939393"> · 1 value set here</span></span><button style="font-size: 11px; color: #a9c8f7">Show only these</button></div>'''
dev = lambda ic, n, on: (f'<button aria-pressed="{str(on).lower()}" aria-label="{n}: {"shown" if on else "hidden"}" style="height: 44px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; border-radius: 4px; font-size: 10px; '
                         f'{"background: #333333; color: #e8e8e8;" if on else "background: transparent; color: #939393; box-shadow: inset 0 0 0 1px #2f80ed;"}">{icon(ic, 16)}<span style="display: flex; align-items: center; gap: 3px">{"" if on else icon("eye-off", 10)}{n}</span></button>')
vis = (f'<div role="group" aria-label="Show on" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 4px; padding: 2px; background: #262626; border-radius: 4px">{dev("desktop", "Desktop", True)}{dev("tablet", "Tablet", True)}{dev("phone", "Mobile", False)}</div>'
       + f'<div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a8a8a8">{DOT}<span>Hidden at 640 px and smaller</span><span style="flex: 1"></span><span style="font-family: {MONO}; font-size: 10px; color: #939393">display: none</span></div>'
       + f'''<div style="display: flex; align-items: flex-start; gap: 8px; padding: 8px; border-radius: 4px; background: rgba(47,128,237,0.10); box-shadow: inset 0 0 0 1px rgba(47,128,237,0.4)">
<span style="margin-top: 1px">{icon('info', 12, '#58a6ff', 1.25)}</span><span style="flex: 1; font-size: 11px; line-height: 16px; color: #c8c8c8">The site has no way to reach these links on Mobile.<span style="display: block; margin-top: 6px"><button style="height: 22px; padding: 0 8px; border-radius: 4px; background: #246bcb; color: #fff; font-size: 11px; font-weight: 500">Add a menu button</button></span></span></div>''')
press = f'<button aria-label="Visibility · Advanced" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; color: #939393">{icon("sliders", 14)}</button>'
vis_grp = f'<div style="padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 8px"><div style="height: 28px; margin-bottom: -4px; display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">Visibility</span>{press}</div>{vis}</div><div style="height: 1px; background: #303030"></div>'
S.props(panel(header('t-row', 'Nav links', 'Row', 'nav') + strip + vis_grp
              + group('Layout', seg([icon('t-stack', 12) + 'Stack', icon('t-row', 12) + 'Row', icon('t-grid', 12) + 'Grid'], 1) + f(f'<span style="width: 5px; height: 5px; box-sizing: border-box; border-radius: 3px; border: 1px solid #8a8a8a; flex: none"></span><span style="font-size: 11px; color: #939393">Gap</span><span style="flex: 1; color: #a8a8a8">32</span><span style="font-size: 10px; color: #939393">px</span>'))
              + more([mp('Size', 'Fit'), mp('Placement', 'In flow'), mp('Spacing', '0'), mp('Typography', 'Inter 15'), mp('Accessibility', 'Navigation landmark')])))

# ---------------- inset: Screen sizes dialog ----------------
def srow(ic, name, up, canvas, on=False, base=False):
    cell = lambda v, w='', mono=False: f'<span style="height: 26px; {f"width: {w}px;" if w else "flex: 1;"} display: flex; align-items: center; padding: 0 8px; box-sizing: border-box; background: #2a2a2a; border-radius: 2px; {"font-family: " + MONO + "; font-size: 11px;" if mono else ""} {"color: #939393;" if base and v.startswith("—") else ""}">{v}</span>'
    return (f'<div style="display: grid; grid-template-columns: 44px minmax(0, 1fr) 132px 96px 24px; gap: 8px; align-items: center; padding: 6px 8px; border-radius: 4px; {"background: rgba(47,128,237,0.12); box-shadow: inset 0 0 0 1px #2f80ed;" if on else ""}">'
            f'<button aria-label="Icon" style="height: 26px; display: flex; align-items: center; justify-content: center; gap: 2px; background: #2a2a2a; border-radius: 2px; color: {RESP if on else "#a8a8a8"}">{icon(ic, 14)}{icon("chev-down", 8, "#939393", 1.75)}</button>'
            f'{cell(name)}{cell(up)}{cell(canvas)}'
            f'<button aria-label="More" style="height: 24px; display: flex; align-items: center; justify-content: center; color: #939393">{icon("more", 14)}</button></div>')
sw = lambda on: f'<button role="switch" aria-checked="{str(on).lower()}" style="position: relative; width: 28px; height: 16px; border-radius: 8px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {"#fff" if on else "#a8a8a8"}"></span></button>'
hd = lambda t: f'<span style="font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393">{t}</span>'
chipb = lambda t: f'<button style="height: 22px; padding: 0 8px; border-radius: 11px; background: #2a2a2a; font-size: 11px; color: #c8c8c8">{t}</button>'
dialog = f'''<!-- INSET: Screen sizes dialog -->
<div aria-label="Inset: Screen sizes dialog" style="position: absolute; left: 500px; top: 120px; width: 600px; padding: 12px; box-sizing: border-box; background: #1f1f1f; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 8px 24px rgba(0,0,0,0.45); z-index: 10">
<div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 11px"><span style="font-weight: 600">Inset · Screen sizes dialog</span><span style="color: #939393">from + in the screen-size switcher · Page settings › Screen sizes</span></div>
<div role="dialog" aria-label="Screen sizes" style="width: 560px; margin: 0 auto; box-sizing: border-box; background: #262626; border: 1px solid #454545; border-radius: 8px; box-shadow: 0 16px 40px rgba(0,0,0,0.5)">
<div style="height: 48px; padding: 0 12px 0 16px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a"><span style="font-size: 14px; font-weight: 600">Screen sizes</span><span style="flex: 1; font-size: 11px; color: #939393">Halden · all pages</span>{icon('close', 14, '#a8a8a8')}</div>
<div style="padding: 12px 16px; display: flex; flex-direction: column; gap: 4px">
<div style="display: grid; grid-template-columns: 44px minmax(0, 1fr) 132px 96px 24px; gap: 8px; padding: 0 8px 2px">{hd('ICON')}{hd('NAME')}{hd('APPLIES UP TO')}{hd('CANVAS')}<span></span></div>
{srow('desktop', 'Desktop', '— base, above 1024', '1440 px', base=True)}
{srow('tablet', 'Tablet', '≤ 1024 px', '768 px')}
{srow('phone', 'Mobile', '≤ 640 px', '390 px', on=True)}
<button style="height: 28px; align-self: flex-start; margin-top: 4px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; background: #2a2a2a; font-size: 12px; color: #c8c8c8">{icon('plus', 12)}Add screen size</button>
<div style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap; font-size: 11px; color: #939393"><span>Common:</span>{chipb('Wide 1920')}{chipb('Laptop 1280')}{chipb('iPad 834')}{chipb('Phone 375')}</div>
<div style="height: 1px; background: #333333; margin: 8px 0 4px"></div>
<div style="display: flex; align-items: center; gap: 12px"><span style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span>Mobile-first</span><span style="font-size: 11px; line-height: 16px; color: #939393">Off: Desktop is the base and smaller sizes change it (<span style="font-family: {MONO}">max-width</span>). On: Mobile is the base and bigger sizes change it (<span style="font-family: {MONO}">min-width</span>).</span></span>{sw(False)}</div>
<div style="font-size: 11px; color: #939393">Changing a size moves every value set for it · 14 values use Tablet, 6 use Mobile.</div>
</div>
<div style="height: 52px; padding: 0 16px; display: flex; align-items: center; justify-content: flex-end; gap: 8px; border-top: 1px solid #3a3a3a">
<button style="height: 28px; padding: 0 14px; border-radius: 6px; color: #c8c8c8; box-shadow: inset 0 0 0 1px #454545">Cancel</button><button style="height: 28px; padding: 0 14px; border-radius: 6px; background: #246bcb; color: #fff; font-weight: 500">Save</button></div>
</div></div>'''
S.rep('<!-- vertical scroll indicator -->', dialog + '\n<!-- vertical scroll indicator -->')

S.status(['Page', 'Header', 'Row · Nav links'], 'Hidden on Mobile · shown as a dashed placeholder while selected · turn Mobile back on in Visibility to show it', 'x 172 &#160;y 32')
S.save('D23-Mobile.dc.html')
print('ok')
