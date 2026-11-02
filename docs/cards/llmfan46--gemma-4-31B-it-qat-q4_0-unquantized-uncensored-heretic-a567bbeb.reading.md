# Reading of the Stage 1 and Stage 2 result: llmfan46/gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic against google/gemma-4-31B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Nautilus, round 36 piece 1 (download job 4167620, compare job 4167621, sweep 4167629; the pull carries
the measurements and the sweep record and no job log). Modified revision `ce415cf3` (twenty-one commits on
2026-06-11 between 18:22Z and 18:42Z: a model, tokenizer and README upload at 18:25Z, every file deleted at 18:26Z,
a second upload of "7 files" and the two shards by 18:31Z, the README and four edits of it to 18:42Z, the pattern
of the maker's 26B QAT export in round 34), original pinned at `4f926903` (06-05, the release commit of the
QAT-unquantized 31B checkpoint). The card (36,890 bytes, the tool's page under the maker's storage appeal and
support table) says Heretic v1.2.0's arbitrary-rank ablation: `start_layer_index` 9, `end_layer_index` 36,
`preserve_good_behavior_weight` 0.4826, `steer_bad_behavior_weight` 0.0002, `overcorrect_relative_weight` 1.0491,
`neighbor_count` 15, `attn.o_proj` the one targeted component, no preservation claim, KL divergence 0.0365, 11
refusals in 100 against 99. The `base_model` field names the QAT checkpoint. The maker's seventh Gemma 4 copy in
the census and the third on a QAT checkpoint (the 26B-A4B in round 34, the 12B in round 37).

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 16 flags (all
first shares, 0.877 to 0.979), on the cluster and after re-scoring at home. On reading, the copy is the card's
edit on a selection of the window's layers.

- 16 of 1,188 tensors changed: the attention outputs of layers 16, 18, 21, 22 and 24 to 35, inside the card's
  window of 9 to 35 (the end exclusive) and on its one target. Layers 9 to 15, 17, 19, 20 and 23 of the window
  did not move above the threshold; ten of them (10 to 15, 17, 19, 20 and 23) were rewritten under it, at
  relative changes of 0.00003 to 0.000195, which is the largest relative change outside the changed set
  (0.000195, layer 20). The search gave those layers weights near zero. No down projection and no tower tensor
  moved, which places the copy on the QAT checkpoint (finding 48).
- A few directions per matrix: first shares 0.877 to 0.979, fourth cumulative shares 0.946 to 0.989.
- Input side on all 16 (left kept -0.01 to 0.91, right kept negative on every matrix). Read as weights, one
  minus the right kept fraction, 1.58 to 3.64 (median 2.29), 3.64 at layer 32 where the relative change is also
  the largest (0.066) and 3.17 at layer 21, where the left kept fraction is -0.01.
- Rows moved 0.0023 to 0.0515, 0.052 at layer 16, 0.034 at 32 and 0.029 at 33, under no preservation claim;
  three matrices fall in finding 22's band by chance.
- A direction per matrix: 0.21 to 0.48 to the group reference.

| Layer | Change | E1 | E4 | Left kept | Right kept | Weight read | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 16 | 0.0549 | 0.877 | 0.956 | 0.31 | -1.28 | 2.28 | 0.0515 |
| 18 | 0.0387 | 0.914 | 0.976 | 0.47 | -1.33 | 2.33 | 0.0033 |
| 21 | 0.0474 | 0.970 | 0.989 | -0.01 | -2.17 | 3.17 | 0.0119 |
| 22 | 0.0387 | 0.962 | 0.981 | 0.74 | -1.30 | 2.30 | 0.0105 |
| 24 | 0.0261 | 0.979 | 0.984 | 0.72 | -0.67 | 1.67 | 0.0032 |
| 28 | 0.0314 | 0.942 | 0.953 | 0.84 | -1.02 | 2.02 | 0.0058 |
| 32 | 0.0662 | 0.955 | 0.975 | 0.72 | -2.64 | 3.64 | 0.0339 |
| 35 | 0.0234 | 0.929 | 0.946 | 0.83 | -0.58 | 1.58 | 0.0072 |

The full table (16 rows) is in the report.

Directions. Against the saved vectors of twenty-three 31B measurements on the shared names, the leading
directions stand at 0.993 on the left and 0.984 on the right to coder3101's edit of the same checkpoint five
days earlier (piece 2, 14 shared matrices), at 0.938 and 0.957 to coder3101's instruct 31B edit (16), at 0.925
and 0.956 to the maker's own instruct 31B edit (6 shared, that edit's window being 30 to 47), at 0.92 and 0.96 to
MoonRide's April edit and 0.87 and 0.91 to the custom one, at 0.87 and 0.43 to wnfldchen's merged rank-256
export, at 0.79 and 0.71 to Bahushruth's, at 0.37 and 0.71 to OS-Software's rank-four edit of the same
checkpoint (piece 4) and at 0.22 or less to every kernel and projection edit: the 31B arbitrary-rank family of
finding 82, carried to the QAT checkpoint (finding 89). The second shard (`fd00e7a5`) is byte-equal to
coder3101's second shard: both are two-shard saves of the same checkpoint whose edits lie in the first shard.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home: `chat_template.jinja` is the maker's 23,077-byte template,
equal to the text of the maker's 26B QAT export (finding 19's sixth template, with `thinking_gate` and
`preserve_thinking` among its identifiers), in place of the pin's 17,333-byte file; the fixed conversation
renders the same text under both. The two version strings (5.6.2 to 5.10.2) are a re-save.

## For the recipe library

The directional-per-layer entry is the nearest and its 16 flags are the few directions per matrix; an
arbitrary-rank entry with the card's window and target, allowing the window's skipped layers, would read the
copy as a clean match. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus36/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
