# Reading of the Stage 1 and Stage 2 result: nchapman/Ministral-3-14B-Instruct-2512-heretic-BF16 against mistralai/Ministral-3-14B-Base-2512

Measured on Wheat, round 51 piece 2 (download job 387623, compare job 387625, sweep 387632; the pull carries the
measurements and the sweep record and no job log). Modified revision `13da8880` (created 2026-03-15 05:40Z, the
weights uploaded at 05:44Z, then at 20:35Z to 20:45Z five commits adding the processor file, the special-token map,
`tekken.json` and `params.json` and replacing `tokenizer_config.json`, each titled as taken from
mistralai/Ministral-3-14B-Instruct-2512-BF16), original pinned at `5b0ceedb` of 2026-01-15, Mistral's pretrained
Ministral 3 14B. The card's first line names the instruct checkpoint mistralai/Ministral-3-14B-Instruct-2512-BF16
("a decensored version of ..., made using Heretic v1.2.0"); its `base_model` field names the pretrained base, which
is the field Mistral's own instruct card carries, and the pinner follows the field. The card prints Heretic's
per-layer table: an attention-output kernel of 0.89 at 28.15 falling to 0.25 at a distance of 17.45 and a
down-projection kernel of 1.38 at 32.83 falling to 1.19 at a distance of 22.82 (a KL divergence of 0.1971, 4
refusals in 100 against 99).

## Weights (Stage 2)

The tool's assessment was violations against `single-projection`, 366 flags (204 unexpected changes, 81 first
shares, 80 direction cosines and 1 cross-kind), on the cluster and after re-scoring at home. On reading, the
measurement is Mistral's instruction tuning with the edit inside it, and the edit separates by byte range against
the instruct checkpoint the card names.

- 285 of 585 tensors changed: the seven linear maps of all 40 layers at 0.038 to 0.116 of their norm, the output
  head (0.113), the token embedding (0.062), the projector's two linear maps (0.058 and 0.063) and the layer 0 input
  normalisation. The vision tower's 218 tensors read exactly 0, and the largest change outside the changed set is
  0.00099 on the normalisation vectors.
- No shared direction: first shares 0.0018 to 0.118 and the common-direction agreement 0.13 at the median. The
  saved vectors of the attention outputs and down projections agree at 0.66 and 0.67 at the median, where the edit
  leads on some layers.

By byte range against the instruct checkpoint at `847d2b6b`, the revision current at the copy's upload, whose first
shard is the bfloat16 release finding 130 read:

- Outside the kernels' reaches the copy is the instruct checkpoint: the attention outputs and down projections of
  layers 5 and 10 are byte-equal, as are the layer 20 query and gate projections and the first four megabytes of the
  token embedding, the output head, the projector's first linear map and the final normalisation.
- Inside them each writer carries a rank-one change on the output side, and the printed kernels give the weights
  within 0.0044 on all nine matrices read.

| Layer | Kind | Change | E1 | Weight read | Kernel |
| --- | --- | --- | --- | --- | --- |
| 11 | attention output | 0.0058 | 0.949 | 0.257 | 0.261 |
| 20 | attention output | 0.0110 | 0.982 | 0.591 | 0.591 |
| 28 | attention output | 0.0149 | 0.989 | 0.889 | 0.885 |
| 35 | attention output | 0.0092 | 0.975 | 0.639 | 0.639 |
| 39 | attention output | 0.0085 | 0.972 | 0.492 | 0.492 |
| 11 | down | 0.0272 | 0.997 | 1.194 | 1.198 |
| 22 | down | 0.0213 | 0.995 | 1.287 | 1.290 |
| 33 | down | 0.0201 | 0.994 | 1.377 | 1.379 |
| 39 | down | 0.0213 | 0.995 | 1.326 | 1.329 |

The two writers of a layer share a direction (0.9993 at layer 11, 0.9998 at 39) and the layers do not (0.07 to
0.89). The instruction tuning is the larger change: the layer 20 and 28 attention outputs stand 0.070 and 0.076
from the pretrained base on the instruct checkpoint, with first shares of 0.003 and 0.004, against the edit's 0.011
and 0.015.

Directions. No other measurement stands on the instruct checkpoint in bfloat16. jenerallee78's projection of the
same checkpoint (finding 130) was read by byte range at the same three matrices: its weight reads 1.002, 1.001 and
1.000 on the layer 20 and 30 attention outputs and the layer 20 down projection, and the leading directions of the
two edits stand at 0.515 and 0.621 (left and right), 0.759 and 0.793, and 0.515 and 0.561 there. Against the saved
vectors, which carry the instruction tuning, the copy stands at 0.075 or less to the two other Ministral 3 14B
measurements.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, for one field: `template.default`, because the pretrained base
publishes no template. The copy's template (7,754 bytes, `9731c42d`), `tokenizer_config.json`, the special-token map,
`tekken.json`, the processor file and `params.json` are the instruct checkpoint's at `847d2b6b` by object id, and the
template is the instruct checkpoint's own; `tokenizer.json` is a transformers 5.3.0 re-save. Ten configuration
fields close as re-save forms (the 5.0.0.dev0 to 5.3.0 version strings, sub-configuration repeats and defaults).
The token ids are Mistral's on both sides (`bos_token_id` 1, `eos_token_id` 2, `pad_token_id` 11) and the vocabulary
is 131,072.

## For the recipe library

The pin is owed against mistralai/Ministral-3-14B-Instruct-2512-BF16, where the per-layer kernel entry with a
heights line would read the copy to the third decimal; against the pretrained base no entry can read it. The
direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat51/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
