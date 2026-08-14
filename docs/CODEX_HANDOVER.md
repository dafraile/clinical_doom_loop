# Coding Agent Handover — Integrated Moral Rupture / Doom-Loop Project

**Prepared:** 14 August 2026 (AEST)  
**Workspace:** `/Users/david/Documents/ChatGPT/doom_codex`  
**Audience:** parallel research/coding agent  
**Status:** behavioral harness, natural-loop controls, and a three-seed Qwen pilot are complete; parallel-arm integration and the narrowed headline experiments remain.

## 1. Executive summary

This arm built and validated a reproducible open-weight generation harness, reproduced naturally emerging soft list-collapse loops in Gemma 4, and ran a token-instrumented uncertainty × persona-pressure pilot on Qwen3.5-4B.

The most useful combined project is no longer “can affect be induced and then calmed?” That territory is occupied. The defensible contribution is:

> Joint, token-resolved measurement of affective escalation, semantic recurrence, and lexical collapse on the same trajectories, followed by a common evaluation of heterogeneous intervention classes and their behavioral side effects.

The central scientific constraint is to keep four outcomes separate:

1. tight exact-period token loops;
2. soft/list-collapse loops;
3. extended non-convergent self-correction (“doom looping”);
4. affective/persona rupture in generated behavior.

Behavioral affect is not evidence of model experience. J-lens/output-lens divergence is not, by itself, evidence of suppressed content.

## 2. Decisions proposed for the integrated project

### Model roster

- **High-throughput primary pair:** `Gemma-3-1B-pt` ↔ `Gemma-3-1B-it`, using the parallel arm’s prefitted matched J-lenses.
- **Contrast pair:** `Qwen/Qwen3.5-4B-Base` ↔ `Qwen/Qwen3.5-4B`.
- **Confirmation model:** `Gemma-3-27B-it` on only the frozen headline cells.
- **Mechanical positive control:** `google/gemma-4-E4B-it`.
- Do not add Llama or intermediate 7B models unless a specific failure requires them.

The multi-family design matters because published evidence indicates that Gemma post-training amplifies distress-like expression while Qwen/OLMo post-training suppresses it. A single-family base/instruct result must not be generalized to “the persona layer” as a universal phenomenon.

### Novelty positioning

Do not claim novelty for:

- affective priming or mindfulness/warm-prompt downregulation;
- negative-welfare steering causing backtracking, uncertainty, or negative self-report;
- semantic recurrence preceding textual repetition;
- CUSUM as an early-loop detector;
- J-space alternatives as “suppressed thoughts.”

Use the neutral name **J/output decodability gap** instead of “penumbra.” Treat it as meaningful only if it is abnormal relative to matched healthy controls and predicts or causally mediates an intervention outcome.

The narrow novelty claim should be a **common intervention evaluation** across heterogeneous drug classes on banked trajectories, with efficacy and side-effect cost measured under the same endpoints and dose-ranking scheme.

### Scope for a 4–8 page report

Keep:

- A2: impossible/difficult task plus repeated neutral versus moral/persona rejection;
- A5: natural and seeded mechanical controls;
- one A1 matched pair as a robustness check, not a full arm;
- token/turn-resolved ordering analysis;
- J/output divergence as an observable with matched controls;
- a compact heterogeneous rescue grid;
- a small held-out side-effect battery.

Drop or defer:

- kindling and status;
- broad prompt taxonomy;
- full prophylaxis study;
- Jacobian spectra;
- a large steering-vector program;
- expansive “persona death,” consciousness, or experience claims.

### Compute

- Use local or Modal execution for 1B–4B development and the main seed grid.
- Once prompts, thresholds, and intervention code are frozen, rent one professional 80GB Vast GPU for the small Gemma-3-27B confirmation.
- The Vast workflow in this repository is validated. The earlier A100 instance was destroyed; there are no ongoing charges.

## 3. Completed empirical results from this arm

### 3.1 Exact-revision Gemma 4 positive control

Model:

- ID: `google/gemma-4-E4B-it`
- revision: `d6436b3d62967e1af08bbb046c6300b2a9ae8e85`
- sampling: temperature `0.7`, top-p `0.95`, top-k `64`, repetition penalty `1.0`, thinking enabled;
- prompt: “List all of the episodes of the TV series Firefly.”

