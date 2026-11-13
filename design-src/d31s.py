import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

P['globe'] = ('stroke', 'M8 1.5a6.5 6.5 0 1 1 0 13 6.5 6.5 0 0 1 0-13zM1.5 8h13M8 1.5c2 2 2 11 0 13M8 1.5c-2 2-2 11 0 13')
P['palette'] = ('stroke', 'M8 1.5a6.5 6.5 0 1 0 0 13c1 0 1.5-.6 1.5-1.4 0-1.2-1-1.3-1-2.3 0-.8.6-1.3 1.5-1.3h1.6a2.9 2.9 0 0 0 2.9-2.9C14.5 4 11.6 1.5 8 1.5z')
P['share'] = ('stroke', 'M10.5 4.5L8 2 5.5 4.5M8 2v8M3.5 8v5.5h9V8')
sw = lambda on: f'<button role="switch" aria-checked="{str(on).lower()}" style="position: relative; width: 28px; height: 16px; flex: none; border-radius: 8px; background: {"#246bcb" if on else "#454545"}"><span style="position: absolute; {"right" if on else "left"}: 2px; top: 2px; width: 12px; height: 12px; border-radius: 6px; background: {"#fff" if on else "#a8a8a8"}"></span></button>'
lab = lambda t, right='': f'<div style="display: flex; align-items: baseline; gap: 8px; margin-bottom: 5px"><span style="font-size: 12px; color: #e8e8e8">{t}</span><span style="flex: 1"></span>{right}</div>'
cnt = lambda n, mx: f'<span style="font-size: 10px; color: {"#939393" if n <= mx else "#e3b34a"}; font-variant-numeric: tabular-nums">{n} / {mx}</span>'
inp = lambda v, focus=False, mono=False, h=28, ph=False, warn=False: f'<div style="min-height: {h}px; display: flex; align-items: center; padding: 5px 10px; box-sizing: border-box; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px {"#d29922" if warn else ("#2f80ed" if focus else "#3a3a3a")}; line-height: 17px; {"font-family: " + MONO + "; font-size: 11px;" if mono else ""} color: {"#939393" if ph else "#e8e8e8"}">{v}</div>'
hint = lambda t, c='#939393': f'<div style="margin-top: 4px; font-size: 11px; line-height: 15px; color: {c}">{t}</div>'
row = lambda t, sub, ctl: f'<div style="display: flex; align-items: center; gap: 12px; padding: 8px 10px; border-radius: 6px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a"><div style="flex: 1"><div>{t}</div><div style="font-size: 11px; line-height: 15px; color: #939393">{sub}</div></div>{ctl}</div>'
dd = lambda v, w='100%': f'<button style="width: {w}; height: 28px; display: flex; align-items: center; justify-content: space-between; padding: 0 10px; box-sizing: border-box; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; color: #e8e8e8">{v}{icon("chev-down", 10, "#939393", 1.75)}</button>'
sec = lambda t, right='': f'<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393">{t}</span>{right}</div>'
warnb = f'<span>{icon("warning", 11, "#d29922", 1.25)}</span>'
TABS = [('file', 'General'), ('share', 'Search and social'), ('palette', 'Appearance'), ('code', 'Code'), ('sliders', 'Advanced')]
def dialog(active, body, page='Home · <span style="font-family: ' + MONO + '">index.html</span>', badges=None, h=380, nav_extra='', head_extra='', skip=()):
    badges = badges or {}
    tabs = ''.join(f'<div style="height: 30px; display: flex; align-items: center; gap: 8px; padding: 0 10px; border-radius: 5px; {"background: #333333; color: #e8e8e8; font-weight: 500;" if i == active else "color: #a8a8a8;"}">{icon(ic, 14, "#e8e8e8" if i == active else "#939393")}<span style="flex: 1">{t}</span>{badges.get(i, "")}</div>' for i, (ic, t) in enumerate(TABS) if i not in skip)
    return f'''<div style="height: {h}px; display: flex; flex-direction: column; background: #262626; border: 1px solid #454545; border-radius: 10px; overflow: hidden; box-shadow: 0 12px 32px rgba(0,0,0,0.45)">
<div style="height: 42px; flex: none; display: flex; align-items: center; gap: 10px; padding: 0 12px 0 16px; border-bottom: 1px solid #3a3a3a"><b style="font-weight: 600">Page settings</b><span style="font-size: 11px; color: #939393">{page}</span><span style="flex: 1"></span>{head_extra}{icon('close', 13, '#a8a8a8')}</div>
<div style="flex: 1; min-height: 0; display: flex"><div style="width: 176px; flex: none; padding: 8px; box-sizing: border-box; display: flex; flex-direction: column; gap: 2px; border-right: 1px solid #3a3a3a; background: #222222; font-size: 12px">{tabs}{nav_extra}</div>
<div style="flex: 1; min-width: 0; padding: 14px 18px; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px; position: relative">{body}</div></div></div>'''
def btab(title, w=230, favicon_only=False, active=True):
    fav = daisy(12).replace('#e8e8e8', '#b5532d')
    if favicon_only:
        return f'<span style="width: 38px; height: 30px; display: inline-flex; align-items: center; justify-content: center; border-radius: 8px 8px 0 0; background: {"#ffffff" if active else "#d3d6db"}">{fav}</span>'
    return (f'<span style="width: {w}px; height: 30px; display: inline-flex; align-items: center; gap: 8px; padding: 0 10px; box-sizing: border-box; border-radius: 8px 8px 0 0; background: {"#ffffff" if active else "#d3d6db"}; color: #202124; font: 12px/1 Arial, sans-serif">'
            f'{fav}<span style="flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{title}</span><span style="color: #5f6368">×</span></span>')
