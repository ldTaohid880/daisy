"""Shared helpers for the Daisy D-00 design system artboards."""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;'
         'family=JetBrains+Mono:wght@400&amp;family=Fraunces:opsz,wght@9..144,400;9..144,600&amp;display=swap">')

MONO = "'JetBrains Mono', ui-monospace, monospace"
FOCUS = "box-shadow: 0 0 0 1px #1f1f1f, 0 0 0 3px #2f80ed"

T = dict(
    titlebar='#141414', toolbar='#1b1b1b', chrome='#181818', panel='#1f1f1f', capsule='#232323',
    workspace='#2a2a2a', control='#2a2a2a', hover='#323232', active='#3a3a3a', popover='#262626',
    line_subtle='#262626', line='#303030', line_strong='#454545', page_edge='#3c3c3c',
    text='#e8e8e8', text2='#a8a8a8', muted='#939393', disabled='#4f4f4f',
    accent='#2f80ed', accent_hover='#4b93f1', accent_fill='#246bcb',
    accent_subtle='rgba(47,128,237,0.18)', resp='#d29922', resp_subtle='rgba(210,153,34,0.14)',
    state='#a371f7', state_subtle='rgba(163,113,247,0.16)', info='#58a6ff', success='#3fb950',
    warning='#d29922', danger='#f85149', daisy='#f2b84b',
)


def lum(h):
    h = h.lstrip('#')
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]


def contrast(a, b):
    a, b = lum(a), lum(b)
    return (max(a, b) + .05) / (min(a, b) + .05)


