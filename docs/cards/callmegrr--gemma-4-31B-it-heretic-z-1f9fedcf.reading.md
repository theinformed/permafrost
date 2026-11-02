# Reading of the Stage 1 and Stage 2 result: callmegrr/gemma-4-31B-it-heretic-z against google/gemma-4-31B-it (2026-11-02)

Measured on Wheat, round 33 piece 1 (download job 387105, compare job 387106, sweep 387114; the pull of 11-02
01:02Z carries the measurements and the sweep record and no job log). Modified revision `19abfc1e` (74 commits:
created 2026-08-07 at 21:26Z, the model's last upload on 08-08 at 18:48Z, with a `reproduce/` folder of the tool's
configuration, its SHA256SUMS and the evaluation prompts), original pinned at `842da379`
(07-20). The card is Heretic's generated page (29,074 bytes) over Google's: Heretic v1.4.0, direction index "per
layer", attention output kernel 1.26 at position 41.65 falling to 0.19 at distance 4.97, down projection kernel
1.37 at 40.81 falling to 1.29 at 1.06, KL divergence 0.0106, refusals 93 of 100 against 99 of 100. The field
`base_model` names google/gemma-4-31B, the pretrained base; the first sentence names the instruct model, and the
pinner paired by the sentence. The second 31B copy on Wheat and the first unmeasured 31B Heretic export.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 8 flags (first
shares 0.914 to 0.989 on eight matrices), on the cluster and after re-scoring at home. On reading, the copy is the
narrowest Heretic edit of a 31B in the census, and its two kernels read back to the layer.

- 12 of 1,188 tensors changed: the attention outputs of layers 37 to 46 and the down projections of 40 and 41 of
  60. The attention kernel reaches 41.65 plus or minus 4.97, layers 37 to 46; the down kernel 40.81 plus or minus
  1.06, layers 40 and 41. Nothing else moved; the largest relative change outside the changed set is exactly 0.
- One direction per layer, as the card says, shared by the two writers where both write (within-layer cosines
  0.995 and 0.997 on layers 40 and 41) and loosely across layers (group medians 0.82 and 0.83, 0.27 across the
  two kinds). First shares 0.914 to 0.994.
- Output side, the left kept fraction below the right on 12 of 12. The weights read off the left: the attention
  outputs 0.19, 0.41, 0.62, 0.69, 1.10, 1.16, 0.95, 0.61, 0.44 and 0.31 on layers 37 to 46 against the kernel's
  0.26, 0.47, 0.69, 0.90, 1.12, 1.18, 0.97, 0.75, 0.54 and 0.32; the down projections 1.25 and 1.34 against
  1.31 and 1.36. The shape and the heights both read, within 0.21 on every layer and within 0.05 on seven.
- Rows moved 0.0010 to 0.0038, the band Heretic's public row normalisation leaves (finding 22); the card claims
  no restoration.

| Layer | Attention output: change, E1, left kept, weight, kernel | Down projection: change, E1, left kept, weight, kernel | Rows |
| --- | --- | --- | --- | --- |
| 37 | 0.0037, 0.914, 0.81, 0.19, 0.26 | | 0.0012 |
| 39 | 0.0108, 0.983, 0.38, 0.62, 0.69 | | 0.0033 |
| 41 | 0.0154, 0.991, -0.10, 1.10, 1.12 | 0.0194, 0.994, -0.34, 1.34, 1.36 | 0.0027, 0.0027 |
| 42 | 0.0159, 0.991, -0.16, 1.16, 1.18 | | 0.0020 |
| 44 | 0.0104, 0.981, 0.39, 0.61, 0.75 | | 0.0016 |
| 46 | 0.0047, 0.925, 0.69, 0.31, 0.32 | | 0.0010 |

The copy's two shards: the first (`07728539`) is its own; the second (`2bdb2df0`, layers 48 to 59 and the vision
tower in the library's two-shard layout) equals the second shard of Sabomako's and llmfan46's 31B exports, since
none of the three touched a tensor in it (finding 71). The first shards differ and no measured field equals
either copy's.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster (one field) and "consistent with re-save noted" at home:
`text_config.moe_intermediate_size` closes by the default rule, and the two version strings are all that differ.
The template is the pin's 18,683-byte file and the fixed conversation renders identically.

## For the recipe library

The per-layer entry reads the window and the side and flags eight first shares of 0.914 to 0.989 on a copy whose
kernels read back within 0.21; the card's record is enough to predict all twelve matrices and their heights
(finding 59). The `base_model` field is the tool's, copied from Google's own header, and names the pretrained base
on six of this round's eight copies (finding 67). The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat33/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
