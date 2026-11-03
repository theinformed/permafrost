# Reading of the Stage 1 and Stage 2 result: Naphula/Darkest-muse-v1-abliterated against sam-paech/Darkest-muse-v1 (2026-11-03)

Measured on Wheat, round 49 piece 8 (download job 387515, compare job 387523, sweep 387524; the pull carries the
measurements and the sweep record and no job log). Modified revision `0b2568a5` (created 2025-12-08 12:44Z, the card
written in three edits, six small files at 12:51Z, the fifth shard at 12:53Z and the other four one at a time from
15:12Z to 16:25Z), parent pinned at `55f6ba02` of 2024-10-25, sam-paech's Darkest-muse-v1, a `dare_ties` merge (its
`mergekit_config.yml` published) of two of the author's Gutenberg3 preference-trained Gemma 2 9B fine-tunes onto
lemon07r's Gemma-2-Ataraxy-v2-9B, "Fine-tuned from Gemma-2-9b-it" by its card (`Gemma2ForCausalLM`, 42 layers,
hidden size 3,584, vocabulary 256,000). It is the census's first copy on a Gemma 2 checkpoint and its first community
parent on that line. The copy's card names no method or parameter: "they have not been ablated with MPOA, so may
suffer some cognitive decline", "made these mainly for testing purpose", untested for compliance, with a pointer to
grimjim's norm-preserving biprojection for anyone who would merge first and edit afterward. The parent counts as
neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was a match to `single-projection`, with no flag, on the cluster and after re-scoring at home.
On reading, the copy is the classic projection of one direction out of both writers of every layer at a flat weight
of 1.5.

- 84 of 465 tensors changed: the down projections and attention outputs of all 42 layers. Everything else is
  exactly 0, the embedding and the output head included, and the copy's configuration, shard index and token files
  are the parent's by object id.
- One direction for all 84 matrices: agreement 0.9995 at the median and 0.9964 at the least, across kinds 0.9948.
- Output side on all 84: one minus the left kept fraction reads 1.500 to 1.511 on every matrix; the right side keeps
  -0.04 to 0.90.
- First shares 0.9952 to 0.9969; relative changes 0.0228 to 0.0291; rows moved 0.0034 to 0.0317 under a card that
  disclaims the norm-preserving form.

| Layer | Kind | Change | E1 | Weight read | Rows |
| --- | --- | --- | --- | --- | --- |
| 0 | attention output | 0.0257 | 0.996 | 1.502 | 0.0095 |
| 21 | attention output | 0.0262 | 0.996 | 1.501 | 0.0220 |
| 36 | attention output | 0.0236 | 0.995 | 1.503 | 0.0317 |
| 0 | down | 0.0249 | 0.996 | 1.501 | 0.0095 |
| 3 | down | 0.0254 | 0.996 | 1.506 | 0.0076 |
| 21 | down | 0.0266 | 0.996 | 1.500 | 0.0099 |
| 39 | down | 0.0238 | 0.996 | 1.500 | 0.0063 |

The full table (84 rows) is in the report.

Directions. No other measurement in the census is on Gemma 2, and none shares the 3,584 hidden size, so the saved
vectors have nothing to stand against. By byte range the parent stands 0.0021 from google/gemma-2-9b-it at
`11c9b309` on the layer 20 attention output, 0.0032 on the layer 20 down projection and 0.0012 on the layer 5 query
projection, with no leading component (first shares 0.050, 0.012 and 0.006); the copy's layer 20 attention output is
a rank-one change from the parent's (first share 0.996, 0.0252) and its layer 5 query projection is the parent's
bytes.

## Token and configuration side (Stage 1)

"Undecided" on the cluster and at home, with no field differing. The two reasons are on both sides: neither
repository publishes a `generation_config.json`, and the template both share by object id (591 bytes, in
`tokenizer_config.json`) raises "System role not supported" on the fixed conversation, so the card lists the render
as missing evidence. Rendered at home through its own Jinja text on a conversation without a system turn, the two
give the same string. The token ids are Gemma 2's on both sides (`bos_token_id` 2, `eos_token_id` 1, `pad_token_id`
0, vocabulary 256,000); with no generation file, `<end_of_turn>` (107) is a stop token on neither side.

## For the recipe library

The single-projection entry reads the copy cleanly. The metadata tool needs the render line of round 47, a fixed
conversation without a system turn when a template refuses one, and a line that names a missing generation file as
the parent's own when both sides lack it, so that a pair with no differing field is not left undecided. The
direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat49/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
