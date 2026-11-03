# Reading of the Stage 1 and Stage 2 result: keithtyser/gemma-4-26B-A4B-it-local-abliterated-sota-internal-t34 against google/gemma-4-26B-A4B-it

Measured on Wheat, round 51 piece 5 (download job 387623, compare job 387628, sweep 387632; the pull carries the
measurements and the sweep record and no job log). Modified revision `38b6875c` (created 2026-05-03 00:58Z, the
weights uploaded at 01:04Z, the card edited at 01:11Z and twice more on 07-16 to add safety guidance and to redact
two local paths), original pinned at `4c55b528` of 2026-04-28, the last revision of Google's 26B-A4B instruct
checkpoint before the copy's creation. The card says the checkpoint was produced with the maker's model-forge
pipeline using Heretic as its backend, with "full row normalization, orthogonalized refusal direction, 80 trials,
24 startup trials, selected trial 34" (1 refusal in 27 at a KL divergence of 0.0183), and prints no parameter table;
the repository's `model_forge_sota_heretic.json` names the backend, the trial and a recipe file.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 24 flags (16 first shares and 8 layer
direction cosines), on the cluster and after re-scoring at home. On reading, the copy is a per-layer Heretic pass on
both dense writers of layers 12 to 29, two kernel shapes the card does not print, with no expert touched.

- 35 of 1,013 tensors changed: the attention outputs of layers 12 to 28 and the dense down projections of 12 to 29.
  The 128 experts of every layer, the routers, the queries, keys and values, the vision tower and the embedding are
  unchanged; the layer 11 down projection moved by 0.00074, the largest change outside the changed set, the tail of
  the down kernel.
- One direction per layer: the two writers of a layer agree at 0.965 at the median (0.903 at the least), the layers
  at 0.35.
- Output side on all 35. One minus the left kept fraction draws two shapes: 0.65 at layer 12 rising to 1.36 at 21
  and back to 0.99 at 28 on the attention outputs, with a dip to 0.695 at 27, and 0.12 at 12 rising to 0.80 at 20 and
  falling to 0.04 at 29 on the down projections.
- First shares 0.988 to 0.997 on the attention outputs and 0.834 to 0.993 on the down projections, the smallest
  where the weight is smallest; relative changes 0.0021 to 0.0304; rows moved 0.0034 to 0.0258 under "full row
  normalization".

| Layer | Kind | Change | E1 | Left kept | Right kept | Weight read | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | attention output | 0.0299 | 0.988 | 0.35 | 0.35 | 0.647 | 0.0199 |
| 14 | attention output | 0.0257 | 0.995 | -0.09 | 0.49 | 1.089 | 0.0200 |
| 17 | attention output | 0.0272 | 0.997 | -0.22 | 0.40 | 1.222 | 0.0227 |
| 19 | attention output | 0.0292 | 0.997 | -0.35 | 0.36 | 1.345 | 0.0142 |
| 21 | attention output | 0.0302 | 0.997 | -0.36 | 0.36 | 1.361 | 0.0133 |
| 24 | attention output | 0.0270 | 0.997 | -0.15 | 0.33 | 1.154 | 0.0092 |
| 27 | attention output | 0.0217 | 0.995 | 0.31 | 0.58 | 0.695 | 0.0058 |
| 28 | attention output | 0.0200 | 0.994 | 0.01 | 0.46 | 0.991 | 0.0057 |
| 12 | down | 0.0024 | 0.889 | 0.88 | 0.98 | 0.121 | 0.0040 |
| 15 | down | 0.0071 | 0.967 | 0.65 | 0.92 | 0.348 | 0.0113 |
| 17 | down | 0.0107 | 0.983 | 0.49 | 0.89 | 0.508 | 0.0091 |
| 20 | down | 0.0172 | 0.993 | 0.20 | 0.80 | 0.799 | 0.0115 |
| 23 | down | 0.0120 | 0.986 | 0.42 | 0.89 | 0.575 | 0.0090 |
| 26 | down | 0.0079 | 0.971 | 0.82 | 0.93 | 0.183 | 0.0039 |
| 29 | down | 0.0021 | 0.834 | 0.96 | 0.99 | 0.041 | 0.0044 |

The full table (35 rows) is in the report.

Directions. Against the saved vectors of the 26B-A4B measurements the direction stands on the left at 0.899 to
tvall43's Heretic pass (13 names), 0.893 to SevenOfNine's edit, 0.889 to sh0ck0r's and BinxNet's Heretic passes,
0.878 to TrevorJS's edit and the four copies of it (35 names), 0.859 to xdavxd's QAT pass, 0.850 to Rootkit7's
edit and 0.810 to the two DiffusionGemma passes; at 0.59 to WWTCyberLab's edit and Mitchins's QAT kernel pass; and at
0.21 or less to every arbitrary-rank search of the checkpoint and its fine-tunes (coder3101's, llmfan46's,
Vortex5's, SubMaroon's, SassyDiffusion's), to huihui-ai's projection (0.147), to OS-Software's edit of this round
(pair 8, 0.029) and to the antislop training (0.012).

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, for one field: `template.default`. The copy's template is
16,448 bytes (`98da08eb`), Google's own template of 04-10 (commits `1db3cff1` and `7d4c97e5`), where the pinned
revision carries the 16,934-byte template of the 04-28 commit; the template rule reads only commits after the pin,
so a copy built from a snapshot older than the pin reads as unexplained. The fixed conversation renders the same.
The version strings move from 5.5.0.dev0 to 5.6.2; `tokenizer.json` is 154 bytes longer than Google's. The token
ids are the instruct checkpoint's (`eos_token_id` `[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2,
`pad_token_id` 0) and the vocabulary is 262,144.

## For the recipe library

A per-layer kernel entry with a heights line and no expert would read the copy; the per-layer entry charges the
first shares of fifteen down projections and one attention output, lowest where the weight is smallest, and eight
layer cosines. To the metadata tool: the earlier-revision template line owed since round 47 would close this field. The
direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat51/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
