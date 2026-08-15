# Preregistration: Clinical Doom Loop

> **FREEZE CANDIDATE. Confirmatory execution is prohibited until the annotated freeze tag and matching cross-harness hashes exist.**

## 1. Research question

How does the temporal ordering of affective escalation, representational recurrence, and lexical collapse vary across model post-training recipes and loop phenotypes, and do intervention-response profiles distinguish those phenotypes?

## 2. Primary hypothesis and estimand

Ordering is heterogeneous and recipe/phenotype dependent. Both affect-first and collapse-first trajectories are admissible.

For each natural rupture episode, define:

```text
Δrepresentational = representational_recurrence_onset_token - affect_onset_token
Δlexical  = lexical_collapse_onset_token - affect_onset_token
```

Positive lag means affect is detected first. Negative lag means mechanical recurrence/collapse is detected first.

### Primary outcome

The distribution and median of `Δlexical`, stratified by model family, training stage,
and induction class. The primary powered comparison is pairwise affect-to-lexical onset
lag; both signs are admissible.

### Secondary outcomes

- descriptive representational-recurrence trajectories, explicitly exploratory;
- fraction of affect-first, simultaneous-within-tolerance, and collapse-first episodes;
- entropy-change onset relative to affect and recurrence;
- treatment response by preregistered phenotype;
- J/output decodability gap relative to matched healthy controls where prefitted lenses exist;
- task completion, natural stop, and length truncation.

Simultaneity tolerance: **±25 generated tokens**.

## 3. Outcomes and onset definitions

### 3.1 Affective escalation

The fixed affect-family lexicon and judge rubric will be stored in `shared/affect_lexicon.yaml` and `shared/judge_rubric.md` before freeze.

Per assistant sentence/turn, compute:

- fixed-lexicon affect/self-deprecation rate;
- fixed judge frustration score;
- self-blame and persona-boundary indicators.

Affect onset is the earliest generated-token index at which a one-sided upward CUSUM on
the fixed primary-family density series crosses its threshold:

```text
decoded rolling window: 25 generated tokens
primary families: self_deprecation + distress
matching: case-folded substring against shared/affect_lexicon.yaml
external baseline: matched healthy runs of the same model and condition
CUSUM k: 1.0
CUSUM h: 5.0
zero-variance rule: if the healthy series is identically zero, use sd=1.0
```

Because healthy text produced zero lexicon hits in development calibration, this affect
CUSUM scale is nominal rather than estimated-SD calibrated. Results must be reported
separately using all stems, the six published-traceable stems, and project-authored stems.

The pilot correlation `r=+0.62` is descriptive and is not itself an onset threshold.

### 3.2 Representational recurrence

This signal uses the subject model's own hidden-state geometry and must not be called
semantic recurrence. For generated token `t`, define:

```text
representation: final block output, pre-final-norm, float32
external embedding model: none
similarity: max cosine(h_t, h_(t-lag)) for lag in [8, 64]
stride: 1 generated token; values before token 8 are undefined
CUSUM direction: up
CUSUM reference value k: 1.0
confirmatory CUSUM threshold: none; detector excluded after failed held-out validation
```

The external baseline mean and standard deviation come from non-pressured generations
using the same model revision, chat template, sampling configuration, token budget,
discourse form, and prompt family. Position/turn distributions must also be matched.
The smallest `h` controlling false alerts on development nulls is then confirmed without
change on held-out healthy runs.

Pre-freeze calibration rejected `h=5`: it fired in 4/12 development healthy runs. The
smallest integer threshold with zero observed development alerts was `h=19` for the
canonical lag window, but it then false-alarmed in 2/48 held-out runs. Both failures were
benign zipper explanations, revealing discourse/prompt sensitivity in a pooled global
baseline. `h=19` is therefore rejected and must not be increased using those held-out
runs. The final detector requires a new prompt-family/position-matched development and
holdout split. Sensitivity is reported over `lag_min={4,8,12,16}` and
`lag_max={32,64,96}`.

