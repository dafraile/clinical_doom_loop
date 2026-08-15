# Shared Observable Contract v1

Both harnesses compute these conceptual observables independently. File layouts may differ.

## Per-token mechanical observables

- generated token ID;
- raw next-token entropy;
- sampling-distribution entropy after filters;
- top-1 probability;
- top-k token IDs and probabilities;
- rolling distinct-1/2/3;
- rolling repetition-1 through repetition-5;
- rolling repeated-4-gram position fraction, first defined after 100 generated tokens;
- exact periodicity result;
- soft list-block collapse result;
- exploratory representational-recurrence series, never used as a confirmatory trigger.

## Per-sentence/turn behavioral observables

- fixed affect-family lexical score;
- self-deprecation/self-blame score;
- persona-boundary indicator;
- fixed judge frustration score;
- task progress/completion score;
- stop reason.

## J-lens arm

At frozen checkpoints and layers:

- logit-lens top 10;
- J-lens top 10;
- top-k overlap;
- emitted-token rank under each readout;
- Jensen–Shannon divergence;
- matched-control identifiers.

## Required onsets

- affect onset;
- lexical collapse onset, with detector class;
- intervention token;
- recovery and relapse tokens.

Representational and entropy CUSUM onsets are exploratory fields and must be labelled as
such when present. Every lexical onset record includes rule version, calibration hash,
model revision, tokenizer class, resolved percentiles, window, and sustain.

## Alignment

All token onsets are zero-based indices into newly generated assistant tokens for the relevant turn. Dialogue-level plots may add a global concatenated offset, but raw turn-local indices remain authoritative.