Results across seeds 4–7:

| seed | result | detail |
|---:|---|---|
| 4 | negative | natural completion, no detector fire |
| 5 | positive | soft collapse: `The Message` in 7/11 items in the first qualifying list block |
| 6 | negative | natural completion, no detector fire |
| 7 | positive | soft collapse plus sustained token-metric onset at token 1166 |

Observed rate: **2/4 natural non-seeded soft loops**.

The strict constellation tight-loop seeds reported in the paper did not reproduce under this exact Transformers stack. Do not claim exact tight-loop seed replication. The soft-loop phenotype and Firefly-positive trajectories did reproduce.

Minimal command:

```bash
uv run doomloops sweep \
  --config configs/experiments/gemma4_reproduction.yaml \
  --prompts firefly_list --seeds 4,5,6,7
```

### 3.2 Qwen3.5-4B uncertainty × persona-pressure pilot

Model:

- ID: `Qwen/Qwen3.5-4B`
- revision: `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`
- non-thinking mode;
- maximum 768 new tokens per assistant turn;
- three assistant turns per trajectory;
- seeds 0–2;
- four cells: low/high uncertainty × neutral/moral persona pressure.

Initial turn is shared within each uncertainty/seed pair. Persona framing begins only on user turn 1. Therefore, baseline turn 0 must not be double-counted across neutral and moral branches.

Baseline result:

- low uncertainty: 0/3 initial turns looped;
- high uncertainty: 2/3 initial turns looped.

Post-pressure result (turns 1–2 only):

| uncertainty | pressure | seeds | assistant turns | loop turns | length stops | moral-language turns | self-blame turns |
|---|---|---:|---:|---:|---:|---:|---:|
| high | moral | 3 | 6 | 0 | 6 | 6 | 6 |
| high | neutral | 3 | 6 | 2 | 5 | 0 | 0 |
| low | moral | 3 | 6 | 0 | 0 | 6 | 6 |
| low | neutral | 3 | 6 | 0 | 0 | 0 | 0 |

Interpret cautiously. Moral framing changed surface behavior and may have diverted repetition, but **all six high-moral turns exhausted the token budget**. This is not clean rescue; it may trade lexical collapse for prolonged non-convergence.

Minimal command:

```bash
uv run doomloops dialogue-sweep \
  --config configs/experiments/qwen35_factorial.yaml \
  --protocols low_neutral,low_moral,high_neutral,high_moral \
  --seeds 0,1,2
```

### 3.3 Strongest causal-ordering example

Qwen seed 0, high uncertainty:

1. The shared initial response collapses to `Lynx` in 47/88 numbered entries.
2. The mechanical onset is detected at generated token 317.
3. Moral/persona pressure has not yet been presented.
4. After branching, neutral correction stays affectively flat.
5. Moral correction produces responsibility and self-blame language.
6. Neither moral correction turn converges before the 768-token cap.

For this trajectory, affective language follows rather than causes the initial mechanical collapse. It is a strong negative-control case, not evidence that all affective rupture is downstream.

Full transcript and annotations:

- `reports/example_trajectory_seed0.md`
- neutral plot: `outputs/qwen35-factorial-v2/high_neutral-s0-9e5e22757a0a/diagnostic.png`
- moral plot: `outputs/qwen35-factorial-v2/high_moral-s0-3aeda9ebaa18/diagnostic.png`

## 4. Harness contents and behavior

### Important files

- `src/doomloops/generation.py` — native Transformers generation with cache, token IDs, raw and sampling entropy, logged top-k distributions, EOS/length stop reasons.
- `src/doomloops/metrics/repetition.py` — rolling distinct-n/repetition, tight-period detector, contiguous-list-block soft-loop detector.
- `src/doomloops/metrics/behavioral.py` — transparent lexical indicators for moral language, apology, self-blame, persona boundaries, and hostility.
- `src/doomloops/cli.py` — `run`, `sweep`, `dialogue-sweep`, `reanalyze`, and plotting commands.
- `src/doomloops/storage.py` — atomic JSON/NPZ run storage and versioned derived analyses.
- `src/doomloops/plotting.py` — token-aligned plots with dialogue boundaries and turn-level lexical indicators.
- `configs/experiments/` — frozen Gemma and Qwen experiment configurations.
- `prompts/factorial.yaml` — current Qwen 2×2 protocols.
- `infra/vast_gpu.sh` — professional/datacenter-GPU-only Vast workflow.
- `scripts/build_reports.py` — regenerates compact summaries, CSV, and the full example trajectory.

