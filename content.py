# -*- coding: utf-8 -*-
"""
Page content for 간다GO. Each entry is genuinely differentiated per region /
program (no "swap the place name" bodies). Meta descriptions are kept <= 80
characters (enforced by an assert in build.render).
"""
from config import TEL_LINK, TEL_DISPLAY
from blocks import (
    hero, section, cards, chips, faq_block, prose, WHO_HOW_WHY, SERVICE_NOTE,
)

CTA = [("전화 예약", TEL_LINK, "btn--primary"), ("예약 전 확인", "/check/", "btn--ghost")]


def region_faqs(extra):
    base = [
        ("전화 예약은 어떻게 하나요?",
         f"{TEL_DISPLAY} 로 전화하시면 지역·숙소 유형·예약 시간대를 확인한 뒤 방문 가능 여부를 안내드립니다."),
    ]
    return base + extra


# ---------------------------------------------------------------------------
# 1. MAIN HUB
# ---------------------------------------------------------------------------
PRICING = """
<div class="pricing">
  <div class="price-card">
    <h3>60분 코스</h3>
    <div class="price-amount">90,000<small>원</small></div>
    <div class="price-min">60분</div>
    <p class="price-desc">기본 컨디션·릴렉스 케어</p>
    <a class="btn btn--ghost btn--block" href="%TEL%">예약 문의</a>
  </div>
  <div class="price-card price-card--featured">
    <span class="price-badge">추천</span>
    <h3>90분 코스</h3>
    <div class="price-amount">150,000<small>원</small></div>
    <div class="price-min">90분</div>
    <p class="price-desc">아로마 포함 추천 구성</p>
    <a class="btn btn--primary btn--block" href="%TEL%">예약 문의</a>
  </div>
  <div class="price-card">
    <h3>120분 코스</h3>
    <div class="price-amount">180,000<small>원</small></div>
    <div class="price-min">120분</div>
    <p class="price-desc">전신 집중 프리미엄 케어</p>
    <a class="btn btn--ghost btn--block" href="%TEL%">예약 문의</a>
  </div>
</div>
<p class="center muted" style="margin-top:24px">지역·예약 시간대·이동 거리에 따라 상담 시 최종 확인됩니다.
<a class="brand-text" href="/check/travel/">상세 요금 안내 보기 →</a></p>
""".replace("%TEL%", TEL_LINK)

REGION_CARDS = [
    {"title": "부산권", "body": "해운대·서면·광안리·명지·기장 등 해안 상권과 도심 생활권 중심.", "url": "/busan/", "cta": "부산권 보기"},
    {"title": "창원권", "body": "상남·중앙·성산 업무지구와 창원국가산단·진해 해안 생활권.", "url": "/changwon/", "cta": "창원권 보기"},
    {"title": "마산권", "body": "마산합포·마산회원·마산역·오동동 구도심 생활권 별도 안내.", "url": "/masan/", "cta": "마산권 보기"},
    {"title": "김해권", "body": "장유·율하 신도시와 내외동 도심, 김해공항 인접 생활권.", "url": "/gimhae/", "cta": "김해권 보기"},
    {"title": "경남권", "body": "양산·진주·거제·통영·사천·밀양 등 주요 시·군 생활권.", "url": "/gyeongnam/", "cta": "경남권 보기"},
    {"title": "경북권", "body": "포항·경주·구미·김천·안동·경산 등 산업·관광 생활권.", "url": "/gyeongbuk/", "cta": "경북권 보기"},
    {"title": "제주권", "body": "제주시·서귀포와 공항·연동·노형·중문·애월·성산 생활권.", "url": "/jeju/", "cta": "제주권 보기"},
]

LIFE_CHIPS = [
    ("해운대·센텀", "/life/busan-haeundae-centum/"),
    ("서면·전포", "/busan/"),
    ("창원 상남·중앙", "/life/changwon-sangnam-jungang/"),
    ("마산합포·회원", "/masan/"),
    ("김해 장유·율하", "/life/gimhae-jangyu-yulha/"),
    ("양산 물금", "/gyeongnam/"),
    ("진주혁신도시", "/gyeongnam/"),
    ("거제·통영", "/gyeongnam/"),
    ("포항·경주", "/gyeongbuk/"),
    ("구미·김천", "/gyeongbuk/"),
    ("제주 연동·노형", "/jeju/"),
    ("서귀포·중문", "/life/jeju-city-seogwipo/"),
]

PROGRAM_CARDS = [
    {"title": "스웨디시", "body": "부드러운 오일 압으로 릴렉스 중심. 호텔·오피스텔 이용 전 확인.", "url": "/program/swedish/"},
    {"title": "타이마사지", "body": "스트레칭 위주. 공간 확보와 복장 확인이 필요한 프로그램.", "url": "/program/thai-massage/"},
    {"title": "아로마테라피", "body": "향·피부 민감도와 숙소 오일 정책을 함께 확인합니다.", "url": "/program/aroma-therapy/"},
    {"title": "스포츠 마사지", "body": "운동 후 압 조절 중심. 치료·회복 보장 표현은 쓰지 않습니다.", "url": "/program/sports-massage/"},
    {"title": "발마사지", "body": "장시간 보행·관광객에게 맞춘 발·종아리 집중 관리.", "url": "/program/foot-massage/"},
    {"title": "딥티슈", "body": "심부 근육을 강한 압으로 집중 관리. 통증 부위 사전 고지.", "url": "/program/deep-tissue/"},
    {"title": "로미로미", "body": "팔·전완을 활용한 리듬감 있는 하와이안 오일 케어.", "url": "/program/lomi-lomi/"},
    {"title": "커플 관리", "body": "두 분이 함께 받는 2인 동시 진행. 공간·인원 확인.", "url": "/program/couple/"},
    {"title": "야간 예약", "body": "야간 건물 출입·이동 확인 후 안내. 24시간 무제한 아님.", "url": "/program/night/"},
]

USE_CARDS = [
    {"title": "자택·아파트", "body": "공동현관·주차·엘리베이터 등 출입 동선을 예약 전 확인합니다.", "url": "/use/"},
    {"title": "호텔·숙소", "body": "호텔별 외부인 방문 정책과 프런트 안내 기준을 확인합니다.", "url": "/use/"},
    {"title": "오피스텔", "body": "공동현관 비밀번호·방문 등록 등 건물 규정을 확인합니다.", "url": "/use/"},
    {"title": "리조트·펜션", "body": "관광 숙소 정책과 야간 이동 거리를 함께 확인합니다.", "url": "/use/"},
]

