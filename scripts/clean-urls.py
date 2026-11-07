#!/usr/bin/env python3
"""One-time migration to extensionless URLs.

The site is a set of static files, so Apache serves them at their real names:
/about.html, /services/meta-ads-management.html. Netlify used to hide the
extension automatically; LiteSpeed does not, which is why /about returned 404
after the move to shared hosting.

This rewrites every internal link, canonical, og:url and structured-data URL in
the hand-written index.html and in the two page generators so that one address
exists per page:

    /                               home
    /about                          about
    /services/                      services hub (a real directory)
    /services/<slug>                a service
    /case-<slug>                    a case study

.htaccess serves those from the .html files on disk and 301s any .html request
onto them, so old links and anything Google already indexed keep working.

Run once:  python3 scripts/clean-urls.py
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


def sub_all(text, pairs, label, report):
    for pattern, repl in pairs:
        text, n = re.subn(pattern, repl, text)
        if n:
            report.append("  %-58s %d" % (label + ": " + pattern[:50], n))
    return text


def migrate_index(report):
    p = ROOT / "index.html"
    s = p.read_text(encoding="utf-8")
    pairs = [
        # The logo is a link home, not a scroll to the top of the current page:
        # "#top" put a fragment in the address bar on every visit.
        (r'<a class="mark" href="#top" aria-label="Isuru Marasinghe, back to top">',
         '<a class="mark" href="/" aria-label="Isuru Marasinghe, back to the home page">'),
        # Self-links written as index.html#section reload the page for no reason.
        (r'href="index\.html#', 'href="#'),
        (r'href="index\.html"', 'href="/"'),
        (r'href="about\.html"', 'href="/about"'),
        (r'href="(case-[a-z-]+)\.html"', r'href="/\1"'),
        (r'href="services/([a-z0-9-]+)\.html"', r'href="/services/\1"'),
        (r'href="services/"', 'href="/services/"'),
        # Canonical, og:url and structured data.
        (r'(https://isurumarasinghe\.com/)about\.html', r'\1about'),
        (r'(https://isurumarasinghe\.com/)(case-[a-z-]+)\.html', r'\1\2'),
        (r'(https://isurumarasinghe\.com/services/)([a-z0-9-]+)\.html', r'\1\2'),
    ]
    out = sub_all(s, pairs, "index.html", report)
    p.write_text(out, encoding="utf-8")


def migrate_generator(name, report):
    p = ROOT / "scripts" / name
    s = p.read_text(encoding="utf-8")
    pairs = [
        # Nav and footer links, with or without the ../ prefix used by subpages.
        (r'href="\{prefix\}index\.html#', 'href="/#'),
        (r'href="\{prefix\}index\.html"', 'href="/"'),
        (r'href="\{prefix\}about\.html"', 'href="/about"'),
        (r'href="\{prefix\}services/"', 'href="/services/"'),
        (r'href="%sservices/%s\.html"', 'href="/services/%s"'),
        (r'href="index\.html#', 'href="/#'),
        (r'href="index\.html"', 'href="/"'),
        (r'href="about\.html"', 'href="/about"'),
        (r'href="services/([a-z0-9-]+)\.html"', r'href="/services/\1"'),
        (r'href="services/"', 'href="/services/"'),
        (r'href="\{prv\[.slug.\]\}\.html"', 'href="/{prv[\'slug\']}"'),
        (r'href="\{nxt\[.slug.\]\}\.html"', 'href="/{nxt[\'slug\']}"'),
        (r'href="(case-[a-z-]+)\.html"', r'href="/\1"'),
        # Links written inside service-page copy, relative to /services/.
        (r'href=\\"([a-z-]+)\.html\\"', r'href=\\"/services/\1\\"'),
        # Canonicals, og:url and structured-data URLs.
        (r'\{SITE\}\{case\[.slug.\]\}\.html', "{SITE}{case['slug']}"),
        (r'SITE \+ "services/" \+ sv\["slug"\] \+ "\.html"', 'SITE + "services/" + sv["slug"]'),
        (r'SITE \+ "services/" \+ s\["slug"\] \+ "\.html"', 'SITE + "services/" + s["slug"]'),
        (r'SITE \+ "about\.html"', 'SITE + "about"'),
    ]
    out = sub_all(s, pairs, name, report)
    p.write_text(out, encoding="utf-8")


def migrate_sitemap(report):
    p = ROOT / "sitemap.xml"
    s = p.read_text(encoding="utf-8")
    out, n = re.subn(r'(<loc>https://isurumarasinghe\.com/[^<]*?)\.html</loc>', r'\1</loc>', s)
    report.append("  %-58s %d" % ("sitemap.xml: <loc> entries", n))
    p.write_text(out, encoding="utf-8")


def main():
    report = []
    migrate_index(report)
    migrate_generator("build-services.py", report)
    migrate_generator("build-cases.py", report)
    migrate_sitemap(report)
    print("\n".join(report) or "nothing to change")
    # Nothing internal should still point at a .html page.
    leftovers = []
    for f in [ROOT / "index.html", ROOT / "sitemap.xml",
              ROOT / "scripts" / "build-services.py", ROOT / "scripts" / "build-cases.py"]:
        for m in re.finditer(r'href="[^"]*?(?<!\.css)(?<!\.js)\.html[^"]*"|<loc>[^<]*\.html</loc>',
                             f.read_text(encoding="utf-8")):
            leftovers.append("%s: %s" % (f.name, m.group(0)[:90]))
    if leftovers:
        print("\nSTILL POINTING AT .html:")
        print("\n".join("  " + x for x in leftovers))
        return 1
    print("\nno internal .html links remain")
    return 0


if __name__ == "__main__":
    sys.exit(main())
