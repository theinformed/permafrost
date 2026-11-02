# Reading of the Stage 1 and Stage 2 result: DuoNeural/gemma-4-26B-A4B-it-abliterated against google/gemma-4-26B-A4B-it (2026-11-02)

Measured on Nautilus, round 38 piece 5 (download job 4168771, compare job 4168776, sweep 4168780; the pull carries
the measurements and the sweep record and no job log). Modified revision `dbe44bd9` (five commits from 2026-04-11,
the weights at 10:57Z "Add files using upload-large-folder tool", the card the next day, the rest links), original
pinned at `7d4c97e5`. The card (3,699 bytes) says the copy was made with "Expert-Granular Abliteration (EGA)", which
it defines against dense abliteration: "EGA computes a per-expert refusal direction across all 128 experts
independently and orthogonalizes each via biprojection", with 3 refusals in 100 against 29 for a dense-only run;
it links the maker's own GGUF export, which the pinner noted beside the `base_model` field naming Google. It names
no tool, no parameter and no other maker. TrevorJS/gemma-4-26B-A4B-it-uncensored (revision `fc582b97`, 2026-04-03)
was measured in rounds 2 and 3 (findings 13 and 24).

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer`, 31 flags (the worst
expert's first share on 30 packed tensors, 0.881 in layer 0 and 0.951 to 0.990 elsewhere; the within-layer cosine
of layer 29 at 0.949), on the cluster and after re-scoring at home. On reading, the copy is TrevorJS's edit.

- 90 of 1,013 tensors changed: the attention outputs, the dense down projections and the packed expert down
  projections of all 30 layers, with 128 of 128 experts changed in each. The 30 gate-up tensors, the 30 routers
  and everything else are exactly 0; the largest relative change outside the changed set is exactly 0.
- One direction per layer across the three kinds (within-layer cosines 0.949 to 0.9997) and across the 128
  experts of a layer (the experts' left vectors agree at a median of 0.9957 to 0.9991, minimum 0.94 to 0.993):
  not a per-expert direction found independently, which would give 128 directions, but one direction applied to
  every expert, as finding 13 read on TrevorJS's copy. First shares 0.992 to 0.996 on the dense matrices; the
  median expert 0.99 in every layer, the worst 0.881 to 0.990.
- Output side with the biprojection's second term on all 90: along the leading output direction the attention
  outputs keep 0.02 to 0.28, the dense down projections 0.00 to 0.51 and the experts a median 0.009 to 0.519, with
  the right side keeping 0.45 to 0.68, 0.64 to 0.85 and 0.81 to 0.88, finding 24's "scale 1.0 with the second
  term". Rows moved 0.0001 to 0.0004 on the attention outputs, 0.0002 to 0.0011 on the dense down projections and
  0.0005 to 0.0012 per packed expert tensor, TrevorJS's figures (0.00014 to 0.00037 and 0.00023 to 0.00106 on his
  dense matrices) under a card that claims nothing about rows.

| Layer | Attention output: change, E1, left kept, right kept | Dense down: change, E1, left kept, right kept | Expert down: change, worst E1, median left kept, right kept | Within-layer cosine | Rows |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.0291, 0.994, 0.08, 0.68 | 0.0219, 0.993, 0.03, 0.75 | 0.0195, 0.881, 0.19, 0.88 | 0.995 | 0.0002, 0.0003, 0.0006 |
| 6 | 0.0285, 0.993, 0.24, 0.48 | 0.0197, 0.994, 0.05, 0.74 | 0.0201, 0.984, 0.04, 0.85 | 0.985 | 0.0003, 0.0004, 0.0007 |
| 12 | 0.0235, 0.993, 0.24, 0.49 | 0.0184, 0.991, 0.04, 0.82 | 0.0210, 0.981, 0.07, 0.85 | 0.970 | 0.0002, 0.0003, 0.0009 |
| 18 | 0.0197, 0.992, 0.20, 0.59 | 0.0189, 0.991, 0.16, 0.84 | 0.0192, 0.981, 0.14, 0.85 | 0.986 | 0.0001, 0.0006, 0.0007 |
| 24 | 0.0219, 0.994, 0.03, 0.45 | 0.0191, 0.992, 0.06, 0.78 | 0.0198, 0.987, 0.10, 0.83 | 0.994 | 0.0002, 0.0003, 0.0010 |
| 29 | 0.0192, 0.993, 0.08, 0.48 | 0.0288, 0.991, 0.25, 0.85 | 0.0206, 0.988, 0.52, 0.81 | 0.949 | 0.0001, 0.0006, 0.0010 |

The full table (90 rows, with the `experts` block per packed tensor) is in the report.

Directions. Against twenty-four saved vectors of 26B-A4B measurements, the leading directions stand at 1.000 to
TrevorJS's edit on all 90 shared names (left minimum 1.000, right minimum 0.978; 1.000 on both sides on the 60
dense names of his first pass) and, with it, to the four re-uploads of his file (claymorecrystal's, sitten1's,
erunda337's and, through the family check, the second pass); at 0.97 and 0.95 to xdavxd's independent run of the
same method on the QAT checkpoint (finding 74); at 0.965 to 0.981 to the 26B-A4B kernel edits (sh0ck0r's,
tvall43's, BinxNet's, SevenOfNine's), which share the mean-difference direction; at 0.73 and 0.25 to WWTCyberLab's;
and at 0.22 or less to the arbitrary-rank family. The per-tensor measures agree with TrevorJS's second-pass report
to four or five significant digits and are equal on none of the 90 (layer 12's attention output 0.0234676 against
0.0234689, the largest absolute difference equal on both, 0.05212). Read from the hub by byte range
(`tools/hub_range_read.py`), the layer 12 attention output and down projection and the layer 29 attention output
stand 0.02346, 0.01839 and 0.01919 from Google's in both copies and 0.00037, 0.00035 and 0.00063 from each other,
not byte-equal: the same directions applied to the same original with a different last few bits, two to three
percent of the edit. The two shards (`4415dd6b`, `e6dbf9c4`) differ from TrevorJS's (`4b988df4`, `3d2388e8`) and
match no measured file. The copy was uploaded eight days after TrevorJS's.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the version strings (5.5.0.dev0 to 5.5.3) are the
re-save, the template the pin's 16,448-byte file, `tokenizer.json` (`a2619fe1`) the file the later Google
revisions carry.

## For the recipe library

A norm-preserving biprojection entry with the expert pass (finding 24's band, the median expert for the first
share) would read the copy as a clean match of TrevorJS's method; the direction check against the family is what
reads it as TrevorJS's run, and it belongs at the pin. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus38/measurements/pair-5/weights.directions.safetensors`, against
`nautilus3/measurements/pair-4/` for TrevorJS's.

Weight differences alone cannot certify the absence of hidden behavior.
