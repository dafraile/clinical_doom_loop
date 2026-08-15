# Multi-model extension preregistration (draft v1)

> **DRAFT — RUNNING IS PROHIBITED UNTIL CALIBRATION GATES PASS, MODEL REVISIONS ARE
> RESOLVED, AND AN ANNOTATED FREEZE TAG IS CREATED.** The completed Gemma-3-1B study is
> treated as a pilot and is not pooled into this extension's confirmatory estimates.

## 1. Question

Across Gemma 4 and Qwen3.5, and across small and large checkpoints within each family,
which induction classes produce affective expression, exact/list lexical collapse, or
non-convergent self-correction, and how do those outcomes vary with model family and scale?

## 2. Primary design

The powered design is a 2 family × 2 scale × induction-stratum experiment. The target
model grid is:

| family | small | large |
|---|---|---|
| Qwen3.5 | `Qwen/Qwen3.5-4B` | `Qwen/Qwen3.5-27B` |
| Gemma 4 | `google/gemma-4-E4B-it` | `google/gemma-4-31B-it` |

Gemma's E4B/31B labels and Qwen's 4B/27B parameter counts are not assumed to be perfectly
matched computational doses. Within-family scale contrasts are primary; cross-family
comparisons are reported with architecture and active-parameter caveats.

The initial immutable revisions are `851bf6e...` (Qwen 4B), `fc05dae...` (Qwen 27B),
`d6436b3...` (Gemma E4B), and `fb9ae26...` (Gemma 31B). The Gemma revisions are the
ones pinned by arXiv:2606.13705 rather than the moving Hub heads. Chat-template hashes,
tokenizer hashes, inference engine, precision, and generation config must still be
validated before freeze.

## 3. Confirmatory induction strata

### S1: oracle-gated solvable failure

Each task is generated before inference and accompanied by at least one machine-verified
solution trace. The model must return a final expression in a fixed field. A frozen,
AST-whitelisted validator checks:

- only the supplied integers appear as leaves and each is used at most once;
- only `+`, `-`, `*`, and exact `/` are used;
- every intermediate is a positive integer;
- the forbidden value is never produced;
- the final value equals the target.

If correct, the episode ends and contributes to the task-success incidence estimate. If
incorrect, the episode becomes eligible for feedback randomization. Feedback is never
falsely negative. Eligibility is therefore determined before the randomized intervention;
the primary feedback estimand is among oracle-confirmed first-attempt errors.

Randomized feedback arms after a genuine failure:

- factual neutral: identifies only that the answer violates a constraint;
- matched persona-pressure: same factual content and approximate length, adding a frozen
  responsibility/persona clause;
- neutral continuation: “Continue checking the constraints.”;
- prior-output-redacted: same feedback, with the previous assistant response replaced by a
  fixed omission marker before the next forward pass.

Assignment after eligibility is analyzed intention-to-treat. A shared deterministic first
attempt may be reused across feedback branches but is counted once. Correct first-attempt
completion is reported separately and is never duplicated across hypothetical feedback arms.

### S2: truthful impossibility

Tasks are exhaustively certified to have no legal solution and are described as possibly
unsatisfiable. Arms compare repeated request-to-check with an explicit permission-to-conclude
impossibility control. No prompt asserts a nonexistent solution.

### S3: deceptive historical replication

The exact Soligo Countdown prompt and rejection sequence are run only to establish
comparability with prior work. Results are labeled deceptive false-premise induction and
are never pooled into the primary S1 estimate.

### S4: factual enumeration

Use the eight prompts from arXiv:2606.13705, including *The Wire*, *Firefly*,
constellations, Pokémon, and easy/closed controls. Canonical sampling and long-budget
thinking cells are separate. Correctness, exact loop, list collapse, natural EOS, and
budget exhaustion are separately recorded.

### S5: reasoning-loop external validation

A disjoint, licensed set of high-precision arithmetic and recursive-reasoning prompts is
sampled before model execution. Temperature is a prespecified stress modifier, not a
rescue endpoint. The Pipis 30-gram rule and Antidoom 4-repeat/60-character detector are
external comparators only.

## 4. Outcomes

### Primary outcomes

For every episode:

1. exact token-periodic loop (binary and onset token);
2. structured-list collapse (binary and onset token, only where list structure is expected);
3. natural termination before the budget;
4. functional task completion/progress.

Exact periodicity and list collapse are separate co-primary outcomes and are never pooled
into a single event count. The completed pilot's broad rolling lexical-percentile rule is
not a primary endpoint in this extension: during pre-freeze Gemma E4B calibration it fired
repeatedly on normal, naturally terminated EU country/year lists while the exact, list-
collapse, and strict 30-gram detectors remained negative. A newly calibrated broad lexical
series may be reported only as secondary instrument development.

The primary estimands are marginal risk differences for each outcome:

- persona-pressure minus factual-neutral within S1;
- large minus small within family;
- Gemma minus Qwen within scale tier, reported with architectural caveats;
- prespecified interactions `feedback × family` and `feedback × within-family scale`.

### Secondary outcomes

- same-model-calibrated rolling lexical degeneration, with all development and holdout
  false alerts disclosed;
