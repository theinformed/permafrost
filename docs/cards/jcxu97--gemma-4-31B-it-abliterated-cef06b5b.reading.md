# Reading of the Stage 1 and Stage 2 result: jcxu97/gemma-4-31B-it-abliterated against google/gemma-4-31B-it (2026-11-02)

Measured on Wheat, round 41 piece 7 (download job 387195, compare job 387202, sweep 387203; the pull carries the
measurements and the sweep record and no job log). Modified revision `3772316f` (one commit, 2026-04-12 15:50Z,
titled "Duplicate from wangzhang/gemma-4-31B-it-abliterated"), original pinned at `439edf56` of 04-10. The parent
repository is measured (round 2, repeated in round 3) at its head, which is not the export the duplicate holds:
wangzhang's history runs from uploads of 04-07 and 04-10 (`2a9b26cd`, the weights) through a tokenizer and
template sync of 04-11 (`90a225e3`, the state the duplicate copied the next day) to "Update Gemma 4 31B
abliterated to trial 40" on 04-29 (`18b899a5`) and two card commits of 08-29. The batch note says the copy "was
duplicated from wangzhang's and its weight files differ", and the hub's file listings place the duplicate's two
shards (`613f3f35`, `566addbf`) at wangzhang's `2a9b26cd` and `90a225e3` by object id. The card is wangzhang's
of 04-10, byte for byte: Abliterix, "direct orthogonal projection on attention Q/K/V/O projections and MLP down
projections (5 steerable components per layer)", "norm-preserving row magnitude restoration", winsorised steering
vectors, a strength range of 1.0 to 6.0, 18 refusals in 100 against 99 after "20/80 (warmup phase only)" trials
and a KL divergence of 0.0007. The copy drops the `.linear.` segment from 189 names the original carries, mapped
before the comparison.

## Weights (Stage 2)

The tool's assessment was a clean match of `directional-per-layer-selected`, 0 flags, on the cluster and after
re-scoring at home. On reading, the copy is one direction per layer projected from all five of the card's
components across layers 27 to 59, the readers on the input side and the writers on the output side, at weights
to 5.5, with every row restored.

- 120 of 1,188 tensors changed: the attention outputs of layers 29 to 59 (31), the down projections of 29 to
  58 (30), the keys of 27 to 53 (27), the queries of 31 to 47 (17) and the values of 42 to 58 (15). Nothing
  else moved; the largest relative change outside the changed set is exactly 0 on all 1,068 other tensors.
- Rank one on every matrix (first shares 0.993 to 0.999) and one direction per layer shared by all five kinds:
  the readers and writers of a layer at 1.000 to each other, the layers at 0.13 to 0.93 to layer 44.
- Output side on the writers: one minus the left kept fraction is 1.38 at layer 29 rising to 1.95 at 52 on the
  attention outputs and 1.86 at 29 rising to 5.33 at 44 and falling to 1.85 at 58 on the down projections.
  Input side on the readers: one minus the right kept fraction is 3.6 to 4.3 on the keys, 3.9 at layer 31
  rising to 5.54 at 39 and falling to 4.0 at 47 on the queries, and 1.41 to 1.72 on the values. Rows moved
  0.00007 to 0.00108 on all 120, the card's restoration. Relative changes 0.0185 to 0.0756.

