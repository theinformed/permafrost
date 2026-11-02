# Reading of the Stage 1 and Stage 2 result: huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated against yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 (2026-11-02)

Measured on Wheat, round 45 piece 2 (download job 387355, compare job 387357, sweep 387364; the pull carries the
measurements and the sweep record and no job log). Modified revision `cbee1466` (created 2026-06-21 01:11Z, one
upload of nine files at 01:34Z), parent pinned at `237e5d8e` of 2026-06-18, yuxinlu1's coding fine-tune of
google/gemma-4-12B-it, saved in float16, the parent of richardyoung's Heretic edit (finding 18), of
lemuralabs's copy (finding 25) and of OpenYourMind's projection (finding 101), and of pair 1 of this round. The
card is huihui-ai's usual one: "created with abliteration", Sumandora's remove-refusals-with-transformers named as
the method, no layer, no weight, no count. The copy is one `model.safetensors` (`b9780d88`, 23,919,548,728 bytes)
where the parent has one of 23,919,548,736 (`da00c3ea`); its configuration, generation file, template, processor
file and token files carry the parent's object ids.

## Weights (Stage 2)

The tool's assessment was a clean match to `directional-per-layer-selected`, 0 flags, on the cluster and after
re-scoring at home. On reading, the copy is a projection of one direction out of both residual writers of layers 23
to 28, at a weight of 1.00, with the direction the maker found on Google's checkpoint.

- 12 of 677 tensors changed: the attention outputs and down projections of layers 23 to 28. The other 665 read
  exactly 0, the largest relative change outside the changed set is exactly 0, and the twelve edited matrices are
  saved in bfloat16 inside a float16 file.
- One direction on layers 24 to 27 (agreement 0.99999 between layers and within each layer), with layers 23 and 28
  apart from it at 0.47 and 0.74 and each sharing one direction between its two writers (0.99999).
- Output side on all 12 at weight 1.00 (left kept fraction -0.003 to 0.005), first shares 0.993 to 0.997.
- Relative changes 0.0182 to 0.0310; rows moved 0.016 to 0.079, over finding 22's band on every matrix, with no
  restoration step.

| Layer | Attention output: change, E1, left kept, right kept, rows | Down projection: change, E1, left kept, right kept, rows |
| --- | --- | --- |
| 23 | 0.0183, 0.994, 0.005, 0.89, 0.0268 | 0.0187, 0.993, 0.003, 0.63, 0.0162 |
| 24 | 0.0231, 0.995, -0.003, 0.84, 0.0777 | 0.0258, 0.996, -0.003, 0.84, 0.0774 |
| 25 | 0.0220, 0.995, -0.003, 0.82, 0.0775 | 0.0264, 0.996, -0.003, 0.82, 0.0787 |
| 26 | 0.0310, 0.997, -0.003, 0.85, 0.0783 | 0.0249, 0.996, -0.003, 0.76, 0.0599 |
| 27 | 0.0184, 0.993, -0.003, 0.80, 0.0508 | 0.0209, 0.994, -0.003, 0.73, 0.0520 |
| 28 | 0.0183, 0.993, 0.002, 0.83, 0.0394 | 0.0182, 0.993, 0.003, 0.63, 0.0336 |

Directions. Against the saved vectors of the forty measurements of the 12B and its QAT checkpoint, the
direction stands at 1.000 on the left and on the right to huihui-ai's own projection of google/gemma-4-12B-it
(round 13) on all 12 names, minimum 1.000, and so to its two hub duplicates (TimelessSoul's and
Ishowbackup's); at 0.978 and 0.982 to the maker's edit of the agentic fine-tune (pair 8); at 0.70 and 0.81 to the
maker's QAT projection; at 0.66 to AEON-7's; at 0.62 to smashingtags's and Paul691's; at 0.49 and 0.40 to tpls's
edit of the same parent (pair 1, 11 names); at 0.50 and 0.43 to richardyoung's Heretic edit of the same parent;
at 0.53 to TrevorJS's; at 0.43 to lemuralabs's; at 0.21 or less to igorls's first pass, Vampelium's, llmfan46's
two, coder3101's two, wnfldchen's, RumiaChannel's three and OS-Software's three; and at 0.01 to AlekseyCalvin's
training. By byte range at layer 25 the
leading direction of the copy's change from its parent stands at 0.99998 to the leading direction of huihui-ai's
Google edit's change from Google's, on the attention output and on the down projection, and the parent projected
along the Google edit's direction reproduces the copy to within 0.0016 of the matrix (0.06 to 0.07 of the change,
the bfloat16 rounding of the save); the copy's matrices stand 0.0058 and 0.0067 from the Google edit's, the
distance between the two parents (the fine-tune stands 0.0055 and 0.0063 from Google's at that layer). The layer 30
attention output and the layer 5 query projection are byte-equal to the parent's, and the parent's are 0.0064 and
0.0031 from Google's.

## Token and configuration side (Stage 1)

"Consistent" on the cluster and at home: no compared field differs. The token ids are the instruct checkpoint's
through the parent (`eos_token_id` `[1, 106]` in the configuration, `[1, 106, 50]` in the generation file,
`bos_token_id` 2, `pad_token_id` 0), the vocabulary is 262,144 on both sides, and the 17,466-byte template (Google's
05-18 revision, `e61bbfe9`) renders the fixed conversation identically.

## For the recipe library

The per-layer selected entry reads the copy cleanly; a reused-direction line would say that the edit's direction is
the one the maker found on the base checkpoint and applied to the fine-tune unchanged. The direction vectors stay in
the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat45/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