tabstrip = lambda inner: f'<div style="display: flex; align-items: flex-end; gap: 2px; padding: 6px 8px 0; border-radius: 8px 8px 0 0; background: #dee1e6; overflow: hidden">{inner}</div>'
two = lambda a, b, cols='minmax(0, 1fr) minmax(0, 1fr)': f'<div style="display: grid; grid-template-columns: {cols}; gap: 16px; align-items: start">{a}{b}</div>'
cap = lambda t, desc: f'<div style="display: flex; flex-direction: column; gap: 2px; margin-bottom: 10px"><div style="font-weight: 600">{t}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{desc}</div></div>'
photo = lambda h: f'<div style="position: relative; height: {h}px; background: #e6dccd; overflow: hidden"><span style="position: absolute; left: 30%; right: 30%; top: 38%; height: 34%; border-radius: 0 0 50% 50% / 0 0 100% 100%; background: #b5532d"></span><span style="position: absolute; left: 33%; right: 33%; top: 26%; height: 22%; border-radius: 0 0 50% 50% / 0 0 100% 100%; background: #6b7d5a"></span><span style="position: absolute; left: 64%; width: 9%; top: 40%; height: 30%; border-radius: 2px 2px 5px 5px; background: #1d1a16"></span></div>'
card = lambda net, w, h_img: f'<div style="border-radius: 8px; overflow: hidden; background: #ffffff; color: #1c1e21; font-family: Arial, sans-serif; box-shadow: 0 0 0 1px #dadde1">{photo(h_img)}<div style="padding: 6px 10px; background: #f0f2f5"><div style="font-size: 9px; color: #606770; text-transform: uppercase">halden.studio · {net}</div><div style="font-size: 12px; font-weight: 600; line-height: 15px">Hand-thrown ceramics for everyday tables</div></div></div>'

