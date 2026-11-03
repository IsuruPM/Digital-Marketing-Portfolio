#!/usr/bin/env python3
"""Generate the services hub, the service pages and the about page.

The service pages are written by discipline, not by city: one page per thing Isuru
sells, readable by a client anywhere. Location keywords are carried by the home page
and by about.html, which states where he is and who he works with, rather than by
doorway pages for each market.

Everything lives under services/ except about.html, so paths inside a service page
reach the site root with ../. Run: python3 scripts/build-services.py
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
PERSON = SITE + "#isuru"

# Line icons, 24x24, drawn in the same hand as the process section on the home page.
ICONS = {
 "target": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1" fill="currentColor"/>',
 "layers": '<path d="M12 3 20.5 7.5 12 12 3.5 7.5Z"/><path d="M3.5 12 12 16.5 20.5 12"/><path d="M3.5 16.5 12 21l8.5-4.5"/>',
 "chart": '<path d="M3.5 20h17"/><path d="M6.5 20v-5M11 20v-9M15.5 20v-4M20 20V6.5"/>',
 "spark": '<path d="M12 3.2 13.7 9l5.8 1.7-5.8 1.7L12 18.2l-1.7-5.8L4.5 10.7 10.3 9Z"/><path d="M18.5 16.5l.7 2.3 2.3.7-2.3.7-.7 2.3-.7-2.3-2.3-.7 2.3-.7Z"/>',
 "search": '<circle cx="11" cy="11" r="6.5"/><path d="M15.8 15.8 20.5 20.5"/>',
 "play": '<rect x="3.5" y="5" width="17" height="14" rx="3"/><path d="M10.5 9.5 15 12l-4.5 2.5Z"/>',
 "flow": '<circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="6" r="2.5"/><circle cx="12" cy="18" r="2.5"/><path d="M6 8.5v3a2 2 0 0 0 2 2h2.2M18 8.5v3a2 2 0 0 1-2 2h-2.2"/>',
 "mail": '<rect x="3" y="5.5" width="18" height="13" rx="2.5"/><path d="M3.4 7 12 13l8.6-6"/>',
 "camera": '<path d="M3.5 8.5h3.2l1.6-2.4h7.4l1.6 2.4h3.2v10h-17Z"/><circle cx="12" cy="13" r="3.6"/>',
 "compass": '<circle cx="12" cy="12" r="8.5"/><path d="M15 9l-1.8 4.2L9 15l1.8-4.2Z"/>',
 "shield": '<path d="M12 3.2 19 6v6c0 4.3-3 7.3-7 8.8C8 19.3 5 16.3 5 12V6Z"/><path d="M9 12l2 2 4-4"/>',
 "globe": '<circle cx="12" cy="12" r="8.5"/><path d="M3.6 12h16.8"/><path d="M12 3.5c2.2 2.3 3.4 5.3 3.4 8.5S14.2 18.2 12 20.5c-2.2-2.3-3.4-5.3-3.4-8.5S9.8 5.8 12 3.5Z"/>',
}


def icon(name):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'
            % ICONS[name])


# Every figure below is taken from the case studies, which come from the accounts.
SERVICES = [
{
 "slug": "meta-ads-management",
 "nav": "Meta ads",
 "icon": "target",
 "art": "meta-ads",
 "art_alt": "Two phone screens running a lead form, beside a funnel resolving into leads",
 "eyebrow": "Facebook &amp; Instagram",
 "h1": "Meta ads management",
 "title": "Facebook &amp; Meta Ads Management | Isuru Marasinghe",
 "desc": ("Meta ads management by a Meta Certified media buyer: lead generation, Advantage+ "
          "shopping, creative testing and the Conversions API. 5,364 leads from one account "
          "and USD 36.6M in closed deals."),
 "lede": ("Facebook and Instagram still carry most lead generation and e-commerce budgets, and "
          "still waste most of it on cheap form fills that never close. I run Meta accounts on "
          "the outcome rather than the submission."),
 "service_type": "Social media advertising",
 "why_h": "Why most Meta accounts stall",
 "why": ["The signal is wrong. An account optimising against a badly mapped event learns the "
         "wrong lesson faster the more you spend on it, and no amount of audience work fixes "
         "that. Events come before everything else.",
         "Creative supply runs out. Advantage+ and broad targeting only work when the algorithm "
         "has genuinely different ideas to choose between, so there is a test lane live at all "
         "times and winners get promoted rather than restarted.",
         "The budget is fragmented. Too many ad sets on too little money means nothing exits the "
         "learning phase. Consolidation is usually the first change, and often the largest."],
 "does": [("target", "Lead generation", "Instant forms and landing pages, lead quality scored in "
           "the CRM rather than at the form, so cost per closed deal is visible."),
          ("layers", "Advantage+ shopping", "Catalogue setup and the manual prospecting that runs "
           "against Advantage+ so the two compete on one objective."),
          ("spark", "Creative testing", "A permanent test lane of hooks, statics and video, judged "
           "on its own terms rather than against the scaling set."),
          ("flow", "Conversions API", "Server-side events, deduplication and event match quality, "
           "usually the biggest single lift on a neglected account."),
          ("shield", "Audience hygiene", "Exclusions and overlap control so prospecting and "
           "retargeting stop bidding against each other.")],
 "proof": [("case-meta-leads.html", "5,364 property leads from one account",
            "An eight-times spread between the best and worst ad set, at AED 43.75 blended."),
           ("case-meta-ecom.html", "Purchase-optimised growth on Meta",
            "3.55x top ad-set ROAS, 3.02% click-through rate, USD 0.35 cost per click."),
           ("case-crm-closings.html", "USD 36.6M closed from those leads",
            "75 deals, followed past the form and into the CRM.")],
 "faq": [("Are you Meta certified?",
          "Yes. Meta Certified Digital Marketing Associate and Meta Certified Creative Strategy "
          "Professional, both shown with the badges in the credentials section."),
         ("What budget does a Meta account need?",
          "Enough for each ad set to exit the learning phase, which is a structural question "
          "rather than a fixed figure. The same money consolidated into fewer ad sets usually "
          "performs better than spread thin, and the audit says which applies."),
         ("Can you fix an account that stopped performing?",
          "Usually. The cause is nearly always one of three things: event signal quality, "
          "creative fatigue, or a structure fragmenting the budget. The audit identifies which "
          "before anything gets rebuilt."),
         ("Do you produce the creative too?",
          "Yes. Direction, scripts, statics and video, shot and edited rather than briefed out.")],
},
{
 "slug": "google-ads-management",
 "nav": "Google Ads",
 "icon": "search",
 "art": "google-ads",
 "art_alt": "A search bar above sponsored results, beside a rising return curve",
 "eyebrow": "Search, Shopping &amp; Performance Max",
 "h1": "Google Ads and PPC management",
 "title": "Google Ads &amp; PPC Management | Isuru Marasinghe",
 "desc": ("PPC and Google Ads management across Search, Shopping and Performance Max, with GA4 "
          "and server-side tracking. A 15.73x peak return held across four monthly snapshots."),
 "lede": ("Search catches demand that already exists, which makes it the most honest channel in "
          "the mix and the easiest to flatter with the wrong attribution window. I run it on "
          "return, read across months rather than on one good one."),
 "service_type": "Search engine marketing",
 "why_h": "How the account gets judged",
 "why": ["Four snapshots, not one. A single strong month proves nothing, so the account below is "
         "reported across four, including the weakest, which is the month spend was pulled back "
         "hardest.",
         "The feed before the bid strategy. Most Shopping underperformance is a feed problem "
         "wearing a bidding costume: titles, attributes and how the product set is segmented.",
         "Measurement that survives consent. GA4, Tag Manager and server-side tagging, so the "
         "conversion data stays usable instead of quietly degrading until the bidding is blind."],
 "does": [("search", "Search campaigns", "Query mining, match type discipline, negative structure "
           "and copy written to the intent behind the term rather than the term."),
          ("layers", "Shopping and Performance Max", "Feed quality, product segmentation and "
           "asset groups built so PMax can be judged instead of trusted."),
          ("chart", "GA4 and Tag Manager", "Event design, conversion imports and server-side "
           "tagging."),
          ("compass", "Landing pages", "Message match and conversion rate work, because the "
           "cheapest improvement is usually not in the auction."),
          ("flow", "Remarketing", "Lists built from real behaviour rather than from everyone who "
           "ever landed.")],
 "proof": [("case-google-ads.html", "Google Ads at a 15.73x return",
            "Four monthly snapshots, double digits held in three of them."),
           ("case-meta-ecom.html", "The Meta half of the same funnel",
            "Purchase-optimised campaigns on a seven-day click window."),
           ("case-klaviyo.html", "What happens after the purchase",
            "Flows out-earning campaigns past 144,000 recipients.")],
 "faq": [("Do you handle Shopping feeds as well as campaigns?",
          "Yes, and usually first. Titles, attributes and segmentation decide what Shopping can "
          "bid on at all, so the feed is where most of the early gain sits."),
         ("How do you report on Google Ads?",
          "On return and revenue, with the attribution window stated. Where the business runs on "
          "leads rather than transactions, reporting follows the lead into the CRM."),
         ("What is your position on Performance Max?",
          "Used where it earns its place and segmented enough to be readable. A PMax campaign "
          "that cannot be broken out by asset group and product set is not a campaign, it is a "
          "black box."),
         ("Can you work alongside our existing agency?",
          "Yes, as a fractional performance lead: strategy, forecasting and oversight while the "
          "agency keeps hands on the account.")],
},
{
 "slug": "tiktok-ads-management",
 "nav": "TikTok ads",
 "icon": "play",
 "art": "tiktok-ads",
 "art_alt": "Three vertical video frames beside cost per lead falling across markets",
 "eyebrow": "TikTok Ads",
 "h1": "TikTok ads management",
 "title": "TikTok Ads Management | Isuru Marasinghe",
 "desc": ("TikTok ads management and native creative production: 35 campaigns, AED 143.73 "
          "blended cost per lead and AED 3.50 in the strongest market."),
 "lede": ("TikTok rewards creative volume more than any other platform and punishes repurposed "
          "Meta assets. The accounts that work produce natively, test widely, and move budget to "
          "the spread rather than splitting it evenly."),
 "service_type": "Social media advertising",
 "why_h": "What the platform actually rewards",
 "why": ["Spread over even splits. On the account below, an AED 290 test bought 83 leads at "
         "AED 3.50 in one market while another paid AED 294 for each of its 44. Budget followed "
         "that gap instead of sitting on an even split.",
         "Native production, not cropping. A landscape ad resized to vertical reads as an ad, "
         "and the cost per result says so. Hooks are written, shot and cut for the platform.",
         "Volume with a read on it. Thirty-five campaigns only helps if the account is structured "
         "so the winners stay visible rather than averaging out."],
 "does": [("target", "Lead generation", "Instant forms and landing pages, with lead quality read "
           "past the submission."),
          ("play", "Creative production", "Scripts, hooks, shooting and editing for vertical "
           "video, at the rate the platform consumes it."),
          ("globe", "Market testing", "Deliberately wide early tests so the cost spread between "
           "markets is visible before the budget commits."),
          ("flow", "Pixel and Events API", "Clean event setup so optimisation has something real "
           "to aim at."),
          ("spark", "Spark ads and creator content", "Running creative from real accounts where "
           "that beats brand-handle delivery.")],
 "proof": [("case-tiktok-leads.html", "TikTok lead generation across 35 campaigns",
            "AED 143.73 blended cost per lead, best market at AED 3.50."),
           ("case-meta-leads.html", "The same offer on Meta",
            "5,364 leads, for a cross-platform comparison."),
           ("case-crm-closings.html", "Where those leads ended up",
            "75 closed deals worth AED 134,417,569.")],
 "faq": [("Does TikTok work for lead generation?",
          "It did on the account shown, at a blended AED 143.73 and far less in the strongest "
          "markets. Whether it works for a given brand depends on the offer and on whether "
          "creative can be produced at the rate the platform consumes it."),
         ("Can we reuse our Meta creative?",
          "It can be tested, but it rarely wins. The platform reads produced-for-Meta assets as "
          "ads and the cost shows it, which is why production is part of the engagement."),
         ("How many creatives does an account need?",
          "More than feels reasonable, and refreshed continuously. Fatigue arrives faster here "
          "than anywhere else in the mix."),
         ("Do you run TikTok Shop campaigns?",
          "Lead generation is where the account evidence sits. E-commerce work to date has been "
          "on Meta and Google, shown in those cases.")],
},
{
 "slug": "linkedin-ads-management",
 "nav": "LinkedIn ads",
 "icon": "layers",
 "art": "linkedin-ads",
 "art_alt": "Profile cards connected into a targeted audience and a qualified lead",
 "eyebrow": "LinkedIn Ads &amp; B2B",
 "h1": "LinkedIn ads management",
 "title": "LinkedIn Ads Management for B2B | Isuru Marasinghe",
 "desc": ("LinkedIn ads management for B2B and high-consideration services: audience targeting, "
          "lead gen forms, offer design and the reporting that follows a lead to a signed "
          "contract."),
 "lede": ("LinkedIn costs several times what Meta does per click, which is only a problem if the "
          "deal at the end is small. For B2B, education and high-ticket services, the maths "
          "usually works, as long as the offer is worth a professional's attention."),
 "service_type": "Social media advertising",
 "why_h": "Where LinkedIn earns its premium",
 "why": ["The targeting is declared, not inferred. Job title, seniority, company size and "
         "industry come from what people maintain about themselves, which is why the premium is "
         "worth paying when the buyer is narrow.",
         "The offer has to carry its own weight. A demo request at LinkedIn prices needs a reason "
         "to exist; a guide, a benchmark or an assessment converts where a sales call does not.",
         "Reporting has to run to contract value. Cost per lead on LinkedIn always looks "
         "alarming in isolation, which is why it is reported against deal size instead."],
 "does": [("target", "Audience build", "Job title, seniority, company size, industry and matched "
           "account lists, kept narrow enough to stay honest."),
          ("mail", "Lead gen forms", "Native forms and landing pages, with the fields that "
           "qualify rather than the fields that are easy."),
          ("spark", "Offer and creative", "Positioning the thing being asked for, plus the copy "
           "and document creative that carries it."),
          ("chart", "Pipeline reporting", "Cost per lead read against contract value rather than "
           "against a Meta benchmark."),
          ("flow", "Retargeting", "Sequencing across website visitors, video viewers and form "
           "openers.")],
 "proof": [("case-crm-closings.html", "Reporting that runs to closed value",
            "The method, shown on a real-estate pipeline: USD 36.6M closed, tracked by stage."),
           ("case-meta-leads.html", "Lead quality scored past the form",
            "5,364 leads, judged on what closed rather than on what submitted."),
           ("case-google-ads.html", "High-intent demand capture",
            "Search and Shopping at a 15.73x return.")],
 "faq": [("Is LinkedIn worth it for a small budget?",
          "Only if the deal size justifies it. Below a certain contract value the maths does not "
          "work and the money is better spent on search. That is a conversation worth having "
          "before the account is built, not after."),
         ("Are you certified on LinkedIn?",
          "Yes, LinkedIn Certified Marketing Insider through LinkedIn Marketing Labs."),
         ("Can you run account-based campaigns?",
          "Yes, with matched account lists, provided the list is large enough for the platform to "
          "deliver against."),
         ("What creative works on LinkedIn?",
          "Documents, plain-spoken founder video and anything that reads as useful rather than "
          "promotional. Polished brand film tends to underperform here.")],
},
{
 "slug": "creative-direction-production",
 "nav": "Creative direction",
 "icon": "spark",
 "art": "creative-direction",
 "art_alt": "A storyboard of three frames beside a stack of finished cuts and a marked winner",
 "eyebrow": "Creative strategy &amp; production",
 "h1": "Creative direction and production",
 "title": "Creative Digital Marketing &amp; Ad Production | Isuru Marasinghe",
 "desc": ("Ad creative direction and production for paid social and search: hooks, scripts, "
          "statics and video, built as a testing system rather than as a one-off campaign."),
 "lede": ("Targeting is largely automated now. What is left for a marketer to decide is what the "
          "ad says and how it says it in the first three seconds, which is why creative stopped "
          "being a deliverable and became the lever."),
 "service_type": "Advertising creative services",
 "why_h": "Creative as a system, not a batch",
 "why": ["Volume with a structure around it. Ads are produced against named angles, so when one "
         "wins you know which idea won rather than which file did.",
         "A permanent test lane. Winners get promoted into scaling campaigns and losers get "
         "retired, which keeps the scaling set clean and the learning continuous.",
         "Judged on the right metric. A test ad and a scaling ad do not share a scorecard; "
         "holding both to click-through rate is how good ideas get killed early."],
 "does": [("compass", "Angle and message strategy", "The named propositions everything else is "
           "produced against, drawn from what the account already proved."),
          ("spark", "Hooks and scripts", "Written for the first three seconds, where the cost per "
           "result is actually decided."),
          ("camera", "Statics and video", "Shot and edited in house, including on location, "
           "rather than briefed out and waited on."),
          ("layers", "Iteration systems", "Variants built so one element changes at a time and "
           "the result means something."),
          ("chart", "Creative reporting", "Performance read by angle and format, so the next "
           "round starts from evidence.")],
 "proof": [("case-meta-ecom.html", "A dedicated test lane against a scaling set",
            "The test set beat scaling on return while losing on click-through rate."),
           ("case-tiktok-leads.html", "Native production at platform pace",
            "35 campaigns, with the best market at AED 3.50 per lead."),
           ("case-meta-leads.html", "Eight-times spread between mechanics",
            "The argument for running ideas against each other rather than picking one.")],
 "faq": [("Do you shoot, or only direct?",
          "Both. Photography and video direction is a service in its own right, and on most paid "
          "accounts the production sits inside the engagement."),
         ("How many creatives per month?",
          "Set by the spend and the platform. TikTok consumes far more than Meta, and Meta more "
          "than search. The plan names a rate rather than a number pulled from the air."),
         ("Can you work with our existing brand guidelines?",
          "Yes. Performance creative and brand consistency are not in conflict; most of the "
          "tension comes from treating ads as brand films."),
         ("Who owns the files?",
          "You do, including the project files, handed over at the end of the engagement.")],
},
{
 "slug": "conversion-tracking-ga4",
 "nav": "Tracking &amp; GA4",
 "icon": "flow",
 "art": "conversion-tracking",
 "art_alt": "A browser event passing through a tag manager and a server before reaching the ad platforms",
 "eyebrow": "Measurement &amp; tracking",
 "h1": "Conversion tracking, GA4 and the Conversions API",
 "title": "GA4, Google Analytics &amp; Conversion Tracking | Isuru Marasinghe",
 "desc": ("GA4, Google Tag Manager, server-side tagging and the Meta Conversions API, set up so "
          "ad platforms optimise against real conversions instead of a degraded signal."),
 "lede": ("Every bidding decision a platform makes is downstream of the events you send it. When "
          "the events are wrong, more budget buys more of the wrong thing, and no creative or "
          "audience work will rescue it."),
 "service_type": "Web analytics and conversion tracking",
 "why_h": "Why this comes before the media work",
 "why": ["Browser-only tracking has been leaking for years. Consent choices, tracking prevention "
         "and ad blockers remove a meaningful share of events, and the platforms fill the gap "
         "with modelling rather than telling you it is gone.",
         "Most accounts optimise against the wrong event. A thank-you page view and a qualified "
         "lead are not the same thing, and the platform will happily find you thousands of the "
         "first.",
         "Server-side closes the gap. Events sent from a server, properly deduplicated against "
         "the browser, restore match quality and give the bidding something solid to aim at."],
 "does": [("chart", "GA4 setup and repair", "Event and conversion design, data streams, "
           "cross-domain, and the reports that answer a question rather than fill a screen."),
          ("layers", "Google Tag Manager", "Container build, trigger logic and a naming scheme "
           "the next person can follow."),
          ("flow", "Server-side tagging", "Server containers and event forwarding so measurement "
           "survives the browser."),
          ("shield", "Conversions API", "Meta CAPI, TikTok Events API and Google enhanced "
           "conversions, with deduplication and match quality checked rather than assumed."),
          ("target", "Offline and CRM events", "Closed deals fed back to the platforms so "
           "optimisation aims at revenue instead of form fills.")],
 "proof": [("case-crm-closings.html", "CRM stages matched back to ad sets",
            "Which is how closings became attributable rather than guessed."),
           ("case-meta-leads.html", "Lead quality read past the form",
            "5,364 leads scored on what they became."),
           ("case-meta-ecom.html", "Attribution held steady on purpose",
            "A seven-day click window kept constant so comparisons meant something.")],
 "faq": [("Can you audit our existing setup rather than rebuild it?",
          "Yes, and that is usually the first step. Most setups have two or three specific faults "
          "rather than needing replacement."),
         ("Do we need server-side tagging?",
          "If you spend meaningfully on Meta or TikTok, it is normally the highest-return "
          "measurement work available. Below that, cleaning the browser events first is better "
          "value."),
         ("Will this work with consent mode?",
          "Yes. Consent Mode v2 is part of the build rather than something bolted on after a "
          "compliance review."),
         ("What about GA4 reports nobody reads?",
          "Those get removed. The deliverable is a small number of reports tied to decisions, not "
          "a dashboard that exists to look thorough.")],
},
{
 "slug": "email-lifecycle-klaviyo",
 "nav": "Lifecycle &amp; email",
 "icon": "mail",
 "art": "email-lifecycle",
 "art_alt": "A triggered email flow branching into three sends and a revenue curve",
 "eyebrow": "Lifecycle &amp; retention",
 "h1": "Email, lifecycle and retention",
 "title": "Klaviyo Email Marketing &amp; Ecommerce Lifecycle | Isuru Marasinghe",
 "desc": ("Klaviyo flows and campaigns for e-commerce: welcome, cart and browse abandonment, "
          "post-purchase and win-back, with flows out-earning campaigns past 144,000 "
          "recipients."),
 "lede": ("Paid media rents attention. Lifecycle owns it. On most e-commerce accounts the flows "
          "quietly out-earn the campaigns while costing nothing per send, which makes neglecting "
          "them the most expensive habit in the business."),
 "service_type": "Email marketing",
 "why_h": "Where the revenue actually sits",
 "why": ["Flows beat campaigns on efficiency. They fire on behaviour rather than on a calendar, "
         "which is why on the account below they out-earned campaigns on placed orders while "
         "campaigns did the wider reaching.",
         "Scale usually breaks revenue per send. A list growing past 144,000 normally dilutes, "
         "and holding the per-send number through that growth is the part that takes work.",
         "Deliverability is a revenue question. Sending to people who stopped opening is how a "
         "list stops reaching the ones who still do."],
 "does": [("flow", "Core flows", "Welcome, cart and browse abandonment, post-purchase, win-back "
           "and replenishment, written rather than templated."),
          ("mail", "Campaign calendar", "A send rhythm that fits the catalogue and the margin, "
           "not a weekly habit."),
          ("layers", "Segmentation", "Engagement tiers, purchase behaviour and predictive values "
           "put to use instead of admired."),
          ("shield", "Deliverability", "Sunset policies, list hygiene and authentication so the "
           "sends reach the inbox."),
          ("chart", "Reporting", "Revenue per recipient and flow contribution, read against the "
           "paid media rather than beside it.")],
 "proof": [("case-klaviyo.html", "Flows out-earning campaigns on placed orders",
            "Recipients past 144,000 without revenue per send collapsing."),
           ("case-meta-ecom.html", "The acquisition side of the same store",
            "Purchase-optimised Meta campaigns at a 3.55x top ad-set return."),
           ("case-google-ads.html", "And the demand capture",
            "Search and Shopping at a 15.73x peak return.")],
 "faq": [("Do you work with Klaviyo only?",
          "Klaviyo is where the account evidence sits and where Shopify stores are best served. "
          "Other platforms are workable; the thinking does not change with the tool."),
         ("How long until flows are live?",
          "The core set is normally built and sending inside the first two to three weeks, "
          "starting with the flows that earn most."),
         ("Can you write the emails as well?",
          "Yes. Copy and design are part of the build rather than something handed back as a "
          "brief."),
         ("What about SMS?",
          "Where it suits the market and the consent position is clean, it runs alongside email "
          "in the same flows.")],
},
{
 "slug": "photography-video-production",
 "nav": "Photo &amp; video",
 "icon": "camera",
 "art": "photography-video",
 "art_alt": "A camera on a tripod beside a lighting stand and a framed shot",
 "eyebrow": "Production",
 "h1": "Photography and video production",
 "title": "Brand Photography &amp; Video Production | Isuru Marasinghe",
 "desc": ("Photography and video direction for brands and events, including Fortune 500 event "
          "coverage for Zoom and CNBC, produced with the paid media it feeds in mind."),
 "lede": ("I shoot as well as buy media, which means the production is planned around what the "
          "ad accounts will need rather than delivered as a gallery and reformatted afterwards."),
 "service_type": "Photography and video production",
 "why_h": "Production planned backwards from the ad account",
 "why": ["One shoot, many cuts. Framing that survives a 9:16 crop and a 1:1 crop is decided on "
         "set, not in the edit, which is where most asset libraries lose half their usable "
         "frames.",
         "Shot lists built from angles. The call sheet is derived from the propositions the "
         "account needs to test, so the footage maps onto the creative plan.",
         "Event coverage that holds up. Fortune 500 events for Zoom and CNBC, where there is no "
         "second take and the deliverable is due the same week."],
 "does": [("camera", "Brand and product photography", "Studio and location, shot for catalogue, "
           "site and paid social at once."),
          ("play", "Video direction", "Concept, shot list, direction and edit, for ads and for "
           "brand film."),
          ("spark", "Event and conference coverage", "Stills and video, including Fortune 500 "
           "event work."),
          ("layers", "Asset libraries", "Delivered in the crops and formats each placement "
           "actually takes."),
          ("compass", "Creative direction on set", "Direction of talent and framing against the "
           "angles the account is testing.")],
 "proof": [("case-tiktok-leads.html", "Native vertical production at pace",
            "35 campaigns, produced for the platform rather than cropped to it."),
           ("case-meta-ecom.html", "Creative lane feeding the scaling set",
            "Test creative judged separately and promoted on merit."),
           ("case-meta-leads.html", "Creative variety behind the volume",
            "5,364 leads across mechanics run against each other.")],
 "faq": [("Do you travel for shoots?",
          "Yes, across the UAE, to Sri Lanka and further where the production justifies it."),
         ("Is production available without the media management?",
          "Yes, as a standalone engagement. Most clients come for one and add the other."),
         ("What do you deliver?",
          "Edited stills and cuts in the formats each placement takes, plus the raw files and "
          "project files on request."),
         ("Can you work with our existing agency or in-house team?",
          "Yes, as the director and shooter inside their process.")],
},
{
 "slug": "fractional-cmo",
 "nav": "Fractional CMO",
 "icon": "compass",
 "art": "fractional-lead",
 "art_alt": "A performance dashboard reviewed above a small team",
 "eyebrow": "Advisory &amp; leadership",
 "h1": "Fractional CMO and performance lead",
 "title": "Fractional CMO &amp; Digital Marketing Strategy Consultant | Isuru Marasinghe",
 "desc": ("A fractional CMO and digital marketing strategy consultant: marketing strategy, "
          "forecasting, account oversight and team leadership for companies with hands on the "
          "work but nobody owning the number."),
 "lede": ("Plenty of companies have people who can run the ads and nobody who owns the number. A "
          "fractional CMO is the senior layer without the salary: marketing strategy, forecasts, "
          "account oversight, team leadership and the uncomfortable question in the weekly "
          "review."),
 "service_type": "Marketing consulting",
 "why_h": "What the role actually covers",
 "why": ["Owning the forecast. What the spend should be, what it should return, and what has to "
         "be true for that to happen, stated in advance rather than explained afterwards.",
         "Oversight of whoever is executing. In-house, agency or freelance, the work gets "
         "reviewed against the plan by someone who has run the accounts themselves.",
         "Decisions, not decks. The output is what to change this week, with the reasoning "
         "attached, in a format the founder can act on without a translator."],
 "does": [("chart", "Strategy and forecasting", "Channel mix, budget allocation and the "
           "forecast the plan is held to."),
          ("search", "Account oversight", "Regular review of the accounts and the tracking "
           "behind them, whoever is running them."),
          ("layers", "Team direction", "Hiring input, briefing standards and the review rhythm "
           "that keeps quality steady."),
          ("flow", "Vendor management", "Agency and freelancer selection, scoping and "
           "accountability."),
          ("compass", "Board and investor reporting", "The numbers framed so they survive a "
           "board meeting.")],
 "proof": [("case-crm-closings.html", "Reporting that runs to revenue",
            "Media spend read against USD 36.6M of closed deals."),
           ("case-google-ads.html", "Performance held over time",
            "Four monthly snapshots rather than one flattering month."),
           ("case-meta-ecom.html", "Structure that keeps learning",
            "A test lane and a scaling set judged on different terms.")],
 "faq": [("How much time does a fractional CMO take?",
          "Typically a day or two a week, set by the size of the team and the spend. The scope is "
          "agreed before it starts rather than billed by surprise."),
         ("Do you take over the accounts?",
          "Only if that is what the engagement calls for. The usual arrangement keeps your team "
          "or agency executing while the strategy and oversight sit with me."),
         ("Will you help us hire?",
          "Yes: role definition, screening, trial tasks and onboarding."),
         ("How is progress reported?",
          "A weekly written review against the forecast, and a monthly session with whoever needs "
          "to see it, including the board.")],
},
]

BY_SLUG = {s["slug"]: s for s in SERVICES}

NAV_LINKS = [(s["slug"], s["nav"], s["icon"]) for s in SERVICES]


def nav(prefix=""):
    """Site navigation. prefix is '../' for pages inside services/."""
    items = "\n".join(
        '          <a href="%sservices/%s.html">%s%s</a>' % (prefix, slug, icon(ic), label)
        for slug, label, ic in NAV_LINKS)
    return f"""      <div class="has-menu">
        <a class="menu-top" href="{prefix}services/">Services</a>
        <div class="menu" role="group" aria-label="Services">
{items}
          <a class="menu-all" href="{prefix}services/">All services<span class="arrow" aria-hidden="true">&rarr;</span></a>
        </div>
      </div>
      <a href="{prefix}index.html#work">Results</a>
      <a href="{prefix}index.html#clients">Clients</a>
      <a href="{prefix}index.html#credentials">Credentials</a>
      <a href="{prefix}about.html">About</a>
      <a href="{prefix}index.html#contact">Contact</a>"""


def footer_services(prefix=""):
    return "\n".join(
        '      <a href="%sservices/%s.html">%s</a>' % (prefix, s["slug"], strip(s["nav"]))
        for s in SERVICES)


SOCIALS = """      <a class="soc" href="https://www.linkedin.com/in/isuru-marasinghe/" target="_blank" rel="noopener me" aria-label="Isuru Marasinghe on LinkedIn" title="LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9.5h4v11H3v-11Zm6.5 0h3.83v1.5h.05c.53-.95 1.84-1.95 3.78-1.95 4.04 0 4.79 2.5 4.79 5.76v5.69h-4v-5.05c0-1.2-.02-2.75-1.73-2.75-1.73 0-2 1.31-2 2.66v5.14h-4v-11Z"/></svg></a>
      <a class="soc" href="https://www.facebook.com/isurupm" target="_blank" rel="noopener me" aria-label="Isuru Marasinghe on Facebook" title="Facebook"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06c0 5.02 3.66 9.18 8.44 9.94v-7.03H7.9v-2.91h2.54V9.85c0-2.52 1.49-3.91 3.77-3.91 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.78-1.63 1.57v1.89h2.78l-.45 2.91h-2.33V22c4.78-.76 8.44-4.92 8.44-9.94Z"/></svg></a>
      <a class="soc" href="https://www.instagram.com/x_isuru_x/" target="_blank" rel="noopener me" aria-label="Isuru Marasinghe on Instagram" title="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1.2" fill="currentColor" stroke="none"/></svg></a>"""


def strip(s):
    return html.unescape(s)


def shell(prefix, title, desc, canon, body, extra_ld, crumb_label):
    """One page, head to footer. prefix reaches the site root from this page."""
    ld = "\n".join('<script type="application/ld+json">\n%s\n</script>'
                   % json.dumps(b, indent=2) for b in extra_ld)
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
<title>{title}</title>
<meta name="google-site-verification" content="{VERIFY}" />
<meta name="description" content="{html.escape(strip(desc))}">
<meta name="author" content="Isuru Marasinghe">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="canonical" href="{canon}">
<meta property="og:url" content="{canon}">
<meta property="og:site_name" content="Isuru Marasinghe">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{html.escape(strip(desc))}">
<meta property="og:type" content="website">
<meta property="og:image" content="{SITE}assets/img/og-cover.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{OG_ALT}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{html.escape(strip(desc))}">
<meta name="twitter:image" content="{SITE}assets/img/og-cover.jpg">
<meta name="theme-color" content="#FFFFFF">
<link rel="icon" href="{prefix}favicon.ico" sizes="48x48 32x32 16x16">
<link rel="icon" type="image/png" sizes="96x96" href="{prefix}favicon-96x96.png">
<link rel="icon" type="image/png" sizes="32x32" href="{prefix}favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{prefix}favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="{prefix}apple-touch-icon.png">
<link rel="manifest" href="{prefix}site.webmanifest">
<link rel="preload" href="{prefix}assets/fonts/HankenGrotesk.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{prefix}assets/fonts/InstrumentSans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{prefix}assets/css/site.css">
{ld}
</head>
<body>

<header class="top">
  <div class="wrap top-inner">
    <a class="mark" href="{prefix}index.html" aria-label="Isuru Marasinghe, back to the home page"><img src="{prefix}assets/img/wordmark.svg" alt="Isuru Marasinghe" width="661" height="152"></a>
    <nav class="nav" aria-label="Sections">
{nav(prefix)}
    </nav>
    <div class="top-actions">
      <a class="btn btn-primary btn-sm" href="https://calendly.com/isurumarasinghe/30min" target="_blank" rel="noopener">Book a call</a>
    </div>
  </div>
</header>

<main id="top">
{body}
</main>

<div class="wa" id="wa-widget">
  <a class="wa-btn" id="wa-btn" href="https://wa.me/971529127002?text=Hi%20Isuru%2C%20I%27d%20like%20to%20talk%20about%20a%20project." target="_blank" rel="noopener" aria-label="Chat with Isuru Marasinghe on WhatsApp">
    <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-1 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.5-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>
  </a>
</div>

<footer>
  <div class="wrap foot-grid">
    <div class="foot-col">
      <span class="h">Services</span>
{footer_services(prefix)}
    </div>
    <div class="foot-col">
      <span class="h">Work</span>
      <a href="{prefix}index.html#work">Case studies</a>
      <a href="{prefix}index.html#clients">Clients</a>
      <a href="{prefix}index.html#credentials">Credentials</a>
      <a href="{prefix}about.html">About Isuru</a>
    </div>
    <div class="foot-col">
      <span class="h">Contact</span>
      <a href="mailto:hello@isurumarasinghe.com">hello@isurumarasinghe.com</a>
      <a href="https://calendly.com/isurumarasinghe/30min" target="_blank" rel="noopener">Book a discovery call</a>
      <a href="https://wa.me/971529127002" target="_blank" rel="noopener">WhatsApp</a>
      <span class="q">Dubai, UAE &middot; working worldwide</span>
    </div>
  </div>
  <div class="wrap foot">
    <span>&copy; 2026 Isuru Marasinghe &middot; Full Stack Digital Marketer</span>
    <span class="links">
{SOCIALS}
      <a href="{prefix}index.html">Home</a></span>
  </div>
</footer>

<script src="{prefix}assets/js/site.js" defer></script>
</body>
</html>
"""


