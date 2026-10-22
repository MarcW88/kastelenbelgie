# Oost-Vlaanderen editorial brief

workflow_version: museum-v1
mode: NEW_PAGE
owner: REGION
language: nl-BE
research: content/research/kastelen/oost-vlaanderen/serp-coverage.md

Target: kastelen Oost-Vlaanderen and visit-selection variants. Reader decision: choose an interior, guided visit or park outing and discover the correct reservation boundary. Scope is a documented selection, not every monument, a wedding venue directory or a ranked list.

## Angle / structure

Answer directly in a short provincial introduction. Show eight blocks in one browsable selection (Gravensteen, Laarne, Ooidonk, Poeke, Wissekerke, Cortewalle, Breivelde, Park van Beervelde). Keep locality, visit mode, actual distinguishing facts and official practical source visible. Follow with region-specific guidance for city/Leie/Meetjesland/Waasland/park choices, then the practical reservation and mobility boundaries. This differs from West-Vlaanderen's separate access-mode sections; shared card markup is intentional UI reuse.

All MUST rows of the research matrix apply. In particular, preserve guided-only Ooidonk interior, Poeke's park/interior distinction, Cortewalle's individual season, Beervelde's advance walking request and non-original villa distinction, Laarne's mobility constraints and the current check date. Do not invent daily hours, prices, personal experience, distances, scores, accessible paths or restaurant availability.

Use DESIGN.md and content/brand/voice.md. Calm, precise heritage atlas in Belgian Dutch; ordinary place names before generic enthusiasm. Relevant historical details explain a difference between sites and do not expand into eight formulaic mini histories. No fixed article word count or compulsory FAQ. Source links are the reader's booking/verification next action.

## Rendering and links

Author content/kastelen/oost-vlaanderen/body.html and append the route to content/reviewed-pages.json. Reuse assets/province-guide.css without altering West-Vlaanderen. Use route-qualified fragments because the shell has a base URL. Preserve noindex, add a self-canonical and CollectionPage/ItemList/BreadcrumbList matching visible sites. Keep all critical content without JS.

Use the actual parent directory and the already authored West-Vlaanderen page for a logical next regional choice; do not advertise unfilled individual fiches as finished guides. Run the original internal-linking script on exported authored HTML.

## Gates

Separate fact-check after draft, then GEO, Humanizer (with its sibling checks), general-writing, anti-slop, on-page/technical SEO and editorial QA. seo-drift is N/A without a substantive baseline; evidence-based-reviews is N/A for this documentary selection; a separate JTBD workshop is unnecessary because the visit task is explicit. Record real data gaps rather than fabricated metrics.

Persist post-write MUST/SHOULD coverage. Run build/check, verify repeat-build stability and byte preservation of all other published pages. Execute actual Playwright desktop/mobile/tablet, menu, keyboard, in-page links and no-JS checks; inspect captures. Only then issue the final museum-analysis PUBLISH_REVIEW. Human approval/indexation remain separate.