# 1 · Social sharing (set)
s1 = two(f'''<div style="display: flex; flex-direction: column; gap: 10px">
<div>{lab('Social image', '<span style="font-size: 10px; color: #3fb950">1200 × 630 ✓</span>')}<div style="display: flex; gap: 8px; align-items: center"><div style="width: 96px; border-radius: 4px; overflow: hidden; box-shadow: 0 0 0 1px #3a3a3a">{photo(50)}</div><div style="display: flex; flex-direction: column; gap: 4px"><span style="font-family: {MONO}; font-size: 11px">share-hero.jpg</span><span style="display: flex; gap: 6px"><button style="font-size: 11px; color: #a9c8f7">Replace</button><button style="font-size: 11px; color: #a8a8a8">Crop</button><button style="font-size: 11px; color: #a8a8a8">Remove</button></span></div></div></div>
{row('Same title and description as search', 'Turn off to write a shorter one for social', sw(True))}
<div style="font-size: 11px; line-height: 15px; color: #939393">Favicon and app icon: Appearance</div></div>''',
           f'<div style="display: flex; flex-direction: column; gap: 8px">{sec("PREVIEW", "<span style=\"font-size: 10px; color: #939393\">Large card · Messages</span>")}{card("Facebook, LinkedIn", 0, 110)}<div style="display: flex; gap: 8px; align-items: center; padding: 6px; border-radius: 10px; background: #e9e9eb; color: #111; font-family: Arial, sans-serif"><div style="width: 52px; border-radius: 6px; overflow: hidden">{photo(40)}</div><div style="font-size: 11px; line-height: 14px"><b>Hand-thrown ceramics…</b><br><span style="color: #666">halden.studio</span></div></div></div>', 'minmax(0, 1fr) 270px')
S1 = dialog(1, s1)

# 2 · Social sharing (empty)
s2 = (f'<div style="display: flex; gap: 16px; align-items: stretch">'
      f'<div style="flex: 1; display: flex; flex-direction: column; gap: 10px"><div style="display: flex; gap: 8px; padding: 10px; border-radius: 6px; background: rgba(210,153,34,0.10); box-shadow: inset 0 0 0 1px rgba(210,153,34,0.45); font-size: 11px; line-height: 16px"><span style="margin-top: 1px">{icon("warning", 12, "#d29922", 1.25)}</span><span style="color: #c8c8c8"><b style="font-weight: 600; color: #e8e8e8">No social image.</b> Shared links will use the first image on the page, cropped by each app.</span></div>'
      f'<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px">'
      + ''.join(f'<button style="display: flex; flex-direction: column; gap: 6px; padding: 8px; border-radius: 6px; background: #2a2a2a; text-align: left"><span style="height: 54px; border-radius: 4px; overflow: hidden">{g}</span><span style="font-size: 11px; color: #e8e8e8">{t}</span><span style="margin-top: -4px; font-size: 10px; color: #939393">{d}</span></button>'
                for t, d, g in [('From the Hero', 'Title over the hero image', photo(54)), ('Pick an asset', '1200 × 630 works best', '<span style="display: flex; height: 54px; align-items: center; justify-content: center; background: #1f1f1f; color: #939393">' + icon('t-image', 18, '#939393') + '</span>'), ('Upload', 'jpg, png or webp', '<span style="display: flex; height: 54px; align-items: center; justify-content: center; background: #1f1f1f">' + icon('upload', 18, '#939393') + '</span>')])
      + '</div></div></div>')
S2 = dialog(1, s2, badges={1: warnb})

# 3 · Appearance
swatchf = lambda c, name: f'<div style="height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 10px; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a"><span style="width: 14px; height: 14px; border-radius: 3px; background: {c}; box-shadow: inset 0 0 0 1px rgba(0,0,0,0.25)"></span><span style="flex: 1">{name}</span><span style="font-family: {MONO}; font-size: 10px; color: #939393">{c.upper()}</span></div>'
s3 = two(f'''<div style="display: flex; flex-direction: column; gap: 10px">
<div>{lab('Page background')}{swatchf('#f6f1ea', 'sand · Halden')}</div>
<div>{lab('Base text')}<div style="display: grid; grid-template-columns: minmax(0, 1fr) 70px; gap: 6px">{dd('Inter')}{inp('16 <span style="color: #939393; font-size: 10px; margin-left: 4px">px</span>')}</div><div style="margin-top: 6px">{swatchf('#1d1a16', 'ink · Halden')}</div>{hint('Every text without its own style uses these')}</div></div>''',
         f'''<div style="display: flex; flex-direction: column; gap: 10px">
<div>{lab('Browser bar colour', '<span style="font-size: 10px; color: #939393">phones</span>')}{swatchf('#1d1a16', 'ink')}</div>
<div>{lab('Simulated window height')}{inp('900 <span style="color: #939393; font-size: 10px; margin-left: 4px">px · draws the fold line</span>')}</div>
{row('Smooth scrolling for links', 'Jumps to #sections glide', sw(True))}</div>''')
S3 = dialog(2, s3)

