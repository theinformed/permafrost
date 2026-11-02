# Census round 25: eight Gemma 4 E2B and E4B pairs whose exports drop the shared-KV tensors (2026-11-01)

Eight published copies compared with their stated originals on Blueback from the batch pinned as
`data/batches/round-25-batch-1.json` (pinned 2026-10-31 18:27Z): eight E2B and E4B copies whose exports drop the
shared-KV tensors (54 names on the E4B, 60 on the E2B), admitted since kit `d86656a` maps them (finding 14). The
pull of 11-01 18:57Z brought home the eight measurement folders and the sweep record and no job log, so the
download, compare and sweep job numbers and their seconds are not recorded in this note; the sweep deleted the
seven original checkpoints (`d6436b3d`, `ee0ef602`, `c53e9d33` and `83df0a88` of the E4B original for pairs 1, 2,
3 and 5, and 4; `b446025c`, `b4a60110` and `6b7e72c6` of the E2B original for pairs 6, 7 and 8) from
`/p/work1/sdegan/model-audit/rounds/25/originals/`. The pinner held back two copies (eshucode's and
KridgeDookie's). The eight measurements were re-scored at home with the recipe table as committed and the saved
direction vectors, and no flag count moved. Every metadata report was judged again at home under transformers
5.22.1 with the originals' commit histories, and the committed reports carry that judgement. Each pair has a card
(the tool's Stage 1 text after the home judgement, with the Stage 2 line) and a reading note in `docs/cards/`;
the measurements are in `results/weights/` and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/blueback25/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | jokernifty/gemma-4-e4b-it-abliterated | google/gemma-4-E4B-it | match, 0 flags | the card's single projection at weight 1.0000 on both writers of layers 20 to 34 and on the token embedding, one shared direction, saved in float16: first shares of 0.9999 where every bfloat16 copy reads 0.989 to 0.997, the storage floor of finding 3 absent |
| 2 | Dingdust/ContextPilot-E4B-heretic | google/gemma-4-E4B-it | violations, 360 flags (205 unexpected changes, 75 first shares, 79 direction cosines, one cross-kind) | a Heretic edit on a fine-tune the README's second card names (tencent/ContextPilot-E4B) and the `base_model` field does not: 285 tensors changed by 0.1 to 0.4 percent with no direction, and the card's two kernels readable on the attention outputs of layers 25 to 41 and the down projections of 27 to 41, the windows to the layer, the strengths shallower |
| 3 | DuoNeural/Gemma-4-E4B-Heretic | google/gemma-4-E4B-it | violations, 18 flags (first shares 0.976 to 0.990 on the weakest attention outputs) | one shared direction, output side, on the down projections of layers 6 to 41 at a flat weight of 1.36 to 1.41 and the attention outputs of 10 to 41 at 0.39 to 0.89 with a centre near layer 30, where the card says "42 layers each"; the copy ships no chat template |
| 4 | treadon/gemma4-E4B-it-abliterated | google/gemma-4-E4B-it | match, 0 flags | the card's norm-preserving biprojected abliteration to the number: 17 layers, one direction per layer, scale 1.0 (left kept fraction within 0.013 of 0), rows restored within 0.0003 |
| 5 | treadon/gemma4-E4B-it-Abliterated-AND-Disinhibited-USE-THIS | google/gemma-4-E4B-it | violations, 32 flags (first shares 0.66 to 0.76 on the 16 doubled layers) | the card's two edits in sequence: the disinhibition at 1.5 on 20 layers and the abliteration at 1.0 on 17, two directions where both reach, one where one does; layer 17, abliteration alone, equals pair 4 in every field |
| 6 | wangzhang/gemma-4-E2B-it-abliterated | google/gemma-4-E2B-it | violations, 5 flags (first shares 0.987 to 0.990 on the weakest queries) | the card's Abliterix edit on four of its five components with a weight band per kind: attention outputs 1.9 to 3.1, values 2.3 to 3.0, down projections 0.7 to 1.4, queries 0.56 to 0.89, no key touched, rows restored; the window reads 9 to 34 where the card says 5 to 30 |
| 7 | treadon/gemma4-E2B-it-abliterated | google/gemma-4-E2B-it | match, 0 flags | the card's edit to the number: 24 layers, one direction per layer, scale 1.75 (left kept fraction -0.744 to -0.760 on all 48), rows restored within 0.0003 |
| 8 | treadon/gemma4-E2B-it-Abliterated-AND-Disinhibited-USE-THIS | google/gemma-4-E2B-it | violations, 42 flags (40 first shares 0.54 to 0.63 on the 20 doubled layers, two within-layer cosines on layer 9) | the card's two edits in sequence: the abliteration at 1.75 on pair 7's 24 layers and the disinhibition at 1.5 on 20 of them, two directions where both reach and one where one does; no field equal to pair 7 |

Nothing moved outside the matrices the maker's method reaches in any pair but one: the largest relative change
outside the changed set is exactly 0 in pairs 3, 4, 5, 6, 7 and 8, 1.07 × 10⁻⁶ in pair 1 (bfloat16 values of the
per-layer input gates rounded by the float16 save) and 0.000998 in pair 2, whose fine-tune sits at the threshold
on 189 tensors beside the 285 above it. The round's result is eight edits and no re-upload, the second such round.
Six of the eight read as their cards say to the number (pairs 4 and 7 in layer count, scale and restoration, pair
1 in window, weight and the embedding, pairs 5 and 8 in both layer counts and both scales, pair 3 in its two
kernels' shape), one (pair 6) reads four of five components and a window four layers higher than the card's, and
one (pair 2) reads a Heretic edit on a fine-tune its `base_model` field does not name and its README does. The
exports: all eight drop the shared-KV tensors the model never reads (54 on the E4B, 60 on the E2B), and the kit
maps them without a flag.

The weights read off the weights: 1.0000 on pair 1's 30 projections (left kept fraction within 0.00005 of 0, a
float16 save), 1.0 on pair 4's 34 (within 0.013), 1.75 on pair 7's 48 (within 0.016), 1.5 and 1.0 on pair 5's
layers (the disinhibition's -0.50 leading on 20, the abliteration's 0.00 on layer 17), 1.75 and 1.5 on pair 8's
(the abliteration's -0.75 leading on all 24), four bands on pair 6's four kinds (1.91 to 3.12 on the attention
outputs, 2.31 to 3.02 on the values, 0.72 to 1.43 on the down projections, 0.56 to 0.89 on the queries), 1.36 to
1.41 on pair 3's down projections with 0.39 to 0.89 on its attention outputs, and pair 2's kernels shallower than
the card under the fine-tune (the down kernel's -0.40 reading -0.32 to 0.09).

Preservation claims. The five treadon and wangzhang copies (pairs 4 to 8) claim row restoration and read it:
rows within 0.0003, 0.0004, 0.0005, 0.0003 and 0.0005. Pairs 1, 2 and 3 carry no claim and moved their rows
0.004 to 0.015, 0.001 to 0.16 and 0.003 to 0.015.

Fingerprints. Sixteen measurements now stand on the E4B instruct original; pair 3's first and last shards equal
OS-Software's and TheUmbraWalker's (the library's four-shard layout of the embeddings and the tail), pairs 4 and 5
share the two matrices of layer 17 in every field, and nothing else is shared. Thirteen stand on the E2B instruct
original; pairs 7 and 8 change the same 48 tensors with no field equal, and pair 6 shares no field with anything.

## The token side

The cluster's cards read "unexplained differences" on all eight, every one on configuration or template fields
and none on a weight. Re-judged at home under transformers 5.22.1, eight fields move (one per pair,
`text_config.moe_intermediate_size`, null in 5.5.3 to 5.16.1 saves against a 5.5.0.dev0 original, closed by the
default rule) and five cards change their reading to "consistent with re-save noted" (pairs 4, 5, 6, 7 and 8:
the version strings and nothing else). Three stay as printed:

- Pair 1: the storage type. `dtype`, `text_config.dtype`, `audio_config.dtype` and `vision_config.dtype` read
  `bfloat16` in the original and `float16` in the copy, and every tensor in the weight file is float16. A true
  difference the card does not mention, correctly read.
- Pair 2: ten fields. The 5.16 `per_layer_config` form (the eighth copy on it), closed by hand; three token ids
  (`bos_token_id` 2 against null, `eos_token_id` 1 against [1, 106], `pad_token_id` 0 against null) written
  through by the fine-tune's save in `config.json` and the tokenizer's special ids, a loader's defaults as
  finding 15 read; and a 17,336-byte template of Google's earlier format under a 07-20 pin, inherited from the
  fine-tune. The cluster's original-side render timed out at the worker's four seconds, the first such timeout.
- Pair 3: a template the copy does not ship. No `chat_template.jinja` and none in the tokenizer configuration;
  the tool records "chat template missing". A loader falls back to no template.

Every fixed conversation in the round but pair 2's and pair 3's renders identically.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Composed edits, 32 and 42 flags (pairs 5 and 8): first shares of 0.54 to 0.76 on the layers both edits reach,
  where the fourth cumulative share is 0.993 to 0.999 and the two directions are the two scales; on pair 8 two
  within-layer cosines on layer 9, where the writers carry the two directions in different proportions. An entry
  for a composed edit would read the fourth share and a scale per direction.
- A fine-tune under a kernel pair, 360 flags (pair 2): 205 unexpected changes on the queries, keys, values, gates,
  up projections and vectors, 75 first shares of 0.003 to 0.988, 79 direction cosines and one cross-kind flag.
  As finding 18's pairs, the parent must be measured as a separate term.
- The floor on weak edits, 18 and 5 flags (pairs 3 and 6): first shares of 0.976 to 0.990 on attention outputs
  changed by 0.9 to 1.4 percent and queries changed by 1.4 to 1.5 percent.
- No flag on pairs 1, 4 and 7, three copies from two makers whose cards state the writers, the layers and the
  scale.

The round's finding for the measure is pair 1: the same edit size that reads first shares of 0.989 to 0.993 on
every bfloat16 copy reads 0.9999 on a float16 save, which is finding 3's storage floor confirmed from the other
side, on a copy whose configuration declares the type change the card omits.

## Owed to the metadata tool

Added since: nothing this round. What remains: the 5.16 `per_layer_config` form as the library's own save (pair
2, the eighth time); a reading of a storage-type change as what it is (pair 1: the four `dtype` fields agree with
the weight file, so "unexplained" understates it); a note when the copy ships no template (pair 3); and a
`base_model` check that reads a README's second card (pair 2, where the true parent is named in the file and not
in the field, finding 48's third case). The template worker's four-second limit should be raised for the E4B's
original file (pair 2's timeout).

## Operational

The pull of 11-01 18:57Z carries the eight measurement folders (card, metadata, weights, direction vectors and the
sha256 record of each) and the sweep record; no job log came home, so the jobs' numbers, nodes and seconds are
not in this note. Every compare finished with its card and its weights report, and the sweep ran after all eight
and deleted the seven originals. The cluster's template worker timed out once (pair 2, the original side, four
seconds). The home judgement ran under transformers 5.22.1.

Weight differences alone cannot certify the absence of hidden behavior.
