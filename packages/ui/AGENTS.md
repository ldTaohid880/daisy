# @daisy/ui

Daisy's own UI kit: tokens and primitives for the editor chrome.

**Owns:** CSS custom properties from UI_DESIGN_PLAN.md 9 (dark and light), primitives (Button, Field, Capsule, Segmented, Switch, Popover, Menu, Dialog, Tooltip, Tabs), icon set.

**Specification:** UI_DESIGN_PLAN.md 9 (design system), 9.2 (light theme), D-00 sheets on the design canvas

**May import:** @daisy/di · react, react-dom, radix-ui, lucide-react. The full graph is in `docs/architecture/dependencies.json` and is checked by `pnpm check:deps`.

**Rules:** Never hard-code a colour, size or radius outside tokens.css. Never use the accent for decoration; violet is for states only.

**Tests:** `pnpm --filter @daisy/ui test`. Test files sit next to the code as `*.test.ts`.
