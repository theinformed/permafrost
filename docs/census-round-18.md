# Census round 18: eight Gemma 4 and Magistral pairs (2026-10-31)

Eight published copies compared with their stated originals on Nautilus, 2026-10-31, from the batch pinned as
`data/batches/round-18-batch-1.json`: push card 5473, round card 5477, download job 4125751 (finished 06:35Z),
compares 4125752 to 4125759 on the background queue (06:43Z to 07:09Z), sweep 4125760 (07:09Z, exit 0), which
deleted the six original checkpoints (`5926caa4` and `707f0a3b` of the 12B original, one weight file under two
revisions; `419b2efe` of the 31B original, shared by pairs 3 and 4; `47b6801b` of the 26B-A4B original;
`b4a60110` of the E2B original; `a31cc96a` of Magistral Small 2509, shared by pairs 7 and 8). Card 5493 pulled the
measurements home. This was the first round on the repaired compare script, and every compare posted its drop
record. The eight measurements were re-scored at home with the recipe table as committed and the saved direction
vectors, and no flag count moved. Every metadata report was judged again at home under transformers 5.6.2 with the
originals' commit histories. Each pair has a card (the tool's Stage 1 text after the home judgement, with the Stage
2 line) and a reading note in `docs/cards/`; the measurements are in `results/weights/` and `results/meta/`, and
the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/nautilus18/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | coder3101/gemma-4-12B-it-heretic | google/gemma-4-12B-it | violations, 170 flags (energy shares, within-layer directions) | consistent: arbitrary-rank edits on the attention outputs and down projections of layers 2 to 44, input side, searched weights 0.92 to 3.90 on 51 matrices, 35 rewritten under the threshold; the maker's first copy to edit the down projections; rows moved 0.007 under a preservation claim |
| 2 | 3MPER0RR/gemma-4-12b-it-3MPER0RR-abliterated | google/gemma-4-12B-it | violations, 5 flags | consistent with the card's own table: 48 matrices (29 attention outputs, 19 down projections), one shared direction, rank one at the floor, a per-layer strength that follows no kernel and reads no side; 629 tensors equal the original, where the maker's Mistral 7B copy changed every matrix |
| 3 | prithivMLmods/gemma-4-31B-it-Uncensored-MAX | google/gemma-4-31B-it | violations, 52 flags (floor) | consistent as far as the census can test: one shared direction at weight 1.00 on all 120 residual writers, output side; the card names huihui-ai's first 31B version, which is unmeasured, and the second version is ruled out field by field |
| 4 | null-space/gemma-4-31b-it-abliterated | google/gemma-4-31B-it | violations, 80 flags (energy shares) | consistent in every stated number: eight directions per matrix on the 80 writers of layers 20 to 59, the card's per-layer scale of 0.35 to 1.35 read to two decimals from the kept fraction, two shared direction sets; every small file byte-equal to Google's |
| 5 | WWTCyberLab/gemma-4-26B-A4B-it-abliterated | google/gemma-4-26B-A4B-it | violations, 51 flags | consistent in kind: one or two directions on the attention output, shared down projection and all 128 experts' down projections of 18 layers (the card names 13 layer passes), output side, weight near 1 where the card says 4.0 and 3.0; exactly 13 token-embedding rows scaled to one sixth, as the card says; the second edit of this base to reach the experts |
| 6 | prithivMLmods/gemma-4-E2B-it-Uncensored-MAX | google/gemma-4-E2B-it | match, 0 flags | consistent as far as the census can test: one shared direction at weight 1.00 on the 50 writers of layers 10 to 34, the layer set huihui-ai's E2B card states; that copy is unmeasured; the template is Google's release file, the earlier-revision case |
| 7 | llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v2 | mistralai/Magistral-Small-2509 | violations, 91 flags (energy shares, within-layer directions) | consistent: arbitrary-rank edits on 26 down projections and 23 attention outputs of layers 9 to 36, input side, weights 1.69 to 4.71, seven in-range matrices rewritten under the threshold; the token side is a third party's conversion of an original that ships no library tokenizer |
| 8 | grayarea/Magistral-Small-2509-Heretic-v1.2 | mistralai/Magistral-Small-2509 | violations, 13 flags (floor) | consistent: one shared direction on 34 attention outputs and 30 down projections of layers 6 to 39, output side, weight 1.24 to 1.35 on the attention outputs and a 0.51 to 1.39 to 1.13 kernel on the down projections; rows moved 0.003 to 0.011 under a "full row renormalization" claim; the same conversion on the token side |

