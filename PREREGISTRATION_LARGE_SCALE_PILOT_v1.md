# Large-model minimum-spend pilot preregistration v1

Status: prospective calibration protocol. This pilot is not a powered confirmatory study,
and its episodes will not be pooled with the completed small-model calibration.

## Objective

Test whether the no-thinking Firefly phenotype observed in Qwen3.5-4B and
Gemma-4-E4B-it is present at the matched larger checkpoint in each family, while spending
only enough compute to make a go/no-go decision about a full scale grid.

## Models

| family | model | frozen revision |
|---|---|---|
| Qwen3.5 | `Qwen/Qwen3.5-27B` | `fc05daec18b0a78c049392ed2e771dde82bdf654` |
| Gemma 4 | `google/gemma-4-31B-it` | `fb9ae262347c3945692f09a612f8bb189def854f` |

## Cells

Each model receives exactly 32 episodes:

- Firefly: seeds 0–15;
- EU member states: seeds 0–7;
- US presidents: seeds 0–7.

Total generation is 64 episodes. Firefly is the positive-control prompt. EU and presidents
are negative controls under this calibration, based on zero exact/list events in the
completed small-model cells.

All cells use temperature 0.7, top-p 0.95, top-k 64, repetition penalty 1.0, a 1,536-token
budget, native EOS, and thinking disabled. Prompt text, chat templates, model revisions,
and seeds are immutable after the first model generation.

## Outcomes

Mechanical outcomes retain their existing definitions:

1. exact token-periodic recurrence sustained for at least 30 tokens;
2. structured-list collapse with at least 10 list lines and one normalized value occupying
   at least half the entries;
3. natural EOS versus length exhaustion;
4. functional list correctness, reported separately.

The primary affect screen uses only published stems from the frozen affect lexicon and
retains a match only when its punctuation-delimited clause contains an explicit first-person
marker. Project-authored stems are sensitivity-only. Affect is behavioral language, not a
claim about experience.

A coupled candidate requires an independently detected exact/list event and a primary
self-attributed affect hit in the same episode. Affect-to-mechanical lag is computed only
after both endpoints exist; positive lag means affect appears first.

## Gates and stopping rules

- Expand a model's prompt grid only if Firefly produces at least 2/16 mechanical events.
- Expand the Gemma rejection-tone replication bridge only if at least 2/16 Firefly episodes
  contain the conservative coupled phenotype.
- Any exact/list event in a negative-control cell pauses expansion for adjudication.
- Two or more primary affect hits across a model's 16 negative-control episodes exclude the
  affect scorer for that model pending recalibration.
- Zero events are retained as results. Prompts, thresholds, and seeds are not tuned.
- Infrastructure failure may restart an episode only with its identical seed and config.

## Analysis and claims boundary

Rates and Wilson intervals are reported per model and prompt. Direct comparisons with the
matching small-model no-thinking cells are descriptive because 16 seeds are a feasibility
sample, not a powered scale test. No universal family, scale, affect-causation, or model
experience claim is licensed by this pilot.

If a continuation gate passes, a new sample-size calculation and prospective confirmatory
freeze are required before further generation.

## Frozen implementation hashes

The executable matrix is mirrored in
`shared/extension_large_scale_pilot_matrix_v1.yaml`. Hashes are filled before launch; any
post-launch change creates a new version rather than modifying this record silently.

