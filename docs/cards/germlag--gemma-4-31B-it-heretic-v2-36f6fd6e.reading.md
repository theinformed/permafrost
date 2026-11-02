# Reading of the Stage 1 and Stage 2 result: germlag/gemma-4-31B-it-heretic-v2 against google/gemma-4-31B-it (2026-11-02)

Measured on Nautilus, round 40 piece 1 (download job 4169647, compare job 4169648, sweep 4169656; the pull carries
the measurements and the sweep record and no job log). Modified revision `4261acd0` (one commit, 2026-04-05
17:59Z, titled "Duplicate from coder3101/gemma-4-31B-it-heretic-v2"; the parent repository answers "not found"
on the hub, so this duplicate is the one measurement of it), original pinned at `419b2efe`, the release revision.
The card is coder3101's: Heretic 1.2.0 with magnitude-preserving orthogonalisation, a direction index per layer,
two kernels (`attn.o_proj` with a maximum weight of 1.47 at position 57.33 and a minimum of 1.33 at a distance of
29.21; `mlp.down_proj` with 1.32 at 49.63 and 1.23 at 23.83), a KL divergence of 0.3801 and 37 refusals in 100
against 99 in 100. The batch note says the copy's weight files differ from coder3101's first 31B export (round
12). The copy drops the `.linear.` segment from 189 names the original
carries, mapped before the comparison.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 2 flags (the within-layer cosine
of layer 59 at 0.925), on the cluster and after re-scoring at home. On reading, the copy is one direction per
layer projected from both writers on the output side across the card's two windows, at weights that rise with
the layer to the card's two maxima.

- 65 of 1,188 tensors changed: the down projections of layers 26 to 59 (34) and the attention outputs of 29 to
  59 (31). Nothing else moved; the largest relative change outside the changed set is exactly 0 on all 1,123
  other tensors. The card's kernels place their maxima at 49.63 and 57.33 and their minima 23.83 and 29.21
  layers before, which is layers 26 and 28 (finding 43's reading of a window from the kernel), and the windows
  open at 26 and 29.
- Rank one on every matrix: first shares 0.993 to 0.996. One direction per layer, the two writers of a layer at
  0.925 to 1.000 to each other and the layers at 0.25 (median) to one another.
- Output side on all 65: one minus the left kept fraction is 0.16 at layer 26 rising to 1.31 at 49 on the down
  projections and 0.21 at layer 29 rising to 1.46 at 57 on the attention outputs, the two maxima within 0.01 of
  the card's 1.32 and 1.47 and at the layers the card prints; the right side keeps 0.00 to 0.77. Rows moved
  0.0016 to 0.0079 on 64 matrices and 0.047 on the last down projection, under a card naming magnitude
  preservation. Relative changes 0.0181 to 0.0265.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 26 | - | - | 0.0213, 0.995, 0.79, 0.22 | 0.21 | -, 0.0027 |
| 29 | 0.0222, 0.994, 0.79, 0.39 | 0.21 | 0.0222, 0.994, 0.78, 0.18 | 0.22 | 0.0066, 0.0063 |
| 33 | 0.0251, 0.995, 0.25, 0.42 | 0.75 | 0.0218, 0.995, 0.09, 0.29 | 0.91 | 0.0059, 0.0055 |
| 37 | 0.0195, 0.994, -0.06, 0.39 | 1.06 | 0.0194, 0.994, -0.08, 0.26 | 1.08 | 0.0043, 0.0033 |
| 41 | 0.0192, 0.994, -0.37, 0.32 | 1.37 | 0.0185, 0.993, -0.27, 0.10 | 1.27 | 0.0029, 0.0026 |
| 45 | 0.0194, 0.993, -0.16, 0.59 | 1.16 | 0.0182, 0.993, -0.29, 0.02 | 1.29 | 0.0028, 0.0017 |
| 49 | 0.0217, 0.995, -0.00, 0.37 | 1.00 | 0.0186, 0.993, -0.31, 0.11 | 1.31 | 0.0037, 0.0025 |
| 53 | 0.0199, 0.994, -0.43, 0.21 | 1.43 | 0.0188, 0.993, -0.29, 0.11 | 1.29 | 0.0031, 0.0024 |
| 57 | 0.0211, 0.994, -0.46, 0.72 | 1.46 | 0.0192, 0.994, -0.25, 0.06 | 1.25 | 0.0030, 0.0019 |
| 59 | 0.0234, 0.995, -0.11, 0.29 | 1.11 | 0.0224, 0.995, -0.07, 0.66 | 1.07 | 0.0065, 0.0474 |

The full table (34 rows) is in the report.

Directions. Against twenty-six saved vectors of other measurements of the 31B, the directions stand at 1.000 on
both sides to 3MPER0RR's export on all 41 shared names (minimum 0.9999), at 1.000 to Vampelium's copy of this
round on all 47 shared (left minimum 0.983, at layer 34 where Vampelium's change is 0.0014), at 1.000 to
callmegrr's heretic-z on 12 (minima 0.997 and 0.999), at 0.985 and 0.994 to ressl's (65), at 0.948 and 0.962 to
TrevorJS's (65), at 0.92 to Sabomako's (8), 0.86 to nguyenthilaitrieulong's and 0.84 to wangzhang's, and at 0.51
or less to the rest: 0.14 to coder3101's first export (30 shared), 0.21 to MoonRide's arbitrary-rank searches,
0.25 to huihui-ai's, 0.23 to Jim-darby's and 0.014 to cosmicoptima's. Four makers' per-layer passes at 1.000 with
four windows and four kernels; by byte range the four copies differ from Google and from each other on every
edited tensor read (the layer 41 attention output 0.0094 to 0.0192 from Google and 0.0017 to 0.0100 apart; the
layer 41 down projection 0.0005 to 0.0035 apart; the layer 50 down projection 0.0010 to 0.0017 apart, callmegrr's
byte-equal to Google there, outside its window), and the layer 10 query projection is byte-equal to Google's on
this copy and Vampelium's. The two shards (`20e9835e`, `af865e9a`) match no measured file; the first is the size
of coder3101's first export's first shard and not its bytes.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home: the home judgement closed
`text_config.moe_intermediate_size` by the default rule under transformers 5.22.1, leaving the version strings
(5.5.0.dev0 to 5.5.0). The tokenizer, the token ids (`eos_token_id` `[1, 106]`, generation `[1, 106, 50]`), the
generation settings and the 12,045-byte template are the release revision's.

## For the recipe library

The per-layer entry with selection reads the copy on 63 of its 65 matrices; a weight line would print the two
kernels rising to 1.31 and 1.46 at the card's layers. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus40/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