Nothing moved outside the matrices the maker's method reaches in any pair: the largest relative change outside
the changed set is exactly 0 in pairs 1, 2, 3, 4, 5, 6 and 8 and 0.00031 in pair 7, on an in-range attention output
the search weighted near zero. The round's result is six copies that read as their cards say and two whose cards
name a parent the census has not measured. Pair 4 is the fullest agreement between a card and a weight file in the
census: layer range, direction count, component list and the per-layer scale all read back, the scale to the second
decimal on both writers of every layer (0.35 on layers 20 to 26, 1.35 at the peaks of layers 41 and 58). Pair 5
agrees in kind and differs in count: 18 layers where the card names 13 layer passes, and a kept fraction near 0
(weight near 1) where the card's scales are 4.0 and 3.0; its 13 scaled embedding rows are exactly the card's 13.
Pair 2's card is a weight-comparison table and nothing else, and the table is right to the tensor (48 changed, 29
layers). Pairs 7 and 8 are two Heretic configurations on one base and share no equal field in 288: arbitrary rank on
the input side with a residue set against one shared direction on the output side with a kernel.

The weights read off the weights: 1.00 on pair 3's 120 matrices (−0.001 to 0.008 remaining) and on pair 6's 50
(−0.000 to −0.005), the first weight-1.0 readings on a copy that names huihui-ai as its parent; searched per-layer
weights of 0.92 to 3.90 on pair 1's input side and 1.69 to 4.71 on pair 7's, left above right on all 100; pair 4's
schedule of 0.35 to 1.35; pair 8's 1.24 to 1.35 on 32 of 34 attention outputs and a kernel of 0.51 to 1.39 to 1.13 on
the down projections. Pair 2 reads no weight and no side: −0.20 to 0.96 kept on the left and 0.02 to 0.89 on the
right, the left below the right on 24 of 48, with no shape across the layers. Pair 5 reads a weight near 1 on every
layer matrix and on the median expert (−0.13 to 0.17 kept), and the embedding reads 0.16666 kept along each of eight
directions, a division by six on 13 rows.

Two preservation claims and one new direction count. Pair 1's rows moved by 0.0057 to 0.0079 under coder3101's
row-norm preservation, the band finding 22 reads on the maker's three other bases; pair 8's moved by 0.0026 to 0.0107
under a "full row renormalization", a second maker's restoration step reading as a leftover. Pair 4's eight
directions carry 0.94 to 0.996 of each change with the first at 0.58 to 0.69, the first subspace edit in the census
with its rank stated in the card (round 16's aifeifei798 copy had two or three per matrix and no card number), and
its rows moved by 0.025 to 0.098 on layers 20 to 51 and 0.002 to 0.006 on 52 to 59 under one norm-preservation
claim.

Fingerprints. Seven measurements of six makers' copies now stand on the one 26B-A4B weight file (TrevorJS twice,
huihui-ai, coder3101, llmfan46, prithivMLmods and WWTCyberLab) and no changed matrix of pair 5 has an equal
measurement in any field of the six others; two of the seven reach the experts, TrevorJS's on all 30 layers and
WWTCyberLab's on 18. Seven copies stand on the one 31B weight file (wangzhang, llmfan46, coder3101, TrevorJS,
huihui-ai's second version, prithivMLmods and null-space), and pairs 3 and 4 share no field with any of the five
earlier ones or with each other but one largest absolute difference, a single bfloat16 value of null-space's
layer 54 coinciding with TrevorJS's. Pair 3 against huihui-ai's second version is the test the card invites and it
fails on every field, which fits the card: the first version is named, it edits every layer where the second leaves
five alone, and its weights went up 77 minutes before pair 3's. Pair 6 against the two E2B copies measured (llmfan46,
aifeifei798) shares no field; huihui-ai's E2B copy, the named parent, is unmeasured. Pairs 1 and 2 against the four
earlier 12B copies on the same file share nothing but a handful of largest absolute differences on residue matrices
(10, 12 and 2, single bfloat16 steps). The re-upload test of finding 9 therefore has no new positive this round and
two cases that wait on their parents: both prithivMLmods copies read as a weight-1.0 shared projection on the layer
set the named huihui-ai card states, with timings five days and 77 minutes after the parents' uploads.

