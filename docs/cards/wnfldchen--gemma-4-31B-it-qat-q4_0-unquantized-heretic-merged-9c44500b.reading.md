# Reading of the Stage 1 and Stage 2 result: wnfldchen/gemma-4-31B-it-qat-q4_0-unquantized-heretic-merged against google/gemma-4-31B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Wheat, round 37 piece 3 (download job 387161, compare job 387164, sweep 387170; the pull carries the
measurements and the sweep record and no job log). Modified revision `e9a15cd7` (four commits on 2026-08-14: the
repository at 08:28Z, the model files and the card at 08:32Z, a benchmark table at 10:11Z), original pinned at
`1e4d8bee` (04-28), the QAT-unquantized 31B checkpoint, which enters the census with this pair as its fifth QAT
original. The card (4,422 bytes, the maker's own) says the repository is the merged form of the maker's adapter
repository wnfldchen/gemma-4-31B-it-qat-q4_0-unquantized-heretic (adapter commit `8cce1a71`, Heretic commit
`ee47df2f`, "export_strategy=merge"), made with Heretic v1.4.0's arbitrary-rank method "with row-norm
preservation": trial 6, `target_components` `attn.o_proj`, `ara_lora_rank` 256, `start_layer_index` 24,
`end_layer_index` 54, `preserve_good_behavior_weight` 0.1182, `steer_bad_behavior_weight` 0.0050,
`overcorrect_relative_weight` 0.8715, `neighbor_count` 15, keywords 8 of 100 against 99 of 100, KL divergence
0.0900. A `reproduce/` folder carries the configuration, the 1.5 MB trial record, the prompt set and three
reproduction records, and `export-summary.json` records the export as "model_saved_then_execution_cancelled": the
tool wrote the thirteen shards, began a second redundant save that rewrote `config.json`,
`generation_config.json` and the first shard, and was cancelled. The `base_model` field names the QAT checkpoint.
The maker's second copy in the census after the 12B QAT export of round 34 (finding 72); the adapter repository
itself, 120 adapter tensors under a `base_model` prefix, was refused at the pin.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 30 flags (all first
shares, 0.63 to 0.98), on the cluster and after re-scoring at home. On reading, the copy is the card's window on
the attention outputs alone, input side on 27 of 30, at weights that reach 4.5, with one matrix rewritten and no
row restored.

- 30 of 1,188 tensors changed: the attention outputs of layers 24 to 53, the card's start 24 and end 54 with the
  end exclusive and its one target component. No down projection, no other projection and nothing in the vision
  tower moved; the largest relative change outside the changed set is exactly 0 and 1,158 tensors equal the
  original, which places the copy on the QAT checkpoint (finding 48).
- A few directions per matrix: first shares 0.63 to 0.98, the fourth cumulative share 0.83 to 0.999 and the eighth
  0.96 to 1.000; the rank-256 adapter resolved to one to four directions where it merged.
- Input side on 27 of 30 (the left kept fraction above the right). Read as weights, one minus the right kept
  fraction, 0.27 to 4.47 (median 1.54): 4.47 at layer 41, 4.12 at 53, 3.32 at 48, 3.00 at 37, 2.97 at 47. Layers
  38 and 43 keep more than 1 on both sides (right 1.59 and 1.13, left 1.08 and 1.03), the leading component
  amplified rather than removed, as two of the maker's 12B attention outputs were (finding 72). Layer 50 is
  rewritten: relative change 0.416, the left kept fraction -2.56 with the right at -0.14, a reflection and more
  on the output side of one matrix.
- A direction per matrix: 0.03 to 0.44 to the group reference.
- Rows moved 0.014 to 0.75 on all 30 under the card's "row-norm preservation", every one above finding 22's band
  (0.0057 to 0.0080): 0.75 on layer 50, 0.22 on 47, 0.20 on 41 and 53, 0.16 on 37. The maker's 12B export held
  the rows within 0.0106 on 44 of 46 matrices under the same words; this export, at a preservation weight of
  0.1182 against the 12B's 0.9174, holds none.
- Relative changes 0.039 to 0.416, the largest Heretic changes the census has read on a 31B (coder3101's and
  llmfan46's 31B edits reach 0.06).

| Layer | Change | E1 | E4 | Left kept | Right kept | Weight read | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 24 | 0.0757 | 0.751 | 0.942 | 0.91 | -1.05 | 2.05 | 0.086 |
| 28 | 0.0660 | 0.726 | 0.871 | 0.97 | 0.73 | 0.27 | 0.032 |
| 32 | 0.0741 | 0.783 | 0.895 | 0.89 | -1.23 | 2.23 | 0.053 |
| 37 | 0.1030 | 0.856 | 0.996 | 0.79 | -2.00 | 3.00 | 0.165 |
| 38 | 0.0659 | 0.746 | 0.878 | 1.08 | 1.59 | -0.59 | 0.069 |
| 41 | 0.1033 | 0.952 | 0.995 | 0.85 | -3.47 | 4.47 | 0.201 |
| 44 | 0.1754 | 0.918 | 0.999 | 0.46 | -0.83 | 1.83 | 0.109 |
| 47 | 0.1291 | 0.980 | 0.996 | 0.71 | -1.97 | 2.97 | 0.220 |
| 50 | 0.4156 | 0.869 | 0.999 | -2.56 | -0.14 | 3.56 on the left | 0.747 |
| 53 | 0.1056 | 0.965 | 0.989 | 0.82 | -3.12 | 4.12 | 0.201 |

The full table (30 rows) is in the report.

Directions. Against the saved vectors of twenty 31B measurements, the leading left vectors stand at a median of
0.85 to llmfan46's 31B edit (18 shared), 0.80 and 0.79 to MoonRide's two edits (24 each, piece 5 among them),
0.78 to coder3101's (30) and 0.76 to Bahushruth's (26), the 31B arbitrary-rank family; the right vectors stand at
0.37 to 0.40 to the same five. The kernel and projection edits of the 31B stand at 0.11 or less on the left. The
family's output direction survives the rank-256 search and the QAT checkpoint; its input direction, the side this
branch acts on, does not. None of the thirteen shards equals a measured file.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.6.2 to 5.10.1) are all
that differ; the template is the pin's 18,683-byte file and the fixed conversation renders identically.

## For the recipe library

The directional-per-layer entry is the nearest and its 30 flags are the few directions per matrix; an
arbitrary-rank entry would flag the 30 rows against the preservation claim and layer 50 against any weight band.
The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat37/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
