# Reading of the Stage 1 and Stage 2 result: Hyphonical/gemma-4-E4B-it-Uncensored-MAX-opus-4.7 against prithivMLmods/gemma-4-E4B-it-Uncensored-MAX

Measured on Wheat, round 52 piece 4 (download job 387662, compare job 387666, sweep 387671; the pull carries the
measurements and the sweep record and no job log). Modified revision `af78a529`, parent pinned at `a236367a`, an
earlier revision of the repository round 7 measured at `19d2605f` against google/gemma-4-E4B-it: prithivMLmods's
re-sharded upload of huihui-ai's E4B edit, one shared direction removed from the attention outputs and down
projections of layers 7 to 41 at a weight of 2.5 (finding 9). By byte range the pinned revision carries that edit:
its layer 20 and 30 attention outputs keep -1.501 and -1.499 of Google's component along the edit's direction. The
copy carries Unsloth's upload card ("trained 2x faster with Unsloth and Huggingface's TRL library"), names the
parent in its card and field, and names no data or method; the name adds a distillation target. The parent is a
measured copy, here the community parent the card names (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `single-projection`, 379 flags (210 unexpected changes, 84 first
shares, 84 direction cosines and one cross-kind direction), on the cluster and after re-scoring at home. On reading,
the copy is training on every linear map of the text decoder, with the parent's edit kept whole under it.

- 294 of 2,130 tensors changed: the query, key, value, attention output, gate, up and down projections of all 42
  layers, at 0.0089 to 0.0769 of their norm (median 0.0206). Everything else is exactly 0: the towers, the token and
  per-layer embeddings, the per-layer input maps, the layer scalars and every norm.
- No direction: the common-direction agreement is 0.13 at the median, the within-layer agreement 0.43, first shares
  0.16 to 0.999, and the kept fractions along the leading directions are near 1 on most maps.
- The edit stays. On the layer 20 and 30 attention outputs the training is 0.0180 and 0.0125 of the norm against
  the edit's 0.0528 and 0.0504, 12.5 and 7.1 percent of the training lies along the edit's direction, and the copy
  keeps -1.495 and -1.497 of Google's component along it where the parent keeps -1.501 and -1.499.
- The keys and values of layers 24 to 41, which read the cache shared from earlier layers and take part in no
  forward pass, changed too: the keys by 0.023 to 0.043 (first shares 0.51 to 0.90) and the values by 0.041 to 0.077
  (first shares 0.76 to 0.999, above 0.99 on 15 of 18). By byte range the layer 31 and 40 values, Google's bytes in
  the parent, carry a rank-one change (first shares 0.9987 and 0.9990) at 0.075 and 0.077 of the norm, at a cosine of
  0.003 to the weight, on matrices whose own spectrum is flat (first share 0.004). AlSamCur123's adapter left the same
  projections untouched (finding 157).
- Rows moved by 0.0010 to 0.61, the largest on the layer 23 key and the layer 35 and 41 queries.

| Layer | Kind | Change | E1 | Left kept | Right kept | Rows |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | attention output | 0.0148 | 0.433 | 1.00 | 1.00 | 0.0024 |
| 30 | attention output | 0.0125 | 0.905 | 0.98 | 0.98 | 0.0127 |
| 10 | down | 0.0185 | 0.639 | 0.99 | 0.96 | 0.0023 |
| 30 | down | 0.0180 | 0.892 | 0.96 | 0.89 | 0.0025 |
| 10 | value | 0.0147 | 0.616 | 1.00 | 0.99 | 0.0029 |
| 24 | value | 0.0746 | 0.998 | 1.19 | 1.86 | 0.0207 |
| 31 | value | 0.0750 | 0.999 | 1.11 | 1.51 | 0.0233 |
| 40 | value | 0.0769 | 0.999 | 1.10 | 1.49 | 0.0241 |
| 30 | key | 0.0430 | 0.847 | 0.93 | 0.63 | 0.0081 |
| 36 | query | 0.0655 | 0.998 | 0.74 | 0.95 | 0.2089 |

The full table (294 rows) is in the report.

Directions. Against the saved vectors of every measurement on Google's E4B the leading vectors stand at 0.14 or less at the
median to every one: 0.059 to huihui-ai's edit and prithivMLmods's copy of it on the 70 names they share, 0.138 to
Himanshuoo8's duplicate of DavidAU's Unsloth fine-tune over coder3101's edit (finding 97) on 287 names. That
fine-tune moves the unused shared-cache values too, and there the two trainings meet: 0.57 to 0.81 on the values of
layers 24 to 29 and 31 to 41 (0.05 at layer 30), where their other maps stand at 0.0 to 0.5.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home; the home judgement closed 25 fields, the 24 special-token
declarations and the added-token map that repeat the shared `tokenizer.json`. What stays is an Unsloth save: the
configuration adds an `unsloth_version` field, a `model_name` naming the parent (finding 97's form) and
`pad_token_id` 0, and writes `torch_dtype` where the parent writes `dtype`; the generation file is dropped, and the
parent's stop list `[1, 106, 50]` and sampling defaults go with it; the template is written into the 19,106-byte
`tokenizer_config.json` beside a `chat_template.jinja` that is the parent's by checksum. The fixed conversation renders
the same 176 bytes.

## For the recipe library

A training entry with a used-maps line would charge the shared-cache keys and values here and clear them on finding
157's copy: the two trainings differ in whether those maps move. To the metadata tool: the dropped generation file of
an Unsloth save, with the stop list it carried. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat52/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
