# Live article test — Humanizer, General Writing, Anti-AI-Slop
Date: 2026-10-23
Article: content/kasteel/kasteel-rivierenhof/body.html
Method: actual sequential editorial revision, not a regex-only checker or authorship detector.

## Source integrity
The same canonical SKILL.md Git blob SHA was verified across bloc-notes-numerique, aspirateurs-chantier and kastelenbelgie:
- humanizer: accad07f498f5f57e0b6460e74591d057bd96b2b
- general-writing: 9ae8219798fcc0565f891cd4bd650e911903ca27
- anti-ai-slop: a0ae97dc8814bf450847eb2b7653ab64fbdf0ee0

## 1. Humanizer — APPLIED
Observed source: generic framing "Een kasteel bij de spiegelvijver met een horecafunctie" and repeated 'een andere bezoekvorm' contrasts.
Action: lead rewritten to "Aan de spiegelvijver ligt een kasteelrestaurant. Voor een wandeling heb je het restaurant niet nodig; voor een bezoek aan historische zalen bestaat hier geen regulier museumparcours." Recast repeated explanatory bridges as direct reader language.
Check: factual scope preserved: park, restaurant, no independent museum circuit.

## 2. General Writing — APPLIED
Observed source: vague H2 "Praktisch kiezen" and inflated/unclear contrast between restaurant, park and museum.
Action: H2 replaced with "Een wandeling of een restaurantbezoek plannen". Sentences shortened and reordered around an actual decision: walking independently, eating with a restaurant reservation, or choosing another castle for a guided interior.
Check: all key user decisions still present.

## 3. Anti-AI-Slop — APPLIED
Observed source: duplicate standalone section "Een kasteel zonder museumparcours" restated almost all of previous park/restaurant/Sterckshof sections.
Action: removed entire duplicate section and strengthened concise location-specific claims in remaining sections; Sterckshof historical rebuilding preserved.
Check: only one section explains Sterckshof; restaurant vs independent walking remains clear.

## Test result
PASS: confirmed distinct, visible direct content edits by all three editorial methods, committed in the article itself.
NOT CLAIMED: fully autonomous running of LLM text edits in GitHub Actions. These SKILL.md files are instructions, not executable programs. Current CI pattern lint or source-blob equality is not a substitute for an editor applying their procedures.
No other site workflow used for this test.
