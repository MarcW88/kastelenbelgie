# Analyse → correction — kasteel-dursel
workflow: museum-analysis-workflow / AUDIT → museum-content-workflow / LIGHT_UPDATE → PUBLISH_REVIEW
execution_date: 2026-10-23
route: /kasteel/kasteel-dursel/

## Diagnostic
Décision: LIGHT_UPDATE
Problème constaté: Exposition temporaire trop susceptible d'être lue comme ouverture permanente.
Intention: informer précisément sur la visite de l'entité, pas remplacer la sélection régionale /kastelen/antwerpen/.
Conserver: Histoire d'Ursel, portretten, parc public.

## Correction exécutée sur HTML
Encadré textuel temporel lié au 2 novembre 2026; vérifier actualisation de l'agenda.
Source de vérité: content/kasteel/kasteel-dursel/body.html

## Passes de rédaction
- fact-check / freshness: limiter les affirmations changeantes à leurs périodes; ne pas promettre de disponibilité.
- seo-aeo-geo: conserver réponse directe sur ce qui peut être visité.
- humanizer: réduire les formulations prudentes en cascade et clarifier les sujets.
- general-writing: raccourcir ou redéfinir la phrase identifiée.
- anti-ai-slop: supprimer les formulations de comparaison générique quand non nécessaires.
- internal-linking: lien provincial et sortie vers la source officielle conservés.

## PUBLISH_REVIEW
Résultat: FAIL — KEEP_NOINDEX (données de visite dynamiques; source et calendrier à recontrôler avant validation humaine/indexation). Les corrections de LIGHT_UPDATE sont effectuées, mais cette conclusion ne certifie pas un audit SERP top-10 exhaustif.
