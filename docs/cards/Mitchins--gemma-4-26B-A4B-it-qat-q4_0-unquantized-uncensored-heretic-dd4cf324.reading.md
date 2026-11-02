# Reading of the Stage 1 and Stage 2 result: Mitchins/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic against google/gemma-4-26B-A4B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Nautilus, round 36 piece 7 (download job 4167620, compare job 4167627, sweep 4167629; the pull carries
the measurements and the sweep record and no job log). Modified revision `d62fa836` (two commits on 2026-08-23:
the repository at 07:39Z, one folder upload at 09:30Z), original pinned at `f1e06dc5` (07-20, the revision current
when the repository was created and the commit the maker's own record names). The card (3,302 bytes, the maker's
own text) says the copy was made with Heretic by directional ablation with an Optuna kernel search: the kernel was
optimised on the stock google/gemma-4-26B-A4B-it over 200 trials and transferred to the QAT checkpoint with the
directions recomputed there (a mean per-layer cosine of 0.973 to the stock directions), applied to the attention
out-projections and dense down projections through merged adapters and to all 128 fused expert down projections
of each layer, with a patched tool (fused-expert support, low-memory loading); it reports 24 refusal keywords in
100 against 100, a KL divergence of 0.078, ARC-Challenge 94.11 against 93.86, and a `reproduce/` folder. That
folder's record (`reproduce.json`, version 3, timestamped 07:38Z) names Heretic v2.0.0.dev0 from a local source,
transformers 5.15.0, trial 140 of 200 at seed 140, `orthogonalize_direction` true, `row_normalization` full with
`full_normalization_lora_rank` 3, `direction_index` 20.7, and three kernels: attention outputs 1.43 at position
18.25 falling to 1.37 at distance 15.79, expert down projections 1.33 at 18.4 falling to 0.5 at distance 7.86,
dense down projections 1.47 at 19.09 falling to 0.87 at distance 4.86; its `SHA256SUMS` lists the eleven shards
the hub serves. The `base_model` field names both the QAT checkpoint and the instruct model. The maker's first
copy in the census.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 8 flags (seven
first shares of 0.976 to 0.989 on the worst expert of seven packed tensors, one within-layer cosine of 0.867 at
layer 19), on the cluster and after re-scoring at home. On reading, the copy is the record's three kernels to the
layer, one direction through the dense writers and the experts, with the rows not restored on the experts.

- 52 of 1,013 tensors changed: the attention outputs of layers 3 to 29 (27), the packed expert down projections
  of layers 11 to 26 (16 tensors, all 128 experts of each) and the dense down projections of layers 15 to 23
  (9). Each set is a kernel's reach: 18.25 less 15.79 is 2.46, so the attention kernel reaches layers 3 to 29;
  18.4 plus or minus 7.86 spans 10.54 to 26.26, layers 11 to 26; 19.09 plus or minus 4.86 spans 14.23 to 23.95,
  layers 15 to 23. No router, gate-up, reading-side projection or tower tensor moved; the largest relative
  change outside the changed set is exactly 0 and 961 tensors equal the original, which places the copy on the
  QAT checkpoint (finding 48).
- One direction: first shares 0.996 to 0.998 on the attention outputs and 0.992 to 0.997 on the dense down
  projections; the experts of a layer share their direction at 0.9999 (median) and the three kinds agree at
  0.80 or better (group medians 0.986, 0.99999 and 0.998). The scorer's seven flags are the worst expert of a
  packed tensor at 0.976 to 0.989, finding 13's reading.
- No readable kernel: the attention outputs keep -0.36 to 0.70 on the left and 0.23 to 0.56 on the right (the
  left below the right on 26 of 27), the dense down projections -0.28 to 0.16 and 0.66 to 0.84, the experts
  -0.29 to 0.47 and 0.81 to 0.93; read as one minus the right fraction the three kinds give 0.44 to 0.77, 0.16
  to 0.34 and 0.07 to 0.19 against kernels of 1.37 to 1.43, 0.87 to 1.47 and 0.5 to 1.33, finding 46's scatter on
  the mixture.
- Rows moved 0.0074 to 0.0161 on the attention outputs, 0.0086 to 0.0218 on the dense down projections and
  0.028 to 0.184 on the experts (0.18 at layer 16, 0.17 at 19), under the record's `row_normalization` full at
  adapter rank 3: the restoration holds within twice finding 22's band on the dense writers and not on the
  experts.

| Layer | Writer | Change | E1 | Left kept | Right kept | Group cosine | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | attention | 0.0255 | 0.996 | -0.21 | 0.46 | 0.98 | 0.0109 |
| 11 | experts | 0.0106 | packed | 0.45 | 0.93 | 1.00 | 0.0291 |
| 15 | dense down | 0.0161 | 0.992 | 0.14 | 0.77 | 1.00 | 0.0099 |
| 16 | experts | 0.0213 | packed | -0.08 | 0.85 | 1.00 | 0.1837 |
| 19 | dense down | 0.0281 | 0.997 | -0.28 | 0.66 | 1.00 | 0.0193 |
| 19 | attention | 0.0394 | 0.998 | 0.70 | 0.27 | 0.93 | 0.0151 |
| 26 | experts | 0.0098 | packed | 0.47 | 0.92 | 1.00 | 0.0314 |
| 29 | attention | 0.0235 | 0.996 | -0.24 | 0.40 | 0.97 | 0.0100 |

The full table (52 rows) is in the report.

Directions. Against the saved vectors of twenty-two 26B-A4B measurements on the shared names, the leading
directions stand at 0.57 and 0.60 to sh0ck0r's edit (30 shared; 0.70 on the dense down projections, 0.44 on the
attention outputs), at 0.54 to xdavxd's run of TrevorJS's method on the same checkpoint (52 shared; the experts
at 0.58 on the left and 0.05 on the right), at 0.53 to SevenOfNine's and BinxNet's, at 0.47 to TrevorJS's edit
and its four copies (the dense down projections 0.68 and 0.72, the attention outputs 0.29 and 0.35, the experts
0.55 and 0.06), at 0.35 to WWTCyberLab's, and at 0.15 or less to the arbitrary-rank edits and huihui-ai's: a
direction of its own, nearest the kernel edits on the dense down projections (finding 92). The eleven shards
equal no measured file and equal the record's checksums.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, eight fields. `generation_config.json` was written by the
library from the model configuration (`_from_model_config` true, 5.15.0): `do_sample` true, `top_k` 64 and
`top_p` 0.95 are gone, `temperature` 1.0 is gone (closed as the default), and `eos_token_id` reads [1, 106]
where the checkpoint's reads [1, 106, 50], the third stop token being `<|tool_response>`; loaded as published
the copy decodes greedily and does not stop at a tool response, and the card says nothing of it (finding 4).
`config.json` carries the 5.15.0 save's `per_layer_config` map in place of `global_head_dim` 512 and
`num_global_key_value_heads` 2, finding 39's form, closed by hand. The template is the pin's and renders
identically.

## For the recipe library

The directional-per-layer entry is the nearest and its 8 flags are the worst experts and one layer; a kernel
entry that takes the record's three kernels and the expert kind, with a per-expert median in place of the worst
expert, would read the copy as a clean match. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus36/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
