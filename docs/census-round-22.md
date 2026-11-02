# Census round 22: eight Gemma 4 pairs on Blueback, the first there since round 14 (2026-11-01)

Eight published copies compared with their stated originals on Blueback from the batch pinned as
`data/batches/round-22-batch-1.json` (pinned 2026-10-31 17:28Z under rulings model-audit-13 and 14, the first
Blueback batch since round 14). The pull of 11-01 18:37Z brought home the eight measurement folders and the sweep
record and no job log, so the download, compare and sweep job numbers and their seconds are not recorded in this
note; the sweep deleted the five original checkpoints (`419b2efe` of the 31B original for pair 1; `4742fe84` of
the E2B original for pairs 2 and 7; `5926caa4` of the 12B original for pairs 3 and 6 and `707f0a3b` for pairs 4
and 5; `b4a60110` of the E2B original for pair 8) from `/p/work1/sdegan/model-audit/originals/`. The batch was
pinned before the duplicate rule (finding 38) and carries three measurements the rule would have refused: two hub
duplicates (pairs 5 and 8) and a repeat of round 13's pair 2 (pair 2). The pinner's note held back two copies
(unsloth's Magistral and tvall43's 26B-A4B heretic, whose 27 renamed vision-tower tensors the kit of the time
could not map). The eight measurements were re-scored at home with the recipe table as committed and the saved
direction vectors, and no flag count moved. Every metadata report was judged again at home under transformers
5.22.1 with the originals' commit histories, and the committed reports carry that judgement. Each pair has a card
(the tool's Stage 1 text after the home judgement, with the Stage 2 line) and a reading note in `docs/cards/`;
the measurements are in `results/weights/` and `results/meta/` (pair 2 under a `.pass-2` suffix beside round 13's
files), and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/blueback22/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | huihui-ai/Huihui-gemma-4-31B-it-abliterated | google/gemma-4-31B-it | violations, 52 flags (first shares 0.989 to 0.990, the floor) | the maker's shared projection at weight 1.00 on both writers of all 60 layers, output side, nothing else moved; every field of all 1,188 tensors equals prithivMLmods's round 18 re-upload, which closes finding 9's open case on the 31B |
| 2 | huihui-ai/Huihui-gemma-4-E2B-it-abliterated (second pass) | google/gemma-4-E2B-it | match, 0 flags | a repeat of round 13's measurement of the same two revisions on the same system: every field of all 2,011 tensors equal to the last digit; the batch note's "unmeasured" was stale |
| 3 | RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals9 | google/gemma-4-12B-it | violations, 97 flags (55 first shares 0.002 to 0.968, 42 within-layer cosines) | the card's Heretic 1.2.0 arbitrary-rank window (layers 14 to 43) with every in-range matrix rewritten: 34 edits on the input side at weights 0.61 to 1.25, 21 rounding residues and 5 under the threshold, rows within 0.008 under the preservation claim (finding 22) |
| 4 | Vampelium/gemma-4-12B-it-heretic | google/gemma-4-12B-it | violations, 38 flags (first shares 0.79 to 0.99 at the windows' edges) | a Heretic pair the card does not print: the attention outputs of layers 5 to 47 and the down projections of 16 to 47, one shared direction, output side, with kept fractions that run smoothly to -0.29 and -0.41 at the windows' centres, a weight schedule on Gemma 4 12B where finding 46's three copies read none |
| 5 | laladream/gemma-4-12B-it-uncensored | google/gemma-4-12B-it | violations, 1 flag (the floor on layer 42) | "Duplicate from TrevorJS/gemma-4-12B-it-uncensored": TrevorJS's file under its checksum, every field equal to the round 8 report, the fifth repository on that file |
| 6 | Carlosian/Gemma-4-12b-it-Abliterated | google/gemma-4-12B-it | violations, 48 flags (42 first shares 0.59 to 0.91, six within-layer cosines) | the card's clean-cone band (layers 14 to 34) on both writers with the card's cone rank 2: two directions per matrix (fourth share 0.986 to 0.995), rows restored within 0.0005, nothing else moved |
| 7 | WWTCyberLab/gemma-4-E2B-it-abliterated | google/gemma-4-E2B-it | violations, 48 flags (unexpected changes on the gate and up projections) | four writers on the 24 layers amkkk's copy lists (finding 47), one direction and one scale per layer read to the third decimal on all four (1.31 to 1.51 on layers 9 to 32, 2.40 on 34), where the card names two writers and a scale of 1.50 |
| 8 | lessans/gemma-4-E2B-it-uncensored | google/gemma-4-E2B-it | violations, 3 flags (the floor on layer 0, a within-layer cosine on layer 3) | "Duplicate from TrevorJS/gemma-4-E2B-it-uncensored": TrevorJS's file under its checksum, every field equal to the round 13 report |

Nothing moved outside the matrices the maker's method reaches in any pair: the largest relative change outside
the changed set is exactly 0 in pairs 1, 2, 4, 5, 6, 7 and 8, and 0.00096 in pair 3, on the down projection of
layer 17, inside the card's window, one of five in-range matrices the search weighted under the threshold. The
round's result is five edits read, two hub duplicates and one repeat. Three of the five edits read as their cards
say to the number (pair 1 at the maker's weight 1.00, pair 3 in window and claim, pair 6 in band and rank), one
(pair 7) reads its 24 layers and a scale per layer where the card prints one scale and two writers, and one (pair
4) reads a kernel pair under a card of three sentences. The three measurements the duplicate rule would have
refused cost three downloads and three compares for results the repository already held, two of them (pairs 5
and 8) readable from one commit title each and the third (pair 2) from `results/weights/` by hub id and revision.

The weights read off the weights: 1.00 on pair 1's 120 matrices (left kept fraction -0.001 to 0.008, left below
right on 120 of 120); 1.00 on pair 2's 50, as before; searched input-side weights of 0.61 to 1.25 on pair 3's 34
edits (left above right on 34 of 34); a schedule on pair 4's 75 (left below right on 75 of 75, running 0.88 to
-0.29 and back on the attention outputs and 0.90 to -0.41 and back on the down projections); 1.31 to 1.51 and
2.40 per layer on pair 7's 96, the same number on all four writers of a layer. Pair 6's two directions per matrix
carry no single side. Pairs 5 and 8 read their parents' numbers.

Preservation claims. Pair 3's rows moved by 0.0053 to 0.0079 on its 34 edits under Heretic's row-norm
preservation, the band finding 22 reads on every copy that claims the step. Pair 6's rows moved by at most 0.0005
under the Nous toolkit's norm-preserving lineage, a restoration in the sense TrevorJS's copies read. Pair 7 claims
"norm-preserving" and its rows moved by 0.005 to 0.052 on the two output-side writers (0.83 and 1.05 on layer 34)
and by at most 0.0006 on the two input-side ones: the claim holds on half the targets. Pairs 5 and 8 inherit
TrevorJS's restoration (within 0.0004).

Fingerprints. Thirteen measurements now stand on the 31B instruct original; pair 1 equals prithivMLmods's re-upload
in every field and shares no checksum with it (a re-save), and shares nothing with TrevorJS's and ressl's copies
of the same 120 matrices. Twenty-one stand on the 12B instruct original; pair 5 carries TrevorJS's shard
(`dd7fcab672`) and pairs 3, 4 and 6 share no field with anything. Ten stand on the E2B instruct original; pair 8
carries TrevorJS's shard (`8237e4818b`), pair 7 changes amkkk's 96 tensors with no field equal, and pair 2 is
round 13's file (`90daa0b268`).

## The token side

The cluster's cards read "consistent" on pairs 1 and 2 (every field equal, 5.5.0.dev0 on both sides) and
"unexplained differences" on the six others, every one on configuration or template fields and none on a weight.
Re-judged at home under transformers 5.22.1, 26 fields move and two cards change their reading:

- Pairs 3, 4, 5 and 6: the 12B family's six fields (finding 39) close by tool on all four, the four omitted
  defaults by the default rule and the two sub-configuration data types by the data-type rule. Pair 6 moves to
  "consistent with re-save noted" (5.12.1 against 5.10.0.dev0 and nothing else). Pair 3 keeps its template open:
  the copy's 18,682-byte file, refreshed by the maker on 07-21, is one byte short of Google's 18,683-byte Canonical
  file of 07-20, which the later-revision rule does not match at that distance. Pair 5 keeps the earlier-revision
  template through a re-upload (TrevorJS's 17,466-byte file of 06-03 under a 07-20 pin). Pair 4 keeps the 5.16
  `per_layer_config` form (`global_head_dim` 512 and `num_global_key_value_heads` 1 moved into a per-layer map), the
  seventh copy on it and the first 12B, closed by hand.
- Pairs 7 and 8: `text_config.moe_intermediate_size`, null in 5.5.0 saves against a 5.5.0.dev0 original, closes
  by the default rule. Pair 7 moves to "consistent with re-save noted". Pair 8 keeps the earlier-revision template
  through a re-upload (TrevorJS's 11,926-byte file of the 04-02 revision under a 04-10 pin).

Every fixed conversation in the round renders identically under both templates.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- The floor, 52, 1 and 3 flags (pairs 1, 5, 8): first shares of 0.988 to 0.990 on edits of 1.2 to 1.6 percent,
  where the bfloat16 leftover (0.0013 to 0.0016 of the norm) crosses the 0.99 line, and on pair 8 a within-layer
  cosine of 0.943 on layer 3 that the parent's report carries.
- Arbitrary rank on both writers, 97 flags (pair 3): 55 first shares, 21 of them at 0.002 to 0.094 on residues
  the search weighted to nothing, 34 at 0.49 to 0.97 on edits whose fourth share is 0.87 to 0.98, and 42
  within-layer cosines of 0.006 to 0.37, since each matrix has its own direction. An `arbitrary-rank` entry that
  sets residues aside would count none.
- A kernel pair at the windows' edges, 38 flags (pair 4): first shares of 0.79 to 0.99 on the matrices where the
  kernel's weight is under 0.5 and the edit under 1.5 percent, the floor again.
- Rank two, 48 flags (pair 6): 42 first shares of 0.59 to 0.91 where the fourth cumulative share is 0.986 to
  0.995, and six within-layer cosines of 0.84 to 0.95. A `cone-rank-k` entry reading the fourth share would count
  none.
- Four writers with one scale per layer, 48 flags (pair 7): unexpected changes on the gate and up projections,
  which no entry lists. The scale reads to the third decimal on all four writers (the right kept fraction on the
  gate and up projections equals the left on the attention output and down projection, layer for layer), the
  second four-writer E2B copy after amkkk's.

The round's finding for the measure is the pair of E2B copies that share 24 layers: amkkk's configuration lists
layers 9 to 13, 15 to 32 and 34, WWTCyberLab's card says "24 of 35", and both change exactly those layers on the
same four writers from the same per-layer refusal signal, one at a scale per writer and one at a scale per layer.
The layer choice belongs to the signal, and an entry that names the four writers would read both.

## Owed to the metadata tool

Added since: nothing this round. What remains: the 5.16 `per_layer_config` form as the library's own save (pair
4, the seventh time); a later-revision rule tolerant of a line ending (pair 3, one byte); the earlier-revision
template through a re-upload (pairs 5 and 8, which the readings close by hand as the Ishowbackup pairs were). To
the pinner: refuse a hub id and revision already in `results/weights/` (pair 2) beside the checksum rule, and a
re-save check for a copy whose every field equals a measured copy's without a shared checksum (pair 1 against
prithivMLmods's, finding 9).

## Operational

The pull of 11-01 18:37Z carries the eight measurement folders (card, metadata, weights, direction vectors and the
sha256 record of each) and the sweep record; no job log came home, so the jobs' numbers, nodes and seconds are
not in this note. Every compare finished with its card and its weights report, and the sweep ran after all eight
and deleted the five originals. The home judgement ran under transformers 5.22.1.

Weight differences alone cannot certify the absence of hidden behavior.
