# Reading of the Stage 1 and Stage 2 result: xdavxd/gemma-4-26B-A4B-it-qat-heretic-ega against google/gemma-4-26B-A4B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Nautilus, round 34 piece 5 (download job 4163806, compare job 4163811, sweep 4163815; the pull of
11-01 21:23Z carries the measurements and the sweep record and no job log). Modified revision `e4f7ab90` (13
commits: created 2026-09-06 at 06:34Z, the weights at 06:41Z under the title "xdavxd v0: biprojection + EGA on
gemma-4-26B-A4B-it-qat-q4_0-unquantized (f1e06dc)", eleven README edits to 09-08 15:46Z), original pinned at
`f1e06dc5`, the commit the title names (a later Google revision than pieces 1 and 3's `641f1844`, with the same
weight file). The card (19,592 bytes) describes TrevorJS's norm-preserving biprojection with an expert-granular
ablation run through a Heretic HEAD: per-layer directions from residual differences winsorised at 0.995 and
orthogonalised against the harmless mean, scale 1.0, expert scale 1.0, row-norm preservation, 60 dense slices and
3,840 expert slices, "1,013 tensors, same names", KL divergence 0.0789, refusals 4 of 100, transformers 5.16.1, on
a DGX Spark. The field `base_model` names the QAT checkpoint.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer`, 30 flags, on the cluster
and after re-scoring at home: the worst expert's first share in 29 of the 30 packed tensors (0.946 to 0.990,
under the rule's line while every median is above it) and the within-layer cosine of layer 15 (0.949). On
reading, the copy is TrevorJS's method on every layer and every expert of the model, with the rows put back,
along TrevorJS's directions.

- 90 of 1,013 tensors changed: the attention outputs, the shared dense down projections and the packed expert
  down tensors of all 30 layers, 128 of 128 experts measured in each. The 30 gate-up tensors, the 30 routers and
  everything else read exactly 0; the largest relative change outside the changed set is exactly 0, which places
  the copy on the QAT checkpoint (finding 48). The card's 60 dense and 3,840 expert slices are the changed set.
- One direction per layer across the three kinds: within-layer cosines 0.95 to 1.00, the experts' left vectors
  agreeing with each other at 0.996 to 0.999 (median per layer); across layers the directions drift, 0.007 to
  0.63 to the group reference.
- Output side on 90 of 90. Along the leading output direction the attention outputs keep 0.02 to 0.46 (weights
  0.54 to 0.98), the shared down projections 0.02 to 0.41 (0.59 to 0.98), and the experts a median 0.014 to 0.18
  on 28 layers and 0.33 and 0.43 on layers 26 and 29 (one expert of layer 26 keeps 0.87): finding 24's "scale
  1.0 with the biprojection's second term". The right side keeps 0.44 to 0.85.
- Rows moved 0.0001 to 0.0004 on the dense matrices and 0.0005 to 0.0009 per packed expert tensor: the
  restoration holds, the second preservation claim in the census to do so after Bahushruth's (finding 57), and
  within finding 24's 0.0004 and 0.0012.
- First shares 0.991 to 0.997 on the dense matrices, 0.990 to 0.994 (median) on the experts with a worst expert
  at 0.946: the storage floor of finding 3 on a bfloat16 file.
- Against TrevorJS's own 26B-A4B edit of the instruct model (second pass, nautilus3 pair 4) the saved leading
  left vectors stand at 0.79 to 0.99 on all 90 shared tensors (median 0.97; right median 0.95): the same method
  finds the same directions on the two Google checkpoints. Against eadx's duplicate of huihui-ai's QAT edit the
  directions touch at layer 10 (0.78) and fall away; against huihui-ai's instruct edit the median is 0.20
  (0.75 at layer 13); against mewse's and OS-Software's arbitrary-rank edits of this checkpoint 0.35 and 0.27 at
  most; against llmfan46's 0.41 at most.

| Layer | Attention output: change, E1, left kept, right kept | Shared down: change, E1, left kept, right kept | Experts: change (median), E1 (median, min), left kept (median, min, max), right kept (median), left agreement | Within-layer cosine | Cross-layer cosine | Rows (dense, experts) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.0308, 0.995, 0.46, 0.55 | 0.0226, 0.993, 0.03, 0.77 | 0.0191, 0.991, 0.946, 0.09, -0.03, 0.52, 0.86, 0.997 | 0.975 | 0.036 | 0.0002, 0.0005 |
| 2 | 0.0244, 0.996, 0.15, 0.47 | 0.0185, 0.995, 0.03, 0.82 | 0.0196, 0.994, 0.950, 0.03, 0.00, 0.19, 0.84, 0.998 | 0.991 | 0.067 | 0.0002, 0.0005 |
| 4 | 0.0289, 0.993, 0.23, 0.46 | 0.0205, 0.994, 0.05, 0.75 | 0.0195, 0.992, 0.970, 0.06, 0.02, 0.26, 0.84, 0.997 | 0.983 | 0.177 | 0.0003, 0.0005 |
| 6 | 0.0286, 0.993, 0.25, 0.47 | 0.0191, 0.994, 0.06, 0.77 | 0.0198, 0.993, 0.985, 0.03, -0.00, 0.20, 0.84, 0.996 | 0.982 | 0.245 | 0.0003, 0.0009 |
| 8 | 0.0246, 0.994, 0.21, 0.50 | 0.0190, 0.994, 0.04, 0.77 | 0.0205, 0.992, 0.987, 0.02, -0.01, 0.23, 0.85, 0.997 | 0.982 | 0.350 | 0.0003, 0.0005 |
| 10 | 0.0279, 0.994, 0.26, 0.51 | 0.0188, 0.992, 0.03, 0.82 | 0.0221, 0.991, 0.981, 0.01, -0.00, 0.19, 0.86, 0.998 | 0.960 | 0.500 | 0.0003, 0.0005 |
| 12 | 0.0230, 0.993, 0.29, 0.49 | 0.0190, 0.991, 0.03, 0.83 | 0.0207, 0.991, 0.982, 0.09, 0.04, 0.26, 0.85, 0.997 | 0.963 | 0.485 | 0.0003, 0.0005 |
| 14 | 0.0219, 0.993, 0.13, 0.57 | 0.0199, 0.992, 0.08, 0.78 | 0.0218, 0.991, 0.984, 0.05, 0.01, 0.21, 0.86, 0.998 | 0.982 | 0.592 | 0.0003, 0.0005 |
| 15 | 0.0240, 0.993, 0.28, 0.59 | 0.0183, 0.991, 0.13, 0.79 | 0.0203, 0.990, 0.983, 0.03, -0.01, 0.12, 0.86, 0.998 | 0.949 | 0.581 | 0.0003, 0.0005 |
| 16 | 0.0227, 0.993, 0.26, 0.59 | 0.0187, 0.991, 0.26, 0.78 | 0.0202, 0.990, 0.979, 0.03, 0.00, 0.12, 0.85, 0.997 | 0.974 | 0.624 | 0.0003, 0.0006 |
| 18 | 0.0203, 0.993, 0.18, 0.58 | 0.0193, 0.991, 0.17, 0.84 | 0.0190, 0.990, 0.982, 0.18, 0.05, 0.41, 0.85, 0.998 | 0.972 | 0.622 | 0.0004, 0.0005 |
| 20 | 0.0200, 0.992, 0.06, 0.61 | 0.0209, 0.993, 0.08, 0.77 | 0.0194, 0.991, 0.984, 0.02, -0.02, 0.16, 0.83, 0.998 | 0.996 | 0.628 | 0.0003, 0.0007 |
| 22 | 0.0198, 0.993, 0.12, 0.53 | 0.0192, 0.992, 0.10, 0.75 | 0.0191, 0.992, 0.989, 0.04, -0.02, 0.10, 0.83, 0.998 | 0.995 | 0.589 | 0.0003, 0.0005 |
| 24 | 0.0219, 0.994, 0.04, 0.44 | 0.0192, 0.992, 0.06, 0.78 | 0.0189, 0.992, 0.988, 0.08, 0.02, 0.24, 0.83, 0.999 | 0.994 | 0.539 | 0.0002, 0.0006 |
| 26 | 0.0216, 0.994, 0.02, 0.48 | 0.0222, 0.993, 0.41, 0.80 | 0.0195, 0.992, 0.982, 0.01, 0.00, 0.11, 0.83, 0.999 | 0.995 | 0.461 | 0.0002, 0.0005 |
| 27 | 0.0200, 0.993, 0.35, 0.60 | 0.0252, 0.993, 0.23, 0.78 | 0.0190, 0.992, 0.989, 0.14, 0.01, 0.61, 0.83, 0.999 | 0.980 | 0.435 | 0.0003, 0.0005 |
| 28 | 0.0193, 0.993, 0.03, 0.48 | 0.0242, 0.993, 0.23, 0.79 | 0.0188, 0.992, 0.990, 0.04, 0.01, 0.68, 0.82, 0.999 | 0.998 | 0.387 | 0.0002, 0.0005 |
| 29 | 0.0192, 0.993, 0.07, 0.47 | 0.0281, 0.991, 0.10, 0.85 | 0.0194, 0.992, 0.989, 0.43, 0.04, 0.87, 0.81, 0.998 | 0.996 | 0.301 | 0.0004, 0.0005 |

The copy's two shards are `e3adddf8` and `8892c963`, the sizes of the library's two-shard layout for this
checkpoint and both its own, because the experts of every layer are touched; no measured file is equal.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home: the 5.16 save form of finding 39 (`global_head_dim` 512
and `num_global_key_value_heads` 2 absent from the copy, a `per_layer_config` map added) beside the version
strings (5.6.2 to 5.16.1). The same three fields were closed by hand on mewse's and OS-Software's copies in round
32 and stand as "unexplained" on their committed cards too; the reclassification tool under 5.22.1 moves none of
them. The template is the pin's 18,683-byte file and the fixed conversations render identically.

## For the recipe library

The norm-preserving biprojection entry (finding 24) matches every measure: one direction per layer across the
three kinds, output side, kept medians 0.01 to 0.18 on 28 of 30 layers, rows within 0.0009. The per-layer
entry counts the worst expert in 29 layers for a first share under 0.99 while every median is 0.990 or above;
a rule on the median expert would clear all 29. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus34/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