# ---------- icons (16 px grid, 1.5 stroke, round caps) ----------
P = {
    # tools
    'select': ('fill', 'M4 2l9 6.2-4.1.9 2.4 4.4-1.7.9-2.4-4.4L4 13z'),
    'direct': ('stroke', 'M4 2l9 6.2-4.1.9 2.4 4.4-1.7.9-2.4-4.4L4 13z'),
    'section': ('stroke', 'M1.5 4.5h13v7h-13z'),
    'box': ('stroke', 'M3 3h10v10H3z'),
    'text': ('stroke', 'M3 3h10M8 3v10M6 13h4'),
    'media': ('stroke', 'M2 3h12v10H2zM2 11l3.5-3.5 3 3 2-2L14 12M10.5 6h.01'),
    'button': ('stroke', 'M4.5 4.5h7a3.5 3.5 0 0 1 0 7h-7a3.5 3.5 0 0 1 0-7zM5.5 8h5'),
    'link': ('stroke', 'M6.8 9.2a2.8 2.8 0 0 0 4 0l2-2a2.8 2.8 0 0 0-4-4l-.8.8M9.2 6.8a2.8 2.8 0 0 0-4 0l-2 2a2.8 2.8 0 0 0 4 4l.8-.8'),
    'form': ('stroke', 'M1.5 4.5h13v7h-13zM4.5 6.5v3'),
    'place': ('stroke', 'M2 2h2M6 2h2M10 2h2M14 2v2M14 6v2M14 10v2M14 14h-2M10 14H8M6 14H4M2 14v-2M2 10V8M2 6V4M8 5v6M5 8h6'),
    'layout': ('stroke', 'M2 2h12v12H2zM7 2v12M7 8h7'),
    'spacing': ('stroke', 'M5.5 5.5h5v5h-5zM2 2h2M6 2h4M12 2h2v2M14 6v4M14 12v2h-2M10 14H6M4 14H2v-2M2 10V6M2 4V2'),
    'transform': ('stroke', 'M2.5 7.5h6v6h-6zM8 2.5a5.5 5.5 0 0 1 5.5 5.5M11.5 6.5l2 1.5 1.5-2'),
    'gradient': ('stroke', 'M2 2h12v12H2zM2 10l8-8M2 14L14 2M6 14l8-8'),
    'eyedropper': ('stroke', 'M10.5 2.5l3 3-2 2-3-3zM9 4.5l-6 6V13h2.5l6-6'),
    'measure': ('stroke', 'M1.5 5h13v6h-13zM4.5 5v2.5M7.5 5v1.5M10.5 5v2.5'),
    'hand': ('stroke', 'M5 8.5V4a1 1 0 0 1 2 0v3.5M7 7V3a1 1 0 0 1 2 0v4M9 7V4a1 1 0 0 1 2 0v4M11 8V6a1 1 0 0 1 2 0v4a4.5 4.5 0 0 1-4.5 4.5H8a4.5 4.5 0 0 1-3.6-1.8L2.6 10.2a1 1 0 0 1 1.6-1.2L5 10'),
    'zoom': ('stroke', 'M11.5 7a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0zM10.5 10.5L14 14'),
    # generic
    'chev-down': ('stroke', 'M4 6l4 4 4-4'), 'chev-right': ('stroke', 'M6 4l4 4-4 4'),
    'chev-up': ('stroke', 'M4 10l4-4 4 4'), 'chev-left': ('stroke', 'M10 4L6 8l4 4'),
    'close': ('stroke', 'M4 4l8 8M12 4l-8 8'), 'plus': ('stroke', 'M8 3v10M3 8h10'), 'minus': ('stroke', 'M3 8h10'),
    'check': ('stroke', 'M3 8.5l3 3 7-7'),
    'eye': ('stroke', 'M1.5 8S4 3.5 8 3.5 14.5 8 14.5 8 12 12.5 8 12.5 1.5 8 1.5 8zM10 8a2 2 0 1 1-4 0 2 2 0 0 1 4 0z'),
    'eye-off': ('stroke', 'M1.5 8S4 3.5 8 3.5 14.5 8 14.5 8 12 12.5 8 12.5 1.5 8 1.5 8zM2 2l12 12'),
    'lock': ('stroke', 'M3.5 7.5h9v6h-9zM5.5 7.5V5a2.5 2.5 0 0 1 5 0v2.5'),
    'unlock': ('stroke', 'M3.5 7.5h9v6h-9zM5.5 7.5V5a2.5 2.5 0 0 1 4.9-.7'),
    'trash': ('stroke', 'M2.5 4h11M6 4V2.5h4V4M4 4l.7 9.5h6.6L12 4'),
    'gear': ('stroke', 'M6.9 1.5h2.2l.4 1.8 1.2.5 1.6-1 1.5 1.5-1 1.6.5 1.2 1.8.4v2.2l-1.8.4-.5 1.2 1 1.6-1.5 1.5-1.6-1-1.2.5-.4 1.8H6.9l-.4-1.8-1.2-.5-1.6 1-1.5-1.5 1-1.6-.5-1.2-1.8-.4V6.9l1.8-.4.5-1.2-1-1.6 1.5-1.5 1.6 1 1.2-.5zM10.2 8a2.2 2.2 0 1 1-4.4 0 2.2 2.2 0 0 1 4.4 0z'),
    'play': ('fill', 'M4.5 2.5l9 5.5-9 5.5z'),
    'search': ('stroke', 'M11.5 7a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0zM10.5 10.5L14 14'),
    'more': ('fill', 'M4.8 8a1.3 1.3 0 1 1-2.6 0 1.3 1.3 0 0 1 2.6 0zM9.3 8a1.3 1.3 0 1 1-2.6 0 1.3 1.3 0 0 1 2.6 0zM13.8 8a1.3 1.3 0 1 1-2.6 0 1.3 1.3 0 0 1 2.6 0z'),
    'undo': ('stroke', 'M5.5 3.5l-3 3 3 3M2.5 6.5H10a3.5 3.5 0 0 1 0 7H7'),
    'redo': ('stroke', 'M10.5 3.5l3 3-3 3M13.5 6.5H6a3.5 3.5 0 0 0 0 7h3'),
    'desktop': ('stroke', 'M1.5 2.5h13v8.5h-13zM5.5 14h5M8 11v3'), 'tablet': ('stroke', 'M3.5 1.5h9v13h-9zM7 12.5h2'),
    'phone': ('stroke', 'M5 1.5h6v13H5zM7.5 12.5h1'), 'wide': ('stroke', 'M.5 3.5h15v7H.5zM5.5 13.5h5M8 10.5v3'),
    'warning': ('stroke', 'M8 2l6.5 11.5h-13zM8 6.5v3M8 11.6v.01'),
    'info': ('stroke', 'M14.5 8a6.5 6.5 0 1 1-13 0 6.5 6.5 0 0 1 13 0zM8 7.5v3.5M8 5v.01'),
    'folder': ('stroke', 'M1.5 4V13h13V5.5H8L6.5 3.5h-5z'),
    'file': ('stroke', 'M9.5 1.5H3.5v13h9V4.5zM9.5 1.5v3h3'),
    'code': ('stroke', 'M5.5 4.5L2 8l3.5 3.5M10.5 4.5L14 8l-3.5 3.5'),
    'sliders': ('stroke', 'M2.5 4.5h7M12.5 4.5h1M2.5 11.5h1M6.5 11.5h7M12.5 4.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zM6.5 11.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z'),
    'swap': ('stroke', 'M3 6h10l-3-3M13 10H3l3 3'),
    'upload': ('stroke', 'M8 10V2.5M5 5.5l3-3 3 3M3 10v3.5h10V10'),
    'grip': ('fill', 'M6.5 4a1 1 0 1 1-2 0 1 1 0 0 1 2 0zM11.5 4a1 1 0 1 1-2 0 1 1 0 0 1 2 0zM6.5 8a1 1 0 1 1-2 0 1 1 0 0 1 2 0zM11.5 8a1 1 0 1 1-2 0 1 1 0 0 1 2 0zM6.5 12a1 1 0 1 1-2 0 1 1 0 0 1 2 0zM11.5 12a1 1 0 1 1-2 0 1 1 0 0 1 2 0z'),
    'menu': ('stroke', 'M2.5 4h11M2.5 8h11M2.5 12h11'),
    'outline': ('stroke', 'M2.5 4h11M5 8h8.5M7.5 12h6'),
    'corners': ('stroke', 'M3 6V5a2 2 0 0 1 2-2h1M10 3h1a2 2 0 0 1 2 2v1M13 10v1a2 2 0 0 1-2 2h-1M6 13H5a2 2 0 0 1-2-2v-1'),
    'radius': ('stroke', 'M3 13V8a5 5 0 0 1 5-5h5'),
    'external': ('stroke', 'M9 2.5h4.5V7M13.5 2.5L7 9M11 9.5v4H2.5V5h4'),
    'copy': ('stroke', 'M5 5h8.5v8.5H5zM3 11V2.5h8.5'),
    'new-page': ('stroke', 'M9.5 1.5H4v13h8V4zM9.5 1.5V4H12M8 7.5v4M6 9.5h4'),
    'snap': ('stroke', 'M4 2.5v6a4 4 0 0 0 8 0v-6M4 5.5h3M9 5.5h3'),
    'flow': ('stroke', 'M3 3h10M3 8h10M3 13h6'),
    'free': ('stroke', 'M8 1.5l6.5 6.5L8 14.5 1.5 8z'),
    # element types
    't-section': ('stroke', 'M1.5 4.5h13v7h-13z'), 't-para': ('stroke', 'M7 13V3h5M10 3v10M7 3a2.5 2.5 0 0 0 0 5'),
    't-heading': ('stroke', 'M3 3.5h10M8 3.5V13'), 't-image': ('stroke', 'M2.5 3.5h11v9h-11zM2.5 11l3.5-3.5 3 3 1.5-1.5 3 3'),
    't-button': ('stroke', 'M4.5 4.5h7a3.5 3.5 0 0 1 0 7h-7a3.5 3.5 0 0 1 0-7z'),
    't-grid': ('stroke', 'M2.5 2.5h4.5v4.5H2.5zM9 2.5h4.5v4.5H9zM2.5 9h4.5v4.5H2.5zM9 9h4.5v4.5H9z'),
    't-stack': ('stroke', 'M3 3h10v4H3zM3 9h10v4H3z'), 't-row': ('stroke', 'M3 4v8M8 4v8M13 4v8'),
    't-link': ('stroke', 'M6.8 9.2a2.8 2.8 0 0 0 4 0l2-2a2.8 2.8 0 0 0-4-4l-.8.8M9.2 6.8a2.8 2.8 0 0 0-4 0l-2 2a2.8 2.8 0 0 0 4 4l.8-.8'),
    't-field': ('stroke', 'M1.5 4.5h13v7h-13zM4.5 6.5v3'), 't-list': ('stroke', 'M6 4h7.5M6 8h7.5M6 12h7.5M2.5 4h.01M2.5 8h.01M2.5 12h.01'),
    't-table': ('stroke', 'M2 3h12v10H2zM2 6.5h12M6.5 3v10'), 't-embed': ('stroke', 'M2 3h12v10H2zM6 6.5L4.5 8 6 9.5M10 6.5l1.5 1.5-1.5 1.5'),
}


