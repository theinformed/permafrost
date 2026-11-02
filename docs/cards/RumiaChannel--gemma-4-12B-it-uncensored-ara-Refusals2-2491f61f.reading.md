# Reading of the Stage 1 and Stage 2 result: RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals2 against google/gemma-4-12B-it (2026-11-02)

Measured on Nautilus, round 38 piece 3 (download job 4168771, compare job 4168774, sweep 4168780; the pull carries
the measurements and the sweep record and no job log). Modified revision `23484b14` (seven commits from 2026-06-05
to 07-21, the last two updating the template and `tokenizer_config.json`), original pinned at `5926caa4`. The card
(28,796 bytes) is Heretic 1.2.0's card for an arbitrary-rank edit with row-norm preservation: `start_layer` 23,
`end_layer` 43, `preserve_weight` 0.2271, `steer_weight` 0.0001, `overcorrect_weight` 0.1443, `n_neighbors` 13, KL
divergence 0.0103, 2 refusals in 100 against 91. The maker's Refusals9 copy of the same base was measured in round
33 (finding 83's family table).

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 80 flags (40 first
shares, 40 within-layer cosines), 56 rules skipped, on the cluster and after re-scoring at home. On reading, the
copy is what the card says, with three matrices left as residues.

- 40 of 677 tensors changed: both writers of layers 23 to 42, the card's start 23 and end 43 to the layer. Nothing
  else moved; the largest relative change outside the changed set is exactly 0.
- 37 edits and 3 residues: the down projections of layers 25, 27 and 32 changed by 0.0013 to 0.0017 with first
  shares of 0.005 to 0.006, both kept fractions at 1.00 and rows within 0.0008, matrices the search rewrote without
  a direction (finding 58). The 37 edits carry a few directions each (first shares 0.801 to 0.968 on the attention
  outputs, 0.185 to 0.925 on the down projections; four shares 0.552 to 0.975), each writer its own direction
  (within-layer cosines 0.002 to 0.101).
- Input side on all 37: the weight, one minus the right kept fraction, 0.45 to 1.52 on the attention outputs and
  0.77 to 1.08 on the down projections, several partial. Rows moved 0.0061 to 0.0079 on the attention outputs and
  0.0052 to 0.0078 on the down projections, finding 22's band on every edit. Relative changes 0.007 to 0.017.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Within-layer cosine | Rows |
| --- | --- | --- | --- | --- |
| 23 | 0.0067, 0.881, 0.97, 0.26 | 0.0093, 0.910, 0.91, 0.00 | 0.101 | 0.0073, 0.0058 |
| 25 | 0.0143, 0.968, 0.94, 0.13 | 0.0017, 0.006, 1.00, 1.00 (residue) | 0.002 | 0.0079, 0.0007 |
| 27 | 0.0144, 0.937, 0.92, 0.23 | 0.0013, 0.005, 1.00, 1.00 (residue) | 0.093 | 0.0077, 0.0008 |
| 30 | 0.0140, 0.801, 0.93, 0.20 | 0.0162, 0.427, 0.92, -0.08 | 0.027 | 0.0079, 0.0077 |
| 32 | 0.0146, 0.941, 0.92, -0.01 | 0.0013, 0.005, 1.00, 1.00 (residue) | 0.097 | 0.0074, 0.0008 |
| 35 | 0.0123, 0.935, 0.99, 0.37 | 0.0095, 0.883, 0.88, -0.05 | 0.022 | 0.0066, 0.0068 |
| 38 | 0.0171, 0.957, 0.86, 0.12 | 0.0094, 0.860, 0.84, -0.05 | 0.021 | 0.0079, 0.0052 |
| 42 | 0.0170, 0.948, 0.98, 0.10 | 0.0125, 0.621, 0.90, 0.11 | 0.054 | 0.0076, 0.0078 |

The full table (40 rows) is in the report.

Directions. Against thirty-seven saved vectors of 12B measurements, the leading directions stand at 0.98 and 0.99
to the maker's Refusals9 on 38 shared names (eleven names below 0.9, the three residues among them); at 0.64 and
0.27 to OS-Software's first Japanese export on 40; at 0.61 and 0.77 to llmfan46's 12B edit (16), 0.57 and 0.60 to
coder3101's QAT edit, 0.56 and 0.79 to llmfan46's QAT edit, 0.55 and 0.55 to coder3101's 12B edit (40); and at
0.49 or less to the rest, the kernel and projection edits at 0.15 or less. One maker's two searches agree with each
other at the family's own level and stand to the English family at the distance finding 93 measured between two
searches by one maker. The weight file (`b3f9ba0c`) matches no measured file; `tokenizer.json` (`a2619fe1`) is 154
bytes longer than Google's (`cc8d3a0c`), the form finding 19 read on the maker's other copies.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home. The home judgement closed five
fields: `audio_config.audio_samples_per_token`, `audio_config.hidden_size`, `audio_config.output_proj_dims` and
`vision_config.model_patch_size`, absent from the 5.10.2 save and the same values under 5.22.1, and the template,
18,681 bytes against the pin's 17,466, byte-equal to Google's revision `711c1368` of 07-15 ("fix: chat template:
null handling, reasoning preservation, turn-tag balance, input validation"), which the later-revision check
matches. The version strings (5.10.0.dev0 to 5.10.2) are the re-save.

## For the recipe library

An arbitrary-rank entry with the card's window would read the copy as a clean match with three residues named.
The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus38/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
