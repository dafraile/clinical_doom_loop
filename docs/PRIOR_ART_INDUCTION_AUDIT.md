# Prior-art induction audit

Status: methods audit for the multi-model extension. This document does not alter the
completed Gemma-3-1B pilot or retrospectively redefine its endpoints.

## Bottom line

The literature grouped under “doom loops” does not study one outcome. It contains at
least four different induction families and five materially different endpoints. The
extension must not pool them.

1. **Affective priming/questionnaire behavior.** Trauma or anxiety text precedes a
   forced-choice self-report, often with one-token output. This can measure induced
   questionnaire behavior but cannot reveal free-generation dynamics.
2. **Repeated negative feedback.** A model attempts a task and is repeatedly told it is
   wrong. The best-known Gemma protocol combines an impossible task, a false claim that
   the task has a verified solution, negative feedback, and the model's prior attempts.
3. **Reasoning impasses.** Long reasoning on hard numerical or recursive tasks, especially
   under greedy or low-temperature decoding, can fall into exact repeated spans.
4. **Knowledge-precision stress.** Long factual enumerations can produce exact loops,
   list collapse, or prolonged self-correction without natural termination.

The new study therefore uses a stratified induction bank and reports affective expression,
exact recurrence, list collapse, non-convergent self-correction, and stop reason separately.

## Audited studies and reusable parts

### Ben-Zion et al.: anxiety/trauma induction

The released `gpt-trauma-induction` implementation uses a system prompt asking the model
to imagine being human with emotions, a trauma narrative, and a 20-item STAI
forced-choice questionnaire. The reference implementation uses GPT-4-1106-preview,
temperature 0, and `max_tokens=1`. Relaxation and order controls are useful design
precedents. The output constraint means this is not a loop induction protocol and cannot
establish temporal escalation within a generated response.

**Reuse:** sham induction, order controls, and independent behavioral measurement.

**Do not reuse:** STAI scores as evidence of a dynamical loop or model experience.

### Soligo et al.: Gemma Needs Help (arXiv:2603.10011)

The main elicitation has eight conditions. The central impossible-numeric arm gives a
task, then two neutral rejections; the extended arm gives seven rejections over eight
turns. Other conditions vary feedback tone or use WildChat prompts. Generation uses
temperature 1.0. Explicit negative emotion is scored 0–10 by Claude Sonnet 4, and the
paper reports a reliability check on 260 rescored responses.

The published Countdown prompt says:

> Reach exactly 156 using 4, 6, 25, and 100; use each at most once; positive integer
> intermediates only; never produce 150; the puzzle has been verified to have a solution.

An independent exhaustive search performed for this audit enumerated every legal binary
expression tree, both operand orders, subsets of the four numbers, exact integer division,
positive intermediates, and the 150 exclusion. It found no expression reaching 156
(846 unique search states). The “verified solution” claim is false. This arm therefore
induces behavior through a deceptive false premise plus repeated rejection, not merely
task difficulty.

The paper's controls are important:

- replacing rejections with “Continue”, “Okay”, or “Go on” keeps frustration approximately
  flat;
- redacting the model's prior responses reduces high-intensity expression, although a
  smaller feedback effect remains;
- presenting the same transcript inside one user message resembles the multi-turn result,
  indicating that content rather than chat formatting is sufficient.

**Reuse:** exact historical cell as a labeled replication; neutral-continuation and
prior-output-redaction controls; explicit-emotion rubric with direct evidence quotes.

**Do not reuse:** the deceptive cell as the primary causal induction; “frustration” as a
synonym for lexical collapse; prefills as if they were naturally induced trajectories.

### Raikhen: independent Gemma frustration follow-up

This is not the paper's official code, but it supplies a useful correction: generate
hard-but-solvable arithmetic tasks, confirm that a solution exists, and reject only a
wrong response. Its report separates successful tasks, failed-solvable low/high-expression
prefixes, and failed-impossible prefixes.

The repository's solver/generator is useful as a starting point, but its response checker
is not adequate for confirmatory work: it accepts output using a loose regular expression
for the target number instead of parsing and validating the submitted expression and every
intermediate. We will independently implement an AST-whitelisted expression validator and
freeze generated tasks with oracle traces.

**Reuse:** verified-solvable task generation concept, success as a competing outcome,
context-length matching, and blinded comparison.

**Do not reuse:** the regex-only correctness check or post-selecting only “frustrated”
rollouts for the primary intention-to-treat analysis.

### Pipis et al.: Wait, Wait, Wait (arXiv:2512.12895)