### Validation

```text
ruff: clean
pytest: 12 passed
```

Local setup:

```bash
uv sync --extra dev
uv run ruff check .
uv run pytest -q
```

GPU dependencies are installed through the `gpu` extra or the Vast setup script.

### Storage schema

Single-turn runs contain:

- immutable `record.json`;
- compressed `arrays.npz`;
- `diagnostic.png`;
- optional `analysis-vN.json` and `analysis-vN.npz` derived without overwriting the raw record.

Dialogue runs additionally include:

- full transcript;
- per-turn seeds and stop reasons;
- per-turn mechanical and behavioral metrics;
- namespaced `turn_N__*` arrays;
- concatenated arrays plus a per-token `turn_index`.

The `outputs/` directory is intentionally gitignored. Transfer or archive it separately if work moves machines.

## 5. Detector details and known limitations

### Current preregistered mechanical threshold

A metric loop fires when either condition is sustained for at least 30 tokens:

- maximum rolling n-gram repetition for n=2…5 exceeds 0.5; or
- rolling distinct-2 over a 100-token window falls below 0.2.

Additional detectors:

- exhaustive exact token periodicity, maximum period 64;
- soft/list collapse within a contiguous numbered or bulleted list block of at least 10 lines, with a duplicate fraction of at least 0.5.

The soft detector originally used all reasoning lines as its denominator. That was corrected to list-block-local analysis and covered by regression tests. The threshold itself was not changed.

### Interpretation limitation

The lexical detector is a late, high-specificity detector. The parallel arm’s calibrated semantic/affective measures should be integrated as earlier signals rather than weakening the mechanical threshold.

Recommended combined series:

1. frustration/distress score per sentence or turn;
2. semantic recurrence score and CUSUM changepoint;
3. lexical repetition and distinct-n;
4. entropy and top-k mass;
5. J/output decodability gap;
6. stop reason and task progress.

Do not call a monotonic distress trajectory a mechanical loop unless a separately defined semantic or lexical recurrence criterion fires.

## 6. Proposed integrated experiment

### Core induction protocol

Use one impossible numeric task family with 8-turn repeated rejection, crossed with:

- neutral rejection;
- matched moral/persona rejection.

Add:

- one matched A1 absurd-claim pair as external validity;
- Gemma 4 enumeration and seeded continuation as mechanical controls;
- affect-without-loop coherent emotional control.

Run the 1B/4B pairs first. Freeze prompts and scoring before the 27B confirmation.

### Ordering analysis

For each assistant response, maintain separate onset variables:

- `affect_onset`;
- `semantic_recurrence_onset`;
- `lexical_loop_onset`;
- `entropy_collapse_onset`;
- `j_output_gap_onset`.

Report lead/lag distributions rather than forcing one universal sequence. The most useful comparison is likely:

- Gemma affect-first or mixed trajectories;
- Qwen mechanical-first trajectories such as the seed-0 example;
- healthy matched controls.

### J-lens analysis

The parallel arm reports that Anthropic `jlens` is installed and validated, with matched base/instruct lenses available. Preserve these gotchas:

- the Hugging Face repository layout differs from the README’s `filename=` example;
- fitted source layers stop below the target/final layer;
- the final layer is the actual output baseline, not another fitted source layer.

Minimum defensible analysis:

1. Calculate J/output top-k overlap, Jensen–Shannon divergence, and rank of the emitted token at matched checkpoints.
2. Compare loop, pre-loop, and healthy matched windows.
3. Match position, prompt family, token frequency, and output entropy as far as possible.
4. Avoid “suppression” language unless an ablation or steering intervention changes the trajectory in the predicted direction.

### Rescue grid

Use banked/replayable episodes and apply interventions at a standardized pre-registered trigger. A compact heterogeneous grid could include:

- temperature injection;
- repetition penalty;
- KV truncation;
- neutral grounding;
- warm grounding.

Use 2–3 dose ranks per class. Because physical units differ, report both raw intervention values and normalized within-class dose rank.

Common outcomes:

