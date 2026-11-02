# Reading of the Stage 1 and Stage 2 result: coder3101/gemma-4-31B-it-qat-q4_0-unquantized-heretic against google/gemma-4-31B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Nautilus, round 36 piece 2 (download job 4167620, compare job 4167622, sweep 4167629; the pull carries
the measurements and the sweep record and no job log). Modified revision `150747c1` (six commits on 2026-06-06:
the model, tokenizer and README at 15:58Z, a README edit at 15:59Z, a `preprocessor_config.json` at 16:48Z; the
maker's 26B QAT export followed at 18:23Z), original pinned at `4f926903` (06-05, the release commit of the
QAT-unquantized 31B checkpoint). The card (29,510 bytes, the tool's page) says Heretic v1.2.0's arbitrary-rank
ablation with row-norm preservation: `start_layer_index` 15, `end_layer_index` 39, `preserve_good_behavior_weight`
0.6649, `steer_bad_behavior_weight` 0.0001, `overcorrect_relative_weight` 1.0818, `neighbor_count` 15, no targeted
component printed, KL divergence 0.0564, 11 refusals in 100 against 99. The `base_model` field names the QAT
checkpoint. The maker's eighth copy in the census and the fourth on a QAT checkpoint (the E2B in round 32, the 12B
in round 34, the E4B in round 35).

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 21 flags (all
first shares), on the cluster and after re-scoring at home. On reading, the copy is the card's edit with the
window's residues left where the search gave a layer no weight.

- 21 of 1,188 tensors changed, all attention outputs, inside the card's window of 15 to 38 (the end exclusive).
  Seventeen are edits: layers 16, 22 and 24 to 38, relative changes 0.0106 to 0.0541, first shares 0.887 to
  0.976. Four are residues above the threshold (layers 15, 17, 19, 20: relative change 0.0011 to 0.0016, first
  share 0.003 to 0.027, both kept fractions 1.00, rows 0.0008), and three more sit under it (18, 21, 23 at
  0.00083 to 0.00090), the largest relative change outside the changed set being 0.000898. The shape is finding
  22's: the maker's instruct 31B edit left 23 such residues. No down projection and no tower tensor moved, which
  places the copy on the QAT checkpoint (finding 48).
- Input side on all 17 edits (left kept 0.35 to 0.91, right kept negative on 16). Read as weights, one minus the
  right kept fraction, 1.52 to 3.79 (median 2.04) on 16 of them, 3.79 at layer 30 and 3.53 at 31; layer 16 reads
  0.57 (right kept 0.43), a partial removal at the window's low end.
- Rows moved 0.0068 to 0.0079 on all 17 edits, finding 22's band on every one, under the card's preservation
  claim.
- A direction per matrix: 0.04 to 0.45 to the group reference.

| Layer | Change | E1 | E4 | Left kept | Right kept | Weight read | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | 0.0015 | 0.012 | 0.021 | 1.00 | 1.01 | residue | 0.0008 |
| 16 | 0.0106 | 0.887 | 0.938 | 0.82 | 0.43 | 0.57 | 0.0075 |
| 22 | 0.0271 | 0.976 | 0.982 | 0.77 | -0.95 | 1.95 | 0.0074 |
| 24 | 0.0237 | 0.954 | 0.960 | 0.74 | -0.52 | 1.52 | 0.0077 |
| 27 | 0.0406 | 0.963 | 0.972 | 0.56 | -1.63 | 2.63 | 0.0079 |
| 30 | 0.0520 | 0.968 | 0.977 | 0.68 | -2.79 | 3.79 | 0.0068 |
| 31 | 0.0541 | 0.961 | 0.973 | 0.75 | -2.53 | 3.53 | 0.0079 |
| 38 | 0.0277 | 0.960 | 0.972 | 0.78 | -0.62 | 1.62 | 0.0078 |

The full table (21 rows) is in the report.

Directions. Against the saved vectors of twenty-three 31B measurements on the shared names, the leading
directions stand at 0.993 on the left and 0.984 on the right to llmfan46's edit of the same checkpoint five days
later (piece 1, 14 shared matrices), at 0.956 and 0.943 to the maker's own instruct 31B edit of April (21
shared), at 0.952 and 0.939 to llmfan46's instruct 31B edit (9), at 0.88 and 0.96 to MoonRide's April edit, at
0.83 and 0.43 to wnfldchen's merged export, at 0.76 and 0.68 to Bahushruth's, at 0.41 and 0.70 to OS-Software's
rank-four edit of the same checkpoint (piece 4) and at 0.21 or less to the kernel and projection edits: the 31B
arbitrary-rank family on the QAT checkpoint, the maker's QAT edit on the maker's instruct direction as finding 72
reads (finding 89). The second shard (`fd00e7a5`) is byte-equal to llmfan46's.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.6.2 to 5.10.0.dev0) and
nothing else; the template is the pin's and renders identically.

## For the recipe library

The directional-per-layer entry is the nearest and its 21 flags are the few directions per matrix on 17 and the
residues on 4; an arbitrary-rank entry with the card's window with residues allowed and rows in the band under a claim, would read the copy as a clean match. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus36/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
