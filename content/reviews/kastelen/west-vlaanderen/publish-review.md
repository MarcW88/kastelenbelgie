# Museum analysis workflow: PUBLISH_REVIEW

Route: /kastelen/west-vlaanderen/
Workflow: museum-v1, with the separate nl-BE castle context
Date: 2026-10-22

## Decision

**PASS — READY_FOR_HUMAN_VALIDATION**

This is editorial readiness for human review, not an indexing instruction. The existing noindex,follow remains in place. No physical visit, user study, Google ranking gain or AI citation test is claimed.

## Gate evidence

| Gate | Result | Evidence |
|---|---|---|
| NEW_PAGE research and ownership | PASS | Existing live URL is a placeholder. Research matrix records current search findings, inspected pages, eight primary-source visit choices, conflicts and limitations. REGION scope retained. |
| Brief before drafting | PASS | content/briefs/kastelen/west-vlaanderen.md; requirements derive from visit intent, not a compulsory article template. |
| MUST coverage and post-write review | PASS | post-write-gap-check.md; no central MUST missing. |
| Useful visit proposition / entity precision | PASS | Three access modes, real municipalities, different reasons to choose each site. No invented collections, architects, IDs or historic-room access. |
| Factuality / freshness | PASS for the scoped conditional claims | Separate fact-check.md; official sources beside the blocks and actual check date; chosen-day availability/tariffs not asserted. Source-fetch limitations disclosed in research. |
| Style / GEO / anti-slop | PASS for local editorial checks | Separate passes in editorial-passes.md; direct answer, extractable list, functional blocks, no manufactured FAQ or false firsthand narrative. |
| Cannibalisation / local links | PASS for available content | Provincial ownership retained; parent directory link is verified in body by the original linking script (no_action_needed). No new competing URLs; no claims about unavailable performance signals. |
| Static rendering / metadata | PASS | One H1, self-canonical, preserved robots, honest CollectionPage/ItemList/BreadcrumbList. Native reviewed-content checker passes. |
| Source-of-truth preservation | PASS | Native build loads body.html through reviewed-pages.json. Two successive builds are byte-identical; other 54 published HTML pages unchanged. |
| Shared agent identity | PASS | verify_museum_agents.py: 555 shared files + 30 original migration files intact. |
| Responsive / interaction evidence | PASS | playwright.json: 1440, 768, 390 and 320px; eight blocks at each width; no overflow or JS/network errors; jump links, keyboard skip link and mobile menu checked. Eight blocks remain without JS. |
| Visual inspection | PASS for this page | Final top/group/park/planning and full-page captures inspected at desktop/mobile sizes. Small-screen brand/title and route-qualified anchor issues fixed. Actual Cormorant Garamond and Manrope loaded after configuring the test browser's environment network proxy; final report has no failed requests. |

## Scope and remaining limits

- Preserve the current noindex until explicit human validation and a separate indexation instruction.
- This is a curated selection, not every castle in West Flanders and not an absolute beauty/quality ranking.
- Conditions can change after 22 October 2026; links point readers to the responsible operator/public institution.
- Some primary websites returned 403 to extraction. Current indexed official information and accessible official alternatives were used for the limited claims; no blocked daily details were invented.
- Google Rich Results Test, Search Console inspection, field Core Web Vitals and external AI-product citation benchmarks were not run. Local JSON-LD syntax/content matching is verified, not external rich-result eligibility.
- Existing sitewide issues outside the one-page change (including other placeholder pages) were not treated as finished content or audited into a global PASS.
- Photographs are optional here. No generated image impersonates a real castle and no image license was invented.
- Captures are intentionally unversioned in .artifacts/design-review/west-vlaanderen/ per the source design workflow; filenames and hashes are recorded in screenshots.json. JSON interaction/layout evidence is versioned.
