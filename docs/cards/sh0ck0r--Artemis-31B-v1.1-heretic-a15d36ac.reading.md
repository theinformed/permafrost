# Reading of the Stage 1 and Stage 2 result: sh0ck0r/Artemis-31B-v1.1-heretic against google/gemma-4-31B-it (2026-11-01)

Measured on Nautilus, round 20 piece 2 (download job 4143641, compare job 4143643, 2,557 seconds, sweep 4143650).
Modified revision `b3bdce6a` (twelve commits between 03:41Z and 03:52Z on 2026-08-29: the weights, the tokenizer,
the processor, the README and a `reproduce/` folder with the tool's configuration, its trial record, its
requirements and the checksums of the parent), original pinned at `842da379` (07-28), the revision current when
the repository was created. The `base_model` field names Google; the README's first sentence names
TheDrummer/Artemis-31B-v1.1, a fine-tune of Google's 31B, as the model it was made from. The card prints the full
Heretic 1.4.0 record: quantization "none", row normalisation "full" with a rank-three correction, trial 187 of the
search, a KL divergence of 0.0109 against the parent, 23 refusals in 100 against the parent's count, and two
kernels, the attention outputs at weight 1.20 centred on layer 58.68 (minimum 0.28, width 34.46) and the down
projections at 1.48 centred on 35.77 (minimum 0.86, width 19.15).

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 686 flags, on the cluster and
after re-scoring at home: 482 unexpected changes, 121 first shares of 0.002 to 0.047, 82 direction cosines and one
cross-kind flag. The copy differs from the pinned original in every matrix and in no vector: 603 of 1,188 tensors
changed, which is all 602 two-dimensional tensors (every projection of the 60 layers, the embeddings, the whole
vision tower) and the one three-dimensional tensor; all 585 one-dimensional tensors (every norm) equal the
original. The relative change is 0.0875 to 0.1045 on every changed tensor, median 0.0939, with no dependence on
the layer or the kind. That is not an ablation's footprint. It is the parent's.

The parent was read from the hub by range (finding 45), without downloading it: the same four tensors fetched
whole from the three repositories' files (Google, TheDrummer, sh0ck0r) by byte-range requests against the hub, located from each
safetensors header, and decoded from bfloat16 (`tools/hub_range_read.py`).

- A vision projection in TheDrummer's file holds at most 16 distinct values in every block of 64 (median 14 over
  the first 4,000 blocks),
  14.58 percent of its entries are exactly zero, and its relative difference from Google's is 0.1029: the
  signature of weights that were quantised to 4-bit normal floats in blocks of 64 and written back to bfloat16.
  sh0ck0r's bytes for the same window equal TheDrummer's.
- A key projection of layer 30 (56 distinct values per block, difference 0.0975 from Google) and a query
  projection of layer 0 (45 distinct, 0.0929) read the same way, and sh0ck0r's bytes equal TheDrummer's on both.
  These are the matrices no Heretic kernel touches; the ablation leaves them as the parent wrote them.
- On the attention output of layer 45 (TheDrummer 50 distinct values per block, sh0ck0r 53) and the down
  projection of layer 30 (43 against 54), sh0ck0r's bytes differ from TheDrummer's by 0.0114 and 0.0185 relative:
  the ablation, on the matrices its kernels reach, a tenth the size of the parent's round trip.
- A layer norm is byte-equal in all three files.
- The spectrum of the difference from Google is flat (first singular value 0.118 of the norm, the five-hundredth
  0.040), which is what a full-rank perturbation of every entry gives.

TheDrummer's card states a 4-bit training recipe with adapters merged; the window read is consistent with weights
that were dequantised from 4-bit blocks of 64 and had a low-rank delta added. On that base the measure reads the
ablation where its weight is large enough to rise above a 9 percent floor:

- The leading direction of the difference on the down projections of layers 17 to 54 agrees with the group
  reference at 0.96 to 0.999, and on the attention outputs of layers 33 to 59 at 0.88 to 0.93; on the other
  layers of both writers it is the parent's noise (0.01 to 0.6). The card's down kernel is centred at 35.77 with
  width 19.15, so it reaches layers 17 to 54 exactly; the attention kernel is centred at 58.68 with width 34.46
  and reaches 25 to 59, with its weight below 0.5 before layer 40.