def service_page(sv):
    prefix = "../"
    url = SITE + "services/" + sv["slug"] + ".html"
    others = [s for s in SERVICES if s["slug"] != sv["slug"]][:4]

    why = "\n".join('      <p>%s</p>' % p for p in sv["why"])
    does = "\n".join(
        '        <li><span class="ic" aria-hidden="true">%s</span><h3>%s</h3><p>%s</p></li>'
        % (icon(ic), h, b) for ic, h, b in sv["does"])
    proof = "\n".join(
        '        <a class="svc-proof" href="%s%s"><span class="t">%s</span><span class="d">%s</span>'
        '<span class="more">Read the case<span class="arrow" aria-hidden="true">&rarr;</span></span></a>'
        % (prefix, href, t, d) for href, t, d in sv["proof"])
    faq = "\n".join(
        '      <details class="faq"><summary>%s</summary><p>%s</p></details>' % (q, a)
        for q, a in sv["faq"])
    siblings = "\n".join(
        '        <a class="svc-next" href="%s.html"><span class="ic" aria-hidden="true">%s</span>'
        '<span>%s</span></a>' % (o["slug"], icon(o["icon"]), strip(o["h1"])) for o in others)

    body = f"""
<article class="casestudy service">
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb"><a href="{prefix}index.html">Isuru Marasinghe</a><span aria-hidden="true">/</span><a href="./">Services</a><span aria-hidden="true">/</span><span>{strip(sv['h1'])}</span></nav>

    <header class="cs-head split-head reveal">
      <div class="t">
        <span class="eyebrow">{sv['eyebrow']}</span>
        <h1>{sv['h1']}</h1>
      </div>
      <div class="d">
        <p class="lede">{sv['lede']}</p>
        <div class="row">
          <a class="btn btn-primary" href="https://calendly.com/isurumarasinghe/30min" target="_blank" rel="noopener">Book a discovery call</a>
          <a class="btn btn-ghost" href="{prefix}index.html#work">See the results</a>
        </div>
      </div>
    </header>

    <figure class="svc-art reveal">
      <img src="{prefix}assets/img/services/{sv['art']}.svg" alt="{html.escape(sv['art_alt'])}" width="800" height="360" loading="lazy" decoding="async">
    </figure>

    <section class="svc-sec reveal" aria-labelledby="svc-why">
      <div class="h"><h2 id="svc-why">{sv['why_h']}</h2></div>
      <div class="c">
{why}
      </div>
    </section>

    <section class="svc-sec reveal" aria-labelledby="svc-does">
      <div class="h"><h2 id="svc-does">What the engagement covers</h2></div>
      <div class="c">
        <ul class="svc-list">
{does}
        </ul>
      </div>
    </section>

    <section class="svc-sec reveal" aria-labelledby="svc-proof">
      <div class="h"><h2 id="svc-proof">The accounts behind this</h2></div>
      <div class="c">
        <div class="svc-proofs">
{proof}
        </div>
      </div>
    </section>

    <section class="svc-sec reveal" aria-labelledby="svc-faq">
      <div class="h"><h2 id="svc-faq">Questions I get asked</h2></div>
      <div class="c">
{faq}
      </div>
    </section>

    <section class="svc-sec reveal" aria-labelledby="svc-next">
      <div class="h"><h2 id="svc-next">Other services</h2></div>
      <div class="c">
        <div class="svc-nexts">
{siblings}
        </div>
      </div>
    </section>

    <div class="cs-cta reveal">
      <div>
        <h2>Let's look at your account.</h2>
        <p class="lede">Thirty minutes, no charge, wherever you are. You leave knowing what I would change first, whether or not we work together.</p>
      </div>
      <div class="row">
        <a class="btn btn-primary" href="https://calendly.com/isurumarasinghe/30min" target="_blank" rel="noopener">Book a discovery call</a>
        <a class="btn btn-ghost" href="{prefix}index.html#contact">Send an inquiry</a>
      </div>
    </div>
  </div>
</article>
"""

    service_ld = {
      "@context": "https://schema.org",
      "@type": "Service",
      "name": strip(sv["h1"]),
      "serviceType": sv["service_type"],
      "url": url,
      "description": strip(sv["desc"]),
      "provider": {"@type": "Person", "@id": PERSON, "name": "Isuru Marasinghe", "url": SITE},
      "areaServed": {"@type": "Place", "name": "Worldwide"},
      "availableChannel": {
        "@type": "ServiceChannel",
        "serviceUrl": "https://calendly.com/isurumarasinghe/30min",
        "servicePhone": "+971529127002",
        "availableLanguage": "English",
      },
      "inLanguage": "en",
    }
    faq_ld = {
      "@context": "https://schema.org", "@type": "FAQPage",
      "mainEntity": [{"@type": "Question", "name": strip(q),
                      "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
                     for q, a in sv["faq"]],
    }
    crumbs = {
      "@context": "https://schema.org", "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Isuru Marasinghe", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": "Services", "item": SITE + "services/"},
        {"@type": "ListItem", "position": 3, "name": strip(sv["h1"]), "item": url},
      ],
    }
    return shell(prefix, sv["title"], sv["desc"], url, body,
                 [service_ld, faq_ld, crumbs], strip(sv["h1"]))


