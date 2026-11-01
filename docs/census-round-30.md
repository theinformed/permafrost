# Census round 30: eight Gemma 4, Ministral 3 and DiffusionGemma pairs (2026-10-31)

Eight published copies compared with their stated originals on Wheat, 2026-10-31, from the batch pinned as
`data/batches/round-30-batch-1.json`: probe job 386940 (hub and PyPI reachable, no container image on the system),
download job 386942, compares 386943 to 386950, sweep 386951, which deleted the seven original checkpoints
(`47b6801b` and `7d4c97e5` of the 26B-A4B original for pairs 1 and 2; `ee0ef602` and `3555bddc` of the E4B original
for pairs 3 and 4; `6c2c4c82` of Ministral 3 8B Reasoning for pair 5; `f7f5b7f5` and `0f28bc42` of DiffusionGemma
26B A4B for pair 6 and for pairs 7 and 8). This is the first round run without the container image: the kit built
a standalone Python 3.11.18 in the project's work space and installed its pins there, and every job ran under it.
The eight measurements were re-scored at home with the recipe table as committed (one naming entry added this
round, below) and the saved direction vectors; three flag counts moved, all on the diffusion pairs, for the naming
reason. Every metadata report was judged again at home under transformers 5.22.1 with the originals' commit
histories, and the committed reports carry that judgement. Each pair has a card (the tool's Stage 1 text after the
home judgement, with the Stage 2 line) and a reading note in `docs/cards/`; the measurements are in
`results/weights/` and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/wheat30/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | sitten1/gemma-4-26B-A4B-it-uncensored | google/gemma-4-26B-A4B-it | violations, 31 flags (expert energy shares, one within-layer direction) | TrevorJS/gemma-4-26B-A4B-it-uncensored's weight file under another name: a hub duplicate, LFS checksums `4b988df4e5` and `3d2388e809`, every field equal to the round 3 second pass but the sketch's last digits |
| 2 | erunda337/gemma-4-26B-A4B-it-uncensored | google/gemma-4-26B-A4B-it | violations, 31 flags | the same file a third time, duplicated four days after pair 1 under a later pin; equal to pair 1 in every field |
| 3 | OS-Software/gemma-4-E4B-it-uncensored-heretic | google/gemma-4-E4B-it | violations, 40 flags (energy shares, within-layer directions) | a rank-four edit, read as exactly rank four from the singular values, on the attention outputs and down projections of layers 18 to 27, input side, rows unrestored: the card's Heretic 2.0 "transport" table read off the weights |
| 4 | TheUmbraWalker/gemma-4-E4B-it-2-heretic | google/gemma-4-E4B-it | violations, 61 flags (energy shares, within-layer directions) | two Heretic 1.3 passes on one base: both kernels' windows read back to the layer (73 changed, two directions exactly where the windows overlap), the strengths do not |
| 5 | AISafety-Student/Ministral-3-8B-Reasoning-2512-heretic | mistralai/Ministral-3-8B-Reasoning-2512 | violations, 1 flag (one first share 0.9893) | the card's Heretic 1.2 kernel as written: windows, side, rank and all 45 strengths read back within 0.004; the second copy on this original and the first ablation of it |
| 6 | Goodoldjam/DiffusionGemma-26B-E38-Abliterated-BF16 | google/diffusiongemma-26B-A4B-it | violations, 21 flags on the cluster (names unread), 40 at home | the card's 20 tensors (layers 7 to 16, two writers), five at the round-trip floor, fifteen multi-direction edits on the input side with per-matrix directions; the first diffusion-variant copy measured |
| 7 | FredyRivera-dev/diffusiongemma-26B-A4B-it-HERETIC-Uncensored | google/diffusiongemma-26B-A4B-it | violations, 68 flags on the cluster, 86 at home | edwixx's weight file with a processor file added, first measurement of it: one direction per layer on the attention outputs, down projections and all 128 experts of layers 11 to 29, output side, 20 round-trip floors |
| 8 | nnnxnsn/diffusiongemma-26B-A4B-it-HERETIC-Uncensored | google/diffusiongemma-26B-A4B-it | violations, 68 flags on the cluster, 86 at home | edwixx's file under a hub duplicate; equal to pair 7 in every field |

