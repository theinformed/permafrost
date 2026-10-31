# Reading of the Stage 1 and Stage 2 result: DuoNeural/Mistral-NeMo-12B-Abliterated against mistralai/Mistral-Nemo-Instruct-2407 (2026-10-31)

Measured on Blueback, round 13 piece 7 (push card 5404, download job 3400579, compare job 3400586; pulled home by
card 5530). Modified revision `8440a3d7` (the repository was created on 2026-06-04 at 13:11Z), original pinned at
`04d8a905`. The card states the method in full: an orthogonal rank-1 projection on `down_proj` and `o_proj` of all
40 layers, direction by difference of means over 10 harmful and 10 harmless prompts at the last token of the final
layer, α 0.3, a KL divergence of 0.0004 on 10 benign probes, and a research note that the base answered 6 of 6
harmful probes before any weight was touched ("model was already compliant").

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 80 flags, on the cluster and
after re-scoring at home, all energy shares: 0.916 to 0.950, the storage floor on an edit three times weaker than
a full projection (relative change 0.0042 to 0.0058).

- 80 of 363 tensors changed: the attention output and the down projection of all 40 layers, the card's targets.
  Nothing else moved; the largest relative change outside the changed set is exactly 0 and 283 tensors equal the
  original.
- One shared direction: cross-layer cosine 0.9996 to 1.000 on all 80 matrices, the card's single difference of
  means.
- The left kept fraction is 0.703 to 0.708 on all 80: a weight of 0.29 to 0.30, the card's α 0.3 to the second
  decimal on both writers of every layer. The right is 0.80 to 0.96 and the left is below the right on 80 of 80,
  an output-side edit.
