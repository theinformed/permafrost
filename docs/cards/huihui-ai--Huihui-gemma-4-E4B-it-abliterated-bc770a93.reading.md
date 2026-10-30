# Reading of the Stage 1 and Stage 2 result: huihui-ai/Huihui-gemma-4-E4B-it-abliterated against google/gemma-4-E4B-it (2026-10-30)

Measured on Blueback, round 7 piece 2 (round card 5291, compare jobs 3392878 to 3392885, 4 to 6 minutes each, exit 0;
pulled home by card 5302). Modified revision `03ce1f3a` (2026-04-10), original pinned at `ab4d2025` (2026-04-10,
02:02Z). The maker's card names the method by its source, "remove-refusals-with-transformers", a difference-of-means
direction projected out of the layer matrices, and says the first five layers were left alone.

## Weights (Stage 2)

The tool's assessment was "recipe match", nearest recipe `single-projection-selected`, 0 flags, on the cluster and
after re-scoring at home. On reading, the footprint matches the card with one count off by two.

- 70 of 2,130 tensors changed: the attention output and the feed-forward down projection in each of layers 7 to 41 of
  42. Layers 0 to 6 are untouched, seven layers where the card says five. Nothing else moved; the largest relative
  change outside the changed set is exactly 0.
- One shared direction. Within each kind the leading directions agree with their median at cosine 0.999998 or better,
  across kinds at 0.999997, and within each layer at 0.999998. First-value energy share is 0.9989 to 0.9993 on
  relative changes of 0.046 to 0.061.
- The projection weight reads off the weights. Along the shared direction the copy keeps -1.501 to -1.499 of the
  original's action in all 70 matrices, so the edit is `W - 2.5 r (rT W)`: the output along the direction is reversed
  and enlarged by half. A weight-1 ablation leaves 0 and a reflection leaves -1. The card does not state a weight.
- Row norms moved by up to 0.068 relative, as a projection at that weight must.

## Token and configuration side (Stage 1)

The tool's Stage 1 assessment is "unexplained differences" in one field, `template.default`, before and after the home
re-judgment, and the reading closes it by hand.

- The copy's template (11,926 bytes) equals Google's release template at `292a7e27` (2026-04-02) byte for byte: the
  template the original repository carried until Google's commit `ab4d2025` ("prefix-preserving tool calls + dialog
  compliance") at 02:02Z on 2026-04-10. The copy's repository was created at 15:55Z that day and its weights uploaded
  at 18:05Z, so the pin rule chose the revision Google had published 14 hours earlier, while the maker worked from the
  earlier snapshot. The fixed conversation renders identically. The tool's later-revision rule reads only commits
  after the pinned one, which is why it did not find this.
- No configuration field differs.

## For the recipe library

Consistent with the stated change on both sides. For the recipe library this is the first measured projection weight
above 2: the remaining-fraction measurement reads 2.5 directly, where the round 2 mlabonne copy read 1.5. A template
that equals an earlier revision of the original repository is a second explanation the metadata tool should test
beside the later-revision rule. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback7/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