# 4 · Search engines
code = lambda t: f'<div style="padding: 8px 10px; border-radius: 4px; background: #1b1b1b; box-shadow: inset 0 0 0 1px #2c2c2c; font: 10.5px/16px {MONO}; color: #a8a8a8; white-space: pre">{t}</div>'
s4 = two(f'''<div style="display: flex; flex-direction: column; gap: 10px">
<div>{lab('Canonical address')}{inp('https://halden.studio/', mono=True)}{hint('The one address search engines should use for this page')}</div>
<div>{lab('In the sitemap')}{dd('Yes · checked weekly')}</div>
<div>{lab('Text direction')}<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #1f1f1f; border-radius: 4px; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px"><span style="height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: #3a3a3a; color: #e8e8e8">Left to right</span><span style="height: 22px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">Right to left</span></div></div></div>''',
         f'''<div style="display: flex; flex-direction: column; gap: 6px">
<div>{lab('Business details', sw(True))}{dd('Local store · ceramics')}</div>
{code('{ "@type": "Store",\n  "name": "Halden",\n  "address": "Riverside Works, Unit 4",\n  "url": "https://halden.studio" }')}
<div style="font-size: 10px; color: #939393">Filled from Halden's footer · lets search show the address and hours</div>
<div style="font-size: 10px; color: #939393">Also here: follow links, meta tags, preload the hero image, html and body attributes</div></div>''')
S4 = dialog(4, s4)

# 5 · Code in <head>
ln = lambda n, t, c='#a8a8a8': f'<div style="display: flex"><span style="width: 28px; flex: none; text-align: right; padding-right: 8px; color: #5b5b5b">{n}</span><span style="color: {c}">{t}</span></div>'
s5 = (f'<div style="display: flex; align-items: center; gap: 8px">{sec("CUSTOM CODE IN &lt;HEAD&gt;")}<span style="flex: 1"></span><span style="font-size: 10px; color: #939393">this page only · site-wide code: </span><button style="font-size: 10px; color: #a9c8f7">Project settings</button></div>'
      f'<div style="padding: 6px 0; border-radius: 4px; background: #1b1b1b; box-shadow: inset 0 0 0 1px #2f80ed; font: 11px/17px {MONO}">'
      + ln(1, '<span style="color: #8a8a8a">&lt;</span><span style="color: #7fb0f0">link</span> rel=<span style="color: #9cc58a">"preconnect"</span> href=<span style="color: #9cc58a">"https://shop.halden.studio"</span><span style="color: #8a8a8a">&gt;</span>')
      + ln(2, '<span style="color: #8a8a8a">&lt;</span><span style="color: #7fb0f0">script</span> defer src=<span style="color: #9cc58a">"https://stats.example/s.js"</span><span style="color: #8a8a8a">&gt;&lt;/</span><span style="color: #7fb0f0">script</span><span style="color: #8a8a8a">&gt;</span>')
      + ln(3, '') + '</div>'
      f'<div style="display: flex; gap: 8px; padding: 8px 10px; border-radius: 6px; background: rgba(47,128,237,0.10); box-shadow: inset 0 0 0 1px rgba(47,128,237,0.4); font-size: 11px; line-height: 16px"><span style="margin-top: 1px">{icon("info", 12, "#58a6ff", 1.25)}</span><span style="color: #c8c8c8">Scripts run only in Preview and the exported site, never in the editor · this one loads from another site, so it is added to the export checks.</span></div>')
S5 = dialog(3, s5)

