# Census round 16: seven Gemma 4 and Mistral pairs (2026-10-31)

Seven published copies compared with their stated originals on Nautilus, 2026-10-31, from the batch pinned as
`data/batches/round-16-batch-1.json`: push card 5433, round card 5434, download job 4120061 (finished 00:42Z),
compares 4120062 to 4120068 on the background queue, sweep 4120069 (finished 03:00Z, exit 0), which deleted the six
original checkpoints (`237e5d8e` of yuxinlu1's coder fine-tune; `47b6801b` of the 26B-A4B original, shared by pairs 2
and 4; `66bc78a7` of the 12B original; `d4883f9b` of the Ministral 3 8B base; `3e22461f` of the E2B original;
`21b49d4b` of Mistral Small 24B 2501). Card 5467 pulled the measurements home. The compares ran under a kit defect
that lost their finish records and the drop records and cut pair 1's log, the one that built the environment, at 8
KB; the seven measurements are complete and read as every earlier round's. They were re-scored at home with the
recipe table as committed and the saved direction vectors, and no flag count moved. Every metadata report was judged
again at home under transformers 5.6.2 with the originals' commit histories, as every round with Gemma 4 copies has
needed. Each pair has a card (the tool's Stage 1 text after the home judgement, with the Stage 2 line) and a reading
note in `docs/cards/`; the measurements are in `results/weights/` and `results/meta/`, and the direction vectors stay
in the pull copy (`/opt/ai/hpc-packages/pulls/model-audit/nautilus16/measurements/pair-N/`). Pair 1 is a second
measurement of a copy round 8 measured against its grandparent, so its files carry the suffix `.parent` beside round
8's (the convention `.pass-2` set for second passes), and round 8's card is left as written.

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic | yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | violations, 8 flags (within-layer direction) | consistent with the card: against the parent only the 52 matrices the card lists changed, one shared rank-one direction; the card's weights still do not read (−0.09 to 0.95 kept where 1.24 to 1.48 would read −0.24 to −0.48), so the spread round 8 laid on the fine-tune is the edit's own |
| 2 | llmfan46/gemma-4-26B-A4B-it-uncensored-heretic | google/gemma-4-26B-A4B-it | violations, 27 flags (energy shares) | consistent: arbitrary-rank edits on the attention outputs of layers 2 to 29 (layers 1 and 5 rewritten under the threshold), input side, weights 0.42 to 1.52; no expert touched; the template is Google's 2026-04-28 template with the maker's tool-declaration patch |
| 3 | lemuralabs/Gemma-4-12B-uncensored-bf16 | google/gemma-4-12B-it | violations, 592 flags | not consistent: under a shared-direction ablation of layers 9 to 47 the copy carries yuxinlu1's coder fine-tune, recast to bfloat16, which the card names nowhere; 229 normalisation vectors equal round 8's measurement of that fine-tune to the last digit |
| 4 | prithivMLmods/gemma-4-26B-A4B-it-Uncensored-MAX | google/gemma-4-26B-A4B-it | match, 0 flags | consistent, and it is huihui-ai's edit: every field of all 1,013 tensors equals round 12's pair 5 and the direction files are equal byte for byte; weight 3.0 on layers 5 to 29 |
| 5 | Felldude/Ministral-3-8B-Uncensored | mistralai/Ministral-3-8B-Base-2512 | violations, 312 flags | not consistent with the stated original: dense training at 5 to 11 percent of every language-model matrix, saved in float32, under a chat template equal to Ministral-3-8B-Instruct-2512's byte for byte; an instruct-lineage model declared against the base |
| 6 | aifeifei798/Heretic-Scalpel-E2B | google/gemma-4-E2B-it | violations, 237 flags | the card's ablation and fine-tuning read as a per-layer ablation of rank one to three on the attention outputs of layers 10 to 34 and the down projections of 15 to 34, with 0.1 to 0.3 percent of training on every projection; the shared key-value tensors the card says it reconstructed are Google's bit for bit |
| 7 | venkycs/Mistral-Small-24B-Instruct-2501-Abliterated | mistralai/Mistral-Small-24B-Instruct-2501 | violations, 56 flags (floor) | consistent on the weights: one shared direction at weight 1.0 on every attention output and down projection of layers 1 to 39, the method of the huihui-ai card the maker copied; the template is the 2409 model's and renders every conversation differently |

Nothing moved outside the matrices the maker's method reaches in pairs 1, 4 and 7 (largest relative change outside
the changed set exactly 0) and in pair 2 (0.000235, an in-range layer rewritten near zero). The three others are the
round's result. Pair 3's 553 changed tensors and pair 5's 243 are dense changes the cards do not describe, and in
both the change can be named: pair 3's is yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1, because the 229
normalisation vectors it moved have difference norms equal to the last digit to round 8's measurement of that
fine-tune under richardyoung's ablation (which leaves them alone, pair 1 shows), and because the projections carry
the fine-tune's change at a quarter of its entries, which is what a float16 fine-tune becomes when recast to
bfloat16; pair 5's is instruction tuning plus the maker's, because the template is the instruct repository's file
and the base has none (finding 8's marker, on a second maker). Pair 6's 179 changed tensors are what its card says
in kind (an ablation and three fine-tunes) with one claim that reads as nothing: the 71 shared key-value tensors of
layers 15 to 34 that the card's first stage reconstructs read a relative difference of exactly 0.

The weights read off the weights: 3.0 on pair 4's 50 matrices (−1.998 to −2.004 remaining, huihui-ai's number on
this base), 1.0 on pair 7's 78 (−0.004 to −0.002), searched per-layer weights of 0.42 to 1.52 on pair 2's input side
(left above right on all 27, five under 1). Pairs 1 and 3 read no weight: −0.09 to 0.95 and −0.19 to 0.97 kept along
rank-one shared directions whose cards give 1.24 to 1.48 and nothing. Pair 1 is the test round 8 asked for. The
same copy against its parent instead of Google changes 52 tensors instead of 557 and leaves 625 at exactly 0, so the
fine-tune is gone from the measurement, and the kept fraction is the same spread as before. The maker's
`reproduce/config.toml` names two steps the calibrated projection does not have, a "full" row normalisation with a
rank-3 correction and an orthogonalised direction, and the reading leaves the cause between them. Pair 3's method
(a different tool, "ablation 1.3.0") reads the same way, with directions a few tens of degrees apart between the two
writers of a layer (within-layer cosine 0.42 to 0.90) where pair 1's agree (0.92 to 1.00).

