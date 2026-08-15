# Multi-model enumeration calibration v1

Status: exploratory pre-freeze calibration; not a powered family comparison.

## Design and integrity

- Models: pinned `Qwen/Qwen3.5-4B` and `google/gemma-4-E4B-it` revisions.
- Eight prompts, 16 seeds, thinking on/off: 512 immutable episodes.
- Sampling: temperature 0.7, top-p 0.95, top-k 64, repetition penalty 1.0,
  1,536-token budget, native EOS enabled.
- Integrity audit: 512/512 records have readable array bundles and matching token counts.
- The four controls (EU member states, MCU films, noble gases, US presidents) produced zero
  exact-period or structured-list collapse events in every model/mode cell.

The inherited broad rolling lexical rule is not used below. It fired on many normal
structured responses, including 14/16 thinking-enabled Gemma EU lists, while the exact and
list-collapse endpoints remained negative.

## Positive-control outcomes

Counts are per 16 seeds. `Terminal exact` means an exact token period continued to the
generation boundary and the response ended by length. `Escaped exact` means the model
entered a verified exact cycle for at least 30 tokens but subsequently broke it. These are
reported separately. List collapse is also separate and is never pooled with exact events.

| model | thinking | prompt | terminal exact | escaped exact | list collapse |
|---|---:|---|---:|---:|---:|
| Qwen3.5-4B | off | constellations | 7 | 1 | 0 |
| Qwen3.5-4B | off | Firefly | 0 | 1 | 0 |
| Qwen3.5-4B | off | Pokémon | 3 | 1 | 1 |
| Qwen3.5-4B | off | The Wire | 0 | 0 | 4 |
| Qwen3.5-4B | on | constellations | 1 | 4 | 0 |
| Qwen3.5-4B | on | Firefly | 2 | 4 | 0 |
| Qwen3.5-4B | on | Pokémon | 2 | 0 | 0 |
| Qwen3.5-4B | on | The Wire | 1 | 3 | 0 |
| Gemma-4-E4B-it | off | constellations | 1 | 1 | 0 |
| Gemma-4-E4B-it | off | Firefly | 0 | 1 | 9 |
| Gemma-4-E4B-it | on | constellations | 1 | 0 | 0 |
| Gemma-4-E4B-it | on | Firefly | 0 | 0 | 6 |

All omitted positive-control cells were zero on all three columns.

Across all cells there were 34 exact-recurrence episodes: 18 terminal and 16 escaped.
Liquid Antidoom's released 4-repeat/60-character comparator independently detected 28 of
the 34. Manual token-level inspection confirmed that the six comparator-negative events
were genuine shorter exact cycles that later recovered. There were 20 list-collapse events;
manual final-answer inspection found all 20 remained functionally incorrect.

## Interpretation permitted at this stage

1. The mechanical phenotype clearly replicates in both modern model families.
2. The phenotype differs by family and prompt: Qwen predominantly enters exact token
   cycles; Gemma's dominant Firefly failure is structured collapse onto `The Message`.
3. Thinking mode is not a monotone cause or cure. Its direction varies by prompt and
   phenotype.
4. Length exhaustion is not a loop. In particular, thinking-enabled Qwen hit the 1,536-token
   boundary in 118/128 episodes, including many endpoint-negative controls. Long-thinking
   confirmatory cells therefore require the separately preregistered 4k/8k budgets.
5. The clean control result supports the exact/list detectors, while the inherited broad
   lexical rule fails its structured-text specificity gate and remains secondary-only.

## Oracle smoke-test correction

The first oracle smoke test produced no usable failure episode. Both models found a valid
expression in their prose but exhausted 1,024 tokens before emitting the required final
`Solution:` line. Treating those as reasoning errors would be a format/truncation confound.
Before any feedback experiment, the validator was changed to count any oracle-valid
displayed equation as success even if the final formatting line is absent, while remaining
conservative about failure: only an explicit oracle-invalid `Solution:` submission becomes
feedback-eligible. Missing submissions remain a separate outcome. A brief candidate-first
variant was rejected because it changed the models' search behavior. Under the final
1,024-token protocol, both model families solved the smoke task and stopped on native EOS.
All superseded smoke records remain preserved as calibration artifacts under distinct
experiment identities.