Nothing moved outside the matrices the maker's method reaches in any pair: the largest relative change outside the
changed set is exactly 0 in pairs 1 to 6 and 0.00095 in pairs 7 and 8, on eight attention outputs and down
projections of layers 1 to 6 that the merge touched without an edit. The round's result is five edits and three
re-uploads, one of which (pair 7) is the only measurement of its parent. Three of the five edits read as their
cards say to the number (pair 5 in every kernel value, pair 3 in window and rank, pair 6 in tensor set and largest
difference), one (pair 4) reads its two cards' windows and not their strengths, and one (pair 7) carries a card
that prints no numbers to read. The three re-uploads are the hub's duplicate function and one upload with the
parent's files: pairs 1 and 2 are TrevorJS's 26B-A4B copy under two accounts, 5 and 10 days after the parent's
weights went up, 103 GB of downloads and two compare jobs for a file the census measured in rounds 2 and 3; pair 8
is edwixx's diffusion copy duplicated eleven days after its upload; pair 7 is the same file uploaded by hand with
a 1,689-byte processor configuration added and the README crediting edwixx. The pinner's duplicate check (finding
38) would have filed pairs 1, 2 and 8 as their parents' measurements and pair 7 as a new one.

## The token side

The cluster's cards read "consistent" on pair 6, "consistent with re-save noted" on pairs 1, 7 and 8 and
"unexplained differences" on pairs 2, 3, 4 and 5, every one of them on configuration or tokenizer fields and none
on a weight. Re-judged at home under transformers 5.22.1, pair 4 closes by tool (`text_config.moe_intermediate_size`,
written as null by a 5.6.2 save where Google's file omits it, the field round 19's MoonRide copy closed by the same
rule) and moves to "consistent with re-save noted"; pair 3 closes the same field and keeps three; the others stay as
printed, for these reasons:

- Pair 2: the template. The copy carries Google's 12,045-byte file of 04-02, the one TrevorJS's repository and pair
  1's pin hold, where the 04-10 pin's template is a 16,448-byte revision. The earlier-revision case through a
  re-upload, the seventh in the census; the two files render the fixed conversation identically. The rule that reads
  the original's later commits cannot close a copy that carries the original's earlier file. Closed by hand.
- Pair 3: the 5.16 save form (finding 39). `global_head_dim` 512 and `num_global_key_value_heads` leave the text
  configuration and return as a `per_layer_config` map under the seven global layers' indices. The third copy on
  this form; closed by hand.
- Pair 5: 1,003 fields that are one omission. The copy's 407-byte `tokenizer_config.json` carries no
  `added_tokens_decoder` where the original's declares 1,000 entries, and no `additional_special_tokens` list, while
  the two sides share the same `tokenizer.json` and template byte for byte. The scorer has a rule for declarations
  that move between files and none for declarations that disappear while the token file is shared. Closed by hand.

Pairs 1, 7 and 8 differ from their originals in the two version strings and nothing else; pair 6's configuration,
generation settings and token files are the original's field for field, with a `model_index.json` and a scheduler
folder added for the diffusion pipeline and a template 1,109 bytes longer that renders identically. Every fixed
conversation in the round renders identically.

## What the scorer learned

The flag counts are the same on the cluster and at home on pairs 1 to 5 and moved on pairs 6 to 8. Their causes,
by pair:

- Expert energy shares, 31 flags (pairs 1 and 2): TrevorJS's second-pass flags, the worst expert of each layer
  at 0.881 to 0.990 and layer 29's within-layer cosine 0.949, repeated to the last digit on the non-SVD fields
  and within 2.3 × 10⁻⁶ on the sketched ones.
- Rank four, 40 flags (pair 3): first shares 0.587 to 0.883 on all 20 edited matrices, where the fourth share is
  0.999 to 1.000 and the fifth singular value is 0; within-layer cosines 0.005 to 0.147, the two writers of a
  layer on unrelated directions. A `transport-rank-k` entry (a layer window on both writers, first-k share at
  least 0.99 with k read from the singular values, left above right, rows unrestored) would fit it with no flags.
