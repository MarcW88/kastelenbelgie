---
name: museum-content-workflow
description: Workflow de production/correction SEO/GEO pour visite-musee.fr. Consomme un handoff d'analyse, une matrice SERP/content-gap et un brief, puis orchestre les skills existants de voice, copy, factualité, GEO, maillage, humanisation, SEO et QA. Une nouvelle page ou un DEEP_REWRITE ne peut pas être rédigé sans research artifact et doit produire un post-write gap check.
provenance: custom
metadata:
  engine_version: 1
  adapted_for: visite-musee.fr
  source_engine: https://github.com/MarcW88/thuisrenovatie-gids/tree/main/.agents/skills/renovation-content-workflow
  source_engine_parent: https://github.com/MarcW88/bloc-notes-numerique/tree/main/.agents/skills/guide-content-workflow
  orchestration_target: ">=80% existing GitHub skills/workflows"
  custom_scope: "research handoff + museum source-of-truth + entity/freshness controls + post-write coverage gate"
---

# Museum Content Workflow v1

## Rôle

C'est le workflow de production/correction de `visite-musee.fr`.

Séquence normale :

`AUDIT/NEW_PAGE -> decision/handoff -> research gate -> brief -> draft -> factual/entity/GEO/style/SEO passes -> post-write gap check -> PUBLISH_REVIEW`.

Décisions :

- `KEEP` -> ne pas réécrire ;
- `LIGHT_UPDATE` -> corriger uniquement le scope identifié ;
- `DEEP_REWRITE` -> reconstruire en préservant la valeur identifiée, uniquement après research gate ;
- `NEW_PAGE / READY_FOR_BRIEF` -> brief puis rédaction après research gate ;
- `MERGE / NOINDEX / BLOCKED` -> aucune nouvelle version sans résolution ou décision humaine.

Le workflow ne change jamais l'indexation.

---

# 1. Entrées obligatoires

Lire :

- `AGENTS.md` ;
- `.agents/MUSEUM_MODEL.md` ;
- `.agents/SKILL_REGISTRY.md` ;
- `.agents/skills/museum-analysis-workflow/SKILL.md` ;
- audit / NEW_PAGE handoff / cluster conclusions ;
- page existante et source éditoriale si disponible ;
- pages voisines ;
- sources et preuves disponibles.

Pour `NEW_PAGE` et `DEEP_REWRITE`, lire obligatoirement :

- `content/research/<route>/serp-coverage.md` ;
- le brief associé lorsque disponible.

Si le research artifact manque, n'utilise pas une SERP actuelle, laisse un ownership ambigu ou contient un data gap bloquant sur un MUST : `STOP — RETURN_TO_ANALYSIS`.

---

# 2. Skills existants : exécution réelle

Ouvrir et appliquer les skills depuis `.agents/SKILL_REGISTRY.md`. Un simple nom de skill dans ce fichier n'est pas une validation.

La couche custom musée ne doit pas recopier les frameworks génériques de keyword research, brief, copy, GEO, humanisation ou QA.

---

# 3. Brief

Utiliser :

- `seo-keyword` ;
- `search-intent` ;
- `seo-competitor` pour les conclusions SERP d'un `NEW_PAGE` ou `DEEP_REWRITE` ;
- `jtbd-framing` si le job de visite doit être précisé ;
- `information-architecture` si l'ownership reste sensible ;
- `content-brief-authoring` comme méthode principale.

Persister :

`content/briefs/<route>.md`

avec `workflow_version: museum-v1`.

Le brief doit contenir au minimum :

- primary query + tâche ;
- audience/contexte seulement s'ils sont supportés par intent/JTBD, sans persona theater ;
- route owner et exclusions ;
- MUST / SHOULD issus de la matrice ;
- proposition de visite / angle ;
- entités à mobiliser ;
- faits et sources nécessaires ;
- classes de fraîcheur ;
- data gaps ;
- information gain ;
- valeur existante à préserver ;
- prochaines questions et liens internes ;
- structure proposée après recherche.

Ne pas imposer une architecture parce que la page est de type `MUSEUM`, `CITY`, `THEME`, etc.

---

# 4. Voice avant copy

Utiliser `brand-voice` avec la direction de marque disponible dans le repo (`DESIGN.md` et toute future source de voice dédiée).

La voix attendue est :

- culturelle sans être académique ;
- précise sans encyclopédisme gratuit ;
- utile à la décision de visite ;
- indépendante ;
- descriptive avant d'être laudative ;
- prudente sur les données instables.

Ne jamais transformer une absence de preuve en enthousiasme marketing.

---

# 5. Rédaction pour la substance

Utiliser `content-and-copy`.

Le draft doit :

- répondre tôt à la tâche centrale ;
- couvrir chaque MUST avec la profondeur nécessaire ;
- expliquer ce qui rend le musée pertinent pour l'intention visée ;
- utiliser collections, artistes, œuvres, bâtiment, histoire ou exposition seulement lorsqu'ils servent cette proposition ;
- distinguer faits stables, données pratiques et interprétation éditoriale ;
- intégrer contraintes et trade-offs qui changent réellement la décision ;
- préserver les passages valides identifiés par l'audit ;
- éviter remplissage, synonymie décorative et répétitions ;
- ne jamais inventer visite, durée, affluence, prix, horaire, exposition, œuvre exposée, accessibilité ou service.

