---
name: museum-analysis-workflow
description: Workflow d'analyse SEO/GEO pour visite-musee.fr. Audite une URL ou un cluster, prépare une nouvelle page, impose une recherche SERP/content-gap, contrôle intention de visite, entités, preuves, fraîcheur, cannibalisation et similarité, puis décide KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX. Sert aussi de PUBLISH_REVIEW final.
provenance: custom
metadata:
  engine_version: 1
  adapted_for: visite-musee.fr
  source_engine: https://github.com/MarcW88/thuisrenovatie-gids/tree/main/.agents/skills/renovation-analysis-workflow
  source_engine_parent: https://github.com/MarcW88/bloc-notes-numerique/tree/main/.agents/skills/guide-analysis-workflow
  domain_models:
    - https://github.com/linked-art/linked.art
    - https://github.com/CollectionBuilder/collectionbuilder-gh
    - https://github.com/TheScienceMuseum/heritage-connector
  orchestration_target: ">=80% existing GitHub skills/workflows"
  custom_scope: "orchestration + museum route ownership + entity/freshness model + research gates + publish gate"
---

# Museum Analysis Workflow v1

## Rôle

C'est le workflow d'analyse éditoriale de `visite-musee.fr`.

Il ne rédige pas. Il doit lire `AGENTS.md`, `.agents/MUSEUM_MODEL.md`, `.agents/SKILL_REGISTRY.md` et appliquer les skills existants dans leur version canonique avant d'ajouter seulement les contrôles propres au site.

Séparation stricte :

- `museum-analysis-workflow` = recherche, diagnostic, décision, cluster audit, new-page research et publish review ;
- `museum-content-workflow` = brief, rédaction/correction, passes factualité/GEO/style/SEO et post-write gap check.

Un cluster (`MUSEUM`, `CITY`, `THEME`, etc.) définit un ownership d'intention, jamais une structure de texte.

---

# 1. Modes

## `AUDIT`

Pour une URL existante. Retourne une décision sans réécrire.

## `NEW_PAGE`

Pour une URL nouvelle ou encore vide. Établit ownership, intention, SERP, besoins utilisateur, entités, preuves, gaps et brief handoff. Aucun draft à ce stade.

## `CLUSTER_AUDIT`

Analyse plusieurs URLs ensemble : ownership, overlap SERP, cannibalisation, fragmentation, trous utiles, maillage, similarité structurelle et cohérence des entités.

## `PUBLISH_REVIEW`

Gate final après `museum-content-workflow`.

Résultats autorisés :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS ne change jamais l'indexation automatiquement.

---

# 2. Inputs à lire avant décision

Selon le périmètre :

- `AGENTS.md` ;
- `.agents/MUSEUM_MODEL.md` ;
- `.agents/SKILL_REGISTRY.md` ;
- page rendue et source éditoriale si elle existe ;
- research artifacts, brief et reviews existants ;
- pages voisines susceptibles de partager l'intention ;
- analyse sémantique, GSC, logs ou autres données disponibles ;
- SERP actuelle lorsque la demande ou le format doit être confirmé ;
- sources actuelles pour les faits `SEMI_STABLE` et `VOLATILE`.

Ne jamais remplacer un input absent par la mémoire du modèle. Tout manque susceptible de changer la décision devient un `DATA_GAP` explicite.

---

# 3. Skills existants à exécuter

Le workflow ne réécrit pas leur méthode. Ouvrir les skills depuis les sources déclarées dans `.agents/SKILL_REGISTRY.md`.

## 3.1 Audit / refresh

- `seo-content-audit` pour valeur, intent drift, thin content, duplication, consolidation ou retrait ;
- `content-refresh` pour obsolescence, trust gaps, generic prose, structural cloning et opportunités de mise à jour.

## 3.2 Keyword / intent / JTBD

