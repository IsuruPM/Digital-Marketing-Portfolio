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

## Deploy to Netlify

The site is static, so there is nothing to build. Two ways to publish:

1. **Connect the repository** (recommended). In Netlify choose *Add new site → Import an
   existing project*, pick this GitHub repository and the branch you want to publish. Leave the
   build command empty and the publish directory as `.` (both are already set in
   `netlify.toml`). Every push then redeploys.
2. **Drag and drop.** Upload the `netlify-site.zip` produced by `npm run zip` (or the folder
   itself) at https://app.netlify.com/drop.

After the first deploy, turn on the inquiry form:

* *Site configuration → Forms → Enable form detection*, then redeploy once so Netlify registers
  the form named `inquiry`.
* *Forms → Form notifications → Add notification → Email notification*, and enter
  `isurupm1997@gmail.com`. Every submission (name, email, contact number, inquiry) is then
  emailed there and also listed under *Forms* in the Netlify dashboard.
* Spam is filtered by Netlify's honeypot field plus its built-in Akismet check.

If the site is ever hosted somewhere other than Netlify, the form falls back to opening the
visitor's email app with the message pre-filled and addressed to the same inbox.

Other integrations on the page: the "Book a discovery call" buttons open
https://calendly.com/isurumarasinghe/30min, and the floating WhatsApp widget opens a chat with
+971 52 912 7002.

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
| — | Hero | "Hey, I'm Isuru Marasinghe", intro, qualifications, four headline metrics with count-up |
| 01 | About | Positioning, philosophy, the five outcomes |
| 02 | Expertise | Four white cards with line icons: creative, paid media, measurement, lifecycle |
| 03 | Results | Five cases from live accounts; each opens a dialog with tables and screenshots |
| 04 | Production | Fortune 500 event coverage (Zoom, CNBC) |
| 05 | Clients | Colour logo marquee on white, with industry tags |
| 06 | Testimonials | Six client quotes (drafted, awaiting each person's sign-off) |
| 07 | Stack | Platform logos and tools, with a note on creative direction |
| 08 | Credentials | Education, Meta licences, CIM Level 7 awards, memberships |
| 09 | Contact | Ink band with discovery-call CTA, inquiry form, contact details and portrait |

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
* **Wordmark**: the nav uses `assets/img/wordmark.svg` (the signature SVG, viewBox tightened and
  fill set to `currentColor`).
* **Kingsford College of Business and Technology** is a text placeholder in the marquee
  (`li.wm-fallback`) until the logo file is added as `assets/img/logos/kingsford.png`; then
  replace that `<li>` with an `<img>` like the others (in both marquee copies and in the deck).
* **Client logos** run in two opposite-direction marquees on white and pause on hover.
  Logos designed for dark backgrounds had their white pixels mapped to ink so they read
  on white. Under `prefers-reduced-motion` the marquee becomes a static wrapped row.
* **Currency**: headline figures are USD; AED platform figures are converted at the
  pegged 3.6725 and the AED original is kept in the tables.

## Design tokens

All values are in `:root` at the top of `assets/css/site.css` and match the Soft Ground
specification: ground `#F1F0EE`, surface `#FFFFFF`, ink `#17191B`, hairline `#E4E2DF`,
4 px spacing scale, 8 px card radius, pill buttons, one hover-only shadow.
