import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *
import wiz as WZ

kb = lambda t, on_accent=False: (f'<span style="height: 18px; box-sizing: border-box; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; '
                                 f'{"background: rgba(255,255,255,0.18); color: #ffffff;" if on_accent else "background: #333333; box-shadow: inset 0 -1px 0 #454545; color: #a8a8a8;"} font-size: 10px; font-weight: 500">{t}</span>')


def thumb(bg, ink, accent, hero_dark=False, layout='split'):
    """A tiny drawing of the project's home page, 240 x 150, on bg-workspace."""
    head = f'<div style="height: 10px; display: flex; align-items: center; justify-content: space-between; padding: 0 8px"><span style="width: 22px; height: 4px; border-radius: 1px; background: {ink}"></span><span style="display: flex; gap: 4px">' + ''.join(f'<span style="width: 10px; height: 2px; background: {ink}; opacity: 0.5"></span>' for _ in range(3)) + f'</span><span style="width: 16px; height: 5px; border-radius: 3px; background: {accent}"></span></div>'
    if layout == 'split':
        hero = f'''<div style="display: grid; grid-template-columns: 1.1fr 1fr; gap: 8px; padding: 10px 8px 8px; align-items: center">
<div style="display: flex; flex-direction: column; gap: 3px"><span style="width: 90%; height: 6px; border-radius: 1px; background: {ink}"></span><span style="width: 70%; height: 6px; border-radius: 1px; background: {ink}"></span><span style="width: 80%; height: 2px; background: {ink}; opacity: 0.4; margin-top: 3px"></span><span style="width: 60%; height: 2px; background: {ink}; opacity: 0.4"></span><span style="width: 34px; height: 6px; border-radius: 3px; background: {accent}; margin-top: 4px"></span></div>
<div style="height: 52px; border-radius: 3px; background: {accent}; opacity: 0.55"></div></div>'''
    elif layout == 'center':
        hero = f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 4px; padding: 14px 8px 10px; {"background: " + ink + ";" if hero_dark else ""}">
<span style="width: 60%; height: 7px; border-radius: 1px; background: {bg if hero_dark else ink}"></span><span style="width: 40%; height: 2px; background: {bg if hero_dark else ink}; opacity: 0.5"></span><span style="width: 30px; height: 6px; border-radius: 3px; background: {accent}; margin-top: 4px"></span></div>'''
    else:  # grid gallery
        hero = f'<div style="padding: 8px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 4px">' + ''.join(f'<span style="height: 28px; border-radius: 2px; background: {accent}; opacity: {0.35 + 0.15 * (i % 3)}"></span>' for i in range(6)) + '</div>'
    cards = f'<div style="padding: 0 8px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 4px">' + ''.join(f'<span style="height: 18px; border-radius: 2px; background: {ink}; opacity: 0.12"></span>' for _ in range(3)) + '</div>'
    return f'''<div aria-hidden="true" style="height: 150px; display: flex; align-items: flex-end; justify-content: center; background: #2a2a2a">
<div style="width: 196px; height: 132px; overflow: hidden; background: {bg}; box-shadow: 0 0 0 1px #3c3c3c">{head}{hero}{cards}</div></div>'''


projects = [
    ('Halden', 4, 'Edited 12 minutes ago', thumb('#f6f1ea', '#1d1a16', '#b5532d'), True),
    ('Riverside Café', 2, 'Edited yesterday', thumb('#fffaf2', '#2b2118', '#c9822b', layout='center')),
    ('Portfolio 2026', 6, 'Edited 3 days ago', thumb('#111318', '#e9ecf1', '#7aa2ff', layout='grid')),
    ('Nord Studio', 3, 'Edited 1 week ago', thumb('#eef1ee', '#17201b', '#2f6b4f', True, 'center')),
    ('Lumen careers', 1, 'Edited 2 weeks ago', thumb('#ffffff', '#0b1f3a', '#c9a24b')),
    ('Kiln workshop', 2, 'Edited last month', thumb('#f3ece4', '#2a1e16', '#8a5a3c', layout='grid')),
]


def card(name, pages, edited, th, hover=False):
    hv = 'box-shadow: inset 0 0 0 1px #454545;' if hover else 'box-shadow: inset 0 0 0 1px #2a2a2a;'
    more = f'<button aria-label="{name} options" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8; {"background: #323232;" if hover else ""}">{icon("more", 14)}</button>'
    return f'''<a href="#{name}" style="display: flex; flex-direction: column; width: 240px; border-radius: 6px; overflow: hidden; background: #1a1a1a; {hv} color: #e8e8e8; text-decoration: none">
{th}
<div style="display: flex; align-items: center; gap: 8px; padding: 10px 8px 10px 12px">
<div style="flex: 1; min-width: 0"><div style="font-weight: 500; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{name}</div>
<div style="font-size: 11px; color: #939393">{pages} page{"s" if pages > 1 else ""} · {edited}</div></div>{more}</div></a>'''


cards_html = ''.join(card(x[0], x[1], x[2], x[3], len(x) > 4 and x[4]) for x in projects)

files = [('promo-banner.html', 'D:\\Mine\\marketing', 'Opened 2 hours ago'), ('invite-card.html', 'D:\\Mine\\events', 'Opened yesterday'), ('newsletter-header.html', 'Downloads', 'Opened last week')]
files_html = ''.join(f'''<div style="height: 36px; display: grid; grid-template-columns: 20px minmax(0, 1fr) 260px 160px 120px; align-items: center; gap: 12px; padding: 0 12px; border-bottom: 1px solid #262626">
{icon("file", 14, "#a8a8a8")}<span style="font-family: {MONO}; font-size: 12px">{n}</span><span style="font-family: {MONO}; font-size: 11px; color: #939393">{p}</span><span style="font-size: 11px; color: #939393">{t}</span>
<button style="justify-self: end; height: 22px; padding: 0 8px; border-radius: 4px; font-size: 11px; color: #a8a8a8">Add to project</button></div>''' for n, p, t in files)

page_body = f'''<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; background: #1f1f1f; color: #e8e8e8; font-family: 'Inter', system-ui, sans-serif; font-size: 12px; line-height: 16px">