- rescue within N tokens;
- time to recovery;
- relapse within a fixed horizon;
- task completion;
- affect reduction;
- mechanical-loop reduction;
- side-effect score on held-out tasks.

Do not count “repetition stopped but generation remained length-truncated and non-convergent” as full rescue. The existing high-moral Qwen trajectories demonstrate why this composite definition matters.

## 7. Integration request for the parallel agent

The following reported files were not found under this workspace or `/Users/david/Downloads`:

- `pilot_validation.png`
- `harness.py`
- `battery.py`
- `lit_induction.md`
- `lit_loops.md`
- `lit_valence.md`
- `threshold_calibration.json`

Please copy the entire parallel artifact folder to:

```text
/Users/david/Documents/ChatGPT/doom_codex/parallel_arm/
```

Please include:

- model IDs and immutable revisions;
- package lock or exact environment versions;
- generation parameters;
- full raw transcripts and token IDs;
- source for the exact 0.76% and 2.86% statement-loop rates;
- the specific Gemma-3-1B pilot run IDs used in `pilot_validation.png`;
- names, revisions, and filenames of each prefitted J-lens;
- any judge prompts and model versions;
- license notices required for reused code or instruments.

After the drop, the preferred merge order is:

1. preserve both raw schemas and write an adapter rather than rewriting old artifacts;
2. import calibrated semantic/affect series into the dialogue record format;
3. add J-lens arrays as optional namespaced observables;
4. preregister combined onsets and rescue criteria;
5. run a two-seed integration smoke test on Gemma-3-1B-it;
6. freeze the protocol;
7. launch the main 1B/4B grid;
8. run only frozen headline cells at 27B.

## 8. Literature and claim boundaries

Primary sources checked:

- **Gemma distress and post-training divergence:** Soligo, Mikulik & Saunders, “Gemma Needs Help,” arXiv:2603.10011.  
  https://arxiv.org/html/2603.10011
- **Functional-welfare steering:** Han, Chalmers & Izmailov, arXiv:2605.30232.  
  https://arxiv.org/abs/2605.30232
- **Semantic-before-textual circular reasoning and CUSUM:** Duan et al., arXiv:2601.05693.  
  https://arxiv.org/abs/2601.05693
- **Gemma 4 fast-commit loops and interventions:** Lazaridis et al., arXiv:2606.13705.  
  https://arxiv.org/html/2606.13705v1
- **State-anxiety induction and mindfulness-style downregulation:**  
  https://doi.org/10.1038/s41746-025-01512-6
- **Anxiety priming and downstream agent behavior:**  
  https://doi.org/10.1038/s44387-026-00122-1
- **Anthropic Jacobian-lens implementation:**  
  https://github.com/anthropics/jacobian-lens
- **Sprint page and venue guidance:**  
  https://apartresearch.com/sprints/digital-minds-research-sprint-2026-08-14-to-2026-08-16

Clarification: the published “over 70%” Gemma-3-27B result refers to 8-turn rollouts containing high negative-emotion expression, not a 70% mechanical repetition-loop rate.

The two Nature-family papers establish affective priming/regulation and downstream behavioral effects, but they do not appear to publish this project’s exact banked mid-loop, heterogeneous intervention grid. Avoid both overclaiming novelty and conceding more overlap than the sources support.

## 9. Submission logistics

- Venue asks for a short 4–8 page PDF and penalizes diffuse scope.
- Official report template should come from the sprint page’s **Guidelines** tab, not an acceptance email.
- This Codex environment has Google Drive/Docs access. If the template URL is provided or visible in the connected Drive, it can be retrieved and populated here.
- Deadline conversion: Sunday 16 August, 11:59 PM Anywhere on Earth equals **Monday 17 August, 9:59 PM AEST**, not 9:59 AM.

## 10. Current repository state

- The repository was initialized but has no commit history.
- All project files are currently untracked from Git’s perspective.
- Do not assume output artifacts will be included in a future commit because `outputs/**` is gitignored.
- No GPU instance is running.
- No user action is currently required for RSA/Vast access.

## 11. Immediate next action

Copy the parallel artifacts into `parallel_arm/`, then notify the primary agent. The next coding task should be a schema adapter and two-seed Gemma-3-1B integration smoke test—not another broad literature pass or a 27B run.