home_body = (
    hero(
        "부산·경남·경북·제주 출장마사지<br>주요 생활권별 방문 가능 지역 안내",
        "부산 해운대, 창원 상남, 마산합포·마산회원, 김해 장유, 포항·경주·구미, 제주·서귀포 등 "
        "주요 생활권과 호텔·오피스텔·리조트·자택 이용 전 확인사항을 안내합니다.",
        ctas=[("전화 예약 " + TEL_DISPLAY, TEL_LINK, "btn--primary"),
              ("권역 보기", "#regions", "btn--ghost")],
        eyebrow="부산·경남·경북·제주 방문형 웰니스 안내",
    )
    + section("이용 코스와 요금 살펴보기", PRICING,
              eyebrow="COURSE & PRICE",
              tight=True)
    + section("부산·경남·경북·제주는 생활권별 이용 기준이 다릅니다",
              prose(
                  "<p>같은 ‘출장마사지’ 검색이라도 지역마다 실제 확인해야 할 항목이 다릅니다. "
                  "부산은 해안 숙소와 도심 상권, 창원은 산업도시와 업무지구, 마산은 구도심·마산역 생활권, "
                  "김해는 부산 인접 신도시, 경북은 산업·관광·동해안 생활권, 제주는 공항·리조트·펜션 "
                  "이동 기준이 중요합니다.</p>"
                  "<p>본 사이트는 지역명만 바꾼 페이지가 아니라, 각 생활권의 <strong>숙소 유형·건물 출입·"
                  "이동 거리·예약 전 확인 항목</strong>을 실제 기준으로 나눠 안내합니다.</p>")
              + SERVICE_NOTE)
    + '<a id="regions"></a>' + section("권역별 안내", cards(REGION_CARDS, cols=3), eyebrow="REGIONS")
    + section("주요 생활권 바로가기", chips(LIFE_CHIPS), eyebrow="LIFE AREAS")
    + section("마사지 프로그램 안내", cards(PROGRAM_CARDS, cols=3), eyebrow="PROGRAMS")
    + section("이용 장소별 확인 기준", cards(USE_CARDS, cols=4), eyebrow="PLACES")
    + section("자주 묻는 질문", faq_block([
        ("어느 지역까지 방문할 수 있나요?",
         "부산·경남·경북·제주 주요 생활권을 안내하며, 외곽·도서 지역은 이동 거리에 따라 상담 시 확인됩니다."),
        ("요금은 어떻게 정해지나요?",
         "60·90·120분 코스별 기준 요금이 있으며, 지역·예약 시간대·이동 거리에 따라 상담 시 최종 확인됩니다."),
        ("예약 전 무엇을 확인해야 하나요?",
         "숙소 유형, 건물 공동현관·주차, 예약 시간대, 이동 거리를 확인합니다. 예약 전 확인 페이지에서 항목을 정리했습니다."),
    ]), eyebrow="FAQ")
)

MAIN = {
    "path": "/",
    "title": "부산·경남·경북·제주 출장마사지｜창원·마산·김해·포항·제주 홈타이 안내 | 간다GO",
    "desc": "부산·경남·경북·제주 출장마사지·홈타이 주요 생활권과 호텔·오피스텔·리조트 이용 전 확인사항 안내.",
    "crumbs": None,
    "priority": "1.0",
    "faqs": [
        ("어느 지역까지 방문할 수 있나요?",
         "부산·경남·경북·제주 주요 생활권을 안내하며, 외곽·도서 지역은 이동 거리에 따라 상담 시 확인됩니다."),
        ("요금은 어떻게 정해지나요?",
         "60·90·120분 코스별 기준 요금이 있으며, 지역·예약 시간대·이동 거리에 따라 상담 시 최종 확인됩니다."),
        ("예약 전 무엇을 확인해야 하나요?",
         "숙소 유형, 건물 공동현관·주차, 예약 시간대, 이동 거리를 확인합니다."),
    ],
    "body": home_body,
}


# ---------------------------------------------------------------------------
# Region hub factory
# ---------------------------------------------------------------------------
def region_page(path, name, title, desc, h1, lead, intro_html,
                area_cards, life_chips, program_chips, faqs, priority="0.8"):
    body = (
        hero(h1, lead, ctas=CTA, eyebrow=f"{name} 생활권 안내")
        + section(f"{name} 생활권 특징", prose(intro_html) + SERVICE_NOTE)
        + section("주요 도시·구·군 안내", cards(area_cards, cols=3), eyebrow="AREAS")
        + section("핵심 생활권 바로가기", chips(life_chips), eyebrow="LIFE AREAS")
        + section("추천 프로그램", chips(program_chips), eyebrow="PROGRAMS")
        + section("자주 묻는 질문", faq_block(faqs), eyebrow="FAQ")
        + section("작성·검수 기준", WHO_HOW_WHY, eyebrow="WHO · HOW · WHY", tight=True)
    )
    return {
        "path": path, "title": title, "desc": desc,
        "crumbs": [("홈", "/"), (f"{name} 출장마사지", path)],
        "priority": priority, "faqs": faqs, "body": body,
    }


BUSAN = region_page(
    "/busan/", "부산",
    "부산 출장마사지｜해운대·서면·광안리 생활권 안내 | 간다GO",
    "부산 출장마사지 해운대·서면·광안리·명지·기장 생활권과 호텔·오피스텔 이용 기준 안내.",
    "부산 출장마사지 · 해운대·서면·광안리 생활권 안내",
    "부산은 해안 관광 숙소와 도심 상권, 환승역 접근성이 지역마다 크게 다릅니다. 생활권별 이용 기준을 정리했습니다.",
    "<p>부산은 <strong>해운대·센텀</strong>의 호텔·오피스텔, <strong>서면·전포</strong>의 도심 상권, "
    "<strong>광안리·수영</strong>의 해안 숙박권, <strong>명지·강서</strong>의 신도시·공항 인접권, "
    "<strong>기장·정관</strong>의 외곽 생활권으로 이용 기준이 나뉩니다.</p>"
    "<p>해안 관광 숙소는 성수기 프런트 방문 정책을, 도심 오피스텔은 공동현관 규정을, "
    "명지·강서는 이동 거리를 예약 전에 확인하는 것이 좋습니다.</p>",
    [
        {"title": "해운대·센텀", "body": "마린시티·벡스코 인접 호텔·오피스텔 밀집. 관광 숙소 방문 정책 확인.", "url": "/life/busan-haeundae-centum/"},
        {"title": "서면·전포", "body": "부산 최대 도심 상권. 환승역과 오피스텔 공동현관 규정 확인.", "url": "/life/busan-seomyeon-jeonpo/"},
        {"title": "광안리·수영", "body": "해안 숙박권과 민락·남천 주거권. 야간 이동 거리 확인.", "url": "/life/busan-gwangalli-suyeong/"},
        {"title": "명지·강서·공항", "body": "신도시·김해공항 인접권. 장기 출장 숙소와 이동 거리 확인.", "url": "/life/busan-west-airport-myeongji/"},
        {"title": "부산역·남포", "body": "KTX 부산역·남포 원도심 관광 숙소. 성수기 방문 정책 확인.", "url": "/life/busan-station-nampo/"},
        {"title": "동래·온천장", "body": "온천 숙박과 동래·연산 행정·주거권. 단지 출입 동선 확인.", "url": "/life/busan-dongnae-oncheon/"},
        {"title": "사상·하단", "body": "서부시외버스터미널·낙동강 서부 주거권. 이동·주차 확인.", "url": "/life/busan-sasang-hadan/"},
        {"title": "기장·정관", "body": "정관신도시·오시리아 리조트. 이동 거리와 방문 정책 확인.", "url": "/life/busan-gijang-jeonggwan/"},
    ],
    [("해운대·센텀", "/life/busan-haeundae-centum/"), ("서면·전포", "/life/busan-seomyeon-jeonpo/"),
     ("광안리·수영", "/life/busan-gwangalli-suyeong/"), ("부산역·남포", "/life/busan-station-nampo/"),
     ("동래·온천장", "/life/busan-dongnae-oncheon/"), ("사상·하단", "/life/busan-sasang-hadan/"),
     ("기장·정관", "/life/busan-gijang-jeonggwan/"), ("명지·강서·공항", "/life/busan-west-airport-myeongji/"),
     ("남구·대연·문현", "/life/busan-namgu-daeyeon/"), ("금정·부산대", "/life/busan-geumjeong-pnu/"),
     ("북구·화명·덕천", "/life/busan-bukgu-hwamyeong/")],
    [("스웨디시", "/program/swedish/"), ("아로마테라피", "/program/aroma-therapy/"),
     ("발마사지", "/program/foot-massage/")],
    region_faqs([
        ("해운대 호텔에서도 이용할 수 있나요?",
         "호텔마다 외부인 방문 정책이 달라 예약 전 프런트 방문 가능 여부를 확인한 뒤 안내드립니다."),
        ("공항 근처 명지·강서도 되나요?",
         "명지·강서·녹산은 이동 거리에 따라 상담 시 방문 가능 여부와 예약 시간대를 확인합니다."),
    ]),
    priority="0.9",
)

