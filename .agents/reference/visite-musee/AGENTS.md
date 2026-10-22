# Visite Musée — agent rules

## Mission

Visite Musée aide à décider **quel musée visiter, pourquoi il correspond à une intention donnée et comment préparer la visite avec des informations fiables**. Le site n'est ni un catalogue neutre de lieux, ni un guide touristique générique, ni un faux site d'avis.

L'agent doit privilégier :

1. la satisfaction de l'intention de visite ;
2. la fiabilité et la fraîcheur des informations pratiques ;
3. la compréhension des entités culturelles (musée, collection, artiste, œuvre, exposition, lieu, période, thème) ;
4. l'information gain par rapport aux pages déjà présentes et à la SERP ;
5. l'indexation seulement après validation humaine.

## Architecture éditoriale et ownership

| Cluster | Route | Rôle principal |
|---|---|---|
| MUSEUM | `/musee/<slug>/` | fiche d'un musée précis : proposition de visite, identité, collections, œuvres/artistes, bâtiment, informations pratiques |
| CITY | `/musees/<ville>/` | sélection et comparaison de musées dans une ville |
| REGION | `/regions/<region>/` | découverte géographique plus large |
| DEPARTMENT | `/departements/<departement>/` | découverte géographique départementale |
| THEME | `/themes/<theme>/` | sélection par collection, discipline, période ou type de musée |
| VISIT_INTENT | `/visiter/<intent>/` | sélection selon une contrainte ou un besoin de visite |
| EXHIBITION | `/expositions/<ville-or-slug>/` | programmation temporaire et actualité d'exposition |
| INSPIRATION | `/inspiration/<slug>/` | découverte éditoriale, sélection, comparaison ou idée de sortie |
| GUIDE | `/guides/<slug>/` | question pratique ou méthodologique transverse |

Ces types définissent une **frontière éditoriale**, jamais un template de texte. Aucun nombre fixe de sections, mots, FAQ, tableaux ou CTA n'est imposé.

## Workflow obligatoire

### URL existante

1. `museum-analysis-workflow / AUDIT`
2. décision : `KEEP`, `LIGHT_UPDATE`, `DEEP_REWRITE`, `MERGE` ou `NOINDEX`
3. seulement pour `LIGHT_UPDATE` ou `DEEP_REWRITE` : `museum-content-workflow`
4. `museum-analysis-workflow / PUBLISH_REVIEW`
5. validation humaine avant toute indexation ou action structurelle

### Nouvelle URL

1. `museum-analysis-workflow / NEW_PAGE`
2. SERP + intent + ownership + sources + modèle d'entités
3. création du research artifact et du brief
4. `museum-content-workflow`
5. `museum-analysis-workflow / PUBLISH_REVIEW`
6. validation humaine

### Cluster

Utiliser `museum-analysis-workflow / CLUSTER_AUDIT` pour overlap, cannibalisation, trous de couverture, similarité structurelle et maillage. Ce mode ne réécrit pas automatiquement.

## Skills first, custom orchestration second

Les workflows musée n'inventent pas de méthode SEO, recherche, rédaction ou QA. Ils orchestrent des skills existants déclarés dans `.agents/SKILL_REGISTRY.md`.

Priorité aux skills existants :

- `seo-content-audit`, `seo-keyword`, `search-intent`, `seo-competitor`, `content-refresh` ;
- `jtbd-framing`, `information-architecture` ;
- `fact-check`, `evidence-based-reviews` lorsque pertinent ;
- `content-brief-authoring`, `brand-voice`, `content-and-copy` ;
- `seo-aeo-geo`, `internal-linking-audit` ;
- `humanizer`, `general-writing`, `anti-ai-slop` ;
- `seo-onpage`, `seo-technical`, `seo-best-practices`, `seo-drift` si baseline disponible ;
- `editorial-qa`.

Ne pas créer de skill custom `visit-intent`, `entity-geo`, `museum-fact-check`, `museum-writing` ou équivalent si le besoin est déjà couvert par un skill existant.

## Modèle métier musée

Lire `.agents/MUSEUM_MODEL.md` avant toute recherche ou rédaction sur une fiche musée. Le modèle s'inspire de Linked Art / CIDOC-CRM pour les relations d'entités, de CollectionBuilder pour la logique metadata-first et de Heritage Connector pour l'enrichissement Wikidata / knowledge graph.

Le modèle simplifié doit rester utile au produit : ne pas reproduire une ontologie complète si elle n'aide ni l'utilisateur, ni le maillage, ni la factualité, ni le GEO.

## Fraîcheur et factualité

Classer chaque claim dans l'une de ces catégories :

- `STABLE` : histoire du musée, architecture historique, artistes, mouvements, dates historiques, origine des collections ;
- `SEMI_STABLE` : collections exposées, services, accessibilité, politique famille, espaces, parcours ;
- `VOLATILE` : horaires, tarifs, gratuité, réservation, fermetures, travaux, conditions d'accès, expositions temporaires.

