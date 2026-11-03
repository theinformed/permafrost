# Reading of the Stage 1 and Stage 2 result: coder3101/Skyfall-31B-v4.2-heretic against TheDrummer/Skyfall-31B-v4.2 (2026-11-03)

Measured on Wheat, round 49 piece 1 (download job 387515, compare job 387516, sweep 387524; the pull carries the
measurements and the sweep record and no job log). Modified revision `a9368324` (created 2026-06-02 09:02Z, the
weights uploaded at 09:06Z, the card edited at 12:30Z), parent pinned at `e36a890b` of 2026-04-03, TheDrummer's
Skyfall 31B v4.2, whose weights went up on 02-13 and whose `base_model` field names mistralai/Magistral-Small-2509.
Skyfall is a depth-upscaled Magistral Small: 54 layers against Magistral's 40, hidden size 5,120. The card is
Heretic v1.2.0's kernel table with a fractional `direction_index` of 21.36 (one interpolated direction for every
layer): `attn.o_proj` with a maximum weight of 1.48 at position 36.76 and a minimum of 1.48 at a distance of
27.61, `mlp.down_proj` with a maximum of 0.99 at 38.21 falling to 0.46 at a distance of 30.90, a KL divergence of
0.0050 and 6 refusals in 100 against 89. The parent counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 47 flags (46 first shares of 0.959 to
0.990 under the 0.99 floor and one cross-kind cosine), on the cluster and after re-scoring at home. On reading, the
copy is one shared direction on both writers over the two kernels' reaches, with the printed heights read only on
the layers the upscale inserted.

- 90 of 489 tensors changed: the down projections of layers 8 to 53 and the attention outputs of layers 10 to 53,
  the two kernels' reaches to the layer (7.31 to 69.11 and 9.15 to 64.37, cut at the last layer). Everything else is
  exactly 0.
- One direction for every layer and both writers: agreement 0.997 at the median (0.960 at the least), the two
  writers of a layer at 0.995, cross-kind 0.933.
- Output side on all 90: one minus the left kept fraction reads 0.45 to 0.98 on the down projections and 0.64 to
  1.49 on the attention outputs; the right side keeps 0.39 to 0.90.
- First shares 0.959 to 0.996; relative changes 0.0070 to 0.0271; rows moved 0.0022 to 0.0168 under a card that
  claims no norm.

The parent's own layers say where the kernel reads exactly. Fourteen of Skyfall's layers (28 and 29, 31 and 32, 34
and 35, 37 and 38, 40 and 41, 43 and 44, 46 and 47) carry attention outputs of norm 0.23 to 0.41 and down
projections of norm 1.07 to 1.15, against 9.9 to 20.6 and 36.8 to 47.3 on the other forty. By byte range the
forty others stand on Magistral Small's forty layers in order (Skyfall's layer 5 query projection 0.0153 from
Magistral's layer 5, and layers 30, 33, 48 and 53 0.019 to 0.024 from Magistral's 28, 29, 34 and 39), and each
inserted pair copies the inputs of the layer before it (the layer 28 query projection 0.036 from Magistral's layer
27, the layer 28 and 29 query projections 0.0035 apart). On the fourteen inserted attention outputs the weight reads the card's flat 1.48 within 0.011
(1.473 to 1.491); on the thirty others it reads 0.64 to 1.35. On the down projections it reads the kernel's shape
everywhere and falls below its height by 0.0065 to 0.0123 on the inserted layers and by up to 0.112 on the others.

| Layer | Kind | Change | E1 | Left kept | Right kept | Weight read | Kernel | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | attention output | 0.0220 | 0.995 | -0.13 | 0.62 | 1.132 | 1.480 | 0.0050 |
| 27 | attention output | 0.0236 | 0.995 | 0.16 | 0.66 | 0.836 | 1.480 | 0.0061 |
| 28 | attention output | 0.0242 | 0.995 | -0.49 | 0.90 | 1.491 | 1.480 | 0.0162 |
| 29 | attention output | 0.0242 | 0.995 | -0.49 | 0.90 | 1.489 | 1.480 | 0.0168 |
| 30 | attention output | 0.0203 | 0.994 | -0.06 | 0.70 | 1.058 | 1.480 | 0.0071 |
| 40 | attention output | 0.0230 | 0.995 | -0.47 | 0.84 | 1.474 | 1.480 | 0.0077 |
| 53 | attention output | 0.0225 | 0.995 | -0.28 | 0.82 | 1.278 | 1.480 | 0.0102 |
| 8 | down | 0.0070 | 0.959 | 0.54 | 0.71 | 0.457 | 0.472 | 0.0030 |
| 20 | down | 0.0109 | 0.981 | 0.35 | 0.72 | 0.653 | 0.678 | 0.0064 |
| 28 | down | 0.0127 | 0.986 | 0.20 | 0.61 | 0.803 | 0.815 | 0.0057 |
| 38 | down | 0.0152 | 0.990 | 0.02 | 0.51 | 0.977 | 0.986 | 0.0059 |
| 53 | down | 0.0106 | 0.980 | 0.29 | 0.77 | 0.707 | 0.736 | 0.0043 |

The full table (90 rows) is in the report.

Directions. Against the saved vectors of the Mistral Small 24B measurements, matched by layer number (which past
layer 27 pairs Skyfall's layers with shallower ones; both directions compared first are shared across layers, and
on layers 0 to 27 alone the numbers move by 0.003), the direction stands at 0.817 to grayarea's text-only pass of
Mistral Small 3.2 (61 names, minimum 0.783) and 0.792 to the same maker's Magistral Small 2509 pass (60 names), the
two shared-direction passes of finding 137, then 0.586 to vprilepskii's Harbinger edit of this round (pair 4), 0.544
to SAIFIINDUSTRIES's Dolphin projection, 0.529 to the maker's Magidonia edit of this round (pair 2), 0.511 to
venkycs's Mistral Small 24B projection, 0.509 and 0.451 to Pranavz's Hearthfire pass, 0.190 to huihui-ai's Mistral
Small 3.2 projection and 0.10 or less to llmfan46's three searches and the PaintedFantasy search of this round. The
census holds no other measurement on Skyfall, and the maker's measured edits in `results/` are Gemma 4 searches,
which share no hidden size with it. By byte range the layer 40 and 39 attention outputs change by rank-one
differences (first shares 0.995 and 0.994) whose left vectors stand at 0.992 to each other.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the version strings in the configuration and the
generation file move from 5.0.0 to 5.5.0. The template (`chat_template.jinja`, 4,725 bytes, `685eca2d`),
`tokenizer.json` (`bc81a4cb`) and `tokenizer_config.json` are the parent's by object id. The token ids are
Mistral's through the parent (`bos_token_id` 1, `eos_token_id` 2, `pad_token_id` 11, generation `[2]`) and the
vocabulary is 131,072.

## For the recipe library

A shared-direction kernel entry with a heights line would read the copy and would mark where the heights fall short;
the per-layer and single-projection entries charge the first shares under 0.99. The direction vectors stay in the
pull copy at `/opt/ai/hpc-packages/pulls/model-audit/wheat49/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
