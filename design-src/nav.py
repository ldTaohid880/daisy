import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *


def row(cid, name, anatomy, cells):
    cs = ''.join(f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 10px; min-width: 96px">
<div style="min-height: 48px; display: flex; align-items: center; justify-content: center">{inner}</div>
<span style="font-size: 10px; line-height: 14px; color: #939393; text-align: center">{lab}</span></div>''' for lab, inner in cells)
    return f'''<div style="display: grid; grid-template-columns: 260px 1fr; gap: 32px; padding: 20px 0; border-bottom: 1px solid #262626; align-items: center">
<div><div style="font-family: {MONO}; font-size: 11px; color: #939393">{cid}</div><div style="font-weight: 600; margin: 2px 0 4px">{name}</div><div style="font-size: 11px; line-height: 16px; color: #939393">{anatomy}</div></div>
<div style="display: flex; flex-wrap: wrap; gap: 24px 28px; align-items: flex-start">{cs}</div>
</div>'''


FLOAT = 'background: #262626; border: 1px solid #454545; box-shadow: 0 8px 24px rgba(0,0,0,0.45);'


# C-16 menu
def mrow(label, state='rest', key='', ic=None, sub=False):
    bg = 'background: #323232;' if state == 'hover' else ''
    col = {'disabled': '#4f4f4f', 'danger': '#f85149'}.get(state, '#e8e8e8')
    left = icon('check', 12, '#e8e8e8') if state == 'checked' else (icon(ic, 14, '#a8a8a8' if state != 'danger' else '#f85149') if ic else '')
    right = icon('chev-right', 12, '#939393') if sub else f'<span style="font-size: 11px; color: #939393">{key}</span>'
    return f'<span style="height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 8px; border-radius: 3px; color: {col}; {bg}"><span style="width: 16px; display: flex; justify-content: center">{left}</span><span style="flex: 1">{label}</span>{right}</span>'


sep = '<span style="height: 1px; margin: 4px 0; background: #333333; display: block"></span>'
menu = f'''<span style="position: relative; display: block; width: 240px; padding: 4px; box-sizing: border-box; border-radius: 4px; {FLOAT}">
{mrow('Copy', 'rest', 'Ctrl+C', 'copy')}{mrow('Duplicate', 'hover', 'Ctrl+D')}{mrow('Paste inside', 'disabled', 'Ctrl+Shift+V')}{sep}
{mrow('Snap to guides', 'checked')}{mrow('Placement', 'rest', '', None, True)}{sep}{mrow('Delete', 'danger', 'Del', 'trash')}
<span style="position: absolute; left: 244px; top: 120px; width: 180px; padding: 4px; box-sizing: border-box; border-radius: 4px; {FLOAT}">{mrow('In flow', 'checked')}{mrow('Free', 'hover')}{mrow('Fixed to screen')}{mrow('Sticks when scrolling')}</span>
</span>'''

popover = f'''<span style="display: flex; flex-direction: column; gap: 12px; width: 320px; padding: 12px; box-sizing: border-box; border-radius: 6px; {FLOAT}">
<span style="display: flex; align-items: center; justify-content: space-between"><span style="font-weight: 600">Where should this go?</span><button aria-label="Close" style="width: 20px; height: 20px; display: flex; align-items: center; justify-content: center; border-radius: 3px; color: #a8a8a8">{icon('close', 12)}</button></span>
<span style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 2px; padding: 2px; background: #1f1f1f; border-radius: 4px; font-size: 11px"><button style="height: 20px; border-radius: 3px; color: #939393">Web address</button><button style="height: 20px; border-radius: 3px; background: #3a3a3a">Section</button><button style="height: 20px; border-radius: 3px; color: #939393">Email</button></span>
<span style="height: 24px; display: flex; align-items: center; justify-content: space-between; padding: 0 6px; background: #2a2a2a; border-radius: 2px">This season{icon('chev-down', 10, '#939393', 1.75)}</span>
</span>'''

tooltip = f'''<span style="display: flex; flex-direction: column; gap: 2px; max-width: 260px; padding: 6px 8px; border-radius: 4px; {FLOAT}">
<span>Space between</span><span style="font-family: {MONO}; font-size: 11px; color: #939393">gap · 64px</span></span>'''

dialog = f'''<span style="display: flex; flex-direction: column; width: 400px; border-radius: 4px; {FLOAT}">
<span style="height: 44px; display: flex; align-items: center; justify-content: space-between; padding: 0 16px; border-bottom: 1px solid #333333"><span style="font-size: 14px; line-height: 20px; font-weight: 600">New project</span><button aria-label="Close" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; color: #a8a8a8">{icon('close', 12)}</button></span>
<span style="display: flex; flex-direction: column; gap: 6px; padding: 16px"><span style="font-size: 11px; color: #a8a8a8">Name</span><span style="height: 24px; display: flex; align-items: center; padding: 0 6px; background: #2a2a2a; border-radius: 2px; box-shadow: inset 0 0 0 1px #2f80ed"><span style="background: rgba(47,128,237,0.35)">Untitled project</span></span><span style="font-size: 11px; color: #939393">Enter to create</span></span>
<span style="height: 52px; display: flex; align-items: center; justify-content: flex-end; gap: 8px; padding: 0 16px; border-top: 1px solid #333333">
<button style="height: 24px; padding: 0 12px; border-radius: 4px; background: #2a2a2a; box-shadow: inset 0 0 0 1px #454545; font-weight: 500">Cancel</button><button style="height: 24px; padding: 0 12px; border-radius: 4px; background: #246bcb; color: #fff; font-weight: 500">Create</button></span>
</span>'''


def tabs(active=0, hover=None, focus=None):
    out = ''
    for i, t in enumerate(['Layers', 'Elements', 'Assets']):
        col = '#e8e8e8' if i in (active, hover) else '#a8a8a8'
        under = '<span style="position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: #2f80ed"></span>' if i == active else ''
        f = 'border-radius: 2px; ' + FOCUS + ';' if i == focus else ''
        out += f'<button style="position: relative; height: 31px; font-weight: 500; color: {col}; {f}">{t}{under}</button>'
    return f'<span style="width: 236px; height: 32px; display: flex; gap: 16px; padding: 0 12px; box-sizing: border-box; background: #1f1f1f; border-bottom: 1px solid #303030">{out}</span>'


ADV = 'M2.5 4.5h7M12.5 4.5h1M2.5 11.5h1M6.5 11.5h7M12.5 4.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zM6.5 11.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z'


def ghead(state):
    adv_style = 'color: #939393;'
    dot = ''
    warn = ''
    bg = ''
    if state == 'hover':
        bg = 'background: #232323;'
    if state == 'advanced open':
        adv_style = 'background: #3a3a3a; color: #e8e8e8;'
    if state == 'with dot':
        dot = '<span style="position: absolute; right: 3px; top: 3px; width: 5px; height: 5px; border-radius: 3px; background: #2f80ed"></span>'
    if state == 'with warning':
        warn = icon('warning', 12, '#d29922', 1.25, 'Accessibility issue')
    f = FOCUS + ';' if state == 'focus' else ''
    return f'''<span style="width: 260px; height: 28px; display: flex; align-items: center; gap: 6px; padding: 0 8px 0 12px; box-sizing: border-box; background: #1f1f1f; {bg}">
<span style="flex: 1; font-weight: 600; display: flex; align-items: center; gap: 6px">Typography{warn}</span>
<button aria-label="Advanced" style="position: relative; width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; {adv_style} {f}"><svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="{ADV}"></path></svg>{dot}</button></span>'''


def omark(kind):
    st = {'set here': 'background: #2f80ed;', 'from screen size': 'box-shadow: inset 0 0 0 1.25px #d29922;',
          'from parent': 'box-shadow: inset 0 0 0 1.25px #939393;', 'none': ''}[kind]
    return f'<span style="width: 150px; height: 24px; box-sizing: border-box; display: flex; align-items: center; gap: 6px; padding: 0 6px; background: #2a2a2a; border-radius: 2px"><span style="width: 6px; height: 6px; border-radius: 3px; flex: none; {st}"></span><span style="font-size: 11px; color: #939393">Size</span><span style="flex: 1">{"48" if kind != "none" else "<span style=\"color: #939393\">16</span>"}</span><span style="font-size: 10px; color: #939393">px</span></span>'


def chip(text, kind):
    st = {'neutral': 'background: #3a3a3a; color: #a8a8a8;', 'resp': 'background: rgba(210,153,34,0.16); color: #e3b34a;',
          'state': 'background: rgba(163,113,247,0.18); color: #c4a5fa;', 'warning': 'background: rgba(210,153,34,0.16); color: #e3b34a;',
          'danger': 'background: rgba(248,81,73,0.16); color: #ff7b72;'}[kind]
    x = f'<span style="display: flex; margin-left: 2px">{icon("close", 10, "currentColor", 1.75)}</span>' if kind in ('resp', 'state') else ''
    return f'<span style="height: 20px; display: inline-flex; align-items: center; gap: 4px; padding: 0 8px; border-radius: 10px; font-size: 11px; font-weight: 500; white-space: nowrap; {st}">{text}{x}</span>'


for c in ('#e3b34a', '#c4a5fa', '#ff7b72'):
    assert contrast(c, '#262626') >= 4.5, (c, contrast(c, '#262626'))


def trow(state):
    pad = 'padding: 0 12px 0 44px;'
    guides = 'background-image: linear-gradient(#262626,#262626), linear-gradient(#262626,#262626); background-size: 1px 100%, 1px 100%; background-position: 14px 0, 26px 0; background-repeat: no-repeat;'
    name = 'Hero image'
    right = '<span style="font-size: 11px; color: #939393">img</span>'
    extra = ''
    bg = ''
    op = ''
    col = '#e8e8e8'
    ic_col = '#a8a8a8'
    if state == 'hover':
        bg = 'background-color: #262626;'
        right = f'<span style="display: flex; gap: 4px; color: #a8a8a8">{icon("eye", 14)}{icon("unlock", 14)}</span>'
    elif state == 'selected':
        bg = 'background-color: rgba(47,128,237,0.18);'
        ic_col = '#e8e8e8'
    elif state == 'selected-unfocused':
        bg = 'background-color: #3a3a3a;'
    elif state == 'hidden':
        op = 'opacity: 0.45;'
        right = f'<span style="color: #a8a8a8">{icon("eye-off", 14)}</span>'
    elif state == 'locked':
        right = f'<span style="color: #a8a8a8">{icon("lock", 14)}</span>'
    elif state == 'drop-between':
        extra = '<span style="position: absolute; left: 44px; right: 8px; top: -1px; height: 2px; background: #2f80ed"></span><span style="position: absolute; left: 40px; top: -3px; width: 6px; height: 6px; box-sizing: border-box; border: 1.5px solid #2f80ed; border-radius: 3px; background: #1f1f1f"></span>'
    elif state == 'drop-inside':
        bg = 'background-color: rgba(47,128,237,0.18); box-shadow: inset 0 0 0 1px #2f80ed;'
        name = 'Hero text'
    elif state == 'invalid':
        extra = '<span style="position: absolute; left: 44px; right: 8px; top: -1px; height: 2px; background: #f85149"></span>'
    elif state == 'renaming':
        name = f'<span style="flex: 1; height: 20px; display: flex; align-items: center; padding: 0 4px; background: #2a2a2a; border-radius: 2px; box-shadow: inset 0 0 0 1px #2f80ed"><span style="background: rgba(47,128,237,0.35)">Hero image</span></span>'
    elif state == 'focus':
        bg = FOCUS + ';'
    nm = name if state == 'renaming' else f'<span style="flex: 1; color: {col}">{name}</span>'
    return f'<span style="position: relative; width: 240px; height: 24px; display: flex; align-items: center; gap: 4px; box-sizing: border-box; {pad} {guides} {bg} {op}">{extra}<span style="width: 12px"></span>{icon("t-image", 14, ic_col)}{nm}{right}</span>'


def crumb(state):
    segs = ['Page', 'Section · Hero', 'Box · Hero text', 'Heading · h1']
    out = ''
    for i, s in enumerate(segs):
        col = '#e8e8e8' if i == len(segs) - 1 else '#a8a8a8'
        st = ''
        if state == 'hover' and i == 1:
            st = 'color: #e8e8e8; text-decoration: underline; text-underline-offset: 2px;'
        if state == 'focus' and i == 2:
            st = 'border-radius: 2px; ' + FOCUS + ';'
        out += f'<button style="color: {col}; {st}">{s}</button>' + ('<span style="color: #6b6b6b">›</span>' if i < len(segs) - 1 else '')
    return f'<span style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px; background: #181818; font-size: 11px">{out}</span>'


def notice(kind):
    col = '#58a6ff' if kind == 'info' else '#e3b34a'
    ic = 'info' if kind == 'info' else 'warning'
    txt = 'Changed Hero to Column so its children can be aligned' if kind == 'info' else 'Hero image needs a description'
    act = 'Undo' if kind == 'info' else 'Fix'
    return f'<span style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 12px; background: #181818; font-size: 11px; color: {col}">{icon(ic, 12, col, 1.25)}{txt} · <button style="text-decoration: underline; text-underline-offset: 2px; color: #e8e8e8">{act}</button></span>'


hint = f'<span style="width: 276px; display: flex; align-items: center; gap: 6px; font-size: 11px; color: #58a6ff">{icon("info", 12, "#58a6ff", 1.25)}<span style="flex: 1">Row places children side by side.</span><button aria-label="Dismiss for good" style="width: 18px; height: 18px; display: flex; align-items: center; justify-content: center; border-radius: 3px; color: #a8a8a8">{icon("close", 10, "currentColor", 1.75)}</button></span>'


def swt(state):
    if state == 'add tile':
        return f'<button aria-label="Add from selection" style="width: 24px; height: 24px; box-sizing: border-box; border-radius: 2px; border: 1px dashed #454545; color: #a8a8a8; display: flex; align-items: center; justify-content: center">{icon("plus", 12)}</button>'
    st = {'rest': '', 'hover': 'transform: scale(1.08);', 'selected': 'outline: 2px solid #2f80ed; outline-offset: 1px;', 'light colour': 'box-shadow: inset 0 0 0 1px rgba(0,0,0,0.25);', 'focus': FOCUS + ';'}[state]
    bg = '#f6f1ea' if state == 'light colour' else '#b5532d'
    tip = f'<span style="position: absolute; left: -26px; top: -34px; padding: 4px 6px; border-radius: 4px; white-space: nowrap; font-size: 11px; {FLOAT}">brand · <span style="font-family: {MONO}">#b5532d</span></span>' if state == 'hover' else ''
    return f'<span style="position: relative"><button aria-label="brand" style="width: 24px; height: 24px; border-radius: 2px; background: {bg}; {st}"></button>{tip}</span>'


def lrow(state):
    bg = ''
    grip = '<span style="width: 12px"></span>'
    op = ''
    eye = icon('eye', 14, '#a8a8a8')
    if state == 'hover':
        bg = 'background: #262626;'
        grip = f'<span style="color: #939393">{icon("grip", 12)}</span>'
    if state == 'dragging':
        bg = f'background: #2a2a2a; {FLOAT.split(";")[2]};'
        grip = f'<span style="color: #e8e8e8">{icon("grip", 12)}</span>'
    if state == 'hidden':
        op = 'opacity: 0.45;'
        eye = icon('eye-off', 14, '#a8a8a8')
    return f'<span style="width: 260px; height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 8px; box-sizing: border-box; border-radius: 2px; {bg} {op}">{grip}<span style="width: 20px; height: 20px; border-radius: 2px; background: #b5532d; flex: none"></span><span style="flex: 1">Colour</span><span style="font-family: {MONO}; font-size: 11px; color: #939393">#b5532d</span>{eye}<span style="color: #a8a8a8">{icon("more", 14)}</span></span>'


empty = f'<span style="width: 236px; display: flex; flex-direction: column; align-items: center; gap: 10px; padding: 20px 12px; box-sizing: border-box; background: #1f1f1f; border: 1px dashed #454545; border-radius: 4px; text-align: center"><span style="color: #939393">{icon("upload", 32, sw=1.25)}</span><span style="color: #a8a8a8">Drop images, video or fonts here</span><button style="height: 24px; padding: 0 12px; border-radius: 4px; background: #2a2a2a; box-shadow: inset 0 0 0 1px #454545; font-weight: 500">Upload</button></span>'


def ptab(state):
    base = 'position: relative; height: 32px; box-sizing: border-box; display: flex; align-items: center; gap: 8px; padding: 0 8px 0 12px;'
    name, file = 'Shop', 'shop.html'
    right = '<span style="width: 18px; height: 18px"></span>'
    bg = 'background: #181818;'
    col = '#a8a8a8'
    top = ''
    lead = ''
    if state in ('active', 'focus'):
        bg, col = 'background: #2a2a2a;', '#e8e8e8'
        top = '<span style="position: absolute; left: 0; right: 0; top: 0; height: 2px; background: #2f80ed"></span>'
        name, file = 'Home', 'index.html @ 85%'
        right = f'<span style="width: 18px; height: 18px; display: flex; align-items: center; justify-content: center; border-radius: 3px; color: #a8a8a8">{icon("close", 10, "currentColor", 2)}</span>'
    if state == 'hover':
        bg, col = 'background: #1f1f1f;', '#e8e8e8'
        right = f'<span style="width: 18px; height: 18px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: #323232; color: #e8e8e8">{icon("close", 10, "currentColor", 2)}</span>'
    if state == 'unsaved':
        right = '<span style="width: 18px; height: 18px; display: flex; align-items: center; justify-content: center"><span style="width: 7px; height: 7px; border-radius: 4px; background: #a8a8a8"></span></span>'
    if state == 'single file':
        name, file = '', 'promo-banner.html'
        lead = icon('file', 12)
    if state == 'dragging':
        bg = f'background: #262626; box-shadow: 0 8px 24px rgba(0,0,0,0.45); transform: rotate(-1.5deg);'
        col = '#e8e8e8'
    f = FOCUS + ';' if state == 'focus' else ''
    nm = f'<span style="font-weight: {500 if state in ("active", "focus") else 400}">{name}</span>' if name else ''
    return f'<span style="{base} {bg} color: {col}; {f}">{top}{lead}{nm}<span style="font-family: {MONO}; font-size: 11px; color: #939393">{file}</span>{right}</span>'


def search(state):
    ring = {'rest': 'box-shadow: inset 0 0 0 1px #2e2e2e;', 'hover': 'box-shadow: inset 0 0 0 1px #454545;', 'focus': 'box-shadow: inset 0 0 0 1px #2f80ed, 0 0 0 1px #141414, 0 0 0 3px rgba(47,128,237,0.45);'}[state]
    kb = '<span style="height: 18px; box-sizing: border-box; display: flex; align-items: center; padding: 0 5px; border-radius: 3px; background: #2a2a2a; box-shadow: inset 0 -1px 0 #3a3a3a; font-size: 10px; font-weight: 500; color: #a8a8a8">{}</span>'
    txt = 'Search <span style="color: #e8e8e8; font-weight: 500">Halden</span>' if state != 'focus' else '<span style="color: #e8e8e8">hero</span><span style="width: 1px; height: 14px; background: #e8e8e8; display: inline-block; vertical-align: middle"></span>'
    bar = f'<span style="width: 440px; height: 28px; box-sizing: border-box; display: flex; align-items: center; gap: 8px; padding: 0 6px 0 10px; border-radius: 6px; background: #1f1f1f; color: #939393; {ring}">{icon("search", 13, "currentColor", 1.75)}<span style="flex: 1">{txt}</span><span style="display: flex; gap: 2px">{kb.format("Ctrl")}{kb.format("P")}</span></span>'
    if state != 'focus':
        return f'<span style="padding: 6px; background: #141414; border-radius: 6px">{bar}</span>'

    def res(ic, t, meta, hi=False):
        return f'<span style="height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 8px; border-radius: 4px; {"background: #323232;" if hi else ""}">{icon(ic, 14, "#a8a8a8")}<span style="flex: 1">{t}</span><span style="font-size: 11px; color: #939393">{meta}</span></span>'
    cap = '<span style="display: block; padding: 6px 8px 2px; font-size: 10px; font-weight: 500; letter-spacing: 0.04em; color: #939393">{}</span>'
    drop = f'''<span style="display: block; width: 440px; margin-top: 6px; padding: 4px; box-sizing: border-box; border-radius: 6px; {FLOAT}">
{cap.format("LAYERS · HOME")}{res("t-heading", "<b style='font-weight: 500'>Hero</b> title", "h1 · Home", True)}{res("t-grid", "<b style='font-weight: 500'>Hero</b> grid", "div · Home")}{res("t-image", "<b style='font-weight: 500'>Hero</b> image", "img · Home")}
{cap.format("PAGES")}{res("file", "Home", "index.html")}
{cap.format("COMMANDS · TYPE &gt;")}{res("code", "Show code for selection", "Ctrl+`")}
</span>'''
    return f'<span style="display: block; padding: 6px; background: #141414; border-radius: 6px">{bar}{drop}</span>'


def tchip(tool, ic, key, temp=False):
    st = 'background: rgba(47,128,237,0.14);' if not temp else 'box-shadow: inset 0 0 0 1px #2f80ed; border: 0; background: transparent; outline: 1px dashed #2f80ed; outline-offset: -1px;'
    return f'<span style="height: 26px; display: inline-flex; align-items: center; gap: 8px; padding: 0 8px 0 7px; border-radius: 6px; {st}">{icon(ic, 14, "#2f80ed")}<span style="font-weight: 500">{tool}</span><span style="height: 16px; display: flex; align-items: center; padding: 0 4px; border-radius: 3px; background: rgba(47,128,237,0.22); font-size: 10px; font-weight: 600; color: #8fb8f5">{key}</span></span>'


def mprow(state):
    bg = ''
    col = '#a8a8a8'
    plus = ''
    val = '<span style="font-size: 11px; color: #939393">none</span>' if state != 'no value' else ''
    if state in ('hover', 'focus'):
        bg = 'background: #262626;'
        col = '#e8e8e8'
        plus = f'<span style="width: 18px; height: 18px; margin-left: 8px; display: flex; align-items: center; justify-content: center; border-radius: 3px; background: #333333; color: #e8e8e8">{icon("plus", 12, "currentColor", 1.75)}</span>'
    f = FOCUS + ';' if state == 'focus' else ''
    nm = 'Effects' if state == 'no value' else 'Fill'
    return f'<button style="width: 276px; height: 28px; display: flex; align-items: center; padding: 0 8px 0 12px; box-sizing: border-box; color: {col}; {bg} {f}"><span style="flex: 1; text-align: left">{nm}</span>{val}{plus}</button>'


body = sheet_header('D-00d', 'Navigation, panels and overlays', 'Floating layers, tabs, panel patterns, tree rows, status-bar messages and the v0.2 additions: page tab, search bar and More properties row.')
r = ''
r += row('C-16', 'Menu / context menu', 'bg-popover · 4 padding · 28 rows · icon column 16 · shortcut right in text-muted · submenu chevron. Keyboard focus moves the same hover highlight (arrow keys)', [('rest · hover · disabled · checked · submenu · danger', f'<span style="display: block; width: 430px; height: 230px">{menu}</span>')])
r += row('C-17 · C-18', 'Popover · Tooltip', 'Popover 320 (360 link) · 12 padding · radius 6. Tooltip max 260 · 6 × 8 · line 2 mono CSS name and value · 500 ms delay', [('popover', popover), ('tooltip', tooltip)])
r += row('C-19', 'Dialog', 'Title 44 · body 16 · footer 52, buttons right (secondary, primary) · over a 50% black scrim', [('New project · 400', dialog)])
r += row('C-20', 'Tabs', 'Text tabs 12 medium · 2 px accent underline on active', [('active', tabs()), ('hover', tabs(0, 1)), ('focus', tabs(0, None, 2))])
r += row('C-21', 'Group header + Advanced', 'Title 12 semibold · 24 px Advanced icon button (sliders) on the right', [(s, ghead(s)) for s in ('rest', 'hover', 'advanced open', 'with dot', 'with warning', 'focus')])
r += row('C-22', 'Origin marker', '6 px dot at the start of the field', [('set here', omark('set here')), ('from screen size', omark('from screen size')), ('from parent', omark('from parent')), ('none · computed', omark('none'))])
r += row('C-23', 'Chip / tag', '20 h pill · 11 medium · context chips have ×. Tinted text ≥ 4.5:1', [('neutral', chip('custom', 'neutral')), ('neutral', chip('inactive', 'neutral')), ('resp', chip('Editing: Tablet and smaller', 'resp')), ('state', chip('Editing: Mouse over', 'state')), ('warning', chip('1 needs attention', 'warning')), ('danger', chip('runs script', 'danger'))])
r += row('C-24', 'Tree row (Layers)', '24 h · indent 12 · guides line-subtle · hover shows eye and lock', [(s, trow(s)) for s in ('rest', 'hover', 'selected', 'selected-unfocused', 'hidden', 'locked', 'drop-between', 'drop-inside', 'invalid', 'renaming', 'focus')])
r += row('C-25', 'Breadcrumb', 'Status bar · 11 px · last segment text-primary · hover outlines the element on canvas', [(s, crumb(s)) for s in ('rest', 'hover', 'focus')])
r += row('C-26 · C-27', 'Notice · Inline hint', 'Notice replaces the status hint for 6 s, with an action. Hint: one line, × dismisses forever', [('notice · info', notice('info')), ('notice · warning', notice('warning')), ('inline hint', hint)])
r += row('C-28', 'Swatch tile', '24 square · radius 2 · inner border for light colours', [(s, swt(s)) for s in ('rest', 'hover', 'selected', 'light colour', 'focus', 'add tile')])
r += row('C-31', 'Layer / fill list row', '28 h · 20 preview · label · value · eye · ⋯ · grip on hover', [(s, lrow(s)) for s in ('rest', 'hover', 'dragging', 'hidden')] + [('focus', lrow('rest').replace('border-radius: 2px; ', 'border-radius: 2px; ' + FOCUS + '; ', 1))])
r += row('C-32', 'Empty state', '32 icon · one sentence · optional button', [('Assets, empty', empty)])
r += row('C-34', 'Page tab', '32 h · page name + mono file name · active joins the canvas with a 2 px accent top line', [(s, ptab(s)) for s in ('active', 'inactive', 'hover', 'unsaved', 'single file', 'dragging', 'focus')])
r += row('C-35', 'Search bar', '440 × 28 · radius 6 · project name in the placeholder · Ctrl P · > for commands', [('rest', search('rest')), ('hover', search('hover')), ('focus · results', search('focus'))])
r += row('C-37', 'More properties row', '28 h · value on the right · hover shows + · click opens the group', [(s, mprow(s)) for s in ('rest', 'no value', 'hover', 'focus')])
body += r

H = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
open('/home/claude/daisy/project/DS-Navigation.dc.html', 'w', encoding='utf-8').write(page('Daisy · D-00d Navigation, panels and overlays', 1920, H, body))
