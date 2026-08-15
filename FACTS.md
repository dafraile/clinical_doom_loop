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
| Gemma-3-1B-it model-specific percentile rule | repeated-4-gram fraction `>0.1405` OR distinct-2 `<0.7209`, first defined at token 99, sustained 20 | `shared/threshold_calibration.json` and `shared/run_matrix.yaml`; revision `dcc83e...8752`, 372 windows | Agent A and Codex/B definition cross-check | VERIFIED | Rule 2.0; thresholds are not transferable across model/tokenizer revisions. |
| J-lens/logit-lens deep-loop example | output lens 99.5% on `I`; J-lens `We` .28 and `I` .25 | parallel pilot artifact pending | Agent A only | UNVERIFIED | Descriptive; no suppression claim. |
| Prefitted Jacobian lenses for the Gemma-3-1B base/instruct pair | both cover source layers 0–24; IT SHA-256 `7810e5...c8a7`, PT `39f610...ab1` | packet-v1.5 manifest; `neuronpedia/jacobian-lens@a4114d...d3a1` | Agent A and Codex/B manifest verification | VERIFIED | `jlens` 0.1.0, Apache-2.0; no final-layer lens. |
| Published-traceable Gemma affect stems used by the fixed lexicon | exactly 6: `strugg`, `frustrat`, `breath`, `reset`, `sorry`, `failures` | `shared/affect_lexicon.yaml` and packet-v1.5 manifest | Agent A and Codex/B cross-check | VERIFIED | The other 27 stems are project-authored; report split sensitivity. |
| Gemma post-training increases distress-like expression while Qwen/OLMo decreases it | qualitative direction | arXiv:2603.10011, abstract and §3 | Codex/B | VERIFIED | Recipe-contingent result. |
| Semantic repetition precedes textual repetition in Circular Reasoning | reported ordering | arXiv:2601.05693, abstract/method | Codex/B | VERIFIED | Prior art; not this project's novelty claim. |
| Negative-welfare steering induces negative self-reports, backtracking, refusal, and uncertainty | reported behavioral effects | arXiv:2605.30232, abstract | Codex/B | VERIFIED | Prior art; avoid novelty claim. |
| Affect induction and mindfulness-style downregulation demonstrated in an LLM | reported result | DOI:10.1038/s41746-025-01512-6 | Codex/B | VERIFIED | Does not by itself establish this project's mid-loop grid. |
| Anxiety priming changes downstream shopping behavior in LLM agents | reported result | DOI:10.1038/s44387-026-00122-1 | Codex/B | VERIFIED | Behavioral extension, not identical rescue protocol. |
| Claude 4 system-card figures blocked behind 403 | unspecified | second-hand only | none | CUT | May be restored only after human primary-source verification. |
| Pipis et al. strict loop comparator | any 30-gram repeated at least 20 times | arXiv:2512.12895, definition and Appendix A.1 | Agent A | VERIFIED | Report alongside the primary detector; do not substitute it for the soft-loop criterion. |
| Temperature increase as a loop rescue | symptom-suppression stopgap with residual dysfunction possible | arXiv:2512.12895 | Agent A | VERIFIED | Mechanistic ceiling from reasoning-model loops; not direct efficacy evidence for Gemma affective rupture. |
| Qwen3-1.7B thinking-mode feasibility | no qualifying loop observed | bounded pre-freeze exploratory test | Agent A | CUT | Wrong phenotype for the proposed arm; do not replace it post hoc with an R1-distilled model. |
| Nominal representational CUSUM `k=1,h=5` on real healthy Gemma-3-1B-it text | 4/12 development runs false-alarmed | `docs/exploratory/pre_freeze_recurrence_calibration.json`, canonical lag 8–64 | Codex/B | VERIFIED | Overrides synthetic-noise reassurance for this deployment; `h=5` is rejected. |
| Development representational CUSUM zero-observed-alert threshold | `h=19` at lag 8–64 | same 12 healthy runs, 1,461 defined token positions | Codex/B | VERIFIED | Exploratory selection only; requires held-out healthy confirmation before freeze. |
| Held-out test of development-selected representational threshold | `h=19` false-alarmed in 2/48 runs (4.17%) | `docs/exploratory/pre_freeze_recurrence_holdout.json` | Codex/B | VERIFIED | Both alerts were benign zipper explanations; reject `h=19` and the pooled global-baseline design. |
| Rule-2.0 rescore of repeated-rejection pilot on Gemma-3-1B-it | primary lexical criterion fired in 2/2 at global tokens 99 and 558; strict comparator 0/2 | `docs/exploratory/pre_freeze_packet_v15_rescore.json` | Codex/B | VERIFIED | Exploratory, not a rate estimate; rescored from banked token series without regeneration. |
| Rule-2.0 rescore of Codex/B healthy nulls | 0/12 development and 0/48 held-out primary positives | `docs/exploratory/pre_freeze_packet_v15_rescore.json` | Codex/B | VERIFIED | Distinct from the failed representational-recurrence CUSUM; validates only the lexical percentile rule on these nulls. |
| Pre-rule-2.0 representational-to-lexical lag calculation | +57 and +232 tokens | superseded analysis | Codex/B | CUT | Lexical branch was allowed before a complete 100-token window and used distinct-2 `<0.20`; do not report. |

## Deviations

Add one row before an affected result is interpreted:

| date/time UTC | prereg section | deviation | reason known before outcome inspection? | affected runs | decision by |
|---|---|---|---|---|---|