Le contenu visible ne doit pas ressembler à une fiche de base de données mise en prose.

---

# 6. Factualité et entités après draft

Exécuter `fact-check` sur les claims réellement écrits.

Pour chaque claim important, vérifier :

- source ;
- scope ;
- classe `STABLE / SEMI_STABLE / VOLATILE` ;
- date de vérification si nécessaire ;
- cohérence avec `.agents/MUSEUM_MODEL.md`.

Contrôles musée spécifiques :

- une œuvre de collection n'est pas automatiquement actuellement exposée ;
- une exposition temporaire doit avoir dates + source officielle ;
- horaires/tarifs/gratuité/réservation doivent être actuels ;
- Wikidata/sameAs servent à désambiguïser, jamais à remplacer une source officielle pour les conditions de visite ;
- toute estimation éditoriale (ex. durée) doit être clairement distinguée d'une information officielle.

Si un claim central échoue : corriger ou supprimer. Ne pas le masquer par une formulation vague.

---

# 7. GEO / AEO

Exécuter `seo-aeo-geo` après factualité.

Appliquer seulement les patterns qui améliorent aussi l'expérience humaine :

- réponse directe lorsque naturelle ;
- faits atomiques + contexte/source ;
- désambiguïsation d'entités ;
- définitions utiles ;
- tableaux uniquement pour de vraies comparaisons/données ;
- dates et scope pour les données instables ;
- relations claires entre musée, collection, artiste, œuvre, lieu et exposition.

Interdits :

- FAQ artificielle ;
- répétition d'une même réponse pour créer des snippets ;
- headings bots-first ;
- accumulation de noms d'entités sans utilité ;
- jargon Linked Art/CIDOC visible pour impressionner les moteurs.

Objectif : `citation worthiness`, pas écriture robotique.

---

# 8. Maillage

Exécuter `internal-linking-audit`.

Les liens doivent répondre à une prochaine question logique, par exemple :

- musée -> ville / thème / artiste / guide pertinent ;
- ville -> musées réellement différenciés ;
- thème -> musées qui illustrent réellement ce thème ;
- exposition -> musée hôte ;
- guide -> pages de décision concrètes.

Aucun quota de liens.

---

# 9. Finition éditoriale

Exécuter séparément :

1. `humanizer` ;
2. `general-writing` ;
3. `anti-ai-slop` ;
4. `seo-drift` seulement si baseline utile.

Après chaque passe, préserver :

- faits et sources ;
- nuance ;
- distinction entre officiel et éditorial ;
- MUST coverage ;
- information gain ;
- singularité de structure.

Le humanizer ne doit jamais supprimer dates, conditions ou précautions factuelles nécessaires.

---

# 10. SEO / QA

Exécuter :

1. `seo-onpage` ;
2. `seo-technical` ;
3. `seo-best-practices` ;
4. `editorial-qa` ;
5. lecture du rendu desktop/mobile si disponible.

Vérifier :

- title/H1/description alignés sur l'intention réelle ;
- canonical / robots cohérents ;
- structured data seulement si les données existent réellement ;
- liens internes cohérents ;
- pas de duplication structurelle évidente avec les autres fiches.

---

# 11. Post-write gap check obligatoire

Pour tout `NEW_PAGE` ou `DEEP_REWRITE`, créer :

`content/reviews/<route>/post-write-gap-check.md`

à partir de `references/post-write-gap-check-template.md`.

Reporter chaque MUST et SHOULD pertinent :

- `COVERED / PARTIAL / MISSING` ;
- emplacement ;
- preuve/source ;
- fraîcheur ;
- justification si `PARTIAL`.

Puis vérifier :

- proposition de visite spécifique et prouvable ;
- entités utiles correctement reliées ;
- données volatiles vérifiées ;
- information gain préservé ;
- GEO utile sans slop ;
- voice / humanizer / general-writing / anti-ai-slop exécutés séparément ;
- aucune structure clonée créée.

Tout `MUST = MISSING`, claim central non vérifié ou donnée volatile centrale sans source force :

`FAIL — KEEP_NOINDEX`.

---

# 12. Handoff final

Passer la main à :

`museum-analysis-workflow / PUBLISH_REVIEW`.

Ne pas auto-valider.

Statuts internes possibles :

- `BRIEF_READY`
- `DRAFT_READY`
- `QA_IN_PROGRESS`
- `REVISION_REQUIRED`
- `READY_FOR_PUBLISH_REVIEW`
- `HUMAN_APPROVED`

L'indexation est toujours une instruction distincte.

---

# 13. Interdits

Ne pas utiliser comme proxy de qualité : quota de mots, nombre minimum de H2/H3, nombre obligatoire de sources/liens, FAQ/tableau obligatoire, nombre fixe de « raisons de visiter », score artificiel ou template éditorial imposé par type de page.
