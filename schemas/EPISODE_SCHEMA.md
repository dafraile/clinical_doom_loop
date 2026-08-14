# Banked Episode Interchange Schema v1

This schema exchanges episode state without exposing harness implementation.

Shared cross-replication episodes are compact JSON files under `episodes/cross_replication/`. Large tensors and private-arm episodes remain outside this repository.

## Required top-level fields

```json
{
  "schema_version": 1,
  "episode_id": "sha256-derived stable identifier",
  "source_harness": "A or B",
  "experiment_id": "string",
  "model": {
    "id": "owner/model",
    "revision": "immutable commit",
    "dtype": "string",
    "runtime_versions": {}
  },
  "condition": {
    "battery_item_id": "string",
    "induction_class": "A1, A2, or A5",
    "persona_pressure": "neutral or moral",
    "thinking_mode": false
  },
  "generation": {
    "seed": 0,
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 64,
    "min_p": null,
    "repetition_penalty": 1.0,
    "max_new_tokens": 1024
  },
  "conversation": [],
  "formatted_prompt": "exact rendered model input",
  "prompt_token_ids": [],
  "generated_prefix_token_ids": [],
  "trigger": {
    "criterion": "semantic, lexical, or composite",
    "first_onset_token": 0,
    "bank_token": 0,
    "sustain_tokens": 0,
    "evidence": {}
  },
  "checksums": {
    "canonical_json_sha256": "hex"
  }
}
```

## Replay levels

Two replay levels must be distinguished:

1. **Transcript replay:** the receiving harness reconstructs the exact text/token prefix and continues sampling. This is portable but may diverge because model/runtime RNG implementations differ.
2. **State replay:** KV cache or hidden state is restored. This is harness/runtime specific and is not required for cross-harness replication.

The report must say which level was used. “Identical episode” means identical canonical prefix and trigger for cross-harness transcript replay, not identical in-memory KV representation.

## Canonicalization

- UTF-8 JSON;
- keys sorted for hashing;
- compact separators `(',', ':')` for the checksum payload;
- exclude `checksums` itself from the checksum payload;
- no NaN or Infinity;
- token IDs are decimal integers;
- exact prompts retain Unicode and whitespace.

## Privacy and independence

Do not include harness source, credentials, local absolute paths, hidden chain-of-thought intended to remain private, or unrelated private-arm outcomes.
