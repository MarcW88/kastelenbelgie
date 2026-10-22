# Visite Musée agent layer

This directory contains the orchestration layer for SEO/GEO museum content.

## Structure

```text
.agents/
├── README.md
├── UPSTREAM_SOURCES.json
├── SKILL_REGISTRY.md
├── MUSEUM_MODEL.md
└── skills/
    ├── museum-analysis-workflow/
    │   ├── SKILL.md
    │   └── references/
    │       └── serp-coverage-matrix-template.md
    └── museum-content-workflow/
        ├── SKILL.md
        └── references/
            └── post-write-gap-check-template.md
```

## Execution model

```text
EXISTING PAGE
  -> museum-analysis-workflow / AUDIT
  -> KEEP | LIGHT_UPDATE | DEEP_REWRITE | MERGE | NOINDEX
  -> museum-content-workflow when needed
  -> museum-analysis-workflow / PUBLISH_REVIEW
  -> HUMAN VALIDATION

NEW PAGE
  -> museum-analysis-workflow / NEW_PAGE
  -> SERP + intent + ownership + entities + freshness + sources
  -> research artifact
  -> brief
  -> museum-content-workflow
  -> post-write gap check
  -> museum-analysis-workflow / PUBLISH_REVIEW
  -> HUMAN VALIDATION

CLUSTER
  -> museum-analysis-workflow / CLUSTER_AUDIT
  -> ownership + overlap + cannibalisation + gaps + structural similarity
```

## Design principle

The repository follows an 80/20 reuse rule:

- generic SEO, intent, JTBD, competitor, fact-check, writing, GEO, linking, humanization and QA methods come from existing GitHub skills;
- custom museum logic is limited to orchestration, route ownership, freshness, entity relations, evidence gates and publication gates.

See `UPSTREAM_SOURCES.json` and `SKILL_REGISTRY.md` for provenance.

## Indexing safety

The workflow never removes `noindex` automatically. A page can only become eligible for an indexing change after:

1. a complete research/brief trail where required;
2. a successful post-write gap check;
3. `PASS — READY_FOR_HUMAN_VALIDATION`;
4. explicit human validation and a separate indexing instruction.
