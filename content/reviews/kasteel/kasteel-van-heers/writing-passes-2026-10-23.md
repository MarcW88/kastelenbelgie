# Passes éditoriales séparées — kasteel-van-heers
Date: 2026-10-23

## 1. humanizer (après factualité)
Article complet lu, titres et lead inclus. Genre: fiche culturelle et aide à la visite. Sous-passes better-usage, academic-voice (précision sans registre académique), writing-cadence et non-autoregressive-writing-pass appliquées.

- Avant: `Dat maakt het bezoek inhoudelijk anders dan een rondgang door gerestaureerde salons. Je ziet een plek waarvan de toekomst nog wordt uitgewerkt en krijgt uitleg over verval, onderzoek en herstel.`
  Après: `De gids geeft uitleg over het verval en het herstel dat nu wordt voorbereid of uitgevoerd.`
- Avant: `Die compacte opbouw helpt om het kasteel als geheel te begrijpen, ook wanneer een deel achter stellingen schuilgaat.`
  Après: `De vier vleugels vormen samen een compact geheel, ook waar stellingen het zicht onderbreken.`
- Avant: `De latere heropbouw en de aanpassingen door opeenvolgende eigenaars horen bij hetzelfde verhaal. Het is nuttiger die lagen uit elkaar te houden dan het hele complex één middeleeuwse datum te geven.`
  Après: `De vermelding uit 1274 gaat over de plek; de huidige vorm ontstond door de latere heropbouw en aanpassingen.`
- Avant: `De werfrondleiding is dus een kans om het herstel te begrijpen terwijl het gebeurt.`
  Après: `Tijdens de werfrondleiding staat het herstel zelf mee centraal.`

Contrôle de préservation: dates, personnes, conditions d’accès et liens conservés; les phrases retirées répétaient une distinction ou un jugement, sans fait propre perdu. Les contrastes qui bornent réellement l’accès restent en place.

## 2. general-writing (sur la version humanizer)
Passe minimale de clarté et néerlandais: syntaxe, sujets/verbes, précision et titres relus séparément. La passe broad humanizer précédente n’a pas été simulée une deuxième fois.

- Avant: `Op de op 23 oktober 2026 geraadpleegde kalender loopt`
  Après: `Op de kalender loopt bij de controle op 23 oktober 2026`
- Avant: `Wie vooral een ingerichte residentie zoekt, heeft aan die vorm mogelijk minder dan aan een museumbezoek in`
  Après: `Wie vooral een ingericht kasteel met een museumverhaal zoekt, kan een bezoek overwegen aan`

Évaluation references/eval.md: sens et voix préservés; détails factuels comparés à la version fact-check; phrases utiles, acteurs clairs, pas de superlatif ou d’abstraction sans contenu; séries réservées aux ensembles utiles; titres, débuts/fins de paragraphes et transitions relus. Pas de voix personnelle ou de faux vécu ajouté. Format HTML et liens conservés. Les éléments non applicables (abstract académique, README, détection d’auteur) ne sont pas certifiés comme tests exécutés.

## 3. anti-ai-slop (review après general-writing, puis remédiation)
Contrat: informer sur ce château et rendre un choix de visite fiable, nl-BE. Protocoles review_workflow/output_design_review_gate, dimensions writing_information/localization_register appliqués.

P2 — Fin de fiche trop systématiquement orientée vers une autre sélection. Signal visible dans le cluster: les 12 fins ajoutaient une comparaison ou un renvoi à la province après avoir déjà résolu la visite. Un lien dans le fil est utile seulement s’il répond à une vraie suite; le renvoi provincial reste disponible dans le fil d’Ariane.

- Preuve: `Voor een bevestigde binnenrondleiding gebruik je de ticketshop van Herita; de <a href="/kastelen/limburg/">selectie kastelen in Limburg</a> helpt om bezoekvormen buiten een restauratiewerf te vergelijken.`
  Correction: `De ticketshop van Herita geeft aan welke binnenrondleidingen je daadwerkelijk kunt reserveren.`

Re-review: architecture et titres comparés aux 11 fiches; le sujet et la preuve organisent la progression, pas les anciens labels identiques. Les composants de page et la date commune sont fonctionnels, pas des défauts de style. Les phrases de restriction nécessaires à la visite ne sont pas supprimées pour varier artificiellement. Pas de superlatifs ni faux vécu; aucun signal HIGH restant. Confiance élevée sur cette observation éditoriale; aucune conclusion sur l’auteur ou une probabilité IA.
