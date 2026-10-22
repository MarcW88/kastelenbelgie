# SERP coverage: Oost-Vlaanderen

workflow_version: museum-v1
mode: NEW_PAGE
owner: REGION
market: Belgium / nl-BE
research_date: 2026-10-22
baseline_commit: c3e712d676466ad71e0058e2493e3c2386a0a43a

## Entry and intent

The existing live URL /kastelen/oost-vlaanderen/ and its native source are placeholders, not a substantive article. Preserve its URL/noindex and the atlas design. The task is a regional visit-selection page with named blocks, not a product comparison, a wedding-venue catalogue or a beauty ranking.

Primary cluster: kastelen Oost-Vlaanderen; kastelen Oost-Vlaanderen bezoeken; bezoekbare kastelen Oost-Vlaanderen; kasteelparken Oost-Vlaanderen. Named places are supporting entities, not a reason to create duplicate URLs. The intent is to choose a real visit and understand the difference between a ticketed interior, guided/reserved visit and outdoor access.

## Actual discovery / inspected results

Web discovery used both search engines on 22 October 2026, followed by official operator/municipal pages. This is qualitative search research, not a Google Belgium rank export or search-volume dataset. Google-specific PAA/AIO ownership and performance are unknown.

| Result read | Format / observed value | Gap this page can close |
|---|---|---|
| https://www.komoot.com/nl-nl/guide/370783/de-mooiste-kastelen-in-oost-vlaanderen | Community highlights and route-oriented castle tips; rankings/votes express discovery value, not current interior admission. | Explicit visit modes and primary booking sources; no imitation of community scores. |
| https://www.scheldeland.be/kastelen-van-de-schelde | Official destination editorial combining heritage sites along the Scheldt, across provincial boundaries. | Keep East Flanders ownership; do not import Bornem/Hingene simply because they appear in a Scheldt selection. |
| https://www.routen.be/wandelroutes-kastelen | Official route-oriented discovery, e.g. Ooidonk garden/interior distinctions. | Explain visit conditions even for readers who are not planning a walking route. No invented journey times. |
| https://ooidonk.be/visit | Direct operator calendar separates guided residential castle visits, groups and gardens. | Make the reservation requirement visible next to the name, not buried under an attractive photo. |
| https://www.gemeentebkz.be/toerisme/kastelen/kasteelcortewalle/plan-je-bezoek-cortewalle | Official guided group offering and a bounded May–September Sunday individual season. | Do not advertise individual interior visits as available throughout the year. |

Search also returned event/wedding-venue directories. These do not establish public castle access and are excluded as primary visitor evidence.

## Verified candidate evidence

| Site | Locality | Visit distinction | Current primary source |
|---|---|---|---|
| Gravensteen | Gent | Historic city fortress with public visitor/ticket offering; consult operator's access information | https://historischehuizen.stad.gent/nl/gravensteen/bezoek/plan-je-bezoek and https://visit.gent.be/nl/zien-doen/gravensteen |
| Kasteel van Laarne | Laarne | Castle visitor experience, stories of witch trials; no lift and restricted wheelchair access documented | https://www.herita.be/nl/monumenten/kasteel-van-laarne and /plan-je-bezoek |
| Kasteel Ooidonk | Bachte-Maria-Leerne, Deinze | Occupied castle: guided visit and reservation, gardens separate | https://ooidonk.be/visit |
| Kasteel van Poeke | Poeke, Aalter | Public park; interior only with guide/reservation | https://www.aalter.be/kasteel-van-poeke and https://www.samenherbestemmen.be/nl/locaties/kasteel-van-poeke/wat-er-te-doen |
| Kasteel Wissekerke | Bazel, Waasland | Individual audio-guided interior offer and park; group guide is a separate option | https://www.gemeentebkz.be/toerisme/kastelen/wissekerke/plan-je-bezoek |
| Kasteel Cortewalle | Beveren, Waasland | Guided groups on request; individual Sunday interior season May–September | https://www.gemeentebkz.be/toerisme/kastelen/kasteelcortewalle/plan-je-bezoek-cortewalle |
| Kasteel/domein Breivelde | Grotenberge, Zottegem | Landscape park and castle setting; do not promise a museum tour or current restaurant availability | https://zottegem.be/natuur-en-milieu/parken-en-groen/park-van-breivelde |
| Park van Beervelde | Beervelde, Lochristi | Private park: walking request in advance; current villa replaced old castle, not an intact original castle interior | https://www.parkvanbeervelde.be/nl/bezoek-het-park and https://www.waasland.be/kasteelpark-beervelde |

