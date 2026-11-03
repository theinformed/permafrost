# Reading of the Stage 1 and Stage 2 result: AlSamCur123/gemma-4-E4B-it-uncensored-continued against unsloth/gemma-4-E4B-it

Measured on Wheat, round 51 piece 6 (download job 387623, compare job 387629, sweep 387632; the pull carries the
measurements and the sweep record and no job log). Modified revision `1c0a49e9` (created 2026-07-29 02:14Z, the
weights uploaded in two commits titled "(Trained with Unsloth)" at 02:14Z and 02:17Z), parent pinned at `4e22d7e5`
of 2026-07-17, unsloth's re-upload of Gemma 4 E4B instruct, whose one weight file is google/gemma-4-E4B-it's by
object id. The card is Unsloth's 574-byte upload card ("This gemma4 model was trained 2x faster with Unsloth and
Huggingface's TRL library") and names no method, data or edit; the name says "uncensored" and "continued". The
maker published `gemma-4-E4B-ituncensored` six minutes later and "continued" and plain versions of the E2B, 26B-A4B
and 31B in the next ten days. The parent is a re-upload of a publisher's checkpoint and counts as neither an
original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `single-projection`, 343 flags (174 unexpected changes, 84 first
shares, 84 direction cosines and 1 cross-kind), on the cluster and after re-scoring at home. On reading, the copy is
training on every linear map the text decoder uses and nothing else, with no direction.

- 258 of 2,130 tensors changed: the query, attention output, gate, up and down projections of all 42 layers and the
  keys and values of layers 0 to 23. The keys and values of layers 24 to 41, which read the shared cache and are
  never used, are unchanged, as are the vision and audio towers, the token and per-layer embeddings, the per-layer
  gates and projections, the layer scalars and every normalisation vector: exactly 0 outside the changed set.
- Relative changes 0.0052 to 0.0768 (median 0.0162), largest on the gate projections (median 0.031) and smallest on
  the values (0.0075).
- No direction: the common-direction agreement is 0.13 at the median and the two writers of a layer stand at 0.44.
  First shares run 0.24 to 0.994 (medians 0.46 on the keys to 0.93 on the gates), the high ones the mark of a
  low-rank adapter, and the kept fractions along the leading directions run 0.64 to 1.38, added as often as taken
  away.
- Rows moved by up to 0.378 (the layer 35 query projection) and 0.375 (the layer 22 key projection).

| Kind | Matrices | Relative change | First share (median) |
| --- | --- | --- | --- |
| Query | 42 | 0.0065 to 0.0768 | 0.80 |
| Key | 24 | 0.0067 to 0.0209 | 0.46 |
| Value | 24 | 0.0052 to 0.0136 | 0.76 |
| Attention output | 42 | 0.0058 to 0.0253 | 0.53 |
| Gate | 42 | 0.0211 to 0.0462 | 0.93 |
| Up | 42 | 0.0082 to 0.0409 | 0.78 |
| Down | 42 | 0.0071 to 0.0334 | 0.79 |

Directions. Against the saved vectors of the forty-two measurements of the E4B the leading vectors stand at 0.042 or less
on the left to every one of them, edits and trainings alike (treadon's projection at 0.042, Dingdust's ContextPilot
pass at 0.033, the remaining forty at 0.031 or less), so no measured refusal direction leads the change.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home. The copy is an Unsloth save: its `tokenizer_config.json`
declares the 24 special tokens of the vocabulary in `added_tokens_decoder`, which the parent's file does not, its
configuration adds `bos_token_id` 2, `model_name` unsloth/gemma-4-E4B-it, `unsloth_version` 2026.7.5 and `use_cache`
false and drops `transformers_version`, and its generation file moves from 5.5.0.dev0 to 5.5.0. Its template is a
2,375-byte file (`582bb4df`) that opens with the beginning-of-sequence token and a macro that strips thought blocks,
against the parent's 18,810 bytes; no revision of the parent or of google/gemma-4-E4B-it carries it, and the fixed
conversation renders the same through both. `tokenizer.json` is 155 bytes longer than the parent's. The token ids are
the instruct checkpoint's (`eos_token_id` `[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0)
and the vocabulary is 262,144.

## For the recipe library

A training entry with a used-maps line would read the copy: every map the forward pass uses, the unused shared-cache
keys and values left alone, which an adapter trained by back-propagation leaves untouched. The direction vectors
stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat51/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
