# Reading of the Stage 1 and Stage 2 result: coder3101/gemma-4-12B-it-heretic against google/gemma-4-12B-it (2026-10-31)

Measured on Nautilus, round 18 piece 1 (push card 5473, round card 5477, download job 4125751, compare job 4125752
on the background queue, sweep 4125760; pulled home by card 5493). Modified revision `c664c907` (2026-06-06, a
preprocessor configuration commit; the repository was created on 2026-06-04 at 17:18Z and the weights were uploaded
two minutes later), original pinned at `5926caa4` (2026-06-04, the commit that set `max_position_embeddings` to the
full context length). The maker's card names the method and its parameters: Heretic 1.2.0 with Arbitrary-Rank
Ablation and row-norm preservation, start layer 2, end layer 45, preserve weight 0.3688, steer weight 0.0004,
overcorrect weight 1.0066, neighbour count 15; it reports 7 refusals in 100 against 99 for the original and a KL
divergence of 0.1576. The card lists no targeted component.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 170 flags, on the
cluster and after re-scoring at home: 86 energy shares and 84 within-layer directions. On reading, the footprint is
the arbitrary-rank method on both residual writers of each layer, the first of this maker's four copies to edit the
down projections, with the layers the search weighted near zero left as residues.

- 86 of 677 tensors changed: the attention output and the down projection of every layer from 2 to 44 of 48, the
  card's range with its end index exclusive, as on the maker's E4B, 26B-A4B and 31B copies. Nothing else moved; the
  largest relative change outside the changed set is exactly 0, and 591 tensors are equal to the original.
- 51 of the 86 are edits: 28 attention outputs (layers 3, 15, 18 to 40 and 42 to 44) and 23 down projections (15 to
  24, 26 to 29, 32, 33, 35 to 38, 41, 43 and 44), relative change 0.012 to 0.076, first-value energy share 0.908 to
  0.978, first eight values 0.946 to 0.991. The other 35 are rounding residues: relative change 0.00107 to 0.00184,
  first share 0.002 to 0.188, the original's action kept at 0.99 to 1.00 along every direction. Rewritten layers
  under the threshold are the case of the maker's 31B copy (23 residues in round 12) and llmfan46's 26B-A4B copy
  (round 16), here on 13 of the 43 down projections below layer 15 and on 7 more above.
