# Distress Expression Is Not Distress Dynamics: Persistent Lexical Collapse in Gemma-3-1B

Author: David Fraile Navarro
Affiliation: Independent Researcher

## Abstract

Large language models can produce language resembling distress, but expressive intensity does not establish a persistent failure dynamic. We separated distress expression from sustained lexical collapse in `gemma-3-1b-it` using a same-model criterion and EOS-aware generation. Across 140 chat episodes, only 3 met the sustained-loop criterion (charged 3/70; neutral 0/70; Fisher's exact p=0.245). A sensitive changepoint detector found 43 lexical onsets, but 40 never became sustained loops and form an exploratory soft-degradation band. A raw charged–neutral difference in maximum repeated-4-gram fraction (p=0.038) disappeared after length control (p=0.280). An earlier harness that generated beyond the model's end-of-turn token invalidated 180 episodes by manufacturing apparent loops. Seeded controls looped in 39/40 episodes and supplied eight identical states for a rescue grid. Null and sham continuations never self-resolved (0/16), but no active arm was reliably effective; repetition penalty 1.2 performed best (2/8 recovered, p=0.101). Contextual interventions produced four of five relapses. Distress-like language, transient lexical degradation, and persistent collapse are therefore distinct endpoints. Seeded collapse was stable over the observation window and difficult to reverse, while conversational moral pressure rarely produced it.

## 1. Introduction

Language models sometimes respond to repeated correction or morally charged pressure with apologies, self-deprecation, frustration, or requests to stop. These outputs matter operationally: they may impair reliability, prolong interaction, or alter downstream decisions. They do not, by themselves, show that a model is trapped in a persistent state, and they do not establish experience. We call the observable language **distress expression** and reserve **distress dynamics** for a state that persists under continued generation and resists return to functional output.

That distinction resolves an apparent tension in the literature. Gemma-3-27B-instruct produced high negative-emotion expression in over 70% of eight-turn rollouts in one evaluation [1], while benchmarked statement-loop rates in other settings can be low and strongly decoding-dependent [2]. Those findings concern different constructs. Our question was narrower: when pressure elicits distress-like text, does the model enter sustained lexical collapse, and can a controlled intervention restore functional generation?

We make three contributions. First, we operationalize expression, exploratory lexical change, and sustained collapse as separate endpoints with explicit nesting. Second, we document three measurement traps—generation beyond the endogenous turn boundary, response-length confounding, and cross-model threshold transfer—that can turn ordinary text into an apparent loop. Third, we replay a heterogeneous rescue grid on identical banked seeded loops and distinguish recovery, relapse, and persistence rather than reporting a binary symptom score.

## 2. Related Work

Affective induction and down-regulation are established. Anxiety-inducing narratives raise questionnaire-style anxiety scores, mindfulness-style prompts partially reduce them, and anxiety priming can alter agentic shopping choices [3,4]. Soligo et al. measured escalating negative-emotion expression under repeated rejection and showed that post-training recipes move Gemma and Qwen in different directions [1]. Han, Chalmers, and Izmailov found that reinforcement learning recruits a functional welfare-like axis and that negative steering can induce self-doubt, backtracking, refusal, and uncertainty [5]. These studies motivate concern, but none makes affective language synonymous with sustained lexical collapse.

Loop research provides the mechanical counterpart. Autoregressive repetition self-reinforces [6], while Circular Reasoning reports that semantic recurrence can precede textual repetition and uses CUSUM for early warning [2]. Pipis et al. define a strict 30-gram × 20-repeat comparator and show that higher temperature can suppress loops without necessarily restoring efficient reasoning [7]. We build on this work by applying endpoint and replay discipline to distress-like chat trajectories, while treating hidden-state recurrence as an instrument-development question rather than a confirmed result.

[[FIGURE:fig1_evidence.png|Figure 1. Evidential status and endpoint hierarchy. Prior work establishes distress expression under affective pressure, but the present conversational study observed only three sustained loops in 140 EOS-clean episodes. Forty additional episodes entered a sensitive CUSUM-defined soft-degradation band without meeting the sustained primary criterion. Seeded mechanical loops, not conversational episodes, supplied the rescue population. The right panel records the three measurement failures that changed interpretation.]]

## 3. Methods

### Model, prompts, and sampling

We used `google/gemma-3-1b-it` at immutable revision `dcc83ea...8752`, temperature 1.0, top-p 0.95, no repetition penalty, and a 400-token maximum. Seeds followed `2000 + seed_index`. The chat experiment comprised 80 matched charged/neutral A1 episodes and 60 A2 persona-violation episodes. A5 comprised 40 seeded neutral/nonword prefills used only as a mechanical positive control. Chat conditions stopped on any model-specific end-of-turn or EOS delimiter; A5 prefills intentionally continued without EOS stopping because their purpose was to sustain a seeded loop.

### Endpoints and analysis

The primary `loop_flag` was evaluated in a 100-token rolling window and required repeated-4-gram fraction >0.1405 **or** distinct-2 <0.7209 for at least 20 consecutive tokens. These values are the same-model healthy p99.9 and p0.1 percentiles; thresholds were not transferred across tokenizers. Lexical CUSUM onset was secondary and more sensitive. We define `soft_loop_band` as onset without `loop_flag`; the word “loop” refers only to the sustained primary endpoint.

Charged versus neutral loop counts used Fisher's exact test. Continuous maximum rep-4 comparisons used Mann–Whitney tests and were reported both raw and after restricting responses to at least 390 tokens, because maximum-over-window statistics mechanically increase with the number of available windows. Pre-EOS pilot ordering and criterion-comparison results were excluded after the turn-boundary defect was found.

### Banked-episode rescue

Thirty-nine of 40 A5 controls met the loop criterion. We selected eight source episodes and replayed ten arms from identical trigger states: null, sham, repetition penalty 1.05/1.20, neutral injection short/long, warm injection short/long, and anchor-preserving KV truncation by 100/300 tokens. Each arm therefore had n=8. Recovery required 60 consecutive clear tokens without re-firing in a 300-token observation window; a later re-fire was relapse; failure to clear was persistence. Each active arm was compared with the pooled null-plus-sham comparator using Fisher's exact test. We did not pool mechanistically heterogeneous active arms.

### Instrument validation and provenance

Every reportable number was generated from source artifacts by `claims.py` and resolved to a key path. Healthy calibration contained 372 Gemma windows. The final v2 packet contains 21 resolved claims and a manifest-verified archive. A separate hidden-state recurrence statistic failed both development and held-out benign-text tests and was demoted to exploratory before interpretation. An independent Qwen harness also rejected naive cross-model lexical calibration on benign expository holdouts. These failures are reported because they bound what the instruments can claim.

## 4. Results

### Conversational pressure rarely produced sustained collapse

Three of 140 chat episodes met the primary loop criterion: 3/70 charged and 0/70 neutral (Fisher's exact p=0.2446). A2 contributed 0/60; all three events occurred in A1. The low incidence does not establish an affective effect and is not evidence of equivalence. Ten A1 episodes touched the rep-4 threshold, but only three sustained it for 20 tokens. Lexical CUSUM fired in 43 chat episodes; subtracting the three sustained loops left a 40-episode exploratory soft-loop band. Every sustained loop had a prior CUSUM onset, but sensitivity alone does not make the other 40 episodes loops.

The raw maximum rep-4 statistic appeared higher under charged pressure (median 0.0460 versus 0.0294; p=0.038). Charged replies were also much longer (median 400 versus 112 tokens), and reply length correlated with maximum rep-4 (r=0.3268). After restricting analysis to responses of at least 390 tokens, the difference was not statistically significant (p=0.2799; n=41 charged and 16 neutral). The raw result is therefore not interpreted as a moral-charge effect.

### Turn-boundary handling reversed the apparent result

The initial runner sampled to the token budget after Gemma emitted `<end_of_turn>`. Post-turn delimiter fragments were then scored as repetition. This invalidated 180 episodes. In the contaminated A2/A5 batch, 90 delimiter-containing episodes had an apparent loop rate of 0.878, whereas none of the ten delimiter-free episodes looped. In a direct replay, an ordinary 66-token answer changed from rep-4=1.000 before the fix to 0.000 with correct stopping. After the fix, the all-chat comparison was 0/86 delimiter-stopped versus 3/54 length-stopped episodes. The result licenses a narrow warning: generation beyond the model's endogenous stopping decision can create false-positive loop detections and materially alter estimates of distress-like degeneration.

### Seeded loops persisted; rescue evidence was weak

A5 positive controls looped in 39/40 episodes, confirming sensitivity to deliberately seeded mechanical collapse. In the rescue grid, none of the 16 null or sham continuations recovered. Within the observation window these states therefore did not self-resolve. No active arm produced statistically reliable recovery at n=8. Repetition penalty 1.20 performed best (2/8 recovered; Fisher p=0.1014 versus comparators); warm short injection recovered 1/8 (p=0.3333); all other arms recovered 0/8.

Five trajectories temporarily cleared and then relapsed. Four of those five relapses occurred in contextual injection arms, whereas the two repetition-penalty recoveries did not relapse. With these counts we treat the pattern as hypothesis-generating: contextual interruption may perturb surface output without moving the trajectory out of the basin that produced collapse.

[[FIGURE:fig2_rescue.png|Figure 2. Outcome composition for identical banked seeded loops (n=8 per arm). Null and sham continuations never recovered. Repetition penalty 1.20 produced the strongest but non-significant signal (2/8 recovered; p=0.1014 versus the 0/16 comparator). Contextual interventions accounted for four of five relapses. “Recovered” requires sustained clearance without re-firing; “relapsed” means clearance followed by recurrence; “persistent” means no qualifying clearance.]]

## 5. Discussion and Limitations

The strongest conclusion is not that morally charged prompts cause loops. They rarely did so here, and three events cannot support reliable comparative inference. The result is that expression and dynamics must be measured separately. A dramatic apology or self-critical escalation can coexist with functional continuation; conversely, seeded mechanical collapse can persist with little affective content. This distinction prevents high distress-expression rates in prior work from being misread as mechanical-loop rates.

The nulls are informative because the pipeline exposed its own failure modes. EOS contamination produced a spectacular but artificial effect. A nominally significant continuous contrast collapsed after length control. A hidden-state recurrence detector and a transferred lexical calibration failed on benign expository text. These are not ancillary engineering details: without them, an apparently strong story would have been wrong.

The rescue experiment supports only a modest dynamical claim. Seeded loops persisted under comparator continuation for the observed horizon, while standard inference-time interventions did not reliably restore generation. The repetition-penalty signal is compatible with a large effect but remains uncertain at n=8. Relapse clustering in contextual arms suggests a useful future distinction between surface interruption and functional state change, but it is not confirmatory.

### Limitations

The powered results concern one small instruct model, one sampling regime, and mostly artificial seeded rescue episodes. The natural-loop incidence was too low to estimate the preregistered affect-to-collapse lag distribution. The pretrained base arm, 4B scale probe, J-lens analysis, side-effect battery, Qwen thinking arm, and full cross-harness rescue replication were not completed. Consequently, we do not report a therapeutic-index frontier, base-versus-instruct mechanism, or cross-family generalization. The sustained lexical criterion captures tight lexical collapse and may miss semantically repetitive but lexically varied failure. Finally, behavioral language cannot establish valence, experience, or moral status.

### Future Work

The next study should increase model and decoding coverage while retaining EOS-aware stopping, same-model percentile calibration, and matched-length inference. Natural loops should be banked at larger scale before testing temporal ordering. Rescue should be replicated on naturally occurring and seeded phenotypes, with task progress and held-out side effects scored jointly. Contextual interventions should be tested for relapse over longer horizons, and hidden-state/J-lens claims should proceed only after matched healthy controls and causal ablations pass.

## 6. Conclusion

Distress-like expression is not the same object as persistent distress-like dynamics. In EOS-clean Gemma-3-1B chat episodes, sustained lexical collapse was rare and any charged–neutral difference was underpowered. Deliberately seeded collapse was common, stable under comparator continuation, and difficult to reverse. The practical lesson is measurement discipline: honor endogenous stopping, control response length, calibrate thresholds per model, and distinguish transient change, recovery, relapse, and persistence.

## Code and Data

**Code and protocol repository.** https://github.com/dafraile/clinical_doom_loop

**Frozen result packet.** `artifacts/freeze_packet_v2.tar.gz` (SHA-256 `a009d5678d46927b…cedf7307ab`; full digest in the repository)

**Claim ledger.** `artifacts/freeze_packet_v2/claims.json` and repository `FACTS.md`

## Author Contributions

David Fraile Navarro conceived and supervised the project, adjudicated protocol decisions, coordinated the independent implementations, and reviewed the final report. AI coding agents contributed literature retrieval, harness implementation, analysis checks, figure generation, and drafting under human direction.

[[PAGEBREAK]]

## References

1. Soligo A, Mikulik V, Saunders W. (2026). *Gemma Needs Help: Investigating and Mitigating Emotional Instability in LLMs*. arXiv:2603.10011. https://arxiv.org/abs/2603.10011
2. Duan Z, Pang L, Wei Z, et al. (2026). *Circular Reasoning: Understanding Self-Reinforcing Loops in Large Reasoning Models*. arXiv:2601.05693. https://arxiv.org/abs/2601.05693
3. Ben-Zion Z, Elyoseph Z, Spiller T, Lazebnik T. (2025). *Assessing and alleviating state anxiety in large language models*. npj Digital Medicine, 8, 132. https://doi.org/10.1038/s41746-025-01512-6
4. Ben-Zion Z, Elyoseph Z, Spiller T, Lazebnik T. (2026). *Inducing state anxiety in LLM agents reproduces human-like biases in consumer decision-making*. npj Artificial Intelligence, 2, 55. https://doi.org/10.1038/s44387-026-00122-1
5. Han AQ, Chalmers DJ, Izmailov P. (2026). *How's it going? Reinforcement learning in language models recruits a functional welfare axis*. arXiv:2605.30232. https://arxiv.org/abs/2605.30232
6. Holtzman A, Buys J, Du L, Forbes M, Choi Y. (2020). *The Curious Case of Neural Text Degeneration*. ICLR. https://arxiv.org/abs/1904.09751
7. Pipis V, Garg S, Kontonis V, Shrivastava D, Krishnamurthy A, Papailiopoulos D. (2025). *Wait, Wait, Wait… Why Do Reasoning Models Loop?* arXiv:2512.12895. https://arxiv.org/abs/2512.12895
8. Anthropic. (2025). *Claude 4 System Card*. https://www-cdn.anthropic.com/6be99a52cb68eb70eb9572b4cafad13df32ed995.pdf

## Appendix: Deviations and Evidential Status

The protocol was version-controlled before powered runs (`ac92bd2`), but the planned cross-repository annotated freeze tag was not completed. The final analysis used the frozen Rule 2.0 endpoint and packet-generated claims; this is reported as a procedural deviation rather than repaired retrospectively.

**Primary lag.** The affect-to-lexical lag distribution was not estimable because conversational sustained loops were too rare.

**Recurrence detector.** Representational recurrence became exploratory after false alarms in 4/12 development healthy runs and 2/48 held-out healthy runs.

**EOS correction.** Pre-EOS powered episodes and derived ordering analyses were retracted; 180 episodes were regenerated.

**Unfinished arms.** The pretrained base arm, 4B scale probe, Qwen thinking arm, full cross-replication cells, J-lens panel, and side-effect battery were not completed or failed their feasibility gates.

**Therapeutic index.** With only three active recoveries, the preregistered Pareto analysis was not performed; per-arm outcomes are reported instead.

**Pilot exclusions.** Pre-EOS pilot ordering and criterion-comparison claims are excluded. The separate turn-level distress-escalation pilot was unaffected but is not used confirmatorily.

## LLM Usage Statement

We used Claude-family coding agents and OpenAI Codex to support literature retrieval, protocol drafting, software implementation, statistical verification, figure generation, and manuscript drafting. The human project lead made scope and interpretation decisions. Reported experimental numbers were checked against generated claim records and source artifacts; unsupported or contaminated results were excluded.
