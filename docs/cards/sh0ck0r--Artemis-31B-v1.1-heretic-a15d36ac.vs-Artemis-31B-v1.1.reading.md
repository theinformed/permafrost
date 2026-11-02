# Reading of the Stage 1 and Stage 2 result, second measurement: sh0ck0r/Artemis-31B-v1.1-heretic against TheDrummer/Artemis-31B-v1.1 (2026-11-02)

Measured on Wheat, round 35 piece 2 (download job 387143, compare job 387145, sweep 387152; the pull carries the
measurements and the sweep record and no job log). Modified revision `b3bdce6a` (twelve commits on 2026-08-29
between 03:41Z and 03:52Z), the same thirteen shards round 20 measured against google/gemma-4-31B-it, the
grandparent the `base_model` field names (finding 45). This pass pins the parent the README's first sentence names,
TheDrummer/Artemis-31B-v1.1 at `d613e5a4` (08-06), the revision current when the copy was created; the parent is
a fine-tune of Google's 31B trained in 4-bit and merged, which round 20 read from the hub by byte range. The card is
the full Heretic 1.4.0 record: `direction_index` 45.88, the attention outputs at 1.20 centred on 58.68 falling to
0.28 at distance 34.46, the down projections at 1.48 centred on 35.77 falling to 0.86 at distance 19.15, row
normalisation "full" with a rank-three correction, KL 0.0109, 23 refusals in 100, and a `reproduce/` folder. This
is the reading of record for the copy; the round 20 report (`results/weights/sh0ck0r-Artemis-31B-v1.1-heretic.json`)
stays as the record of what the field's pin measures.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 45 flags (all first
shares, 0.922 to 0.990 on the attention outputs and the down projections of 17 to 24), on the cluster and after
re-scoring at home. On reading, the copy is the clean Heretic 1.4.0 edit its card describes, and nothing else.

- 73 of 1,188 tensors changed: the attention outputs of layers 25 to 59 (35) and the down projections of 17 to
  54 (38). The attention kernel reaches 58.68 plus or minus 34.46, layers 25 to 59; the down kernel 35.77 plus or
  minus 19.15, layers 17 to 54. Both windows read exactly. The largest relative change outside the changed set is
  exactly 0: the 602 matrices the first pass read at 8.75 to 10.45 percent now read 0 on 529 of them, because the
  parent's 4-bit round trip is on both sides of the comparison.
- One direction: the 73 leading vectors stand at 0.977 to 0.999 to their group references and the two writers of
  a layer agree at 0.991 to 0.999 (cross-kind 0.957). First shares 0.985 to 0.995 on the down projections and
  0.922 to 0.991 on the attention outputs, rising with the weight. Output side on 69 of 73; the down projections
  of layers 28 to 31 read the right kept fraction below the left.
- The down kernel reads to the second decimal on its far side and under its height on the near side. One minus
  the left kept fraction runs 1.23, 1.21, 1.17, 1.14, 1.11, 1.07, 1.04, 1.01, 0.97, 0.94, 0.88 and 0.87 on layers
  43 to 54 against a kernel of 1.25, 1.21, 1.18, 1.15, 1.12, 1.08, 1.05, 1.02, 0.99, 0.95, 0.92 and 0.89 (within
  0.04 on every layer); on 17 to 41 it runs 0.57 to 1.29 against 0.87 to 1.47, under by 0.08 to 0.62, most at
  the peak (0.64 at layer 29 against 1.26). The attention kernel reads within 0.10 on 18 of its 35 layers (1.09
  at 59 against 1.19, 0.98 at 51 against 0.99) and under by 0.11 to 0.32 on the other 17.
- Rows moved 0.0010 to 0.0073 on all 73 under the card's "full" row normalisation with a rank-three correction,
  the band finding 22 reads on Heretic exports with and without the claim.

