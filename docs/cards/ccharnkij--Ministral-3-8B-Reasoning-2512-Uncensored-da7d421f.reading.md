# Reading of the Stage 1 and Stage 2 result: ccharnkij/Ministral-3-8B-Reasoning-2512-Uncensored against mistralai/Ministral-3-8B-Reasoning-2512 (2026-10-30)

Measured on Blueback, round 8 piece 8 (round card 5305, download job 3397500, compare jobs 3397501 to 3397508, all exit
0, sweep 3397509; pulled home by card 5347). Modified revision `4dca5a4f` (2026-06-08, a README commit; the weights
were uploaded on 2026-04-18), original pinned at `6c2c4c82` (2026-01-15). The maker's card says the copy is a LoRA
fine-tune of the reasoning model that removes refusals and allows adult content while keeping its reasoning and
image input; it names no adapter rank, target modules, data or evaluation. The first Ministral 3 copy in the census.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 307 flags, on the cluster and
after re-scoring at home: 170 unexpected changes, 68 energy shares, 68 direction cosines and one cross-kind
direction. On reading, the footprint is a merged low-rank adapter on every projection of the text model and no
ablation, which is what the card says.

- 238 of 531 tensors changed: the query, key, value, output, gate, up and down projections of all 34 layers, and
  nothing else. The token embedding, the output head, the 69 normalisation vectors and the 222 tensors of the vision
  tower and its projector are unchanged; the largest relative change outside the changed set is exactly 0.
- Relative change 0.006 to 0.018 per matrix (medians 0.006 on the down projections to 0.012 on the value
  projections). First-value energy share 0.15 to 0.90 (kind medians 0.26 to 0.61), first eight values 0.67 to 0.99
  (kind medians 0.74 to 0.94); the singular values fall slowly (first over second 1.0 to 5.6, median 1.5). The change
  is spread over more than eight directions on most matrices and its first eight carry two thirds to all but one
  percent of it: a low-rank change, with a rank above eight.
- Nothing was projected out. Along every leading direction on both sides the copy keeps 0.94 to 1.05 of the
  original's action (medians 1.000), where an ablation reads 0 and a scaled projection reads below 0. The leading
  directions are unrelated across layers (cosine 0.14 to 0.47 with their median by kind) and within layers (0.29 to
  0.37).
- Row norms moved by 0.0002 to 0.0036 relative.
- The copy is one 17.8 GB file against the original's four shards and a consolidated file; the shard checksums
  differ as a re-save must. The original and the copy are both bfloat16.

## Token and configuration side (Stage 1)

The tool's Stage 1 assessment is "consistent with re-save noted" on the cluster and at home, ten fields: the version
strings (5.0.0.dev0 to 5.3.0), four fields absent on one side that load as the same default (the kit's 4.56.2 has the
Mistral 3 classes), three data types repeated into sub-configurations, and a pad token repeated from the generation
settings. The chat template (6,206 bytes) equals the pinned revision byte for byte; Mistral replaced it on 2026-07-15
(`81eaece1`, 12,207 bytes), after the copy, and the pin rule chose the January revision. Vocabulary, special tokens
and generation settings are unchanged.

## For the recipe library

Consistent with the card on both sides, and the first copy in the census whose refusal removal is training alone:
no direction leaves the weights, the remaining fractions sit at 1 on all 238 matrices, and the change is low-rank on
every projection. The measures that separate it from an ablation are the remaining fraction near 1, the slow fall
of the singular values and the absence of any shared direction; a "merged adapter" line beside the dense-change
line would name it. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback8/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