- The left kept fraction on the down projections of layers 40 to 54 is -0.18 to 0.13 against the kernel's
  one-minus-weight of -0.34 to 0.11, within 0.16 at layer 40 and 0.02 at 54; near the peak (layers 30 to 38) it
  reads -0.28 to 0.03 against -0.29 to -0.47, shallower than the kernel by up to 0.3. On the attention outputs of
  layers 51 to 59 it reads -0.12 to 0.03 against -0.19 to 0.005. The parent's noise adds to the kept fraction's
  numerator on every matrix, so the read is biased towards 1 everywhere, most where the ablation is weakest.
- The rows moved 0.004 to 0.10 on every changed matrix, the parent's round trip again; the row normalisation the
  card claims cannot be read against Google's file.
- The largest absolute differences are 0.012 to 0.051 on every matrix, with no layer standing out.

| Layer | Attention output: change, E1, left kept, kernel 1-w, group cosine | Down projection: change, E1, left kept, kernel 1-w, group cosine |
| --- | --- | --- |
| 10 | 0.0924, 0.019, 0.99, 0.72, 0.34 | 0.0937, 0.019, 1.00, 0.14, 0.01 |
| 17 | 0.0944, 0.038, 0.98, 0.72, 0.03 | 0.0948, 0.016, 0.28, 0.13, 0.99 |
| 25 | 0.0927, 0.004, 1.00, 0.70, 0.46 | 0.0959, 0.027, 0.27, -0.13, 0.99 |
| 30 | 0.0931, 0.007, 0.99, 0.57, 0.60 | 0.0965, 0.037, 0.24, -0.29, 0.97 |
| 36 | 0.0933, 0.009, 0.57, 0.41, 0.92 | 0.0965, 0.048, -0.19, -0.47, 0.99 |
| 40 | 0.0935, 0.012, 0.58, 0.30, 0.92 | 0.0969, 0.040, -0.18, -0.34, 0.99 |
| 45 | 0.0934, 0.015, 0.89, 0.17, 0.88 | 0.0949, 0.030, -0.17, -0.18, 1.00 |
| 50 | 0.0944, 0.022, 1.00, 0.03, 0.20 | 0.0942, 0.022, -0.01, -0.02, 1.00 |
| 54 | 0.0939, 0.024, -0.00, -0.08, 0.91 | 0.0939, 0.017, 0.13, 0.11, 1.00 |
| 57 | 0.0940, 0.028, -0.12, -0.16, 0.91 | 0.0934, 0.008, 1.00, 0.14, 0.02 |
| 59 | 0.0957, 0.027, -0.08, -0.19, 0.90 | 0.0947, 0.002, 1.00, 0.14, 0.02 |

The kernel column is one minus the card's weight at that layer; the group cosine is the leading direction's
agreement with the writer's reference direction, which is the Heretic direction where it is above 0.85 and the
parent's noise where it is not.

The fingerprint shares nothing with the ten earlier reports on the 31B original or with ressl's copy of this
round, and it cannot: every one of its 603 changed tensors carries the parent's quantisation.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, one field. `text_config.per_layer_config` is the 5.16 save
form (finding 39): `global_head_dim` and `num_global_key_value_heads` leave the text configuration and return as a
map under the ten global layers' indices, as on 3MPER0RR's 31B copy in round 19; the fourth copy on this form,
closed by hand. `text_config.moe_intermediate_size` (null in the 5.16 save, absent in Google's file) closed by the
default rule at home, where the cluster had counted it. The template is Google's pinned file and the fixed
conversation renders identically.

## For the recipe library

A copy measured against its grandparent. The pinner follows the `base_model` field, which names Google; the README
names TheDrummer, and the hub's own metadata of TheDrummer's repository names Google. Measured against the parent
the README names, this copy would read as the clean Heretic 1.4.0 edit its card describes, on the 120 matrices of
its two kernels, and nothing else; measured against Google it reads the parent's 4-bit round trip on 603 matrices
with the edit visible through it on about 65. TheDrummer/Artemis-31B-v1.1 is unmeasured and belongs in the next
batch; the pinner needs a parent rule that reads the README's first sentence before the `base_model` field. The
pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus20/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
