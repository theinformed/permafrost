# Reading of the Stage 1 and Stage 2 result: TrevorJS/gemma-4-31B-it-uncensored against google/gemma-4-31B-it (2026-10-31)

Measured on Blueback, round 12 piece 3 (push card 5366, round card 5367, download job 3399779, compare jobs 3399780 to
3399785, all exit 0, sweep 3399786; pulled home by card 5448). Modified revision `fd8c03dd` (2026-06-13, a link fix in
the card; the repository was created on 2026-04-04 and the weights were uploaded on 2026-04-05), original pinned at
`419b2efe` (2026-04-02, the release commit). The maker's card names the method and its settings: norm-preserving
biprojected abliteration with one direction per layer, applied to the attention output and the down projection in
all layers (100 percent) at scale 1.0, activations winsorized at the 99.5th percentile, the edit made through
adapters and merged before saving; it reports 1 effective refusal in 100 (5 flagged, 4 of them answers after a
disclaimer), 22 refusals in 686 prompts across four other sets, and a KL divergence of 0.124.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer`, 54 flags, on the cluster and
after re-scoring at home: 52 energy shares at the storage floor and the two matrices of one layer under the direction
line. On reading, the footprint matches the card.

- 120 of 1,188 tensors changed: the attention output and the down projection in each of the 60 layers, the card's
  100 percent. Nothing else moved; the largest relative change outside the changed set is exactly 0, and the query,
  key, value, gate and up projections and the vision tower are unchanged.
- One direction per layer: within a layer the two edits agree at cosine 0.925 to 0.999 (median 0.995); 59 of the 60
  layers clear the 0.95 line, 40 of them above 0.99, and layer 12 sits at 0.925 (its two matrices are the two
  direction flags). Between layers the median directions agree at 0.044.
- Row norms moved by 0.00006 to 0.00037 relative, the same restoration as the maker's E4B and 12B copies (0.0001 to
  0.0004).
- Relative change 0.0135 to 0.0253, first-value energy share 0.975 to 0.995. The leftover beyond the first direction
  is 0.0012 to 0.0032 of the weight norm; 119 of the 120 matrices sit inside the calibrated 0.0025 line, and the one
  outside is layer 2's attention output (0.0032, with 0.016 of its energy in the second direction, where the
  biprojection's input-side term shows). The 52 energy flags are shares of 0.975 to 0.990 on changes of 0.0135 to
  0.025, the floor at this edit size.
- Along each matrix's leading output direction the copy keeps −0.00 to 0.71 of the original's action on the
  attention outputs (median 0.11) and −0.10 to 0.55 on the down projections (median 0.03); the left fraction is below
  the right on 118 of 120: scale 1.0 with the biprojection's second term, as on the maker's three smaller copies.
  Along the second to eighth directions the copy keeps 0.98 to 1.13 (medians 1.00).
- Against the four other copies of this base (wangzhang in round 2, pieces 1, 2 and 4 of this round), which stand on
  the same original weight file (shards `eeef8791` and `01891222`), no changed matrix has an equal measurement in
  any field.

Across the maker's four copies the method reads the same and the settings differ once: the E4B copy (round 8) edits
all 42 layers, the 12B copy (round 8) layers 15 to 47 of 48 (the card's 70 percent), the 26B-A4B copy (rounds 2 and 3)
all 30 layers with the packed experts, and this one all 60. Row norms stay within 0.0004 on every dense matrix of the
four. The within-layer direction dips in the same part of the model each time: layer 12 here at 0.925, layers 10 and
12 on the 26B copy at 0.941 and 0.947 before the experts' direction joined, three layers at 0.934 to 0.947 on E4B,
and none below 0.970 on 12B, where the first 15 layers were not edited.

## Token and configuration side (Stage 1)

The tool's Stage 1 assessment is "consistent" on the cluster and at home: no compared field differs. The copy carries
the release template byte for byte, its configuration equals the original's in every field, and both were saved under
transformers 5.5.0.dev0. It is the first Gemma 4 copy in the census whose cluster card needed no home judgement.

## For the recipe library

Consistent with the stated change on both sides. The maker's fourth norm-preserving per-layer copy and the first
on the 31B base; with pieces 1 and 4 of round 2 and the E4B and 12B copies of round 8 the sixth with row norms held
within 0.0011. The biprojection's second term puts one matrix in 120 past the 0.0025 leftover line, a number a
norm-preserving entry should carry as its own band. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback12/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
