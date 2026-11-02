# Reading of the Stage 1 and Stage 2 result: nbeerbower/Gemma4-Gutenberg-31B-Heretic against coder3101/gemma-4-31B-it-heretic (2026-11-02)

Measured on Wheat, round 47 piece 8 (download job 387398, compare job 387406, sweep 387407; the pull carries the
measurements and the sweep record and no job log). Modified revision `289d4af0` (created 2026-06-16 11:35Z, the
weights uploaded at 16:57Z under the title "Gemma4-Gutenberg-31B-Heretic (Gutenberg ORPO merge)", the license line
fixed at 18:45Z), parent pinned at `9a1c7f5d` of 2026-04-14, coder3101's arbitrary-rank Heretic 1.2.0 edit of
google/gemma-4-31B-it, which the census measured against Google at this revision
(`results/weights/coder3101-gemma-4-31B-it-heretic.json`, 58 attention outputs of layers 1 to 58, 23 of them
residues, finding 22); the two shards (`57338b5e`, `607d371a`) are the ones that measurement read. The card is an
ORPO fine-tune for literary prose: a rank-64 adapter on the text decoder merged to full, 454 steps on 14,816
preference pairs, and "the same Gutenberg ORPO adapter merged in" as the maker's Gemma4-Gutenberg-31B, which went
onto google/gemma-4-31B-it 24 minutes earlier. It is the census's first fine-tune applied on top of a measured edit,
the reverse of the usual order. The parent is a copy the census already counts, measured against its own parent, so
this pair adds a measurement and a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 459 flags (262 unexpected changes, 98
first shares, 98 direction cosines, 1 cross-kind cosine), on the cluster and after re-scoring at home. On reading,
the copy is training on the text decoder with no direction, and the edit under it is untouched.

- 360 of 1,188 tensors changed: 55 query, 51 key, 48 value, 58 attention output, 53 gate, 55 up and 40 down
  projections, and 50 more linear maps moved just under the threshold (0.0005 to 0.000999, the largest relative
  change outside the changed set). The 356 vision tensors, the embedding and every normalisation vector read
  exactly 0.
- No direction: first shares 0.04 to 0.95, both kept fractions near 1 on every matrix (left 0.90 to 1.11, right
  0.98 to 1.12).
- Relative changes 0.0010 to 0.0077 (median 0.0023); rows moved 0.00005 to 0.0149.

| Kind | Matrices | Relative change |
| --- | --- | --- |
| Query projection | 55 | 0.0010 to 0.0072 |
| Key projection | 51 | 0.0010 to 0.0038 |
| Value projection | 48 | 0.0010 to 0.0030 |
| Attention output | 58 | 0.0010 to 0.0032 |
| Gate projection | 53 | 0.0010 to 0.0077 |
| Up projection | 55 | 0.0010 to 0.0059 |
| Down projection | 40 | 0.0010 to 0.0064 |

Directions. Against the saved vectors of the thirty-seven other 31B measurements, the training's leading vectors
stand at 0.028 or less on the left to every one on the attention outputs, and at 0.010 to coder3101's edit (56
names). By byte range, on the layer 30 and 45 attention outputs (coder3101's edit, 0.0312 and 0.0343 from Google's
with first shares 0.961 and 0.967): the copy stands 0.00172 and 0.00192 from coder3101's, the maker's standard
Gutenberg stands 0.00172 and 0.00192 from Google's, and the two changes agree at a cosine of 0.994 and 0.997 (they
differ by 0.108 and 0.080 of the change, the bfloat16 rounding of two merges); the copy's change along the edit is
0.00000 and 0.00002 of the edit, and the copy's difference from Google's stands at 0.998 to the edit. On the layer
30 query projection, where coder3101's matrix is Google's bytes, the copy and the standard Gutenberg are
byte-equal. On the layer 10 and 16 attention outputs, two of coder3101's residues, the training moves the matrices
by 0.00115 and 0.00095 and agrees with the standard Gutenberg's at 0.9997 and 0.9996. So the adapter was trained
once and merged onto two bases, and on the base that carries the edit it left the edit where it was.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the version strings move from 5.5.0.dev0 to 5.8.0. The
template (16,433 bytes, `1db0e6d4`) and `tokenizer.json` are the parent's by object id, where the standard Gutenberg
carries Google's 17,466-byte revision of 05-18; the copy publishes a `processor_config.json` in place of the parent's
`preprocessor_config.json`. The token ids are the instruct checkpoint's through the parent (`eos_token_id`
`[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0) and the vocabulary is 262,144.

## For the recipe library

No entry reads training; a training entry would read the copy as its card says. A line that compares a training
pair's change with the parent's measured edit would read "edit kept" here from the saved vectors alone. The
direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat47/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