def icon(name, size=16, color='currentColor', sw=1.5, label=None):
    kind, d = P[name]
    a11y = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    if kind == 'fill':
        return f'<svg width="{size}" height="{size}" viewBox="0 0 16 16" fill="{color}" {a11y}><path d="{d}"></path></svg>'
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 16 16" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" {a11y}><path d="{d}"></path></svg>')


def page(title, w, h, body, extra_css=''):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>
body{{margin:0}}
button{{font:inherit;color:inherit;background:none;border:0;padding:0;margin:0;cursor:default}}
{extra_css}
</style>
</helmet>
<div style="width: {w}px; height: {h}px; box-sizing: border-box; padding: 64px; overflow: hidden; background: #1f1f1f; color: #e8e8e8; font-family: 'Inter', system-ui, sans-serif; font-size: 12px; line-height: 16px; font-variant-numeric: tabular-nums">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''


def sheet_header(code, title, subtitle):
    return f'''<header style="display: flex; align-items: flex-end; gap: 16px; padding-bottom: 24px; margin-bottom: 40px; border-bottom: 1px solid #303030">
<span style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 8px; background: #141414; box-shadow: inset 0 0 0 1px #2e2e2e">{daisy(24)}</span>
<div style="flex: 1">
<div style="font-family: {MONO}; font-size: 11px; color: #939393">{code} · Daisy design system · v0.2</div>
<h1 style="margin: 2px 0 0; font-size: 28px; line-height: 36px; font-weight: 600">{title}</h1>
</div>
<div style="max-width: 560px; text-align: right; font-size: 12px; line-height: 18px; color: #a8a8a8">{subtitle}</div>
</header>'''


