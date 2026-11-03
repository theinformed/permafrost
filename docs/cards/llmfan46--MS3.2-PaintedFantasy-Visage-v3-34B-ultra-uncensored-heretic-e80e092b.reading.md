# Reading of the Stage 1 and Stage 2 result: llmfan46/MS3.2-PaintedFantasy-Visage-v3-34B-ultra-uncensored-heretic against zerofata/MS3.2-PaintedFantasy-Visage-v3-34B (2026-11-03)

Measured on Wheat, round 49 piece 3 (download job 387515, compare job 387518, sweep 387524; the pull carries the
measurements and the sweep record and no job log). Modified revision `0011aca6` (created 2026-03-27 15:50Z, the
weights uploaded at 15:55Z, `special_tokens_map.json` added at 17:09Z and the card edited thirteen times to 19:49Z),
parent pinned at `0c18eaaa` of 2025-09-29, zerofata's PaintedFantasy Visage v3, a 34B depth extension of
ConicCat/Mistral-Small-3.2-AntiRep-24B. Its card publishes the merge: a `passthrough` of the AntiRep model's layers
0 to 28 followed by its layers 10 to 39, 59 layers in all ("Upscale redone with the missing final layer
included"), then continued pretraining, supervised training and preference training through a rank-32 adapter. The
card is Heretic 1.2.0's arbitrary-rank table: `start_layer_index` 3, `end_layer_index` 29,
`preserve_good_behavior_weight` 0.8481, `steer_bad_behavior_weight` 0.0002, `overcorrect_relative_weight` 0.8911,
`neighbor_count` 5, `attn.o_proj` the one target, a KL divergence of 0.0195 and 4 refusals in 100 against 90. The
parent counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 11 flags (first shares 0.747 to
0.973 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is the branch on the
attention outputs of the card's window to the layer, all of it inside the first of the merge's two stacks.

- 11 of 534 tensors changed: the attention outputs of layers 10, 13 to 19, 21, 24 and 27. The other fifteen of
  the window (layers 3 to 9, 11, 12, 20, 22, 23, 25, 26 and 28) moved by 0.0000094 to 0.000268, the largest relative
  change outside the changed set; layers 0 to 2 and 29 to 58, the second stack whole, read exactly 0, as does every
  tensor that is not an attention output.
- One direction per matrix (agreement 0.376 at the median), first shares 0.747 to 0.973.
- Input side on all 11: one minus the right kept fraction reads 1.28 to 2.39 (2.39 at layer 24, 2.21 at 10), the
  left side keeps 0.46 to 0.78; no kept fraction of any of the eight saved components is above 1 (the largest
  0.997), so no component is amplified.
- Relative changes 0.0178 to 0.0404; rows moved 0.0016 to 0.0246 under a card that claims no norm.

| Layer | Change | E1 | Left kept | Right kept | Weight (one minus right kept) | Rows |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | 0.0404 | 0.789 | 0.56 | -1.21 | 2.21 | 0.0056 |
| 13 | 0.0377 | 0.747 | 0.46 | -0.81 | 1.81 | 0.0042 |
| 16 | 0.0215 | 0.960 | 0.71 | -0.39 | 1.39 | 0.0028 |
| 19 | 0.0178 | 0.961 | 0.78 | -0.28 | 1.28 | 0.0016 |
| 21 | 0.0326 | 0.878 | 0.76 | -0.76 | 1.76 | 0.0045 |
| 24 | 0.0392 | 0.780 | 0.66 | -1.39 | 2.39 | 0.0049 |
| 27 | 0.0321 | 0.973 | 0.75 | -0.82 | 1.82 | 0.0028 |

The full table (11 rows) is in the report.

Directions. The window lies where the merge's layers keep the AntiRep model's numbering (layers 3 to 28 of both),
so the saved vectors of the Mistral Small 24B measurements compare layer for layer. The direction stands on the left
at 0.836 (0.903 on the right) to the maker's first Magistral Small 2509 search (5 names), 0.814 (0.922) to the
maker's Mistral Small 3.2 search (4 names) and 0.635 (0.902) to the maker's second Magistral search (11 names), and
at 0.15 or less to every projection and kernel pass on the 5,120 hidden size, Skyfall's of this round at 0.103. By
byte range the parent's layer 5 query projection stands 0.0119 from the AntiRep model's and its layer 20 attention
output 0.0225; its layer 29, the first of the second stack, stands 0.032 from the AntiRep model's layer 10 and 0.035
from its own layer 10, so the two copies of a source layer were trained apart; and the AntiRep model stands 0.0014
and 0.0031 from Mistral Small 3.2 on the same two matrices.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, 1,015 fields, the home judgement closing
`config.rope_parameters` (the 5.x form of `rope_theta`, loaded as the same value). The copy is a transformers 5.3.0
save: its 354-byte `tokenizer_config.json` drops the 1,000 `added_tokens_decoder` declarations the parent's
198,054-byte file carries (the 1,000 fields; finding 44's form), its `tokenizer.json` is rewritten (17,078,192 bytes
against 17,078,037), and its `special_tokens_map.json` is the parent's by object id, uploaded on its own an hour and
a quarter after the weights. The generation file adds `pad_token_id` 11 and the 5.x output defaults, drops
`do_sample` and turns `use_cache` on; the configuration writes `torch_dtype` as `dtype`. The template is the parent's
2,671 bytes with Windows line endings on its 51 lines (2,722 bytes), which the tool reads as equal after line
endings: the maker's 31B copies carry the maker's own template with Windows line endings (finding 140), and this one
carries the parent's the same way. The token ids are Mistral's on both sides (`bos_token_id` 1, `eos_token_id` 2, no
pad in the configuration) and the vocabulary is 131,072.

## For the recipe library

An arbitrary-rank entry with a trace line would read the copy; the per-layer entry charges its first shares. A pin
note naming the passthrough ranges of a depth-extended parent would let the reading map each layer to its source
before the download. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat49/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
