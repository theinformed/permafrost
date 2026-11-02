# Reading of the Stage 1 and Stage 2 result: Paul691/gemma-4-12B-it-abliterated-uncensored against google/gemma-4-12B-it (2026-11-02)

Measured on Wheat, round 39 piece 6 (download job 387181, compare job 387187, sweep 387190; the pull carries the
measurements and the sweep record and no job log). Modified revision `ad7d2c90`, the repository's one commit
(2026-07-23 21:30Z, "Duplicate from OpenYourMind/gemma-4-12B-it-abliterated-uncensored"), original pinned at
`707f0a3b`. The batch note names the duplicate and the pinner recorded the parent, which is live with 1,469
downloads and unmeasured; the weight file (`6503b6fa`), the card (5,833 bytes) and every token file are byte-equal
to the parent's, so the copy is measured as the parent (findings 38 and 97). The parent was created at 19:57Z on
2026-06-03, the copy of finding 7 whose original's surviving history begins later the same day. Its first card
(revision `a67212c0`, 20:00Z) said the edit was made with "abliterix", diff-in-means directions per layer "baked into
the weights as a per-matrix delta on the residual-write modules", followed by "Healing: a short supervised pass";
four minutes later (revision `bfa03793`, "remove abliterix attribution and healing claim") the card named "our own
custom abliteration framework" and no healing, and the later commits add banners and a support section. The card
names google/gemma-4-12B-it as the one parent.

## Weights (Stage 2)

The tool's assessment was violations against `single-projection`, 649 flags (457 unexpected changes, 96 direction
cosines, 95 first shares, 1 cross-kind), on the cluster and after re-scoring at home. On reading, the copy is a
single-direction projection at a weight of 0.40 on both writers of every layer, laid over the coder fine-tune that
finding 25 placed under lemuralabs's copy of the same base.

- 553 of 677 tensors changed. Both writers of all 48 layers moved 0.0068 to 0.0327 with first shares 0.75 to 0.99
  and a left kept fraction of 0.590 to 0.606 on every one of the 96: one direction per matrix projected from the
  output side at a weight of 0.40, the right side keeping 0.72 to 0.99. The two writers of a layer carry different
  directions (0.19 to 0.59, median 0.25) and the layers differ from each other (median 0.35 to the mean).
- The 228 readers (query, key, value, gate and up projections) moved 0.0018 to 0.0036 with first shares 0.001 to
  0.02 and both kept fractions within 0.002 of 1: training, not a projection. The query and key norms moved up to
  0.0864 (layer 13), the other normalisation vectors 0.0010 to 0.0070; 67 tensors stay under the threshold (to
  0.000989) and 57 are exactly 0, the audio and vision embedders among them.
- Equal to lemuralabs/Gemma-4-12B-uncensored-bf16 off the writers. The relative difference of every one of the 228
  readers equals lemuralabs's report to the last digit (the ratio is 1.000 on all 228), the layer 13 query norm
  reads 0.08642 in both, and the saved leading directions stand at 1.000 on both sides to lemuralabs's on all 228
  readers. By byte range from the hub the layer 20 query projection, the layer 20 gate projection and the layer 13
  query norm are byte-equal between the two copies and between this copy and its parent. On the writers the two
  copies part: the layer 5 attention output stands 0.00303 from Google's in lemuralabs's copy (its ablation starts
  at layer 9, so the fine-tune alone) and 0.00723 in this one, 0.00657 apart; the layer 20 attention output 0.0283
  and 0.0327 from Google's and 0.0424 from each other; the layer 20 down projection 0.0024 and 0.0191 from Google's
  and 0.0190 apart. Two projections on one fine-tune, neither made from the other, as finding 25 read lemuralabs's
  against richardyoung's.
- Rows moved 0.0015 to 0.175 on the writers (0.17 on the layer 20 attention output, the largest edit), unrestored
  under no claim.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Query projection: change, E1 |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.0076, 0.843, 0.59, 0.99 | 0.41 | 0.0078, 0.851, 0.60, 0.99 | 0.40 | 0.0018, 0.003 |
| 5 | 0.0072, 0.798, 0.60, 0.92 | 0.40 | 0.0074, 0.840, 0.60, 0.83 | 0.40 | 0.0025, 0.003 |
| 10 | 0.0069, 0.796, 0.60, 0.91 | 0.40 | 0.0068, 0.811, 0.59, 0.99 | 0.41 | 0.0030, 0.011 |
| 13 | 0.0080, 0.881, 0.60, 0.99 | 0.40 | 0.0087, 0.892, 0.60, 0.96 | 0.40 | 0.0028, 0.001 |
| 20 | 0.0327, 0.990, 0.60, 0.90 | 0.40 | 0.0191, 0.981, 0.60, 0.90 | 0.40 | 0.0028, 0.003 |
| 27 | 0.0074, 0.808, 0.60, 0.92 | 0.40 | 0.0082, 0.852, 0.60, 0.88 | 0.40 | 0.0025, 0.003 |
| 30 | 0.0075, 0.840, 0.60, 0.86 | 0.40 | 0.0077, 0.833, 0.60, 0.79 | 0.40 | 0.0027, 0.002 |
| 40 | 0.0073, 0.824, 0.60, 0.91 | 0.40 | 0.0074, 0.803, 0.60, 0.73 | 0.40 | 0.0029, 0.003 |
| 47 | 0.0081, 0.833, 0.60, 0.89 | 0.40 | 0.0074, 0.808, 0.60, 0.72 | 0.40 | 0.0028, 0.001 |

The full table (553 rows) is in the report.

Directions. Against thirty-seven saved vectors of measurements of the 12B, the leading directions stand at 1.000 to
lemuralabs's on the 228 readers and at 0.00 to 0.85 (median 0.11 on the attention outputs, 0.13 on the down
projections) on the 96 writers, so the shared part is the fine-tune and the projection is the maker's own; against
the other 12B edits the writers stand at 0.70 to igorls's QAT edit, 0.69 to smashingtags's, 0.67 to TrevorJS's and
its three re-uploads, and lower to the rest, the scatter of a direction found on a different model.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home: `text_config.max_position_embeddings` 131,072 where the pin
says 262,144, and a 17,466-byte template where the pin's is 18,683. Both are Google's own values on the day the
parent was made: the original's revisions `657684fe` and `66bc78a7` of 06-03 declare 131,072 (raised to 262,144 by
`5926caa4` on 06-04, "Update max_position_embeddings to full context length") and carry the 17,466-byte template
byte for byte, which Google replaced at `711c1368` on 07-15. The copy stands on Google's 06-03 revision and was
pinned against the 07-20 one; the fields are the earlier-revision case the metadata tool does not yet read
(`docs/census-round-38.md`, owed). The configuration's version string (5.10.0.dev0) is that revision's. The end-of-
sequence ids `[1, 106]` and the generation configuration's `[1, 106, 50]` are the pin's.

## For the recipe library

A single-projection entry that allows a dense parent would read the projection (weight 0.40, both writers, all
layers) and name the fine-tune from the readers; the direction comparison against lemuralabs's vectors is the
check that named it here. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat39/measurements/pair-6/weights.directions.safetensors`; lemuralabs's are
under `nautilus16/measurements/pair-3/`.

Weight differences alone cannot certify the absence of hidden behavior.
