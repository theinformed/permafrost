# Reading of the Stage 1 and Stage 2 result: igorls/gemma-4-E4B-it-qat-q4_0-unquantized-heretic against google/gemma-4-E4B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Wheat, round 35 piece 8 (download job 387143, compare job 387151, sweep 387152; the pull carries the
measurements and the sweep record and no job log). Modified revision `61f234c5` (three commits on 2026-06-07
between 12:52Z and 12:54Z: the folder, then the README), original pinned at `dfc5b925` (06-05), the QAT-unquantized
checkpoint of the E4B, shared with pair 7. The card (2,729 bytes, the maker's own) says Heretic "using
Arbitrary-Rank Ablation (LoRA) with chain-of-thought-aware evaluation": the model was ablated and scored with
thinking on, "scoring the final answer after the thought block", KL 0.055, refusals about 21 percent against 98 on
"an extreme adversarial set", and "far lower KL than single-direction abliteration". No layer window, no rank and
no weight are printed. The `base_model` field names the QAT checkpoint with `base_model_relation: finetune`. The
maker's third copy in the census after the 12B instruct edit (round 7, a linear kernel) and the 12B QAT edit with
thinking on (round 33, finding 69).

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 64 flags (32
first shares 0.652 to 0.923, 32 within-layer cosines 0.001 to 0.106), on the cluster and after re-scoring at home.
On reading, the copy is a LoRA-rank edit of both writers over sixteen layers, the largest Heretic changes the
census has read on an E4B, with a direction per matrix and the rows left where the edit put them.

- 32 of 2,076 tensors changed: the attention outputs and the down projections of layers 21 to 36. Exactly 0
  outside them, which places the copy on the QAT checkpoint (finding 48). The 32 are 16 layers of a 42-layer
  stack, one layer above pair 7's window (20 to 35) at both ends.
- Relative change 0.099 to 0.214 on the attention outputs (0.21 at layer 36, 0.20 at 25) and 0.055 to 0.095 on
  the down projections, three to four times pair 7's 0.027 to 0.061 on the same checkpoint's attention outputs.
- Several directions per matrix (first shares 0.65 to 0.92) and a direction per matrix: the two writers of a
  layer agree at 0.001 to 0.106, the layers at 0.03 (median), the groups at 0.21 and 0.25. Input side on 29 of
  32: the right kept fraction is -0.33 to -2.46 (weights 1.33 to 3.46; 2.30 to 2.48 on the attention outputs of
  24 to 26, 28, 29 and 31, 3.46 at 36) where the left keeps 0.34 to 0.96; on the attention outputs of layers 22,
  27 and 33 the right keeps 0.37 to 0.59 and the left 0.86 to 0.95, so neither side reads a weight.
- Rows moved 0.016 to 0.28 (0.20 to 0.28 on the attention outputs of 24, 25, 26 and 28) under no preservation
  claim; the card's method is the LoRA branch, which does not restore them.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Within-layer cosine | Rows |
| --- | --- | --- | --- | --- | --- |
| 21 | 0.139, 0.833, 0.87, -0.40 | 0.076, 0.784, 0.83, -0.53 | 0.021 | 0.077, 0.032 |
| 24 | 0.187, 0.908, -0.21, -1.30 | 0.072, 0.859, 0.64, -1.21 | 0.069 | 0.200, 0.036 |
| 25 | 0.200, 0.912, 0.34, -1.48 | 0.070, 0.838, 0.72, -1.05 | 0.059 | 0.279, 0.020 |
| 27 | 0.148, 0.812, 0.86, 0.59 | 0.085, 0.868, 0.72, -0.68 | 0.010 | 0.092, 0.060 |
| 29 | 0.112, 0.879, 0.92, -1.41 | 0.095, 0.908, 0.62, -1.05 | 0.023 | 0.192, 0.086 |
| 31 | 0.132, 0.816, 0.87, -1.36 | 0.085, 0.848, 0.67, -0.97 | 0.037 | 0.069, 0.049 |
| 33 | 0.126, 0.801, 0.95, 0.37 | 0.087, 0.868, 0.63, -1.05 | 0.008 | 0.075, 0.049 |
| 36 | 0.214, 0.919, 0.62, -2.46 | 0.080, 0.778, 0.62, -0.90 | 0.015 | 0.164, 0.034 |

The full table (32 rows) is in the report.

Fingerprints. The copy's four shards are `62cfc14d`, `f712d377`, `f28d903b` and `8080cb1a`. The first equals the
first shard of prithivMLmods's QAT export (round 34), the start of the QAT file that neither edit touches, and the
fourth is the vision tower that the QAT checkpoint shares with the instruct model and every E4B export in the
library's four-shard layout (findings 71 and 75); the middle two are the copy's own.

Directions. Against the saved vectors of twenty other E4B edits the copy's left vectors reach a median of 0.57 to
0.65 to the arbitrary-rank family (coder3101's instruct edit, JokeHer's, llmfan46's two, NullpoLab's, alphakek's,
pair 7's) with one matrix above 0.85 in each case, and 0.07 or less to the linear-kernel and projection edits
(prithivMLmods's QAT export, p-e-w's, sh0ck0r's, BinxNet's, huihui-ai's, DuoNeural's); on the right the medians are
0.37 or less everywhere. A search with thinking on found, in most of its window, a direction the thinking-off
searches did not, as the maker's 12B QAT search did (finding 69).

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings are all that differ. The
template is the pin's 16,804-byte file and the fixed conversation renders identically.

## For the recipe library

The directional-per-layer entry is the nearest and both of its flag kinds fire on every matrix: several
directions and no shared one. The LoRA branch, read here and on wnfldchen's 12B QAT export (round 34), wants an
entry of its own: a direction per matrix, input side, rows unrestored, the weight read as one minus the right kept
fraction where it reads at all. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat35/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