def hub_page():
    prefix = "../"
    url = SITE + "services/"
    cards = "\n".join(
        '        <a class="svc-card" href="%s.html">\n'
        '          <span class="ic" aria-hidden="true">%s</span>\n'
        '          <h2>%s</h2>\n'
        '          <p>%s</p>\n'
        '          <span class="more">Read more<span class="arrow" aria-hidden="true">&rarr;</span></span>\n'
        '        </a>' % (s["slug"], icon(s["icon"]), s["h1"], s["lede"].split(". ")[0] + ".")
        for s in SERVICES)

    body = f"""
<article class="casestudy service">
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb"><a href="{prefix}index.html">Isuru Marasinghe</a><span aria-hidden="true">/</span><span>Services</span></nav>

    <header class="cs-head split-head reveal">
      <div class="t">
        <span class="eyebrow">What I do</span>
        <h1>Digital marketing services</h1>
      </div>
      <div class="d">
        <p class="lede">Nine disciplines that make up one funnel: the media that buys attention, the creative that earns it, the measurement that proves it and the lifecycle work that keeps it. Taken on together or separately, for brands wherever the work can be done.</p>
        <div class="row">
          <a class="btn btn-primary" href="https://calendly.com/isurumarasinghe/30min" target="_blank" rel="noopener">Book a discovery call</a>
          <a class="btn btn-ghost" href="{prefix}index.html#work">See the results</a>
        </div>
      </div>
    </header>

    <figure class="svc-art reveal">
      <img src="{prefix}assets/img/services/services.svg" alt="Creative, media, measurement and lifecycle as four stages of one funnel" width="800" height="360" loading="lazy" decoding="async">
    </figure>

    <section class="svc-sec wide reveal" aria-labelledby="svc-all">
      <div class="h"><h2 id="svc-all">The nine</h2></div>
      <div class="c">
        <div class="svc-cards">
{cards}
        </div>
      </div>
    </section>

    <div class="cs-cta reveal">
      <div>
        <h2>Not sure which you need?</h2>
        <p class="lede">That is what the call is for. Thirty minutes on your goals, your current spend and what is or is not working.</p>
      </div>
      <div class="row">
        <a class="btn btn-primary" href="https://calendly.com/isurumarasinghe/30min" target="_blank" rel="noopener">Book a discovery call</a>
        <a class="btn btn-ghost" href="{prefix}about.html">About Isuru</a>
      </div>
    </div>
  </div>
</article>
"""
    item_list = {
      "@context": "https://schema.org", "@type": "ItemList",
      "name": "Digital marketing services by Isuru Marasinghe",
      "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": strip(s["h1"]),
         "url": SITE + "services/" + s["slug"] + ".html"}
        for i, s in enumerate(SERVICES)],
    }
    crumbs = {
      "@context": "https://schema.org", "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Isuru Marasinghe", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": "Services", "item": url}],
    }
    return shell(prefix, "Digital Marketing Services | Isuru Marasinghe",
                 "Digital marketing services from a freelance specialist: paid media, creative "
                 "production, conversion tracking and lifecycle marketing. Nine services, taken "
                 "on together or separately, for clients worldwide.",
                 url, body, [item_list, crumbs], "Services")