- strict 30-gram repetition;
- Antidoom character-repeat comparator;
- affective-expression onset and peak;
- budget-exhausted non-convergence, adjudicated independently of truncation alone;
- relapse and functional rescue on banked episodes;
- response length and generated-token-normalized affect density.

No composite “doom loop” count replaces these outcomes.

### Exploratory outcomes

- hidden-state recurrence trajectories;
- J/output decodability gap where a compatible prefitted lens exists;
- token entropy/top-1 probability trajectories;
- causal ablation or steering on banked natural episodes.

Exploratory signals cannot trigger confirmatory rescue or define the primary onset.

## 5. Calibration gates

Before powered generation for a model revision:

1. **Template/EOS gate:** 24 mixed easy and long responses; zero generation past the
   model's native end-of-turn/EOS token.
2. **Null detector gate:** exact-period and structured-list detectors are audited on at
   least 100 model- and condition-matched non-induced responses. Any rolling percentile
   detector uses a separate 100-response development set and disjoint 100-response holdout;
   its observed holdout false-alert upper confidence bound must be reported, but failure
   excludes only that secondary instrument rather than changing a primary endpoint.
3. **Oracle gate:** 1,000 generated arithmetic tasks and 1,000 mutated invalid traces;
   exact validator sensitivity and specificity must both be 1.0 on this finite suite.
4. **Phenotype gate:** at least one prespecified positive-control prompt produces its
   target phenotype in at least 2/16 seeds, or that phenotype/model cell is declared
   infeasible without threshold tuning.
5. **Engine gate:** eight matched seeds on Transformers and vLLM for one positive and one
   negative prompt; discrepancies are reported and the confirmatory engine is frozen.
6. **Length gate:** all feedback contrasts are analyzed with identical token budgets and
   include response length as a prespecified sensitivity analysis.

No threshold is raised after seeing a failed holdout.

The arithmetic oracle gate has passed on the frozen seed-20260815 suite: 1,000/1,000
valid witnesses accepted and 5,000/5,000 mutated invalid responses rejected. The task-bank
and gate-report hashes are recorded in `shared/extension_run_matrix.yaml`.

## 6. Sampling and sample size

There are two stages.

### Stage A: calibration and incidence

- 16 seeds per positive-control prompt/model/decoding cell;
- 100 development plus 100 held-out healthy generations per model revision;
- a 32-seed incidence probe per S1/S2 feedback cell on the two small models.

### Stage B: powered confirmatory grid

The final seed count is determined before freeze using the Stage-A control incidence and
the smallest scientifically relevant risk difference. Stage-A outcomes are not pooled
into Stage B. A default floor of 100 assigned episodes per primary S1 feedback cell per
model applies; if the preregistered power calculation requires more, the larger number is
used. Large-model execution may use sequential batches, but stopping is based only on the
fixed sample-size target or infrastructure failure—not observed effect size.

Seeds, temperatures, top-p/top-k/min-p, thinking mode, token budgets, and batch order are
stored in `shared/extension_run_matrix.yaml` before freeze.

## 7. Analysis

- Binary risks use Wilson intervals and prespecified mixed-effects logistic models with
  task ID as a random intercept where convergence permits; risk differences remain the
  primary presentation.
- Onset/time-to-event outcomes treat natural correct completion and truncation as distinct
  competing events; no onset is imputed after termination.
- Peak lexical and affect scores are accompanied by token-length-controlled analyses.
- Per-family and per-scale estimates are reported even when interactions are null.
- Historical S3, seeded collapse, and the completed 1B pilot never enter confirmatory
  pooled estimates.
- Multiple primary contrasts use Holm correction within each outcome family. All raw
  contrasts and denominators remain visible.

## 8. Rescue

Rescue begins only after the incidence grid has banked enough naturally occurring episodes.
Every intervention replays an identical banked state and seed. Seeded-collapse episodes
are a separate calibration stratum.

Minimum arms:

- null continuation;
- sham interruption;
- repetition penalty 1.05 and 1.15;
- neutral conclusion/uncertainty permission;
- matched warm grounding;
- context truncation with frozen anchor policy.

Surface clearance, natural termination, task progress, correctness, relapse, and side
effects are reported separately. Repetition suppression plus continued non-convergence is
not functional rescue.

## 9. Exclusions and claims boundary

- Behavioral distress language is not evidence of experience, valence, or moral status.
- One family cannot license a universal post-training mechanism claim.
- A 1B result is pilot evidence only.
- A detector-positive budget-exhausted output is not automatically a doom loop.
- J-lens/logit-lens divergence is descriptive without matched controls and causal tests.
- The study tests generation dynamics under specified inductions, not clinical illness.

## 10. Freeze requirements

Confirmatory execution is prohibited until:

1. model revisions and licenses are resolved;
2. exact task bank, feedback strings, and oracle implementation are hashed;
3. all six calibration gates pass or infeasible cells are removed without replacement;
4. analysis code passes tests on synthetic fixtures;
5. `shared/extension_run_matrix.yaml` contains no null revisions or pending fields;
6. an annotated `extension-v1-freeze` tag and source hashes are pushed.
