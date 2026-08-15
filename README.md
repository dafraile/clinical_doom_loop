# Clinical Doom Loop

> The completed Gemma-3-1B result is a pilot. A cross-family, cross-scale extension is
> being prepared on `codex/multimodel-extension`; confirmatory execution remains blocked
> until the new calibration gates and freeze requirements pass. See
> `docs/PRIOR_ART_INDUCTION_AUDIT.md` and `PREREGISTRATION_EXTENSION_v1.md`.

Protocol, evidence packet, and final report for the Digital Minds Research Sprint project on affective expression, lexical collapse, and intervention response in language-model failure trajectories.

This is deliberately **not** a merged inference harness. Two independent implementations are part of the methods design. This repository contains only materials that must remain identical across arms:

- the frozen preregistration;
- the provenance ledger;
- shared stimulus and scoring specifications;
- banked-episode interchange schemas;
- cross-replication tolerances;
- blinding, synchronization, and freeze rules.

## Current state

Analysis is complete. The reportable results are locked in [`artifacts/freeze_packet_v2.tar.gz`](artifacts/freeze_packet_v2.tar.gz), whose SHA-256 is `a009d5678d46927b63d6cda9207a73af8a6b886485df9e747ac986cedf7307ab`. Its 35 manifest-tracked payload files verify without mismatch, and all 21 generated claims resolve to source keys.

The protocol was version-controlled before powered runs at commit `ac92bd2`, but the planned cross-repository annotated freeze tag was not completed. This procedural deviation is disclosed in [`FREEZE_RECORD.md`](FREEZE_RECORD.md), [`DEVIATIONS.md`](DEVIATIONS.md), and the report appendix; it was not repaired retrospectively.

Final submission artifacts:

- [`reports/final_submission/Distress_Expression_Is_Not_Distress_Dynamics.pdf`](reports/final_submission/Distress_Expression_Is_Not_Distress_Dynamics.pdf)
- [`reports/final_submission/Distress_Expression_Is_Not_Distress_Dynamics.docx`](reports/final_submission/Distress_Expression_Is_Not_Distress_Dynamics.docx)
- [`reports/final_submission/report_source.md`](reports/final_submission/report_source.md)

## Repository boundary

Allowed here:

- Markdown protocols and source reviews;
- shared batteries and small configuration files;
- judge rubrics and fixed lexicons;
- compact cross-replication episode JSON after the freeze;
- validation scripts.

Not allowed here:

- either agent's harness implementation;
- private confirmatory outputs before the scheduled unblinding;
- model weights or J-lens tensors;
- credentials;
- large raw arrays.

Exception: the post-unblinding immutable result archive may contain the exact generating implementation and compressed source evidence for reproducibility. Harness code is not extracted into the shared working tree or treated as a merged implementation.

## Validate

Draft validation:

```bash
python3 scripts/validate_repo.py --draft
```

Freeze validation, after every pending field is resolved:

```bash
python3 scripts/validate_repo.py --freeze
```

The freeze validator prints the SHA-256 of `PREREGISTRATION.md`. Record that value and the Git commit in `FREEZE_RECORD.md`, copy the exact preregistration into both harness repositories, and verify matching hashes.

## Governance

- `DECISIONS.md` — accepted scientific and scope decisions.
- `docs/PARALLEL_PROTOCOL.md` — two-agent coordination protocol supplied by the human supervisor.
- `docs/HANDOVER_v2.md` — supervising-agent handover and pivot.
- `docs/CODEX_HANDOVER.md` — results and engineering context from the Codex/Qwen arm.
- `governance/BLINDING_AND_SYNC.md` — information-flow and unblinding rules.
- `FACTS.md` — only numerical claims eligible for the report.
- `FREEZE.md` — exact freeze procedure.
- `DEVIATIONS.md` — deviations and exclusions applied during interpretation.
- `artifacts/freeze_packet_v2/ENDPOINTS.md` — canonical endpoint hierarchy and reporting language.

## Primary scientific stance

Distress-like expression and persistent distress-like dynamics are separate outcomes. In the EOS-clean chat sample, conversational pressure rarely produced sustained lexical collapse; deliberately seeded collapse was common, persisted under comparators, and was difficult to reverse at the tested sample size.

Behavioral affect is not evidence of experience. A J/output decodability gap is descriptive unless matched controls and a causal test support a stronger interpretation.