CHANGWON = region_page(
    "/changwon/", "창원",
    "창원 출장마사지｜상남·중앙·성산·진해 생활권 안내 | 간다GO",
    "창원 출장마사지 상남·중앙·성산·진해와 창원국가산단 인접 숙소 이용 기준 안내.",
    "창원 출장마사지 · 상남·중앙·성산·진해 생활권 안내",
    "창원은 경남 핵심 산업도시로 업무지구·국가산단·해안 생활권의 이용 기준이 서로 다릅니다.",
    "<p>창원은 <strong>상남·중앙</strong>의 도심·오피스텔, <strong>의창·성산</strong>의 행정·업무지구, "
    "<strong>창원국가산단</strong> 인접 장기 출장 숙소, <strong>진해 석동·용원</strong>의 해안 생활권으로 "
    "나뉩니다.</p>"
    "<p>산단 인접 숙소는 야간 이동과 주차 동선을, 상남·중앙 오피스텔은 공동현관 규정을 예약 전에 "
    "확인하는 것이 좋습니다.</p>",
    [
        {"title": "상남·중앙", "body": "창원 핵심 도심·상권. 오피스텔 공동현관·주차 확인.", "url": "/life/changwon-sangnam-jungang/"},
        {"title": "의창·성산", "body": "행정·업무지구와 팔용 생활권. 아파트 단지 출입 확인.", "url": "/changwon/"},
        {"title": "의창·성산", "body": "도청·시청 행정·업무지구와 초고층 아파트(유니시티). 출입 확인.", "url": "/life/changwon-uichang-seongsan/"},
        {"title": "창원국가산단·진해", "body": "산단 인접 장기 출장 숙소·진해 해안. 야간 이동·주차 확인.", "url": "/life/changwon-industrial-jinhae/"},
    ],
    [("상남·중앙", "/life/changwon-sangnam-jungang/"), ("의창·성산", "/life/changwon-uichang-seongsan/"),
     ("창원국가산단·진해", "/life/changwon-industrial-jinhae/"), ("창원중앙역", "/changwon/")],
    [("스포츠 마사지", "/program/sports-massage/"), ("스웨디시", "/program/swedish/"),
     ("아로마테라피", "/program/aroma-therapy/")],
    region_faqs([
        ("창원국가산단 근처 숙소도 되나요?",
         "산단 인접 오피스텔·출장 숙소는 이동 거리와 야간 예약 시간대를 확인한 뒤 방문 가능 여부를 안내합니다."),
        ("진해까지도 방문하나요?",
         "진해 석동·용원 등 해안 생활권은 이동 거리에 따라 상담 시 확인됩니다."),
    ]),
)

MASAN = region_page(
    "/masan/", "마산",
    "마산 출장마사지｜마산합포·마산회원 생활권 안내 | 간다GO",
    "마산 출장마사지 마산합포·마산회원·마산역·오동동 구도심 생활권 이용 기준 안내.",
    "마산 출장마사지 · 마산합포·마산회원 생활권 안내",
    "마산은 행정상 창원시에 속하지만 마산역·합포·회원 구도심 생활권 수요가 뚜렷해 별도로 안내합니다.",
    "<p>마산은 <strong>마산합포구</strong>(오동동·창동·월영)와 <strong>마산회원구</strong>(석전·양덕·합성), "
    "그리고 <strong>마산역·내서</strong> 생활권으로 나뉩니다. 통합 창원시 안의 구도심이지만 검색 수요와 "
    "실제 생활권이 뚜렷합니다.</p>"
    "<p>구도심 특성상 노후 오피스텔·주택의 공동현관과 주차 동선, 마산역 인접 숙소의 이동 거리를 예약 전에 "
    "확인하는 것이 좋습니다.</p>",
    [
        {"title": "마산합포·마산회원", "body": "오동동·창동 구도심과 석전·양덕 주거권. 노후 건물 출입 확인.", "url": "/life/masan-happo-hoewon/"},
        {"title": "마산역·석전", "body": "마산역 인접 숙소·이동 거점. 예약 시간대·이동 거리 확인.", "url": "/masan/"},
        {"title": "내서읍", "body": "마산 외곽 주거 생활권. 이동 거리 확인 후 안내.", "url": "/masan/"},
    ],
    [("마산합포·마산회원", "/life/masan-happo-hoewon/"),
     ("마산역·석전", "/masan/"), ("오동동·창동", "/masan/")],
    [("발마사지", "/program/foot-massage/"), ("아로마테라피", "/program/aroma-therapy/"),
     ("스웨디시", "/program/swedish/")],
    region_faqs([
        ("마산도 창원과 따로 예약하나요?",
         "행정상 창원시지만 마산합포·마산회원·마산역 생활권은 이동 동선이 달라 지역을 확인한 뒤 안내드립니다."),
    ]),
)

GIMHAE = region_page(
    "/gimhae/", "김해",
    "김해 출장마사지｜장유·율하·내외동 생활권 안내 | 간다GO",
    "김해 출장마사지 장유·율하 신도시와 내외동 도심, 김해공항 인접 생활권 안내.",
    "김해 출장마사지 · 장유·율하·내외동 생활권 안내",
    "김해는 부산과 붙어 있는 경남 핵심 생활권으로 신도시·도심·공항 인접권의 이용 기준이 다릅니다.",
    "<p>김해는 <strong>장유·율하</strong>의 신도시 아파트, <strong>내외동</strong>의 도심 생활권, "
    "<strong>삼계·구산</strong>의 주거지, <strong>진영</strong>의 외곽권, 그리고 부산 강서·김해공항으로 "
    "이어지는 <strong>공항 인접권</strong>으로 나뉩니다.</p>"
    "<p>장유·율하 신도시 아파트는 공동현관과 방문 등록을, 공항 인접권은 이동 거리를 예약 전에 확인하는 것이 "
    "좋습니다.</p>",
    [
        {"title": "장유·율하", "body": "신도시 아파트·오피스텔 밀집. 공동현관·방문 등록 확인.", "url": "/life/gimhae-jangyu-yulha/"},
        {"title": "내외동·삼계", "body": "김해 원도심 상권·주거권. 도심 오피스텔·아파트 출입 확인.", "url": "/life/gimhae-naeoe-samgye/"},
        {"title": "진영", "body": "봉하·진영역 낀 동부 외곽 신도시. 이동 거리·아파트 출입 확인.", "url": "/life/gimhae-jinyeong/"},
        {"title": "공항 인접권", "body": "부산 강서·김해공항 연결권. 이동 거리·예약 시간대 확인.", "url": "/gimhae/"},
    ],
    [("장유·율하", "/life/gimhae-jangyu-yulha/"), ("내외동·삼계", "/life/gimhae-naeoe-samgye/"),
     ("진영", "/life/gimhae-jinyeong/"), ("공항 인접권", "/gimhae/")],
    [("스웨디시", "/program/swedish/"), ("타이마사지", "/program/thai-massage/"),
     ("아로마테라피", "/program/aroma-therapy/")],
    region_faqs([
        ("장유 신도시 아파트도 방문하나요?",
         "장유·율하 아파트는 공동현관·방문 등록 절차를 예약 전에 확인한 뒤 방문 가능 여부를 안내합니다."),
    ]),
)

