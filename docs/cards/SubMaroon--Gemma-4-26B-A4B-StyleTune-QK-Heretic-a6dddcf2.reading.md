# Reading of the Stage 1 and Stage 2 result: SubMaroon/Gemma-4-26B-A4B-StyleTune-QK-Heretic against Gryphe/Gemma-4-26B-A4B-StyleTune-V2 (2026-11-02)

Measured on Nautilus, round 42 piece 6 (download job 4171128, compare job 4171134, sweep 4171137; the pull carries
the measurements and the sweep record and no job log). Modified revision `1c802dff` (created 2026-09-13 00:51Z,
the folder uploaded at 00:53Z, the card at 01:11Z, a generation dump and three files at 02:26Z and 02:27Z, the
card revised at 02:28Z), parent pinned at `f34ba405` of 06-20, Gryphe's StyleTune-V2, a fine-tune of
google/gemma-4-26B-A4B-it that trains the `lm_head` alone and leaves every transformer layer as Google's, as its
card says and the bytes below show. The copy's card names three edits and three parents: the body
"coder3101/gemma-4-26B-A4B-it-heretic (Heretic ARA, layers 10-30, KL 0.0499)", the `lm_head` from StyleTune-V2 with
`tie_word_embeddings` set to false, and the queries and keys interpolated toward a roleplay fine-tune trained on
top of StyleTune-V2 (Gryphe's Pantheon-Reasoning 1.1 V2, the third name in its `base_model` field) at alphas of
0.85 on the sliding layers and 0.65 on the global layers 5, 11, 17, 23 and 29, where the keys serve as values; it
says the body was "verified by tensor comparison" and prints the size of the query and key step as a relative
norm and a per-row rotation. The pair is a second-generation measurement against a parent that supplies one of
the three edits, so it reads the other two and reads the third as equal.

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 100 flags (59 unexpected changes, 20
first shares at 0.659 to 0.959, 20 direction cosines, 1 cross-kind cosine), on the cluster and after re-scoring at
home. On reading, the copy is the card's three edits one by one: coder3101's arbitrary-rank body on the attention
outputs of layers 10 to 29, a change without a direction on the queries and keys of every layer, and an `lm_head`
equal to the parent's.

- 79 of 1,014 tensors changed: the attention outputs of layers 10 to 29 (20), the query projections of all 30
  layers and the key projections of 29 (layer 5's key is rewritten by 0.00099, under the threshold and the largest
  relative change outside the changed set, 0.000994). The `lm_head`, the embeddings, the vision tower, the down
  projections and the 128 experts a layer are untouched.
- The body: a few directions per matrix on the 20 attention outputs (first shares 0.66 to 0.96), input side, one
  minus the right kept fraction 0.76 to 1.49 (1.49 at layer 20, 0.76 at 25), relative changes 0.0095 to 0.0377,
  rows 0.0061 to 0.0080, finding 22's band; coder3101's measured edit on the same checkpoint reads the same window
  (layers 10 to 29 under a card to 30).
- The queries and keys: 59 matrices rewritten by 0.0010 to 0.0048 with no direction (first shares 0.04 to 0.83,
  both kept fractions within 0.006 of 1.00), rising with the layer from 0.0012 at layer 0 to 0.0048 at 26; rows
  0.0001 to 0.0177.
- The `lm_head`: relative change 0, the parent's own, which the card names as its source.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Query: change, E1 | Key: change, E1 | Rows (output, query, key) |
| --- | --- | --- | --- | --- | --- |
| 0 | - | - | 0.0012, 0.082 | 0.0011, 0.043 | -, 0.0002, 0.0001 |
| 5 | - | - | 0.0010, 0.124 | 0.00099, under threshold | -, 0.0002, - |
| 10 | 0.0342, 0.659, 0.76, -0.27 | 1.27 | 0.0020, 0.420 | 0.0018, 0.337 | 0.0077, 0.0005, 0.0011 |
| 17 | 0.0207, 0.889, 0.98, -0.43 | 1.43 | 0.0034, 0.540 | 0.0032, 0.255 | 0.0073, 0.0011, 0.0177 |
| 20 | 0.0377, 0.902, 0.94, -0.49 | 1.49 | 0.0034, 0.582 | 0.0033, 0.427 | 0.0073, 0.0006, 0.0010 |
| 23 | 0.0095, 0.905, 0.98, 0.19 | 0.81 | 0.0033, 0.653 | 0.0026, 0.259 | 0.0069, 0.0015, 0.0004 |
| 25 | 0.0148, 0.959, 0.79, 0.24 | 0.76 | 0.0032, 0.684 | 0.0030, 0.354 | 0.0078, 0.0007, 0.0015 |
| 29 | 0.0123, 0.927, 0.95, -0.18 | 1.18 | 0.0033, 0.750 | 0.0026, 0.336 | 0.0075, 0.0009, 0.0003 |

The full table (79 rows) is in the report.

Directions. Against twenty-nine saved vectors of other measurements of the 26B-A4B, the attention outputs stand at
1.000 on both sides to coder3101's edit on all 20 shared names (minimum 1.000), at 0.992 to llmfan46's (20),
0.978 to SassyDiffusion's (18), 0.950 and 0.936 to llmfan46's and coder3101's QAT searches, 0.75 to Goodoldjam's,
0.73 to Umranz's and mewse's, 0.71 to OS-Software's Japanese search, 0.21 or less to every kernel pass and
projection on the base and 0.06 to huihui-ai's and its re-uploads; against the round's other 26B-A4B edits they
stand at 0.984 to Vortex5's Chimera-X edit (13 names) and 0.947 to its Moonlight-Dusk edit (12). By byte range the
layer 20 attention output is byte-equal to coder3101's and 0.0377 from StyleTune-V2's, Google's and Pantheon V2's
(StyleTune-V2's byte-equal to Google's, Pantheon V2's 0.0033 from them); the layer 20 query projection is 0.0034
from StyleTune-V2's, coder3101's and Google's, which are byte-equal to each other, and 0.0004 from Pantheon V2's,
which is 0.0036 from them; the layer 20 key projection 0.0033 from the base's and 0.0003 from Pantheon V2's
(0.0035 apart); the layer 5 key projection, a global layer at the card's lower alpha, 0.0010 from the base's and
0.0003 from Pantheon V2's (0.0011 apart); and the layer 20 down projection byte-equal on StyleTune-V2, coder3101's
and Google's with Pantheon V2's 0.0032 away. The merged queries and keys sit nine tenths of the way to the donor's
on the sliding layer and on the global one; at this size a bfloat16 step is 0.4 percent of a value, so the card's
two alphas cannot be read from the bytes. The three shards (`ebff4d97`, `c7284b61`, and `00ce94a3` for the
`lm_head` alone) match no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home on seven fields, all of them the parent's Unsloth save
against the body's Google form: StyleTune-V2 carries `eos_token_id` 106 alone and `pad_token_id` 0 in its
configuration and its token ids, `unsloth_fixed` true, and its template in `tokenizer_config.json`; the copy
carries `eos_token_id` `[1, 106]`, no `pad_token_id`, no `unsloth_fixed`, and a 18,683-byte `chat_template.jinja`
byte-equal to Google's 26B-A4B revision `35b4173c` of 07-15 in place of the parent's 16,448-byte template (Google's
`1db3cff1` of 04-10), with a version string older than the parent's (5.5.0.dev0 against 5.10.2): the token files
are coder3101's body's and not the parent's. The fixed conversation renders identically under both templates, and
`bos_token_id` 2 and the generation `[1, 106, 50]` are on both sides.

## For the recipe library

No entry reads a merge; a merge entry would read each component against the saved vectors of measured copies and
would have read the body as coder3101's at 1.000 and the `lm_head` as the parent's, leaving the query and key step
as a change without a direction, which is what the card says it is. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus42/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
