#!/usr/bin/env python3
"""Draw the monochrome hero illustration for each service page.

Same vocabulary as the case tile covers in assets/img/covers: a sunk ground, white
fills, ink line work at 1.5 and a mid grey for anything secondary. 800x360, so they
sit as a banner above the page copy. Run: python3 scripts/build-service-art.py
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "img", "services")

INK = "#17191B"
MID = "#8E9296"
SUNK = "#F3F3F2"
LINE = "#D8D6D3"

HEAD = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 360" fill="none" '
        'stroke="%s" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" '
        'role="img" aria-label="%s">\n'
        '  <rect width="800" height="360" fill="%s" stroke="none"/>\n')
FOOT = '</svg>\n'


def frame(x, y, w, h, r=10, fill="#FFFFFF"):
    return ('  <rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s"/>\n'
            % (x, y, w, h, r, fill))


def rows(x, y, widths, gap=13, color=MID, sw=4):
    out = '  <g stroke="%s" stroke-width="%s" opacity=".55">\n' % (color, sw)
    for i, w in enumerate(widths):
        out += '    <line x1="%s" y1="%s" x2="%s" y2="%s"/>\n' % (x, y + i * gap, x + w, y + i * gap)
    return out + '  </g>\n'


ART = {}

# ---------------------------------------------------------------- Meta ads
ART["meta-ads"] = (
    "Two phone screens running a lead form, with the form fields filling in",
    frame(96, 40, 180, 280, 18)
    + frame(118, 70, 136, 60, 6, SUNK)
    + rows(132, 92, [96, 72, 84], 14)
    + frame(118, 146, 136, 14, 7, SUNK)
    + frame(118, 172, 136, 14, 7, SUNK)
    + frame(118, 198, 136, 14, 7, SUNK)
    + frame(118, 232, 136, 30, 15, INK)
    + frame(300, 40, 180, 280, 18)
    + frame(322, 70, 136, 92, 6, SUNK)
    + '  <path d="M352 116 l24-22 20 18 18-16 22 20" stroke="%s"/>\n' % MID
    + rows(322, 182, [112, 88], 16)
    + frame(322, 222, 136, 30, 15, "#FFFFFF")
    + rows(338, 237, [60], 12, INK, 5)
    # funnel of impressions resolving into leads
    + '  <g stroke="%s" stroke-width="1.25" opacity=".7">\n' % MID
    + '    <path d="M536 70 H740 L700 128 H576 Z"/>\n'
    + '    <path d="M576 146 H700 L672 198 H604 Z"/>\n'
    + '    <path d="M604 216 H672 L656 262 H620 Z"/>\n'
    + '  </g>\n'
    + '  <g fill="%s" stroke="none">\n' % INK
    + '    <circle cx="638" cy="290" r="6"/>\n'
    + '  </g>\n'
    + '  <line x1="638" y1="262" x2="638" y2="282" stroke="%s" stroke-width="1.25"/>\n' % MID
)

# -------------------------------------------------------------- Google Ads
ART["google-ads"] = (
    "A search bar above sponsored results and a rising return curve",
    frame(80, 48, 420, 44, 22)
    + '  <circle cx="112" cy="70" r="9" stroke="%s"/>\n' % INK
    + '  <line x1="119" y1="77" x2="127" y2="85" stroke="%s"/>\n' % INK
    + rows(148, 70, [188], 12)
    + frame(432, 56, 56, 28, 14, INK)
    + frame(80, 116, 420, 64, 10)
    + '  <rect x="100" y="134" width="30" height="13" rx="6" fill="none" stroke="%s" stroke-width="1.2"/>\n' % MID
    + rows(146, 141, [150], 12, INK, 5)
    + rows(100, 164, [320], 12)
    + frame(80, 196, 420, 64, 10)
    + '  <rect x="100" y="214" width="30" height="13" rx="6" fill="none" stroke="%s" stroke-width="1.2"/>\n' % MID
    + rows(146, 221, [120], 12, INK, 5)
    + rows(100, 244, [280], 12)
    + frame(80, 276, 420, 44, 10, SUNK)
    + rows(100, 298, [190], 12)
    # the return curve
    + '  <g stroke="%s" stroke-width="1" opacity=".6">\n' % LINE
    + ''.join('    <line x1="548" y1="%s" x2="740" y2="%s"/>\n' % (y, y)
              for y in (92, 148, 204, 260))
    + '  </g>\n'
    + '  <path d="M548 274 L596 252 L644 204 L692 164 L740 84" stroke="%s" stroke-width="2"/>\n' % INK
    + '  <circle cx="740" cy="84" r="7" fill="#FFFFFF" stroke="%s" stroke-width="2"/>\n' % INK
    + '  <line x1="548" y1="300" x2="740" y2="300" stroke="%s"/>\n' % MID
)

# -------------------------------------------------------------- TikTok ads
ART["tiktok-ads"] = (
    "Three vertical video frames side by side with a play control and cost per lead falling",
    frame(92, 54, 150, 252, 14, SUNK)
    + '  <path d="M152 164 l44 26 -44 26 Z" fill="#FFFFFF" stroke="%s" stroke-width="2"/>\n' % INK
    + frame(258, 54, 150, 252, 14)
    + rows(278, 258, [96, 68], 16)
    + '  <g stroke="%s" stroke-width="1.4" opacity=".8">\n' % MID
    + '    <path d="M366 112 a10 10 0 1 1 -14 9 v-22 a14 14 0 0 0 14 13"/>\n'
    + '  </g>\n'
    + frame(424, 54, 150, 252, 14, SUNK)
    + '  <path d="M484 164 l44 26 -44 26 Z" fill="#FFFFFF" stroke="%s" stroke-width="2"/>\n' % INK
    # cost per lead stepping down across markets
    + '  <g stroke="%s" stroke-width="1" opacity=".6">\n' % LINE
    + ''.join('    <line x1="614" y1="%s" x2="742" y2="%s"/>\n' % (y, y) for y in (104, 160, 216))
    + '  </g>\n'
    + '  <g fill="%s" stroke="none">\n' % INK
    + '    <rect x="624" y="96" width="26" height="176" rx="3"/>\n'
    + '    <rect x="666" y="186" width="26" height="86" rx="3" fill="%s"/>\n' % MID
    + '    <rect x="708" y="240" width="26" height="32" rx="3" fill="%s"/>\n' % MID
    + '  </g>\n'
    + '  <line x1="610" y1="282" x2="746" y2="282" stroke="%s"/>\n' % MID
)

# ------------------------------------------------------------ LinkedIn ads
ART["linkedin-ads"] = (
    "Professional profile cards connected into a targeted audience",
    ''.join(
        frame(x, y, 150, 92, 10) +
        '  <circle cx="%s" cy="%s" r="16" fill="%s" stroke="none"/>\n' % (x + 32, y + 46, SUNK) +
        '  <circle cx="%s" cy="%s" r="6" stroke="%s" stroke-width="1.4"/>\n' % (x + 32, y + 41, MID) +
        '  <path d="M%s %s a10 10 0 0 1 20 0" stroke="%s" stroke-width="1.4"/>\n' % (x + 22, y + 56, MID) +
        rows(x + 60, y + 38, [66, 48], 14)
        for x, y in ((86, 42), (86, 160))
    )
    + frame(86, 254, 150, 72, 10)
    + '  <circle cx="118" cy="290" r="16" fill="%s" stroke="none"/>\n' % SUNK
    + '  <circle cx="118" cy="285" r="6" stroke="%s" stroke-width="1.4"/>\n' % MID
    + '  <path d="M108 300 a10 10 0 0 1 20 0" stroke="%s" stroke-width="1.4"/>\n' % MID
    + rows(146, 282, [66, 48], 14)
    + '  <g stroke="%s" stroke-width="1.25" opacity=".75">\n' % MID
    + '    <path d="M236 88 C300 88 300 182 356 182"/>\n'
    + '    <path d="M236 206 H356"/>\n'
    + '    <path d="M236 290 C300 290 300 196 356 196"/>\n'
    + '  </g>\n'
    + frame(356, 128, 170, 124, 12, SUNK)
    + rows(382, 164, [118, 92, 70], 18, INK, 5)
    + '  <g stroke="%s" stroke-width="1.25" opacity=".75"><path d="M526 190 H596"/></g>\n' % MID
    + frame(596, 112, 128, 156, 12)
    + rows(620, 146, [80, 56], 16)
    + '  <path d="M620 198 l22 20 42 -44" stroke="%s" stroke-width="2.5"/>\n' % INK
    + rows(620, 242, [62], 12, MID, 4)
)

# ------------------------------------------------- Creative direction
ART["creative-direction"] = (
    "A storyboard of three frames beside a stack of finished cuts",
    '  <g stroke="%s" stroke-width="1.25" opacity=".6">\n' % MID
    + '    <line x1="72" y1="40" x2="72" y2="320"/>\n'
    + '  </g>\n'
    + ''.join(
        frame(104, y, 196, 72, 8)
        + '  <rect x="118" y="%s" width="52" height="44" rx="4" fill="%s" stroke="none"/>\n' % (y + 14, SUNK)
        + '  <path d="M126 %s l14 -14 12 12 10 -9" stroke="%s" stroke-width="1.4"/>\n' % (y + 46, MID)
        + rows(188, y + 28, [86, 62], 16)
        for y in (40, 132, 224))
    + '  <g stroke="%s" stroke-width="1.25" opacity=".75">\n' % MID
    + '    <path d="M300 76 C348 76 348 170 384 170"/>\n'
    + '    <path d="M300 168 H384"/>\n'
    + '    <path d="M300 260 C348 260 348 176 384 176"/>\n'
    + '  </g>\n'
    + frame(404, 84, 150, 190, 12, SUNK)
    + frame(420, 68, 150, 190, 12)
    + frame(436, 52, 150, 190, 12)
    + '  <path d="M488 128 l38 22 -38 22 Z" fill="%s" stroke="none"/>\n' % INK
    + rows(456, 212, [100, 72], 16)
    # pen marking the winner
    + '  <path d="M632 262 l74 -116 22 14 -74 116 -28 10 Z" fill="#FFFFFF" stroke="%s" stroke-width="1.6"/>\n' % INK
    + '  <line x1="706" y1="146" x2="728" y2="160" stroke="%s" stroke-width="1.6"/>\n' % MID
    + '  <path d="M620 300 h120" stroke="%s" stroke-width="2"/>\n' % INK
)

# ------------------------------------------------- Tracking and measurement
ART["conversion-tracking"] = (
    "A browser event passing through a tag manager and a server before reaching the ad platforms",
    frame(64, 118, 168, 124, 12)
    + '  <path d="M64 146 H232" stroke="%s" stroke-width="1.25"/>\n' % MID
    + '  <g fill="%s" stroke="none"><circle cx="82" cy="132" r="4"/><circle cx="96" cy="132" r="4"/><circle cx="110" cy="132" r="4"/></g>\n' % MID
    + rows(86, 176, [112, 84], 16)
    + frame(86, 206, 72, 22, 11, INK)
    + '  <g stroke="%s" stroke-width="1.5"><path d="M232 180 H296"/><path d="M286 172 l10 8 -10 8"/></g>\n' % INK
    + frame(296, 140, 132, 80, 10, SUNK)
    + '  <path d="M330 162 h64 M330 180 h44 M330 198 h54" stroke="%s" stroke-width="4" opacity=".6"/>\n' % MID
    + '  <circle cx="318" cy="162" r="4" fill="%s" stroke="none"/>\n' % INK
    + '  <circle cx="318" cy="180" r="4" fill="%s" stroke="none"/>\n' % INK
    + '  <circle cx="318" cy="198" r="4" fill="%s" stroke="none"/>\n' % INK
    + '  <g stroke="%s" stroke-width="1.5"><path d="M428 180 H492"/><path d="M482 172 l10 8 -10 8"/></g>\n' % INK
    + frame(492, 134, 112, 92, 10)
    + '  <g stroke="%s" stroke-width="1.4">\n' % MID
    + '    <rect x="512" y="152" width="72" height="20" rx="4"/>\n'
    + '    <rect x="512" y="186" width="72" height="20" rx="4"/>\n'
    + '  </g>\n'
    + '  <circle cx="524" cy="162" r="3.5" fill="%s" stroke="none"/>\n' % INK
    + '  <circle cx="524" cy="196" r="3.5" fill="%s" stroke="none"/>\n' % INK
    + '  <g stroke="%s" stroke-width="1.5">\n' % INK
    + '    <path d="M604 158 C650 158 650 102 692 102"/><path d="M682 94 l10 8 -10 8"/>\n'
    + '    <path d="M604 180 H692"/><path d="M682 172 l10 8 -10 8"/>\n'
    + '    <path d="M604 202 C650 202 650 258 692 258"/><path d="M682 250 l10 8 -10 8"/>\n'
    + '  </g>\n'
    + ''.join('  <circle cx="722" cy="%s" r="20" fill="#FFFFFF" stroke="%s" stroke-width="1.6"/>\n'
              % (cy, INK) for cy in (102, 180, 258))
    + ''.join('  <path d="M712 %s l7 7 13 -14" stroke="%s" stroke-width="2"/>\n' % (cy, INK)
              for cy in (102, 180, 258))
)

# ------------------------------------------------------ Lifecycle and email
ART["email-lifecycle"] = (
    "A triggered email flow branching into three sends over time",
    frame(64, 142, 128, 80, 10)
    + '  <path d="M64 150 L128 194 L192 150" stroke="%s" stroke-width="1.6"/>\n' % INK
    + '  <g stroke="%s" stroke-width="1.25"><path d="M192 182 H268"/></g>\n' % MID
    + '  <circle cx="288" cy="182" r="20" fill="#FFFFFF" stroke="%s" stroke-width="1.6"/>\n' % INK
    + '  <path d="M288 172 v10 l8 6" stroke="%s" stroke-width="1.6"/>\n' % INK
    + '  <g stroke="%s" stroke-width="1.25">\n' % MID
    + '    <path d="M308 182 C352 182 352 74 396 74"/>\n'
    + '    <path d="M308 182 H396"/>\n'
    + '    <path d="M308 182 C352 182 352 290 396 290"/>\n'
    + '  </g>\n'
    + ''.join(
        frame(396, y, 152, 68, 10)
        + '  <path d="M396 %s L472 %s L548 %s" stroke="%s" stroke-width="1.3"/>\n'
          % (y + 8, y + 44, y + 8, MID)
        for y in (40, 148, 256))
    + '  <g stroke="%s" stroke-width="1.25">\n' % MID
    + '    <path d="M548 74 C592 74 592 164 628 164"/>\n'
    + '    <path d="M548 182 H628"/>\n'
    + '    <path d="M548 290 C592 290 592 200 628 200"/>\n'
    + '  </g>\n'
    + frame(628, 126, 112, 112, 12, SUNK)
    + '  <path d="M652 206 l20 -24 18 16 26 -40" stroke="%s" stroke-width="2"/>\n' % INK
    + '  <circle cx="716" cy="158" r="6" fill="#FFFFFF" stroke="%s" stroke-width="2"/>\n' % INK
    + rows(652, 226, [64], 12, MID, 4)
)

# -------------------------------------------------- Photography and video
ART["photography-video"] = (
    "A camera body on a tripod beside a lighting stand and a framed shot",
    frame(132, 128, 212, 136, 14)
    + '  <path d="M172 128 l18 -26 h72 l18 26" fill="#FFFFFF" stroke="%s" stroke-width="1.6"/>\n' % INK
    + '  <circle cx="238" cy="196" r="46" fill="%s" stroke="%s" stroke-width="1.6"/>\n' % (SUNK, INK)
    + '  <circle cx="238" cy="196" r="26" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/>\n' % MID
    + '  <circle cx="226" cy="184" r="6" fill="%s" stroke="none"/>\n' % MID
    + '  <circle cx="314" cy="150" r="6" fill="%s" stroke="none"/>\n' % INK
    + '  <path d="M196 264 l-28 60 M280 264 l28 60 M238 264 v60" stroke="%s" stroke-width="1.6"/>\n' % INK
    + '  <path d="M160 324 h156" stroke="%s" stroke-width="1.6"/>\n' % MID
    # light stand
    + '  <path d="M452 92 h96 l20 44 h-136 Z" fill="#FFFFFF" stroke="%s" stroke-width="1.6"/>\n' % INK
    + '  <g stroke="%s" stroke-width="1.2" opacity=".65">\n' % MID
    + '    <path d="M448 150 l-26 48 M500 152 v52 M552 150 l26 48"/>\n'
    + '  </g>\n'
    + '  <path d="M500 136 v148" stroke="%s" stroke-width="1.6"/>\n' % INK
    + '  <path d="M466 324 l34 -40 34 40" stroke="%s" stroke-width="1.6"/>\n' % INK
    # framed shot
    + frame(612, 112, 136, 136, 10, SUNK)
    + '  <path d="M632 212 l32 -40 24 24 20 -26 20 42" stroke="%s" stroke-width="1.6"/>\n' % INK
    + '  <circle cx="648" cy="150" r="10" stroke="%s" stroke-width="1.4"/>\n' % MID
    + rows(612, 274, [88, 60], 16)
)

# ------------------------------------------------- Fractional performance lead
ART["fractional-lead"] = (
    "A performance dashboard reviewed above a small team",
    frame(96, 44, 400, 196, 14)
    + '  <path d="M96 78 H496" stroke="%s" stroke-width="1.25"/>\n' % MID
    + rows(120, 61, [96], 12, INK, 5)
    + '  <g stroke="%s" stroke-width="1" opacity=".6">\n' % LINE
    + ''.join('    <line x1="128" y1="%s" x2="464" y2="%s"/>\n' % (y, y) for y in (112, 148, 184))
    + '  </g>\n'
    + '  <path d="M128 206 L196 184 L264 190 L332 142 L400 128 L464 100" stroke="%s" stroke-width="2"/>\n' % INK
    + '  <circle cx="464" cy="100" r="7" fill="#FFFFFF" stroke="%s" stroke-width="2"/>\n' % INK
    + '  <path d="M128 212 L196 210 L264 200 L332 202 L400 188 L464 178" stroke="%s" stroke-width="1.4" opacity=".8"/>\n' % MID
    + '  <line x1="128" y1="218" x2="464" y2="218" stroke="%s"/>\n' % MID
    # the team below
    + ''.join(
        '  <circle cx="%s" cy="292" r="19" fill="#FFFFFF" stroke="%s" stroke-width="1.5"/>\n' % (cx, INK)
        + '  <circle cx="%s" cy="286" r="6.5" stroke="%s" stroke-width="1.3"/>\n' % (cx, MID)
        + '  <path d="M%s 304 a11 11 0 0 1 22 0" stroke="%s" stroke-width="1.3"/>\n' % (cx - 11, MID)
        for cx in (168, 240, 312))
    + '  <g stroke="%s" stroke-width="1.25" opacity=".75"><path d="M187 292 H221 M259 292 H293"/></g>\n' % MID
    + '  <path d="M296 240 V268" stroke="%s" stroke-width="1.25" opacity=".6"/>\n' % MID
    # the fractional lead, set apart
    + frame(560, 92, 176, 148, 12, SUNK)
    + '  <circle cx="648" cy="140" r="24" fill="#FFFFFF" stroke="%s" stroke-width="1.6"/>\n' % INK
    + '  <circle cx="648" cy="132" r="8" stroke="%s" stroke-width="1.4"/>\n' % MID
    + '  <path d="M634 156 a14 14 0 0 1 28 0" stroke="%s" stroke-width="1.4"/>\n' % MID
    + rows(588, 192, [120, 84], 18)
    + '  <g stroke="%s" stroke-width="1.25" opacity=".75"><path d="M496 166 H560"/></g>\n' % MID
)

# ------------------------------------------------------------ Dubai
ART["dubai"] = (
    "The Dubai skyline above a funnel resolving into closed deals",
    '  <g stroke="%s" stroke-width="1" opacity=".55"><line x1="56" y1="296" x2="744" y2="296"/></g>\n' % LINE
    + frame(96, 196, 54, 100, 4)
    + frame(164, 148, 44, 148, 4, SUNK)
    + '  <path d="M236 296 V96 l26 -44 26 44 v200 Z" fill="#FFFFFF" stroke="%s" stroke-width="1.6"/>\n' % INK
    + '  <line x1="262" y1="52" x2="262" y2="28" stroke="%s" stroke-width="1.6"/>\n' % INK
    + '  <g stroke="%s" stroke-width="1" opacity=".7">\n' % MID
    + ''.join('    <line x1="240" y1="%s" x2="284" y2="%s"/>\n' % (y, y) for y in range(116, 290, 22))
    + '  </g>\n'
    + frame(312, 168, 48, 128, 4)
    + frame(376, 212, 58, 84, 4, SUNK)
    + '  <g stroke="%s" stroke-width="1" opacity=".5">\n' % MID
    + ''.join('    <line x1="%s" y1="214" x2="%s" y2="288"/>\n' % (x, x) for x in (326, 342))
    + ''.join('    <line x1="%s" y1="232" x2="%s" y2="288"/>\n' % (x, x) for x in (396, 414))
    + '  </g>\n'
    # funnel to closed deals
    + '  <g stroke="%s" stroke-width="1.3">\n' % INK
    + '    <path d="M506 68 H744 L698 128 H552 Z" fill="#FFFFFF"/>\n'
    + '    <path d="M552 146 H698 L666 202 H584 Z" fill="#FFFFFF"/>\n'
    + '    <path d="M584 220 H666 L648 268 H602 Z" fill="%s"/>\n' % SUNK
    + '  </g>\n'
    + rows(538, 98, [174], 12)
    + rows(590, 174, [70], 12)
    + '  <circle cx="625" cy="300" r="7" fill="%s" stroke="none"/>\n' % INK
    + '  <line x1="625" y1="268" x2="625" y2="292" stroke="%s" stroke-width="1.25"/>\n' % MID
)

# ------------------------------------------------------------ Sri Lanka
ART["sri-lanka"] = (
    "Two location markers linked by a flight path above a performance curve",
    '  <g stroke="%s" stroke-width="1" opacity=".55">\n' % LINE
    + ''.join('    <circle cx="400" cy="196" r="%s"/>\n' % r for r in (104, 150, 196))
    + '    <line x1="56" y1="196" x2="744" y2="196"/>\n'
    + '  </g>\n'
    + '  <path d="M212 108 C320 24 492 24 592 112" stroke="%s" stroke-width="1.6" stroke-dasharray="7 9"/>\n' % MID
    # marker one
    + '  <path d="M212 108 c-24 0 -42 20 -42 44 0 32 42 66 42 66 s42 -34 42 -66 c0 -24 -18 -44 -42 -44 Z" fill="#FFFFFF" stroke="%s" stroke-width="1.8"/>\n' % INK
    + '  <circle cx="212" cy="152" r="14" fill="%s" stroke="none"/>\n' % SUNK
    + '  <circle cx="212" cy="152" r="6" fill="%s" stroke="none"/>\n' % INK
    + rows(166, 244, [92, 64], 16)
    # marker two
    + '  <path d="M592 112 c-24 0 -42 20 -42 44 0 32 42 66 42 66 s42 -34 42 -66 c0 -24 -18 -44 -42 -44 Z" fill="#FFFFFF" stroke="%s" stroke-width="1.8"/>\n' % INK
    + '  <circle cx="592" cy="156" r="14" fill="%s" stroke="none"/>\n' % SUNK
    + '  <circle cx="592" cy="156" r="6" fill="%s" stroke="none"/>\n' % INK
    + rows(546, 248, [92, 64], 16)
    # shared performance curve underneath
    + frame(306, 230, 188, 92, 12)
    + '  <path d="M330 296 l32 -16 30 6 32 -30 44 -22" stroke="%s" stroke-width="2"/>\n' % INK
    + '  <circle cx="468" cy="234" r="6" fill="#FFFFFF" stroke="%s" stroke-width="2"/>\n' % INK
    + '  <line x1="326" y1="306" x2="474" y2="306" stroke="%s"/>\n' % MID
)

# ----------------------------------------------------------- Services hub
ART["services"] = (
    "The disciplines of one funnel: creative, media, measurement and lifecycle",
    ''.join(
        frame(x, 96, 150, 168, 12, SUNK if i % 2 else "#FFFFFF")
        for i, x in enumerate((64, 244, 424, 604)))
    + '  <path d="M104 160 l22 -24 18 18 20 -22" stroke="%s" stroke-width="1.8"/>\n' % INK
    + '  <circle cx="106" cy="134" r="8" stroke="%s" stroke-width="1.4"/>\n' % MID
    + rows(90, 206, [98, 72], 16)
    + '  <path d="M284 170 H352 M284 148 H336 M284 192 H324" stroke="%s" stroke-width="5" opacity=".6"/>\n' % MID
    + '  <circle cx="272" cy="148" r="4" fill="%s" stroke="none"/>\n' % INK
    + '  <circle cx="272" cy="170" r="4" fill="%s" stroke="none"/>\n' % INK
    + '  <circle cx="272" cy="192" r="4" fill="%s" stroke="none"/>\n' % INK
    + rows(270, 226, [98, 64], 16)
    + '  <g stroke="%s" stroke-width="1" opacity=".6">\n' % LINE
    + ''.join('    <line x1="448" y1="%s" x2="550" y2="%s"/>\n' % (y, y) for y in (140, 170, 200))
    + '  </g>\n'
    + '  <path d="M448 198 l26 -14 24 -28 26 -24" stroke="%s" stroke-width="2"/>\n' % INK
    + '  <circle cx="524" cy="132" r="6" fill="#FFFFFF" stroke="%s" stroke-width="2"/>\n' % INK
    + rows(448, 226, [92, 60], 16)
    + '  <path d="M628 138 h102 v58 h-102 Z" fill="#FFFFFF" stroke="%s" stroke-width="1.6"/>\n' % INK
    + '  <path d="M628 140 L679 174 L730 140" stroke="%s" stroke-width="1.4"/>\n' % MID
    + rows(628, 226, [92, 70], 16)
    + '  <g stroke="%s" stroke-width="1.25" opacity=".7">\n' % MID
    + '    <path d="M214 180 H244 M394 180 H424 M574 180 H604"/>\n'
    + '  </g>\n'
)


# ------------------------------------------- Fractional performance lead
ART["performance-lead"] = (
    "Four paid channels converging into one forecast curve",
    "".join(
        frame(64, y, 150, 68, 10)
        + '  <circle cx="%s" cy="%s" r="13" fill="%s" stroke="none"/>\n' % (98, y + 34, SUNK)
        + '  <circle cx="98" cy="%s" r="5" fill="%s" stroke="none"/>\n' % (y + 34, MID)
        + rows(126, y + 26, [66, 44], 15)
        for y in (34, 118, 202, 286))
    + '  <g stroke="%s" stroke-width="1.3">\n' % MID
    + '    <path d="M214 68 C286 68 286 174 330 174"/>\n'
    + '    <path d="M214 152 C286 152 286 178 330 178"/>\n'
    + '    <path d="M214 236 C286 236 286 182 330 182"/>\n'
    + '    <path d="M214 320 C286 320 286 186 330 186"/>\n'
    + '  </g>\n'
    + '  <circle cx="352" cy="180" r="22" fill="#FFFFFF" stroke="%s" stroke-width="1.8"/>\n' % INK
    + '  <path d="M342 180 h20 M352 170 v20" stroke="%s" stroke-width="1.6"/>\n' % INK
    + '  <g stroke="%s" stroke-width="1.3"><path d="M374 180 H430"/><path d="M420 172 l10 8 -10 8"/></g>\n' % INK
    + frame(430, 74, 306, 212, 12)
    + '  <path d="M430 108 H736" stroke="%s" stroke-width="1.2"/>\n' % MID
    + rows(452, 92, [86], 12, INK, 5)
    + '  <g stroke="%s" stroke-width="1" opacity=".6">\n' % LINE
    + "".join('    <line x1="456" y1="%s" x2="712" y2="%s"/>\n' % (y, y) for y in (146, 188, 230))
    + '  </g>\n'
    # the forecast, then what actually happened against it
    + '  <path d="M456 250 L520 232 L584 196 L648 166 L712 126" stroke="%s" stroke-width="1.4" stroke-dasharray="6 7"/>\n' % MID
    + '  <path d="M456 254 L520 240 L584 202 L648 158 L712 112" stroke="%s" stroke-width="2.2"/>\n' % INK
    + '  <circle cx="712" cy="112" r="7" fill="#FFFFFF" stroke="%s" stroke-width="2"/>\n' % INK
    + '  <line x1="456" y1="262" x2="712" y2="262" stroke="%s"/>\n' % MID
)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, (label, body) in ART.items():
        svg = HEAD % (INK, label, SUNK) + body + FOOT
        with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
            f.write(svg)
        print("wrote assets/img/services/%s.svg  (%d bytes)" % (name, len(svg)))
