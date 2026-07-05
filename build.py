#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
간다GO static site generator.

Single source of truth for every page so that the footer (orange Telegram
inquiry buttons), the animated floating call button, the meta description
(<= 80 chars) and the JSON-LD schema graph are guaranteed identical across
the whole site. Region/program content lives in the PAGES list below.

Run:  python3 build.py
"""
import html
import json
import os
import re

# ---------------------------------------------------------------------------
# Site configuration lives in config.py — edit there in ONE place.
# ---------------------------------------------------------------------------
from config import (  # noqa: E402
    SITE_NAME, SITE_URL, TEL_DISPLAY, TEL_LINK,
    TELEGRAM_BUILD, TELEGRAM_PARTNER, OG_IMAGE,
)

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Icons (inline SVG)
# ---------------------------------------------------------------------------
PHONE_SVG = (
    '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" '
    'aria-hidden="true"><path d="M6.6 10.8a15.9 15.9 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 '
    '1-.24 11.4 11.4 0 0 0 3.6.58 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 '
    '0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.46.58 3.6a1 1 0 0 1-.24 1L6.6 10.8Z" '
    'fill="currentColor"/></svg>'
)
TELEGRAM_SVG = (
    '<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" '
    'aria-hidden="true"><path d="M21.9 4.3 18.6 20c-.25 1.1-.9 1.37-1.83.85l-5.05-3.72'
    '-2.44 2.35c-.27.27-.5.5-1 .5l.36-5.13L18.9 6.2c.4-.36-.09-.56-.63-.2L5.6 13.9l-4.9-1.5'
    'c-1.06-.34-1.08-1.06.22-1.57L20.5 2.9c.9-.33 1.68.2 1.4 1.4Z"/></svg>'
)


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------------------
# Shared chrome
# ---------------------------------------------------------------------------
NAV_LINKS = [
    ("부산권", "/busan/"),
    ("창원권", "/changwon/"),
    ("마산권", "/masan/"),
    ("김해권", "/gimhae/"),
    ("경남권", "/gyeongnam/"),
    ("경북권", "/gyeongbuk/"),
    ("제주권", "/jeju/"),
    ("프로그램", "/program/"),
    ("예약 전 확인", "/check/"),
]

FOOTER_REGIONS = [
    ("부산 출장마사지", "/busan/"),
    ("창원 출장마사지", "/changwon/"),
    ("마산 출장마사지", "/masan/"),
    ("김해 출장마사지", "/gimhae/"),
    ("경남 출장마사지", "/gyeongnam/"),
    ("경북 출장마사지", "/gyeongbuk/"),
    ("제주 출장마사지", "/jeju/"),
]
FOOTER_INFO = [
    ("마사지 프로그램", "/program/"),
    ("이용 장소 안내", "/use/"),
    ("예약 전 확인", "/check/"),
    ("운영 기준·작성자", "/about/"),
    ("개인정보처리방침", "/policy/privacy/"),
    ("서비스 이용 원칙", "/policy/service/"),
]


def header_html(rel):
    links = "".join(
        f'<a href="{url}">{esc(label)}</a>' for label, url in NAV_LINKS
    )
    return f"""
<header class="site-header">
  <div class="container nav">
    <a class="brand-lockup" href="/"><span class="brand-mark">GO</span>{SITE_NAME}</a>
    <nav class="nav-links" aria-label="주요 메뉴">{links}</nav>
    <div class="nav-cta">
      <a class="nav-tel" href="{TEL_LINK}">☎ {TEL_DISPLAY}</a>
      <a class="btn btn--primary btn--sm" href="{TEL_LINK}">전화 예약</a>
    </div>
    <button class="nav-toggle" aria-label="메뉴 열기" aria-expanded="false">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
    </button>
  </div>
</header>"""


def footer_html():
    region_links = "".join(f'<a href="{u}">{esc(t)}</a>' for t, u in FOOTER_REGIONS)
    info_links = "".join(f'<a href="{u}">{esc(t)}</a>' for t, u in FOOTER_INFO)
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <h4>{SITE_NAME} 출장마사지 지역 안내</h4>
        <p class="footer-biz">
          부산·경남·경북·제주 주요 생활권과 호텔·오피스텔·리조트·자택 이용 전
          확인사항을 안내하는 지역 정보 사이트입니다.
        </p>
        <p class="footer-biz">
          <strong>상호</strong> {SITE_NAME}<br>
          <strong>전화 예약</strong> <a href="{TEL_LINK}">{TEL_DISPLAY}</a>
        </p>
        <div class="footer-cta">
          <a class="tg-btn" href="{TELEGRAM_BUILD}" target="_blank" rel="noopener nofollow">{TELEGRAM_SVG} 웹사이트 제작문의</a>
          <a class="tg-btn" href="{TELEGRAM_PARTNER}" target="_blank" rel="noopener nofollow">{TELEGRAM_SVG} 제휴문의</a>
        </div>
      </div>
      <div class="footer-col">
        <h4>지역별 안내</h4>
        {region_links}
      </div>
      <div class="footer-col">
        <h4>이용 안내</h4>
        {info_links}
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 {SITE_NAME}. 방문형 웰니스 지역 안내.</span>
      <span>불법·선정적 서비스를 제공하거나 암시하지 않습니다.</span>
    </div>
  </div>
</footer>"""


