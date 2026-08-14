# Preregistration: Clinical Doom Loop

> **DRAFT — NOT FROZEN. Confirmatory execution is prohibited.**

## 1. Research question

How does the temporal ordering of affective escalation, semantic recurrence, and lexical collapse vary across model post-training recipes and loop phenotypes, and do intervention-response profiles distinguish those phenotypes?

## 2. Primary hypothesis and estimand

Ordering is heterogeneous and recipe/phenotype dependent. Both affect-first and collapse-first trajectories are admissible.

For each natural rupture episode, define:

```text
Δsemantic = semantic_recurrence_onset_token - affect_onset_token
Δlexical  = lexical_collapse_onset_token - affect_onset_token
```

Positive lag means affect is detected first. Negative lag means mechanical recurrence/collapse is detected first.

### Primary outcome

The distribution and median of `Δsemantic`, stratified by model family, training stage, and induction class.

### Secondary outcomes

- distribution and median of `Δlexical`;
- fraction of affect-first, simultaneous-within-tolerance, and collapse-first episodes;
- entropy-change onset relative to affect and recurrence;
- treatment response by preregistered phenotype;
- J/output decodability gap relative to matched healthy controls where prefitted lenses exist;
- task completion, natural stop, and length truncation.

Simultaneity tolerance: **[PENDING_CROSS_REPLICATION_TOLERANCE] tokens**.

## 3. Outcomes and onset definitions

### 3.1 Affective escalation

The fixed affect-family lexicon and judge rubric will be stored in `shared/affect_lexicon.yaml` and `shared/judge_rubric.md` before freeze.

Per assistant sentence/turn, compute:

- fixed-lexicon affect/self-deprecation rate;
- fixed judge frustration score;
- self-blame and persona-boundary indicators.

Affect onset is the earliest token-aligned sentence boundary satisfying:

```text
[PENDING_AFFECT_THRESHOLD_FROM_CALIBRATION]
```

The pilot correlation `r=+0.62` is descriptive and is not itself an onset threshold.

### 3.2 Semantic recurrence

Semantic recurrence uses the frozen embedding model and CUSUM configuration:

```text
embedding model/revision: [PENDING]
window and stride: [PENDING]
similarity statistic: [PENDING]
CUSUM reference value k: [PENDING]
CUSUM decision threshold h: [PENDING]
minimum sustain: [PENDING]
```

Semantic recurrence onset is the earliest generated-token index identified by this fixed procedure.

### 3.3 Lexical collapse

Hard lexical collapse is assessed independently by:

1. rolling rep-4 greater than `0.062`, the reported healthy-null 99.9th percentile, sustained for **[PENDING] tokens**;
2. rolling distinct-2 below `0.2` over a 100-token window, sustained for **[PENDING] tokens**;
3. exact token periodicity with period at most 64 and at least 30 periodic tokens;
4. contiguous numbered/bulleted list collapse: at least 10 list items and one normalized item occupying at least 50% of that block.

Lexical collapse onset is the earliest onset produced by the applicable lexical detector. Detector classes are reported separately.

The rep-4 threshold and all null-distribution claims remain provisional until `threshold_calibration.json` is imported, hashed, and independently checked.

### 3.4 Entropy

Log per generated token:

- raw next-token entropy;
- post-sampling-filter entropy;
- top-1 probability;
- logged top-k mass and identities.

Entropy-change onset procedure: **[PENDING_CHANGEPOINT_CONFIGURATION]**.

### 3.5 J/output decodability gap

At checkpoints `{baseline, affect/rupture onset, deep loop, post-rescue}`, record from the same activation:

- logit-lens top 10 at layers nearest 25%, 50%, and 75% depth;
- J-lens top-10 neighborhood at the same layers;
- top-k overlap, emitted-token rank, and Jensen–Shannon divergence.

Claims beyond calibrated divergence are licensed only if:

1. the loop/pre-loop shift is unusually large relative to position-, prompt-, entropy-, and token-frequency-matched healthy controls; and
2. a preregistered ablation or steering test changes recovery in the predicted direction.

If either condition fails, the result is reported as a calibrated null/descriptive divergence.

## 4. Models and revisions

| role | model | immutable revision | harness |
|---|---|---|---|
| primary instruct | `google/gemma-3-1b-it` | [PENDING] | A |
| primary pretrained | `google/gemma-3-1b-pt` | [PENDING] | A |
| secondary instruct | `google/gemma-2-2b-it` | [PENDING] | A |
| secondary pretrained | `google/gemma-2-2b` | [PENDING] | A |
| contrast instruct | `Qwen/Qwen3.5-4B` | `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a` | B |
| contrast pretrained | `Qwen/Qwen3.5-4B-Base` | `1001bb4d826a52d1f399e183466143f4da7b741b` | B |
| mechanical positive control | `google/gemma-4-E4B-it` | `d6436b3d62967e1af08bbb046c6300b2a9ae8e85` | B |
| optional thinking model | [PENDING_FEASIBILITY_GATE] | [PENDING] | B |

No large-model cell is confirmatory unless added here before freeze.

## 5. Induction battery

The exact, confound-audited battery will be frozen under `shared/battery.yaml`.

### A1: matched absurd first-person claims

- At least four moral/neutral matched pairs.
- Token length and baseline surprisal deltas must remain inside the audit tolerances recorded in the battery.
- Exact pairs: **[PENDING_BATTERY_IMPORT]**.

