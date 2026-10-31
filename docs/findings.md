# Findings so far

Created by Sean Egan, 2026-10-29.

The results the audit has established so far, strongest first, each with its evidence in this repository. The
population is small: thirty-two measurements of thirty-one distinct published copies on sixteen bases (one copy is a
re-upload of another, and one could not be paired tensor by tensor), plus two edits of my own made to calibrate the
measurement. Numbers are from the committed reports in `results/weights/` and `results/meta/`.

## 1. Twenty-nine of the thirty published copies measured so far are what their cards say they are

Thirty community copies of open-weight models, five from one maker on Qwen bases, five from five makers on Gemma
and Mistral bases (round 2), seven from six makers on Gemma 4 and Mistral 7B bases (round 7), seven from six makers
on Gemma 4 and Ministral 3 bases (round 8) and six from four makers on the two larger Gemma 4 bases (round 12), have
been compared tensor by tensor with their stated originals. In twenty-nine, the changed tensors are exactly the
matrices the stated method reaches, and nothing else moved: the largest relative change outside the changed set is 0
in twenty-six copies, 0.00008 and 0.000006 in two others on matrices
the method itself weighted near zero, and 0.00099 in the richardyoung Gemma 4 12B coder copy, whose fine-tune left 61
normalisation vectors just under the threshold. Twenty-seven of the twenty-nine are ablations; two
(ccharnkij/Ministral-3-8B-Reasoning-2512-Uncensored and richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic)
are training, as their cards say, findings 17 and 18. The thirtieth, 3MPER0RR/Mistral-7B-v0.3-3MPER0RR-abliterated,
changes every matrix in the model and is finding 8. The thirty-first measurement,
prithivMLmods/gemma-4-E4B-it-Uncensored-MAX, is the huihui-ai Gemma 4 E4B copy re-uploaded (finding 9), and the
thirty-second, Jiunsong/supergemma4-e4b-abliterated, paired no tensor with its original (finding 14).

| Copy | Original | Changed tensors | Outside the changed set |
| --- | --- | --- | --- |
| huihui-ai/Huihui-Qwen3-4B-abliterated-v2 | Qwen/Qwen3-4B | 72 of 398 (every attention output and down projection) | 0 |
| huihui-ai/Huihui-Qwen3-30B-A3B-Instruct-2507-abliterated | Qwen/Qwen3-30B-A3B-Instruct-2507 | 6,192 of 18,867 (48 attention outputs, 6,144 expert down projections) | 0 |
| huihui-ai/Huihui-Qwen3.8-27B-abliterated | Qwen/Qwen3.8-27B | 70 (a chosen subset of the residual writers) | 0 |
| huihui-ai/Huihui-Qwen3.5-27B-abliterated | Qwen/Qwen3.5-27B | 130 (every residual writer, prediction head included) | 0 |
| huihui-ai/Qwen2.5-32B-Instruct-abliterated | Qwen/Qwen2.5-32B-Instruct | 129 (128 residual writers and the token embedding) | 0 |
| wangzhang/gemma-4-31B-it-abliterated | google/gemma-4-31B-it | query, key, value and output projections, per layer | 0 |
| mlabonne/gemma-3-27b-it-abliterated | google/gemma-3-27b-it | 124 of 1,247 (every attention output and down projection) | 0 |
| llmfan46/gemma-4-E4B-it-uncensored-heretic | google/gemma-4-E4B-it | 11 attention outputs in the declared layer range | 0.00008 |
| TrevorJS/gemma-4-26B-A4B-it-uncensored | google/gemma-4-26B-A4B-it | attention outputs, down projections and packed expert down projections, per layer | 0 |
| byroneverson/Mistral-Small-Instruct-2409-abliterated | mistralai/Mistral-Small-Instruct-2409 | a listed set of attention outputs and down projections, plus the token embedding | 0 |
| llmfan46/gemma-4-E4B-it-ultra-uncensored-heretic | google/gemma-4-E4B-it | 17 attention outputs in the declared layer range | 0.000006 |
| huihui-ai/Huihui-gemma-4-E4B-it-abliterated | google/gemma-4-E4B-it | 70 of 2,130 (attention output and down projection in layers 7 to 41) | 0 |
| igorls/gemma-4-12B-it-heretic-v1 | google/gemma-4-12B-it | 22 of 677 (13 down projections, 9 attention outputs) | 0 |
| richardyoung/Mistral-7B-Instruct-v0.3-abliterated | mistralai/Mistral-7B-Instruct-v0.3 | 48 of 291 (27 down projections, 21 attention outputs) | 0 |
| prithivMLmods/gemma-4-E4B-it-Uncensored-MAX | google/gemma-4-E4B-it | the same 70 as the huihui-ai copy, field for field | 0 |
| richardyoung/Mistral-7B-Instruct-v0.2-abliterated-obliteratus | mistralai/Mistral-7B-Instruct-v0.2 | 64 of 291 (all seven projections in nine layers, the output head) | 0 |
| evolveon/Mistral-7B-Instruct-v0.3-abliterated | mistralai/Mistral-7B-Instruct-v0.3 | 65 of 291 (every attention output and down projection, the token embedding) | 0 |
| TrevorJS/gemma-4-E4B-it-uncensored | google/gemma-4-E4B-it | 84 of 2,130 (every attention output and down projection) | 0 |
| coder3101/gemma-4-E4B-it-heretic | google/gemma-4-E4B-it | 21 attention outputs in the declared layer range | 0 |
| Madras1/Gemma-4-E4B-Abliterated-Uncensored | google/gemma-4-E4B-it | 81 of 2,076 (attention output, down and gate projection in layers 8 to 34) | 0 |
| llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic | google/gemma-4-E2B-it | 7 attention outputs in the declared layer range | 0 |
| TrevorJS/gemma-4-12B-it-uncensored | google/gemma-4-12B-it | 66 of 677 (attention output and down projection in layers 15 to 47) | 0 |
| richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic | google/gemma-4-12B-it | 557 of 677 (every projection and most normalisations: the parent fine-tune, with the ablation on 52 writers) | 0.00099 |
| ccharnkij/Ministral-3-8B-Reasoning-2512-Uncensored | mistralai/Ministral-3-8B-Reasoning-2512 | 238 of 531 (the seven projections of every layer) | 0 |
| llmfan46/gemma-4-31B-it-uncensored-heretic | google/gemma-4-31B-it | 18 of 1,188 (the attention outputs of layers 30 to 47, the declared range) | 0 |
| coder3101/gemma-4-31B-it-heretic | google/gemma-4-31B-it | 58 of 1,188 (the attention outputs of layers 1 to 58, the declared range; 23 of them rounding residues) | 0 |
| TrevorJS/gemma-4-31B-it-uncensored | google/gemma-4-31B-it | 120 of 1,188 (every attention output and down projection) | 0 |
| huihui-ai/Huihui-gemma-4-31B-it-abliterated-v2 | google/gemma-4-31B-it | 110 of 1,188 (attention output and down projection in layers 5 to 59) | 0 |
| huihui-ai/Huihui-gemma-4-26B-A4B-it-abliterated | google/gemma-4-26B-A4B-it | 50 of 1,013 (attention output and shared down projection in layers 5 to 29; no expert) | 0 |
| coder3101/gemma-4-26B-A4B-it-heretic | google/gemma-4-26B-A4B-it | 20 of 1,013 (the attention outputs of layers 10 to 29, the declared range; no expert) | 0 |

