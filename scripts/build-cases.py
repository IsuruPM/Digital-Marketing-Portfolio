#!/usr/bin/env python3
"""Builds the six case-study pages from the data below.

Each page is a normal static HTML file in the repository root, so it can be
edited by hand afterwards; re-running this script overwrites them.
    python3 scripts/build-cases.py
"""
import html, os, json

SITE = "https://isurumarasinghe.com/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CASES = [
{
 "slug": "case-meta-leads",
 "stitle": "5,364 property leads from one Meta account",
 "num": "Case 01",
 "kicker": "Meta Ads · UAE real estate",
 "title": "5,364 property leads from one Meta account",
 "tag": "Meta Ads · Lead generation",
 "cover": "assets/img/covers/lead-gen.svg",
 "lede": "Lead-form and website-conversion campaigns for property developers and brokerages in the UAE, scaled from AED 40 to AED 500 a day per ad set while holding the account-wide cost per lead at AED 43.75.",
 "desc": "5,364 property leads from one Meta Ads account in the UAE at USD 11.91 average cost per lead, with the Ads Manager report shown in full.",
 "facts": [("Platform","Meta Ads · lead forms and website conversions"),
           ("Market","United Arab Emirates"),
           ("Structure","CBO and ABO, broad and interest stacks, retargeting sequences"),
           ("Reported in","AED · USD converted at the pegged 3.6725")],
 "stats": [("5,364","Leads","Account total"),
           ("USD 11.91","Average cost per lead","AED 43.75"),
           ("USD 63.9K","Amount spent","AED 234,688.78"),
           ("2.16","Average frequency","4.7M accounts reached")],
 "brief": "Developers and brokerages need a steady flow of enquiries the sales floor can call the same day. The job was volume that did not fall apart as budgets went up, in a market where the same buyers see property ads every day of the week.",
 "did": ["Ran lead-form and website-conversion ad sets side by side, so the cheaper mechanic could be found per audience instead of assumed.",
         "Built prospecting on both broad targeting and interest stacks, with retargeting sequences behind each.",
         "Scaled winners from AED 40 to AED 500 a day, judging each increase on frequency as well as cost per lead.",
         "Rotated creative before frequency passed roughly three, which is where cost per lead started to climb in this account."],
 "shots": [("assets/img/results/meta-leads-realestate.jpg",
            "Meta Ads Manager report for Isuru Marasinghe's UAE real estate account, ad sets sorted by leads",
            "Meta Ads Manager · ad sets sorted by leads",
            "What you are looking at: the ten highest-volume ad sets in the account. The leads column runs from 730 down to 196, and the cost-per-lead column beside it from AED 6.48 to AED 53.71. Daily budgets sit between AED 40 and AED 500. The bold row at the bottom is the account total: 5,364 leads, AED 234,688.78 spent, 4,727,354 accounts reached at a 2.16 frequency.")],
 "table": {"head": ["Ad set","Leads","Cost / lead (AED)","Daily budget","Spent (AED)","Reach","Frequency"],
  "rows": [["Lead form · top performer","730","6.48","50","4,732.58","219,977","3.33"],
           ["Conversion leads","419","13.46","40","5,639.38","78,184","3.00"],
           ["Lead form","377","15.77","80","5,946.07","296,158","1.74"],
           ["Conversion leads","365","9.78","50","3,569.00","120,274","3.10"],
           ["Lead form","316","15.25","500","4,817.95","164,071","1.87"],
           ["Lead form","250","13.69","50","3,421.91","278,556","2.08"],
           ["Lead form","216","29.80","200","6,436.00","137,815","2.02"],
           ["Conversion leads","210","52.75","252","11,077.15","80,905","2.73"],
           ["Lead form","207","53.71","161","11,117.78","141,129","2.25"],
           ["Lead form","196","16.64","70","3,262.32","379,188","1.65"],
           ["<strong>Account total</strong>","<strong>5,364</strong>","<strong>43.75</strong>","—","<strong>234,688.78</strong>","<strong>4,727,354</strong>","<strong>2.16</strong>"]],
  "note": "Top ten ad sets by lead volume; the final row is the whole account across 10,212,676 impressions."},
 "result": "The spread between the best and worst ad set is eight times, which is the whole argument for running mechanics against each other rather than picking one. The cheapest ad set delivered 730 leads at AED 6.48, and the account still closed at AED 43.75 per lead after the expensive tests were paid for. Lifetime real-estate spend in the UAE across this and related accounts is around USD 300K.",
},
{
 "slug": "case-crm-closings",
 "stitle": "USD 22.1M closed from direct leads",
 "num": "Case 02",
 "kicker": "CRM · UAE real estate",
 "title": "From lead to closing: USD 22.1M in property sold",
 "tag": "CRM · Closed deals",
 "cover": "assets/img/covers/closings.svg",
 "lede": "The same real-estate pipeline followed past the lead form and into the CRM, where 75 deals closed for a combined AED 81,317,569 on roughly AED 260K of media spend.",
 "desc": "The CRM snapshot behind Isuru Marasinghe's UAE real estate media buying: 75 deals worth USD 22.1M on about USD 71K of ad spend.",
 "facts": [("Source","CRM closed-deals dashboard"),
           ("Market","UAE real estate"),
           ("Media spend","Roughly AED 260,000, about USD 71K, behind the closed pipeline"),
           ("Context","Around USD 300K of lifetime UAE real-estate ad spend to date")],
 "stats": [("75","Deals closed","Recorded in the CRM"),
           ("USD 22.1M","Closed deal value","AED 81,317,569"),
           ("USD 71K","Media spend","≈ AED 260,000"),
           ("313×","Closed value per dollar","Sale value ÷ media spend")],
 "brief": "Cost per lead is easy to flatter and easy to argue with. The only number a developer or brokerage actually cares about is how much property the pipeline sold, so the leads from the Meta account were followed through the CRM to the closing stage.",
 "did": ["Matched CRM stages back to the ad sets and lead forms that created each record, so closings could be attributed rather than guessed.",
         "Reported on closed value alongside cost per lead every week, which changed which ad sets got budget.",
         "Fed the closing data back into targeting and creative, favouring the audiences that produced deals rather than the ones that produced cheap forms."],
 "shots": [("assets/img/results/crm-closings.jpg",
            "CRM closed-deals snapshot from Isuru Marasinghe's UAE real estate pipeline showing AED 81,317,569 closed",
            "CRM · closed-deals snapshot",
            "What you are looking at: the two summary cards from the CRM dashboard. The left card is the count of closed deals, 75. The right card is their combined sale value, AED 81,317,569, which is about USD 22.1M at the pegged rate. Client and project columns are cropped out because the account is under NDA.")],
 "table": {"head": ["Measure","Value","Notes"],
  "rows": [["Deals closed","75","Recorded as won in the CRM"],
           ["Closed value","AED 81,317,569","About USD 22.1M at 3.6725"],
           ["Average deal value","≈ AED 1.08M","Closed value ÷ deals"],
           ["Media spend behind the pipeline","≈ AED 260,000","About USD 71K"],
           ["<strong>Closed value per dirham spent</strong>","<strong>313×</strong>","Sale value, not commission"]],
  "note": "Closed value is the sale value of the properties as recorded in the CRM, not agency revenue or commission."},
 "result": "Three hundred and thirteen dirhams of property sold for every dirham of media. That multiple is the reason the account kept scaling: the conversation with the client stopped being about cost per lead and became about how much pipeline the next AED 100K could buy.",
},
{
 "slug": "case-meta-ecom",
 "stitle": "Purchase-optimised growth on Meta",
 "num": "Case 03",
 "kicker": "Meta Ads · E-commerce",
 "title": "Purchase-optimised growth on Meta",
 "tag": "Meta Ads · Advantage+",
 "cover": "assets/img/covers/ecom-meta.svg",
 "lede": "Advantage+ shopping mixed with creative-led prospecting and retargeting for UAE e-commerce brands, read on a seven-day click window and judged on purchase ROAS rather than clicks.",
 "desc": "Purchase-optimised Meta Ads for UAE e-commerce: 3.55x top ad-set ROAS, 3.02% CTR and USD 0.35 cost per click, with three account views in full.",
 "facts": [("Platform","Meta Ads · Advantage+ shopping and manual campaigns"),
           ("Objective","Purchases, seven-day click attribution"),
           ("Store","Shopify"),
           ("Reported in","AED · USD converted at the pegged 3.6725")],
 "stats": [("3.55×","Top ad-set ROAS","Seven-day click"),
           ("2.24×","Account average ROAS","Blended across the period"),
           ("3.02%","Click-through rate","All placements"),
           ("USD 0.35","Average cost per click","AED 1.27")],
 "brief": "The store needed profitable scale, not a better click price. That meant reading the account at the purchase end of the funnel and keeping creative supply high enough that Advantage+ had something to choose between.",
 "did": ["Ran Advantage+ shopping against manual prospecting so the algorithm and the structure were competing on the same objective.",
         "Kept a dedicated creative test set live at all times and promoted winners into the scaling campaigns.",
         "Read the account on three views, the funnel, the efficiency and the return, rather than optimising one number in isolation.",
         "Held attribution steady on a seven-day click window so week-on-week comparisons meant something."],
 "shots": [("assets/img/results/meta-ecom-roas-1.jpg",
            "Meta Ads Manager funnel view for an e-commerce account managed by Isuru Marasinghe",
            "Account view one · the funnel",
            "What you are looking at: spend against the steps of the purchase funnel. Reading across, the account spent about USD 14,834 (AED 54,480.11) and produced 2,992 adds to cart worth USD 149,595 (AED 549,387.07), then 1,780 checkouts initiated and 626 payment-info submissions, at an average purchase ROAS of 2.24."),
           ("assets/img/results/meta-ecom-roas-2.jpg",
            "Meta Ads Manager efficiency view showing CTR and cost per click for Isuru Marasinghe's e-commerce account",
            "Account view two · the efficiency",
            "What you are looking at: the delivery columns for the same period. 1,421,498 impressions against 400,652 people, a frequency of 3.55, a 3.02% click-through rate, 28,425 link clicks and a cost per click of AED 1.27, which is USD 0.35."),
           ("assets/img/results/meta-ecom-roas-3.jpg",
            "Meta Ads Manager return view showing purchase ROAS up to 4.31 for Isuru Marasinghe's e-commerce account",
            "Account view three · the return",
            "What you are looking at: the same campaigns sorted by purchase ROAS. The creative test set reached 4.31 and the prospecting and retargeting set 3.55, against the 2.24 account average shown in the first view.")],
 "table": {"head": ["Set","Impressions","Reach","Frequency","CTR","Link clicks","CPC","ROAS"],
  "rows": [["Prospecting and retargeting","1,421,498","400,652","3.55","3.02%","28,425","AED 1.27","3.55"],
           ["Creative test set","1,442,564","462,001","3.12","2.25%","22,609","AED 1.36","4.31"]],
  "note": "Purchase ROAS on a seven-day click window. The creative test set carries a lower click-through rate and a higher return, which is why both are kept live."},
 "result": "The test set beat the scaling set on return while losing on click-through rate. That is the case for keeping a separate creative lane rather than judging every ad on the same top-of-funnel metric.",
},
{
 "slug": "case-google-ads",
 "stitle": "Google Ads at a 15.73x return",
 "num": "Case 04",
 "kicker": "Google Ads · E-commerce",
 "title": "Search and Shopping that paid for itself fifteen times over",
 "tag": "Google Ads",
 "cover": "assets/img/covers/ecom-google.svg",
 "lede": "Search and Performance Max campaigns for an online store, built on a tight keyword architecture and a clean product feed, shown as four monthly snapshots straight from the Google Ads overview.",
 "desc": "Google Ads Search and Performance Max returning 15.73x in the best month, with four monthly account snapshots shown in full.",
 "facts": [("Platform","Google Ads · Search and Performance Max"),
           ("Currency","USD, as reported in the account"),
           ("Best month","September 2024, a 15.73× return"),
           ("Range","7.58× to 15.73× across the four snapshots")],
 "stats": [("15.73×","Peak monthly return","September 2024"),
           ("14.19×","August 2024","On USD 1,220 of cost"),
           ("10.98×","May 2025","First eleven days"),
           ("USD 43.7K","Sales across the four","On USD 3,144 of cost")],
 "brief": "A small budget with no room for waste. Every dirham had to land on a query that already wanted the product, which puts the work in the keyword architecture and the feed rather than in bidding tricks.",
 "did": ["Built the account around tight, intent-matched keyword groups instead of broad catch-alls.",
         "Cleaned the product feed so Shopping and Performance Max had accurate titles, categories and availability to work with.",
         "Let Performance Max carry the long tail while Search held the high-intent head terms.",
         "Read the account monthly on conversion value per cost, which is the column these snapshots are sorted on."],
 "shots": [("assets/img/results/google-sep-2024.jpg","Google Ads overview for September 2024 showing a 15.73 return, from an account managed by Isuru Marasinghe","September 2024 · 15.73× return","What you are looking at: the Google Ads overview row for the month. Cost USD 1,260, 210 purchases, USD 19,800 of sales value, and 15.73 in the conversion-value-per-cost column on the right."),
           ("assets/img/results/google-aug-2024.jpg","Google Ads overview for August 2024 showing a 14.19 return, from an account managed by Isuru Marasinghe","August 2024 · 14.19× return","What you are looking at: the same row a month earlier. Cost USD 1,220, 207.6 purchases, USD 17,300 of sales value, 14.19 conversion value per cost."),
           ("assets/img/results/google-dec-2024.jpg","Google Ads overview for December 2024 showing a 7.58 return, from an account managed by Isuru Marasinghe","December 2024 · 7.58× return","What you are looking at: a deliberately throttled month. Cost USD 198, 60 purchases, USD 1,500 of sales value, 7.58 conversion value per cost."),
           ("assets/img/results/google-may-2025.jpg","Google Ads overview for May 2025 showing a 10.98 return, from an account managed by Isuru Marasinghe","1–11 May 2025 · 10.98× return","What you are looking at: a part-month, eleven days only. Cost USD 466, 43.4 purchases, USD 5,120 of sales value, 10.98 conversion value per cost.")],
 "table": {"head": ["Period","Cost","Purchases","Sales value","Conv. value / cost"],
  "rows": [["1–31 Aug 2024","$1,220","207.6","$17,300","14.19"],
           ["1–30 Sep 2024","$1,260","210.0","$19,800","15.73"],
           ["1–31 Dec 2024","$198","60.0","$1,500","7.58"],
           ["1–11 May 2025","$466","43.4","$5,120","10.98"]],
  "note": "Purchase counts are fractional where Google attributes partial conversions. Sales values appear rounded in the platform overview."},
 "result": "Four snapshots rather than one, because a single good month proves nothing. The account held a double-digit return in three of the four, and the weakest month is the one where spend was pulled back hardest.",
},
{
 "slug": "case-tiktok-leads",
 "stitle": "857 property leads from TikTok",
 "num": "Case 06",
 "kicker": "TikTok Ads · UAE real estate",
 "title": "857 property leads from TikTok at USD 39 each",
 "tag": "TikTok Ads · Lead generation",
 "cover": "assets/img/covers/tiktok-leads.svg",
 "lede": "Eighteen months of always-on TikTok buying for a Dubai brokerage: 35 campaigns across the UAE, Canada, the UK, Pakistan and the wider Arabic-speaking market, at a USD 3.47 CPM.",
 "desc": "TikTok Ads case study: 35 campaigns, 9.67M impressions and 857 property leads at USD 39.14 each for a Dubai real estate brokerage.",
 "facts": [("Platform","TikTok Ads Manager"),
           ("Period","23 October 2024 to 21 April 2026"),
           ("Scope","35 campaigns, Smart+ and manual, CBO and daily-budget"),
           ("Markets","UAE, Canada, UK, Pakistan, multi-region Arabic"),
           ("Reported in","AED · USD converted at the pegged 3.6725")],
 "stats": [("USD 33.5K","Media spend","AED 123,179.61"),
           ("857","Leads","Across 35 campaigns"),
           ("USD 39.14","Cost per lead","AED 143.73"),
           ("USD 3.47","CPM","AED 12.74")],
 "brief": "Property advertising on TikTok is mostly reach with nothing behind it. The brief was to treat it as a lead channel: cheap impressions are only worth buying if the form on the other end fills in, so every campaign was judged on cost per lead rather than views.",
 "did": ["Ran developer launches, Arabic-language lead generation and expat targeting as separate campaigns rather than one audience blob.",
         "Tested the same creative across the UAE, Canada, the UK and Pakistan, because the same video can be eighty times cheaper per lead in one market than another.",
         "Used Smart+ where volume justified it and manual CBO where the audience was narrow enough to control by hand.",
         "Kept cheap tests running at AED 20 a day alongside the large launches, which is where the best cost per lead came from."],
 "shots": [("assets/img/results/tiktok-account.jpg",
            "TikTok Ads Manager campaign report for the UAE real estate account managed by Isuru Marasinghe",
            "TikTok Ads Manager · 35 campaigns",
            "What you are looking at: the TikTok Ads Manager campaign table, cropped to the metric columns, with the account totals on the bold row at the bottom. Reading that row: AED 123,179.61 of cost, AED 4.04 cost per click, a AED 12.74 CPM, 9,665,499 impressions, 30,457 destination clicks at a 0.32% click-through rate, and 857 conversions at AED 143.73 each. The conversions column counts property enquiry forms, which is why this case calls them leads. Campaign names and the account name are cropped out because the account is under NDA.")],
 "table": {"head": ["Campaign","Cost","Impressions","Clicks","CTR","Leads","Cost / lead"],
  "rows": [["Tower launch · UAE","AED 49,998.69","4,738,265","13,198","0.28%","307","AED 162.86"],
           ["Community launch · Smart+ · UAE","AED 20,813.45","1,022,629","2,912","0.28%","143","AED 145.55"],
           ["Creative split test · Pakistan","AED 290.40","609,776","3,322","0.54%","83","AED 3.50"],
           ["Recruitment · Smart+","AED 79.71","16,312","140","0.86%","63","AED 1.27"],
           ["Developer launch · Canada · CBO","AED 12,945.69","516,074","2,436","0.47%","44","AED 294.22"],
           ["Arabic-language leads · multi-region","AED 2,484.41","467,246","2,204","0.47%","39","AED 63.70"],
           ["Luxury yachting · UK","AED 6,031.91","124,940","462","0.37%","38","AED 158.73"],
           ["<strong>Account total · 35 campaigns</strong>","<strong>AED 123,179.61</strong>","<strong>9,665,499</strong>","<strong>30,457</strong>","<strong>0.32%</strong>","<strong>857</strong>","<strong>AED 143.73</strong>"]],
  "note": "Seven of the thirty-five campaigns shown, sorted by leads; the final row is the whole account."},
 "result": "An AED 290 split test in Pakistan bought 83 leads at AED 3.50 while a Canadian launch paid AED 294 for each of its 44. Budget followed that spread rather than sitting on an even split, which is how the blended cost per lead landed at AED 143.73 across the account.",
},
{
 "slug": "case-klaviyo",
 "stitle": "Klaviyo email revenue up 55% year on year",
 "num": "Case 05",
 "kicker": "Klaviyo · Lifecycle",
 "title": "Email revenue that grew while the list grew",
 "tag": "Klaviyo · Shopify",
 "cover": "assets/img/covers/email.svg",
 "lede": "Automated flows and a campaign calendar for a Shopify store in Klaviyo. Over twelve months, attributed placed-order value grew 55% and add-to-cart value grew 141% against the year before.",
 "desc": "Klaviyo flows and campaigns for a Shopify store: placed-order value up 55% and add-to-cart value up 141% year on year, both dashboards shown.",
 "facts": [("Platform","Klaviyo on Shopify"),
           ("Period","20 April 2025 to 21 April 2026, against the previous period"),
           ("Split","Flows carried 60% of order value, campaigns 40%"),
           ("Reported in","AED · USD converted at the pegged 3.6725")],
 "stats": [("USD 9.4K","Placed-order value","AED 34,523.69"),
           ("+55%","Year on year","Placed order"),
           ("USD 40.1K","Add-to-cart value","AED 147,288.50"),
           ("+141%","Year on year","Added to cart")],
 "brief": "Paid media had brought the traffic; most of it left without buying. The list was the cheapest place to recover that revenue, so the work was to make the automated flows carry the weight rather than relying on campaign sends.",
 "did": ["Built the core flows first, welcome, browse abandon, cart abandon and post-purchase, before touching the campaign calendar.",
         "Segmented sends by engagement so the list stayed deliverable as it grew past 144,000 recipients.",
         "Tied Klaviyo attribution back to Shopify orders so the numbers in the dashboard matched the store.",
         "Kept campaigns for launches and moments, and let flows do the repeatable revenue."],
 "shots": [("assets/img/results/klaviyo-placed-order.jpg","Klaviyo dashboard showing placed-order value up 55.09% for a store managed by Isuru Marasinghe","Klaviyo · placed order","What you are looking at: attributed placed-order value for the twelve months, AED 34,523.69, with the comparison against the previous period showing +55.09%. The split underneath is campaigns AED 13,829.48 and flows AED 20,694.21."),
           ("assets/img/results/klaviyo-added-to-cart.jpg","Klaviyo dashboard showing add-to-cart value up 141.43% for a store managed by Isuru Marasinghe","Klaviyo · added to cart","What you are looking at: attributed add-to-cart value over the same window, AED 147,288.50, up 141.43% year on year, split campaigns AED 80,743.20 and flows AED 66,545.30.")],
 "table": {"head": ["Conversion metric","Attributed value","Change","Campaigns","Flows"],
  "rows": [["Placed order","AED 34,523.69","+55.09%","AED 13,829.48 (40%)","AED 20,694.21 (60%)"],
           ["Added to cart","AED 147,288.50","+141.43%","AED 80,743.20 (55%)","AED 66,545.30 (45%)"],
           ["Campaign recipients","144,188","&gt;999%","—","—"]],
  "note": "Klaviyo attribution, matched against Shopify orders for the same period."},
 "result": "Flows out-earned campaigns on placed orders while campaigns did the wider reaching. Recipients grew past 144,000 without the revenue per send collapsing, which is the part that usually breaks when a list scales.",
},
]

