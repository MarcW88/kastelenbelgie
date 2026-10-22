# Post-write gap check — <route>

Workflow version: museum-v1
Research artifact: <path to SERP coverage matrix>
Brief: <path to brief>
Draft/source: <path to source content>
Review date: YYYY-MM-DD

## 1. Coverage verification

Map every `MUST` and relevant `SHOULD` item from the pre-write matrix to the final page.

| Requirement | Priority | Final status | Where covered | Evidence/source preserved? | Notes |
|---|---|---|---|---|---|
| | MUST / SHOULD | COVERED / PARTIAL / MISSING | heading/paragraph | yes/no/n-a | |

## 2. Visit proposition verification

- The page makes clear why this museum/page is relevant for the chosen intent: yes/no
- The proposition relies on specific facts rather than generic praise: yes/no
- Important trade-offs or constraints are visible where they affect the decision: yes/no
- No fake first-person visit/test/observation is implied: yes/no

## 3. Entity verification

| Entity / relation | Final status | Source | Potential ambiguity resolved? | Notes |
|---|---|---|---|---|
| | CONFIRMED / REMOVED / PARTIAL | | yes/no | |

Specific checks:

- collection ownership was not confused with current display: yes/no/n-a
- temporary exhibitions have official dates/source: yes/no/n-a
- Wikidata/sameAs links are used for identity, not as a substitute for current practical information: yes/no/n-a

## 4. Freshness / factuality verification

| Claim | Freshness class | Source retained | Checked at | Final status |
|---|---|---|---|---|
| | STABLE / SEMI_STABLE / VOLATILE | | | CONFIRMED / PARTIAL / MISSING |

Any volatile central claim without a current source is a blocker.

## 5. GEO verification

- Direct answers are present where natural: yes/no
- Important facts are atomic and source-adjacent: yes/no
- Entity names are disambiguated where needed: yes/no
- Volatile claims show date/scope where useful: yes/no
- No manufactured FAQ/snippet blocks were added only for GEO: yes/no
- Information gain survived the style passes: yes/no

## 6. Voice / anti-slop / structure

- Brand voice applied: yes/no
- Humanizer run separately: yes/no
- General-writing pass run separately: yes/no
- Anti-ai-slop review run separately: yes/no
- Repeated museum template introduced: yes/no
- Generic praise without evidence remains: yes/no
- Intro/conclusion could be swapped with another museum by replacing names: yes/no

## 7. Internal linking / ownership

- Links answer the next logical reader need: yes/no
- No major intent overlap introduced with another URL: yes/no
- Route still respects its cluster ownership: yes/no

## Gate

Any unresolved `MUST = MISSING`, unsupported central claim, stale volatile evidence, ambiguous central entity/relation, unresolved cannibalisation or generic/non-specific visit proposition forces:

`FAIL — KEEP_NOINDEX`

`PARTIAL` on a MUST requires explicit rationale and cannot silently pass.
