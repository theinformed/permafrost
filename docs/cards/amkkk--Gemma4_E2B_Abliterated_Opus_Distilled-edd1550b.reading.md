# Reading of the Stage 1 and Stage 2 result: amkkk/Gemma4_E2B_Abliterated_Opus_Distilled against amkkk/Gemma4_E2B_Abliterated_Baked_HF_Ready

Measured on Wheat, round 52 piece 7 (download job 387662, compare job 387669, sweep 387671; the pull carries the
measurements and the sweep record and no job log). Modified revision `68ffc4a5`, parent pinned at `9cea12fb`, the
revision of the maker's baked edit measured in round 32 against google/gemma-4-E2B-it (finding 47): an input-side
projection on the attention output, down, gate and up projections of 24 listed layers, with the 60 unused
shared-cache tensors of layers 15 to 34 dropped. The copy's field names Google's checkpoint and the baked edit, and
its card calls it the step-two distillation branch on the step-one baked edit: a LoRA adapter trained for one epoch
on 928 tokenised examples drawn from three reasoning sets, rank 16, alpha 32, a learning rate of 0.0001, merged into
bfloat16 weights, with `target_modules` `down_proj.linear, gate_proj.linear, k_proj.linear, o_proj.linear,
per_layer_input_gate, per_layer_projection, q_proj.linear, up_proj.linear, v_proj.linear` and 7,708,672 trainable
parameters. The parent is a measured copy, and here it is the community parent the card names (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 71 flags (70 unexpected changes and one
missing changed projection), on the cluster and after re-scoring at home. On reading, the copy is training on the
per-layer input maps alone, and the edit under it is the parent's to the bit.

- 70 of 1,951 tensors changed: the per-layer input gate and the per-layer projection of all 35 layers, at 0.0052 to
  0.2331 of their norm (0.233 on the layer 0 gate, 0.138 on the layer 14 gate, 0.068 or less on the other 68).
  Everything else is exactly 0, the 96 matrices of the baked edit, every attention and MLP map of the text decoder,
  the embeddings, the norms and both towers included.
- The card's target list, read as module names, explains the set. The `.linear` names belong to the wrapped
  projections of the vision tower (16 layers, seven maps each) and the audio tower (12 layers, the query, key and
  value maps); the text decoder names its projections without the wrapper, so the only text-decoder modules the
  list names are the 70 per-layer maps. Rank 16 on those 218 modules gives 7,708,672 parameters, the card's count
  exactly. The 148 tower adapters merged as nothing: a LoRA adapter starts with one factor at zero, and a module
  that text-only examples never run receives no gradient to move it.
- Training, with no direction: first shares 0.33 to 0.98, the leading directions agree at 0.16 and 0.22 within the
  two kinds, the kept fractions along them 0.89 to 1.04 on the left. Rows moved by up to 1.29 on the layer 15
  projection, a row of near-zero norm, and 0.25 or less elsewhere.

| Layer | Kind | Change | E1 | Left kept | Right kept | Rows |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | per-layer input gate | 0.2331 | 0.818 | 0.89 | 0.46 | 0.1358 |
| 0 | per-layer projection | 0.0052 | 0.365 | 0.99 | 0.99 | 0.0029 |
| 13 | per-layer input gate | 0.0450 | 0.476 | 0.99 | 0.96 | 0.0154 |
| 14 | per-layer input gate | 0.1378 | 0.654 | 0.95 | 0.69 | 0.0388 |
| 15 | per-layer projection | 0.0243 | 0.688 | 1.01 | 1.00 | 1.2936 |
| 20 | per-layer input gate | 0.0096 | 0.686 | 1.00 | 0.99 | 0.0008 |
| 33 | per-layer projection | 0.0135 | 0.981 | 0.97 | 0.99 | 0.0063 |
| 34 | per-layer input gate | 0.0675 | 0.526 | 1.04 | 1.13 | 0.2475 |

The full table (70 rows) is in the report.

Directions. No other measurement of the E2B saves vectors for the per-layer input maps, so there is nothing to place
them against; the parent's edit directions are unchanged under the training.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the generation file's version string moves from
5.5.0.dev0 to 5.5.3. `tokenizer_config.json` (2,807 bytes against 2,095) and the template (16,660 bytes against
16,317) differ from the parent's files with no compared field changed, and the fixed conversation renders the same;
`tokenizer.json` is the parent's by checksum.

## For the recipe library

A training entry with a used-maps line would read the 70 maps as an adapter's reach and the towers as untrained. A
card's adapter target list can be checked against the checkpoint's module names before a download, and here it
predicts the changed set and the parameter count exactly. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat52/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
