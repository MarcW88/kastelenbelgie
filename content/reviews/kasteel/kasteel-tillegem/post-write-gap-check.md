# kasteel-tillegem — post-write gap check & PUBLISH_REVIEW
workflow_version: museum-v1
mode: NEW_PAGE
checked_at: 2026-10-22

| Workflow step | Status | Evidence / blocker |
|---|---|---|
| Route ownership & intent | COVERED | One specific estate /kasteel/kasteel-tillegem/; province selection not duplicated |
| Primary operator source | COVERED | Official outgoing link in content |
| Historical facts and scope | PARTIAL | Official operator heritage material; not every claim independently confirmed |
| Visitor decision (inside vs park) | COVERED | Direct explanation in content |
| Competitive SERP research | PARTIAL | Search conducted, ranking/top-ten/keyword exports absent |
| Brief | COVERED | content/briefs/kasteel/kasteel-tillegem.md |
| Structured SERP matrix | PARTIAL | content/research/kasteel/kasteel-tillegem/serp-coverage.md |
| Facts, entity and freshness | PARTIAL | Official primary sources; claims not all individually logged |
| GEO / citation worthiness | PARTIAL | Concrete place/event/context with official links |
| Humanizer / general-writing / anti-ai-slop | PARTIAL | Distinct text reviewed for clone risk; full canonical specialist passes not attested |
| Internal linking | COVERED | Parent province and official operator |
| SEO technical/build | PASS (build) | GitHub Pages build/deploy run 39828024102 completed successfully |
| Desktop/mobile Playwright | PASS (technical) | 2026-10-22 run 39828024075: HTTP 200 at 1440/390, no horizontal overflow or console errors; screenshots inspected, layout remains repetitive |
| Editorial QA / PUBLISH_REVIEW | FAIL | Research and specialist gates incomplete, and structural clone risk HIGH across eight same-layout pages |

Decision: FAIL — KEEP_NOINDEX. These are publication drafts, NOT certified complete pages. Never remove noindex without separate human validation and instruction.

## Humanizer + anti-ai-slop revision — 2026-10-22
- Source edit: content/kasteel/kasteel-tillegem/body.html.
- Current approximate body words including navigation: 453.
- Humanizer: removed duplicated conclusions and softened mechanical repeated visitor contrasts; preserved named people, dates, locations, access constraints and official links.
- Anti-ai-slop: removed overlapping H2 narrative and repeated explanation blocks; retained these concrete page-specific headings: Een omwald kasteel met een lange bewoningsgeschiedenis | Wat er achter de gesloten deur bewaard blijft | Rosmolen, bos en wandelingen | Welke wandelroute past bij je bezoek? | Welke routes maken het domein interessant? | Controleer je bezoek bij de beheerder.
- Separate automated heuristic findings: GitHub Actions West Flanders editorial gates / style-findings artifact (machine check, not proof of human authorship or complete specialist signoff).
- Factuality: volatile opening and price claims should be cross-checked at the official URLs before indexation.
- Verdict: revision performed; comprehensive SERP gate and final human PUBLISH_REVIEW status unchanged.