def float_call_html():
    return f"""
<a class="float-call" href="{TEL_LINK}" aria-label="전화 예약 {TEL_DISPLAY}">
  <span class="float-label">전화 예약 {TEL_DISPLAY}</span>{PHONE_SVG}
</a>"""


# ---------------------------------------------------------------------------
# Schema (JSON-LD @graph)
# ---------------------------------------------------------------------------
def organization_node():
    return {
        "@type": "Organization",
        "@id": SITE_URL + "/#organization",
        "name": SITE_NAME,
        "url": SITE_URL + "/",
        "telephone": TEL_DISPLAY,
        "description": "부산·경남·경북·제주 방문형 웰니스 서비스의 지역·이용 기준 안내",
        "logo": {
            "@type": "ImageObject",
            "url": OG_IMAGE,
        },
        "sameAs": [TELEGRAM_BUILD],
    }


def build_schema(page):
    url = SITE_URL + page["path"]
    graph = [organization_node()]

    webpage = {
        "@type": "WebPage",
        "@id": url + "#webpage",
        "url": url,
        "name": page["title"],
        "description": page["desc"],
        "isPartOf": {"@id": SITE_URL + "/#website"},
        "inLanguage": "ko-KR",
        "primaryImageOfPage": {
            "@type": "ImageObject",
            "url": OG_IMAGE,
        },
    }
    graph.append(webpage)

    graph.append({
        "@type": "WebSite",
        "@id": SITE_URL + "/#website",
        "url": SITE_URL + "/",
        "name": SITE_NAME,
        "inLanguage": "ko-KR",
        "publisher": {"@id": SITE_URL + "/#organization"},
    })

    # Breadcrumb
    crumbs = page.get("crumbs")
    if crumbs:
        items = []
        for i, (name, path) in enumerate(crumbs, start=1):
            items.append({
                "@type": "ListItem",
                "position": i,
                "name": name,
                "item": SITE_URL + path,
            })
        graph.append({
            "@type": "BreadcrumbList",
            "@id": url + "#breadcrumb",
            "itemListElement": items,
        })

    # FAQ
    if page.get("faqs"):
        graph.append({
            "@type": "FAQPage",
            "@id": url + "#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a},
                }
                for q, a in page["faqs"]
            ],
        })

    # Service (used cautiously on program pages only)
    if page.get("service"):
        graph.append({
            "@type": "Service",
            "name": page["service"],
            "serviceType": page["service"],
            "areaServed": "부산·경남·경북·제주",
            "provider": {"@id": SITE_URL + "/#organization"},
        })

    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Reusable content blocks
# ---------------------------------------------------------------------------
def breadcrumb_html(crumbs):
    if not crumbs:
        return ""
    parts = []
    for i, (name, path) in enumerate(crumbs):
        if i < len(crumbs) - 1:
            parts.append(f'<a href="{path}">{esc(name)}</a><span>›</span>')
        else:
            parts.append(f"<span>{esc(name)}</span>")
    return f'<nav class="breadcrumb container" aria-label="breadcrumb">{"".join(parts)}</nav>'


# ---------------------------------------------------------------------------
# Page renderer
# ---------------------------------------------------------------------------
PAGE_TMPL = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{site}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ogimage}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ogimage}">
<meta name="theme-color" content="#0b0f16">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/css/style.css">
<script type="application/ld+json">
{schema}
</script>
</head>
<body>
{header}
{breadcrumb}
<main>
{body}
</main>
{footer}
{floatcall}
<script src="/assets/js/main.js" defer></script>
</body>
</html>"""


def render(page):
    canonical = SITE_URL + page["path"]
    robots = '<meta name="robots" content="noindex, follow">' if page.get("noindex") else ""
    desc = page["desc"]
    assert len(desc) <= 80, f"description too long ({len(desc)}): {page['path']}"
    return PAGE_TMPL.format(
        title=esc(page["title"]),
        desc=esc(desc),
        canonical=esc(canonical),
        robots=robots,
        site=esc(SITE_NAME),
        ogimage=esc(OG_IMAGE),
        schema=build_schema(page),
        header=header_html(page["path"]),
        breadcrumb=breadcrumb_html(page.get("crumbs")),
        body=page["body"],
        footer=footer_html(),
        floatcall=float_call_html(),
    )


def write_page(page):
    path = page["path"]
    if path == "/":
        fp = os.path.join(OUT, "index.html")
    else:
        fp = os.path.join(OUT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(render(page))
    return path


# ===========================================================================
# CONTENT — imported from content.py to keep this file focused on machinery.
# ===========================================================================
from content import PAGES  # noqa: E402


def write_sitemap(pages):
    urls = []
    for p in pages:
        if p.get("noindex"):
            continue
        urls.append(
            f"  <url><loc>{SITE_URL}{p['path']}</loc>"
            f"<changefreq>weekly</changefreq><priority>{p.get('priority','0.6')}</priority></url>"
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls) + "\n</urlset>\n"
    )
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)


def write_robots():
    txt = (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {SITE_URL}/sitemap.xml\n"
    )
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(txt)


def main():
    written = [write_page(p) for p in PAGES]
    write_sitemap(PAGES)
    write_robots()
    print(f"Generated {len(written)} pages + sitemap.xml + robots.txt")
    for p in written:
        print("  ", p)


if __name__ == "__main__":
    main()
