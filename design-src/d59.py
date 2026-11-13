"""D-59 MCP: Preferences › AI tools and MCP · D-59b an AI tool working in the editor · D-59c MCP states."""
import sys
sys.path.insert(0, '/home/claude/ds')
from screen import *
_s = open('/home/claude/ds/d49.py').read(); PR = {}; exec(_s[:_s.index('# ═════ D-49 Preferences')], PR)
P['plug'] = ('stroke', 'M5.5 1.5v3M10.5 1.5v3M3.5 4.5h9v2.5a4.5 4.5 0 0 1-9 0zM8 11.5v3')
P['spark'] = ('stroke', 'M8 1.5l1.6 4.9 4.9 1.6-4.9 1.6L8 14.5l-1.6-4.9L1.5 8l4.9-1.6z')
P['keep'] = ('stroke', 'M5 2.5h6v5l2 2.5H3l2-2.5zM8 10v4')
P['copy'] = ('stroke', 'M5.5 5.5h8v8h-8zM2.5 10.5v-8h8')
P['server'] = ('stroke', 'M2.5 2.5h11v4.5h-11zM2.5 9h11v4.5h-11zM5 4.75h1M5 11.25h1')
vtab, segm, sw, dd, chk, modal, done = PR['vtab'], PR['segm'], PR['sw'], PR['dd'], PR['chk'], PR['modal'], PR['done']
sm = lambda t, c='#939393': f'<span style="font-size: 11px; line-height: 15px; color: {c}">{t}</span>'
pill = lambda t, c: f'<span style="height: 20px; display: inline-flex; align-items: center; gap: 6px; padding: 0 8px; border-radius: 10px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-size: 11px; color: #c8c8c8; white-space: nowrap"><span style="width: 6px; height: 6px; border-radius: 3px; background: {c}"></span>{t}</span>'
GREEN, AMBER, RED, GREY = '#3fb950', '#d29922', '#f85149', '#6b6b6b'
btn = lambda t, k='sec': f'<button style="height: 28px; padding: 0 12px; border-radius: 4px; white-space: nowrap; font-size: 12px; {"background: #246bcb; color: #fff; font-weight: 500;" if k == "pri" else ("color: #a8a8a8;" if k == "ghost" else ("box-shadow: inset 0 0 0 1px #454545; color: #ff938c;" if k == "danger" else "box-shadow: inset 0 0 0 1px #454545; color: #e8e8e8;"))}">{t}</button>'
mono = lambda t, w='': f'<span style="{w} height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 6px 0 10px; box-sizing: border-box; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px #3a3a3a; font-family: {MONO}; font-size: 11px; color: #c8c8c8"><span style="flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{t}</span><button aria-label="Copy" style="width: 22px; height: 22px; display: flex; align-items: center; justify-content: center; color: #939393">{icon("copy", 12)}</button></span>'
logo = lambda ch, bg: f'<span style="width: 28px; height: 28px; flex: none; display: flex; align-items: center; justify-content: center; border-radius: 6px; background: {bg}; color: #fff; font-size: 12px; font-weight: 700">{ch}</span>'
row = lambda label, ctl, d='': f'<div style="display: grid; grid-template-columns: 200px minmax(0, 1fr); gap: 16px; align-items: center; padding: 7px 0"><div style="display: flex; flex-direction: column; gap: 2px"><span>{label}</span>{sm(d) if d else ""}</div><div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap">{ctl}</div></div>'
sec = lambda t, d='': f'<div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #333333; display: flex; align-items: baseline; gap: 10px"><span style="font-size: 11px; font-weight: 500; letter-spacing: 0.04em; color: #939393">{t}</span>{sm(d)}</div>'
def item(lg, name, sub, status, right):
    return (f'<div style="height: 48px; display: grid; grid-template-columns: 28px minmax(0, 1fr) auto auto; gap: 12px; align-items: center; padding: 0 10px; border-radius: 6px; background: #2a2a2a">{lg}'
            f'<span style="display: flex; flex-direction: column; min-width: 0"><span style="font-weight: 500; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{name}</span><span style="font-size: 11px; color: #939393; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{sub}</span></span>{status}<span style="display: flex; gap: 6px">{right}</span></div>')

