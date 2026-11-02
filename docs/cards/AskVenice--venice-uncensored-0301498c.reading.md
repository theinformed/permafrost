# Reading of the Stage 1 and Stage 2 result: AskVenice/venice-uncensored against dphn/Dolphin-Mistral-24B-Venice-Edition (2026-11-02)

Measured on Wheat, round 45 piece 5 (download job 387355, compare job 387360, sweep 387364; the pull carries the
measurements and the sweep record and no job log). Modified revision `12e3e8cc` (created 2025-11-25 21:28Z, the
weights uploaded at 11-26 17:46Z "via LFS", two card edits after), parent pinned at `853f8702` of 2025-09-08,
dphn's Venice Edition of Mistral Small 24B Instruct 2501 (created 2025-06-12, the weights uploaded at 05:34Z that
day and replaced by a version 1.2 with a vision tower on 2026-04-16). The card is Venice.ai's "Venice Uncensored
(Dolphin Mistral 24B)", "a special edition of the renowned Dolphin series" made with the Dolphin team, with
`base_model` naming Mistral's instruct model and dphn's edition; it prints no method, no layer and no count, and its
system prompt is the parent's. The copy's ten shards (`65828eac` to `2ca2d9db`) are the parent's ten from its
upload of 06-12 to the pinned revision by the hub's object ids, an upload of the same files under a second name
rather than the hub's duplicate function; the configuration, the generation file, the shard index, the special-token
map and the token configuration are re-saves with other object ids, and the `tokenizer.json` is the parent's and
Mistral's (`b76085f9`).

## Weights (Stage 2)

The tool's assessment was `unchanged`, with one flag (`missing_changed_projection`, the nearest entry asking for
a changed writer), on the cluster and after re-scoring at home. On reading, the copy is its parent.

- 0 of 363 tensors changed: every tensor reads exactly 0, the first copy in the census with an empty changed set.
- No direction to read; the saved vector file holds no entry.

What the copy's uncensoring is, in the method's vocabulary, is the parent's fine-tune. By byte range at layer 20 the
parent's attention output stands 0.0056 from Mistral Small 24B Instruct 2501's, its query projection 0.0043 and its
down projection 0.0035; the difference is spread over many components (first shares 0.082 on the attention output,
0.29 on the query projection and 0.22 on the down projection, the later components at 0.01 to 0.06 each), the shape
of training and not of a projection, and its leading direction stands at 0.35 on the attention output and 0.073 on
the down projection to venkycs's projection of the same instruct model, and at 0.19 and 0.016 to saukko's projection
of the R1 fine-tune (pair 4). The instruct model itself stands 0.034 to 0.038 from the base checkpoint on those
three matrices, so the Venice fine-tune moved the instruct model by about a tenth of the distance the instruct
tuning moved the base.

## Token and configuration side (Stage 1)

"Consistent" on the cluster and at home: no compared field differs. The token ids are Mistral's on both sides
(`bos_token_id` 1, `eos_token_id` 2, no pad token), the vocabulary is 131,072, and the 1,150-byte V7-Tekken template
renders the fixed conversation identically.

## For the recipe library

An unchanged pair needs no entry; the scorer's one flag is the nearest entry's request for a changed writer and
would read as a re-upload line beside the hub-duplicate rule of finding 38, which the copy's object ids satisfy
though its first commit is no duplicate.

Weight differences alone cannot certify the absence of hidden behavior.
