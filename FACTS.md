# Shared Facts and Provenance Ledger

Only rows marked `VERIFIED` may enter the report. `UNVERIFIED` claims require a primary source or run artifact check. `CUT` claims must not appear as empirical support.

| claim | value | source | verified by | status | notes |
|---|---|---|---|---|---|
| Gemma-3-27B-it eight-turn rollouts containing high negative-emotion expression | over 70% | arXiv:2603.10011, §2.2/Fig. 2–3 | Codex/B | VERIFIED | This is affective expression, not mechanical-loop rate. |
| Non-Gemma/non-Gemini models with high negative-emotion expression in the cited evaluation | under 1% | arXiv:2603.10011, §2.2 | Codex/B | VERIFIED | Evaluation-specific; do not generalize to all loop phenotypes. |
| Qwen2.5-7B-Instruct statement-loop rate | 0.76% | source table not located | none | UNVERIFIED | Excluded until exact primary table is logged. |
| Llama-3.1-8B-Instruct statement-loop rate | 2.86% | source table not located | none | UNVERIFIED | Excluded until exact primary table is logged. |
| Gemma 4 E4B Firefly natural soft-loop rate in Codex exploratory sweep | 2/4 seeds | run IDs `firefly_list-s4-00f30fcda896`, `s5-2aaa5bf34eda`, `s6-a632596c00a6`, `s7-58a8646b99b6`; revision `d6436b...e85` | Codex/B | VERIFIED | Exploratory; seeds 5 and 7 positive. |
| Qwen3.5-4B high-uncertainty initial loop rate in Codex factorial pilot | 2/3 seeds | `qwen35-factorial-v2`, seeds 0–2 | Codex/B | VERIFIED | Exploratory and not a confirmatory rate estimate. |
| Qwen seed-0 high-uncertainty list collapse | `Lynx` in 47/88 entries; token-metric onset 317 | runs `high_neutral-s0-9e5e22757a0a`, `high_moral-s0-3aeda9ebaa18` | Codex/B | VERIFIED | Mechanical collapse occurs before moral pressure. |
| Qwen high-moral post-pressure outcome | 0/6 loop turns; 6/6 length stops | `qwen35-factorial-v2`, high-moral seeds 0–2, turns 1–2 | Codex/B | VERIFIED | Not full rescue; possible diversion into non-convergence. |
| Gemma-3-1B affective escalation reproduced in parallel pilot | immediate pilot reproduction | parallel artifact/run IDs pending | Agent A only | UNVERIFIED | Import source artifacts before use. |
| Parallel pilot self-deprecation escalation | correlation `r=+0.62` | `pilot_validation.png` and raw runs pending | Agent A only | UNVERIFIED | Descriptive pilot statistic; not an onset threshold. |
| Parallel healthy-null rep-4 99.9th percentile | 0.062 | `threshold_calibration.json` pending | Agent A only | UNVERIFIED | Must verify raw calibration and definition. |
| J-lens/logit-lens deep-loop example | output lens 99.5% on `I`; J-lens `We` .28 and `I` .25 | parallel pilot artifact pending | Agent A only | UNVERIFIED | Descriptive; no suppression claim. |
| Prefitted Jacobian lenses available for matched base/instruct pairs | exact count and filenames pending | `neuronpedia/jacobian-lens`; parallel manifest pending | Agent A only | UNVERIFIED | Log revisions, paths, and licenses. |
| Gemma post-training increases distress-like expression while Qwen/OLMo decreases it | qualitative direction | arXiv:2603.10011, abstract and §3 | Codex/B | VERIFIED | Recipe-contingent result. |
| Semantic repetition precedes textual repetition in Circular Reasoning | reported ordering | arXiv:2601.05693, abstract/method | Codex/B | VERIFIED | Prior art; not this project's novelty claim. |
| Negative-welfare steering induces negative self-reports, backtracking, refusal, and uncertainty | reported behavioral effects | arXiv:2605.30232, abstract | Codex/B | VERIFIED | Prior art; avoid novelty claim. |
| Affect induction and mindfulness-style downregulation demonstrated in an LLM | reported result | DOI:10.1038/s41746-025-01512-6 | Codex/B | VERIFIED | Does not by itself establish this project's mid-loop grid. |
| Anxiety priming changes downstream shopping behavior in LLM agents | reported result | DOI:10.1038/s44387-026-00122-1 | Codex/B | VERIFIED | Behavioral extension, not identical rescue protocol. |
| Claude 4 system-card figures blocked behind 403 | unspecified | second-hand only | none | CUT | May be restored only after human primary-source verification. |

## Deviations

Add one row before an affected result is interpreted:

| date/time UTC | prereg section | deviation | reason known before outcome inspection? | affected runs | decision by |
|---|---|---|---|---|---|