- `seo-keyword` pour query set, variantes, clustering et SERP quand nécessaire ;
- `search-intent` pour tâche, résultat attendu, sous-intentions, maturité et exclusions ;
- `jtbd-framing` lorsque le job de visite reste ambigu : situation, motivation, résultat fonctionnel/émotionnel/social, hire/fire criteria.

Ne pas créer de persona fictif pour justifier une section.

## 3.3 Compétition et information gain

Exécuter `seo-competitor` pour :

- tout `DEEP_REWRITE` ;
- tout `NEW_PAGE` stratégique ;
- toute cannibalisation potentielle ;
- toute intention ou profondeur de couverture contestable.

L'objectif est de comprendre la SERP et les besoins non satisfaits, pas d'imiter les concurrents.

## 3.4 Architecture / ownership

Exécuter `information-architecture` lorsque le rôle de l'URL est incertain.

Frontières :

- `/musee/` = entité musée exacte + décision de visite ;
- `/musees/<ville>/`, `/regions/`, `/departements/` = sélection géographique ;
- `/themes/` = sélection par sujet/collection/type ;
- `/visiter/` = contrainte ou besoin de visite ;
- `/expositions/` = programmation temporaire ;
- `/inspiration/` = découverte éditoriale ;
- `/guides/` = question pratique transverse.

Si deux URLs peuvent garder la même réponse centrale en remplaçant seulement le lieu, thème ou nom du musée, l'ownership ou l'information gain est insuffisant.

## 3.5 Factualité / preuves

Exécuter `fact-check` sur tout claim qui influence la décision de visite.

Appliquer les classes de fraîcheur de `AGENTS.md` :

- `STABLE` ;
- `SEMI_STABLE` ;
- `VOLATILE`.

Les informations volatiles exigent source actuelle + date de vérification. Une donnée officielle plus récente prime sur une source secondaire.

`evidence-based-reviews` n'est utilisé que si une conclusion dépend réellement d'une méthodologie d'évaluation. Ne jamais simuler une visite, un test, une file d'attente observée ou une expérience familiale.

## 3.6 Entités / knowledge graph

Lire `.agents/MUSEUM_MODEL.md` et vérifier seulement les relations utiles : musée, lieu, collection, thème, artiste, œuvre, exposition, bâtiment, architecte, Wikidata/sameAs.

Une relation incertaine reste absente ou explicitement marquée comme gap. Ne pas confondre « œuvre détenue par la collection » et « œuvre actuellement exposée ».

## 3.7 SEO/GEO / QA

En review :

- `seo-onpage` ;
- `seo-technical` ;
- `seo-aeo-geo` ;
- `internal-linking-audit` ;
- `anti-ai-slop` ;
- `editorial-qa` ;
- `seo-drift` seulement si un baseline utile existe.

---

# 4. Research gate obligatoire

Pour tout `NEW_PAGE` et tout `DEEP_REWRITE`, créer :

`content/research/<route>/serp-coverage.md`

à partir de `references/serp-coverage-matrix-template.md`.

La matrice doit contenir au minimum :

1. requête principale, variantes et sous-intentions ;
2. résultats réellement inspectés et types de pages gagnants ;
3. SERP features pertinentes ;
4. besoins/questions récurrents ;
5. informations pratiques, entités, preuves ou formats utilisés par les meilleurs résultats ;
6. état actuel `MISSING / PARTIAL / COVERED` ;
7. priorité `MUST / SHOULD / OPTIONAL` ;
8. opportunités d'information gain ;
9. opportunités GEO/citation réellement utiles ;
10. overlap avec les URLs internes ;
11. entités à vérifier ;
12. data gaps et fraîcheur.

### Gate

Le handoff vers rédaction est interdit si :

- la SERP nécessaire n'a pas été inspectée ;
- l'ownership de l'intention reste ambigu ;
- un `MUST` central dépend d'une donnée introuvable ou non vérifiée ;
- la proposition de visite repose sur des adjectifs génériques plutôt que sur des faits ;
- un conflit de cannibalisation n'est pas résolu.

