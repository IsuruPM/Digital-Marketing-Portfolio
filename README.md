# Isuru Marasinghe — Digital Marketing Portfolio

A single-page portfolio and a matching PDF deck, built on the **Soft Ground** design system
(warm off-white ground, white hairline cards, one near-black action colour, Hanken Grotesk /
Instrument Sans / JetBrains Mono). This edition is monochrome: no tints, no accent colour.

```
index.html                      the site (no build step, no framework)
assets/css/site.css             tokens + components + motion
assets/js/site.js               reveal-on-scroll, count-up metrics, nav state, case dialog
assets/fonts/*.woff2            self-hosted variable fonts
assets/img/                     portraits, client logos, credential badges, platform screenshots
print/deck.html + deck.css      the 13-page 16:9 deck used for the PDF
scripts/build-pdf.mjs           renders the deck to Isuru-Marasinghe-Portfolio.pdf with Playwright
Isuru-Marasinghe-Portfolio.pdf  the exported deck
```

## Run it locally

Any static server works. Fonts are loaded with `@font-face`, so open it over HTTP rather than
`file://`:

```sh
npx serve .            # or: python3 -m http.server 8080
```

## Rebuild the PDF

```sh
npm install            # installs playwright
npx playwright install chromium   # once, if no Chromium is available
npm run pdf
```

The deck is laid out at 1440 × 810 CSS pixels per page and exported at that size, so it
presents full-screen like a slide deck.

## Structure of the site

| # | Section | What it holds |
|---|---------|---------------|
| — | Hero | Thesis line, intro, four headline metrics with count-up |
| 01 | About | Positioning, philosophy, the five outcomes |
| 02 | Expertise | Four white cards with line icons: creative, paid media, measurement, lifecycle |
| 03 | Results | Five cases from live accounts; each opens a dialog with tables and screenshots |
| 04 | Production | Fortune 500 event coverage (Zoom, CNBC) |
| 05 | Clients | 22 brands in a colour logo marquee, with industry tags |
| 06 | Stack | Platform logos and tools, with a note on creative direction |
| 07 | Credentials | Education, Meta licences, CIM Level 7 awards, memberships |
| 08 | Contact | Ink band with WhatsApp, email, LinkedIn and portrait |

## Editing content

* **Case studies** live twice in `index.html`: the tile in the `.work` grid and a
  `<template id="tpl-…">` with the full detail. The dialog title and eyebrow are in the
  `meta` object at the bottom of `assets/js/site.js`.
* **Screenshots** in `assets/img/results/` are cropped to exactly what the original deck
  showed (campaign names and client columns stay hidden). Replace a file with the same name
  to update both the site and the deck.
* **Tile covers** are monochrome SVG illustrations in `assets/img/covers/` (funnel,
  pipeline, product cards, search-and-chart, email flows). Replace any of them with a
  4:3 photograph of the same name to swap in a photographic cover; the screenshots stay
  inside the case dialog.
* **Client logos** run in two opposite-direction marquees on white and pause on hover.
  Logos designed for dark backgrounds had their white pixels mapped to ink so they read
  on white. Under `prefers-reduced-motion` the marquee becomes a static wrapped row.
* **Currency**: headline figures are USD; AED platform figures are converted at the
  pegged 3.6725 and the AED original is kept in the tables.

## Design tokens

All values are in `:root` at the top of `assets/css/site.css` and match the Soft Ground
specification: ground `#F1F0EE`, surface `#FFFFFF`, ink `#17191B`, hairline `#E4E2DF`,
4 px spacing scale, 8 px card radius, pill buttons, one hover-only shadow.
