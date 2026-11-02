# Reading of the Stage 1 and Stage 2 result: bgg1996/Melinoe-Gemma4-31B-VL-heretic against bgg1996/Melinoe-Gemma4-31B-VL (2026-11-02)

Measured on Nautilus, round 42 piece 1 (download job 4171128, compare job 4171129, sweep 4171137; the pull carries
the measurements and the sweep record and no job log). Modified revision `ac6bff06` (created 2026-07-11 15:51Z, the
weights, the tokenizer, the card and a `reproduce/` folder uploaded within the next minute, the card revised at
18:06Z), parent pinned at `26acdef2` of 06-02, the maker's own fine-tune of google/gemma-4-31B-it (created 05-30,
its thirteen shards uploaded 06-01, "fine-tuned for engaging in empathetic, intellectually stimulating, and deeply
personal conversations"). The card is Heretic 1.4.0's table: `direction_index` "per layer", `attn.o_proj` at a
maximum of 1.45 at position 51.65 and a minimum of 0.93 at a distance of 28.98, `mlp.down_proj` at 1.22 at 43.01
and 1.11 at 5.21, a KL divergence of 0.0306 and 15 refusals in 100 against 100. The record under `reproduce/`
names the parent at `26acdef2`, mlabonne's `harmless_alpaca` and `harmful_behaviors` at `train[:400]` for the
directions and `test[:100]` for the evaluation, the system prompt "You are a helpful assistant.",
`orthogonalize_direction` true, `row_normalization` "full" at a LoRA rank of 3, trial 155 of 200, Heretic 1.4.0
from PyPI, PyTorch 2.13.0 and one RTX PRO 6000 Blackwell with 95 GB, the same settings ImanolSuarez's 1.3.0 record
carried (finding 114). This is the first second-generation pair in the census: the copy is measured against the
fine-tune its card names and not against Google, so the pair reads the edit alone and the fine-tune's own
distance from Google is read by byte range below.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 2 flags (first shares 0.98996 and
0.98999 at layers 26 and 30 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the
copy is one direction per layer projected on the output side from the attention outputs of layers 23 to 59 and
the down projections of 38 to 48, the card's two kernels to the layer at both ends, with the down kernel's shape
and the attention kernel's peak in the kept fractions.

- 48 of 1,188 tensors changed: the attention outputs of layers 23 to 59 (37) and the down projections of 38 to 48
  (11). Nothing else moved; the largest relative change outside the changed set is exactly 0 on all 1,140 other
  tensors, the parent's fine-tuned layers 0 to 22 included.
- The windows are the card's: 51.65 less 28.98 gives 22.67 and the attention edits open at 23; 43.01 less 5.21
  gives 37.80 and 43.01 plus 5.21 gives 48.22, and the down edits run 38 to 48; the attention kernel's far end
  (80.63) lies past the stack's last layer, 59, where the window ends.
- Rank one on every matrix (first shares 0.990 to 0.995) and one direction per layer: the two writers of a layer
  at 0.993 to 0.998 where both are edited.
- Output side on all 48. One minus the left kept fraction on the attention outputs is 0.31 at layer 23, 0.3 to
  0.5 to layer 32, 0.7 to 1.2 from 33 to 50, 1.41 at 51 and 53 and 1.19 at 59, with 0.18 at 28, 0.82 at 40, 0.98
  at 47 and 0.60 at 52 off the rise; on the down projections 1.03 at 38 rising to 1.21 at 43 and falling to 1.10
  at 48. The card prints 1.45 at 51.65 and 1.22 at 43.01: the down kernel to the second decimal at its peak and
  within 0.08 at its ends (1.03 and 1.10 under 1.11), the attention kernel within 0.04 at its peak and 0.62 under
  at its lower end (0.31 under 0.93). Relative changes 0.0146 to 0.0227.
- Rows moved 0.0016 to 0.0077 on all 48 under the record's full row normalisation at rank 3, the third reading of
  that setting (0.0039 to 0.0112 on ImanolSuarez's, finding 114), and not the exact restoration of a norm-preserving
  projection (finding 74).

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 23 | 0.0157, 0.992, 0.69, 0.59 | 0.31 | - | - | 0.0032, - |
| 28 | 0.0156, 0.991, 0.82, 0.55 | 0.18 | - | - | 0.0052, - |
| 33 | 0.0195, 0.993, 0.30, 0.54 | 0.70 | - | - | 0.0044, - |
| 38 | 0.0182, 0.993, -0.03, 0.49 | 1.03 | 0.0172, 0.993, -0.03, 0.37 | 1.03 | 0.0057, 0.0035 |
| 43 | 0.0176, 0.993, -0.10, 0.29 | 1.10 | 0.0171, 0.992, -0.21, 0.08 | 1.21 | 0.0023, 0.0016 |
| 48 | 0.0195, 0.994, -0.23, 0.19 | 1.23 | 0.0157, 0.991, -0.10, 0.17 | 1.10 | 0.0022, 0.0019 |
| 51 | 0.0210, 0.995, -0.41, 0.37 | 1.41 | - | - | 0.0038, - |
| 52 | 0.0215, 0.994, 0.40, 0.64 | 0.60 | - | - | 0.0032, - |
| 53 | 0.0196, 0.994, -0.41, 0.09 | 1.41 | - | - | 0.0017, - |
| 59 | 0.0195, 0.993, -0.19, 0.49 | 1.19 | - | - | 0.0077, - |

The full table (48 rows) is in the report.

Directions. Against thirty saved vectors of other measurements of the 31B, the Google-rooted family standing in
for the parent, the directions stand at 0.920 on the left and 0.922 on the right to Vampelium's per-layer pass on
all 36 shared names (minimum 0.558), 0.919 to callmegrr's (12), germlag's (42) and 3MPER0RR's (30), the four
passes of finding 105 that stand at 1.000 to each other, at 0.888 to ressl's (48), 0.874 to TrevorJS's (48), 0.84
to Sabomako's 31B on its 4 names, 0.81 to jcxu97's duplicate and nguyenthilaitrieulong's, 0.79 to wangzhang's
head, 0.49 to null-space's, 0.40 to sh0ck0r's two measurements, 0.37 to DuoNeural's, 0.25 to 0.26 to huihui-ai's
two edits and their re-uploads, 0.24 to Kooten's, 0.21 to Bahushruth's, 0.20 to Jim-darby's search, 0.19 or less
to the other arbitrary-rank searches, 0.131 and 0.145 to llmfan46's two 31B edits of this round, and 0.009 to
cosmicoptima's. By byte range the layer 44 attention output is 0.0181 from the parent's, 0.0201 from Google's,
0.0130 from Vampelium's and 0.0133 from germlag's (the parent 0.0087 from Google's; Vampelium's and germlag's
0.0068 apart, 0.0130 and 0.0194 from Google's), the layer 44 down projection 0.0168 from the parent's and 0.0183
from Google's (the parent 0.0072 from Google's), and the layer 10 query projection byte-equal to the parent's and
0.0094 from Google's, the fine-tune's own change on a matrix the kernels do not reach. The first five shards
(`39cd04b3`, `d4c37918`, `3488cce8`, `bb0e0090`, `16ee2995`) are byte-equal to the parent's, the layers below 23;
the other eight match no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on `text_config.moe_intermediate_size`, "consistent with re-save noted"
at home: the home judgement under transformers 5.22.1 closed the field (absent on one side, the same default),
leaving the version strings (5.5.0.dev0 to 5.13.1 in the configuration and the generation file). The tokenizer,
the token ids (`eos_token_id` `[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0), the
generation settings and the template are the parent's.

## For the recipe library

The per-layer entry with selection reads the copy on 2 of 48 matrices under its first-share floor; a floor at
0.98 would read it as its card, and no rule reads the attention kernel's lower end at 0.31 under a printed 0.93.
The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus42/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
