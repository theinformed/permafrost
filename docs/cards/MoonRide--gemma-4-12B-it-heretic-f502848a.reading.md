# Reading of the Stage 1 and Stage 2 result: MoonRide/gemma-4-12B-it-heretic against google/gemma-4-12B-it (2026-11-01)

Measured on Nautilus, round 20 piece 5 (download job 4143641, compare job 4143646, 639 seconds, sweep 4143650).
Modified revision `0a9f7d52` (twelve commits on 2026-06-04 between 11:39Z and 12:11Z: the weights at 11:40Z, the
tokenizer, the README, a `reproduce/` folder with the tool's configuration and trial record, and two README
edits after), original pinned at `66bc78a7` (06-04), the revision current when the repository was created. The
card prints the Heretic 1.3.0 record: direction index 29.60, the attention outputs at weight 1.35 centred on layer
31.80 (minimum 0.88, width 15.78), the down projections at 1.39 centred on 42.25 (minimum 1.16, width 15.71), a
KL divergence of 0.0353 and 27 refusals in 100 against the original. The `base_model` field names Google.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 7 flags, on the
cluster and after re-scoring at home: four first shares of 0.978 to 0.990, two cosines of 0.899 and 0.906 to the
group direction on layers 20 and 44, and one cross-kind direction at 0.627. On reading, the footprint is the
card's two kernels to the layer and the direction is one shared direction; the kept fraction reads neither the
kernel's strengths nor a side.

- 52 of 677 tensors changed: the attention outputs of layers 17 to 47 (31 matrices) and the down projections of
  layers 27 to 47 (21). The attention kernel centred on 31.80 with width 15.78 reaches 16.02 to 47.58, the down
  kernel centred on 42.25 with width 15.71 reaches 26.54 to 57.96 of a 48-layer model: layers 17 to 47 and 27 to
  47 exactly. Nothing else moved; the largest relative change outside the changed set is exactly 0 and 625
  tensors equal the original.
- Each change is rank one (first share 0.978 to 0.997, the fourth cumulative share within 0.0005 of the first)
  along one direction shared by both writers and all layers: the leading directions agree with the group
  reference at 0.90 to 0.999 and within a layer at 0.78 to 1.000 (0.78 on layer 47, 0.91 on 44, above 0.93
  elsewhere). The single direction of the card's `direction_index`.
- The kept fractions along that direction carry no weight and no side. On the attention outputs the left kept
  fraction runs from -0.26 (layer 29) to 0.97 (layer 20) with no trend across the kernel, and the right from 0.22
  to 0.90; the left is below the right on 14 of 31. On the down projections the left runs -0.25 to 0.73 and the
  right 0.02 to 0.42, the left below the right on 11 of 21. The kernel's weights would read as a left or right kept
  fraction of 0.12 at the window edges falling to -0.35 (attention) and -0.16 to -0.39 (down) at the centres;
  nothing of that shape is in either column.
- Rows moved by 0.003 to 0.011, unrestored, on all 52.
- Relative changes of 0.016 to 0.031, the largest on the attention output of layer 32.
- The shards: the copy's first two shards equal 3MPER0RR's and igorls's 12B copies' (the library's sharding of
  the embeddings and the layers none of the three edits touches); no measured field is shared with either.

| Layer | Attention output: change, E1, E4, left kept, right kept | Down projection: change, E1, E4, left kept, right kept | Within-layer cosine | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- |
| 17 | 0.0177, 0.993, 0.994, 0.86, 0.68 | - | - | 0.995/- | 0.0043, - |
| 20 | 0.0276, 0.996, 0.997, 0.97, 0.28 | - | - | 0.899/- | 0.0037, - |
| 23 | 0.0203, 0.994, 0.995, 0.83, 0.52 | - | - | 0.996/- | 0.0046, - |
| 26 | 0.0253, 0.996, 0.997, 0.85, 0.42 | - | - | 0.985/- | 0.0046, - |
| 27 | 0.0234, 0.996, 0.996, 0.33, 0.56 | 0.0240, 0.996, 0.996, 0.29, 0.42 | 0.997 | 0.98/0.98 | 0.0067, 0.0065 |
| 29 | 0.0236, 0.996, 0.996, -0.26, 0.55 | 0.0249, 0.996, 0.997, -0.05, 0.35 | 0.996 | 0.96/0.99 | 0.0079, 0.0089 |
| 32 | 0.0312, 0.997, 0.998, 0.85, 0.22 | 0.0226, 0.995, 0.996, 0.59, 0.21 | 0.968 | 0.97/0.98 | 0.0062, 0.0057 |
| 35 | 0.0229, 0.996, 0.996, 0.69, 0.48 | 0.0213, 0.995, 0.995, -0.03, 0.07 | 0.972 | 1.00/1.00 | 0.0051, 0.0035 |
| 38 | 0.0251, 0.996, 0.997, 0.91, 0.39 | 0.0222, 0.996, 0.996, 0.28, 0.02 | 0.929 | 0.97/1.00 | 0.0065, 0.0030 |
| 41 | 0.0186, 0.993, 0.994, 0.60, 0.53 | 0.0222, 0.995, 0.996, -0.10, 0.08 | 0.986 | 1.00/1.00 | 0.0052, 0.0043 |
| 44 | 0.0220, 0.978, 0.996, 0.90, 0.72 | 0.0225, 0.995, 0.996, 0.04, 0.06 | 0.908 | 0.97/1.00 | 0.0089, 0.0039 |
| 47 | 0.0186, 0.991, 0.994, 0.93, 0.60 | 0.0203, 0.995, 0.995, -0.25, 0.11 | 0.781 | 0.97/0.97 | 0.0049, 0.0030 |

The full table (52 rows) is in the report; the rows shown are every third layer with the window edges.

The fingerprint shares no measured field with the fourteen earlier reports on the 12B original. It is the third
Heretic copy of this base (3MPER0RR in round 18, prithivMLmods's decensored copy in round 19) whose kept fractions
read a shared direction and no weight, where the same tool's copies of Mistral 7B (piece 8) and Ministral (finding
41) read their kernels to the third decimal (finding 46).

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, six fields, and "consistent with re-save noted" at home. The six are the
12B family's: four defaults the 5.13.0 save writes where Google's 5.9.0 file omits them (audio samples per token,
audio hidden size, audio output projection dimensions, vision patch size), which load to the same values under
transformers 5.22.1, and the audio and vision sub-configuration data types, which repeat the top-level declaration
where Google's file left them null (finding 39). The template is Google's pinned file and the fixed conversation
renders identically.

## For the recipe library

The card's windows read to the layer and its direction reads as one; its strengths do not read at all. Finding 46
takes this up: on the 12B base the Heretic kernels of three makers leave kept fractions that scatter between -0.3
and 1.0 with no side, while on Mistral 7B and Ministral 3 8B the same tool's kernels read back within 0.003. The
difference is in the base, not the tool, and the measure needs a term for it before a Heretic entry for Gemma 4
12B can carry a weight. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus20/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