ORDER = ["case-meta-leads","case-crm-closings","case-meta-ecom","case-google-ads","case-klaviyo","case-tiktok-leads"]
BY_SLUG = {c["slug"]: c for c in CASES}

NAV = """      <a href="index.html#about">About</a>
      <a href="index.html#expertise">Expertise</a>
      <a href="index.html#work">Results</a>
      <a href="index.html#clients">Clients</a>
      <a href="index.html#testimonials">Testimonials</a>
      <a href="index.html#credentials">Credentials</a>
      <a href="index.html#process">Process</a>
      <a href="index.html#contact">Contact</a>"""


def picture(src, alt, cls="", extra=""):
    webp = os.path.splitext(src)[0] + ".webp"
    tag = f'<img src="{src}" alt="{html.escape(alt)}" {extra} loading="lazy" decoding="async">'
    if os.path.exists(os.path.join(ROOT, webp)):
        return f'<picture><source srcset="{webp}" type="image/webp">{tag}</picture>'
    return tag


def build(case):
    i = ORDER.index(case["slug"])
    nxt = BY_SLUG[ORDER[(i + 1) % len(ORDER)]]
    prv = BY_SLUG[ORDER[(i - 1) % len(ORDER)]]

    stats = "\n".join(
        f'      <div><div class="v metric">{v}</div><div class="l">{l}</div><div class="c">{c}</div></div>'
        for v, l, c in case["stats"])
    facts = "\n".join(f'        <div><span class="k">{k}</span><span>{v}</span></div>' for k, v in case["facts"])
    did = "\n".join(f'        <li><span>{d}</span></li>' for d in case["did"])

    shots = []
    for src, alt, cap, what in case["shots"]:
        exists = os.path.exists(os.path.join(ROOT, src))
        media = (f'<button class="shot-img" type="button" data-zoom="{src}" aria-label="Open this report full size">'
                 f'{picture(src, alt)}</button>') if exists else (
                 '<div class="shot-missing"><span>Report image to be added</span></div>')
        opener = (f'<button class="shot-open" type="button" data-zoom="{src}">Open full size</button>'
                  if exists else '')
        shots.append(f"""      <figure class="shot">
        {media}
        <figcaption><span class="cap">{cap}</span><span class="what">{what}</span>{opener}</figcaption>
      </figure>""")
    shots = "\n".join(shots)

    t = case["table"]
    NC = ' class="n"'
    head = "".join("<th%s>%s</th>" % (NC if i else "", h) for i, h in enumerate(t["head"]))
    rows = "\n".join("<tr>" + "".join(
        "<td%s>%s</td>" % (NC if i else "", c) for i, c in enumerate(r)) + "</tr>" for r in t["rows"])

    crumbs = {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": "Results", "item": SITE + "#work"},
        {"@type": "ListItem", "position": 3, "name": case["stitle"], "item": SITE + case["slug"] + ".html"}
      ]
    }
    ld = {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": case["title"],
      "description": case["desc"],
      "author": {"@type": "Person", "name": "Isuru Marasinghe", "url": SITE},
      "publisher": {"@type": "Person", "name": "Isuru Marasinghe", "url": SITE},
      "mainEntityOfPage": SITE + case["slug"] + ".html",
      "inLanguage": "en",
      "about": [case["kicker"].split(" · ")[0], case["kicker"].split(" · ")[-1]],
    }

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{case['stitle']} — Isuru Marasinghe</title>
<meta name="google-site-verification" content="DIW5ROwDRpi_2F6pmTCKQRL050cAkq0UAVs_hDUr6RQ" />
<meta name="description" content="{html.escape(case['desc'])}">
<meta name="author" content="Isuru Marasinghe">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="canonical" href="{SITE}{case['slug']}.html">
<meta property="og:url" content="{SITE}{case['slug']}.html">
<meta property="og:site_name" content="Isuru Marasinghe">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{case['stitle']} — Isuru Marasinghe">
<meta property="og:description" content="{html.escape(case['desc'])}">
<meta property="og:type" content="article">
<meta property="og:image" content="{SITE}assets/img/og-cover.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{case['stitle']} — Isuru Marasinghe">
<meta name="twitter:description" content="{html.escape(case['desc'])}">
<meta name="twitter:image" content="{SITE}assets/img/og-cover.jpg">
<meta name="theme-color" content="#F1F0EE">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preload" href="assets/fonts/HankenGrotesk.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/InstrumentSans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css">
<script type="application/ld+json">
{json.dumps(ld, indent=2)}
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