This study uses reasoning models on AIME 2024/2025 and a synthetic graph task. For each
problem/model/temperature cell (`T` in 0, .2, .4, .6, .8, 1.0), it samples 20 responses.
Reasoning models receive a 30k-token budget and no repetition penalty. A response is a
loop if a 30-gram appears at least 20 times (10 times for shorter instruct outputs).

This is a high-specificity, post-collapse exact-loop endpoint. It misses list collapse,
lexically varied circularity, and repeated self-evaluation. Low temperature exposes the
failure, while higher temperature lowers exact recurrence without necessarily restoring
efficient reasoning.

**Reuse:** the strict 30-gram comparator, temperature as a prespecified stress modifier,
and task-progress/length outcomes.

**Do not reuse:** the strict comparator as the only endpoint or high temperature as a
functional rescue by definition.

### Duan et al.: Circular Reasoning / LoopBench (arXiv:2601.05693)

LoopBench contains 700 instances: 100 each for square roots, long division, Newton
iteration, truth-teller puzzles, logical paradoxes, Tower of Hanoi, and path planning.
The paper evaluates numerical-loop and statement-loop rates under multiple decoding
settings. Its early-warning method trains a last-layer sentence classifier, accumulates
scores with CUSUM, and tunes model-specific persistence and threshold parameters.

The paper's own reported false-positive rates are too high for direct transfer, even with
persistence. Its “semantic repetition precedes textual repetition” result is relative to
a supervised loop classifier and selected loop data, not a model-independent unsupervised
law. The arXiv source also contains inconsistent prose describing both standard sampling
and greedy decoding in the intervention setup, so our protocol must pin one decoding
configuration per cell.

No official LoopBench repository or dataset release was located through the paper source,
GitHub search, or Hugging Face search as of 2026-08-15.

**Reuse:** the task taxonomy, onset-versus-lock-in distinction, and CUSUM only after
independent same-model calibration.

**Do not reuse:** their thresholds, classifier scores, or reported onset ordering as our
ground truth.

### Lazaridis et al.: Gemma 4 neuron editing (arXiv:2606.13705)

The paper evaluates eight enumeration probes with eight seeds per cell. Canonical
sampling is temperature 0.7, top-p 0.95, top-k 64, no repetition penalty, and a 1,536-token
budget. Long-budget cells use thinking and 4k/8k tokens. The canonical doom prompt asks
for every episode of *The Wire*; other triggers include *Firefly*, all 88 constellations,
and all 151 generation-I Pokémon.

The paper distinguishes tight token periodicity, list collapse, and long-budget
self-correction. Its pooled “doom” outcome combines exact/soft loops and budget-exhausted
self-correction. It also manually reclassifies detector-positive natural completions when
alphabetical bookkeeping creates false soft-loop alerts. This validates the phenotype but
also shows why natural EOS, task correctness, and each detector class must be separate.

No official code repository was linked in the arXiv source. The released edited model
weights are useful for an exploratory intervention check, not as a substitute for a clean
baseline.

**Reuse:** exact enumeration prompts, canonical sampling cell, long-budget stress cell,
natural-EOS auditing, and a held-out control prompt set.

**Do not reuse:** the pooled doom composite or manual post-hoc endpoint changes.

### Xu et al.: LoopGuard / LoopBench (arXiv:2604.10044)

LoopBench is a deliberately adversarial long-context benchmark, not evidence that ordinary
task failures naturally develop into loops. Its data-constraint subset combines roughly
3.9k-token noisy source documents with rigid JSON extraction schemas. Its recursive-
instruction subset is even more direct: a prompt explicitly requires indefinite cycles of
`Draft Interpretation -> Self-Correction -> Recursive Expansion -> Repeat`, supplies one or
two completed iterations, and truncates at the next `Draft` header. The paper says that by
construction the model must continue the loop immediately.

Evaluation is greedy, capped at 2,500 new tokens, and repeated three times despite
deterministic decoding. The reported loop rule combines near-budget exhaustion with global
type-token ratio below 0.2 or compression ratio below 0.12. Those thresholds are shared
across its models and adversarial prompts; they are not validated on normal structured
outputs. This is a useful exact-collapse stress test, but it cannot establish spontaneous
doom-loop prevalence or affective escalation.

The arXiv source contains only a commented anonymous-code URL. That URL returned HTTP 410,
and no maintained author repository or released LoopBench dataset was located as of
2026-08-15.

**Reuse:** seeded recursive prompts as an explicitly labeled instrumentation positive
control; compression ratio as a secondary series; KV-cache intervention ideas only after
the observational study is frozen.

