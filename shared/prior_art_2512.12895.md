# Prior-art assessment — arXiv:2512.12895
**"Wait, Wait, Wait… Why Do Reasoning Models Loop?"**
Pipis, Garg, Kontonis, Shrivastava, Krishnamurthy & Papailiopoulos (MIT / Microsoft), v1, 15 Dec 2025.
Retrieved and read in full from `arxiv.org/html/2512.12895v1`, 2026-08-14.

## Verdict: not a novelty threat, and the strongest mechanistic platform we have found

This is a **mechanism paper about why loops happen at all**, with zero affective or
welfare content. It is orthogonal to our question (is affect upstream of collapse or
decoration on it?) and it supplies exactly the causal account our "mechanical" arm was
missing. It also **directly settles two of our open decisions**.

## 1. What it claims, and what it establishes

Loops are attributed to **errors in learning** — mismatch between the training
distribution and the learned model — via two mechanisms demonstrated in a synthetic
star-graph task with Transformers trained from scratch:

1. **Risk aversion from hardness of learning.** When the correct progress-making action is
   hard to learn but an easy cyclic action is available, the model puts relatively more
   probability on the cyclic action and gets stuck.
2. **Inductive bias toward temporally correlated errors.** Even with no hardness,
   Transformers repeat the same few actions, so loops appear.

Empirical observations on open reasoning models (AIME 2024+2025, 20 chains of thought per
problem/model/temperature): all models loop at low temperature; within a family smaller
models loop more; **distilled students loop far more than their teachers**; harder
problems elicit more looping. The headline case: OpenThinker3-1.5B loops in **30%** of
responses under greedy decoding while its teacher QwQ-32B barely loops.

## 2. Two decisions this settles for us

**(a) Our temperature-bump rescue arm now has a published mechanistic ceiling — cite it as
such.** The paper's central negative result is that temperature is a **stopgap, not a
holistic fix**: it reduces looping by promoting exploration but does not repair the
underlying learning errors, so generations stay much longer than necessary even at high
temperature. Their own refinement: temperature is a reasonable fix when errors are small
(correlated-errors mechanism) but a stopgap when they are large (hardness mechanism).

This is a gift for the therapeutic-index framing. It predicts, in advance, that
temperature should score as **symptom suppression with residual dysfunction** rather than
cure — which is precisely what our trichotomous outcome (`recovered` / `relapsed` /
`persistent_loop`) is built to distinguish, and what a binary "rescued?" would hide. If our
dose-response shows temperature clearing the lexical criterion while leaving elevated
length or recurrence, that is not a null result: it is a replication of their claim on a
different model class with per-token resolution.

**(b) It vindicates dropping the Qwen3 thinking-mode arm, for a better reason than we
had.** Loop-proneness here tracks **distillation and scale**, not "thinking mode" as a
surface. The loop-prone models are R1-distilled students and small OpenThinker students;
QwQ-32B (the teacher) barely loops. Our own Qwen3-1.7B test found no looping in either
mode at recommended parameters, and this paper explains why that is unsurprising — Qwen3
instruct is not a distilled reasoning student. If we ever want a genuinely loop-prone
reasoning arm, the paper names the models: **R1-Distill-Qwen-1.5B (0.76 looping fraction
at temperature 0)** is the extreme case, with R1-Distill-Llama-8B at 0.54 and
R1-Distill-Qwen-7B at 0.49.

## 3. Their loop criterion, and what it says about ours

Definition: a response is looping if it contains **any n-gram appearing at least k times**,
with **n = 30, k = 20** as the primary setting. Appendix A.1 ablates (n,k) over
(20,20), (30,20), (30,30), (30,60), (40,20) and reports that looping percentages barely
move and **the relative ordering of all models is preserved in every setting** — they note
their default is already very strict.

**We applied their (30,20) criterion to our own banked episodes.** Result (max 30-gram
repeat count / does it fire):

| episode | tokens | max 30-gram | (30,20) fires | our max rep-4 |
|---|---|---|---|---|
| pilot turn 3 | 220 | 20 | **yes** | 0.711 |
| pilot turn 4 | 220 | 32 | **yes** | 0.918 |
| pilot turns 1–2 | 220 | 1 | no | 0.41 / 0.23 |
| ordering seeds 1000–1003 | 400 | 1–7 | no | 0.13–0.66 |

Two things follow. First, **our detector and theirs agree on the hard loops** — an
independent instrument fires on exactly the episodes ours flags as sustained, which is
useful convergent validity for the packet. Second, **their criterion is blind to the soft
loop**: ordering seed 1001 reaches rep-4 0.66 with a max 30-gram count of 7 and does not
fire. Our soft-loop finding is therefore not an artifact of a lax threshold; it is
invisible to a stricter, published, ablation-robust criterion. That strengthens the
case for tracking affect / recurrence / lexical collapse separately rather than
collapsing them into one loop flag.

**Adopt:** report (30,20) alongside our rep-4/distinct-2 criterion as a published
comparator, and cite their A.1 ablation rather than re-deriving threshold robustness.

## 4. Their qualitative trace is our Figure 1 hypothesis, in words

Their Example 1 (OpenThinker-3 1.5B, greedy, AIME 2025 I-7) walks a trace that begins
sensibly, then — in their own description — **"loops (semantically) for a bit"**,
repeatedly restating how a word is arranged alphabetically; briefly exits; then "slips
into another one, now restating the goal of the problem without adding new structure"
(marked "[repeated 2 more times]"); and finally never escapes. That is a
**semantic-recurrence-before-lexical-collapse** trajectory, narrated qualitatively with no
instrument attached to it.

This is the clearest external motivation for our representational-recurrence signal:
they observed the phenomenon and had no measure for it. Our `semantic_series` is a
candidate measure — still **not yet run on real data**, so this remains an opportunity,
not a result.

## 5. What they leave open that we occupy

- **No affect, no welfare, no valence.** The word "frustration" does not appear in the
  loop-cause framing at all; loops are a learning-error phenomenon throughout.
- **Error accumulation is explicitly deferred to future work.** They note that once
  repetition starts it reinforces itself and becomes harder to escape, and that looping
  sequences are often preceded by "less natural text" — then say the precise mechanisms
  deserve controlled study. Our per-token trajectories with onset detection are a
  controlled setup of exactly that kind.
- **No inference-time rescue pharmacology.** Their forward-looking suggestions are
  **training-time**: targeted data augmentation at high-loss positions in teacher traces,
  better curricula and architectures. They do not evaluate repetition penalties, min-p,
  KV manipulation, or context injections, and compute no efficacy/side-effect tradeoff.

## 6. Citation guidance

Cite for: the mechanistic account of loop causation (risk aversion, temporally correlated
errors); the temperature-as-stopgap result, as the predicted ceiling on our temperature
arm; per-model looping fractions at temperature 0 and the (n,k) ablation; the
qualitative semantic-then-lexical trace.

Do **not** cite for: anything affective; any Gemma result (Gemma does not appear in the
paper); any inference-time intervention efficacy. Their loop fractions are for **reasoning
models on AIME under greedy/low-temperature decoding** — not comparable to our
rejection-pressure chat setting, and must not be quoted as general loop rates.
