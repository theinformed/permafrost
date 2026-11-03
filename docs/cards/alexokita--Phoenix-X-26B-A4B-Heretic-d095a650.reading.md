# Reading of the Stage 1 and Stage 2 result: alexokita/Phoenix-X-26B-A4B-Heretic against Vortex5/Phoenix-X-26B-A4B

Measured on Wheat, round 52 piece 3 (download job 387662, compare job 387665, sweep 387671; the pull carries the
measurements and the sweep record and no job log). Modified revision `e526f302`, parent pinned at `2ef31dd8`, the
merge's revision three days before the copy. The parent publishes its merge configuration: a `phantom` merge over
google/gemma-4-26B-A4B-it of Gryphe's Pantheon-Reasoning 1.1, Darkhn's Animus V14.1 FFT, Vortex5's own
Moonlight-Dusk merge, zerofata's MeroMero and electroglyph's fiction fine-tune (whose own field names TrevorJS's
26B-A4B edit), computed in float32 and saved in bfloat16. The card prints no parameter table: a Heretic run of 200
trials, the merge exported from Pareto trial 58, 21 refusals in 100 against 97, a KL divergence of 0.0225. The parent
counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 7 flags (six within-layer cosines of
0.894 to 0.936 at layers 15, 16 and 19 and one first share of 0.989 at the layer 12 down projection), on the cluster
and after re-scoring at home. On reading, the copy is a per-layer pass on both dense writers, with no expert touched.

- 37 of 1,013 tensors changed: the dense down projections of layers 8 to 29 and the attention outputs of layers 15
  to 29. The 128 experts, the routers, every reader, the towers and the embeddings are exactly 0.
- One direction per layer: the two writers of a layer agree at 0.965 at the median, least at the three flagged
  layers, and the layers at 0.64.
- Output side on all 37. One minus the left kept fraction reads 0.44 to 1.10 on the down projections and 0.39 to
  1.30 on the attention outputs. The weights rise across the window without following one smooth kernel: they dip
  to 0.564, 0.717 and 0.436 at the down projections of layers 9, 16 and 26 and to 0.705, 0.682 and 0.385 on the
  attention outputs of layers 15, 16 and 19, the last three where the two writers of the layer agree least. The
  three full-attention layers in the window (17, 23 and 29, with 8,192 inputs) read 1.14, 1.12 and 1.10.
- First shares 0.989 to 0.997; relative changes 0.0138 to 0.0348; rows moved 0.0037 to 0.0255 under a card that
  names no norm.

| Layer | Kind | Change | E1 | Left kept | Right kept | Weight read | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | attention output | 0.0227 | 0.993 | 0.30 | 0.65 | 0.705 | 0.0235 |
| 17 | attention output | 0.0205 | 0.994 | -0.14 | 0.58 | 1.140 | 0.0163 |
| 19 | attention output | 0.0248 | 0.995 | 0.61 | 0.55 | 0.385 | 0.0151 |
| 21 | attention output | 0.0253 | 0.996 | -0.30 | 0.49 | 1.295 | 0.0118 |
| 26 | attention output | 0.0221 | 0.995 | -0.25 | 0.51 | 1.254 | 0.0037 |
| 29 | attention output | 0.0211 | 0.994 | -0.09 | 0.69 | 1.095 | 0.0078 |
| 8 | down | 0.0138 | 0.992 | 0.10 | 0.87 | 0.900 | 0.0130 |
| 9 | down | 0.0170 | 0.992 | 0.44 | 0.88 | 0.564 | 0.0232 |
| 16 | down | 0.0176 | 0.993 | 0.28 | 0.83 | 0.717 | 0.0130 |
| 21 | down | 0.0206 | 0.994 | -0.10 | 0.79 | 1.104 | 0.0131 |
| 26 | down | 0.0204 | 0.995 | 0.56 | 0.74 | 0.436 | 0.0057 |
| 29 | down | 0.0348 | 0.997 | 0.19 | 0.86 | 0.806 | 0.0248 |

The full table (37 rows) is in the report.

Directions. Against the saved vectors of the 26B-A4B measurements the direction stands on the left at 0.863 to
0.871 to the per-layer Heretic passes of Google's checkpoint (BinxNet's, sh0ck0r's, tvall43's and SevenOfNine's),
0.851 to xdavxd's QAT pass, 0.844 to TrevorJS's edit and its four copies, 0.81 to keithtyser's pipeline pass and
Rootkit7's edit, 0.67 to WWTCyberLab's and 0.61 to Mitchins's; at 0.27 or less to every arbitrary-rank search,
Vortex5's two searches of its own merges among them (0.267 and 0.244), to coder3101's shared-direction pass (0.181),
to huihui-ai's projection (0.139) and to OS-Software's CyberStag edit (0.024). On the right the order is the same,
0.73 to 0.79 to the per-layer family.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, in two fields. The copy adds a generation file the merge does
not publish (`bos_token_id` 2, `eos_token_id` `[1, 106]`, `pad_token_id` 0), the instruct checkpoint's ids, and its
configuration adds `text_config.per_layer_config`, the transformers 5.15.0 form that declares a head dimension of 512
and two key-value heads on the full-attention layers 5, 11, 17, 23 and 29. The version string moves from 5.5.3 to
5.15.0. The template (18,683 bytes) and `tokenizer.json` are the parent's by checksum, and the fixed conversation
renders the same.

## For the recipe library

A per-layer entry with no expert and two free kernel shapes would read this copy with the three disagreeing layers
flagged. To the metadata tool: an added generation file that carries the instruct checkpoint's ids over a merge that
publishes none, and the 5.15.0 per-layer configuration read as a save form. The direction vectors stay in the pull
copy at `/opt/ai/hpc-packages/pulls/model-audit/wheat52/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
