# Reading of the Stage 1 and Stage 2 result: prithivMLmods/gemma-4-E4B-it-Uncensored-MAX against google/gemma-4-E4B-it (2026-10-30)

Measured on Blueback, round 7 piece 6 (round card 5291, compare jobs 3392878 to 3392885, 4 to 6 minutes each, exit 0;
pulled home by card 5302). Modified revision `19d2605f` (2026-06-01, a README commit; the weights were uploaded on
2026-04-13), original pinned at `83df0a88` (2026-04-10, 16:35Z). The maker's card says the copy is built on
huihui-ai/Huihui-gemma-4-E4B-it-abliterated, re-sharded for newer library versions, with "no modifications to weights
or architecture"; its `base_model` field names google/gemma-4-E4B-it, which is what the pin rule compared against.

## Weights (Stage 2)

The tool's assessment was "recipe match", nearest recipe `single-projection-selected`, 0 flags, on the cluster and
after re-scoring at home. On reading, the measurement is piece 2's measurement.

- The two reports agree in every one of 29,820 per-tensor fields across the 2,130 tensors (relative change,
  difference norm, extrema, singular values, energy shares, direction cosines, row norms, remaining fractions), and
  the two saved direction files are equal byte for byte (2,503,680 bytes). The two pinned originals, `ab4d2025` and
  `83df0a88`, carry the same weight file (shard checksum `cfbd3d2f`). The copy's weights are therefore the huihui
  copy's weights, stored in four shards instead of one.
- What that edit is: 70 of 2,130 tensors changed, the attention output and down projection in each of layers 7 to 41,
  one shared direction at cosine 0.999998, projection weight 2.5 read from the remaining fractions, row norms moved by
  up to 0.068. The reading of piece 2 carries the detail.

## Token and configuration side (Stage 1)

The tool's Stage 1 assessment is "unexplained differences" in one field on the cluster, `template.default`; the home
re-judgment explains `config.text_config.moe_intermediate_size` (null, the library default) and leaves the template.

- The copy's template equals the huihui copy's and Google's release template at `292a7e27` (2026-04-02) byte for
  byte, the template Google replaced on 2026-04-10. The fixed conversation renders identically. The tool's rule reads
  the original's later revisions only, so this earlier revision is read by hand.
- The copy was saved with transformers 5.6.0.dev0 against the original's 5.5.0.dev0.

## For the recipe library

Consistent with the card on both sides, and the first re-upload the census has measured: the card discloses the real
parent, the `base_model` field names the grandparent, and the weight fingerprint shows which is right. Two copies with the same original
whose measurements agree field for field are the same edit, and the comparison can say so without a reading. The
saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback7/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
