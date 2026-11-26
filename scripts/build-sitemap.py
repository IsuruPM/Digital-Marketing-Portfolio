#!/usr/bin/env python3
"""Generate sitemap.xml from the pages that actually exist.

It was maintained by hand, so <lastmod> went stale the moment a page changed:
it still read 2026-11-03 after the move to extensionless URLs. A lastmod in the
past tells a crawler nothing has changed since then, which is the opposite of
what you want right after a URL migration, and it showed up in Search Console
as case pages stuck on "Discovered - currently not indexed".

lastmod now comes from the date of the last commit that touched each page, so
it is accurate, reproducible, and never older than the content. A page not yet
committed falls back to its file modification time.

Run:  python3 scripts/build-sitemap.py
"""
import datetime
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://isurumarasinghe.com"

# Priority by kind of page. The home page outranks the hubs, which outrank the
# service pages, which outrank the case studies.
PRIORITY = {"home": "1.0", "hub": "0.9", "service": "0.8", "case": "0.7"}


def last_changed(rel):
    """Date of the last commit touching this file, else its mtime."""
    path = os.path.join(ROOT, rel)
    try:
        out = subprocess.run(
            ["git", "-C", ROOT, "log", "-1", "--format=%cs", "--", rel],
            capture_output=True, text=True, timeout=15)
        stamp = out.stdout.strip()
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", stamp):
            return stamp
    except Exception:
        pass
    try:
        return datetime.date.fromtimestamp(os.path.getmtime(path)).isoformat()
    except OSError:
        return datetime.date.today().isoformat()


def pages():
    """(url, file, kind) for every indexable page, in sitemap order."""
    out = [(SITE + "/", "index.html", "home")]
    if os.path.exists(os.path.join(ROOT, "services", "index.html")):
        out.append((SITE + "/services/", "services/index.html", "hub"))
    if os.path.exists(os.path.join(ROOT, "about.html")):
        out.append((SITE + "/about", "about.html", "hub"))
    if os.path.exists(os.path.join(ROOT, "work.html")):
        out.append((SITE + "/work", "work.html", "hub"))

    svc_dir = os.path.join(ROOT, "services")
    if os.path.isdir(svc_dir):
        for name in sorted(os.listdir(svc_dir)):
            if name.endswith(".html") and name != "index.html":
                slug = name[:-5]
                out.append((SITE + "/services/" + slug, "services/" + name, "service"))

    for name in sorted(os.listdir(ROOT)):
        if re.fullmatch(r"case-[a-z0-9-]+\.html", name):
            out.append((SITE + "/" + name[:-5], name, "case"))
    return out


def noindexed(rel):
    try:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            return re.search(r'<meta[^>]+name="robots"[^>]+noindex', f.read()) is not None
    except OSError:
        return True


# Images to surface in Google Images, per page. His photographs are listed first
# and with his name, so the portrait and headshot can be discovered and indexed.
IMAGES = {
    "index.html": [
        ("assets/img/portrait-cover.jpg", "Isuru Marasinghe, full stack digital marketer and media buyer in Dubai"),
        ("assets/img/portrait-profile.jpg", "Isuru Marasinghe, performance marketer and creative strategist"),
    ],
    "about.html": [
        ("assets/img/about/headshot.jpg", "Isuru Marasinghe, full stack digital marketer"),
        ("assets/img/portrait-profile.jpg", "Isuru Marasinghe, performance marketer in Dubai"),
        ("assets/img/about/graduation-mba.jpg", "Isuru Marasinghe graduating with an MBA from the University of Gloucestershire"),
        ("assets/img/about/graduation-cim.jpg", "Isuru Marasinghe graduating from the Chartered Institute of Marketing"),
        ("assets/img/about/graduation-esm.jpg", "Isuru Marasinghe at the ESM Business School and AIPQ graduation"),
        ("assets/img/about/graduation-horizon.jpg", "Isuru Marasinghe graduating from Horizon Campus, Sri Lanka"),
    ],
}
CASE_SHOTS = {
    "case-meta-leads.html": "assets/img/results/meta-leads-realestate.jpg",
    "case-crm-closings.html": "assets/img/results/crm-closings.jpg",
    "case-meta-ecom.html": "assets/img/results/meta-ecom-roas-1.jpg",
    "case-google-ads.html": "assets/img/results/google-sep-2024.jpg",
    "case-klaviyo.html": "assets/img/results/klaviyo-placed-order.jpg",
    "case-highered-leads.html": "assets/img/results/highered-leads.jpg",
    "case-fitout-whatsapp.html": "assets/img/results/fitout-whatsapp.jpg",
    "case-fitness-leads.html": "assets/img/results/fitness-leads.jpg",
    "case-fragrance-ecom.html": "assets/img/results/fragrance-ecom.jpg",
}


def _img_xml(rel):
    imgs = list(IMAGES.get(rel, []))
    if rel in CASE_SHOTS:
        imgs.append((CASE_SHOTS[rel], "Platform report by Isuru Marasinghe (account names blurred)"))
    out = []
    for src, cap in imgs:
        if os.path.exists(os.path.join(ROOT, src)):
            out.append("    <image:image>\n      <image:loc>%s/%s</image:loc>\n"
                       "      <image:caption>%s</image:caption>\n    </image:image>"
                       % (SITE.rstrip("/"), src, cap))
    return ("\n" + "\n".join(out)) if out else ""


def main():
    rows = []
    for url, rel, kind in pages():
        if noindexed(rel):
            print("skipping noindex page:", rel, file=sys.stderr)
            continue
        rows.append(
            "  <url>\n"
            "    <loc>%s</loc>\n"
            "    <lastmod>%s</lastmod>\n"
            "    <changefreq>monthly</changefreq>\n"
            "    <priority>%s</priority>%s\n"
            "  </url>" % (url, last_changed(rel), PRIORITY[kind], _img_xml(rel)))

    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
           '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    print("wrote sitemap.xml with %d URLs" % len(rows))


if __name__ == "__main__":
    main()
