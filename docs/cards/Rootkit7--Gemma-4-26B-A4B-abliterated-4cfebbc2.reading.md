# Reading of the Stage 1 and Stage 2 result: Rootkit7/Gemma-4-26B-A4B-abliterated against google/gemma-4-26B-A4B-it (2026-11-02)

Measured on Nautilus, round 40 piece 3 (download job 4169647, compare job 4169650, sweep 4169656; the pull carries
the measurements and the sweep record and no job log). Modified revision `f32460a0` (created 2026-07-29 00:13Z,
one upload two minutes later titled "Abliterated Gemma-4-26B-A4B via EGA (Solutus): ~7% refusal, near-lossless
MMLU"), original pinned at `4d7ae498` of 07-20, the first measurement against this revision. The card names the
Solutus toolkit's expert-granular abliteration, "norm-preserving biprojection for MoE": a per-layer, winsorised,
harmless-orthogonalised refusal direction edited into "every residual-writing matrix", the attention output, the
dense down projection and every expert's down projection, by "a per-row, magnitude-restoring biprojection", with
`scale` 0.721, `expert_scale` 0.790 and `layer_fraction` 0.547 ("16 of 30 layers, all 128 experts"), a KL
divergence of 0.021 on benign prompts and MMLU 91.0 to 88.0 on 100 questions. It is the second EGA export in the
census after xdavxd's on the QAT checkpoint (round 34).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 17 flags (16 first shares on the
expert stacks at 0.978 to 0.989, one within-layer cosine at 0.948), on the cluster and after re-scoring at home.
On reading, the copy is its card: one direction per layer on the output side of all three writers of sixteen
layers, the rows restored.

- 48 of 1,013 tensors changed: the attention output, the dense down projection and the stacked expert down
  projections of layers 10 to 15 and 19 to 28, sixteen layers. Nothing else moved; the largest relative change
  outside the changed set is exactly 0 on all 965 other tensors.
- Rank one on every matrix: first shares 0.991 to 0.994 on the attention outputs and dense down projections,
  0.978 to 0.989 on the expert stacks (128 slices under one direction). One direction per layer: the three
  writers of a layer stand at 0.948 to 0.9996 to each other.
- Output side on all 48: one minus the left kept fraction is 0.48 to 0.98 on the attention outputs, 0.43 to 0.96
  on the dense down projections and 0.75 to 0.99 on the experts (the card's `scale` 0.721 and `expert_scale`
  0.790 are not these fractions, which vary by layer); the right side keeps
  0.47 to 0.87. Rows moved 0.0001 to 0.0003 on the attention outputs, 0.0003 to 0.0010 on the dense down
  projections and 0.0006 to 0.0012 on the experts, the card's norm preservation read in the rows, under finding
  22's band. Relative changes 0.0177 to 0.0283.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Dense down projection: change, E1, left kept, right kept | Weight | Expert down projections: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | 0.0283, 0.994, 0.25, 0.51 | 0.75 | 0.0200, 0.992, 0.04, 0.87 | 0.96 | 0.0224, 0.979, 0.02, 0.86 | 0.98 | 0.0002, 0.0006, 0.0008 |
| 12 | 0.0246, 0.992, 0.25, 0.48 | 0.75 | 0.0186, 0.991, 0.05, 0.82 | 0.95 | 0.0209, 0.978, 0.07, 0.86 | 0.93 | 0.0002, 0.0004, 0.0007 |
| 14 | 0.0216, 0.992, 0.09, 0.57 | 0.91 | 0.0199, 0.992, 0.09, 0.80 | 0.91 | 0.0223, 0.981, 0.05, 0.86 | 0.95 | 0.0003, 0.0007, 0.0007 |
| 19 | 0.0213, 0.993, 0.52, 0.55 | 0.48 | 0.0201, 0.992, 0.11, 0.79 | 0.89 | 0.0195, 0.980, 0.12, 0.86 | 0.88 | 0.0002, 0.0007, 0.0006 |
| 21 | 0.0213, 0.993, 0.06, 0.55 | 0.94 | 0.0190, 0.991, 0.07, 0.79 | 0.93 | 0.0193, 0.983, 0.03, 0.84 | 0.97 | 0.0002, 0.0005, 0.0011 |
| 24 | 0.0214, 0.994, 0.09, 0.47 | 0.91 | 0.0186, 0.992, 0.09, 0.75 | 0.91 | 0.0194, 0.987, 0.17, 0.83 | 0.83 | 0.0002, 0.0006, 0.0012 |
| 26 | 0.0218, 0.994, 0.02, 0.47 | 0.98 | 0.0236, 0.993, 0.57, 0.81 | 0.43 | 0.0203, 0.983, 0.01, 0.83 | 0.99 | 0.0002, 0.0004, 0.0008 |
| 28 | 0.0195, 0.993, 0.03, 0.49 | 0.97 | 0.0256, 0.994, 0.20, 0.75 | 0.80 | 0.0187, 0.989, 0.06, 0.83 | 0.94 | 0.0002, 0.0003, 0.0006 |

The full table (16 rows) is in the report.

Directions. Against twenty-four saved vectors of measurements of the 26B-A4B, the directions stand at 0.931 and
0.921 to TrevorJS's edit and its four re-uploads and DuoNeural's copy of it on all 48 shared names (left minimum
0.910), at 0.92 to SevenOfNine's (26), tvall43's (10), sh0ck0r's and BinxNet's kernel exports, at 0.907 to
xdavxd's EGA on the QAT checkpoint on all 48, at 0.75 on the left to WWTCyberLab's, 0.45 to Mitchins's, and at
0.19 or less to the arbitrary-rank edits and huihui-ai's: an independent run inside the 26B-A4B's one-direction
family of findings 24 and 74, not a copy of any. By byte range the layer 20 attention output is 0.0194 from
Google's and 0.0117 from TrevorJS's. The second shard (`5c0b909c`) is byte-equal to SassyDiffusion's and
WWTCyberLab's second shards, the library's layout placing no edited tensor in it (finding 71); the first
(`7841d2ad`) matches no measured file.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home, the home judgement moving nothing: the version
strings changed (5.5.0.dev0 to 5.14.1) and the tokenizer, the token ids, the generation settings and the template
are the pin's.

## For the recipe library

The per-layer entry with selection reads the copy on 47 of 48 matrices; an expert-aware first-share floor at
0.97 would read the stacks. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus40/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
