#!/usr/bin/env python3
"""Generate the service landing pages from the data below.

Each page targets one search intent the single-page portfolio cannot rank for on its
own: a home page can carry one title and one H1, and these queries each want their
own. Edit the SERVICES list and run `python3 scripts/build-services.py`.

Every figure quoted here comes from the case studies, which come from the accounts.
Nothing is rounded up and nothing is invented; if a number changes in
scripts/build-cases.py it has to change here too.
"""

import html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://isurumarasinghe.com/"
GA = "G-307CN46RYD"
VERIFY = "DIW5ROwDRpi_2F6pmTCKQRL050cAkq0UAVs_hDUr6RQ"
OG_ALT = ("Isuru Marasinghe, full stack digital marketer, with USD 4.5M+ ad spend managed "
          "and USD 61.5M+ in closed deal value")

SERVICES = [
{
 "slug": "digital-marketer-dubai",
 "eyebrow": "Dubai, UAE · available now",
 "h1": "Freelance digital marketer in Dubai",
 "title": "Freelance Digital Marketer in Dubai | Isuru Marasinghe",
 "desc": ("Freelance digital marketer and media buyer in Dubai. USD 4.5M+ managed across Meta, "
          "Google and TikTok, and USD 61.5M+ in closed deal value from direct leads. "
          "Book a 30-minute call."),
 "lede": ("I run paid media and the conversion journey behind it for brands in the UAE: Meta, "
          "Google, TikTok and LinkedIn, plus the tracking, creative and lifecycle work that "
          "decides whether the spend turns into pipeline. Based in Dubai, working with clients "
          "across the Emirates, Sri Lanka and remote."),
 "service_name": "Freelance digital marketing and paid media management",
 "service_type": "Digital marketing",
 "intro_h": "What a freelance marketer gets you that an agency does not",
 "intro": ["You work with the person running the account. There is no account manager relaying "
           "questions to a buyer you never meet, and no junior learning on your budget.",
           "Reporting stops at pipeline rather than at clicks. The real-estate account below is "
           "reported on closed deal value, because that is the number the client actually cares "
           "about.",
           "Scope flexes. Some engagements are a full retained build, some are a fractional "
           "performance lead sitting alongside an in-house team, some are a single audit."],
 "does_h": "What I take on",
 "does": [("Paid media management",
           "Meta, Google, TikTok and LinkedIn: structure, budgets, audiences, bidding and the "
           "weekly optimisation that keeps cost per result moving in the right direction."),
          ("Creative direction and production",
           "Hooks, scripts, statics and video, shot and edited rather than briefed out. Creative "
           "supply is the constraint on most accounts, not targeting."),
          ("Tracking and measurement",
           "GA4, Google Tag Manager, the Meta Conversions API and server-side events, so the "
           "platforms optimise against real conversions instead of guesses."),
          ("Lifecycle and retention",
           "Klaviyo flows and campaigns for e-commerce, and CRM stage mapping so leads can be "
           "followed to the closing."),
          ("Fractional performance lead",
           "Strategy, forecasting and account oversight for teams that have the hands but need "
           "someone senior owning the numbers.")],
 "proof_h": "The accounts behind that",
 "proof": [("case-meta-leads.html", "5,364 property leads from one Meta account",
            "AED 43.75 blended cost per lead across the account, with the cheapest ad set at AED 6.48."),
           ("case-crm-closings.html", "USD 36.6M closed from direct leads",
            "75 deals worth AED 134,417,569 on roughly AED 440,000 of media."),
           ("case-google-ads.html", "Google Ads at a 15.73× return",
            "Four separate monthly snapshots rather than one good month.")],
 "faq": [("How much does a freelance digital marketer in Dubai cost?",
          "It depends on scope and on how much is already in place. A single-platform account "
          "with existing creative is a different engagement from a build that includes tracking, "
          "creative production and lifecycle. The discovery call ends with a scope and a number, "
          "and there is no charge for that call."),
         ("Do you work with businesses outside Dubai?",
          "Yes. I am based in Dubai and work across the UAE, in Sri Lanka, and remotely with "
          "clients elsewhere. Paid media is run from the platforms, so location matters less than "
          "overlap in working hours."),
         ("Which industries have you worked in?",
          "UAE real estate is the deepest, followed by e-commerce and higher education. The "
          "clients page lists the brands, and the case studies show the accounts in full."),
         ("Do you take over an existing account or start fresh?",
          "Usually take over. The first step is an audit of the ad accounts, the tracking and the "
          "funnel behind them, which normally finds enough to fix before anything is rebuilt."),
         ("What does the first month look like?",
          "Audit and plan in week one, build and launch inside the first two weeks, then weekly "
          "optimisation and reporting. The process section on the home page sets out all four "
          "steps.")],
},
{
 "slug": "meta-ads-dubai",
 "eyebrow": "Meta Ads · Facebook &amp; Instagram",
 "h1": "Meta ads management in Dubai",
 "title": "Meta Ads Management Dubai — Facebook &amp; Instagram | Isuru Marasinghe",
 "desc": ("Facebook and Instagram ads management in Dubai by a Meta Certified media buyer. "
          "5,364 property leads from one account and USD 36.6M in closed deals. "
          "Lead generation, Advantage+ and the Conversions API."),
 "lede": ("Facebook and Instagram are still where most UAE lead generation and e-commerce "
          "spend goes, and still where most of it is wasted on cheap forms that never close. "
          "I run Meta accounts on the outcome, not the form fill."),
 "service_name": "Meta Ads (Facebook and Instagram) management",
 "service_type": "Meta Ads management",
 "intro_h": "How the account gets run",
 "intro": ["Creative supply first. Advantage+ and broad targeting only work when the algorithm "
           "has enough distinct ideas to choose between, so a test set stays live at all times "
           "and winners get promoted into scaling campaigns.",
           "Events before audiences. The Conversions API and clean event mapping come before any "
           "restructure, because an account optimising against a bad signal cannot be fixed by "
           "better targeting.",
           "Judged past the click. Lead quality is read in the CRM, and purchases on a seven-day "
           "click window held steady so week-on-week comparisons mean something."],
 "does_h": "What that covers",
 "does": [("Lead generation", "Instant forms and landing pages, lead quality scoring, and CRM "
           "stage mapping so cost per closed deal is visible rather than cost per form."),
          ("Advantage+ shopping", "Catalogue setup, creative supply and the manual prospecting "
           "that runs against Advantage+ so the two compete on the same objective."),
          ("Creative testing", "A permanent test lane with hooks, statics and video, measured on "
           "its own terms rather than against the scaling set's click-through rate."),
          ("Conversions API", "Server-side events, deduplication and event match quality, which "
           "is usually the single biggest lift available on a neglected account."),
          ("Retargeting and exclusions", "Audience hygiene so prospecting and retargeting stop "
           "bidding against each other.")],
 "proof_h": "Meta accounts in full",
 "proof": [("case-meta-leads.html", "5,364 property leads from one Meta account",
            "An eight-times spread between the best and worst ad set, which is the whole argument "
            "for running mechanics against each other."),
           ("case-meta-ecom.html", "Purchase-optimised growth on Meta",
            "3.55× top ad-set ROAS, 3.02% click-through rate, USD 0.35 average cost per click."),
           ("case-crm-closings.html", "USD 36.6M closed from those leads",
            "The same pipeline followed past the form and into the CRM.")],
 "faq": [("Are you Meta certified?",
          "Yes. Meta Certified Digital Marketing Associate and Meta Certified Creative Strategy "
          "Professional, both listed with the badges in the credentials section."),
         ("What budget does a Meta account need to work?",
          "Enough for the learning phase on each ad set rather than a fixed figure. An account "
          "split across too many ad sets on a small budget learns nothing; the same money "
          "consolidated usually does. That is one of the first things the audit checks."),
         ("Can you fix an account that stopped performing?",
          "Often, and the cause is usually one of three things: event signal quality, creative "
          "fatigue, or a structure that fragments the budget. The audit identifies which before "
          "anything is rebuilt."),
         ("Do you write and produce the creative as well?",
          "Yes. Direction, scripts, statics and video, shot and edited rather than briefed out to "
          "a separate team.")],
},
{
 "slug": "google-ads-dubai",
 "eyebrow": "Google Ads · Search &amp; Shopping",
 "h1": "Google Ads management in Dubai",
 "title": "Google Ads Management Dubai — Search &amp; Shopping | Isuru Marasinghe",
 "desc": ("Google Ads management in Dubai: Search, Shopping and Performance Max, with GA4 and "
          "server-side tracking. A 15.73x peak return across four monthly snapshots."),
 "lede": ("Search catches demand that already exists, which makes it the most honest channel in "
          "the mix and the easiest to flatter with the wrong attribution. I run it on return, "
          "read across months rather than a single good one."),
 "service_name": "Google Ads management",
 "service_type": "Google Ads management",
 "intro_h": "How the account gets run",
 "intro": ["Four snapshots, not one. A single strong month proves nothing, so the account below "
           "is reported across four, including the weakest, which is the month spend was pulled "
           "back hardest.",
           "Shopping feed before bid strategy. Most Shopping underperformance is a feed problem "
           "wearing a bidding costume: titles, attributes and the product set.",
           "Measurement that survives consent. GA4, Tag Manager and server-side tagging, so "
           "conversion data stays usable rather than quietly degrading."],
 "does_h": "What that covers",
 "does": [("Search", "Query mining, match type discipline, negative keyword structure and ad "
           "copy that matches the intent behind the term rather than the term itself."),
          ("Shopping and Performance Max", "Feed quality, product segmentation and the asset "
           "groups that let PMax be judged instead of trusted."),
          ("Landing pages", "Message match and conversion rate work, because the cheapest click "
           "improvement is usually not in the auction."),
          ("GA4 and Tag Manager", "Event design, conversion imports and server-side tagging."),
          ("Remarketing", "Audience lists built from real behaviour rather than all visitors.")],
 "proof_h": "The account in full",
 "proof": [("case-google-ads.html", "Google Ads at a 15.73× return",
            "Four monthly snapshots; a double-digit return held in three of them."),
           ("case-meta-ecom.html", "The Meta half of the same funnel",
            "Purchase-optimised campaigns read on a seven-day click window."),
           ("case-klaviyo.html", "What happens after the purchase",
            "Flows out-earning campaigns on placed orders past 144,000 recipients.")],
 "faq": [("Do you handle Shopping feeds as well as campaigns?",
          "Yes, and usually first. Titles, attributes and product segmentation decide what "
          "Shopping can bid on at all, so the feed is where most of the early gain is."),
         ("How do you report on Google Ads?",
          "On return and on revenue, with the attribution window stated. Where the business is "
          "lead generation rather than e-commerce, reporting follows the lead into the CRM."),
         ("Can you work alongside our existing agency?",
          "Yes, as a fractional performance lead: strategy, forecasting and oversight while the "
          "agency keeps the hands on the account."),
         ("What about Performance Max?",
          "Used where it earns its place and segmented enough to be readable. PMax that cannot "
          "be broken out by asset group and product set is not a campaign, it is a black box.")],
},
{
 "slug": "tiktok-ads-dubai",
 "eyebrow": "TikTok Ads · lead generation",
 "h1": "TikTok ads management in Dubai",
 "title": "TikTok Ads Management Dubai | Isuru Marasinghe",
 "desc": ("TikTok ads management in Dubai: lead generation and creative-led campaigns across 35 "
          "campaigns, with leads at AED 3.50 in the strongest market. Native creative produced "
          "in house."),
 "lede": ("TikTok rewards creative volume more than any other platform and punishes repurposed "
          "Meta assets. The accounts that work are the ones producing natively, testing widely "
          "across markets, and moving budget to the spread rather than splitting it evenly."),
 "service_name": "TikTok Ads management",
 "service_type": "TikTok Ads management",
 "intro_h": "How the account gets run",
 "intro": ["Market spread over even splits. On the account below, an AED 290 test in Pakistan "
           "bought 83 leads at AED 3.50 while a Canadian launch paid AED 294 for each of its 44. "
           "Budget followed that gap.",
           "Native creative, produced here. Hooks written for the platform, shot and cut for it, "
           "rather than a landscape ad cropped to vertical.",
           "Volume with a read on it. Thirty-five campaigns is only useful if the account is "
           "structured so the winners are visible."],
 "does_h": "What that covers",
 "does": [("Lead generation", "Instant forms and landing pages, with lead quality read past the "
           "submission."),
          ("Creative production", "Scripts, hooks, shooting and editing for vertical video, in "
           "the volume the platform needs."),
          ("Market testing", "Deliberately wide early tests so the cost spread between markets "
           "becomes visible before the budget commits."),
          ("Pixel and events API", "Clean event setup so optimisation has something real to aim "
           "at."),
          ("Spark ads and creator content", "Running creative from real accounts where that "
           "outperforms brand-handle delivery.")],
 "proof_h": "The account in full",
 "proof": [("case-tiktok-leads.html", "TikTok lead generation across 35 campaigns",
            "AED 143.73 blended cost per lead, with the best market at AED 3.50."),
           ("case-meta-leads.html", "The same offer on Meta",
            "5,364 leads, for comparison across platforms."),
           ("case-crm-closings.html", "Where those leads ended up",
            "75 closed deals worth AED 134,417,569.")],
 "faq": [("Does TikTok work for real estate in the UAE?",
          "It generated leads on the account shown, at a blended AED 143.73 and far less in the "
          "strongest markets. Whether it works for a given brand depends on the offer and on "
          "whether creative can be produced at the rate the platform consumes it."),
         ("Can we reuse our Meta creative on TikTok?",
          "It can be tested, but it rarely wins. The platform reads produced-for-Meta assets as "
          "ads and the cost shows it, which is why creative production is part of the engagement "
          "rather than a separate line."),
         ("How many creatives does a TikTok account need?",
          "More than feels reasonable, and refreshed continuously. Creative fatigue arrives "
          "faster here than anywhere else in the mix."),
         ("Do you run TikTok Shop or e-commerce campaigns?",
          "Lead generation is where the account evidence is. E-commerce work to date has been on "
          "Meta and Google, shown in those case studies.")],
},
{
 "slug": "digital-marketer-sri-lanka",
 "eyebrow": "Sri Lanka · remote and on site",
 "h1": "Digital marketer in Sri Lanka",
 "title": "Digital Marketer in Sri Lanka | Isuru Marasinghe",
 "desc": ("Sri Lankan digital marketing specialist working from Dubai: paid media across Meta, "
          "Google and TikTok, creative production and measurement, for brands in Sri Lanka and "
          "the UAE."),
 "lede": ("I am Sri Lankan, trained in Colombo and the UK, and now working out of Dubai. Several "
          "of the brands below are Sri Lankan, and the education and migration accounts in "
          "particular run across both markets at once."),
 "service_name": "Digital marketing and paid media management",
 "service_type": "Digital marketing",
 "intro_h": "Working across two markets",
 "intro": ["Education and migration brands sell into Sri Lanka and deliver in the UAE, UK or "
           "Australia, which makes them two audiences in one account. That is most of the "
           "cross-market work.",
           "Costs and benchmarks do not transfer. A cost per lead that looks strong in Colombo "
           "means something different in Dubai, so accounts are read per market rather than "
           "blended.",
           "Time zone is a non-issue. Dubai is an hour and a half behind Colombo, so the working "
           "day overlaps almost entirely."],
 "does_h": "What I take on",
 "does": [("Paid media management", "Meta, Google, TikTok and LinkedIn across both markets."),
          ("Creative direction and production", "Shot and edited in house, including on location."),
          ("Tracking and measurement", "GA4, Tag Manager and server-side events."),
          ("Lifecycle and retention", "Klaviyo for e-commerce, CRM stage mapping for lead "
           "generation."),
          ("Fractional performance lead", "Senior oversight for teams that already have the "
           "hands.")],
 "proof_h": "Selected accounts",
 "proof": [("case-meta-leads.html", "5,364 property leads from one Meta account",
            "UAE real estate, run from Dubai."),
           ("case-klaviyo.html", "Flows out-earning campaigns on placed orders",
            "E-commerce lifecycle past 144,000 recipients."),
           ("case-google-ads.html", "Google Ads at a 15.73× return",
            "Search and Shopping for e-commerce.")],
 "faq": [("Are you based in Sri Lanka or Dubai?",
          "Dubai. I work with Sri Lankan brands remotely and travel for production."),
         ("Do you work with education and migration agencies?",
          "Yes, that is one of the deepest verticals, and the client list includes several "
          "institutions and agencies in that space."),
         ("Do you bill in LKR or USD?",
          "Either, agreed before the engagement starts."),
         ("What are your qualifications?",
          "MBA (UK), ACIM (UK), PgDip.M (UK), AMSLIM (SL), CLSSWB, CDMP (USA) and a first-class "
          "BM (Hons) in Marketing from Horizon Campus, Sri Lanka, plus fifteen platform and "
          "institute certifications listed on the home page.")],
},
]

