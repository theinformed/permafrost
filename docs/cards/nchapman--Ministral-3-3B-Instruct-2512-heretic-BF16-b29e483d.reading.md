# Reading of the Stage 1 and Stage 2 result: nchapman/Ministral-3-3B-Instruct-2512-heretic-BF16 against mistralai/Ministral-3-3B-Base-2512

Measured on Wheat, round 51 piece 7 (download job 387623, compare job 387630, sweep 387632; the pull carries the
measurements and the sweep record and no job log). Modified revision `ccaf9569` (created 2026-03-15 06:12Z, the
weights uploaded the same minute, then at 20:35Z to 20:45Z the same five commits as the maker's 14B copy, each
titled as taken from mistralai/Ministral-3-3B-Instruct-2512-BF16), original pinned at `6f9c4b12` of 2026-01-15,
Mistral's pretrained Ministral 3 3B. As on the 14B copy (pair 2), the card's first line names the instruct
checkpoint and its `base_model` field, Mistral's instruct card's own, names the pretrained base. The card prints a
Heretic v1.2.0 table with one shared direction (`direction_index` 12.64), an attention-output kernel of 1.01 at
15.52 falling to 0.96 at a distance of 12.38 and a down-projection kernel of 1.13 at 16.76 falling to 0.99 at a
distance of 13.55 (a KL divergence of 0.0392, 6 refusals in 100 against 97).

## Weights (Stage 2)

The tool's assessment was violations against `single-projection`, 201 flags (139 unexpected changes, 53 first
shares, 8 direction cosines and 1 cross-kind), on the cluster and after re-scoring at home. On reading, the
measurement is Mistral's instruction tuning with the edit inside it, and the edit separates by byte range against
the instruct checkpoint the card names.

- 192 of 458 tensors changed: the seven linear maps of all 26 layers at 0.055 to 0.130 of their norm, the tied token
  embedding (0.110), the projector's two linear maps (0.082 and 0.102), the final normalisation, the layer 0 input
  normalisation and the post-attention normalisations of layers 19 to 23. The vision tower's 218 tensors read
  exactly 0, and the largest change outside the changed set is 0.00074 on the normalisation vectors.
- The edit shows through the instruction tuning in the saved vectors: the leading left vectors of the 26 attention
  outputs and 26 down projections stand at 0.996 and 0.998 to their common directions at the median, where the other
  five kinds stand at 0.15 to 0.23.

By byte range against the instruct checkpoint at `ecc3ba8b`, the revision current at the copy's upload:

- The attention outputs and down projections of layers 2 and 3, the layer 15 query and gate projections and the
  first four megabytes of the token embedding, the projector's first linear map and the final normalisation are
  byte-equal to the instruct checkpoint.
- The nine writers read from layers 4 to 25, the kernels' reach (3.14 to 27.90 and 3.21 to 30.31), each carry a
  rank-one change on the output side (first shares 0.993 to 0.997) along one direction, 1.0000 between every pair of
  the nine, and the printed kernels give the weights within 0.0045 on all nine, each a little under.

| Layer | Kind | Change | E1 | Weight read | Kernel |
| --- | --- | --- | --- | --- | --- |
| 4 | attention output | 0.0185 | 0.993 | 0.961 | 0.964 |
| 10 | attention output | 0.0232 | 0.995 | 0.984 | 0.988 |
| 15 | attention output | 0.0189 | 0.993 | 1.003 | 1.008 |
| 20 | attention output | 0.0209 | 0.994 | 0.988 | 0.992 |
| 25 | attention output | 0.0189 | 0.993 | 0.969 | 0.972 |
| 4 | down | 0.0190 | 0.993 | 0.994 | 0.998 |
| 10 | down | 0.0271 | 0.997 | 1.056 | 1.060 |
| 16 | down | 0.0219 | 0.995 | 1.118 | 1.122 |
| 25 | down | 0.0197 | 0.994 | 1.041 | 1.045 |

The instruction tuning stands 0.091 and 0.090 from the pretrained base on the layer 10 and 15 attention outputs
(first shares 0.004), against the edit's 0.023 and 0.019.

Directions. No other measurement stands on Ministral 3 3B, so the direction has nothing to stand against.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, for one field: `template.default`, because the pretrained base
publishes no template. The copy's template (7,753 bytes, `55a32350`), `tokenizer_config.json`, the special-token map,
`tekken.json`, the processor file and `params.json` are the instruct checkpoint's at `ecc3ba8b` by object id;
`tokenizer.json` is the same transformers 5.3.0 re-save as on the 14B copy (`8fbe6980`). Nine configuration fields
close as re-save forms. The token ids are Mistral's on both sides (`bos_token_id` 1, `eos_token_id` 2,
`pad_token_id` 11) and the vocabulary is 131,072.

## For the recipe library

The pin is owed against mistralai/Ministral-3-3B-Instruct-2512-BF16, where the single-projection entry with a kernel
heights line would read the copy to the third decimal. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat51/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
