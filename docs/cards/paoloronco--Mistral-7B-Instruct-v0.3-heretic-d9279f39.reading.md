# Reading of the Stage 1 and Stage 2 result: paoloronco/Mistral-7B-Instruct-v0.3-heretic against mistralai/Mistral-7B-Instruct-v0.3 (2026-11-02)

Measured on Blueback, round 26 piece 2. The pull carries the measurements and the sweep record and no job log.
Modified revision `58b15e53` (three commits on 2026-05-27 from 14:03Z to 14:56Z: the repository, a folder upload
and the card), original pinned at `c170c708` (2025-12-03), the revision current when the repository was created.
The card names Heretic v1.3.0 and prints the chosen trial's parameters (trial 173): `direction_index` 16.87, the
attention-output kernel 1.44 at position 24.50 falling to 1.01 at distance 13.91, the down-projection kernel 1.18
at 20.94 falling to 1.16 at distance 8.36; it reports 4 refusals in 100 and a KL divergence of 0.0606, and says the
correction is "applied via LoRA, a lightweight, targeted weight modification". The `base_model` field names the
original.

## Weights (Stage 2)

The tool's assessment was "recipe match", nearest recipe `directional-per-layer-selected`, 0 flags, on the cluster
and after re-scoring at home. On reading, the copy is the card's kernel pair to the second decimal, written into the
weights.

- 38 of 291 tensors changed: the attention outputs of layers 11 to 31 and the down projections of 13 to 29. Nothing
  else moved; the largest relative change outside the changed set is exactly 0 and 253 tensors equal the original.
  No adapter file is in the repository: the "LoRA" of the card is 38 matrices edited in place.
- One shared direction: within each kind the leading directions agree with their median at 0.953 to 0.9999 (medians
  0.998 and 0.9996), across kinds at 0.92, within each layer at 0.986 to 1.000. First share 0.992 to 0.995 at
  relative changes of 0.017 to 0.024, the storage floor's band.
- Output side: the left kept fraction below the right on 38 of 38.
- The kernels read off the kept fractions. The attention outputs keep -0.40 at layer 25 (a weight of 1.40 against
  the card's 1.44 at 24.50), -0.39 at 24, -0.36 at 26, falling to -0.02 at layer 12 and 0.04 at 11 (the card's
  1.01 at distance 13.9); layer 31, the last matrix of the window, keeps 0.86. The down projections keep -0.10 to
  -0.16 on all 17 (the card's 1.16 to 1.18), -0.16 at layers 17 and 18 (the card's 1.18 at 20.94).
- Rows moved by 0.003 to 0.013; the card claims no preservation.

| Layer | Attention output: change, E1, left kept | Down projection: change, E1, left kept | Within-layer cosine |
| --- | --- | --- | --- |
| 11 | 0.0172, 0.992, 0.04 | | |
| 13 | 0.0209, 0.994, -0.04 | 0.0221, 0.995, -0.14 | 0.996 |
| 18 | 0.0213, 0.994, -0.13 | 0.0202, 0.994, -0.16 | 0.994 |
| 21 | 0.0196, 0.994, -0.28 | 0.0182, 0.993, -0.14 | 0.997 |
| 25 | 0.0233, 0.995, -0.40 | 0.0175, 0.992, -0.11 | 0.995 |
| 29 | 0.0200, 0.994, -0.25 | 0.0177, 0.992, -0.12 | 0.994 |
| 31 | 0.0210, 0.994, 0.86 | | |

The full table (38 rows) is in the report. The fingerprint shares no measured field with the four earlier reports
on this original.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, 777 fields. Under transformers 5.22.1 `head_dim` and
`rope_parameters` (a 5.9.0 save's forms of two fields the 4.42 original omits) close by the default rule. What
remains: the tokenizer configuration of the save carries no `added_tokens_decoder` block where the original
declares 771 added tokens, and the two `tokenizer.json` files are different saves (3,672,121 bytes against
1,961,548), so finding 44's rule, which reads the dropped block against a shared token file, cannot run; a
`pad_token` of `</s>` (id 2) written where the original declares none; and the 5.x renames `dtype` for
`torch_dtype`. The template moved from the tokenizer configuration into `chat_template.jinja` (explained by the
tool), and the fixed conversation renders identically.

## For the recipe library

The per-layer entry fits with no flag, and a `single-projection-selected` entry with a kernel would fit tighter:
the direction is shared and the weight is the card's schedule. The second Heretic kernel pair on a Mistral 7B base
to read to the second decimal (finding 41's copy was the first on a Mistral base). The pull copy keeps the
direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback26/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