# 6 · Validation
serp = lambda title, desc: f'<div style="padding: 10px 12px; border-radius: 8px; background: #ffffff; color: #202124; font-family: Arial, sans-serif"><div style="font-size: 11px; color: #4d5156">halden.studio</div><div style="margin-top: 3px; font-size: 15px; line-height: 19px; color: #1a0dab">{title}</div><div style="margin-top: 2px; font-size: 12px; line-height: 17px; color: #4d5156">{desc}</div></div>'
s6 = two(f'''<div style="display: flex; flex-direction: column; gap: 10px">
<div>{lab('Page title', cnt(74, 60))}{inp('Halden — Hand-thrown ceramics for everyday tables, made in our river studio', True, warn=True)}{hint('Search engines cut titles after about 60 characters', '#e3b34a')}</div>
<div>{lab('Description', cnt(0, 160))}{inp('Empty · search engines pick text from the page', ph=True)}<div style="display: flex; gap: 8px; margin-top: 6px"><button style="height: 22px; padding: 0 8px; border-radius: 4px; background: #246bcb; font-size: 11px; color: #fff">Use the first paragraph</button></div></div></div>''',
         f'<div style="display: flex; flex-direction: column; gap: 8px">{sec("IN SEARCH RESULTS")}{serp("Halden — Hand-thrown ceramics for everyday tables, made in…", "<i style=\"color: #70757a\">Small-batch stoneware · Est. 2014. Hand-thrown ceramics for everyday tables. Each piece is wheel-thrown…</i>")}<div style="font-size: 10px; color: #939393">Cut-off and borrowed text shown as search would</div>{sec("IN THE BROWSER TAB")}{tabstrip(btab("Halden — Hand-thrown ceramics for everyday tables, made in our river studio", 270))}</div>', 'minmax(0, 1fr) 300px')
S6 = dialog(0, s6, badges={0: warnb})

# 7 · Another page: address
s7 = (f'<div>{lab("Address on the site")}<div style="display: flex; align-items: center; height: 30px; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #2f80ed; font-family: {MONO}; font-size: 11px"><span style="padding: 0 2px 0 10px; color: #939393">halden.studio/</span><span>shop</span><span style="display: inline-block; width: 1px; height: 13px; background: #e8e8e8; margin-left: 1px"></span></div>'
      + hint('Saved as shop.html · lowercase letters, numbers and dashes') + '</div>'
      f'<div style="display: flex; gap: 8px; padding: 8px 10px; border-radius: 6px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; line-height: 16px"><span style="margin-top: 1px">{icon("check", 12, "#3fb950", 2)}</span><span style="color: #c8c8c8">Renamed from <code style="font-family: {MONO}">/store</code> · <b style="font-weight: 600">3 links</b> on Home and Journal update automatically · the old address redirects in the export.</span></div>'
      f'<div>{lab("Tried first")}<div style="display: flex; align-items: center; height: 28px; padding: 0 10px; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #c9302c; font-family: {MONO}; font-size: 11px; color: #e8e8e8">halden.studio/journal</div>' + hint('“journal” is already used by the Journal page', '#f47067') + '</div>')
S7 = dialog(0, s7, page='Shop · <span style="font-family: ' + MONO + '">shop.html</span>')

# 8 · Hidden from search
s8 = two(f'''<div style="display: flex; flex-direction: column; gap: 10px">
{row('Show in search results', 'Off · this page has noindex and is left out of the sitemap', sw(False))}
<div style="font-size: 11px; line-height: 16px; color: #939393">Good for thank-you pages, drafts and test pages. Visitors can still open it with the link.</div></div>''',
         f'<div style="position: relative">{serp("Halden — Visit the studio", "Opening hours, directions and how to book a visit to our riverside studio.")}<div style="position: absolute; inset: 0; border-radius: 8px; background: rgba(38,38,38,0.78); display: flex; align-items: center; justify-content: center; gap: 6px; font-size: 12px; color: #e8e8e8">{icon("eye-off", 14, "#e8e8e8")}Hidden from search results</div></div>', 'minmax(0, 1fr) 300px')
S8 = dialog(1, s8, page='Visit · <span style="font-family: ' + MONO + '">visit.html</span>', badges={1: icon('eye-off', 11, '#939393')})

