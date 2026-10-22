# Page-scoped SEO and design review

Date: 2026-10-22. Scope /kastelen/vlaams-brabant/ only. Static Node-generated HTML, not React/Laravel. Existing source renderer and shared CSS reused unchanged.

## On-page SEO

| Dimension | Result | Evidence |
|---|---|---|
| Title | PASS | Unique provincial visit title aligned with H1 |
| Description | PASS | Actual sites and conditions, no unsupported promise or keyword list |
| Headings | PASS | One H1, geographic H2 sections, named-site H3s; final mobility H3 |
| Body | PASS local editorial review | Early answer, seven different visitor options, current conditional access and source links |
| Internal links | PASS | Native target check plus original linking audit: two contextual destinations already present |
| Media | N/A photography | No new images; shared decorative logo has fixed dimensions/empty alt |
| URL | PASS | Existing clean provincial URL preserved |
| Schema | PASS local syntax/content match | CollectionPage, seven-item ItemList, BreadcrumbList; no fabricated ratings/hours/author |

## Technical / best-practices checks

- Rendering PASS: static HTML includes all seven blocks with JS disabled. Canonical self-references. Existing noindex,follow deliberately retained; no claim of indexability or traffic improvement.
- Architecture PASS for scoped changes: route already linked by home/province directory; parent breadcrumb and contextual links verified. Other 54 generated HTML pages remain byte-identical.
- Performance implementation: existing fonts use display=swap, logo dimensions reserved, no new heavy assets/embeds/client-fetch content. Field LCP/INP/CLS and Search Console rendering not measured: DATA_GAP.
- Social metadata: OG title/description/type/url and summary Twitter card present. No social preview image supplied: NOT_ADDED; no image/large-card PASS claimed.
- Crawl infrastructure: robots.txt, sitemap.xml and llms.txt absent in this existing repository. This page-scoped task preserves that state; sitewide discovery/indexation infrastructure is not certified. All content remains noindex. No artificial schema/word-length quotas used.
- Rich Results Test / Schema.org external validator: NOT_RUN. Local JSON-LD parsing and visible-content matching verified; eligibility not claimed.
- React/Inertia/Blade rules N/A. Temporary local dependency link/browser proxy adapter is not deployed. Shared original runner files unchanged.

## Design verdict

The page fits the existing atlas: ivory/ink/green/wine tokens, Cormorant Garamond headings and Manrope text, restrained bordered listing cards. Desktop and mobile captures inspected after fonts loaded. No blocking or major local visual finding remains. This is not a whole-site accessibility certification.

Concrete positives: title identifies the province/visit task immediately; mode badges distinguish real access conditions; sources are adjacent and descriptive; two geographic groups orient the reader; mobile cards keep the full text and source link.

| Priority | Finding / evidence | Decision |
|---|---|---|
| Resolved local check | Long province/card/source labels could wrap on 320px | Captures and measured DOM show reflow without clipping or horizontal overflow |
| Scope limitation | Original French runner's .content-main/.burger selectors do not exist here | Recorded fields null/0 are N/A, supplemented by actual main/[data-menu]/[data-castle-site] tests, not counted as passing empty selectors |
| Optional | No real location photography | No license invented; functional typography-led cards retained |

No significant generic-output cluster observed: brand serif/ivory system predates this page; cards satisfy the user's listing requirement and display distinct conditions, rather than decoration or false live metrics.

## Browser evidence

Original site-design-review runner executed unchanged on the actual route at 1440×1000 and 390×844. Environment-only adapter selected installed Chromium headless shell, network proxy and TLS context. Original JSON diagnostic copied to original-visual-report.json. Additional scoped Playwright tests at 1440, 768, 390 and 320px verify seven cards, one H1, canonical/robots, loaded brand fonts, no main overflow, no page/network errors, jump targets below sticky header, menu toggle aria state and keyboard skip navigation (Enter then Tab into main). All seven cards render without JS. No dynamic API/backend exists in this page flow.

Inspected captures: desktop top and middle Bouchout/Arenberg section; mobile top, Horst and planning; 320px Coloma card; open mobile menu. Screenshots remain in ignored .artifacts/design-review/vlaams-brabant per original workflow; hashes recorded separately. CSS source and West/Oost pages unchanged.
