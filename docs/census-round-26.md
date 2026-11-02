# Census round 26: eight pairs on Blueback, three of them one file under three names (2026-11-02)

Eight published copies compared with their stated originals on Blueback from the batch pinned as
`data/batches/round-26-batch-1.json` (pinned 2026-10-31 18:41Z): the first Gemma 4 31B copy from a maker with its own
solver (Bahushruth), a Mistral 7B v0.3 heretic export (paoloronco), four E4B copies (Bahushruth, Pound1320, Cup4,
Cup5) and two E2B copies (anlord, Ishowbackup). The pull of 11-01 23:59Z brought home the eight measurement folders
and the sweep record and no job log, so the download, compare and sweep job numbers and their seconds are not
recorded in this note; the sweep deleted the four original checkpoints (`8ee0b411` of the 31B original for pair 1,
`ef77f2e4` of the Mistral 7B instruct original for pair 2, `0f830d9a` of the E4B original for pairs 3 to 6 and
`5e6bb5ba` of the E2B original for pairs 7 and 8) from `/p/work1/sdegan/model-audit/rounds/26/originals/`. The batch
was pinned before the duplicate rule (finding 38) and carries four measurements the rule would have refused: three
copies of one file under three accounts (pairs 4, 5 and 6) and a hub duplicate of TrevorJS's E2B edit (pair 8). The
pinner's note held back two copies (AgentAnon's 26B-A4B, which the hub refused to list for the account, and
darkc0de's Mistral Small 3.2 heretic, whose tensor names carry a prefix the kit of the time could not map; round 29
carries the first pair measured through that mapping). The eight measurements were re-scored at home with the
recipe table as committed and the saved direction vectors, and no flag count moved. Every metadata report was
judged again at home under transformers 5.22.1 with the originals' commit histories, and the committed reports
carry that judgement. Each pair has a card (the tool's Stage 1 text after the home judgement, with the Stage 2
line) and a reading note in `docs/cards/`; the measurements are in `results/weights/` and `results/meta/`, and the
direction vectors stay in the pull copy (`/opt/ai/hpc-packages/pulls/model-audit/blueback26/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | Bahushruth/gemma-4-31B-it-abliterated | google/gemma-4-31B-it | violations, 132 flags (66 first shares 0.34 to 0.79, 66 within-layer cosines 0.002 to 0.13) | the card's arbitrary-rank solver on both writers of 33 layers, 17 to 49, where the card says all 60: many directions per matrix (eighth cumulative share 0.70 to 0.93), the input side over-reflected (kept fractions -0.84 to -2.46), rows preserved within 0.0007 as the card claims, nothing else moved |
| 2 | paoloronco/Mistral-7B-Instruct-v0.3-heretic | mistralai/Mistral-7B-Instruct-v0.3 | match, 0 flags | the card's Heretic 1.3.0 kernel pair read to the second decimal: the attention outputs of layers 11 to 31 at 0.97 to 1.40 (the card's 1.01 to 1.44 centred on 24.5) and the down projections of 13 to 29 at 1.10 to 1.16 (the card's 1.16 to 1.18), one shared direction, output side; the card's "applied via LoRA" is 38 matrices edited in place |
| 3 | Bahushruth/gemma-4-E4B-it-abliterated | google/gemma-4-E4B-it | violations, 48 flags (24 first shares 0.19 to 0.45, 24 within-layer cosines) | the same solver on 12 of the card's 42 layers, 21 to 32, eighth share 0.61 to 0.79, input side (kept -0.19 to -1.18), rows within 0.0005; the export drops the 54 shared-KV tensors |
| 4 | Pound1320/gemma-4-E4B-it-uncensored-heretic | google/gemma-4-E4B-it | violations, 11 flags (first shares 0.92 to 0.96, the parent's) | "Duplicate from Titanfrm/gemma-4-E4B-it-uncensored-heretic", itself a duplicate of a repository the hub no longer serves: llmfan46's file under its checksum (`4967172bea`), every field equal to the round 2 report and its second pass |
| 5 | Cup4/gemma-4-E4B-it-uncensored-heretic | google/gemma-4-E4B-it | violations, 11 flags (the same) | the same file, the same title, 21 minutes after pair 4 |
| 6 | Cup5/gemma-4-E4B-it-uncensored-heretic | google/gemma-4-E4B-it | violations, 11 flags (the same) | the same file, the same title, 18 minutes after pair 5 |
| 7 | anlord/gemma-4-E2B-it-abliterated | google/gemma-4-E2B-it | violations, 28 flags (unexpected changes on the gate and up projections) | the repository's own reproduction record read to the third decimal: four Gaussian kernels on seven components, the attention outputs of layers 22 to 26 peaking at 1.757, the queries of 4 to 34 with the keys and values to 14 at 1.078 to 1.095, the down projections of 1 to 24 peaking at 1.766, the gate and up projections of 12 to 25 peaking at 1.566; one direction per layer; rows moved 0.002 to 0.040 under a "row normalization: full" setting |
| 8 | Ishowbackup/gemma-4-E2B-it-uncensored | google/gemma-4-E2B-it | violations, 3 flags (the floor on layer 0, a within-layer cosine on layer 3) | "Duplicate from TrevorJS/gemma-4-E2B-it-uncensored": TrevorJS's file under its checksum (`8237e4818b`), every field equal to the round 13 report, the third repository on that file and the account's third duplicate in three minutes |

Nothing moved outside the matrices the maker's method reaches in any pair: the largest relative change outside the
changed set is exactly 0 in pairs 1, 2, 3, 7 and 8, and 0.00008 in pairs 4, 5 and 6, the parent's seventeen
attention outputs its search weighted near zero. The round's result is four edits read, three measurements of one
file and one hub duplicate. Two of the four edits read as their cards say to the number (pair 2 in both kernels,
pair 7 in all four), and two (pairs 1 and 3) read the card's method on a window the card does not give: both
writers of 33 of 60 layers and of 12 of 42, where the cards say all. The four measurements the duplicate rule would
have refused cost four downloads and four compares for results the repository already held, every one readable from
a commit title and a file checksum.

The weights read off the weights. Pair 7's kernels against the record the maker ships beside the weights
(`abliteration_reproduction.json`, trial 16): the attention output of layer 24 keeps -0.753 of the original's action
along its leading output direction, the record's 1.757 at position 23.78, and the kernel falls to -0.450 at layer 26
and -0.547 at 22 with its stated minimum of 0.676 at distance 2.72; the queries, keys and values keep -0.078 at
layer 4, -0.095 at 21 and -0.084 at 34 on the input side, the record's 1.048 to 1.095 centred on 20.95; the down
projections keep -0.764 at layers 12 and 13 on the output side, the record's 1.766 at 12.61, falling to -0.252 at
layer 1 and -0.267 at 24; the gate and up projections keep -0.566 at layer 18 on the input side, the record's 1.566
at 18.10, and -0.512 at 12 and -0.500 at 25. Pair 2's kernels against the card: the attention outputs keep -0.40 at
layer 25 (the card's 1.44 at 24.50), -0.02 at 12 and 0.04 at 11 (the card's 1.01 at distance 13.9), with layer 31,
the last of the window, keeping 0.86; the down projections keep -0.10 to -0.16 on all 17 (the card's 1.16 to 1.18).
Pairs 1 and 3 read no single weight: along each matrix's leading input direction the 31B copy keeps -0.84 to -2.46
and the E4B copy -0.19 to -1.18, past a reflection on 65 of 66 and on 2 of 24, with the second to eighth
directions carrying 0.14 to 0.54 of the change beside the first. Pairs 4, 5 and 6 read the parent's numbers and add
one the parent's first report lacked: the eleven attention outputs keep 0.29 to 0.92 on the output side and -0.27
to -0.79 on the input side, an input-side edit at 1.27 to 1.79, the fields the parent's second pass carries. Pair 8
reads TrevorJS's numbers.

Preservation claims. Pairs 1 and 3 claim rows "preserved exactly by reparameterization" and read it: the largest
row-norm change is 0.00073 on the 31B's 66 matrices and 0.00047 on the E4B's 24, a tenth of the 0.005 to 0.008
every Heretic copy that claims the step leaves (finding 22). Pair 7's configuration says `row_normalization: full`
with a rank-3 correction, and its rows moved by 0.002 to 0.040 (0.040 on layer 1's down projection, 0.028 on layer
25's up projection): the setting does not restore them. Pair 2 claims nothing and moved its rows 0.003 to 0.013.
Pairs 4, 5 and 6 inherit a parent with no claim (0.0016 to 0.0165); pair 8 inherits TrevorJS's restoration (within
0.0004).

Fingerprints. Fourteen measurements now stand on the 31B instruct original's weight file; pair 1 shares no field
with the thirteen. Twenty stand on the E4B instruct original's file; pairs 4, 5 and 6 carry llmfan46's shard
(`4967172bea`) and are the fourth, fifth and sixth repositories measured on it, pair 3 shares no field with anything.
Fifteen stand on the E2B instruct original's file; pair 8 carries TrevorJS's shard (`8237e4818b`), the third
repository on it after lessans's, and pair 7's first shard (`9ebcea1985`, the embeddings under the library's
three-shard layout) equals the first shard of three earlier copies (aifeifei798's, amkkk's, prithivMLmods's) while
its edits share no field with any. Five stand on the Mistral 7B v0.3 instruct original; pair 2 shares nothing.

## The token side

The cluster's cards read "unexplained differences" on all eight, every one on configuration or template fields
and none on a weight. Re-judged at home under transformers 5.22.1, nine fields move and two cards change their
reading to "consistent with re-save noted" (pairs 1 and 3: `text_config.moe_intermediate_size`, null in a 5.14.1
save against a 5.5.0.dev0 original, closed by the default rule, with the version strings and nothing else left).
The same field closes on pairs 4 to 8, and on pair 2 `head_dim` and `rope_parameters` (a 5.9.0 save's forms of two
fields a 4.42 original omits) close by the default rule. What stays as printed:

- Pair 2: 777 fields. The tokenizer configuration of the 5.9.0 save carries no `added_tokens_decoder` block where
  the original declares 771 added tokens, and the two `tokenizer.json` files are different saves (3,672,121 bytes
  against 1,961,548), so the rule of finding 44 does not read them; a `pad_token` of `</s>` (id 2) written where
  the original declares none, the loader's choice finding 15 read on a Qwen copy; and the 5.x renames (`dtype` for
  `torch_dtype`, `rope_parameters` for `rope_theta`). The fixed conversation renders identically from the moved
  template.
- Pairs 4, 5 and 6: the template. The copies carry llmfan46's 16,804-byte file, which is Google's file of the E4B's
  04-28 revision (`c53e9d33`) as the parent refreshed it on 05-04, under a pin of 07-20 whose Canonical file is
  18,569 bytes: the earlier-revision template through a re-upload, twice removed.
- Pair 7: the 5.16 `per_layer_config` form (`global_head_dim` 512 and `num_global_key_value_heads` 1 moved into a
  per-layer map), the ninth copy on it, and `vision_config.rope_parameters.rope_type` written as `axial` where the
  original says `default`, a 5.19.0 save's name for the same vision rotary scheme, the first copy to carry it. Both
  closed by hand.
- Pair 8: the earlier-revision template through a re-upload, TrevorJS's 11,926-byte file of the 04-02 revision
  under the 07-20 pin, as lessans's copy of the same file in round 22.

Every fixed conversation in the round renders identically under both templates.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- A solver's arbitrary rank on both writers, 132 and 48 flags (pairs 1 and 3): every changed matrix flags its
  first share (0.19 to 0.79, where the eighth cumulative share is 0.61 to 0.93) and its within-layer cosine (0.002
  to 0.14), because each matrix is its own many-direction edit and the two writers of a layer share nothing. An
  entry for a solved edit would read the spectrum beyond the eighth direction and the row-norm bound, and count
  none.
- Seven components under four kernels, 28 flags (pair 7): unexpected changes on the gate and up projections, which
  no entry lists. Every other measure reads the shipped record. An entry naming the seven components with a kernel
  per group would count none.
- The parent's flags, 11 each (pairs 4, 5 and 6): first shares of 0.92 to 0.96 on llmfan46's eleven searched
  attention outputs, the arbitrary-rank floor of finding 22.
- The floor and the biprojection's bend, 3 flags (pair 8): layer 0's down projection at 0.988 and layer 3's two
  writers at 0.943, the parent's flags.
- No flag on pair 2, a Heretic kernel pair on a Mistral base, as finding 41's copy.

The round's finding for the measure is pair 7: a maker who ships the search's chosen parameters beside the
weights, and the kept fractions along the leading directions read every one of the eight numbers back to the
third decimal, on the seven components the four kernels reach. Beside it, pairs 1 and 3 read a preservation claim
that holds to 0.0007, where every earlier claim of the step left 0.007.

## Owed to the metadata tool

Added since: nothing this round. What remains: the earlier-revision template through a re-upload (pairs 4, 5, 6 and
8, four more; a rule that reads the parent's revision when the checksum names a parent); the 5.16 `per_layer_config`
form (pair 7, the ninth time) and the 5.19 `axial` name for the vision rotary scheme (pair 7, the first); a
tokenizer configuration saved without its `added_tokens_decoder` when the token file is not shared (pair 2, where
finding 44's rule cannot run); and a pad token written by a save (pair 2). To the pinner: a duplicate chain. The
three Cup and Pound repositories name Titanfrm's, Titanfrm's names AST-1320's, and AST-1320's no longer answers;
the title rule stops at the first link, the checksum rule pairs all three with llmfan46's measured file at once.

## Operational

The pull of 11-01 23:59Z carries the eight measurement folders (card, metadata, weights, direction vectors and the
sha256 record of each) and the sweep record; no job log came home, so the jobs' numbers, nodes and seconds are
not in this note. Every compare finished with its card and its weights report, and the sweep ran after all eight
and deleted the four originals. The home judgement ran under transformers 5.22.1.

Weight differences alone cannot certify the absence of hidden behavior.