BY_SLUG = {s["slug"]: s for s in SERVICES}
ORDER = [s["slug"] for s in SERVICES]

NAV = """      <a href="index.html#about">About</a>
      <a href="index.html#expertise">Expertise</a>
      <a href="index.html#work">Results</a>
      <a href="index.html#clients">Clients</a>
      <a href="index.html#testimonials">Testimonials</a>
      <a href="index.html#credentials">Credentials</a>
      <a href="index.html#process">Process</a>
      <a href="index.html#contact">Contact</a>"""

SOCIALS = """      <a class="soc" href="https://www.linkedin.com/in/isuru-marasinghe/" target="_blank" rel="noopener me" aria-label="Isuru Marasinghe on LinkedIn" title="LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9.5h4v11H3v-11Zm6.5 0h3.83v1.5h.05c.53-.95 1.84-1.95 3.78-1.95 4.04 0 4.79 2.5 4.79 5.76v5.69h-4v-5.05c0-1.2-.02-2.75-1.73-2.75-1.73 0-2 1.31-2 2.66v5.14h-4v-11Z"/></svg></a>
      <a class="soc" href="https://www.facebook.com/isurupm" target="_blank" rel="noopener me" aria-label="Isuru Marasinghe on Facebook" title="Facebook"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06c0 5.02 3.66 9.18 8.44 9.94v-7.03H7.9v-2.91h2.54V9.85c0-2.52 1.49-3.91 3.77-3.91 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.78-1.63 1.57v1.89h2.78l-.45 2.91h-2.33V22c4.78-.76 8.44-4.92 8.44-9.94Z"/></svg></a>
      <a class="soc" href="https://www.instagram.com/x_isuru_x/" target="_blank" rel="noopener me" aria-label="Isuru Marasinghe on Instagram" title="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1.2" fill="currentColor" stroke="none"/></svg></a>"""


