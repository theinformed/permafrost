# Census round 2: five Gemma and Mistral pairs (2026-10-29)

Five published copies compared with their stated originals on Nautilus, 2026-10-15 (run card 2442, jobs 3763593 to
3763597, all exit 0, 459 GB downloaded and deleted after each comparison). The measurements were pulled home and
re-scored on 2026-10-29 with the recipe table as committed today. Each pair has a card (the tool's Stage 1 text with
the Stage 2 line) and a reading note in `docs/cards/`; the full measurements are in `results/weights/` and
`results/meta/`.

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | wangzhang/gemma-4-31B-it-abliterated | google/gemma-4-31B-it | violations, 95 flags | consistent with the card: per-layer norm-preserving projection on Q, K, V and O |
| 2 | mlabonne/gemma-3-27b-it-abliterated | google/gemma-3-27b-it | match, 0 flags | consistent: one shared direction on every attention output and down projection, weight 1.5 |
| 3 | llmfan46/gemma-4-E4B-it-uncensored-heretic | google/gemma-4-E4B-it | violations, 23 flags | consistent with the card: arbitrary-rank edits on 11 attention outputs in the declared layer range |
| 4 | TrevorJS/gemma-4-26B-A4B-it-uncensored | google/gemma-4-26B-A4B-it | violations, 121 flags | consistent with the card: per-layer norm-preserving projection on o_proj, down_proj and all packed expert down projections |
| 5 | byroneverson/Mistral-Small-Instruct-2409-abliterated | mistralai/Mistral-Small-Instruct-2409 | violations, 75 flags | consistent with the linked notebook: per-layer directions at amount 2.0 on a listed set, plus the token embedding |

Nothing in the five pairs moved outside the matrices the maker's own description names. In four of the five the
largest relative change outside the changed set is exactly 0; in the fifth (pair 3) it is 0.00008, on attention
outputs the method weighted near zero.

## The token side

Pairs 4 and 5 are clean. Pair 2's twenty configuration fields are additions with the library's default values,
written by a newer transformers at save time; no field present in both files differs. The metadata tool now classes
an added field that loads as the library default as explained by re-save, so pair 2 reads "consistent with re-save
noted" (judged under transformers 4.56.2, the round's pins). Pairs 1 and 3 carry Google's own later chat template
(the 2026-04-28 "update SI and tool call handling" revision of each original), matched byte for byte against the
original repos' commit histories, plus one null configuration field the newer library writes, now explained the same
way. Every fixed conversation renders identically. The tool also reads the original repository's later commits: both
templates equal Google's 2026-04-28 fix byte for byte, so pairs 1 and 3 read "consistent with re-save noted" as well,
and every round 2 pair now closes on the token side without a hand reading.

## What the scorer learned

The flags on four pairs have four causes, none of them tampering, and each names a gap in the recipe table:

- Per-layer directions. Pairs 1, 4 and 5 compute a direction per layer, as their descriptions say. The table's
  projection entries ask for one shared direction. A per-layer form of the projection envelope is needed.
- Reading-side projections. Pair 1 projects the query, key and value matrices too. The table lists only residual
  writers as changeable kinds.
- Arbitrary rank. Pair 3's edits spread over many directions by design; the "arbitrary-rank" entry is still
  "not yet measured". Its signature, an energy profile that does not approach 1 by the eighth value, is distinct
  from the bfloat16 floor, which only lowers the first share on small edits.
- Packed experts. Pair 4's expert down projections are one three-dimensional tensor per layer. The shared table now
  names them; the measurement still computes no singular values for them.

Pair 5's 24 energy-share flags are the bfloat16 storage floor found in the calibration run, following the same law
across two decades of edit size. The row-norm rule, once the scorer reads the calibrated 0.001 line, separates
norm-preserving edits (pairs 1 and 4, under 0.0011) from plain projections (pair 2, 0.069) and from
over-projection (pair 5, up to 0.45).

Weight differences alone cannot certify the absence of hidden behavior.
