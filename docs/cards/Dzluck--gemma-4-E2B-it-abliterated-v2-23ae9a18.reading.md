# Reading of the Stage 1 and Stage 2 result: Dzluck/gemma-4-E2B-it-abliterated-v2 against google/gemma-4-E2B-it (2026-11-02)

Measured on Wheat, round 35 piece 5 (download job 387143, compare job 387148, sweep 387152; the pull carries the
measurements and the sweep record and no job log). Modified revision `113010e1` (two commits on 2026-06-19:
created 16:29Z, the files at 16:32Z by the large-folder uploader), original pinned at `70af34e2` (06-03), the
revision current when the repository was created. The card is huihui-ai's: its first heading reads
"huihui-ai/Huihui-gemma-4-E2B-it-abliterated-v2", it names the maker's remove-refusals script, says "the first 5
layers have not been abliterated" and prints the maker's perplexity table (147.0 for the original, 164.5 for the
first version, 180.3 for this one). The hub confirms what the card says: huihui-ai/Huihui-gemma-4-E2B-it-abliterated-v2
(created 2026-04-11) serves one weight file `c1a72f14`, the file this repository carries, and its README, template,
tokenizer configuration, configuration and generation file are equal to this repository's byte for byte. Dzluck's
repository is a re-upload of huihui-ai's second E2B version under another name, with no duplicate relation in the
hub's metadata (the commit title is "Add files" where a hub duplicate's reads "Duplicate from"), and the pinner's duplicate rule, which compares
weight files against measured copies, had nothing to match because the parent is unmeasured. This is the only
measurement of huihui-ai's E2B v2 edit, the third such case after findings 64 and 73.

## Weights (Stage 2)

The tool's assessment was "recipe match", recipe `single-projection-selected`, 0 flags, on the cluster and after
re-scoring at home. On reading, the copy is the maker's shared projection at a weight of 2.50 from layer 5.

- 60 of 2,011 tensors changed: the attention output and the down projection of layers 5 to 34, the thirty layers
  the card leaves after "the first 5". Exactly 0 outside them; the 1,951 other tensors equal the original.
- One direction: the 60 leading vectors agree at 0.999999 within and across layers and kinds, first shares 0.9992
  to 0.9995.
- The weight is 2.50 on every matrix: the left kept fraction is -1.4997 to -1.5011 on all 60 (the output along
  the direction reversed and amplified by one and a half), the right 0.19 to 0.62 on the attention outputs and
  -1.01 to 0.29 on the down projections. Relative change 0.057 to 0.070, rows moved 0.015 to 0.15 under no claim.
- The direction is the first version's. Against the saved vectors of huihui-ai/Huihui-gemma-4-E2B-it-abliterated
  (round 13, weight 1.00 on layers 10 to 34) the left and right vectors agree at 1.000 on all 50 matrices both
  edit, and at 1.000 against prithivMLmods's re-upload of that file (round 18). Against the eight other E2B edits
  the agreement is 0.02 to 0.05 at the median (TrevorJS's, treadon's, anlord's and aifeifei798's reach 0.89 to
  0.96 on one or two matrices each).

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Rows |
| --- | --- | --- | --- |
| 5 | 0.0632, 0.9993, -1.4997, 0.12 | 0.0633, 0.9993, -1.5000, -0.10 | 0.061, 0.026 |
| 10 | 0.0640, 0.9994, -1.5000, 0.06 | 0.0661, 0.9994, -1.5000, 0.21 | 0.031, 0.046 |
| 15 | 0.0653, 0.9994, -1.5001, -0.00 | 0.0696, 0.9995, -1.4999, 0.06 | 0.017, 0.038 |
| 20 | 0.0631, 0.9993, -1.4997, 0.04 | 0.0638, 0.9994, -1.4999, -0.74 | 0.069, 0.046 |
| 25 | 0.0627, 0.9993, -1.4999, 0.11 | 0.0634, 0.9994, -1.5000, -1.01 | 0.057, 0.025 |
| 30 | 0.0668, 0.9994, -1.4999, 0.62 | 0.0630, 0.9993, -1.4999, -0.99 | 0.073, 0.015 |
| 34 | 0.0649, 0.9994, -1.5000, -0.32 | 0.0642, 0.9994, -1.5000, -0.74 | 0.140, 0.151 |

The full table (60 rows) is in the report. The single weight file `c1a72f14` equals the parent's and no measured
copy's.

What the second version is. The maker's first E2B edit projected one direction out of both writers of layers 10
to 34 at a weight of 1.00; the second projects the same direction, to the third decimal, out of layers 5 to 34 at
2.50, the weight the maker's E4B edit uses on layers 7 to 41 (finding 21). The card describes the change as five
layers added at the front and compares the versions by perplexity; it does not say the weight was multiplied by
two and a half. The maker's 31B went from 1.00 to 1.5 between its versions the same way (finding 21).

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, one field: the `default` template, an 11,926-byte file
against the pin's 17,336, rendering the fixed conversation identically. The copy's `tokenizer_config.json` is also
27 bytes shorter than the pin's. Both are Google's own earlier files: the template and the tokenizer configuration
are byte-equal (by sha256) to google/gemma-4-E2B-it at `4742fe84`, the release revision of 04-02 that was current
when huihui-ai made the edit on 04-11; the pin follows the re-uploader's creation date, two months and five
template revisions later. The later-revision rule reads the original's later commits and cannot see an earlier
one, the case round 31 left owed. Every other field is the pin's.

## For the recipe library

The single-projection entry matched with no flag, and the reading adds the weight (2.50), the window (5 to 34)
and the identity of the direction with the maker's first version. For the pinner: a copy whose README's first
heading names another repository is a re-upload candidate whatever the commit message says, and the duplicate
check has to compare weight files against the hub's listing of that repository, measured or not (finding 71's
rule, one step further); and a token-side difference that an earlier revision of the original explains should be
read against the snapshot current at the parent's creation rather than the re-upload's. The direction vectors stay in the
pull copy at `/opt/ai/hpc-packages/pulls/model-audit/wheat35/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