The fair statement of the result is narrow: at the weight level, twenty-nine copies contain the edit or the training
they claim and no other, one contains an edit its card does not name, and one could not be paired. Weight differences
alone cannot certify the absence of hidden behaviour, and the census is thirty measured copies.

## 2. The weights identify the method, and the methods differ more than the cards say

Each copy's difference from its original has a shape that names the recipe, and the shapes do not match the shared
word "abliterated":

- One shared direction, every layer (mlabonne, Gemma 3 27B; huihui-ai, Qwen3 4B, Qwen3 30B-A3B and Qwen3.5 27B). The leading
  direction of every changed matrix agrees with every other at cosine 0.99998 or better.
- One shared direction, chosen layers (huihui-ai, Qwen3.8 27B): 70 of 128 residual writers, the pattern of a tool
  that keeps the layers where the edit measured best.
- One direction per layer (wangzhang, Gemma 4 31B; TrevorJS, Gemma 4 26B-A4B): the edits of one layer agree with
  each other at cosine 0.9996 and above (wangzhang) or 0.94 to 0.99 (TrevorJS), while the layers agree with each other
  at 0.10 to 0.17. These two also restore every row's norm after the projection: the largest row-norm change is under
  0.0011.
- One direction per matrix (byroneverson, Mistral Small 2409): in all 12 layers where both an attention output and a
  down projection changed, the two directions are unrelated (cosine 0.001 to 0.09).
- Many directions per matrix (llmfan46, Gemma 4 E4B): the energy of each change spreads across the leading eight
  directions instead of sitting in the first, a different family of method from the rest.

The maker's description, where there is one, agrees with the shape in every case. The weight of the projection is
readable too: mlabonne's card says refusal weight 1.5 and the row norms move by up to 0.069, where a weight-1
projection leaves a rank-one change and a norm-restored one leaves none; byroneverson's notebook says amount 2.0 and
its row norms move by up to 0.45. The remaining-fraction measurement added after round 2 reads that weight directly
(finding 10). Round 12 adds two shared-direction copies at weights 1.5 and 3.0 (huihui-ai, Gemma 4 31B and 26B-A4B,
finding 21), the per-layer biprojection on all 60 layers of the 31B (TrevorJS, finding 24) and three more arbitrary-rank
copies (finding 22); each reads as its card says.

## 3. The published pass line for "rank one" was a storage artefact

The analytic test for a rank-one edit asks the first singular value to carry at least 99 percent of the change's
energy. Applied to the census it flagged 68 to 121 matrices per copy. I applied the single projection myself to a
verified Mistral Small 3.2 24B base and the same line flagged 68 of my own 80 matrices. The cause is bfloat16
storage: saving a rank-one edit rounds every entry that moved, and the rounding lands outside the first direction.
On every changed matrix in every copy measured, that leftover is 0.0015 to 0.0016 of the weight's norm, across 6,593
matrices on five bases, and a synthetic bfloat16 matrix given the same edit reproduces the share, the leftover and the
27 percent of entries that round back unchanged. One minus the energy share is close to the square of the leftover
over the relative change, so a fixed floor on the share measures how hard the edit pushed and says nothing about its rank: a
matrix clears 0.99 only when the edit moved it by more than about 1.55 percent of its norm.

The pass line that carries between bases is the leftover itself, at most 0.0025 of the weight norm, because it depends
on the storage type alone. Under it, a second change hiding beside a projection would have to stay below about 0.0014
to 0.002 of the weight norm to go unseen. Details and the calibration table: `docs/calibration-mistral-small-3.2.md`.

## 4. One undisclosed configuration change, with an internal contradiction

