# SERP coverage matrix: kastelen/west-vlaanderen

Workflow version: museum-v1
Mode: NEW_PAGE (existing URL contains only an editorial placeholder)
Market: Belgium / nl-BE
Research date: 2026-10-22
Source commit inspected: 81542f042cf0f9ebf81a986f8d7ac842c02ea16c

## Ownership and intent

REGION: select and plan visits to castle sites in West Flanders. Primary query: kastelen West-Vlaanderen. Supporting queries: kastelen West-Vlaanderen bezoeken, bezoekbare kastelen West-Vlaanderen, kasteelpark West-Vlaanderen, kastelen rond Brugge. Dominant intent: informational discovery with visit-planning constraints, not a product ranking or an exhaustive monument inventory.

The requested outcome is a usable block/listing of accessible castles plus relevant explanatory copy. Distinguish regular interior visits, group-only interior visits and public parks around buildings not open for free interior visits. A park being public says nothing about wheelchair access or the castle interior.

Scope excludes hotels/wedding venues unless a separate documented visit exists; no private sites presented as freely open. No new castle fiche URLs or other province content are created here.

## Actual search evidence

Research used web search on both available engines and inspection of current results on 22 October 2026. Queries included the primary cluster and official-site queries for each access condition. These are qualitative discovery observations, not a reproducible Google Belgium rank export, GSC data or search-volume measurements.

| Inspected result | Page type and observations | Coverage opportunity |
|---|---|---|
| https://kasteelatlas.nl/provincie/west-vlaanderen/kastelen-in-west-vlaanderen | Province directory; 105 named locations, map/list, individual detail links. Listing itself does not distinguish visits to the interior and park access. | Curate documented visit options and show the access condition directly in each block. Do not compete by inventing an exhaustive count. |
| https://www.visitflanders.com/nl/ontdek-vlaanderen/kunst-en-erfgoed/kastelen-en-tuinen-buiten-de-stadsmuren/brugge-en-het-brugse | Official tourism editorial selection; Loppem interiors, Kasteelbossen, Tudor outside/park, links to operators and transport information. | Cover a province-wide selection including Veurne, Rumbeke, Torhout and Diksmuide, not only Bruges; make group restrictions scannable. |
| https://www.visitroeselare.be/nl/zien-en-doen/cultuur-en-erfgoed/monumenten-en-gebouwen/kasteel-van-rumbeke | Official local detail page; explicit group booking, park, visit access limit. | Use as a primary source for one listing, link to booking rather than reproducing unstable tariffs. |
| https://www.uitinvlaanderen.be/tip/kastelen-voor-kinderen-in-west-vlaanderen | Family-oriented result discovered; published years ago. Full fetch returned 405. | Discovery signal only, not factual proof or a fully inspected competitor. |

Search results surfaced maps/directories, destination editorials and visit-condition pages. No verified Google PAA, featured-snippet or AI Overview ownership dataset was available; no such feature or ranking is claimed.

## Needs / coverage matrix before writing

| Requirement | Existing page | Priority | Evidence / information gain |
|---|---|---|---|
| Answer which sites can actually be visited | MISSING | MUST | Eight selected sites with documented modes of access; no claim to list every castle. |
| Identify municipality/province | MISSING | MUST | Official operator/local tourism information; no East Flanders or Wallonia spillover. |
| Distinguish inside, group and park access | MISSING | MUST | Operator/official public sources; restriction next to each name. |
| Show reservation/season limits without claiming open now | MISSING | MUST | Date-stamped checks, official calendar links, group conditions; no live badges. |
| Explain why the sites differ | MISSING | MUST | Neogothic interiors, Beauvoorde's restored historic setting, Renaissance group visit, nature-centre uses and park-only options. |
| Give links to official practical information | MISSING | MUST | Source next to each block; current prices/hours delegated to operator. |
| Warn about Wijnendale's changed visit model | MISSING | MUST if included | Museum and free domain access closed, yet booked group arrangements remain available; minimum tariff basis 40 people, including smaller groups. |
| Offer a concise way to choose by interest | MISSING | SHOULD | Interiors vs outside walk, individual vs organised group. |
| Avoid implying wheelchair access from bezoekbaar | MISSING | MUST | Explicit distinction and Rumbeke's documented restriction. |
| Integrate a rebuild-persistent content source | MISSING | MUST | Native build currently overwrites all detail pages with placeholders; add scoped reviewed-page loading. |
| Add relevant internal navigation | PARTIAL (breadcrumb/footer only) | SHOULD | Parent province directory can be linked; do not send users to unfilled castle fiches. |
| Original location photographs | MISSING | OPTIONAL | No licensed media inventory supplied; no invented or AI-generated castle photos. |

## Candidate decision and sources