# ═════ D-59 Preferences › AI tools and MCP ═════
S = Screen('Daisy · D-59 AI tools and MCP')
nav = f'''<nav style="width: 210px; flex: none; padding: 12px 10px; box-sizing: border-box; display: flex; flex-direction: column; gap: 2px; border-right: 1px solid #3a3a3a; background: #222222">
{vtab('gear', 'General')}{vtab('palette', 'Appearance')}{vtab('cursor', 'Canvas and editing')}{vtab('code', 'Code')}{vtab('keyboard', 'Keyboard shortcuts')}{vtab('disk', 'Files and saving')}{vtab('plug', 'AI tools and MCP', True)}{vtab('shield', 'Privacy and updates')}
<div style="flex: 1"></div><div style="padding: 8px 10px; font-size: 11px; line-height: 15px; color: #939393">MCP is the open standard AI apps use to talk to tools. Nothing is shared until you turn it on.</div></nav>'''
clients = (item(logo('C', '#c96442'), 'Claude Code', 'Connected now · 14 changes today', pill('Connected', GREEN), dd('Ask before changes', 168) + btn('Disconnect', 'ghost'))
           + item(logo('Cu', '#3a3a3a'), 'Cursor', 'Last used yesterday · read the Home page', pill('Not connected', GREY), dd('Read only', 168) + btn('Remove', 'ghost')))
servers = (item(logo('S', '#1f7a52'), 'Supabase', '6 tools · used by Collections', pill('Ready', GREEN), btn('Tools') + btn('…', 'ghost'))
           + item(logo('U', '#2b2b2b'), 'Unsplash', '2 tools · used in Assets › Images', pill('Ready', GREEN), btn('Tools') + btn('…', 'ghost'))
           + item(logo('N', '#4a4a4a'), 'Notion', 'Sign-in expired on 9 Nov', pill('Needs sign-in', AMBER), btn('Sign in') + btn('…', 'ghost')))
main = f'''<div style="flex: 1; min-width: 0; padding: 18px 26px; box-sizing: border-box; display: flex; flex-direction: column; gap: 4px">
<div style="display: flex; align-items: center; gap: 10px"><span style="font-size: 14px; font-weight: 600">AI tools and MCP</span><span style="flex: 1"></span><button style="font-size: 11px; color: #a9c8f7">What is MCP?</button></div>
{sec('LET AI APPS WORK IN DAISY', 'Daisy runs an MCP server, so apps like Claude Code or Cursor can read and edit your open project.')}
{row('Daisy MCP server', sw(True) + pill('Running · 1 app connected', GREEN))}
{row('Connect by', segm(['Local app (stdio)', 'Address (HTTP)'], 1) + mono('http://127.0.0.1:7341/mcp', 'width: 300px;'), 'Only this computer can reach it.')}
{row('Quick setup', btn('Copy for Claude Code') + btn('Cursor') + btn('VS Code') + btn('Other (JSON)', 'ghost'), 'Copies the settings to paste into that app.')}
{row('New apps may', segm(['Read only', 'Ask before changes', 'Change freely'], 1), 'Every change by an app is one step in Undo and is listed in History.')}
{row('Apps can see', segm(['The open project', 'All recent projects'], 0))}
<div style="display: flex; flex-direction: column; gap: 6px; padding: 4px 0 0 216px">{clients}</div>
</div>'''
modal(S, 'Preferences', 'for you on this computer', nav + main, 1080, 600, '<span style="font-size: 11px; color: #939393">Changes apply at once</span>' + done, top=130)
S.save('D59-MCP.dc.html')

