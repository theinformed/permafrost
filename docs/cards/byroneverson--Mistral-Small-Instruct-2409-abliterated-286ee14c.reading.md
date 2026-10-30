# Reading of the Stage 1 and Stage 2 result: byroneverson/Mistral-Small-Instruct-2409-abliterated against mistralai/Mistral-Small-Instruct-2409 (2026-10-29)

Measured on Nautilus, round 2 piece 5 (job 3763597, 20 minutes, exit 0). Modified revision `5e24aaef` (2024-09-23),
original pinned at `63e53df6` (2024-09-17). The card says only "abliterated" and links the notebook that made the copy.
The notebook is specific: one direction per layer from a PCA read of harmful and harmless activations, applied as
`W - amount * (W d) d^T` with amount 2.0 to a hand-picked list of attention outputs and feed-forward down projections,
and the token embedding patched with layer 25's feed-forward direction, also at amount 2.0.

## Weights (Stage 2)

The automatic verdict was "recipe violations", nearest recipe single-projection-selected, 75 flags, as scored on the
cluster; re-scored with the per-layer entries it is nearest `directional-per-layer-selected` with 48 flags, 24 of them
the energy shares below and 24 a new measurement. In every one of the 12 layers where both an attention output and a
down projection changed, the two edits use unrelated directions (cosine 0.001 to 0.09), so the notebook's direction
is per matrix, not per layer; the per-layer entry cannot describe it and a per-matrix entry would assert nothing
about direction. The same vectors confirm the embedding patch: the embedding's direction equals layer 24's
down-projection direction, the notebook's layer 25, at cosine 1.000. On reading, the changed set is the notebook's
list, and every flag has a measured cause.

- 50 of 507 tensors changed: the token embedding, 21 attention outputs and 28 feed-forward down projections. The
  notebook counts layers from 1. Every changed attention output is in its attention list and every changed down
  projection is in its feed-forward list, shifted by one. The list entries that did not register as changed are the
  early layers (attention 1 to 12 and 16, feed-forward 3 to 8 in the notebook's numbering), where the edit landed
  below the 0.001 threshold: those tensors differ from the original by 0.000004 to 0.0007 of their norm, so the
  edits were made and were tiny, as a weak early-layer direction would be. Nothing outside the notebook's list moved.
- The 24 energy-share flags are the bfloat16 storage floor. The edits here span relative change 0.0012 to 0.21, and
  the first-value share follows the calibration law 1 - E1 = (0.00153 / change)^2 along the whole run: 0.69 at
  0.0012, 0.90 at 0.0038, 0.984 at 0.012, 0.9989 at 0.05, 0.9999 at 0.2. The shortfall is rounding on small edits,
  not extra directions.
- The 49 direction flags measure the notebook's per-layer directions: the leading directions agree with their kind
  median only at cosine 0.11 to 0.32. The table's single-projection entries ask for one shared direction.
- Amount 2.0 is a reflection, not a removal, and it shows in the row norms: the largest relative change in a row norm
  is 0.45 (layer 53's down projection), with 0.1 to 0.25 on the other large late-layer edits. That is the signature
  of over-projection, and it is in the notebook as a deliberate choice ("2.0 seems like a good amount").
- The embedding edit (relative change 0.038, one direction, energy share 0.9982) is the notebook's token-embedding
  patch. The one "unexpected change" flag is the table not listing the embedding among the kinds a projection may
  touch; the same gap appeared on huihui-ai/Qwen2.5-32B-Instruct-abliterated and is a scorer follow-up.

## Token and configuration side (Stage 1)

The automatic verdict is "consistent": no metadata differences at all. The copy was patched shard by shard and the
small files were uploaded unchanged.

## For the recipe library

Consistent with the method the card links, read against the notebook rather than the card's single word. It is the
second census upload (after huihui-ai/Qwen2.5-32B-Instruct-abliterated) that edits the token embedding, and the
first measured at amount 2.0; both the reflection's row-norm signature and the per-layer directions are now in the
record for the recipe library.

Weight differences alone cannot certify the absence of hidden behavior.

## Second pass (2026-10-30)

Measured again on Nautilus, round 3 piece 5 (card 5055, download job 4080809, compare job 4080815, exit 0), on the
same pins (modified `5e24aaef`, original `63e53df6`) and the same shard checksums, with the comparison as of commit
d0f48bb. The second-pass report is
`results/weights/byroneverson-Mistral-Small-Instruct-2409-abliterated.pass-2.json`; its leading vectors are in the
pull copy at `/opt/ai/hpc-packages/pulls/model-audit/nautilus3/measurements/pair-5/weights.directions.safetensors`.

It reads as before: recipe violations, nearest `directional-per-layer-selected`, the same 48 flags (24 energy
shares, 24 within-layer directions), 50 changed tensors, 0.0007 outside them. Every measure both passes report is
equal to the last digit, the unrelated attention and feed-forward directions within a layer included (cosine 0.001
to 0.09 in all 12 layers).

The new measure reads the notebook's amount off each matrix, and it is not 2.0 on any of them. Along the leading
output direction the 49 attention outputs and down projections keep 0.95 of the original's action at the smallest
edit (layer 9's down projection, relative change 0.0012) and −10.1 at the largest (layer 50's down projection,
relative change 0.21); as weights, 0.05 to 11.1, rising with the size of the edit. The ratio of relative change to
weight is 0.0155 to 0.042 on all 49, which is each matrix's own share of its norm along the direction, so the thing
that varies between layers is the weight. A weight of 2.0 on a unit direction reads −1 on every matrix. The
direction's length was therefore not 1: the weight applied is 2 × |d|², with |d|² from 0.02 in the early layers to
5.6 at layer 50, and the early-layer entries that fell below the 0.001 threshold in the first pass are the layers
where |d| was smallest. Along the second to eighth directions every matrix keeps 0.9996 to 1.0005, so each edit is
still one direction, however heavy.

The embedding patch reads the same way and ties to its source. The embedding's residual coordinates are its
columns, and along its leading input direction it keeps −2.0854; layer 24's down projection keeps −2.0853 along its
leading output direction. Equal to four decimals, the two were patched with the same vector at the same weight,
3.09, which is the notebook's layer 25 at its amount of 2.0 times that layer's |d|² of 1.54. On 49 of the 50
matrices the left fraction is below the right one, the order of an edit on the output side; the embedding is the
one exception, as it should be.

On the token side the cluster's card reads "consistent" as before, no field differing. The report is
`results/meta/byroneverson-Mistral-Small-Instruct-2409-abliterated.pass-2.json`.
