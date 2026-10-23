# Passes éditoriales séparées — paleis-op-de-meir
Date: 2026-10-23

## 1. humanizer (après factualité)
Article complet lu, titres et lead inclus. Genre: fiche culturelle et aide à la visite. Sous-passes better-usage, academic-voice (précision sans registre académique), writing-cadence et non-autoregressive-writing-pass appliquées.

- Avant: `Je hoeft daarvoor geen volledige stijlenleer te kennen: kijk naar de manier waarop ornamenten rond een deur, wand of plafond zijn uitgewerkt.`
  Après: `Let bij een bezoek op de uitwerking van die motieven rond deuren en aan de wanden.`
- Avant: `De verbinding met Napoleon is dus reëel, maar een verhaal over zijn dagelijkse leven in deze kamers zou verder gaan dan de feiten.`
  Après: `De empire-inrichting getuigt van zijn opdracht, niet van een verblijf ter plaatse.`
- Avant: `Rococo en latere toevoegingen vertellen verschillende hoofdstukken van hetzelfde gebouw.`
  Après: `Je ziet er de rococo van de oorspronkelijke opdracht naast de ingrepen van latere eigenaars.`

Contrôle de préservation: dates, personnes, conditions d’accès et liens conservés; les phrases retirées répétaient une distinction ou un jugement, sans fait propre perdu. Les contrastes qui bornent réellement l’accès restent en place.

## 2. general-writing (sur la version humanizer)
Passe minimale de clarté et néerlandais: syntaxe, sujets/verbes, précision et titres relus séparément. La passe broad humanizer précédente n’a pas été simulée une deuxième fois.

- Avant: `heeft hij er zelf nooit verbleven`
  Après: `is hij er zelf nooit verbleven`
- Avant: `Op de op 23 oktober geraadpleegde <a href=`
  Après: `Op de <a href=`
- Avant: `bezoekerspagina van Herita</a> staan individuele bezoeken`
  Après: `bezoekerspagina van Herita</a>, nagekeken op 23 oktober 2026, staan individuele bezoeken`

Évaluation references/eval.md: sens et voix préservés; détails factuels comparés à la version fact-check; phrases utiles, acteurs clairs, pas de superlatif ou d’abstraction sans contenu; séries réservées aux ensembles utiles; titres, débuts/fins de paragraphes et transitions relus. Pas de voix personnelle ou de faux vécu ajouté. Format HTML et liens conservés. Les éléments non applicables (abstract académique, README, détection d’auteur) ne sont pas certifiés comme tests exécutés.

## 3. anti-ai-slop (review après general-writing, puis remédiation)
Contrat: informer sur ce château et rendre un choix de visite fiable, nl-BE. Protocoles review_workflow/output_design_review_gate, dimensions writing_information/localization_register appliqués.

P2 — Fin de fiche trop systématiquement orientée vers une autre sélection. Signal visible dans le cluster: les 12 fins ajoutaient une comparaison ou un renvoi à la province après avoir déjà résolu la visite. Un lien dans le fil est utile seulement s’il répond à une vraie suite; le renvoi provincial reste disponible dans le fil d’Ariane.

- Preuve: `<p>Het paleis is vooral een keuze voor historische interieurs in de stad. Voor een buitenverblijf met een park kun je <a href="/kasteel/kasteel-dursel/">Kasteel d’Ursel in Hingene</a> bekijken. De <a href="/kastelen/antwerpen/">selectie kastelen in Antwerpen</a> maakt dat verschil in bezoekvorm zichtbaar.</p>`
  Correction: `[suppression du renvoi ou du résumé sans valeur propre]`

Re-review: architecture et titres comparés aux 11 fiches; le sujet et la preuve organisent la progression, pas les anciens labels identiques. Les composants de page et la date commune sont fonctionnels, pas des défauts de style. Les phrases de restriction nécessaires à la visite ne sont pas supprimées pour varier artificiellement. Pas de superlatifs ni faux vécu; aucun signal HIGH restant. Confiance élevée sur cette observation éditoriale; aucune conclusion sur l’auteur ou une probabilité IA.
