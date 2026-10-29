# Findings so far

Created by Sean Egan, 2026-10-29.

The results the audit has established so far, strongest first, each with its evidence in this repository. The
population is small: ten published copies on ten bases, plus two edits of my own made to calibrate the measurement. Numbers are from the committed reports in `results/weights/` and `results/meta/`.

## 1. Every published copy measured so far is what its card says it is

Ten community copies of open-weight models, five from one maker on Qwen bases and five from five makers on Gemma and
Mistral bases, have been compared tensor by tensor with their stated originals. In every one, the changed tensors
are exactly the matrices the stated method edits, and nothing else moved: the largest relative change outside the
changed set is 0 in nine copies and 0.00008 in the tenth, on matrices the method itself weighted near zero. No copy
carries an edit its card does not describe.

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

The fair statement of the result is narrow: at the weight level, these copies contain the edit they claim and
no other. Weight differences alone cannot certify the absence of hidden behaviour, and the census is ten copies.

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
its row norms move by up to 0.45. The second pass now running on Nautilus measures that weight directly, as the
fraction of the original's action the copy keeps along each leading direction.

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
other token and configuration difference in the census is a re-save effect: fields a newer library adds with their
default values, declarations moved between files, or the original vendor's own later chat-template fix carried over
byte for byte. The reading: `docs/cards/huihui-ai--Qwen2.5-32B-Instruct-abliterated-228c265b.reading.md`.

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
- Population. Ten copies is a sample; the inventory sample of 30 repositories
  (`docs/inventory-sample.md`) shows how mirrors and re-quantizations outnumber sources and how often the stated
  original cannot be resolved (16 of 30).

Weight differences alone cannot certify the absence of hidden behavior.