# ═════ D-59b An AI app editing through MCP ═════
S = Screen('Daisy · D-59b An AI app working in Daisy')
S.remove_h1_overlay(); S.remove_parent_outline()
POP = 'background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5);'
chipbar = f'''<span role="status" style="height: 24px; display: flex; align-items: center; gap: 6px; padding: 0 4px 0 8px; border-radius: 12px; background: rgba(47,128,237,0.14); box-shadow: inset 0 0 0 1px rgba(47,128,237,0.5); color: #d6e6fb; font-size: 11px; white-space: nowrap">{icon('plug', 11, '#a9c8f7')}Claude Code is working<span style="width: 1px; height: 12px; background: rgba(169,200,247,0.4)"></span><button style="padding: 0 6px; color: #a9c8f7">Pause</button><button style="padding: 0 6px; color: #a9c8f7">Stop</button></span>
'''
S.rep('<span role="status" title="Saved to D:', chipbar + '<span role="status" title="Saved to D:')
# canvas: mark the hero heading as the element the app is changing
ov = f'''<!-- AI app activity on canvas -->
<div aria-hidden="true" style="position: absolute; left: 398px; top: 354px; width: 488px; height: 182px; border: 1.5px dashed #2f80ed; z-index: 20; pointer-events: none">
<span style="position: absolute; left: -1.5px; bottom: calc(100% + 4px); height: 20px; padding: 0 7px; display: flex; align-items: center; gap: 5px; background: #246bcb; color: #fff; font-size: 11px; white-space: nowrap; border-radius: 2px">{icon('plug', 10, '#fff')}Claude Code · proposed change</span></div>
<svg aria-hidden="true" style="position: absolute; left: 886px; top: 420px; z-index: 20" width="30" height="10"><path d="M0 5h30" stroke="#2f80ed" stroke-width="1.5" stroke-dasharray="4 3"/></svg>
<div style="position: absolute; left: 916px; top: 380px; width: 300px; padding: 10px 12px; box-sizing: border-box; display: flex; flex-direction: column; gap: 6px; {POP} z-index: 21; font-size: 12px; line-height: 16px">
<span style="font-size: 11px; color: #939393">Heading · text</span>
<span style="display: grid; grid-template-columns: 36px minmax(0, 1fr); gap: 6px"><span style="font-size: 11px; color: #ff938c">Was</span><span style="color: #a8a8a8; text-decoration: line-through">Hand-thrown ceramics for everyday tables</span></span>
<span style="display: grid; grid-template-columns: 36px minmax(0, 1fr); gap: 6px"><span style="font-size: 11px; color: #7ee787">Now</span><span>Stoneware made by hand, for every day</span></span></div>
<!-- POPOVER: MCP change request -->
<section role="dialog" aria-label="Claude Code wants to make changes" style="position: absolute; left: 1282px; top: 96px; width: 328px; box-sizing: border-box; padding: 0 12px 12px; display: flex; flex-direction: column; gap: 10px; background: #262626; border: 1px solid #454545; border-radius: 6px; box-shadow: 0 12px 32px rgba(0,0,0,0.5); z-index: 40; font-size: 12px; line-height: 16px">
<div style="height: 40px; margin: 0 -12px; padding: 0 8px 0 12px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #3a3a3a">{logo('C', '#c96442').replace('28px', '20px').replace('font-size: 12px', 'font-size: 10px')}
<span style="font-weight: 600">Claude Code</span><span style="flex: 1; font-size: 11px; color: #939393">3 changes</span>
<button aria-label="Pin open" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; color: #939393">{icon("keep", 14)}</button><button aria-label="Close" style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; color: #a8a8a8">{icon("close", 14)}</button></div>
<div style="padding: 8px 10px; border-radius: 4px; background: #1f1f1f; font-size: 11px; line-height: 15px; color: #c8c8c8">“Make the Home hero warmer and add a short testimonials section.”</div>
<div style="display: flex; flex-direction: column; gap: 4px">{''.join(f'<div style="display: grid; grid-template-columns: 14px minmax(0, 1fr); gap: 8px; align-items: start; padding: 7px 8px; border-radius: 4px; background: {"rgba(47,128,237,0.14)" if i == 0 else "#2a2a2a"}">{chk_ok}<span style="display: flex; flex-direction: column; gap: 2px; min-width: 0"><span style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{t}</span>{sm(d)}</span></div>' for i, (t, d, chk_ok) in enumerate([
    ('Hero heading · text', 'Shown on the canvas', icon('check', 12, '#a9c8f7', 2)),
    ('Hero button · Fill → clay-600', 'Uses a design-system colour', icon('check', 12, '#a9c8f7', 2)),
    ('Add section “Testimonials” after Hero', '3 quotes · built from the Card component', icon('check', 12, '#a9c8f7', 2))]))}</div>
<div style="display: flex; align-items: center; gap: 8px; font-size: 11px"><span style="width: 13px; height: 13px; border-radius: 3px; box-shadow: inset 0 0 0 1px #6b6b6b"></span>Allow changes without asking until I close Daisy</div>
<div style="display: flex; gap: 8px"><button style="flex: 1; height: 28px; border-radius: 4px; background: #246bcb; color: #fff; font-weight: 500">Allow 3 changes</button>{btn('Deny')}</div>
<div style="font-size: 10px; line-height: 14px; color: #939393">Allowed changes become one step: “Claude Code · 3 changes”. Undo or History removes them together.</div>
</section>'''
S.rep('<div style="width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;',
      '<div style="position: relative; width: 1920px; height: 1080px; display: flex; flex-direction: column; overflow: hidden;')
