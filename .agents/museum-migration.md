# Migration Visite Musée → Kastelen België

Date: 2026-10-22

## Original files

- Visite Musée source commit: `7c30b136a4e069d472282678bed4205fd0f2b972`.
- Both original museum workflows and both report templates copied unchanged.
- Original MUSEUM_MODEL.md and SKILL_REGISTRY.md copied unchanged.
- Original source AGENTS.md, README.md and provenance retained under reference/visite-musee/.
- Five missing specialists and their complete directories copied from the canonical repository explicitly named by that registry: thuisrenovatie-gids at `33ff11ae8c9b6c9fcc416d3d3cff2a3d5e98de95`.
- 30 original files pinned individually in museum-agents.lock.json; all 22 specialists required by the source are locally present.
- The 555 existing shared source files remain unchanged.

## Activation

AGENTS.md, shared-routing.json and site-context.shared.md select the cultural workflows for the homepage and all castle, geographic, theme, visiting, itinerary, inspiration and guide content. The separate castle-context.md maps nl-BE / Belgium, entities and routes to the unchanged source workflows. Source template examples about France/museums are adapted in produced artifacts, not by changing source files. Trust and design keep their own original workflows.

## Actual validation

- `python3 scripts/verify_museum_agents.py`: PASS for the 555 existing source files, 30 migration originals, specialist availability, workflow references and cultural routing.
- `npm run check`: PASS, 55 existing HTML pages checked. This checks CSS references/noindex, not editorial quality.
- No page, style, asset, generator or indexing state changed by this migration.

This is agent installation, not a content audit or a Playwright review. The current build writes placeholder HTML from hardcoded source data: reviewed content must be integrated into that source pipeline before publishing it through a rebuild. The separate context records this requirement so authored content is not silently overwritten. NEW_PAGE/research and existing-page audits can use the migrated workflows now.
