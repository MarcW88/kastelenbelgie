# Museum analysis workflow: PUBLISH_REVIEW

Route: /kastelen/oost-vlaanderen/. Workflow: museum-v1 with nl-BE castle context. Date: 2026-10-22.

**PASS — READY_FOR_HUMAN_VALIDATION**

This is editorial readiness, not an instruction to remove noindex. No physical visit, Google ranking improvement or external AI citation performance is claimed.

| Gate | Result | Evidence |
|---|---|---|
| NEW_PAGE research / REGION ownership | PASS | Research matrix: actual search discovery, official sources, conflicts and data limitations |
| Brief before drafting | PASS | content/briefs/kastelen/oost-vlaanderen.md |
| MUST coverage | PASS | post-write-gap-check.md; all central requirements covered |
| Factual / entity / freshness | PASS for scoped claims | fact-check.md, official source per block and dated conditional access |
| GEO, Humanizer, general-writing, anti-slop | PASS local editorial checks | Separate documented passes in editorial-passes.md |
| Local links | PASS | Original internal-linking-audit script: two no_action_needed contextual links |
| Metadata / static content | PASS | Native checks: one H1, self-canonical, matching JSON-LD, preserved robots and source bytes |
| Repeat build / preservation | PASS | build-preservation.json; only target generated HTML changed, other 54 pages identical, second build identical |
| Shared agent identity | PASS | verify_museum_agents.py: 555 shared + 30 migration-original files unchanged |
| Responsive / interaction | PASS | playwright.json: 1440/768/390/320px, eight cards each, no overflow/errors/failed requests, jump links, mobile menu, keyboard skip navigation into main; eight cards without JS |
| Visual inspection | PASS for inspected page | Desktop top and middle cards, mobile top/late card/planning/menu screenshots inspected. Actual Cormorant Garamond and Manrope loaded. Existing CSS reused unchanged. Capture hashes in screenshots.json |

The keyboard skip test checks fragment navigation followed by Tab into main content, rather than requiring a non-tabindex main element itself to become document.activeElement. This verifies the actual sequential keyboard behavior.

Scope: curated eight-site selection, not every castle or a beauty ranking. Current daily availability/tariffs remain with operators. Extraction restrictions and source disagreements are disclosed in research. No GSC, external Rich Results Test, field CWV or AI-product citation benchmark was run. The rest of the site was preserved, not declared editorially complete. No unverified photography or coordinates added. Captures remain unversioned under .artifacts as required by the source design workflow. Existing noindex,follow is preserved pending a separate indexing decision.
