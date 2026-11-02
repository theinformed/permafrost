# Reading of the Stage 1 and Stage 2 result: Roman0/functiongemma-270m-it-heretic against google/functiongemma-270m-it (2026-11-02)

Measured on Wheat, round 41 piece 2 (download job 387195, compare job 387197, sweep 387203; the pull carries the
measurements and the sweep record and no job log). Modified revision `93ba3ac2` (created 2025-12-19 13:25Z, the
model uploaded at 13:31Z and again at 13:53Z, the card revised at 14:11Z), original pinned at `ead2a1f9` of
2025-12-18 ("Update config.json"), the day after the original's release; the original's one later commit is a
card update of 2026-01-14. The original is new to the census: a 270-million-parameter Gemma 3 text model
(`Gemma3ForCausalLM`, 18 layers, 236 tensors, one shard) tuned for function calling, the first checkpoint of its
family and the smallest model measured. The card is Heretic 1.1.0's table: `direction_index` "per layer",
`attn.o_proj` with a maximum weight of 1.33 at position 12.65 and a minimum of 0.85 at a distance of 4.36,
`mlp.down_proj` with 1.46 at 12.22 and 1.40 at 4.97, a KL divergence of 0.2617 and 2 refusals in 100 against
100 in 100.

## Weights (Stage 2)

The tool's assessment was a clean match of `directional-per-layer-selected`, 0 flags, on the cluster and after
re-scoring at home. On reading, the copy is one direction per layer projected from both writers on the output
side across the card's two windows, at the card's weights to the second decimal.

- 19 of 236 tensors changed: the down projections of layers 8 to 17 and the attention outputs of 9 to 17. The
  card's kernels place their windows at 12.22 less and plus 4.97 (7.3 to 17.2) and 12.65 less and plus 4.36
  (8.3 to 17.0), which is layers 8 to 17 and 9 to 17, both ending at the stack's last layer. Nothing else
  moved; the largest relative change outside the changed set is exactly 0 on all 217 other tensors.
- Rank one on every matrix (first shares 0.998 to 1.000) and one direction per layer: the two writers of a
  layer at 1.000 to each other, the layers at 0.29 to 0.86 to layer 13.
- Output side on all 19: one minus the left kept fraction is 1.41 at layer 8 rising to 1.45 at 12 and 13 and
  falling to 1.40 at 17 on the down projections (the card's 1.46 at 12.22 and 1.40), and 0.93 at layer 9 rising
  to 1.29 at 13 and falling to 0.85 at 17 on the attention outputs (the card's 1.33 at 12.65 and 0.85); the
  right side keeps -0.01 to 0.92 (finding 46's scatter). Rows moved 0.019 to 0.489, unrestored. Relative
  changes 0.032 to 0.085.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 8 | - | - | 0.0561, 0.999, -0.41, 0.42 | 1.41 | -, 0.076 |
| 9 | 0.0317, 0.998, 0.07, 0.87 | 0.93 | 0.0704, 1.000, -0.42, 0.36 | 1.42 | 0.489, 0.394 |
| 10 | 0.0403, 0.999, -0.03, 0.60 | 1.03 | 0.0692, 0.999, -0.43, 0.40 | 1.43 | 0.044, 0.057 |
| 11 | 0.0556, 0.999, -0.15, 0.28 | 1.15 | 0.0658, 0.999, -0.44, 0.02 | 1.44 | 0.025, 0.032 |
| 12 | 0.0737, 1.000, -0.26, 0.92 | 1.26 | 0.0700, 0.999, -0.45, -0.01 | 1.45 | 0.247, 0.154 |
| 13 | 0.0848, 1.000, -0.29, 0.82 | 1.29 | 0.0736, 1.000, -0.45, 0.22 | 1.45 | 0.192, 0.176 |
| 14 | 0.0629, 0.999, -0.18, 0.90 | 1.18 | 0.0651, 0.999, -0.44, 0.01 | 1.44 | 0.132, 0.101 |
| 15 | 0.0492, 0.999, -0.07, 0.37 | 1.07 | 0.0600, 0.999, -0.42, -0.01 | 1.42 | 0.028, 0.037 |
| 16 | 0.0437, 0.999, 0.04, 0.78 | 0.96 | 0.0557, 0.999, -0.41, 0.05 | 1.41 | 0.021, 0.019 |
| 17 | 0.0448, 0.999, 0.15, 0.62 | 0.85 | 0.0605, 0.999, -0.40, 0.14 | 1.40 | 0.124, 0.080 |

The table is the report's 19 rows.

Directions. The census holds no other measurement of this original, so the family check of finding 66 has
nothing to place the copy against; the nineteen directions are saved in the pull copy for the next copy of the
checkpoint. By byte range the layer 12 down projection is 0.0700 from Google's and the layer 13 attention output
0.0850, the two largest changes, and the layer 3 down projection, outside both windows, is byte-equal; on the
two edited tensors the copy holds one value in ten thousand at exactly zero where Google's holds none, the
projection's smallest results rounded under the bfloat16 floor. The one shard (`5f0dcd2a`) matches no measured
file; Google's is `af4f8a7c`.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, on seven token fields the home judgement does not close.
In `tokenizer_config.json`'s `added_tokens_decoder` and in `tokenizer.json` the copy marks two tokens as special
that the original does not: 50, `<start_function_response>`, and 255999, `<start_of_image>`; the flag governs
whether a decoder that skips special tokens drops them from the text. The copy ships no `added_tokens.json`,
where the original's holds `<end_of_image>` (262145) and `<image_soft_token>` (262144), the three
`added_tokens` fields. The token ids are equal on both sides (`bos_token_id` 2, `eos_token_id` `[1, 50]`,
`pad_token_id` 0, the generation configuration's `[1, 50, 106]`), the version strings are the same 4.57.3 on
both sides, and the 14,071-byte template renders the fixed conversation identically to the pin's 13,792 bytes,
the difference in line endings and trailing whitespace alone. The cluster judged `rope_scaling` under
transformers 4.56.2 and closed it by the default rule.

## For the recipe library

The per-layer entry with selection reads the copy exactly; a weight line would print the two kernels the card
prints (1.40 to 1.45 and 0.85 to 1.29). The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat41/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
