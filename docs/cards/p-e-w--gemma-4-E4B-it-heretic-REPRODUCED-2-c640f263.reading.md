# Reading of the Stage 1 and Stage 2 result: p-e-w/gemma-4-E4B-it-heretic-REPRODUCED-2 against google/gemma-4-E4B-it (2026-11-02)

Measured on Wheat, round 39 piece 3 (download job 387181, compare job 387184, sweep 387190; the pull carries the
measurements and the sweep record and no job log). Modified revision `74bb1abd` (five commits in one minute at
07:32Z on 2026-06-11), original pinned at `fee6332c`. The repository is the third of three the tool's author
uploaded in twenty-two minutes that morning: p-e-w/gemma-4-E4B-it-heretic at 07:10Z (eleven commits, with a
`reproduce/` folder: the configuration, the selected trial, the system and a `SHA256SUMS` of its four shards),
p-e-w/gemma-4-E4B-it-heretic-REPRODUCED at 07:22Z and this one at 07:32Z, each a fresh repository with the same
card. The card is Heretic's table: direction index 31.26, `attn.o_proj` kernel maximum 0.81 at 26.47 and minimum
0.44 at a distance of 15.86, `mlp.down_proj` maximum 1.47 at 27.73 and minimum 0.55 at 23.71, KL divergence 0.0072,
42 refusals in 100; the `base_model` field names google/gemma-4-E4B, the pretrained checkpoint, as the first
export's does (finding 67), and the pinner paired it by the card's first sentence. The reproduce record of the
first export names the pinned revision `fee6332c` as the base, Heretic 1.3.0 installed from a local directory
("Reproducibility cannot be guaranteed in this environment"), trial 88 of 200, seed 2684903619, `row_normalization`
"full" with a rank-3 correction, and one RTX PRO 4500 Blackwell.

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 37 flags (32 first shares, 4 direction
cosines, 1 cross-kind), on the cluster and after re-scoring at home: the count and the causes of the first export
(round 33). On reading, the copy is the first export measured again.

- 68 of 2,076 tensors changed: the attention outputs of layers 11 to 41 (31) and the down projections of 5 to 41
  (37), the card's two windows to the layer. The 54 shared-key-value tensors are absent from the save. Nothing
  else moved; the largest relative change outside the changed set is exactly 0 on all 2,008 other tensors.
- One direction per kind and nearly one for the model: first shares 0.969 to 0.998, the down projections at 0.991
  to their mean direction (minimum 0.963), the attention outputs at 0.974 (minimum 0.897), the two kinds at 0.848;
  the two writers of a layer agree at 0.88 to 0.998 (median 0.976).
- Output side with the kernels' shape: on the down projections one minus the left kept fraction runs 0.47 at layer
  5, 1.34 at 26 and 0.86 at 41, under a card maximum of 1.47 at 27.73; on the attention outputs 0.17 at 11, 0.73 at
  26 and 0.41 at 41, under a maximum of 0.81 at 26.47. The right side keeps 0.63 to 0.03 to 0.37 on the down
  projections and 0.80 to 0.64 to 0.85 on the attention outputs. Rows moved 0.0027 to 0.0086 under the "full"
  normalisation with a rank-3 correction. Relative changes 0.0081 to 0.0321.
- Equal to the first export, not byte for byte: every per-tensor relative difference and first share agrees with
  the round 33 report of p-e-w/gemma-4-E4B-it-heretic to four to six digits (largest spread 0.00011) and to the
  last digit on none. By byte range from the hub, the three exports stand at the same distance from Google's
  (0.01551 on the layer 26 attention output, 0.02845 on the layer 26 down projection, 0.00885 on the layer 11
  attention output); the first export and REPRODUCED are byte-equal on all three, and REPRODUCED-2 stands
  0.00012, 0.00016 and 0.00009 from them. Its first and fourth shards (`aa3e9d1e`, `8080cb1a`) equal the first
  export's, the E4B layout shared with sh0ck0r's, BinxNet's and TheUmbraWalker's exports and, for the fourth, with
  igorls's and prithivMLmods's QAT exports (finding 71); its second and third
  (`ad521587`, `62d196fb`) differ from the first export's (`78c1ee08`, `2dda6bb6`), which is where the 68 edited
  tensors live.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 5 | - | - | 0.0116, 0.984, 0.53, 0.63 | 0.47 | 0.0042 |
| 11 | 0.0089, 0.974, 0.83, 0.80 | 0.17 | 0.0162, 0.991, 0.30, 0.38 | 0.70 | 0.0027, 0.0042 |
| 16 | 0.0114, 0.983, 0.57, 0.81 | 0.43 | 0.0206, 0.994, 0.06, 0.40 | 0.94 | 0.0041, 0.0054 |
| 21 | 0.0132, 0.987, 0.68, 0.80 | 0.32 | 0.0237, 0.996, 0.09, 0.21 | 0.91 | 0.0062, 0.0044 |
| 26 | 0.0155, 0.990, 0.27, 0.76 | 0.73 | 0.0285, 0.997, -0.34, 0.05 | 1.34 | 0.0050, 0.0043 |
| 31 | 0.0144, 0.989, 0.80, 0.73 | 0.20 | 0.0279, 0.997, -0.27, -0.00 | 1.27 | 0.0073, 0.0047 |
| 36 | 0.0125, 0.986, 0.72, 0.79 | 0.28 | 0.0219, 0.995, 0.25, 0.23 | 0.75 | 0.0041, 0.0075 |
| 41 | 0.0081, 0.969, 0.59, 0.85 | 0.41 | 0.0183, 0.993, 0.14, 0.37 | 0.86 | 0.0033, 0.0051 |

The full table (68 rows) is in the report.

Directions. Against thirty-nine saved vectors of measurements of the E4B, the directions stand at 1.000 on both
sides to the first export on all 68 shared names (minimum 1.000 on both), at 0.96 to sh0ck0r's E4B export (60
shared), 0.94 to BinxNet's (47), 0.82 to prithivMLmods's kernel export of the QAT checkpoint (54), 0.31 to
treadon's, 0.30 to Madras1's, and 0.24 or less to every other E4B edit (TheUmbraWalker's, TrevorJS's and its
re-upload, jokernifty's, Bahushruth's, NullpoLab's three, MoonRide's, coder3101's, llmfan46's). Two runs of one
method by two makers stand at 0.96; the author's own reproduction stands at 1.000, the number the census has read
only on re-uploads and on copies of a run (findings 85 and 95).

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home. The home judgement closed
`text_config.moe_intermediate_size` by the default rule under transformers 5.22.1; what remains is the version
strings of the configuration and the generation configuration (5.5.0.dev0 to 5.11.0), a re-save. The template, the
tokenizer and the token ids are the pin's.

## For the recipe library

A one-direction kernel entry with the first share floor at 0.96 would read the copy clean with both kernels. The
direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat39/measurements/pair-3/weights.directions.safetensors`; the first
export's are under `wheat33/measurements/pair-2/`.

Weight differences alone cannot certify the absence of hidden behavior.