S.rep('<!-- ═══════════ TOP BAR v3', ov + '\n<!-- ═══════════ TOP BAR v3')
S.status(['Page', 'Hero', 'Heading'], 'Claude Code is connected through MCP · it can read this project and asks before changing it', 'x 0 &#160;y 0')
S.save('D59b-MCP-Live.dc.html')

# ═════ D-59c MCP states ═════
_d = open('/home/claude/ds/dstates3.py').read(); ST = {}; exec(_d[:_d.index('# ═════ D-56b')], ST)
frame, cap_, sheet = ST['frame'], ST['cap'], ST['sheet']
POPS = 'background: #262626; border: 1px solid #454545; border-radius: 8px; box-shadow: 0 12px 32px rgba(0,0,0,0.5);'
def box(title, body, foot='', w=560):
    return (f'<div style="width: {w}px; display: flex; flex-direction: column; {POPS} overflow: hidden"><div style="height: 44px; display: flex; align-items: center; gap: 10px; padding: 0 12px 0 16px; border-bottom: 1px solid #3a3a3a"><span style="font-weight: 600; font-size: 13px">{title}</span><span style="flex: 1"></span>{icon("close", 13, "#a8a8a8")}</div>'
            f'<div style="padding: 14px 16px; display: flex; flex-direction: column; gap: 10px">{body}</div>' + (f'<div style="height: 50px; display: flex; align-items: center; gap: 8px; padding: 0 16px; border-top: 1px solid #3a3a3a; background: #222222">{foot}</div>' if foot else '') + '</div>')
center = lambda inner, h: frame(f'<div style="flex: 1; display: flex; align-items: center; justify-content: center; background: #1c1c1c">{inner}</div>', h)
lbl = lambda l, c: f'<div style="display: grid; grid-template-columns: 110px minmax(0, 1fr); gap: 10px; align-items: center"><span style="font-size: 11px; color: #a8a8a8">{l}</span><div style="display: flex; gap: 8px; align-items: center">{c}</div></div>'
inp = lambda t, ph=False, focus=False: f'<span style="flex: 1; height: 28px; display: flex; align-items: center; padding: 0 10px; box-sizing: border-box; border-radius: 4px; background: #1f1f1f; box-shadow: inset 0 0 0 1px {"#2f80ed" if focus else "#3a3a3a"}; font-family: {MONO}; font-size: 11px; color: {"#6b6b6b" if ph else "#c8c8c8"}; white-space: nowrap; overflow: hidden">{t}</span>'
spin = '<span style="width: 12px; height: 12px; border-radius: 6px; border: 2px solid #454545; border-top-color: #2f80ed; box-sizing: border-box"></span>'
foot_add = lambda label='Add server', dis=False: '<span style="flex: 1"></span>' + btn('Cancel', 'ghost') + (f'<button style="height: 28px; padding: 0 12px; border-radius: 4px; background: #333; color: #6b6b6b">{label}</button>' if dis else btn(label, 'pri'))

