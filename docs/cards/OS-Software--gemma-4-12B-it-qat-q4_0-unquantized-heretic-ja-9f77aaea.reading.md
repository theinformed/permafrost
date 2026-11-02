# Reading of the Stage 1 and Stage 2 result: OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-heretic-ja against google/gemma-4-12B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Nautilus, round 36 piece 8 (download job 4167620, compare job 4167628, sweep 4167629; the pull carries
the measurements and the sweep record and no job log). Modified revision `b23c6b1c` (ten commits: the model,
tokenizer, processor and README on 2026-06-25 between 01:11Z and 01:14Z, four README edits to 02:05Z, one more
on 08-02), original pinned at `58540658` (06-05, the release commit of the QAT-unquantized 12B checkpoint). The
card (31,715 bytes) is Heretic v1's page with `abliteration_method` ARA LoRA: `start_layer_index` 10,
`end_layer_index` 47, `preserve_good_behavior_weight` 0.5040, `steer_bad_behavior_weight` 0.0001,
`overcorrect_relative_weight` 0.5472, `neighbor_count` 14, no row-normalisation line, KL divergence 0.0319, 3
refusals in 100 against 97, measured on the maker's Japanese prompt sets (`harmless_alpaca_ja`,
`harmful_behaviors_ja`). The `base_model` field names google/gemma-4-12B-it; the README's first sentence names the
QAT checkpoint, and the pinner paired by the name (finding 48). The maker's first Japanese-prompt export, a month
before the `-ja-v2` of round 37 (finding 83).

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 138 flags (66
first shares of 0.657 to 0.990 and 72 within-layer cosines of 0.001 to 0.101), on the cluster and after
re-scoring at home. On reading, the copy is the card's LoRA-adapter arbitrary-rank edit on both writers of the
whole window, at the largest weights and row movements of the maker's exports.

- 73 of 677 tensors changed: the down projections of layers 10 to 46 (37) and the attention outputs of 10 and 12
  to 46 (36), the card's window of 10 to 46 (the end exclusive) on both writers. The attention output of layer 11
  sits under the threshold at 0.000086, the largest relative change outside the changed set and the one residue;
  nothing else moved, which places the copy on the QAT checkpoint (finding 48).
- A few directions per matrix: first shares 0.657 to 0.999, fourth cumulative shares 0.949 to 1.000.
- Input side on all 73 (the left kept fraction above the right on every matrix). Read as weights, one minus the
  right kept fraction, 0.74 to 1.77 on the down projections (median 1.30) and 0.79 to 3.73 on the attention
  outputs (median 1.39), 3.73 at layer 35 and 3.08 at 41 where the relative change is the largest (0.088).
- The two writers of a layer take different directions (within-layer cosines 0.001 to 0.101), as on the maker's
  `-ja-v2`.
- Rows moved 0.0007 to 0.0456 on the down projections (nine in finding 22's band, thirteen under it, fifteen
  over) and 0.0083 to 0.209 on the attention outputs (0.209 at layer 41, 0.105 at 39, 0.087 at 35), under no
  printed claim; the `-ja-v2` card prints row-norm preservation and its rows held at or under the band.

| Layer | Writer | Change | E1 | E4 | Left kept | Right kept | Weight read | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | down | 0.0238 | 0.790 | 0.959 | 1.00 | 0.15 | 0.85 | 0.0023 |
| 10 | attention | 0.0498 | 0.848 | 0.949 | 0.81 | -0.25 | 1.25 | 0.0232 |
| 19 | down | 0.0668 | 0.917 | 0.994 | 0.84 | -0.77 | 1.77 | 0.0456 |
| 19 | attention | 0.0682 | 0.988 | 0.997 | 0.66 | -0.83 | 1.83 | 0.0500 |
| 35 | down | 0.0283 | 0.937 | 0.994 | 0.78 | 0.26 | 0.74 | 0.0043 |
| 35 | attention | 0.0795 | 0.999 | 0.999 | 0.92 | -2.73 | 3.73 | 0.0870 |
| 41 | attention | 0.0879 | 0.997 | 1.000 | 0.81 | -2.08 | 3.08 | 0.2093 |
| 46 | attention | 0.0390 | 0.976 | 0.994 | 0.96 | -0.03 | 1.03 | 0.0094 |

The full table (73 rows) is in the report.

Directions. Against the saved vectors of thirty-five 12B measurements on the shared names, the leading left
vectors stand at 0.64 to RumiaChannel's Refusals2 (40 shared), 0.59 to the maker's own `-ja-v2` (54), 0.58 to
llmfan46's QAT edit, 0.57 to wnfldchen's, 0.54 to llmfan46's instruct edit, 0.54 to coder3101's QAT edit, 0.53 to
RumiaChannel's Refusals9, 0.52 to coder3101's instruct edit (69 shared) and 0.50 to the maker's `-v3`, with the
kernel and projection edits at 0.15 or less; the right vectors stand lower, 0.19 to 0.39 to the same edits. The
first Japanese search's output direction shares half to two thirds of its cosine with the English arbitrary-rank
family's, more than the second search's (0.30 to 0.40, finding 83), and its input direction a fifth to a third
(finding 93). The one shard (`9807fa52`) equals no measured file.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.10.0.dev0 to 5.12.1) and
nothing else; the template is the pin's 17,874-byte file and renders identically.

## For the recipe library

The directional-per-layer entry is the nearest and its 138 flags are the few directions per matrix and the two
writers' different directions; a LoRA-adapter arbitrary-rank entry with the card's window on both writers would
read the copy as a clean match with one residue. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus36/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
