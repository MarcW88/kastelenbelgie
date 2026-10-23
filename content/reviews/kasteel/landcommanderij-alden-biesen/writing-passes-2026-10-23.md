# Passes éditoriales séparées — landcommanderij-alden-biesen
Date: 2026-10-23

## 1. humanizer (après factualité)
Article complet lu, titres et lead inclus. Genre: fiche culturelle et aide à la visite. Sous-passes better-usage, academic-voice (précision sans registre académique), writing-cadence et non-autoregressive-writing-pass appliquées.

- Avant: `De omvang van het domein kan de indruk geven dat één toegang overal geldt. `
  Après: `[suppression de la phrase sans information propre]`
- Avant: `Dat is een belangrijke uitzondering op de eenvoudige voorstelling van Alden Biesen als een volledig gratis domein.`
  Après: `Voor de Franse tuinen bepaalt de museumkalender dus of je een ticket nodig hebt.`
- Avant: `Dat netwerk verklaart de schaal van het geheel beter dan het beeld van één familie die een groot kasteel bewoonde.`
  Après: `De gebouwen dienden daarmee een regionaal bestuur, naast het verblijf van de landcommandeur.`
- Avant: `Die wintergrens ontbreekt vaak in korte bezoekerssamenvattingen. `
  Après: `[suppression de la phrase sans information propre]`

Contrôle de préservation: dates, personnes, conditions d’accès et liens conservés; les phrases retirées répétaient une distinction ou un jugement, sans fait propre perdu. Les contrastes qui bornent réellement l’accès restent en place.

## 2. general-writing (sur la version humanizer)
Passe minimale de clarté et néerlandais: syntaxe, sujets/verbes, précision et titres relus séparément. La passe broad humanizer précédente n’a pas été simulée une deuxième fois.

- Avant: `Wat een landcommanderij bestuurde`
  Après: `Het bestuurscentrum van de balije Biesen`
- Avant: `Voor de periode tot en met 7 maart 2027 gelden dinsdag tot zondag van 10 tot 17 uur`
  Après: `Tot en met 7 maart 2027 is het museum open van dinsdag tot zondag van 10 tot 17 uur`

Évaluation references/eval.md: sens et voix préservés; détails factuels comparés à la version fact-check; phrases utiles, acteurs clairs, pas de superlatif ou d’abstraction sans contenu; séries réservées aux ensembles utiles; titres, débuts/fins de paragraphes et transitions relus. Pas de voix personnelle ou de faux vécu ajouté. Format HTML et liens conservés. Les éléments non applicables (abstract académique, README, détection d’auteur) ne sont pas certifiés comme tests exécutés.

## 3. anti-ai-slop (review après general-writing, puis remédiation)
Contrat: informer sur ce château et rendre un choix de visite fiable, nl-BE. Protocoles review_workflow/output_design_review_gate, dimensions writing_information/localization_register appliqués.

P2 — Fin de fiche trop systématiquement orientée vers une autre sélection. Signal visible dans le cluster: les 12 fins ajoutaient une comparaison ou un renvoi à la province après avoir déjà résolu la visite. Un lien dans le fil est utile seulement s’il répond à une vraie suite; le renvoi provincial reste disponible dans le fil d’Ariane.

- Preuve: `Voor andere daadwerkelijk aangeboden bezoeken kun je de <a href="/kastelen/limburg/">Limburgse kastelenselectie</a> vergelijken.`
  Correction: `[suppression du renvoi ou du résumé sans valeur propre]`

Re-review: architecture et titres comparés aux 11 fiches; le sujet et la preuve organisent la progression, pas les anciens labels identiques. Les composants de page et la date commune sont fonctionnels, pas des défauts de style. Les phrases de restriction nécessaires à la visite ne sont pas supprimées pour varier artificiellement. Pas de superlatifs ni faux vécu; aucun signal HIGH restant. Confiance élevée sur cette observation éditoriale; aucune conclusion sur l’auteur ou une probabilité IA.
