# 간다GO — 부산·경남·경북·제주 출장마사지 지역 안내

정적 사이트입니다. 모든 페이지는 **하나의 소스**(`build.py` + `content.py`)에서
생성되어 푸터·플로팅 전화 버튼·메타 설명(80자 이내)·JSON-LD 스키마가
전 페이지에서 동일하게 유지됩니다.

## 빌드

```bash
python3 build.py      # 24개 페이지 + sitemap.xml + robots.txt 생성
```

로컬 미리보기:

```bash
python3 -m http.server 8099   # http://localhost:8099
```

## 구조

| 파일 | 역할 |
|------|------|
| `config.py`  | 상호·전화·텔레그램·도메인 등 **사이트 상수 (여기만 수정)** |
| `blocks.py`  | 본문 조립용 재사용 HTML 블록(hero/cards/chips/faq/Who·How·Why) |
| `content.py` | 페이지별 **고유 콘텐츠** (지역·프로그램) — 지역명만 바꾼 본문 금지 |
| `build.py`   | 공통 헤더·푸터·플로팅 버튼·스키마 렌더링 + 파일 출력 |
| `assets/`    | Pretendard 기반 프리미엄 토큰 CSS, JS, 파비콘·OG 이미지 |

## 반드시 교체해야 하는 값 (`config.py`)

- `SITE_URL` — 실제 도메인 (canonical/OG/sitemap에 사용)
- `TELEGRAM_BUILD`, `TELEGRAM_PARTNER` — 실제 텔레그램 핸들
  (현재 `https://t.me/gandago` 플레이스홀더)

`상호(간다GO)`, `전화(0508-202-4719)`는 확정값으로 반영되어 있습니다.

## 구현된 요구사항

- **푸터 오렌지 텔레그램 버튼** 2종: 웹사이트 제작문의 · 제휴문의
- **모바일 우측 하단 플로팅 전화 아이콘**: 오렌지, 바운스+펄스 애니메이션,
  터치 시 전화 연결(`tel:`), 전 페이지 노출 (`prefers-reduced-motion` 존중)
- **메타 설명 80자 이내** (전 페이지, 빌드 시 assert로 강제)
- **JSON-LD 스키마**: Organization / WebSite / WebPage / BreadcrumbList /
  FAQPage / (프로그램 한정) Service.
  정책에 따라 **LocalBusiness · Review · AggregateRating 미사용**
- **프리미엄 디자인 토큰**: 딥 차콜-네이비 + 앰버/골드 팔레트,
  Pretendard 가변 폰트, 컴포넌트 오버레이(버튼·카드·가격·FAQ·트러스트 블록)
- **내부링크·롱테일 강화**: 지역 ↔ 생활권 ↔ 프로그램 상호 링크,
  Who·How·Why(E-E-A-T) 블록, 불법·선정적 서비스 불가 안내 전 페이지 배치

## 페이지 확장

`content.py`의 `PAGES` 리스트에 항목을 추가하면 됩니다.
지역 허브는 `region_page(...)`, 생활권 상세는 `life_page(...)`,
프로그램은 `program_page(...)` 팩토리를 사용하세요.
각 페이지는 고유한 본문(생활권·숙소·이동 기준)을 작성해
"지역명만 바꾼 중복 페이지"를 만들지 않습니다.
