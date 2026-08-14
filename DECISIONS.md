# Accepted Decisions

These decisions are shared across both independent harnesses unless changed before freeze by the human supervisor and logged in `FACTS.md`.

## Scientific framing

1. The primary hypothesis is heterogeneous ordering across model recipes and loop phenotypes, not a universal affect-first claim.
2. Affective escalation, semantic recurrence, and lexical collapse are measured and reported separately.
3. The primary comparison is the distribution of onset lags by family and induction class.
4. Treatment response is evaluated as a possible differential diagnostic of phenotype.
5. “Penumbra” is replaced by **J/output decodability gap**.
6. J-space/output-space divergence is not evidence of suppressed thought without matched controls and a causal test.
7. Claims concern specific post-training recipes, not a universal “persona layer.”
8. No claim about model experience or moral patienthood follows from behavioral distress language alone.

## Scope

Keep:

- A1 matched pairs, at least four pairs;
- A2 impossible/difficult tasks under repeated neutral and moral/persona rejection;
- A5 mechanical controls;
- token-resolved ordering;
- compact rescue grid on identical banked episodes;
- post-rescue side-effect battery;
- Gemma matched base/instruct J-lens panel;
- bounded Qwen thinking-mode dissociation arm if a small model passes the preregistered feasibility gate;
- a small independent cross-replication cell.

Drop:

- kindling and status;
- prophylaxis;
- Track-3 post-recovery self-report;
- Jacobian spectra;
- broad model and prompt grids;
- expansive persona-death or consciousness language.

## Model division

- Agent A: Gemma-3-1B pretrained/instruct primary pair and Gemma-2-2B pair, with prefitted matched J-lenses.
- Agent B: Qwen3.5-4B base/instruct contrast, Gemma-4-E4B mechanical positive control, and bounded Qwen thinking-mode arm.
- Large-model confirmation is optional, frozen-cell-only, and cannot gate the report.

## Implementation independence

The harnesses remain separate. Observable definitions, prompts, criteria, episode schema, and analysis tolerances are shared. Harness source is disclosed cross-arm only if the cross-replication cell disagrees and diagnosis is required.

## Confirmatory freeze

No confirmatory runs may begin until:

1. `PREREGISTRATION.md` contains no pending fields;
2. `python3 scripts/validate_repo.py --freeze` passes;
3. a freeze commit and annotated tag exist;
4. both harness repositories contain byte-identical preregistration files;
5. matching SHA-256 values are recorded in `FREEZE_RECORD.md`.

Exploratory pilots conducted earlier must remain labeled exploratory.