Three fingerprints. Pair 4 is huihui-ai's 26B-A4B edit re-uploaded, every per-tensor field equal and the direction
files equal byte for byte (sha256 `2b8bd691`), the second such copy from this maker after finding 9's E4B; its weights
went up nine hours after huihui-ai's. Pair 3 carries yuxinlu1's fine-tune, the equality above, under its own
ablation: on the layers both edit, its directions and richardyoung's agree at cosine 0.75 to 0.93, on the layers
only one edits they are unrelated, and its changes are smaller than richardyoung's on every shared layer, so it was
made from the fine-tune and not from richardyoung's copy. Pair 1 against round 8's report on the same copy shares an
equal largest absolute difference on 16 of 52 matrices and nothing else, as two measurements against two originals
should. Across the base with the most copies, 26B-A4B, five copies by five makers are now measured on one original
weight file in six measurements (TrevorJS twice, huihui-ai, coder3101, llmfan46 and prithivMLmods), and apart from the re-upload no
changed matrix of any pair has an equal measurement in any field. None of the five edits reaches an expert: the 30
packed expert down tensors, the 30 gate-up tensors and the 30 routers are unchanged in huihui-ai's, coder3101's,
llmfan46's and prithivMLmods's copies, and only TrevorJS's (round 2) changed them. The two Mistral-family copies
share nothing with ccharnkij's Ministral copy of round 8: different originals, no equal field, and a change (5 to 11
percent) four to ten times that adapter's.

