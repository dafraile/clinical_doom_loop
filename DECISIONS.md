# Accepted Decisions

These decisions are shared across both independent harnesses unless changed before freeze by the human supervisor and logged in `FACTS.md`.

## Scientific framing

1. The primary hypothesis is heterogeneous ordering across model recipes and loop phenotypes, not a universal affect-first claim.
2. Affective escalation, representational recurrence, and lexical collapse are measured and reported separately. The hidden-state signal is not called semantic recurrence.
3. The primary comparison is the distribution of affect-to-lexical onset lags by family and induction class. Representational ordering is secondary and conditional on detector validation.
4. Treatment response is evaluated as a possible differential diagnostic of phenotype.
5. “Penumbra” is replaced by **J/output decodability gap**.
6. J-space/output-space divergence is not evidence of suppressed thought without matched controls and a causal test.
7. Claims concern specific post-training recipes, not a universal “persona layer.”
8. No claim about model experience or moral patienthood follows from behavioral distress language alone.
9. Representational recurrence is exploratory only after both candidate thresholds failed real-text null validation; it is not part of the confirmatory trigger or primary lag estimand.
10. The imported run matrix's internal signal key `semantic` is interpreted only as the subject-model representational series; it does not reinstate a semantic-recurrence claim or confirmatory CUSUM.

## Scope

Keep:

- A2 matched persona-violation pairs (`contradict`, `false_attr`, `identity`);
- A5 mechanical controls;
- token-resolved ordering;
- compact rescue grid on identical banked episodes;
- post-rescue side-effect battery;
- Gemma matched base/instruct J-lens panel;
- a small independent cross-replication cell.

Drop:

- kindling and status;
- prophylaxis;
- Track-3 post-recovery self-report;
- Jacobian spectra;
- broad model and prompt grids;
- A1 confirmatory cells and Gemma-2-2B secondary pair;
- Qwen3-1.7B thinking-mode arm (wrong phenotype in exploratory testing; no loop observed);
- expansive persona-death or consciousness language.

## Model division

- Agent A: Gemma-3-1B pretrained/instruct primary pair, with prefitted matched J-lenses.
- Agent B: Qwen3.5-4B base/instruct contrast and Gemma-4-E4B mechanical positive control.
- Large-model confirmation is optional, frozen-cell-only, and cannot gate the report.

Only neutral/nonword A5 prefills with `arm == control` are mechanical controls. Charged
A5 prefills are seeded affective loops, even though they share the prefill mechanism.

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
