# Reading of the Stage 1 and Stage 2 result: Umranz/diffusiongemma-26B-A4B-it-abliteration against google/diffusiongemma-26B-A4B-it (2026-11-02)

Measured on Nautilus, round 34 piece 8 (download job 4163806, compare job 4163814, sweep 4163815; the pull of
11-01 21:23Z carries the measurements and the sweep record and no job log). Modified revision `082d18f9` (3
commits inside five minutes on 2026-07-05 from 03:10Z: "Upload Trial 144 abliterated merged model", "Add model
card and ARA training details"), original pinned at `156b5c86`, the diffusion variant of the 26B-A4B mixture
(finding 40), the third copy of it in the census after edwixx's and Goodoldjam's. The card (1,974 bytes) is the
maker's own text over Heretic's arbitrary-rank parameters: trial 144 of a 150-trial Optuna search, target layers 1
to 20, `attn.o_proj` and `mlp.down_proj`, preserve 0.8357, steer 0.0359, overcorrect 0.0418, 11 neighbours,
refusals 98 to 4 of 100, KL divergence 0.1106, and a reason for the window: ablating the deepest layers of a
block-diffusion mixture "causes significant catastrophic degradation", so the ablation is "strictly capped at
layer 20". The usage block names the repository `Umranz/diffusiongemma-26B-A4B-it-ara`, a name the hub does not
serve. The field `base_model` names the diffusion model.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 76 flags, on the
cluster and after re-scoring at home: the first shares of all 38 matrices (0.02 to 0.97) and the within-layer
cosines of all 19 layers counted on both writers. On reading, the copy is an arbitrary-rank edit of both writers
of layers 1 to 19, of which 15 matrices are residues of the solver and 23 are edits, at weights near one, with the
rows put back under no claim.

- 38 of 1,047 tensors changed, under the `model.decoder.` prefix (finding 40): the attention outputs and down
  projections of layers 1 to 19 of 30, the card's "1 to 20". No expert, router, gate-up, norm or tower tensor
  moved; the largest relative change outside the changed set is exactly 0.
- Fifteen of the 38 are residues: both writers of layers 1 and 3 to 8 and layer 2's down projection changed by
  0.0012 to 0.0045 of their norm with no leading direction (first shares 0.02 to 0.87) and both sides kept at
  0.98 to 1.01, finding 22's rewritten-and-restored matrices. The 23 edits are the attention outputs of layers 2
  and 9 to 19 and the down projections of 9 to 19, changed by 0.008 to 0.047; layer 18's down projection is the
  largest (0.047, right kept -0.42, a weight of 1.42, largest single difference 0.33).
- Input side on the attention edits: the right keeps -0.20 to +0.13 (weights 0.87 to 1.20) with the left at 0.82
  to 0.99. The down projections of 9 to 11 keep 0.09 to 0.40 on the right (0.60 to 0.91); those of 12 to 17 and
  19 keep 0.74 to 0.96 on both sides and read no side, the solver's small changes without a direction (finding 58).
- Each matrix its own direction: within-layer cosines 0.001 to 0.115; across layers 0.001 to 0.48 to the group reference.
- Rows moved 0.0043 to 0.0079 on 37 of 38 and 0.0006 on layer 3's down projection: finding 22's preservation band
  under a card that claims no preservation, as JokeHer's E4B export of round 33 (finding 68).
- Against Goodoldjam's arbitrary-rank edit of the same base (round 30, wheat30 pair 6) the saved leading left
  vectors stand at 0.91 to 0.99 on the attention outputs of layers 7, 8, 9, 12, 14, 15 and 16 and at 0.86 to 0.99
  on the down projections of 7, 8, 13, 15 and 16, and at 0.13 or less on the other eight shared matrices (median
  0.90): two searches on the diffusion base agree on most of the layers both reach. Against edwixx's the cosines
  are 0.39 or less.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Within-layer cosine | Rows |
| --- | --- | --- | --- | --- |
| 1 | 0.0016, 0.42, 0.45, 1.00, 1.01 | 0.0027, 0.57, 0.64, 0.99, 0.99 | 0.001 | 0.0074, 0.0061 |
| 2 | 0.0403, 0.34, 0.88, 0.69, -0.02 | 0.0016, 0.14, 0.18, 1.00, 0.99 | 0.036 | 0.0075, 0.0052 |
| 3 | 0.0036, 0.63, 0.73, 0.99, 0.91 | 0.0012, 0.02, 0.10, 1.00, 1.00 | 0.009 | 0.0076, 0.0006 |
| 4 | 0.0030, 0.61, 0.68, 1.00, 0.95 | 0.0025, 0.62, 0.65, 0.98, 0.90 | 0.036 | 0.0074, 0.0053 |
| 5 | 0.0022, 0.39, 0.40, 1.00, 0.98 | 0.0045, 0.87, 0.89, 1.00, 0.84 | 0.033 | 0.0060, 0.0075 |
| 6 | 0.0032, 0.70, 0.74, 0.99, 0.97 | 0.0038, 0.81, 0.82, 0.99, 1.00 | 0.066 | 0.0076, 0.0076 |
| 7 | 0.0031, 0.67, 0.70, 0.99, 0.97 | 0.0033, 0.72, 0.75, 0.99, 0.94 | 0.006 | 0.0078, 0.0070 |
| 8 | 0.0036, 0.77, 0.81, 0.99, 0.93 | 0.0040, 0.77, 0.80, 0.98, 0.99 | 0.015 | 0.0043, 0.0060 |
| 9 | 0.0241, 0.47, 0.91, 0.90, 0.02 | 0.0186, 0.52, 0.97, 0.93, 0.30 | 0.009 | 0.0076, 0.0074 |
| 10 | 0.0426, 0.22, 0.79, 0.96, -0.20 | 0.0302, 0.43, 0.91, 0.91, 0.09 | 0.039 | 0.0076, 0.0071 |
| 11 | 0.0135, 0.61, 0.93, 0.96, -0.08 | 0.0244, 0.73, 0.96, 0.77, 0.40 | 0.020 | 0.0062, 0.0076 |
| 12 | 0.0158, 0.84, 0.95, 0.87, -0.09 | 0.0109, 0.63, 0.92, 0.93, 0.93 | 0.013 | 0.0078, 0.0068 |
| 13 | 0.0162, 0.84, 0.93, 0.95, -0.14 | 0.0083, 0.92, 0.93, 0.95, 0.94 | 0.115 | 0.0078, 0.0067 |
| 14 | 0.0266, 0.35, 0.90, 0.86, -0.01 | 0.0111, 0.81, 0.93, 0.92, 0.93 | 0.104 | 0.0079, 0.0071 |
| 15 | 0.0236, 0.47, 0.89, 0.94, -0.06 | 0.0106, 0.95, 0.96, 0.96, 0.91 | 0.047 | 0.0074, 0.0066 |
| 16 | 0.0260, 0.38, 0.89, 0.88, -0.01 | 0.0109, 0.95, 0.96, 0.91, 0.89 | 0.068 | 0.0076, 0.0072 |
| 17 | 0.0125, 0.83, 0.92, 0.99, -0.17 | 0.0139, 0.94, 0.96, 0.86, 0.74 | 0.008 | 0.0067, 0.0075 |
| 18 | 0.0155, 0.81, 0.94, 0.88, 0.13 | 0.0471, 0.52, 0.96, 0.94, -0.42 | 0.029 | 0.0077, 0.0069 |
| 19 | 0.0359, 0.28, 0.87, 0.82, -0.14 | 0.0145, 0.94, 0.97, 0.93, 0.74 | 0.021 | 0.0077, 0.0073 |

The copy's eleven shards: the first seven are its own; shards 8 to 11 (`aca5d3bd`, `8e241886`, `93d564b7`,
`afec0471`) equal the original's and Goodoldjam's, the layers above the window and the towers in the library's
layout for this model (finding 71). No measured file is equal on every shard.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home: `generation_config.return_dict_in_generate` is added (null
to true) beside the version strings (5.8.0.dev0 to 5.14.0.dev0). The template is the pin's 17,336-byte file and
the fixed conversations render identically.

## For the recipe library

An arbitrary-rank entry (finding 22) would count 23 projections and 15 residues; the per-layer entry counts every
matrix twice, for its first share and for not sharing a direction with the other writer. The direction vectors
stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus34/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