_unused = [('list_tables', 'Read', True, 'Lists tables and fields'), ('query_rows', 'Read', True, 'Reads rows for Collections'), ('insert_row', 'Changes data', False, 'Writes a row'), ('run_sql', 'Changes data', False, 'Runs any SQL')]
c5 = center(box('Allow an app to connect?', f'<div style="display: flex; align-items: center; gap: 12px">{logo("Cu", "#3a3a3a")}<span style="display: flex; flex-direction: column"><span style="font-weight: 600">Cursor</span>{sm("wants to use Daisy’s MCP server on this computer")}</span></div>'
                + lbl('It may', segm(['Read only', 'Ask before changes', 'Change freely'], 0)) + lbl('It can see', segm(['Halden (open)', 'All recent projects'], 0))
                + sm('You can change or remove this any time in Preferences › AI tools and MCP.'), '<span style="flex: 1"></span>' + btn('Don’t allow', 'ghost') + btn('Allow', 'pri')), 380)
c6 = center(box('Claude Code · stopped', f'<div style="display: flex; align-items: center; gap: 10px">{pill("Disconnected", GREY)}<span style="font-size: 11px; color: #c8c8c8">The app closed while it was working.</span></div>'
                + '<div style="display: flex; flex-direction: column; gap: 4px">' + ''.join(f'<div style="height: 28px; display: flex; align-items: center; gap: 8px; padding: 0 8px; border-radius: 4px; background: #2a2a2a">{icon("check", 11, GREEN, 2) if ok else icon("close", 11, "#939393", 2)}<span style="flex: 1; {"" if ok else "color: #939393"}">{t}</span>{sm("done" if ok else "not started")}</div>' for t, ok in [('Hero heading · text', True), ('Hero button · Fill', True), ('Add section “Testimonials”', False)]) + '</div>'
                + sm('Nothing is half done: each change finished or did not start.'), '<span style="flex: 1"></span>' + btn('Undo the 2 changes') + btn('Keep', 'pri')), 380)
hist = [('plug', 'Claude Code · 3 changes', '12:46 · Home · asked and allowed', True), ('t-para', 'Edited text · Intro', '12:31 · you', False), ('plug', 'Cursor · read only', '12:20 · read Home and Shop · no changes', False), ('t-section', 'Added section · This season', '11:58 · you', False)]
c7 = center(box('History', ''.join(f'<div style="height: 40px; display: grid; grid-template-columns: 18px minmax(0, 1fr) auto; gap: 10px; align-items: center; padding: 0 10px; border-radius: 4px; background: {"rgba(47,128,237,0.14)" if on else "#2a2a2a"}">{icon(ic, 13, "#a9c8f7" if "plug" == ic else "#a8a8a8")}<span style="display: flex; flex-direction: column"><span>{t}</span>{sm(d)}</span>{btn("Undo", "ghost") if on else ""}</div>' for ic, t, d, on in hist)
                + sm('App steps carry the app’s name. Reads are listed so you can see what an app looked at.'), w=520), 380)
c9 = center(box('Cursor can only read', f'<div style="display: flex; align-items: center; gap: 12px">{logo("Cu", "#3a3a3a")}<span style="display: flex; flex-direction: column"><span style="font-weight: 600">Cursor tried to change “Hero heading”</span>{sm("It has Read only access, so nothing was changed.")}</span></div>'
                + sm('Cursor was told the change was refused. To let it ask for changes, raise its access.'), '<span style="flex: 1"></span>' + btn('Keep read only', 'ghost') + btn('Allow it to ask', 'pri')), 380)
cells = [('An app asks to connect', 'First time only. Access and reach are chosen here.', c5),
         ('A read-only app tries to change something', 'Refused and reported once; access can be raised here.', c9),
         ('An app stops mid-task', 'Changes are whole or not started; one button undoes them.', c6),
         ('History shows app steps', 'Named, grouped, undoable; reads listed too.', c7)]
sheet('D-59c', 'MCP · states', 'Apps connecting, read-only refusals, stopping mid-task and history', cells, 'D59c-MCP-States.dc.html', 1160)
print('ok')