- Row norms moved by 0.003 to 0.007, the leftover of a scaled projection with no restoration step.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.0043, 0.923, 0.929, 0.70, 0.96 | 0.0043, 0.920, 0.926, 0.71, 0.80 | 0.30/0.29 | 1.00/1.00 | 0.0045, 0.0041 |
| 1 | 0.0044, 0.924, 0.930, 0.71, 0.93 | 0.0042, 0.919, 0.925, 0.71, 0.81 | 0.29/0.29 | 1.00/1.00 | 0.0051, 0.0040 |
| 2 | 0.0044, 0.924, 0.930, 0.71, 0.93 | 0.0043, 0.919, 0.926, 0.71, 0.81 | 0.29/0.29 | 1.00/1.00 | 0.0052, 0.0041 |
| 3 | 0.0043, 0.921, 0.928, 0.71, 0.93 | 0.0043, 0.919, 0.926, 0.71, 0.83 | 0.29/0.29 | 1.00/1.00 | 0.0030, 0.0040 |
| 4 | 0.0043, 0.921, 0.927, 0.71, 0.92 | 0.0043, 0.920, 0.926, 0.71, 0.82 | 0.29/0.29 | 1.00/1.00 | 0.0047, 0.0031 |
| 5 | 0.0043, 0.920, 0.926, 0.71, 0.93 | 0.0042, 0.919, 0.925, 0.71, 0.82 | 0.29/0.29 | 1.00/1.00 | 0.0047, 0.0039 |
| 6 | 0.0042, 0.918, 0.925, 0.71, 0.92 | 0.0043, 0.919, 0.926, 0.71, 0.82 | 0.29/0.29 | 1.00/1.00 | 0.0033, 0.0050 |
| 7 | 0.0042, 0.919, 0.926, 0.71, 0.92 | 0.0043, 0.920, 0.926, 0.71, 0.84 | 0.29/0.29 | 1.00/1.00 | 0.0051, 0.0048 |
| 8 | 0.0042, 0.918, 0.925, 0.71, 0.93 | 0.0042, 0.918, 0.924, 0.71, 0.86 | 0.29/0.29 | 1.00/1.00 | 0.0042, 0.0047 |
| 9 | 0.0042, 0.919, 0.925, 0.71, 0.92 | 0.0042, 0.919, 0.925, 0.71, 0.84 | 0.29/0.29 | 1.00/1.00 | 0.0054, 0.0046 |
| 10 | 0.0043, 0.921, 0.927, 0.71, 0.93 | 0.0042, 0.919, 0.926, 0.71, 0.83 | 0.29/0.29 | 1.00/1.00 | 0.0032, 0.0044 |
| 11 | 0.0044, 0.925, 0.931, 0.71, 0.93 | 0.0043, 0.920, 0.927, 0.71, 0.83 | 0.29/0.29 | 1.00/1.00 | 0.0034, 0.0041 |
| 12 | 0.0043, 0.921, 0.927, 0.71, 0.93 | 0.0043, 0.920, 0.926, 0.71, 0.83 | 0.29/0.29 | 1.00/1.00 | 0.0046, 0.0030 |
| 13 | 0.0044, 0.923, 0.929, 0.71, 0.93 | 0.0043, 0.920, 0.927, 0.71, 0.85 | 0.29/0.29 | 1.00/1.00 | 0.0047, 0.0034 |
| 14 | 0.0043, 0.920, 0.927, 0.71, 0.95 | 0.0042, 0.919, 0.926, 0.71, 0.85 | 0.29/0.29 | 1.00/1.00 | 0.0044, 0.0026 |
| 15 | 0.0044, 0.922, 0.928, 0.71, 0.93 | 0.0043, 0.919, 0.926, 0.71, 0.86 | 0.29/0.29 | 1.00/1.00 | 0.0042, 0.0033 |
| 16 | 0.0044, 0.923, 0.929, 0.71, 0.93 | 0.0043, 0.920, 0.926, 0.71, 0.84 | 0.29/0.29 | 1.00/1.00 | 0.0037, 0.0040 |
| 17 | 0.0045, 0.926, 0.931, 0.71, 0.92 | 0.0043, 0.919, 0.925, 0.71, 0.83 | 0.29/0.29 | 1.00/1.00 | 0.0043, 0.0034 |
| 18 | 0.0044, 0.923, 0.929, 0.71, 0.92 | 0.0043, 0.921, 0.927, 0.71, 0.81 | 0.29/0.29 | 1.00/1.00 | 0.0047, 0.0038 |
| 19 | 0.0044, 0.923, 0.929, 0.71, 0.94 | 0.0043, 0.920, 0.926, 0.71, 0.81 | 0.29/0.29 | 1.00/1.00 | 0.0050, 0.0050 |
| 20 | 0.0044, 0.922, 0.928, 0.71, 0.92 | 0.0043, 0.919, 0.926, 0.71, 0.80 | 0.29/0.29 | 1.00/1.00 | 0.0045, 0.0050 |
| 21 | 0.0044, 0.921, 0.928, 0.71, 0.91 | 0.0043, 0.920, 0.926, 0.71, 0.81 | 0.29/0.29 | 1.00/1.00 | 0.0057, 0.0042 |
| 22 | 0.0044, 0.925, 0.931, 0.71, 0.91 | 0.0043, 0.919, 0.926, 0.71, 0.81 | 0.29/0.29 | 1.00/1.00 | 0.0038, 0.0035 |
| 23 | 0.0043, 0.921, 0.927, 0.71, 0.91 | 0.0043, 0.919, 0.926, 0.71, 0.80 | 0.29/0.29 | 1.00/1.00 | 0.0038, 0.0044 |
| 24 | 0.0043, 0.922, 0.928, 0.71, 0.89 | 0.0043, 0.919, 0.926, 0.71, 0.80 | 0.29/0.29 | 1.00/1.00 | 0.0045, 0.0040 |
| 25 | 0.0044, 0.923, 0.929, 0.71, 0.88 | 0.0043, 0.920, 0.926, 0.71, 0.80 | 0.29/0.29 | 1.00/1.00 | 0.0051, 0.0032 |
| 26 | 0.0042, 0.918, 0.925, 0.71, 0.90 | 0.0042, 0.918, 0.925, 0.71, 0.81 | 0.29/0.29 | 1.00/1.00 | 0.0049, 0.0041 |
| 27 | 0.0044, 0.921, 0.927, 0.71, 0.89 | 0.0042, 0.918, 0.925, 0.71, 0.81 | 0.29/0.29 | 1.00/1.00 | 0.0053, 0.0044 |
| 28 | 0.0044, 0.922, 0.929, 0.71, 0.90 | 0.0042, 0.919, 0.925, 0.71, 0.81 | 0.29/0.29 | 1.00/1.00 | 0.0045, 0.0047 |
| 29 | 0.0043, 0.922, 0.928, 0.71, 0.89 | 0.0042, 0.918, 0.924, 0.71, 0.82 | 0.29/0.29 | 1.00/1.00 | 0.0041, 0.0044 |
| 30 | 0.0043, 0.920, 0.926, 0.71, 0.89 | 0.0042, 0.918, 0.925, 0.71, 0.83 | 0.29/0.29 | 1.00/1.00 | 0.0047, 0.0046 |
| 31 | 0.0043, 0.920, 0.927, 0.71, 0.89 | 0.0042, 0.916, 0.923, 0.71, 0.84 | 0.29/0.29 | 1.00/1.00 | 0.0035, 0.0041 |
| 32 | 0.0042, 0.918, 0.925, 0.71, 0.89 | 0.0042, 0.917, 0.923, 0.71, 0.83 | 0.29/0.29 | 1.00/1.00 | 0.0044, 0.0045 |
| 33 | 0.0044, 0.922, 0.929, 0.71, 0.91 | 0.0042, 0.917, 0.924, 0.71, 0.82 | 0.29/0.29 | 1.00/1.00 | 0.0038, 0.0045 |
| 34 | 0.0042, 0.919, 0.926, 0.71, 0.90 | 0.0042, 0.918, 0.924, 0.71, 0.82 | 0.29/0.29 | 1.00/1.00 | 0.0043, 0.0045 |
| 35 | 0.0044, 0.923, 0.929, 0.71, 0.90 | 0.0042, 0.918, 0.925, 0.71, 0.82 | 0.29/0.29 | 1.00/1.00 | 0.0052, 0.0051 |
| 36 | 0.0045, 0.926, 0.932, 0.71, 0.90 | 0.0043, 0.920, 0.926, 0.71, 0.81 | 0.29/0.29 | 1.00/1.00 | 0.0045, 0.0051 |
| 37 | 0.0046, 0.927, 0.933, 0.71, 0.91 | 0.0045, 0.924, 0.930, 0.71, 0.80 | 0.29/0.29 | 1.00/1.00 | 0.0033, 0.0050 |
| 38 | 0.0056, 0.948, 0.953, 0.70, 0.90 | 0.0050, 0.937, 0.942, 0.71, 0.82 | 0.30/0.29 | 1.00/1.00 | 0.0060, 0.0045 |
| 39 | 0.0058, 0.950, 0.954, 0.70, 0.94 | 0.0058, 0.949, 0.953, 0.70, 0.82 | 0.30/0.30 | 1.00/1.00 | 0.0066, 0.0064 |

Against grimjim's copy of the same base (pair 6), no changed matrix has an equal measurement in any field.

## Token and configuration side (Stage 1)

"Unexplained differences", 1,006 token fields and two configuration forms, all a re-save under transformers 5.10.1:
the 1,000 added tokens moved out of `tokenizer_config.json` into `tokenizer.json`, the rotary settings moved into
`rope_parameters`, `torch_dtype` renamed `dtype`, and the template moved into `chat_template.jinja` (closed at home,
it is the original's text). The fixed conversation renders identically.

## For the recipe library

Consistent with the card in every stated number: all 40 layers, both writers, one direction, α 0.3 read as 0.29 to
0.30 on 80 matrices, output side. This is the first copy in the census whose shared weight reads below one half on every matrix, and
its 80 flags are the floor on a weak edit, the finding 3 artefact at its clearest: the first-value share falls to
0.92 because the bfloat16 leftover is fixed while the edit is small. The saved direction vectors are not
committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback13/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