# 9 · Page switcher open
pm = lambda name, file, note, on=False, warn=False: f'<div style="height: 32px; display: flex; align-items: center; gap: 8px; padding: 0 8px; border-radius: 4px; {"background: #333333;" if on else ""}">{icon("file", 13, "#a8a8a8")}<span style="color: #e8e8e8">{name}</span><span style="font-family: {MONO}; font-size: 10px; color: #939393">{file}</span><span style="flex: 1"></span>{icon("warning", 11, "#d29922", 1.25) if warn else ""}<span style="font-size: 10px; color: #939393">{note}</span></div>'
menu = (f'<div style="position: absolute; right: 30px; top: -2px; width: 300px; padding: 4px; border-radius: 6px; background: #2a2a2a; border: 1px solid #454545; box-shadow: 0 10px 28px rgba(0,0,0,0.5); z-index: 5">'
        + pm('Home', 'index.html', 'no social image', True, True) + pm('Shop', 'shop.html', 'all set') + pm('Journal', 'journal.html', 'no description', warn=True) + pm('Visit', 'visit.html', 'hidden from search')
        + '<div style="height: 1px; background: #3a3a3a; margin: 4px 0"></div><div style="padding: 4px 8px; font-size: 11px; color: #a9c8f7">Fill missing descriptions on all pages…</div></div>')
S9 = dialog(0, '<div style="opacity: 0.35">' + f'<div>{lab("Page title", cnt(50, 60))}{inp("Halden — Hand-thrown ceramics for everyday tables")}</div>' + '</div>' + menu,
            head_extra=f'<button style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 10px; border-radius: 4px; background: #333333; box-shadow: inset 0 0 0 1px #2f80ed; font-size: 11px; color: #e8e8e8">Home{icon("chev-up", 10, "#939393", 1.75)}</button>')

# 10 · Single file (outside the project)
s10 = (f'<div style="display: flex; gap: 8px; padding: 8px 10px; border-radius: 6px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; line-height: 16px"><span style="margin-top: 1px">{icon("info", 12, "#58a6ff", 1.25)}</span><span style="color: #c8c8c8"><b style="font-weight: 600; color: #e8e8e8">A single file,</b> not part of a project. It has no site address or sitemap, and it brings its own colours and fonts.</span></div>'
       + two(f'<div>{lab("Page title", cnt(28, 60))}{inp("Weekend sale — 20% off bowls")}</div>', f'<div>{lab("Saved as")}{inp("D:\\Mine\\promo-banner.html", mono=True)}</div>')
       + f'<div><button style="height: 26px; padding: 0 10px; border-radius: 4px; background: #2a2a2a; font-size: 11px; color: #c8c8c8">Move into Halden…</button><span style="margin-left: 8px; font-size: 11px; color: #939393">to share its design system and appear in exports</span></div>')
S10 = dialog(0, s10, page='<span style="font-family: ' + MONO + '">promo-banner.html</span> · single file',
             nav_extra='<div style="margin-top: 6px; padding: 6px 8px; font-size: 10px; line-height: 14px; color: #939393">No address or sitemap for single files</div>')


# 11 · Page title in the browser
s11 = two(f'''<div style="display: flex; flex-direction: column; gap: 10px">
<div>{lab('Page title', cnt(50, 60))}{inp('Halden — Hand-thrown ceramics for everyday tables', True)}{hint('Put the words people need first · tabs show about 25 characters')}</div>
<div style="display: flex; gap: 8px; padding: 8px 10px; border-radius: 6px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; line-height: 16px"><span style="margin-top: 1px">{icon("info", 12, "#58a6ff", 1.25)}</span><span style="color: #c8c8c8">The icon comes from Project settings › Favicon.</span></div></div>''',
          f'''<div style="display: flex; flex-direction: column; gap: 7px">
<div style="display: flex; align-items: center; justify-content: space-between">{sec("PREVIEW")}<span style="display: flex; gap: 2px; padding: 2px; border-radius: 5px; background: #1f1f1f; font-size: 10px"><span style="padding: 0 8px; height: 18px; line-height: 18px; color: #a8a8a8">Search</span><span style="padding: 0 8px; height: 18px; line-height: 18px; color: #a8a8a8">Share</span><span style="padding: 0 8px; height: 18px; line-height: 18px; border-radius: 3px; background: #3a3a3a; color: #e8e8e8">Tab</span></span></div>
<div style="font-size: 10px; color: #939393">One tab open</div>{tabstrip(btab("Halden — Hand-thrown ceramics for everyday tables", 280))}
<div style="font-size: 10px; color: #939393">Many tabs open</div>{tabstrip(btab("Halden — Hand-thrown ceramics for everyday tables", 104) + btab("Inbox", 104, active=False) + btab("Maps", 70, active=False))}
<div style="font-size: 10px; color: #939393">Pinned · bookmark</div><div style="display: flex; align-items: center; gap: 10px">{tabstrip(btab("", favicon_only=True))}<span style="display: inline-flex; align-items: center; gap: 6px; height: 24px; padding: 0 8px; border-radius: 12px; background: #dee1e6; color: #202124; font: 11px Arial">{daisy(11).replace("#e8e8e8", "#b5532d")}Halden — Hand-thrown…</span></div></div>''', 'minmax(0, 1fr) 320px')
S11 = dialog(0, s11)

