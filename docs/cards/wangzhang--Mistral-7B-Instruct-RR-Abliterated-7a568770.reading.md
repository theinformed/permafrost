# Reading of the Stage 1 and Stage 2 result: wangzhang/Mistral-7B-Instruct-RR-Abliterated against GraySwanAI/Mistral-7B-Instruct-RR (2026-11-02)

Measured on Wheat, round 47 piece 2 (download job 387398, compare job 387400, sweep 387407; the pull carries the
measurements and the sweep record and no job log). Modified revision `180527d8` (created 2026-04-13 19:01Z, a first
upload at 19:02Z, the weights replaced on 04-14 at 00:49Z under the title "v2: full LoRA strip + minimal direct
abliteration", notices added on 08-29), parent pinned at `5b9121da` of 2024-07-09, GraySwanAI's Mistral 7B
Instruct with circuit breakers inserted by representation rerouting (the weights uploaded on 07-08, the
configuration's `_name_or_path` mistralai/Mistral-7B-Instruct-v0.2). The card describes abliterix in two steps:
the circuit breaker read as "a rank-16 LoRA delta on `mistralai/Mistral-7B-Instruct-v0.2`" and stripped whole
(`--lambda 0.0`), then a direct-mode pass with one direction (`vector_method=mean`, `n_directions=1`,
`steering_mode=direct`, `decay_kernel=linear`, `strength_range=[1.5, 6.0]`, trial 39 of 60), 12 refusals in 100
against 69 at a KL divergence of 0.042; the first upload was a partial strip at 0.3 with three directions. It is
the census's first edit of a model trained to refuse by representation rerouting. The parent counts as neither an
original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 215 flags (138 unexpected changes, 41
first shares, 35 direction cosines, 1 cross-kind cosine), on the cluster and after re-scoring at home. On reading,
the copy is Mistral's instruct model with the circuit breaker taken out and one direction edited in, and the
parent's training accounts for most of the changed set.

- 200 of 291 tensors changed: the query, key, value and output projections of all 32 layers, the gate and up
  projections of layers 0 to 20 and the down projections of 0 to 20 and 23 to 31. The normalisation vectors, the
  embedding and the head read exactly 0.
- The parent's own change, read by byte range against mistralai/Mistral-7B-Instruct-v0.2 at `63a8b081`: all seven
  linear maps of layers 0 to 20 move by 0.013 to 0.016 on the three matrices read, sixteen components carrying 0.985
  to 0.990 of the change (the card's rank-16 adapter within the bfloat16 rounding), and layers 21 to 31 are the
  instruct model's bytes.
- The copy against the instruct model: the first 2,000,000 bytes of every linear map are equal on 142 of the 224,
  the gate and up projections of every layer, the down projections of 0 to 22, the queries of 0 to 17, the keys and
  values of 0 to 15 and the attention outputs of 0 to 4, and the layer 10 gate and query projections read whole are
  byte-equal. So 118 of the 200 matrices changed against the parent are the strip alone, the parent's adapter
  removed to the last bit, and 82 carry the edit.
- The edit: the attention outputs of layers 5 to 31 and the down projections of 23 to 31 on the output side, the
  keys and values of 16 to 31 on the input side, one direction across all of them (the attention outputs of 10 to
  31, the down projections and the input side of the keys and values at 1.000 to the layer 25 attention output,
  layers 5 to 9 at 0.975 to 0.9995), and the queries of 18 to 31 on their output side along a shared direction of
  their own (0.945 to each other on the output side, their input side at 0.04 or less to the first). Read on layers
  21 to 31, where the parent is the instruct model, one minus the kept fraction is 5.62 at layer 22 and 5.55 at 23
  on the attention outputs, falling by 0.245 to 0.25 a layer to 3.57 at 31 (and to 1.31 at layer 5 as read against
  the parent), 1.84 to 1.95 on the down projections, 1.88 to 2.76 on the input side of the keys and values and 2.49
  to 2.99 on the output side of the queries, inside the card's strength range; first shares 0.997 to 0.9997. By byte
  range the copy stands 0.0447, 0.0811 and 0.0463 from the instruct model on the layer 10 and 25 attention outputs
  and the layer 25 query projection, each difference rank one (0.9987, 0.9996, 0.9988).
- Rows moved 0.048 to 0.178 on the attention outputs, 0.024 to 0.108 on the queries, 0.005 to 0.047 on the down
  projections and under 0.005 on the keys and values.

| Layer | Attention output weight | Down weight | Key, value weight (input side) | Query weight | Rows (attention output) |
| --- | --- | --- | --- | --- | --- |
| 21 | 5.38 | - | 2.11, 2.12 | 2.74 | 0.129 |
| 22 | 5.62 | - | 2.23, 2.19 | 2.82 | 0.091 |
| 24 | 5.30 | 1.86 | 2.47, 2.33 | 2.99 | 0.178 |
| 26 | 4.81 | 1.91 | 2.47, 2.48 | 2.90 | 0.100 |
| 28 | 4.31 | 1.95 | 2.23, 2.62 | 2.74 | 0.132 |
| 31 | 3.57 | 1.88 | 1.88, 2.70 | 2.49 | 0.062 |

Directions. Against the saved vectors of the Mistral 7B measurements, on the 32 attention outputs, the direction
stands on the left at 0.733 to 3MPER0RR's edit measured against the instruct v0.3 model (26 names), 0.674 to
paoloronco's Heretic pass of v0.3, 0.648 to DogOnKeyboard's, 0.555 to richardyoung's v0.3 edit, 0.549 to evolveon's,
0.397 to the Zephyr pass of this round and 0.012 to richardyoung's OBLITERATUS edit of v0.2, the one other edit on
this instruct model. The comparison is made on the attention outputs because 118 of the changed matrices carry
the adapter's components and no edit.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on thirteen fields and at home on eleven, the home judgement closing
`config.head_dim` and `config.rope_parameters` (the 5.x form of `rope_theta`, the same value on both sides). The
fields left are a transformers 5.5.3 save of a 4.40.0 parent: the three `added_tokens_decoder` entries and the empty
`additional_special_tokens` list are not written, `torch_dtype` is written as `dtype`, `rope_theta` as
`rope_parameters`, and the template moved from `tokenizer_config.json` to a 476-character `chat_template.jinja`
with the parent's text. The fixed conversation opens with a system turn, which this template refuses ("Conversation
roles must alternate"), so both renders are listed as missing evidence; rendered at home on a user, assistant, user
conversation the two give the same string. The copy's `tokenizer.json` (3,505,904 bytes, `780dd6a1`) is the file the
Zephyr copy of this round carries, the parent's is a 1,795,595-byte older save. The token ids are Mistral's on both
sides (`bos_token_id` 1, `eos_token_id` 2, no pad) and the vocabulary is 32,000.

## For the recipe library

No entry reads a strip under an edit; measured against mistralai/Mistral-7B-Instruct-v0.2 the copy would read
82 matrices, a one-direction entry on both writers and the input side of the keys and values with a linear-kernel
weight line and a second direction on the queries. The pinner should mark a parent whose card or configuration
names an adapter on a publisher's checkpoint and queue the pair against that checkpoint as well. A template
render that falls back to a conversation without a system turn would read the template here. The direction
vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat47/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