| Site | Municipality | Confirmed usable access | Primary evidence |
|---|---|---|---|
| Kasteel van Loppem | Loppem, Zedelgem | Interior according to seasonal calendar; park, maze managed separately | https://www.kasteelvanloppem.be/nl and https://www.kasteelvanloppem.be/nl/bezoek |
| Kasteel Beauvoorde | Wulveringem, Veurne | Restored castle reopened April 2026; tickets with dates/time slots | https://www.herita.be/nl/monumenten/kasteel-beauvoorde/plan-je-bezoek and https://herita.odoo.com/event/bezoek-kasteel-beauvoorde-14/register |
| Kasteel van Rumbeke | Rumbeke, Roeselare | Group booking for interior; Sterrebos walking; castle visit not wheelchair accessible | https://www.visitroeselare.be/nl/zien-en-doen/cultuur-en-erfgoed/monumenten-en-gebouwen/kasteel-van-rumbeke |
| Kasteel Wijnendale | Torhout | No regular museum/free domain entry; booked group arrangements with minimum tariff based on 40 participants, also for smaller groups | https://www.visittorhout.be/kasteel-van-wijnendale |
| Kasteel Tillegem | Sint-Michiels, Brugge | Public provincial forest/park; office building not freely visitable inside | https://www.west-vlaanderen.be/domeinen/tillegembos and https://www.west-vlaanderen.be/vrije-tijd-toerisme/provinciedomeinen-en-bezoekerscentra/tillegembos/geschiedenis-van-het |
| Kasteel Tudor | Sint-Andries, Brugge | Public gardens/woodland/herb garden; privately used castle, no regular interior visit promised | https://www.brugge.be/vrije-tijd/natuur/kasteel-kruidentuin-tudor |
| Kasteel Beisbroek | Sint-Andries, Brugge | Public domain and nature centre; nature/astronomy use rather than a historic-room tour | https://www.brugge.be/vrije-tijd/natuur/bezoek-domein-beisbroek and https://www.brugge.be/vrije-tijd/natuur/natuurcentrum-beisbroek |
| Kasteel De Blankaart | Woumen, Diksmuide | Park/nature, visitor centre information; no historical castle-interior tour promised | https://www.bezoekdiksmuide.be/de-blankaart |

Excluded from this first selection: private castles without confirmed visitor access; hotels/event properties without a separate public visit; Wallemote/Wolvenhof not needed to establish the page's scope. This is an editorial selection, not a census or a claim of superiority.

## Entity / provenance model

Every included object is a castle or castle site, located in its confirmed municipality in West-Vlaanderen, Belgium. No unverified architect, date, person, collection, artwork or Wikidata ID is added. Beauvoorde's Arthur Merghelynck association is directly documented by its operator. Garden access and interior access are separate predicates. Schema uses CollectionPage/ItemList/Place, not Review, rating, Product or invented hours.

## Freshness and conflicts

Access, booking and tariffs are VOLATILE; park/interior function is checked as at least SEMI_STABLE, elevated when it changes the decision. Historical style is STABLE but still supported. Check date is 2026-10-22, not a promise of real-time availability.

- Beauvoorde: old tourism/event pages still mention restoration closure. New Herita 2026 reopening announcement, current visit page and dated operator booking slots establish reopening. Use the current operator; do not propagate old closure text.
- Wijnendale: snippets saying the museum is closed omit the full official page's group arrangements. Preserve both facts; do not label freely open or absolutely unvisitable.
- Blankaart: a past news item planned a move of the visitor centre; current official local tourism still describes the centre in the castle. The piece promises the verified park/nature visit, not a historic-room tour or an unverified floorplan.
- Herita/provincial pages sometimes returned 403 to direct extraction. Current indexed official text was read and cross-checked with accessible operator booking/local tourism pages. No exact daily hours, prices, path accessibility or live availability are inferred from blocked pages.
- Weather, storms and maintenance can restrict outdoor access; recommend checking the operator before departure. Do not publish an unverified route distance or travel time.

## Internal overlap / preservation

The existing target URL and its HTML were read locally and live; it has only placeholders. Preserve URL, noindex, header/footer/navigation and design tokens. Parent /kastelen/ provides a province directory; /kastelen/vlaanderen/ is a broader regional placeholder. /bezoeken/kastelen-met-kinderen/ and /bezoeken/kastelen-met-tuin/ own use-case selection; /kasteel/<slug>/ owns detailed entity history. Do not create near-duplicate pages for individual query variants. Real cannibalisation/performance signals are unavailable (no GSC/backlink/log export).

## NEW_PAGE handoff

READY_FOR_BRIEF. All central facts needed for the bounded selection have source evidence; unknown exact daily availability/prices are intentionally not asserted. No blocking entity/ownership conflict remains. Missing analytics, actual user interviews/card sorts and Google-specific rank/feature data limit performance predictions, not the ability to produce this scoped visit guide. No traffic or ranking outcome is promised.