GYEONGNAM = region_page(
    "/gyeongnam/", "경남",
    "경남 출장마사지｜양산·진주·거제·통영 생활권 안내 | 간다GO",
    "경남 출장마사지 양산·진주·거제·통영·사천·밀양 주요 시·군 생활권 이용 기준 안내.",
    "경남 출장마사지 · 양산·진주·거제·통영 생활권 안내",
    "경남은 시·군마다 산업·혁신도시·조선업·해안 관광 등 성격이 달라 이용 기준을 시·군별로 나눠 안내합니다.",
    "<p>경남은 <strong>양산·물금</strong>의 부산·울산 사이 주거권, <strong>진주·혁신도시</strong>의 "
    "대학·공공기관 생활권, <strong>거제·통영</strong>의 조선업·해안 관광권, <strong>사천·밀양</strong> "
    "등으로 나뉩니다. 창원·김해·마산은 별도 권역에서 자세히 안내합니다.</p>"
    "<p>거제·통영은 장거리 이동과 리조트·펜션 정책을, 진주혁신도시는 오피스텔 출입 규정을 예약 전에 "
    "확인하는 것이 좋습니다.</p>",
    [
        {"title": "양산·물금", "body": "물금 신도시 아파트·오피스텔. 부산·울산 사이 이동 거리 확인.", "url": "/life/yangsan-mulgeum/"},
        {"title": "진주·혁신도시", "body": "평거·가좌·혁신도시 생활권. KTX·터미널 이동 기준 확인.", "url": "/life/jinju-innovation-city/"},
        {"title": "거제·통영", "body": "조선업 숙소·해안 리조트. 장거리 이동과 숙소 정책 확인.", "url": "/life/geoje-tongyeong/"},
        {"title": "사천·삼천포", "body": "사천 항공산단(KAI)과 삼천포항 관광권. 산단·펜션 기준 확인.", "url": "/life/sacheon-samcheonpo/"},
        {"title": "밀양", "body": "밀양 도심·나노국가산단·밀양역 KTX. 도심·산단 숙소 확인.", "url": "/life/miryang-city/"},
    ],
    [("양산·물금", "/life/yangsan-mulgeum/"), ("진주혁신도시", "/life/jinju-innovation-city/"),
     ("거제·통영", "/life/geoje-tongyeong/"), ("사천·삼천포", "/life/sacheon-samcheonpo/"),
     ("밀양", "/life/miryang-city/")],
    [("스포츠 마사지", "/program/sports-massage/"), ("아로마테라피", "/program/aroma-therapy/"),
     ("발마사지", "/program/foot-massage/")],
    region_faqs([
        ("거제·통영까지도 방문하나요?",
         "거제·통영은 장거리 이동 지역으로 이동 거리와 예약 시간대를 확인한 뒤 방문 가능 여부를 안내합니다."),
    ]),
)

GYEONGBUK = region_page(
    "/gyeongbuk/", "경북",
    "경북 출장마사지｜포항·경주·구미·김천 생활권 안내 | 간다GO",
    "경북 출장마사지 포항·경주·구미·김천·안동·경산 산업·관광 생활권 이용 기준 안내.",
    "경북 출장마사지 · 포항·경주·구미·김천 생활권 안내",
    "경북은 철강·전자 산업단지, 관광 숙소, 동해안 생활권이 도시마다 뚜렷해 이용 기준을 나눠 안내합니다.",
    "<p>경북은 <strong>포항·영일대</strong>의 철강산단·해안 숙소, <strong>경주·보문</strong>의 관광 숙소·"
    "리조트, <strong>구미·인동</strong>의 국가산단·오피스텔, <strong>김천혁신도시</strong>, "
    "<strong>안동·경산</strong> 생활권으로 나뉩니다.</p>"
    "<p>산단 인접 숙소는 장기 체류·야간 이동을, 경주 관광 숙소는 성수기 방문 정책을 예약 전에 확인하는 "
    "것이 좋습니다.</p>",
    [
        {"title": "포항·경주", "body": "포항 철강산단·해안과 경주 보문·황리단길 관광 숙소. 장기·성수기 확인.", "url": "/life/pohang-gyeongju/"},
        {"title": "구미·김천", "body": "구미국가산단·김천혁신도시. KTX·장기 출장 숙소 이동 확인.", "url": "/life/gumi-gimcheon/"},
        {"title": "안동·도청신도시", "body": "경북도청신도시 신축 아파트·안동 구도심. 이동 거리 확인.", "url": "/life/andong-dochung/"},
        {"title": "경산·하양", "body": "대구 인접 대학가 원룸·오피스텔과 산업권. 공간·주차 확인.", "url": "/life/gyeongsan-hayang/"},
    ],
    [("포항·경주", "/life/pohang-gyeongju/"), ("구미·김천", "/life/gumi-gimcheon/"),
     ("안동·도청신도시", "/life/andong-dochung/"), ("경산·하양", "/life/gyeongsan-hayang/")],
    [("스포츠 마사지", "/program/sports-massage/"), ("아로마테라피", "/program/aroma-therapy/"),
     ("발마사지", "/program/foot-massage/")],
    region_faqs([
        ("포항 산단 출장 숙소도 되나요?",
         "철강산단 인접 오피스텔·출장 숙소는 장기 체류·야간 이동 기준을 확인한 뒤 방문 가능 여부를 안내합니다."),
    ]),
)

