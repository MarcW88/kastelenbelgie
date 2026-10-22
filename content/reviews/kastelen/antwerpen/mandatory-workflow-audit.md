# Antwerpen — audit final des étapes exécutables
Date : 2026-10-22
Route : /kastelen/antwerpen/
Mode : AUDIT → LIGHT_UPDATE → PUBLISH_REVIEW
Conclusion : contenu corrigé ; indexation inchangée.

## Analyse — étapes effectuées
| Agent | État | Travail concret |
|---|---|---|
| museum-analysis-workflow | PASS (analyse) | Conservation de la page de province ; sélection par visite réelle, pas classement générique |
| seo-content-audit | PASS | Valeur des six fiches conservée ; absence de GSC reconnue |
| content-refresh | PASS | Révision ciblée des passages répétitifs et des erreurs de libellés |
| seo-keyword | PASS qualitatif | Cluster « kastelen in Antwerpen bezoeken », variantes province/commune ; pas de volumes inventés |
| search-intent | PASS | Choisir un domaine visitable, des salles historiques ou un parc ; réponse dès l'introduction |
| information-architecture | PASS | URL régionale distincte des pages entité et des pages des autres provinces |
| seo-competitor | PARTIAL | Confrontation aux pages sources des opérateurs ; relevé exhaustif de positions SERP/backlinks non disponible |
| fact-check | PASS sur les points de visite publiés | Six sources primaires inspectées ; distinction ouverture intérieure/extérieur ; faits historiques du Sterckshof confirmés |
| JTBD | N/A | Besoin déjà explicite, pas de persona fictif |

## Rédaction et finition — passes indépendantes
| Agent | État | Résultat |
|---|---|---|
| content-brief-authoring | PASS | Brief déjà lié aux exigences principales |
| brand-voice | PASS | Néerlandais belge descriptif, sans superlatifs |
| content-and-copy | PASS | Chaque fiche expose l'intérêt spécifique et les limites pratiques |
| seo-aeo-geo | PASS | Faits atomiques, sources situées près des affirmations, réponses utiles ; pas de FAQ artificielle |
| internal-linking-audit | PASS de page | Breadcrumbs + Vlaanderen / Oost-Vlaanderen / Vlaams-Brabant ; audit du site entier hors périmètre |
| humanizer | PASS | Formulations identiques retirées, paragraphes non uniformisés au détriment des faits |
| general-writing | PASS | Descriptions et indications pratiques clarifiées ; parcours du visiteur mis en avant |
| anti-ai-slop | PASS éditorial | Contrôle du jargon, superlatifs, structure mécanique, fausse expérience, CTA répétitifs : aucun motif HIGH restant dans le texte ; cartes homogènes conservées pour l'UX |
| seo-onpage | PASS de source | Un H1, sections H2/H3 logiques, méta title et description dans manifest |
| seo-technical | PASS des contrôles natifs de build ; PARTIAL du terrain | Canonical, noindex, HTML de construction ; pas de CWV ni de crawl externe complet |
| seo-best-practices | PARTIAL | HTML statique, liens et hiérarchie examinés ; performance terrain non mesurée |
| editorial-qa | PASS éditorial | Faits sourcés, couverture des intentions, pas de faux témoignages ni promesses d'accès général |
| seo-drift | N/A | Aucune baseline performance disponible |

## Contrôle des sources (22 octobre 2026)
- Bornem, guidage et accessibilité : https://www.domeinvanbornem.be/bezoek/
- Hingene, exposition TALKING HEADS et park : https://www.kasteeldursel.be/index.php/nl/contact-en-bereikbaarheid ; https://www.kasteeldursel.be/index.php/nl/kalender/talking-heads-portretten-met-een-verhaal-1626-2026
- Oostmalle, rondleidingen : https://www.toerisme-malle.be/domein-de-renesse
- Meir, samedi 11–17 h : https://www.herita.be/nl/monumenten/paleis-op-de-meir/plan-je-bezoek
- Rivierenhof, restaurant : https://kasteel-rivierenhof.be/restaurant-deurne/
- Sterckshof, patrimoine et datation : https://inventaris.onroerenderfgoed.be/erfgoedobjecten/11279

## Délibérément différé — pas de faux PASS
- Playwright visuel desktop/mobile et inspection des captures. Aucune preuve récente du rendu.
- SERP top 10, données GSC, backlinks et mesures Core Web Vitals.
- Contrôle navigateur des liens externes et capture de leur statut à travers un crawler autonome.

## PUBLISH_REVIEW
Editorialement, les MUST de choix et de conditions de visite sont couverts. L'approbation visuelle n'est pas fournie : FAIL — KEEP_NOINDEX pour publication/indexation. Ne jamais retirer noindex sans demande et validation explicites.