<article class="casestudy">
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb"><a href="index.html#work">Results</a><span aria-hidden="true">/</span><span>{case['num']}</span></nav>

    <header class="cs-head reveal">
      <span class="eyebrow">{case['num']} · {case['kicker']}</span>
      <h1>{case['title']}</h1>
      <p class="lede">{case['lede']}</p>
    </header>

    <div class="statbar case-stats reveal">
{stats}
    </div>

    <div class="cs-grid">
      <section class="cs-copy reveal">
        <h2>The brief</h2>
        <p>{case['brief']}</p>
        <h2>What I did</h2>
        <ul class="ticks">
{did}
        </ul>
      </section>
      <aside class="cs-facts reveal" aria-label="Account details">
{facts}
      </aside>
    </div>

    <section class="cs-evidence reveal" aria-labelledby="evidence-{case['slug']}">
      <h2 id="evidence-{case['slug']}">The report behind it</h2>
      <p class="lede">Taken from the platform exactly as exported. Click any report to open it full size.</p>
{shots}
    </section>

    <section class="cs-numbers reveal" aria-labelledby="numbers-{case['slug']}">
      <h2 id="numbers-{case['slug']}">The numbers</h2>
      <div class="table-wrap">
        <table class="case-table">
          <thead><tr>{head}</tr></thead>
          <tbody>
{rows}
          </tbody>
        </table>
      </div>
      <p class="small">{t['note']}</p>
    </section>

    <section class="cs-result reveal">
      <h2>What it means</h2>
      <p>{case['result']}</p>
    </section>

    <nav class="cs-nav reveal" aria-label="More cases">
      <a class="prev" href="{prv['slug']}.html"><span class="num">{prv['num']}</span><span>{prv['title']}</span></a>
      <a class="next" href="{nxt['slug']}.html"><span class="num">{nxt['num']}</span><span>{nxt['title']}</span></a>
    </nav>

    <div class="cs-cta reveal">
      <div>
        <h2>Want numbers like these on your account?</h2>
        <p class="lede">Book a 30-minute call and I will tell you what I would change first, whether or not we work together.</p>
      </div>
      <div class="row">
        <a class="btn btn-primary" href="https://calendly.com/isurumarasinghe/30min" target="_blank" rel="noopener">Book a discovery call</a>
        <a class="btn btn-ghost" href="index.html#work">All six cases</a>
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
    <span>© 2026 Isuru Marasinghe · Full Stack Digital Marketer</span>
    <span class="links"><a href="https://www.linkedin.com/in/isuru-marasinghe/" target="_blank" rel="noopener">LinkedIn</a><a href="index.html">Home</a></span>
  </div>
</footer>

<script src="assets/js/site.js" defer></script>
</body>
</html>
"""


if __name__ == "__main__":
    for c in CASES:
        path = os.path.join(ROOT, c["slug"] + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build(c))
        print("wrote", c["slug"] + ".html")
