"""render.py <file> <out.png> [--measure]  — renders a .dc.html at its own width; prints content height."""
import sys, re
from playwright.sync_api import sync_playwright
src, out = sys.argv[1], sys.argv[2]
html = open(src, encoding='utf-8').read().replace('<script src="./support.js"></script>', '')
w = int(re.search(r'"\$preview":\{"width":(\d+)', html).group(1))
h = int(re.search(r'"height":(\d+)\}', html).group(1))
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': w, 'height': min(h, 4000)})
    pg.set_content(html)
    pg.wait_for_timeout(400)
    sh = pg.evaluate("() => { const r=document.querySelector('x-dc > div'); const t=r.getBoundingClientRect().top; let m=0; for (const c of r.children) m=Math.max(m, c.getBoundingClientRect().bottom-t); return Math.ceil(m+64); }")
    print('content height', sh, 'declared', h)
    pg.screenshot(path=out, full_page=True)
    b.close()
