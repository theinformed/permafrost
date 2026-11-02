# Census round 32: eight Gemma 4 pairs, the first on the QAT originals (2026-11-01)

Eight published copies compared with their stated originals on Nautilus, 2026-11-01, from the batch pinned as
`data/batches/round-32-batch-1.json`: push card 5667, round card 5668, download job 4145233 on the transfer node,
compares 4145234 to 4145241 on the background queue, sweep 4145242, which deleted the seven original checkpoints
(`b2a81a03` and `20da991a` of the 26B-A4B instruct original for pairs 1 and 2; `b324173c` and `b4a60110` of the E2B
original for pairs 3 and 7; `58540658` of the 12B QAT-unquantized original for pair 4; `f1e06dc5` of the 26B-A4B
QAT-unquantized original for pairs 5 and 8; `d40c88a0` of the E2B QAT-unquantized original for pair 6). This is the
first batch pinned by the pinner that refuses copies whose weight files equal a measured copy (it refused seven),
and the first round with pairs on the three QAT-unquantized originals, which held no measurement before it. Card
5690 pulled the measurements home after the Kerberos hold, card 5676 the logs. The eight measurements were
re-scored at home with the recipe table as committed and the saved direction vectors, and no flag count moved. Every
metadata report was judged again at home under transformers 5.22.1 with the originals' commit histories, and the
committed reports carry that judgement. Each pair has a card (the tool's Stage 1 text after the home judgement, with
the Stage 2 line) and a reading note in `docs/cards/`; the measurements are in `results/weights/` and
`results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/nautilus32/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | sh0ck0r/gemma-4-26B-A4B-it-heretic | google/gemma-4-26B-A4B-it | violations, 19 flags (seven first shares 0.967 to 0.988, twelve within-layer cosines 0.88 to 0.95) | the card's Heretic 1.3.0 kernels to the layer: one direction per matrix on the attention outputs of layers 9 to 29 and the down projections of 13 to 29, output side, no expert reached; the strengths read back in shape, shallower than the card by 0.04 to 0.12 across the centre of both windows and by up to 0.5 at their edges |
| 2 | BinxNet/gemma-4-26B-A4B-it-heretic | google/gemma-4-26B-A4B-it | violations, 21 flags (five first shares 0.985 to 0.989, sixteen within-layer cosines 0.88 to 0.95) | the card's Heretic 1.4.0 kernels to the layer: the attention outputs of layers 5 to 29 and the down projections of 11 to 29, output side, no expert; the strengths read at about half the card's depth, under the version's rank-three row normalisation |
| 3 | DavidAU/gemma-4-E2B-it-The-DECKARD-HERETIC-UNCENSORED-Thinking | google/gemma-4-E2B-it | violations, 276 flags (135 unexpected changes, 70 first shares 0.54 to 0.97, 70 direction cosines, one cross-kind) | "uncensored, then fine tuned", as the card says: all seven projections of all 35 layers changed by 0.2 to 4.8 percent in a low-rank shape, no vector and no embedding moved, the ablation still readable on the attention outputs of layers 16 to 31; the maker's template writes a `<\|think\|>` line after the generation prompt (finding 49) |
| 4 | huihui-ai/Huihui-gemma-4-12B-it-qat-q4_0-unquantized-abliterated | google/gemma-4-12B-it-qat-q4_0-unquantized | match, 0 flags | huihui-ai's shared projection at weight 1.0 on the attention outputs and down projections of layers 23 to 36, the card's window, output side: the 12B edit's method on the QAT checkpoint, reaching eight layers more than it did on the instruct file (finding 21) |
| 5 | mewse/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ara | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | violations, 25 flags (24 within-layer cosines 0.009 to 0.13, one first share 0.932) | the card's arbitrary-rank window (layers 11 to 22) on both writers, input side, right-side weights 1.56 to 4.35 on the attention outputs and 1.23 to 2.33 on the down projections, unrelated directions per matrix, rows moved up to 0.25; the `base_model` field names the instruct model, the README the QAT checkpoint (finding 48) |
| 6 | coder3101/gemma-4-E2B-it-qat-q4_0-unquantized-heretic | google/gemma-4-E2B-it-qat-q4_0-unquantized | violations, 17 flags (first shares 0.012 to 0.966) | the card's arbitrary-rank window (layers 6 to 23) on the attention outputs alone: nine edited (input side, right-side weights 1.75 to 3.12) and eight touched at the bfloat16 floor, with layer 6 under the threshold; rows within 0.008, the maker's preservation band (finding 22); no down projection changed |
| 7 | amkkk/Gemma4_E2B_Abliterated_Baked_HF_Ready | google/gemma-4-E2B-it | violations, 136 flags (40 first shares 0.977 to 0.990, 48 within-layer cosines, 48 unexpected changes on gate and up projections) | an ablation whose parameters are written into `config.json` and read back from the weights: strengths 1.0, 1.0, 1.2 and 1.2 on four writers read as right-side kept fractions 0.00, 0.00, -0.20 and -0.20 within 0.003 on all 96 matrices, the stated layer list exactly (finding 47); the export drops the 60 shared-KV tensors of layers 15 to 34 |
| 8 | OS-Software/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic-v2 | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | violations, 32 flags (16 first shares 0.75 to 0.96, 16 within-layer cosines 0.002 to 0.12) | the card's Heretic 2.0 rank-four transport window (layers 12 to 19) on both writers: fourth cumulative share 0.998 to 0.9995, input side, right-side weights up to 2.45, rows unrestored, unrelated directions per matrix, as the maker's E4B copy read in round 30 (finding 42), now on the QAT checkpoint; the `base_model` field names the instruct model |

Nothing moved outside the matrices the maker's method reaches in any pair: the largest relative change outside
the changed set is exactly 0 in pairs 1, 2, 3, 4, 5, 7 and 8, and 0.00077 in pair 6, on the attention output of
layer 6, the first layer of the card's window, which the search weighted to nothing. The round's result is eight
edits and no re-upload, the first such round since the pinner's duplicate check. Six of the eight read as their
cards say to the number (pair 7 in every strength and every layer, pair 4 in window and weight, the three arbitrary-rank pairs (5, 6, 8) in
window and side, pair 1 in window and in the shape of both kernels), one (pair 2) reads its windows and about
half its strengths, and one (pair 3) reads an ablation under a fine-tune, which is what its card says in five
words. Three pairs stand on QAT-unquantized originals that the census had not measured: the checkpoints Google
extracted from quantisation-aware training, in bfloat16, under names that end in `-qat-q4_0-unquantized`. Two of
the three copies (pairs 5 and 8) name the plain instruct model in their `base_model` field and the QAT checkpoint
in their README's first sentence; the pinner read the README. Measured against the QAT original, both read exactly 0
outside their windows. Measured against the instruct model the field names, the comparison would read the QAT retraining on
every matrix it moved, beside the edit (finding 48).

The weights read off the weights: per-layer output-side weights of 0.36 to 1.39 on pair 1's 21 attention outputs
and 0.35 to 0.98 on its 17 down projections (left below right on 36 of 38), 0.36 to 1.38 and 0.56 to 1.18 on pair
2's (42 of 44), weight 1.0 on pair 4's 28 matrices (left kept fraction within 0.005 of 0 on all 28), searched
input-side weights of 1.23 to 4.35 on pair 5's 24 edits (left above right on 24 of 24), 1.75 to 3.12 on pair 6's
nine edits (9 of 9), the config's 1.0 and 1.2 on pair 7's 96 (96 of 96), and rank-four weights of 0.68 to 2.45 on
pair 8's 16 (16 of 16). Pair 3's leading directions are the fine-tune's on the queries, keys, values and feed-forward
inputs (kept fractions 0.96 to 1.04 on both sides) and the ablation's on the attention outputs of layers 16 to 31
(left 0.65 to 0.97, right -0.47 to 0.39, where layers 0 to 15 and 32 to 34 read 1.0 on both sides).

Preservation claims. Pair 6's rows moved by 0.0005 to 0.0079 on its 17 attention outputs under coder3101's row-norm
preservation, the band finding 22 reads on the maker's four instruct copies (0.0057 to 0.0080), now on a QAT
original. Pair 2's rows moved 0.004 to 0.051 under Heretic 1.4.0's `row_normalization = "full"` with a rank-three
correction, which is not a restoration in the sense the measure reads (every matrix of the 44 differs from the
original in its row norms by more than the 0.0004 TrevorJS's restoration leaves). Pairs 5 and 8 carry no claim and
moved their rows 0.007 to 0.25 and 0.011 to 0.047.

Fingerprints. Thirteen measurements now stand on the 26B-A4B instruct original; pairs 1 and 2 share their first two
shards (`a868d472`, `a3de0db5`), the library's 11-shard layout of the embeddings and the first eight layers that
neither edit touches, and no measured field; pair 1 shares its first shard with SevenOfNine's copy for the same
reason. Seven stand on the E2B instruct original; pair 7 shares its first two shards with huihui-ai's E2B file (as
prithivMLmods's duplicate carries it) and with aifeifei798's copy, the same sharding of the per-layer embeddings,
and no field with either (0 of 50 of huihui-ai's changed tensors equal). The three QAT originals carry one
measurement each but the 26B-A4B's, which carries two that share nothing.

## The token side

The cluster's cards read "consistent" on pair 4 (a copy whose configuration, generation settings and token files
equal the original's field for field, version strings included), "consistent with re-save
noted" on three pairs (1, 2, 6), and "unexplained differences" on the four others (3, 5, 7, 8), every one of them on configuration
or template fields and none on a weight. Re-judged at home under transformers 5.22.1, one field moves (pair 7's
`text_config.moe_intermediate_size`, null in a 5.5.3 save, closed by the default rule) and no card changes its
reading. The four stay as printed, for these reasons:

- Pair 3: a template the maker changed in the generation prompt. The copy's
  16,352-byte `chat_template.jinja` (`c74f3aa5`) is Google's 16,804-byte file of the pin with one edit: a
  `<|think|>` line emitted after the generation prompt, so the fixed conversation renders one line longer than the
  original's. The commit "Update chat_template.jinja" of 05-17 is the maker's, a day after the upload. Nothing to
  close: the field reads as what it is.
- Pairs 5 and 8: the 5.16 save form (finding 39). `global_head_dim` 512 and `num_global_key_value_heads` 2 leave the
  text configuration and return as a `per_layer_config` map under the five global layers' indices, written by
  5.15.0 and 5.16.1 saves against the QAT original's 5.6.2 file. The fifth and sixth copies on this form; closed by
  hand. Pair 8's template differs from Google's 18,683-byte file in line endings alone (19,073 bytes) and the tool
  closed it.
- Pair 7: twelve fields the maker added to `config.json` to document the edit (`ablation_layers`,
  `ablation_scope`, `ablation_strength`, `direction_source`, `direction_source_layer`, `export_source_model`,
  `export_type`, `mlp_down_strength`, `mlp_gate_strength`, `mlp_up_strength`, `self_attn_o_strength`,
  `target_weights`), with an `export_manifest.json` beside them that repeats the values. The fields are the card;
  the weights agree with every one of them (finding 47). Nothing to close.

The three re-save pairs (1, 2, 6) differ from their originals in the two version strings and nothing else. Every fixed conversation
in the round but pair 3's renders identically.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Per-layer directions, 19 and 21 flags (pairs 1 and 2): first shares of 0.967 to 0.989 on the down projections
  nearest the window's edge, where the kernel's weight is smallest and the change 0.7 to 1.3 percent of the norm,
  and within-layer cosines of 0.88 to 0.95 on the layers where the two writers' directions agree least. Both
  copies fit the `directional-per-layer-selected` entry's shape; the 0.95 within-layer line counts Heretic's
  per-layer directions as violations on about half the layers of every per-layer copy measured.
- The fine-tune, 276 flags (pair 3): 135 unexpected changes on the queries, keys, values, gates and up projections,
  70 first shares of 0.54 to 0.97 on the attention outputs and down projections, 70 direction cosines of 0.03 to
  0.65, and one cross-kind flag. An ablation-then-training pair, as finding 18's training-then-ablation pair, needs
  the training measured as a separate term before any recipe can fit.
- Arbitrary rank, 25 flags (pair 5): within-layer cosines of 0.009 to 0.13 on all 12 layers, counted on both
  writers, and one first share of 0.932 on layer 20's down projection; every other edit is rank one (first share
  0.991 to 0.999) along its own direction.
- Arbitrary rank on one writer, 17 flags (pair 6): first shares of 0.012 to 0.021 on the eight floor matrices,
  where the leading direction of a 0.1 percent bfloat16 residue carries nothing, and 0.94 to 0.97 on the nine
  edits. The entry would read this copy if the floor matrices were set aside as finding 40's were.
- Four writers on the input side, 136 flags (pair 7): 48 unexpected changes on the gate and up projections, which
  no entry lists as writers, 48 within-layer cosines of 0.11 to 0.71 (three inputs per layer: the gate and up
  projections share theirs at 0.92 to 0.97, the attention output and the down projection each read their own), and 40 first shares of 0.977 to 0.990 on the attention outputs and down
  projections at the floor. An entry for a per-module input-side projection with four writers would count none.
- Rank four, 32 flags (pair 8): first shares of 0.75 to 0.96 on all 16 edits, where the fourth cumulative share is
  0.998 to 0.9995, and within-layer cosines of 0.002 to 0.12. The `transport-rank-k` entry round 30 described for
  the maker's E4B copy would fit this one with no flags.

The round's finding for the measure is pair 7: when a maker writes the strengths into the configuration, the
right-side kept fraction returns them to the third decimal on every matrix of four writers, which is the cleanest
read-back the census has, and the recipe table still counts 136 flags because no entry names those writers or that
side. The table lags the makers by one kind of edit per round.

## Owed to the metadata tool

Added since: nothing this round. What remains: the 5.16 `per_layer_config` form as the library's own save (pairs 5
and 8, the fifth and sixth times); a rule that reads a maker's documentation fields in `config.json` as
documentation (pair 7's twelve, which no library writes and no loader reads); a note in the card when a template
changes the rendering (pair 3, where "unexplained" understates it); and a `base_model` check that names the QAT
checkpoint when the README does (pairs 5 and 8, which the pinner handled by hand). To the batch: the remaining
QAT-unquantized copies at every size, now that the originals are known to pair.

## Operational

The round ran on the kit whose printed messages fit 100 columns. The download fetched the eight copies and seven
originals, planned at 438.6 GB, on nautilus-xfer03 in 8,088 seconds (00:55:55Z to 03:10:43Z), of which the hub
fetch took 2 hours 9 minutes 11 seconds. The compares ran 1,367 and 1,394 seconds on the two 26B-A4B instruct
pairs, 284 on the DavidAU pair, 715 on the 12B QAT pair, 1,369 and 1,350 on the two 26B-A4B QAT pairs, 363 on the
E2B QAT pair and 399 on the amkkk pair; the sweep took 1 second. All ten jobs exited 0. Pair 3's compare finished
its measurement and its card and then missed the desk at its report-home step, a DNS failure on r07u03n01, so the
desk saw no drop for 4145236 until the logs came home; the sweep ran behind it on the queue's own accounting and
deleted its original. Every compute node printed its facts (cores: 1 visible, grant 128; 257,717 MB memory); the
compares built the compute environment from the staged wheels under the system's Python 3.11.0 module, and the
cluster's library was transformers 4.56.2 (no Gemma 4 class), the home judgement 5.22.1.

Weight differences alone cannot certify the absence of hidden behavior.
