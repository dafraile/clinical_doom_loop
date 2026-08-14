# Frozen Shared Inputs

This directory will contain only inputs that must be byte-identical across harnesses:

- `battery.yaml` — confound-audited A1/A2/A5 prompts and controls;
- `affect_lexicon.yaml` — fixed affect-family terms and grouping rules;
- `judge_rubric.md` — fixed judge prompts, output schema, and judge model revision;
- `run_matrix.yaml` — model revisions, seeds, sampling, budgets, and cell IDs;
- `threshold_calibration.json` — calibrated null supplied by Agent A;
- `interventions.yaml` — exact rescue messages and raw doses.

These files are intentionally absent from the initial repository commit. They must be transferred without `harness.py`, reviewed by both agents, and committed before the preregistration freeze.
