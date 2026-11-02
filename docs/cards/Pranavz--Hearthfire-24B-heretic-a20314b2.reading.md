# Reading of the Stage 1 and Stage 2 result: Pranavz/Hearthfire-24B-heretic against mistralai/Mistral-Small-3.2-24B-Instruct-2506 (2026-11-02)

Measured on Blueback, round 29 piece 1, the first pair measured through the prefix mapping. The pull carries the
measurements and the sweep record and no job log. Modified revision `6d3f74c1` (2026-05-07), original pinned at
`95a6d26c` (2025-12-22), the revision current when the repository was created. The card's title says what the
`base_model` field does not: "a decensored version of LatitudeGames/Hearthfire-24B, made using Heretic v1.2.0".
Hearthfire is a supervised fine-tune of Mistral Small 3.2 for text adventure and roleplay under a ChatML template,
published 2025-12-06, and the census has not measured it. The card prints the chosen trial: the attention-output
kernel 3.75 at position 26.51 falling to 3.06 at distance 8.14, the down-projection kernel 2.66 at 14.59 falling to
3.73 at distance 25.63, `direction_index` per layer, 2 refusals in 100 against 96 for Hearthfire, a KL divergence
of 0.5561 against Hearthfire. The pin follows the field, so the measurement reads the fine-tune and the ablation
together.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 347 flags (201 unexpected
changes, 65 first shares, 80 direction cosines, one cross-kind), on the cluster and after re-scoring at home. On
reading, the fine-tune is everywhere at about one percent and the ablation sits on top of it where the card says.

- The mapping: the original stores its text tower under `language_model.` and the copy stores a flat causal
  model, so the tool renamed 363 tensors and matched all 363; the original's 222 other tensors (the vision tower
  and the projector) have no counterpart and are reported as left out, the first copy measured that way.
- 282 of 363 matched tensors changed, every linear of all 40 layers plus the embedding and the output head; the
  81 unchanged are the norms. Relative change 0.004 to 0.076, median 0.012; on the seven kinds the training
  alone touches (queries, keys, values, gate, up, and the attention outputs outside the window) the first share
  is 0.06 to 0.44 and the kept fractions 0.95 to 1.15 on both sides: a diffuse change that preserves the action,
  training's signature.
- The down projections carry the ablation through the training on all 40 layers: first share 0.984 to 0.995 at a
  relative change of 0.044 to 0.076, and along the leading output direction the copy keeps -0.61 at layer 0,
  -1.94 to -2.08 at layers 1 to 13, -1.52 to -1.80 at 15 to 33 and -2.27 to -2.60 at 32 to 38 (-2.60 at layer
  38, -2.48 at 39): weights of 1.6 to 3.6 against the card's 2.66 at layer 14.6 falling to 3.73 at the ends.
- The attention outputs carry it on layers 19 to 34: first share 0.90 to 0.97 where the other 24 sit at 0.06 to
  0.26, kept fractions -0.13 to -2.22 (-2.09 to -2.22 at layers 30 to 32, the card's peak of 3.75 at 26.5) where
  the other 24 keep 0.99 to 1.01. Within the window the two writers of a layer agree at 0.58 to 0.68 and outside
  it at 0.23 to 0.35, the one cross-kind flag.
- The embedding's 2.6 percent change is a filled block: rows that are zero in the release (unused vocabulary
  entries) carry values in the copy, which is why its row error reads 1.2e9; the output head changed by 6.3
  percent. Both are the fine-tune's.
- Rows moved 0.001 to 0.24 on the down projections; the card claims no preservation.

| Layer | Down: change, E1, left kept | Attention output: change, E1, left kept | Within-layer cosine |
| --- | --- | --- | --- |
| 0 | 0.060, 0.994, -0.61 | 0.015, 0.23, 1.01 | 0.33 |
| 4 | 0.050, 0.990, -2.08 | 0.013, 0.18, 1.00 | 0.29 |
| 14 | 0.061, 0.992, -1.71 | 0.013, 0.09, 1.00 | 0.30 |
| 19 | 0.045, 0.986, -1.79 | 0.052, 0.93, -1.74 | 0.58 |
| 26 | 0.047, 0.986, -1.72 | 0.075, 0.96, -0.40 | 0.68 |
| 31 | 0.045, 0.985, -2.21 | 0.060, 0.92, -2.22 | 0.67 |
| 34 | 0.050, 0.989, -2.27 | 0.044, 0.92, -0.86 | 0.64 |
| 38 | 0.060, 0.994, -2.60 | 0.010, 0.13, 1.01 | 0.31 |

The full table (282 rows) is in the report. The copy's ten shards share no checksum with Hearthfire's
(`f290181015` against `b1bd5d3ce3` on the first), as expected of an edited copy.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, 1,027 fields. Under transformers 5.22.1 `head_dim` closes by
the default rule. What remains is the fine-tune's: the release ships `tekken.json` and a multimodal configuration
where the copy ships a transformers tokenizer under ChatML with `<|im_end|>` (id 999) as its end token and a flat
`MistralForCausalLM` configuration; the 292-byte template is Hearthfire's and the release ships none of that form. The tool renders the
fixed conversation differently under the two, as it must.

## For the recipe library

The pin should follow the card's title, not the `base_model` field: measured against LatitudeGames/Hearthfire-24B
the training would cancel and the two kernels would read to the second decimal, as they do on the Mistral 7B and
Voxtral copies of these rounds. Measured against the release, the kernels still read through the training on the
down projections (the weight falls where the card says it falls) and the window reads on the attention outputs.
An entry for a Heretic edit on a fine-tune needs the fine-tune as the pin. The direction vectors stay in the pull
copy at `/opt/ai/hpc-packages/pulls/model-audit/blueback29/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
