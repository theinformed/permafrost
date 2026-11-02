# Reading of the Stage 1 and Stage 2 result: Sabomako/gemma-4-12B-it-heretic against google/gemma-4-12B-it (2026-11-02)

Measured on Wheat, round 41 piece 6 (download job 387195, compare job 387201, sweep 387203; the pull carries the
measurements and the sweep record and no job log). Modified revision `6a54537f` (created 2026-06-18 16:29Z, the
folder uploaded two minutes later, the card created and revised on 06-28, the morning the maker also revised the
31B's card), original pinned at `5926caa4` of 06-04. The card is 674 bytes: "made using Heretic v1.3.0 with
custom ORBA abliteration method", "Refusal classification via an LLM judge (Gemma3-12B-it-Heretic)", a KL
divergence of 0.0545 and 0 refusals in 100 against 98 in 100, no table, no window and no preservation line. It
is the maker's second export in the census after the 31B of finding 65 (round 31).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 29 flags (first shares 0.741 to
0.989 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is one direction
per layer projected on the output side from 31 matrices in three bands, at weights to 6.5 on three down
projections and under 0.4 on most of the rest, with every row restored.

- 31 of 677 tensors changed: both writers of layers 18 to 23, the down projections alone of 24 to 30, and both
  writers of 34 to 39. Nothing else moved; the largest relative change outside the changed set is exactly 0 on
  all 646 other tensors.
- Rank one on every matrix (first shares 0.741 to 0.992, the small changes carrying the larger rounding share)
  and one direction per layer: the two writers of a layer at 0.984 to 1.000, the layers at 0.11 to 0.70 to
  layer 27 on the down projections.
- Output side on all 31: one minus the left kept fraction is 6.29, 6.52 and 6.16 on the down projections of
  layers 21, 22 and 23 (relative changes 0.121 to 0.128, the right side at -2.0 to -2.3 under the same weight),
  0.60 to 1.08 on those of 18 to 20, 0.07 to 0.14 on 24 to 30, and 0.98 at 34 falling to 0.21 at 37 and 0.25 at
  39; 0.06 to 0.39 on the twelve attention outputs. Rows moved 0.00007 to 0.00026 on all 31, the exact
  restoration the maker's 31B carried (finding 65) and TrevorJS's biprojection carries (finding 3). Relative
  changes 0.0011 to 0.128.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 18 | 0.0013, 0.816, 0.93, 0.97 | 0.07 | 0.0101, 0.989, 0.40, 0.67 | 0.60 | 0.00013, 0.00010 |
| 20 | 0.0011, 0.767, 0.94, 0.99 | 0.06 | 0.0192, 0.988, -0.08, 0.38 | 1.08 | 0.00012, 0.00026 |
| 21 | 0.0064, 0.972, 0.63, 0.94 | 0.37 | 0.1209, 0.985, -5.29, -2.33 | 6.29 | 0.00019, 0.00018 |
| 22 | 0.0061, 0.969, 0.64, 0.95 | 0.36 | 0.1284, 0.985, -5.52, -2.12 | 6.52 | 0.00016, 0.00018 |
| 23 | 0.0066, 0.970, 0.61, 0.88 | 0.39 | 0.1268, 0.988, -5.16, -2.05 | 6.16 | 0.00012, 0.00015 |
| 24 | - | - | 0.0024, 0.871, 0.88, 0.94 | 0.12 | -, 0.00008 |
| 27 | - | - | 0.0023, 0.847, 0.89, 0.95 | 0.11 | -, 0.00007 |
| 30 | - | - | 0.0015, 0.763, 0.93, 0.97 | 0.07 | -, 0.00007 |
| 34 | 0.0036, 0.901, 0.78, 0.92 | 0.22 | 0.0171, 0.992, 0.02, 0.26 | 0.98 | 0.00014, 0.00008 |
| 36 | 0.0044, 0.921, 0.74, 0.98 | 0.26 | 0.0083, 0.971, 0.50, 0.62 | 0.50 | 0.00015, 0.00008 |
| 39 | 0.0016, 0.741, 0.92, 0.99 | 0.08 | 0.0045, 0.921, 0.75, 0.83 | 0.25 | 0.00010, 0.00007 |

The full table (19 rows) is in the report.

Directions. Against twenty-eight saved vectors of other measurements of the 12B, the directions stand at 0.986
on the left and 0.989 on the right to TrevorJS's 12B edit and its four re-uploads on all 31 shared names (0.986
on the down projections, minimum 0.977; 0.980 on the attention outputs, minimum 0.952), at 0.61 to Carlosian's
(21), 0.60 to Paul691's duplicate (31), 0.56 to huihui-ai's and its two re-uploads (7), 0.45 to AEON-7's, 0.44
to igorls's, 0.41 to jwest33's null-space projection, 0.24 to 0.27 to the kernel passes (prithivMLmods's,
MoonRide's, 3MPER0RR's, Vampelium's, BinxNet's) and coder3101's, 0.24 to RumiaChannel's Refusals2 and 0.047 to
its Refusals4 of this round, 0.011 to AlekseyCalvin's. The maker's 31B of finding 65 stands at 0.90 to 0.94 to
TrevorJS's 31B on its 8 names and at 0.86 to jcxu97's of this round. By byte range the layer 21 down projection
is 0.1208 from Google's and 0.1025 from TrevorJS's (his 0.0191 from Google's), the layer 21 attention output
0.0064 from Google's and 0.0119 from TrevorJS's, the layer 30 down projection 0.0015 from Google's and 0.0176
from TrevorJS's, and the layer 10 query projection byte-equal on all three: the family's direction at 0.99 under
the maker's own weights, further from TrevorJS's tensors than from Google's on two of three. The one shard
(`981e7d36`) matches no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on four fields, "consistent with re-save noted" at home: the home
judgement closed `audio_config.audio_samples_per_token`, `audio_config.hidden_size`,
`audio_config.output_proj_dims` and `vision_config.model_patch_size`, absent on one side and the same value
under transformers 5.22.1, leaving the version strings (5.10.0.dev0 to 5.12.1) and the sub-configuration data
types the cluster had explained. The tokenizer, the token ids (`eos_token_id` `[1, 106]`, generation
`[1, 106, 50]`), the generation settings and the 17,466-byte template are the pin's.

## For the recipe library

The per-layer entry with selection reads the copy on 2 of 31 matrices under its first-share floor; a floor at
0.74 for a restored projection, and a weight line, would print the three down projections at 6.2 to 6.5 under a
card with no table. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat41/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