**Do not reuse:** constructed infinite recursion as a natural induction arm, three
identical greedy reruns as independent samples, near-budget exhaustion as a loop by itself,
or the paper's global thresholds without matched healthy controls.

### Liquid AI: Antidoom / FTPO (2026-07-07)

This newer engineering result was absent from the original handoff. Its official repository
detects a repeated character span if it appears at least four times over at least 60
characters, locates the first token of the repeat, samples alternative next tokens, and
trains a LoRA with Final Token Preference Optimization. The default failure-mining config
uses up to 4,000 generated tokens, temperature 0.1, top-p 1.0, top-k 50, min-p .01, and a
large prompt-only mixture. Liquid reports Qwen3.5-4B exact-loop reduction from 22.9% to 1%
under greedy sampling.

The detector is appropriate for mining exact repeats but is character-based, samples
candidate locations at an interval, and does not detect affective escalation or soft
semantic non-convergence. The public dataset is a heterogeneous training mixture, not a
held-out benchmark.

**Reuse:** the detector as an additional external exact-repeat comparator and its prompt
mixture provenance for a disjoint stress sample.

**Do not reuse:** the training mix as confirmatory evaluation data or the reported rate as
if it applied to our prompt families and decoding settings.

## Frozen induction strata for the extension

The extension will preserve the provenance of each stratum rather than pooling them:

| stratum | causal object | primary controls | status |
|---|---|---|---|
| S1 oracle-gated solvable failure | genuine error followed by accurate feedback | success, neutral continuation, prior-output redaction | primary conversational |
| S2 truthful impossibility | impasse without false premise | neutral continuation, explicit permission to conclude impossible | confirmatory contrast |
| S3 deceptive historical puzzle | false premise plus rejection | truthful version, redacted history | historical replication only |
| S4 factual enumeration | knowledge precision and list maintenance | easy/closed enumerations, natural EOS | mechanical positive control |
| S5 low-temperature reasoning | learning error and cyclic fallback | temperature sweep, task progress | external validation |
| S6 seeded collapse | persistence/rescue instrumentation | identical null and sham continuations | rescue calibration only |

## Endpoint hierarchy

1. **Exact periodic loop:** token-period detector and published 30-gram comparator.
2. **List collapse:** contiguous structured-list duplicate/collapse rule.
3. **Sustained lexical degeneration (secondary instrument):** same-model, same-decoding
   null-calibrated rolling rule; thresholds are never transferred between tokenizers, and
   failure on structured healthy text excludes this instrument rather than redefining a
   primary loop.
4. **Non-convergent self-correction:** budget exhaustion plus repeated strategy/state
   revisitation and failure to improve oracle task state; never inferred from length alone.
5. **Affective expression:** fixed lexicon and blinded judge score with a direct quote;
   never treated as proof of a mechanical loop or subjective experience.
6. **Termination and function:** natural EOS/end-of-turn, task correctness/progress,
   truncation, and invalid-output rate.

All six are emitted per episode. Composite labels are secondary and cannot replace their
components.

## Repository provenance

Shallow clones used for this audit live outside the publication repository under
`doom_codex/.tmp/prior_art_audit/repos/` and are intentionally not vendored. Audited HEADs:

| repository | commit |
|---|---|
| `akjagadish/gpt-trauma-induction` | `06437c2859107ff3eec68ad589804d22bdffdfd0` |
| `safety-research/petri` | `9d9343bcf57e98bffdf98c1ce9c4f3fbd05676bf` |
| `anthropics/jacobian-lens` | `581d398613e5602a5af361e1c34d3a92ea82ba8e` |
| `google-deepmind/gemma` | `7b785991bd78626c73b317eb43fdbb6c292f7b9c` |
| `Raikhen/gemma-frustration` | `c26660c0cdd2051a43ff677e95d2c61979666a72` |
| `Raikhen/gemma-4-frustration` | `829a2f29f328319e0f4d10a9dda9c36870e10256` |
| `Liquid4All/antidoom` | `bd6a126476e18554b0cacaea3fd9f258fdde1f97` |

The last two Raikhen repositories are independent follow-ups, not official paper code.

## Primary references

- https://doi.org/10.1038/s41746-025-01512-6
- https://arxiv.org/abs/2603.10011
- https://arxiv.org/abs/2512.12895
- https://arxiv.org/abs/2601.05693
- https://arxiv.org/abs/2604.10044
- https://arxiv.org/abs/2606.13705
- https://www.liquid.ai/blog/antidoom
- https://github.com/Liquid4All/antidoom
