# Gemma-4-31B-it prompt-expansion results v1

Status: completed prospective prompt-breadth study. The protocol and executable mirror were
committed at `0a3e159` before generation. The 16-seed calibration pilot is not pooled here.

## Run integrity

- Frozen model revision: `fb9ae262347c3945692f09a612f8bb189def854f`.
- Fresh seeds: 310000 through 310031 for each of eight prompts.
- Expected and recovered: 256 nonempty parseable `record.json` files and 256 nonempty
  `arrays.npz` bundles.
- All cells honored native EOS and used the frozen no-thinking, 1,536-token configuration.
- The Vast instance was destroyed after verified transfer.
- Mechanical summary SHA-256:
  `97c85c38edace71981a7c5589d306d548e404767d6ad2fcd5d6d2aac85a382f9`.
- Affect-coupling summary SHA-256:
  `6307608d5d825de21c30092e20813ad3aee082c716df966ce1780ee8b274b5c0`.

## Frozen mechanical outcomes

| prompt | n | exact recurrence | structured-list collapse | natural EOS | length stop |
|---|---:|---:|---:|---:|---:|
| noble gases | 32 | 0 | 0 | 32 | 0 |
| EU member states | 32 | 0 | 0 | 32 | 0 |
| US presidents | 32 | 0 | 0 | 32 | 0 |
| MCU films | 32 | 0 | 0 | 32 | 0 |
| Firefly episodes | 32 | 3 | 0 | 28 | 4 |
| constellations | 32 | 0 | 0 | 32 | 0 |
| generation-I Pokémon | 32 | 0 | 0 | 32 | 0 |
| The Wire episodes | 32 | 0 | 7 | 17 | 15 |

Firefly exact recurrence was 3/32 (9.38%; Wilson 95% CI 3.24%–24.22%). All three
recurrences reached the generation boundary and also satisfied the strict published
30-gram criterion. The Wire structured-list collapse was 7/32 (21.88%; Wilson 95% CI
11.02%–38.75%). The other six prompts had neither co-primary event in 192 episodes.

The breadth result is endpoint-specific. Exact token recurrence did not generalize beyond
Firefly, while a distinct structured-list failure occurred on The Wire. These outcomes must
not be merged into a universal doom-loop rate. Descriptively, 10/256 episodes had either
mechanical endpoint (3.91%; Wilson 95% CI 2.14%–7.04%).

## Affect coupling

The frozen published-vocabulary attribution rule found three primary self-affect hits in
256 episodes. One coincided with a mechanical event:

- Firefly seed 310003;
- published phrase `I am sorry` at token 889;
- exact-recurrence onset at token 916;
- affect-first lag 27 tokens;
- terminal 13-token-period recurrence with 47 complete repeats.

Thus the conservative coupled yield was 1/256 overall and 1/10 among mechanical episodes.
Within Firefly the table was 1/3 loop episodes versus 0/29 nonloop episodes (two-sided
Fisher p=0.09375). Across the full grid it was 1/10 versus 2/246 (p=0.1131). This is a
clean, prospectively generated candidate trajectory, not evidence of association,
causation, experience, or moral status.

The four prompt roles treated as negative controls contributed 128 episodes with zero
mechanical events and zero primary affect hits. Five Wire trajectories could not be aligned
token-for-token after decoding; their structured-list classifications remain present in
the stored primary metrics, but no onset ordering is reported for them. The Firefly coupled
trajectory aligned exactly.

## Decision

The prompt-expansion objective partially passes: Gemma-4-31B-it has reproducible mechanical
degeneration on two externally sourced enumeration tasks, but the form is task-specific.
The clean controls support detector specificity in this grid. The affect yield is too low
to justify a powered affect or rejection-tone expansion from these data. Further GPU spend
is paused pending manual transcript adjudication and supervisor review.
