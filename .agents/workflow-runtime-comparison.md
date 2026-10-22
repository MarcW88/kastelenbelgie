# Runtime comparison: Kastelen België versus three source repositories

Reviewed: 2026-10-22

## Repositories (actual repository identifiers)
- MarcW88/bloc-notes-numerique (not `bloc-notes-numeriques`)
- MarcW88/aspirateurs-chantier
- MarcW88/visite-musee
- MarcW88/kastelenbelgie

## Content-method integrity
- `museum-analysis-workflow/SKILL.md` in Kastelen is byte-identical (Git blob 645e064e...) to `visite-musee`.
- `museum-content-workflow/SKILL.md` in Kastelen is byte-identical (Git blob b6d21c4f...) to `visite-musee`.
- `anti-ai-slop/SKILL.md` from Bloc-notes and Aspirateurs is byte-identical (Git blob a0ae97dc...); shared agent verification on Kastelen reports success.
- Therefore broken editorial work was NOT caused by an incomplete copy of these specific SKILL files.

## Missing execution bindings and why earlier requests failed
1. **A skill specification is not an executable agent.** The SKILL.md files instruct a capable author/agent to research, write, check and exercise editorial judgment. A GitHub Actions runner does not perform those passes merely because it can read the text.
2. **Kastelen originally had deploy, agent file integrity and visual screenshot workflows, but no real quality pipeline.** Visite-musee has PR `quality.yml` (build + check). Bloc-notes has a `regenerate-guides.yml` that calls site-specific generation, indexing and validation scripts; Aspirateurs likewise has `validate-guide-methodology-pilot.yml` that runs generators and asserts site-specific editorial evidence. Copying their job names alone would not work with Kastelen's JS generator.
3. **Dead-end evidence-only gate.** The first `west-flanders-editorial-gates.yml` required `content/reviews/kasteel/<slug>/workflow-evidence.json`, which no agent, script or workflow created. This is a guaranteed fail rather than an executor. Replaced with machine-verifiable checks against real content/briefs/reviews and an uploaded report.
4. **Incorrect fact-report detector.** Machine-check script looked only for `factual|fact-check|feit`; the real report table called the column `Facts, entity and freshness`. Eight false negative failures resulted. Detector now recognizes the actual heading but labels this as DOCUMENTED rather than an independent fact-check PASS.
5. **Build consistency.** The canonical build is `npm run build` plus `npm run check`, using `content/reviewed-pages.json`. Machine and visual tests now rebuild first. Generated HTML should not be edited in isolation.
6. **Playwright was previously confused with a content-quality audit.** The actual `site-design-review` takes route and output options, captures viewport screenshots and browser errors. It does not analyze historical truth, source traceability or editorial voice. Keep those separate.
7. **Indexing cannot be auto-approved.** Source museum workflow requires a comprehensive research gate and `PUBLISH_REVIEW` with human validation before changing noindex. Machine-integrity results must never be used to invent evidence or remove the tag.

## Operational sequence (non-substitutable)
For each page:
1. AUDIT/NEW_PAGE — specialist research and analysis: SERP results actually observed, source provenance, ownership and overlap.
2. RESEARCH — report real source URLs, MUST/SHOULD coverage, unanswered needs, volatile facts with date.
3. BRIEF — a page-specific structure from the research (no cloned H2 order).
4. DRAFT — authorship under museum-content-workflow, with unique site-specific contribution.
5. FACT-CHECK — individual meaningful claims with source link and current date if necessary.
6. GEO and internal linking — citation-worthy evidence, next relevant local destination.
7. HUMANIZER / GENERAL-WRITING / ANTI-AI-SLOP — distinct editorial passes, with actual recorded findings and remediations.
8. ONPAGE/TECHNICAL/EDITORIAL-QA — build, metadata, canonical, routes, claimed coverage.
9. PLAYWRIGHT — inspect desktop/mobile captures for that rendered revision.
10. PUBLISH_REVIEW — factual/editorial human judgment. Status `FAIL — KEEP_NOINDEX` until every blocker resolved.

## Machine tooling provided in Kastelen
- `scripts/check-west-flanders.mjs`: exact source-to-render links, routes, H1, metadata technical guards and canonical.
- `scripts/verify-west-editorial-gates.mjs`: objective machine checks and machine-readable artifact `.artifacts/qa/west-flanders-machine-gates.json`; checks presence of recorded editorial work, does NOT execute LLM specialist passes.
- `.github/workflows/west-flanders-editorial-gates.yml`: run canonical JS build + machine tests and upload the QA artifact for inspection.
- `.github/workflows/visual-design-review.yml`: real Playwright viewport captures, independent of editorial quality.

**External human/LLM execution is still required** for truthfulness, depth, competing SERP analysis, anti-slop and final human approval. Any workflow claiming to automate those without an actual inference agent and accessible sources is deceptive.