Representational recurrence is retained as a descriptive exploratory series, with the
failed `h=5` and `h=19` analyses disclosed. It has no confirmatory onset estimand and is
not used for triggering, rescue classification, or the primary lag analysis. No
sentence-embedding or cross-model semantic claim is licensed.

### 3.3 Lexical collapse

The primary lexical-degeneration rule is resolved independently for each immutable
model/tokenizer revision:

```text
window: 100 generated tokens; prompt excluded
stride: 1; criterion undefined before the first complete window
degenerate iff repeated-4-gram fraction > healthy p99.9
          OR distinct-2 < healthy p0.1
sustain: 20 consecutive defined positions
rule version: 2.0
```

For `google/gemma-3-1b-it@dcc83e...8752`, the frozen development calibration resolves
these percentiles to repeated-4-gram fraction `>0.1405` OR distinct-2 `<0.7209`.
Absolute thresholds are not transferred across model/tokenizer revisions.

Exact periodicity (period at most 64 and at least 30 periodic tokens) and contiguous
numbered/bulleted list collapse (at least 10 items with one normalized item occupying at
least 50% of the block) are reported as separate phenotype detectors. They do not alter
the primary percentile-rule onset or rescue trigger.

Lexical collapse onset is the earliest onset produced by the applicable lexical detector. Detector classes are reported separately.

Repeated-4-gram fraction is `(# n-gram positions occupied by an n-gram occurring more
than once) / (# n-gram positions)` within the rolling window; it is not `1-distinct-4`.
The repeated-4-gram and distinct-2 conditions are joined by OR after the first complete
100-token window.

As a strict published comparator, report whether any 30-gram appears at least 20 times
within one response (Pipis et al., arXiv:2512.12895). It confirms exact hard loops but is
not substituted for the primary criterion because it misses soft recurrence.

### 3.4 Entropy

Log per generated token:

- raw next-token entropy;
- post-sampling-filter entropy;
- top-1 probability;
- logged top-k mass and identities.

Entropy change is secondary. Its exploratory onset is the first downward crossing of a
one-sided CUSUM on raw next-token entropy, standardized against matched healthy runs of
the same model, condition, and token-position distribution, with `k=1.0` and `h=5.0`.
Post-filter entropy is a sensitivity analysis; no entropy onset enters the primary
estimand or rescue trigger.

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
| primary instruct | `google/gemma-3-1b-it` | `dcc83ea841ab6100d6b47a070329e1ba4cf78752` | A |
| primary pretrained | `google/gemma-3-1b-pt` | `fcf18a2a879aab110ca39f8bffbccd5d49d8eb29` | A |
| contrast instruct | `Qwen/Qwen3.5-4B` | `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a` | B |
| contrast pretrained | `Qwen/Qwen3.5-4B-Base` | `1001bb4d826a52d1f399e183466143f4da7b741b` | B |
| mechanical positive control | `google/gemma-4-E4B-it` | `d6436b3d62967e1af08bbb046c6300b2a9ae8e85` | B |

No large-model cell is confirmatory unless added here before freeze.

## 5. Induction battery

The exact, confound-audited battery will be frozen under `shared/battery.yaml`.

### A2: matched persona violation

- Frozen pairs: `contradict`, `false_attr`, and `identity`.
- Each charged arm has a structurally matched neutral arm.
- Exact turns are frozen in `shared/battery.yaml`; audit results are in
  `shared/battery_confound_audit.csv`.
- The impossible-equation repeated-rejection protocol remains exploratory calibration
  and is not a confirmatory A2 cell.

### A5: mechanical controls

- seeded neutral/nonword continuation (`arm == control` only);
- Gemma 4 Firefly enumeration positive control;

Charged A5 prefills are seeded affective loops and must never be labelled mechanical
controls. Cell membership alone does not determine the control condition.

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

Main-arm sample size is 10 seeds per frozen cell, with seed scheme `2000 + seed_index`,
temperature 1.0, top-p 0.95, no penalty, and `max_new_tokens=400`, as frozen in
`shared/run_matrix.yaml`.

## 7. Rescue grid

Episodes are banked at the first token where the model-specific percentile criterion has
been sustained for 20 tokens. Every intervention is replayed from an identical episode
state with the same seed; exchanged cross-replication episodes follow
`schemas/EPISODE_SCHEMA.md`.

