# Census round 20: eight Gemma 4, Magistral Small and Mistral 7B pairs (2026-11-01)

Eight published copies compared with their stated originals on Nautilus, 2026-10-31 to 11-01, from the batch pinned as
`data/batches/round-20-batch-1.json`: push card 5644, round card 5646, download job 4143641 on the transfer node,
compares 4143642 to 4143649 on the background queue, sweep 4143650, which deleted the six original checkpoints
(`35487898` and `842da379` of the 31B original for pairs 1 and 2; `707f0a3b` of the 12B original for pairs 3 and 4
and `66bc78a7` for pair 5; `b2a81a03` of the 26B-A4B original for pair 6; `a31cc96a` of Magistral Small 2509 for pair
7; `0d4b76e1` of Mistral 7B Instruct v0.3 for pair 8). The desk let the round run as placed after the duplicate check
of 11-01 00:04Z had named pairs 3 and 4 as measured files, because the download had already been fetching for an
hour. Card 5681 pulled the measurements home after the Kerberos hold. The eight measurements were re-scored at home
with the recipe table as committed and the saved direction vectors, and no flag count moved. Every metadata report
was judged again at home under transformers 5.22.1 with the originals' commit histories, and the committed reports
carry that judgement. Each pair has a card (the tool's Stage 1 text after the home judgement, with the Stage 2 line)
and a reading note in `docs/cards/`; the measurements are in `results/weights/` and `results/meta/`, and the
direction vectors stay in the pull copy (`/opt/ai/hpc-packages/pulls/model-audit/nautilus20/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | ressl/gemma-4-31B-it-uncensored | google/gemma-4-31B-it | violations, 56 flags (54 first shares 0.975 to 0.990, two within-layer cosines 0.925) | one direction per matrix on every attention output and every down projection of all 60 layers, output side, rows restored within 0.0004, kept fractions 0.00 to 0.71: the reach and the restoration of TrevorJS's 31B copy on a new weight file, under a card that prints refusal counts and no method |
| 2 | sh0ck0r/Artemis-31B-v1.1-heretic | google/gemma-4-31B-it (the README names TheDrummer/Artemis-31B-v1.1) | violations, 686 flags (482 unexpected changes, 121 first shares 0.002 to 0.047, 82 direction cosines, one cross-kind) | every matrix in the model changed by 8.7 to 10.4 percent and no vector: the named parent is a 4-bit round trip of Google's weights with adapters merged, read from the hub by range (finding 45); the Heretic 1.4.0 kernel's direction still reads on the down projections of layers 17 to 54 |
| 3 | Ishowbackup/gemma-4-12B-it-uncensored | google/gemma-4-12B-it | violations, 1 flag (floor) | TrevorJS/gemma-4-12B-it-uncensored's weight file under a fourth name: a hub duplicate, LFS checksum `dd7fcab672`, every field equal to the round 8 report and to the two round 19 duplicates |
| 4 | Ishowbackup/Huihui-gemma-4-12B-it-abliterated | google/gemma-4-12B-it | match, 0 flags | huihui-ai's 12B weight file under a third name: a hub duplicate, LFS checksum `2dd13d8676`, every field equal to the round 13 report and to TimelessSoul's round 14 duplicate |
| 5 | MoonRide/gemma-4-12B-it-heretic | google/gemma-4-12B-it | violations, 7 flags (four first shares 0.978 to 0.990, two cosines 0.90 to 0.91, one cross-kind 0.63) | one shared direction, rank one, on the attention outputs of layers 17 to 47 and the down projections of 27 to 47, the card's Heretic 1.3.0 windows to the layer; the kept fraction reads neither the kernel's strengths nor a side, the third 12B copy to read this way (finding 46) |
| 6 | prithivMLmods/gemma-4-26B-A4B-Heretic-Stable | google/gemma-4-26B-A4B-it | match, 0 flags | huihui-ai/Huihui-gemma-4-26B-A4B-it-abliterated's weights re-sharded into five files: every field equal to the round 13 report and to prithivMLmods's Uncensored-MAX copy, the card says so, the checksums do not |
| 7 | llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v1 | mistralai/Magistral-Small-2509 | violations, 32 flags (18 first shares 0.75 to 0.96, 14 within-layer cosines 0.003 to 0.12) | the card's arbitrary-rank window (layers 16 to 26 of 40) on both writers, input side, right-side weights 1.55 to 2.43 on the attention outputs and 1.29 to 2.20 on the down projections, unrelated directions per matrix; four attention outputs of 23 to 26 touched under the threshold |
| 8 | DogOnKeyboard/Mistral-7B-Heretic | mistralai/Mistral-7B-Instruct-v0.3 | violations, 23 flags (down-projection first shares 0.976 to 0.990) | the card's Heretic 1.0.1 kernel as written: one shared direction (index 17.44), the attention outputs of layers 12 to 31 and the down projections of 7 to 31, all 45 strengths read back within 0.003; the first Heretic copy of this original |

Nothing moved outside the matrices the maker's method reaches in pairs 1 and 3 to 8: the largest relative change
outside the changed set is exactly 0 in six of those seven pairs and 0.00029 in pair 7, on four attention outputs of
layers 23 to 26 inside the card's window that the search weighted to nothing. Pair 2 is the exception by
construction: its changed set is every matrix in the model, because the parent the README names is itself a
changed copy of the pinned original. The round's result is five edits and three re-uploads. Three of the five edits
read as their cards say to the number (pair 8 in every kernel value, pair 7 in window and side, pair 5 in window
and direction count), one (pair 1) carries a card that prints no numbers to read, and one (pair 2) reads its
parent's quantisation before it reads its own edit. The three re-uploads are the hub's duplicate function twice
(pairs 3 and 4, "Duplicate from" in the one commit title of each, the parent's checksum on the weight file, both made
on 08-18 two minutes apart) and one re-save (pair 6), where prithivMLmods
loaded huihui-ai's file and saved it under five shards with a 5.9.0 version string, so no checksum matches the
parent and every measured field does. The pinner's duplicate check (finding 38) would have filed pairs 3 and 4 as
their parents' measurements; it cannot file pair 6, whose card names the parent in its first sentence.

The weights read off the weights: per-layer weights of 0.29 to 1.00 on pair 1's 60 attention outputs and 0.43 to
1.00 on its 60 down projections (output side, left below right on 118 of 120, rows back within 0.0004 on all 120),
searched input-side weights of 1.29 to 2.43 on pair 7's 18 edits (left above right on 18 of 18), the kernel's
1.12 to 1.44 on pair 8's attention outputs and 0.60 to 0.95 on its down projections (output side, 45 of 45), and
nothing on pair 5, where the kept fraction along the one shared direction runs from -0.26 to 0.97 on the attention
outputs and -0.25 to 0.73 on the down projections with the left below the right on 25 of 52. The duplicates read
what their parents read: weight 1.0 with the biprojection's second term on pair 3, weight 1.0 on pair 4, weight 3.0
on pair 6 (left kept fraction -2.00 on all 50 matrices, huihui-ai's number on this base, finding 21). Pair 2's
leading directions are the parent's noise on 440 of its 603 changed matrices and the Heretic direction on the
others; the reading note gives the layer-by-layer comparison with the card's kernel.

Fingerprints. Twelve measurements now stand on the 31B original and pairs 1 and 2 share no field with any of the
ten earlier ones or with each other. Pair 1 has the changed set of TrevorJS's 31B copy exactly (the same
120 tensors) and none of its values: the two edits differ in every kept fraction by up to 0.37 and in every largest
absolute difference. Seventeen measurements of copies stand on the 12B file; pairs 3 and 4 equal their parents'
reports in every field of all 677 tensors and carry the parents' checksums, and pair 5 shares its first two shards
with 3MPER0RR's and igorls's 12B copies, the library's sharding of the embeddings and the layers none of the three
edits touches, and no measured field. Pair 6 shares no checksum with huihui-ai's two-shard file and every field of
all 1,013 tensors. Pair 7 is llmfan46's first Magistral copy beside the v2 measured in round 18 on the same
original revision: 18 changed tensors against 49, no field shared. Pair 8 is the fourth copy on Mistral 7B
Instruct v0.3 after three abliterations (rounds 7 and 11) and the first Heretic.

## The token side

The cluster's cards read "unexplained differences" on all eight, every one of them on configuration or tokenizer
fields and none on a weight. Re-judged at home under transformers 5.22.1, two close by tool: pair 1 moves to
"consistent with re-save noted" on two fields (`text_config.moe_intermediate_size`, written as null by a 5.13.0
save where Google's file omits it, by the default rule; and the template, which is Google's own 07-15 revision
"fix: chat template" of the 31B repository, by the later-revision rule, the first time that rule has closed a
field in a round's own judgement), and pair 5 moves to the same reading on the 12B family's six fields (finding 39).
The six others stay as printed, for these reasons:

- Pair 2: the 5.16 save form (finding 39). `global_head_dim` and `num_global_key_value_heads` leave the text
  configuration and return as a `per_layer_config` map under the ten global layers' indices, as on 3MPER0RR's 31B
  copy in round 19. The fourth copy on this form; closed by hand.
- Pair 3: the template. The copy carries Google's 17,466-byte file of 06-03 (`36e3a42e`), TrevorJS's pin, under a
  pin (07-20) whose template is the 18,683-byte Canonical file (`ae53464b`): the earlier-revision case through a
  re-upload, as Justbackup's 12B copy in round 19, the eighth in the census. The six 12B family fields closed by
  tool. Closed by hand.
- Pair 4: the same earlier-revision template through the same re-upload, plus huihui-ai's own
  `text_config.max_position_embeddings` of 131,072 against Google's 262,144, the field the parent's report has
  carried open since round 13. The parent's reading, carried along.
- Pair 6: the template again, further back: the copy carries Google's 12,045-byte file of 04-02 (`2dfbfc7d`), the
  one huihui-ai's repository holds, under a pin (05-18) whose template is the 17,466-byte revision. The ninth
  earlier-revision case; the tokenizer configuration grew by 620 bytes between the two Google files. Closed by hand.
- Pair 7: an original without a library tokenizer (finding 31). Magistral Small 2509 ships `tekken.json` and no
  `tokenizer.json`, configuration or template; the copy carries unsloth's files, as llmfan46's v2 and grayarea's
  copy do on the same original, and the tool counts the whole added table against nothing. One field closed by
  tool at home (`text_config.rope_parameters`, written by a 5.3.0 save and absent from the 4.56.1 original, loads
  to the same default); `unsloth_fixed` and the three token ids are the conversion's, as before.
- Pair 8: a rename the scorer has no rule for. The copy's 4.57.1 save writes `dtype: bfloat16` where the original's
  4.42.0 file wrote `torch_dtype: bfloat16`; the library renamed the field between those versions and the two
  declare the same type. The template moved from `tokenizer_config.json` to `chat_template.jinja` and closed by the
  existing rule. Closed by hand; the rename rule is owed.

Every fixed conversation in the round renders identically, under the three earlier-revision templates as under the
pins.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Per-layer directions near the floor, 56 flags (pair 1): 54 first shares of 0.975 to 0.990 against the 0.99
  floor on matrices whose change is 1.4 to 2.5 percent of the norm, and two within-layer cosines of 0.925 on layer
  12. The edit is rank one everywhere (second cumulative share within 0.0008 of the first); the floor is a
  bfloat16 effect on 60-layer matrices, as on TrevorJS's and 3MPER0RR's 31B copies.
- The parent's noise, 686 flags (pair 2): 482 unexpected changes on the matrices no ablation reaches (every
  query, key, value, gate and up projection, the embeddings, the whole vision tower), 121 first
  shares of 0.002 to 0.047 where a full-rank 9 percent difference leaves the leading direction with almost nothing,
  82 direction cosines on the attention outputs and down projections whose leading direction is the Heretic one on
  some layers and the noise on others, and one cross-kind flag. A recipe cannot fit this pair; the parent must be
  measured first (finding 45).
- The floor, 1 flag (pair 3): TrevorJS's layer 42 attention output at 0.9899.
- A shared direction without a weight, 7 flags (pair 5): four first shares of 0.978 to 0.990, two cosines of 0.899
  and 0.906 to the group direction on layers 20 and 44, and one cross-kind direction at 0.627. The
  `single-projection-selected` entry matched the shape, and the reading adds that the kept fraction reads nothing
  (finding 46).
- Arbitrary rank, 32 flags (pair 7): first shares of 0.75 to 0.96 on all 18 edits, within-layer cosines of 0.003
  to 0.12 on the seven layers with both writers edited, counted on both: the shape of llmfan46's other ARA copies
  (finding 22).
- The floor, 23 flags (pair 8): first shares of 0.976 to 0.990 on 23 of the 25 down projections, whose change is
  0.95 to 1.6 percent of the norm under the kernel's 0.59 to 0.95; the attention outputs at 1.12 to 1.45 clear it.
  The Heretic 1.0.1 entry would need the 0.985 floor finding 41 named, or a floor that scales with the weight.

The round's own finding for the measure is pair 2 against pair 8: the leading-direction read gives the kernel to
the third decimal on a clean base (pair 8, 45 of 45 within 0.003) and gives the parent's quantisation instead on a
base that carries one (pair 2), with the ablation visible only where the kernel's weight is large enough to rise
above a 9 percent floor. Measuring sh0ck0r's copy against TheDrummer's file, not Google's, would read the edit
alone; the pinner follows the `base_model` field, which names Google.

## Owed to the metadata tool

Added since: nothing this round. What remains: the `torch_dtype` to `dtype` rename across 4.56 (pair 8, closed by
hand); the 5.16 `per_layer_config` form as the library's own save (pair 2, the fourth time); the earlier-revision
template through a re-upload (the three re-uploads, the seventh to ninth times), which needs the pinner to pair a
duplicate with its parent; a re-save check beside the checksum check, which would have filed pair 6 from its card's
first sentence; and a parent check in the pinner, which would have measured pair 2 against the parent its README
names instead of the grandparent its `base_model` field names. To the batch: TheDrummer/Artemis-31B-v1.1 itself,
whose 4-bit round trip is the round's finding and whose own repository is unmeasured.

## Operational

The round ran on the kit whose login half runs no storage probe. The download fetched the eight copies and six
originals on nautilus-xfer04 in 5,939 seconds (23:07:52Z to 00:46:51Z); its log did not come home, so the planned
size is not recorded here. The compares ran 2,557 seconds on the Artemis pair (every matrix compared), 664, 592 and
639 on the three 12B pairs, 1,257 on the 26B-A4B pair, 1,271 on the Magistral pair, 409 on the Mistral 7B pair;
the sweep took 1 second; the compare of pair 1 posted no drop to the desk, so its seconds are not known, and
its measurement and the sweep's deletion of its original both came home. All ten jobs that reported exited 0. The
cluster's library was transformers 4.56.2 (no Gemma 4 class), the home judgement 5.22.1.

Weight differences alone cannot certify the absence of hidden behavior.
