# Reading of the Stage 1 and Stage 2 result: jwest33/gemma-3-4b-null-space-abliterated-RP-writer against jwest33/gemma-3-4b-it-null-space-abliterated (2026-11-02)

Measured on Wheat, round 47 piece 4 (download job 387398, compare job 387402, sweep 387407; the pull carries the
measurements and the sweep record and no job log). Modified revision `4e2fac1d` (created 2026-01-09 02:30Z, the
folder uploaded at 02:42Z and again at 02:45Z), parent pinned at `3d50eeaa` of 2026-01-06, the maker's own
null-space projection of google/gemma-3-4b-it (first uploaded on 01-04, the weights replaced on 01-06), the
toolkit finding 94 read on the 12B: winsorised activations, null-space constraints at a rank ratio of 0.90, a
Gaussian per-layer weight, a directional multiplier of 1.03 and Frobenius-norm preservation. The census has not
measured the parent against Google. The copy's card is a creative-writing and role-play fine-tune over that edit:
a rank-8 adapter (alpha 8) on all seven projections of the language model, 200 steps of response-only training on
a filtered LimaRP subset through Unsloth, merged. The copy ships the parent's `abliteration_config.json`,
`refusal_directions.pt` and `null_space_projectors.pt` by object id. The pair is a second-generation measurement
against an unmeasured first edit (finding 117), so it reads the training and the edit under it only by byte range.

## Weights (Stage 2)

The tool's assessment was violations against `single-projection`, 302 flags (165 unexpected changes, 68 first
shares, 68 direction cosines, 1 cross-kind cosine), on the cluster and after re-scoring at home. On reading, the
copy is training on every linear map of every layer of the language model, with no direction and the vision tower
untouched, as its card says.

- 233 of 883 tensors changed: the query, value, attention output, gate, up and down projections of all 34 layers
  and the key projections of 29; the other five key projections (layers 1, 2, 3, 5 and 14) moved by 0.0009 to
  0.00099, just under the threshold and the largest relative change outside the changed set. The 437 vision
  tensors, the embedding and the normalisation vectors read exactly 0.
- No direction: first shares 0.17 to 0.86, the top eight components carrying 0.53 to 0.96 of each change, both
  kept fractions near 1 on every matrix (left 0.95 to 1.02, right 0.97 to 1.02).
- Relative changes 0.0010 to 0.0071 (median 0.0026); rows moved 0.0001 to 0.0228.

| Kind | Matrices | Relative change |
| --- | --- | --- |
| Query projection | 34 | 0.0018 to 0.0052 |
| Key projection | 29 | 0.0010 to 0.0025 |
| Value projection | 34 | 0.0011 to 0.0036 |
| Attention output | 34 | 0.0029 to 0.0071 |
| Gate projection | 34 | 0.0018 to 0.0041 |
| Up projection | 34 | 0.0020 to 0.0038 |
| Down projection | 34 | 0.0028 to 0.0064 |

Directions. The census has one other Gemma 3 4B measurement, DavidAU's fine-tune over the maker's own Extreme (round
42), and the two trainings' vectors stand at 0.079, nothing to share. Against the parent's published
`refusal_directions.pt` (the mean of the directions of layers 8 to 24), the training's leading vectors stand at
0.083 or less on every matrix (median 0.009 to 0.017 by kind, the level of a random direction in 2,560
dimensions), and by byte range at layer 20 the training puts 0.00017 to 0.00036 of its change along the mean
direction on the attention output, the down and the query projections, under the 0.00039 a random direction would
take. The edit under it, read by byte range against google/gemma-3-4b-it at `093f9f38`: the layer 20 attention
output, down and query projections stand 0.0160, 0.0156 and 0.0152 from Google's, each difference rank one (first
shares 0.992, 0.991 and 0.990) along one direction that stands at 0.782 to the published mean direction, and the token
embedding stands 0.0220 from Google's along the mean direction itself (1.000, first share 0.995); the layer 5 gate
projection stands 0.0022 from Google's (0.83), the Gaussian weight's low tail. The training stands 0.0034 to 0.0045
from the parent on the three layer 20 matrices and 0.0022 on the layer 5 gate, with its leading direction at 0.03 or
less to the edit's.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home on two fields, no field closing: the generation file drops
the parent's `cache_implementation: hybrid`, and the template (1,581 bytes against the parent's 1,579) differs
beyond line endings and renders the fixed conversation identically. The configuration, the index, the processor
files and the special-token map are the parent's by object id, the `tokenizer.json` a re-save. The token ids are
the instruct checkpoint's through the parent (`eos_token_id` `[1, 106]`, generation `[1, 106]`, `bos_token_id` 2,
`pad_token_id` 0) and the vocabulary is 262,208.

## For the recipe library

No entry reads training; a training entry would read the copy as its card says. The pinner should queue the
parent against google/gemma-3-4b-it, which would read the null-space edit on all 34 layers and the embedding as
finding 94 read it on the 12B. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat47/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
