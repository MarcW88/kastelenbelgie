# Passes éditoriales séparées — kasteel-marnix-de-sainte-aldegonde
Date: 2026-10-23

## 1. humanizer (après factualité)
Article complet lu, titres et lead inclus. Genre: fiche culturelle et aide à la visite. Sous-passes better-usage, academic-voice (précision sans registre académique), writing-cadence et non-autoregressive-writing-pass appliquées.

- Avant: `Het water rond het domein is meer dan een decor. `
  Après: `[suppression de la phrase sans information propre]`
- Avant: `Dat onderscheid helpt wanneer je naar de torens en het dubbele grachtenstelsel kijkt. Ze tonen hoe een adellijke familie haar residentie een historiserend karakter gaf. Je ziet er zowel oudere bouwsporen als een latere voorstelling van een kasteel.`
  Après: `De torens en het dubbele grachtenstelsel passen bij die negentiende-eeuwse keuze voor een historiserende residentie. De bewaarde muurdelen verbinden dat ontwerp met het oudere slot.`
- Avant: `Beyaerts waterburcht is geen ongewijzigde middeleeuwse burcht`
  Après: `De negentiende-eeuwse waterburcht van Beyaert`
- Avant: `Die concrete details geven meer houvast dan de verwachting van één consequent middeleeuws interieur.`
  Après: `De inrichting brengt daardoor andere perioden in beeld dan de middeleeuwse aanblik van de buitenkant doet vermoeden.`

Contrôle de préservation: dates, personnes, conditions d’accès et liens conservés; les phrases retirées répétaient une distinction ou un jugement, sans fait propre perdu. Les contrastes qui bornent réellement l’accès restent en place.

## 2. general-writing (sur la version humanizer)
Passe minimale de clarté et néerlandais: syntaxe, sujets/verbes, précision et titres relus séparément. La passe broad humanizer précédente n’a pas été simulée une deuxième fois.

- Avant: `de aanblik van het geheel is in belangrijke mate negentiende-eeuws`
  Après: `het geheel oogt vooral negentiende-eeuws`
- Avant: `Bespreek dus de gekozen formule vooraf`
  Après: `Bespreek de gekozen formule vooraf`

Évaluation references/eval.md: sens et voix préservés; détails factuels comparés à la version fact-check; phrases utiles, acteurs clairs, pas de superlatif ou d’abstraction sans contenu; séries réservées aux ensembles utiles; titres, débuts/fins de paragraphes et transitions relus. Pas de voix personnelle ou de faux vécu ajouté. Format HTML et liens conservés. Les éléments non applicables (abstract académique, README, détection d’auteur) ne sont pas certifiés comme tests exécutés.

## 3. anti-ai-slop (review après general-writing, puis remédiation)
Contrat: informer sur ce château et rendre un choix de visite fiable, nl-BE. Protocoles review_workflow/output_design_review_gate, dimensions writing_information/localization_register appliqués.

P2 — Fin de fiche trop systématiquement orientée vers une autre sélection. Signal visible dans le cluster: les 12 fins ajoutaient une comparaison ou un renvoi à la province après avoir déjà résolu la visite. Un lien dans le fil est utile seulement s’il répond à une vraie suite; le renvoi provincial reste disponible dans le fil d’Ariane.

- Preuve: `Zoek je in dezelfde gemeente een residentie met een ander verhaal, bekijk dan <a href="/kasteel/kasteel-dursel/">Kasteel d’Ursel in Hingene</a>; de <a href="/kastelen/antwerpen/">provincieselectie Antwerpen</a> vergelijkt ook andere bezoekvormen.`
  Correction: `</p><p>In dezelfde gemeente biedt <a href="/kasteel/kasteel-dursel/">Kasteel d’Ursel in Hingene</a> een ander perspectief: een vroegere zomerresidentie met tentoonstellingen en een afzonderlijk toegankelijk park.`

Re-review: architecture et titres comparés aux 11 fiches; le sujet et la preuve organisent la progression, pas les anciens labels identiques. Les composants de page et la date commune sont fonctionnels, pas des défauts de style. Les phrases de restriction nécessaires à la visite ne sont pas supprimées pour varier artificiellement. Pas de superlatifs ni faux vécu; aucun signal HIGH restant. Confiance élevée sur cette observation éditoriale; aucune conclusion sur l’auteur ou une probabilité IA.

## 4. Retour depuis le rendu / correction et re-review
FAIL initial mobile 390 px: le H2 `Het volledige bezoek of alleen het belevingscentrum?` débordait à cause d’un mot composé long. Correction éditoriale: `Kasteelkamers of het verhaal van Bornem?`. Aucune règle CSS ou workflow modifiée. Le sens de la section et sa couverture restent identiques; titre repassé par clarté, anti-slop et SEO. Nouvelle capture et mesure requises après rebuild.
