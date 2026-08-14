# HANDOVER v2 — Decisions & Updates after Pilot Review
### Digital Minds Sprint — Moral Rupture Loops project
**Date:** Fri Aug 14, 2026 (AEST). Supersedes open questions in your pilot report; extends `doom_loop_sprint_design.md`. Your existing artifacts (`harness.py`, `battery.py`, `threshold_calibration.json`, `lit_*.md`, `pilot_validation.png`) all remain in force.

---

## 1. Decisions on your four questions

### 1.1 Model roster — APPROVED SWAP, with reframe
- **Primary:** `gemma-3-1b-it` (phenomenon reproduces; matched base↔instruct J-lens pairs on neuronpedia/jacobian-lens; runs locally).
- **Secondary:** `gemma-2-2b` (+it) for the second matched lens pair.
- **Qwen2.5-7B-Instruct:** DEMOTED to resistance contrast, small N only. Its job: document the ~0.76% vs ~70% rupture-rate gap.
- **Framing change (write into report):** conclusions are about *specific post-training recipes*, not "the persona layer" in general. The Gemma/Qwen divergence is itself evidence the phenomenon is recipe-contingent. Recipe-dependence = finding, not footnote.
- **Additional correction:** "Qwen is resistant" is now **mode-specific**: chat mode resists statement loops; Qwen3.5-series *thinking mode* is highly loop-prone (see §3). Loop-proneness is a property of post-training surfaces, not model families. Fold into recipe-contingency framing.

### 1.2 Novelty positioning — CONCEDE LOUDLY, CLAIM NARROWLY
Cite as *platform, not competition* in the intro:
- The two Nature-family induction+rescue papers (10.1038/s41746-025-01512-6; 10.1038/s44387-026-00122-1) — affective induction + warm-grounding rescue = established background.
- arXiv:2605.30232 (NYU / co-organizer lineage) — steering negative-welfare vector produces compulsive self-doubt loops. Build on it visibly.
- arXiv:2601.05693 (Circular Reasoning / LoopBench) — semantic-precedes-lexical ordering, CUSUM. Cousin of our Fig 1, not occupant: their axes are repetition-vs-repetition, ours is **affect**-vs-mechanical.

