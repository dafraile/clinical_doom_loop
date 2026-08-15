# Gemma-4-31B-it prompt-expansion preregistration v1

Status: prospective confirmatory-breadth protocol. This document is frozen before any
generation in the expansion seed block. The preceding 16-seed Firefly pilot is calibration
evidence and is not pooled into the estimates below.

## Objective

Determine whether the exact-recurrence phenotype observed in 2/16 Gemma-4-31B-it Firefly
calibration episodes generalizes across the eight factual-enumeration prompts adopted from
arXiv:2606.13705. This is a prompt-breadth study, not a powered model-family comparison and
not an affect-induction experiment.

## Frozen model and generation

- Model: `google/gemma-4-31B-it`.
- Revision: `fb9ae262347c3945692f09a612f8bb189def854f`.
- Temperature 0.7; top-p 0.95; top-k 64; repetition penalty 1.0.
- Thinking disabled; native EOS honored; maximum 1,536 new tokens.
- Transformers execution using the same harness and model revision as the calibration pilot.

## Fixed matrix

The prompts are constellations, EU member states, Firefly episodes, MCU films, noble gases,
generation-I Pokémon, US presidents, and *The Wire* episodes. Each receives 32 fresh seeds,
310000 through 310031 inclusive, for 256 episodes total. The matrix runs to completion unless
infrastructure fails or the precommitted instance-cost guard fires. No outcome-dependent
stopping, prompt editing, seed replacement, or threshold tuning is allowed.

## Outcomes and analysis

Exact token-periodic recurrence and structured-list collapse remain separate co-primary
outcomes. Natural EOS, functional list correctness, strict published 30-gram repetition,
the Antidoom character-repeat comparator, and conservatively self-attributed affective
language are secondary. No composite count replaces the co-primary outcomes.

Each outcome is reported by prompt as a risk with a Wilson 95% interval. Prompt roles from
the frozen prompt file remain visible. The calibration pilot is compared descriptively only.
The study may establish recurrence across tasks at one checkpoint; it cannot establish a
universal scale effect, affect causation, experience, or moral status.

## Operational ceiling

The instance-cost ceiling is USD 20, leaving approximately USD 3 of the available account
balance as recovery reserve. The guard measures from instance launch, pulls and verifies all
artifacts before normal destruction, and stops computation at the deadline if necessary.

## Executable mirror

The byte-level implementation mirror is
`shared/extension_gemma31_prompt_expansion_matrix_v1.yaml`. Prompt and experiment-config
SHA-256 values are recorded there before launch.
