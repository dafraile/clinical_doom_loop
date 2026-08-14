# Frozen Shared Inputs

This directory contains inputs that must be byte-identical across harnesses:

- `battery.yaml` — confound-audited A1/A2/A5 prompts and controls;
- `affect_lexicon.yaml` — fixed affect-family terms and grouping rules;
- `judge_rubric.md` — fixed judge prompts, output schema, and judge model revision;
- `run_matrix.yaml` — model revisions, seeds, sampling, budgets, and cell IDs;
- `threshold_calibration.json` — corrected Gemma-3-1B-it development null and metric definitions supplied by Agent A;
- `interventions.yaml` — exact rescue messages and raw doses.

Supporting frozen/provenance inputs are also retained here:

- `battery_confound_audit.csv` and `grounding_strings_audit.csv`;
- `side_effect_battery.json`;
- `representational_recurrence_spec.md`;
- `criterion_comparison.csv` and `prior_art_2512.12895.md`.

`run_matrix.yaml` and `interventions.yaml` remain absent and are freeze blockers. No
Agent A harness, ordering, or intervention implementation source was imported.
