# Rumbeke: post-write gap check and PUBLISH_REVIEW
workflow_version: museum-v1
mode: AUDIT -> DEEP_REWRITE -> PUBLISH_REVIEW
checked_at: 2026-10-25

| Requirement | Coverage | Location / evidence |
|---|---|---|
| Specific visit decision | COVERED | Header/intro, group interior versus independent Sterrebos |
| Renaissance construction and legend distinction | COVERED | bouwgeschiedenis; Inventaris/operator |
| Later restoration / information gain | COVERED | 1962 Viérin spire, not an untouched16th-century silhouette |
| Concrete interior evidence | COVERED | interieur; operator features, itinerary caveat |
| Park design, hours and route | COVERED | sterrebos; dated source scope, official plans and interactive route |
| Group terms and uncertainty | COVERED | Semantic source-comparison table,80+3/75min versus80+4/90min, max25 attributed to city |
| Price of actual future booking | PARTIAL, intentionally unresolved | Official publications conflict; no single confirmed quote asserted, organizer confirmation required |
| Accessibility and address | COVERED | toegang-en-adres; inside restriction separated from park plan |
| Authentic photography | COVERED | Local Commons derivative, author/date/licence/display crop |
| Research, brief and claim provenance | COVERED | Route-specific research, brief and separate fact-check |
| Natural internal links | COVERED | Beauvoorde independent route, Tillegem park comparison, province selection |

## Applied separate editorial passes
- content-and-copy: consolidated repeated group-pricing and history paragraphs, replaced appended FAQ and generic practical cards with a single source-aware visit section. Rebuilt narrative around Rumbeke's phases, interior traces and designed landscape; shared Ooidonk shell only.
- fact-check: logged written claims separately in fact-check.md. Corrected the apparent certainty of one group price/duration; both official offers are dated and attributed. Preserved legend qualification; added verified1962 tower restoration. Omitted outdated inventory statement about future reuse and disputed exact door date.
- seo-aeo-geo: explicit entity/alias/place, one direct visitor decision, atomic sourced facts and honest breadcrumb/entity JSON-LD. No fabricated review, FAQ stuffing or schema with unconfirmed ticket terms.
- internal-linking-audit: inspected source links and candidate target roles. Province link answers geographic selection; Beauvoorde answers individual house-route need; Tillegem answers another park choice. No duplicate internal body destination or dot-separated inventory.
- humanizer (including better-usage, academic-voice genre calibration, cadence and global spine/boundary checks): removed repeated inside/outside conclusions, generic “not a waiting room” contrast and inflated “one of oldest” shorthand. Preserved precise history, dates and uncertainty. No invented visit or embellishment.
- general-writing: reviewed title, lead, every heading, caption and navigation label as well as prose. Removed redundant final instruction from lead. Changed the abstract “zestiende eeuw achter het silhouet” to direct “Bouw en restauratie van het Kaasterkasteel”; shortened split-intro title to avoid a stranded first word. Retained all substantive distinctions.
- anti-ai-slop: review purpose is cultural explanation and visit choice. Repeated generic FAQ/cards/list blocks removed. The comparison table has two real contradictory source records, so its structure has a functional reason. No HIGH issue retained.
- editorial-qa: intent, evidence, natural Dutch, practical usefulness, semantic HTML, metadata and scope reviewed. The page is useful without commercial links. Unresolved actual booking price remains explicit, not hidden behind a PASS.

## Local technical/visual evidence
Native build/check and agent integrity checks run separately from editorial review. Dedicated Playwright checks cover1440×1000,768×1024,390×844,360×800 with actual Chromium153. Native repository visual runner also executes desktop/mobile; its product-template selectors are supplemented by assertions for castle-specific components. Route-qualified anchor links account for generated base href=/; click checks verify both pathname and hash. Photo decoded1280×853. Native screenshots and detailed diagnostics stay under ignored .artifacts/design-review/rumbeke(-native)/.

Final screenshot inspection completed at1440,768,390 and360px with actual site fonts and the local authentic photo. No horizontal overflow, page/console errors, failed requests, duplicate IDs, nested links or broken fragments. Keyboard focus, menu and anchor landing below the sticky header passed. The real tariff table was separately captured/inspected at1440 and360px:833px/328px wide, three rows, scoped row/column headers, no clipping. Second build reproduces the exact Rumbeke HTML. All201 tracked HTML robots tags match the baseline; manifest diff changes Rumbeke only.

PUBLISH_REVIEW: PASS — READY_FOR_HUMAN_VALIDATION. Actual organizer quote remains intentionally unresolved; both published source records are accurately represented. Noindex retained. GitHub Actions and public deployment are separate release checks and will be reported with their actual state after the main commit.
