# Census round 2: five Gemma and Mistral pairs (2026-10-29)

Five published copies compared with their stated originals on Nautilus, 2026-10-15 (run card 2442, jobs 3763593 to
3763597, all exit 0, 459 GB downloaded and deleted after each comparison). The measurements were pulled home and
re-scored on 2026-10-29 with the recipe table as committed today. Each pair has a card (the tool's Stage 1 text with
the Stage 2 line) and a reading note in `docs/cards/`; the full measurements are in `results/weights/` and
`results/meta/`.

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | wangzhang/gemma-4-31B-it-abliterated | google/gemma-4-31B-it | violations, 10 flags (95 before the per-layer entries) | consistent with the card: per-layer norm-preserving projection on Q, K, V and O |
| 2 | mlabonne/gemma-3-27b-it-abliterated | google/gemma-3-27b-it | match, 0 flags | consistent: one shared direction on every attention output and down projection, weight 1.5 |
| 3 | llmfan46/gemma-4-E4B-it-uncensored-heretic | google/gemma-4-E4B-it | violations, 11 flags (23 before) | consistent with the card: arbitrary-rank edits on 11 attention outputs in the declared layer range |
| 4 | TrevorJS/gemma-4-26B-A4B-it-uncensored | google/gemma-4-26B-A4B-it | violations, 64 flags (121 before) | consistent with the card: per-layer norm-preserving projection on o_proj, down_proj and all packed expert down projections |
| 5 | byroneverson/Mistral-Small-Instruct-2409-abliterated | mistralai/Mistral-Small-Instruct-2409 | violations, 48 flags (75 before) | consistent with the linked notebook: per-layer directions at amount 2.0 on a listed set, plus the token embedding |

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

- Per-layer directions. Pairs 1, 4 and 5 compute a direction per layer, as their descriptions say, and the table's
  projection entries ask for one shared direction. The table now has `directional-per-layer` and its selected form:
  the scorer compares the edits of one layer in the residual stream's coordinates (a writer's left vector, a
  reader's right vector) and asks for agreement within the layer only. Pair 1 agrees within every layer at cosine
  0.9996 or better while its layers agree with each other at 0.17; its 95 flags fall to 10, all rounding-floor
  energy shares on the smallest query and value edits. Pair 4 agrees within a layer at 0.94 to 0.99 (median
  0.977) against 0.10 between layers; 28 of its 30 layers clear the 0.95 line and two (layers 10 and 12) sit at
  0.941 and 0.947, four flags on their four matrices, the bend a second, input-side projection term puts on the
  leading direction. Pair 5 does not agree within a layer:
  in all 12 layers where both an attention output and a down projection changed, the two directions are unrelated
  (cosine 0.001 to 0.09). The notebook's directions are per matrix, not per layer, so those 24 flags are a
  measurement of the method, and a per-matrix entry would assert nothing about direction at all. The same
  rescoring confirms the notebook's embedding patch: the embedding's direction equals layer 24's down-projection
  direction (the notebook's layer 25) at cosine 1.000.
- Reading-side projections. Pair 1 projects the query, key and value matrices too. The table's reader kinds now
  carry a `residual_reader` mark, and the per-layer entries take the three attention readers as optional kinds, so
  the 54 "unexpected change" flags on pair 1 are gone. The shared-direction entries still list writers only.
- Arbitrary rank. Pair 3's edits spread over many directions by design; the "arbitrary-rank" entry is still
  "not yet measured". Its signature, an energy profile that does not approach 1 by the eighth value, is distinct
  from the bfloat16 floor, which only lowers the first share on small edits. Pair 3 changes one matrix per layer,
  so the per-layer entry says nothing about its directions and it now reads nearest to
  `directional-per-layer-selected` with its 11 energy-share flags; the label is the nearest line, not a match.
- Packed experts. Pair 4's expert down projections are one three-dimensional tensor per layer. The shared table now
  names them; the measurement still computes no singular values for them.

Pair 5's 24 energy-share flags are the bfloat16 storage floor found in the calibration run, following the same law
across two decades of edit size; its other 24 flags are the per-matrix directions above. The row-norm rule, once the scorer reads the calibrated 0.001 line, separates
norm-preserving edits (pairs 1 and 4, under 0.0011) from plain projections (pair 2, 0.069) and from
over-projection (pair 5, up to 0.45).

Weight differences alone cannot certify the absence of hidden behavior.