huihui-ai/Qwen2.5-32B-Instruct-abliterated changes the tokenizer's padding token from `<|endoftext|>` (id 151643) to
`<|im_end|>` (id 151645) and adds a padding entry to the special-token map. The card does not mention it, and the
copy's generation settings still pad with 151643, so code reading the tokenizer and code reading the generation
config pad differently. Harmless for single-prompt generation, a quiet fault for batched generation or further
training. The same copy also projects the refusal direction out of the token embedding: the change moves 71 percent of
the embedding's entries, where a padding remap would move one row, and its direction agrees with all 128 residual
writers at cosine 0.99993 or better. The card documents the embedding edit only by reference to a blog article. Every
other token and configuration difference in the first ten copies is a re-save effect: fields a newer library adds
with their default values, declarations moved between files, or the original vendor's own later chat-template fix
carried over byte for byte. The reading: `docs/cards/huihui-ai--Qwen2.5-32B-Instruct-abliterated-228c265b.reading.md`.
Round 7 adds three kinds of token-side change that are not re-save effects, none of them in a card: a chat template
that marks a different lineage (finding 8), configuration values a copy dropped (finding 11), and a padding token,
`</s>` (id 2), that three copies declare where their originals declare none. Two abliteration tools set the pad token
to the end-of-sequence token when a tokenizer has none (Heretic's `model.py`, lines 151 to 152, is one); in all three
copies the two token files agree and the generation settings are unchanged, so there is no contradiction of the kind
above. Readings: `docs/cards/3MPER0RR--Mistral-7B-v0.3-3MPER0RR-abliterated-d0ad7aaf.reading.md`,
`richardyoung--Mistral-7B-Instruct-v0.3-abliterated-b702c120.reading.md`,
`richardyoung--Mistral-7B-Instruct-v0.2-abliterated-obliteratus-acce918f.reading.md`.

## 5. Makers reach further into the model than the name suggests

Within one maker, the footprint changes from model to model: huihui-ai edits attention outputs only on Qwen3.8 27B,
attention outputs and every feed-forward down projection on Qwen3.5 27B, the multi-token-prediction head as well on
the same copy, and the token embedding on Qwen2.5 32B. On mixture-of-experts bases the edit reaches every expert:
6,144 expert down projections on Qwen3 30B-A3B, and all packed expert down projections on Gemma 4 26B-A4B. wangzhang's
Gemma 4 31B edits the reading side of attention (query, key and value) as well as the writing side. The published
descriptions of the method name the writers; the copies in circulation edit readers, embeddings and prediction heads
too. Round 12 adds the opposite case: on Gemma 4 26B-A4B, where the experts of a layer are one packed tensor, the same
maker's edit reaches the attention outputs and the shared down projections and no expert (finding 20).

## 6. byroneverson's embedding patch equals one layer's direction

The Mistral Small 2409 copy's notebook patches the token embedding separately. The weights show the embedding's
leading direction equal to layer 24's down-projection direction at cosine 1.000 (the notebook's layer 25, counting
from one). The embedding edit therefore reuses one internal layer's direction, a detail the notebook does not state.

## 7. Four copies whose stated original cannot be pinned or compared

Choosing the eight pairs for the seventh census round (`data/batches/round-7-batch-1.json`) turned up four copies
whose cards name an original that the pinning rule (`hpc/pin_census.py`) cannot settle. Each is a provenance fact in
its own right, and each is a reason the published card alone cannot carry the audit.

- OpenYourMind/gemma-4-12B-it-abliterated-uncensored was created at 19:57Z on 2026-06-03. Its stated original,
  google/gemma-4-12B-it, was created on 2026-05-23, yet the original's visible history now begins at 21:14Z on
  2026-06-03, two hours after the copy, and runs to 2026-07-20 in seven commits. Google rewrote the repository's
  history after release, so no surviving revision of the original predates the copy and no revision can be named as
  the one the copy was made from. The same rewrite touches every copy of that base made before 06-03.
- mlabonne/gemma-3-12b-it-abliterated-v2 names google/gemma-3-12b-it correctly, but Google's own card for that model
  declares a base repository, google/gemma-3-12b, that does not exist on the hub. The lineage walker stops at a
  declared parent it cannot open, so the pair waits on a rule for publisher declarations that point nowhere.
- minpeter/Voxtral-Mini-3B-Text-2507-hf-heretic is a text-only extraction of mistralai/Voxtral-Mini-3B-2507, whose
  release carries the audio tower as well. The two repositories do not share tensor names, so a weight-by-weight
  comparison against the stated original is undefined until the text tower is cut out of the original by the same
  recipe, which the card does not give.
- timfromhcs/Ministral-3-14B-abliterated is stored in bf16; its stated original, mistralai/Ministral-3-14B-Instruct-2512,
  is published in FP8 with per-tensor scales. The tensor names differ, so the comparison needs a dequantized original
  first, and any difference measured then includes the dequantization as well as the edit.

The first two were replaced in the batch by igorls/gemma-4-12B-it-heretic-v1 and
llmfan46/gemma-4-E4B-it-ultra-uncensored-heretic; the last two by richardyoung/Mistral-7B-Instruct-v0.2-abliterated-obliteratus
and evolveon/Mistral-7B-Instruct-v0.3-abliterated. The inventory sample (`docs/inventory-sample.md`) already showed
the stated original failing to resolve in 16 of 30 repositories; these four show the ways it fails even when a
repository by that name exists.

## 8. One copy's weights contradict the original its card names

3MPER0RR/Mistral-7B-v0.3-3MPER0RR-abliterated names mistralai/Mistral-7B-v0.3, the base model, as its original, in its
card and in its `base_model` field. Compared against that base, 226 of its 291 tensors changed: every query, key,
value, output, gate, up and down projection in all 32 layers, the token embedding (0.021 of its norm) and the output
head (0.017); only the 65 normalisation vectors are unchanged. The reading-side matrices carry a dense change, 0.008 to
0.027 of each norm, with first-value energy shares of 0.01 to 0.24, leading directions unrelated across layers (cosine
0.03 to 0.24) and 0.94 to 1.11 of the original's action remaining along them. That is training, in every matrix, at
about 2 percent. On top of it the attention outputs of layers 6 to 30 and the down projections of layers 9 to 31 carry
a shared-direction ablation (cosine 0.95 or better across layers, 0.998 and 0.996 in the middle) whose weight follows
a kernel over the layers, 0.11 at layer 9 rising to 1.32 at layer 24 and falling to 0.74 at layer 31, the shape of
Heretic's per-component weight schedule; the card's "Trials: 200" is that tool's default.

