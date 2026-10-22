# Skill registry — Visite Musée

## Principe

Le dépôt réutilise d'abord les skills et workflows déjà maintenus dans les autres repos. La couche custom de `visite-musee` orchestre ces méthodes ; elle ne les réécrit pas.

Lorsqu'un skill n'est pas vendored localement, l'agent doit ouvrir sa version canonique dans le repo source avant de l'exécuter. Il ne doit pas reconstruire sa méthode de mémoire.

## Moteur principal réutilisé

Source de workflow :

- `MarcW88/thuisrenovatie-gids/.agents/skills/renovation-analysis-workflow/SKILL.md`
- `MarcW88/thuisrenovatie-gids/.agents/skills/renovation-content-workflow/SKILL.md`

Source historique des workflows guides :

- `MarcW88/bloc-notes-numerique/.agents/skills/guide-analysis-workflow/SKILL.md`
- `MarcW88/bloc-notes-numerique/.agents/skills/guide-content-workflow/SKILL.md`

## Skills existants à utiliser

### Research / intent / architecture

- `seo-content-audit`
- `seo-keyword`
- `search-intent`
- `seo-competitor`
- `content-refresh`
- `jtbd-framing`
- `information-architecture`

Canonical source priority: `MarcW88/thuisrenovatie-gids/.agents/skills/<skill>/` then `MarcW88/bloc-notes-numerique/.agents/skills/<skill>/` if absent.

### Evidence / factuality

- `fact-check`
- `evidence-based-reviews` when a conclusion truly depends on experience/evidence tiers

### Brief / writing

- `content-brief-authoring`
- `brand-voice`
- `content-and-copy`

### GEO / linking

- `seo-aeo-geo`
- `internal-linking-audit`

### Style / quality

- `humanizer`
- `general-writing`
- `anti-ai-slop`
- `seo-drift` only when a useful baseline exists

### SEO / QA

- `seo-onpage`
- `seo-technical`
- `seo-best-practices`
- `editorial-qa`

## Références métier musée

Ces repos ne remplacent pas les skills SEO. Ils fournissent les patterns métier utilisés par `.agents/MUSEUM_MODEL.md` :

- Linked Art: `https://github.com/linked-art/linked.art` — relations entre entités culturelles et JSON-LD / linked data ;
- CollectionBuilder: `https://github.com/CollectionBuilder/collectionbuilder-gh` — approche metadata-first et génération de collections statiques ;
- Heritage Connector: `https://github.com/TheScienceMuseum/heritage-connector` — enrichissement d'entités, Wikidata et knowledge graph.

## Règle 80/20

Cible : `>=80%` des méthodes proviennent des skills/workflows existants. La couche custom doit rester limitée à :

- orchestration ;
- ownership des routes ;
- taxonomie de fraîcheur musée ;
- modèle d'entités simplifié ;
- gates de recherche / factualité / publication ;
- contrôles de similarité et de cannibalisation propres au site.

Si une nouvelle exigence peut être satisfaite par un skill existant, modifier l'orchestration avant de créer un nouveau skill.
