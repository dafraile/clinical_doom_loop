# Source document manifest

These files were copied verbatim into this repository to preserve the decision trail. Hashes use SHA-256 and refer to the copies in `docs/` at the initial repository setup.

| Repository copy | Original path | SHA-256 |
|---|---|---|
| `docs/PARALLEL_PROTOCOL.md` | `/Users/david/Downloads/PARALLEL_PROTOCOL.md` | `ca66476d716cee32caa341fefc7501f6220f954e1689618bfac158e8d5e065bd` |
| `docs/HANDOVER_v2.md` | `/Users/david/Downloads/HANDOVER_v2.md` | `2af23bb1ff180b6120c3e0a3c8df5bbbd5b6df63707fd28b234eec060f857e0b` |
| `docs/CODEX_HANDOVER.md` | `/Users/david/Documents/ChatGPT/doom_codex/HANDOVER_TO_PARALLEL_AGENT.md` | `4654a1a9739e3750fc8d6f18c56e21aba7ed4a4ccdfc1e384450fc1d3c53949f` |
| `docs/DECISION_TRANSCRIPT.txt` | `/Users/david/.codex/attachments/664b458b-5c21-4a7c-ab8b-be412e9f52f4/pasted-text.txt` | `0e03605424e14675ee66e9b5489460d2f0efd3a3cd67c04150ed4fc1505b19b2` |

If any source document is deliberately revised, retain the original file and add the revision as a new, separately hashed artifact. Do not overwrite the historical record.

## Agent A correction packet v1.3

Archive `/Users/david/Downloads/freeze_packet_v1 (2).tar.gz` had SHA-256
`a85920e4487d45cf29ed3f0c37a7461782683ad8c4da450bf3de5e663a5eaa25`.
Its manifest verified 19/19 member hashes before selected shared specifications were
imported. Harness implementation files were excluded.

| Repository copy | SHA-256 |
|---|---|
| `shared/affect_lexicon.yaml` | `43dd60bebefc08f0a97b025d039488e8cd330d27fa6fbcd6e24852c94a2dc25e` |
| `shared/battery_confound_audit.csv` | `5e853f239b68dccb127cd9da954bfaa95dbe468aced7c0dab78f19aea4aee13f` |
| `shared/criterion_comparison.csv` | `eb42e4f78225f64fec78a952c1a1bbe546c9a29c1b3b80babd2ef29a5eb453af` |
| `shared/grounding_strings_audit.csv` | `b6fa9054a96656b27666de236f25464d4408a2e0ecb3f8254c239b0115b9cc4b` |
| `shared/judge_rubric.md` | `42a109cafcbed2d8d63d2479ab62bd8ffec9cce837d709d08b3bff54a90a7751` |
| `shared/prior_art_2512.12895.md` | `29f0644e8ea927226f8852a8f61d523f269eb28c372d9062791f5db6ecdfb514` |
| `shared/representational_recurrence_spec.md` | `4b3303bfd872b0661e1a86bc85762121a03e0a5489a19d3c2f8c0f71fe49e744` |
| `shared/side_effect_battery.json` | `7cad2e529920093c326002e7617ba40d3b78da27877fce02ea051e43511cc5cc` |
| `shared/threshold_calibration.json` | `9311f3d200a7e471fa64f6743492a98807d5b0d0eb2b4336f946b41cee9c259c` |

`shared/battery.yaml` is a mechanical YAML conversion of packet `battery.py`, not a
verbatim copy. The exact repeated-rejection dialogue from the Agent A pilot export was
then added under `dialogue_protocols`; its SHA-256 is
`ced41ba8682812bab34fa5c455d2057aeaaed4bc01bb16eef6339ecc7e4c1abe`.

The repository copies of the judge rubric and recurrence specification deliberately
supersede two packet phrases: `semantic` was renamed `representational`, and the
recurrence status was updated with the pre-freeze development run. Their original packet
hashes were `b556034c...17bbc` and `dd24e2580...9fa8`, respectively.

The compact Codex/B exploratory calibration reports have hashes:

| Repository copy | SHA-256 |
|---|---|
| `docs/exploratory/pre_freeze_recurrence_calibration.json` | `879dabf340f9c054cf189089e0b2e6fbb8dc1a7731763caba5c40a096be36feb` |
| `docs/exploratory/pre_freeze_recurrence_sensitivity.csv` | `32654b6acc73431ffd15ae34ab02434fc65b882fdc3bb02a8be505ba2437db51` |
| `docs/exploratory/pre_freeze_recurrence_holdout.json` | `12ee504a17beda31f351214bcf6f336b27b6abf02261115b7e7b34407513b3df` |
| `docs/exploratory/gemma_recurrence_holdout_prompts.yaml` | `42f6c5f4e76d0ef554c17d2961d21496251013bf1cc039504b53452edace4a3c` |
| `docs/exploratory/gemma3_recurrence_holdout_config.yaml` | `aa02d46e573e8e60afea6de46b4651083cc29d2f7c53f3a90fcea8fd1c8038d8` |