The token side names the parent the weights point to. The copy carries a `chat_template.jinja` of 3,959 bytes that
equals mistralai/Mistral-7B-Instruct-v0.3's template at `c170c708` byte for byte; the base has no chat template, and
base and instruct share the same `config.json` and `tokenizer.json` checksums, so the template is the one small file
that tells them apart. The measured footprint fits an abliteration of the instruct model, or of another dense
fine-tune of the base, described as an abliteration of the base. One further comparison, against the instruct
weights, would leave only the ablation. Evidence: `results/weights/3MPER0RR-Mistral-7B-v0.3-3MPER0RR-abliterated.json`,
`results/meta/3MPER0RR-Mistral-7B-v0.3-3MPER0RR-abliterated.json`, the reading
`docs/cards/3MPER0RR--Mistral-7B-v0.3-3MPER0RR-abliterated-d0ad7aaf.reading.md`, and `docs/census-round-7.md`.

## 9. A re-upload measured as the same edit

prithivMLmods/gemma-4-E4B-it-Uncensored-MAX names google/gemma-4-E4B-it in its `base_model` field and says in its card
that it is huihui-ai/Huihui-gemma-4-E4B-it-abliterated re-sharded with no change to the weights. Measured against the
Google original it was pinned to, its report equals the huihui copy's report in every one of 29,820 per-tensor fields
across 2,130 tensors, and the two saved direction files (2,503,680 bytes) are equal byte for byte; the two pinned
Google revisions carry one weight file (shard checksum `cfbd3d2f`). The card names the parent and the field names the grandparent, and the
weight fingerprint shows which is right without a reading. A census that counts copies has to count this one as the huihui
edit, and a comparison tool can flag two pairs with the same original weights and identical measurements by itself.
Evidence: `results/weights/prithivMLmods-gemma-4-E4B-it-Uncensored-MAX.json` against
`results/weights/huihui-ai-Huihui-gemma-4-E4B-it-abliterated.json`; the readings in `docs/cards/`.

## 10. The weight and the rank of an edit are readable from the weights