JEJU = region_page(
    "/jeju/", "제주",
    "제주 출장마사지｜제주시·서귀포 관광 숙소 안내 | 간다GO",
    "제주 출장마사지 제주시·서귀포와 공항·연동·노형·중문·애월·성산 생활권 안내.",
    "제주 출장마사지 · 제주시·서귀포 관광 숙소 안내",
    "제주는 도심형보다 공항·렌터카 이동, 호텔·리조트·펜션, 해안 숙소 기준이 중요한 지역입니다.",
    "<p>제주는 <strong>제주시 연동·노형</strong> 도심과 <strong>제주공항·용담</strong> 인접권, "
    "<strong>애월·함덕</strong> 해안 숙소, <strong>서귀포 도심</strong>과 <strong>중문·색달</strong> "
    "관광단지, <strong>성산·표선</strong> 외곽권으로 나뉩니다.</p>"
    "<p>제주는 렌터카 이동 거리와 리조트·펜션 방문 정책, 야간 이동 기준을 예약 전에 확인하는 것이 특히 "
    "중요합니다.</p>",
    [
        {"title": "연동·노형", "body": "제주시 도심 호텔·오피스텔. 공항 접근성·방문 정책 확인.", "url": "/life/jeju-city-seogwipo/"},
        {"title": "제주공항·용담", "body": "공항 인접 숙소·렌터카 이동 거점. 이동 거리 확인.", "url": "/jeju/"},
        {"title": "애월·함덕", "body": "해안 펜션·독채. 야간 이동 거리와 숙소 정책 확인.", "url": "/life/jeju-aewol-hamdeok/"},
        {"title": "중문·성산", "body": "중문 관광단지 리조트·호텔과 성산 동부. 성수기·장거리 확인.", "url": "/life/jeju-jungmun-seongsan/"},
        {"title": "서귀포 도심", "body": "이중섭거리·올레시장 구도심과 강정 혁신도시. 이동 거리 확인.", "url": "/life/seogwipo-downtown/"},
        {"title": "대정·안덕", "body": "모슬포·산방산·영어교육도시 제주 서부. 관광 펜션·이동 확인.", "url": "/life/jeju-daejeong-andeok/"},
    ],
    [("연동·노형", "/life/jeju-city-seogwipo/"), ("제주공항", "/jeju/"),
     ("애월·함덕", "/life/jeju-aewol-hamdeok/"), ("중문·성산", "/life/jeju-jungmun-seongsan/"),
     ("서귀포 도심", "/life/seogwipo-downtown/"), ("대정·안덕", "/life/jeju-daejeong-andeok/")],
    [("스웨디시", "/program/swedish/"), ("아로마테라피", "/program/aroma-therapy/"),
     ("발마사지", "/program/foot-massage/")],
    region_faqs([
        ("중문 리조트에서도 되나요?",
         "중문·색달 관광단지 리조트·호텔은 방문 정책과 이동 거리를 확인한 뒤 방문 가능 여부를 안내합니다."),
        ("펜션·독채도 가능한가요?",
         "애월·함덕·성산 등 해안 펜션은 야간 이동 거리와 숙소 정책을 확인한 뒤 안내드립니다."),
    ]),
)


# ---------------------------------------------------------------------------
# Life (생활권) detail factory
# ---------------------------------------------------------------------------
def life_page(path, name, title, desc, h1, lead, sections_html, region_crumb, faqs):
    body = (
        hero(h1, lead, ctas=CTA, eyebrow=f"{name} 생활권")
        + section("", prose(sections_html) + SERVICE_NOTE, center_head=False)
        + section("추천 프로그램·이용 장소", chips([
            ("스웨디시", "/program/swedish/"), ("아로마테라피", "/program/aroma-therapy/"),
            ("호텔·숙소 이용 기준", "/use/hotel/"), ("건물 출입 확인", "/check/building-access/"),
            ("이동비·요금 기준", "/check/travel/"), ("예약 전 확인", "/check/"),
        ]), eyebrow="LINKS")
        + section("자주 묻는 질문", faq_block(faqs), eyebrow="FAQ")
        + section("작성·검수 기준", WHO_HOW_WHY, eyebrow="WHO · HOW · WHY", tight=True)
    )
    return {
        "path": path, "title": title, "desc": desc,
        "crumbs": [("홈", "/"), region_crumb, (name, path)],
        "priority": "0.7", "faqs": faqs, "body": body,
    }


LIFE_HAEUNDAE = life_page(
    "/life/busan-haeundae-centum/", "해운대·센텀",
    "부산 해운대·센텀 출장마사지 생활권 안내 | 간다GO",
    "부산 해운대·센텀·마린시티 호텔·오피스텔 출장마사지 이용 전 확인사항 안내.",
    "부산 해운대·센텀 출장마사지 생활권 안내",
    "해운대·센텀시티·마린시티·벡스코 인접 관광 숙소와 오피스텔 이용 기준을 정리했습니다.",
    "<h2>이 생활권의 특징</h2>"
    "<p>해운대·센텀은 마린시티 고층 오피스텔, 벡스코·센텀 업무지구, 해운대 해변 호텔이 밀집한 "
    "부산의 대표 관광·업무 복합 생활권입니다. 관광 성수기에는 호텔별 외부인 방문 정책이 달라집니다.</p>"
    "<h2>호텔·숙소 이용 전 확인</h2>"
    "<p>해운대 해변 호텔은 프런트 방문 등록 여부를, 마린시티 오피스텔은 공동현관 비밀번호와 주차 동선을 "
    "예약 전에 확인하는 것이 좋습니다.</p>"
    "<h2>가까운 역·거점</h2>"
    "<p>해운대역·센텀시티역·벡스코 인접으로 이동 접근성이 좋아 예약 시간대 조율이 비교적 수월합니다.</p>",
    ("부산 출장마사지", "/busan/"),
    region_faqs([
        ("마린시티 오피스텔도 되나요?",
         "고층 오피스텔은 공동현관·주차 동선을 예약 전에 확인한 뒤 방문 가능 여부를 안내합니다."),
    ]),
)

LIFE_SANGNAM = life_page(
    "/life/changwon-sangnam-jungang/", "창원 상남·중앙",
    "창원 상남·중앙 출장마사지 생활권 안내 | 간다GO",
    "창원 상남·중앙 도심 오피스텔·업무지구 출장마사지 이용 전 확인사항 안내.",
    "창원 상남·중앙 출장마사지 생활권 안내",
    "창원 최대 도심 상권인 상남·중앙 오피스텔과 업무지구 이용 기준을 정리했습니다.",
    "<h2>이 생활권의 특징</h2>"
    "<p>상남·중앙은 창원 도심 상권과 오피스텔이 밀집한 지역으로, 업무·야간 수요가 함께 있습니다.</p>"
    "<h2>오피스텔 이용 전 확인</h2>"
    "<p>도심 오피스텔은 공동현관 비밀번호와 방문 등록, 주차 동선을 예약 전에 확인하는 것이 좋습니다.</p>"
    "<h2>가까운 역·거점</h2>"
    "<p>창원중앙역·시외버스 접근성이 좋아 예약 시간대 조율이 수월한 편입니다.</p>",
    ("창원 출장마사지", "/changwon/"),
    region_faqs([
        ("야간 예약도 되나요?",
         "야간은 건물 출입 가능 여부와 이동 거리를 확인한 뒤 안내드리며, ‘24시간 무조건 가능’은 안내하지 않습니다."),
    ]),
)

LIFE_JANGYU = life_page(
    "/life/gimhae-jangyu-yulha/", "김해 장유·율하",
    "김해 장유·율하 출장마사지 생활권 안내 | 간다GO",
    "김해 장유·율하 신도시 아파트·오피스텔 출장마사지 이용 전 확인사항 안내.",
    "김해 장유·율하 출장마사지 생활권 안내",
    "장유·율하 신도시 아파트·오피스텔의 공동현관과 방문 등록 기준을 정리했습니다.",
    "<h2>이 생활권의 특징</h2>"
    "<p>장유·율하는 김해의 대표 신도시로 아파트 단지와 오피스텔이 밀집해 있고 부산 접근성이 좋습니다.</p>"
    "<h2>아파트·오피스텔 이용 전 확인</h2>"
    "<p>신축 단지는 공동현관 방문 등록과 지상·지하 주차 동선, 엘리베이터 카드키 여부를 예약 전에 확인하는 "
    "것이 좋습니다.</p>"
    "<h2>이동 거리</h2>"
    "<p>부산 강서·김해공항과 가까워 예약 시간대에 따라 이동 거리를 확인합니다.</p>",
    ("김해 출장마사지", "/gimhae/"),
    region_faqs([
        ("신축 아파트 공동현관은 어떻게 하나요?",
         "방문 등록·세대 호출 방식이 단지마다 달라 예약 전에 출입 방법을 확인한 뒤 안내드립니다."),
    ]),
)

