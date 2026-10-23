# Passes éditoriales séparées — kasteel-dursel
Date: 2026-10-23

## 1. humanizer (après factualité)
Article complet lu, titres et lead inclus. Genre: fiche culturelle et aide à la visite. Sous-passes better-usage, academic-voice (précision sans registre académique), writing-cadence et non-autoregressive-writing-pass appliquées.

- Avant: `Dat maakt de salons interessanter dan een losse verzameling mooie kamers: hun inrichting hoort bij het leven dat hier tijdens het zomerseizoen werd georganiseerd.`
  Après: `De salons dienden om gasten te ontvangen; hun inrichting hoorde bij het zomerse leven van de familie.`
- Avant: `Die ontwikkeling kreeg een architecturale vertaling. Jean Beausire werkte`
  Après: `Jean Beausire werkte`
- Avant: `De verschillende ingrepen maken duidelijk waarom één stijlwoord het huis onvoldoende beschrijft. De familie liet niet telkens een volledig nieuw kasteel bouwen, maar veranderde een bestaande residentie.`
  Après: `De familie paste haar bestaande residentie telkens aan een nieuwe smaak aan.`
- Avant: `Dat is een manier om de werken te bekijken, geen bewering dat elk detail een vaststaande betekenis heeft. `
  Après: `[suppression de la phrase sans information propre]`

Contrôle de préservation: dates, personnes, conditions d’accès et liens conservés; les phrases retirées répétaient une distinction ou un jugement, sans fait propre perdu. Les contrastes qui bornent réellement l’accès restent en place.

## 2. general-writing (sur la version humanizer)
Passe minimale de clarté et néerlandais: syntaxe, sujets/verbes, précision et titres relus séparément. La passe broad humanizer précédente n’a pas été simulée une deuxième fois.

- Avant: `Op de op 23 oktober geraadpleegde website staan`
  Après: `Op de website staan bij de controle op 23 oktober 2026`
- Avant: `Tijdens een inhoudelijke rondleiding`
  Après: `Tijdens een rondleiding over het kasteel`

Évaluation references/eval.md: sens et voix préservés; détails factuels comparés à la version fact-check; phrases utiles, acteurs clairs, pas de superlatif ou d’abstraction sans contenu; séries réservées aux ensembles utiles; titres, débuts/fins de paragraphes et transitions relus. Pas de voix personnelle ou de faux vécu ajouté. Format HTML et liens conservés. Les éléments non applicables (abstract académique, README, détection d’auteur) ne sont pas certifiés comme tests exécutés.

## 3. anti-ai-slop (review après general-writing, puis remédiation)
Contrat: informer sur ce château et rendre un choix de visite fiable, nl-BE. Protocoles review_workflow/output_design_review_gate, dimensions writing_information/localization_register appliqués.

P2 — Fin de fiche trop systématiquement orientée vers une autre sélection. Signal visible dans le cluster: les 12 fins ajoutaient une comparaison ou un renvoi à la province après avoir déjà résolu la visite. Un lien dans le fil est utile seulement s’il répond à une vraie suite; le renvoi provincial reste disponible dans le fil d’Ariane.

- Preuve: `Laat je keuze afhangen van het onderwerp dat je wilt zien: een tijdelijke tentoonstelling geeft een ander bezoek dan een rondleiding over het huis en zijn bewoners. `
  Correction: `[suppression du renvoi ou du résumé sans valeur propre]`
- Preuve: `Beide locaties staan in de <a href="/kastelen/antwerpen/">selectie kastelen in Antwerpen</a>, met hun afzonderlijke bezoekvoorwaarden.`
  Correction: `[suppression du renvoi ou du résumé sans valeur propre]`

Re-review: architecture et titres comparés aux 11 fiches; le sujet et la preuve organisent la progression, pas les anciens labels identiques. Les composants de page et la date commune sont fonctionnels, pas des défauts de style. Les phrases de restriction nécessaires à la visite ne sont pas supprimées pour varier artificiellement. Pas de superlatifs ni faux vécu; aucun signal HIGH restant. Confiance élevée sur cette observation éditoriale; aucune conclusion sur l’auteur ou une probabilité IA.
