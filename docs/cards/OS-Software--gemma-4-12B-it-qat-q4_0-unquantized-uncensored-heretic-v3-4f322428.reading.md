# Reading of the Stage 1 and Stage 2 result: OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic-v3 against google/gemma-4-12B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Nautilus, round 36 piece 5 (download job 4167620, compare job 4167625, sweep 4167629; the pull carries
the measurements and the sweep record and no job log). Modified revision `f637e7d3` (five commits on 2026-09-07
between 20:55Z and 20:58Z: the model, tokenizer, processor and README), original pinned at `b6ed8627` (07-20, the
checkpoint's `response_template` commit, the revision current when the repository was created). The card (32,490
bytes) is Heretic v2's page with the same record as the maker's 31B export of the next morning (piece 4):
`start_layer_index` 23, `end_layer_index` 32, `transport` gaussian, `transport_rank` 4, `lora_rank` 128,
`row_normalization` none, `target_components` `attn.o_proj, mlp.down_proj`, `neighbor_count` 1, the preservation
and overcorrection weights 1.0, 0 refusals in 100 against 99, KL divergence 0.0032. The `base_model` field names
google/gemma-4-12B-it; the README's first sentence names the QAT checkpoint, and the pinner paired by the name
(finding 48). The maker's fourth copy of this checkpoint in the census beside the Japanese-prompt `-ja` (piece 8)
and `-ja-v2` (round 37), and its fourth rank-four export.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 35 flags (17
first shares of 0.798 to 0.990 and 18 within-layer cosines of 0.004 to 0.080), on the cluster and after
re-scoring at home. On reading, the copy is the maker's rank-four transport edit on a fourth base, the card's
window on both writers.

- 18 of 677 tensors changed: the attention outputs and down projections of layers 23 to 31, the card's window
  with its exclusive end. Nothing else moved; the largest relative change outside the changed set is exactly 0
  and 659 tensors equal the original, which places the copy on the QAT checkpoint (finding 48).
- Rank four exactly: fourth cumulative shares 0.989 to 0.999, where the first share alone is 0.798 to 0.913 on
  the down projections and 0.935 to 0.993 on the attention outputs.
- Input side on all 18. Read as weights along the leading input direction, 0.76 to 1.67 on the down projections
  (median 1.42; 0.76 and 0.81 at layers 23 and 24) and 0.58 to 2.43 on the attention outputs (median 1.29; 0.58
  at 23 and 24, 2.43 at 29).
- The two writers of a layer take unrelated directions (within-layer cosines 0.004 to 0.080); the layers agree
  at 0.20 to 0.43 with their group reference.
- Rows moved 0.0010 to 0.0056 on the down projections and 0.0099 to 0.0312 on the attention outputs, under the
  card's `row_normalization` none.

| Layer | Writer | Change | E1 | E4 | Left kept | Right kept | Weight read | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 23 | down | 0.0136 | 0.913 | 0.989 | 0.95 | 0.24 | 0.76 | 0.0056 |
| 23 | attention | 0.0222 | 0.990 | 0.996 | 0.99 | 0.42 | 0.58 | 0.0099 |
| 25 | down | 0.0201 | 0.862 | 0.994 | 0.89 | -0.05 | 1.05 | 0.0017 |
| 25 | attention | 0.0549 | 0.986 | 0.999 | 0.93 | -0.24 | 1.24 | 0.0289 |
| 28 | down | 0.0201 | 0.806 | 0.994 | 0.85 | -0.66 | 1.66 | 0.0018 |
| 28 | attention | 0.0426 | 0.935 | 0.999 | 0.89 | -0.48 | 1.48 | 0.0138 |
| 29 | attention | 0.0359 | 0.988 | 0.998 | 0.97 | -1.43 | 2.43 | 0.0145 |
| 31 | attention | 0.0435 | 0.975 | 0.999 | 0.95 | -1.11 | 2.11 | 0.0223 |

The full table (18 rows) is in the report.

Directions. Against the saved vectors of thirty-five 12B measurements on the shared names, the leading left
vectors stand at 0.50 or less to every edit (0.50 to the maker's `-ja` export, 0.48 to RumiaChannel's two,
llmfan46's and coder3101's edits, 0.39 to the maker's `-ja-v2`) and the leading right vectors at 0.59 to 0.68 to
the arbitrary-rank edits of the 12B and its QAT checkpoint (wnfldchen's 0.68, coder3101's QAT 0.66, coder3101's
instruct 0.63, llmfan46's two 0.59 and 0.60), 0.50 to the maker's `-ja-v2` and 0.39 to its `-ja`, with the kernel
and projection edits at 0.17 or less: as on the 31B, the leading input direction shares its cosine with the
arbitrary-rank family's and the output direction does not (finding 90). The first two shards (`513abfa9`,
`ebfb917e`) are byte-equal to JJaguar's export's (piece 6) and the first to the maker's `-ja-v2`, wnfldchen's
and igorls's: the library layout of the 12B QAT checkpoint under one shard size (finding 71), the shards below
every window.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, three fields: the 5.16.1 save moved `global_head_dim` 512
and `num_global_key_value_heads` 1 into a `per_layer_config` map, finding 39's form (its first 12B case was
Vampelium's), closed by hand; the version strings (5.10.0.dev0 to 5.16.1) are a re-save; the template is the
pin's and renders identically.

## For the recipe library

The directional-per-layer entry is the nearest and its 35 flags are the four directions per matrix and the
unrelated writers; a rank-stated subspace entry would read the copy as a clean match (finding 42). The direction
vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus36/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