LIFE_JEJU = life_page(
    "/life/jeju-city-seogwipo/", "제주시·서귀포",
    "제주시·서귀포 출장마사지 생활권 안내 | 간다GO",
    "제주시 연동·노형과 서귀포 중문 호텔·리조트 출장마사지 이용 전 확인사항 안내.",
    "제주시·서귀포 출장마사지 생활권 안내",
    "제주시 연동·노형 도심과 서귀포 중문 관광 숙소의 이동·방문 기준을 정리했습니다.",
    "<h2>이 생활권의 특징</h2>"
    "<p>제주시 연동·노형은 도심 호텔·오피스텔, 서귀포 중문은 관광단지 리조트·호텔이 중심입니다. "
    "렌터카 이동이 일반적이라 이동 거리 기준이 중요합니다.</p>"
    "<h2>호텔·리조트 이용 전 확인</h2>"
    "<p>중문 리조트는 성수기 외부인 방문 정책을, 도심 호텔은 프런트 등록 여부를 예약 전에 확인하는 것이 "
    "좋습니다.</p>"
    "<h2>이동 거리</h2>"
    "<p>제주공항에서 연동·노형은 가깝지만 중문·성산은 이동 거리가 길어 예약 시간대 조율이 필요합니다.</p>",
    ("제주 출장마사지", "/jeju/"),
    region_faqs([
        ("공항에서 중문까지 이동 거리가 먼가요?",
         "제주공항–중문은 이동 거리가 있어 예약 시간대와 이동 시간을 확인한 뒤 방문 가능 여부를 안내합니다."),
    ]),
)


# ---------------------------------------------------------------------------
# Program hub + program pages
# ---------------------------------------------------------------------------
PROGRAM_HUB = {
    "path": "/program/",
    "title": "마사지 프로그램 안내｜스웨디시·타이·아로마 | 간다GO",
    "desc": "스웨디시·타이·아로마·스포츠·발마사지 프로그램별 특징과 숙소 이용 기준 안내.",
    "crumbs": [("홈", "/"), ("마사지 프로그램", "/program/")],
    "priority": "0.8",
    "faqs": [
        ("어떤 프로그램을 선택해야 하나요?",
         "릴렉스 중심이면 스웨디시·아로마, 스트레칭 중심이면 타이마사지, 운동 후 관리면 스포츠 마사지를 참고하세요."),
    ],
    "body": (
        hero("마사지 프로그램 안내",
             "프로그램마다 압·오일·필요 공간·복장 기준이 다릅니다. 숙소 유형에 맞춰 선택 기준을 정리했습니다.",
             ctas=CTA, eyebrow="PROGRAMS")
        + section("프로그램 살펴보기", cards(PROGRAM_CARDS, cols=3))
        + section("이용 장소별 선택 기준", cards(USE_CARDS, cols=4), eyebrow="PLACES")
        + section("자주 묻는 질문", faq_block([
            ("어떤 프로그램을 선택해야 하나요?",
             "릴렉스 중심이면 스웨디시·아로마, 스트레칭 중심이면 타이마사지, 운동 후 관리면 스포츠 마사지를 참고하세요."),
        ]), eyebrow="FAQ")
    ),
}


def program_page(path, name, title, desc, lead, body_html, faqs):
    body = (
        hero(f"{name}", lead, ctas=CTA, eyebrow="PROGRAM")
        + section("", prose(body_html) + SERVICE_NOTE, center_head=False)
        + section("이 프로그램이 잘 맞는 지역", chips([
            ("부산 해운대·센텀", "/life/busan-haeundae-centum/"),
            ("창원 상남·중앙", "/life/changwon-sangnam-jungang/"),
            ("김해 장유·율하", "/life/gimhae-jangyu-yulha/"),
            ("제주 연동·노형", "/life/jeju-city-seogwipo/"),
        ]), eyebrow="REGIONS")
        + section("자주 묻는 질문", faq_block(faqs), eyebrow="FAQ")
    )
    return {
        "path": path, "title": title, "desc": desc,
        "crumbs": [("홈", "/"), ("마사지 프로그램", "/program/"), (name, path)],
        "priority": "0.6", "faqs": faqs, "service": name, "body": body,
    }


SWEDISH = program_page(
    "/program/swedish/", "스웨디시",
    "스웨디시 마사지 안내｜부드러운 오일 릴렉스 케어 | 간다GO",
    "스웨디시 마사지 특징과 오일 사용·호텔·오피스텔 이용 전 확인사항 안내.",
    "부드러운 압과 오일을 사용하는 릴렉스 중심 프로그램입니다.",
    "<h2>스웨디시 특징</h2>"
    "<p>스웨디시는 부드럽고 일정한 압으로 전신을 이완시키는 오일 마사지입니다. 강한 지압보다 릴렉스를 "
    "원하는 분께 적합합니다.</p>"
    "<h2>이용 전 확인</h2>"
    "<p>오일을 사용하므로 호텔·오피스텔의 침구·타월 정책과 샤워 가능 여부를 예약 전에 확인하는 것이 "
    "좋습니다. 피부가 민감한 경우 미리 알려주세요.</p>",
    [("오일이 침구에 묻지 않나요?",
      "타월을 사용하며, 숙소 침구 정책에 맞춰 준비합니다. 호텔은 예약 전에 타월·샤워 가능 여부를 확인해 주세요.")],
)

THAI = program_page(
    "/program/thai-massage/", "타이마사지",
    "타이마사지 안내｜스트레칭 중심 프로그램 | 간다GO",
    "타이마사지 특징과 필요 공간·복장 등 자택·숙소 이용 전 확인사항 안내.",
    "스트레칭과 지압 위주로 진행되는 프로그램입니다.",
    "<h2>타이마사지 특징</h2>"
    "<p>타이마사지는 오일 없이 스트레칭과 체중을 이용한 지압으로 진행됩니다. 몸을 크게 움직이므로 바닥 "
    "공간이 어느 정도 필요합니다.</p>"
    "<h2>이용 전 확인</h2>"
    "<p>매트를 펼 수 있는 공간과 편한 복장이 필요합니다. 좁은 오피스텔은 공간 확보 여부를 예약 전에 "
    "확인하는 것이 좋습니다.</p>",
    [("공간이 얼마나 필요한가요?",
      "매트를 펼 수 있는 바닥 공간이 필요합니다. 원룸·오피스텔은 예약 전에 공간을 확인해 주세요.")],
)

AROMA = program_page(
    "/program/aroma-therapy/", "아로마테라피",
    "아로마테라피 안내｜향과 오일 릴렉스 케어 | 간다GO",
    "아로마테라피 특징과 향·피부 민감도, 숙소 오일 정책 확인사항 안내.",
    "아로마 오일과 향을 활용한 릴렉스 중심 프로그램입니다.",
    "<h2>아로마테라피 특징</h2>"
    "<p>아로마테라피는 향이 있는 오일을 사용해 이완을 돕는 프로그램입니다. 향과 오일에 대한 민감도가 "
    "사람마다 달라 사전 확인이 중요합니다.</p>"
    "<h2>이용 전 확인</h2>"
    "<p>향 민감도·피부 알레르기, 숙소의 오일·환기 정책을 예약 전에 확인하는 것이 좋습니다.</p>",
    [("향에 민감한데 괜찮을까요?",
      "향 강도를 조절할 수 있습니다. 알레르기·민감 사항이 있으면 예약 시 미리 알려주세요.")],
)

