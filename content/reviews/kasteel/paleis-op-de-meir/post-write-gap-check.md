# Post-write gap check — /kasteel/paleis-op-de-meir/
Workflow version: museum-v1
Review date: 2026-10-23
Research artifact: content/research/kasteel/paleis-op-de-meir/serp-coverage.md
Brief: content/briefs/kasteel/paleis-op-de-meir.md
Draft/source: content/kasteel/paleis-op-de-meir/body.html
SHA-256 de l’article final: `fe0684922773fd4535cd204fd3961a409a701f486c509273066cc105ce74a00f`

## 1. Vérification contre les besoins initiaux
| Requirement | Priority | Final status | Where covered | Evidence/source preserved? | Notes |
|---|---|---|---|---|---|
| Van Susteren, Van Baurscheit, rococo et empire | MUST | COVERED | Een koopman bestelt een paleis | voir fact-check-2026-10-23.md et liens visibles | MISSING → réponse développée dans la version finale |
| Napoléon propriétaire mais jamais résident | MUST | COVERED | Napoleon liet het inrichten, maar verbleef er nooit | voir fact-check-2026-10-23.md et liens visibles | MISSING → réponse développée dans la version finale |
| Accès 2026 distinct des commerces et événements | MUST | COVERED | De paleiszalen bezoeken in het najaar van 2026 | voir fact-check-2026-10-23.md et liens visibles | COVERED → réponse développée dans la version finale |
| Restauration récente et mobilité | SHOULD | COVERED | De gevel werd opnieuw hersteld | voir fact-check-2026-10-23.md et liens visibles | PARTIAL → réponse développée dans la version finale |

## 2. Proposition de visite et entités
D’une commande de marchand aux intérieurs royaux: les changements de propriétaires se lisent dans le décor.
Donner des repères pour lire les styles et éviter le faux récit d’un Napoléon ayant habité ici.
Entité et lieu désambiguïsés: Paleis op de Meir, Antwerpen, Meir 50. Collection, architecture et usage actuel distingués. Pas de passage affirmant une visite personnelle. Aucun événement futur présenté comme déjà ouvert. Pas de fusion avec la fiche de province.

## 3. Factualité et fraîcheur
Le fact-check séparé est conservé dans `fact-check-2026-10-23.md`. Les affirmations de la version finale ont été relues après les passes de style, et non validées depuis le seul brief. Sources consultées le 23 octobre 2026. Faits STABLE: construction et histoire; SEMI_STABLE: usage/mobilité; VOLATILE: horaires, événements, réservations et travaux. Les conditions gardent leurs dates et portée.

## 4. Passes GEO / style / maillage
Réponse principale dans le lead, faits et liens de source proches, noms de lieux précis. Pas de FAQ ou d’accumulation d’entités créée pour les robots. Les phrases de l’article ont été modifiées via content-and-copy, puis humanizer, general-writing et anti-ai-slop dans cet ordre. Voir `writing-passes-2026-10-23.md` pour les extraits avant/après distincts.
Le maillage a été vérifié sur les HTML produits avec le script existant `scripts/internal_link_audit.py` en import: 12 sources lues, 8 candidats contextuels déjà présents, aucune action d’ajout requise. Les cibles réellement présentes sont aussi contrôlées par npm run check. Les renvois de fin répétitifs ont été supprimés; le fil d’Ariane vers la province est conservé.

## 5. SEO et lecture du rendu
Title et meta propres à cette fiche dans reviewed-pages.json; un H1; URL /kasteel/paleis-op-de-meir/ et canonical propres; langue nl-BE; JSON-LD WebPage + BreadcrumbList cohérent avec le contenu. Aucun schema Review, Museum ou classement d’avis inventé. robots noindex,follow inchangé.
Build/check: 89 HTML générés, 48 pages rédigées contrôlées. Reconstruction répétée: mêmes empreintes sur les 89 pages. Comparaison au build du HEAD d’origine: seules les 12 fiches demandées diffèrent. Les autres différences de fichiers HTML préexistantes entre sources et artefacts suivis ne sont pas publiées dans ce changement.
Rendu Playwright/Chromium 153 vérifié en 1440×1000 et 390×844: HTTP 200, texte du main identique à la source, aucun paragraphe caché et aucun débordement horizontal dans les deux rendus finaux. Captures pleine page réellement inspectées. Les champs du runner liés à .content-main (ancienne famille Guides) sont non applicables ici; ils ne sont pas utilisés pour valider les titres ou le contenu.
Limite de rendu: la requête Google Fonts échoue dans cet environnement (ERR_EMPTY_RESPONSE); les captures utilisent les polices de repli. Le chargement des polices externes et les CWV terrain ne sont donc pas certifiés. Aucune erreur JavaScript de page. La navigation mobile et le focus du lien d’évitement ont été exercés sur une fiche témoin.

## Synthèse des passes exécutées
| Skill | Résultat sur le texte final | Preuve |
|---|---|---|
| humanizer | PASS | extraits avant/après dans writing-passes-2026-10-23.md, passe 1 |
| general-writing | PASS | corrections distinctes dans writing-passes-2026-10-23.md, passe 2 |
| anti-ai-slop | PASS | détection, remédiation et re-review dans writing-passes-2026-10-23.md, passe 3 |
| seo-aeo-geo | PASS sur l’extractibilité du contenu | réponses directes, noms désambiguïsés, dates et sources; citations LLM non mesurées |
| seo-onpage | PASS sur le périmètre édité | metadata propre, H1, headings utiles, liens et WebPage/BreadcrumbList |
| seo-technical / seo-best-practices | PASS sur le build et le périmètre édité | source statique, canonical, robots et JSON-LD contrôlés; limites fontes/CWV ci-dessus |
| editorial-qa | PASS | intention, spécificité, factualité, naturel, préservation et utilité vérifiés ci-dessous |

## 6. Editorial QA / PUBLISH_REVIEW
Intent: réponse spécifique et utilisable. Original value: histoire contextualisée et distinction des accès. Factuality: preuves reliées et incertitudes bornées. Natural Dutch: syntaxe et rythme relus séparément. SEO preservation: noms, URL, canonical et indexation conservés. Usefulness: article utile sans affiliation. Images: aucune image générée nécessaire pour cette correction de texte; aucune représentation inventée du monument.
Architecture comparée aux onze autres fiches: les fonctions et les enchaînements sont motivés par le lieu (reconstruction, jardins, commanderie, séjour, chantier ou production), pas par les anciens blocs identiques. Les phrases génériques et fins systématiques ont été corrigées. Aucun MUST MISSING, claim central non vérifié présenté comme certain, ou signal HIGH anti-slop restant.

**PASS — READY_FOR_HUMAN_VALIDATION**

Cette décision est le résultat du mode PUBLISH_REVIEW sur la version finale, pas le résultat du contrôle d’intégrité des skills. La publication sur main est demandée explicitement dans cette tâche. Aucun changement d’indexation autorisé ou effectué.
