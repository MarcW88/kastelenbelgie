# Antwerpen — vérification du workflow canonique
Date : 2026-10-22
URL : /kastelen/antwerpen/
Décision actuelle : FAIL — KEEP_NOINDEX

## Audit et recherche
| Skill | Résultat | Preuve / limite |
|---|---|---|
| museum-analysis-workflow / AUDIT | EXECUTED | Page existante; décision LIGHT_UPDATE; même intention provinciale que West/Oost, six options différenciées |
| seo-content-audit | EXECUTED | Pas de changement d'URL; valeur conservée (six sites, conditions), données GSC absentes |
| content-refresh | EXECUTED | Labels trompeurs et formulation répétitive corrigés, pas de rewrite intégral |
| seo-keyword | PARTIAL | Groupe intentionnel « kastelen provincie Antwerpen bezoeken », variantes locales, pas de volumes GSC |
| search-intent | EXECUTED | Trouver un château par type de visite, pas liste exhaustive |
| information-architecture | EXECUTED | Parent /kastelen/vlaanderen/, pages provinciales sœurs distinctes |
| seo-competitor | PARTIAL | Sources officielles de six entités vérifiées; SERP top 10 et outils backlinks indisponibles |
| fact-check | PARTIAL | Sources primaires Bornem, d'Ursel, Herita, Toerisme Malle, Kasteel Rivierenhof, Inventaris Onroerend Erfgoed; pas de contrôle indépendant de chaque proposition secondaire |
| JTBD | NOT_REQUIRED | But du visiteur clair : visite intérieure guidée vs calendrier événementiel vs balade |

## Production et qualité éditoriale
| Skill | Résultat | Preuve / limite |
|---|---|---|
| museum-content-workflow | EXECUTED PARTIALLY | Brief et post-write présents, publication non validée |
| content-brief-authoring | EXECUTED | content/briefs/kastelen/antwerpen.md |
| brand-voice | EXECUTED | nl-BE descriptif; pas de superlatifs non étayés |
| content-and-copy | EXECUTED | Corrections ciblées du body.html sur base des conditions de visite |
| seo-aeo-geo | EXECUTED | Distinction explicite kasteelinterieur, wandelpark, event, restaurant; sources dans chaque carte |
| internal-linking-audit | PARTIAL | Navigation et routes sœurs vérifiées en source; crawl complet non effectué |
| humanizer | EXECUTED | Suppression du label cloné « Voor je bezoek » sur les six fiches |
| general-writing | EXECUTED | Corrections de précision et des termes de réservation |
| anti-ai-slop | PARTIAL | Labels mécaniques et contradictions de l'ancienne passe corrigés; audit de l'ensemble du pack non lancé |
| seo-onpage | EXECUTED | H1, sections H2/H3, titre/description dans manifest |
| seo-technical | PARTIAL | Génération statique et canonical prévus par scripts; pas de test crawler/field |
| seo-best-practices | PARTIAL | Structure HTML inspectée; métriques CWV non recueillies |
| editorial-qa | PARTIAL | Utilité et transparence revues; audit visuel et validation de toute la factualité incomplets |
| seo-drift | NOT_APPLICABLE | Pas de baseline fiable |

## Sources officielles vérifiées le 22/10/2026
- Bornem (visite guidée, accessibilité): https://www.domeinvanbornem.be/bezoek/
- d'Ursel (exposition jusqu'au 02/11/2026): https://www.kasteeldursel.be/kalender
- Meir (samedi de juillet à novembre 2026): https://www.herita.be/nl/monumenten/paleis-op-de-meir/plan-je-bezoek
- De Renesse (intérieur avec guide, de avril à octobre): https://www.toerisme-malle.be/domein-de-renesse
- Rivierenhof restaurant: https://kasteel-rivierenhof.be/contact/
- Sterckshof inventaire patrimonial: https://inventaris.onroerenderfgoed.be/aanduidingsobjecten/5847

## Gate
Existing repository GitHub Actions run `verify_museum_agents.py`, `npm run build` and `npm run check`; passing them does not certify browser appearance. Browser Playwright was attempted separately before an unrequested temporary workflow was removed. No final valid desktop/mobile screenshot and no completed specialist exhaustive audit are currently available. Publishing condition: FAIL — KEEP_NOINDEX. Do not remove noindex or describe this document as a complete PASS.