SPORTS = program_page(
    "/program/sports-massage/", "스포츠 마사지",
    "스포츠 마사지 안내｜운동 후 컨디션 관리 | 간다GO",
    "스포츠 마사지 특징과 압 조절·이용 전 확인사항 안내. 치료·회복 보장은 아닙니다.",
    "운동 후 뭉친 부위를 압 조절 중심으로 관리하는 프로그램입니다.",
    "<h2>스포츠 마사지 특징</h2>"
    "<p>스포츠 마사지는 운동 후 근육 피로 부위를 중심으로 압을 조절해 관리합니다. 무리한 압은 사용하지 "
    "않으며, <strong>치료·회복을 보장하는 의료 행위가 아닙니다.</strong></p>"
    "<h2>이용 전 확인</h2>"
    "<p>통증·부상 부위가 있으면 예약 전에 알려주세요. 상태에 따라 압을 조절합니다.</p>",
    [("부상 부위가 있어도 되나요?",
      "부상·통증 부위는 예약 전에 알려주시면 압을 조절합니다. 치료가 필요한 경우 의료기관 상담을 권합니다.")],
)

FOOT = program_page(
    "/program/foot-massage/", "발마사지",
    "발마사지 안내｜발·종아리 집중 관리 | 간다GO",
    "발마사지 특징과 관광·장시간 보행 후 이용 전 확인사항 안내.",
    "장시간 보행 후 발과 종아리를 집중 관리하는 프로그램입니다.",
    "<h2>발마사지 특징</h2>"
    "<p>발마사지는 발·종아리 부위를 집중적으로 관리하는 프로그램으로, 관광·출장으로 오래 걸은 분께 "
    "적합합니다.</p>"
    "<h2>이용 전 확인</h2>"
    "<p>의자 또는 앉을 공간이 있으면 편하게 진행할 수 있습니다. 숙소 유형을 예약 전에 알려주세요.</p>",
    [("관광 중 호텔에서도 되나요?",
      "호텔 방문 정책과 예약 시간대를 확인한 뒤 안내드립니다. 관광 후 저녁 시간대 예약이 많습니다.")],
)


# ---------------------------------------------------------------------------
# Use / Check / About / Policy / Contact
# ---------------------------------------------------------------------------
USE = {
    "path": "/use/",
    "title": "이용 장소별 확인 기준｜호텔·오피스텔·자택 | 간다GO",
    "desc": "자택·호텔·오피스텔·리조트 등 숙소 유형별 출장마사지 이용 전 확인 기준 안내.",
    "crumbs": [("홈", "/"), ("이용 장소", "/use/")],
    "priority": "0.7",
    "faqs": [
        ("숙소 유형을 왜 미리 알려야 하나요?",
         "자택·호텔·오피스텔·리조트마다 출입 방식과 방문 정책이 달라, 방문 가능 여부와 예약 시간대를 정확히 안내하기 위함입니다."),
    ],
    "body": (
        hero("이용 장소별 확인 기준",
             "숙소 유형마다 공동현관·방문 정책·주차·이동 거리가 다릅니다. 예약 전 확인 항목을 정리했습니다.",
             ctas=CTA, eyebrow="PLACES")
        + section("", prose(
            "<h2>자택·아파트</h2><p>공동현관 방문 등록, 세대 호출, 주차·엘리베이터 동선을 확인합니다.</p>"
            "<h2>호텔·숙소</h2><p>호텔마다 외부인 방문 정책이 달라 프런트 등록 여부를 예약 전에 확인합니다.</p>"
            "<h2>오피스텔</h2><p>공동현관 비밀번호·방문 등록 등 건물 규정을 확인합니다.</p>"
            "<h2>리조트·펜션</h2><p>관광 숙소 방문 정책과 야간 이동 거리를 함께 확인합니다.</p>"
        ) + SERVICE_NOTE, center_head=False)
        + section("장소별 상세 안내", chips([
            ("자택·아파트", "/use/home/"), ("호텔·숙소", "/use/hotel/"),
            ("오피스텔", "/use/officetel/"), ("리조트·펜션", "/use/resort/"),
            ("산업단지 인접", "/use/industrial-area/"), ("야간 예약", "/use/night/"),
        ]), eyebrow="PLACES")
        + section("지역별 안내로 이동", chips([
            ("부산", "/busan/"), ("창원", "/changwon/"), ("김해", "/gimhae/"),
            ("경남", "/gyeongnam/"), ("경북", "/gyeongbuk/"), ("제주", "/jeju/"),
        ]), eyebrow="REGIONS")
        + section("자주 묻는 질문", faq_block([
            ("숙소 유형을 왜 미리 알려야 하나요?",
             "자택·호텔·오피스텔·리조트마다 출입 방식과 방문 정책이 달라, 방문 가능 여부와 예약 시간대를 정확히 안내하기 위함입니다."),
        ]), eyebrow="FAQ")
    ),
}

CHECK = {
    "path": "/check/",
    "title": "예약 전 확인사항｜출입·이동·시간·개인정보 | 간다GO",
    "desc": "출장마사지 예약 전 건물 출입·이동 거리·예약 시간·개인정보 처리 확인사항 안내.",
    "crumbs": [("홈", "/"), ("예약 전 확인", "/check/")],
    "priority": "0.7",
    "faqs": [
        ("예약할 때 무엇을 알려줘야 하나요?",
         "지역·숙소 유형·건물 출입 방법·희망 시간대를 알려주시면 방문 가능 여부와 이동 시간을 확인해 드립니다."),
        ("개인정보는 어떻게 처리되나요?",
         "예약에 필요한 최소 정보만 확인하며, 개인정보처리방침에 따라 처리합니다."),
    ],
    "body": (
        hero("예약 전 확인사항",
             "매끄러운 방문을 위해 미리 확인하면 좋은 항목을 정리했습니다.",
             ctas=CTA, eyebrow="BEFORE BOOKING")
        + section("", prose(
            "<h2>주소·건물 출입</h2><p>정확한 주소와 공동현관·방문 등록 방법을 확인합니다.</p>"
            "<h2>이동 거리·예약 시간</h2><p>지역·시간대에 따라 이동 시간이 달라 방문 가능 여부를 확인합니다.</p>"
            "<h2 id='travel'>요금·이동</h2><p>60·90·120분 코스별 기준 요금이 있으며, 이동 거리에 따라 상담 시 최종 확인됩니다.</p>"
            "<h2>개인정보 처리</h2><p>예약에 필요한 최소 정보만 확인하며 개인정보처리방침에 따라 처리합니다.</p>"
        ) + SERVICE_NOTE, center_head=False)
        + section("항목별 상세 확인", chips([
            ("주소·위치 확인", "/check/address/"), ("건물 출입 확인", "/check/building-access/"),
            ("예약 시간 확인", "/check/time/"), ("이동비·요금 기준", "/check/travel/"),
            ("야간 출입·이동", "/check/night-access/"), ("개인정보처리방침", "/policy/privacy/"),
        ]), eyebrow="CHECKLIST")
        + section("자주 묻는 질문", faq_block([
            ("예약할 때 무엇을 알려줘야 하나요?",
             "지역·숙소 유형·건물 출입 방법·희망 시간대를 알려주시면 방문 가능 여부와 이동 시간을 확인해 드립니다."),
            ("개인정보는 어떻게 처리되나요?",
             "예약에 필요한 최소 정보만 확인하며, 개인정보처리방침에 따라 처리합니다."),
        ]), eyebrow="FAQ")
    ),
}

