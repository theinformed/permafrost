# Reading of the Stage 1 and Stage 2 result: Tetratype/Gemma-4-26B-A4B-it-heretic-antislop against coder3101/gemma-4-26B-A4B-it-heretic (2026-11-03)

Measured on Wheat, round 49 piece 6 (download job 387515, compare job 387521, sweep 387524; the pull carries the
measurements and the sweep record and no job log). Modified revision `5a9793e1` (created 2026-05-26 20:39Z, the
weights uploaded in one commit at 22:11Z, the card edited on 05-29), parent pinned at `e6d09d5c` of 2026-04-14,
coder3101's arbitrary-rank Heretic 1.2.0 edit of google/gemma-4-26B-A4B-it, which the census measured against Google
at this revision (`results/weights/coder3101-gemma-4-26B-A4B-it-heretic.json`, the attention outputs of layers 10 to
29, no expert). The card is 221 bytes, naming coder3101/gemma-4-26B-A4B-it-heretic as the model and Sam Paech's
auto-antislop, with its repository link, as the fine-tuning. The configuration carries `unsloth_version` 2026.5.8 and
`model_name` coder3101/gemma-4-26B-A4B-it-heretic. The parent is a copy the census already counts, measured against
its own parent, so this pair adds a measurement and a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 46 flags (16 first shares, 15 layer
direction cosines and 15 unexpected changes), on the cluster and after re-scoring at home. On reading, the copy is
training on the last five layers and the tied embedding, saved in float16, with no direction and coder3101's edit
left where it was.

- 31 of 1,013 tensors changed: in each of layers 25 to 29 the attention output, the dense gate, up and down
  projections and the packed gate-up and down tensors of the 128 experts, and the token embedding. The query, key and
  value projections of those layers and every tensor of layers 0 to 24 and of the vision tower moved by the float16
  recast alone (0.00000024 at most, the largest relative change outside the changed set); the normalisation vectors
  read exactly 0.
- No direction: first shares 0.014 to 0.053 on the expert tensors and 0.51 to 0.94 on the dense ones, both kept
  fractions 0.985 to 1.005 on every layer matrix.
- Relative changes 0.0025 to 0.0085 on the layers (median 0.0030); rows moved 0.0002 to 0.0037.
- The embedding moved by 0.0129 with a first share of 0.922 and kept fractions above 1 (1.004 on the left, 1.145 on
  the right): something added, not removed. By byte range every one of its 262,144 rows moved by more than 0.0001,
  261,682 by more than 0.001, 113,777 by more than 0.01 and six by more than 0.1 (the largest 0.132), and the
  leading component is one vector of the hidden size added to nearly every row (the leading right vector at 0.9997
  to the mean row change). The configuration ties the embedding to the output head, so the training's change to one
  is its change to the other.

| Kind | Matrices | Relative change | First share |
| --- | --- | --- | --- |
| Attention output | 5 | 0.0025 to 0.0038 | 0.721 to 0.849 |
| Gate projection | 5 | 0.0029 to 0.0038 | 0.627 to 0.776 |
| Up projection | 5 | 0.0027 to 0.0041 | 0.642 to 0.843 |
| Down projection | 5 | 0.0028 to 0.0085 | 0.506 to 0.942 |
| Expert gate-up | 5 | 0.0025 to 0.0028 | 0.014 to 0.023 |
| Expert down | 5 | 0.0028 to 0.0032 | 0.027 to 0.053 |
| Token embedding | 1 | 0.0129 | 0.922 |

The edit under it. The training and coder3101's edit meet on the attention outputs of layers 25 to 29. By byte range
against Google's checkpoint at `47b6801b`, the edit stands 0.0123 to 0.0162 from Google's there (first shares 0.913
to 0.959); the training moves those matrices by 0.0025 to 0.0038, a fifth to a quarter of the edit's size, by
-0.00015 to -0.00003 of the edit along the edit, with its leading directions at 0.002 to 0.039 to the edit's; and the
copy's difference from Google's stands at 1.0000 to the edit's leading direction on all five. On the layer 20
attention output, inside the edit and outside the training, the copy is coder3101's matrix to the float16 rounding.
The saved vectors say the same before the bytes: the training's leading vectors stand at 0.027 or less to every
26B-A4B measurement that shares its names and at 0.009 to coder3101's edit on the five shared attention outputs.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, thirteen fields, the version strings (5.5.0.dev0 to 5.5.0) the
two explained. The rest is Unsloth's save: the configuration's `eos_token_id` goes from `[1, 106]` to 1 and its
generation list from `[1, 106, 50]` to `[1, 1, 106, 50]`, `bos_token_id` 2 and `pad_token_id` 0 are written at the
top of the configuration, `dtype` goes from bfloat16 to float16, `use_cache` is turned off, and `unsloth_version` and
`model_name` are added. The tokenizer's end of sequence stays `<eos>` (1), so this is a different move from finding
98's, which put `<turn|>` (106) alone in the configuration: the generation list still stops on 106. The template
(16,433 bytes, `1db0e6d4`) and `tokenizer.json` are the parent's by object id; `tokenizer_config.json` is rewritten
with `padding_side` right, and the parent's `preprocessor_config.json` is dropped. The vocabulary is 262,144.

## For the recipe library

No entry reads training; a training entry with an edit-kept line, the line round 47 asked for, would read the copy
as its card says. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat49/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