| Layer | Attention output: change, E1, left kept, read, kernel | Down projection: change, E1, left kept, read, kernel | Rows |
| --- | --- | --- | --- |
| 17 | - | 0.0119, 0.985, 0.23, 0.77, 0.87 | -, 0.0017 |
| 21 | - | 0.0138, 0.988, 0.26, 0.74, 1.00 | -, 0.0025 |
| 25 | 0.0043, 0.922, 0.77, 0.23, 0.30 | 0.0158, 0.991, 0.20, 0.80, 1.13 | 0.0010, 0.0027 |
| 29 | 0.0058, 0.950, 0.76, 0.24, 0.41 | 0.0182, 0.993, 0.36, 0.64, 1.26 | 0.0014, 0.0025 |
| 33 | 0.0076, 0.968, 0.62, 0.38, 0.51 | 0.0201, 0.994, -0.23, 1.23, 1.39 | 0.0020, 0.0023 |
| 36 | 0.0089, 0.974, 0.52, 0.48, 0.59 | 0.0211, 0.995, -0.21, 1.21, 1.47 | 0.0018, 0.0031 |
| 40 | 0.0101, 0.979, 0.49, 0.51, 0.70 | 0.0195, 0.994, -0.19, 1.19, 1.34 | 0.0018, 0.0026 |
| 44 | 0.0110, 0.983, 0.35, 0.65, 0.81 | 0.0170, 0.992, -0.21, 1.21, 1.21 | 0.0020, 0.0021 |
| 48 | 0.0123, 0.986, 0.09, 0.91, 0.91 | 0.0147, 0.990, -0.07, 1.07, 1.08 | 0.0018, 0.0018 |
| 51 | 0.0136, 0.988, 0.02, 0.98, 0.99 | 0.0135, 0.988, 0.03, 0.97, 0.99 | 0.0022, 0.0018 |
| 54 | 0.0146, 0.990, -0.03, 1.03, 1.08 | 0.0122, 0.985, 0.13, 0.87, 0.89 | 0.0023, 0.0022 |
| 57 | 0.0157, 0.991, -0.12, 1.12, 1.16 | - | 0.0038, - |
| 59 | 0.0157, 0.991, -0.09, 1.09, 1.19 | - | 0.0026, - |

The read is one minus the left kept fraction; the kernel is the card's weight at that layer.

Against round 20. The field's pin read 603 tensors changed at 8.75 to 10.45 percent (every matrix in the model),
686 flags, first shares 0.002 to 0.047, and the Heretic direction above the parent's noise on the down
projections of 17 to 54 and the attention outputs of 33 to 59; this pin reads 73 tensors, 45 flags, first shares
0.92 to 0.995 and the direction on every changed matrix. The saved leading left vectors of the two passes agree at
0.85 or better on 64 of the 73 matrices (median 0.998) and the right vectors at a median of 0.994: where the first
pass read the Heretic direction through the round trip, it read the same direction this pass reads against the
parent, and the nine disagreements are the attention outputs of layers 25 to 32 and 50, where the first pass had read
the parent's noise (group cosine 0.34 to 0.60 then). The kept fractions agree to the second decimal where the first
pass read them above the floor: layer 54's down projection at 0.13 in both, layer 59's attention output at -0.08
then and -0.09 now, layer 40's down at -0.18 in both. The bias the first reading named, every kept fraction pulled
towards 1 by the parent's noise, is gone; the under-reading on the down kernel's near side is the edit's own and
stands in both passes (-0.19 against -0.47 at layer 36 in round 20, -0.21 against -0.47 now).

The copy's thirteen shards share no checksum with Google's 31B or with any measured copy, as round 20 found; the
parent's shards were on the cluster for this compare only and were deleted by the sweep.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, one field after the home judgement. `text_config.per_layer_config`
is the 5.16 save form (finding 39), the same ten-layer map round 20 read; `text_config.moe_intermediate_size` closed at
home by the default rule (it had closed the same way in round 20 against Google). The two version strings
(5.5.0.dev0 to 5.16.1) are explained as a re-save. The template is the parent's 18,683-byte file, equal to Google's,
and the fixed conversation renders identically. TheDrummer's token files are Google's, so the token side reads the
same against either pin.

## For the recipe library

The copy against its parent is the entry the single-projection recipe nearly fits: one direction, two linear
kernels whose windows read to the layer and whose heights read to the second decimal on the far side of the peak.
The first measurement is kept as the record of what a `base_model` field one step above the parent produces; the
pinner now records a `card_parent` from the README's first sentence (`docs/weights-method.md`), which is how this
pair was pinned. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat35/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
