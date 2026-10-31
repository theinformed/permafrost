# Reading of the Stage 1 and Stage 2 result: huihui-ai/Huihui-gemma-4-31B-it-abliterated-v2 against google/gemma-4-31B-it (2026-10-31)

Measured on Blueback, round 12 piece 4 (push card 5366, round card 5367, download job 3399779, compare jobs 3399780 to
3399785, all exit 0, sweep 3399786; pulled home by card 5448). Modified revision `7db456ef` (2026-04-13, a card
commit; the repository was created on 2026-04-11 at 14:02Z and the weights were uploaded on 2026-04-12), original
pinned at `439edf56` (2026-04-10, 16:35Z, "Update schema"), whose weight file equals the release's (shards `eeef8791`
and `01891222` in both revisions). The maker's card names the method as abliteration with the
remove-refusals-with-transformers code and says this second version leaves the first 5 layers alone; it gives no
weight and no layer list beyond that, and reports a perplexity of 13,161 against 14,875 for the original and 13,336
for the first version, at f16 and a context of 8,192.

## Weights (Stage 2)

The tool's assessment was "recipe match", nearest recipe `single-projection-selected`, 0 flags, on the cluster and
after re-scoring at home. On reading, the footprint matches the card and the measures add the weight.

- 110 of 1,188 tensors changed: the attention output and the down projection in each of layers 5 to 59 of 60, the
  card's "first 5 layers have not been abliterated" read from the weights. Nothing else moved; the largest relative
  change outside the changed set is exactly 0.
- One shared direction. Within each kind the leading directions agree with their median at cosine 0.999994 or
  better, across kinds at 0.99998, and within each layer at 0.99999. First-value energy share is 0.9944 to 0.9971 on
  relative changes of 0.018 to 0.027; the leftover beyond the first direction is 0.00138 to 0.00147 of the weight
  norm, the storage floor.
- The projection weight reads off the weights. Along the shared direction the copy keeps −0.497 to −0.501 of the
  original's action in all 110 matrices, so the edit is `W − 1.5 r (rᵀ W)`, the weight mlabonne's Gemma 3 copy
  declares and this card does not. The maker's E4B copy of round 7 read 2.5 on 70 matrices and the 26B-A4B copy of
  piece 5 reads 3.0. Along the second to eighth directions the copy keeps 0.997 to 1.004. The left fraction is below
  the right on all 110: an edit on the output side.
- Row norms moved by 0.0045 to 0.643 relative (layer 59's down projection 0.643, layer 57's 0.322), as a projection at
  that weight must where a row lies along the direction; the E4B copy's largest was 0.068.
- Against the four other copies of this base (wangzhang in round 2, pieces 1, 2 and 3 of this round), which stand on
  the same original weight file, no changed matrix has an equal measurement in any field. The maker's first version of
  this copy is not in the census.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" in one field and the home judgement keeps it, so the committed card
reads "unexplained differences"; the reading closes it by hand.

- `template.default`: the copy's `chat_template.jinja` (12,045 bytes) is Google's release template of 2026-04-02
  (`419b2efe`), byte for byte the template the three other 31B pairs of this round were pinned against. The pin rule
  took the latest commit at or before the repository's creation, which is Google's 2026-04-10 revision carrying the
  "prefix-preserving tool calls" fix of 02:02Z that day and the schema update of 16:35Z; the repository was created
  21 hours after the second commit, and the maker worked from the release files. The fixed conversation renders
  identically. The earlier-revision case of round 7 (pairs 2 and 6, the same maker) again, which the tool cannot close
  because it reads the original's later revisions only.
- The configurations are equal in every field, both saved under transformers 5.5.0.dev0, and the tokenizer, special
  tokens and generation settings are unchanged.

## For the recipe library

Consistent with the stated change on both sides, with the weight (1.5) and the layer range (5 to 59) read from the
weights. The third shared-direction copy of this maker on a Gemma 4 base and the third weight: 2.5 on E4B, 1.5 here,
3.0 on 26B-A4B; a projection entry that carries a weight band would record it. The saved direction vectors are not
committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback12/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