- The leading direction sits on the input side on all 51 edits: the copy keeps 0.52 to 0.99 of the original's action
  on the left and −2.90 to 0.08 on the right, so the searched weight is 0.92 (layer 15's attention output) to 3.90
  (layer 32's down projection), median 2.2 on the attention outputs and 2.4 on the down projections. The band widens
  past the 0.76 to 1.49 of the 26B-A4B copy and stays inside the 0.51 to 10.18 of the 31B copy.
- The leading directions differ by layer and by writer: cross-layer cosine 0.13 in the middle (0.001 to 0.67), and the
  two edits of a layer agree at 0.0004 to 0.26 on the 42 layers where both carry an edit or a residue (layer 14's two
  residues at 0.99 are the one exception). One direction per matrix, as on every copy of the method.
- Row norms moved by 0.0057 to 0.0079 relative on all 51 edits (median 0.0075), the seven tenths of a percent the
  maker's preservation claim reads on every base (finding 22). Of the 35 residues, 26 keep their rows within 0.0009
  and 9 move them by 0.0047 to 0.0073, so the restoration step ran on layers the ablation barely touched.

| Layer | Attention output: change, E1, right, weight | Down projection: change, E1, right, weight |
| --- | --- | --- |
| 3 | 0.030, 0.949, −0.63, 1.63 | residue |
| 15 | 0.018, 0.908, 0.08, 0.92 | 0.012, 0.962, −0.43, 1.43 |
| 16 | residue | 0.016, 0.958, −0.57, 1.57 |
| 17 | residue | 0.014, 0.958, −0.54, 1.54 |
| 18 | 0.043, 0.927, −1.36, 2.36 | 0.029, 0.923, −0.74, 1.74 |
| 19 | 0.052, 0.937, −1.52, 2.52 | 0.030, 0.936, −0.31, 1.31 |
| 20 | 0.041, 0.945, −1.25, 2.25 | 0.025, 0.959, −0.75, 1.75 |
| 21 | 0.037, 0.959, −1.03, 2.03 | 0.028, 0.970, −0.84, 1.84 |
| 22 | 0.036, 0.958, −1.05, 2.05 | 0.018, 0.971, −0.76, 1.76 |
| 23 | 0.015, 0.934, −0.42, 1.42 | 0.018, 0.963, −0.81, 1.81 |
| 24 | 0.037, 0.943, −0.94, 1.94 | 0.028, 0.971, −1.14, 2.14 |
| 25 | 0.034, 0.938, −0.67, 1.67 | residue |
| 26 | 0.031, 0.946, −0.53, 1.53 | 0.027, 0.958, −1.21, 2.21 |
| 27 | 0.034, 0.965, −1.13, 2.13 | 0.033, 0.920, −1.60, 2.60 |
| 28 | 0.039, 0.952, −0.84, 1.84 | 0.025, 0.965, −1.35, 2.35 |
| 29 | 0.017, 0.917, −0.45, 1.45 | 0.023, 0.963, −1.39, 2.39 |
| 30 | 0.030, 0.958, −0.69, 1.69 | residue |
| 31 | 0.035, 0.960, −0.79, 1.79 | residue |
| 32 | 0.049, 0.962, −0.98, 1.98 | 0.045, 0.961, −2.90, 3.90 |
| 33 | 0.076, 0.961, −1.51, 2.51 | 0.032, 0.937, −1.51, 2.51 |
| 34 | 0.051, 0.939, −1.82, 2.82 | residue |
| 35 | 0.074, 0.932, −1.56, 2.56 | 0.022, 0.966, −1.29, 2.29 |
| 36 | 0.020, 0.965, −0.90, 1.90 | 0.028, 0.959, −1.63, 2.63 |
| 37 | 0.044, 0.937, −1.72, 2.72 | 0.025, 0.965, −1.70, 2.70 |
| 38 | 0.037, 0.975, −1.23, 2.23 | 0.025, 0.949, −1.23, 2.23 |
| 39 | 0.015, 0.937, −0.56, 1.56 | residue |
| 40 | 0.014, 0.978, −0.39, 1.39 | residue |
| 41 | residue | 0.035, 0.937, −2.35, 3.35 |
| 42 | 0.027, 0.965, −1.23, 2.23 | residue |
| 43 | 0.035, 0.963, −1.17, 2.17 | 0.024, 0.965, −1.71, 2.71 |
| 44 | 0.032, 0.942, −1.66, 2.66 | 0.042, 0.935, −2.68, 3.68 |

Layers 2 and 4 to 14 carry two residues each; "right" is the fraction of the original's action kept along the
leading right direction and the weight is one minus it.

Against the five other copies of this base (TrevorJS in round 8, igorls in round 7, richardyoung and lemuralabs in
rounds 8 and 16, 3MPER0RR in this round, the last on the 2026-07-20 revision of the same weight file, shard
`5a84cb31`), no edit has an equal measurement in any field; 10 and 12 of the residues share a largest absolute
difference with the richardyoung and lemuralabs reports, one bfloat16 step coinciding on matrices that barely
moved. Against the maker's three other copies the method is the same (input side, one direction per matrix, 0.007
on the rows) and the component set is wider: the E4B, 26B-A4B and 31B copies edited attention outputs only.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" on seven configuration fields and the home judgement under
transformers 5.6.2 with the original's commit history closes them by hand, so the committed card keeps the tool's
text with this reading beside it.

- Both repositories were saved under transformers 5.10.0.dev0. The copy's `config.json` lacks the four values of
  finding 11 (the audio tower's `audio_samples_per_token`, `hidden_size` and `output_proj_dims`, 640, 640, 640, and
  the vision patch size, 48) and repeats `bfloat16` as `dtype` in the audio, text and vision sub-configurations.
  The four are the class defaults a 5.10 save omits and the loader restores, and the three repeats are the save
  writing the top-level data type into every block; Google's file was written by hand before the 5.10 save form.
  The tool classed one of the three repeats as a re-save effect and left the rest; all seven are one cause.
- The template is Google's pinned one byte for byte (17,466 bytes, `36e3a42e`), the tokenizer, special tokens and
  generation settings are equal, and the fixed conversation renders identically.

## For the recipe library

Consistent with the card on both sides. The arbitrary-rank entry (candidate since round 3) now has nine copies on
five bases, and this one adds the down projections to the component list and a residue count (35 of 86) larger than
the edit count on one writer kind. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/nautilus18/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
