# Reading of the Stage 1 and Stage 2 result: coder3101/Magidonia-24B-v4.3-heretic against TheDrummer/Magidonia-24B-v4.3 (2026-11-03)

Measured on Wheat, round 49 piece 2 (download job 387515, compare job 387517, sweep 387524; the pull carries the
measurements and the sweep record and no job log). Modified revision `b46e1fd1` (created 2025-12-20 17:47Z, the
weights uploaded at 17:49Z, the card edited on 12-21), parent pinned at `5e5b5e15` of 2025-12-17, TheDrummer's
Magidonia 24B v4.3, a fine-tune whose `base_model` field names mistralai/Magistral-Small-2509 (40 layers, hidden
size 5,120). The card is Heretic v1.1.0's per-layer kernel table: `direction_index` "per layer", `attn.o_proj` with
a maximum weight of 0.89 at position 30.54 falling to 0.69 at a distance of 4.37, `mlp.down_proj` with a maximum of
1.01 at 23.69 falling to 0.98 at a distance of 11.82, a KL divergence of 0.0485 and 5 refusals in 100 against 73.
The parent counts as neither an original nor a copy (finding 117). The maker's four Cydonia edits, the other
Mistral Small fine-tunes of the same parent maker, are in round 44, which is still on the cluster.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 18 flags (first shares 0.981 to
0.988 under the 0.99 floor on the eight attention outputs and ten down projections), on the cluster and after
re-scoring at home. On reading, the copy is the card's two kernels, one direction per layer on both writers, read to
the third decimal.

- 32 of 363 tensors changed: the down projections of layers 12 to 35 and the attention outputs of layers 27 to 34,
  the two kernels' reaches to the layer (11.87 to 35.51 and 26.17 to 34.91). Everything else is exactly 0, and the
  copy's first three shards and its tenth are the parent's by object id.
- One direction per layer: the two writers of a layer agree at 0.99998 at the median, the layers at 0.56.
- Output side on all 32: one minus the left kept fraction reads 0.977 to 1.013 on the down projections and 0.725 to
  0.865 on the attention outputs; the printed kernels give the same weights within 0.0036 on all 24 down projections
  and within 0.0050 on all 8 attention outputs, the attention outputs every one a little under the kernel. The right
  side keeps 0.39 to 0.92.
- First shares 0.981 to 0.996; relative changes 0.0107 to 0.0260; rows moved 0.0101 to 0.0705 under a card that
  claims no norm.

| Layer | Kind | Change | E1 | Left kept | Right kept | Weight read | Kernel | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 27 | attention output | 0.0131 | 0.987 | 0.28 | 0.85 | 0.725 | 0.728 | 0.0261 |
| 29 | attention output | 0.0138 | 0.988 | 0.18 | 0.87 | 0.816 | 0.820 | 0.0259 |
| 31 | attention output | 0.0140 | 0.988 | 0.14 | 0.73 | 0.865 | 0.869 | 0.0238 |
| 34 | attention output | 0.0107 | 0.981 | 0.27 | 0.84 | 0.728 | 0.732 | 0.0110 |
| 12 | down | 0.0197 | 0.994 | 0.02 | 0.69 | 0.977 | 0.980 | 0.0303 |
| 18 | down | 0.0233 | 0.995 | 0.01 | 0.91 | 0.994 | 0.996 | 0.0448 |
| 24 | down | 0.0159 | 0.991 | -0.01 | 0.70 | 1.013 | 1.009 | 0.0225 |
| 30 | down | 0.0133 | 0.987 | 0.01 | 0.39 | 0.993 | 0.994 | 0.0289 |
| 35 | down | 0.0169 | 0.992 | 0.02 | 0.90 | 0.979 | 0.981 | 0.0370 |

The full table (32 rows) is in the report.

Directions. Against the saved vectors of the Mistral Small 24B measurements the direction stands on the left at
0.645 to Pranavz's Hearthfire pass (32 names, minimum 0.551), 0.529 to the maker's Skyfall edit of this round (pair
1), 0.467 and 0.439 to grayarea's text-only and Magistral passes, 0.383 to vprilepskii's Harbinger edit (pair 4),
0.360 to SAIFIINDUSTRIES's Dolphin projection, 0.320 to venkycs's Mistral Small 24B projection, and 0.16 or less to
llmfan46's searches and huihui-ai's projection. No other measurement stands on Magidonia. By byte range the parent
stands 0.0182 from Magistral Small 2509 on the layer 5 query projection and 0.0269 on the layer 30 attention output,
with no leading component, and the copy's layer 30 attention output is a rank-one change from the parent's (first
share 0.984) while its layer 5 query projection is the parent's bytes.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the version strings move from 4.57.1 to 4.57.3. The
template (4,722 bytes, `4ad87a4f`), `tokenizer.json`, `tokenizer_config.json` and `special_tokens_map.json` are the
parent's by object id. The token ids are Mistral's through the parent (`bos_token_id` 1, `eos_token_id` 2,
`pad_token_id` 11, generation `[2]`) and the vocabulary is 131,072.

## For the recipe library

A per-layer kernel entry with a heights line would read the copy to the third decimal; the per-layer entry charges
the first shares under 0.99. grayarea's edits of Skyfall and Magidonia are pinned in round 51, so the comparison of
two tools on one checkpoint (finding 127) waits for that round. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat49/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
