# paleis-op-de-meir — post-write gap check / PUBLISH_REVIEW
workflow_version: museum-v1
mode: NEW_PAGE
checked_at: 2026-10-23

| Etape obligatoire | Etat | Preuve / manque |
|---|---|---|
| AUDIT / NEW_PAGE ownership | COVERED | One entity /kasteel/paleis-op-de-meir/ versus regional /kastelen/antwerpen/ |
| seo-keyword + search-intent + JTBD | PARTIAL | content/research/kasteel/paleis-op-de-meir/serp-coverage.md ; primary and variants identified, volumes unknown |
| seo-competitor + live SERP matrix | BLOCKED | Official/heritage results inspected; independent top ten and SERP-feature matrix incomplete |
| Entity and source research | COVERED | Primary institutional source URL in body and research |
| fact-check and volatility ledger | PARTIAL | Named facts grounded in official page; not every historic claim independently corroborated, booking volatile |
| content-brief-authoring, brand-voice | COVERED | content/briefs/kasteel/paleis-op-de-meir.md, cultural voice |
| content-and-copy | DRAFT | content/kasteel/paleis-op-de-meir/body.html, individual structure and copy |
| seo-aeo-geo | PARTIAL | Clear answer to visit intent and source-linked factual language; extractibility requires editorial review |
| internal-linking-audit | PARTIAL | province/detail two-way links exist; other cluster links pending |
| humanizer | PARTIAL | Initial natural Belgian-Dutch prose; full original specialist review not independently certified |
| general-writing | PARTIAL | Initial editorial pass; detailed proof missing |
| anti-ai-slop | PARTIAL | Distinct claims, but repetitive H2 functions across new pages require review |
| seo-onpage / seo-technical / seo-best-practices | PENDING | CI build + title, canonical, noindex, CSS, route source verification |
| editorial-qa | BLOCKED | Research and separate specialist pass incomplete |
| Playwright desktop/mobile | PENDING | Run on latest commit |
| PUBLISH_REVIEW | FAIL — KEEP_NOINDEX | No certified research gate or human validation |

**Decision: FAIL — KEEP_NOINDEX.** The source is a public review draft, not complete workflow approval. Do not add unverified facts or remove robots noindex.

## Passes sur le contenu — 2026-10-23
- HUMANIZER: révision directe du corps HTML pour clarifier la décision du visiteur, supprimer les conclusions promotionnelles et expliciter les limites d'accès. Source: content/kasteel/paleis-op-de-meir/body.html, section `bezoekerskeuze`.
- GENERAL-WRITING: phrases orientées sur une question réelle de visite; la nouvelle section distingue les composantes du lieu et évite une affirmation d'expérience personnelle.
- ANTI-AI-SLOP: ajout d'une distinction patrimoniale/pratique vérifiable plutôt qu'une promesse vague; à revérifier pour la répétition éventuelle avec les sections existantes.
- FACT-CHECK: sources institutionnelles consignées dans `specialist-evidence.md`; conditions volatiles non garanties en temps réel.
- SEO/GEO: une entité par fiche, lien vers source officielle et choix depuis la page provinciale.
- PUBLISH_REVIEW: les résultats techniques ne suffisent pas à certifier la SERP complète et la validation humaine; `FAIL — KEEP_NOINDEX` inchangé.
