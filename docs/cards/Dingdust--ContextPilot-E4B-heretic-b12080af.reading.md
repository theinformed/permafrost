# Reading of the Stage 1 and Stage 2 result: Dingdust/ContextPilot-E4B-heretic against google/gemma-4-E4B-it (2026-11-01)

Measured on Blueback, round 25 piece 2. The pull carries the measurements and the sweep record and no job log.
Modified revision `5bf557de` (five commits on 2026-09-03 from 15:41Z to 17:24Z: the model, the tokenizer, the
processor and the README), original pinned at `ee0ef602` (07-20), the revision current when the repository was
created. The README is two cards in one file. The first half prints a Heretic record against "the original":
direction index 31.13, the attention outputs at weight 1.38 centred on layer 36.40 (minimum 0.09, width 12.19),
the down projections at 1.41 centred on 40.24 (minimum 1.39, width 13.62), a KL divergence of 0.0064 and 32
refusals in 100 against 100. The second half is tencent/ContextPilot-E4B's card, byte for byte in its body: "the
Gemma4-E4B checkpoint of ContextPilot", a reinforcement-learning fine-tune of google/gemma-4-E4B-it for
long-horizon context management, with that model's citation and licence. The `base_model` field names Google, and
the pinner paired the copy with Google's E4B. The copy's parent is one step below the field, as finding 45's was.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 360 flags, on the
cluster and after re-scoring at home: 205 unexpected changes, 75 first shares of 0.003 to 0.988, 79 direction
cosines and one cross-kind flag. On reading, the copy is the fine-tune the second card describes on every kind of
tensor, with the first card's two kernels readable on the attention outputs and down projections inside the
windows the kernels give.

- 285 of 2,076 tensors changed, with 189 more under the threshold at 0.0008 to 0.000998 and 1,602 equal: every
  down projection (42), 39 gate and 37 up projections, 39 queries, 22 keys (layers 1 to 23, the layers with their
  own keys), 20 values, 38 attention outputs and 48 vectors (per-layer input gates and normalisations, four of
  them post-per-layer-input norms the tool could not decompose). Outside the kernels' windows the change is 0.10
  to 0.43 percent of each matrix's norm with no leading direction (first share 0.003 to 0.05), rows within
  0.0001, and both sides' kept fractions at 1.000: training, not a projection. The 54 shared-KV tensors are
  dropped by the export.
- The attention kernel: 1.38 at 36.40 with width 12.19 reaches 24.21 to 48.59 of a 42-layer model, layers 25 to
  41, and the attention outputs of exactly those 17 layers carry a leading direction (first share 0.74 at layer
  25 rising to 0.99 at 36, relative change 0.004 to 0.028) where layers 1 to 24 carry none. The down kernel: 1.41
  at 40.24 with width 13.62 reaches 26.62 upward, layers 27 to 41, and the down projections of exactly those 15
  layers carry one (first share 0.978 to 0.988, relative change 0.026 to 0.032) where 0 to 26 carry none.
- The strengths read shallower than the card under the fine-tune. The down kernel is nearly flat (1.41 at its
  centre, 1.39 at its edge), so one minus the weight should read -0.39 to -0.41 on all 15; the left kept fraction
  reads -0.32 to 0.09 (median -0.19), the right -0.06 to 0.16. On the attention outputs the left runs 0.85 at
  layer 25, 0.60 at 29, 0.075 at 35 and 0.35 at 36 where the kernel gives 0.91, 0.46, 0.06 and -0.37, then 0.73,
  0.62, 0.82, 0.76 and 0.22 on layers 37 to 41 where the kernel gives -0.3; the right kept fraction is 0.52 to
  0.95 throughout. The two writers of a layer share no direction (within-layer cosine 0.01 to 0.44), and across
  layers the attention outputs' directions agree at a median of 0.05.
