# Findings so far

Created by Sean Egan, 2026-10-29.

The results the audit has established so far, strongest first, each with its evidence in this repository. The
population is small: eighteen measurements of seventeen distinct published copies on fourteen bases (one copy is a
re-upload of another), plus two edits of my own made to calibrate the measurement. Numbers are from the committed
reports in `results/weights/` and `results/meta/`.

## 1. Sixteen of the seventeen published copies measured so far are what their cards say they are

Seventeen community copies of open-weight models, five from one maker on Qwen bases, five from five makers on Gemma and
Mistral bases (round 2) and seven more from six makers on Gemma 4 and Mistral 7B bases (round 7), have been compared
tensor by tensor with their stated originals. In sixteen, the changed tensors are exactly the matrices the stated
method edits, and nothing else moved: the largest relative change outside the changed set is 0 in fourteen copies and
0.00008 and 0.000006 in the two others, on matrices the method itself weighted near zero. The seventeenth,
3MPER0RR/Mistral-7B-v0.3-3MPER0RR-abliterated, changes every matrix in the model and is finding 8. The eighteenth
measurement, prithivMLmods/gemma-4-E4B-it-Uncensored-MAX, is the huihui-ai Gemma 4 E4B copy re-uploaded (finding 9).

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

The fair statement of the result is narrow: at the weight level, sixteen copies contain the edit they claim and no
other, and one contains an edit its card does not name. Weight differences alone cannot certify the absence of hidden
behaviour, and the census is seventeen copies.

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
(finding 10).

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
too.

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
Evidence: the eight `results/weights/` reports of round 7 and `docs/census-round-7.md`.

## 11. A configuration that loads a different tower than the weights it ships

igorls/gemma-4-12B-it-heretic-v1 changes 22 text matrices and nothing else, and its `config.json` lacks four values
the original's carries: the audio tower's `audio_samples_per_token`, `hidden_size` and `output_proj_dims` (640, 640,
640) and the vision patch size (48). Under the library version that saved the copy (transformers 5.10.1) the original's
configuration loads those values and the copy's loads a hidden size of 1024, an output projection of 1536 and nothing
for the other two; a 5.10.1 re-save of the original's configuration writes all four back, so the library did not drop
them. The copy ships the audio embedding projection unchanged at shape [3840, 640], the original's geometry, which its
own configuration no longer describes. The card's text-only use is unaffected; whether the copy accepts audio input is
not something this audit runs. Evidence: `results/meta/igorls-gemma-4-12B-it-heretic-v1.json`, the reading
`docs/cards/igorls--gemma-4-12B-it-heretic-v1-5c5f6826.reading.md`, and the library check recorded in
`docs/census-round-7.md`.

## What the second pass adds

The second census pass (Nautilus, card 5055, jobs 4080809 to 4080815) measures, for every changed matrix, how much of
the original's action the copy keeps along each leading direction, which reads the projection weight off the weights
(0 for a removal, negative for an over-projection), and measures the packed Gemma 4 expert tensors one expert at a
time. Those results settle the projection weights of items 2 and 6, give the arbitrary-rank method of llmfan46 its own
measured line, and complete the TrevorJS reading on its thirty expert tensors.

## Not yet established

- Behaviour. Study 1 (Qwen3-4B, original pass complete, modified and repeat passes owed) is the first behavioural read.
  Nothing above says what any copy does when asked a harmful question.
- Variation. Each calibration recipe has one run on one base.
- Population. Seventeen copies is a sample; the inventory sample of 30 repositories
  (`docs/inventory-sample.md`) shows how mirrors and re-quantizations outnumber sources and how often the stated
  original cannot be resolved (16 of 30).

Weight differences alone cannot certify the absence of hidden behavior.
