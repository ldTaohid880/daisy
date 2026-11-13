import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *
P['type'] = ('stroke', 'M3 4V3h10v1M8 3v10M6 13h4')
P['redirect'] = ('stroke', 'M2 5h8a3 3 0 0 1 0 6H6M9 8l3-3-3-3')
P['devices'] = ('stroke', 'M1.5 3h9v7h-9zM4 12.5h4M12 6h2.5v7.5H12z')
P['grip2'] = ('fill', 'M6 4h1.5v1.5H6zM8.5 4H10v1.5H8.5zM6 7.25h1.5v1.5H6zM8.5 7.25H10v1.5H8.5zM6 10.5h1.5V12H6zM8.5 10.5H10V12H8.5z')
M_ = "font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 11px"
cap = lambda t, d: f'<div style="margin-bottom: 10px"><div style="font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{d}</div></div>'
sw = lambda on: f'<span style="display: inline-block; position: relative; width: 28px; height: 16px; flex: none; border-radius: 8px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {"#fff" if on else "#a8a8a8"}"></span></span>'
segm = lambda items, sel: '<div style="display: inline-grid; grid-template-columns: repeat(' + str(len(items)) + ', auto); gap: 2px; padding: 2px; background: #1f1f1f; border-radius: 4px; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px">' + ''.join(f'<button style="height: 24px; padding: 0 10px; white-space: nowrap; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #a8a8a8;"}">{t}</button>' for i, t in enumerate(items)) + '</div>'
fld = lambda inner, w='', focus=False: f'<span style="{w} height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 10px; box-sizing: border-box; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px {"#2f80ed" if focus else "#3a3a3a"}">{inner}</span>'
dd = lambda v, w='width: 200px;': fld(f'<span style="flex: 1">{v}</span>' + icon('chev-down', 10, '#939393', 1.75), w)
row = lambda l, c, d='': f'<div style="display: grid; grid-template-columns: 190px minmax(0, 1fr); gap: 14px; align-items: center; padding: 7px 0"><div style="display: flex; flex-direction: column; gap: 2px"><span>{l}</span>{f"<span style=\"font-size: 11px; line-height: 15px; color: #939393\">{d}</span>" if d else ""}</div><div style="display: flex; align-items: center; gap: 10px; min-width: 0">{c}</div></div>'
TABS = [('gear', 'General'), ('type', 'Fonts'), ('devices', 'Screen sizes'), ('redirect', 'Redirects'), ('code', 'Site-wide code'), ('external', 'Export defaults')]
def panel(cur, title, body, h=420):
    nav = ''.join(f'<div style="height: 30px; display: flex; align-items: center; gap: 9px; padding: 0 10px; border-radius: 5px; {"background: #333333; color: #e8e8e8; font-weight: 500;" if t == cur else "color: #a8a8a8;"}">{icon(ic, 14, "#e8e8e8" if t == cur else "#939393")}{t}</div>' for ic, t in TABS)
    return f'''<div style="width: 880px; height: {h}px; display: flex; border-radius: 8px; overflow: hidden; background: #262626; border: 1px solid #454545; font-size: 12px; line-height: 16px">
<nav style="width: 180px; flex: none; padding: 10px 8px; box-sizing: border-box; display: flex; flex-direction: column; gap: 2px; background: #222222; border-right: 1px solid #3a3a3a">{nav}</nav>
<div style="flex: 1; min-width: 0; padding: 14px 20px; box-sizing: border-box; display: flex; flex-direction: column"><div style="font-size: 14px; font-weight: 600; margin-bottom: 6px">{title}</div>{body}</div></div>'''

# General
gen = (row('Project name', fld('Halden', 'width: 260px;'))
       + row('Site address', fld(f'<span style="{M_}; color: #939393">https://</span><span style="{M_}">halden.studio</span>', 'width: 260px;'), 'Used for links in search and social previews')
       + row('Language', dd('English · en'), 'Pages can override it')
       + row('Home page', dd('Home · index.html'))
       + row('Favicon', f'<span style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 6px; background: #b5532d">{daisy(16).replace("#e8e8e8", "#fff")}</span>{dd("Daisy mark in brand", "width: 220px;")}<button style="font-size: 11px; color: #a9c8f7">Upload…</button>')
       + row('Social image', '<span style="width: 72px; height: 38px; border-radius: 3px; background: #e6dccd"></span><span style="font-size: 11px; color: #939393">Default for pages without their own · 1200 × 630</span>'))
