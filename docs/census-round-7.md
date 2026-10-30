# Census round 7: eight Gemma 4 and Mistral pairs (2026-10-30)

Eight published copies compared with their stated originals on Blueback, 2026-10-30. The first round card (5239) lost
its download job (3392481, exit 1 after 23 minutes) and its compare chain was cancelled the same hour; the round was
refiled as card 5291: download 3392877 (1 h 01), compares 3392878 to 3392885 (4 to 6 minutes each, exit 0), sweep
3392886, which deleted all eight originals (sweep.json: eight deleted, none kept). Card 5302 pulled the measurements
home and they were re-scored with the recipe table as committed today; the kit carried the same table, so no count
moved. Each pair has a card (the tool's Stage 1 text with the Stage 2 line) and a reading note in `docs/cards/`; the
full measurements are in `results/weights/` and `results/meta/`, and the saved direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/blueback7/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | llmfan46/gemma-4-E4B-it-ultra-uncensored-heretic | google/gemma-4-E4B-it | violations, 17 flags (energy shares) | consistent with the card: arbitrary-rank edits on 17 attention outputs in layers 18 to 35, inside the declared 7 to 36 |
| 2 | huihui-ai/Huihui-gemma-4-E4B-it-abliterated | google/gemma-4-E4B-it | match, 0 flags | consistent: one shared direction on every attention output and down projection in layers 7 to 41, weight 2.5 |
| 3 | igorls/gemma-4-12B-it-heretic-v1 | google/gemma-4-12B-it | violations, 9 flags (floor) | consistent: one direction, per-layer weights 1.08 to 1.38 on 13 down projections and 0.49 to 0.70 on 9 attention outputs |
| 4 | 3MPER0RR/Mistral-7B-v0.3-3MPER0RR-abliterated | mistralai/Mistral-7B-v0.3 | violations, 243 flags | not consistent with the stated original: a dense 2 percent change in all 226 matrices, embedding and head, under a directional ablation; the copy carries the instruct model's chat template |
| 5 | richardyoung/Mistral-7B-Instruct-v0.3-abliterated | mistralai/Mistral-7B-Instruct-v0.3 | violations, 21 flags (floor) | consistent: one direction, weights 1.24 to 1.31 on 27 down projections and 0.54 to 0.82 on 21 attention outputs |
| 6 | prithivMLmods/gemma-4-E4B-it-Uncensored-MAX | google/gemma-4-E4B-it | match, 0 flags | consistent with the card: the same weights as pair 2, field for field, re-sharded |
| 7 | richardyoung/Mistral-7B-Instruct-v0.2-abliterated-obliteratus | mistralai/Mistral-7B-Instruct-v0.2 | violations, 82 flags | consistent with the tool's description: rank-four edits on all seven projections of layers 22 and 24 to 31 and on the output head |
| 8 | evolveon/Mistral-7B-Instruct-v0.3-abliterated | mistralai/Mistral-7B-Instruct-v0.3 | violations, 13 flags (floor) | consistent: weight-1 projection on every attention output and down projection and on the token embedding |

In seven of the eight pairs nothing moved outside the matrices the maker's description names; the largest relative
change outside the changed set is exactly 0 in six and 0.000006 in pair 1. Pair 4 is the first copy in the census whose
measured footprint does not fit the original its card names: every matrix in the model changed by about 2 percent of
its norm in a full-rank way (first-value share 0.01 to 0.24 on the reading-side matrices, remaining fraction 0.94 to
1.11 along the leading directions), and on top of that the attention outputs of layers 6 to 30 and the down
projections of layers 9 to 31 carry a shared-direction ablation whose weight follows a kernel over the layers (0.11 at
layer 9, 1.32 at layer 24, 0.74 at layer 31). The copy's chat template equals Mistral-7B-Instruct-v0.3's byte for byte,
and the base has none; base and instruct share the same `config.json` and `tokenizer.json`. The dense change is the
instruct fine-tune or something like it, and one more comparison, against the instruct weights, would leave only the
ablation.

Pair 6 is the first re-upload the census has measured. Its card says it is the huihui copy re-sharded with no change
to the weights, and the measurement agrees: all 29,820 per-tensor fields equal pair 2's, the saved direction files are
equal byte for byte, and the two pinned Google revisions share one weight file. Its `base_model` field names Google,
which is what the pin rule compared against; the card names the real parent.

## The token side

Pair 8 is clean (a library version string). Pair 1 closes by tool once re-judged at home with the later-revision rule:
its template equals Google's 2026-04-28 fix (`c53e9d33`) byte for byte and its one null configuration field loads as
the library default, so its committed card reads "consistent with re-save noted". The other six keep "unexplained
differences" by tool and close by hand, each field with its evidence:

- Pairs 2 and 6 carry Google's release template (`292a7e27`, 2026-04-02), which Google replaced at 02:02Z on
  2026-04-10, fourteen hours before the huihui repository was created. The pin rule chose the newer revision; the maker
  worked from the older one. The tool reads the original's later revisions only, so an earlier-revision rule is owed.
  Every fixed conversation renders identically.
- Pairs 4, 5 and 7 write `config.dtype` where the original wrote `torch_dtype` (the same bfloat16); pair 4 also folds
  `rope_theta` into `rope_parameters` and writes `head_dim` 128 (4096 over 32 heads). The pinned library (5.6.2)
  writes all three renames with the same values, so they are re-save effects the tool does not name yet. Pair 4's
  `tokenizer_config.json` no longer lists the 771 added tokens the original's does; all 771 are present with equal
  ids and flags in its `tokenizer.json`, a newer library's layout.
- Pairs 4, 5 and 7 add a padding token, `</s>` (id 2), where the original declares none. Heretic's model loader sets
  the pad token to the end-of-sequence token when a tokenizer has none (its `model.py`, lines 151 to 152), and the
  OBLITERATUS copy shows the same addition. The two token files agree, the generation settings carry no pad, and the
  copies' cards do not mention it. A real change, made by the tool, harmless for single-prompt use.
- Pair 4's chat template is present where the base has none and equals the instruct model's. A real change and the
  lineage marker above.
- Pair 3's six configuration fields split in two. The three `dtype` entries repeat the top-level bfloat16 in each
  sub-configuration (re-save). The other four are values the original carries and the copy lacks: the audio tower's
  `audio_samples_per_token`, `hidden_size` and `output_proj_dims` (640, 640, 640) and the vision patch size (48).
  Loaded under the library that saved the copy (5.10.1), the original's configuration gives those values and the
  copy's gives 1024, 1536 and nothing for the rest; a 5.10.1 re-save of the original writes all four back. The copy's
  `config.json` dropped them, and the copy ships the audio embedding projection unchanged at shape [3840, 640], the
  original's geometry. The card's text-only use is unaffected; audio input through that configuration is untested
  here.

## What the scorer learned

The flag counts are the same on the cluster and at home because the kit carried today's table. Their causes:

- The bfloat16 storage floor, 43 flags on pairs 3, 5 and 8. Every flagged matrix has a leftover of 0.00142 to 0.00155
  of its norm, inside the calibrated 0.0025 line, and one minus the first share is 0.79 to 0.93 of the floor law's
  prediction from the relative change. Pair 8 is a textbook weight-1 projection on every layer and the analytic
  `single-projection` entry still flags 13 of its 64 matrices, because the entry reads the share (0.99) and the
  calibrated line is the leftover.
- Arbitrary rank, 17 flags on pair 1: first shares 0.936 to 0.975 that climb only to 0.963 to 0.985 by the eighth
  value, directions that differ by layer, unequal remaining fractions on the two sides of each matrix. The second
  measured copy of the method; the entry stays "not yet measured" until a run of our own.
- Rank four, 82 flags on pair 7: a group of four near-equal singular values and then a drop of 25 to 40 times, the
  first four carrying 0.90 to 0.99 of each change, on all seven projections of nine layers and the output head. The
  table has no rank-k entry; one would take the rank from the spectrum gap and ask the first k shares to sum near 1.
- A dense change under a projection, 243 flags on pair 4. The nearest-recipe search names `single-projection`, which
  misreads the copy; a "dense change" line (first share under 0.5 on readers and writers, remaining fractions near 1,
  every matrix changed) should outrank every projection entry, and a lineage check should compare the copy's chat
  template with the templates of the original's own derivatives.

The remaining-fraction measurement added after round 2 now reads each method's weight off the weights: 2.5 on the
huihui copy (output along the direction reversed and enlarged by half; row norms up to 0.068), 1.0 on the evolveon copy
(0.000 to 0.004 remaining), and the per-layer kernels of the heretic copies (1.08 to 1.38 and 0.49 to 0.70 on pair 3,
1.24 to 1.31 and 0.54 to 0.82 on pair 5, 0.11 rising to 1.32 and falling to 0.74 on pair 4's down projections). The
row norms sort the same copies by their norm handling: 0.0018 to 0.0040 for the later heretic's approximate
restoration (pair 3), 0.003 to 0.068 for the plain projections (pairs 2, 5, 8), against the 0.0011 the two exact
restorations of round 2 held. Heretic's single-direction setting shows as cross-layer agreement of 0.9925 or better
(pair 3) and 0.99995 or better (pair 5), where its per-layer setting would show as the 0.1 to 0.2 of round 2's pairs 1
and 4.

Two things the comparison could say by itself. Two pairs with the same original weights whose measurements agree in
every field are the same edit (pairs 2 and 6), which a fingerprint over the per-tensor fields would catch without a
reading. And a copy whose every matrix changed densely has a nearer parent than the one its card names (pair 4), which
the dense-change line above would say before any recipe is named.

## Owed to the metadata tool

An earlier-revision template rule (pairs 2 and 6); the `dtype` and `rope_parameters` renames as named re-save effects
(pairs 4, 5, 7); the padding-token fallback as a recognised tool signature (pairs 4, 5, 7); a rule for a field whose
absence loads differently from its presence, judged under the library that saved the copy (pair 3); the chat-template
lineage check (pair 4).

Weight differences alone cannot certify the absence of hidden behavior.