def strip(s):
    """Plain text for a JSON-LD field: entities resolved, no markup."""
    return html.unescape(s)


def build(sv):
    url = SITE + sv["slug"] + ".html"
    others = [BY_SLUG[s] for s in ORDER if s != sv["slug"]]

    does = "\n".join(
        '      <li><h3>%s</h3><p>%s</p></li>' % (h, b) for h, b in sv["does"])
    intro = "\n".join('      <p>%s</p>' % p for p in sv["intro"])
    proof = "\n".join(
        '        <a class="svc-proof" href="%s"><span class="t">%s</span>'
        '<span class="d">%s</span><span class="more">Read the case'
        '<span class="arrow" aria-hidden="true">&rarr;</span></span></a>' % (href, t, d)
        for href, t, d in sv["proof"])
    faq = "\n".join(
        '      <details class="faq"><summary>%s</summary><p>%s</p></details>' % (q, a)
        for q, a in sv["faq"])
    siblings = "\n".join(
        '        <a class="tag" href="%s.html">%s</a>' % (o["slug"], strip(o["h1"]))
        for o in others)

    service_ld = {
      "@context": "https://schema.org",
      "@type": "Service",
      "name": sv["service_name"],
      "serviceType": sv["service_type"],
      "url": url,
      "description": strip(sv["desc"]),
      "provider": {
        "@type": "Person",
        "@id": SITE + "#isuru",
        "name": "Isuru Marasinghe",
        "url": SITE,
        "jobTitle": "Full Stack Digital Marketer",
        "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE"},
      },
      "areaServed": [
        {"@type": "City", "name": "Dubai"},
        {"@type": "Country", "name": "United Arab Emirates"},
        {"@type": "Country", "name": "Sri Lanka"},
      ],
      "availableChannel": {
        "@type": "ServiceChannel",
        "serviceUrl": "https://calendly.com/isurumarasinghe/30min",
        "servicePhone": "+971529127002",
      },
      "inLanguage": "en",
    }

    faq_ld = {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {"@type": "Question", "name": strip(q),
         "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
        for q, a in sv["faq"]
      ],
    }

    crumbs = {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Isuru Marasinghe", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": strip(sv["h1"]), "item": url},
      ],
    }

    return f"""<!doctype html>
<html lang="en">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', '{GA}');
</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{sv['title']}</title>
<meta name="google-site-verification" content="{VERIFY}" />
<meta name="description" content="{html.escape(strip(sv['desc']))}">
<meta name="author" content="Isuru Marasinghe">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="canonical" href="{url}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Isuru Marasinghe">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{sv['title']}">
<meta property="og:description" content="{html.escape(strip(sv['desc']))}">
<meta property="og:type" content="website">
<meta property="og:image" content="{SITE}assets/img/og-cover.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{OG_ALT}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{sv['title']}">
<meta name="twitter:description" content="{html.escape(strip(sv['desc']))}">
<meta name="twitter:image" content="{SITE}assets/img/og-cover.jpg">
<meta name="theme-color" content="#FFFFFF">
<link rel="icon" href="favicon.ico" sizes="48x48 32x32 16x16">
<link rel="icon" type="image/png" sizes="96x96" href="favicon-96x96.png">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preload" href="assets/fonts/HankenGrotesk.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/InstrumentSans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css">
<script type="application/ld+json">
{json.dumps(service_ld, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps(faq_ld, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps(crumbs, indent=2)}
</script>
</head>
<body>

<header class="top">
  <div class="wrap top-inner">
    <a class="mark" href="index.html" aria-label="Isuru Marasinghe, back to the home page"><img src="assets/img/wordmark.svg" alt="Isuru Marasinghe" width="661" height="152"></a>
    <nav class="nav" aria-label="Sections">
{NAV}
    </nav>
    <div class="top-actions">
      <a class="btn btn-primary btn-sm" href="https://calendly.com/isurumarasinghe/30min" target="_blank" rel="noopener">Book a call</a>
    </div>
  </div>
</header>

<main id="top">

<article class="casestudy service">
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb"><a href="index.html">Isuru Marasinghe</a><span aria-hidden="true">/</span><span>{strip(sv['h1'])}</span></nav>

    <header class="cs-head reveal">
      <span class="eyebrow">{sv['eyebrow']}</span>
      <h1>{sv['h1']}</h1>
      <p class="lede">{sv['lede']}</p>
      <div class="row" style="margin-top:28px">
        <a class="btn btn-primary" href="https://calendly.com/isurumarasinghe/30min" target="_blank" rel="noopener">Book a discovery call</a>
        <a class="btn btn-ghost" href="index.html#work">See the results</a>
      </div>
    </header>

    <section class="svc-sec reveal" aria-labelledby="svc-intro">
      <h2 id="svc-intro">{sv['intro_h']}</h2>
{intro}
    </section>

    <section class="svc-sec reveal" aria-labelledby="svc-does">
      <h2 id="svc-does">{sv['does_h']}</h2>
      <ul class="svc-list">
{does}
      </ul>
    </section>

    <section class="svc-sec reveal" aria-labelledby="svc-proof">
      <h2 id="svc-proof">{sv['proof_h']}</h2>
      <div class="svc-proofs">
{proof}
      </div>
    </section>

    <section class="svc-sec reveal" aria-labelledby="svc-faq">
      <h2 id="svc-faq">Questions I get asked</h2>
{faq}
    </section>

    <section class="svc-sec reveal" aria-labelledby="svc-more">
      <h2 id="svc-more">Also available</h2>
      <div class="industry-tags" style="margin-top:18px">
{siblings}
      </div>
    </section>

    <div class="cs-cta reveal">
      <div>
        <h2>Let's look at your account.</h2>
        <p class="lede">Thirty minutes, no charge. You leave knowing what I would change first, whether or not we work together.</p>
      </div>
      <div class="row">
        <a class="btn btn-primary" href="https://calendly.com/isurumarasinghe/30min" target="_blank" rel="noopener">Book a discovery call</a>
        <a class="btn btn-ghost" href="index.html#contact">Send an inquiry</a>
      </div>
    </div>
  </div>
</article>

</main>

<div class="wa" id="wa-widget">
  <a class="wa-btn" id="wa-btn" href="https://wa.me/971529127002?text=Hi%20Isuru%2C%20I%27d%20like%20to%20talk%20about%20a%20project." target="_blank" rel="noopener" aria-label="Chat with Isuru Marasinghe on WhatsApp">
    <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-1 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.5-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>
  </a>
</div>

<footer>
  <div class="wrap foot">
    <span>&copy; 2026 Isuru Marasinghe &middot; Full Stack Digital Marketer</span>
    <span class="links">
{SOCIALS}
      <a href="index.html">Home</a></span>
  </div>
</footer>

<script src="assets/js/site.js" defer></script>
</body>
</html>
"""


if __name__ == "__main__":
    for sv in SERVICES:
        path = os.path.join(ROOT, sv["slug"] + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build(sv))
        print("wrote", sv["slug"] + ".html")
