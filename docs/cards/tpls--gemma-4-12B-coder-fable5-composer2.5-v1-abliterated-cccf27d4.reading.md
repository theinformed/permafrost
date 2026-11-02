# Reading of the Stage 1 and Stage 2 result: tpls/gemma-4-12B-coder-fable5-composer2.5-v1-abliterated against yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 (2026-11-02)

Measured on Wheat, round 45 piece 1 (download job 387355, compare job 387356, sweep 387364; the pull carries the
measurements and the sweep record and no job log). Modified revision `6e57830b` (created 2026-06-23 04:30Z, the
weights uploaded at 04:30:58Z in one commit titled "abliterated bf16 (yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1,
KL_MAX=0.2)" and unchanged through the thirty-five later commits, which add and withdraw GGUF files and rewrite
the card), parent pinned at `237e5d8e` of 2026-06-18, yuxinlu1's coding fine-tune of google/gemma-4-12B-it saved in
float16, the parent pair 2 shares. The card marks the repository deprecated in favour of the maker's later SFT v5
edit and names one step, "refusal-direction ablation", with no layer, weight or tool; the commit title's `KL_MAX`
is the one setting printed anywhere. The copy is five bfloat16 shards (`5aa9f6f6` to `cd09b767`) where the parent
is one float16 file; no weight file is shared with pair 2 at any revision of either repository (the template, the
processor file and `tokenizer.json` are the parent's on both), and the copy's history has one weight upload.

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 355 flags (232 unexpected changes, 66
first shares, 56 direction cosines, 1 cross-kind cosine), on the cluster and after re-scoring at home. On reading,
the copy is one shared direction on the down projections of layers 9 to 47 and the attention outputs of 24 to 43,
inside a bfloat16 recast of the float16 parent that moves every linear map.

- 322 of 677 tensors changed. 263 of them are the recast alone: the query, key, value, gate and up projections of
  every layer, 27 attention outputs and four down projections at relative changes of 0.0011 to 0.0016, the
  rounding of float16 values into bfloat16 (by byte range the layer 5 query projection is the parent's float16
  matrix rounded to the nearest bfloat16 value on every entry). Six more matrices sit just under the threshold
  (0.00087 to 0.00097, down projections of layers 2 to 5 and 8 and the attention output of 17), so the largest
  relative change outside the changed set is 0.00097. The other 349 tensors, the embeddings and every
  normalisation vector among them, read exactly 0, their float16 values being exact in bfloat16.
- The edit is the other 59: the down projections of layers 9 to 47 (39) and the attention outputs of 24 to 43
  (20), at relative changes of 0.013 to 0.028 and 0.0028 to 0.033.
- One direction on the left side of all 59: 0.981 to their common direction at the median (minimum 0.763), the
  down projections at 0.987 and the attention outputs at 0.978, the two writers of a layer at 0.978 to each other;
  the right sides unrelated (median 0.005 between adjacent layers).
- First shares 0.978 to 0.995 on the down projections and 0.56 to 0.995 on the attention outputs, the lowest at
  the window's ends (0.594 at layer 24, 0.559 at 43).
- No weight to read: the kept fractions scatter on both sides (left -0.16 to 0.98, right -0.02 to 0.98), the
  left below the right on 24 of 59, the shape finding 18 read on richardyoung's edit of this parent.
- Rows moved 0.0009 to 0.0165, through and over finding 22's band.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept |
| --- | --- | --- |
| 9 | - | 0.0130, 0.985, 0.94, 0.92 |
| 15 | - | 0.0190, 0.990, 0.79, 0.34 |
| 20 | - | 0.0246, 0.991, 0.88, 0.11 |
| 24 | 0.0028, 0.594, 0.98, 0.95 | 0.0246, 0.991, 0.73, 0.26 |
| 28 | 0.0140, 0.980, 0.62, 0.69 | 0.0284, 0.993, -0.16, 0.15 |
| 32 | 0.0329, 0.995, 0.87, 0.13 | 0.0276, 0.993, 0.59, 0.05 |
| 36 | 0.0216, 0.989, 0.81, 0.60 | 0.0217, 0.990, -0.01, 0.23 |
| 40 | 0.0105, 0.965, 0.76, 0.76 | 0.0195, 0.990, 0.07, 0.22 |
| 43 | 0.0028, 0.559, 0.91, 0.98 | 0.0184, 0.986, 0.27, 0.35 |
| 47 | - | 0.0150, 0.984, 0.09, 0.43 |

Directions. Restricted to the 59 edited matrices, the direction stands at 0.957 on the left and 0.936 on the right
(minimum 0.940) to richardyoung's Heretic edit of the same parent on all 39 shared names (round 16's measurement
against the parent), at 0.921 to BinxNet's Heretic pass of Google's 12B, 0.87 to 3MPER0RR's, prithivMLmods's and
MoonRide's, 0.863 to lemuralabs's ablation over this fine-tune, 0.70 to enkato64bit's, 0.54 to jwest33's null-space
projection, 0.49 and 0.40 to huihui-ai's projection of this parent (pair 2, 11 names) and to its Google and agentic
twins, 0.24 to TrevorJS's, 0.20 to OpenYourMind's through Paul691's duplicate and 0.09 to coder3101's. By byte range
at layer 25 the leading direction of the copy's change from the parent stands at 0.958 on the attention output and
0.963 on the down projection to richardyoung's and at 0.488 and 0.487 to pair 2's, and at layer 30 at 0.952 to
richardyoung's; the copy stands 0.0049, 0.0253 and 0.0176 from the parent on the layer 25 attention output, the
layer 25 down projection and the layer 30 attention output, 0.0183, 0.0133 and 0.0108 from richardyoung's copy and
0.0217, 0.0329 and 0.0176 from pair 2's. The two edits of one checkpoint are two methods: this one a Heretic-family
direction with the row-normalised kept fractions of finding 18, pair 2 the maker's Google direction carried over
at weight 1.00.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home: the four `dtype` fields (`float16` to `bfloat16` in the
configuration and its audio, text and vision sub-configurations), the recast the commit title names; the version
strings (5.10.2 to 5.12.1) are explained by re-save. The token ids are the instruct checkpoint's through the parent
on both sides (`eos_token_id` `[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0), the
vocabulary is 262,144, and the 17,466-byte template is the parent's and renders the fixed conversation identically.

## For the recipe library

A single-direction entry with a recast line would read the copy: the scorer's 232 unexpected changes are the
precision change, which a line comparing each untouched matrix with the parent rounded to the copy's type would
close, and the first shares and direction cosines are the edit's ends and the right sides. The direction vectors
stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat45/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
