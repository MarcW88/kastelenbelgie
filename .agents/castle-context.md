# Kastelen België — cultural context adapter

## Authority and language

Use the complete original `museum-analysis-workflow` and `museum-content-workflow`, their references, `.agents/MUSEUM_MODEL.md` and `.agents/SKILL_REGISTRY.md` without rewriting or translating their source files. This separate context adapts only subject, market, entity vocabulary, routes and native sources. The cultural routing in `.agents/shared-routing.json` takes precedence over earlier generic guide/comparison/brand/usage selections for cultural pages.

Write publishable content in natural Belgian Dutch (`nl-BE`), market Belgium. Research Flemish/Belgian Dutch queries according to actual intent; French/German official heritage sources may support facts when relevant. The original template's `France / fr-FR` is an example: fill created research reports for Belgium / nl-BE, without modifying the template. Keep technical field/status names from the original workflow.

## Entity interpretation of the unchanged museum model

- Museum/MUSEUM → the exact castle, fortress, palace, ruin or historical estate; no implication that it operates as a museum.
- Place → municipality, province, Belgian region and country. Preserve confirmed multilingual names and aliases without merging different places.
- Building → the historic castle/buildings; verified architects, periods, historical people and events only when useful to the reader.
- Collection/Work → an actually documented collection/object, when applicable; otherwise not applicable. Do not invent a collection, artwork or exhibition to fill the source model.
- Exhibition → a real exhibition or temporary cultural event, with official dates and source, when relevant.
- Visit → independently verify interiors, courtyard, gardens, park, domain, guided visits and accommodation. Public park access does not prove public access to a private castle; visiting and overnight stays are distinct services.
- OFFICIAL_MUSEUM → official castle/site operator for evidence classification. Preserve the original token in the report, specifying the actual official institution.

The original model is a reasoning and provenance model, not a mandatory page layout or a requirement to fill in every field. Missing facts stay missing.

## Route ownership

| Route | Original workflow owner | Actual role |
|---|---|---|
| `/kasteel/<slug>/` | MUSEUM | One identified castle/estate: why visit, heritage and verified access constraints |
| `/kastelen/` and region/province children | REGION or CITY according to actual scope | Geographic exploration/selection with differentiated places |
| `/soorten/<slug>/` | THEME | Heritage type or architectural theme, with confirmed examples |
| `/bezoeken/<slug>/` | VISIT_INTENT | Visiting need: children, gardens, guided visit, access, overnight stay |
| `/routes/<slug>/` | VISIT_INTENT | Feasible itinerary; verify distances, timings, sequence, booking and access rather than inventing a day plan |
| `/inspiratie/<slug>/` | INSPIRATION | Evidence-backed editorial discovery/selection |
| `/gidsen/<slug>/` | GUIDE | Practical or heritage question transverse to a single castle |
| `/` | INSPIRATION | Atlas orientation/discovery; preserve its distinct scope |

These are ownership bindings, not templates. No compulsory headings, tables, FAQ, number of locations, word count or repeated castle structure. Trust pages (`/bronnen/`, `/over-ons/`, `/contact/`) keep trust-content-workflow; design keeps site-design-review. Keep the two museum agents under their original names.

## Entry modes and source artifacts

Read both original workflows and each required specialist in full. Use AUDIT for an existing substantive page; a placeholder/empty editorial page uses NEW_PAGE, as the source workflow specifies. An existing URL alone does not establish existing substantive content. Inspect current page, source, internal neighbours and actual SERP; do not assume the skeleton's sections are the correct brief. Cluster checks use CLUSTER_AUDIT.

For NEW_PAGE/DEEP_REWRITE, keep the original research gate, actual SERP evidence, MUST/SHOULD coverage, brief, separate factual/entity/GEO/style/SEO passes, post-write gap check and PUBLISH_REVIEW. Use:

- `content/research/<route>/serp-coverage.md`
- `content/briefs/<route>.md` with `workflow_version: museum-v1`
- `content/reviews/<route>/post-write-gap-check.md`

Resolve `<route>` including its directory (for example `kasteel/gravensteen`), to avoid slug collisions. Report missing required tools/data as BLOCKED, not as an executed skill or PASS. Humanizer, general-writing and anti-ai-slop are separate passes and must preserve facts, source dates, nuance and conditions.

## Factuality and freshness

Apply the source's complete STABLE / SEMI_STABLE / VOLATILE rules. Important historical/architectural claims require appropriate evidence; contested or uncertain facts remain qualified. Opening hours, closures, ticket prices, booking, tours and events need current official evidence and a verification date. Accessibility/family services are at least SEMI_STABLE. Recheck the facts that influence the actual decision of visit.

Prefer the official castle/site operator and official heritage/tourism/public institutions for their actual remit. Entity databases help identify places and relationships; they do not replace current official visit conditions. Do not invent a personal visit, queue, travel time, recommended duration, accessibility, availability, free entry or an event. A current owner or estate association does not prove public access.

## Native source-of-truth and technical gates

The present `scripts/build.mjs` contains hardcoded page data and writes the atlas homepage and placeholder HTML. It has no reviewed-content loader. Do not run it over authored HTML and lose content. Before publishing authored content, integrate its source into the native build and verify that a rebuild preserves the reviewed text, evidence and metadata. Keep research/brief/review artifacts separate from rendered HTML. This migration does not change the generator or author pages.

`npm run check` is the existing static check of CSS references and noindex; it does not validate editorial depth, facts or coverage. `python3 scripts/verify_museum_agents.py` checks source identity, specialist availability and routing, not page quality. CSS/Playwright gates use real rendered pages and inspected screenshots when a UI task requires them. A missing browser or adapter is a real limitation, never a visual PASS.

Preserve URLs, canonical/robots policy and design. PUBLISH_REVIEW is exactly PASS — READY_FOR_HUMAN_VALIDATION or FAIL — KEEP_NOINDEX; a PASS does not remove noindex. Indexation and structural changes require the original human decisions. The full original Visite Musée instructions are retained at `.agents/reference/visite-musee/AGENTS.md` for their source freshness/evidence context; its museum route names are adapted by this document.

## Specialist provenance

All 22 specialists named in the original registry are available locally. Five previously absent specialists (seo-competitor, jtbd-framing, information-architecture, brand-voice, seo-aeo-geo) and their full tracked directories are copied unchanged from the registry's declared canonical repository, MarcW88/thuisrenovatie-gids at 33ff11ae8c9b6c9fcc416d3d3cff2a3d5e98de95. Their exact source paths and hashes are in museum-agents.lock.json. Existing common specialists retain their canonical shared bytes and lock.
