# Reading of the Stage 1 and Stage 2 result: TheUmbraWalker/gemma-4-E4B-it-heretic against google/gemma-4-E4B-it (2026-11-02)

Measured on Wheat, round 37 piece 4 (download job 387161, compare job 387165, sweep 387170; the pull carries the
measurements and the sweep record and no job log). Modified revision `9bf78429` (four commits on 2026-05-16 between
15:22Z and 15:24Z: the repository, the weights, the tokenizer, the README), original pinned at `3555bddc` (05-07).
The card (27,552 bytes) is Heretic 1.3.0's card for "a decensored version of a model" (the tool's text when the
model is loaded from a local path): `direction_index` per layer, attention output weight 1.31 at position 27.47
falling to 0.82 at distance 24.19, down projection 1.42 at 28.35 falling to 1.38 at distance 22.01, KL divergence
0.1487, 11 refusals in 100 against 99. It is, line for line, the lower of the two cards on the maker's second
copy, TheUmbraWalker/gemma-4-E4B-it-2-heretic (round 30), whose README stacks a second pass's card over this one.
The `base_model` field names the pretrained google/gemma-4-E4B (finding 67); the pin is the instruct model. The
repository was made the day before the second copy.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 8 flags (the
within-layer cosines of layers 22, 23, 30 and 33, 0.91 to 0.95 where the rule asks 0.95), on the cluster and after
re-scoring at home. On reading, the copy is the per-layer Heretic pass the second copy was built on.

- 73 of 2,076 tensors changed: the attention outputs of layers 4 to 41 (38) and the down projections of 7 to 41
  (35). The card's kernels reach layers 3.3 to 51.7 and 6.3 to 50.4, which on a 42-layer model are 4 to 41 and 7
  to 41, the changed sets exactly, as round 30 read them under the second pass. Nothing else moved; the largest
  relative change outside the changed set is exactly 0 and 2,003 tensors equal the original. The 54 shared-key-value
  tensors of layers 24 to 41 are absent from the save, as from the second copy's.
- Rank one on every matrix (first shares 0.994 to 0.999) and one direction per layer: the two writers agree at 0.91
  to 0.997 within a layer and at 0.00 to 0.69 across layers, the `per layer` of the card.
- The kept fractions carry no readable weight: the left is below the right on 60 of 73 and above it on 13, and
  neither column follows the kernels (one minus the left kept fraction runs 0.28 to 1.15 across the attention window,
  0.99 at layer 19 and 0.28 at layer 10, with no kernel shape), finding 46's scatter on a per-layer direction. Rows moved 0.0028 to 0.0148, unrestored,
  under no claim. Relative changes 0.019 to 0.041, the largest on the down projections of layers 20 to 23.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Within-layer cosine | Rows |
| --- | --- | --- | --- | --- |
| 4 | 0.0215, 0.997, 0.52, 0.68 | - | - | 0.009 |
| 8 | 0.0190, 0.995, 0.21, 0.67 | 0.0334, 0.997, 0.17, 0.47 | 0.968 | 0.008, 0.009 |
| 14 | 0.0230, 0.996, 0.24, 0.68 | 0.0321, 0.998, -0.24, 0.02 | 0.993 | 0.008, 0.005 |
| 20 | 0.0274, 0.996, 0.39, 0.72 | 0.0413, 0.999, 0.09, 0.19 | 0.993 | 0.007, 0.009 |
| 22 | 0.0265, 0.996, 0.63, 0.56 | 0.0409, 0.997, 0.35, 0.29 | 0.911 | 0.008, 0.009 |
| 27 | 0.0265, 0.996, -0.15, 0.61 | 0.0315, 0.997, -0.37, 0.09 | 0.997 | 0.006, 0.005 |
| 33 | 0.0248, 0.996, 0.56, 0.59 | 0.0279, 0.997, -0.21, -0.05 | 0.929 | 0.005, 0.006 |
| 41 | 0.0210, 0.994, 0.01, 0.62 | 0.0270, 0.996, -0.31, 0.13 | 0.996 | 0.005, 0.004 |

The full table (73 rows) is in the report.

Directions. Against the second copy's saved vectors on the same 73 names, the leading directions are equal at 0.99
or better on 57 and at a median of 1.000; the 16 that differ (0.007 to 0.37, and 0.91 at layer 30) are the
attention outputs of layers 18 to 33, the second pass's attention window exactly, where round 30 read two
directions per matrix; on the down projections of 29 to 41, the second pass's other window, the leading direction
is still this pass's at 0.99 or better. The second copy is this one plus the second pass, with no other change
between them, and its second shard (`df30ce31`) is byte-equal to this copy's. Against TrevorJS's E4B edit (round
7) and senjiangchen's duplicate of it, the directions stand at 0.89 to 1.00 on all 73, median 0.98 on the left and
0.99 on the right: the per-layer mean-difference direction of one tool and the per-layer direction of another are
the same direction on this base. treadon's abliteration stands at 0.84 on 34, the arbitrary-rank family at 0.40 or
less. The first shard (`aa3e9d1e`) is the library's layout shared with BinxNet's, p-e-w's, DuoNeural's and
prithivMLmods's E4B exports and the fourth (`8080cb1a`) the vision tower shared across the E4B releases (findings
71 and 75).

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home: `text_config.moe_intermediate_size`
closed by the default rule under transformers 5.22.1, and the two version strings (5.5.0.dev0 to 5.6.2) are a
re-save. The template is the pin's 16,804-byte file and the fixed conversation renders identically.

## For the recipe library

The directional-per-layer entry is the right one and its eight flags are four layers whose two writers agree at
0.91 to 0.95; a tolerance of 0.90 on the within-layer rule would read the copy as a clean match. The direction
vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat37/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