c_gen = panel('General', 'General', gen, 420)

# Screen sizes
def sz(ic, n, w, base, cols, on=True, main=False):
    return (f'<div style="height: 38px; display: grid; grid-template-columns: 14px 20px 190px 90px minmax(0, 1fr) 40px; align-items: center; gap: 10px; padding: 0 10px; border-radius: 4px; background: #2a2a2a">'
            f'{icon("grip2", 12, "#6b6b6b")}{icon(ic, 14, "#a8a8a8")}<span style="font-weight: 500">{n}{"<span style=\"margin-left: 6px; font-size: 10px; font-weight: 400; color: #939393\">design here first</span>" if main else ""}</span>'
            f'{fld(f"<span style=\"flex: 1\">{w}</span><span style=\"font-size: 10px; color: #939393\">px</span>", "width: 90px; height: 26px;")}'
            f'<span style="font-size: 11px; color: #939393">{base} · {cols} columns</span><span style="justify-self: end">{sw(on)}</span></div>')
sizes = ('<div style="font-size: 11px; color: #939393; margin-bottom: 8px">The sizes pages are designed at. Changes made at a smaller size apply to that size and below.</div><div style="display: flex; flex-direction: column; gap: 4px">'
         + sz('desktop', 'Desktop', 1440, 'from 1025', 12, main=True) + sz('tablet', 'Tablet', 768, '641 – 1024', 8) + sz('phone', 'Mobile', 390, 'up to 640', 4) + sz('wide', 'Wide', 1920, 'from 1600', 12, on=False) + '</div>'
         + '<div style="display: flex; align-items: center; gap: 12px; margin-top: 10px"><button style="font-size: 11px; color: #a9c8f7">+ Add a screen size</button><span style="flex: 1"></span><span style="font-size: 11px; color: #939393">Grid columns and margins are in the design system</span></div>'
         + row('Write CSS as', segm(['Desktop first (max-width)', 'Mobile first (min-width)'], 0), 'Changes how media queries are written; the design is the same'))
c_sz = panel('Screen sizes', 'Screen sizes', sizes, 420)

# Redirects
rd = lambda a, b, code, note='', warn=False: f'<div style="height: 36px; display: grid; grid-template-columns: minmax(0, 1fr) 16px minmax(0, 1fr) 70px 140px 16px; align-items: center; gap: 10px; padding: 0 10px; border-radius: 4px; background: #2a2a2a"><span style="{M_}">{a}</span>{icon("arrow" if "arrow" in P else "chev-right", 12, "#6b6b6b")}<span style="{M_}; color: {"#e3b34a" if warn else "#c8c8c8"}">{b}</span><span style="font-size: 11px; color: #a8a8a8">{code}</span><span style="font-size: 11px; color: #939393">{note}</span>{icon("more", 12, "#a8a8a8")}</div>'
P['arrow'] = ('stroke', 'M3 8h10M9 4l4 4-4 4')
redir = ('<div style="font-size: 11px; color: #939393; margin-bottom: 8px">Old addresses that should send visitors to a new page. Renaming a page can add one for you.</div>'
         + '<div style="display: grid; grid-template-columns: minmax(0, 1fr) 16px minmax(0, 1fr) 70px 140px 16px; gap: 10px; padding: 0 10px 4px; font-size: 10px; color: #6b6b6b"><span>From</span><span></span><span>To</span><span>Kind</span><span></span><span></span></div>'
         + '<div style="display: flex; flex-direction: column; gap: 4px">' + rd('/journal.html', '/stories.html', 'Moved', 'added by Rename · today')
         + rd('/shop/old-bowls', '/shop.html#tide', 'Moved', 'added by you') + rd('/press', 'https://press.halden.studio', 'Temporary', 'checks: reachable') + rd('/visit-us', '/visit.html', 'Moved', 'page deleted · 404', True) + '</div>'
         + f'<div style="display: flex; align-items: center; gap: 12px; margin-top: 10px"><button style="font-size: 11px; color: #a9c8f7">+ Add a redirect</button><button style="font-size: 11px; color: #a8a8a8">Import from a file…</button><span style="flex: 1"></span><span style="font-size: 11px; color: #939393">Exported as _redirects, .htaccess or vercel.json</span></div>')
c_rd = panel('Redirects', 'Redirects', redir, 340)

