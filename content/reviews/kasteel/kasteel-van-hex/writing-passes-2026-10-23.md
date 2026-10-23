# Passes éditoriales séparées — kasteel-van-hex
Date: 2026-10-23

## 1. humanizer (après factualité)
Article complet lu, titres et lead inclus. Genre: fiche culturelle et aide à la visite. Sous-passes better-usage, academic-voice (précision sans registre académique), writing-cadence et non-autoregressive-writing-pass appliquées.

- Avant: `Bij het kijken naar die ruimte is vooral het verband tussen reliëf en zichtassen interessant: de bebouwing staat niet los van het landschap eromheen.`
  Après: `Het reliëf en de zichtassen bepalen zo mee het zicht op het kasteel.`
- Avant: `Een rechte as en een landschappelijke vallei zijn hier dus geen tegenstrijdigheid, maar onderdelen uit verschillende ontwerpfasen.`
  Après: `De rechte assen en de landschappelijke vallei horen bij die verschillende ontwerpfasen.`
- Avant: `Dat biedt verschillende redenen voor een bezoek: je kunt voor planten komen, maar ook om de historische aanleg te lezen. Een festival in juni geeft een ander seizoensbeeld dan een openstelling in september. De concrete bloei van een bepaalde roos wordt hier niet voorspeld.`
  Après: `Een tuinwandeling kan daardoor zowel over de plantencollectie als over de aanleg gaan. Bekijk voor een gericht plantenbezoek het programma van de gekozen openstelling.`

Contrôle de préservation: dates, personnes, conditions d’accès et liens conservés; les phrases retirées répétaient une distinction ou un jugement, sans fait propre perdu. Les contrastes qui bornent réellement l’accès restent en place.

## 2. general-writing (sur la version humanizer)
Passe minimale de clarté et néerlandais: syntaxe, sujets/verbes, précision et titres relus séparément. La passe broad humanizer précédente n’a pas été simulée une deuxième fois.

- Avant: `Op de op 23 oktober 2026 geraadpleegde <a href=`
  Après: `Op de <a href=`
- Avant: `bezoekerspagina</a> staat een maximum van 35 personen`
  Après: `bezoekerspagina</a>, nagekeken op 23 oktober 2026, staat een maximum van 35 personen`
- Avant: `Voor een zelfstandige parkuitstap zonder groepsafspraak is Hex dus geen vanzelfsprekende keuze.`
  Après: `Voor een zelfstandige parkuitstap zonder afspraak kun je hier niet terecht.`

Évaluation references/eval.md: sens et voix préservés; détails factuels comparés à la version fact-check; phrases utiles, acteurs clairs, pas de superlatif ou d’abstraction sans contenu; séries réservées aux ensembles utiles; titres, débuts/fins de paragraphes et transitions relus. Pas de voix personnelle ou de faux vécu ajouté. Format HTML et liens conservés. Les éléments non applicables (abstract académique, README, détection d’auteur) ne sont pas certifiés comme tests exécutés.

## 3. anti-ai-slop (review après general-writing, puis remédiation)
Contrat: informer sur ce château et rendre un choix de visite fiable, nl-BE. Protocoles review_workflow/output_design_review_gate, dimensions writing_information/localization_register appliqués.

P2 — Fin de fiche trop systématiquement orientée vers une autre sélection. Signal visible dans le cluster: les 12 fins ajoutaient une comparaison ou un renvoi à la province après avoir déjà résolu la visite. Un lien dans le fil est utile seulement s’il répond à une vraie suite; le renvoi provincial reste disponible dans le fil d’Ariane.

- Preuve: `Wil je juist de restauratie van een gebouw zien, dan ligt ook <a href="/kasteel/kasteel-van-heers/">Kasteel van Heers</a> in dezelfde gemeente. De <a href="/kastelen/limburg/">Limburgse selectie</a> onderscheidt die bezoekvormen.`
  Correction: `[suppression du renvoi ou du résumé sans valeur propre]`

Re-review: architecture et titres comparés aux 11 fiches; le sujet et la preuve organisent la progression, pas les anciens labels identiques. Les composants de page et la date commune sont fonctionnels, pas des défauts de style. Les phrases de restriction nécessaires à la visite ne sont pas supprimées pour varier artificiellement. Pas de superlatifs ni faux vécu; aucun signal HIGH restant. Confiance élevée sur cette observation éditoriale; aucune conclusion sur l’auteur ou une probabilité IA.
