# Census round 19: eight Gemma 4 and Mistral Small pairs (2026-10-31)

Eight published copies compared with their stated originals on Nautilus, 2026-10-31, from the batch pinned as
`data/batches/round-19-batch-1.json`: push card 5605, probe card 5616 (job 4142428 on the transfer node, hub
reachable, 2 seconds), round card 5626, download job 4142666, compares 4142667 to 4142674 on the background queue,
sweep 4142675, which deleted the six original checkpoints (`145dc250` and `842da379` of the 31B original, one weight
file under two revisions, for pairs 1 and 2; `20da991a` of the 26B-A4B original; `5926caa4` and `707f0a3b` of the
12B original, one weight file under two revisions, for pairs 4 and 6 and for 5 and 7; `1483f238` of Mistral Small
3.2 for pair 8). An earlier download for this batch (4138542) fetched nothing and was cancelled by the desk with its
chain; the parcel was rebuilt with bounded pip steps and wheels staged per system before this round ran. Card 5647
pulled the measurements home. The eight measurements were re-scored at home with the recipe table as committed and
the saved direction vectors, and no flag count moved. Every metadata report was judged again at home under
transformers 5.6.2 with the originals' commit histories, and once more under 5.12.0 in a scratch environment to
test the two rules added this round. Each pair has a card (the tool's Stage 1 text after the home judgement, with
the Stage 2 line) and a reading note in `docs/cards/`; the measurements are in `results/weights/` and
`results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/nautilus19/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | MoonRide/gemma-4-31B-it-heretic-ara-custom | google/gemma-4-31B-it | violations, 90 flags (energy shares, within-layer directions) | consistent: arbitrary-rank edits on the attention outputs of layers 30 to 55 and 18 down projections of 32 to 55, input side, searched weights 0.63 to 2.93, ten in-range matrices rewritten near zero (six under the threshold, four over it); rows moved 0.006 to 0.008 under a preservation claim |
| 2 | 3MPER0RR/gemma-4-31b-it-3MPER0RR-abliterated | google/gemma-4-31B-it | violations, 22 flags (floor) | one direction per layer on the down projections of layers 39 to 59 and the attention outputs of 40 to 59, output side, weight 1.16 to 1.40 on the down projections and 0.34 to 0.82 on the attention outputs; the card says nothing to be consistent with |
| 3 | SevenOfNine/Gemma-4-26B-A4B-It-Abliterated | google/gemma-4-26B-A4B-it | violations, 8 flags (within-layer directions) | consistent: one direction per layer on the attention outputs of layers 4 to 29 and the shared down projections of 16 to 29, output side, a schedule of 0.87 to 1.40 rising with depth; no expert reached |
| 4 | Iambackup/gemma-4-12B-it-uncensored | google/gemma-4-12B-it | violations, 1 flag (floor) | TrevorJS/gemma-4-12B-it-uncensored's weight file under another name: a hub duplicate, LFS checksum `dd7fcab672`, every field equal to round 8's report |
| 5 | Justbackup/gemma-4-12B-it-uncensored | google/gemma-4-12B-it | violations, 1 flag (floor) | the same file a third time, duplicated two months later under a later pin; the template reads as the earlier-revision case |
| 6 | prithivMLmods/gemma-4-12B-it-heretic_decensored | google/gemma-4-12B-it | violations, 6 flags | one shared direction, rank one, on the attention outputs of layers 15 to 47 and the down projections of 25 to 47; the kept fraction reads neither the card's kernel nor a side |
| 7 | MeFFyLe/gemma-4-12B-it-uncensored-heretic | google/gemma-4-12B-it | violations, 15 flags (energy shares) | llmfan46/gemma-4-12B-it-uncensored-heretic's weight file under another name: a hub duplicate, LFS checksum `4e6ac81d39`, every field equal to round 13's report, the maker's patched template carried along |
| 8 | nicoboss/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-llamacppfixed | mistralai/Mistral-Small-3.2-24B-Instruct-2506 | match, 0 flags | huihui-ai's weight file under another name (ten shards, same checksums, every field equal to round 13's report) with a `tokenizer.json` added and two added-token names changed, the repair the name claims |

Nothing moved outside the matrices the maker's method reaches in any pair: the largest relative change outside the
changed set is exactly 0 in pairs 2 to 8 and 0.000999 in pair 1, on six down projections inside the declared range
that the search weighted near zero. The round's result is four edits and four re-uploads. Three of the four edits
read as their cards say (pairs 1 and 3 in every stated number, pair 2 under a card that states none), and one (pair
6) reads a direction and a rank the card implies and none of the five kernel numbers the card prints. The four
re-uploads are the hub's duplicate function at work: each repository's first commit says "Duplicate from" and names
the parent, each carries the parent's README byte for byte, and the hub's own file listing shows the parent's LFS
checksum on every weight file before a byte is downloaded (finding 38). Pairs 4 and 5 are the same file twice, under
two accounts named for the purpose, 1 and 67 days after TrevorJS uploaded it; pair 7 is llmfan46's 12B copy three
months on; pair 8 is huihui-ai's Mistral Small 3.2 copy from five days after its upload, with the token files
repaired fourteen minutes after the duplication.

The weights read off the weights: searched input-side weights of 0.63 to 2.93 on pair 1's 44 edits (left above
right on all 48 changed matrices), a per-kind strength on pair 2 (−0.40 to −0.16 kept on the down projections,
0.18 to 0.66 on the attention outputs, left below right on 41 of 41), a schedule on pair 3 (the attention outputs
keep −0.07 to 0.13 on layers 4 to 12 and −0.09 to −0.40 on 13 to 29, the down projections 0.00 to 0.25; left below
right on 38 of 40), and nothing on pair 6, where the kept fraction along one shared direction runs from −0.01 to
0.98 on the attention outputs and −0.28 to 0.77 on the down projections with the left below the right on 25 of 56.
The card for pair 6 prints Heretic's kernel (a weight of 0.81 to 1.18 peaking at layer 40 on the attention outputs,
0.97 to 1.37 peaking at 46 on the down projections), which would read as kept fractions of 0.19 to −0.18 and 0.03
to −0.37 falling smoothly; the measured fractions read 0.98, 0.96, 0.87, 0.63 and 0.76 on layers 15 to 19 and
0.37, 0.57, 0.82, 0.16 and 0.89 on 40 to 44. The second copy in the census that reads no weight and no side on a
rank-one shared direction (3MPER0RR's 12B copy in round 18 was the first) and the first of the two under a card that
states the numbers. The duplicates read what their parents read: weight 1.0 with the biprojection's second term on
pairs 4 and 5, searched weights 0.32 to 3.63 on pair 7, weight 1.0 on pair 8.

One preservation claim. Pair 1's rows moved by 0.0059 to 0.0077 on its 44 edits under the maker's row-norm
preservation, the band finding 22 reads on coder3101's four copies of the same release (0.0057 to 0.0080), now on a
second maker. Pair 3's rows moved 0.004 to 0.048 and pair 2's 0.0016 to 0.042 under no claim; pairs 4 and 5 carry
TrevorJS's restoration within 0.0004.

Fingerprints. Nine measurements now stand on the one 31B weight file and pairs 1 and 2 share no field with any of the
seven earlier ones or with each other but one largest absolute difference (pair 1 against coder3101's copy, a single
bfloat16 step). Eight stand on the 26B-A4B file and pair 3 shares none. Fifteen measurements of copies stand on the
12B file; pairs 4 and 5 equal TrevorJS's report in every field of all 677 tensors and carry its shard checksum
(`dd7fcab6`), pair 7 equals llmfan46's in every field and carries its checksum (`4e6ac81d`), and pair 6 shares no
field with any of the others but one largest absolute difference with lemuralabs's copy; its first shard is
byte-equal to the first shard of 3MPER0RR's and igorls's 12B copies, the same library sharding of a block none of
the three edits touches. Pair 8 carries huihui-ai's ten shard checksums and equals its report in every field of all
585 tensors. The re-upload test of finding 9 has four positives this round, the most in any round, and all four were
visible from the hub's commit titles and LFS checksums before the download.

## The token side

The cluster's cards read "consistent with re-save noted" on pair 3 and "unexplained differences" on the seven
others, every one of them on configuration or tokenizer fields and none on a weight. Re-judged at home under the
kit's transformers 5.6.2, pair 1 closes by tool (`text_config.moe_intermediate_size`, written as null by a 5.7.0
save, the 5.6.2 default) and moves to "consistent with re-save noted"; the six others stay as printed, for these
reasons:

- The 5.16 save form, pair 2: `global_head_dim` 512 and `num_global_key_value_heads` 4 leave the text configuration
  and return as a `per_layer_config` map under the ten global layers' indices, as on the maker's 12B copy in round
  18; the version strings read 5.5.0.dev0 to 5.16.1 and the template is the pinned file. Closed by hand.
- The 12B family's six fields, pairs 4 to 7: Google's `config.json` for this model, written by hand under
  5.10.0.dev0, carries the four values the library's unified Gemma 4 classes hold as defaults (the audio tower's
  `audio_samples_per_token`, `hidden_size` and `output_proj_dims`, 640, 640, 640, and the vision patch size, 48)
  and a null `dtype` in the audio and vision sub-configurations. A save under 5.10.2, 5.12.0 or 5.12.1 omits the
  four and writes `bfloat16` into the two. The six fields are not an edit; they are what finding 11 established in
  round 8 and every 12B copy judged since has read the same way (TrevorJS, llmfan46, coder3101, 3MPER0RR, AEON-7
  and these four). Two of the six close at home by the first rule added this round (a sub-configuration data type
  written where the other side left it null repeats the top-level declaration, the sibling of the rule for an
  absent one). The four defaults cannot close under 5.6.2, because the family's top-level `model_type` is
  `gemma4_unified` and 5.6.2 has no such class: the kit's default lookup returns nothing and the configurations
  cannot be loaded at all. Loaded under 5.12.0, both sides give 640, 640, 640 and 48, and the second rule added
  this round (an absent field that both saved configurations load to the same value, with the version recorded)
  closes them; under that library pairs 4 and 6 read "consistent with re-save noted" and pairs 5 and 7 keep their
  template as the one open field. The committed reports are the 5.6.2 judgement, as every earlier round's are.
- Two templates, pairs 5 and 7. Pair 5's is Google's 17,466-byte file of 06-03, the parent's pin, under a pin
  (07-20) whose template is the 18,681-byte "Canonical" file of 07-09: the earlier-revision case through a
  re-upload, as TimelessSoul's 12B copy in round 14, and the sixth earlier-revision case in the census. Pair 7's is
  llmfan46's patched 21,488-byte template (finding 19), carried through the duplicate into a fifth repository.
  Both render the fixed conversation identically.
- An original without a library tokenizer, pair 8: Mistral Small 3.2 ships `tekken.json` and no `tokenizer.json`,
  tokenizer configuration or template (finding 31). The parent carried unsloth's configuration, special-tokens
  map and template and no `tokenizer.json`, so its ids read as unresolved; this copy adds a `tokenizer.json` of
  17,078,037 bytes that matches no file the census has seen (unsloth's is 17,078,019 bytes, llmfan46's 17,078,174),
  a `chat_template.json`, and rewrites the configuration and map so that ids 32 and 33 read `<SPECIAL_32>` and
  `<SPECIAL_33>` where the parent says `[ARGS]` and `[CALL_ID]`; 998 of the 1,000 added-token entries are the
  parent's. The ids now resolve (1, 2, 11, 0). The tool counts 2,025 fields against the parent's 1,025, the extra
  thousand being the table the parent lacked; none is a change the original can be compared on.

Five of the seven Gemma 4 copies carry the template they were pinned against byte for byte (pairs 1, 2, 3, 4 and 6);
no template is blank-line-normalised or patched by its own maker this round, and the one patched template (pair 7)
is a duplicate's.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Arbitrary rank, 90 flags (pair 1): first shares 0.862 to 0.973 on the 44 edits and 0.001 to 0.003 on the four
  residues above the threshold, within-layer cosines of 0.002 to 0.10 on the 21 layers with both writers edited,
  counted on both. The thirteenth copy of the method, the third with the down projections, the first whose residue
  set straddles the threshold (six under, four over).
- The floor, 22 flags (pair 2): first shares 0.981 to 0.986 on 20 attention outputs whose change is 0.010 to 0.013
  of the norm, leftover 0.0012 to 0.0017, and two within-layer cosines of 0.925 on layer 59.
- Within-layer agreement, 8 flags (pair 3): four layers (16, 18, 19 and 27) whose two writers agree at 0.88 to
  0.95, under the 0.95 line, on a per-layer edit whose other 10 two-writer layers agree at 0.95 to 0.98.
- A shared direction without a weight, 6 flags (pair 6): three cosines of 0.899 to 0.910 to the group direction,
  two first shares of 0.980 and 0.989, one cross-kind direction at 0.617. The `single-projection-selected` entry
  matched the shape and the reading adds that the kept fraction reads nothing.
- The parents' flags on the duplicates (pairs 4, 5, 7 and 8): one floor share at 0.9899 on TrevorJS's layer 42,
  fifteen arbitrary-rank shares on llmfan46's copy, none on huihui-ai's.

The remaining fraction read a weight on four of the eight (0.63 to 2.93, the two strengths 1.16 to 1.40 and 0.34
to 0.82, the schedule 0.87 to 1.40, and 1.0 on pair 8) and the parents' weights on pairs 4, 5 and 7, and none on
pair 6. It read the side on seven: input on pairs 1 and 7, output on pairs 2, 3, 4, 5 and 8, neither on pair 6.

Two things the comparison could say by itself. A duplicate check before the download: a repository whose first
commit title begins "Duplicate from", or whose weight files carry LFS checksums the census has already measured,
is its parent's measurement and needs no compute (four of eight this round, 96 GB of downloads and eight compare
jobs for four results the hub's listing already gave). And a kernel read-back: when a card prints Heretic's
maximum weight, minimum weight, position and distance, the comparison can compute the implied kept fraction per
layer and report the agreement in one number per matrix, which would have named pair 3's schedule and pair 6's
disagreement without a reading.

## Owed to the metadata tool

Added this round, in `audit/compare.py` with tests in `tests/test_resave.py`: a sub-configuration data type written
where the other side left it null closes as the repeat of the top-level declaration (pairs 4 to 7, two fields each,
under any library); an absent field that both saved configurations load to the same value closes with the library
version recorded (pairs 4 to 7, four fields each, under a library that has the family's class; inert under 5.6.2).
What remains: the kit's own library, which cannot load the 12B family at all, so that every 12B copy's four defaults
stay open on the committed reports until the home environment moves past 5.10; the 5.16 `per_layer_config` form as
the library's own save (pair 2, the second time); the duplicate check above, which belongs in the pinner before a
pair is filed; a conversion lookup that names unsloth's files for pair 8's three unchanged ones and reports the
added `tokenizer.json` as new; and a rendering comparison between a copy and its named parent when the original
ships no template. To the batch: nothing from this round's duplicates, whose parents are measured; the Heretic
trials log the pair 6 card points to, if it carries the per-trial parameters, would let the kernel read-back be
tested on a copy whose card and weights disagree.

Weight differences alone cannot certify the absence of hidden behavior.
