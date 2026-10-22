# Antwerpen — SERP / coverage audit
workflow_version: museum-v1
mode: AUDIT → LIGHT_UPDATE
owner: REGION
locale: nl-BE
checked_at: 2026-10-22
decision: LIGHT_UPDATE (preserve differentiated approved blocks; add Kempen coverage and correct source URL)

## Search intent and ownership
Primary cluster: kastelen Antwerpen bezoeken, kastelen provincie Antwerpen.
Secondary: kasteel bezoeken Antwerpen, Kasteel Bornem, Kasteel d'Ursel, Kasteel de Renesse, Paleis op de Meir, kastelen Rivierenhof.
Task: choose a site by historic interest, province area and actual access (guided visit, exhibition, individual opening, park only). This geographic hub owns provincial choice and visit conditions, not ranking /inspiratie/mooiste-kastelen-vlaanderen/ and not individual /kasteel/ entity pages.

## Evidence inspected and coverage
| Need | Priority | Status | Verified evidence | Distinctive contribution |
|---|---|---|---|---|
| Bornem guided interior and coach museum | MUST | COVERED | https://www.domeinvanbornem.be/bezoek/ | Guided castle/garden versus independent experience centre, season and accessibility |
| d'Ursel temporary exhibition / castle park | MUST | COVERED | https://www.kasteeldursel.be/kalender ; https://www.kasteeldursel.be/index.php/nl/contact-en-bereikbaarheid | 2026 exhibition through 2 November, event-only castle and public park |
| Paleis op de Meir individual visits | MUST | COVERED | https://www.herita.be/nl/monumenten/paleis-op-de-meir/plan-je-bezoek | Saturday visit from 11 July to 7 November 2026 (exceptions) |
| De Renesse Kempen castle and freely accessible domain | MUST | COVERED | https://www.malle.be/activiteiten/detail/80/domein-de-renesse ; https://www.kempen.be/index.php/nl/beleven-overzicht/domein-de-renesse | Kasteel tour versus public landscaped domain |
| Rivierenhof and Sterckshof different heritage entities | SHOULD | COVERED | https://www.provincieantwerpen.be/ ; https://inventaris.onroerenderfgoed.be/aanduidingsobjecten/5847 | Restaurant castle vs heritage landmark without guaranteed interior access |
| Opening and reservation caveats | MUST | COVERED | Operator links above, inspected 22 October 2026 | No promise that whole castle is open whenever the park is |
| Current full SERP benchmark and features | SHOULD | PARTIAL | Search-based discovery, not a systematic captured top-10 SERP | No invented ranks, PAA or search volumes |
| Browser view and interaction proof | MUST for visual PASS | MISSING | No Playwright capture yet | Cannot claim visual PASS |

## Competing patterns
Official operator pages own actual access and calendars; tourism/heritage overview pages typically group by geography or heritage type. https://www.vlaanderen.be/publicaties/bezoek-de-mooiste-kastelen-van-vlaanderen (2022) is contextual discovery, not valid proof of 2026 visiting conditions. Actual result-by-result SERP ranking, snippets and features not captured: DATA_GAP.

## Novelty and overlap
The route combines six verified site types, distinguishes guided interior / temporary exhibition / event visits / park-only, and navigates province subareas. Neighbor provincial pages target other places. The theme/ranking route must not inherit the same visitor facts as its central purpose.

## Freshness and accuracy
STABLE: architectural histories and locations, sourced to heritage/official operators.
SEMI_STABLE: whether restaurant, tour, park or interior accessible in principle.
VOLATILE: events, opening calendars, tickets, pricing, reservation and exhibitions — verify at operator before trip.
Sources were inspected 2026-10-22. No fabricated travel-time, prices, accessibility or first-person experience.

## Gate
Editorial research supports a focused improvement but not an unqualified final PASS: full live SERP grid and browser-based visual validation remain outstanding. Keep noindex.
