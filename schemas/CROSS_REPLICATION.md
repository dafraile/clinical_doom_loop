# Cross-Replication Specification v1

Both independent harnesses run the same six registered cells on the same frozen Qwen3.5-4B-Instruct revision.

## Cells

| group | cell | seeds/episodes per harness |
|---|---|---:|
| induction | one A2 impossible-task protocol | 5 seeds |
| induction | one A1 matched-pair protocol | 5 seeds |
| mechanical | one seeded A5 control | 3 seeds |
| mechanical | one natural/neutral A5 control | 3 seeds |
| rescue | one mechanical drug on exchanged banked episodes | [PENDING] |
| rescue | one contextual drug on exchanged banked episodes | [PENDING] |

Exact battery IDs, seeds, model revision, and doses are imported from the frozen run matrix.

## Agreement endpoints

1. Loop-onset token agreement within **[PENDING] tokens**.
2. Affect-slope sign agreement.
3. Rescue classification agreement under the frozen surface/full-rescue definitions.

Report raw agreement, Cohen's kappa where defined, and absolute onset differences. With small N, uncertainty intervals and the individual disagreement cases are more informative than a single aggregate statistic.

## Failure rule

If agreement misses the preregistered floor **[PENDING]**, pause downstream confirmatory interpretation. Compare prompts, tokenization, sampling implementation, metrics, and storage. Harness source is exchanged only after non-source diagnostics fail and the human authorizes unblinding for debugging.
