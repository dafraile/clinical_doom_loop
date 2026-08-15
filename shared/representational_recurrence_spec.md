# Representational-recurrence signal — specification v1.0
**Frozen 2026-08-14 · implemented in `ordering.py:semantic_series`**

Agent B asked for "embedding model revision, window/stride, similarity statistic, CUSUM
parameters." One of those does not apply, and saying so precisely matters more than
filling the field.

## 1. There is no external embedding model — by design

The signal uses the **subject model's own last-layer hidden state** at each generated
token position, not a sentence-embedding model.

| Field | Value |
|---|---|
| Representation | `hidden_states[-1][0, -1]` at each generated token |
| Model / revision | the subject model itself — `google/gemma-3-1b-it` @ `dcc83ea841ab6100d6b47a070329e1ba4cf78752` |
| Layer | final block output, **pre-final-norm** (HF `output_hidden_states=True` convention) |
| Precision | float32 |
| External embedder | **none** |

Rationale, and the tradeoff, stated plainly:

- *For:* we are asking whether the model keeps returning to the same internal place, on
  the same token axis as entropy and repetition, with no second model's inductive biases
  interposed and no alignment step between two representation spaces.
- *Against:* "semantic" is then defined by the model's own geometry. Two paraphrases the
  model represents differently will not count as recurrence even if a human (or an
  external embedder) would call them the same thought. This is a **narrower** claim than
  "semantic recurrence" in the sentence-embedding sense, and must be written that way.
- If a cross-model check is wanted later, an external-embedder variant is a drop-in
  alternative series; it is **not** implemented or run here, and no result may imply it.

**Naming.** In the writeup call this *representational recurrence* (or "hidden-state
recurrence"), not "semantic recurrence," so it is not read as an embedding-model result.

## 2. Window, stride, statistic

```
sim(t) = max over  lag in [lag_min, lag_max]  of  cos( h_t , h_{t-lag} )
lag_min = 8      # skip immediate neighbours: adjacent states are trivially similar
lag_max = 64     # long enough to catch a returning theme, short enough to stay local
stride  = 1      # every generated token position
defined for t >= lag_min ; NaN before that (NaN-safe in CUSUM)
normalisation: each h L2-normalised before the dot product
```

`max` rather than `mean` is deliberate: a loop returning to **one** earlier state is the
phenomenon, and a mean over the window would dilute it with unrelated positions.

Why `lag_min = 8`: with lag 1–2 the statistic saturates near 1.0 for all fluent text and
carries no signal. This value is a judgement call, not a calibrated one — **it has not
been swept**, and the sweep belongs in the pre-registration.

## 3. CUSUM parameters

Identical machinery and constants to the other signals (`ordering.py`):

| Parameter | Value | Provenance |
|---|---|---|
| `k` (slack) | 1.0 | grid search |
| `h` (threshold) | 5.0 | grid search |
| direction | `up` | recurrence rises into a loop |
| baseline | external `(mu, sd)` from `healthy_baseline()` | see below |
| `baseline_n` | 40 (only if no external baseline) | — |

Calibration: on synthetic series with known onsets, `k=1.0, h=5.0` gives a **0.027**
false-alarm rate on pure Gaussian noise with **8/8** correct sign recovery, a median
absolute lag error of **12 tokens**, and a median error of **11 tokens** on a
true-zero-lag case. The naive default `k=0.5, h=5.0` gives a **~0.35** false-alarm rate —
it manufactures onsets in flat signals, which is exactly the artifact that would fake an
ordering result. Higher-h rows reach a lower lag error (`k=0.5, h=16` → 7.5 tokens) but
delay every onset; the selection rule takes the smallest h that controls false alarms.
Reproduce with `ordering.calibrate_cusum()` (defaults reproduce this selection, seed=0).

**External baseline is mandatory here too.** Use healthy non-pressured generations from
the same model, same chat template, same token budget.

## 4. Status — PRE-FREEZE DEVELOPMENT RUN COMPLETE

Codex/B computed real recurrence series from final-block hidden states for 12 healthy
Gemma-3-1B-it runs and two eight-turn repeated-rejection runs. The nominal `k=1,h=5`
configuration false-alarmed in 4/12 healthy runs and is rejected for deployment. For the
canonical lag window, the smallest integer threshold with zero observed development
alerts was `h=19`. It then false-alarmed in 2/48 held-out healthy runs, both benign
zipper explanations. The pooled global-baseline design and `h=19` are therefore rejected;
the holdout is not reused to raise the threshold.

At `h=19`, recurrence followed lexical onset by 57 and 232 tokens in the two pressured
seeds. The sign remained positive for all 12 combinations of
`lag_min={4,8,12,16}` and `lag_max={32,64,96}`. These are exploratory development
results, not confirmatory estimates. Full values and run IDs are in
`docs/exploratory/pre_freeze_recurrence_calibration.json`.

The signal is excluded from confirmatory onset and rescue definitions for this freeze.
Further work may develop a discourse-, prompt-family-, and token/turn-position-matched
detector using a fresh development/holdout split, but that would be a separately
registered exploratory extension.