## The token side

The cluster's cards read "consistent" on pair 4, "consistent with re-save noted" on pair 5, and "unexplained
differences" on the six others. Re-judged at home, one field closes by tool on pairs 3 and 6
(`config.text_config.moe_intermediate_size`, the 5.6.2 default) and two on pair 7 (the `rope_parameters` blocks),
pair 3's card moves to "consistent with re-save noted", and the rest close by hand:

- Nothing to close, pair 4: every small file equals Google's at the pin byte for byte. Re-save only, pair 5: 5.5.0.dev0
  to 5.5.0 in two version strings.
- A 5.10 save under the same version, pair 1: both files say 5.10.0.dev0, the copy lacks the four class defaults of
  finding 11 (640, 640, 640, 48) and repeats `bfloat16` in the three sub-configurations. Google's file was written by
  hand with the defaults in it; the save omits them. The template is the pinned one byte for byte.
- A 5.16 save, pair 2: the same four defaults and three repeats, the version 5.10.0.dev0 to 5.16.1, and the text
  configuration's `global_head_dim` 512 and `num_global_key_value_heads` 1 moved into a `per_layer_config` map under
  the global layers' indices. The per-layer head map finding 15 met on a loader's save is also the newer library's
  own form, with no `unsloth_fixed` beside it. The template is the pinned one byte for byte. The map could not be
  loaded at home (transformers 5.6.2 has no `gemma4_unified` class).
- A re-save of the release files, pair 3: two version strings and the tool-closed field; the template is Google's
  release file, which is the pin.
- The earlier-revision case, pair 6: the template (11,926 bytes) equals Google's E2B release template of 2026-04-02
  byte for byte where the pin is the 2026-04-10 revision (16,317 bytes), because the copy's files are those of the
  huihui-ai repository created on 2026-04-08, whose template is the same release file with carriage-return line
  endings. The fifth earlier-revision case in the census and the first arrived at through a re-upload. The fixed
  conversation renders identically.
- An original without a library tokenizer, pairs 7 and 8: Magistral Small 2509 ships `tekken.json` and
  `params.json` and no `tokenizer.json`, tokenizer configuration, special-tokens map or chat template, and both
  copies ship the four, taken from unsloth/Magistral-Small-2509: pair 8's `tokenizer.json` and template equal that
  repository's files at its 2025-09-29 revision byte for byte, pair 7's template is the same file with 104
  carriage returns and its tokenizer and configuration are a 5.3.0 re-save of the same conversion. Both carry the
  conversion's `unsloth_fixed`, the three token ids written into the configuration, and the original's
  `SYSTEM_PROMPT.txt` as it stood before its 2025-12-02 revision. The 1,033 and 2,027 fields are the 1,000 special
  tokens listed once or twice, the ids the original's own format assigns, and the conversion's configuration
  fields; none is a change the original can be compared on, and the two templates render the fixed conversation to
  the same string. Pair 8's configuration adds a `grayarea` block naming the maker's Heretic configuration and
  dataset.

No copy this round declares a pretrained base under an instruct name, and no template is a blank-line-normalised
or patched Google file: four of the six Gemma 4 copies carry the template they were pinned against (pairs 1, 2, 3
and 4), one carries Google's release file at an earlier revision (pair 6) and one the pinned release file (pair 5).

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Arbitrary rank, 170 and 91 flags (pairs 1 and 7): first shares 0.908 to 0.978 and 0.841 to 0.971 on the edits,
  0.002 to 0.188 on pair 1's 35 residues, and within-layer cosines of 0.0004 to 0.26 and 0.003 to 0.18, counted on
  both writers. Ten copies of the method are now measured, all on the input side; these two are the first to edit
  the down projections beside the attention outputs, so the candidate entry's component list widens.
