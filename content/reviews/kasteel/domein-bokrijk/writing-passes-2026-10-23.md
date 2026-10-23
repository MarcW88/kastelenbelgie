# Passes éditoriales séparées — domein-bokrijk
Date: 2026-10-23

## 1. humanizer (après factualité)
Article complet lu, titres et lead inclus. Genre: fiche culturelle et aide à la visite. Sous-passes better-usage, academic-voice (précision sans registre académique), writing-cadence et non-autoregressive-writing-pass appliquées.

- Avant: `Het gebouw is daarmee een werk- en ontmoetingsplek, verbonden met de vraag hoe historische kennis en materialen in hedendaags ontwerp kunnen worden gebruikt.`
  Après: `Ontwerpers en makers werken er rond het gebruik van historische kennis en materialen in hedendaags ontwerp.`
- Avant: `Dat zijn concrete voorbeelden van een hedendaagse ingreep in een historisch huis. Ze zijn geen reconstructie van een adellijk interieur uit één periode.`
  Après: `Deze objecten zijn hedendaagse ontwerpen voor het historische huis, geen reconstructie van een vroegere inrichting.`
- Avant: `Dat is geen rondgang van salon naar salon in het kasteel. `
  Après: `[suppression de la phrase sans information propre]`
- Avant: `Dat zijn afzonderlijke tijdvensters. Een open speeltuin in de winter betekent dus niet dat ook het Openluchtmuseum in zijn gewone seizoen draait.`
  Après: `De winteropening van de speeltuin loopt dus los van het museumseizoen.`

Contrôle de préservation: dates, personnes, conditions d’accès et liens conservés; les phrases retirées répétaient une distinction ou un jugement, sans fait propre perdu. Les contrastes qui bornent réellement l’accès restent en place.

## 2. general-writing (sur la version humanizer)
Passe minimale de clarté et néerlandais: syntaxe, sujets/verbes, précision et titres relus séparément. La passe broad humanizer précédente n’a pas été simulée une deuxième fois.

- Avant: `Volgens de op 23 oktober 2026 geraadpleegde <a href=`
  Après: `Volgens de <a href=`
- Avant: `officiële openingstijden</a> loopt het museumseizoen`
  Après: `officiële openingstijden</a>, nagekeken op 23 oktober 2026, loopt het museumseizoen`
- Avant: `De winteropening van de speeltuin loopt dus los van het museumseizoen.`
  Après: `De speeltuin blijft dus ook buiten het gewone museumseizoen open.`

Évaluation references/eval.md: sens et voix préservés; détails factuels comparés à la version fact-check; phrases utiles, acteurs clairs, pas de superlatif ou d’abstraction sans contenu; séries réservées aux ensembles utiles; titres, débuts/fins de paragraphes et transitions relus. Pas de voix personnelle ou de faux vécu ajouté. Format HTML et liens conservés. Les éléments non applicables (abstract académique, README, détection d’auteur) ne sont pas certifiés comme tests exécutés.

## 3. anti-ai-slop (review après general-writing, puis remédiation)
Contrat: informer sur ce château et rendre un choix de visite fiable, nl-BE. Protocoles review_workflow/output_design_review_gate, dimensions writing_information/localization_register appliqués.

P2 — Fin de fiche trop systématiquement orientée vers une autre sélection. Signal visible dans le cluster: les 12 fins ajoutaient une comparaison ou un renvoi à la province après avoir déjà résolu la visite. Un lien dans le fil est utile seulement s’il répond à une vraie suite; le renvoi provincial reste disponible dans le fil d’Ariane.

- Preuve: `Wie een waterburcht met een expliciet museumverhaal zoekt, kan <a href="/kasteel/landcommanderij-alden-biesen/">Alden Biesen</a> vergelijken; de <a href="/kastelen/limburg/">Limburgse selectie</a> toont het verschil met andere kasteeldomeinen.`
  Correction: `[suppression du renvoi ou du résumé sans valeur propre]`

Re-review: architecture et titres comparés aux 11 fiches; le sujet et la preuve organisent la progression, pas les anciens labels identiques. Les composants de page et la date commune sont fonctionnels, pas des défauts de style. Les phrases de restriction nécessaires à la visite ne sont pas supprimées pour varier artificiellement. Pas de superlatifs ni faux vécu; aucun signal HIGH restant. Confiance élevée sur cette observation éditoriale; aucune conclusion sur l’auteur ou une probabilité IA.

## 4. Retour depuis le rendu / correction et re-review
FAIL initial mobile 390 px: le H2 `Het Openluchtmuseum vertelt een ander verhaal` débordait à cause d’un mot composé long. Correction éditoriale: `Het museum naast het kasteel`. Aucune règle CSS ou workflow modifiée. Le sens de la section et sa couverture restent identiques; titre repassé par clarté, anti-slop et SEO. Nouvelle capture et mesure requises après rebuild.
