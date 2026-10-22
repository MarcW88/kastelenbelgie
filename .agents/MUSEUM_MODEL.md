# Museum model — Visite Musée

## Objectif

Ce modèle est une couche métier simplifiée pour guider recherche, données structurées, maillage et GEO. Il s'inspire de Linked Art / CIDOC-CRM, CollectionBuilder et Heritage Connector, sans chercher à reproduire une ontologie muséale complète.

Le modèle ne remplace jamais une source. Une relation n'existe dans le contenu que si elle est confirmée.

## Entités principales

### Museum

Champs utiles :

- `name`
- `official_name`
- `alternate_names[]`
- `museum_type[]`
- `official_url`
- `wikidata_id`
- `same_as[]`
- `address`
- `coordinates`
- `city`
- `department`
- `region`
- `country`
- `building_name`
- `architects[]`
- `opening_date`
- `collections[]`
- `themes[]`
- `periods[]`
- `artists[]`
- `notable_works[]`
- `current_exhibitions[]`

### Collection / Theme

- `name`
- `type`
- `periods[]`
- `artists[]`
- `works[]`
- `museum`
- `source`

### Person / Group

Pour artiste, architecte, fondateur ou institution :

- `name`
- `role`
- `wikidata_id`
- `same_as[]`
- `related_museums[]`
- `related_works[]`

### Work

- `title`
- `creator`
- `date_or_period`
- `work_type`
- `current_museum`
- `collection`
- `wikidata_id` si disponible
- `source`

Ne jamais déclarer qu'une œuvre est exposée actuellement sur la seule base de son appartenance à une collection.

### Exhibition

- `title`
- `museum`
- `start_date`
- `end_date`
- `booking_required`
- `official_url`
- `checked_at`

Une exposition est toujours `VOLATILE`.

### Place

- `name`
- `place_type`
- `city`
- `department`
- `region`
- `country`
- `coordinates`
- `wikidata_id`

## Relations utiles

Relations conceptuelles à utiliser pour raisonner et mailler :

- `Museum -> located_in -> Place`
- `Museum -> holds_collection -> Collection`
- `Museum -> associated_with -> Person/Group`
- `Museum -> presents -> Exhibition`
- `Collection -> includes_or_relates_to -> Work`
- `Work -> created_by -> Person/Group`
- `Work -> current_museum -> Museum`
- `Museum -> housed_in -> Building/Place`
- `Museum -> relevant_for -> VisitIntent`

`relevant_for` n'est pas une vérité ontologique : c'est une conclusion éditoriale qui doit être justifiée par des faits.

## Données de visite

Objet logique `visit` :

- `opening_hours`
- `closures`
- `ticket_price`
- `free_conditions`
- `reservation`
- `accessibility`
- `family_services`
- `visitor_services`
- `recommended_duration`
- `access_transport`
- `checked_at`
- `sources[]`

### Règles spécifiques

- `opening_hours`, `closures`, `ticket_price`, `free_conditions`, `reservation` = `VOLATILE` ;
- `accessibility`, `family_services`, `visitor_services` = au minimum `SEMI_STABLE` ;
- `recommended_duration` ne peut être présenté comme donnée officielle que si une source le fournit. Sinon, il doit être formulé comme estimation éditoriale avec méthode/contexte, ou rester absent.

## Provenance

Chaque fait important doit pouvoir être relié à :

- `source_url`
- `source_type`
- `checked_at`
- `claim_scope`
- `freshness_class`

Valeurs de `source_type` recommandées :

- `OFFICIAL_MUSEUM`
- `OFFICIAL_PUBLIC`
- `ENTITY_DATABASE`
- `RELIABLE_EDITORIAL`
- `COMMUNITY_SIGNAL`

## Entités et GEO

Avant rédaction d'une fiche musée, identifier au minimum si les sources le permettent :

- musée exact et nom officiel ;
- lieu ;
- type(s) de collection ;
- périodes ou mouvements majeurs ;
- artistes ou créateurs particulièrement structurants ;
- œuvres réellement pertinentes et confirmées ;
- bâtiment / architecte si cela contribue à la proposition de visite ;
- Wikidata / sameAs utiles.

Le contenu visible reste naturel. Les identifiants et relations servent à éviter les ambiguïtés, améliorer le maillage et rendre les faits plus extractibles, pas à exposer du jargon de knowledge graph.

## Metadata-first

La logique CollectionBuilder retenue est :

`métadonnées fiables -> relations -> ownership de page -> contenu -> rendu`.

Éviter l'inverse : ne pas rédiger d'abord une narration puis inventer les métadonnées pour la faire correspondre.

## Knowledge graph enrichment

La logique Heritage Connector retenue est :

1. identifier l'entité ;
2. la relier à un identifiant externe fiable quand disponible ;
3. vérifier les relations utiles ;
4. exploiter uniquement les relations qui améliorent recherche, navigation ou compréhension.

Pas de relation déduite automatiquement sans validation lorsque l'erreur pourrait modifier la décision de visite.
