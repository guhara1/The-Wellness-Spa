# -*- coding: utf-8 -*-
"""Reusable HTML content blocks for composing page bodies (used by content.py)."""
import html


def esc(s):
    return html.escape(s, quote=True)


def hero(h1, lead, ctas=None, eyebrow=None):
    eye = f'<span class="eyebrow">{esc(eyebrow)}</span>' if eyebrow else ""
    cta = ""
    if ctas:
        btns = "".join(
            f'<a class="btn {cls}" href="{url}">{esc(label)}</a>'
            for label, url, cls in ctas
        )
        cta = f'<div class="hero-cta">{btns}</div>'
    return f"""
<section class="hero section--tight">
  <div class="container center">
    {eye}
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    {cta}
  </div>
</section>"""


def section(title, inner, eyebrow=None, tight=False, center_head=True):
    cls = "section--tight" if tight else "section"
    eye = f'<span class="eyebrow">{esc(eyebrow)}</span>' if eyebrow else ""
    head = ""
    if title:
        align = "center" if center_head else ""
        head = f'<div class="{align}" style="margin-bottom:32px">{eye}<h2>{title}</h2></div>'
    return f'<section class="{cls}"><div class="container">{head}{inner}</div></section>'


def cards(items, cols=3):
    out = [f'<div class="grid grid--{cols}">']
    for c in items:
        link = (f'<a class="card-link" href="{c["url"]}">{esc(c.get("cta", "자세히 보기"))}</a>'
                if c.get("url") else "")
        tag = f'<span class="tag">{esc(c["tag"])}</span> ' if c.get("tag") else ""
        out.append(
            f'<article class="card">{tag}<h3>{esc(c["title"])}</h3>'
            f'<p>{esc(c["body"])}</p>{link}</article>'
        )
    out.append("</div>")
    return "".join(out)


def chips(items):
    return '<div class="chips">' + "".join(
        f'<a class="chip" href="{u}">{esc(t)}</a>' for t, u in items
    ) + "</div>"


def faq_block(faqs):
    items = "".join(
        f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>"
        for q, a in faqs
    )
    return f'<div class="faq">{items}</div>'


def prose(inner):
    return f'<div class="prose">{inner}</div>'


WHO_HOW_WHY = """
<div class="trust-block">
  <div><h4>Who · 누가</h4><p>부산·경남·경북·제주 지역의 행정구역·생활권·교통 거점 자료를 바탕으로, 방문형 웰니스 이용 전 확인사항을 정리하는 지역 안내 편집팀이 관리합니다.</p></div>
  <div><h4>How · 어떻게</h4><p>공식 행정구역 자료와 실제 예약 전 확인 항목을 기준으로 작성하며, AI 보조 도구를 쓰더라도 최종 문구는 사람이 검수해 과장·중복·허위 표현을 제거합니다.</p></div>
  <div><h4>Why · 왜</h4><p>검색 순위 조작이 아니라 자택·호텔·오피스텔·리조트 이용 전 필요한 확인사항을 쉽게 안내하기 위한 페이지입니다. 불법·선정적 내용은 제공·암시하지 않습니다.</p></div>
</div>"""

SERVICE_NOTE = """
<div class="callout callout--warn">
  본 사이트는 지역·이용 기준 <strong>안내 매체</strong>이며 불법·선정적 서비스를
  제공하거나 알선·암시하지 않습니다. 방문 가능 여부는 실제 주소와 예약 조건 확인 후
  안내되며, 허위 후기·별점은 게시하지 않습니다.
</div>"""
