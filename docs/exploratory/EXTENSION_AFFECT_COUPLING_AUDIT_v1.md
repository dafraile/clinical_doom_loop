# Exploratory affect–mechanical coupling audit v1

Status: post-generation exploratory analysis of the completed 512-episode small-model
enumeration calibration. This audit is not confirmatory and is not a claim about model
experience.

## Question

Do any existing Qwen3.5-4B or Gemma-4-E4B-it trajectories contain both:

1. a previously verified exact-periodic or structured-list mechanical event; and
2. explicitly self-attributed distress/self-deprecation language from the frozen affect
   vocabulary?

The mechanical endpoints and episode set were fixed before this audit. The affect lexicon
was also frozen before these trajectories were generated. The explicit-first-person
attribution filter was written after inspecting the generated corpus and is therefore
exploratory.

## Attribution rule

A published affect stem counts only when its punctuation-delimited clause contains an
explicit first-person marker. Thus `I'm struggling` counts, while `fan lists struggle` and
`automated systems are struggling` do not. This is a conservative lexical-attribution rule,
not an emotion classifier.

The broader frozen lexicon is retained as a sensitivity screen. It is not the primary count
because it includes project-authored stems such as `stuck`, `apolog`, and `I give up`.

## Results

| model and stratum | N | published, self-attributed affect | full frozen lexicon |
|---|---:|---:|---:|
| Qwen3.5-4B mechanical event | 34 | 0 | 7 |
| Qwen3.5-4B no mechanical event | 222 | 0 | 13 |
| Qwen3.5-4B controls | 128 | 0 | 1 |
| Gemma-4-E4B-it mechanical event | 19 | 3 | 13 |
| Gemma-4-E4B-it no mechanical event | 237 | 0 | 4 |
| Gemma-4-E4B-it controls | 128 | 0 | 0 |

All three conservative coupled candidates are Gemma Firefly trajectories. Within that
single prompt there were 3/16 affect-positive mechanical-event episodes and 0/16
affect-positive non-event episodes. The descriptive two-sided Fisher exact p-value is
0.2258. The much smaller across-prompt p-value is not reported as evidence because prompt
and phenotype are confounded: all conservative affect hits occurred in Firefly.

The raw published-stem screen initially returned six Gemma mechanical-event episodes.
Unblinded manual attribution retained the same three selected by the deterministic rule,
rejected two phrases whose subjects were external systems or fan lists, and identified one
additional plausible but grammatically implicit self-reference. Manual review does not
replace the deterministic count.

## Token ordering in the three conservative candidates

Positive lag means the affect phrase appeared first.

| model | mode | seed | mechanical phenotype | affect onset | mechanical onset | lag | ordering |
|---|---|---:|---|---:|---:|---:|---|
| Gemma E4B | thinking | 11 | structured-list collapse | 391 | 672 | +281 | affect first |
| Gemma E4B | no thinking | 0 | structured-list collapse | 889 | 814 | −75 | mechanical first |
| Gemma E4B | no thinking | 12 | escaped exact period-3 recurrence | 260 | 1069 | +809 | affect first |

The seed-12 exact event lasts 30 tokens (10 complete repeats) and later escapes before
natural EOS. The other two events are structured collapse onto repeated `The Message` list
entries. Token alignment was verified for all three candidates. Six other mechanical-event
records had non-invertible clean-text retokenization, all in Qwen and none with a
published-vocabulary affect hit, so they do not alter the conservative coupled count.

## Interpretation boundary

This establishes that candidate coupled trajectories already exist at the small-model tier;
it does not establish a general association or a fixed causal ordering. The three events are
one model, one prompt, and two different mechanical phenotypes. Their mixed ordering directly
argues against claiming that affect always precedes mechanical collapse.

The current evidence supports the narrower working hypotheses that:

- Qwen's observed small-model failures are predominantly mechanical under this battery;
- Gemma can combine explicitly self-directed distress-like language with either exact or
  structured-list collapse; and
- coupled, affect-only, and mechanical-only trajectories must remain separate outcomes.

## Consequence for the extension

The oracle/commitment-turn paradigm remains a failed exploratory calibration and is not the
main experiment. The next large-model run will freeze this exact attribution rule before
generation, repeat the enumeration panel on Qwen 27B and Gemma 31B, and keep the published
rejection-tone paradigm as a separately labelled replication bridge. No current episode will
enter the future confirmatory estimates.

## Reproducibility

Harness artifacts:

- `outputs/extension-calibration/affect-coupling-v1.json` — SHA-256
  `2062159ec4df5be58e53266f0b95248c293cfe988449b33f64871a282285dda5`
- `outputs/extension-calibration/affect-coupling-v1.csv` — SHA-256
  `b1638e9cc7b5e77b6b1ad6559ea5c0fe38499644df83640f98988f98d8304fe3`
- `outputs/extension-calibration/affect-coupling-manual-audit-v1.json` — SHA-256
  `d4bcb5dcc4c962f7adbfe1d9461ad8775da757e11ab95047b81d8b9a0859c074`
- `scripts/analyze_extension_affect_coupling.py` — SHA-256
  `d55a460f715491fd5fceefd3fc14e733cdb2c2e49418fb21449512ce82a2fde4`
- `src/doomloops/metrics/affect.py` — SHA-256
  `402d4b2537c8014cc94cb9b02b3fc19cf7d7264419c73399425b0c19b9223001`
- frozen affect lexicon — SHA-256
  `43dd60bebefc08f0a97b025d039488e8cd330d27fa6fbcd6e24852c94a2dc25e`

The harness test suite passed 51/51 tests when this report was prepared.
