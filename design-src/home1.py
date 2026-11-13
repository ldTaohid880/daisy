import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

kb = lambda t, on_accent=False: (f'<span style="height: 18px; box-sizing: border-box; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; '
                                 f'{"background: rgba(255,255,255,0.18); color: #ffffff;" if on_accent else "background: #333333; box-shadow: inset 0 -1px 0 #454545; color: #a8a8a8;"} font-size: 10px; font-weight: 500">{t}</span>')

body = f'''<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; background: #1f1f1f; color: #e8e8e8; font-family: 'Inter', system-ui, sans-serif; font-size: 12px; line-height: 16px">

<header style="height: 40px; flex: none; box-sizing: border-box; display: flex; align-items: center; gap: 10px; padding: 0 8px; background: #141414; border-bottom: 1px solid #262626">
<span style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 6px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #2e2e2e">{daisy(18)}</span>
<span style="font-weight: 600">Daisy</span>
<span style="flex: 1"></span>
<button aria-label="Preferences" title="Preferences" style="width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon('gear', 16)}</button>
</header>

<main style="flex: 1; display: flex; align-items: center; justify-content: center; padding-bottom: 80px">
<div style="width: 480px; display: flex; flex-direction: column; gap: 24px">
<div style="display: flex; flex-direction: column; gap: 8px">
<h1 style="margin: 0; font-size: 20px; line-height: 28px; font-weight: 600">Your projects</h1>
<p style="margin: 0; font-size: 13px; line-height: 20px; color: #a8a8a8">A project holds your pages and one design system they all share. Every new page starts as one empty section. You build everything else.</p>
</div>

<div style="display: flex; align-items: center; gap: 8px">
<button style="height: 32px; display: flex; align-items: center; gap: 10px; padding: 0 8px 0 14px; border-radius: 6px; background: #246bcb; color: #ffffff; font-weight: 500">New project<span style="display: flex; gap: 2px">{kb('Alt', True)}{kb('N', True)}</span></button>
<button style="height: 32px; display: flex; align-items: center; gap: 10px; padding: 0 8px 0 12px; border-radius: 6px; color: #e8e8e8; font-weight: 500; box-shadow: inset 0 0 0 1px #3a3a3a">{icon('file', 14, '#a8a8a8')}Open file…<span style="display: flex; gap: 2px">{kb('Ctrl')}{kb('O')}</span></button>
</div>

<div style="display: flex; align-items: flex-start; gap: 10px; padding-top: 20px; border-top: 1px solid #2a2a2a; font-size: 11px; line-height: 16px; color: #939393">
<span style="margin-top: 1px">{icon('info', 14, '#939393', 1.25)}</span>
<span><span style="color: #a8a8a8">Open file</span> edits one HTML page on its own, without a project. You can add it to a project later. You can also drop an <code style="font-family: {MONO}">.html</code> file anywhere in this window.</span>
</div>
</div>
</main>
</div>'''

html = page('Daisy · D-01 Home, first run', 1920, 1080, '')
html = html.replace('''<div style="width: 1920px; height: 1080px; box-sizing: border-box; padding: 64px; overflow: hidden; background: #1f1f1f; color: #e8e8e8; font-family: 'Inter', system-ui, sans-serif; font-size: 12px; line-height: 16px; font-variant-numeric: tabular-nums">

</div>''', body)
assert body in html
open('/home/claude/daisy/project/D01-Home.dc.html', 'w', encoding='utf-8').write(html)
