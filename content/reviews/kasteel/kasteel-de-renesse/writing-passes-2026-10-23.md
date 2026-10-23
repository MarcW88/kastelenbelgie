# Passes éditoriales séparées — kasteel-de-renesse
Date: 2026-10-23

## 1. humanizer (après factualité)
Article complet lu, titres et lead inclus. Genre: fiche culturelle et aide à la visite. Sous-passes better-usage, academic-voice (précision sans registre académique), writing-cadence et non-autoregressive-writing-pass appliquées.

- Avant: `De ongelijke bouwdelen zijn daardoor een aanknopingspunt om de geschiedenis te begrijpen, niet zomaar een onregelmatigheid in een verder afgewerkt plan.`
  Après: `De ongelijke bouwdelen laten zo ook zien waar de verbouwing onafgewerkt bleef.`
- Avant: `De site combineert erfgoedbehoud daardoor met gebruik door verenigingen en bezoekers.`
  Après: `[suppression de la phrase sans information propre]`
- Avant: `Die cijfers zijn geen betrouwbare basis om je traject op de minuut te plannen; kies de route op de actuele kaart bij het vertrekpunt.`
  Après: `Kies daarom de route op de actuele kaart bij het vertrekpunt.`

Contrôle de préservation: dates, personnes, conditions d’accès et liens conservés; les phrases retirées répétaient une distinction ou un jugement, sans fait propre perdu. Les contrastes qui bornent réellement l’accès restent en place.

## 2. general-writing (sur la version humanizer)
Passe minimale de clarté et néerlandais: syntaxe, sujets/verbes, précision et titres relus séparément. La passe broad humanizer précédente n’a pas été simulée une deuxième fois.

- Avant: `Je kunt dus bij een cafébezoek wél in een deel van het kasteel komen`
  Après: `Bij een cafébezoek kom je dus in een deel van het kasteel`
- Avant: `in de winter een vroegere sluiting op maandag om 17 uur`
  Après: `in de winter op maandag sluiting om 17 uur`

Évaluation references/eval.md: sens et voix préservés; détails factuels comparés à la version fact-check; phrases utiles, acteurs clairs, pas de superlatif ou d’abstraction sans contenu; séries réservées aux ensembles utiles; titres, débuts/fins de paragraphes et transitions relus. Pas de voix personnelle ou de faux vécu ajouté. Format HTML et liens conservés. Les éléments non applicables (abstract académique, README, détection d’auteur) ne sont pas certifiés comme tests exécutés.

## 3. anti-ai-slop (review après general-writing, puis remédiation)
Contrat: informer sur ce château et rendre un choix de visite fiable, nl-BE. Protocoles review_workflow/output_design_review_gate, dimensions writing_information/localization_register appliqués.

P2 — Fin de fiche trop systématiquement orientée vers une autre sélection. Signal visible dans le cluster: les 12 fins ajoutaient une comparaison ou un renvoi à la province après avoir déjà résolu la visite. Un lien dans le fil est utile seulement s’il répond à une vraie suite; le renvoi provincial reste disponible dans le fil d’Ariane.

- Preuve: `Voor een ander park met twee duidelijk verschillende kasteelgebouwen biedt het <a href="/kasteel/kasteel-rivierenhof/">Rivierenhof in Deurne</a> een vergelijking. Andere bezoekvormen vind je in de <a href="/kastelen/antwerpen/">provincieselectie Antwerpen</a>.`
  Correction: `[suppression du renvoi ou du résumé sans valeur propre]`

Re-review: architecture et titres comparés aux 11 fiches; le sujet et la preuve organisent la progression, pas les anciens labels identiques. Les composants de page et la date commune sont fonctionnels, pas des défauts de style. Les phrases de restriction nécessaires à la visite ne sont pas supprimées pour varier artificiellement. Pas de superlatifs ni faux vécu; aucun signal HIGH restant. Confiance élevée sur cette observation éditoriale; aucune conclusion sur l’auteur ou une probabilité IA.

## 4. Séparation des accès après vérification CI
Le check historique check-antwerpen.mjs échouait sur son quota de quatre H2, qui n’est pas une preuve de qualité et n’a pas été modifié. Relecture de la longue section finale: elle traitait deux tâches réellement différentes. Les conditions de visite guidée sont maintenant séparées du café qui utilise la Ridderzaal et de son usage familial. Nouveaux titres: `Met een gids door de historische vertrekken` et `Een café in de Ridderzaal`. Pas de remplissage ajouté. Les mêmes faits et restrictions ont été relus après déplacement; nouveau rendu requis.