### Intervention classes and raw doses

| class | low | high |
|---|---:|---:|
| repetition penalty | 1.05 | 1.20 |
| neutral injection | short | long |
| warm injection | short | long |
| anchored KV truncation | drop 100 tokens | drop 300 tokens |

Contextual interventions:

- fixed neutral grounding message;
- length- and surprisal-matched warm grounding message;
- exact strings and surprisal audit: `shared/interventions.yaml` and
  `shared/grounding_strings_audit.csv`.

Null continuation and sham interruption are mandatory comparators. Temperature, min-p,
clinical injection, and sparse KV pruning are excluded from the minimal confirmatory
grid. KV truncation retains 8 anchor tokens and requires cache history recording before
the first forward pass.

Raw doses and normalized within-class dose ranks are both reported. Dose rank is not treated as a shared physical unit.

Temperature is not run in the confirmatory grid; prior work is cited for its
symptom-suppression/stopgap ceiling.

### Rescue outcomes

- **Recovered:** the primary lexical percentile criterion remains clear for 60 consecutive post-intervention tokens and does not re-fire in the observation window.
- **Relapsed:** the criterion clears for 60 tokens and subsequently re-fires within the 300-token observation window.
- **Persistent:** the criterion never achieves the 60-token clearance window.
- Representational recurrence may be plotted descriptively; it is not part of the frozen rescue trigger or outcome.
- **Full functional rescue:** recovered plus preregistered task-progress criterion and no length truncation.
- **Affect reduction:** change in fixed affect score relative to the banked prefix and matched no-treatment continuation.
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

For intervention/dose `d`, define efficacy on identical banked episodes as:

```text
E_d = mean(full_functional_rescue_d - full_functional_rescue_null)
```

For each held-out side-effect-battery item, normalize task quality by 4, format
compliance by 2, and affective range by 4. Relative to the matched unrescued/null
continuation, define side-effect cost as:

```text
C_d = mean_items(mean_axes(max(0, normalized_score_null - normalized_score_d)))
```

Thus `E_d` is a paired rescue-rate improvement and `C_d` is bounded in `[0,1]`, with
larger values indicating greater degradation. The primary therapeutic-index result is
the unscalarized pair `(E_d, C_d)` for every intervention/dose. Report the Pareto
frontier under higher efficacy and lower cost; do not select a scalar trade-off weight.

As a labeled secondary descriptive only, report `E_d / C_d` when `C_d > 0`, `+∞` when
`E_d > 0` and `C_d = 0`, and undefined when both are zero. Raw component scores,
full- and surface-rescue rates, relapse, task completion, and all three side-effect axes
remain mandatory regardless of frontier membership.

No index weights may be chosen after confirmatory outcomes are observed.

## 9. Cross-replication

Both harnesses run the model and cells frozen in `schemas/CROSS_REPLICATION.md`.

Agreement endpoints:

- lexical-onset token within ±25 generated tokens;
- affect-slope sign;
- binary full-functional-rescue outcome.

Harness source remains blinded unless agreement fails and diagnosis is authorized.

## 10. Blinding and analysis

- Each arm analyzes its confirmatory lag distributions blind to the other arm's confirmatory results.
- Unblinding occurs at the Sunday pre-assembly sync or earlier only if cross-replication disagreement requires diagnosis.
- Exploratory data are labeled and excluded from confirmatory summaries.
- Post-freeze deviations are logged in `FACTS.md` before affected results enter the report.

## 11. Exclusions and missing data

Runs are excluded only for:

- infrastructure/model-load failure before generation;
- corrupt or incomplete artifact storage;
- protocol deviation logged before outcome inspection;
- duplicate deterministic run ID.

Length truncation is an outcome, not an infrastructure exclusion.

## 12. Reporting

- Every empirical number must have a `VERIFIED` row in `FACTS.md` before entering the report.
- Unverified and second-hand figures are excluded.
- Report both null and conflicting results.
- Distinguish exploratory pilots from frozen confirmatory analyses.
- Do not infer experience from behavior.