<header style="height: 40px; flex: none; box-sizing: border-box; display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; gap: 16px; padding: 0 8px; background: #141414; border-bottom: 1px solid #262626">
<div style="display: flex; align-items: center; gap: 10px">
<span style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 6px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #2e2e2e">{daisy(18)}</span><span style="font-weight: 600">Daisy</span></div>
<button aria-label="Search projects and files" style="width: 440px; height: 28px; box-sizing: border-box; display: flex; align-items: center; gap: 8px; padding: 0 6px 0 10px; border-radius: 6px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #2e2e2e; color: #939393">{icon("search", 13, "currentColor", 1.75)}<span style="flex: 1; text-align: left">Search projects and files</span><span style="display: flex; gap: 2px">{kb("Ctrl")}{kb("P")}</span></button>
<div style="display: flex; justify-content: flex-end"><button aria-label="Preferences" style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon("gear", 16)}</button></div>
</header>

<main style="flex: 1; overflow: hidden; display: flex; justify-content: center; padding-top: 48px">
<div style="width: 1488px; display: flex; flex-direction: column">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 20px">
<h1 style="flex: 1; margin: 0; font-size: 20px; line-height: 28px; font-weight: 600">Your projects</h1>
<button style="height: 28px; display: flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 4px; color: #a8a8a8">Last edited{icon("chev-down", 10, "currentColor", 1.75)}</button>
<button style="height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 8px 0 12px; border-radius: 6px; color: #e8e8e8; font-weight: 500; box-shadow: inset 0 0 0 1px #3a3a3a">{icon("file", 13, "#a8a8a8")}Open file…</button>
<button style="height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 12px; border-radius: 6px; background: #246bcb; color: #ffffff; font-weight: 500">{icon("plus", 12, "currentColor", 2)}New project</button>
</div>
<div style="display: grid; grid-template-columns: repeat(6, 240px); gap: 16px">{cards_html}</div>

<div style="display: flex; align-items: baseline; gap: 10px; margin: 40px 0 8px">
<h2 style="margin: 0; font-size: 14px; line-height: 20px; font-weight: 600">Recent files</h2><span style="font-size: 11px; color: #939393">Single pages opened without a project</span></div>
<div style="border-top: 1px solid #262626">{files_html}</div>

<div style="margin-top: 24px"><a href="#deleted" style="display: inline-flex; align-items: center; gap: 6px; font-size: 11px; color: #a8a8a8; text-decoration: none">{icon("trash", 12)}Recently deleted (2)</a></div>
</div>
</main>

<!-- scrim + New project dialog -->
<div aria-hidden="true" style="position: absolute; inset: 0; background: rgba(0,0,0,0.5)"></div>
<div style="position: absolute; left: 360px; top: 150px">{WZ.step_project()}</div>
</div>'''

html = page('Daisy · D-02 Home with projects, New project dialog', 1920, 1080, '')
blank = '''<div style="width: 1920px; height: 1080px; box-sizing: border-box; padding: 64px; overflow: hidden; background: #1f1f1f; color: #e8e8e8; font-family: 'Inter', system-ui, sans-serif; font-size: 12px; line-height: 16px; font-variant-numeric: tabular-nums">

</div>'''
assert blank in html
html = html.replace(blank, page_body)
open('/home/claude/daisy/project/D02-Home-Projects.dc.html', 'w', encoding='utf-8').write(html)