---

# 5. NEW_PAGE

Ordre recommandé :

`information-architecture -> seo-keyword -> search-intent -> jtbd-framing si nécessaire -> seo-competitor -> entity/source research -> fact-check -> SERP coverage matrix -> handoff`.

Output minimum :

- route et cluster owner ;
- primary query / task ;
- sous-intentions et exclusions ;
- proposition de visite provisoire fondée sur des preuves ;
- entités confirmées / à confirmer ;
- MUST / SHOULD / OPTIONAL ;
- sources prioritaires ;
- fraîcheur des claims ;
- information gain ;
- internal overlap ;
- data gaps ;
- statut `READY_FOR_BRIEF` ou `BLOCKED`.

`NEW_PAGE` ne rédige pas la page.

---

# 6. Décisions AUDIT

## `KEEP`

Tâche claire, distincte, suffisamment utile, actuelle et factuellement solide.

## `LIGHT_UPDATE`

Corrections limitées : faits, fraîcheur, metadata, maillage, sources, entités ou frontière.

## `DEEP_REWRITE`

Problème structurant : intent drift, mauvais ownership, faible information gain, generic prose, preuves centrales insuffisantes, cannibalisation ou architecture industrialisée. Déclenche obligatoirement le research gate.

## `MERGE`

Une autre URL possède essentiellement la même tâche. Recommandation seulement tant qu'aucune action structurelle n'est explicitement demandée.

## `NOINDEX`

Valeur, preuve, distinctivité ou justification insuffisante. Aucune suppression automatique.

Chaque décision inclut : confiance, valeur à préserver, preuves, unknowns, freshness gaps, cannibalisation et prochaine étape.

---

# 7. Similarité structurelle

En `CLUSTER_AUDIT` et `PUBLISH_REVIEW`, vérifier :

- mêmes fonctions de H2 dans le même ordre ;
- mêmes blocs « pourquoi visiter » ;
- mêmes tableaux pratiques sans justification ;
- mêmes introductions ou conclusions avec substitution d'entité ;
- mêmes nombres de raisons/étapes ;
- même rythme et mêmes CTA ;
- mêmes jugements vagues (`incontournable`, `unique`, `idéal`) sans preuve spécifique.

Les composants UI peuvent être partagés ; la logique éditoriale ne doit pas être clonée.

---

# 8. PUBLISH_REVIEW

Ne l'exécuter que sur une version considérée terminée.

Vérifier :

- research artifact présent pour `NEW_PAGE` / `DEEP_REWRITE` ;
- brief relié aux MUST et data gaps ;
- post-write gap check présent ;
- aucun `MUST = MISSING` ;
- tout `MUST = PARTIAL` est justifié sans affaiblir la tâche centrale ;
- intention réellement satisfaite ;
- proposition de visite spécifique et prouvable ;
- faits importants sourcés ;
- claims volatils datés et actuels ;
- entités et relations non ambiguës ;
- pas de fausse expérience ;
- information gain réel ;
- cannibalisation maîtrisée ;
- GEO extractible sans FAQ/slop artificiel ;
- pas de signal `HIGH` anti-AI-slop ;
- title/H1/canonical/robots/schema/liens cohérents ;
- similarité structurelle acceptable.

Tout blocker central force :

`FAIL — KEEP_NOINDEX`

Sinon :

`PASS — READY_FOR_HUMAN_VALIDATION`

---

# 9. Indexation

Le workflow ne retire jamais `noindex` et ne change jamais une politique d'indexation. Cela exige un PASS, une validation humaine et une instruction explicite distincte.

---

# 10. Interdits

Ne jamais utiliser comme proxy de qualité : quota de mots, nombre minimum de headings, quota de sources/liens, FAQ obligatoire, tableau obligatoire, nombre fixe de raisons, score artificiel ou template imposé par cluster.