# 12 · Draft
s12 = (f'<div style="display: flex; align-items: center; gap: 10px; padding: 8px 12px; border-radius: 6px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a"><span style="height: 18px; padding: 0 7px; border-radius: 9px; background: #3a3a3a; font-size: 10px; font-weight: 600; line-height: 18px; color: #e8e8e8">DRAFT</span><span style="flex: 1; font-size: 11px; color: #c8c8c8">Left out of exports and the sitemap · you can still open it in Preview</span></div>'
       + f'<div>{lab("Status")}<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #1f1f1f; border-radius: 4px; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px"><span style="height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: #3a3a3a; color: #e8e8e8; font-weight: 500">Draft</span><span style="height: 24px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">Published</span></div>{hint("Links to a draft page are flagged in the export checks")}</div>'
       + f'<div>{lab("Page title", cnt(22, 60))}{inp("Journal — Spring firing")}</div>')
S12 = dialog(0, s12, page='Journal · <span style="font-family: ' + MONO + '">journal.html</span> · draft')

cells = [
    ('1 · Search and social', 'Social image set at 1200 × 630, the same text as search by default, previews for a link card and a chat message', S1),
    ('2 · Search and social · no image', 'A warning, and three ways to get an image: from the Hero, an asset, or an upload', S2),
    ('3 · Appearance', 'Page background and base text from Halden tokens, phone browser colour, fold height, smooth scrolling', S3),
    ('4 · Advanced', 'Canonical address, sitemap, text direction and business details; the rarely needed settings', S4),
    ('5 · Code', 'Code in the head of this page; scripts run only in Preview and exports', S5),
    ('6 · Too long and empty', 'Amber counter and border; the search and tab previews show the cut-off and borrowed text', S6),
    ('7 · Another page’s address', 'Editable slug, links updated and old address redirected; a taken name in red', S7),
    ('8 · Hidden from search', 'Show in search results off: the preview is covered with “Hidden from search results”', S8),
    ('9 · Page switcher', 'Every page with what it is missing, and a fix for all at once', S9),
    ('10 · Single file', 'Outside a project: no address or sitemap, with a way to move it into Halden', S10),
    ('11 · Page title in the browser', 'The Tab preview: one tab, many tabs (about 25 characters show), pinned and bookmark', S11),
    ('12 · Draft', 'A draft page: left out of exports and the sitemap, still visible in Preview', S12),
]
body = sheet_header('D-31b', 'Page settings · states', 'The other sections and the states of Page settings, drawn at a compact size: search and social, appearance, advanced, code, validation, another page’s address, a hidden page, the page switcher, a single file, the title in the browser tab and a draft. Read with D-31.')
body += '<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 48px 64px; align-items: start">' + ''.join(f'<div>{cap(t, dsc)}{c}</div>' for t, dsc, c in cells) + '</div>'
H = int(sys.argv[1]) if len(sys.argv) > 1 else 2600
open('/home/claude/daisy/project/D31b-PageSettings-States.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-31b Page settings states', 1920, H, body))
print('ok')