Règles :

- les claims `VOLATILE` exigent une source actuelle et une date de vérification ;
- les claims `SEMI_STABLE` doivent être vérifiés dès qu'ils influencent la décision de visite ;
- les claims `STABLE` doivent rester exacts et sourcés lorsqu'ils sont spécifiques ou contestables ;
- ne jamais inventer horaires, prix, gratuité, accessibilité, durée, affluence, exposition ou réservation ;
- ne jamais présenter comme expérience personnelle une visite qui n'a pas eu lieu.

## Proposition de visite

Une fiche `/musee/` doit pouvoir répondre, avec des faits vérifiables, à :

> Pourquoi ce musée plutôt qu'un autre, pour quel type de visite ou de visiteur, et quelles contraintes pratiques faut-il connaître ?

Ce n'est pas une obligation de produire une section nommée ainsi ni un nombre fixe de raisons. La réponse doit émerger de l'intention, des collections, du bâtiment, des œuvres, de la programmation, des contraintes et de la comparaison implicite avec les alternatives pertinentes.

## Sources et hiérarchie de preuve

Pour les informations pratiques et institutionnelles, privilégier :

1. site officiel du musée ou de l'institution ;
2. source publique ou institutionnelle officielle ;
3. base d'entités reconnue (Wikidata, BnF, data culture, etc.) pour identité et relations ;
4. sources éditoriales fiables pour contexte, réception ou comparaison ;
5. signaux communautaires uniquement comme signaux d'usage, jamais comme source unique d'un fait critique.

Une source secondaire ne doit pas écraser une donnée officielle plus récente.

## GEO / entités

Le GEO doit découler de données utiles aux humains :

- noms officiels et aliases ;
- ville, région, adresse et coordonnées si fiables ;
- types de collections, périodes, artistes et œuvres notables ;
- bâtiment / architecte lorsque pertinent ;
- liens Wikidata / sameAs lorsqu'ils sont confirmés ;
- faits atomiques sourcés et datés lorsque nécessaire.

Ne pas ajouter de FAQ artificielle, de blocs répétitifs ou de jargon ontologique visible uniquement pour les moteurs.

## Similarité structurelle

En `CLUSTER_AUDIT` et `PUBLISH_REVIEW`, rechercher :

- même séquence de H2 sur plusieurs musées sans justification ;
- même intro/conclusion avec substitution du nom du musée ;
- mêmes listes de « raisons de visiter » ;
- même tableau pratique quand les données ne le justifient pas ;
- mêmes CTA ou transitions ;
- mêmes formulations de jugement non sourcé.

Les composants UI peuvent être réutilisés. La structure éditoriale doit être déterminée par l'intention et les preuves.

## Source de vérité

Le workflow doit conserver séparément :

- recherche : `content/research/<route>/` ;
- briefs : `content/briefs/<route>.md` ;
- reviews : `content/reviews/<route>/` ;
- données structurées musée : `content/data/museums/<slug>.json` lorsqu'elles seront activées ;
- contenu éditorial : la source utilisée par le générateur du site, jamais seulement le HTML généré final.

Tant que le dépôt n'a pas encore de structure `content/`, le workflow peut créer les artefacts de recherche et de brief sans modifier les pages générées.

## PUBLISH_REVIEW

Résultats autorisés :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS n'active jamais automatiquement l'indexation.

Tout `MUST = MISSING`, claim central non vérifié, donnée volatile non sourcée, ownership ambigu ou cannibalisation non résolue force `FAIL — KEEP_NOINDEX`.

## Indexation

Les pages existantes restent `noindex,follow` tant qu'une instruction humaine explicite ne demande pas de changer cette politique après un `PUBLISH_REVIEW` PASS.


## Shared agents — canonical routing (installation 2026-10-22)

Read `.agents/site-context.shared.md` and `.agents/shared-routing.json` before any editorial or design task. Use the full original files in `.agents/skills/` listed there, including every required specialist, phase and gate. Bloc-notes numérique is canonical for shared methods; Aspirateurs chantier supplies complementary model/recovery workflows. Do not substitute a shortened local workflow. This routing supersedes earlier workflow selections in this file; existing factual, safety, preservation, source-of-truth and indexation constraints remain mandatory. More specific site paths are resolved through the shared context.

Read workflows in full: existing-page AUDIT first, then only the correction justified by its handoff, then PUBLISH_REVIEW and actual evidence. A machine integrity PASS is not an editorial or visual PASS. Model workflows retain their original phase/audit-only limits. Read the original site-design-review for design/CSS/Playwright tasks. Do not create an absent page family merely because its agent is installed.

Original source workflows, configs, scripts and Actions are retained intact in `.agents/reference/`. Those French site generators/Actions are reference dependencies, not commands to run blindly on this site's content. Resolve theme, language, routes and native commands through the site context; record a missing required adapter as BLOCKED, never as PASS.

Run `python3 scripts/verify_site_agents.py` to verify all pinned original files.