- The floor, 52 and 13 flags (pairs 3 and 8): first shares 0.989 to 0.993 on changes of 0.012 to 0.016 and 0.967
  to 0.993 on changes of 0.008 to 0.019, leftover 0.0013 to 0.0016 of the norm, every matrix inside the 0.0025 line.
- Eight directions, 80 flags (pair 4): first shares 0.58 to 0.69 with the first eight at 0.94 to 0.996 and the first
  singular value 1.7 to 2.8 times the second, read by the energy-share rule as 80 failed projections. A first-k share
  with k read from the singular values, or from the card, names it as one number per matrix (round 16 asked for the
  same on the two- and three-direction copy).
- Two passes and an embedding, 51 flags (pair 5): 36 energy shares on the ten two-direction layers and the
  embedding, 15 within-layer directions where the three writers of a two-direction layer lead with different
  members of the pair. The embedding's 13 scaled rows read as a first share of 0.245 with eight near-equal singular
  values, which the rule reports as a failed projection; a row-count test (rows whose norm changed by a fixed
  factor) would name it.
- A strength without a side, 5 flags (pair 2): two cross-layer cosines at 0.90 and 0.91, two first shares at 0.980
  and 0.990, one cross-kind direction, on a shared direction whose kept fraction wanders from −0.20 to 0.96 with no
  kernel. The entry matched the shape and reported the band; the reading adds that the measurement reads no weight.
- Nothing, on pair 6: `single-projection-selected` matched the weight-1.0 edit with the first ten layers as the
  unchanged subset.

The remaining fraction read a weight on six of the eight (1.00, 1.00, 0.92 to 3.90, 1.69 to 4.71, the 0.35 to 1.35
schedule, and 0.92 to 1.39), near 1 on pair 5 under a card that states 4.0 and 3.0, and none on pair 2. It read the
side on seven: input on pairs 1 and 7 (left above right on all 100), output on pairs 3, 4, 5, 6 and 8 (left below
right on all 368 layer matrices), and neither on pair 2 (24 of 48). It read a per-layer scale schedule for the first
time, on pair 4, to the second decimal, and a row scaling on an embedding, on pair 5, to five digits (0.16666).

Three things the comparison could say by itself. A rank per matrix from the singular values (pair 4's eight, pair
5's one or two, round 16's two or three) in place of a pass line on the first share. A row-change test on
embeddings and heads (rows moved, factor if constant) beside the direction measures, which would have reported pair
5's embedding as "13 rows scaled by 0.1667" and byroneverson's patch of finding 6 as its row set. And on the token
side, a lookup of the copy's tokenizer files against every conversion the census has cached when the original ships
none, which would have closed pairs 7 and 8 by naming unsloth/Magistral-Small-2509 and its revision.

## Owed to the metadata tool

The earlier-revision rule (pair 6, the fifth case, the first through a re-upload); the 5.10 class-default list and
the dtype repeats as one cause (pairs 1 and 2, seven fields each); the 5.16 `per_layer_config` form as the library's
own save, distinct from the loader's (pair 2); a conversion lookup for originals that ship no library tokenizer,
naming the repository and revision whose files the copy carries (pairs 7 and 8, 3,060 fields between them); and a
rendering comparison between two copies of one original when the original has no template to render. To the batch:
huihui-ai/Huihui-gemma-4-31B-it-abliterated (the first version) and huihui-ai/Huihui-gemma-4-E2B-it-abliterated, the
two named parents of this round's prithivMLmods copies, for the fingerprint test of finding 9; and
unsloth/Magistral-Small-2509 against mistralai/Magistral-Small-2509, to measure the conversion itself once, so that
every later Mistral copy on it can be read against a measured intermediate.

Weight differences alone cannot certify the absence of hidden behavior.
