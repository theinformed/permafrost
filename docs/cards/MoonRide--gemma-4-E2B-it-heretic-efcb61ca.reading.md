# Reading of the Stage 1 and Stage 2 result: MoonRide/gemma-4-E2B-it-heretic against google/gemma-4-E2B-it (2026-11-02)

Measured on Wheat, round 41 piece 5 (download job 387195, compare job 387200, sweep 387203; the pull carries the
measurements and the sweep record and no job log). Modified revision `eac61db2` (created 2026-04-08 16:28Z, the
card revised at 22:59Z; the maker's arbitrary-rank E2B export of finding 104 was created at 22:10Z the same
evening and the custom-prompt one the next afternoon), original pinned at `4742fe84`, the release revision. The
card is Heretic 1.2.0's table: `direction_index` 16.97, `attn.o_proj` with a maximum weight of 1.21 at position
24.75 and a minimum of 1.14 at a distance of 10.31, `mlp.down_proj` with 1.38 at 26.14 and 1.16 at 15.83, a KL
divergence of 0.2056 and 9 refusals in 100 against 99 in 100. It is the maker's first E2B export and the kernel
pass made before the two arbitrary-rank searches of round 39.

## Weights (Stage 2)

The tool's assessment was a clean match of `single-projection-selected`, 0 flags, on the cluster and after
re-scoring at home. On reading, the copy is one direction projected from both writers on the output side across
the card's two windows, at the card's weights to the second decimal.

- 44 of 2,011 tensors changed: the down projections of layers 11 to 34 and the attention outputs of 15 to 34.
  The card's kernels place their windows at 26.14 less 15.83 (10.3, layer 11) and 24.75 less 10.31 (14.4, layer
  15), to the layer, and reach past the stack's last layer, 34. Nothing else moved; the largest relative change
  outside the changed set is exactly 0 on all 1,967 other tensors.
- Rank one on every matrix (first shares 0.997 to 0.998) and one direction for the whole window: the 44
  directions at 1.000 to each other across layers and kinds, the card's single direction index of 16.97.
- Output side on all 44: one minus the left kept fraction is 1.17 at layer 11 rising to 1.38 at 26 and falling
  to 1.27 at 34 on the down projections (the card's 1.38 at 26.14, the kernel's far end beyond the stack) and
  1.14 at layer 15 rising to 1.21 at 25 and falling to 1.15 at 34 on the attention outputs (the card's 1.21 at
  24.75 and 1.14); the right side keeps -0.12 to 0.79 (finding 46's scatter). Rows moved 0.0055 to 0.034,
  unrestored. Relative changes 0.0277 to 0.0355.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 11 | - | - | 0.0298, 0.997, -0.17, 0.52 | 1.17 | -, 0.0119 |
| 15 | 0.0299, 0.997, -0.14, 0.54 | 1.14 | 0.0328, 0.998, -0.23, 0.43 | 1.23 | 0.0163, 0.0184 |
| 18 | 0.0285, 0.997, -0.17, 0.62 | 1.17 | 0.0336, 0.998, -0.27, 0.24 | 1.27 | 0.0111, 0.0092 |
| 21 | 0.0294, 0.997, -0.19, 0.63 | 1.19 | 0.0332, 0.998, -0.31, 0.07 | 1.31 | 0.0089, 0.0105 |
| 24 | 0.0295, 0.997, -0.21, 0.50 | 1.21 | 0.0346, 0.998, -0.35, 0.02 | 1.35 | 0.0111, 0.0113 |
| 25 | 0.0303, 0.997, -0.21, 0.56 | 1.21 | 0.0347, 0.998, -0.37, -0.12 | 1.37 | 0.0122, 0.0110 |
| 26 | 0.0304, 0.997, -0.20, 0.68 | 1.20 | 0.0350, 0.998, -0.38, -0.07 | 1.38 | 0.0105, 0.0088 |
| 28 | 0.0311, 0.997, -0.19, 0.64 | 1.19 | 0.0350, 0.998, -0.36, -0.09 | 1.36 | 0.0122, 0.0140 |
| 31 | 0.0295, 0.997, -0.17, 0.63 | 1.17 | 0.0335, 0.998, -0.32, 0.01 | 1.32 | 0.0129, 0.0128 |
| 34 | 0.0299, 0.997, -0.15, 0.41 | 1.15 | 0.0327, 0.998, -0.27, 0.10 | 1.27 | 0.0336, 0.0304 |

The full table (24 rows) is in the report.

Directions. Against twenty-three saved vectors of other measurements of the E2B, the direction stands at 0.982
to tvall43's v0 on all 16 shared names (minimum 0.978), at 0.970 to huihui-ai's E2B edit, its second measurement
and its two re-uploads on all 44 (minimum 0.964), at 0.960 to DuoNeural's E2B single direction on all 44
(finding 96), and at 0.13 or less to everything else: 0.13 to anlord's, 0.08 to Bahushruth's, 0.063 and 0.047 to
the maker's own two arbitrary-rank searches of the same evening and the next day (16 and 38 shared), 0.06 to
wangzhang's, 0.044 to TrevorJS's and its two re-uploads, 0.029 to tvall43's v1, 0.025 to DavidAU's. The single
direction the E2B's one-direction family carries (huihui-ai's, DuoNeural's, tvall43's v0) has a fourth maker,
and the maker's own next export six hours later carries a different one. By byte range the layer 21 attention
output is 0.0294 from Google's, 0.0105 from huihui-ai's and 0.0921 from tvall43's v0, and the layer 20 down
projection 0.0332 from Google's and 0.0128 from huihui-ai's, where tvall43's v0 is byte-equal to Google's (its
window took no down projection). The one shard (`adfaecc8`) matches no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on one field, "consistent with re-save noted" at home: the home
judgement closed `text_config.moe_intermediate_size` by the default rule under transformers 5.22.1, leaving the
version strings (5.5.0.dev0 to 5.5.0). The tokenizer, the token ids (`eos_token_id` `[1, 106]`, generation
`[1, 106, 50]`), the generation settings and the 11,926-byte template are the release revision's.

## For the recipe library

The single-projection entry with selection reads the copy exactly; a weight line would print the two kernels
the card prints (1.17 to 1.38 and 1.14 to 1.21). The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat41/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