This bounded selection is not an exhaustive inventory of every castle. Beervelde is explicitly a kasteelpark, not marketed as another original historic castle interior. No private room or garden is inferred to be open from the presence of a wedding/restaurant listing.

## Before-write needs matrix

| Need | Before | Priority | Planned evidence / useful difference |
|---|---|---|---|
| Named, geographically correct visit choices | MISSING | MUST | Eight documented sites; no province spillover from broader Scheldt results. |
| Scanable blocks with actual visit mode | MISSING | MUST | Individual, guided, seasonal, park or private request distinguished per site. |
| Clear interior/garden/reservation boundaries | MISSING | MUST | Ooidonk, Poeke, Cortewalle and Beervelde conditions are materially different. |
| Official next action | MISSING | MUST | Named practical source adjacent to every block. |
| Freshness and source limitations | MISSING | MUST | Visible check date; no open-now badge or unsourced exact prices/hours. |
| Regional guidance and relevant heritage differences | MISSING | MUST | City fortress, Leiestreek/Meetjesland, Waasland and landscape-park choices. |
| Accessibility caution | MISSING | MUST | No inference from bezoekbaar to wheelchair access; Laarne's no-lift limit kept. |
| Stable rebuild source | MISSING | MUST | Existing reviewed-pages loader; preserve West-Vlaanderen and all other pages. |
| Useful internal next step | NAV ONLY | SHOULD | Parent regional directory and the already authored West-Vlaanderen page where the reader wants another province. |
| Photographs or a new map | MISSING | OPTIONAL | No licensed imagery/verified coordinate dataset supplied; do not fabricate either. |

## Sources / freshness / conflicts

STABLE: fortress/castle/site identity and supported heritage distinctions. SEMI_STABLE: visitor use and accessibility; verify when it changes the visit decision. VOLATILE: calendar, reservation rules, price, closure, event and current horeca operation. These are checked at the stated date and are not a live availability guarantee.

- Poeke: operator/current municipality distinguish a public park and guided interior. Public website descriptions disagree on a single architectural label (rococo vs neoclassical); no unsupported universal style label is needed in the copy.
- Cortewalle: individual May–September Sundays are not the same as year-round guided group applications. Current date lies outside that individual season; retain the boundary without inventing next-year dates.
- Beervelde: free walking and prior permission are compatible, not evidence of unrestricted walk-in access. Current contact variants exist on operator pages; link the current operator instruction rather than duplicating a possibly stale email. The postwar villa must not be presented as the original standing castle.
- Breivelde: municipal park page mentions horeca, while a municipal 2026 announcement concerns a concession starting 1 November. Do not infer that a restaurant will be open on the reader's chosen day; the selection promises park exploration only.
- Herita and some operator pages rejected full extraction (403/502/429 on initial requests). Current indexed official information and accessible official alternatives were used only for the scoped claims. No unknown daily schedule or full wheelchair route was guessed.

## Entity model / internal ownership

Named castle/site -> confirmed locality -> East Flanders -> Belgium. Keep building/park/interior as separate relations. No unverified architect, artwork, rating, Wikidata ID, travel duration or coordinate. The main page owns regional selection, while individual /kasteel/ routes own deep entity histories. West-Vlaanderen owns a different province and must not be duplicated with renamed entities; reuse only UI components, not its article outline or text.

No GSC, logs, backlink data, exact search volumes, user interviews or Google-specific SERP-feature export were supplied. These limit performance predictions and broad cannibalisation measurements, not the conditional factual selection.

## NEW_PAGE handoff

READY_FOR_BRIEF. The central evidence is sufficient for the bounded page. Unknown chosen-day openings, prices and current horeca are intentionally not asserted. Use one curated listing, then province-specific planning and access guidance; do not copy West-Vlaanderen's three access-mode sections. Preserve noindex and the existing rendering pipeline.