- Two passes, 61 flags (pair 4): first shares 0.504 to 0.860 and within-layer cosines 0.006 to 0.855 on exactly
  the matrices the second card's kernels reach (attention outputs 18 to 33, down projections 29 to 41), where the
  two passes' directions are summed; rank one with cosines of 0.96 to 1.00 everywhere else. The per-layer entry
  reads the first pass; an entry for stacked passes would allow rank two where two kernels overlap.
- One share, 1 flag (pair 5): the attention output of layer 22 at 0.9893 against the entry's 0.99 floor, on a copy
  whose other 44 matrices sit at 0.990 to 0.996. A floor of 0.985 on the Heretic 1.2 entry would admit it and
  nothing else measured.
- Names, 21 to 40 and 68 to 86 flags (pairs 6 to 8): the diffusion original stores the Gemma 4 language stack under
  `model.decoder.` where the instruct original uses `model.language_model.`. The cluster's naming table did not
  list the prefix, so every changed tensor was kind "other", the rankers found no projection to compare and each
  change was flagged as unexpected. With `decoder.` in the table (added this round in `audit/recipes.json`, with
  a test), the home score reads the roles and the real flags appear: pair 6's 20 first shares (0.005 to 0.967)
  and 20 direction cosines, pair 7's 67 first shares (0.957 to 0.989 on the dense edits, 0.002 to 0.018 on the
  20 floors, 0.971 at the worst expert) and 19 within-layer cosines (0.24 to 0.82). The committed reports are the
  home ones; the cluster's counts are in the `rescoring` block of each.

The round's own finding for the measure is pair 4: the leading-direction kept fraction reads a Heretic kernel
back to two decimals when one pass was applied (pair 5) and reads nothing when two passes were summed, because
the two projections along different directions leave a rank-two difference whose leading direction belongs to
neither. A per-matrix rank-two decomposition reporting two directions and two kept fractions would read both
cards.

## Owed to the metadata tool

Added this round: the reclassify command keeps the Stage 2 line of a card it rewrites (`audit/metadata.py`,
`card_with_weights`, with tests in `tests/test_resave.py`), so a judged-again card no longer loses the weights
line that was appended by hand after each round. What remains: a rule for a tokenizer configuration that drops
its `added_tokens_decoder` map while `tokenizer.json` is byte-equal (pair 5, 1,003 fields); the 5.16
`per_layer_config` form as the library's own save (pair 3, the third time); the earlier-revision template through
a re-upload (pair 2, the seventh time), which needs the pinner to pair a duplicate with its parent; and the
duplicate check itself, which this round would have spared two 51 GB downloads and three compare jobs. To the
batch: nothing from this round's duplicates. edwixx's own repository holds pair 7's file under the same checksums
and needs no measurement; Goodoldjam's NVFP4 derivative is a quantised copy of pair 6's file and needs none for
its edit; other DiffusionGemma copies are now measurable with their roles read.

## Operational

The first image-free round. The probe found hub and PyPI reachable and no container image on Wheat; the download
job ran under a standalone Python 3.11.18 unpacked into the project's work space with the kit's pins, and fetched the eight copies and seven
originals, planned at 525.8 GB, in 5,335 seconds, of which the hub fetch took 1 hour 27 minutes 36 seconds
(21:59:37Z to 23:27:13Z). The compares ran 1,678 and 1,633 seconds on the two 26B-A4B pairs, 608 and 466 on the
E4B pairs, 520 on the Ministral pair and 1,509, 1,401 and 1,451 on the three diffusion pairs; the sweep took 1
second. All ten jobs exited 0. The download printed its node (wheat-r16-dt37a) and core count (1); the compares
printed no node facts because the parcel predates the cores line in the step header, so the per-pair seconds
above are from the desk's drop records. The cluster's library was transformers 4.56.2 (no Gemma 4 or
DiffusionGemma class), the home judgement 5.22.1.
