# Reading of the Stage 1 and Stage 2 result: JJaguar/gemma-4-12B-it-qat-q4_0-unquantized-heretic-nx against google/gemma-4-12B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Nautilus, round 36 piece 6 (download job 4167620, compare job 4167626, sweep 4167629; the pull carries
the measurements and the sweep record and no job log). Modified revision `66251327` (five commits on 2026-08-07
between 02:44Z and 02:52Z: the model, tokenizer, processor and README), original pinned at `b6ed8627` (07-20, the
revision current when the repository was created). The card (30,971 bytes) is Heretic v1's kernel page:
`direction_index` 29.14, an attention-output kernel of 1.33 at position 44.28 falling to 1.20 at distance 19.29,
a down-projection kernel of 1.43 at 33.36 falling to 1.35 at distance 13.11, KL divergence 0.1217, 9 refusals in
135 against 112 (a prompt set of 135 where the tool's page usually reports 100). The `base_model` field names
google/gemma-4-12B-it; the README's first sentence names the QAT checkpoint, and the pinner paired by the name
(finding 48). The card does not say what `nx` in the name means. The maker's first copy in the census.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 2 flags (one first
share of 0.980 on the attention output of layer 44 and one cross-kind direction cosine of 0.846), on the cluster
and after re-scoring at home. On reading, the copy is the card's kernel pass exactly, one direction shared by
every edited matrix.

- 49 of 677 tensors changed: the down projections of layers 21 to 46 and the attention outputs of 25 to 47, the
  reach of the two kernels to the layer (the attention kernel's minimum lies at 44.28 less 19.29, so the first
  layer it reaches is 25, and the down kernel's at 33.36 plus or minus 13.11, so 21 to 46). Nothing else moved;
  the largest relative change outside the changed set is exactly 0 and 628 tensors equal the original, which
  places the copy on the QAT checkpoint (finding 48).
- Rank one: first shares 0.992 to 0.997 (0.980 on one matrix), and one direction for the whole edit: the group
  cosines are 0.96 to 1.00 (median 0.993 on the down projections, 0.986 on the attention outputs), the two
  writers of a layer agree at 0.90 to 0.998 (median 0.988) and the kinds at 0.85.
- No readable weight: the kept fractions scatter (left -0.24 to 0.89, right -0.05 to 0.86; the left below the
  right on 18 of 49), where the card's kernels run 1.20 to 1.43. Read as one minus the right fraction the down
  projections give 0.72 to 1.05 and the attention outputs 0.14 to 0.81, finding 46's scatter on a Gemma 4 12B,
  now on the QAT checkpoint.
- Rows moved 0.0026 to 0.0112 under no claim.

| Layer | Writer | Change | E1 | Left kept | Right kept | Group cosine | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 21 | down | 0.0296 | 0.996 | 0.79 | 0.01 | 0.96 | 0.0028 |
| 25 | down | 0.0283 | 0.996 | 0.66 | 0.17 | 0.98 | 0.0053 |
| 25 | attention | 0.0212 | 0.995 | 0.63 | 0.55 | 1.00 | 0.0059 |
| 33 | down | 0.0261 | 0.996 | 0.58 | -0.01 | 0.99 | 0.0038 |
| 33 | attention | 0.0275 | 0.996 | 0.86 | 0.38 | 0.98 | 0.0046 |
| 44 | down | 0.0229 | 0.995 | 0.10 | 0.04 | 1.00 | 0.0031 |
| 44 | attention | 0.0332 | 0.980 | 0.85 | 0.61 | 0.96 | 0.0112 |
| 47 | attention | 0.0296 | 0.997 | 0.88 | 0.33 | 0.97 | 0.0046 |

The full table (49 rows) is in the report.

Directions. Against the saved vectors of thirty-five 12B measurements on the shared names, the leading
directions stand at 0.92 and 0.89 to BinxNet's kernel export of the instruct 12B (34 shared matrices), at 0.90
and 0.89 to lemuralabs's (49), 3MPER0RR's (42), prithivMLmods's (45) and MoonRide's (43), the five Heretic kernel
passes of the instruct 12B that finding 46 read as one shared direction; at 0.72 to richardyoung's edit of a
coder fine-tune, 0.54 to enkato64bit's, 0.50 to jwest33's; at 0.25 and 0.26 to igorls's thinking-on kernel
search of the same checkpoint (finding 69) and 0.35 to huihui-ai's projection of it; and at 0.18 or less to every
arbitrary-rank edit. The kernel family's direction holds on the QAT checkpoint at 0.90, and the search with
thinking on found another (finding 91). The first two shards (`513abfa9`, `ebfb917e`) are byte-equal to
OS-Software's `-v3` export's (piece 5), the layout below both windows.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.10.0.dev0 to 5.14.1) and
nothing else; the template is the pin's and renders identically.

## For the recipe library

The single-projection entry reads the copy with two flags, one first share at 0.980 and the cross-kind cosine
at 0.85 against the rule's 0.95; a kernel entry that takes the card's two kernels and checks the reach would
read it as a clean match. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus36/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
