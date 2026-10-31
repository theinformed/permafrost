# Findings so far

Created by Sean Egan, 2026-10-29.

The results the audit has established so far, strongest first, each with its evidence in this repository. The
population is small: fifty-nine measurements of fifty-six distinct published copies on twenty-three originals (four
copies are re-uploads of others and one more names an unmeasured copy as its parent, two copies are measured against
two originals each, one could not be paired tensor by tensor, and one could not be read because its original is
published in float8), plus two edits of my own made to calibrate the measurement. Numbers are from the committed reports in `results/weights/` and `results/meta/`.

## 1. Forty-seven of the fifty published copies measured so far are what their cards say they are

Fifty community copies of open-weight models, five from one maker on Qwen bases, five from five makers on
Gemma and Mistral bases (round 2), seven from six makers on Gemma 4 and Mistral 7B bases (round 7), seven from six
makers on Gemma 4 and Ministral 3 bases (round 8), six from four makers on the two larger Gemma 4 bases (round 12),
five from five makers on Gemma 4, Ministral 3 and Mistral Small bases (round 16), six from six makers on Gemma 4
and Magistral Small bases (round 18), eight from seven makers on Gemma 4, Mistral Nemo and Mistral Small bases
(round 13) and one more on Mistral Small (round 14), have been compared tensor by tensor with their stated
originals. In forty-seven, the changed tensors are exactly the matrices the stated method reaches, and nothing else
moved: the largest relative change outside the changed set is 0 in thirty-nine copies, 0.00008, 0.000006, 0.00024,
0.00031, 0.000096 and 0.000225 in six others on matrices the method itself weighted near zero or did not name,
0.00099 in the richardyoung Gemma 4 12B coder copy, whose fine-tune left 61 normalisation vectors just under the
threshold, and 0.000998 in the aifeifei798 E2B copy, whose fine-tuning sits at the threshold on 26 tensors.
Forty-five of the forty-seven are ablations (one, aifeifei798's, with 0.1 to 0.3 percent of training beside it, as
its card says); two
(ccharnkij/Ministral-3-8B-Reasoning-2512-Uncensored and richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic)
are training, as their cards say, findings 17 and 18. The three others carry a parent their cards do not name:
3MPER0RR/Mistral-7B-v0.3-3MPER0RR-abliterated changes every matrix in the model (finding 8),
lemuralabs/Gemma-4-12B-uncensored-bf16 carries a third party's coding fine-tune under its ablation (finding 25), and
Felldude/Ministral-3-8B-Uncensored carries the instruct model's template and 5 to 11 percent of dense change against
the pretrained base it names (finding 26). The measurements beyond fifty: prithivMLmods's four Uncensored-MAX
copies name huihui-ai copies as their parents, three of them measured as the huihui-ai E4B, 26B-A4B and E2B edits
field for field and one (31B, round 18) reading as a weight-1.0 shared projection on the layer set the named
parent's card states, with that parent unmeasured (finding 9); TimelessSoul/Huihui-gemma-4-12B-it-abliterated is
huihui-ai's 12B file under another name, shard checksum and every field equal (finding 9);
Jiunsong/supergemma4-e4b-abliterated paired no tensor with its original (finding 14);
timfromhcs/Ministral-3-14B-abliterated was compared against an original published in float8 and read nothing but
the quantisation (findings 7 and 37); the richardyoung coder copy is measured twice, against its grandparent and
against its parent (finding 18); and 3MPER0RR's Mistral 7B copy is measured twice, against the pretrained base its
card names and against the instruct model its weights point to (finding 8).

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
| richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic | yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 (the parent) | 52 of 677 (the attention outputs of layers 15 to 47 and the down projections of 24 to 42, the card's list) | 0 |
| llmfan46/gemma-4-26B-A4B-it-uncensored-heretic | google/gemma-4-26B-A4B-it | 27 of 1,013 (the attention outputs of layers 2 to 29, the declared range less two rewritten near zero; no expert) | 0.00024 |
| lemuralabs/Gemma-4-12B-uncensored-bf16 | google/gemma-4-12B-it | 553 of 677 (every projection and most normalisations: a third party's fine-tune the card does not name, with the ablation on 87 writers) | 0.00099 |
| prithivMLmods/gemma-4-26B-A4B-it-Uncensored-MAX | google/gemma-4-26B-A4B-it | the same 50 as the huihui-ai copy, field for field | 0 |
| Felldude/Ministral-3-8B-Uncensored | mistralai/Ministral-3-8B-Base-2512 | 243 of 531 (the seven projections of every layer, the embedding, the head and the projector: dense training at 5 to 11 percent) | 0.00037 |
| aifeifei798/Heretic-Scalpel-E2B | google/gemma-4-E2B-it | 179 of 2,011 (the attention outputs of layers 10 to 34 and down projections of 15 to 34, with training at the threshold on 117 others) | 0.000998 |
| venkycs/Mistral-Small-24B-Instruct-2501-Abliterated | mistralai/Mistral-Small-24B-Instruct-2501 | 78 of 363 (every attention output and down projection of layers 1 to 39) | 0 |
| coder3101/gemma-4-12B-it-heretic | google/gemma-4-12B-it | 86 of 677 (the attention output and down projection of layers 2 to 44, the declared range; 35 of them rounding residues) | 0 |
| 3MPER0RR/gemma-4-12b-it-3MPER0RR-abliterated | google/gemma-4-12B-it | 48 of 677 (29 attention outputs and 19 down projections, the card's own table) | 0 |
| prithivMLmods/gemma-4-31B-it-Uncensored-MAX | google/gemma-4-31B-it | 120 of 1,188 (every attention output and down projection; the named huihui-ai parent is unmeasured) | 0 |
| null-space/gemma-4-31b-it-abliterated | google/gemma-4-31B-it | 80 of 1,188 (the attention output and down projection of layers 20 to 59, the declared range) | 0 |
| WWTCyberLab/gemma-4-26B-A4B-it-abliterated | google/gemma-4-26B-A4B-it | 55 of 1,013 (attention output, shared down projection and packed expert down projections of layers 9 to 26, and 13 rows of the token embedding) | 0 |
| prithivMLmods/gemma-4-E2B-it-Uncensored-MAX | google/gemma-4-E2B-it | 50 of 2,011 (the attention output and down projection of layers 10 to 34, the named huihui-ai parent's stated range; that parent is unmeasured) | 0 |
| llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v2 | mistralai/Magistral-Small-2509 | 49 of 585 (26 down projections and 23 attention outputs in the declared range; 7 in-range matrices rewritten near zero) | 0.00031 |
| grayarea/Magistral-Small-2509-Heretic-v1.2 | mistralai/Magistral-Small-2509 | 64 of 585 (the attention outputs of layers 6 to 39 and the down projections of 10 to 39) | 0 |
| TrevorJS/gemma-4-E2B-it-uncensored | google/gemma-4-E2B-it | 70 of 2,011 (every attention output and down projection) | 0 |
| huihui-ai/Huihui-gemma-4-E2B-it-abliterated | google/gemma-4-E2B-it | 50 of 2,011 (attention output and down projection in layers 10 to 34, the card's range) | 0 |
| AEON-7/Gemma-4-12B-it-AEON-Abliterated-K4-BF16 | google/gemma-4-12B-it | 48 of 677 (the attention output and down projection of the card's 24 listed layers, four directions each) | 0 |
| huihui-ai/Huihui-gemma-4-12B-it-abliterated | google/gemma-4-12B-it | 12 of 677 (attention output and down projection in layers 23 to 28, the card's range) | 0 |
| huihui-ai/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated | mistralai/Mistral-Small-3.2-24B-Instruct-2506 | 80 of 585 (every attention output and down projection) | 0 |
| grimjim/mistralai-Mistral-Nemo-Instruct-2407-extensive-BP-abliteration-12B | mistralai/Mistral-Nemo-Instruct-2407 | 70 of 363 (attention output and down projection in layers 3 to 37, three block directions) | 0.000096 |
| DuoNeural/Mistral-NeMo-12B-Abliterated | mistralai/Mistral-Nemo-Instruct-2407 | 80 of 363 (every attention output and down projection, at the card's α 0.3) | 0 |
| llmfan46/gemma-4-12B-it-uncensored-heretic | google/gemma-4-12B-it | 16 of 677 (the attention outputs of layers 24 to 39, the declared range) | 0 |
| 3MPER0RR/Mistral-7B-v0.3-3MPER0RR-abliterated | mistralai/Mistral-7B-Instruct-v0.3 (the parent the weights point to) | 49 of 291 (26 attention outputs of layers 6 to 31, 23 down projections of 9 to 31; the dense change against the base is gone) | 0 |
| timfromhcs/Ministral-3-14B-abliterated | mistralai/Ministral-3-14B-Instruct-2512 | not readable: the original is published in float8 and 280 matrices read as the quantisation | not readable |
| llmfan46/Mistral-Small-3.2-24B-Instruct-2506-ultra-uncensored-heretic | mistralai/Mistral-Small-3.2-24B-Instruct-2506 | 8 of 585 (attention outputs inside the declared layers 7 to 34; 20 in-range matrices rewritten near zero) | 0.000225 |
| TimelessSoul/Huihui-gemma-4-12B-it-abliterated | google/gemma-4-12B-it | the same 12 as the huihui-ai copy, shard checksum and every field equal | 0 |

The fair statement of the result is narrow: at the weight level, forty-seven copies contain the edit or the
training they claim and no other, three carry a parent their cards do not name, one could not be paired and one
could not be read. Weight differences alone cannot certify the absence of hidden behaviour, and the census is
fifty-six distinct copies, fifty of them read.

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
copies (finding 22); each reads as its card says. Round 16 adds a shared projection at weight 1.0 on all 78 residual
writers of Mistral Small 24B 2501 (venkycs, finding 28), an arbitrary-rank copy on the mixture (llmfan46, finding 22),
the first ablation with two or three directions per matrix (aifeifei798, finding 27), the row-normalised method
measured against its parent (richardyoung, finding 18) and two copies whose dense change carries a parent the card
does not name (lemuralabs and Felldude, findings 25 and 26). Round 18 adds an eight-direction subspace projection
whose per-layer scale schedule reads from the weights to two decimals (null-space, finding 29), a two-pass per-layer
ablation that reaches a mixture's experts and scales thirteen embedding rows (WWTCyberLab, finding 30), two Heretic
configurations on one reasoning model that share no equal field (llmfan46 and grayarea, finding 31), two more
arbitrary-rank copies, the first to edit the down projections (coder3101 12B and llmfan46 Magistral, finding 22), a
shared-direction edit whose per-layer strength follows no kernel (3MPER0RR 12B) and two weight-1.0 shared
projections whose cards name unmeasured huihui-ai parents (prithivMLmods 31B and E2B, finding 9).

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
to 0.002 of the weight norm to go unseen. Details and the calibration table: `docs/calibration-mistral-small-3.2.md`. Round 16's venkycs copy of Mistral Small
24B 2501 reads the floor again on a base outside that calibration: on its 78 changed matrices (relative change 0.013 to
0.019) the leftover is 0.00152 to 0.00155 of the weight norm and the first share 0.986 to 0.994, 56 of the 78 under the
0.99 line and all 78 inside the 0.0025 line (`results/weights/venkycs-Mistral-Small-24B-Instruct-2501-Abliterated.json`). Round 18 reads it on
three more copies and a seventh base: prithivMLmods's 31B copy (120 matrices, changes 0.012 to 0.016, leftover
0.0013 to 0.0014, 52 under the 0.99 line), its E2B copy (50 matrices, changes 0.023 to 0.028, leftover 0.0014 to
0.0016, none under the line) and grayarea's Magistral copy (64 matrices, changes 0.008 to 0.025, leftover 0.0014 to
0.0016, 13 under the line), every one of the 234 inside the 0.0025 line. Rounds 13 and 14 read it on five more
copies and an eighth base: huihui-ai's Mistral Small 3.2 copy (80 matrices, changes 0.014 to 0.022, leftover
0.00152 to 0.00157, 37 under the 0.99 line, inside the calibration envelope made on that base so no flag),
grimjim's Nemo copy (70, changes 0.013 to 0.022, leftover 0.00152 to 0.00157, 34 under the line), huihui-ai's E2B
and 12B copies (50 and 12, leftover 0.00127 to 0.00158, none under the line) and 3MPER0RR's copy against the instruct
model (49, leftover 0.00096 to 0.00162, 14 under the line on its weakest down projections), every one of the 261
inside the 0.0025 line. DuoNeural's Nemo copy is the artefact at its clearest: a weight of 0.3 moves each matrix by
only 0.0042 to 0.0058 of its norm, the leftover stays at 0.00119 to 0.00130, and the first share falls to 0.916 to
0.950 on all 80 matrices, every one flagged and every one a rank-one edit at the card's own weight
(`results/weights/DuoNeural-Mistral-NeMo-12B-Abliterated.json`).

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
repository by that name exists. Round 14 measured the fourth pair anyway: the pinner admitted
timfromhcs/Ministral-3-14B-abliterated against the float8 original, the download verified both sides' checksums,
and the comparison read raw eight-bit codes against bfloat16 values, 280 of 585 matrices at relative change 0.999
with 921 flags (finding 37). The rule this list implied is now a refusal the pinner should make: an original whose
configuration carries a `quantization_config` is not compared until it is dequantised.

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
weights, would leave only the ablation. Round 16's Felldude/Ministral-3-8B-Uncensored repeats the pattern on a second
family and a second maker (finding 26): a pretrained base named as the original, the instruct repository's template
byte for byte, and dense change in every language-model matrix. Evidence:
`results/weights/3MPER0RR-Mistral-7B-v0.3-3MPER0RR-abliterated.json`,
`results/meta/3MPER0RR-Mistral-7B-v0.3-3MPER0RR-abliterated.json`, the reading
`docs/cards/3MPER0RR--Mistral-7B-v0.3-3MPER0RR-abliterated-d0ad7aaf.reading.md`, and `docs/census-round-7.md`.
The same maker's Gemma 4 12B copy (round 18) does not repeat the pattern: against the instruct model it names, 48
matrices changed and 629 tensors are equal to the original, one shared direction at an irregular per-layer strength
and no dense change beneath it, with the card's own comparison table right to the tensor
(`results/weights/3MPER0RR-gemma-4-12b-it-3MPER0RR-abliterated.json`).

Round 14 ran the further comparison, and it settles the finding. Against mistralai/Mistral-7B-Instruct-v0.3 at
`c170c708`, the same copy revision changes 49 of 291 tensors, the attention outputs of layers 6 to 31 and the down
projections of layers 9 to 31, and the other 242 equal the instruct weights exactly: the 226-tensor dense change
measured against the base was the instruct fine-tune, and the copy is an ablation of the instruct model described
as an ablation of the base. The 49 leading directions equal round 7's on the same matrices (cosine median 0.9999,
least 0.988), so the base comparison had isolated the ablation's direction through the fine-tune, and the kernel
now reads cleanly: 0.11 at layer 9 rising to 1.32 at layer 24 and falling to 0.74 at layer 31 on the down
projections, 1.10 to 1.35 on the attention outputs of layers 6 to 30 and 0.05 at layer 31, output side (left below
right on 48 of 49), rows moved 0.001 to 0.011. The template that named the parent is, against this original, a
moved file. Evidence: `results/weights/3MPER0RR-Mistral-7B-v0.3-3MPER0RR-abliterated.instruct.json`,
`results/meta/3MPER0RR-Mistral-7B-v0.3-3MPER0RR-abliterated.instruct.json`, the reading
`docs/cards/3MPER0RR--Mistral-7B-v0.3-3MPER0RR-abliterated-d0ad7aaf.instruct.reading.md` and
`docs/census-round-14.md`.

## 9. A re-upload measured as the same edit

prithivMLmods/gemma-4-E4B-it-Uncensored-MAX names google/gemma-4-E4B-it in its `base_model` field and says in its card
that it is huihui-ai/Huihui-gemma-4-E4B-it-abliterated re-sharded with no change to the weights. Measured against the
Google original it was pinned to, its report equals the huihui copy's report in every one of 29,820 per-tensor fields
across 2,130 tensors, and the two saved direction files (2,503,680 bytes) are equal byte for byte; the two pinned
Google revisions carry one weight file (shard checksum `cfbd3d2f`). The card names the parent and the field names the grandparent, and the
weight fingerprint shows which is right without a reading. A census that counts copies has to count this one as the huihui
edit, and a comparison tool can flag two pairs with the same original weights and identical measurements by itself.
Round 16 measured the same maker's prithivMLmods/gemma-4-26B-A4B-it-Uncensored-MAX, whose card says the same of
huihui-ai/Huihui-gemma-4-26B-A4B-it-abliterated and whose `base_model` field again names Google: every per-tensor
field of all 1,013 tensors equals the huihui-ai report of round 12, the direction files are equal byte for byte
(sha256 `2b8bd691`), and the weights went up nine hours after huihui-ai's. Two re-uploads from one maker, both
counted as the huihui-ai edit. Evidence: `results/weights/prithivMLmods-gemma-4-E4B-it-Uncensored-MAX.json` against
`results/weights/huihui-ai-Huihui-gemma-4-E4B-it-abliterated.json`,
`results/weights/prithivMLmods-gemma-4-26B-A4B-it-Uncensored-MAX.json` against
`results/weights/huihui-ai-Huihui-gemma-4-26B-A4B-it-abliterated.json`; the readings in `docs/cards/`.

Round 18 measured the maker's 31B and E2B copies, whose cards name huihui-ai/Huihui-gemma-4-31B-it-abliterated (the
first version) and huihui-ai/Huihui-gemma-4-E2B-it-abliterated, neither of which the census has measured, so the
field test cannot be run. What the weights say fits the cards: both are one shared direction at weight 1.00 on the
output side (−0.001 to 0.008 and −0.000 to −0.005 remaining), on all 120 residual writers of the 31B and on the 50 of
layers 10 to 34 of the E2B, the layer set the huihui-ai E2B card states ("the first 10 layers have not been
abliterated"); the 31B copy's weights went up 77 minutes after the first huihui-ai version's and a day before the
second version existed, and against that second version (round 12, 110 matrices at weight 1.5) no field is equal;
the E2B copy's went up five days after its parent's. The E2B copy also carries the parent's template, Google's
release file under a later pin (finding 19). Both wait on their parents in a batch. Evidence:
`results/weights/prithivMLmods-gemma-4-31B-it-Uncensored-MAX.json`,
`results/weights/prithivMLmods-gemma-4-E2B-it-Uncensored-MAX.json` and the readings in `docs/cards/`.

Round 13 measured the E2B parent and the field test runs: huihui-ai/Huihui-gemma-4-E2B-it-abliterated equals the
prithivMLmods E2B copy in every field of all 2,011 tensors and in every singular value, on one original weight file
(shard `2db5482b` under both pins), with the two modified shards differing only in checksum because the
repositories were saved separately. Three of the maker's four re-uploads are now measured as the huihui-ai edits;
the 31B parent (the first version) was pinned in round 14 and did not run. Round 14 adds a fourth re-upload from
another maker: TimelessSoul/Huihui-gemma-4-12B-it-abliterated, one commit saying "Duplicate from
huihui-ai/Huihui-gemma-4-12B-it-abliterated", carries the source's shard under the same checksum (`2dd13d86`) and
equals round 13's measurement of the source in every field; its `base_model` field names Google. Evidence:
`results/weights/huihui-ai-Huihui-gemma-4-E2B-it-abliterated.json`,
`results/weights/TimelessSoul-Huihui-gemma-4-12B-it-abliterated.json` against
`results/weights/huihui-ai-Huihui-gemma-4-12B-it-abliterated.json`, and the readings in `docs/cards/`.

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
(coder3101, 26B-A4B), the first weights under 1 read on the method. Round 16 reads 3.00 again on the 50 matrices of
prithivMLmods's re-upload of the huihui-ai 26B-A4B copy (−1.998 to −2.004), 1.00 on all 78 of venkycs's Mistral Small
24B copy (−0.0041 to −0.0020 remaining; the card the maker copied names no weight) and searched input-side weights of
0.42 to 1.52 on llmfan46's 26B-A4B copy, the smallest on the method. It reads no weight on the two row-normalised
ablations, richardyoung's against its parent and lemuralabs's, where −0.27 to 0.95 and −0.33 to 0.97 of the original's
action remain along a rank-one shared direction, and no single weight on aifeifei798's two- and three-direction edits.
Round 18 reads 1.00 on the 120 matrices of prithivMLmods's 31B copy and the 50 of its E2B copy (−0.001 to 0.008
and −0.000 to −0.005 remaining), searched input-side weights of 0.92 to 3.90 on coder3101's 12B copy and 1.69 to
4.71 on llmfan46's Magistral copy, null-space's per-layer scale schedule of 0.35 to 1.35 to the second decimal on
all 80 matrices (finding 29), grayarea's 1.24 to 1.35 on 32 of 34 attention outputs and 0.51 to 1.39 to 1.13 kernel
on 30 down projections, and a weight near 1 on every layer matrix of WWTCyberLab's copy (−0.13 to 0.17 remaining)
under a card that states 4.0 and 3.0; it reads no weight on 3MPER0RR's 12B copy, where −0.20 to 0.96 remains along
one shared direction with no shape across the layers. Evidence: the eight `results/weights/` reports of round 7,
the six of round 12, the seven of round 16, the eight of round 18, the five
`results/weights/*.pass-2.json` reports and
`docs/census-round-7.md` and `docs/census-round-3.md`. Rounds 13 and 14 read 1.00 on the 50 matrices of huihui-ai's
E2B copy and the 12 of its 12B copy (−0.005 to 0.005 remaining), 0.99 on the 80 of its Mistral Small 3.2 copy (0.006
to 0.008), 1.0 on grimjim's 70 (−0.003 to 0.005), 0.29 to 0.30 on all 80 of DuoNeural's against a card that states
α 0.3 (finding 35), the kernel of finding 8 cleanly on 3MPER0RR's copy against the instruct model (0.11 to 1.32 to
0.74 on the down projections, 1.10 to 1.35 on the attention outputs), and searched input-side weights of 0.32 to
3.63 on llmfan46's 12B copy and 2.62 to 5.28 on its Mistral Small 3.2 copy. It reads no single weight on AEON-7's
rank-four edit, where the first-four share (0.996 to 0.997) and the gap between the fourth and fifth singular
values (19 to 195 times) read the rank instead (finding 34), and reads TrevorJS's E2B biprojection as near 0 kept
on most layers with 0.24 to 0.69 on three.

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
library check recorded in `docs/census-round-8.md`. Round 18's two 12B copies lack the same four fields, coder3101's
under the same version string as Google's file (5.10.0.dev0 on both sides: Google's configuration was written with
the defaults in it and any 5.10 save drops them) and 3MPER0RR's under 5.16.1, which also moves `global_head_dim`
and `num_global_key_value_heads` into a `per_layer_config` map (`results/meta/coder3101-gemma-4-12B-it-heretic.json`,
`results/meta/3MPER0RR-gemma-4-12b-it-3MPER0RR-abliterated.json`). Round 13's AEON-7 and llmfan46 12B copies lack
the same four fields (5.10.0.dev0 and 5.10.2), and the round adds a fifth field that is a revision and not a
default: `text_config.max_position_embeddings`, which Google raised from 131,072 to 262,144 in commit `5926caa4` of
2026-06-04. AEON-7's copy, pinned to the revision before, carries the later value because the maker made the same
change on 06-07 ("Restore native 256k context"); huihui-ai's 12B copy, pinned to the revision after, carries the
earlier value because its configuration is Google's 06-03 file byte for byte; TimelessSoul's re-upload of that copy,
pinned to July's revision, reads the same field the same way. One field, three copies, no edit by any maker
(`results/meta/AEON-7-Gemma-4-12B-it-AEON-Abliterated-K4-BF16.json`,
`results/meta/huihui-ai-Huihui-gemma-4-12B-it-abliterated.json`,
`results/meta/TimelessSoul-Huihui-gemma-4-12B-it-abliterated.json`).

## 12. Which side of a matrix an edit touched is readable, and one method edits the input side

The two remaining fractions of a changed matrix (along the leading left direction and along the leading right one)
fall in a fixed order for an output-side edit: 273 of the 274 output-side matrices in round 2's pairs 1, 2, 4 and 5 put
the left fraction below the right, and the one exception is the token embedding, whose residual coordinates are its
columns. wangzhang's 54 reading-side edits (query, key and value projections) and all 11 changed matrices of
llmfan46/gemma-4-E4B-it-uncensored-heretic put it the other way. For that heretic copy the leading direction therefore
sits in the input space of each attention output, one over-projected direction per layer at weights 1.27 to 1.79
(median 1.46), under a weak tail of many directions that each keep 0.90 to 1.03 of the original; no entry in the
recipe table describes an input-side direction yet. Round 12 adds 73 input-side matrices on three arbitrary-rank copies
(left above right on all 73) and 280 output-side matrices on three others (left below right on 278). Round 16 adds 27
input-side matrices (llmfan46's 26B-A4B copy, left above right on all 27) and 128 output-side matrices on two shared
projections (prithivMLmods's re-upload and venkycs's copy, left below right on all 128); the row-normalised edits read a
side less cleanly (left below right on 20 of richardyoung's 52 matrices against the parent and 29 of lemuralabs's 66
ablated ones). Round 18 adds 100 input-side matrices on two arbitrary-rank copies (coder3101's 12B, 51; llmfan46's
Magistral, 49; left above right on all 100) and 368 output-side matrices on five copies (prithivMLmods's 31B and E2B,
120 and 50; null-space's 31B, 80; grayarea's Magistral, 64; WWTCyberLab's 54 layer matrices; left below right on all
368); 3MPER0RR's 12B copy reads no side (left below right on 24 of 48). Rounds 13 and 14 add 24 input-side
matrices on two arbitrary-rank copies (llmfan46's 12B, 16; its Mistral Small 3.2, 8; left above right on all 24) and
455 output-side matrices on eight copies (TrevorJS E2B 68 of 70, huihui-ai E2B 50, AEON-7 47 of 48, huihui-ai 12B 12,
huihui-ai Mistral Small 3.2 80, grimjim 70, DuoNeural 80, 3MPER0RR against the instruct model 48 of 49). Evidence:
`results/weights/*.pass-2.json`, the six `results/weights/` reports of round 12, the seven of round 16,
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
`docs/cards/TrevorJS--gemma-4-26B-A4B-it-uncensored-ce34ef70.reading.md`. WWTCyberLab's copy of the same base
(round 18, finding 30) is the second to reach the experts: in each of its 18 layers all 128 experts' down projections
changed, sharing the leading output direction at median cosine 0.98 to 1.00, with the median expert's first share
0.990 to 0.996 in the eight rank-one layers and 0.56 to 0.68 in the ten two-direction layers, the same split as the
dense writers beside them (`results/weights/WWTCyberLab-gemma-4-26B-A4B-it-abliterated.json`).

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
`results/weights/Madras1-Gemma-4-E4B-Abliterated-Uncensored.json` and the readings in `docs/cards/`. Round 14 adds
two tensor sets the comparison could not map. DarkRomeo88/gemma-4-12b-it-heretic-comfyui holds four whole
single-file checkpoints with no index, so one tensor name recurs four times and the loader stopped (finding 33).
mistralai/Ministral-3-14B-Instruct-2512 holds 560 scale tensors (`weight_scale_inv`, `activation_scale`) beside its
float8 weights that no bfloat16 copy has, so the pair reads as 560 tensors on one side and a quantisation on the
other (finding 37).

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
the loader's signature is a pattern the metadata tool should name. aifeifei798/Heretic-Scalpel-E2B (round 16,
finding 27) carries the same signature with no token moved: no library version, `torch_dtype` beside `dtype`, the
per-layer head map, the end token repeated in the generation list and the template written into the tokenizer
configuration as well, with every token id and both templates equal to Google's. Evidence:
`results/meta/Madras1-Gemma-4-E4B-Abliterated-Uncensored.json` and
`docs/cards/Madras1--Gemma-4-E4B-Abliterated-Uncensored-6ee6560d.reading.md`. Round 18 separates two of the
signature's parts. 3MPER0RR's 12B copy carries the per-layer head map with no `unsloth_fixed` field and
`transformers_version` 5.16.1: the map is the newer library's own save form, and only the other marks name the
loader. llmfan46's and grayarea's Magistral copies carry `unsloth_fixed` with the three token ids written into the
configuration, on a base whose original ships no library tokenizer at all; there the loader's conversion supplied
the tokenizer files themselves (finding 31). Round 14's llmfan46 Mistral Small 3.2 copy carries `unsloth_fixed`
the same way, on a second original that ships no library tokenizer, with a 423-byte tokenizer configuration
re-saved under 5.3.0 and the conversion's template and special-tokens map
(`results/meta/llmfan46-Mistral-Small-3.2-24B-Instruct-2506-ultra-uncensored-heretic.json`).

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

## 18. An ablation on top of a fine-tune, measured against the grandparent, separates but its weight does not (corrected 2026-10-31)

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
Google's action, which round 8 laid on the fine-tune's own change along that direction. The copy's
`config.json` equals the parent's in every field but the version string, so its eight configuration differences from
Google are the parent's, and the copy is float16 throughout because the parent was saved so. The comparison that
would leave only the ablation is against the parent (`237e5d8e`), owed to the next batch with the 3MPER0RR pair of
finding 8. After the re-upload of finding 9 this is the second copy whose card names a nearer parent than its
`base_model` field, and the second reason the pin rule should read the card.

Round 16 made the parent comparison, and it corrects the explanation. Against yuxinlu1's fine-tune the copy changes
52 of 677 tensors, the 33 attention outputs and 19 down projections the card lists, and the other 625 read exactly 0;
the fine-tune is gone from the measurement. The ablation is rank one (first share 0.990 to 0.9999, the first singular
value 10 to 171 times the second) along one shared direction (cross-layer cosine 0.90 to 0.998), and the kept
fraction is the same spread as before: −0.09 to 0.95 on the attention outputs (median 0.74), −0.27 to 0.70 on the
down projections, left below right on 20 of 52, where the card's 1.24 to 1.48 would read −0.24 to −0.48. The spread
is the edit's own. The maker's `reproduce/config.toml` names two steps the calibrated projection does not have, a
"full" row normalisation with a rank-3 correction and an orthogonalised direction, and the measurement leaves the
cause between them; the row norms read 0.0035 to 0.033 off after the restoration. The same shape appears on a second
tool in the same round (lemuralabs's "ablation 1.3.0", finding 25: −0.19 to 0.97 kept along a rank-one shared
direction, no weight stated). For a method with a row-normalisation step the remaining fraction reads the side and
the rank of the edit and no weight, on the parent as on the grandparent. Evidence:
`results/weights/richardyoung-gemma-4-12B-coder-fable5-composer2.5-v1-heretic.json` (against Google),
`results/weights/richardyoung-gemma-4-12B-coder-fable5-composer2.5-v1-heretic.parent.json` (against the parent),
the two `results/meta/` reports of the same names and the two readings in `docs/cards/`.

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

Round 16 adds four Gemma 4 copies. Two carry the pinned template (lemuralabs 12B, prithivMLmods 26B-A4B, the latter
pinned to the release commit), one carries it twice, in `chat_template.jinja` and inside `tokenizer_config.json`,
both Google's byte for byte (aifeifei798 E2B, a loader's save), and llmfan46's 26B-A4B copy carries the maker's
patched template again: Google's 2026-04-28 template with the same 14-line macro and the same `is iterable` and
list-typed comparisons as the E2B copy above, without the empty thought block of finding 23, matching none of
Google's 13 revisions and rendering the fixed conversation identically. Of the seventeen Gemma 4 copies of rounds 8,
12 and 16, seven carry the template they were pinned against, and the maker's patch is now in three of its five
copies. Evidence: `results/meta/llmfan46-gemma-4-26B-A4B-it-uncensored-heretic.json` and `docs/census-round-16.md`.

Round 18 adds six Gemma 4 copies. Five carry the template they were pinned against (coder3101 12B, 3MPER0RR 12B,
null-space 31B, WWTCyberLab 26B-A4B, prithivMLmods 31B, the last two pinned to the release commit) and one carries
Google's E2B release template of 2026-04-02 under a 2026-04-10 pin (prithivMLmods E2B), the earlier-revision case
arrived at through a re-upload: the copy's files are those of the huihui-ai repository created on 2026-04-08, whose
own template is the release file with carriage-return line endings. No patched or blank-line-normalised template
this round. Of the twenty-three Gemma 4 copies of rounds 8, 12, 16 and 18, twelve carry the template they were pinned
against. Evidence: `results/meta/prithivMLmods-gemma-4-E2B-it-Uncensored-MAX.json` and `docs/census-round-18.md`.

Rounds 13 and 14 add six Gemma 4 copies. Three carry the template they were pinned against byte for byte (TrevorJS
E2B, AEON-7 12B, huihui-ai 12B) and one the same text with carriage-return line endings (huihui-ai E2B, pinned to
the release commit it was made from: the source of the prithivMLmods case above). One is the earlier-revision case
through a re-upload again (TimelessSoul 12B, Google's 17,466-byte file of 06-03 under a pin whose template is the
18,683-byte file of 07-09). One is the maker's patch a fourth time: llmfan46's 12B copy carries Google's pinned
template plus the `format_type_argument` macro of its 26B-A4B copy and two guards, 21,488 bytes against 17,466,
without the thought-block line of finding 23. Of the twenty-nine Gemma 4 copies of rounds 8, 12, 13, 14, 16 and 18,
fifteen carry the template they were pinned against byte for byte and one more up to line endings. Evidence:
`results/meta/llmfan46-gemma-4-12B-it-uncensored-heretic.json`,
`results/meta/TimelessSoul-Huihui-gemma-4-12B-it-abliterated.json`, `docs/census-round-13.md` and
`docs/census-round-14.md`.

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
the kind left unchanged is the experts. Round 16 adds two more edits of this base that reach no expert, llmfan46's
arbitrary-rank copy on 27 attention outputs (finding 22) and prithivMLmods's re-upload of this copy (finding 9); in
both the 30 packed expert down tensors, the 30 gate-up tensors and the 30 routers read exactly 0. Of the seven
measurements on this original, TrevorJS's and WWTCyberLab's (round 18, finding 30) changed the experts; the four
others left all 3,840 expert matrices alone. Evidence:
`results/weights/huihui-ai-Huihui-gemma-4-26B-A4B-it-abliterated.json`,
`results/weights/llmfan46-gemma-4-26B-A4B-it-uncensored-heretic.json`,
`results/weights/prithivMLmods-gemma-4-26B-A4B-it-Uncensored-MAX.json`,
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
`results/weights/huihui-ai-Huihui-gemma-4-E4B-it-abliterated.json` and the readings in `docs/cards/`. Round 18
adds a fourth weight on two copies whose cards name this maker as their parent and whose parents are unmeasured
(finding 9): 1.00 on all 120 residual writers of the 31B (the first version, every layer) and 1.00 on the 50 of
layers 10 to 34 of the E2B. If the cards hold, the maker's 31B edit went from weight 1.0 on all 60 layers to 1.5 on
layers 5 to 59 between its two versions, a change the second version's card describes as leaving the first five
layers alone and compares by perplexity. Round 13 measured two of the maker's parents and a copy on a Mistral base,
and the weights read 1.00 on the E2B (−0.005 to −0.003 on the 50 writers of layers 10 to 34, the prithivMLmods
re-upload confirmed field for field), 1.00 on the 12B (−0.003 to 0.005 on the 12 writers of layers 23 to 28, the
card's "Only layers 23-28") and 0.99 on Mistral Small 3.2 (0.006 to 0.008 on all 80 writers). Six weights on six
bases from one script, 2.5, 1.5, 3.0, 1.00, 1.00 and 0.99, none in a card; the three measured first (E4B, the 31B
second version, 26B-A4B) sit above 1 and the three measured now sit at 1. Evidence:
`results/weights/huihui-ai-Huihui-gemma-4-E2B-it-abliterated.json`,
`results/weights/huihui-ai-Huihui-gemma-4-12B-it-abliterated.json`,
`results/weights/huihui-ai-Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated.json`.

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
restoration step of the method is an approximation that leaves seven tenths of a percent at every size. Round 16's
llmfan46/gemma-4-26B-A4B-it-uncensored-heretic is the eighth copy and the second on the mixture: 27 attention outputs
in layers 2 to 29, input side (left above right on all 27), weights 0.42 to 1.52 with five under 1 (0.42 on layer 3
is the smallest on the method), no expert touched, and the attention outputs of layers 1 and 5, inside the declared
range, rewritten at 0.000235 and 0.000127 of their norm, the residue case at a smaller size; the rows moved by 0.0006
to 0.0079 under no preservation claim. Evidence:
`results/weights/llmfan46-gemma-4-26B-A4B-it-uncensored-heretic.json`,
`results/weights/llmfan46-gemma-4-31B-it-uncensored-heretic.json`,
`results/weights/coder3101-gemma-4-31B-it-heretic.json`, `results/weights/coder3101-gemma-4-26B-A4B-it-heretic.json`,
the four earlier reports named in findings 10 and 12, and the readings in `docs/cards/`.

Round 18 adds the ninth and tenth copies, the first two that edit the down projections beside the attention
outputs, on both sides of the maker line. coder3101/gemma-4-12B-it-heretic changes both writers of layers 2 to 44:
51 edits (28 attention outputs, 23 down projections) at searched input-side weights of 0.92 to 3.90, and 35 in-range
matrices left as rounding residues (relative change 0.00107 to 0.00184), more residues than edits on the lower
down projections; the rows of all 51 edits moved by 0.0057 to 0.0079 under the maker's preservation claim, the band
of its three other bases. llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v2, the first on a Mistral base,
changes 26 down projections and 23 attention outputs of layers 9 to 36 at weights 1.69 to 4.71, leaves 7 in-range
matrices at 0.00008 to 0.00031, and moves its rows by 0.0004 to 0.099 under no claim. Ten copies, five bases, all on
the input side, one direction per matrix. Evidence: `results/weights/coder3101-gemma-4-12B-it-heretic.json`,
`results/weights/llmfan46-Magistral-Small-2509-ultra-uncensored-heretic-v2.json` and the readings in `docs/cards/`.

Rounds 13 and 14 add the eleventh and twelfth copies, both llmfan46's, both attention outputs only on the input
side. The 12B copy edits layers 24 to 39 (the card's range with its exclusive end) at weights 0.32 to 3.63, with
layer 37 at 0.32 and layer 35 at 3.63 beside each other, and rows moved by 0.0014 to 0.083 under no claim. The
Mistral Small 3.2 copy, the second on a Mistral base, edits eight attention outputs inside its declared layers 7 to
34 at weights 2.62 to 5.28 (layer 15 at 5.28, relative change 0.100, the largest searched weight on a Mistral base)
and leaves twenty in-range attention outputs as residues at 0.000097 to 0.000225 of their norm, more residues than
edits. Twelve copies, seven bases, all on the input side. Evidence:
`results/weights/llmfan46-gemma-4-12B-it-uncensored-heretic.json`,
`results/weights/llmfan46-Mistral-Small-3.2-24B-Instruct-2506-ultra-uncensored-heretic.json` and the readings in
`docs/cards/`.

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
`results/weights/TrevorJS-gemma-4-26B-A4B-it-uncensored.pass-2.json` and the readings in `docs/cards/`. Round 13
adds the fifth size, E2B (70 matrices, all 35 layers, both writers): rows within 0.00043, first share 0.988 to 0.996,
a median 0.03 and 0.11 kept along the leading output direction on the two writers, and the second term bending the
two edits of layer 3 apart to 0.943, with none of the other 34 layers below 0.95. One matrix in 70 passes the 0.0025
leftover line (layer 0's down projection, 0.0037). Evidence: `results/weights/TrevorJS-gemma-4-E2B-it-uncensored.json`.

## 25. A copy whose card names Google as its one parent carries a third party's fine-tune, and the normalisation vectors say whose

lemuralabs/Gemma-4-12B-uncensored-bf16 names google/gemma-4-12B-it in its card ("full-precision (bf16) abliterated
google/gemma-4-12B-it", a one-step lineage drawing, "no new capabilities were added") and in its `base_model` field.
Against that original 553 of 677 tensors changed. The reading-side, gate and up projections of every layer moved by
0.18 to 0.36 percent with first-value shares of 0.001 to 0.024, unrelated directions (cosine 0.00 to 0.42) and 0.99
to 1.01 of the original kept: training. The 229 normalisation vectors that moved (up to 8.6 percent) have difference
norms equal to the last digit to round 8's measurement of yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 under
richardyoung's ablation against the same Google file, as do the 110 that stayed under the threshold in both reports,
and the token embedding reads 5.3678e-5 in both; richardyoung's ablation leaves every one of those tensors at
exactly 0 against the fine-tune (finding 18), so the equality is with the fine-tune itself. On the projections the
fine-tune's change comes through at a quarter of its entries (0.13 to 0.34 of each matrix's entries differ from
Google's, against 0.89 to 0.97 on richardyoung's float16 copy): the fine-tune was saved in float16, this copy in
bfloat16, and the recast returns three entries in four to Google's value. The copy's configuration is Google's
(`max_position_embeddings` 131072 where the fine-tune declares 262144), so the files were assembled from two
repositories. On top of the fine-tune sits the maker's own ablation, a shared rank-one direction on the attention
outputs of layers 9 to 47 and the down projections of layers 21 to 47 (first share 0.94 to 0.99, cross-layer cosine
0.89 to 1.00), which agrees with richardyoung's directions at cosine 0.75 to 0.93 on the layers both edit and is
smaller than richardyoung's on every one of them, so it was made from the fine-tune and not from the other
maker's copy. After 3MPER0RR's (finding 8) this is the second copy whose weights carry a parent its card names
nowhere, and the first where the parent is identified from the census's own reports: a tensor set an ablation does
not touch, equal to the last digit between two reports on one original, names the fine-tune both copies stand on. A
comparison tool holding the reports can run that test on every new pair. Evidence:
`results/weights/lemuralabs-Gemma-4-12B-uncensored-bf16.json` against
`results/weights/richardyoung-gemma-4-12B-coder-fable5-composer2.5-v1-heretic.json`,
`results/meta/lemuralabs-Gemma-4-12B-uncensored-bf16.json` and
`docs/cards/lemuralabs--Gemma-4-12B-uncensored-bf16-b09ffb4f.reading.md`.

## 26. An "instruct uncensored" copy declared against the pretrained base, with the instruct model's template and 5 to 11 percent of dense change

Felldude/Ministral-3-8B-Uncensored is titled "Ministral 3 8B Instruct Uncensored" and calls itself a full fine-tune;
its `base_model` field names mistralai/Ministral-3-8B-Base-2512, the pretrained model. Against that base 243 of 531
tensors changed: the seven projections of all 34 layers at 5.0 to 11.0 percent of their norm, the token embedding
(6.4 percent, with rows that are zero in the base filled in), the output head (9.6 percent), the two linear maps of
the multimodal projector (7.7 and 8.1 percent) and one normalisation; the 218 tensors of the vision tower are
unchanged to 0.000005, the size of the copy's cast to float32. Nothing in the change is rank one or shared across
layers (first shares 0.001 to 0.070, cosines 0.03 to 0.61), so there is no ablation under it. The base has no chat
template and the copy carries one of 7,759 bytes equal to mistralai/Ministral-3-8B-Instruct-2512's byte for byte at
that repository's first three revisions, with `tie_word_embeddings` false, the instruct configuration's key. The
template is finding 8's marker on a second maker and a second family: the copy stands on the instruct model, or on a
model made from it, and the 5 to 11 percent against the base is Mistral's instruction tuning and the maker's training
together, in a proportion only a comparison against the instruct weights can give. The change is four to ten times
ccharnkij's adapter training on the Reasoning sibling (finding 17) and reaches the embedding, head and projector that
copy left alone. The copy's tokenizer was re-saved without its `added_tokens_decoder` block and
`special_tokens_map.json` (1,007 of the card's 1,011 flagged fields; ids and vocabulary unchanged), a re-save and not a
change. Evidence: `results/weights/Felldude-Ministral-3-8B-Uncensored.json`,
`results/meta/Felldude-Ministral-3-8B-Uncensored.json` and
`docs/cards/Felldude--Ministral-3-8B-Uncensored-ad52113f.reading.md`.

## 27. A per-layer ablation with two or three directions per matrix, and a reconstruction claim that reads as no change

aifeifei798/Heretic-Scalpel-E2B's card describes an ablation followed by a "singular value topology surgery" that
reconstructs the shared key-value projections of layers 15 to 34 and three rounds of fine-tuning. Against
google/gemma-4-E2B-it 179 of 2,011 tensors changed. The attention outputs of layers 10 to 34 and the down projections
of layers 15 to 34 carry the ablation: rank one in layers 10 to 13 and 15 to 18 (first share 0.98 to 0.997), two or
three directions from layer 14 on (first share 0.43 to 0.74 with the first eight at 0.997; singular values 2.33, 1.70
and 0.10 at layer 15, 2.28, 1.93 and 1.09 at layer 25, 2.49, 2.24 and 1.40 at layer 34), the directions per layer
(cross-layer cosine 0.03 to 0.71), output side (right above left on 42 of 45), no single weight (−0.38 to 0.67 kept
along the first direction, −0.37 to 0.04 along the second). The other 117 changed projections and the attention
outputs and down projections of the lower layers moved by 0.10 to 0.27 percent with 0.99 to 1.01 kept and unrelated
directions, the small merged change three rounds of fine-tuning leave. The 71 key and value projections and key
normalisations of layers 15 to 34, the tensors the card's first stage reconstructs, read a relative difference of
exactly 0: the published file carries Google's values bit for bit, and the key and value projections that did change
(9 and 15) are all in layers 0 to 14, where the model computes its own. This is the first ablation in the census
with more than one direction per matrix; the energy-share rule reads its second and third directions as 57
violations, and a rank per matrix would name it. The copy's files are one loader's save (no library version,
`torch_dtype` for `dtype`, the resolved per-layer head sizes written out, the end token repeated in the generation
list, the template written into the tokenizer configuration as well), finding 15's signature with no token moved.
Evidence: `results/weights/aifeifei798-Heretic-Scalpel-E2B.json`, `results/meta/aifeifei798-Heretic-Scalpel-E2B.json`
and `docs/cards/aifeifei798--Heretic-Scalpel-E2B-6632ade0.reading.md`.

## 28. A copy that carries the previous model's chat template, under another maker's card

venkycs/Mistral-Small-24B-Instruct-2501-Abliterated's card is huihui-ai's card for
huihui-ai/Mistral-Small-24B-Instruct-2501-abliterated, copied with its title, its method line and its ollama pull
command. The weights are that method's shape: 78 of 363 tensors changed, every attention output and down projection of
layers 1 to 39, one shared direction (cross-layer cosine 0.99999 or more) at weight 1.0 (−0.004 to −0.002 kept on the
left of all 78), rank one at the storage floor, nothing else moved. huihui-ai's own copy of this base is not measured,
so whether the two are one file cannot yet be said. The template is the result: the copy's `tokenizer_config.json`
carries a template of 3,959 bytes that matches none of the 2501 repository's 54 revisions and equals
mistralai/Mistral-Small-Instruct-2409's byte for byte, the previous model's, with the old `[INST] ... [/INST]`
spacing and the system message folded into the last user turn where the 2501 model was released with a
`[SYSTEM_PROMPT]` block and no spaces. The fixed conversation renders differently, so every conversation through this
copy is formatted as the earlier model's. The maker's tokenizer upload is dated 2025-03-12, two weeks after the
weights; the copy's five other token-side fields are Mistral's own revision of 41 minutes after the pin. After
Jiunsong's fixed system text (finding 16) and llmfan46's thought block (finding 23) this is the third template in the
census that changes what a conversation renders to, and the first by substitution of another model's file; a
template lookup across the originals the census has cached would have named it, as it would have named 3MPER0RR's
(finding 8) and Felldude's (finding 26). Evidence:
`results/weights/venkycs-Mistral-Small-24B-Instruct-2501-Abliterated.json`,
`results/meta/venkycs-Mistral-Small-24B-Instruct-2501-Abliterated.json` and
`docs/cards/venkycs--Mistral-Small-24B-Instruct-2501-Abliterated-c4890956.reading.md`.

## 29. An eight-direction subspace projection whose per-layer scale schedule reads from the weights to two decimals

null-space/gemma-4-31b-it-abliterated changes 80 of 1,188 tensors, the attention output and the down projection of
layers 20 to 59, and nothing else (1,108 tensors equal to the original, every small file byte-equal to Google's).
Its card gives the method in numbers: the top 8 of 32 SVD directions per layer projected out with norm preservation,
at a scale of 0.35 to 0.45 on layers 20 to 37 and two bells to 1.35 around layers 41 and 58. The weights carry each
number. The first-value energy share is 0.58 to 0.69 and the first eight directions 0.94 to 0.996 of every change,
the first singular value 1.7 to 2.8 times the second: eight directions, the leading one carrying two thirds. One
minus the fraction kept along the leading direction is 0.35 on layers 20 to 26, 0.40 on 27 and 28, 0.35 on 29 to 35,
0.40, 0.45, 0.55, 0.65 on 36 to 39, 1.10, 1.35, 1.10 on 40 to 42, 0.70 falling to 0.40 on 43 to 51, then 0.60, 1.15,
1.00, 1.00, 1.00, 1.25, 1.35, 1.15 on 52 to 59, on both writers of every layer to the second decimal. The leading
directions form two sets: layers 20 to 51 share one at cosine 1.000 and layers 52 to 59 another at 0.18 to the first,
so what was applied to each block is the subspace measured at its peak layer. The preservation claim reads in two
bands: rows moved by 0.025 to 0.098 on layers 20 to 51 and by 0.002 to 0.006 on 52 to 58. The card's own key-value
comparison calls layers 0 to 20 unmodified while layer 20 is edited at 0.006 of its norm. After aifeifei798's two-
and three-direction copy (finding 27) this is the second multi-direction edit and the first whose rank and scale are
stated and read back; the energy-share rule reports it as 80 failed projections, and a first-k share would report it
as one number per matrix. Evidence: `results/weights/null-space-gemma-4-31b-it-abliterated.json`,
`results/meta/null-space-gemma-4-31b-it-abliterated.json` and
`docs/cards/null-space--gemma-4-31b-it-abliterated-a429e3fe.reading.md`.

## 30. A mixture edit that reaches the experts and scales thirteen embedding rows to one sixth

WWTCyberLab/gemma-4-26B-A4B-it-abliterated changes 55 of 1,013 tensors: the attention output, the shared down
projection and the packed expert down tensor of each of layers 9 to 26, and the token embedding; the 30 gate-up
tensors, the 90 routers and everything else read exactly 0. The layer edits are rank one in eight layers (first
share 0.982 to 0.997) and rank two in ten (0.50 to 0.96 with the first eight at 0.99, the first singular value 1.1 to
5.0 times the second), the shape two passes on one layer leave; the card describes two passes, the first on layers
16, 18 and 19 and the second on ten re-measured layers, which are among the ten two-direction layers here, and
names 13 layer passes where the weights carry 18 layers. In every edited layer all 128 experts' down projections
changed (0.015 to 0.048 per expert) and share the leading output direction at median cosine 0.98 to 1.00, with the
median expert's first share splitting as the dense writers do (0.990 to 0.996 against 0.56 to 0.68). The kept
fraction along the leading direction is −0.13 to 0.17 on every layer matrix and on the median expert, a weight near
1, where the card's scales are 4.0 and 3.0. The embedding is the card's third stage read exactly: 13 rows, whose
tokens are "While", "Please", "It", "That", "I", "As", "Sorry", "However", "Creating", "*(", "Modern", "*" and
"***", scaled to 0.16666 of their length (the card's "strength 5", a division by six), with eight near-equal singular
values and a largest row-norm change of 0.833. Seven measurements of six makers' copies now stand on this base's one
weight file, and this is the second to reach an expert (finding 20); unlike TrevorJS's one direction per layer on
every expert of all 30 layers (finding 13), it carries one or two per layer on 18, and no field of its report equals
any of the six others. A tool that edits linear modules reaches the packed experts when it is written to, so the
layout argument of finding 20 says where a method stopped and not where it could reach. Evidence:
`results/weights/WWTCyberLab-gemma-4-26B-A4B-it-abliterated.json` and
`docs/cards/WWTCyberLab--gemma-4-26B-A4B-it-abliterated-89c6759c.reading.md`.

## 31. Two heretics of one reasoning model, both standing on a third party's conversion of an original that ships no library tokenizer

mistralai/Magistral-Small-2509 ships its tokenizer as `tekken.json` with `params.json`, a configuration and a system
prompt, and no `tokenizer.json`, tokenizer configuration, special-tokens map or chat template. Its two copies in the
census, llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v2 and grayarea/Magistral-Small-2509-Heretic-v1.2,
both ship those four files, and both took them from unsloth/Magistral-Small-2509: grayarea's `tokenizer.json` and
`chat_template.jinja` equal that repository's files at its 2025-09-29 revision byte for byte, llmfan46's template is
the same file with 104 carriage returns added and its tokenizer and configuration are a transformers 5.3.0 re-save
of the same conversion (`rope_parameters` for `rope_theta`, `tie_word_embeddings` written at two levels), and both
carry the conversion's `unsloth_fixed`, its three token ids in the configuration, and the original's
`SYSTEM_PROMPT.txt` as it stood before its 2025-12-02 revision. The metadata tool reports 1,033 and 2,027 differing
fields (the 1,000 special tokens listed once or twice, the ids, the vocabulary size, the configuration fields and the
template) and marks the four files missing on the original's side; none of the fields is a change the original can
be compared on, and the two templates render the fixed conversation to the same string. On the weights the two
copies are two Heretic configurations and share no equal field in the 288 of their 48 common matrices: llmfan46's is
the arbitrary-rank method on 49 matrices (26 down projections, 23 attention outputs), input side, searched weights
1.69 to 4.71, seven in-range matrices rewritten under the threshold (finding 22); grayarea's is one shared direction
on 64 (34 attention outputs of layers 6 to 39, 30 down projections of 10 to 39), output side, weight 1.24 to 1.35 on
the attention outputs and a kernel of 0.51 to 1.39 to 1.13 on the down projections, with rows moved by 0.0026 to
0.0107 under a card that claims "full row renormalization" (the second restoration claim to read as a leftover,
after coder3101's 0.007 of finding 22), and a `grayarea` block in its configuration naming its Heretic configuration
and dataset. The token-side rule the census needs is a lookup of the copy's tokenizer files against the conversions
it has cached when the original ships none, naming the repository and revision; and the conversion itself,
unsloth/Magistral-Small-2509 against the original, is one measurement that would let every later copy on it be read
against a measured intermediate. Evidence:
`results/weights/llmfan46-Magistral-Small-2509-ultra-uncensored-heretic-v2.json`,
`results/weights/grayarea-Magistral-Small-2509-Heretic-v1.2.json`, the two `results/meta/` reports of the same names
and the readings in `docs/cards/`.

Rounds 13 and 14 add a second such original and the lookup succeeds by checksum. mistralai/Mistral-Small-3.2-24B-
Instruct-2506 ships `tekken.json` and no library tokenizer at either pinned revision. huihui-ai's copy carries
unsloth/Mistral-Small-3.2-24B-Instruct-2506's tokenizer configuration, special-tokens map and template byte for
byte at that repository's revisions `42cd5fdb`, `ff984dcd` and `776efdbd` of 2025-06-20 to 06-23, and no
`tokenizer.json`; llmfan46's carries the same special-tokens map, unsloth's template of 2025-08-26 (`3ed8d341`)
after the removal of 299 carriage returns, a 17 MB `tokenizer.json` and a 5.3.0 re-save of the configuration with
`unsloth_fixed`. Both carry the conversion's seven generation fields in place of the original's two (finding 32).
The 1,025 fields each report are the conversion's token table and none is a change the original can be compared on.
Evidence: `results/meta/huihui-ai-Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated.json`,
`results/meta/llmfan46-Mistral-Small-3.2-24B-Instruct-2506-ultra-uncensored-heretic.json` and the readings in
`docs/cards/`.

## 32. An original whose generation settings were invalid JSON for seventeen days, and what every copy and every strict reader did with it

mistralai/Mistral-Small-3.2-24B-Instruct-2506 shipped a `generation_config.json` of 135 bytes with a trailing comma
after `"temperature": 0.15` from its release commit of 2025-06-20 until commit `46a27874` of 2025-07-07 ("fix
invalid json file (#18)"), seventeen days in which the file was not JSON. The revision the census pinned for
huihui-ai's copy (`1483f238`, 2025-06-27) is inside that window, and the cluster's metadata step stopped on it
(round 13, compare 3400584), so the token side was built at home. Under transformers 5.6.2 a strict load of that
revision's generation settings raises an error ("not a valid JSON file") and the model loader falls back to settings
built from the model configuration, with a note in the log and the temperature of 0.15 gone; a runtime that reads
the file directly fails outright. Neither copy of the original in the census carries the file: huihui-ai's (made
2025-07-02, inside the window) and llmfan46's (2026-03-19) both carry the seven fields of unsloth's conversion
(beginning, end and padding tokens, sampling on, a maximum length of 131,072, temperature 0.15, version 4.52.4),
written by the loader that re-saved the model, so the copies have a temperature the pinned original cannot load,
and a comparison of generation settings reads seven fields against two. The conversion itself carried the invalid
file at its first revision (`993fccfc`, 2025-06-20 20:34Z) and replaced it within two hours. Mistral's later revision
`95a6d26c` of 2025-12-22 ("Fix generation config saving error") adds `do_sample` to the fixed file. What the census
takes from it: a lenient read with the fault named (`hpc/rounds/2/measure.py read_document`, commit 6a08e37); a
record of the original's generation file at every revision in the pin window, because the file a copy's maker
loaded may not be the file the pin serves; and a note that a copy's generation settings on a Mistral base are the
conversion's unless the copy ships the original's two-field file. Evidence:
`results/meta/huihui-ai-Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated.json` (the `home_measurement` note
and the configuration fields), `results/meta/llmfan46-Mistral-Small-3.2-24B-Instruct-2506-ultra-uncensored-heretic.json`,
`docs/cards/huihui-ai--Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-d9f80c54.reading.md`,
`docs/census-round-13.md` and the cluster log `blueback13/logs/3400584.out` in the pull copy.

## 33. A published copy that is four whole checkpoints under one name, with every tensor name repeated

DarkRomeo88/gemma-4-12b-it-heretic-comfyui names google/gemma-4-12B-it and llmfan46/gemma-4-12B-it-uncensored-heretic
as its two `base_model` entries and ships four `safetensors` files of 12.7, 13.1, 8.3 and 9.7 GB with no index and
no configuration: a float8-scaled, an int8 (with a rotation), a w4a8 and a w6a8 quantisation of llmfan46's copy
(round 13 pair 8), each a whole model for a ComfyUI text-encoder folder, uploaded between 2026-08-22 and 10-05. The
safetensors headers, read at home by HTTP range (never a whole shard), list 1,162, 1,334, 1,990 and 1,664 tensors,
6,150 names of which 2,322 are distinct: 918 names appear in all four files, and `audio_projector.embedding_
projection.weight` is a bfloat16 tensor of shape 3,840 by 640 in each, at data offsets 968, 8,962,048, 8,983,040 and
10,010,624. The two later files' metadata names llmfan46's copy as `source` and ComfyUI as `converted_for`; each file
carries a `tokenizer_json` tensor, nine to eleven vision tensors and no audio tower. The census's loader takes every
`*.safetensors` in a repository as the shards of one checkpoint and stopped at the first repeated name (round 14,
compare 3401156, `duplicate tensor name`), after the download had verified every published checksum. The
repository is not an edit of Google's model and cannot be compared with it; it is four re-quantisations of a copy
the census has measured, under a card that names the grandparent first. Two rules follow: a repository with several
weight files and no index is several checkpoints until shown otherwise (count the files, report the repeated names
with their offsets, pair each file on its own), and a card with two `base_model` entries names the nearer one as the
original to compare against. Evidence: the header listing in `docs/census-round-14.md`, the cluster log
`blueback14/logs/3401156.out` in the pull copy, and `data/batches/round-14-batch-1.json`.

## 34. A rank-four subspace projection reads exactly, and four other makers' directions lie partly inside it

AEON-7/Gemma-4-12B-it-AEON-Abliterated-K4-BF16's card states a "K=4 multi-direction biprojection": four refusal
directions measured at layers 24, 37, 39 and 26, orthonormalised, projected out of both residual writers of the top
half of the layers by refusal score, which it lists as layers 21 to 42, 44 and 45. The weights carry every number.
48 of 677 tensors changed, the attention output and down projection of exactly those 24 layers (43 skipped on both
sides); each change has four near-equal singular values and then a drop of 19 to 195 times, the first four carrying
0.9961 to 0.9970 of the energy; the 48 leading left vectors span one four-dimensional subspace (stacked singular
values 4.50, 3.65, 2.95, 2.34, then 0.24; 99.4 percent in four), and 0.984 to 1.000 of each matrix's leading vector
lies inside it; the left kept fraction is below the right on 47 of 48 (output side) and the rows moved by at most
0.00033 under the card's norm preservation. The two scoring rules written for one direction count it as 90 flags
(48 first shares of 0.26 to 0.32 and 42 within-layer cosines), the second rank-stated subspace edit in the census
after null-space's eight-direction 31B copy (finding 29) and the clearest case for a first-k share with k read from
the singular-value gap. The subspace is not the maker's alone: the leading output-side vectors of the other 12B
copies on this weight file lie partly inside it, igorls 0.60 to 0.61, huihui-ai 0.56 to 0.79, 3MPER0RR 0.37 to 0.47,
richardyoung 0.34 to 0.49, where the input-side copies do not (llmfan46 about 0.1, coder3101 about 0.07); four makers'
single directions, measured on four prompt sets, share a part of one four-dimensional refusal subspace of this
model, and no changed matrix of any of them has an equal measurement in any field. Evidence:
`results/weights/AEON-7-Gemma-4-12B-it-AEON-Abliterated-K4-BF16.json`, the subspace numbers in
`docs/cards/AEON-7--Gemma-4-12B-it-AEON-Abliterated-K4-BF16-5fdf67da.reading.md`, the direction file in the pull
copy (`blueback13/measurements/pair-3/weights.directions.safetensors`) and the six other 12B reports in
`results/weights/`.

## 35. A weight of 0.3 read on every matrix, on a base the card says was already compliant

DuoNeural/Mistral-NeMo-12B-Abliterated's card gives an orthogonal rank-1 projection on `down_proj` and `o_proj` of
all 40 layers at α 0.3, a direction from 10 harmful and 10 harmless prompts, and a research note that the base
answered 6 of 6 harmful probes before any weight changed. The weights read α to the second decimal: the copy keeps
0.703 to 0.708 of the original's action along one shared direction (cross-layer cosine 0.9996 to 1.000) on all 80
matrices, a weight of 0.29 to 0.30, output side on 80 of 80, rows moved 0.003 to 0.007, nothing outside the 80 and
283 tensors equal to the original. It is the first copy in the census whose shared weight is below one half on
every matrix (the per-layer kernels of finding 10 dip to 0.49 and 0.05 on single layers, and the arbitrary-rank
searches to 0.32 to 0.51), and its 80 flags are all the storage floor of finding 3 on an edit of 0.0042 to 0.0058 of each norm.
A weight of 0.3 against a direction the maker's own probes say the base does not refuse along is a change of three
tenths of a direction the card itself calls inert; what the weights certify is that the card's number is the
number applied. Evidence: `results/weights/DuoNeural-Mistral-NeMo-12B-Abliterated.json` and
`docs/cards/DuoNeural--Mistral-NeMo-12B-Abliterated-b8205ddb.reading.md`.

## 36. Three block directions under a three-sentence card, and a norm-preserving name without the restoration

grimjim/mistralai-Mistral-Nemo-Instruct-2407-extensive-BP-abliteration-12B's card says biprojected abliteration on
"the majority of layers", "grounded in three particular layer measurements", "abliterated to excess", and nothing
else. The weights say: both residual writers of layers 3 to 37 (70 of 363 tensors), one direction per matrix at the
floor, three directions shared by block, layers 3 to 16 (28 matrices, within-block cosine 0.9993), 17 to 21 (10) and
22 to 37 (32), at cosine 0.68 to 0.89 between blocks, weight 1.0 on every matrix (−0.003 to 0.005 kept), output side on
70 of 70, and a few bfloat16 values moved in three matrices the method does not name (layer 0's gate projection at
0.000096, layer 39's key and down projections). The maker is the author of the norm-preserving biprojection whose
restoration holds within 0.0005 on the five TrevorJS copies and within 0.0004 on AEON-7's, all made with the
published scripts; this copy's rows moved by 0.004 to 0.032, the leftover of a projection with no restoration step.
Whether the "BP" in the name is the biprojection without its norm step or an earlier form of it, the card does not
say, and the weights read the difference: three directions, one weight, no restoration. Evidence:
`results/weights/grimjim-mistralai-Mistral-Nemo-Instruct-2407-extensive-BP-abliteration-12B.json` and
`docs/cards/grimjim--mistralai-Mistral-Nemo-Instruct-2407-extensive-BP-abliteration-12B-0c30f0e3.reading.md`.

## 37. A float8 original compared raw reads 280 rewritten matrices and 921 flags, and the pair is still unmeasured

timfromhcs/Ministral-3-14B-abliterated is bfloat16; mistralai/Ministral-3-14B-Instruct-2512 is published in
`float8_e4m3fn` with a `quantization_config` and 560 scale tensors (`weight_scale_inv`, `activation_scale`) the copy
does not have. Round 14 compared them as they are: 280 of 585 matched matrices read as changed at relative change
0.999, first shares of 0.001 to 0.2, 921 flags, "recipe violations" on the cluster and at home, every number a
measurement of eight-bit codes against sixteen-bit values and none of the edit. The copy is one commit, a
"Duplicate from jenerallee78/Ministral-3-14B-abliterated" of 2025-12-05, which names grimjim's norm-preserving
biprojection; its template is the original's 2025-12 file (7,754 bytes against 7,760, line endings apart) where the
pin of 2026-07-15 carries an 11,913-byte one, so the copy also stands on an earlier revision of the original than
the pin rule chose. Finding 7 listed this pair as unpinnable on 2026-10-29; the pinner admitted it on 10-30. What the
pair needs is the original dequantised once at home (560 scales applied, saved in bfloat16, checksummed) and the
comparison run against that, for this copy and for its source. Evidence:
`results/weights/timfromhcs-Ministral-3-14B-abliterated.json` (the `original_only` list and the 280 matrices),
`results/meta/timfromhcs-Ministral-3-14B-abliterated.json` and
`docs/cards/timfromhcs--Ministral-3-14B-abliterated-c9f55a6b.reading.md`.

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
- Population. Fifty-six copies is a sample; the inventory sample of 30 repositories
  (`docs/inventory-sample.md`) shows how mirrors and re-quantizations outnumber sources and how often the stated
  original cannot be resolved (16 of 30).

Weight differences alone cannot certify the absence of hidden behavior.