The remaining-fraction measurement (how much of the original's action the copy keeps along each leading direction)
reads a projection's weight as one minus the fraction. Across round 7 it reads 2.5 on the huihui-ai Gemma 4 E4B copy
(fraction -1.501 to -1.499 in all 70 matrices: the output along the direction is reversed and enlarged by half, with
row norms moved by up to 0.068), 1.0 on the evolveon Mistral copy (0.000 to 0.004 remaining in all 64 matrices, a plain
ablation, and 0.004 on the token embedding's input side), and the per-layer kernels of three Heretic copies: 1.08 to
1.38 on down projections and 0.49 to 0.70 on attention outputs (igorls, Gemma 4 12B), 1.24 to 1.31 and 0.54 to 0.82
(richardyoung, Mistral 7B Instruct v0.3), and the 0.11 to 1.32 to 0.74 kernel of finding 8. None of these weights is
in a card. The rank is readable too: the OBLITERATUS "advanced" copy (richardyoung, Mistral 7B Instruct v0.2) shows a
group of four near-equal singular values and then a drop of 25 to 40 times on each of 63 layer matrices and the output
head, the first four directions carrying 0.90 to 0.99 of each change, which matches the tool's "4 directions (SVD)";
the llmfan46 arbitrary-rank copies show no such gap, with shares that climb only to 0.96 to 0.99 by the eighth value.
Round 8 reads 1.355 on all 81 matrices of the Madras1 Gemma 4 E4B copy against a card that states 1.35, on the output
side of the 54 writers and the input side of the 27 gate projections as the card's two formulas say, and reads the
searched input-side weights of two more arbitrary-rank copies at 1.32 to 2.02 (coder3101, E4B) and 1.86 to 4.41
(llmfan46, E2B). The second pass of round 2 reads the same quantity on the earlier copies. mlabonne's Gemma 3 27B copy reads 1.50
within 0.01 on all 124 matrices against the card's 1.5, with directions 2 to 8 untouched within 0.004. wangzhang's
norm-preserving Gemma 4 31B edit, whose row norms move by at most 0.0008 and so show nothing to the row-norm rule,
reads weights of 2.75 to 3.78 on its 40 attention outputs (past a reflection in every layer) and up to 5.6 on its
query and key projections; the card names a searched strength and no value. byroneverson's Mistral Small copy, whose
notebook says amount 2.0, reads 0.05 to 11.1 by layer: the notebook's per-layer direction is not of unit length, so a
fixed amount becomes a weight of twice the direction's squared length, and the token embedding and layer 24 read the
same 3.09 to four decimals. Round 12 reads 1.50 on all 110 matrices of huihui-ai's second 31B copy (−0.497 to −0.501)
and 3.00 on all 50 of its 26B-A4B copy (−1.998 to −2.004), neither in a card, and the searched input-side weights of
three more arbitrary-rank copies: 1.37 to 3.36 (llmfan46, 31B), 0.51 to 10.18 (coder3101, 31B) and 0.76 to 1.49
(coder3101, 26B-A4B), the first weights under 1 read on the method.
Evidence: the eight `results/weights/` reports of round 7, the six of round 12, the five `results/weights/*.pass-2.json` reports and
`docs/census-round-7.md` and `docs/census-round-3.md`.

## 11. Four configuration values that later libraries omit on save and restore on load (corrected 2026-10-30)

As first written on 2026-10-30 from round 7, this finding said that igorls/gemma-4-12B-it-heretic-v1's `config.json`
lacked four values the original's carries (the audio tower's `audio_samples_per_token`, `hidden_size` and
`output_proj_dims`, 640, 640, 640, and the vision patch size, 48), that the copy's configuration loaded a different
audio geometry under the library that saved it, and that the library had not dropped them. The second and third
claims were wrong. Round 8 measured two more copies of Gemma 4 12B (TrevorJS, saved with transformers 5.12.0;
richardyoung, saved with 5.12.1 from a parent saved with 5.10.2) and both lack the same four fields. Loaded at home
under 5.10.1 and under 5.12.1, the original's configuration, the igorls copy's and the TrevorJS copy's all give 640,
640, 640 and 48: the four values are the defaults of the library's unified Gemma 4 audio and vision configuration
classes (`model_type` gemma4_unified), which the library omits when it writes a configuration and restores when it
reads one, and a save of Google's own configuration under either version drops the same four fields. The 1024 and
1536 read in round 7 are the defaults of the library's other Gemma 4 class, which the copy's `model_type` does not
select. The copies' configurations describe the weights they ship. What stands: a copy saved under transformers 5.10
or later will lack these four fields, the metadata tool needs a rule that judges an absent field under the saving
library's own class defaults, and a reading that loads a configuration must use the class its `model_type` names.
Evidence: `results/meta/igorls-gemma-4-12B-it-heretic-v1.json`, `results/meta/TrevorJS-gemma-4-12B-it-uncensored.json`,
`results/meta/richardyoung-gemma-4-12B-coder-fable5-composer2.5-v1-heretic.json`, the readings in `docs/cards/` and the
library check recorded in `docs/census-round-8.md`.

## 12. Which side of a matrix an edit touched is readable, and one method edits the input side

The two remaining fractions of a changed matrix (along the leading left direction and along the leading right one)
fall in a fixed order for an output-side edit: 273 of the 274 output-side matrices in round 2's pairs 1, 2, 4 and 5 put
the left fraction below the right, and the one exception is the token embedding, whose residual coordinates are its
columns. wangzhang's 54 reading-side edits (query, key and value projections) and all 11 changed matrices of
llmfan46/gemma-4-E4B-it-uncensored-heretic put it the other way. For that heretic copy the leading direction therefore
sits in the input space of each attention output, one over-projected direction per layer at weights 1.27 to 1.79
(median 1.46), under a weak tail of many directions that each keep 0.90 to 1.03 of the original; no entry in the
recipe table describes an input-side direction yet. Round 12 adds 73 input-side matrices on three arbitrary-rank copies
(left above right on all 73) and 280 output-side matrices on three others (left below right on 278). Evidence:
`results/weights/*.pass-2.json`, the six `results/weights/` reports of round 12,
`docs/cards/llmfan46--gemma-4-E4B-it-uncensored-heretic-cc7eab73.reading.md` and `docs/census-round-3.md`.

## 13. A mixture-of-experts abliteration reads expert by expert

TrevorJS/gemma-4-26B-A4B-it-uncensored changes all 128 experts of each of 30 packed expert tensors. Measured one
expert at a time, the experts of a layer share one output direction at median cosine 0.996 to 0.999 (minimum 0.940),
the median expert keeps a first-value energy share of 0.989 to 0.994 in every layer, and the worst expert of a layer
falls to 0.881 in layer 0 and 0.951 to 0.990 elsewhere. The experts' median direction, added to the layer's group,
resolves the two layers the dense matrices left at 0.941 and 0.947: layers 10 and 12 now agree at 0.991 and 0.995.
The scorer takes the worst expert, which is why the copy still carries 30 flags on those tensors; the per-expert
numbers say the edit is one direction per layer applied to every expert. huihui-ai's copy of the same base (round 12)
changes the attention output and the shared down projection of layers 5 to 29 and no expert (finding 20). Evidence:
`results/weights/TrevorJS-gemma-4-26B-A4B-it-uncensored.pass-2.json` and
`docs/cards/TrevorJS--gemma-4-26B-A4B-it-uncensored-ce34ef70.reading.md`.

## 14. Re-exports change the tensor set, and the comparison must map it before it can measure

Two copies in round 8 do not carry the original's tensor names. Jiunsong/supergemma4-e4b-abliterated holds 719 tensors
under `language_model.model.` where google/gemma-4-E4B-it holds 2,130 under `model.`; every one of the 719 is a
language-model name of the original once the prefix is removed, and the audio tower (752 tensors), the vision tower
(659) and their two embedding projections are absent, as is `vision_config` from the copy's configuration. The
comparison strips three wrappers and this is a fourth, so it paired nothing: the report has no measurement and 2,850
flags that count names. Madras1/Gemma-4-E4B-Abliterated-Uncensored holds 2,076 of the original's 2,130 tensors; the 54
absent are the key projection, value projection and key normalisation of layers 24 to 41, the 18 layers that reuse
the keys and values of earlier layers (`num_kv_shared_layers` 18 in both configurations), which the original ships
and never reads and the copy's loader (transformers 5.16.1, `unsloth_fixed`) omits. The 2,076 that remain measure as
a clean scaled projection (finding 10). A census that compares names has to know the wrappers and the unused tensors
of each architecture, or it will report a text-only re-export as unmeasurable and a lighter save as 54 violations.
Evidence: `results/weights/Jiunsong-supergemma4-e4b-abliterated.json`,
`results/weights/Madras1-Gemma-4-E4B-Abliterated-Uncensored.json` and the readings in `docs/cards/`.

## 15. A loader moved a copy's end-of-sequence token, and the copy's files disagree about it

Madras1/Gemma-4-E4B-Abliterated-Uncensored was saved by a loader that writes `unsloth_fixed: true` into
`config.json`. Its `tokenizer_config.json` declares the end-of-sequence token as `<turn|>` (id 106) where the original
declares `<eos>` (id 1), its `config.json` lists `eos_token_id` 106 where the original lists [1, 106], and a pad token
of 0 is added to the configuration and the special-token ids; its generation settings still list [1, 106, 50]. Under
the library, generation stops as the original does; a runtime that reads the configuration or the tokenizer alone
stops at the turn marker only and no longer at `<eos>`. The same loader rewrote the chat template's error branch for
string-valued tool arguments (the fixed conversation renders identically) and wrote the global head dimension as a
per-layer map. None of it is in the card, whose method section the weights confirm in every number. This is the
second copy with a token-side change made by a tool and a disagreement between files (finding 4 is the first);
the loader's signature is a pattern the metadata tool should name. Evidence:
`results/meta/Madras1-Gemma-4-E4B-Abliterated-Uncensored.json` and
`docs/cards/Madras1--Gemma-4-E4B-Abliterated-Uncensored-6ee6560d.reading.md`.

## 16. A copy whose template writes a fixed system text into every conversation, beside an unmodified one

Jiunsong/supergemma4-e4b-abliterated's `chat_template.jinja` is Google's template of 2026-04-10 with a six-line block
added that defines a fixed system text ("You are a precise coding assistant", followed by three rules on raw JSON,
code-only answers and the shortest valid answer) and with the condition that opens the system turn replaced by
`if true`; every conversation rendered with it begins with that text, and a system message the user supplies follows
it. The fixed conversation renders at 545 bytes against the original's 176. The same repository's
`tokenizer_config.json` carries Google's unmodified template, so which template applies depends on the loader. The
card speaks of formatting discipline and release hardening and does not describe the template or the two towers it
dropped (finding 14). At the prompt level this is the largest behavioural change in the census so far, and the
weights behind it are unmeasured. Evidence: `results/meta/Jiunsong-supergemma4-e4b-abliterated.json` and
`docs/cards/Jiunsong--supergemma4-e4b-abliterated-abcc2f15.reading.md`.

## 17. Refusal removal by a merged adapter is readable, and it is distinct from every ablation measured

ccharnkij/Ministral-3-8B-Reasoning-2512-Uncensored, whose card says "LoRA" and names no modules, changes the query,
key, value, output, gate, up and down projections of all 34 layers (238 matrices) and nothing else: the token
embedding, the output head, the 69 normalisation vectors and the 222 tensors of the vision tower are unchanged.
Each matrix moved by 0.6 to 1.8 percent of its norm; the first singular value carries 0.15 to 0.90 of each change and
the first eight 0.67 to 0.99, with the singular values falling slowly (first over second 1.0 to 5.6), so the change is
low-rank with a rank above eight on most matrices. Along every leading direction on both sides the copy keeps 0.94 to
1.05 of the original's action (medians 1.000): nothing was projected out. The leading directions are unrelated across
layers (cosine 0.14 to 0.47 with their median) and within layers (0.29 to 0.37). Three measures separate a
merged adapter from an ablation without a card: a remaining fraction at 1, a slow fall of the singular values and no
shared direction; every ablation in the census takes part or all of the original's action away along its direction
on at least one side (the lower of the two fractions is at or below 0 on the projections and 0.01 to 0.77 on the
biprojected copies) and reads a shared or per-layer direction. Evidence: `results/weights/ccharnkij-Ministral-3-8B-Reasoning-2512-Uncensored.json` and
`docs/cards/ccharnkij--Ministral-3-8B-Reasoning-2512-Uncensored-da7d421f.reading.md`.

## 18. An ablation on top of a fine-tune, measured against the grandparent, separates but its weight does not

richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic names yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1,
a coding fine-tune of google/gemma-4-12B-it, as its parent in the first line of its card and google/gemma-4-12B-it in
its `base_model` field; the pin rule compared against the field. Against Google, 557 of 677 tensors changed. The
dense part is the fine-tune: every projection of all 48 layers at 0.2 to 1.0 percent, first-value shares 0.05 to 0.80,
leading directions unrelated across layers (0.10 to 0.14), 0.98 to 1.09 of the original's action kept along them,
normalisation vectors moved by up to 8.6 percent, the token embedding untouched. On top of it one shared direction
sits on the attention outputs of layers 15 to 47 and the down projections of layers 24 to 42: first-value shares 0.93
to 0.99 there against 0.02 to 0.80 elsewhere, cross-layer agreement 0.90 to 0.998 with the attention outputs of
layers 0 to 14 at 0.042 at most, within-layer agreement 0.918 to 0.998 where both writers carry it. The card's
weights (1.24 to 1.28 and 1.47 to 1.48) do not read: along the shared direction the copy keeps −0.10 to 0.95 of
Google's action, because the fine-tune's own change along that direction adds to the ablation's. The copy's
`config.json` equals the parent's in every field but the version string, so its eight configuration differences from
Google are the parent's, and the copy is float16 throughout because the parent was saved so. The comparison that
would leave only the ablation is against the parent (`237e5d8e`), owed to the next batch with the 3MPER0RR pair of
finding 8. After the re-upload of finding 9 this is the second copy whose card names a nearer parent than its
`base_model` field, and the second reason the pin rule should read the card. Evidence:
`results/weights/richardyoung-gemma-4-12B-coder-fable5-composer2.5-v1-heretic.json`,
`results/meta/richardyoung-gemma-4-12B-coder-fable5-composer2.5-v1-heretic.json` and the reading in `docs/cards/`.

## 19. Half of the round's Gemma 4 copies carry a chat template that matches no revision Google published

Of the seven Gemma 4 copies in round 8, three carry Google's template at the pinned revision byte for byte (TrevorJS
E4B and 12B, richardyoung) and four carry a template that equals no commit of the original repository, each in a
different way. coder3101's is Google's 2026-04-10 template with 14 blank lines removed. llmfan46's E2B copy carries
Google's 2026-04-28 template plus a 14-line macro and seven call sites that accept a list of types in a tool schema,
which no commit of Google's E2B or E4B repository contains (neither repository has a pull-request branch) and which
Google's next template of 2026-05-18 does not adopt. Madras1's is Google's 2026-07-20 template with its header comment
removed and its string-arguments error branch rewritten by the loader. Jiunsong's is finding 16. Three of the four
render the fixed conversation identically, so a rendering check alone passes them; the later-revision rule, which
closed the templates of rounds 2 and 7 by matching Google's own commits, closes none of the four. Patched Google
templates circulate, and a template reading that stops at "matches a published revision" will miss them. Evidence:
the four `results/meta/` reports of round 8 and `docs/census-round-8.md`.