## The token side

The cluster's cards read "consistent with re-save noted" on pairs 1 and 4 and "unexplained differences" on the five
others. Re-judged at home, one field closes by tool (pair 6's `config.text_config.moe_intermediate_size`, the 5.6.2
default, as on round 12's pairs 1 and 2) and the rest close by hand, each pair its own case:

- Re-save, pairs 1 and 4: version strings only (5.10.2 to 5.12.1, 5.5.0.dev0 to 5.6.0.dev0). Pair 1's template,
  configuration (float16, `max_position_embeddings` 262144) and tokenizer equal the parent's, which settles round
  8's eight configuration differences as the parent's. Pair 4 was pinned to the release commit, so the
  earlier-revision case of the huihui-ai copies does not arise.
- A 5.10 re-save, pair 3: four audio and vision configuration values absent (640, 640, 640, 48) and two dtype fields
  repeated, under 5.10.1 against Google's 5.10.0.dev0. The four are class defaults a 5.10 save omits and the loader
  restores (finding 11's rule; the parent fine-tune's configuration, saved under 5.10.2, omits the same four). The
  copy's configuration otherwise equals Google's, `max_position_embeddings` 131072 included where the fine-tune it
  carries declares 262144: the configuration was written from Google's files and the weights from the fine-tune's.
  The template is Google's and renders identically. Judged again under transformers 5.22.1 after the home environment
  moved, the four close and the report reads "consistent with re-save noted" (finding 39).
- A loader's save, pair 6: no `transformers_version`, `torch_dtype` for `dtype` at every level, `per_layer_config`
  written out with the resolved head sizes, the end token repeated in the generation list, the 24 control tokens
  written into an `added_tokens_decoder` block, and the template written a second time into `tokenizer_config.json`:
  finding 15's loader signature, on a copy where it moved no token. Both templates equal Google's pinned one byte for
  byte and the fixed conversation renders identically.
- A patched Google template, pair 2: the copy's `chat_template.jinja` (17,344 bytes) matches none of Google's 13
  revisions and is Google's 2026-04-28 template (`4c55b528`, 16,934 bytes) with the maker's tool-declaration edits: a
  14-line `format_type_argument` macro prepended, five `is sequence` tests changed to `is iterable`, and four type
  comparisons rewritten to accept a type given as a list. The same macro and substitutions as the maker's E2B template
  of round 8 (finding 19), without the empty thought block that one adds, so the fixed conversation renders
  identically. A real change outside the card, to the tool path only.
- Another repository's template, pairs 5 and 7, the two real changes to what a conversation renders to or carries.
  Pair 5's base has no template and the copy's (7,759 bytes) equals Ministral-3-8B-Instruct-2512's byte for byte at
  that repository's first three revisions (2025-12-02 to 2026-06-30); with it come `tie_word_embeddings` false (the
  instruct configuration's key) and `dtype` float32, and a tokenizer re-saved without its `added_tokens_decoder`
  block and `special_tokens_map.json` (1,007 of the card's 1,011 fields; the ids and vocabulary are unchanged). Pair
  7's template (3,959 bytes) matches none of the 2501 repository's 54 revisions and equals
  Mistral-Small-Instruct-2409's byte for byte: the old `[INST] ... [/INST]` form with spaces and the system message
  folded into the last user turn, where the 2501 model was released with `[SYSTEM_PROMPT]` and no spaces; the fixed
  conversation renders differently (the reading has both strings). Pair 7's five other fields (three special tokens
  written as objects, the additional tokens as strings, `do_sample` true) are the forms Mistral committed 41 minutes
  after the pin (`e969dcf1`) and kept since, later-revision effects the rule would have closed had the template let it
  run.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Within-layer direction, 8 flags (pair 1): layers 26, 38, 39 and 42 at 0.918 to 0.950 under the per-layer entry's
  0.95 line, counted on both writers; the 15 other shared layers read 0.953 to 1.000. The method's two extra steps
  bend the two edits of a layer apart by a few degrees, as the biprojection does (finding 24).
- Arbitrary rank, 27 flags (pair 2): first shares 0.836 to 0.963, the profile the candidate entry of round 3 is for;
  eight copies of the method are now measured, all on the input side of the attention output, and this one takes
  the weight band down to 0.42 (layer 3) and adds two in-range layers rewritten under the threshold (0.000235 and
  0.000127), the residue case of round 12's pair 2 at a smaller size.
- The floor, 56 flags (pair 7): first shares 0.986 to 0.994 on changes of 0.013 to 0.019, leftover 0.0015 to 0.0016 of
  the norm, every one inside the 0.0025 line; the single-direction floor of finding 3 exactly.
- Nothing, on pair 4: the `single-projection-selected` entry matched huihui-ai's edit again, with the expert kind
  as the unchanged subset, and said nothing about the experts.
- Dense change under a projection envelope, 1,141 flags (pairs 3, 5 and 6: 592, 312 and 237). The envelope reports a
  fine-tune as hundreds of unexpected changes, failed energy shares and unrelated directions, which is right and
  unreadable. The reading sorted each by hand into training (relative change 0.1 to 11 percent, first share under
  0.1, 0.99 to 1.01 kept, unrelated directions) and the ablation above it (first share over 0.9 or a rank-two or
  rank-three profile with the first eight at 0.997), and the sort took the per-kind summary and nothing the tool
  does not already compute.

The remaining fraction read the weight of every single-direction edit in the round (3.00 and 1.00 to two decimals,
0.42 to 1.52 searched) and the side of every edit (output side on pairs 4 and 7 and on 42 of pair 6's 45 ablated
matrices, input side on all 27 of pair 2), and it read no weight on the two row-normalised ablations (pairs 1 and
3), as round 8 found and this round confirms with the fine-tune removed. Pair 6 adds the first edit with more than
one direction per matrix: first shares 0.43 to 0.74 with the first eight at 0.997 and singular values such as 2.33,
1.70, 0.10, read by the energy-share rule as 57 violations. A rank the scorer reads per matrix (the count of
singular values above a fraction of the first) would name it as one number per matrix.

Three things the comparison could say by itself. A dense change should be sorted before the envelope is applied: a
"training" line per kind (relative change, first share under 0.1, kept fraction at 1, unrelated directions) with the
envelope applied to what is left, which on pair 3 would have reported "fine-tune in 505 tensors, shared-direction
ablation on 87" instead of 592 flags. A measurement equal to another report's on tensors an ablation does not touch
identifies a parent, and the comparison has every number it needs in `results/weights/`: pair 3 against round 8's
richardyoung report (229 normalisation vectors equal to the last digit) is the case, and finding 9's fingerprint test
across whole reports is the same test on the whole copy. And a rank per matrix, as above.

## Owed to the metadata tool

The earlier-revision rule (no case this round; four cases, all huihui-ai's); a patched-template reading that names
the nearest publisher commit and the lines that differ (pair 2, the second case after round 12's pair 1); a
template lookup across every original the census has cached, so that a template equal to another repository's file
is named as such (pairs 5 and 7, and 3MPER0RR's in round 7: three copies whose template names a parent the card does
not); the later-revision rule run field by field when the template differs (pair 7's five fields); the 5.10
class-default list (pair 3's four fields, finding 11's rule on a newer library); the loader signature read as one
cause (pair 6's 29 fields); and the whitespace-normalised comparison that drops blank lines (round 12's three cases,
none this round). To the batch: Felldude's copy against Ministral-3-8B-Instruct-2512 and 3MPER0RR's against
Mistral-7B-Instruct-v0.3, the two instruct-lineage copies declared against their bases; lemuralabs's copy against
yuxinlu1's fine-tune, which would leave its ablation alone; huihui-ai's own Mistral Small 2501 copy, for the
fingerprint test pair 7 asks for; and huihui-ai's first 31B version from round 12's list.

Weight differences alone cannot certify the absence of hidden behavior.