# Site-wide code
code_box = lambda lab, sub, lines, n: f'''<div style="display: flex; flex-direction: column; gap: 6px"><div style="display: flex; align-items: baseline; gap: 8px"><span style="font-weight: 500">{lab}</span><span style="font-size: 11px; color: #939393">{sub}</span><span style="flex: 1"></span><span style="font-size: 11px; color: #939393">{n}</span></div>
<pre style="margin: 0; padding: 10px 12px; border-radius: 4px; background: #1b1b1b; box-shadow: inset 0 0 0 1px #303030; {M_}; line-height: 18px; color: #c8c8c8; white-space: pre; overflow: hidden">{lines}</pre></div>'''
sc = (code_box('In &lt;head&gt;', 'every page, after Daisy’s own tags', '<span style="color: #7a7a7a">&lt;!-- Plausible analytics --&gt;</span>\n<span style="color: #7fb0f0">&lt;script</span> defer data-domain=<span style="color: #9cc58a">"halden.studio"</span> src=<span style="color: #9cc58a">"https://plausible.io/js/script.js"</span><span style="color: #7fb0f0">&gt;&lt;/script&gt;</span>', '2 lines')
      + '<div style="height: 10px"></div>'
      + code_box('Before &lt;/body&gt;', 'every page', '<span style="color: #7a7a7a">&lt;!-- nothing yet --&gt;</span>', '')
      + f'<div style="display: flex; align-items: center; gap: 10px; margin-top: 10px; font-size: 11px; color: #a8a8a8">{sw(False)}<span>Run it in the editor and Preview</span><span style="flex: 1"></span><span style="color: #939393">Off: it only runs on the exported site · one page only: Page settings › Code</span></div>')
c_sc = panel('Site-wide code', 'Site-wide code', sc, 340)

# Export defaults
ck = lambda t: '<span style="display: flex; align-items: center; gap: 6px"><span style="width: 14px; height: 14px; border-radius: 3px; display: flex; align-items: center; justify-content: center; background: #246bcb">' + icon('check', 10, '#fff', 2) + '</span>' + t + '</span>'
also = '<span style="display: flex; gap: 14px; font-size: 11px">' + ''.join(ck(t) for t in ['sitemap.xml', 'robots.txt', '404.html']) + '</span>'
ex = (row('Export to', dd('Folder · D:\\Sites\\halden-export', 'width: 320px;'), 'Or .zip, or a host from Export')
      + row('Addresses', segm(['/shop.html', '/shop', '/shop/'], 1), 'Clean addresses need a host that supports them')
      + row('CSS', segm(['One file', 'One per page'], 0) + f'<span style="display: flex; align-items: center; gap: 8px; font-size: 11px; color: #a8a8a8">{sw(True)}Remove unused · minify</span>')
      + row('Images', f'<span style="display: flex; align-items: center; gap: 8px; font-size: 11px; color: #a8a8a8">{sw(True)}Resize to the largest size used · WebP with fallback</span>')
      + row('Before exporting', f'<span style="display: flex; align-items: center; gap: 8px; font-size: 11px; color: #a8a8a8">{sw(True)}Check links and accessibility · problems never block</span>')
      + row('Also write', also))
c_ex = panel('Export defaults', 'Export defaults', ex, 420)

cells = [('General', 'Name, address, language, home page, favicon and the default social image.', c_gen),
         ('Screen sizes', 'Order, widths and ranges; Desktop is designed first. How media queries are written.', c_sz),
         ('Redirects', 'From → to with kind and where it came from; a redirect to a deleted page is flagged.', c_rd),
         ('Site-wide code', 'Code for every page, in head and before the end of body; off in the editor by default.', c_sc),
         ('Export defaults', 'Where, address style, CSS, images, the pre-export check and extra files.', c_ex)]
body = sheet_header('D-44b', 'Project settings · the other tabs', 'The five tabs beside Fonts (D-44), drawn compact. Same panel frame, same row pattern; nothing here is repeated in Page settings.')
body += '<div style="display: grid; grid-template-columns: repeat(2, 880px); gap: 48px 32px; align-items: start">' + ''.join(f'<div>{cap(t, d)}{c}</div>' for t, d, c in cells) + '</div>'
H = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
open('/home/claude/daisy/project/D44b-ProjectSettings-Tabs.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-44b Project settings tabs', 1920, H, body))
print('ok')
