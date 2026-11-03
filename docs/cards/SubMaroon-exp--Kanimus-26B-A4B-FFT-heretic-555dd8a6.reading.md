# Reading of the Stage 1 and Stage 2 result: SubMaroon-exp/Kanimus-26B-A4B-FFT-heretic against Vortex5/Gemma-4-26B-A4B-Animus-V14.1-FFT-heretic

Measured on Wheat, round 52 piece 6 (download job 387662, compare job 387668, sweep 387671; the pull carries the
measurements and the sweep record and no job log). Modified revision `d53b0991`, parent pinned at `e413cb2e`. The
parent is Vortex5's Heretic 1.2.0 arbitrary-rank pass "with row-norm preservation" of Darkhn's Animus V14.1 FFT
fine-tune of the 26B-A4B (window 15 to 30), unmeasured; it counts as neither an original nor a copy (finding 117).

The card describes two edits on the parent. Step 1 is task arithmetic on the query and key projections alone,
`W_out = W_animus + α · (W_opus − W_parent)`, with TeichAI/gemma-4-26B-A4B-it-Claude-Opus-Distill-v2 as the target
and unsloth/gemma-4-26B-A4B-it as its parent, α 0.50 on the sliding-window queries and keys and the full-attention
queries and 0.25 on the full-attention keys, computed in float32 and saved in bfloat16. Step 2 merges the LoRA
adapter SubMaroon/Dark-Goetia-26B-A4B-LoRA-v4 (rank 32, alpha 64, scaled so that 0.40 times BA is added) into the
four attention projections and the shared dense MLP of all 30 layers, "205 modules", with the line "Everything outside
them is the base, bit for bit." The adapter's own configuration names Naphula/Goetia-26B-A4B-v1.3-Absolute-Heretic-ARA
as its base and lists text-decoder module names as its targets.

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 29 flags (28 unexpected changes on the
queries and keys and one missing changed projection), on the cluster and after re-scoring at home. On reading, the
weights carry step 1 and nothing of step 2.

- 60 of 1,013 tensors differ from the parent, the query and key projections of all 30 layers: 28 of them over the
  threshold (the queries of layers 14 to 29 at 0.0010 to 0.0022, the keys of layers 15 to 28 at 0.0010 to 0.0016)
  and the other 32 under it at 0.00005 to 0.00081, the largest outside the changed set on the layer 14 key.
- The value projections, the attention outputs, the shared dense gate, up and down projections, the 128 experts,
  the routers, every norm, the towers and the embeddings are exactly 0: the parent's values on every one of the 145
  modules step 2 names outside the queries and keys.
- No direction: first shares 0.10 to 0.59, the kept fractions along the leading directions 0.99 to 1.01, the
  within-kind agreement 0.22 at the median; rows moved by 0.0014 or less.
- By byte range the copy is step 1 to the last bit. On the layer 20 query and key projections and the layer 5
  query projection (α 0.50) and the layer 23 key projection (α 0.25, a full-attention layer), the copy equals, on
  every entry, the bfloat16 rounding of the parent plus α times the difference between TeichAI's distillation (read
  at its head, `a0e9522e`) and unsloth's re-upload (at `60941ad6`): 0 of the 43,253,760 entries differ, 6,939,376 of
  them moved from the parent, and with α doubled 7,758,270 would differ. The distillation stands 0.0003 to 0.0026 from
  unsloth's file on those four matrices, and unsloth's file is Google's bytes on the two matrices read for both.
  Nothing of rank 32 sits on the queries and keys beside the arithmetic.
- The adapter as published (read at its head, `eb793246`) holds 115 modules, the queries, keys and attention
  outputs of all 30 layers and 25 value projections, and no MLP map, where the card counts 205 with 90 MLP maps. Its
  factors are trained: merged at the card's scale it would move 2,622,459 of the 11,534,336 entries of the layer 20
  attention output, 0.00102 of the norm, and the copy holds the parent's bytes there.

| Layer | Kind | Change | E1 | Left kept | Right kept | Rows |
| --- | --- | --- | --- | --- | --- | --- |
| 14 | query | 0.0010 | 0.348 | 1.00 | 1.00 | 0.0004 |
| 20 | query | 0.0012 | 0.261 | 1.00 | 1.00 | 0.0004 |
| 23 | query | 0.0018 | 0.506 | 1.01 | 1.00 | 0.0006 |
| 29 | query | 0.0022 | 0.589 | 0.99 | 1.00 | 0.0007 |
| 15 | key | 0.0010 | 0.103 | 1.00 | 1.00 | 0.0003 |
| 28 | key | 0.0016 | 0.397 | 1.00 | 1.00 | 0.0010 |

The full table (28 rows) is in the report.

Directions. The queries and keys carry no direction for the saved vectors to place, and the edit the card relies on
for its refusal behaviour, the parent's, is under the measurement and unchanged by it.

## Token and configuration side (Stage 1)

"Consistent" on the cluster and at home: no compared field differs. The copy's `tokenizer_config.json` is 2,725 bytes
against the parent's 2,713, the card's patch that turns `extra_special_tokens` from a list into a mapping, and the
tool reads the two forms as the same declarations. `tokenizer.json`, the generation file, the configuration and the
template are the parent's by checksum.

## For the recipe library

A task-arithmetic entry would read the queries and keys as the card's α times a named difference, checkable by byte
range against the two named checkpoints. The second step the card describes is absent from the bfloat16 files; the
GGUF export the card also links is not measured. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat52/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
