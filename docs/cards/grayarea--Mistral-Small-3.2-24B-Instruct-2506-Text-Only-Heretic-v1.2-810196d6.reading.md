# Reading of the Stage 1 and Stage 2 result: grayarea/Mistral-Small-3.2-24B-Instruct-2506-Text-Only-Heretic-v1.2 against anthracite-core/Mistral-Small-3.2-24B-Instruct-2506-Text-Only (2026-11-02)

Measured on Wheat, round 47 piece 3 (download job 387398, compare job 387401, sweep 387407; the pull carries the
measurements and the sweep record and no job log). Modified revision `ef3cefbf` (created 2026-03-29 22:00Z, the
folder uploaded at 22:02Z and again at 22:13Z), parent pinned at `c5ac8f3b` of 2025-06-21, anthracite-core's
text-only re-save of mistralai/Mistral-Small-3.2-24B-Instruct-2506 ("No vision encoder", `MistralForCausalLM`, 40
layers, saved by transformers 4.50.0.dev0). The card names Heretic v1.2.0 with MPOA (magnitude-preserving
orthogonal ablation), "Full row renormalization", a winsorization quantile of 0.997 and a custom prompt set, 0
refusals in 108 against 96 at a KL divergence of 0.0138, and prints no parameter table; its link for "the normal
multi-modal" edit points to the parent repository. It is the maker's second v1.2 pass in the census after the
Magistral copy of finding 31. The parent counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 26 flags (first shares 0.979 to
0.990 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is one shared
direction on both writers, a kernel shape in the kept fractions, and the rows in and under the band.

- 61 of 363 tensors changed: the down projections of layers 8 to 39 and the attention outputs of 11 to 39; the
  queries, keys, values, gate and up projections, the embedding, the head and the normalisation vectors read
  exactly 0.
- One direction for every layer and both writers: median agreement 0.999 (minimum 0.972), cross-kind 0.942, the
  two writers of a layer at 0.958 to 1.000.
- Output side: one minus the left kept fraction reads 0.69 at layer 8 rising to 1.27 at 31 and back to 1.09 at 39
  on the down projections, and 0.68 at 11 rising to 1.25 at 26 and back to 0.74 at 39 on the attention outputs
  (0.88 at 27, the one break in the shape); the right side keeps 0.07 to 0.92.
- First shares 0.979 to 0.994; relative changes 0.0102 to 0.0202; rows moved 0.0023 to 0.0078, in and under
  finding 22's band, under a card that names full row renormalization.

| Layer | Down weight | Attention output weight | Rows (down, attention output) |
| --- | --- | --- | --- |
| 8 | 0.69 | - | 0.0034, - |
| 11 | 0.76 | 0.68 | 0.0037, 0.0037 |
| 16 | 0.91 | 0.87 | 0.0034, 0.0030 |
| 21 | 1.05 | 1.06 | 0.0054, 0.0073 |
| 26 | 1.18 | 1.25 | 0.0034, 0.0059 |
| 31 | 1.27 | 1.10 | 0.0023, 0.0035 |
| 36 | 1.17 | 0.88 | 0.0050, 0.0078 |
| 39 | 1.09 | 0.74 | 0.0042, 0.0035 |

The full table (61 rows) is in the report.

Directions. Against the saved vectors of every Mistral Small 24B measurement (hidden size 5,120, 40 layers), the
direction stands on the left at 0.856 and on the right at 0.857 to the maker's Magistral Small 2509 pass (59
names, minimum 0.854), 0.628 to saukko's projection of Dolphin 3.0 R1 (the SAIFIINDUSTRIES duplicate of round 45),
0.533 to venkycs's projection of Mistral Small 24B Instruct 2501, 0.398 and 0.370 to Pranavz's Hearthfire pass
against its parent and against Mistral's checkpoint, 0.235 to huihui-ai's projection of Mistral Small 3.2 and to
nicoboss's duplicate of it, and 0.06 or less to llmfan46's three arbitrary-rank searches on Mistral Small 3.2 and
Magistral; the two calibration edits of Mistral Small 3.2 have no saved vectors at home and were not compared.
By byte range the parent's layer 20 attention output, layer 5 query projection and token embedding are byte-equal
to the language model of mistralai/Mistral-Small-3.2-24B-Instruct-2506 at `95a6d26c`, so the parent is Mistral's
checkpoint with the vision tower left out; the copy's layer 20 attention output stands 0.0180 from it, rank one
(0.9925), and its layer 5 query projection and embedding are Mistral's bytes.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, no field closing: `torch_dtype` written as `dtype` with the
same value. The version strings move from 4.50.0.dev0 to 4.57.3, and the template moved from a
`chat_template.json` to `chat_template.jinja` with the same text and renders identically. The tokenizer and the
special-token map are the parent's by object id (`4135d4bb`, `a47054b4`). The token ids are Mistral's on both sides
(`bos_token_id` 1, `eos_token_id` 2, no pad) and the vocabulary is 131,072.

## For the recipe library

The per-layer entry reads the copy with a row-normalisation line; a shared-direction entry on both writers with a
kernel line would read it whole. The pinner should record a text-only re-save whose tensors are a publisher's
language model by byte range as that checkpoint, so that the pair counts against the original. The direction
vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat47/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
