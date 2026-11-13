"""Shared pieces for setting up a design system (New project dialog, D-36b)."""
import sys
sys.path.insert(0, '/home/claude/ds')
from lib import *

MONO_ = "font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 11px"
lbl = lambda t: f'<span style="font-size: 11px; color: #a8a8a8">{t}</span>'
fld = lambda inner, focus=False: f'<span style="height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 8px; box-sizing: border-box; background: #2a2a2a; border-radius: 2px; {"box-shadow: inset 0 0 0 1px #2f80ed;" if focus else ""}">{inner}</span>'
colf = lambda name, c, focus=False: f'<label style="display: flex; flex-direction: column; gap: 6px">{lbl(name)}{fld(f"<span style=\"width: 14px; height: 14px; border-radius: 2px; background: {c}; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.12)\"></span><span style=\"{MONO_}\">{c[1:].upper()}</span>", focus)}</label>'
dd = lambda name, v, ff='Inter, sans-serif': f'<label style="display: flex; flex-direction: column; gap: 6px">{lbl(name)}{fld(f"<span style=\"flex: 1; font-family: {ff}\">{v}</span>" + icon("chev-down", 10, "#939393", 1.75))}</label>'
def seg(items, sel):
    return ('<div role="group" style="display: grid; grid-template-columns: repeat(' + str(len(items)) + ', minmax(0, 1fr)); gap: 2px; padding: 2px; background: #1f1f1f; border-radius: 4px">'
            + ''.join(f'<button aria-pressed="{str(i == sel).lower()}" style="height: 24px; display: flex; align-items: center; justify-content: center; gap: 6px; border-radius: 3px; {"background: #3a3a3a; color: #e8e8e8; font-weight: 500;" if i == sel else "color: #939393;"}">{t}</button>' for i, t in enumerate(items)) + '</div>')
corner = lambda r: f'<span style="width: 12px; height: 9px; border: 1.5px solid currentColor; border-radius: {r}px"></span>'
chips = lambda cs: '<span style="display: flex; gap: 3px">' + ''.join(f'<span style="width: 14px; height: 14px; border-radius: 3px; background: {c}; box-shadow: inset 0 0 0 1px rgba(0,0,0,0.12)"></span>' for c in cs) + '</span>'

DEF = dict(brand='#3d63dd', ink='#1b1b1f', bg='#ffffff', head='Inter', body='Inter', size=1, corners=1, space=1)
GEN = ['#3d63dd', '#2f4fb8', '#6f8ce8', '#1b1b1f', '#55565c', '#ffffff', '#f4f5f8', '#e2e4ea']

def setup_form(o=DEF, gen=GEN, focus='brand', preview_w=220):
    hf = "'Fraunces', serif" if o['head'] == 'Fraunces' else 'Inter, sans-serif'
    rad = [2, 8, 16][o['corners']]
    left = f'''<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 12px">
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px">{colf('Brand colour', o['brand'], focus == 'brand')}{colf('Text', o['ink'])}{colf('Background', o['bg'])}</div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">{dd('Headings', o['head'], hf)}{dd('Body text', o['body'])}</div>
<div style="display: flex; flex-direction: column; gap: 6px">{lbl('Text size')}{seg(['Small · 15', 'Regular · 16', 'Large · 18'], o['size'])}</div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">
<div style="display: flex; flex-direction: column; gap: 6px">{lbl('Corners')}{seg([corner(0) + 'Sharp', corner(3) + 'Soft', corner(6) + 'Round'], o['corners'])}</div>
<div style="display: flex; flex-direction: column; gap: 6px">{lbl('Spacing')}{seg(['Tight', 'Regular', 'Roomy'], o['space'])}</div></div>
</div>'''
    prev = f'''<div style="width: {preview_w}px; flex: none; display: flex; flex-direction: column; gap: 8px">
{lbl('Preview')}
<div style="padding: 16px; border-radius: 4px; background: {o['bg']}; color: {o['ink']}; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.08); display: flex; flex-direction: column; gap: 8px">
<span style="font-family: {hf}; font-size: 22px; line-height: 1.1; font-weight: 600">Your first heading</span>
<span style="font-size: 11px; line-height: 1.5; color: {gen[4]}">Body text reads like this, at the size you chose.</span>
<span style="display: flex; gap: 6px; margin-top: 4px"><span style="height: 24px; display: flex; align-items: center; padding: 0 12px; border-radius: {rad}px; background: {o['brand']}; color: #ffffff; font-size: 11px; font-weight: 500">Button</span><span style="height: 24px; display: flex; align-items: center; padding: 0 12px; border-radius: {rad}px; box-shadow: inset 0 0 0 1px {gen[7]}; font-size: 11px">Second</span></span></div>
{chips(gen)}
<span style="font-size: 11px; line-height: 16px; color: #939393">8 colours, 5 text styles, 4 radius and 8 spacing tokens</span>
</div>'''
    return f'<div style="display: flex; gap: 20px">{left}{prev}</div>'

def choice(sel):
    return seg(['Set up now', 'Copy from a project…', 'Skip for now'], sel)
