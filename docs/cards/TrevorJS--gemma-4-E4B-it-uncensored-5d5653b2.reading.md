# Reading of the Stage 1 and Stage 2 result: TrevorJS/gemma-4-E4B-it-uncensored against google/gemma-4-E4B-it (2026-10-30)

Measured on Blueback, round 8 piece 1 (round card 5305, download job 3397500, compare jobs 3397501 to 3397508, all exit
0, sweep 3397509; pulled home by card 5347). Modified revision `6aa4636a` (2026-06-13; the repository was created on
2026-04-03), original pinned at `292a7e27` (2026-04-02). The maker's card names the method and its settings:
norm-preserving biprojected abliteration with one refusal direction per layer, applied to the attention output and
the feed-forward down projection in 100 percent of the layers at scale 1.0, activations winsorised at the 99.5th
percentile; it reports 0 to 3 refusals in 100 and a KL divergence of 0.068.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer`, 6 flags, on the cluster and
after re-scoring at home with the saved direction vectors (the kit carried today's table, so no count moved). All 6
flags are within-layer direction cosines in three layers. On reading, the footprint matches the card.

- 84 of 2,130 tensors changed: the attention output and the down projection in every one of the 42 layers. Nothing
  else moved; the largest relative change outside the changed set is exactly 0, the per-layer embeddings and the
  audio and vision towers included.
- One direction per layer. Within a layer the two edits agree at cosine 0.934 to 0.998 (median 0.986); between
  layers the median directions agree at 0.022. Layers 5, 30 and 33 sit at 0.944, 0.947 and 0.934, under the entry's
  0.95 line, and both matrices of each are the six flags. The same maker's 26B-A4B copy in round 2 read 0.94 to 0.99
  within layers.
- Row norms moved by 0.0001 to 0.0003 relative (largest 0.00034), under the 0.0011 the two norm-preserving copies of
  round 2 held and the tightest restoration measured so far.
- Relative change 0.018 to 0.029, first-value energy share 0.991 to 0.996, leftover 0.0014 to 0.0019 of the weight
  norm, inside the calibrated floor.
- Along each matrix's leading output direction the copy keeps 0.03 to 0.77 of the original's action on the attention
  outputs (median 0.16) and 0.01 to 0.54 on the down projections (median 0.06); the left fraction is below the right
  on 82 of 84 matrices. That is the card's scale 1.0 with the biprojection's second term added, the pattern the round
  2 copy showed (0.02 to 0.28 and 0.00 to 0.51).
- Against the three other E4B copies of this round and the three measured in rounds 2 and 7, which all stand on the
  same original weight file (shard `cfbd3d2f`), no changed matrix has an equal measurement in any field. The copy is
  its own edit.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" in one field. Re-judged at home it reads "consistent with re-save
noted", and that is the card committed here.

- `config.text_config.moe_intermediate_size`: absent in the original, present and null in the copy, which the library
  in the pins (5.6.2) loads as its default. Saved with transformers 5.5.0 against the original's 5.5.0.dev0.
- The chat template equals the pinned release template byte for byte (11,926 bytes, `292a7e27`). The pin rule took
  the revision at the repository's creation in April, and the template agrees with it although the weights were
  uploaded in June.

## For the recipe library

Consistent with the stated change on both sides. The per-layer entry's 0.95 within-layer line catches three layers
of a method that computes its direction once per layer and projects it out of two matrices with a second,
input-side term, which separates the two leading directions by a few degrees. The saved direction vectors are not
committed (`*.safetensors` is ignored); the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback8/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
