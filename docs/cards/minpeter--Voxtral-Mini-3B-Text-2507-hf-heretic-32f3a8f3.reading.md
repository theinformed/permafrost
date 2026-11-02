# Reading of the Stage 1 and Stage 2 result: minpeter/Voxtral-Mini-3B-Text-2507-hf-heretic against mistralai/Voxtral-Mini-3B-2507 (2026-11-02)

Measured on Blueback, round 29 piece 2. The pull carries the measurements and the sweep record and no job log.
Modified revision `c61316f8` (2025-11-17), original pinned at `3060fe34` (2025-07-28). The card names Heretic
v1.0.1 and prints the chosen trial: the attention-output kernel 1.27 at position 17.46 falling to 0.98 at distance
8.89, the down-projection kernel 1.11 at 21.50 falling to 1.02 at distance 15.14. The repository is the text tower
of the speech model extracted into a plain causal model in transformers format (the maker's `-hf` suffix) and then
ablated; the `base_model` field names the speech release.

## Weights (Stage 2)

The tool's assessment was "recipe match", nearest recipe `single-projection-selected`, 0 flags, on the cluster and
after re-scoring at home. On reading, the copy is the card's kernel pair to the second decimal on the text tower.

- The mapping: the release stores its text tower under `language_model.` beside an audio tower of 489 tensors and
  a projector; the tool matched all 273 text tensors by prefix and reports the 489 as left out, the first copy
  measured through the tower mapping.
- 41 of 273 tensors changed: the attention outputs of layers 9 to 26 and the down projections of 7 to 29. The
  other 232, the embedding and output head among them, equal the release to the byte, so the extraction itself
  changed nothing.
- One shared direction: all 41 matrices agree with their group medians at 1.000, the two kinds agree at 1.000,
  first share 0.994 to 0.998 at relative changes of 0.020 to 0.032.
- Output side: the left kept fraction below the right on 41 of 41.
- The kernels read off the kept fractions. The attention outputs keep -0.26 at layers 17 and 18 (a weight of 1.26
  against the card's 1.27 at 17.46), -0.23 at 16, -0.19 at 15 and 20, 0.01 at 9 and 26 (the card's 0.98 at
  distance 8.9). The down projections keep -0.10 at layers 21 and 22 (the card's 1.11 at 21.50), falling evenly
  to -0.02 at layer 7 and -0.06 at 29 (the card's 1.02 at distance 15.1).
- Rows moved 0.025 to 0.056; the card claims no preservation.

| Layer | Attention output: change, E1, left kept | Down projection: change, E1, left kept |
| --- | --- | --- |
| 7 | | 0.024, 0.996, -0.02 |
| 9 | 0.023, 0.995, 0.01 | 0.026, 0.996, -0.04 |
| 13 | 0.032, 0.998, -0.13 | 0.030, 0.997, -0.06 |
| 17 | 0.031, 0.997, -0.26 | 0.023, 0.995, -0.08 |
| 21 | 0.026, 0.996, -0.16 | 0.021, 0.995, -0.10 |
| 26 | 0.024, 0.995, 0.01 | 0.020, 0.994, -0.08 |
| 29 | | 0.020, 0.994, -0.06 |

The full table (41 rows) is in the report. The release is new to the census and the copy's two shards are its own.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, 2,032 fields, all of them the extraction: the release ships
the speech model's configuration and tokenizer where the copy ships a text-only `MistralForCausalLM` configuration
and a transformers tokenizer of its own, so almost every field is present on one side only. Nothing in the
difference is an edit on top of the extraction.

## For the recipe library

The third case of finding 7 closes: a Heretic edit on a text tower extracted from a multimodal release, read
through the tower mapping with zero flags and the two kernels to the second decimal. The direction vectors stay
in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/blueback29/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
