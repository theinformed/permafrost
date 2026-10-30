# Reading of the Stage 1 and Stage 2 result: richardyoung/Mistral-7B-Instruct-v0.2-abliterated-obliteratus against mistralai/Mistral-7B-Instruct-v0.2 (2026-10-30)

Measured on Blueback, round 7 piece 7 (round card 5291, compare jobs 3392878 to 3392885, 4 to 6 minutes each, exit 0;
pulled home by card 5302). Modified revision `9c17c8bd` (2026-09-26, a README commit; the weights were uploaded on
2026-03-28), original pinned at `63a8b081` (2025-07-24). The maker's card names OBLITERATUS's "advanced" method and
reports 85 refusals in 100 at a KL divergence of 0.4224. The tool's own description of that preset: four directions
from an SVD, norm-preserving, bias projection, two refinement passes, layer-adaptive strength; its source lists the
query, key, value and output projections, the gate, up and down projections and the output head as targets.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 82 flags, on the cluster
and after re-scoring at home: 46 unexpected changes, 18 energy shares, 17 direction cosines and one cross-kind
direction. On reading, the footprint matches the tool's description, and no entry in the table describes it.

- 64 of 291 tensors changed: all seven projections in each of layers 22 and 24 to 31 (63 matrices) and the output
  head (0.032 of its norm). Layer 23 and layers 0 to 21 are untouched, and so is the token embedding; the largest
  relative change outside the changed set is exactly 0.
- Every change is rank four. The singular values come in a group of four near-equal values and then drop 25 to 40
  times (the layer 22 attention output: 1, 0.988, 0.965, 0.958, 0.038, 0.029 relative to the first). The first four
  directions carry 0.90 to 0.99 of each change's energy (0.98 in the middle). The first alone carries 0.24 to 0.38,
  which is what the 18 energy flags and the 17 direction flags measure.
- Relative change is 0.017 to 0.025 in every kind (0.021 in the middle). Along the leading input direction the copy
  keeps 0.30 to 0.36 of the original's action in all 63 layer matrices, the same fraction on readers and writers.
- Row norms moved by 0.002 to 0.042 on the layer matrices and by 0.105 on the output head. The preset's norm
  preservation does not show in the stored weights.
- Directions are not shared across layers: 0.12 to 0.56 with the median for the reading-side kinds, 0.06 to 0.96 for
  the down projections.

## Token and configuration side (Stage 1)

The tool's Stage 1 assessment is "unexplained differences" in four fields, before and after the home re-judgment, the same
four as piece 5 from the same maker.

- `pad_token` added as `</s>` (id 2) in both token files where the original declares none; the generation settings
  carry no pad. A real change, harmless for single-prompt use.
- `config.dtype` for `config.torch_dtype`, both bfloat16: the copy's library (4.57.6) against the original's 4.36.0.
  Re-save.
- The chat template moved to `chat_template.jinja` and renders identically; the tool explains it.

## For the recipe library

Consistent with the tool's description, which the card names. This is the first measured rank-k edit: a fixed small
rank (four) on every projection of a chosen layer range plus the output head, with a clean gap in the spectrum after
the fourth value. A "rank-k projection" entry would take the rank from the spectrum gap and ask the first k shares to
sum near 1, which these do at 0.90 to 0.99. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback7/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
