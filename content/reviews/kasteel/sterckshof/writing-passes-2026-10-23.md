# Passes éditoriales séparées — sterckshof
Date: 2026-10-23

## 1. humanizer (après factualité)
Article complet lu, titres et lead inclus. Genre: fiche culturelle et aide à la visite. Sous-passes better-usage, academic-voice (précision sans registre académique), writing-cadence et non-autoregressive-writing-pass appliquées.

- Avant: `Het oude Zilvermuseum en het nieuwe project zijn niet hetzelfde`
  Après: `Geen museumticket op basis van de oude naam`
- Avant: `Die naam beschrijft een historische functie van het gebouw. `
  Après: `[suppression de la phrase sans information propre]`
- Avant: `De oude kern en de twintigste-eeuwse verbeelding van historische architectuur horen allebei bij de geschiedenis van het monument.`
  Après: `De huidige gebouwen combineren zo de oude kern met aanvullingen uit de twintigste eeuw.`
- Avant: `Het huidige uiterlijk als torenrijk kasteel mag niet eenvoudig op die zestiende-eeuwse toestand worden teruggeprojecteerd.`
  Après: `De torens en gevels die je nu ziet, tonen dus niet zonder meer de toestand van Stercks buitenverblijf.`

Contrôle de préservation: dates, personnes, conditions d’accès et liens conservés; les phrases retirées répétaient une distinction ou un jugement, sans fait propre perdu. Les contrastes qui bornent réellement l’accès restent en place.

## 2. general-writing (sur la version humanizer)
Passe minimale de clarté et néerlandais: syntaxe, sujets/verbes, précision et titres relus séparément. La passe broad humanizer précédente n’a pas été simulée une deuxième fois.

- Avant: `De torens en gevels die je nu ziet, tonen dus niet zonder meer de toestand van Stercks buitenverblijf.`
  Après: `De huidige torens en gevels tonen dus niet zonder meer Stercks buitenverblijf.`
- Avant: `het Sterckshof als erfgoedplek bij een wandeling`
  Après: `het Sterckshof tijdens een erfgoedwandeling`

Évaluation references/eval.md: sens et voix préservés; détails factuels comparés à la version fact-check; phrases utiles, acteurs clairs, pas de superlatif ou d’abstraction sans contenu; séries réservées aux ensembles utiles; titres, débuts/fins de paragraphes et transitions relus. Pas de voix personnelle ou de faux vécu ajouté. Format HTML et liens conservés. Les éléments non applicables (abstract académique, README, détection d’auteur) ne sont pas certifiés comme tests exécutés.

## 3. anti-ai-slop (review après general-writing, puis remédiation)
Contrat: informer sur ce château et rendre un choix de visite fiable, nl-BE. Protocoles review_workflow/output_design_review_gate, dimensions writing_information/localization_register appliqués.

P2 — Fin de fiche trop systématiquement orientée vers une autre sélection. Signal visible dans le cluster: les 12 fins ajoutaient une comparaison ou un renvoi à la province après avoir déjà résolu la visite. Un lien dans le fil est utile seulement s’il répond à une vraie suite; le renvoi provincial reste disponible dans le fil d’Ariane.

- Preuve: `De <a href="/kastelen/antwerpen/">provincieselectie Antwerpen</a> helpt om daarnaast een kasteel met een bevestigd interieurbezoek te vinden.`
  Correction: `[suppression du renvoi ou du résumé sans valeur propre]`
- Preuve: `Ook de bescherming van het kasteel en zijn bruggen sinds 1994 geeft geen recht op toegang tot alle onderdelen. De binnenplaatsen en kapel kun je dus niet op grond van hun vermelding alleen aan een vrij wandelparcours toevoegen.`
  Correction: `Het kasteel en de toegangsbruggen zijn sinds 1994 beschermd. De binnenplaatsen en kapel horen bij het monument, maar er is op de geraadpleegde projectpagina geen gewone vrije bezoekregeling voor bevestigd.`

Re-review: architecture et titres comparés aux 11 fiches; le sujet et la preuve organisent la progression, pas les anciens labels identiques. Les composants de page et la date commune sont fonctionnels, pas des défauts de style. Les phrases de restriction nécessaires à la visite ne sont pas supprimées pour varier artificiellement. Pas de superlatifs ni faux vécu; aucun signal HIGH restant. Confiance élevée sur cette observation éditoriale; aucune conclusion sur l’auteur ou une probabilité IA.
