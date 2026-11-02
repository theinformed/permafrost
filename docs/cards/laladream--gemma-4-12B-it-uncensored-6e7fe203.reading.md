# Reading of the Stage 1 and Stage 2 result: laladream/gemma-4-12B-it-uncensored against google/gemma-4-12B-it (2026-11-01)

Measured on Blueback, round 22 piece 5. The pull carries the measurements and the sweep record and no job log.
Modified revision `8e5d67bd` (one commit, 2026-08-21 at 08:10Z, "Duplicate from TrevorJS/gemma-4-12B-it-uncensored";
the README is TrevorJS's, 4,929 bytes), original pinned at `707f0a3b` (07-20). The card is the source's:
norm-preserving biprojected abliteration on the attention outputs and down projections of layers 15 to 47. The
repository's `base_model` field names Google.

## Weights (Stage 2)

The tool's assessment was "recipe violations", recipe `directional-per-layer-selected`, 1 flag, on the cluster and
after re-scoring at home: the attention output of layer 42 at a first share of 0.9899. The weight file is
TrevorJS's: the hub lists the same LFS checksum (`dd7fcab672`) on the 23,919,549,408-byte `model.safetensors` in
both repositories and in the Iambackup, Justbackup and Ishowbackup duplicates, and every measured field of all 677
tensors equals the round 8 report (`results/weights/TrevorJS-gemma-4-12B-it-uncensored.json`): 66 changed, the
attention output and the down projection of layers 15 to 47, one direction per layer (within-layer cosine 0.97 to
0.999, cross-layer median 0.49), the left kept fraction -0.012 to 0.68 and the right 0.25 to 0.85, the left below
the right on 65 of 66, first share 0.990 to 0.996, rows moved by at most 0.0004 (the restoration the card claims),
611 tensors equal to the original. The layer table and the reading are in
`TrevorJS--gemma-4-12B-it-uncensored-*.reading.md`; this is the fifth repository to carry that file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, one field. At home under transformers 5.22.1 the 12B
family's six fields (finding 39) close by tool with the version strings (5.10.0.dev0 to 5.12.0). The template is
the earlier-revision case through a re-upload: TrevorJS's files carry Google's 17,466-byte file of 06-03 under a
pin whose template is the 18,683-byte Canonical file of 07-20, chosen because the copy was created on 08-21. The
fixed conversation renders identically under both.

## For the recipe library

Nothing new on the weights: a byte-identical re-upload of TrevorJS's 12B copy, the fourth made with the hub's
duplicate function. The pinner's duplicate check (finding 38) would have paired it with its parent by the LFS
checksum before any download; the batch was pinned before the rule.

Weight differences alone cannot certify the absence of hidden behavior.
