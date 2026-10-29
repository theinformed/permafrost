# Reading of the Stage 1 and Stage 2 result: wangzhang/gemma-4-31B-it-abliterated against google/gemma-4-31B-it (2026-10-29)

Measured on Nautilus, round 2 piece 1 (job 3763593, 28 minutes, exit 0). Modified revision `d7431183` (2026-08-29),
original pinned at `419b2efe` (2026-04-02, the release commit). The maker's card names the method: Abliterix, a direct
norm-preserving orthogonal projection on the attention Q, K, V and O projections, with the MLP down projection
left alone for this run, a strength searched over 60 trials, and winsorized steering vectors.

## Weights (Stage 2)

The automatic verdict is "recipe violations", nearest recipe single-projection-selected, 95 flags. On reading, the
weights match what the card says, and the flags come from the table not yet having an entry for this recipe.

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

The automatic verdict is "unexplained differences": one field, the template, once the re-save rule for added fields
took the configuration field. On reading, both are explained.

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

Consistent with the stated change on both sides. The recipe table needs two things to score it formally: an entry
whose changed kinds include the attention query, key and value projections, and a per-layer-direction form of the
projection envelope. Both are filed as scorer follow-ups. The modified revision is five months newer than the repo's
first upload; the card says the weights were replaced by a later trial, and the comparison above is of that later
revision.

Weight differences alone cannot certify the absence of hidden behavior.
