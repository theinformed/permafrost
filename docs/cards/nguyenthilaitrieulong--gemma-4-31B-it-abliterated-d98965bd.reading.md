# Reading of the Stage 1 and Stage 2 result: nguyenthilaitrieulong/gemma-4-31B-it-abliterated against google/gemma-4-31B-it (2026-11-02)

Measured on Wheat, round 31 batch 3 piece 4 (download job 387097, compare job 387101, sweep 387102; the pull of
11-02 00:22Z carries the measurements and the sweep record and no job log). Modified revision `1b283037` (one
commit, 2026-08-04 at 09:58Z, "Duplicate from WWTCyberLab/gemma-4-31B-it-abliterated", the hub's duplicate
function), original pinned at `842da379` (07-20), the revision current when the copy was made. The README is the
parent's, 6,551 bytes, signed "Produced by WWT Cyber Lab": a "five-surface attack" of a rank-32 adapter on 18
modules of layers 57 to 59 trained on 177 compliance pairs and merged, a "primary direction interpolation" at
layer 59, an "orthogonal residual ablation" of layers 55 to 59 at scale 1.5, 13 "refusal-starting token embeddings
scaled down by 10x", and `bad_words_ids` blocking a disclaimer phrase; a technical summary adds "standard at
L33-52". The parent, WWTCyberLab/gemma-4-31B-it-abliterated, was pinned for Raider in round 17 and never measured,
so this is the only measurement of that edit. The `base_model` field names Google.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 65 flags (47 first
shares, 12 within-layer cosines, 6 unexpected changes), on the cluster and after re-scoring at home. On reading,
four of the card's five surfaces are in the weights as stated and the fifth is in a different window.

- 77 of 1,188 tensors changed: the attention output and the down projection of layers 25 to 27 and 31 to 59 (32
  layers; 28, 29 and 30 untouched), the queries, keys, gates and up projections of layers 57 to 59, and the token
  embedding. Nothing else moved; the largest relative change outside the changed set is exactly 0.
- The adapter: 18 modules of layers 57 to 59, the six linear maps per layer less the value projection, as the
  card's "18 modules" count says (6 by 3). Relative changes 0.011 to 0.031, first shares 0.59 to 0.96, kept
  fractions 0.73 to 1.56, no restoration (rows 0.004 to 0.51).
- The 1.5 pass: the attention outputs and down projections of layers 55 to 59 keep -0.494 to -0.5001 of the
  original's action along their leading output direction, a weight of 1.50 on all ten, with a second direction
  under it (first shares 0.69 to 0.79, second cumulative 0.78 to 0.99), the orthogonal pass the card describes.
- The "standard" ablation reads on layers 25 to 27 and 31 to 54, not the card's 33 to 52: one direction per
  matrix (first shares 0.983 to 0.995), the left kept fraction 0.25 at layer 25 falling to 0.00 at 39 and rising
  to 0.24 at 54 (weights 0.75 to 1.00 on a smooth schedule), the two writers of each layer within 0.01 of each
  other, output side on 32 of 32. Directions change along the stack (0.14 to 1.00 with the group median).
- The embedding: relative change 0.0075, eight singular values of near-equal size (cumulative shares 0.36, 0.45,
  0.53, 0.60, 0.65, 0.71, 0.76, 0.80), a largest row-norm change of 0.9091, the rows left at 0.0909 of their
  length, one eleventh. The card's "10x" is a division by eleven, as the same maker's "strength 5" on the 26B-A4B
  was a division by six (finding 30): the maker scales a row by one over one plus the stated number.
- The byte-range check against huihui-ai's second 31B version, whose weight 1.5 on layers 5 to 59 reads the same
  -0.5 (finding 21): layer 56's attention output differs from huihui-ai's by 0.0306 of its norm and from Google's
  by 0.0237, where huihui-ai's differs from Google's by 0.0193. Two edits at one weight along different
  directions; the copy does not stand on huihui-ai's.

| Layer | Attention output: change, E1, left kept | Down projection: change, E1, left kept | Other modules |
| --- | --- | --- | --- |
| 25 | 0.0145, 0.990, 0.25 | 0.0155, 0.991, 0.25 | |
| 27 | 0.0109, 0.984, 0.23 | 0.0117, 0.986, 0.23 | |
| 31 | 0.0164, 0.992, 0.24 | 0.0150, 0.991, 0.25 | |
| 39 | 0.0176, 0.993, -0.00 | 0.0167, 0.992, -0.00 | |
| 47 | 0.0117, 0.984, 0.17 | 0.0118, 0.984, 0.17 | |
| 54 | 0.0106, 0.981, 0.24 | 0.0111, 0.982, 0.24 | |
| 55 | 0.0234, 0.773, -0.49 | 0.0246, 0.785, -0.50 | |
| 57 | 0.0245, 0.690, -0.50 | 0.0277, 0.710, -0.50 | q 0.020, k 0.021, gate 0.031, up 0.020 |
| 59 | 0.0246, 0.701, -0.50 | 0.0248, 0.686, -0.50 | q 0.017, k 0.011, gate 0.019, up 0.016 |

The full table (77 rows) is in the report. The two shards are the parent's file under the copy's name; neither
equals a measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster (three fields) and at home (two). `text_config.moe_intermediate_size`
closes by the default rule. What stays: `generation.bad_words_ids`, five token sequences the original does not
set, the card's fifth surface, a true change and a disclosed one; and the template, Google's 12,045-byte file of
the 04-10 revision under the 07-20 pin whose template is the 18,683-byte Canonical file, the earlier-revision case
through a re-upload, as akpsahan's copy in round 29. The fixed conversation renders identically.

## For the recipe library

A re-upload read as its parent's edit, the parent unmeasured (finding 9's kind) and the duplicate readable from
the commit title before any download (finding 38); the batch was pinned without the checksum rule. The edit
itself (finding 64) is five methods in one file, four of them read back to the number, and the fifth in a window
the card misstates by six layers at each end. The per-layer entry's 65 flags are the two-direction layers, the
adapter's six modules per layer and the embedding; no entry describes the stack. The direction vectors stay in
the pull copy at `/opt/ai/hpc-packages/pulls/model-audit/wheat31/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
