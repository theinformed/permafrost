# Reading of the Stage 1 and Stage 2 result: DavidAU/gemma-4-E2B-it-The-DECKARD-HERETIC-UNCENSORED-Thinking against google/gemma-4-E2B-it (2026-11-01)

Measured on Nautilus, round 32 piece 3 (download job 4145233, compare job 4145236, 284 seconds, sweep 4145242;
the compare finished its measurement and its card and then missed the desk at its report-home step on a DNS
failure, so its drop arrived with the logs). Modified revision `5a385da5` (five commits: the weights on
2026-05-16 at 11:48Z as "Upload folder using huggingface_hub", "Update chat_template.jinja" on 05-17 at 02:54Z,
a README created two minutes later and edited on 05-19), original pinned at `b324173c`, the revision current when
the repository was created. The card is 986 bytes and says the model was "uncensored, then fine tuned", with the
training framework named and no layer, weight or dataset. The `base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 276 flags, on the cluster and
after re-scoring at home: 135 unexpected changes, 70 first shares of 0.54 to 0.97, 70 direction cosines of 0.03 to
0.65 and one cross-kind flag. On reading, the copy is what its card says in five words: a fine-tune laid over an
ablation, with the ablation still readable on the attention outputs of sixteen layers.

- 205 of 2,011 tensors changed: the query, output, gate, up and down projections of all 35 layers (175) and the
  key and value projections of layers 0 to 14 (30), which are every projection the model has (layers 15 to 34
  share the keys and values of earlier layers). No norm, no embedding, no per-layer embedding and no vision or
  audio tensor moved; the largest relative change outside the changed set is exactly 0 and 1,806 tensors equal
  the original.
- The change is 0.2 to 4.8 percent of the norm and low-rank everywhere: first share 0.54 to 0.97, fourth
  cumulative share 0.72 to 0.96, which is a trained delta of small rank rather than a projection (rank one) or a
  round trip (flat).
- On 189 of the 205 the kept fractions read within 0.04 of 1 on the right side, and on the left within 0.04 of 1
  on the attention inputs (queries, keys, values), the attention outputs outside the window and the down
  projections, 0.74 to 1.25 on the
  gate and up projections: the fine-tune moved the matrices without removing a direction from any of them. On the attention outputs of layers 16 to 31 they read 0.65 to
  0.97 on the left and -0.47 to 0.39 on the right, output side on all 16, with the largest changes of the model
  (2.4 to 4.9 percent against 0.3 to 0.8 on the attention outputs of layers 0 to 15 and 32 to 34). That is the
  ablation under the fine-tune: a window of sixteen layers on one writer, one direction per matrix (the leading
  directions agree at 0.07 to 0.18 with the group reference), with the training's delta added over it.
- The down projections of layers 15 to 34 read first shares of 0.91 to 0.97 against 0.78 to 0.94 on layers 0 to
  14, and kept fractions of 0.92 to 1.02 on both sides: the fine-tune, not a second ablation writer.
- Rows moved by 0.0004 to 0.013 on the 205 matrices; the attention outputs of 16 to 31 moved 0.006 to 0.009.

| Layer | Attention output: change, E1, E4, left kept, right kept | Down projection: change, E1, E4, left kept, right kept |
| --- | --- | --- |
| 4 | 0.0083, 0.933, 0.959, 1.01, 1.03 | 0.0055, 0.852, 0.902, 1.00, 1.00 |
| 12 | 0.0045, 0.733, 0.832, 0.99, 0.99 | 0.0052, 0.799, 0.883, 1.00, 1.00 |
| 15 | 0.0071, 0.623, 0.868, 0.98, 0.98 | 0.0088, 0.947, 0.963, 1.01, 1.02 |
| 16 | 0.0485, 0.824, 0.897, 0.65, -0.42 | 0.0111, 0.966, 0.975, 0.99, 0.97 |
| 18 | 0.0277, 0.835, 0.907, 0.80, -0.47 | 0.0073, 0.931, 0.946, 0.99, 0.97 |
| 21 | 0.0206, 0.807, 0.912, 0.97, 0.08 | 0.0089, 0.954, 0.961, 0.99, 0.96 |
| 25 | 0.0434, 0.885, 0.926, 0.65, -0.23 | 0.0090, 0.960, 0.966, 0.99, 0.96 |
| 28 | 0.0245, 0.835, 0.943, 0.84, -0.17 | 0.0094, 0.951, 0.968, 0.99, 0.97 |
| 31 | 0.0224, 0.781, 0.917, 0.94, -0.01 | 0.0081, 0.937, 0.955, 0.99, 0.96 |
| 32 | 0.0074, 0.643, 0.873, 1.00, 1.00 | 0.0091, 0.889, 0.961, 1.00, 0.98 |
| 34 | 0.0077, 0.703, 0.923, 1.01, 1.02 | 0.0132, 0.901, 0.978, 0.97, 0.97 |

The other five projections are in the report (the home table lists all 205 rows): changes of 0.2 to 1.6 percent
on the three attention inputs (queries, keys, values) with first shares of 0.27 to 0.90, and 0.4 to 2.9 percent on the gate and up
projections with first shares of 0.33 to 0.97, the fine-tune's shape on every layer.

The fingerprint shares no measured field with the five earlier reports on the E2B original or with amkkk's copy
of this round.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, two fields, and a template that changes the generation
prompt. The copy's 16,352-byte `chat_template.jinja` (`c74f3aa5`) is Google's 16,804-byte file of
the pin (`33204f1a`) with one edit: a `<|think|>` line emitted after the generation prompt, so the fixed
conversation renders one line longer than the original's. The commit "Update chat_template.jinja" of 05-17 is the
maker's own, a day after the upload, and the README created two minutes after it names the thinking mode in its
title. The configuration and generation settings equal the original's field for field, version strings included
(5.5.0.dev0 on both sides). Nothing to close: the field reads as what it is.

## For the recipe library

An ablation-then-training pair, the mirror of finding 18's training-then-ablation pair, under a template edit
that changes what the model is asked to continue (finding 49). No recipe can fit a fine-tune; the ablation under it
reads as a sixteen-layer window on the attention outputs with its weights blurred by the training's delta, and a
reading that wanted the kernel would need the training measured as a separate term first. The pull copy keeps
the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus32/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
