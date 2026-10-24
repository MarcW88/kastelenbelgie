# Beauvoorde: post-write gap check and PUBLISH_REVIEW
workflow_version: museum-v1
mode: AUDIT -> DEEP_REWRITE -> PUBLISH_REVIEW
checked_at: 2026-10-24

| Requirement | Coverage | Location / evidence |
|---|---|---|
| One castle and a specific visit proposition | COVERED | Intro, bouwgeschiedenis; Arthur's reconstructed historical house |
| Original fabric versus later additions | COVERED | bouwgeschiedenis/interieur; Herita + Inventaris |
| Concrete interior evidence | COVERED | Dated fireplaces, acquired panelling, Vinck chapel; historical source scope |
| Recent restoration and diary route | COVERED | restauratie/bezoekparcours; operator restoration and visit pages |
| Calendar, fees and booking limits | COVERED | praktisch-bezoek; scoped 2026 dates, last entry, counter/online distinction, group exception |
| Accessibility and visitor address | COVERED | toegang-en-adres; explicit wheelchair limitation and current operator address |
| Children/park information | COVERED | Named searches and scoped park rules, no invented services |
| Authentic image and attribution | COVERED | Dated Commons photo, LimoWreck + colour correction Siebrand, licence and display-crop notice |
| Contextual internal links | COVERED | Loppem interiors, Rumbeke/Sterrebos, province; no artificial dot-list or duplicate body destination |
| Research, brief, factual audit | COVERED | Route-specific artifacts; all central claims sourced, retrieval limits disclosed |

## Separate applied passes
1. content-and-copy: rebuilt the page around Beauvoorde's architectural layers and actual visitor route. Merged duplicated 1764/1875/1876/1902 narratives and removed appended generic FAQ/practical-card repetitions. Preserved correct historical distinctions, reopening and useful existing links.
2. fact-check: applied the separate claim table in fact-check.md. Corrected absolute advance-booking implication, explicit access restriction, current Dutch visitor address, photo aspect ratio and incomplete attribution. Retained uncertainty about an earlier motte. No invented guided duration.
3. seo-aeo-geo: clear entity/place scope, original versus acquired interior pieces, direct access answer, dated calendar and operator links. Honest TouristAttraction/BreadcrumbList only; no invented review or availability schema.
4. internal-linking-audit: inspected source and contextual targets. Retained parent geography, linked Loppem for coordinated interiors and Rumbeke for castle/bos combination. Header and editorial province links have different functions; no repeated body link to an internal target.
5. humanizer (with better-usage, academic-voice genre calibration, writing-cadence and global spine/boundary pass): removed vague “Dat maakt ... tijdscapsule” and generic authenticity conclusion. Replaced “lees je de vertrekken ... persoonlijke keuzes” with “Zijn keuzes bepalen nog steeds de inrichting die je bezoekt.” Preserved named people/dates, source scope and uncertainty; no first-hand voice.
6. general-writing: checked full title/lead/headings/caption/navigation and paragraph boundaries. Changed blunt calendar injunction to a dated 2027 recheck condition, kept each section focused, removed repeated recaps. The interior example explains object age versus placement without a generic slogan. Passed the general-writing evaluation against final prose.
7. anti-ai-slop: purpose = independent visit decision and cultural interpretation. Removed repeated FAQ, generic third-party promotional superlatives, three-card facts and artificial castle inventory. Shared Ooidonk visual components are justified; its editorial argument is not copied. No HIGH signal retained.
8. editorial-qa: intent, evidence, natural Belgian Dutch, practical usability and SEO preservation reviewed. The page is useful without commercial links; no affiliate, invented experience or automatic indexation.

## Technical / visual review
- Native npm build/check and west-flanders source checks pass; full agent integrity checks pass (not editorial proof).
- Local Playwright ran with Chromium 153 via an available packaged browser. Native repository visual runner also executed for Beauvoorde desktop/mobile. Its product-site selectors do not measure the castle aside; dedicated assertions additionally check the actual castle components.
- Dedicated viewports: 1440×1000, 768×1024, 390×844, 360×800. HTTP 200 locally; authentic local photo decodes 1280×960; no horizontal overflow, duplicate IDs, nested anchors or broken fragment destinations. One H1 and valid JSON-LD/canonical/noindex.
- Actual click caught the inherited base-href issue: bare # fragments navigated to the homepage. Beauvoorde's links now use /kasteel/kasteel-beauvoorde/#section. Click assertions verify both pathname and hash.
- Screenshot review prompted tablet stacking, a smaller single-line brand at <=400px, and anchor/sticky-aside offsets below the header. Keyboard focus and mobile menu opening/closing tested. Screenshots remain in ignored .artifacts/design-review/beauvoorde/ and beauvoorde-native/ as required.
- Browser initially reported a blocked Google Fonts request when bypassing the environment proxy. The final proxy-configured render loaded the actual Cormorant Garamond/Manrope fonts with no failed requests or console errors at all four viewports. Final desktop, tablet and mobile screenshots were inspected; image, caption, text, header, aside and anchor landing remain readable.

Local editorial verdict: PASS — READY_FOR_HUMAN_VALIDATION. Final screenshots inspected; no remaining local blocker. This never removes noindex. GitHub Actions and public deployment are separate release checks; record their actual state after the main commit, never assume queued means success.