| Layer | Attention output: change, left kept, weight | Down projection: change, left kept, weight | Key: change, right kept, weight | Query: change, right kept, weight | Value: change, right kept, weight | Rows (largest) |
| --- | --- | --- | --- | --- | --- | --- |
| 27 | - | - | 0.0494, -2.61, 3.61 | - | - | 0.00018 |
| 29 | 0.0216, -0.38, 1.38 | 0.0303, -0.86, 1.86 | 0.0495, -2.71, 3.71 | - | - | 0.00034 |
| 31 | 0.0210, -0.38, 1.38 | 0.0345, -1.21, 2.21 | 0.0595, -2.84, 3.84 | 0.0559, -2.91, 3.91 | - | 0.00035 |
| 35 | 0.0237, -0.46, 1.46 | 0.0546, -2.35, 3.35 | 0.0687, -3.14, 4.14 | 0.0685, -3.76, 4.76 | - | 0.00063 |
| 39 | 0.0252, -0.57, 1.57 | 0.0721, -3.62, 4.62 | 0.0636, -3.32, 4.32 | 0.0732, -4.54, 5.54 | - | 0.00053 |
| 41 | 0.0229, -0.63, 1.63 | 0.0740, -4.09, 5.09 | 0.0513, -3.33, 4.33 | 0.0751, -4.43, 5.43 | - | 0.00061 |
| 44 | 0.0243, -0.72, 1.72 | 0.0742, -4.33, 5.33 | 0.0599, -3.19, 4.19 | 0.0636, -3.72, 4.72 | 0.0203, -0.47, 1.47 | 0.00046 |
| 47 | 0.0256, -0.81, 1.81 | 0.0679, -3.94, 4.94 | 0.0508, -2.96, 3.96 | 0.0565, -3.03, 4.03 | - | 0.00051 |
| 50 | 0.0268, -0.88, 1.88 | 0.0587, -3.08, 4.08 | 0.0522, -2.76, 3.76 | - | 0.0224, -0.70, 1.70 | 0.00021 |
| 53 | 0.0262, -0.92, 1.92 | 0.0444, -2.09, 3.09 | 0.0425, -2.59, 3.59 | - | - | 0.00050 |
| 56 | 0.0297, -0.93, 1.93 | 0.0335, -1.26, 2.26 | - | - | 0.0221, -0.59, 1.59 | 0.00016 |
| 58 | 0.0338, -0.92, 1.92 | 0.0285, -0.85, 1.85 | - | - | 0.0223, -0.50, 1.50 | 0.00018 |
| 59 | 0.0288, -0.91, 1.91 | - | - | - | - | 0.00011 |

The full table (120 rows) is in the report.

Directions. Against twenty-four saved vectors of other measurements of the 31B, the directions stand at 1.000
on both sides to the census's measurement of wangzhang's repository, trial 40, on all 73 shared names (29
attention outputs, 13 keys, 17 queries and 14 values; the minimum 1.000), where the kept fractions differ on
every one of them (the layer 29 attention output at -0.38 here and -2.48 there, the layer 30 key at -2.77 and
-0.11) and the duplicate's 30 down projections have no counterpart, trial 40 touching no down projection. The
same tool on the same base and prompts gives the two trials one direction and two weights, finding 105's
reading of 1.000 on the 31B. The directions stand at 0.89 to callmegrr's heretic-z (12), 0.86 to 0.87 to
ressl's, Vampelium's, Sabomako's 31B and 3MPER0RR's, 0.85 to TrevorJS's and 0.84 to germlag's duplicate, 0.79 to
nguyenthilaitrieulong's, and at 0.52 or less to the rest: 0.52 to null-space's, 0.37 to DuoNeural's, 0.27 to
0.29 to huihui-ai's two, 0.22 to Jim-darby's, 0.21 to Bahushruth's and Kooten's, 0.11 to coder3101's, 0.055 to
sh0ck0r's Artemis copy on all 120 names and 0.013 to cosmicoptima's. By byte range the duplicate is byte-equal
to wangzhang's `90a225e3` on the layer 41 attention output, query projection and down projection and the layer
10 query projection, and 0.0295, 0.0032 and 0.0740 from the head's trial 40 on the three edited tensors (the
head's layer 41 down projection byte-equal to Google's); against Google's the three are 0.0229, 0.0751 and
0.0740 apart, and the layer 10 query projection is byte-equal on all four.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on one field, "consistent with re-save noted" at home: the home
judgement closed `text_config.moe_intermediate_size` by the default rule under transformers 5.22.1, leaving the
version strings (5.5.0.dev0 to 5.5.3). The tokenizer, the token ids (`eos_token_id` `[1, 106]`, generation
`[1, 106, 50]`), the generation settings and the 16,448-byte template are the pin's, the template and tokenizer
configuration being the ones wangzhang synced from Google on 04-11.

## For the recipe library

The per-layer entry with selection reads the copy exactly across five kinds; a weight line would print the
down-projection kernel to 5.33 and the query kernel to 5.54. The duplicate rule should read a parent's history
and not its head: the measured repository name did not mean the measured bytes. The direction vectors stay in
the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat41/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
