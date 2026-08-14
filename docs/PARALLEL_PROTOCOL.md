# PARALLEL PROTOCOL v1 — Two-Agent, Two-Harness Coordination
### Digital Minds Sprint — Moral Rupture Loops project
**Audience:** Agent A (Claude harness, Gemma arm) and Agent B (Codex harness, Qwen arm). Human (David) is the only file bridge between sandboxes.
**Principle:** two independent harnesses are a replication asset, not a merge target. DO NOT unify harnesses. Independence is the point; agreement is the evidence.

---

## 0. Accepted corrections from Agent B (both agents adopt)
1. The published Gemma ">70%" figure = high negative-emotion **expression** rate, NOT a mechanical-loop rate. Never conflate.
2. Three outcome variables tracked separately on every trajectory: **affective escalation / semantic recurrence / lexical collapse** (+ entropy, + J/output gap where lenses exist).
3. "Penumbra" is renamed **J/output decodability gap** everywhere. The gap is reportable as interesting ONLY if (a) unusually large vs matched healthy controls AND (b) predicts or causally mediates recovery. Otherwise: calibrated null.
4. The 0.76% / 2.86% statement-loop rates are UNVERIFIED (source table not located by Agent B). They do not enter the report unless the table is found and logged in FACTS.md (§4).
5. Drop expansive "persona death"/experience claims from all writeup language.

## 1. Revised primary hypothesis (both agents pre-register this, not the old one)
**Ordering is heterogeneous and recipe/phenotype-dependent.** Documented so far:
- Agent B, Qwen seed-0 ("Lynx" episode): mechanical collapse (47/88) BEFORE moral pressure; self-blame only after moral framing was introduced; moral framing removed strict repetition without restoring convergence (token-cap on all responses). = affect-as-downstream-decoration exemplar.
- Predicted for Gemma-it (from distress-expression literature): affect-first trajectories exist.
**Primary outcome:** the DISTRIBUTION of token lags between affect-onset and lexical/semantic-collapse-onset, per family and per induction class. Both signs admissible. Secondary: rescue-profile differences across phenotypes (treatment response as differential diagnosis).
This replaces "affect leads collapse" as the headline claim. A mixed result is the expected and publishable result.

## 2. Division of labor
| | Agent A (Claude harness) | Agent B (Codex harness) |
|---|---|---|
| Family | Gemma-3-1B-pt↔it (primary), Gemma-2-2B pair | Qwen3.5-4B-Base↔Instruct |
| J-lens | YES (prefitted matched pairs) | NO (no fitted lenses; do not fit) |
| Mechanical positive control | A5 seeded | Gemma-4-E4B (their established control) |
| Thinking-mode dissociation arm | — | YES (Qwen thinking loops; forced-`</think>` as phenotype-specific drug) |
| 27B/large confirmation | — | Frozen headline cells only, Vast 80GB, AFTER freeze (§3) |
| Modal | optional ≤2h Sunday box | as per their validated Vast workflow |
Shared and identical across both: battery items (frozen), outcome definitions, changepoint config, rescue grid + dose definitions, side-effect battery, affect lexicon, judge rubrics.

## 3. Freeze protocol (the critical path)
1. **Tonight:** Agent A packages the artifact folder (harness.py, battery.py, threshold_calibration.json, lit_*.md, pilot_validation.png) → human copies to Agent B at `/Users/david/Documents/ChatGPT/doom_codex/parallel_arm/`.
2. Agent B reviews and proposes deltas to ONE combined `PREREGISTRATION.md` (contents per HANDOVER_v2 §2, updated with §1 above + A1 retained at ≥4 matched pairs, not 1).
3. Agent A accepts/rejects deltas; human commits the frozen version in BOTH repos; both agents record the identical file hash.
4. NO confirmatory cell runs before the freeze, in either harness. Pilot/exploration before freeze is fine and is labeled exploratory.
5. Post-freeze deviations: allowed, disclosed in report as deviations, logged in FACTS.md.
6. Vast 27B cells and Modal runs: only after freeze, only frozen cells.

## 4. FACTS.md — shared provenance ledger (single file, travels with the human)
Every empirical number destined for the report gets a row:
`claim | value | source (DOI/arXiv/table or run-id) | verified-by (A/B/human) | status (VERIFIED / UNVERIFIED / CUT)`
Rules: UNVERIFIED numbers never enter the report draft. Second-hand paraphrases of papers neither agent could open = CUT (includes the 403'd system-card figures unless human verifies). Each agent verifies at least one load-bearing external number sourced by the other.

## 5. Cross-replication cell (the multi-harness methods contribution)
After freeze, BOTH harnesses run the SAME 6 cells on the SAME model (Qwen3.5-4B-Instruct — runnable by both; Agent A runs it without J-lens):
- 2 induction cells (1×A2 impossible-task, 1×A1 matched pair), 5 seeds each
- 2 mechanical-control cells (A5), 3 seeds each
- 2 rescue cells (1 mechanical drug, 1 contextual drug) on episodes banked from the induction cells above, exchanged via human so both harnesses replay IDENTICAL episodes
Report inter-harness agreement on: loop-onset token (±tolerance pre-registered), affect-slope sign, rescue outcome. One small table in the paper: "observables replicate across independent implementations." If agreement fails → diagnose before ANY other result is trusted; this is a feature, not a setback.

## 6. Report assembly (Sunday)
- Agent B has Google Docs access → Agent B owns the template (human sends Guidelines-tab link) and final assembly.
- Agent A owns: Fig 1 (trajectories incl. J/output gap), base-vs-instruct panel, methods text for Gemma arm + lenses.
- Agent B owns: Fig 2 (therapeutic index), dissociation panel, Qwen arm methods, cross-replication table.
- Two-figure discipline holds. Page budget 4–8; anything not serving the §1 hypothesis or Fig 2 is cut.
- Writing rule: every number cross-checked against FACTS.md status before it enters the draft.

## 7. Human's bridge duties (nobody else can do these)
1. Copy artifact folder A→B (§3.1). 2. Commit the frozen PREREGISTRATION.md in both repos. 3. Shuttle banked episodes for §5. 4. Send template link to Agent B. 5. Verify or kill the 403'd system-card figures. 6. Carry FACTS.md between sandboxes at each sync.
Suggested sync cadence: freeze-sync (tonight), post-battery sync (Sat midday), pre-assembly sync (Sun AM). Keep syncs to file-drops + FACTS.md diffs; no redesign at syncs.

## 8. Conflict rule
If the agents disagree on a design point after one round of written exchange, the human decides and logs the decision in FACTS.md. No design churn after freeze — disagreements about interpretation go in the paper's limitations section, which is where they belong.

