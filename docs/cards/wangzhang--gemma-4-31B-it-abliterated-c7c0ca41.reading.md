# Reading of the Stage 1 and Stage 2 result: wangzhang/gemma-4-31B-it-abliterated against google/gemma-4-31B-it (2026-10-29)

Measured on Nautilus, round 2 piece 1 (job 3763593, 28 minutes, exit 0). Modified revision `d7431183` (2026-08-29),
original pinned at `419b2efe` (2026-04-02, the release commit). The maker's card names the method: Abliterix, a direct
norm-preserving orthogonal projection on the attention Q, K, V and O projections, with the MLP down projection
left alone for this run, a strength searched over 60 trials, and winsorized steering vectors.

## Weights (Stage 2)

The automatic verdict was "recipe violations", nearest recipe single-projection-selected, 95 flags, as scored on the
cluster. On reading, the weights match what the card says, and the flags came from the table not yet having an entry
for this recipe. Re-scored with the per-layer entries, the verdict is still "recipe violations", nearest
`directional-per-layer-selected`, 10 flags: the energy shares of ten query and value edits, 0.9836 to 0.9891 at
relative change 0.011 to 0.014, which is the bfloat16 floor at that edit size (the calibration law gives 0.98 to
0.99). Within each of the 29 layers with more than one edit, the leading directions of the attention output and the
query, key and value edits agree at cosine 0.9996 or better; between layers the median agreement is 0.17.

- 94 of 1,188 tensors changed: 40 attention outputs (layers 18 to 57 of 60), 25 query projections (layers 29 to 53),
  13 key projections (layers 30 to 42) and 16 value projections (layers 39 to 57). No feed-forward matrix changed and
  the vision tower is bit-identical. The largest relative change outside those 94 is exactly 0. That footprint is the
  card's "Q/K/V/O, MLP disabled", with a per-layer selection the card's strength search would produce.
- Each change is one direction. First-value energy share is at least 0.9929 on the attention outputs and 0.9836 on
  the smallest value-projection edits, in the band bfloat16 storage leaves for edits of this size (relative change
  0.011 to 0.091).
- The 54 "unexpected change" flags are the query, key and value edits. The recipe table's projection entries list
  only the residual writers, so a method that also projects the reading side of attention has no entry to match.
- The 40 direction flags on the attention outputs are the other half of the same gap. The leading directions of the
  40 output edits agree with their median only at cosine 0.12 to 0.73: the direction differs by layer. The table's
  single-projection entries ask for one shared direction. The maker's tool computes its steering vector per layer.
- Row norms were restored. The largest relative change in any row norm is 0.0008 across all 94 matrices, where a
  plain projection of this size moves row norms by 0.005 to 0.015 (the calibration run). That is the card's
  "norm-preserving row magnitude restoration", and it is what the scorer's row-norm rule, once it reads the 0.001
  line, will recognise.

## Token and configuration side (Stage 1)

The automatic verdict is "consistent with re-save noted" now that the tool reads the library defaults and the
original repository's later commits; it finds the same two commits named below, `145dc250` and `ba74f5b6`. On first scoring it was
"unexplained differences" in two fields, and the reading stands.

- `template.default`: the chat template is not the pinned original's, it is Google's own later revision of the
  template. The text matches `google/gemma-4-31B-it` at commits `145dc250` (2026-04-28, "update SI and tool call
  handling") and `ba74f5b6` (2026-05-07) exactly. The maker re-exported the copy after Google's fix landed; the
  weights still equal the April original tensor for tensor, so the pin on the weights holds. The fixed conversation
  renders identically with both templates.
- `config.text_config.moe_intermediate_size`: absent in every Google revision, present and null in the copy. The
  copy was saved with transformers 5.6.2 (the original with 5.5.0.dev0), and that library writes the field with a
  null value for this architecture. It is a re-save addition, not a configuration change, and the tool now classes
  it as explained by re-save.

## For the recipe library

Consistent with the stated change on both sides. The recipe table now has both things it needed to score it: the attention
query, key and value projections as optional kinds, and a per-layer-direction form of the projection envelope.
What remains is the rounding floor on the ten smallest edits, which a measured per-layer line on this base would
carry as its calibrated energy limit. The modified revision is five months newer than the repo's
first upload; the card says the weights were replaced by a later trial, and the comparison above is of that later
revision.

Weight differences alone cannot certify the absence of hidden behavior.

## Second pass (2026-10-30)

Measured again on Nautilus, round 3 piece 1 (card 5055, download job 4080809, compare job 4080810, exit 0), on the
same pins (modified `d7431183`, original `419b2efe`) and the same shard checksums, with the comparison as of commit
d0f48bb. The second-pass report is `results/weights/wangzhang-gemma-4-31B-it-abliterated.pass-2.json`; its leading
vectors are in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus3/measurements/pair-1/weights.directions.safetensors`.

Scored with today's table it reads as before: recipe violations, nearest `directional-per-layer-selected`, the same
10 energy-share flags on the same ten query and value edits, 94 changed tensors, 0 outside them. Every measure both
passes report is equal to the last digit: relative change, difference norms, energy shares, row norms, the
within-layer direction cosines (median 0.99999, minimum 0.9996) and the between-layer agreement (0.17). One number
moved: the cross-layer direction cosine of the two key projections in layers 35 and 41 reads 0.022 where the first
pass read 0.715. Those two form a group of two, and the comparison now reports the angle between the pair
(2 × 0.715² − 1 = 0.022) where the older kit reported each vector's angle from their mean. Same measurement, one
convention.

The new measure reads the weight of each projection off the weights. Along the leading output direction of each
attention output the copy keeps −1.75 to −2.78 of the original's action: −1.75 at layer 18, falling smoothly to
−2.78 at layers 37 and 38, back to −1.77 at layer 57. A projection of weight a leaves 1 − a, so the weight on the
attention outputs is 2.75 to 3.78, in a smooth arc over the layers. Along the second to eighth directions the copy
keeps 0.91 to 1.05 (median 0.99), so each edit is one direction. On the reading side the clean fraction is along the
input direction: query 0.19 at layer 29, −4.61 at layer 41, −0.02 at layer 53 (weights 0.8 to 5.6); key −0.11 at
layer 30, −4.63 at layer 36, −0.34 at layer 42 (weights 1.1 to 5.6); value 0.17 at layer 39, −0.42 at layer 48,
0.15 at layer 57 (weights 0.8 to 1.4). The sides agree with the roles: on all 40 output edits the left fraction is
below the right one, the order a rank-one edit on the output side produces, and on all 54 query, key and value
edits the right fraction is below the left one. The row-norm rule read 0.0008 on these matrices in the first pass;
the norm restoration removes the trace a weight of 3 leaves in the row norms, and the remaining fraction is the
only reading of that weight the weights give. The card names a strength searched over 60 trials and gives no value.

On the token side the cluster's card reads "unexplained differences" on `config.text_config.moe_intermediate_size`
and `template.default`, the two fields the first pass closed. Both closed at home for the same reason as before,
and the cluster could not apply either rule: the compare job runs without network access, so the original
repository's later commits (the template rule) are out of its reach, and its pinned transformers 4.56.2 has no
Gemma 4 configuration class, so the library-default rule has nothing to ask. Re-judged at home under transformers
5.6.2 with the original repository's history, the same report reads "consistent with re-save noted" on the same
commits, `145dc250` and `ba74f5b6`; that re-judged report is
`results/meta/wangzhang-gemma-4-31B-it-abliterated.pass-2.json`, with the cluster's reading kept in its
`reclassification` block.
