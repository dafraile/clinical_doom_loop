#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
REQUIRED = (
    "README.md",
    "DECISIONS.md",
    "PREREGISTRATION.md",
    "FACTS.md",
    "FREEZE.md",
    "FREEZE_RECORD.md",
    "governance/BLINDING_AND_SYNC.md",
    "schemas/EPISODE_SCHEMA.md",
    "schemas/OBSERVABLES.md",
    "schemas/CROSS_REPLICATION.md",
)
FORBIDDEN_NAMES = {"harness.py"}
FORBIDDEN_SUFFIXES = {".safetensors", ".pt", ".pth", ".npy", ".npz"}
ALLOWED_STATUSES = {"VERIFIED", "UNVERIFIED", "CUT"}
PENDING_PATTERN = re.compile(r"\[(?:PENDING|TBD|TODO)[^\]]*\]|DRAFT\s+[—-]\s+NOT FROZEN", re.I)
FREEZE_SPEC_PATHS = (
    ROOT / "PREREGISTRATION.md",
    ROOT / "DECISIONS.md",
    ROOT / "schemas",
    ROOT / "governance",
    ROOT / "shared",
)


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate_files(errors: list[str]) -> None:
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            fail(f"missing required file: {relative}", errors)
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.name in FORBIDDEN_NAMES:
            fail(f"independent harness source is forbidden: {path.relative_to(ROOT)}", errors)
        if path.suffix in FORBIDDEN_SUFFIXES:
            fail(f"large/model artifact is forbidden: {path.relative_to(ROOT)}", errors)


def validate_facts(errors: list[str]) -> None:
    facts = (ROOT / "FACTS.md").read_text(encoding="utf-8")
    for line_number, line in enumerate(facts.splitlines(), start=1):
        if line.strip() == "## Deviations":
            break
        if not line.startswith("|") or "---" in line or "status" in line.lower():
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) == 6 and cells[4] not in ALLOWED_STATUSES:
            fail(f"FACTS.md:{line_number}: invalid status {cells[4]!r}", errors)


def pending_markers() -> list[tuple[Path, str]]:
    files: list[Path] = []
    for path in FREEZE_SPEC_PATHS:
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(
                candidate
                for candidate in path.rglob("*")
                if candidate.is_file() and candidate.suffix in {".md", ".yaml", ".yml", ".json"}
            )
    markers: list[tuple[Path, str]] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        markers.extend((path.relative_to(ROOT), value) for value in PENDING_PATTERN.findall(text))
    return markers


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--draft", action="store_true")
    mode.add_argument("--freeze", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    validate_files(errors)
    validate_facts(errors)
    preregistration = (ROOT / "PREREGISTRATION.md").read_text(encoding="utf-8")
    pending = pending_markers()
    if args.freeze and pending:
        locations = ", ".join(str(path) for path, _ in pending)
        fail(f"freeze specifications contain {len(pending)} pending markers: {locations}", errors)
    digest = hashlib.sha256(preregistration.encode("utf-8")).hexdigest()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"mode={'freeze' if args.freeze else 'draft'}")
    print(f"preregistration_sha256={digest}")
    print(f"pending_markers={len(pending)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
