# Reading of the Stage 1 and Stage 2 result: 3MPER0RR/Mistral-7B-v0.3-3MPER0RR-abliterated against mistralai/Mistral-7B-v0.3 (2026-10-30)

Measured on Blueback, round 7 piece 4 (round card 5291, compare jobs 3392878 to 3392885, 4 to 6 minutes each, exit 0;
pulled home by card 5302). Modified revision `2f2f0b9a` (2026-10-27, a README commit; the weights were uploaded on
2026-09-07), original pinned at `caa1feb0` (2025-07-24). The card is five lines: "Experimental modified / abliterated
versions", model Mistral-7B-v0.3, "Trials: [200]", original model Mistral-7B-v0.3. The stated original is the base
model, and its `base_model` field says the same.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 243 flags, on the cluster and after
re-scoring at home: 161 unexpected changes, 65 energy shares, 16 direction cosines and one cross-kind direction. On
reading, the measured change is two edits laid on each other, and the stated original does not fit the first of them.

- 226 of 291 tensors changed: every query, key, value, output, gate, up and down projection in all 32 layers (224
  matrices), the token embedding (0.021 of its norm) and the output head (0.017). Only the 65 normalisation vectors
  are unchanged, and the largest of those differs by 0.00018.
- The reading-side matrices (query, key, value, gate, up) carry a dense change: relative change 0.008 to 0.027,
  first-value energy share 0.01 to 0.24 and eight values together 0.04 to 0.67, leading directions unrelated across
  layers (cosine 0.03 to 0.24), and along each leading direction the copy keeps 0.94 to 1.11 of the original's action.
  Nothing was removed along any direction. The same holds for the embedding (first share 0.005, 44 percent of entries
  up and 44 percent down) and the output head (first share 0.14). That is the shape of training, in every matrix of
  the model, at about 2 percent of each matrix's norm.
- The writers carry a directional ablation on top of it. In 25 of the 32 attention outputs (layers 6 to 30) and 23 of
  the 32 down projections (layers 9 to 31) the leading direction agrees across layers at cosine 0.95 or better (0.998
  and 0.996 in the middle). Along that direction the copy keeps -0.35 to -0.01 of the original's action on the
  attention outputs, a projection weight of 1.01 to 1.35, and on the down projections the weight follows a smooth
  kernel over the layers: 0.11 at layer 9, rising through 0.52 at layer 14 and 1.02 at layer 20 to 1.32 at layer 24,
  then falling to 0.74 at layer 31. That kernel is the shape of Heretic's per-component weight schedule, and "Trials:
  200" is that tool's default number of trials.
- The dense change is what Mistral-7B-Instruct-v0.3 differs from the base by. The copy's `chat_template.jinja`
  (3,959 bytes) equals the instruct repository's template at `c170c708` byte for byte; the base repository has no
  chat template; base and instruct share the same `config.json` and `tokenizer.json` checksums (`affafc64`,
  `e553af6f`), so the template is the one small file that tells them apart, and the copy carries the instruct one.
  Together the weights and the template fit an abliteration of Mistral-7B-Instruct-v0.3, or of another dense
  fine-tune of the base, compared here against the base the card names. The direct test is one more comparison,
  this copy against the instruct model's weights (29 GB), which would leave only the directional edit.

## Token and configuration side (Stage 1)

The tool's Stage 1 assessment is "unexplained differences" in 780 fields on the cluster; the home re-judgment under 5.6.2
explains `config.head_dim` (128 is 4096 over 32 heads) and leaves the rest. Read by hand, with the library's own
behaviour as evidence:

- `template.default`: present in the copy, absent in the original. Equal to the instruct model's template, as above.
  A real change and the lineage marker.
- `special_tokens.tokenizer_config.json:pad_token`: `</s>` (id 2) added where the base declares none. Heretic's model
  loader sets the pad token to the end-of-sequence token when a tokenizer has none (its `model.py`, lines 151 to 152),
  and the other heretic copy in this round (piece 5) carries the same addition, as does the OBLITERATUS copy (piece 7). The generation settings and
  `config.pad_token_id` still carry no pad, so nothing contradicts it. A real change, declared by the tool rather than
  the card, harmless for single-prompt use.
- `config.dtype` and `config.torch_dtype`, `config.rope_parameters` and `config.rope_theta`: the copy's library
  (5.16.1) writes `dtype` for `torch_dtype` and folds `rope_theta` 1,000,000 into `rope_parameters`; the pinned 5.6.2
  writes the same two renames with the same values. Re-save.
- `added_tokens.decoder` and the 771 `special_tokens.added_tokens_decoder` entries: the copy's `tokenizer_config.json`
  (462 bytes) no longer lists the 771 added tokens the original's (136,697 bytes) does; the copy's `tokenizer.json`
  carries all 771 with equal ids and flags. Re-save by the newer library. The `special_tokens_map.json` entries that
  moved into `tokenizer_config.json` are explained by the tool.

## For the recipe library

Not consistent with the stated original. This is the first copy in the census whose measured footprint contradicts
the lineage on its card: a dense 2 percent change in every matrix, embedding and head is a fine-tune, and the scorer
should name it as such before it names a nearest projection recipe. Two table entries would carry it: a "dense
change" line (first-value share under 0.5 on readers and writers alike, remaining fractions near 1, every matrix
changed) that outranks the projection recipes, and a lineage check that compares the copy's chat template with the
templates of the original's own derivatives. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback7/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
