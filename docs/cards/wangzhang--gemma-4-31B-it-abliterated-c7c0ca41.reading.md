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
