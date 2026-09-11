# Isuru Marasinghe — Digital Marketing Portfolio

A single-page portfolio and a matching PDF deck, built on the **Soft Ground** design system
(warm off-white ground, white hairline cards, one near-black action colour, five desaturated
category tints, Hanken Grotesk / Instrument Sans / JetBrains Mono).

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
| 02 | Expertise | Four tint cards: creative, paid media, measurement, lifecycle |
| 03 | Results | Five cases from live accounts; each opens a dialog with tables and screenshots |
| 04 | Production | Fortune 500 event coverage (Zoom, CNBC) |
| 05 | Clients | 23 brands grouped into 8 industries |
| 06 | Stack | Platforms and tools |
| 07 | Credentials | Education, Meta licences, CIM Level 7 awards, memberships |
| 08 | Contact | Mist conversion band with WhatsApp, email, LinkedIn |

## Editing content

* **Case studies** live twice in `index.html`: the tile in the `.work` grid and a
  `<template id="tpl-…">` with the full detail. The dialog title and eyebrow are in the
  `meta` object at the bottom of `assets/js/site.js`.
* **Screenshots** in `assets/img/results/` are cropped to exactly what the original deck
  showed (campaign names and client columns stay hidden). Replace a file with the same name
  to update both the site and the deck.
* **Logos** are transparent PNGs. Logos designed for dark backgrounds sit inside an
  `.ind.dark` card; everything else renders greyscale and reveals colour on hover.
* **Tile covers** currently use the platform screenshots. Six illustrative placeholder
  images (Dubai architecture, keys and contract, skincare still life, apparel flat-lay,
  email on a phone, studio behind-the-scenes) were generated with Nano Banana on
  Higgsfield and sit in that account's generation history; drop them into
  `assets/img/covers/` and point the `.cover` images at them if a photographic cover is
  preferred over the screenshot.

## Design tokens

All values are in `:root` at the top of `assets/css/site.css` and match the Soft Ground
specification: ground `#F1F0EE`, surface `#FFFFFF`, ink `#17191B`, hairline `#E4E2DF`,
tints mint / sage / blush / cream / mist, 4 px spacing scale, 8 px card radius, pill buttons,
one hover-only shadow.
