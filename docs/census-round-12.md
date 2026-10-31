# Census round 12: six Gemma 4 31B and 26B-A4B pairs (2026-10-31)

Six published copies compared with their stated originals on Blueback, 2026-10-30 and 31, from the batch pinned as
`data/batches/round-12-batch-1.json`: push card 5366, round card 5367, download job 3399779 (finished 20:57Z),
compares 3399780 to 3399785 on the background queue (exit 0), sweep 3399786 (finished 01:03Z on 10-31, exit 0), which
deleted the four original checkpoints (`419b2efe` of the 31B original, shared by pairs 1 to 3; `439edf56` of the same
original for pair 4; `7d4c97e5` and `47b6801b` of the 26B-A4B original for pairs 5 and 6; the two revisions of each
original carry one weight file). Card 5448 pulled the measurements home at 01:13Z. The six pins are round 6's,
refiled after round 9's compares died in a venv build race before reading any weights, and the six compares released
together ran clean under the serialized venv build. They were re-scored with the recipe table as committed today and
the saved direction vectors; the kit carried the same table, so no flag count moved. Every metadata report was judged
again at home under transformers 5.6.2 with the originals' commit histories, as every round of Gemma 4 copies has
needed (the kit's pinned 4.56.2 has no Gemma 4 class and the compute nodes have no hub access). Each pair has a card
(the tool's Stage 1 text after the home judgement, with the Stage 2 line) and a reading note in `docs/cards/`; the
measurements are in `results/weights/` and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/blueback12/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | llmfan46/gemma-4-31B-it-uncensored-heretic | google/gemma-4-31B-it | violations, 18 flags (energy shares) | consistent with the card: arbitrary-rank edits on the 18 attention outputs of layers 30 to 47, input side, weights 1.37 to 3.36; the template is Google's latest with one line changed by the maker |
| 2 | coder3101/gemma-4-31B-it-heretic | google/gemma-4-31B-it | violations, 58 flags (energy shares) | consistent: 58 attention outputs rewritten in layers 1 to 58, 35 of them arbitrary-rank edits at weights 0.51 to 10.18 and 23 rounding residues at weight near zero; the claimed row-norm preservation reads 0.007 |
| 3 | TrevorJS/gemma-4-31B-it-uncensored | google/gemma-4-31B-it | violations, 54 flags (52 floor, one layer's direction) | consistent: one direction per layer on every attention output and down projection of all 60 layers, row norms within 0.0004, scale 1.0 with the biprojection's second term; the token side reads consistent on the cluster |
| 4 | huihui-ai/Huihui-gemma-4-31B-it-abliterated-v2 | google/gemma-4-31B-it | match, 0 flags | consistent: one shared direction on every attention output and down projection in layers 5 to 59, weight 1.5 |
| 5 | huihui-ai/Huihui-gemma-4-26B-A4B-it-abliterated | google/gemma-4-26B-A4B-it | match, 0 flags | consistent, the expert statement included: one shared direction on the attention output and the shared down projection in layers 5 to 29, weight 3.0, and no expert touched |
| 6 | coder3101/gemma-4-26B-A4B-it-heretic | google/gemma-4-26B-A4B-it | violations, 20 flags (energy shares) | consistent: arbitrary-rank edits on the 20 attention outputs of layers 10 to 29, input side, weights 0.76 to 1.49; no expert touched; the claimed row-norm preservation reads 0.007 |

In all six pairs nothing moved outside the matrices the maker's description reaches: the largest relative change
outside the changed set is exactly 0 in every one. All six are ablations and read as their cards say, with the weight
and the side of the edit read off the weights: 1.5 on all 110 matrices of pair 4 and 3.0 on all 50 of pair 5, two
shared-direction projections whose cards give no number; scale 1.0 under a biprojection on pair 3 (−0.10 to 0.71
remaining along the leading output direction, left below right on 118 of 120); searched per-layer weights on the
input side of the attention outputs on the three arbitrary-rank copies, 1.37 to 3.36 (pair 1), 0.51 to 10.18 (pair 2)
and 0.76 to 1.49 (pair 6), the left fraction above the right on all 73 of their edited matrices.

These are the second measured copies on each of the two larger Gemma 4 bases (round 2 measured wangzhang's 31B copy
and TrevorJS's 26B-A4B copy). On the 31B dense model the recipes touch what they touch on E4B and 12B: the attention
output (5376 by 8192, or by 16384 in the ten global layers) alone for the two arbitrary-rank copies, the attention
output and the down projection (5376 by 21504) for the biprojection and the shared projection. The query, key and
value projections, the gate and up projections, the normalisation vectors and the 356 vision-tower tensors are
unchanged in all four 31B pairs; wangzhang's copy of round 2 remains the only one on this base that edits the reading
side. On the mixture the two edits stop at the dense modules: huihui-ai's changes the attention output (2816 by 4096,
or by 8192 in the five global layers) and the shared down projection (2816 by 2112) of layers 5 to 29, coder3101's the
attention output of layers 10 to 29, and the 30 packed expert down tensors (128 by 2816 by 704), the 30 packed gate-up
tensors (128 by 1408 by 2816) and the 30 routers are unchanged in both. TrevorJS's copy of round 2 changed all 128
experts of every layer, and huihui-ai's own Qwen3 30B-A3B copy changed all 6,144 expert down projections; on this
base, where the experts are one packed parameter per layer rather than a linear module each, the same maker's tool
leaves them alone, and its card says so (with 256 experts named where the configuration has 128). The scorer has a
kind for the packed expert tensors and measured them expert by expert on the TrevorJS copy; here it had nothing to
measure, and the "selected" entry let it skip the kind, which is why pair 5 is a clean match. It has no kind for the
router projection, scale and per-expert scale (90 tensors on the mixture), the per-layer scalar, the query and key
normalisations or the extra feed-forward normalisations of the mixture (three per layer), all classed "other" and all
unchanged in every pair.

No duplicate fingerprint turned up. The five 31B copies now measured (wangzhang in round 2 and the four of this round)
stand on one original weight file (shards `eeef8791` and `01891222`, the same in Google's 04-02 and 04-10 revisions),
and the three 26B-A4B copies (TrevorJS in rounds 2 and 3, pairs 5 and 6) on another (`11276849` and `aab47033`); across
every pair of them no changed matrix has an equal measurement in any field. Across sizes each maker's method reads the
same. TrevorJS's biprojection, now measured on four bases (E4B, 12B, 26B-A4B, 31B), holds every row norm within 0.0004
on the dense matrices, reads scale 1.0 with the second term, and dips below the 0.95 within-layer line in the same
part of the model each time (layer 12 at 0.925 here, layers 10 and 12 on 26B-A4B before the experts' direction
joined, three layers at 0.934 to 0.947 on E4B). llmfan46's arbitrary-rank copies, four on three bases, edit the
attention outputs only, on the input side, without restoring norms, at weights that rise with the base (1.27 to 1.79 on
E4B, 1.86 to 4.41 on E2B, 1.37 to 3.36 on 31B); on 31B every layer of the declared range changed, where the E4B copies
left 17 and 13 in-range layers within 0.00008. coder3101's three copies (E4B, 31B, 26B-A4B) claim row-norm preservation
and read 0.0059 to 0.0080 on all 75 edited matrices, a residue the restoration step leaves at the same size on every
base; its 31B copy rewrote 58 layers and left 23 as rounding residues (relative change 0.0013 to 0.0018, first share
0.002 to 0.028), and its layer 48 carries the largest edit of the method so far (weight 10.18, relative change 0.169).
huihui-ai's shared projection reads three weights on three Gemma 4 bases: 2.5 on E4B (layers 7 to 41), 1.5 on the 31B
second version (layers 5 to 59), 3.0 on 26B-A4B (layers 5 to 29). The two coder3101 copies also share one template
file byte for byte (below), committed three minutes apart.

## The token side

The cluster's cards read "unexplained differences" on five of the six pairs and "consistent" on pair 3, the first
Gemma 4 copy whose cluster card needed no home judgement (release template byte for byte, configuration equal in every
field, both sides saved under 5.5.0.dev0). Re-judged at home, the null `config.text_config.moe_intermediate_size` of
pairs 1 and 2 closes by tool as the 5.6.2 default, and the two configuration files of pair 1 settle it without the
tool: they differ in that one line and in the version string (5.5.0.dev0 against 5.5.0) and in nothing else, and the
text configuration carries `enable_moe_block` false and `num_experts` null on both sides, so the field is a default
for a block the dense model does not have. Pair 1's version strings are re-save effects. Nothing else moves by tool;
the five templates close by hand, each a different case:

- Google's earlier revision, pairs 4 and 5. Both huihui-ai copies carry the 2026-04-02 release template byte for byte
  (12,045 bytes; the template pairs 1, 2, 3 and 6 were pinned against), and both were pinned against Google's
  2026-04-10 revision because each repository was created after it (21 hours after on 31B, 10 hours after on 26B-A4B).
  The weight file is the same in both revisions, so the weight pin holds; the maker worked from the release files, as
  it did on the E4B copy in round 7. The tool reads the original's later revisions only, and the earlier-revision rule
  owed since round 7 is still owed. Every fixed conversation renders identically.
- Google's later revision with blank lines removed, pairs 2 and 6. Both coder3101 copies carry Google's 2026-04-10
  template (16,448 bytes, the same file in the 31B and 26B-A4B repositories) with its 15 blank lines removed and
  nothing else changed (16,433 bytes), one file byte for byte in both copies, committed at 16:39Z and 16:42Z on
  2026-04-14; both repositories were created on 2026-04-02 within ten hours of the release, so the pins took the
  release template. The same pattern as the maker's E4B copy in round 8 (14 blank lines). The later-revision rule
  compares byte for byte after line endings and trailing whitespace, and blank lines defeat it: a re-save effect in
  all but the rule's letter. Both render identically.
- Google's latest template with one line changed by the maker, pair 1. llmfan46's `chat_template.jinja` (18,841
  bytes) is Google's 2026-07-15 template (`68abe480`, carried unchanged through the current `842da379`; 18,683 bytes,
  with Google's own "Published: 2026-07-09" header) with one line changed: every model turn in the history gets an
  empty thought block (`<|channel>thought`, newline, `<channel|>`) after `<|turn>model` whenever thinking is off and
  the message carries no reasoning field, where Google's template writes nothing. The fixed conversation renders at
  232 bytes against 204. The maker's commit of 2026-09-19 uploaded, beside it, a file named
  `chat_template.jinja.official-2026-07-09.bak` that equals Google's 2026-07-15 template byte for byte and deleted it
  nine seconds later; the maker replaced the template seven times between 2026-04-14 and 2026-09-19. Google's card
  says the 26B and 31B models emit the empty block themselves when thinking is off and that earlier turns' thoughts
  are not to be added to the history. A real change by the maker to the prompt of every multi-turn conversation with
  thinking off, outside the card, and the second template in the census (after Jiunsong's in round 8) that changes
  what a conversation renders to.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Arbitrary rank, 73 flags (pairs 1, 2 and 6), the energy-share profile that climbs only to 0.93 to 0.99 by the eighth
  value. Seven copies of the method are now measured, all on the input side of the attention output, with searched
  per-layer weights of 0.51 to 10.18; the candidate entry of round 3 should take its first-share line down to 0.65
  (pair 6's layer 10, first share 0.659, first eight 0.918) and its weight band below 1 (five matrices read 0.51 to
  0.92) and up to 10.2. Two of the seven claim row-norm preservation and read 0.007.
- Rewritten layers at weight near zero, 23 flags (pair 2): relative change 0.0013 to 0.0018, first share 0.002 to
  0.028, remaining fractions at 1 on both sides, row norms within 0.0008. The energy-share rule reads a matrix that
  was rewritten and barely moved as a failed rank-one edit; a line for a changed matrix with no structure (relative
  change under 0.002, first share under 0.05, fractions at 1) would name it, as it would have named layer 41 of the
  maker's E4B copy in round 8.
- The floor, 52 flags (pair 3): shares 0.975 to 0.990 on changes of 0.0135 to 0.025, leftover 0.0012 to 0.0032; 119 of
  the 120 matrices sit inside the calibrated 0.0025 line and one (layer 2's attention output, 0.0032) sits outside it,
  where the biprojection's input-side term holds 0.016 of the energy in the second direction. The norm-preserving
  biprojection, measured on four bases, is a method whose second term the single-direction floor does not quite cover.
- Within-layer direction, 2 flags (pair 3): layer 12 at 0.925 under the per-layer entry's 0.95 line, the one layer of
  60; the method's second term bends the two edits of a layer apart by a few degrees, most in the early-middle layers
  on every base it has been measured on.
- Nothing, on pairs 4 and 5: the first clean matches since round 7's huihui-ai E4B pair and its re-upload. The
  `single-projection-selected` entry matched because it allows any subset of the residual writers to stay unchanged;
  on pair 5 that subset is the whole expert kind, and the entry does not say so. The matches carry no weight; the
  remaining fraction read 1.50 on 110 matrices and 3.00 on 50.

The remaining fraction read the weight of every edit in the round: 1.50 and 3.00 to two decimals on the two shared
projections (−0.497 to −0.501 and −1.998 to −2.004), the biprojection's scale 1.0 with its second term (medians 0.11
on the attention outputs and 0.03 on the down projections of pair 3), and the searched per-layer weights of the three
arbitrary-rank copies, including the first weights under 1 on the method (0.51 on pair 2's layer 50, 0.76 to 0.92 on
four layers of pair 6). It read the side of every edit: output side on the 280 matrices of pairs 3, 4 and 5 (left
below right on 278), input side on the 73 arbitrary-rank edits (left above right on all). The row norms sort the
restorations as before: 0.00006 to 0.00037 on the biprojection, 0.0059 to 0.0080 on the two copies that claim
preservation and approximate it, 0.0016 to 0.037 on the copy that claims none, 0.0045 to 0.643 on the shared
projections at weights 1.5 and 3.0.

Two things the comparison could say by itself. On a mixture it should report whether the expert tensors were reached
(pair 5 against TrevorJS's copy of the same base, two readings of one base that differ in 3,840 expert matrices), as
a line in the summary rather than a skipped kind. And a matrix that changed below 0.002 with no structure should be
named as rewritten at weight near zero rather than flagged as a failed projection (pair 2's 23).

## Owed to the metadata tool

The earlier-revision template rule (pairs 4 and 5, owed since round 7, four cases now, all this maker); a
whitespace-normalised template comparison that drops blank lines (pairs 2 and 6, three cases now, all this maker); a
"patched Google template" reading that names the nearest Google commit and the lines that differ, with the rendering
difference beside it (pair 1; a one-line patch to the latest template is a case the later-revision rule can nearly
close and should report as such). And to the batch: huihui-ai's first version of the 31B copy, the only one of the
maker's three Gemma 4 copies not measured, and the parent pairs owed since round 8.

Weight differences alone cannot certify the absence of hidden behavior.
