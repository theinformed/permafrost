# Reading of the Stage 1 and Stage 2 result: richardyoung/zephyr-7b-beta-abliterated against HuggingFaceH4/zephyr-7b-beta (2026-11-02)

Measured on Wheat, round 47 piece 1 (download job 387398, compare job 387399, sweep 387407; the pull carries the
measurements and the sweep record and no job log). Modified revision `c464d324` (created 2025-12-15 15:58Z, the
weights uploaded at 16:16Z, the card replaced on 2026-03-28 and a sign-off added on 09-26), parent pinned at
`892b3d7a` of 2024-10-16, HuggingFaceH4's Zephyr 7B beta, a preference-tuned fine-tune of mistralai/Mistral-7B-v0.1
(`MistralForCausalLM`, 32 layers, hidden size 4,096, the weights uploaded on 2023-11-04). The card names Heretic
v1.1, 2 refusals in 100, a KL divergence of 0.076 and an A100, and the repository ships `abliteration_info.json`:
50 trials, the best trial 8, `direction_scope` "per layer", `attn.o_proj` with a maximum weight of 1.3371 at
position 23.834 falling to 0.2024 at a distance of 4.727, and `mlp.down_proj` with a maximum of 1.4981 at 18.791
falling to 1.1473 at a distance of 9.093. It is the census's first copy on the Zephyr line and its first on Mistral
7B v0.1; the parent counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 5 flags (first shares 0.956 to
0.989 on five attention outputs under the 0.99 floor), on the cluster and after re-scoring at home. On reading,
the copy is the card's two kernels, one direction per layer on both writers, read to the third decimal.

- 27 of 291 tensors changed: the down projections of layers 10 to 27 and the attention outputs of layers 20 to
  28, the two kernels' reaches to the layer (9.70 to 27.88 and 19.11 to 28.56). Everything else is exactly 0.
- One direction per layer: the two writers of a layer agree at 0.9996 to 1.0000, the layers at a median of 0.59.
- Output side on all 27: one minus the left kept fraction reads 1.158 at layer 10 rising to 1.490 at 19 and back
  to 1.180 at 27 on the down projections, and 0.414 at 20 rising to 1.297 at 24 and back to 0.335 at 28 on the
  attention outputs; the published kernels give the same numbers within 0.0011 on the down projections and 0.0029
  on the attention outputs. The right side keeps 0.03 to 0.91.
- First shares 0.956 to 0.997; relative changes 0.0064 to 0.0283; rows moved 0.0072 to 0.0325, through and over
  finding 22's band under a card that claims no norm.

| Layer | Kind | Change | E1 | Weight read | Kernel | Rows |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | down | 0.0218 | 0.995 | 1.158 | 1.159 | 0.0162 |
| 15 | down | 0.0272 | 0.997 | 1.352 | 1.352 | 0.0144 |
| 19 | down | 0.0252 | 0.996 | 1.490 | 1.490 | 0.0081 |
| 23 | down | 0.0208 | 0.994 | 1.335 | 1.336 | 0.0285 |
| 27 | down | 0.0179 | 0.993 | 1.180 | 1.181 | 0.0224 |
| 20 | attention output | 0.0072 | 0.963 | 0.414 | 0.417 | 0.0080 |
| 22 | attention output | 0.0164 | 0.991 | 0.896 | 0.897 | 0.0114 |
| 24 | attention output | 0.0220 | 0.995 | 1.297 | 1.297 | 0.0301 |
| 26 | attention output | 0.0145 | 0.989 | 0.816 | 0.817 | 0.0186 |
| 28 | attention output | 0.0064 | 0.956 | 0.335 | 0.337 | 0.0091 |

The full table (27 rows) is in the report.

Directions. No measurement in the census stands on Zephyr or on Mistral 7B v0.1, so no family exists for this
copy. The hidden size (4,096) and the layer count match the Mistral 7B instruct measurements, and against their
saved vectors the direction stands on the left at 0.631 to evolveon's projection of Mistral 7B Instruct v0.3 and
0.627 to the maker's own v0.3 edit (27 names each), 0.559 to DogOnKeyboard's Heretic pass, 0.546 to paoloronco's
Heretic pass (24 names), 0.485 and 0.484 to 3MPER0RR's two measurements, 0.357 to wangzhang's edit of the
circuit-breaker model of this round (25 names) and 0.047 to the maker's OBLITERATUS copy of v0.2; on the right
at 0.58 to 0.04 in the same order. By byte range the layer 24 attention output and the layer 19 down projection
stand 0.0220 and 0.0252 from Zephyr's, each difference rank one (first shares 0.9949 and 0.9961), and the layer 5
query projection is byte-equal to Zephyr's; Zephyr itself stands 0.0354, 0.0440 and 0.0343 from Mistral 7B v0.1
on those three matrices with no leading component (first shares 0.091, 0.025 and 0.051), a full fine-tune.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, no field closing: the four entries of
`special_tokens_map.json` written as objects where the parent writes strings (the same tokens and ids), a
`do_sample: true` added to the generation file, and `torch_dtype` written as `dtype` with the same value; the
version strings move from 4.35.0 to 4.57.3, and the template moved from `tokenizer_config.json` to
`chat_template.jinja` with the same text and renders identically. The token ids are Zephyr's on both sides
(`bos_token_id` 1, `eos_token_id` 2, `pad_token_id` 2 in the configuration, no pad in the generation file) and the
vocabulary is 32,000.

## For the recipe library

The per-layer entry reads the copy with a kernel line naming the published record's two kernels; the five first
shares under the floor are the attention outputs of layers 20, 21 and 26 to 28, where the weight is 0.33 to 0.82. A
line that renames `torch_dtype` to `dtype` would close the two `dtype` fields here and on pairs 2 and 3. The
direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat47/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
