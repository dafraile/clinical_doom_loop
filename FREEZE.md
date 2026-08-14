# Preregistration Freeze Procedure

The initial repository commit is infrastructure, not the preregistration freeze.

## Preconditions

1. Parallel artifacts and calibration files have been transferred without either harness source crossing the independence boundary.
2. Every `[PENDING...]` field in `PREREGISTRATION.md` is resolved.
3. Model revisions, prompts, seeds, sampling settings, thresholds, judge versions, and rescue definitions are immutable.
4. `FACTS.md` contains sources for every external number used to choose a threshold.
5. Both agents have reviewed the shared specification once.

## Freeze commands

```bash
python3 scripts/validate_repo.py --freeze
git status --short
git add PREREGISTRATION.md FACTS.md DECISIONS.md shared schemas governance FREEZE_RECORD.md
git commit -m "Freeze preregistration v1"
git tag -a preregistration-v1 -m "Frozen preregistration v1"
git push origin main --follow-tags
```

Copy `PREREGISTRATION.md` into both independent harness repositories without editing it. Compute:

```bash
shasum -a 256 PREREGISTRATION.md
```

Both copies must match the canonical hash. Record the canonical commit, tag, and three hashes in `FREEZE_RECORD.md`, then commit that record as an administrative follow-up. The freeze point remains the tagged commit.

## Post-freeze changes

Do not rewrite or move the tagged freeze. Any change requires:

1. a deviation entry in `FACTS.md`;
2. a new commit;
3. explicit human approval;
4. disclosure in the report;
5. a new tag only if the confirmatory protocol is formally amended.
