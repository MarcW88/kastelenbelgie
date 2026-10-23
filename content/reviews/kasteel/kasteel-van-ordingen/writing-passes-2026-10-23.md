# Passes éditoriales séparées — kasteel-van-ordingen
Date: 2026-10-23

## 1. humanizer (après factualité)
Article complet lu, titres et lead inclus. Genre: fiche culturelle et aide à la visite. Sous-passes better-usage, academic-voice (précision sans registre académique), writing-cadence et non-autoregressive-writing-pass appliquées.

- Avant: `De geschiedenis van Ordingen begint vóór de huidige hotelinrichting. `
  Après: `[suppression de la phrase sans information propre]`
- Avant: `Het beeld van één middeleeuws gebouw dat simpelweg een hotel werd, klopt daardoor niet: de site was voordien al meermaals veranderd.`
  Après: `Het kasteel was dus al vóór de hotelbestemming grondig veranderd.`
- Avant: `De huidige inrichting moet dus worden onderscheiden van de bewaarde bouwgeschiedenis: een rijk aangeklede kamer is niet automatisch een volledig oorspronkelijk vertrek uit de tijd van de commandeurs.`
  Après: `Porters’ inrichting is een hedendaagse toevoeging aan het historische gebouw, geen reconstructie van de kamers van de commandeurs.`
- Avant: `Dat is een inhoudelijke vergelijking, geen oordeel over de kwaliteit van het hotel.`
  Après: `[suppression de la phrase sans information propre]`

Contrôle de préservation: dates, personnes, conditions d’accès et liens conservés; les phrases retirées répétaient une distinction ou un jugement, sans fait propre perdu. Les contrastes qui bornent réellement l’accès restent en place.

## 2. general-writing (sur la version humanizer)
Passe minimale de clarté et néerlandais: syntaxe, sujets/verbes, précision et titres relus séparément. La passe broad humanizer précédente n’a pas été simulée une deuxième fois.

- Avant: `Voor wie in erfgoed wil overnachten is juist die combinatie van historisch gebouw en hedendaags gebruik relevant. Voor wie authentieke objecten met een museale toelichting wil bestuderen, is het een andere bezoekvorm.`
  Après: `Wie in erfgoed wil overnachten, vindt hier een historisch gebouw met hedendaags comfort. Een studiebezoek aan oorspronkelijke objecten met museale toelichting vraagt een ander aanbod.`
- Avant: `De op 23 oktober 2026 geraadpleegde informatie geeft geen algemeen museumticket`
  Après: `De op 23 oktober 2026 geraadpleegde website biedt geen algemeen museumticket`

Évaluation references/eval.md: sens et voix préservés; détails factuels comparés à la version fact-check; phrases utiles, acteurs clairs, pas de superlatif ou d’abstraction sans contenu; séries réservées aux ensembles utiles; titres, débuts/fins de paragraphes et transitions relus. Pas de voix personnelle ou de faux vécu ajouté. Format HTML et liens conservés. Les éléments non applicables (abstract académique, README, détection d’auteur) ne sont pas certifiés comme tests exécutés.

## 3. anti-ai-slop (review après general-writing, puis remédiation)
Contrat: informer sur ce château et rendre un choix de visite fiable, nl-BE. Protocoles review_workflow/output_design_review_gate, dimensions writing_information/localization_register appliqués.

P2 — Fin de fiche trop systématiquement orientée vers une autre sélection. Signal visible dans le cluster: les 12 fins ajoutaient une comparaison ou un renvoi à la province après avoir déjà résolu la visite. Un lien dans le fil est utile seulement s’il répond à une vraie suite; le renvoi provincial reste disponible dans le fil d’Ariane.

- Preuve: `Voor een andere soort kasteeluitstap helpt de <a href="/kastelen/limburg/">selectie kastelen in Limburg</a>, met naast logies ook tuinen, domeinen en aangekondigde rondleidingen.`
  Correction: `[suppression du renvoi ou du résumé sans valeur propre]`
- Preuve: `Het verblijf afwegen tegen een cultuurbezoek`
  Correction: `Een museumverhaal volgen vanuit Ordingen`

Re-review: architecture et titres comparés aux 11 fiches; le sujet et la preuve organisent la progression, pas les anciens labels identiques. Les composants de page et la date commune sont fonctionnels, pas des défauts de style. Les phrases de restriction nécessaires à la visite ne sont pas supprimées pour varier artificiellement. Pas de superlatifs ni faux vécu; aucun signal HIGH restant. Confiance élevée sur cette observation éditoriale; aucune conclusion sur l’auteur ou une probabilité IA.