ABOUT = {
    "path": "/about/",
    "title": "운영 기준·작성 및 검수 안내 | 간다GO",
    "desc": "간다GO 지역 안내 콘텐츠의 작성·검수 기준과 운영 원칙(E-E-A-T) 안내.",
    "crumbs": [("홈", "/"), ("운영 기준·작성자", "/about/")],
    "priority": "0.5",
    "body": (
        hero("운영 기준 · 작성 및 검수 안내",
             "이 사이트의 콘텐츠가 누가·어떻게·왜 만들어지는지 밝힙니다.",
             ctas=[("문의하기", "/contact/", "btn--primary")], eyebrow="ABOUT")
        + section("작성·검수 기준", WHO_HOW_WHY)
        + section("", prose(
            "<h2>운영 원칙</h2>"
            "<ul>"
            "<li>공식 행정구역·생활권 자료를 기준으로 지역 정보를 작성합니다.</li>"
            "<li>허위 후기·별점, 실제와 다른 구조화 데이터는 사용하지 않습니다.</li>"
            "<li>실제 오프라인 매장이 없으므로 LocalBusiness·Review·평점 스키마는 사용하지 않습니다.</li>"
            "<li>불법·선정적 서비스는 제공·알선·암시하지 않습니다.</li>"
            "<li>AI 보조 도구를 쓰더라도 최종 문구는 사람이 검수합니다.</li>"
            "</ul>"
        ) + SERVICE_NOTE, center_head=False)
    ),
}

PRIVACY = {
    "path": "/policy/privacy/",
    "title": "개인정보처리방침 | 간다GO",
    "desc": "간다GO 개인정보 수집·이용·보관·파기 기준과 이용자 권리 안내.",
    "crumbs": [("홈", "/"), ("개인정보처리방침", "/policy/privacy/")],
    "priority": "0.3",
    "body": (
        hero("개인정보처리방침", "예약 상담에 필요한 최소한의 정보만 처리합니다.", eyebrow="PRIVACY")
        + section("", prose(
            "<h2>수집 항목</h2><p>예약 상담에 필요한 연락처와 방문 지역·숙소 유형·희망 시간대 등 최소 정보만 확인합니다.</p>"
            "<h2>이용 목적</h2><p>방문 가능 여부 확인 및 예약 상담 응대 목적으로만 이용합니다.</p>"
            "<h2>보관·파기</h2><p>상담 목적이 끝나면 관련 정보를 지체 없이 파기합니다.</p>"
            "<h2>이용자 권리</h2><p>본인 정보의 열람·정정·삭제를 요청할 수 있으며, 요청 시 지체 없이 조치합니다.</p>"
            "<h2>문의</h2><p>개인정보 관련 문의는 " + TEL_DISPLAY + " 또는 문의하기 페이지로 접수할 수 있습니다.</p>"
        ), center_head=False)
    ),
}

SERVICE_POLICY = {
    "path": "/policy/service/",
    "title": "서비스 이용 원칙·불법 및 선정적 서비스 불가 안내 | 간다GO",
    "desc": "간다GO는 불법·선정적 서비스를 제공·알선·암시하지 않습니다. 이용 원칙 안내.",
    "crumbs": [("홈", "/"), ("서비스 이용 원칙", "/policy/service/")],
    "priority": "0.3",
    "body": (
        hero("서비스 이용 원칙",
             "건전한 방문형 웰니스 안내를 위한 원칙을 명확히 밝힙니다.",
             eyebrow="POLICY")
        + section("", prose(
            "<h2>불법·선정적 서비스 불가</h2>"
            "<p>본 사이트와 안내되는 서비스는 <strong>불법·선정적 행위를 제공·알선·암시하지 않습니다.</strong> "
            "관련 문의에는 응대하지 않습니다.</p>"
            "<h2>건전한 이용 안내</h2>"
            "<p>안내되는 프로그램은 릴렉스·컨디션 관리 목적의 마사지이며, 의료 행위나 치료를 보장하지 않습니다.</p>"
            "<h2>정확한 정보 제공</h2>"
            "<p>허위 후기·별점을 게시하지 않으며, 방문 가능 여부는 실제 주소와 예약 조건 확인 후 안내합니다.</p>"
        ) + SERVICE_NOTE, center_head=False)
    ),
}

CONTACT = {
    "path": "/contact/",
    "title": "문의하기·전화 예약 | 간다GO",
    "desc": "간다GO 전화 예약 0508-202-4719. 지역·숙소·시간대 확인 후 방문 안내.",
    "crumbs": [("홈", "/"), ("문의하기", "/contact/")],
    "priority": "0.6",
    "faqs": [
        ("어떻게 문의하나요?",
         f"{TEL_DISPLAY} 로 전화하시면 지역·숙소 유형·희망 시간대를 확인한 뒤 방문 가능 여부를 안내드립니다."),
    ],
    "body": (
        hero("문의하기 · 전화 예약",
             f"전화 예약 {TEL_DISPLAY}. 지역·숙소 유형·희망 시간대를 알려주시면 방문 가능 여부를 확인해 드립니다.",
             ctas=[("전화 예약 " + TEL_DISPLAY, TEL_LINK, "btn--primary")],
             eyebrow="CONTACT")
        + section("", prose(
            "<h2>전화 예약</h2><p><a class='brand-text' href='" + TEL_LINK + "'>" + TEL_DISPLAY + "</a> "
            "로 전화 주시면 상담해 드립니다.</p>"
            "<h2>제작·제휴 문의</h2><p>웹사이트 제작문의와 제휴문의는 화면 하단(푸터)의 오렌지색 텔레그램 "
            "버튼으로 접수할 수 있습니다.</p>"
        ) + SERVICE_NOTE, center_head=False)
        + section("자주 묻는 질문", faq_block([
            ("어떻게 문의하나요?",
             f"{TEL_DISPLAY} 로 전화하시면 지역·숙소 유형·희망 시간대를 확인한 뒤 방문 가능 여부를 안내드립니다."),
        ]), eyebrow="FAQ")
    ),
}


PAGES = [
    MAIN,
    BUSAN, CHANGWON, MASAN, GIMHAE, GYEONGNAM, GYEONGBUK, JEJU,
    LIFE_HAEUNDAE, LIFE_SANGNAM, LIFE_JANGYU, LIFE_JEJU,
    PROGRAM_HUB, SWEDISH, THAI, AROMA, SPORTS, FOOT,
    USE, CHECK, ABOUT, PRIVACY, SERVICE_POLICY, CONTACT,
]

# Expansion pages (life areas, place/checklist guides, extra programs).
# Imported after the factories above are defined to avoid a circular import.
from content_more import MORE_PAGES  # noqa: E402
PAGES += MORE_PAGES
from content_more2 import MORE_PAGES2  # noqa: E402
PAGES += MORE_PAGES2
from content_more3 import MORE_PAGES3  # noqa: E402
PAGES += MORE_PAGES3
from content_more4 import MORE_PAGES4  # noqa: E402
PAGES += MORE_PAGES4