- Rows moved by 0.004 to 0.009 on the kernel's down projections and 0.001 to 0.012 on its attention outputs,
  by up to 0.16 on two key projections (layers 22 and 23, a norm-sized change on small matrices).

| Layer | Attention output: change, E1, left kept, right kept, kernel 1-w | Down projection: change, E1, left kept, right kept, kernel 1-w | Gate projection: change, E1 | Query: change, E1 |
| --- | --- | --- | --- | --- |
| 5 | 0.0013, 0.016, 0.999, 1.000, - | 0.0015, 0.003, 1.000, 1.000, - | 0.0010, 0.007 | 0.0011, 0.008 |
| 20 | 0.0019, 0.018, 1.000, 1.000, - | 0.0042, 0.018, 1.000, 1.000, - | 0.0022, 0.010 | 0.0019, 0.019 |
| 25 | 0.0038, 0.739, 0.847, 0.952, 0.91 | 0.0030, 0.013, 1.000, 1.000, - | 0.0017, 0.010 | 0.0016, 0.015 |
| 29 | 0.0134, 0.942, 0.604, 0.797, 0.46 | 0.0316, 0.985, -0.115, 0.041, -0.40 | 0.0018, 0.012 | 0.0020, 0.019 |
| 33 | 0.0216, 0.987, 0.694, 0.638, 0.01 | 0.0266, 0.987, -0.085, 0.028, -0.41 | 0.0016, 0.009 | 0.0017, 0.013 |
| 36 | 0.0285, 0.994, 0.354, 0.522, -0.37 | 0.0269, 0.986, 0.085, 0.064, -0.41 | 0.0015, 0.010 | 0.0019, 0.016 |
| 39 | 0.0237, 0.991, 0.816, 0.700, -0.31 | 0.0268, 0.987, -0.280, 0.037, -0.41 | 0.0016, 0.008 | 0.0019, 0.019 |
| 41 | 0.0155, 0.958, 0.217, 0.712, -0.14 | 0.0271, 0.979, -0.280, 0.077, -0.40 | 0.0018, 0.014 | 0.0022, 0.025 |

The kernel column is one minus the card's weight at that layer; the full table (285 rows) is in the report.

The fingerprint shares no measured field with the eleven earlier reports on this original; the copy's twelve
shards match nothing. Against treadon's E4B copies of this round (pairs 4 and 5), one tensor equals by value and
none by field.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, ten fields. Under transformers 5.22.1
`text_config.moe_intermediate_size` (null in a 5.16.1 save) closes by the default rule. What stays open: the
5.16 save form (`global_head_dim` 512 and `num_global_key_value_heads` absent, a `per_layer_config` map of
`head_dim` 512 under the global layers' indices), the eighth copy on this form, closed by hand; three token ids
written where the original leaves them unset or lists two (`bos_token_id` 2 against null, `eos_token_id` 1 against
[1, 106], `pad_token_id` 0 against null, in `config.json` and the tokenizer's special ids alike), a loader's
defaults written through by the fine-tune's save, as finding 15 read on another copy; and the template, a
17,336-byte file that is Google's earlier format under a pin whose template is the 18,683-byte Canonical file of
07-20. The parent fine-tune was created on 08-27 and carries the earlier file. The cluster's card also records
that the original's template did not render within the worker's four seconds ("original template default render
failed: TimeoutExpired"), the first such timeout in the census; the home judgement keeps the cluster's rendering
block, so the two renderings stand uncompared for this pair.

## For the recipe library

A Heretic edit on top of a fine-tune, measured against the grandparent: the kernels' windows read to the layer on
both writers, the strengths read shallower, and the fine-tune's 0.1 to 0.4 percent sits on every other matrix.
Finding 18's reading (the parent must be measured as a separate term) applies; against tencent/ContextPilot-E4B
the comparison would read the kernels alone, and that parent is unmeasured. The `base_model` check of finding 48
has a third case: a README whose second card names the true parent. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback25/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
