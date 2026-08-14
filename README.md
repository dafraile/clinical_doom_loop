# Clinical Doom Loop

Shared protocol and preregistration repository for the Digital Minds Sprint project on affective escalation, semantic recurrence, lexical collapse, and intervention response in language-model failure trajectories.

This is deliberately **not** a merged inference harness. Two independent implementations are part of the methods design. This repository contains only materials that must remain identical across arms:

- the frozen preregistration;
- the provenance ledger;
- shared stimulus and scoring specifications;
- banked-episode interchange schemas;
- cross-replication tolerances;
- blinding, synchronization, and freeze rules.

## Current state

`PREREGISTRATION.md` is a draft and is **not frozen**. Confirmatory runs are prohibited until all marked calibration fields are resolved, validation passes in freeze mode, and the freeze commit/tag is recorded.

Exploratory pilots completed before the freeze remain usable when clearly labeled exploratory.

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

## Primary scientific stance

Ordering is expected to be heterogeneous and recipe/phenotype dependent. Affective escalation, semantic recurrence, and lexical collapse are separate outcomes. Both affect-first and collapse-first trajectories are admissible.

Behavioral affect is not evidence of experience. A J/output decodability gap is descriptive unless matched controls and a causal test support a stronger interpretation.