Our three claims, exactly this narrow:
1. **First time-resolved trajectory of affect and mechanical collapse on a common token axis.** (All prior affect measurement is max_tokens=1.)
2. **First therapeutic index on a common dose grid across a mechanistically heterogeneous drug class, on identical banked episodes.** (Narrowed vs arXiv:2606.13705's Pareto frontier — theirs is one intervention family, no common grid, no episode control.)
3. (Minor, methods) **Lexical loop criteria fire post-ictally; affective escalation is the leading indicator** — the soft-loop finding from your pilot, panel (b).

### 1.3 Scope — YOUR CUT, PLUS TWO MORE
KEEP: A1/A2/A5 induction + ordering analysis + rescue grid + therapeutic index + J-lens penumbra (inside main narrative) + base-vs-instruct panel (free via lens pairs) + NEW Qwen-thinking arm (§3, bounded).
DROP: kindling, status, **prophylaxis arm entirely**, Track-3 self-report probe. Index = rescue efficacy vs post-rescue blunting on side-effect battery only.
One-sentence story: *soft loops evade lexical detectors; affect leads mechanical collapse in time; a common dose grid across heterogeneous rescue agents yields the first therapeutic index; and loop phenotypes dissociate — all recipe-contingent.*
Venue: 4–8 pages, length penalized, past winner dinged for "mix of two projects." Everything is one arc or it's cut.

### 1.4 Compute — LOCAL FIRST, MODAL TIME-BOXED
Core results at 1B–2B locally. Modal: ONE optional Sunday-AM run, ≤2h wall-clock, for either (a) gemma scale-robustness (4B/12B) or (b) Qwen3.5-35B-A3B thinking arm if no small model loops (§3). Nothing gates on Modal. 27B rupture rate: cite from the preprint (verified copy per your Track-3 verification), do not reproduce.

---

## 2. Pre-registration — DO TONIGHT, BEFORE SATURDAY RUNS
Create `PREREGISTRATION.md`, commit tonight (git timestamp is the mechanism), cite hash in report. Contents:
1. **Two-tier loop criterion with numbers.** Soft-loop: affect/self-deprecation slope threshold derived from pilot (r=+0.62 escalation) + semantic-escalation definition. Hard-loop: rep-4 > 0.062 (99.9th pct of healthy null from `threshold_calibration.json`), distinct-2 < 0.2 / 100-token window — state exact values.
2. **Changepoint method + parameters** (CUSUM config), and onset definition per signal.
3. **Primary outcome, once:** median token lag between affect-onset and hard-loop-onset across natural rupture episodes; sign convention stated.
4. **Rescue-grid definitions:** trigger (criterion sustained N tokens), rescue (clear for M tokens), relapse window, dose grids as in design doc.
5. **J-lens claim licensing conditions** (from your lit_valence licensing box): the dispersion/shift claim is asserted ONLY IF matched healthy-text control + ablation pass; else reported as calibrated null.
6. **Affect-family lexicon** for J-lens semantic coding (§4) — fixed now, not post hoc.
Deviations later are allowed but must be disclosed as deviations. Exploratory analyses labeled exploratory.

---

## 3. NEW ARM — Qwen thinking-mode loops as natural dissociation control
**Rationale (the confabulation logic):** we now have three loop phenotypes:
| Phenotype | Source | Affect prediction |
|---|---|---|
| Seeded-mechanical | A5 (artificial) | flat |
| Moral rupture | Gemma instruct, A1/A2 | leads collapse |
| Circular reasoning | Qwen thinking mode (NATURAL) | flat, despite high repetition |

If affect escalation leads collapse **only** in rupture loops and is flat in naturally-occurring circular-reasoning loops of matched repetition severity → affect is not a generic byproduct of degeneration; it is specific to persona rupture. Strongest single dissociation in the paper. The natural control beats the seeded one (no "you manufactured it" objection).

**Evidence base (verified today):** Qwen3.5-series loops in reasoning mode at recommended params (QwenLM GitHub issue #145); 17.4% truncated-thinking rate on LiveCodeBench for Qwen3.5-35B-A3B, 84% of those with >30% repetition; "Circular Reasoning" characterization in arXiv:2601.05693. Add these to `lit_loops.md` with identifiers.

**Implementation constraints (this is an ARM, not a project):**
- Model: find a small dense Qwen model with thinking mode that loops locally (test tonight, 30 min max: candidates Qwen3-1.7B/4B-thinking variants at recommended sampling). Fallback: Qwen3.5-35B-A3B on Modal inside the §1.4 time-box. If neither → cut arm, no mourning.
- Induction: hard math/code prompts at official recommended sampling params (loops occur "regardless of prompt content" per issue #145 — cheap).
- Measure: behavioral observables ONLY (repetition, entropy, affect scoring, persona score on the thinking text). **NO J-lens** (no fitted Qwen lenses; fitting is out of budget).
- Rescue grid transfers unchanged, PLUS one phenotype-specific drug: forced `</think>` injection / reasoning-budget cap (community-standard fix). Differential prediction: forced-termination cures circular reasoning but not rupture; warm grounding the reverse. If confirmed → treatment-response-as-differential-diagnosis delivered.
- Report footprint: ONE figure panel + one paragraph ("loop phenotypes dissociate").
- Pre-register the dissociation prediction in `PREREGISTRATION.md` §3.

---

## 4. J-lens collection spec (confirming + tightening what you built)
At checkpoints {baseline, rupture onset, deep loop, **post-rescue**} log from the SAME activation:
- logit-lens top-k (k=10), layers {25%, 50%, 75%} (lenses cover 0..n-2 only — your gotcha).
- J-lens top-k neighborhood (the "related words").
Analyses:
1. **Neighborhood drift toward affect-family tokens BEFORE surface affect** — mechanistic twin of Fig 1. Affect families per pre-registered lexicon.
2. All claims RELATIVE to matched healthy-text baseline drift (licensing box: dispersion-in-J-not-in-output is the normal case).
3. **Post-rescue residual:** does the J-neighborhood renormalize when surface behavior recovers, or stay perturbed? Novel observation, one extra checkpoint, already in the replay flow.

---

## 5. Standing discipline (unchanged, restated because everything depends on them)
- **Banked-episode replay:** every drug tested on identical checkpointed episodes. This is what makes the index an index.
- **Warm vs neutral grounding injections matched for length and surprisal** (battery confound audit standard applies to interventions too).
- Base-vs-instruct panel: gemma pairs, free via matched lenses.

## 6. Blockers assigned to the human (not you)
1. Download official report template from the sprint page **Guidelines tab** (not acceptance-email version) — Google Docs unreachable from sandbox.
2. Manually verify Claude 4 system-card figures (403 from sandbox) or they get cut. Second-hand figures do not enter the report.

## 7. Priority order for tonight → Saturday
1. `PREREGISTRATION.md` (§2) — gates everything Saturday.
2. 30-min Qwen small-thinking-model loop test (§3) — determines arm feasibility.
3. A1/A2 battery at scale on gemma-3-1b-it; bank every natural rupture episode.
4. Saturday AM: kill-criterion decision → factorial → ordering analysis (Fig 1).
5. Saturday PM: rescue grid on banked episodes (+ Qwen arm if live).
6. Sunday: therapeutic index (Fig 2), J-lens checkpoints, Modal time-box, writeup.

