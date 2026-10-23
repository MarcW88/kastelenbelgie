# Passes éditoriales séparées — kasteelbrouwerij-ter-dolen
Date: 2026-10-23

## 1. humanizer (après factualité)
Article complet lu, titres et lead inclus. Genre: fiche culturelle et aide à la visite. Sous-passes better-usage, academic-voice (précision sans registre académique), writing-cadence et non-autoregressive-writing-pass appliquées.

- Avant: `Die onderbrekingen zijn belangrijk: de historische band met een abdij bewijst niet dat de huidige brouwerij al sinds de middeleeuwen onafgebroken bier produceert.`
  Après: `De huidige brouwerij begon veel later; uit de band met de abdij volgt geen ononderbroken brouwtraditie op deze plek.`
- Avant: `De productie werd ondergebracht in de voorgebouwen, niet in een fictief bewaard middeleeuws brouwparcours door de woonvertrekken.`
  Après: `De productie werd ondergebracht in de voorgebouwen van het kasteel.`
- Avant: `Tijdens een productiebezoek is juist dat onderscheid interessant: een bestaande plek kreeg een nieuwe economische functie.`
  Après: `De brouwerij gaf de voorgebouwen zo een nieuwe economische functie.`
- Avant: `Het bericht is onvoldoende om alle horeca of het hele domein gesloten te verklaren, maar te relevant om te negeren.`
  Après: `De melding gaat over groepsrondleidingen en bevestigt geen algemene sluiting van de horeca of het domein.`

Contrôle de préservation: dates, personnes, conditions d’accès et liens conservés; les phrases retirées répétaient une distinction ou un jugement, sans fait propre perdu. Les contrastes qui bornent réellement l’accès restent en place.

## 2. general-writing (sur la version humanizer)
Passe minimale de clarté et néerlandais: syntaxe, sujets/verbes, précision et titres relus séparément. La passe broad humanizer précédente n’a pas été simulée une deuxième fois.

- Avant: `Voor oktober tot december 2026 is er echter tegenstrijdige informatie over rondleidingen door werkzaamheden`
  Après: `Over rondleidingen tijdens werkzaamheden in oktober tot december 2026 is de informatie tegenstrijdig`
- Avant: `De beheerder geeft een duur van ongeveer 45 minuten`
  Après: `De beheerder vermeldt een duur van ongeveer 45 minuten`

Évaluation references/eval.md: sens et voix préservés; détails factuels comparés à la version fact-check; phrases utiles, acteurs clairs, pas de superlatif ou d’abstraction sans contenu; séries réservées aux ensembles utiles; titres, débuts/fins de paragraphes et transitions relus. Pas de voix personnelle ou de faux vécu ajouté. Format HTML et liens conservés. Les éléments non applicables (abstract académique, README, détection d’auteur) ne sont pas certifiés comme tests exécutés.

## 3. anti-ai-slop (review après general-writing, puis remédiation)
Contrat: informer sur ce château et rendre un choix de visite fiable, nl-BE. Protocoles review_workflow/output_design_review_gate, dimensions writing_information/localization_register appliqués.

P2 — Fin de fiche trop systématiquement orientée vers une autre sélection. Signal visible dans le cluster: les 12 fins ajoutaient une comparaison ou un renvoi à la province après avoir déjà résolu la visite. Un lien dans le fil est utile seulement s’il répond à une vraie suite; le renvoi provincial reste disponible dans le fil d’Ariane.

- Preuve: `Voor een andere Limburgse erfgoedbestemming, zonder dat productiebezoek als uitgangspunt, kun je de <a href="/kastelen/limburg/">kastelenselectie Limburg</a> bekijken.`
  Correction: `[suppression du renvoi ou du résumé sans valeur propre]`

Re-review: architecture et titres comparés aux 11 fiches; le sujet et la preuve organisent la progression, pas les anciens labels identiques. Les composants de page et la date commune sont fonctionnels, pas des défauts de style. Les phrases de restriction nécessaires à la visite ne sont pas supprimées pour varier artificiellement. Pas de superlatifs ni faux vécu; aucun signal HIGH restant. Confiance élevée sur cette observation éditoriale; aucune conclusion sur l’auteur ou une probabilité IA.

## 4. Retour depuis le rendu / correction et re-review
FAIL initial mobile 390 px: le H2 `Een brouwerijbezoek met kasteelgeschiedenis` débordait à cause d’un mot composé long. Correction éditoriale: `Een rondleiding langs de brouwerij`. Aucune règle CSS ou workflow modifiée. Le sens de la section et sa couverture restent identiques; titre repassé par clarté, anti-slop et SEO. Nouvelle capture et mesure requises après rebuild.
