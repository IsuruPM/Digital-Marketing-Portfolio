# Soft Ground — Design System v1.0

Design system extracted from the digital-marketing reference layout, for the
Digital Marketing Portfolio.

**Shareable spec page:** https://claude.ai/code/artifact/763b4c90-1505-483f-ad7c-111663cd573b

## Files

| File | Use |
| --- | --- |
| `index.html` | The full visual specification — swatches, type specimens, component specs, do/don't rules. Open locally or use the link above. |
| `tokens.css` | Drop-in CSS custom properties (`--sg-*`). Import once, style everything through it. |
| `tokens.json` | Machine-readable tokens with usage notes and contrast ratios — for Figma sync, Style Dictionary, or codegen. |
| `tailwind.config.js` | Tailwind `theme.extend` block mapping the same values to utility classes. |

## The system in one paragraph

A warm off-white ground (`#F1F0EE`) with white cards floating on it, separated by
1px hairlines rather than shadows. One near-black (`#101214`) does every action —
there is no brand accent colour. Display type is a light-weight grotesk at 300
with negative tracking; nothing above 20px is ever bold. Five desaturated tints
(mint, sage, blush, cream, mist) carry service categorisation as card fills only,
never as text or borders. All buttons, tags and controls are pills. Sections rest
128px apart on desktop — the vertical air is the signature.

## Fonts

Google Fonts substitutes for the reference's commercial faces:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@300;400;500&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
```

- **Hanken Grotesk** 300/400 — display and headings
- **Instrument Sans** 400/500/600 — body, UI, eyebrows
- **JetBrains Mono** 400/500 — data and aligned digits (optional)

## Accessibility

- `ink` on `ground` — 14.9:1
- `ink-2` on `ground` — 5.9:1
- `ink-3` on `ground` — 3.1:1 → **uppercase eyebrows and captions only**, never body copy
- Ink tokens do not change on tint fills; all five tints clear 4.5:1 against `ink`.