def about_page():
    prefix = ""
    url = SITE + "about.html"
    comps = ["Performance marketing", "Paid media: Meta, Google, TikTok, LinkedIn, Snapchat",
             "Marketing strategy", "SEO and SEM", "CRM and funnel optimisation", "Branding",
             "Marketing automation", "Influencer and content marketing", "Analytics and GA4",
             "Team leadership", "Digital transformation"]
    comp_tags = "\n".join('          <span class="tag">%s</span>' % c for c in comps)

    body = f"""
<article class="casestudy service">
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb"><a href="index.html">Isuru Marasinghe</a><span aria-hidden="true">/</span><span>About</span></nav>

    <header class="cs-head split-head reveal">
      <div class="t">
        <span class="eyebrow">About</span>
        <h1>Isuru Marasinghe</h1>
      </div>
      <div class="d">
        <p class="lede">A strategic, performance-driven marketer who builds and scales data-driven digital ecosystems. Over USD 30 million in performance-driven revenue generated for clients to date, across real estate, education, technology and FMCG.</p>
        <div class="row">
          <a class="btn btn-primary" href="https://calendly.com/isurumarasinghe/30min" target="_blank" rel="noopener">Book a discovery call</a>
          <a class="btn btn-ghost" href="services/">See the services</a>
        </div>
      </div>
    </header>

    <figure class="svc-art reveal">
      <img src="assets/img/services/sri-lanka.svg" alt="Two markets linked by a flight path above a shared performance curve" width="800" height="360" loading="lazy" decoding="async">
    </figure>

    <section class="svc-sec reveal" aria-labelledby="ab-who">
      <div class="h"><h2 id="ab-who">Full stack, by necessity</h2></div>
      <div class="c">
        <p>I came up doing every part of the job rather than one slice of it, which is why the work spans creative, media, measurement and lifecycle instead of stopping at the ad account. Real estate, education, technology and FMCG all turned out to need the same thing: somebody who could see the whole funnel at once and was willing to be judged on what came out of the end of it.</p>
        <p>That perspective is the point. A media buyer who cannot direct creative is at the mercy of whatever arrives. A strategist who has never built the tracking does not know which numbers to trust. Holding all of it means the plan and the execution answer to each other.</p>
      </div>
    </section>

    <section class="svc-sec reveal" aria-labelledby="ab-how">
      <div class="h"><h2 id="ab-how">Analytical precision, creative storytelling</h2></div>
      <div class="c">
        <p>I design high-converting performance funnels, run paid media across Meta, Google, TikTok, LinkedIn and Snapchat, and optimise the SEO, CRM and lead flow behind them so the account beats its ROAS and conversion benchmarks rather than explaining why it did not.</p>
        <p>The half that gets neglected is the storytelling. Targeting is largely automated now; what is left for a marketer to decide is what the ad says and how it says it in the first three seconds. So the analysis sets the direction and the creative does the work, which is how brands end up connecting with an audience instead of merely reaching one.</p>
        <p>Underneath both sits a bias toward measurement. An account optimising against a badly mapped event gets worse the more you spend on it, so the tracking comes first and the media second. That is unglamorous and it is where most of the recoverable performance hides.</p>
      </div>
    </section>

    <section class="svc-sec reveal" aria-labelledby="ab-proof">
      <div class="h"><h2 id="ab-proof">Judged on what closed</h2></div>
      <div class="c">
        <p>Platforms report on what they can see and agencies report on what flatters them, which leaves the number everyone quietly avoids: what the spend actually turned into. The accounts here are reported past the click.</p>
        <p>On the real-estate pipeline that meant matching CRM stages back to the ad sets that created them, so AED 440,000 of media could be stated against AED 134,417,569 of closed property rather than against a cost per lead. It is a harder number to produce and the only one worth putting in front of a client.</p>
        <div class="svc-proofs">
          <a class="svc-proof" href="case-meta-leads.html"><span class="t">5,364 property leads from one Meta account</span><span class="d">AED 43.75 blended, with the cheapest ad set at AED 6.48.</span><span class="more">Read the case<span class="arrow" aria-hidden="true">&rarr;</span></span></a>
          <a class="svc-proof" href="case-crm-closings.html"><span class="t">USD 36.6M closed from direct leads</span><span class="d">75 deals, reported on sale value rather than form fills.</span><span class="more">Read the case<span class="arrow" aria-hidden="true">&rarr;</span></span></a>
          <a class="svc-proof" href="case-google-ads.html"><span class="t">Google Ads at a 15.73x return</span><span class="d">Four monthly snapshots rather than one good month.</span><span class="more">Read the case<span class="arrow" aria-hidden="true">&rarr;</span></span></a>
        </div>
      </div>
    </section>

    <section class="svc-sec reveal" aria-labelledby="ab-comp">
      <div class="h"><h2 id="ab-comp">Core competencies</h2></div>
      <div class="c">
        <div class="industry-tags" style="margin-top:0">
{comp_tags}
        </div>
      </div>
    </section>

    <section class="svc-sec reveal" aria-labelledby="ab-where">
      <div class="h"><h2 id="ab-where">Where the work happens</h2></div>
      <div class="c">
        <p>I am Sri Lankan, I live in Dubai, and the client base has never been limited to either. Paid media runs from the platforms rather than from a desk in a particular city, so the practical constraint is the working day, not the map. Dubai overlaps the UK morning, the whole of South Asia and the start of the US east coast, which covers most of where clients have been.</p>
        <p>What does not travel is local knowledge. A cost per lead that looks strong in Colombo means something different in Dubai, so accounts spanning both are read per market rather than blended into one flattering average. Several of the education and migration brands do exactly that: selling into one market and delivering in another.</p>
      </div>
    </section>

    <section class="svc-sec reveal" aria-labelledby="ab-cred">
      <div class="h"><h2 id="ab-cred">Qualifications</h2></div>
      <div class="c">
        <p>MBA (UK), ACIM (UK), PgDip.M (UK), a postgraduate diploma in strategic management and leadership, AMSLIM (SL), Certified Lean Six Sigma White Belt, CDMP (USA) from the American Institute of Professional Qualification, and a first-class BM (Hons) in Marketing from Horizon Campus, Sri Lanka.</p>
        <p>Fifteen platform and institute certifications sit alongside those: Meta Certified Digital Marketing Associate and Creative Strategy Professional, Microsoft Advertising Search and Retail, Apple Ads, LinkedIn Certified Marketing Insider and the rest, listed with the badges on the <a href="index.html#credentials">home page</a>.</p>
      </div>
    </section>

    <div class="cs-cta reveal">
      <div>
        <h2>Let's talk.</h2>
        <p class="lede">Thirty minutes, no charge, in whichever time zone suits.</p>
      </div>
      <div class="row">
        <a class="btn btn-primary" href="https://calendly.com/isurumarasinghe/30min" target="_blank" rel="noopener">Book a discovery call</a>
        <a class="btn btn-ghost" href="services/">See the services</a>
      </div>
    </div>
  </div>
</article>
"""
    about_ld = {
      "@context": "https://schema.org", "@type": "AboutPage",
      "url": url, "name": "About Isuru Marasinghe",
      "mainEntity": {"@id": PERSON},
      "inLanguage": "en",
    }
    crumbs = {
      "@context": "https://schema.org", "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Isuru Marasinghe", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": "About", "item": url}],
    }
    return shell(prefix, "About Isuru Marasinghe — Full Stack Digital Marketer",
                 "Isuru Marasinghe is a performance-driven digital marketer working across real "
                 "estate, education, technology and FMCG. Over USD 30 million in performance "
                 "revenue generated for clients.",
                 url, body, [about_ld, crumbs], "About")


if __name__ == "__main__":
    out = os.path.join(ROOT, "services")
    os.makedirs(out, exist_ok=True)
    for sv in SERVICES:
        with open(os.path.join(out, sv["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(service_page(sv))
        print("wrote services/" + sv["slug"] + ".html")
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(hub_page())
    print("wrote services/index.html")
    with open(os.path.join(ROOT, "about.html"), "w", encoding="utf-8") as f:
        f.write(about_page())
    print("wrote about.html")
