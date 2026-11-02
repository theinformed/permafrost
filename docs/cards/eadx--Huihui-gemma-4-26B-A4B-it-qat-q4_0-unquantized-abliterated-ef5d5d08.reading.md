# Reading of the Stage 1 and Stage 2 result: eadx/Huihui-gemma-4-26B-A4B-it-qat-q4_0-unquantized-abliterated against google/gemma-4-26B-A4B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Nautilus, round 34 piece 3 (download job 4163806, compare job 4163809, sweep 4163815; the pull of
11-01 21:23Z carries the measurements and the sweep record and no job log). Modified revision `ac56985f`: one
commit, "Duplicate from huihui-ai/Huihui-gemma-4-26B-A4B-it-qat-q4_0-unquantized-abliterated", with eadx and
huihui-ai as its authors, on 2026-06-12 at 05:31Z, the hub's duplicate function (finding 38). The parent
repository returns 404 today, so this copy is the only measurement of huihui-ai's QAT 26B-A4B edit, the second
such case after nguyenthilaitrieulong's duplicate of WWTCyberLab's 31B edit (finding 64) and the third
repository the census reaches through a hub duplicate of a vanished parent (finding 56). Original pinned at
`641f1844` (06-05). The card (2,758 bytes) is huihui-ai's text: the remove-refusals code, "a crude
proof-of-concept", no layer or weight stated. The field `base_model` names the QAT checkpoint.

## Weights (Stage 2)

The tool's assessment was "recipe match", nearest recipe `directional-per-layer-selected`, 0 flags, on the
cluster and after re-scoring at home. On reading, the copy is huihui-ai's shared projection on every layer of
the model at a weight of 3.50, the largest in the census, along the two directions the maker's instruct edit of
this base uses.

- 60 of 1,013 tensors changed: the attention outputs and the shared dense down projections of all 30 layers.
  No expert, router, gate-up, norm or tower tensor moved; the largest relative change outside the changed set is
  exactly 0, which places the copy on the QAT checkpoint (finding 48). The maker's instruct edit of this base
  starts at layer 5 (finding 21); this one starts at layer 0.
- One weight: the left kept fraction is -2.4976 to -2.5027 on all 60 (a weight of 3.50 along the leading output
  direction), output side on 60 of 60, first shares 0.999 to 1.000. Finding 21's three weights were 2.5, 1.5 and
  3.0 and called 3.0 the largest; 3.5 is now the largest.
- Two directions: layers 0 to 11 share one (cosine 0.712 to the group reference), layers 12 and 13 sit between
  (0.81 and 0.92), layers 14 to 29 share the other (1.000). Within a layer the two writers agree at 1.000.
  Against the maker's instruct 26B-A4B edit (blueback12 pair 5) the saved leading left vectors stand at 0.71 on
  layers 5 to 11, 0.80 and 0.91 on 12 and 13 and 0.99 on 14 to 29: the same two directions, found again on the
  QAT checkpoint and applied half a unit stronger.
- Rows moved 0.116 to 0.971 (0.971 on layer 29's down projection), the model's largest changes 0.044 to 0.113
  of a matrix with a largest single difference of 0.149; no restoration is claimed.
- Against xdavxd's edit of the same checkpoint (piece 5) the directions touch at layer 10 (0.78) and fall away in
  both directions; against llmfan46's (piece 1) 0.03 to 0.22.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Cross-layer cosine | Rows |
| --- | --- | --- | --- | --- |
| 0 | 0.0673, 0.9995, -2.501, 0.34 | 0.0671, 0.9995, -2.499, 0.85 | 0.712 | 0.175, 0.219 |
| 2 | 0.0670, 0.9995, -2.500, -0.30 | 0.0581, 0.9994, -2.500, 0.57 | 0.712 | 0.208, 0.578 |
| 4 | 0.0884, 0.9997, -2.500, -0.36 | 0.0688, 0.9995, -2.500, 0.16 | 0.712 | 0.305, 0.190 |
| 6 | 0.1103, 0.9998, -2.500, -0.45 | 0.0673, 0.9995, -2.500, -0.02 | 0.712 | 0.455, 0.116 |
| 8 | 0.1097, 0.9998, -2.500, -0.61 | 0.0688, 0.9996, -2.500, 0.20 | 0.712 | 0.180, 0.147 |
| 10 | 0.1119, 0.9998, -2.500, -0.56 | 0.0678, 0.9995, -2.500, 0.51 | 0.712 | 0.148, 0.335 |
| 11 | 0.0912, 0.9997, -2.500, -0.15 | 0.0630, 0.9995, -2.500, 0.34 | 0.712 | 0.169, 0.264 |
| 12 | 0.0969, 0.9998, -2.500, -0.63 | 0.0656, 0.9995, -2.500, 0.41 | 0.808 | 0.132, 0.384 |
| 13 | 0.0852, 0.9997, -2.500, -0.38 | 0.0621, 0.9994, -2.500, 0.42 | 0.922 | 0.138, 0.429 |
| 14 | 0.0809, 0.9997, -2.499, -0.30 | 0.0610, 0.9994, -2.500, 0.46 | 1.000 | 0.212, 0.596 |
| 16 | 0.0775, 0.9996, -2.500, 0.33 | 0.0549, 0.9992, -2.499, 0.55 | 1.000 | 0.252, 0.355 |
| 18 | 0.0734, 0.9995, -2.500, -0.05 | 0.0519, 0.9991, -2.500, 0.55 | 1.000 | 0.222, 0.470 |
| 20 | 0.0681, 0.9995, -2.500, -0.19 | 0.0505, 0.9991, -2.500, 0.42 | 1.000 | 0.171, 0.488 |
| 22 | 0.0659, 0.9994, -2.500, -0.25 | 0.0481, 0.9990, -2.499, 0.41 | 1.000 | 0.231, 0.550 |
| 24 | 0.0688, 0.9995, -2.500, 0.04 | 0.0481, 0.9990, -2.499, 0.50 | 1.000 | 0.229, 0.589 |
| 26 | 0.0649, 0.9994, -2.500, -0.22 | 0.0445, 0.9989, -2.503, 0.67 | 1.000 | 0.197, 0.645 |
| 28 | 0.0557, 0.9992, -2.500, -0.13 | 0.0476, 0.9990, -2.501, 0.74 | 1.000 | 0.272, 0.668 |
| 29 | 0.0576, 0.9993, -2.499, 0.06 | 0.0497, 0.9991, -2.500, 0.75 | 1.000 | 0.349, 0.971 |

The copy's two shards are `937574eb` and `fa22da96`; the parent's listing is gone and no measured file is equal.

## Token and configuration side (Stage 1)

"Consistent" on the cluster and at home: nothing differs, both files saved by 5.6.2. The template is the pin's
16,934-byte file and the fixed conversations render identically.

## For the recipe library

The per-layer entry matches, and its match hides the one fact that matters here, the weight: a shared projection
at 3.50 on every writer of every layer is the strongest edit in the library, half a unit above the maker's own
instruct edit. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus34/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
