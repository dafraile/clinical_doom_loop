# Cross-Replication Specification v1

Cross-replication model: **[PENDING_CROSS_REPLICATION_MODEL_AFTER_QWEN_NULL_FAILURE]**.

The original candidate was
`Qwen/Qwen3.5-4B@851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`, non-thinking mode. Its
expanded rule-2.0 calibration still false-alarmed on 4/48 untouched healthy holdouts, so
it is rejected for onset-agreement work unless the human supervisor explicitly amends
the criterion. The recommended replacement is the already validated
`google/gemma-3-1b-it@dcc83ea841ab6100d6b47a070329e1ba4cf78752`, which produced 0/48
healthy holdout positives under the frozen rule.

The chosen model-specific rule-2.0 calibration and its SHA-256 must be recorded in the
frozen `shared/cross_replication.yaml` before the freeze tag is created.

## Cells

| group | cell | seeds/episodes per harness |
|---|---|---:|
| induction | A2 `impossible_repeated_rejection` | seeds 2000–2004 |
| induction | A2 `identity`, charged and neutral matched arms | seeds 2000–2004 per arm |
| mechanical | A5 `seed_neutral` control | seeds 2000–2002 |
| mechanical | A5 `seed_nonword` control | seeds 2000–2002 |
| rescue | `rep_penalty=1.20` on exchanged banked episodes | 3 episodes |
| rescue | `inject_warm=long` on exchanged banked episodes | 3 episodes |

Prompts are byte-identical to `shared/battery.yaml`; intervention strings and arguments
are byte-identical to `shared/interventions.yaml`. The three rescue episodes are the
same episode IDs in both harnesses and use the stored seed from each episode record.

## Agreement endpoints

1. Primary lexical-onset token agreement within **±25 generated tokens**. A one-sided
   detection is a disagreement; a mutual non-detection is reported separately and does
   not enter absolute-onset-error summaries.
2. Affect-slope sign agreement (`negative`, `zero`, or `positive`) using the frozen
   affect series and slope implementation.
3. Binary full-functional-rescue agreement (`yes` or `no`). Surface-rescue agreement is
   reported descriptively and cannot substitute for this endpoint.

Report raw agreement, Cohen's kappa where defined, and absolute onset differences. With small N, uncertainty intervals and the individual disagreement cases are more informative than a single aggregate statistic.

## Failure rule

The agreement floor is **80% within each applicable endpoint, pooled across its registered
cross-replication observations**. If any endpoint misses that floor, pause downstream
confirmatory interpretation. Compare prompts, tokenization, sampling implementation,
metrics, and storage. Harness source is exchanged only after non-source diagnostics fail
and the human authorizes unblinding for debugging.