def daisy(size=18):
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 18 18" aria-hidden="true"><g fill="#e8e8e8"><ellipse cx="9" cy="4" rx="1.9" ry="3"></ellipse><ellipse cx="9" cy="14" rx="1.9" ry="3"></ellipse><ellipse cx="4" cy="9" rx="3" ry="1.9"></ellipse><ellipse cx="14" cy="9" rx="3" ry="1.9"></ellipse><ellipse cx="5.5" cy="5.5" rx="1.7" ry="2.7" transform="rotate(-45 5.5 5.5)"></ellipse><ellipse cx="12.5" cy="12.5" rx="1.7" ry="2.7" transform="rotate(-45 12.5 12.5)"></ellipse><ellipse cx="12.5" cy="5.5" rx="1.7" ry="2.7" transform="rotate(45 12.5 5.5)"></ellipse><ellipse cx="5.5" cy="12.5" rx="1.7" ry="2.7" transform="rotate(45 5.5 12.5)"></ellipse></g><circle cx="9" cy="9" r="2.6" fill="#f2b84b"></circle></svg>'''


def section(code, title, desc, inner, mb=56):
    return f'''<section style="margin-bottom: {mb}px">
<div style="display: flex; align-items: baseline; gap: 12px; margin-bottom: 16px">
<span style="font-family: {MONO}; font-size: 11px; color: #939393">{code}</span>
<h2 style="margin: 0; font-size: 16px; line-height: 24px; font-weight: 600">{title}</h2>
<span style="font-size: 12px; color: #939393">{desc}</span>
</div>
{inner}
</section>'''


def cell(label, inner, w=None, minh=56, align='center'):
    ws = f'width: {w}px;' if w else ''
    return f'''<div style="{ws} display: flex; flex-direction: column; gap: 8px">
<div style="min-height: {minh}px; display: flex; align-items: center; justify-content: {align}; padding: 12px; box-sizing: border-box; background: #1a1a1a; border-radius: 6px; box-shadow: inset 0 0 0 1px #2a2a2a">{inner}</div>
<div style="font-size: 10px; line-height: 14px; color: #939393; text-align: center">{label}</div>
</div>'''


def grid(cols, inner, gap=16, colw=None):
    tpl = f'repeat({cols}, {colw}px)' if colw else f'repeat({cols}, minmax(0, 1fr))'
    return f'<div style="display: grid; grid-template-columns: {tpl}; gap: {gap}px; align-items: start">{inner}</div>'