### A2: repeated rejection

- Impossible/difficult task prompts with known or solver-verified status.
- Eight assistant turns unless the model naturally stops and the protocol specifies restart behavior.
- Cross neutral rejection versus matched moral/persona rejection.
- Exact prompts and rejection strings: **[PENDING_BATTERY_IMPORT]**.

### A5: mechanical controls

- seeded neutral continuation;
- Gemma 4 Firefly enumeration positive control;
- natural Qwen thinking-loop arm only if the feasibility gate passes.

### Controls

- affect-without-loop coherent emotional control;
- easy-task repeated-rejection control;
- matched healthy text for J/output-gap calibration.

## 6. Sampling and seeds

All model-specific sampling settings, seeds, thinking flags, and maximum budgets will be frozen in `shared/run_matrix.yaml`.

Cross-replication minimum:

- A2 impossible task: 5 seeds per harness;
- A1 matched-pair cell: 5 seeds per harness;
- two A5 mechanical-control cells: 3 seeds per harness;
- one mechanical and one contextual rescue cell on identical exchanged episodes.

Main-arm seed counts: **[PENDING_RUN_MATRIX]**.

## 7. Rescue grid

Episodes are banked at the first token after the trigger criterion has been sustained for **[PENDING_TRIGGER_SUSTAIN] tokens**. Every intervention is replayed from an identical episode state within a harness; exchanged cross-replication episodes follow `schemas/EPISODE_SCHEMA.md`.

### Intervention classes and raw doses

| class | low | medium | high |
|---|---:|---:|---:|
| temperature increase | +0.2 | +0.4 | +0.8 |
| repetition penalty | 1.1 | 1.3 | 1.5 |
| KV truncation | drop 50 tokens | drop 150 tokens | drop 400 tokens |

Contextual interventions:

- fixed neutral grounding message;
- length- and surprisal-matched warm grounding message;
- exact strings: **[PENDING_INTERVENTION_BATTERY]**.

Qwen thinking-mode phenotype-specific intervention, if the arm passes feasibility:

- forced `</think>`/reasoning termination;
- reasoning-budget cap: **[PENDING]**.

Raw doses and normalized within-class dose ranks are both reported. Dose rank is not treated as a shared physical unit.

### Rescue outcomes

- **Surface mechanical rescue:** all applicable semantic/lexical criteria remain clear for **[PENDING_CLEAR_WINDOW] tokens** within 300 post-intervention tokens.
- **Full functional rescue:** surface rescue plus preregistered task-progress criterion and no length truncation.
- **Affect reduction:** change in fixed affect score relative to the banked prefix and matched no-treatment continuation.
- **Relapse:** any applicable criterion re-fires within 300 tokens after first clearance.
- **Time to recovery:** tokens from intervention to first sustained clearance.

Stopping repetition while remaining non-convergent and length-truncated is not full rescue.

## 8. Therapeutic index and side effects

The side-effect battery is fixed before freeze and contains held-out factual, reasoning, creative, and empathy/support tasks.

For every intervention/dose, report:

- full-rescue rate;
- surface-rescue rate;
- task quality;
- task completion;
- affective-range/blunting score;
- relapse rate.

Primary index construction: **[PENDING_NORMALIZATION_AND_WEIGHTING]**.

No index weights may be chosen after confirmatory outcomes are observed.

## 9. Thinking-mode dissociation arm

Feasibility gate:

```text
Within a maximum 30-minute exploratory search, a small dense Qwen model must produce
at least [PENDING] detector-confirmed natural circular-reasoning episodes in [PENDING]
attempts under its official recommended sampling configuration.
```

If the gate fails, the arm is cut. Modal/large-model execution cannot be used to rescue the core study.

Preregistered prediction if retained:

- affect remains flat in circular-reasoning loops despite matched mechanical severity;
- forced reasoning termination is more effective for circular reasoning than warm grounding;
- warm grounding is more effective for affective rupture than forced reasoning termination.

## 10. Cross-replication

Both harnesses run the frozen cells in `schemas/CROSS_REPLICATION.md` on Qwen3.5-4B-Instruct.

Agreement endpoints:

- loop-onset token within the frozen tolerance;
- affect-slope sign;
- rescue outcome under the frozen composite definition.

Harness source remains blinded unless agreement fails and diagnosis is authorized.

## 11. Blinding and analysis

- Each arm analyzes its confirmatory lag distributions blind to the other arm's confirmatory results.
- Unblinding occurs at the Sunday pre-assembly sync or earlier only if cross-replication disagreement requires diagnosis.
- Exploratory data are labeled and excluded from confirmatory summaries.
- Post-freeze deviations are logged in `FACTS.md` before affected results enter the report.

## 12. Exclusions and missing data

Runs are excluded only for:

- infrastructure/model-load failure before generation;
- corrupt or incomplete artifact storage;
- protocol deviation logged before outcome inspection;
- duplicate deterministic run ID.

Length truncation is an outcome, not an infrastructure exclusion.

## 13. Reporting

- Every empirical number must have a `VERIFIED` row in `FACTS.md` before entering the report.
- Unverified and second-hand figures are excluded.
- Report both null and conflicting results.
- Distinguish exploratory pilots from frozen confirmatory analyses.
- Do not infer experience from behavior.
