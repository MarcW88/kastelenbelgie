# Repository instructions


## Shared agents — canonical routing (installation 2026-10-22)

Read `.agents/site-context.shared.md` and `.agents/shared-routing.json` before any editorial or design task. Use the full original files in `.agents/skills/` listed there, including every required specialist, phase and gate. Bloc-notes numérique is canonical for shared methods; Aspirateurs chantier supplies complementary model/recovery workflows. Do not substitute a shortened local workflow. This routing supersedes earlier workflow selections in this file; existing factual, safety, preservation, source-of-truth and indexation constraints remain mandatory. More specific site paths are resolved through the shared context.

Read workflows in full: existing-page AUDIT first, then only the correction justified by its handoff, then PUBLISH_REVIEW and actual evidence. A machine integrity PASS is not an editorial or visual PASS. Model workflows retain their original phase/audit-only limits. Read the original site-design-review for design/CSS/Playwright tasks. Do not create an absent page family merely because its agent is installed.

Original source workflows, configs, scripts and Actions are retained intact in `.agents/reference/`. Those French site generators/Actions are reference dependencies, not commands to run blindly on this site's content. Resolve theme, language, routes and native commands through the site context; record a missing required adapter as BLOCKED, never as PASS.

Run `python3 scripts/verify_site_agents.py` to verify all pinned original files.


## Cultural content — Visite Musée migration (2026-10-22)

For any Kastelen België cultural content task, first read `.agents/castle-context.md`, `.agents/shared-routing.json`, `.agents/MUSEUM_MODEL.md` and `.agents/SKILL_REGISTRY.md`. This cultural routing explicitly supersedes generic guide/comparison/brand/usage routing for the atlas homepage and `/kasteel/`, `/kastelen/`, `/soorten/`, `/bezoeken/`, `/routes/`, `/inspiratie/`, `/gidsen/`.

Execute the entire `.agents/skills/museum-analysis-workflow/SKILL.md` and `.agents/skills/museum-content-workflow/SKILL.md`, including all required specialists and their gates. Their original source names/content remain unchanged; the separate castle context resolves language, market, entities and routes. Use NEW_PAGE for placeholders/empty content as defined by the source workflow, AUDIT for substantive existing pages, and PUBLISH_REVIEW after production. Do not substitute the generic product/brand/comparison workflow for a castle fiche. Trust and design retain their own shared workflows.

Keep the complete original research and post-write gap gates; no automatic indexation or invented evidence. Author reviewed content in `content/<route>/body.html` and register the existing route and metadata in `content/reviewed-pages.json`; the native build applies those sources after generating placeholders. Never edit only the generated HTML. Run build/check and confirm the reviewed text survives a rebuild. Run `python3 scripts/verify_museum_agents.py` to verify the migration and existing shared files.
