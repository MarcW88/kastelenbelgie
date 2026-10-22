# Gravensteen — post-write gap and PUBLISH_REVIEW
workflow_version: museum-v1
checked_at: 2026-10-22
mode: NEW_PAGE
route: /kasteel/gravensteen/

| MUST/SHOULD | Status | Evidence |
|---|---|---|
| Exact site identity, address, castle vs provincial intent | COVERED | Hero, Sint-Veerleplein 11, /kastelen/oost-vlaanderen/ |
| Official current opening 10–18 and last sale 16:40 | COVERED | https://historischehuizen.stad.gent/nl/info-tickets |
| Prices incl audioguide and booking | COVERED | https://historischehuizen.stad.gent/nl/info-tickets |
| Heritage/historical context and visitable buildings | COVERED | https://visit.gent.be/nl/zien-doen/gravensteen |
| Two audiotours, official lengths and languages | COVERED | https://historischehuizen.stad.gent/nl/gravensteen/bezoek/individueel-bezoek |
| Wheelchair accessibility, 480+ steps, visioguide | COVERED | https://historischehuizen.stad.gent/nl/gravensteen/bezoek/plan-je-bezoek/toegankelijkheid |
| Search intent and information gain | COVERED | Answers actual tour choice and feasibility, not generic castle inspiration |
| Voice/copy/humanizer/general-writing | REVIEWED, not tool-executed end-to-end | Factual, specific narrative, no fictional personal visit; stylistic subagent automation not directly runnable |
| anti-ai-slop | REVIEWED, not full external-tool audit | No invented experience, unsupported superlatives or forced FAQ |
| Onpage SEO / linking | COVERED | Dedicated title/meta, H1, sources, parent province |
| Full SERP result by result / volumes | DATA_GAP | No exhaustive SERP export, no fabricated ranks |
| Native build/check | PENDING | GitHub Action to confirm |
| Visual desktop/mobile | NOT_EXECUTED | No Playwright capture |

## Gate
All central visitor-decision facts have official source links and explicit checked date. No automatic indexation. PUBLISH_REVIEW: FAIL — KEEP_NOINDEX pending executed specialist QA and visual/technical review, despite completed and pushed content.