Round 12 adds six Gemma 4 copies on the two larger bases. One carries the pinned template byte for byte (TrevorJS 31B).
Two carry Google's release template of 2026-04-02 where the pin chose the 2026-04-10 revision, because each repository
was created within a day after that fix (huihui-ai 31B and 26B-A4B; the maker's E4B copy in round 7 was the same case).
Two carry Google's 2026-04-10 template with its 15 blank lines removed, one file byte for byte in two repositories
(coder3101 31B and 26B-A4B; the maker's E4B copy in round 8 had 14 blank lines removed). One carries Google's latest
template with one line changed (llmfan46 31B, finding 23). Of the thirteen Gemma 4 copies of rounds 8 and 12, four carry
the template they were pinned against. Evidence: the six `results/meta/` reports of round 12 and
`docs/census-round-12.md`.

## 20. A mixture-of-experts abliteration that reaches no expert, and the card says so

huihui-ai/Huihui-gemma-4-26B-A4B-it-abliterated changes 50 of 1,013 tensors: the attention output and the shared dense
down projection (2816 by 2112) in each of layers 5 to 29, one shared direction at weight 3.0. The 30 packed expert down
tensors (128 by 2816 by 704), the 30 packed gate-up tensors, the 30 routers, the reading-side projections and the
vision tower are unchanged; the largest relative change outside the 50 is exactly 0. The card says no ablation was
performed on the experts, naming 256 per layer where the configuration has 128. The same maker's edit of Qwen3
30B-A3B changed all 6,144 expert down projections beside the 48 attention outputs (finding 5), and TrevorJS's copy of
this base changed all 128 experts of every layer (finding 13). The difference is the tensor layout: on Qwen each expert
is a linear module of its own, on Gemma 4 the experts of a layer are one packed three-dimensional parameter, and a
tool that edits linear modules reaches the first and not the second. A refusal direction removed from the attention
output and the shared projection of a mixture, and left in all 3,840 expert matrices that write into the same
residual stream, is a different edit from the one the same word names on a dense model or on another mixture; the
scorer matched the copy cleanly because its "selected" entry lets a whole kind go unchanged, and it should say when
the kind left unchanged is the experts. Evidence:
`results/weights/huihui-ai-Huihui-gemma-4-26B-A4B-it-abliterated.json`,
`results/weights/TrevorJS-gemma-4-26B-A4B-it-uncensored.pass-2.json` and the readings in `docs/cards/`.

## 21. One maker's shared projection reads three weights on three bases

huihui-ai's three Gemma 4 copies are one method, one shared direction projected out of every attention output and
down projection from a chosen layer onward, at three weights the cards do not state: 2.5 on E4B (layers 7 to 41,
round 7), 1.5 on the second version of the 31B copy (layers 5 to 59) and 3.0 on 26B-A4B (layers 5 to 29). Each reads
to two decimals on every changed matrix (−1.501 to −1.499 on 70, −0.497 to −0.501 on 110, −1.998 to −2.004 on 50
along the shared direction), with the second to eighth directions kept within 0.004. The 31B card says the second
version leaves the first five layers alone, and the weights agree; it compares the two versions by perplexity (13,161
against 13,336) and does not say the weight changed. The 3.0 is the largest shared-direction weight in the census:
the output along the direction is reversed and doubled, and row norms move by up to 0.609 on the 26B-A4B copy and
0.643 on the 31B copy, against 0.068 on E4B. Evidence: `results/weights/huihui-ai-Huihui-gemma-4-31B-it-abliterated-v2.json`,
`results/weights/huihui-ai-Huihui-gemma-4-26B-A4B-it-abliterated.json`,
`results/weights/huihui-ai-Huihui-gemma-4-E4B-it-abliterated.json` and the readings in `docs/cards/`.

## 22. Arbitrary-rank copies across sizes: searched weights from 0.51 to 10.18, rewritten layers left as residues, and a preservation claim that reads 0.007 on every base

Seven copies of the arbitrary-rank method are now measured (llmfan46 on E2B, E4B twice and 31B; coder3101 on E4B,
26B-A4B and 31B). All seven edit the attention outputs only, on the input side, with one searched weight per layer and
a tail of weak directions, and read as their cards say. Round 12 widens the measured bands. The per-layer weight runs
from 0.51 (coder3101 31B, layer 50) to 10.18 (the same copy, layer 48, relative change 0.169, the largest edit of the
method), and four layers of the 26B-A4B copy read 0.76 to 0.92, under a plain ablation; the first-value share falls
to 0.659 on the 26B-A4B copy's layer 10. coder3101's 31B copy rewrote the attention outputs of all 58 layers in its
declared range and left 23 of them as rounding residues (relative change 0.0013 to 0.0018, first share 0.002 to
0.028, the original's action kept at 0.99 to 1.01, row norms within 0.0008): layers the search weighted near zero,
which the energy-share rule flags as failed projections. The two makers differ in one claim and the weights read it
the same way on every base: coder3101's cards claim row-norm preservation and the rows move by 0.0059 to 0.0080 on all
75 edited matrices of its three copies, while llmfan46's cards claim none and the rows move by 0.0016 to 0.066. The
restoration step of the method is an approximation that leaves seven tenths of a percent at every size. Evidence:
`results/weights/llmfan46-gemma-4-31B-it-uncensored-heretic.json`,
`results/weights/coder3101-gemma-4-31B-it-heretic.json`, `results/weights/coder3101-gemma-4-26B-A4B-it-heretic.json`,
the four earlier reports named in findings 10 and 12, and the readings in `docs/cards/`.

## 23. A maker's one-line patch to Google's template writes an empty thought block into every earlier model turn

llmfan46/gemma-4-31B-it-uncensored-heretic's `chat_template.jinja` (18,841 bytes) is Google's template of
2026-07-15 (`68abe480`, the one Google's repository still serves) with one line changed: where Google opens each model
turn of the history with `<|turn>model` and a newline, the copy's template adds `<|channel>thought`, a newline and
`<channel|>` whenever thinking is off and the message carries no reasoning field. The fixed conversation renders at
232 bytes against 204, the earlier answer "Four." becoming "<|channel>thought\n<channel|>Four.". The maker's commit
of 2026-09-19 uploaded, beside the new template, a file named `chat_template.jinja.official-2026-07-09.bak` that
equals Google's 2026-07-15 template byte for byte, and deleted it nine seconds later; the maker replaced the template
seven times between 2026-04-14 and 2026-09-19. Google's card says the 26B and 31B models emit the empty block
themselves when thinking is off and that earlier turns' thoughts are not to be added to the history. The change is
the maker's, it reaches the prompt of every multi-turn conversation with thinking off, and the card does not mention
it; the weights of the copy are the original's outside the 18 attention outputs its card names. After Jiunsong's
fixed system text (finding 16) this is the second template in the census that changes what a conversation renders to,
and the first that does so by patching Google's current template, which the later-revision rule nearly matches and
cannot close. Evidence: `results/meta/llmfan46-gemma-4-31B-it-uncensored-heretic.json` and
`docs/cards/llmfan46--gemma-4-31B-it-uncensored-heretic-33dab253.reading.md`.

## 24. One method measured on four sizes of one family reads the same fingerprint

TrevorJS's norm-preserving biprojection is now measured on Gemma 4 E4B (84 matrices), 12B (66), 26B-A4B (60 dense
matrices and 3,840 experts) and 31B (120), and the four readings agree in every measure that does not depend on the
size. The row norms of every dense matrix stay within 0.0004 (and within 0.0012 per expert row), the first-value
share sits at the storage floor (0.975 to 0.996), the copy keeps a median 0.03 to 0.18 of the original's action along
the leading output direction (scale 1.0 with the biprojection's second term), and the second term bends the two
edits of a layer apart by a few degrees in the same part of the model each time: layer 12 of the 31B at 0.925, layers
10 and 12 of the 26B-A4B at 0.941 and 0.947 before the experts' direction joined, three layers of the E4B at 0.934 to
0.947, and none of the 12B's edited layers (15 to 47) below 0.970. The settings differ once, the 12B's 70 percent of
layers against 100 percent on the other three, and the weights read it. The same second term puts one matrix in 120
of the 31B copy past the 0.0025 leftover line (layer 2's attention output, 0.0032, with 0.016 of its energy in the
second direction) and two of the 26B-A4B's 60 past it; the single-direction floor of finding 3 does not quite cover a
biprojection, and a norm-preserving entry needs its own band. Evidence: `results/weights/TrevorJS-gemma-4-31B-it-uncensored.json`,
`results/weights/TrevorJS-gemma-4-12B-it-uncensored.json`, `results/weights/TrevorJS-gemma-4-E4B-it-uncensored.json`,
`results/weights/TrevorJS-gemma-4-26B-A4B-it-uncensored.pass-2.json` and the readings in `docs/cards/`.

## What the second pass settled

The second census pass (Nautilus, card 5055, download 4080809, comparisons 4080810 to 4080815) repeated round 2's five
comparisons with the remaining-fraction and per-expert measures. Every number both passes share is equal to the last
digit on all 6,085 matched tensors, the shard checksums are identical, and no flag count changed except TrevorJS's (64
to 31, the packed tensors now measured). Its one tooling result: a card written on a cluster, without network access
and with a pinned library older than the architecture (transformers 4.56.2 has no Gemma 4 class), reads "unexplained
differences" on configuration fields and templates that close at home, so every Gemma 4 copy's token-side reading is
the home judgement until the pins move. Details in `docs/census-round-3.md`.

## Not yet established

- Behaviour. Study 1 (Qwen3-4B, original pass complete, modified and repeat passes owed) is the first behavioural read.
  Nothing above says what any copy does when asked a harmful question.
- Variation. Each calibration recipe has one run on one base.
- Population. Thirty-one copies is a sample; the inventory sample of 30 repositories
  (`docs/inventory-sample.md`) shows how mirrors and re-quantizations outnumber sources and how often the stated
  original cannot be resolved (16 of 30).

Weight differences alone cannot certify the absence of hidden behavior.
