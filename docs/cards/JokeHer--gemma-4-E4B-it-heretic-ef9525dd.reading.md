# Reading of the Stage 1 and Stage 2 result: JokeHer/gemma-4-E4B-it-heretic against google/gemma-4-E4B-it (2026-11-02)

Measured on Wheat, round 33 piece 4 (download job 387105, compare job 387109, sweep 387114; the pull of 11-02
01:02Z carries the measurements and the sweep record and no job log). Modified revision `50f546e0` (4 commits on
2026-06-08 from 13:06Z to 13:08Z: the model as one `model.safetensors`, the tokenizer, the README), original pinned
at `fee6332c` (06-03). The card is Heretic's generated page (28,219 bytes) for the arbitrary-rank branch: Heretic
v1.2.0 with the Arbitrary-Rank Ablation, start layer 19, end layer 39, preserve-good-behaviour weight 0.6945,
steer-bad-behaviour weight 0.0014, overcorrect relative weight 1.0377, neighbour count 12, KL divergence 0.5806,
refusals 2 of 100 against 99 of 100. The field `base_model` names google/gemma-4-E4B, the pretrained base. No
`reproduce/` folder.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 80 flags (40 first
shares, 40 within-layer direction cosines), on the cluster and after re-scoring at home. On reading, the copy is
the strongest arbitrary-rank edit in the census, on both writers of the declared window, with one matrix rewritten
to its own size.

- 40 of 2,076 matched tensors changed: the attention outputs and the down projections of layers 19 to 38, the
  card's start 19 and end 39 read as a half-open range. Nothing else moved; the largest relative change outside
  the changed set is exactly 0. The 54 original-only names are the shared-KV key norms.
- Input side on 39 of 40: the right kept fraction is the negative one, -0.33 to -3.81 on the attention outputs
  (weights 1.33 to 4.81) and -2.44 to -29.09 on the down projections (3.4 to 30.1), the left 0.17 to 0.77 and
  -4.29 to 0.63. The arbitrary-rank solver's over-reflection of the input side read on llmfan46's and coder3101's
  copies (finding 22, weights to 10.18) and on mewse's (finding 57); this copy's weights run three times higher.
- Layer 37's down projection changed by 1.008 of its own norm (first share 0.650, kept -4.29 and -29.09) and its
  norm moved from 93.619 to 93.614, the rows by 0.0063: a matrix rewritten to its own size, with its row norms
  put back. Read from the hub by byte range (`tools/hub_range_read.py`), its cosine with the original is 0.492.
- Layer 20's down projection is a residue: relative change 0.0017, first share 0.006, kept 1.00 on both sides,
  rows 0.0008; the solver's weight on that layer was near zero, as finding 22 reads on coder3101's 31B.
- Rows moved 0.0057 to 0.0078 on the other 39, the band finding 22 reads where coder3101's cards claim row-norm
  preservation (0.0059 to 0.0080); this card makes no claim.
- No shared direction: within-layer cosines 0.002 to 0.16, group medians 0.21 and 0.23, 0.00 across the kinds.
  Each matrix has its own direction, which is what a per-layer solve with twelve neighbours produces.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Rows |
| --- | --- | --- | --- | --- |
| 19 | 0.074, 0.962, 0.59, -2.19 | 0.232, 0.950, -0.58, -10.45 | 0.0073, 0.0064 |
| 20 | 0.074, 0.969, 0.57, -2.71 | 0.0017, 0.006, 1.00, 1.00 | 0.0074, 0.0008 |
| 24 | 0.085, 0.983, -0.25, -1.81 | 0.255, 0.956, -1.52, -14.72 | 0.0075, 0.0064 |
| 27 | 0.070, 0.978, 0.56, -2.35 | 0.302, 0.943, -1.29, -16.47 | 0.0075, 0.0062 |
| 31 | 0.126, 0.969, 0.17, -1.80 | 0.201, 0.952, -0.15, -6.46 | 0.0073, 0.0057 |
| 33 | 0.120, 0.938, 0.69, -2.78 | 0.063, 0.973, 0.52, -3.40 | 0.0073, 0.0069 |
| 36 | 0.036, 0.960, 0.77, -0.33 | 0.124, 0.965, 0.27, -3.94 | 0.0076, 0.0066 |
| 37 | 0.063, 0.972, 0.42, -1.51 | 1.008, 0.650, -4.29, -29.09 | 0.0075, 0.0063 |
| 38 | 0.077, 0.951, 0.32, -1.50 | 0.129, 0.894, 0.46, -6.38 | 0.0077, 0.0076 |

The copy is one 15,992,595,884-byte file under the checksum `8aae54bb`, its own; it equals no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster (one field) and "consistent with re-save noted" at home:
`text_config.moe_intermediate_size` closes by the default rule, and the two version strings are all that differ.
The template is a 17,695-byte file the tool reads as equivalent, and the fixed conversation renders identically.

## For the recipe library

The per-layer entry reads the window and flags every matrix twice, because the entry expects one direction per
layer shared by the two writers and the solver gives each writer its own. An arbitrary-rank entry (finding 22) that
expects unrelated directions, the input side and a weight band would count this copy's 39 projections and its one
residue, and would still flag layer 37, where the change equals the matrix (finding 68). The direction vectors stay
in the pull copy at `/opt/ai/hpc-packages/pulls/model-audit/wheat33/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
