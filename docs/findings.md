# Findings so far

Created by Sean Egan, 2026-10-29.

The results the audit has established so far, strongest first, each with its evidence in this repository. The
population is small: one hundred and seventy-five measurements of one hundred and sixty-eight distinct published copies on thirty-three originals (twenty-nine
copies are re-uploads of others, six of them the only measurement of their parent, and three more name an unmeasured copy as their parent, five copies are measured against
two originals each (three of them measured again in round 35 against the parent their cards name, which adds a measurement and no copy), one is measured twice against one original, one could not be paired tensor by tensor, and one could not be read because its original is
published in float8), plus two edits of my own made to calibrate the measurement. Numbers are from the committed reports in `results/weights/` and `results/meta/`.

## 1. One hundred and thirty of the one hundred and thirty-eight published copies measured so far are what their cards say they are

Eighty-five community copies of open-weight models, five from one maker on Qwen bases, five from five makers on
Gemma and Mistral bases (round 2), seven from six makers on Gemma 4 and Mistral 7B bases (round 7), seven from six
makers on Gemma 4 and Ministral 3 bases (round 8), six from four makers on the two larger Gemma 4 bases (round 12),
five from five makers on Gemma 4, Ministral 3 and Mistral Small bases (round 16), six from six makers on Gemma 4
and Magistral Small bases (round 18), eight from seven makers on Gemma 4, Mistral Nemo and Mistral Small bases
(round 13), one more on Mistral Small (round 14), four from four makers on the three larger Gemma 4 bases
(round 19), five from five makers on Gemma 4 E4B, Ministral 3 and DiffusionGemma bases (round 30, one of them
through a re-upload of the maker's file), five from five makers on two Gemma 4 bases and two Mistral bases (round
20), eight from eight makers on Gemma 4 bases, three of them the QAT-unquantized checkpoints (round 32), five from
five makers on Gemma 4 bases (round 22, beside two hub duplicates and a repeat) and eight from five makers on Gemma 4
E2B and E4B bases (round 25), four from three makers on Gemma 4 and Mistral 7B bases (round 26, beside four hub duplicates) and
five from five makers on Gemma 4, Mistral Small and Voxtral bases (round 29, beside three hub duplicates) and three
from three makers on Gemma 4 12B, E4B and 31B bases (round 31, beside a re-upload of an unmeasured edit) and eight
from seven makers on Gemma 4 31B, 12B, E4B and E2B bases and the 12B QAT checkpoint (round 33) and seven from seven
makers on the QAT-unquantized checkpoints of the 26B-A4B, 12B and E4B and the DiffusionGemma base (round 34, beside a
hub duplicate of an unmeasured edit) and three from three makers on Gemma 4 31B and E4B bases and the E4B QAT
checkpoint (round 35, beside two re-uploads of unmeasured edits and second measurements of three copies against
the parents their cards name) and eight from six makers on Gemma 4 31B and E4B bases and the QAT-unquantized
checkpoints of the 12B, 26B-A4B and 31B (round 37) and eight from five makers on the three QAT-unquantized
checkpoints (round 36, measured before round 37 and read after it) and seven from five makers on Gemma 4
26B-A4B, E4B, 12B and E2B bases (round 38, beside a hub duplicate of an unmeasured edit), have
been compared tensor by tensor with their stated originals. In one hundred and thirty, the changed tensors are exactly the matrices the stated method reaches, and nothing else
moved: the largest relative change outside the changed set is 0 in one hundred and seven copies, 0.00008, 0.000006, 0.00024,
0.00031, 0.000096, 0.000225, 0.000999, 0.00095, 0.00029, 0.000767, 0.00096, 0.000251, 0.00038, 0.00098, 0.00091, 0.000195, 0.000898, 0.000086 and 0.000673 in nineteen others on matrices the method itself weighted near zero or did not name,
0.0000011 in the jokernifty E4B copy and in Ilya626's, whose float16 saves round the smallest values of untouched tensors,
0.00099 in the richardyoung Gemma 4 12B coder copy, whose fine-tune left 61 normalisation vectors just under the
threshold, 0.000998 in the aifeifei798 E2B copy, whose fine-tuning sits at the threshold on 26 tensors, and 0.000998
in the Dingdust E4B copy, whose parent fine-tune sits at the threshold on 189 tensors.
One hundred and twenty-eight of the one hundred and thirty are ablations (one, aifeifei798's, with 0.1 to 0.3 percent of training beside it,
and one, DavidAU's E2B copy, with a fine-tune laid over it, as their cards say; one, sh0ck0r's Artemis copy, is
measured against the grandparent its `base_model` field names and reads its named parent's 4-bit round trip under
the edit, finding 45, and measured again against that parent in round 35 reads the edit alone, finding 77; one, Dingdust's ContextPilot copy, is measured against the grandparent its field names and
reads the fine-tune of the parent its README's second card names under the edit, finding 54; one, Pranavz's Hearthfire
copy, is measured against the grandparent its field names and reads the fine-tune its README's title names under the
kernels, finding 61, and against that parent reads the kernels alone, finding 77; one, AlekseyCalvin's translation copy, is measured against the grandparent its field names and
reads igorls's 12B Heretic edit under the training, the parent placed from the saved direction vectors, finding 66); two
(ccharnkij/Ministral-3-8B-Reasoning-2512-Uncensored and richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic)
are training, as their cards say, findings 17 and 18. The eight others carry a parent or a change their cards do not name:
3MPER0RR/Mistral-7B-v0.3-3MPER0RR-abliterated changes every matrix in the model (finding 8),
lemuralabs/Gemma-4-12B-uncensored-bf16 carries a third party's coding fine-tune under its ablation (finding 25), and
Felldude/Ministral-3-8B-Uncensored carries the instruct model's template and 5 to 11 percent of dense change against
the pretrained base it names (finding 26), and Felldude/gemma-4-E4B-uncensored does the same on Gemma 4, its norms
byte-equal to the instruct model's, against the pretrained base it names (finding 62; against the instruct model, in round 35, it is a fine-tune of 0.1 to 0.7 percent on
two bands of layers, finding 78), and Ilya626/gemma-4-E4B-it-SDFT_Heretic_RP
replaces the 232 linear maps of its audio and vision towers with random matrices under a card that says nothing of the
towers (finding 63), and Kooten/gemma-4-31b-abliterated-v1.1 replaces the 189 linear maps of its vision tower with random
matrices under a card that says "Uncensored using Heretic" and nothing of the tower (finding 79), and
NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8-attn edits eleven down projections under a card that says the attention outputs
were its one target, the tool's branch having applied the ablation to both writers (finding 87), and
DuoNeural/gemma-4-26B-A4B-it-abliterated carries TrevorJS's 26B-A4B edit, its saved directions at 1.000 to his on all 90
matrices and its tensors within 0.0006 of his by byte range, under a card that names a per-expert method of the maker's
own (finding 95). The measurements beyond one hundred and thirty-eight: four hub duplicates measured in round 19, Iambackup's and Justbackup's copies
of TrevorJS's 12B edit, MeFFyLe's of llmfan46's 12B edit and nicoboss's of huihui-ai's Mistral Small 3.2 edit, each
equal to its parent's report in every field (finding 38); three more in round 30, sitten1's and erunda337's copies
of TrevorJS's 26B-A4B edit, equal to its second pass in every field but the sketch's last digits, and nnnxnsn's
of edwixx's DiffusionGemma edit, equal to FredyRivera-dev's upload of the same file in every field (finding 38); three more in round 20:
Ishowbackup's duplicates of TrevorJS's 12B edit and of huihui-ai's 12B edit, and prithivMLmods's re-save of
huihui-ai's 26B-A4B edit under the name Heretic-Stable, each equal to its parent's report in every field (finding 9); prithivMLmods's four Uncensored-MAX
copies name huihui-ai copies as their parents, all four measured as the huihui-ai E4B, 26B-A4B, E2B and 31B edits
field for field, the 31B parent (the first version) measured in round 22 (finding 9); two more hub duplicates in
round 22, laladream's copy of TrevorJS's 12B edit and lessans's of TrevorJS's E2B edit, each equal to its parent's
report in every field (finding 38); four more in round 26, Pound1320's, Cup4's and Cup5's copies of llmfan46's E4B
edit through a chain of two duplicates and Ishowbackup's of TrevorJS's E2B edit, and three in round 29, akpsahan's of
huihui-ai's second 31B version, claymorecrystal's of TrevorJS's 26B-A4B edit and senjiangchen's of TrevorJS's E4B
edit, each equal to its parent's report in every field (findings 38 and 56); nguyenthilaitrieulong's duplicate of
WWTCyberLab's unmeasured 31B edit in round 31, measured as that edit (finding 64); eadx's duplicate of huihui-ai's unmeasured
QAT 26B-A4B edit in round 34, whose parent repository the hub no longer serves, measured as that edit (finding 73); Dzluck's re-upload of huihui-ai's unmeasured E2B second version and enkato64bit's duplicate of
Jiunsong's unmeasured SuperGemma 12B edit in round 35, each measured as that edit (findings 80 and 81); Himanshuoo8's duplicate of DavidAU's unmeasured E4B fine-tune over coder3101's edit in round 38, measured as that edit (finding 97); the huihui-ai E2B edit measured a second time in round 22, equal to its round 13
report to the last digit (finding 50); TimelessSoul/Huihui-gemma-4-12B-it-abliterated is
huihui-ai's 12B file under another name, shard checksum and every field equal (finding 9);
Jiunsong/supergemma4-e4b-abliterated paired no tensor with its original (finding 14);
timfromhcs/Ministral-3-14B-abliterated was compared against an original published in float8 and read nothing but
the quantisation (findings 7 and 37); the richardyoung coder copy is measured twice, against its grandparent and
against its parent (finding 18); 3MPER0RR's Mistral 7B copy is measured twice, against the pretrained base its
card names and against the instruct model its weights point to (finding 8); and three copies first measured against a grandparent
were measured again in round 35 against the parent their cards name, sh0ck0r's Artemis copy and Pranavz's Hearthfire copy (finding 77)
and Felldude's E4B copy (finding 78).

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
| prithivMLmods/gemma-4-31B-it-Uncensored-MAX | google/gemma-4-31B-it | the same 120 as the huihui-ai first version, re-saved in ten shards, every field equal (round 22) | 0 |
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

| MoonRide/gemma-4-31B-it-heretic-ara-custom | google/gemma-4-31B-it | 48 of 1,188 (the attention outputs of layers 30 to 56 and 21 down projections of 32 to 56, the declared range; 4 of them rounding residues, 6 more under the threshold) | 0.000999 |
| 3MPER0RR/gemma-4-31b-it-3MPER0RR-abliterated | google/gemma-4-31B-it | 41 of 1,188 (the down projections of layers 39 to 59 and the attention outputs of 40 to 59; the card names nothing) | 0 |
| SevenOfNine/Gemma-4-26B-A4B-It-Abliterated | google/gemma-4-26B-A4B-it | 40 of 1,013 (the attention outputs of layers 4 to 29 and the shared down projections of 16 to 29; no expert) | 0 |
| prithivMLmods/gemma-4-12B-it-heretic_decensored | google/gemma-4-12B-it | 56 of 677 (the attention outputs of layers 15 to 47 and the down projections of 25 to 47, one shared direction) | 0 |
| Iambackup/gemma-4-12B-it-uncensored | google/gemma-4-12B-it | the same 66 as the TrevorJS copy, weight-file checksum and every field equal | 0 |
| Justbackup/gemma-4-12B-it-uncensored | google/gemma-4-12B-it | the same 66 as the TrevorJS copy, weight-file checksum and every field equal | 0 |
| MeFFyLe/gemma-4-12B-it-uncensored-heretic | google/gemma-4-12B-it | the same 16 as the llmfan46 copy, weight-file checksum and every field equal | 0 |
| nicoboss/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-llamacppfixed | mistralai/Mistral-Small-3.2-24B-Instruct-2506 | the same 80 as the huihui-ai copy, ten shard checksums and every field equal; the token files repaired | 0 |
| OS-Software/gemma-4-E4B-it-uncensored-heretic | google/gemma-4-E4B-it | 20 of 2,076 (the attention outputs and down projections of layers 18 to 27, the card's window; rank four exactly) | 0 |
| TheUmbraWalker/gemma-4-E4B-it-2-heretic | google/gemma-4-E4B-it | 73 of 2,076 (the attention outputs of layers 4 to 41 and the down projections of 7 to 41, the reach of the first card's kernels; two directions where the second card's overlap) | 0 |
| AISafety-Student/Ministral-3-8B-Reasoning-2512-heretic | mistralai/Ministral-3-8B-Reasoning-2512 | 45 of 531 (the down projections of layers 8 to 33 and the attention outputs of 15 to 33, the card's kernels to the layer and the weight) | 0 |
| Goodoldjam/DiffusionGemma-26B-E38-Abliterated-BF16 | google/diffusiongemma-26B-A4B-it | 20 of 1,047 (the attention outputs and down projections of layers 7 to 16, the card's 20; five at the floor) | 0 |
| FredyRivera-dev/diffusiongemma-26B-A4B-it-HERETIC-Uncensored (edwixx's file) | google/diffusiongemma-26B-A4B-it | 67 of 1,047 (the attention outputs of layers 5 to 29, the down projections of 7 to 29 and all 128 experts of 11 to 29; 20 at the floor) | 0.00095 |
| sitten1/gemma-4-26B-A4B-it-uncensored | google/gemma-4-26B-A4B-it | the same 90 as the TrevorJS copy, two shard checksums and every field equal | 0 |
| erunda337/gemma-4-26B-A4B-it-uncensored | google/gemma-4-26B-A4B-it | the same 90 as the TrevorJS copy, two shard checksums and every field equal | 0 |
| nnnxnsn/diffusiongemma-26B-A4B-it-HERETIC-Uncensored | google/diffusiongemma-26B-A4B-it | the same 67 as the FredyRivera-dev upload, eleven shard checksums and every field equal | 0.00095 |
| ressl/gemma-4-31B-it-uncensored | google/gemma-4-31B-it | 120 of 1,188 (every attention output and down projection, TrevorJS's reach on a new file; the card names no method) | 0 |
| sh0ck0r/Artemis-31B-v1.1-heretic | google/gemma-4-31B-it (the grandparent; the README names TheDrummer/Artemis-31B-v1.1) | 603 of 1,188 (every matrix: the named parent's 4-bit round trip, with the Heretic kernels readable on about 65 of them) | 0 |
| Ishowbackup/gemma-4-12B-it-uncensored | google/gemma-4-12B-it | the same 66 as the TrevorJS copy, weight-file checksum and every field equal | 0 |
| Ishowbackup/Huihui-gemma-4-12B-it-abliterated | google/gemma-4-12B-it | the same 12 as the huihui-ai copy, weight-file checksum and every field equal | 0 |
| MoonRide/gemma-4-12B-it-heretic | google/gemma-4-12B-it | 52 of 677 (the attention outputs of layers 17 to 47 and the down projections of 27 to 47, the card's kernels to the layer, one shared direction) | 0 |
| prithivMLmods/gemma-4-26B-A4B-Heretic-Stable | google/gemma-4-26B-A4B-it | the same 50 as the huihui-ai copy, re-saved in five shards, every field equal | 0 |
| llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v1 | mistralai/Magistral-Small-2509 | 18 of 585 (the attention outputs of layers 16 to 22 and the down projections of 16 to 26, the declared range; four in-range attention outputs rewritten near zero) | 0.00029 |
| DogOnKeyboard/Mistral-7B-Heretic | mistralai/Mistral-7B-Instruct-v0.3 | 45 of 291 (the attention outputs of layers 12 to 31 and the down projections of 7 to 31, the card's kernels to the layer and the weight) | 0 |
| sh0ck0r/gemma-4-26B-A4B-it-heretic | google/gemma-4-26B-A4B-it | 38 of 1,013 (the attention outputs of layers 9 to 29 and the shared down projections of 13 to 29, the card's kernels to the layer; no expert) | 0 |
| BinxNet/gemma-4-26B-A4B-it-heretic | google/gemma-4-26B-A4B-it | 44 of 1,013 (the attention outputs of layers 5 to 29 and the shared down projections of 11 to 29, the card's kernels to the layer; no expert) | 0 |
| DavidAU/gemma-4-E2B-it-The-DECKARD-HERETIC-UNCENSORED-Thinking | google/gemma-4-E2B-it | 205 of 2,011 (every projection of every layer: a fine-tune over an ablation readable on the attention outputs of layers 16 to 31, "uncensored, then fine tuned" as the card says) | 0 |
| huihui-ai/Huihui-gemma-4-12B-it-qat-q4_0-unquantized-abliterated | google/gemma-4-12B-it-qat-q4_0-unquantized | 28 of 677 (the attention output and down projection of layers 23 to 36, the card's range) | 0 |
| mewse/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ara | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | 24 of 1,013 (the attention outputs and shared down projections of layers 11 to 22, the declared range; no expert) | 0 |
| coder3101/gemma-4-E2B-it-qat-q4_0-unquantized-heretic | google/gemma-4-E2B-it-qat-q4_0-unquantized | 17 of 1,951 (attention outputs inside the declared layers 6 to 24; 8 of them rounding residues, one more under the threshold) | 0.000767 |
| amkkk/Gemma4_E2B_Abliterated_Baked_HF_Ready | google/gemma-4-E2B-it | 96 of 1,951 (the attention output, down, gate and up projections of the 24 layers the configuration lists; the 60 unused shared-KV tensors dropped) | 0 |
| OS-Software/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic-v2 | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | 16 of 1,013 (the attention outputs and shared down projections of layers 12 to 19, the card's window; rank four exactly; no expert) | 0 |
| huihui-ai/Huihui-gemma-4-31B-it-abliterated | google/gemma-4-31B-it | 120 of 1,188 (every attention output and down projection, the first version at weight 1.00; equal in every field to the prithivMLmods re-upload) | 0 |
| huihui-ai/Huihui-gemma-4-E2B-it-abliterated (second pass) | google/gemma-4-E2B-it | the same 50 as round 13, every field equal to the last digit | 0 |
| RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals9 | google/gemma-4-12B-it | 55 of 677 (34 edits and 21 rounding residues on both writers of layers 14 to 43, the card's window; 5 more under the threshold) | 0.00096 |
| Vampelium/gemma-4-12B-it-heretic | google/gemma-4-12B-it | 75 of 677 (the attention outputs of layers 5 to 47 and the down projections of 16 to 47, a kernel pair the card does not print) | 0 |
| laladream/gemma-4-12B-it-uncensored | google/gemma-4-12B-it | the same 66 as the TrevorJS copy, weight-file checksum and every field equal | 0 |
| Carlosian/Gemma-4-12b-it-Abliterated | google/gemma-4-12B-it | 42 of 677 (the attention output and down projection of layers 14 to 34, the card's band, two directions each) | 0 |
| WWTCyberLab/gemma-4-E2B-it-abliterated | google/gemma-4-E2B-it | 96 of 1,951 (the attention output, down, gate and up projections of the 24 layers the card counts, one scale per layer) | 0 |
| lessans/gemma-4-E2B-it-uncensored | google/gemma-4-E2B-it | the same 70 as the TrevorJS copy, weight-file checksum and every field equal | 0 |
| jokernifty/gemma-4-e4b-it-abliterated | google/gemma-4-E4B-it | 31 of 2,076 (the attention output and down projection of layers 20 to 34 and the token embedding, the card's three targets; saved in float16) | 0.0000011 |
| Dingdust/ContextPilot-E4B-heretic | google/gemma-4-E4B-it (the grandparent; the README's second card names tencent/ContextPilot-E4B) | 285 of 2,076 (every kind of tensor: the named parent's fine-tune, with the Heretic kernels readable on 32 writers inside the card's windows) | 0.000998 |
| DuoNeural/Gemma-4-E4B-Heretic | google/gemma-4-E4B-it | 68 of 2,076 (the down projections of layers 6 to 41 and the attention outputs of 10 to 41, one shared direction) | 0 |
| treadon/gemma4-E4B-it-abliterated | google/gemma-4-E4B-it | 34 of 2,076 (the attention output and down projection of the card's 17 layers at scale 1.0, rows restored) | 0 |
| treadon/gemma4-E4B-it-Abliterated-AND-Disinhibited-USE-THIS | google/gemma-4-E4B-it | 42 of 2,076 (both writers of 21 layers: the disinhibition on 20 at scale 1.5 and the abliteration on 17 at 1.0, as the card says) | 0 |
| wangzhang/gemma-4-E2B-it-abliterated | google/gemma-4-E2B-it | 72 of 1,951 (the attention outputs of layers 9 to 34, the values of 9 to 14, the down projections of 14 to 34 and the queries of 16 to 34; no key) | 0 |
| treadon/gemma4-E2B-it-abliterated | google/gemma-4-E2B-it | 48 of 1,951 (the attention output and down projection of the card's 24 layers at scale 1.75, rows restored) | 0 |
| treadon/gemma4-E2B-it-Abliterated-AND-Disinhibited-USE-THIS | google/gemma-4-E2B-it | the same 48 as the maker's abliteration: the abliteration on 24 layers at 1.75 and the disinhibition on 20 at 1.5, as the card says | 0 |
| Bahushruth/gemma-4-31B-it-abliterated | google/gemma-4-31B-it | 66 of 1,188 (the attention output and down projection of layers 17 to 49, the maker's solver, many directions per matrix, rows within 0.0007) | 0 |
| paoloronco/Mistral-7B-Instruct-v0.3-heretic | mistralai/Mistral-7B-Instruct-v0.3 | 38 of 291 (the attention outputs of layers 11 to 31 and the down projections of 13 to 29, the card's two kernels) | 0 |
| Bahushruth/gemma-4-E4B-it-abliterated | google/gemma-4-E4B-it | 24 of 2,076 (the attention output and down projection of layers 21 to 32, the maker's solver, rows within 0.0005) | 0 |
| Pound1320/gemma-4-E4B-it-uncensored-heretic | google/gemma-4-E4B-it | the same 11 as the llmfan46 copy, weight-file checksum and every field equal, through a chain of two duplicates | 0.00008 |
| Cup4/gemma-4-E4B-it-uncensored-heretic | google/gemma-4-E4B-it | the same 11 as the llmfan46 copy, weight-file checksum and every field equal | 0.00008 |
| Cup5/gemma-4-E4B-it-uncensored-heretic | google/gemma-4-E4B-it | the same 11 as the llmfan46 copy, weight-file checksum and every field equal | 0.00008 |
| anlord/gemma-4-E2B-it-abliterated | google/gemma-4-E2B-it | 110 of 1,951 (seven components under the four kernels the repository's reproduction record states, read to the third decimal) | 0 |
| Ishowbackup/gemma-4-E2B-it-uncensored | google/gemma-4-E2B-it | the same 70 as the TrevorJS copy, weight-file checksum and every field equal | 0 |
| Pranavz/Hearthfire-24B-heretic | mistralai/Mistral-Small-3.2-24B-Instruct-2506 (the grandparent; the README's title names LatitudeGames/Hearthfire-24B) | 282 of 363 (every linear, the embedding and the head: the named parent's fine-tune, with the down-projection kernel readable on all 40 layers and the attention-output window on 19 to 34) | 0 |
| minpeter/Voxtral-Mini-3B-Text-2507-hf-heretic | mistralai/Voxtral-Mini-3B-2507 | 41 of 273 (the attention outputs of layers 9 to 26 and the down projections of 7 to 29, the card's two kernels; the audio tower left out of the copy) | 0 |
| akpsahan/Huihui-gemma-4-31B-it-abliterated-v2 | google/gemma-4-31B-it | the same 110 as the huihui-ai second version, two shard checksums and every field equal | 0 |
| claymorecrystal/gemma-4-26B-A4B-it-uncensored | google/gemma-4-26B-A4B-it | the same 90 as the TrevorJS copy, two shard checksums and every field equal | 0 |
| NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals5 | google/gemma-4-E4B-it | 29 of 2,076 (the attention outputs of layers 19 to 36 and the down projections of 21 to 34, inside the card's 19 to 42; seven more down projections rewritten under the threshold) | 0.000251 |
| alphakek/gemma-4-E4B-it-heretic-mythos-v1 | google/gemma-4-E4B-it | 34 of 2,076 (the attention output and down projection of layers 11 to 27, two of the down projections left as residues) | 0 |
| senjiangchen/gemma-4-E4B-it-uncensored | google/gemma-4-E4B-it | the same 84 as the TrevorJS copy, weight-file checksum and every field equal | 0 |
| Felldude/gemma-4-E4B-uncensored | google/gemma-4-E4B (the pretrained base the field names; the weights stand on google/gemma-4-E4B-it) | 595 of 2,076 (the whole language model: the base-to-instruct training, with the copy's own edit within 0.006 of the instruct model by byte range) | 0.00088 |
| AlekseyCalvin/Lyrical_Translator_ru2en_on_Gemma4_12b_heretic_SFT_Run2 | google/gemma-4-12B-it (the grandparent; the weights carry igorls's 12B Heretic edit under the training, finding 66) | 328 of 677 (all seven projections of all 48 layers, the global layers' values excepted) | 0 |
| Ilya626/gemma-4-E4B-it-SDFT_Heretic_RP | google/gemma-4-E4B-it | 674 of 2,076 (the language stack trained at 0.16 to 0.56 percent, and the 232 linear maps of the two towers replaced by random matrices, finding 63) | 0.0000011 |
| Sabomako/gemma-4-31B-it-heretic | google/gemma-4-31B-it | 8 of 1,188 (both writers of layers 31 to 34, weights to 5.36 with rows restored) | 0 |
| nguyenthilaitrieulong/gemma-4-31B-it-abliterated | google/gemma-4-31B-it | 95 of 1,188 (WWTCyberLab's unmeasured five-surface edit under the hub's duplicate function, finding 64) | 0 |
| callmegrr/gemma-4-31B-it-heretic-z | google/gemma-4-31B-it | 12 of 1,188 (the attention outputs of layers 37 to 46 and the down projections of 40 and 41, the card's two windows, the kernels read within 0.21) | 0 |
| p-e-w/gemma-4-E4B-it-heretic | google/gemma-4-E4B-it | 68 of 2,076 (the attention outputs of layers 11 to 41 and the down projections of 5 to 41, the card's windows) | 0 |
| sh0ck0r/gemma-4-E4B-it-heretic | google/gemma-4-E4B-it | 60 of 2,076 (the attention outputs of layers 19 to 41 and the down projections of 5 to 41, the card's windows) | 0 |
| JokeHer/gemma-4-E4B-it-heretic | google/gemma-4-E4B-it | 40 of 2,076 (both writers of layers 19 to 38, the card's arbitrary-rank range, layer 37's down projection rewritten to its own size) | 0 |
| BinxNet/gemma-4-E4B-it-heretic | google/gemma-4-E4B-it | 51 of 2,076 (the attention outputs of layers 7 to 41 and the down projections of 26 to 41, the card's windows) | 0 |
| BinxNet/gemma-4-12B-it-heretic | google/gemma-4-12B-it | 55 of 677 (the attention outputs of layers 4 to 47 and the down projections of 27 to 37, the card's windows, the heights unreadable) | 0 |
| yuna1126/gemma-4-E2B-Tema_Q-Abliterated | google/gemma-4-E2B-it | 7 of 2,011 (the attention outputs of layers 14 to 18 and the down projections of 12 and 13, a raised-cosine kernel read to the second decimal) | 0.00038 |
| igorls/gemma-4-12B-it-qat-q4_0-unquantized-heretic | google/gemma-4-12B-it-qat-q4_0-unquantized | 57 of 677 (the attention outputs of layers 16 to 47 and the down projections of 20 to 44, the card's windows, searched with thinking on) | 0 |
| llmfan46/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | 12 of 1,013 (the attention outputs of layers 11 to 22, the card's window on its one component, input side at weights 1.10 to 1.70) | 0 |
| wnfldchen/gemma-4-12B-it-qat-q4_0-unquantized-heretic | google/gemma-4-12B-it-qat-q4_0-unquantized | 46 of 677 (both writers of layers 19 to 41, the card's window, a direction per matrix, input side, four attention outputs outside the weight band) | 0 |
| eadx/Huihui-gemma-4-26B-A4B-it-qat-q4_0-unquantized-abliterated | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | 60 of 1,013 (huihui-ai's unmeasured QAT edit under the hub's duplicate function: both writers of all 30 layers at a weight of 3.50, finding 73) | 0 |
| prithivMLmods/gemma-4-E4B-it-qat-heretic_decensored | google/gemma-4-E4B-it-qat-q4_0-unquantized | 54 of 2,076 (the down projections of layers 12 to 41 and the attention outputs of 18 to 41, the card's windows, the down kernel read under its height) | 0 |
| xdavxd/gemma-4-26B-A4B-it-qat-heretic-ega | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | 90 of 1,013 (the attention outputs, shared down projections and all 128 experts' down projections of all 30 layers, rows restored within 0.0009, finding 74) | 0 |
| smashingtags/gemma-4-12b-it-abliterated | google/gemma-4-12B-it-qat-q4_0-unquantized (the QAT checkpoint the field names, under an instruct-model name; layer 0 byte-equal to it by range read) | 68 of 677 (both writers of layers 14 to 47, a plain projection at weight 1.00) | 0 |
| coder3101/gemma-4-12B-it-qat-q4_0-unquantized-heretic | google/gemma-4-12B-it-qat-q4_0-unquantized | 24 of 677 (the attention outputs of layers 24 to 47, the card's window, input side at weights 0.76 to 2.54, rows 0.007 under the claim) | 0 |
| Umranz/diffusiongemma-26B-A4B-it-abliteration | google/diffusiongemma-26B-A4B-it | 38 of 1,047 (both writers of layers 1 to 19, the card's cap at 20, fifteen of them residues, no expert touched) | 0 |
| sh0ck0r/Artemis-31B-v1.1-heretic (second measurement) | TheDrummer/Artemis-31B-v1.1 (the parent the README names) | 73 of 1,188 (the attention outputs of layers 25 to 59 and the down projections of 17 to 54, the card's windows, one direction, output side) | 0 |
| Pranavz/Hearthfire-24B-heretic (second measurement) | LatitudeGames/Hearthfire-24B (the parent the README's title names) | 56 of 363 (the down projections of all 40 layers and the attention outputs of 19 to 34, the card's windows, the kept fractions equal to the first measurement's) | 0 |
| Felldude/gemma-4-E4B-uncensored (second measurement) | google/gemma-4-E4B-it (the instruct model the weights stand on) | 245 of 2,076 (the language stack of layers 0 to 14 and 27 to 41 by 0.1 to 0.7 percent, no direction; layers 15 to 26, both towers and the embeddings equal) | 0.00099 |
| Kooten/gemma-4-31b-abliterated-v1.1 | google/gemma-4-31B-it (the vision tower paired through the dropped `.linear.` segment) | 256 of 1,188 (67 language matrices under a linear kernel the card does not print, the down projections of 20 to 59 and the attention outputs of 24 to 50; 189 vision-tower linears replaced by fresh draws, finding 79) | 0 |
| Dzluck/gemma-4-E2B-it-abliterated-v2 | google/gemma-4-E2B-it | 60 of 2,011 (huihui-ai's unmeasured E2B second version under another name: both writers of layers 5 to 34 at a weight of 2.50 on the first version's direction, finding 80) | 0 |
| enkato64bit/SuperGemma-4-12b-abliterated | google/gemma-4-12B-it | 320 of 677 (Jiunsong's unmeasured 12B edit under the hub's duplicate function: a projection at 0.50 on both writers of layers 14 to 37 under a merged adapter on every linear, finding 81) | 0.00096 |
| coder3101/gemma-4-E4B-it-qat-q4_0-unquantized-heretic | google/gemma-4-E4B-it-qat-q4_0-unquantized | 16 of 2,076 (the attention outputs of layers 20 to 35, the card's window, input side at weights 1.19 to 1.91, rows 0.007 under the claim) | 0 |
| igorls/gemma-4-E4B-it-qat-q4_0-unquantized-heretic | google/gemma-4-E4B-it-qat-q4_0-unquantized | 32 of 2,076 (both writers of layers 21 to 36, a LoRA-rank search with thinking on, a direction per matrix, input side at weights 1.33 to 3.46) | 0 |
| OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-heretic-ja-v2 | google/gemma-4-12B-it-qat-q4_0-unquantized | 54 of 677 (both writers of layers 13 to 39, the card's window, the LoRA-adapter arbitrary-rank branch searched on Japanese prompts, input side at weights 0.74 to 1.95, rows at or under the band, finding 83) | 0 |
| OS-Software/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ja | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | 32 of 1,013 (the attention outputs and shared down projections of layers 7 to 22, the card's window, the same branch on Japanese prompts, input side at weights 1.24 to 2.09; no expert, finding 83) | 0 |
| wnfldchen/gemma-4-31B-it-qat-q4_0-unquantized-heretic-merged | google/gemma-4-31B-it-qat-q4_0-unquantized | 30 of 1,188 (the attention outputs of layers 24 to 53, the card's window and its one target, a rank-256 adapter merged, input side on 27 at weights to 4.47, one matrix rewritten, rows 0.014 to 0.75 under a preservation claim, finding 84) | 0 |
| TheUmbraWalker/gemma-4-E4B-it-heretic | google/gemma-4-E4B-it | 73 of 2,076 (the attention outputs of layers 4 to 41 and the down projections of 7 to 41, the card's kernels to the layer; the first pass of the maker's second copy, its directions at 1.000 on 57 and TrevorJS's at 0.98 on all 73, finding 85) | 0 |
| MoonRide/gemma-4-31B-it-heretic-ara | google/gemma-4-31B-it | 44 of 1,188 (all 24 attention outputs and 20 down projections of layers 30 to 53, the card's window; 36 edits on the input side at weights 1.35 to 4.39 with rows in the band, 8 residues, 4 more down projections under the threshold, finding 86) | 0.00098 |
| MoonRide/gemma-4-E4B-it-heretic-ara | google/gemma-4-E4B-it | 33 of 2,076 (both writers of layers 21 to 37, the card's window; 26 edits on the input side at weights 0.08 to 2.30 with rows in the band on 25, 7 residues, one down projection under the threshold, finding 86) | 0.00091 |
| llmfan46/gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic | google/gemma-4-12B-it-qat-q4_0-unquantized | 11 of 677 (the attention outputs of layers 24 to 34, the card's window and its one target, input side at weights 1.23 to 2.64, the directions at 0.97 to coder3101's QAT edit and 0.95 to the maker's own instruct edit, finding 87) | 0 |
| NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8-attn | google/gemma-4-E4B-it | 25 of 2,130 (14 attention outputs of layers 17 to 31 inside the card's window and 11 down projections of 18 to 31 the card says were not a target, input side at weights 1.15 to 1.84 and 1.23 to 1.51; five more under the threshold, finding 87) | 0.00013 |
| llmfan46/gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic | google/gemma-4-31B-it-qat-q4_0-unquantized | 16 of 1,188 (the attention outputs of layers 16, 18, 21, 22 and 24 to 35 inside the card's window of 9 to 35, ten more layers of the window under the threshold, input side at weights 1.58 to 3.64, the direction at 0.99 to coder3101's edit of the same checkpoint, finding 89) | 0.000195 |
| coder3101/gemma-4-31B-it-qat-q4_0-unquantized-heretic | google/gemma-4-31B-it-qat-q4_0-unquantized | 21 of 1,188 (17 attention outputs of layers 16, 22 and 24 to 38 edited inside the card's window of 15 to 38 at weights 0.57 to 3.79 with rows in the band, four residues above the threshold and three under it, finding 89) | 0.000898 |
| coder3101/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | 9 of 1,013 (the attention outputs of layers 12 to 20, the card's window, input side at weights 1.06 to 1.81, rows in the band; no expert, finding 89) | 0 |
| OS-Software/gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic | google/gemma-4-31B-it-qat-q4_0-unquantized | 22 of 1,188 (both writers of layers 30 to 40, the card's window, rank four exactly, input side at weights 0.86 to 2.39, writers unrelated, rows unrestored, finding 90) | 0 |
| OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic-v3 | google/gemma-4-12B-it-qat-q4_0-unquantized | 18 of 677 (both writers of layers 23 to 31, the card's window, rank four exactly, input side at weights 0.58 to 2.43, writers unrelated, rows unrestored, finding 90) | 0 |
| JJaguar/gemma-4-12B-it-qat-q4_0-unquantized-heretic-nx | google/gemma-4-12B-it-qat-q4_0-unquantized | 49 of 677 (the down projections of layers 21 to 46 and the attention outputs of 25 to 47, the card's two kernels to the layer, one direction at 0.90 to the instruct model's kernel exports, no readable weight, finding 91) | 0 |
| Mitchins/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | 52 of 1,013 (the attention outputs of layers 3 to 29 with the dense down projections of 15 to 23 and all 128 experts of 11 to 26, the record's three kernels to the layer, one direction, rows to 0.18 on the experts under "full" normalisation, finding 92) | 0 |
| OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-heretic-ja | google/gemma-4-12B-it-qat-q4_0-unquantized | 73 of 677 (both writers of layers 10 to 46, the card's window, the LoRA-adapter branch on Japanese prompts, input side at weights 0.74 to 3.73, rows to 0.21 under no claim, one attention output under the threshold, finding 93) | 0.000086 |
| SassyDiffusion/gemma-4-26B-A4B-it-heretic-ara | google/gemma-4-26B-A4B-it | 35 of 1,013 (20 attention outputs of layers 6 to 28 and 15 dense down projections of 6 to 27, no expert, an arbitrary-rank edit on the input side at weights 0.42 to 1.89 on the 26B-A4B family's directions at 0.98, under a card of 208 bytes of front matter, twelve more under the threshold, finding 98) | 0.000673 |
| SassyDiffusion/gemma-4-E4B-it-heretic | google/gemma-4-E4B-it | 21 of 2,076 (the attention outputs of layers 21 to 41, the card's window and its one target, input side at weights 0.84 to 2.72, rows in the band on every matrix, the E4B family's directions at 0.98, finding 98) | 0 |
| RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals2 | google/gemma-4-12B-it | 40 of 677 (both writers of layers 23 to 42, the card's window, 37 edits on the input side at weights 0.45 to 1.52 with rows in the band and three residues, the maker's Refusals9 direction at 0.98, finding 99) | 0 |
| jwest33/gemma-4-12B-it-null-space-abliterated | google/gemma-4-12B-it | 329 of 677 (every linear map of all 48 layers and the token embedding, one direction equal to the maker's shipped mean direction at 0.96 to 1.00, a Gaussian weight over the layers that reads back from the shipped configuration within 0.047, finding 94) | 0 |
| DuoNeural/gemma-4-26B-A4B-it-abliterated | google/gemma-4-26B-A4B-it | 90 of 1,013 (the attention outputs, dense down projections and packed expert down projections of all 30 layers: TrevorJS's 26B-A4B edit, its directions at 1.000 on all 90 and its tensors within 0.0006 of his by byte range, under a card that names a per-expert method of the maker's own, finding 95) | 0 |
| DuoNeural/Gemma-4-E2B-Heretic | google/gemma-4-E2B-it | 49 of 1,951 (the down projections of layers 6 to 34 and the attention outputs of 15 to 34, one direction at 0.925 to huihui-ai's E2B direction on every matrix, output side at kernel-shaped weights of 0.75 to 1.43 the card does not print, no chat template shipped, finding 96) | 0 |
| Bahushruth/gemma-4-E2B-it-abliterated | google/gemma-4-E2B-it | 18 of 1,951 (both writers of layers 16 to 24 of the 35 the card names, the maker's own solver with many directions per matrix, input side at weights 1.56 to 2.08, rows within 0.0004 under the card's reparameterisation claim, finding 99) | 0 |
| Himanshuoo8/gemma-4-E4B-it-Claude-Opus-4.5-HERETIC-UNCENSORED-Thinking | google/gemma-4-E4B-it | 287 of 2,130 (DavidAU's unmeasured E4B fine-tune under the hub's duplicate function: coder3101's Heretic edit on the attention outputs of layers 21 to 41 at 1.000 on 20 of 21, under a fine-tune of 0.1 to 0.7 percent on every linear map of the 42 layers and a thinking template, finding 97) | 0.000893 |

The fair statement of the result is narrow: at the weight level, one hundred and thirty copies contain the edit or the
training they claim and no other, eight carry a parent or a change their cards do not name, one could not be paired
and one could not be read. Weight differences alone cannot certify the absence of hidden behaviour, and the census is
one hundred and sixty-eight distinct copies, one hundred and thirty-eight of them read.

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
(`results/weights/DuoNeural-Mistral-NeMo-12B-Abliterated.json`). Round 25 reads the floor from the other side:
jokernifty/gemma-4-e4b-it-abliterated is a single projection at weight 1.0000 saved in float16, and its 31 matrices
(changes 0.019 to 0.0225, the band where every bfloat16 copy reads 0.989 to 0.997) read a first share of 0.99988 to
0.99993 with a leftover of 0.00009 of the norm, while 336 untouched tensors carry residues of at most 0.0000011
from the storage change. The floor is the storage type's and nothing else (finding 51; `results/weights/jokernifty-gemma-4-e4b-it-abliterated.json`).

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
Round 31 adds a configuration change of a new kind, on AlekseyCalvin's 12B translation copy:
`text_config.max_position_embeddings` saved as 131,072 where the original declares 262,144, the declared context
halved by the training's save and not mentioned on the card (finding 66). Round 36 adds a change of the generation configuration: Mitchins's 26B-A4B QAT export carries a `generation_config.json` the library wrote from the model configuration (`_from_model_config` true), without the checkpoint's sampling settings (`do_sample`, `top_k` 64, `top_p` 0.95) and with `eos_token_id` [1, 106] where the checkpoint lists [1, 106, 50], the `<|tool_response>` token; the copy decodes greedily and does not stop at a tool response, and the card does not say so (finding 92). Round 38 adds Unsloth's rewrite of SassyDiffusion's 26B-A4B copy, the end-of-sequence token moved to `<turn|>` and a pad token set under a card of front matter alone, and DavidAU's E4B fine-tune through Himanshuoo8's duplicate, which ships no generation configuration at all (findings 97 and 98).

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

Round 29 measured the third case: minpeter/Voxtral-Mini-3B-Text-2507-hf-heretic was pinned against the speech
release mistralai/Voxtral-Mini-3B-2507 and read through the tower mapping of finding 14, 273 text tensors matched,
489 audio tensors reported as left out, zero flags and the card's two kernels to the second decimal (finding 60).
The case closes: a text-only extraction is measurable against the multimodal release it came from. The round 39 pin stage adds a case of the other kind: TurkishCodeMan/gemma-4-e2b-it-abliterated names the Gemma 4 E2B and is, by shape and by byte range, Google's first-generation gemma-2b-it with its two writers edited, so the stated original cannot be compared because it is not the original (finding 88).

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

Round 19 adds four re-uploads in one round, every one made with the hub's duplicate function and named as such in
its first commit title: Iambackup/gemma-4-12B-it-uncensored and Justbackup/gemma-4-12B-it-uncensored ("Duplicate
from TrevorJS/gemma-4-12B-it-uncensored", 2026-06-14 and 08-19), MeFFyLe/gemma-4-12B-it-uncensored-heretic
("Duplicate from llmfan46/gemma-4-12B-it-uncensored-heretic", 09-12) and
nicoboss/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-llamacppfixed ("Duplicate from huihui-ai/...",
2025-07-07, followed by one commit that repairs the token files). Each carries its parent's weight files under the
parent's LFS checksums, its parent's README byte for byte, and so a `base_model` field that names the grandparent;
each equals its parent's report in every field of every tensor (finding 38). Eight of the census's sixty-four
distinct copies are now re-uploads, and the parents of all eight are measured. Evidence:
`results/weights/Iambackup-gemma-4-12B-it-uncensored.json` and
`results/weights/Justbackup-gemma-4-12B-it-uncensored.json` against
`results/weights/TrevorJS-gemma-4-12B-it-uncensored.json`,
`results/weights/MeFFyLe-gemma-4-12B-it-uncensored-heretic.json` against
`results/weights/llmfan46-gemma-4-12B-it-uncensored-heretic.json`,
`results/weights/nicoboss-Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-llamacppfixed.json` against
`results/weights/huihui-ai-Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated.json`, and the readings in
`docs/cards/`.

Round 30 adds three re-uploads and one parent measured through them. sitten1/gemma-4-26B-A4B-it-uncensored and
erunda337/gemma-4-26B-A4B-it-uncensored are one commit each ("Duplicate from TrevorJS/gemma-4-26B-A4B-it-uncensored",
2026-04-08 and 04-12), carry TrevorJS's two shards under the parent's checksums (`4b988df4e5`, `3d2388e809`) and
equal round 3's second pass of the parent in every field that does not depend on the randomised sketch, with the
sketched fields within 2.3 × 10⁻⁶ and the same 31 flags; the two equal each other in every field.
nnnxnsn/diffusiongemma-26B-A4B-it-HERETIC-Uncensored is one commit ("Duplicate from
edwixx/diffusiongemma-26B-A4B-it-HERETIC-Uncensored", 06-22) and FredyRivera-dev/diffusiongemma-26B-A4B-it-HERETIC-Uncensored
is an upload by hand (06-29) of the same eleven shards under edwixx's checksums (`3b78a288` to `f86b80dd`) with a
processor configuration added and a README that says "All credit to edwixx"; the two equal each other in every
field of all 1,047 tensors, and since edwixx's own repository has not been measured, pair 7 stands as the
measurement of that edit (finding 40). Eleven of the census's seventy-two distinct copies are re-uploads, and the
parents of all eleven are measured, one of them only through its re-uploads. Evidence:
`results/weights/sitten1-gemma-4-26B-A4B-it-uncensored.json` and
`results/weights/erunda337-gemma-4-26B-A4B-it-uncensored.json` against
`results/weights/TrevorJS-gemma-4-26B-A4B-it-uncensored.pass-2.json`,
`results/weights/nnnxnsn-diffusiongemma-26B-A4B-it-HERETIC-Uncensored.json` against
`results/weights/FredyRivera-dev-diffusiongemma-26B-A4B-it-HERETIC-Uncensored.json`, and the readings in `docs/cards/`.

Rounds 20 and 32 add three re-uploads, two by the duplicate function and one by a re-save.
Ishowbackup/gemma-4-12B-it-uncensored and Ishowbackup/Huihui-gemma-4-12B-it-abliterated are one commit each
("Duplicate from TrevorJS/gemma-4-12B-it-uncensored" and "Duplicate from huihui-ai/Huihui-gemma-4-12B-it-abliterated",
two minutes apart on 2026-08-18), carry the parents' weight files under the parents' checksums (`dd7fcab672`,
`2dd13d8676`) and equal the round 8 and round 13 reports of the parents in every field of all 677 tensors, the
fourth repository on TrevorJS's file and the third on huihui-ai's. prithivMLmods/gemma-4-26B-A4B-Heretic-Stable
is huihui-ai's 26B-A4B copy loaded and saved again under a 5.9.0 version string in five shards, which the card
says in its first sentence: no shard checksum matches the parent's two, and every field of all 1,013 tensors
equals the round 13 report and the maker's own Uncensored-MAX re-upload of the same file (round 14), so one
huihui-ai file now stands in the census under three names. Round 32 measured no re-upload, the first round pinned
under the duplicate check (finding 38). Fourteen of the census's eighty-eight distinct copies are re-uploads, and
the parents of all fourteen are measured, one of them only through its re-uploads. Evidence:
`results/weights/Ishowbackup-gemma-4-12B-it-uncensored.json` against
`results/weights/TrevorJS-gemma-4-12B-it-uncensored.json`,
`results/weights/Ishowbackup-Huihui-gemma-4-12B-it-abliterated.json` and
`results/weights/prithivMLmods-gemma-4-26B-A4B-Heretic-Stable.json` against the two huihui-ai reports, and the
readings in `docs/cards/`.

Round 22 closes the 31B case and adds three measurements the duplicate rule would have refused.
huihui-ai/Huihui-gemma-4-31B-it-abliterated, the first version, pinned in round 14 and run on Blueback in round
22, equals prithivMLmods/gemma-4-31B-it-Uncensored-MAX's round 18 report in every measured field of all 1,188
tensors (120 changed, weight 1.00 on every residual writer of all 60 layers, 52 flags at the floor) and shares no
checksum with it (two shards against ten, a re-save as the maker's Heretic-Stable was): all four of the maker's
Uncensored-MAX copies are now measured as the huihui-ai edits, and the fourth is the parent's only other
measurement in the census. laladream/gemma-4-12B-it-uncensored (one commit, "Duplicate from
TrevorJS/gemma-4-12B-it-uncensored", 2026-08-21) and lessans/gemma-4-E2B-it-uncensored (one commit, "Duplicate from
TrevorJS/gemma-4-E2B-it-uncensored", 04-18) carry the parents' files under the parents' checksums (`dd7fcab672`,
`8237e4818b`) and equal the round 8 and round 13 reports in every field, the fifth repository on TrevorJS's 12B
file and the second on its E2B file. The round also measured huihui-ai's E2B edit a second time on the same
system against the same pin, and the two reports are equal to the last digit (finding 50). Seventeen of the
census's one hundred and three distinct copies were re-uploads at round 22, and the parents of all seventeen are measured, one
of them only through its re-uploads. Evidence: `results/weights/huihui-ai-Huihui-gemma-4-31B-it-abliterated.json`
against `results/weights/prithivMLmods-gemma-4-31B-it-Uncensored-MAX.json`,
`results/weights/laladream-gemma-4-12B-it-uncensored.json` against
`results/weights/TrevorJS-gemma-4-12B-it-uncensored.json`, `results/weights/lessans-gemma-4-E2B-it-uncensored.json`
against `results/weights/TrevorJS-gemma-4-E2B-it-uncensored.json`, and the readings in `docs/cards/`.

Rounds 26 and 29 add seven re-uploads, all made with the hub's duplicate function and all equal to their parents'
reports in every field: Pound1320's, Cup4's and Cup5's copies of llmfan46's E4B edit, Ishowbackup's of TrevorJS's
E2B edit, akpsahan's of huihui-ai's second 31B version, claymorecrystal's of TrevorJS's 26B-A4B edit and
senjiangchen's of TrevorJS's E4B edit (finding 56). Twenty-four of the census's one hundred and nineteen distinct
copies are re-uploads, and the parents of all twenty-four are measured, one of them only through its re-uploads.

Round 31 adds nguyenthilaitrieulong/gemma-4-31B-it-abliterated, one commit titled "Duplicate from
WWTCyberLab/gemma-4-31B-it-abliterated", whose parent was pinned for Raider in round 17 and never measured, so the
re-upload is the only measurement of that edit (finding 64), the second such case after the prithivMLmods 31B copy
of round 18. Round 34 adds the third: eadx's one-commit duplicate of huihui-ai's QAT 26B-A4B edit, whose parent
repository returns 404, measured as a shared projection at 3.5 on every layer (finding 73).

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

Round 19 adds two readings and one blank. SevenOfNine's 26B-A4B Heretic copy reads a schedule on the output side: the
attention outputs keep −0.07 to 0.13 of the original's action on layers 4 to 12 and −0.09 to −0.40 on 13 to 29, the
shared down projections 0.00 to 0.25 on 16 to 29, a weight of 0.87 rising to 1.40 and the third Heretic kernel the
census reads from the kept fraction. 3MPER0RR's 31B copy, under a card that names nothing, reads one strength per
kind on the output side, 1.16 to 1.40 on the down projections of layers 39 to 59 and 0.34 to 0.82 on the attention
outputs of 40 to 59, where the maker's 12B copy read none. prithivMLmods/gemma-4-12B-it-heretic_decensored reads one
shared direction (cosine 0.90 to 0.998 across its 56 matrices) at rank one and no weight at all: the kept fraction
along that direction runs from −0.01 to 0.98 on the attention outputs and −0.28 to 0.77 on the down projections,
the left below the right on 25 of 56, under a card that prints Heretic's kernel in full (0.81 to 1.18 peaking at
layer 40, 0.97 to 1.37 peaking at 46), which would read as fractions of 0.19 to −0.18 and 0.03 to −0.37 falling
smoothly. The second copy that reads no weight and no side on a rank-one shared direction, and the first whose card
states the numbers the weights do not carry. Evidence: `results/weights/SevenOfNine-Gemma-4-26B-A4B-It-Abliterated.json`,
`results/weights/3MPER0RR-gemma-4-31b-it-3MPER0RR-abliterated.json`,
`results/weights/prithivMLmods-gemma-4-12B-it-heretic_decensored.json` and the readings in `docs/cards/`.

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

Round 19 measured four more 12B copies (TrevorJS's file twice under the Iambackup and Justbackup names, saved with
5.12.0; prithivMLmods's, 5.12.1; llmfan46's under the MeFFyLe name, 5.10.2) against Google's 5.10.0.dev0 file, and
all four lack the same four fields and write `bfloat16` into the audio and vision sub-configurations where Google's
file has null. Nine 12B copies now read the six fields the same way, and the reason the metadata tool cannot close
them at home is now known: the family's top-level `model_type` is `gemma4_unified`, which transformers 5.6.2 (the
home venv) and 4.56.2 (the cluster pin) do not know, so the class-default lookup returns nothing and neither file
can be loaded. Under 5.12.0 both files load to 640, 640, 640 and 48, and the fresh class default is still out of
reach (the unified class leaves its audio and vision sub-configurations empty until given one), so the rule that
closes them must load both saved files and compare what the library reads: that rule and the null-data-type rule
were added in round 19 (`audit/compare.py`, `tests/test_resave.py`), close all six fields under 5.12.0 and two
under 5.6.2; the home environment has since moved to transformers 5.22.1 and the committed reports of all twelve 12B
pairings were judged again under it (finding 39). Evidence:
`results/meta/Iambackup-gemma-4-12B-it-uncensored.json`, `results/meta/Justbackup-gemma-4-12B-it-uncensored.json`,
`results/meta/prithivMLmods-gemma-4-12B-it-heretic_decensored.json`,
`results/meta/MeFFyLe-gemma-4-12B-it-uncensored-heretic.json` and the two judgements recorded in
`docs/census-round-19.md`.

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
dense writers beside them (`results/weights/WWTCyberLab-gemma-4-26B-A4B-it-abliterated.json`). Round 36 reads a third edit through the experts, Mitchins's kernel pass of the QAT checkpoint: all 128 experts of sixteen layers moved along one direction (the experts of a layer at a median cosine of 0.9999, the kinds at 0.80 or better), the worst expert's first share 0.976 to 0.989 on seven tensors, which are the scorer's flags, while the rows moved 0.03 to 0.18 on the experts where the dense writers held within 0.022 (finding 92). Round 38 reads a fourth edit through the experts, DuoNeural's 26B-A4B copy, which is TrevorJS's own edit over again: one direction per layer applied to every expert (left agreement 0.9957 to 0.9991), the worst expert 0.881 in layer 0, and the saved directions at 1.000 to his on all 90 names (finding 95).

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

Round 29 is the first in which the mappings carried a measurement rather than a refusal. Pranavz/Hearthfire-24B-heretic
stores a flat causal model where its original stores the text tower under `language_model.`: the tool renamed and
matched all 363 text tensors and reported the 222 vision tensors as left out (finding 61).
minpeter/Voxtral-Mini-3B-Text-2507-hf-heretic matched its 273 text tensors the same way with the 489 audio tensors
left out (finding 60). Both read with the flag counts their edits deserve and none for the mapping.

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
(`results/meta/llmfan46-Mistral-Small-3.2-24B-Instruct-2506-ultra-uncensored-heretic.json`). Round 38 reads the same move on a Gemma 4 copy, SassyDiffusion's 26B-A4B export saved through Unsloth: the tokenizer's end-of-sequence token `<turn|>` (106) where the original names `<eos>` (1), the configuration's `eos_token_id` 106 alone where the original has `[1, 106]`, a pad token of 0 where the original sets none, and a generation configuration that still names `[1, 106, 50]` (finding 98).

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

Round 19 adds seven Gemma 4 copies. Five carry the template they were pinned against byte for byte (MoonRide 31B,
3MPER0RR 31B, SevenOfNine 26B-A4B, Iambackup 12B, prithivMLmods 12B). Justbackup's 12B copy is the earlier-revision
case through a re-upload again (TrevorJS's files of 06-13 with Google's 17,466-byte template of 06-03, under a pin
of 07-20 whose template is the 18,681-byte file of 07-09; the same file duplicated under the Iambackup name a day
after the parent reads as pinned). MeFFyLe's 12B copy carries llmfan46's patched 21,488-byte template into a fifth
repository, one the maker does not own, through a duplicate. Of the thirty-six Gemma 4 copies of rounds 8, 12, 13,
14, 16, 18 and 19, twenty carry the template they were pinned against byte for byte and one more up to line
endings. Evidence: `results/meta/Justbackup-gemma-4-12B-it-uncensored.json`,
`results/meta/MeFFyLe-gemma-4-12B-it-uncensored-heretic.json` and `docs/census-round-19.md`. Round 34 adds the maker's
sixth template: the 26B-A4B QAT copy carries a 23,077-byte file (437 lines against the pin's 354) that matches no
revision of Google's QAT or instruct repositories, introduces six identifiers (`thinking_gate`, `preserve_thinking`,
`image_url` among them) and renders the fixed conversations identically; the six copies carry six template sizes
(`results/meta/llmfan46-gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic.json`). Round 37 reads the maker's 21,488-byte macro template a second time, in the `tokenizer_config.json` of the 12B QAT export against the checkpoint's `chat_template.jinja` (finding 87). Round 36 reads the 23,077-byte template a second time, byte for byte the 26B-A4B QAT export's text, in llmfan46's 31B QAT export against the checkpoint's 17,333-byte file (`results/meta/llmfan46-gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic.json`, finding 89). Round 38 closes two more templates by the later-revision check, SassyDiffusion's 26B-A4B copy on Google's `4c55b528` and RumiaChannel's Refusals2 on `711c1368`, reads DavidAU's E4B template through Himanshuoo8's duplicate (16,352 bytes that insert `<|think|>` after the system turn, finding 97), and finds DuoNeural's E2B repository shipping no template at all (finding 96).

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

Round 19 adds SevenOfNine/Gemma-4-26B-A4B-It-Abliterated, a Heretic run on the attention outputs of layers 4 to 29
and the shared down projections of 16 to 29, whose 30 packed expert down tensors, 30 gate-up tensors and 30 routers
read exactly 0: the fifth maker's copy on this base to leave all 3,840 expert matrices alone, beside the two
(TrevorJS, WWTCyberLab) that reach them. Evidence:
`results/weights/SevenOfNine-Gemma-4-26B-A4B-It-Abliterated.json`.

Round 30 adds two measurements of TrevorJS's file under other names (sitten1 and erunda337, finding 38), each
reading all 128 experts of every layer changed as the parent did, and the first edits of the diffusion variant of
this mixture (finding 40): edwixx's reaches all 128 experts of layers 11 to 29 by iterating the packed tensor's
slices, Goodoldjam's reaches none. Evidence: `results/weights/sitten1-gemma-4-26B-A4B-it-uncensored.json`,
`results/weights/FredyRivera-dev-diffusiongemma-26B-A4B-it-HERETIC-Uncensored.json` and
`results/weights/Goodoldjam-DiffusionGemma-26B-E38-Abliterated-BF16.json`.

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

Round 32 adds a seventh weight on a seventh base, the first QAT-unquantized checkpoint.
huihui-ai/Huihui-gemma-4-12B-it-qat-q4_0-unquantized-abliterated reads 1.00 (left kept fraction -0.005 to 0.005)
on the 28 writers of layers 23 to 36, the card's window, against google/gemma-4-12B-it-qat-q4_0-unquantized, with
nothing else moved and the token side the original's to the byte. The window is eight layers longer than the
maker's instruct 12B edit (23 to 28, round 13) at the same weight, so the script's layer choice changes with the
checkpoint where its weight does not. Seven weights on seven bases: 2.5, 1.5, 3.0, 1.00, 1.00, 0.99 and 1.00.
Evidence: `results/weights/huihui-ai-Huihui-gemma-4-12B-it-qat-q4_0-unquantized-abliterated.json` and the reading
in `docs/cards/`.

Round 22 measures the maker's own file of the 31B first version, which round 18 had read only through
prithivMLmods's re-upload: weight 1.00 on all 120 residual writers of all 60 layers (left kept fraction -0.001 to
0.008), one shared direction (0.99997 across the two kinds), rows moved up to 0.362, every field equal to the
re-upload's (finding 9). The two versions of one edit on one base now stand measured in the maker's own
repositories: 1.00 on all 60 layers, then 1.5 on layers 5 to 59 a day later, under a card that compares them by
perplexity and does not say the weight changed. Eight weights on seven bases, the 31B carrying two. Evidence:
`results/weights/huihui-ai-Huihui-gemma-4-31B-it-abliterated.json` against
`results/weights/huihui-ai-Huihui-gemma-4-31B-it-abliterated-v2.json` and the reading in `docs/cards/`.

Round 29 adds the first re-upload of the second version, akpsahan/Huihui-gemma-4-31B-it-abliterated-v2, the maker's
two shards under their checksums and every field equal, the weight 1.5 on all 110 matrices (finding 56).

Round 31 reads the same -0.500 on the ten writers of layers 55 to 59 of nguyenthilaitrieulong's copy of
WWTCyberLab's 31B edit, a weight of 1.5 from another maker's script. By byte range, layer 56's attention output
differs from huihui-ai's by 0.0306 of its norm where each differs from Google's by 0.019 and 0.024: two edits at one
weight along different directions (finding 64). Round 34 reads a fourth weight, the largest: the maker's QAT 26B-A4B
edit, through eadx's duplicate, keeps -2.4976 to -2.5027 on both writers of all 30 layers, a weight of 3.50 from
layer 0, along the two directions the instruct edit uses from layer 5 (finding 73). Round 35 reads the maker's E2B second version through Dzluck's re-upload: the first version's direction to the third decimal
at a weight of 2.50 from layer 5, where the first version used 1.00 from layer 10 (finding 80).

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

Round 19 adds the thirteenth copy, MoonRide/gemma-4-31B-it-heretic-ara-custom, the third with the down projections
and the second maker to claim the preservation step: both writers of layers 30 to 56 (the card's range with its
exclusive end), 44 edits (26 attention outputs, 18 down projections) at searched input-side weights of 0.63 to 2.93,
and ten in-range matrices rewritten near zero, six under the threshold (0.00077 to 0.000999) and four over it
(0.0010 to 0.0018), the first residue set that straddles the line; the rows of the 44 edits moved by 0.0059 to
0.0077, the band coder3101's four copies read. The round also measured llmfan46's 12B copy a second time under the
MeFFyLe name, a hub duplicate, with the same 16 matrices and weights. Thirteen copies, seven bases, all on the input
side. Evidence: `results/weights/MoonRide-gemma-4-31B-it-heretic-ara-custom.json` and the reading in `docs/cards/`.

Rounds 20 and 32 add three copies on two new bases. llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v1,
the maker's first Magistral copy, edits both writers of layers 16 to 26 (18 matrices) at input-side weights of
1.29 to 2.43 and leaves four in-range attention outputs (layers 23 to 26) as residues at 0.00029, under the
threshold; its v2 (round 18) reaches layers 9 to 36 at 1.69 to 4.71.
mewse/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ara edits both writers of layers 11 to 22 (24 matrices) on
the QAT-unquantized 26B-A4B at 1.23 to 4.35, rank one on 22 of them, with rows moved 0.007 to 0.25 under no
preservation claim. coder3101/gemma-4-E2B-it-qat-q4_0-unquantized-heretic edits nine attention outputs of layers
9 to 21 on the QAT-unquantized E2B at 1.75 to 3.12, leaves eight in-range attention outputs as residues at 0.0010
to 0.0014 and one more under the threshold at 0.000767, and moves the rows of the nine edits by 0.0073 to
0.0079, the band the maker's four instruct copies read. Sixteen copies, nine bases, all on the input side.
Evidence: `results/weights/llmfan46-Magistral-Small-2509-ultra-uncensored-heretic-v1.json`,
`results/weights/mewse-gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ara.json`,
`results/weights/coder3101-gemma-4-E2B-it-qat-q4_0-unquantized-heretic.json` and the readings in `docs/cards/`.

Round 22 adds the seventeenth copy and a third maker who claims the preservation step.
RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals9 (Heretic 1.2.0, `preserve_good_behavior_weight` 0.9147,
`steer_bad_behavior_weight` 0.0001, neighbour count 12, row-norm preservation on) rewrote every one of the 60
in-range matrices of layers 14 to 43 on the instruct 12B: 34 edits (13 attention outputs, 21 down projections) at
searched input-side weights of 0.61 to 1.25 with a fourth cumulative share of 0.87 to 0.98, 21 rounding residues at
0.0010 to 0.0018 and five matrices under the threshold at 0.00084 to 0.00096, more residues than edits on the
attention outputs (14 to 13). The rows of the 34 edits moved by 0.0053 to 0.0079, the band coder3101's and
MoonRide's copies read, so three makers' preservation steps leave the same seven tenths of a percent. Seventeen
copies, nine bases, all on the input side. Evidence:
`results/weights/RumiaChannel-gemma-4-12B-it-uncensored-ara-Refusals9.json` and the reading in `docs/cards/`.

Rounds 26 and 29 add three more and a second solver. NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals5 is the Heretic
branch on E4B: 29 matrices on both writers of layers 19 to 36, inside the card's 19 to 42, fourth cumulative share
0.95 to 0.99, input-side weights of 1.24 to 2.50, seven down projections in the window rewritten under the threshold
(0.00006 to 0.00025), rows 0.001 to 0.037 under no claim (finding 58). Bahushruth's two copies are the maker's own
L-BFGS solver with the grimjim reparameterization: 66 matrices on layers 17 to 49 of the 31B and 24 on layers 21 to
32 of the E4B, both writers, many directions per matrix (eighth cumulative share 0.61 to 0.93), input-side weights
of 1.19 to 3.46, and rows within 0.0007 and 0.0005, the only preservation claim in the census that holds (finding
57). Twenty copies, nine bases, all on the input side.

Round 33 widens the band again. JokeHer/gemma-4-E4B-it-heretic (Heretic v1.2.0's arbitrary-rank branch, start 19,
end 39, neighbour count 12) edits both writers of layers 19 to 38 on the input side at right-side weights 1.33 to
4.81 on the attention outputs and 3.4 to 30.1 on the down projections, three times the band above, with layer 37's
down projection changed by 1.008 of its own norm (first share 0.650, kept -29.09) and its rows put back within
0.0063, layer 20's left as a residue (0.0017, kept 1.00), and the other 38 matrices' rows moved 0.0057 to 0.0078
under a card that claims no preservation (finding 68). Evidence: `results/weights/JokeHer-gemma-4-E4B-it-heretic.json`.
Round 34 adds four arbitrary-rank copies: coder3101's 12B QAT edit reads the maker's claim band a fifth time
(0.0070 to 0.0079 on all 24 matrices, input side at weights 0.76 to 2.54); llmfan46's 26B-A4B QAT edit reads
input-side weights 1.10 to 1.70 on twelve attention outputs; Umranz's edit of the diffusion variant reads fifteen
residues and 23 projections with the band (0.0043 to 0.0079) under no claim (finding 76); and wnfldchen's LoRA-rank
fork reads rank one with a direction per matrix, input side at 0.95 to 1.90 with two attention outputs at 4.14 and
5.63 and two amplified rather than removed (`results/weights/wnfldchen-gemma-4-12B-it-qat-q4_0-unquantized-heretic.json`). Round 35 reads the band a sixth time on coder3101's E4B QAT edit, 0.0065 to 0.0078 on sixteen attention outputs (finding 82). Round 37 reads it on MoonRide's two April edits (0.0059 to 0.0077 on 36 matrices, 0.0051 to 0.0078 on 26, finding 86), at or under it on OS-Software's two LoRA-adapter exports (finding 83), and reads the first claim that holds on no matrix, wnfldchen's 31B export at a preservation weight of 0.1182 with rows 0.014 to 0.75 on all 30 (finding 84). Round 36 reads the band on coder3101's two QAT edits under the claim (0.0068 to 0.0079 on 17 attention outputs of the 31B checkpoint, 0.0067 to 0.0077 on 9 of the 26B-A4B's), 0.0023 to 0.052 on llmfan46's 31B QAT edit under no claim, then the largest row movement the census has read on a 12B under no claim, 0.21 on one attention output of OS-Software's first Japanese export (findings 89 and 93). Round 38 reads the band on SassyDiffusion's E4B edit (0.0068 to 0.0078 on all 21), on RumiaChannel's Refusals2 (0.0052 to 0.0079 on all 37 edits) and through DavidAU's fine-tune on coder3101's attention outputs (0.0071 to 0.0079, finding 97), and reads a reparameterised claim that holds to the row on Bahushruth's E2B copy (0.0001 to 0.0004, finding 99).

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

Rounds 26 and 29 add three more re-uploads of the fingerprint, Ishowbackup's of the E2B file, senjiangchen's of the
E4B file and claymorecrystal's of the 26B-A4B shards, each equal to the parent's report in every field (finding 56).
The E2B file now stands in three repositories and the 26B-A4B shards in four. Round 34 reads the fingerprint from
a second maker on a second checkpoint: xdavxd's run of the method on the 26B-A4B QAT checkpoint keeps a median 0.014 to
0.18 per expert tensor on 28 of 30 layers, rows within 0.0004 on the dense matrices and 0.0009 per packed expert,
and its directions stand at 0.97 to TrevorJS's own (finding 74). Round 38 reads the fingerprint on a copy that is neither a re-upload of TrevorJS's file nor an independent run: DuoNeural's 26B-A4B copy, its directions at 1.000 to his on all 90 names and its tensors within 0.0006 of his by byte range, under a card that names a method of the maker's own (finding 95).

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

The same maker's Gemma 4 copy repeats the pattern. Felldude/gemma-4-E4B-uncensored names google/gemma-4-E4B, the
pretrained base, carries the instruct model's 17,336-byte template and its two-token end list, and by byte range
its norms and layer scalars are byte-equal to google/gemma-4-E4B-it and its linears within 0.00003 to 0.006 of it,
where both differ from the base by 0.745 (finding 62). Two copies, one maker, the same wrong field on two families.

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

Round 22 adds a rank-two copy under a card that says so: Carlosian/Gemma-4-12b-it-Abliterated, "biprojected
clean cone, K = 4, cone rank 2", changes both writers of layers 14 to 34 of the instruct 12B with a first share of
0.59 to 0.91 and a fourth cumulative share of 0.986 to 0.995 on all 42, the two directions carrying the change and
the bfloat16 floor the rest, rows restored within 0.0005, nothing else moved. The kept fractions along the leading
direction read no single side (the left below the right on 29 of 42), as a rank-two edit gives. Evidence:
`results/weights/Carlosian-Gemma-4-12b-it-Abliterated.json` and the reading in `docs/cards/`.

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

Round 31 reads the maker's scale rule a second time, on its 31B edit through nguyenthilaitrieulong's re-upload:
thirteen embedding rows at 0.0909 of their length under a card that says "scaled down by 10x", a division by eleven
as the 26B-A4B's "strength 5" was a division by six (finding 64). The maker divides a row by one plus the number it
prints.

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

Round 19 adds a repair of the first case above. nicoboss/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-
llamacppfixed is huihui-ai's copy duplicated (the same ten shards) with one commit on top, "Upload 6 files": a
`tokenizer.json` of 17,078,037 bytes that the parent lacked and that matches neither unsloth's (17,078,019 bytes) nor
the one llmfan46's copy carries (17,078,174), a `chat_template.json`, and a rewritten tokenizer configuration and
special-tokens map in which ids 32 and 33 read `<SPECIAL_32>` and `<SPECIAL_33>` where the parent's files say
`[ARGS]` and `[CALL_ID]`; the other 998 added-token entries, the configuration, the generation settings and the
template are the parent's byte for byte. With the file present the token ids resolve (1, 2, 11, 0) where the
parent's report could not resolve them, and the tool reports 2,025 fields against the parent's 1,025, the extra
thousand being the table the parent lacked. The repair is what the name claims and touches no weight. Evidence:
`results/meta/nicoboss-Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-llamacppfixed.json` against
`results/meta/huihui-ai-Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated.json` and the reading in
`docs/cards/`.

Round 20 adds the maker's first Magistral copy, llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v1, on
the same conversion: unsloth's token files under a 5.3.0 re-save, the conversion's `unsloth_fixed` and three
token ids, and 1,021 fields the tool counts against an original that ships none of them. At home one more field
closed by the default rule (`text_config.rope_parameters`, written by the re-save for the original's
`rope_theta`); `vision_config.rope_parameters`, the same rename on the vision side, stays open because the rule
reads the text configuration only. Three copies of this original, all on the one conversion. Evidence:
`results/meta/llmfan46-Magistral-Small-2509-ultra-uncensored-heretic-v1.json` and the reading in `docs/cards/`.

Rounds 26 and 29 add two more copies whose token side is a conversion rather than an edit: Pranavz's Hearthfire
copy, whose 1,027 fields are the fine-tune's own ChatML tokenizer and flat configuration against a release that
ships `tekken.json` (finding 61), and minpeter's Voxtral extraction, whose 2,032 fields are a text-only
configuration and tokenizer against a speech release (finding 60). In neither does anything beyond the conversion
remain.

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

## 38. Four hub duplicates in one round, each readable from its commit title and file checksums before any download

Iambackup/gemma-4-12B-it-uncensored (created 2026-06-14 at 15:38Z), Justbackup/gemma-4-12B-it-uncensored (08-19,
16:23Z), MeFFyLe/gemma-4-12B-it-uncensored-heretic (09-12, 18:03Z) and
nicoboss/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-llamacppfixed (2025-07-07, 15:02Z) each begin with
one commit titled "Duplicate from" and the parent's name (TrevorJS/gemma-4-12B-it-uncensored twice,
llmfan46/gemma-4-12B-it-uncensored-heretic, huihui-ai/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated), the
hub's own duplicate function; three of the four have no other commit. The hub's file listing gives the parent's LFS
checksum on every weight file: `dd7fcab672` on the 23,919,549,408-byte `model.safetensors` of the TrevorJS trio
(with `a2619fe11b` on the 32,169,780-byte `tokenizer.json`), `4e6ac81d39` on MeFFyLe's and llmfan46's, and the ten
shards `b6c0aee6ef` to `101361dc32` with `tekken.json` `6e2501687c` on nicoboss's and huihui-ai's. The READMEs are the
parents' byte for byte (4,929, 36,152 and 7,224 bytes), so each copy's `base_model` field names the grandparent,
Google or Mistral, as the parent's does, and the pinner paired each with that grandparent. Measured so, every
per-tensor field of every tensor equals the parent's report (677, 677, 677 and 585 tensors; 66, 66, 16 and 80
changed) and the flag counts are the parents' (1, 1, 15 and 0). Eight of the census's sixty-four distinct copies are
re-uploads, six of them with "Duplicate from" as the first commit title, and two accounts named for backing up hold
the same TrevorJS file, which a count by repository would count three times. The four cost 96 GB of downloads and
eight compute jobs for results the listing already held. The rule the pinner needs: a first commit titled
"Duplicate from", or weight files whose LFS checksums equal a measured copy's, pairs the repository with its parent,
records it as that measurement, and files no comparison. Evidence: the four `results/weights/` reports named in
finding 9 against their parents', the commit titles and checksums recorded in the four readings in `docs/cards/`,
and `data/batches/round-19-batch-1.json`.

Round 30 adds three more, two of them before the rule was written down and one after: sitten1 (created 2026-04-08
at 20:36Z) and erunda337 (04-12, 04:58Z), "Duplicate from TrevorJS/gemma-4-26B-A4B-it-uncensored", with TrevorJS's
49,323,334,202-byte and 2,288,675,130-byte shards under `4b988df4e5` and `3d2388e809` and TrevorJS's 4,523-byte
README of that week; and nnnxnsn (06-22, 09:09Z), "Duplicate from edwixx/diffusiongemma-26B-A4B-it-HERETIC-Uncensored",
with edwixx's eleven shards under `3b78a288` to `f86b80dd` and edwixx's README of that day. A fourth repository in
the round, FredyRivera-dev's (06-29), is not the duplicate function (an initial commit and an upload by the
large-folder tool) and carries the same eleven checksums with one file added, which the checksum half of the rule
catches where the title half does not. Measured, the three duplicates equal their parents' measurements in every
field and the counts are the parents' (31, 31 and 86 flags); they cost 155 GB of downloads and three compare jobs.
Eleven of seventy-two distinct copies are re-uploads, nine of them with "Duplicate from" as the first commit title.
Evidence: the three `results/weights/` reports named in finding 9 against their parents', the commit titles and
checksums in the four readings in `docs/cards/`, and `data/batches/round-30-batch-1.json`.

Round 20, pinned before the rule was written down, carried two more that the rule catches and one it does not:
Ishowbackup's two repositories (created 2026-08-18 at 15:32Z and 15:34Z, "Duplicate from
huihui-ai/Huihui-gemma-4-12B-it-abliterated" and "Duplicate from TrevorJS/gemma-4-12B-it-uncensored", the
parents' weight files under `2dd13d8676` and `dd7fcab672`), and prithivMLmods/gemma-4-26B-A4B-Heretic-Stable, a
re-save of huihui-ai's 26B-A4B copy in five shards whose checksums match nothing and whose every measured field
equals the parent's. The duplicate check of 11-01 00:04Z named the two Ishowbackup pairs before the compares ran,
and the desk let the round finish because the download was already an hour in; the three cost 1,913 compute
seconds and their share of a 5,939-second download. Round 32 is the first batch pinned under the rule: the pinner
refused seven repositories whose weight files carried a measured copy's checksum, and the round measured no
re-upload. A re-save check is still owed; the hub listing cannot give it, and the card's first sentence can.
Fourteen of eighty-eight distinct copies are re-uploads, eleven of them with "Duplicate from" as the first commit
title. Evidence: the three `results/weights/` reports named in finding 9 against their parents', the commit
titles and checksums in the three readings in `docs/cards/`, `data/batches/round-20-batch-1.json` and
`data/batches/round-32-batch-1.json`.

Round 22, pinned before the rule as round 20 was, carried two more the rule catches and one a second rule would:
laladream/gemma-4-12B-it-uncensored (created 2026-08-21 at 08:10Z, "Duplicate from TrevorJS/gemma-4-12B-it-uncensored",
TrevorJS's 23,919,549,408-byte file under `dd7fcab672`, the parent's 4,929-byte README) and
lessans/gemma-4-E2B-it-uncensored (04-18, 10:46Z, "Duplicate from TrevorJS/gemma-4-E2B-it-uncensored", TrevorJS's
10,246,621,918-byte file under `8237e4818b`, the parent's README of that week), each equal to its parent's report
in every field with the parent's flags (1 and 3); and huihui-ai/Huihui-gemma-4-E2B-it-abliterated at the revision
round 13 had already measured against the same pin, which no checksum rule catches because the parent is the
copy itself. The pinner's note called the E2B copy unmeasured; the committed `results/weights/` held it by hub id
and revision. The three cost three downloads and three compares. Twenty-four of one hundred and nineteen distinct
copies are re-uploads, twenty of them with "Duplicate from" as the first commit title; round 25, pinned under
the rule, measured none, and rounds 26 and 29, pinned before it, measured seven (finding 56), three of them one file
under three account names made in forty minutes. Evidence: `results/weights/laladream-gemma-4-12B-it-uncensored.json`,
`results/weights/lessans-gemma-4-E2B-it-uncensored.json` and
`results/weights/huihui-ai-Huihui-gemma-4-E2B-it-abliterated.pass-2.json` against their parents' reports, the
commit titles and checksums in the readings in `docs/cards/`, and `data/batches/round-22-batch-1.json`.

Round 31 adds a fifth case read from the commit title alone: nguyenthilaitrieulong's one commit "Duplicate from
WWTCyberLab/gemma-4-31B-it-abliterated" of 08-04, whose parent is unmeasured, so the download was worth its cost
and the pair belongs under the parent's name (finding 64).

Round 33 adds the case the rule must not match. Three E4B Heretic exports of one original (p-e-w, sh0ck0r,
BinxNet) share two of their four shard checksums with each other and with four earlier E4B copies, and callmegrr's
31B export shares its second shard with Sabomako's and llmfan46's, because those shards hold tensors no Heretic
edit touches (the token embedding alone, the vision tower, the 31B's layers 48 to 59); the other shards are each
copy's own and no measured field is shared. The rule compares every weight file: a repository is a duplicate when
all of its checksums equal a measured copy's, and a shared subset is the library's shard layout (finding 71).
Round 34's pinner refused liskasYR/gemma-4-12B-it-qat-q4_0-unquantized-heretic, one commit "Duplicate from" igorls's
QAT copy with igorls's shards, and admitted eadx's one-commit duplicate of huihui-ai's QAT 26B-A4B edit because the
parent was never measured and the hub no longer serves it (finding 73). Round 38 adds another case read from the commit title and the checksum before any download: Himanshuoo8's one commit "Duplicate from DavidAU/gemma-4-E4B-it-Claude-Opus-4.5-HERETIC-UNCENSORED-Thinking", the weight file byte-equal to DavidAU's unmeasured fine-tune over coder3101's E4B edit, measured as that edit (finding 97).

## 39. A model family the judging library cannot load reads six unexplained configuration fields on every copy

Every Gemma 4 12B copy measured against Google's `config.json` (written by hand under transformers 5.10.0.dev0) and
saved under a later library reads the same six fields as unexplained: `config.audio_config.audio_samples_per_token`,
`config.audio_config.hidden_size`, `config.audio_config.output_proj_dims` and `config.vision_config.model_patch_size`
(640, 640, 640 and 48 in Google's file, absent from the copy's) and `config.audio_config.dtype` and
`config.vision_config.dtype` (null in Google's file, `bfloat16` in the copy's). Round 19's four (saved under 5.12.0,
5.12.0, 5.12.1 and 5.10.2) make twelve reports in six rounds, counting igorls's, lemuralabs's and richardyoung's round 8
pairing (saved under 5.10.1, 5.10.1 and 5.12.1), which read the same four absent fields. The fields are the saving library's doing, as finding 11
established, and the cards say "unexplained" because of the judging library, not the copy: the family's top-level
`model_type` is `gemma4_unified`, which neither the cluster's 4.56.2 nor the home venv's 5.6.2 of the time knows, so
`AutoConfig.for_model` raises "Unrecognized model identifier", the kit's class-default lookup returns nothing, and
no rule can fire. Loaded under 5.12.0 at home, Google's file and each copy's give 640, 640, 640 and 48, while a
fresh `gemma4_unified` configuration leaves its audio and vision sub-configurations empty, so a default lookup would
still fail there; the rule that closes the four has to load both saved files and compare what the library reads.
Two rules were added in round 19 (`audit/compare.py`, tests in `tests/test_resave.py`): a sub-configuration data
type written where the other side left it null repeats the top-level declaration, and an absent field that both
saved configurations load to the same value is a re-save, with the library version in the reason. Under 5.12.0 the
four pairs close all six fields and two of them read "consistent with re-save noted" (the other two keep a template
difference); under 5.6.2 they close two. The home venv now runs transformers 5.22.1, and every 12B report with the four
fields open (twelve, in six rounds: igorls in round 7, TrevorJS and richardyoung's round 8 pairing, AEON-7 and llmfan46
in 13, lemuralabs in 16, coder3101 and 3MPER0RR in 18, and round 19's four) was judged again under it: the four fields
close on all twelve, six reports move to "consistent with re-save noted" (TrevorJS, coder3101, igorls, lemuralabs,
prithivMLmods and Iambackup) and six keep one other open field (the template on Justbackup's, MeFFyLe's and llmfan46's,
the `per_layer_config` map on 3MPER0RR's, `max_position_embeddings` on AEON-7's and the sub-configuration data types on
richardyoung's round 8 pairing). The committed reports carry that judgement, with the library version in each closed
field's reason. The same mechanism
explains the round's two 31B cards: MoonRide's 5.7.0 save adds `text_config.moe_intermediate_size` as null to a
5.5.0.dev0 file (closed by the 5.6.2 default) and 3MPER0RR's 5.16.1 save moves `global_head_dim` 512 and
`num_global_key_value_heads` 4 into a `per_layer_config` map under the ten global layers (closed by hand, twice
now). A metadata card should carry the judging library's version beside the two saved ones, so that "unexplained"
reads as what it is when the judge cannot load the file. Evidence: the four `results/meta/` reports of round 19's
12B pairs (the `reclassification` records and the reasons on the closed fields), `results/meta/MoonRide-gemma-4-31B-it-heretic-ara-custom.json`,
`results/meta/3MPER0RR-gemma-4-31b-it-3MPER0RR-abliterated.json`, the two judgements in `docs/census-round-19.md`
and the tests.

Round 30's two E4B copies, judged under 5.22.1, follow the 31B pattern: TheUmbraWalker's 5.6.2 save adds
`text_config.moe_intermediate_size` as null and closes by the default rule, moving the card to "consistent with
re-save noted"; OS-Software's 5.16.1 save closes the same field and keeps the `per_layer_config` form, the third
copy on it, closed by hand. Evidence: `results/meta/TheUmbraWalker-gemma-4-E4B-it-2-heretic.json` and
`results/meta/OS-Software-gemma-4-E4B-it-uncensored-heretic.json`.

Rounds 20 and 32, judged under 5.22.1, close the 12B family's six fields by tool for the first time, on
Ishowbackup's two re-uploads and MoonRide/gemma-4-12B-it-heretic (the four omitted defaults by the default rule,
the two sub-configuration data types by the data-type rule), and close ressl/gemma-4-31B-it-uncensored's template
by the later-revision rule, the first field that rule has closed at a round's own judgement: the copy carries
Google's 18,683-byte file of the 31B repository's 07-15 revision ("fix: chat template") against a pin of 06-03.
The `per_layer_config` form appears three more times, on sh0ck0r/Artemis-31B-v1.1-heretic (a 5.16 save on the
31B, the fourth) and on mewse's and OS-Software's copies on the QAT-unquantized 26B-A4B (5.15.0 and 5.16.1 saves
against a 5.6.2 original, the fifth and sixth), closed by hand each time. One rename the scorer has no rule for
stays open on DogOnKeyboard/Mistral-7B-Heretic: `torch_dtype` written as `dtype` by a 4.57.1 save against a
4.42.0 original, the same type on both sides. Evidence: the `reclassification` records in
`results/meta/Ishowbackup-gemma-4-12B-it-uncensored.json`, `results/meta/MoonRide-gemma-4-12B-it-heretic.json`,
`results/meta/ressl-gemma-4-31B-it-uncensored.json`,
`results/meta/mewse-gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ara.json`,
`results/meta/OS-Software-gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic-v2.json` and
`results/meta/DogOnKeyboard-Mistral-7B-Heretic.json`.

Rounds 22 and 25, judged under 5.22.1, close the 12B family's six fields by tool on four more copies
(RumiaChannel's, Vampelium's, laladream's and Carlosian's, saved under 5.10.2, 5.16.1, 5.12.0 and 5.12.1), moving
Carlosian's card to "consistent with re-save noted", and close `text_config.moe_intermediate_size` by the default
rule on all ten E2B and E4B copies of the two rounds (5.5.0 to 5.16.1 saves against 5.5.0.dev0 originals), moving
seven cards (WWTCyberLab's, both treadon pairs', wangzhang's) to the same reading. The `per_layer_config` form
appears twice more, on Vampelium's 12B copy (5.16.1, `global_head_dim` 512 and `num_global_key_value_heads` 1 into
a map, the seventh copy and the first 12B) and on Dingdust's E4B copy (5.16.1, the eighth), closed by hand. Three
template cases stay open that no rule reads: RumiaChannel's 18,682-byte file, refreshed by the maker the day after
Google's 07-20 Canonical file (18,683 bytes) and one byte short of it, which the later-revision rule does not match;
the earlier-revision template through a re-upload on laladream's and lessans's copies (TrevorJS's files of 06-03
and 04-02 under pins of 07-20 and 04-10); and DuoNeural's E4B copy, which ships no template at all. Two cards read
true differences correctly: jokernifty's four `dtype` fields (`bfloat16` to `float16`, with every tensor float16)
and Dingdust's three token ids written through by its parent's save. Evidence: the `reclassification` records in
`results/meta/RumiaChannel-gemma-4-12B-it-uncensored-ara-Refusals9.json`,
`results/meta/Vampelium-gemma-4-12B-it-heretic.json`, `results/meta/Carlosian-Gemma-4-12b-it-Abliterated.json`,
`results/meta/Dingdust-ContextPilot-E4B-heretic.json`, `results/meta/jokernifty-gemma-4-e4b-it-abliterated.json`
and `results/meta/DuoNeural-Gemma-4-E4B-Heretic.json`, and the two judgements in `docs/census-round-22.md` and
`docs/census-round-25.md`.

Rounds 26 and 29 close `text_config.moe_intermediate_size` by the default rule on eleven more reports, on 31B, E4B
and E2B copies as well as the 12B: Bahushruth's two, anlord's, NullpoLab's, alphakek's and six re-uploads. anlord's
E2B copy adds the ninth `per_layer_config` form and the first `vision_config.rope_parameters.rope_type` of `axial`,
the 5.19 library's name for the same vision rotary scheme, both closed by hand (`docs/census-round-26.md`). Round 36 reads the `per_layer_config` form on three more copies, OS-Software's 31B and 12B QAT exports (5.16.1 saves) and Mitchins's 26B-A4B QAT export (5.15.0), closed by hand each time; the home judgement under 5.22.1 moved no field on the round's eight reports (`docs/census-round-36.md`). Round 38 closes `text_config.moe_intermediate_size` at home on four more E4B and E2B cards and four audio and vision fields the 5.10.2 save leaves out on RumiaChannel's 12B card, all the same values under 5.22.1 (`docs/census-round-38.md`).

## 40. The diffusion variant of a mixture carries the same language stack under another prefix, and its first two edits reach the experts and miss them

google/diffusiongemma-26B-A4B-it is the block-diffusion form of Gemma 4 26B-A4B: `DiffusionGemmaForBlockDiffusion`,
a 256-token canvas, a denoising schedule in the generation settings (48 steps, times 0.4 to 0.8), and the same
30-layer mixture (hidden size 2,816, shared feed-forward 2,112, 128 experts of 704, global head dimension 512)
saved as 1,047 tensors: the instruct original's 1,013 language tensors under `model.decoder.` instead of
`model.language_model.`, four `self_conditioning` projections on the decoder, a `layer_scalar` on each of 30
encoder layers, and no audio tower; the chat template is the 26B-A4B's 17,466-byte file. The compare tool's naming
table did not list the prefix, so the two cluster reports read every changed tensor as kind "other" and ranked
nothing (21 and 68 flags of "unexpected change"); with `decoder.` in the table the home score reads the roles and
the real flags appear (40 and 86). The two edits measured differ in reach. edwixx's Heretic run (measured through
FredyRivera-dev's upload and nnnxnsn's duplicate, finding 9) changes 67 tensors: the attention outputs of layers 5
to 29, the down projections of 7 to 29 and the packed expert down tensor of layers 11 to 29, all 128 experts of
each, rank one along one direction per layer on the 47 edited (first share 0.957 to 0.989 on the dense matrices,
0.989 to 0.992 at the median expert), output side with weights of 0.87 to 1.31 on the down projections and 0.62 to
0.99 at the median expert, expert rows within 0.0013 and 20 dense matrices at the bfloat16 floor of a merge that
touched them without an edit. The card says the packed `[128, 2816, 704]` parameter was edited slice by slice
because the tool skips it by default, which is the first time a Heretic card reaches the experts of a Gemma 4
mixture (finding 20 has every other Heretic copy of this base leaving all 3,840 expert matrices alone).
Goodoldjam's E38 changes the 20 tensors its card names (attention outputs and down projections of layers 7 to 16,
largest absolute difference 0.2019, the card's `max_abs_delta` to its last digit) and no expert: five of the 20 are at the floor (relative
change 0.0014 to 0.0017, kept fractions 1.00 on both sides) and the fifteen edited are several directions per
matrix (first share 0.49 to 0.97, eighth 0.95 to 0.98) on the input side of the attention outputs (right-side
weights 1.15 to 1.95) with per-matrix directions unrelated across the two writers of a layer, under a card that
calls the edit "Heretic-based" and prints no kernel; the shape fits a composition of several search trials better
than any single kernel measured. Evidence:
`results/weights/FredyRivera-dev-diffusiongemma-26B-A4B-it-HERETIC-Uncensored.json`,
`results/weights/nnnxnsn-diffusiongemma-26B-A4B-it-HERETIC-Uncensored.json`,
`results/weights/Goodoldjam-DiffusionGemma-26B-E38-Abliterated-BF16.json` (each with the cluster's count in its
`rescoring` block), the layout notes in the three readings in `docs/cards/`, `audit/recipes.json` and
`tests/test_weights.py`. Round 34 adds the third copy of the base, Umranz's arbitrary-rank edit capped at layer 20: 38
of 1,047 tensors under the `model.decoder.` prefix, no expert touched, fifteen residues (finding 76).

## 41. A Heretic kernel reads back from the weights to the third decimal on every layer, under a card whose token files drop a thousand declarations

AISafety-Student/Ministral-3-8B-Reasoning-2512-heretic prints a Heretic 1.2 card: attention output weight 0.90 at
position 26.35 falling to 0.88 at distance 12.34, down projection 1.25 at 25.09 falling to 1.20 at distance 17.83,
per-layer directions. The weights carry every number. 45 of 531 tensors changed, the down projections of layers 8
to 33 and the attention outputs of 15 to 33, which are the layers the two kernels reach on a 34-layer model and
nothing else (486 tensors equal, the largest change outside exactly 0); each change is rank one (first share 0.989
to 0.996); the left kept fraction is below the right on 45 of 45; the two writers of a layer share one direction
(cosine 0.99998 to 1.0, the tightest in the census) that drifts across layers (0.35 to 0.86); and one minus the
left kept fraction reproduces the kernel on every layer, 0.882 to 0.903 to 0.891 on the attention outputs against
the card's 0.882 to 0.900 to 0.889 and 1.205 to 1.248 to 1.229 on the down projections against 1.202 to 1.250 to
1.228, within 0.004 everywhere. The one flag is a first share of 0.9893 against the entry's 0.99 floor. The token
side reads 1,003 unexplained fields that are one omission: the copy's 407-byte `tokenizer_config.json` carries no
`added_tokens_decoder` map (the original's declares 1,000 entries) and no `additional_special_tokens` list, while
`tokenizer.json` and the template are byte-equal on both sides and the fixed conversation renders identically; the
scorer had a rule for declarations that move between files and none for declarations that disappear while the
token file is shared, and the rule written for the case (finding 44) closes all 1,003, so the committed card reads
"consistent with re-save noted". This is the second copy measured on the Ministral 3 8B Reasoning original (ccharnkij's merged
adapter, finding 17, is the first) and the first ablation of it. Evidence:
`results/weights/AISafety-Student-Ministral-3-8B-Reasoning-2512-heretic.json`,
`results/meta/AISafety-Student-Ministral-3-8B-Reasoning-2512-heretic.json`, the kernel column in
`docs/cards/AISafety-Student--Ministral-3-8B-Reasoning-2512-heretic-b0a973c9.reading.md` and the direction file in the
pull copy (`wheat30/measurements/pair-5/weights.directions.safetensors`).

Round 20 adds the second copy that reads its kernel back to the third decimal: DogOnKeyboard/Mistral-7B-Heretic,
Heretic 1.0.1 on Mistral 7B Instruct v0.3, whose card prints the attention kernel 1.45 at layer 23.46 (minimum
1.12, width 12.18) and the down kernel 0.95 at 24.84 (minimum 0.59, width 18.53). The left kept fraction along
the one shared direction is one minus the kernel's weight on all 45 edited matrices within 0.003 (for example
-0.4398 against -0.438 on the attention output of layer 23 and 0.3784 against 0.377 on the down projection of
layer 8), with the windows to the layer (12 to 31 and 7 to 31) and the largest change outside them exactly 0.
Two exact read-backs on two Mistral-family bases, against three Gemma 4 12B copies of the same tool that read no
weight (finding 46). Evidence: `results/weights/DogOnKeyboard-Mistral-7B-Heretic.json`, the kernel column in
`docs/cards/DogOnKeyboard--Mistral-7B-Heretic-4aa7a592.reading.md` and the direction file in the pull copy
(`nautilus20/measurements/pair-8/weights.directions.safetensors`).

Rounds 26 and 29 read two more kernel pairs to the second decimal, paoloronco's on Mistral 7B (1.40 against the
card's 1.44 at the peak, 1.16 against 1.18 on the down projections) and minpeter's on the Voxtral text tower (1.26
against 1.27, 1.10 against 1.11), and one record to the third decimal, anlord's E2B copy, whose repository ships the
trial's four kernels in a file and whose weights return them on seven components (finding 59).

## 42. A rank-four transport edit reads as exactly rank four on the input side, with unrelated directions per matrix

OS-Software/gemma-4-E4B-it-uncensored-heretic prints a Heretic "v2.0.0.dev0+custom" card with a parameter table the
census had not seen: `start_layer_index` 18, `end_layer_index` 28, `transport` gaussian, `transport_rank` 4,
`row_normalization` none, targets `attn.o_proj` and `mlp.down_proj`, with five regularisation and weighting
numbers. The weights carry the shape numbers. 20 of 2,076 tensors changed, the attention outputs and down
projections of layers 18 to 27 (the window, end excluded) and nothing else; each change is rank four exactly, the
fourth cumulative share 0.999 to 1.000 and the fifth singular value 0, where the first share alone is 0.59 to 0.88;
the left kept fraction is above the right on all 20 (input side), with right-side weights of 1.08 to 2.26 on the
down projections rising with depth and 0.50 to 2.02 on the attention outputs; the two writers of a layer take
unrelated directions (cosine 0.005 to 0.147) and the layers agree at 0.21 to 0.42; the rows moved by 0.012 to
0.098 with no restoration. It is the third rank-stated subspace edit after null-space's eight directions (finding
29) and AEON-7's four (finding 34), and differs from both: those were output-side, norm-preserving and shared one
subspace across layers, this one is input-side, unrestored and per matrix, and its rank is a hard cut where
AEON-7's singular values dropped by 19 to 195 times. The scoring rules written for one direction count it as 40
flags; a first-k share with k read from the singular values and no within-layer constraint would count none.
Evidence: `results/weights/OS-Software-gemma-4-E4B-it-uncensored-heretic.json`, the per-layer table in
`docs/cards/OS-Software--gemma-4-E4B-it-uncensored-heretic-d5bcffe8.reading.md` and the direction file in the pull copy
(`wheat30/measurements/pair-3/weights.directions.safetensors`).

Round 32 adds the same maker's rank-four edit on a second base,
OS-Software/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic-v2 against the QAT-unquantized 26B-A4B:
the card's window (layers 12 to 19) on both writers, 16 matrices, fourth cumulative share 0.998 to 0.9995 with
the fifth singular value 0.0015 to 0.004 of the first, input side on 16 of 16, leading-direction weights of 0.68
to 2.45 on the attention outputs and 1.30 to 1.97 on the down projections, unrelated directions per matrix
(within a layer 0.002 to 0.12), rows moved 0.011 to 0.047 under the card's "none", 32 flags under the
one-direction rules. The two copies share nothing but the shape, which is the maker's build. Evidence:
`results/weights/OS-Software-gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic-v2.json`, the per-layer
table in `docs/cards/OS-Software--gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic-v2-5a3468ee.reading.md`
and the direction file in the pull copy (`nautilus32/measurements/pair-8/weights.directions.safetensors`). The maker's two later exports, searched on Japanese prompt sets with the tool's LoRA-adapter branch, read a few directions per matrix and not four, on the input side at 0.74 to 2.09 (finding 83). Round 36 adds the maker's rank-four edit on two more bases, the 31B and 12B QAT checkpoints, the same shape on both writers of the card's window with the rows unrestored, and places it: the leading input direction stands at 0.59 to 0.77 to the arbitrary-rank families of the two sizes where the output direction stands at 0.56 or less (finding 90).

## 43. Two Heretic passes on one base: both kernels' windows read back to the layer, and the leading direction reads neither strength

TheUmbraWalker/gemma-4-E4B-it-2-heretic carries two Heretic 1.3 cards, the second run on the first's output. The
first card's kernels (attention output 1.31 at 27.47 falling to 0.82 at distance 24.19, down projection 1.42 at
28.35 falling to 1.38 at distance 22.01) reach layers 4 to 41 and 7 to 41 on a 42-layer model, and those are the
73 changed tensors exactly (38 attention outputs, 35 down projections; 2,003 tensors equal, the largest change
outside exactly 0). The second card's kernels (1.49 at 25.80 falling to 1.40 at distance 8.12; 1.04 at 38.45
falling to 0.53 at distance 10.11) reach layers 18 to 33 and 29 to 41, and those are exactly the matrices that read
two directions: first share 0.50 to 0.70 on the attention outputs of 18 to 33 and 0.68 to 0.86 on the down
projections of 29 to 41, with the second singular value 0.40 to 0.99 of the first, where every other changed matrix
is rank one (first share 0.994 to 0.999) with the two writers of a layer on one direction (cosine 0.96 to 1.00).
The strengths do not read back: two projections at different weights along different directions sum to a rank-two
difference whose leading direction belongs to neither, so one minus the kept fraction gives 0.28 to 0.97 on the
rank-one attention outputs where the first card implies 0.83 to 1.02, and reads on the wrong side on ten of the 73.
The leading-direction measure that reads a single Heretic kernel to the third decimal (finding 41) reads a stacked
pair's windows and not its weights; a per-matrix rank-two decomposition reporting two directions and two kept
fractions would read both cards. Evidence: `results/weights/TheUmbraWalker-gemma-4-E4B-it-2-heretic.json`, the
two-kernel column in `docs/cards/TheUmbraWalker--gemma-4-E4B-it-2-heretic-0cbd2368.reading.md` and the direction file
in the pull copy (`wheat30/measurements/pair-4/weights.directions.safetensors`).

## 44. A tokenizer configuration that drops a thousand declarations the shared token file still carries, and the rule that reads it

Two copies in the census write a `tokenizer_config.json` whose added-token declarations differ from the original's
while their `tokenizer.json` is the original's under one SHA-256. AISafety-Student/Ministral-3-8B-Reasoning-2512-heretic
(round 30, pair 5) saves a 407-byte configuration with no `added_tokens_decoder` map where the original's declares
1,000 entries and no `additional_special_tokens` list, beside no `special_tokens_map.json`, over a
17,078,110-byte `tokenizer.json` equal to the original's (`57757562`). aifeifei798/Heretic-Scalpel-E2B (round 16, pair 6) goes the
other way: it writes the 24 control tokens of Gemma 4 into an `added_tokens_decoder` block that Google's
configuration does not carry, over Google's 32,169,626-byte `tokenizer.json` (`cc8d3a0c`). The scorer counted each
entry as an unexplained field, 1,003 on the first card and 25 on the second, because its rules explained
declarations that move between files and not declarations that one side lacks. The rule added for the case
triggers only when both manifests record `tokenizer.json` under one checksum. It then reads each declaration
present on one side against the shared file's own added-token records: a decoder entry must repeat the record
under its ID with every flag it writes, and a whole map must consist of such entries; each token in an
`additional_special_tokens` list must be declared special in the shared file under the same ID. A declaration
present on both sides with different content stays unexplained, as does the whole family when the token file
differs. Judged again, the first card closes all 1,003 fields and reads "consistent with re-save noted" (its edit
is the weights, finding 41); the second closes its 25 and keeps six configuration and template fields open. Eight
other reports carry the same dropped map and stay as they were, because the rule's first condition fails: in five
the two sides' `tokenizer.json` differ (3MPER0RR's two reports, DuoNeural's, Felldude's, timfromhcs's), so a
dropped map cannot be read against a file the sides do not share, and in three one side ships no `tokenizer.json`
at all (grayarea's, huihui-ai's Mistral Small 3.2, nicoboss's). What the rule says about loading: a fast tokenizer
built from `tokenizer.json` carries these added tokens whether or not the configuration repeats them, so the
dropped entries change no ID and no flag; what a configuration with fewer declarations still changes is the
Python-side `additional_special_tokens` attribute, which is why the rule records the fields as explained by re-save
rather than as no difference. Evidence: `results/meta/AISafety-Student-Ministral-3-8B-Reasoning-2512-heretic.json`
with `results/meta/aifeifei798-Heretic-Scalpel-E2B.json`, whose `reclassification` blocks name the fields; the rule
in `audit/metadata.py` (`explain_shared_declarations`); its tests in `tests/test_resave.py`. Round 35's second measurement of Pranavz's copy against Hearthfire drops 1,000 control-token declarations with a `tokenizer.json`
155 bytes longer than the parent's, so the rule cannot read the drop against a shared file; the decoders themselves would have to be compared (finding 77).

## 45. A copy's named parent is a 4-bit round trip of the original, read from the hub by byte range without a download

sh0ck0r/Artemis-31B-v1.1-heretic names Google's 31B instruct model in its `base_model` field and
TheDrummer/Artemis-31B-v1.1, a fine-tune of it, in its README's first sentence; the pinner followed the field, and
the compare read 603 of 1,188 tensors changed against Google's file: every two-dimensional tensor in the model
(all 602 matrices) and the one three-dimensional tensor, by 8.75 to 10.45 percent of the norm, median 9.39, with no
dependence on layer or kind, and all 585 vectors equal. That is not an ablation's footprint. To find whose it was,
the same four tensors were fetched whole from the three repositories by HTTP byte-range requests against the
hub's safetensors files, the offsets taken from each file's header (`tools/hub_range_read.py`), without
downloading any checkpoint. In TheDrummer's file a vision projection holds at most 16 distinct values in every
block of 64 entries (median 14 over the first 4,000 blocks), 14.58 percent of its entries are exactly zero, and it
differs from Google's by 0.1029 of its norm; a key projection of layer 30 (56 distinct values per block, 0.0975)
and a query projection of layer 0 (45, 0.0929) read the same way, and a layer norm is byte-equal to Google's.
sh0ck0r's bytes equal TheDrummer's on all three matrices that no Heretic kernel touches, and differ from them by
0.0114 on an attention output of layer 45 and 0.0185 on a down projection of layer 30: the ablation. The signature
(sixteen levels per block of 64, one seventh of the entries at zero, a flat difference spectrum with the first
singular value 0.118 of the norm and the five-hundredth 0.040) is that of weights quantised to 4-bit normal floats
in blocks of 64 and written back to bfloat16, with the low-rank adapters of the stated training merged on top;
TheDrummer's card states a 4-bit training recipe. The measure read the ablation through the round trip where the
kernel's weight rises above the 9 percent floor: the leading direction on the down projections of layers 17 to 54
and the attention outputs of 33 to 59 is the Heretic direction (group cosine 0.88 to 0.999) and elsewhere the
noise, and the kept fractions on the down projections of 40 to 54 are within 0.02 to 0.16 of the card's kernel.
What it means: a `base_model` field one step above the true parent turns a clean 120-matrix edit into a 603-matrix
comparison, and the comparison then measures the parent. The pinner needs a parent rule that reads the README's
first sentence before the field, and TheDrummer/Artemis-31B-v1.1 belongs in the batch as a copy in its own right.
To reproduce: run the range-read tool (`hub_range_read.py` in `tools/`) with `--tensor` and the tensor's name,
followed by the three repositories at their revisions (`google/gemma-4-31B-it@842da379`,
`TheDrummer/Artemis-31B-v1.1@d613e5a4`, `sh0ck0r/Artemis-31B-v1.1-heretic@b3bdce6a`), with a hub token in the
environment; it prints the relative differences, the byte equality and the distinct-values-per-block statistic
for the named tensor. Evidence: `results/weights/sh0ck0r-Artemis-31B-v1.1-heretic.json` (603 changed tensors, the
`rescoring` block), the reading and the kernel table in `docs/cards/sh0ck0r--Artemis-31B-v1.1-heretic-a15d36ac.reading.md`.

Round 29 used the same tool on Felldude/gemma-4-E4B-uncensored against google/gemma-4-E4B and google/gemma-4-E4B-it,
fourteen tensors by byte range, and placed the copy on the instruct model (finding 62). Round 31 used it on three
tower matrices of Ilya626's E4B copy, which read as Gaussian draws at the library's default scale (finding 63), and
on layer 56 of nguyenthilaitrieulong's 31B copy against huihui-ai's second version (finding 64); the same round
placed a parent without it, from the saved direction vectors (finding 66). Round 35 measured the copy against TheDrummer/Artemis-31B-v1.1 itself: 73 matrices, exactly 0 outside, and the kernels this
finding read through the round trip agree with the ones read against the parent to the second decimal of the kept fractions (finding 77).

## 46. Three Heretic copies of Gemma 4 12B read one shared direction and no weight, where the same tool on two Mistral bases reads its kernel to the third decimal

MoonRide/gemma-4-12B-it-heretic (round 20, Heretic 1.3.0: direction index 29.60, attention kernel 1.35 at 31.80
with minimum 0.88 and width 15.78, down kernel 1.39 at 42.25 with minimum 1.16 and width 15.71) changes exactly
the layers those kernels reach (attention outputs 17 to 47, down projections 27 to 47), with one direction shared
by every edited matrix (group cosine 0.90 to 0.999) and rank one everywhere, and its kept fractions read nothing:
the left runs -0.26 to 0.97 on the attention outputs and -0.25 to 0.73 on the down projections, the right 0.22 to
0.90 and 0.02 to 0.42, the left below the right on 25 of 52, with no trend across the window where the kernel's
one-minus-weight would run from 0.12 at the edges to -0.35 and -0.39 at the centres.
3MPER0RR/gemma-4-12b-it-3MPER0RR-abliterated (round 18) and prithivMLmods/gemma-4-12B-it-heretic_decensored (round
19, finding 43) read the same way on the same base: one shared direction, the window to the layer, kept fractions
that carry no weight. On Mistral 7B Instruct v0.3 (DogOnKeyboard, round 20) and Ministral 3 8B Reasoning
(AISafety-Student, round 30, finding 41) the same tool's kernels read back within 0.003 on every matrix. The
difference is in the base. On the Mistral models the projection is the whole change (first share 0.976 to 0.996)
and one minus the kept fraction is the weight; on Gemma 4 12B the first share is as high (0.978 to 0.997) and the
kept fractions scatter anyway, which the measure cannot yet explain: a projection along a direction that differs
from the one the difference reports, or a step between the projection and the saved matrix that the measure does
not model, would both give it. Until that is settled, a Heretic entry for Gemma 4 12B can carry a window and a
direction count but no weight. Evidence: `results/weights/MoonRide-gemma-4-12B-it-heretic.json`,
`results/weights/3MPER0RR-gemma-4-12b-it-3MPER0RR-abliterated.json` and
`results/weights/prithivMLmods-gemma-4-12B-it-heretic_decensored.json` against
`results/weights/DogOnKeyboard-Mistral-7B-Heretic.json` and
`results/weights/AISafety-Student-Ministral-3-8B-Reasoning-2512-heretic.json`, and the readings in `docs/cards/`.

Round 22 reads a fourth Heretic copy of the 12B that does carry a weight. Vampelium/gemma-4-12B-it-heretic, under
a card of three sentences that prints no kernel, changes the attention outputs of layers 5 to 47 and the down
projections of 16 to 47 with one nearly shared direction (group medians 0.996 and 0.998, the two kinds at 0.92),
output side on 75 of 75, and its left kept fractions run smoothly through both windows: 0.88 at layer 5 to -0.29
at 30 and 31 and back to 0.44 at 47 on the attention outputs, 0.90 at 16 to -0.41 at 35 and back to 0.36 at 47 on
the down projections, kernels peaking at 1.29 and 1.41. So the base is not the reason the three earlier copies read
no weight; something in those three edits is, and the measure cannot yet say what. A Heretic entry for Gemma 4
12B can carry a weight when the copy does. Evidence: `results/weights/Vampelium-gemma-4-12B-it-heretic.json` and
the reading in `docs/cards/`.

Round 33 adds two more Heretic copies of the 12B, and both read the scatter. BinxNet/gemma-4-12B-it-heretic
(Heretic 1.4.0: attention kernel 1.44 at 28.65 with minimum 0.11 and width 25.21, down kernel 1.48 at 32.22 with
minimum 0.97 and width 5.73) changes exactly the layers the kernels reach (attention outputs 4 to 47, down
projections 27 to 37) with one shared direction (group medians 0.97 and 0.99), and its left kept fractions read
0.93 at layer 12, 0.97 at 20, -0.44 at 29, 0.87 at 32 and 0.97 at 47 where the kernel's one minus weight would
run 0.44, 0.02, -0.42, -0.26 and 0.53: the peak layer reads and the layers three away read nothing, the left below
the right on 24 of 55, while the relative changes themselves follow the kernel (0.0022 at layer 4 rising to 0.032
at 20 and 32). igorls/gemma-4-12B-it-qat-q4_0-unquantized-heretic, on the QAT checkpoint, reads its down kernel
(1.43 to 1.48) within 0.14 on layers 32 to 44 and scatters on all 32 attention outputs (finding 69). The same
maker's E4B export four days after the 12B, with the same tool version, reads its heights within 0.3 at the peak,
as do three other E4B exports of the round (finding 59). Round 34 reads the scatter on an E4B for the first time, on
the QAT checkpoint: prithivMLmods's export reads its down kernel's slope 0.05 to 0.35 under the height and its
attention heights at 1.09 to 1.19 on layers 24 to 27 and 0.29 to 0.67 on 18, 32, 37 and 39 under a kernel of 1.17
to 1.36 (`results/weights/prithivMLmods-gemma-4-E4B-it-qat-heretic_decensored.json`). Five 12B copies now read the scatter against Vampelium's, which
reads its heights, and two Google checkpoints of the 12B behave alike, so the open question of this finding is about
the 12B's weights and the tool together rather than the base alone. Evidence: `results/weights/BinxNet-gemma-4-12B-it-heretic.json`,
`results/weights/igorls-gemma-4-12B-it-qat-q4_0-unquantized-heretic.json` and the readings in `docs/cards/`. TheUmbraWalker's first E4B pass (round 37) reads the same way, one direction per layer and kept fractions with no kernel shape, under a card that prints two kernels (finding 85). Round 36 reads the scatter twice more: JJaguar's kernel pass of the 12B QAT checkpoint keeps -0.24 to 0.89 on the left and -0.05 to 0.86 on the right under kernels of 1.20 to 1.43 (finding 91), and Mitchins's transferred kernel on the 26B-A4B QAT checkpoint reads no kernel on the attention outputs, the dense down projections or the experts (finding 92). Round 38 reads a weight where the 12B passes read none: DuoNeural's E2B copy, one direction on both writers at one minus the left kept fraction of 0.75 to 1.43 on the down projections and 1.03 to 1.32 on the attention outputs, two kernels the card does not print, under a clean read of the single-projection entry (finding 96).

## 47. An ablation whose parameters are written into the configuration reads back from the weights to the third decimal on four writers

amkkk/Gemma4_E2B_Abliterated_Baked_HF_Ready carries twelve fields in `config.json`, repeated in an
`export_manifest.json`, that state the edit: `ablation_layers` (9 to 13, 15 to 32, 34), strengths of 1.0 on
the attention output and the down projection and 1.2 on the gate and up projections, `direction_source`
"module_input_directions". Measured against google/gemma-4-E2B-it, 96 of 1,951 tensors changed, the four named
writers of the twenty-four listed layers and nothing else (layers 14 and 33 untouched, the largest change outside
the set exactly 0), every change rank one (first share 0.977 to 0.998), input side on 96 of 96, and the right kept
fraction is one minus the stated strength on every matrix: -0.024 to 0.008 on the 48 attention outputs and down
projections (strength 1.0) and -0.1991 to -0.2004 on the 48 gate and up projections (strength 1.2). The gate and
up projections of a layer, which read the same input, share their direction at 0.92 to 0.97, and the attention
output and down projection read their own (0.11 to 0.71 to each other), as "module input directions" says. The
export also drops the 60 tensors of layers 15 to 34 (key projections, value projections, key norms) that the
model never reads. This is the cleanest read-back in the census, on a copy for which no recipe entry exists (136
flags: the gate and up projections are not listed writers and the input side is not the listed side), and it
calibrates the measure for four-writer input-side projections: an entry that names the four writers and reads
the strength per writer would count no flag. Evidence:
`results/weights/amkkk-Gemma4_E2B_Abliterated_Baked_HF_Ready.json` (the `remaining_along_direction` right values
on the 96 changed tensors), `results/meta/amkkk-Gemma4_E2B_Abliterated_Baked_HF_Ready.json` (the twelve fields)
and the table in `docs/cards/amkkk--Gemma4_E2B_Abliterated_Baked_HF_Ready-bb7e3bc0.reading.md`.

Round 22 adds a second four-writer E2B copy on the same 24 layers from another maker,
WWTCyberLab/gemma-4-E2B-it-abliterated, whose card names two writers and a scale of 1.50 and whose weights read
four writers and a scale per layer: 1.31 to 1.51 on layers 9 to 32 and 2.40 on layer 34, the same number to three
decimals on the attention output, down, gate and up projections of a layer, output side on the first two and
input side on the last two (finding 53). No field equals amkkk's. Evidence:
`results/weights/WWTCyberLab-gemma-4-E2B-it-abliterated.json` and the reading in `docs/cards/`.

Round 26 adds a record shipped as a file beside the weights rather than in the configuration:
anlord/gemma-4-E2B-it-abliterated's `abliteration_reproduction.json` states four Gaussian kernels on seven
components, and the kept fractions return every one of its eight numbers to the third decimal (finding 59).

## 48. Three QAT-unquantized originals enter the census, and two copies' `base_model` fields name the instruct model while their READMEs name the QAT checkpoint

Google publishes, beside each Gemma 4 instruct model, a checkpoint extracted from quantisation-aware training
under a name ending in `-qat-q4_0-unquantized`, in bfloat16. Round 32 measured the first four copies on three of
them: huihui-ai's 12B abliteration (finding 21), mewse's and OS-Software's 26B-A4B edits (findings 22 and 42) and
coder3101's E2B edit (finding 22). Against the QAT originals all four read exactly 0 outside their windows
(0.000767 on one in-window residue of coder3101's), which places each copy on the QAT checkpoint and not on the
instruct model. Two of the four, mewse's and OS-Software's, name the instruct model google/gemma-4-26B-A4B-it in
their `base_model` field and the QAT checkpoint in their README's first sentence; the pinner paired them by hand
from the README. Paired by the field, the comparison would have read the difference between the two Google
checkpoints on every matrix the QAT retraining moved, beside the edit, and the copy would have read as a
fine-tune, as finding 45's grandparent pairing did. The QAT originals differ from the instruct files on the token
side and in the tensor set: the 26B-A4B QAT configuration is a 5.6.2 save where the instruct pin is 5.5.0.dev0,
and the E2B QAT file carries 1,951 tensors to the instruct file's 2,011, the 60 unused shared-KV tensors absent.
A `base_model` check that reads the README when the name ends in `-qat-q4_0-unquantized` is owed to the pinner,
and the remaining QAT copies at every size belong in the next batches now that the originals are known to pair.
Evidence: `results/weights/huihui-ai-Huihui-gemma-4-12B-it-qat-q4_0-unquantized-abliterated.json`,
`results/weights/mewse-gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ara.json`,
`results/weights/OS-Software-gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic-v2.json`,
`results/weights/coder3101-gemma-4-E2B-it-qat-q4_0-unquantized-heretic.json` (the `census` blocks record the QAT
revisions) and `data/batches/round-32-batch-1.json`.

Round 25 adds a third case, where the true parent is named in the README's second card and not in the field:
Dingdust/ContextPilot-E4B-heretic names Google and carries tencent/ContextPilot-E4B's fine-tune under its edit
(finding 54). The check that reads the README's first sentence has to read its second card too.

Round 33 measured the fifth copy on a QAT original, igorls/gemma-4-12B-it-qat-q4_0-unquantized-heretic against
google/gemma-4-12B-it-qat-q4_0-unquantized at `58540658`: 57 matrices changed in the card's two windows and exactly
0 outside them, so the copy stands on the QAT checkpoint; its `base_model` field names the QAT checkpoint, as huihui-ai's
and coder3101's do (finding 69). The two wrong fields above are read by finding 67 as Heretic's inherited header:
the QAT checkpoints' own cards name the instruct model in their `base_model` field (`data/batches/round-32-batch-1.json`
records it for all three), and the tool's card carries that field forward. Round 34 measured seven more copies on
QAT checkpoints, the E4B's among them for the first time, every one exactly 0 outside its window and every field
naming the QAT checkpoint; one, smashingtags's, carries the instruct model's name and the QAT checkpoint's weights,
settled by byte range (finding 75). Round 35 places two more E4B copies on the QAT checkpoint by the same test, coder3101's and igorls's, exactly 0 outside their windows (finding 82). Round 37 adds the 31B QAT checkpoint as the census's fifth QAT original with wnfldchen's merged export, and three more copies on the 12B and 26B-A4B checkpoints, every one exactly 0 outside its window (findings 83 and 84). Round 36 adds eight copies on the QAT checkpoints, three on the 31B's and two on the 26B-A4B's with three on the 12B's, every one exactly 0 outside its window or under 0.001 on the window's own residues; four of them, OS-Software's three and JJaguar's, name the instruct model in the field and the QAT checkpoint in the README's first sentence, the case this finding opened, and the pinner paired them by the name rule in `docs/weights-method.md` (findings 89 to 93).

## 49. An ablation with a fine-tune laid over it, under a template edit that changes the generation prompt

DavidAU/gemma-4-E2B-it-The-DECKARD-HERETIC-UNCENSORED-Thinking says "uncensored, then fine tuned" and little else.
Against google/gemma-4-E2B-it, 205 of 2,011 tensors changed: every projection the model has (the query, output,
gate, up and down projections of all 35 layers, and the key and value projections of the 15 layers that own
them), by 0.2 to 4.8 percent, in a low-rank shape (first share 0.54 to 0.97, fourth cumulative share 0.72 to
0.96), with no norm, embedding or tower tensor moved and the largest change outside the set exactly 0. On 189 of
the 205 the kept fractions read within 0.04 of 1 on the right side: the training moved the matrices without
removing a direction. On the attention outputs of layers 16 to 31 they read 0.65 to 0.97 on the left and -0.47 to
0.39 on the right, output side on all 16, with the model's largest changes (2.4 to 4.9 percent): a sixteen-layer,
one-writer ablation under the training. It is the mirror of finding 18's training-then-ablation pair, and like
it cannot be fitted by a recipe until the training is measured as a separate term. The token side adds
something new: the copy's `chat_template.jinja` (16,352 bytes) is Google's pinned file (16,804) with one edit, a
`<|think|>` line emitted after the generation prompt, committed by the maker a day after the weights ("Update
chat_template.jinja", 05-17) and two minutes before the README that names the thinking mode; the fixed
conversation renders one line longer than the original's. The template edits the census has read so far
(findings 16, 19, 23 and 28) carry a system text, a thought block in earlier model turns or another revision's
file; this one changes the generation prompt itself, so what the model is asked to continue differs from the
original on every turn. The metadata tool reports it as two unexplained fields, which understates it; a card line
for a template that changes the rendering is owed. Evidence:
`results/weights/DavidAU-gemma-4-E2B-it-The-DECKARD-HERETIC-UNCENSORED-Thinking.json`,
`results/meta/DavidAU-gemma-4-E2B-it-The-DECKARD-HERETIC-UNCENSORED-Thinking.json` (the
`rendered_template.default` field) and the reading in `docs/cards/`. Round 38 reads the shape a second time, on the E4B through Himanshuoo8's duplicate of DavidAU's copy: coder3101's Heretic edit at 1.000 on 20 of 21 attention outputs under an Unsloth fine-tune of 0.1 to 0.7 percent on every linear map, a thinking template and no generation configuration (finding 97).

## 50. A measurement repeated on one system agrees to the last digit, and a re-upload's parent read eight rounds later agrees with it field for field

Round 22 measured huihui-ai/Huihui-gemma-4-E2B-it-abliterated at revision `3d1e3d50` against google/gemma-4-E2B-it
at `4742fe84` on Blueback, the pair round 13 had measured on the same system against the same pin, because the
batch note of 10-31 called the copy unmeasured. Every measured field of all 2,011 tensors in the second report
equals the first to the last digit, the singular values and the sketched fields included, on the same modified
shard (`90daa0b268`): 50 changed, weight 1.00 on both writers of layers 10 to 34, 0 flags, 1,961 tensors equal to
the original. Round 3's second pass had settled the same point on Nautilus for five pairs; this is the first
repeat on Blueback and the first with the direction vectors saved on both passes. The same round measured
huihui-ai/Huihui-gemma-4-31B-it-abliterated, the first version, which round 18 had read only through
prithivMLmods/gemma-4-31B-it-Uncensored-MAX: every field of all 1,188 tensors equals the re-upload's report (120
changed, weight 1.00 on all 60 layers, 52 flags at the floor), with no checksum shared between the two
repositories (two shards against ten). Two consequences for the census. A re-upload measured before its parent
is the parent's measurement, and the field test confirms it when the parent arrives, as it did here and for the
E4B, 26B-A4B and E2B copies of the same maker (finding 9). And the pinner needs a second rule beside the checksum
rule of finding 38: a hub id and revision already present in `results/weights/` is measured, whatever a batch
note says. How to reproduce: `results/weights/huihui-ai-Huihui-gemma-4-E2B-it-abliterated.pass-2.json` against
`results/weights/huihui-ai-Huihui-gemma-4-E2B-it-abliterated.json`, and
`results/weights/huihui-ai-Huihui-gemma-4-31B-it-abliterated.json` against
`results/weights/prithivMLmods-gemma-4-31B-it-Uncensored-MAX.json`, compared per tensor on every key; the readings
in `docs/cards/`.

Rounds 26 and 29 add seven re-uploads measured against later Google revisions than their parents were (Ishowbackup's
E2B against the 07-20 revision where round 13 read TrevorJS's against 04-02; akpsahan's 31B against 07-20 where round
12 read huihui-ai's against 04-10), every field equal to the last digit: Google's revisions change templates and
configuration files and never the weight shards (finding 56).

## 51. A float16 copy reads no storage floor, and a token-embedding projection reads along the hidden axis

jokernifty/gemma-4-e4b-it-abliterated is a single orthogonal projection, `W_new = W - (r r^T) W` with the direction
taken at layer 25 from 32 harmful and 32 harmless prompts, on `self_attn.o_proj`, `mlp.down_proj` and the token
embedding of text decoder layers 20 to 34 of google/gemma-4-E4B-it, as its card says, and the copy is saved in
float16 where every other copy in the census is bfloat16. Measured, 31 of 2,076 tensors changed, the card's 31,
with 1,709 equal to the original and 336 moved by at most 0.0000011 of their norm (the smallest values of the
per-layer input gates and the vision patch embedder, rounded by the storage change). The 30 projections read one
shared direction (0.9999999 or better) at a left kept fraction within 0.00005 of 0, weight 1.0000, output side on
30 of 30, and a first share of 0.99988 to 0.99993 at relative changes of 0.019 to 0.0225. On every bfloat16 copy
at that edit size the first share reads 0.989 to 0.997, because the bfloat16 rounding of a rank-one edit leaves
0.0013 to 0.0016 of the norm outside the first direction (finding 3); here it leaves 0.00009. The floor is the
storage type's, confirmed from the other side on a maker's file rather than a synthetic one. The embedding reads
the same direction with the sides swapped: right kept fraction 0.00002 along the hidden axis, left 0.943 across
the token rows, relative change 0.0188, which is what projecting a direction out of every token row gives and
which finding 6's one-layer patch and finding 30's thirteen scaled rows did not show. The configuration declares
the change the card omits: `dtype`, `text_config.dtype`, `audio_config.dtype` and `vision_config.dtype` read
`float16` against the original's `bfloat16`, and the metadata tool reads the four as unexplained, which is correct
and understated. The scorer's first-share floor of 0.99 should be read beside the storage type: on a float16 or
float32 save it is a real line, on a bfloat16 save it is the floor. How to reproduce:
`results/weights/jokernifty-gemma-4-e4b-it-abliterated.json` (`first_singular_energy_share` and
`remaining_along_direction` on the 31 changed tensors, `dtype_modified` on every tensor),
`results/meta/jokernifty-gemma-4-e4b-it-abliterated.json`, and the reading in `docs/cards/`.

## 52. Two norm-preserving projections applied in sequence read as two directions where both reach, with both scales and both layer sets

treadon's four copies of round 25 are two edits and their two compositions. The abliterations
(treadon/gemma4-E4B-it-abliterated, treadon/gemma4-E2B-it-abliterated) read as their cards say with no flag: one
direction per layer, output side, rows restored within 0.0003, scale 1.0 on 17 layers of the E4B (left kept
fraction within 0.013 of 0 on all 34 matrices) and scale 1.75 on 24 layers of the E2B (-0.744 to -0.760 on all
48). The compositions (the `Abliterated-AND-Disinhibited-USE-THIS` copies) apply a "disinhibition" at scale 1.5 on
the top 20 layers first and the abliteration recomputed on the disinhibited model second, and the weights read
both. On the E4B, 42 matrices of 21 layers changed: layer 17 carries one direction at scale 1.0 and equals the
abliteration-only copy in every field; layers 20, 29, 39 and 40 carry one direction at -0.50 (scale 1.5, the
disinhibition alone); the 16 other layers carry two directions, first share 0.66 to 0.76 and fourth cumulative
share 0.993 to 0.998, with the disinhibition's -0.50 leading. So the disinhibition touched 20 layers and the
abliteration 17, the card's counts, and the recomputed abliteration chose layers 36 to 38 over 20, 21, 29 and 35
of the stand-alone copy's set. On the E2B, the same 48 matrices as the abliteration-only copy changed: layers 10,
12, 13 and 15 carry one direction at -0.75 (the abliteration alone) and the 20 others two (first share 0.54 to
0.63, fourth share 0.997 to 0.999) with the abliteration's -0.75 leading; no field equals the stand-alone copy,
because its direction was recomputed. The recipe scorer counts 32 and 42 flags on the compositions because two
directions are not one; an entry for a composed edit would read the fourth cumulative share and one scale per
direction and count none. This is the first pair of copies in the census where a composition and its parts are
all published and all measured, and the parts read back inside the whole to the number. How to reproduce: the
four `results/weights/treadon-*.json` reports (`energy_shares`, `remaining_along_direction` per tensor; the two
layer-17 tensors of the E4B pair compared on every key), and the readings in `docs/cards/`.

## 53. Two makers' four-writer edits of the E2B choose the same 24 of 35 layers, one at a scale per writer and one at a scale per layer

amkkk/Gemma4_E2B_Abliterated_Baked_HF_Ready (round 32, finding 47) lists its layers in `config.json`: 9 to 13, 15
to 32 and 34. WWTCyberLab/gemma-4-E2B-it-abliterated (round 22), created on 2026-04-06 by another maker, says "24
of 35 total layers modified" and shows a chart. The two copies change exactly the same 96 tensors of
google/gemma-4-E2B-it, the attention output, down, gate and up projections of those 24 layers, and no measured
field is equal between them. amkkk's edit reads a scale per writer kind, 1.0 on the attention outputs and down
projections and 1.2 on the gates and up projections, the same on every layer, all four on the input side.
WWTCyberLab's reads a scale per layer, 1.31 to 1.51 on layers 9 to 32 and 2.40 on layer 34, the same number to
three decimals on all four writers of a layer (the right kept fraction on the gate and up projections equals the
left on the attention output and down projection), with the attention output and down projection on the output
side and the gate and up projections on the input side, under a card that names two writers and "Ablation Scale
1.50". Both read one direction per layer shared by the four writers. The layer choice, made by two makers from
the per-layer refusal signal of one original, is the signal's: the same 24 layers with 14 and 33 left out both
times, and treadon's E2B copies (finding 52) take the same 24 with 34 traded for 33. WWTCyberLab's "norm-
preserving" holds on its two input-side writers (rows within 0.0006) and not on its two output-side ones (rows
moved 0.005 to 0.052, and 0.83 and 1.05 on layer 34). An entry that names the four writers, a side per writer and
a scale per writer or per layer would read both copies with no flag; the table counts 136 and 48. How to
reproduce: `results/weights/WWTCyberLab-gemma-4-E2B-it-abliterated.json` against
`results/weights/amkkk-Gemma4_E2B_Abliterated_Baked_HF_Ready.json` (the changed-tensor sets, the
`remaining_along_direction` values by layer), and the readings in `docs/cards/`.

## 54. A README that carries two cards: the field names Google, the second card names the fine-tune the weights carry, and the Heretic windows read to the layer under it

Dingdust/ContextPilot-E4B-heretic's `base_model` field names google/gemma-4-E4B-it and its README is two cards in
one file: a Heretic record (direction index 31.13, the attention outputs at weight 1.38 centred on layer 36.40 with
minimum 0.09 at distance 12.19, the down projections at 1.41 centred on 40.24 with minimum 1.39 at distance 13.62,
32 refusals in 100 against 100) followed by tencent/ContextPilot-E4B's card, a reinforcement-learning fine-tune of
the E4B for context management, byte for byte in its body. The pinner read the field and paired the copy with
Google's E4B. Measured so, 285 of 2,076 tensors changed and 189 more sit at the threshold: every down projection,
most gates, up projections, queries, keys and values, and 48 normalisation and gate vectors, moved by 0.1 to 0.4
percent with no leading direction and rows within 0.0001, which is training. Inside that, the card's two kernels
read to the layer: 1.38 at 36.40 with width 12.19 reaches layers 25 to 41, and the attention outputs of exactly
those 17 layers carry a leading direction (first share 0.74 at 25 rising to 0.99 at 36) where layers 1 to 24
carry none; 1.41 at 40.24 with width 13.62 reaches 27 to 41, and the down projections of exactly those 15 carry
one (first share 0.978 to 0.988) where 0 to 26 carry none. The strengths read shallower than the card under the
training: the down kernel's -0.40 reads -0.32 to 0.09, the attention kernel's shape reads on layers 25 to 36 and
scatters after. The token side reads the parent too: `bos_token_id`, `eos_token_id` and `pad_token_id` written
through by the fine-tune's save, and Google's earlier template under a later pin, inherited. This is finding 18's
case (an ablation on a fine-tune, measured against the grandparent) and finding 48's (a field that names the
wrong parent), met together: the true parent is named in the file and not in the field, the `base_model` check
has to read the README's second card, and against tencent/ContextPilot-E4B, unmeasured, the comparison would read
the kernels alone. How to reproduce: `results/weights/Dingdust-ContextPilot-E4B-heretic.json` (the changed set by
kind, `first_singular_energy_share` by layer on the attention outputs and down projections against the card's
kernel windows), `results/meta/Dingdust-ContextPilot-E4B-heretic.json`, the README's two halves, and the reading
in `docs/cards/`.

Round 29 adds the third copy whose README names the parent its field does not: Pranavz/Hearthfire-24B-heretic's
title names LatitudeGames/Hearthfire-24B and its `base_model` field names Mistral Small 3.2, and against the field's
pin the fine-tune reads under the kernels on all 40 layers (finding 61). The check has to read the README's title
as well as its second card.

## 55. A five-component edit reads four components with a weight band per kind, and a window four layers above the card's

wangzhang/gemma-4-E2B-it-abliterated, made with the maker's Abliterix tool, says it projects the refusal direction
out of the attention query, key, value and output projections and the down projection ("5 steerable components ×
27 effective layers") on layers 5 to 30 of 35, rows preserved, with a 100-trial Optuna search choosing trial 60.
Measured against google/gemma-4-E2B-it, 72 of 1,951 tensors changed and nothing else: the attention outputs of
layers 9 to 34, the values of 9 to 14, the down projections of 14 to 34 and the queries of 16 to 34. No key
projection changed, and the values of layers 15 to 34 do not exist in the copy (the export drops the 60 shared-KV
tensors), so the fifth component is absent and the third stops where the model stops carrying it. The window is
9 to 34, not 5 to 30: the lowest edit on every kind is at layer 9 or above and the highest at the last layer.
Within a layer the edited matrices share one direction (0.9994 or better across all four kinds); across kinds the
weight differs by band. The attention outputs read 1.91 at layer 9 rising to 3.12 at 27 and falling to 2.82 at 34
on the output side (left kept fraction -0.91 to -2.12), the values 2.31 to 3.02 on the input side (right -1.31 to
-2.02), the down projections 0.72 to 1.43 on the output side (left 0.28 at 14 through 0 at 22 to -0.43 at 33), the
queries 0.56 to 0.89 on the input side (right 0.11 to 0.44); rows within 0.0005 on all 72. The 3.12 is the largest
searched output-side weight in the census on an E2B. The maker's 31B copy (round 2) edited the queries, keys,
values and outputs of every layer; the E2B edit adds the down projection, drops the keys and takes a window the
card misstates by four layers at each end. The per-layer entry fits the two writers and counts five first shares
at the floor on the weakest queries. How to reproduce: `results/weights/wangzhang-gemma-4-E2B-it-abliterated.json`
(the changed set by kind and layer, `remaining_along_direction` per tensor) and the reading in `docs/cards/`.

## 56. One file under three account names in forty minutes, through a repository the hub no longer serves, and seven re-uploads equal to the last digit across Google's revisions

Round 26 measured Pound1320/gemma-4-E4B-it-uncensored-heretic (created 2026-09-07 at 10:19Z), Cup4/ (10:40Z) and
Cup5/ (10:58Z), each one commit titled "Duplicate from Titanfrm/gemma-4-E4B-it-uncensored-heretic". Titanfrm's
repository was created the same morning at 09:25Z as "Duplicate from AST-1320/gemma-4-E4B-it-uncensored-heretic",
and AST-1320's now answers with an authentication error. All three carry one 15,992,595,884-byte `model.safetensors`
under the LFS checksum `4967172bea`, llmfan46's E4B file, and llmfan46's 31,743-byte README; a fourth, Cup3/, made
at 10:26Z, was in round 24 and is not yet read. Every measured field of all 2,130 tensors in the three reports equals
llmfan46's round 2 report and its second pass: 11 attention outputs changed, left kept fractions 0.29 to 0.92, rows
0.0016 to 0.0165, 0.00008 outside the changed set. Rounds 26 and 29 measured four more duplicates the same way,
Ishowbackup's of TrevorJS's E2B edit (checksum `8237e4818b`, the file's third repository), akpsahan's of
huihui-ai's second 31B version (`9a11eda6e0`, `bc366b3f1b`), claymorecrystal's of TrevorJS's 26B-A4B edit
(`4b988df4e5`, `3d2388e809`, the fourth repository) and senjiangchen's of TrevorJS's E4B edit (`37605ec579`),
each equal to its parent's report in every field. Four of the seven were pinned against a later Google revision
than their parents were (Ishowbackup's against 07-20 where round 13 read the parent against 04-02; akpsahan's
against 07-20 where round 12 read the parent against 04-10) and still equal to the last digit, because Google's
revisions change templates and configuration files and never the weight shards. Why it matters: the duplicate
function makes a chain, and a link in the chain can disappear while the copies stay; the census counts the file
once and the repositories separately (twenty-four re-uploads in one hundred and nineteen), and a pin against any
revision of a Google original reads the same weights. The seven cost seven downloads that the checksum rule of
finding 38 would have saved; both batches were pinned before the rule. How to reproduce: the seven reports in
`results/weights/` (`Pound1320-`, `Cup4-`, `Cup5-`, `Ishowbackup-`, `akpsahan-`, `claymorecrystal-`,
`senjiangchen-`) compared per tensor on every key with their parents' reports, the commit titles and LFS checksums
in the readings in `docs/cards/`, and the hub's commit listing for Titanfrm and AST-1320. Round 34 reaches a second
vanished repository through its duplicate: huihui-ai/Huihui-gemma-4-26B-A4B-it-qat-q4_0-unquantized-abliterated
returns 404 and eadx's one-commit copy carries its edit (finding 73).

## 57. A maker's own arbitrary-rank solver reads on half the layers the card names, over-reflects the input side, and is the only preservation claim that holds

Bahushruth/gemma-4-31B-it-abliterated and Bahushruth/gemma-4-E4B-it-abliterated describe the maker's own method:
an L-BFGS solve at each attention output and down projection of "all 60 layers" (31B) and "all 42 layers" (E4B),
with row norms "preserved exactly by reparameterization (grimjim method)", an Optuna search of 60 trials and the
maker's own harmful set. Measured against google/gemma-4-31B-it and google/gemma-4-E4B-it: 66 of 1,188 tensors
changed on the 31B, both writers of layers 17 to 49 (33 of 60), and 24 of 2,076 on the E4B, both writers of layers
21 to 32 (12 of 42); nothing else moved and the largest change outside the sets is exactly 0. Each matrix carries
many directions (first share 0.19 to 0.79, eighth cumulative share 0.61 to 0.93) with no direction shared between
the two writers of a layer (0.002 to 0.14) or across layers; a solved matrix, not a projection. The edit is on the
input side and past a reflection: along the leading input direction the 31B keeps -0.84 to -2.46 (65 of 66 past
-1) and the E4B -0.19 to -1.18, while the output direction keeps 0.36 to 0.99. Rows moved by at most 0.00073 and
0.00047. Why it matters: three readings a card would need and does not carry. The window is half the model, not
all of it; the solver's weights run to 3.5 on the 31B, above every Heretic kernel but Pranavz's; and the
reparameterization keeps the rows where every Heretic copy that claims the step leaves 0.005 to 0.008 (finding
22), so this is the first preservation claim in ninety-four readings that the weights confirm. The per-layer entry
flags every matrix's first share and every layer's cosine (132 and 48 flags), both the method's nature; an
arbitrary-rank entry reading the spectrum beyond the eighth direction, the side, the row bound and the window would
count none. How to reproduce: `results/weights/Bahushruth-gemma-4-31B-it-abliterated.json` and
`results/weights/Bahushruth-gemma-4-E4B-it-abliterated.json` (`energy_shares` eight deep, `remaining_along_direction`
left and right, `row_norms.max_relative_error` per tensor) and the readings in `docs/cards/`. Round 34 reads the
second claim that holds: xdavxd's norm-preserving biprojection on the 26B-A4B QAT checkpoint keeps every dense row
within 0.0004 and every packed expert tensor within 0.0009 across 90 tensors and 3,840 experts (finding 74). Round 38 reads the maker's solver on a third base, the E2B: both writers of layers 16 to 24 of the 35 the card names, first shares 0.27 to 0.56, input side at weights 1.56 to 2.08, and rows within 0.0004 on all 18, the claim holding to the row (finding 99).

## 58. Two edits on one base leave matrices rewritten without a direction: seven under the threshold, two as residues

NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals5 (the Heretic arbitrary-rank branch, start layer 19, end layer 42,
preservation 0.7662, steering 0.0007, overcorrection 0.9544) changed 29 of 2,130 tensors against google/gemma-4-E4B-it:
the attention outputs of layers 19 to 36 less 26 and the down projections of 21, 23, 24 and 26 to 34, fourth
cumulative share 0.95 to 0.99, input-side kept fractions -0.24 to -1.50, rows 0.001 to 0.037. The largest change
outside the set is 0.000251, not 0, and it is made of seven down projections inside the card's window (layers 19,
20, 22, 25, 26, 35, 36) rewritten at 0.00006 to 0.00025: the solver touched them and moved almost nothing.
alphakek/gemma-4-E4B-it-heretic-mythos-v1 ("a private fork of Heretic", no kernel printed) changed 34: both writers of
layers 11 to 27, a direction per matrix on 32 (first share 0.51 to 0.97, input side at 1.04 to 2.04, rows 0.0057 to
0.0078, Heretic's band under a card that claims nothing), and two down projections, layers 16 and 20, changed by
0.0014 and 0.0017 with first shares of 0.030 and 0.006 and kept fractions of 0.98 to 1.00: a residue with no
direction. Why it matters: the change threshold of 0.001 divides one edit's footprint in two on NullpoLab's copy,
and a residue a tenth of a percent high with no direction on alphakek's is a mark the public Heretic does not
leave; both are what a fork or a solver leaves behind and a card does not say. The seven and the two are the
numbers to look for when either tool publishes. How to reproduce:
`results/weights/NullpoLab-gemma-4-E4B-it-Heretic-ARA-Refusals5.json` (the `relative_difference` of the seven down
projections under 0.001, `energy_shares` on the 29) and `results/weights/alphakek-gemma-4-E4B-it-heretic-mythos-v1.json`
(layers 16 and 20 of the down projections), and the readings in `docs/cards/`. Round 38 adds RumiaChannel's Refusals2: three down projections of layers 25, 27 and 32 rewritten by 0.0013 to 0.0017 without a direction beside 37 edits in the band (finding 99).

## 59. Three more kernel records read back from the weights: one shipped as a file to the third decimal, two printed on cards to the second

anlord/gemma-4-E2B-it-abliterated ships `abliteration_reproduction.json` beside its weights with the chosen trial's
four Gaussian kernels: the attention output 1.757 at position 23.78 falling to 0.676 at distance 2.72, the queries,
keys and values 1.095 at 20.95 falling to 1.048 at 17.65, the down projection 1.766 at 12.61 falling to 0.358 at
12.18, the gate and up projections 1.566 at 18.10 falling to 1.398 at 6.92. Against google/gemma-4-E2B-it, 110 of
1,951 tensors changed and the kept fractions return the record: the attention outputs keep -0.753 at layer 24
(-0.547 at 22, -0.450 at 26, five layers because the minimum sits 2.72 from the peak); the queries, keys and values
keep -0.095 at layer 21 and -0.078 at 4, the three kinds equal to the third decimal in every layer, the keys and
values stopping at layer 14 where the export drops the shared-KV tensors; the down projections keep -0.764 at
layer 12 and -0.765 at 13, -0.252 at 1, -0.267 at 24; the gate and up projections keep -0.566 at layer 18,
-0.512 at 12, -0.500 at 25, equal to the third decimal in every layer. One direction per layer across all seven
components (1.000). Rows moved 0.002 to 0.040 under a `row_normalization: full` setting that does not restore them.
paoloronco/Mistral-7B-Instruct-v0.3-heretic (Heretic 1.3.0, trial 173) prints 1.44 at 24.50 falling to 1.01 at 13.91
on the attention outputs and 1.18 at 20.94 falling to 1.16 at 8.36 on the down projections; against
mistralai/Mistral-7B-Instruct-v0.3 the 38 changed matrices keep -0.40 at layer 25, -0.02 at 12 and 0.86 at 31 on
the attention outputs and -0.10 to -0.16 on all 17 down projections, one shared direction, output side, zero flags.
Its card calls the edit "applied via LoRA"; the repository holds no adapter and the 38 matrices are edited in
place. minpeter/Voxtral-Mini-3B-Text-2507-hf-heretic (Heretic 1.0.1) prints 1.27 at 17.46 falling to 0.98 at 8.89 and
1.11 at 21.50 falling to 1.02 at 15.14; its 41 matrices keep -0.26 at layers 17 and 18 and 0.01 at 9 and 26 on the
attention outputs and -0.10 at 21 and 22 falling to -0.02 at 7 on the down projections, zero flags. Why it
matters: the record reads back whether it is printed on the card, written into the configuration (finding 47) or
shipped as a file, and on seven components as well as two; the per-layer entry still counts anlord's gate and up
projections as unexpected (28 flags) because no entry names them, and an entry for this tool would count none. How
to reproduce: `results/weights/anlord-gemma-4-E2B-it-abliterated.json`,
`results/weights/paoloronco-Mistral-7B-Instruct-v0.3-heretic.json` and
`results/weights/minpeter-Voxtral-Mini-3B-Text-2507-hf-heretic.json` (`remaining_along_direction` per tensor
against the kernels), the repository's `abliteration_reproduction.json`, and the readings in `docs/cards/`.

Round 33 adds seven kernel records that read their windows to the layer on both writers, and one that reads its
heights to the second decimal. The six linear kernels (callmegrr's 31B, p-e-w's, sh0ck0r's and BinxNet's E4B,
BinxNet's 12B, igorls's 12B QAT) each name a peak position and a distance, and the changed layers are exactly the
integers within that distance on all twelve windows; the heights read within 0.21 on callmegrr's twelve matrices,
within 0.07 to 0.34 at the peaks and 0.1 to 0.6 short on the shoulders on the three E4B exports, and scatter on the
two 12B copies (finding 46). yuna1126's E2B copy, from a tool that prints a `kernel_shape` row, reads its raised
cosine back at 0.20, 0.98, 1.53, 1.31 and 0.53 against 0.19, 0.96, 1.53, 1.31 and 0.53 (finding 70). Evidence: the
eight `results/weights/` reports of round 33 (`remaining_along_direction` left against the cards' kernels) and the
readings in `docs/cards/`. Round 34 adds one kernel record on a QAT checkpoint, prithivMLmods's E4B export: both
windows read to the layer, the down kernel's slope reads with the heights 0.05 to 0.35 under, and the attention
heights scatter (finding 46). Round 35 ran the check in reverse on Kooten's 31B: a card that prints no kernel, and kept fractions that read as two straight
lines with their peaks and slopes (finding 79).

## 60. A text tower extracted from a speech model is measurable against the speech release, and the Heretic edit on it reads with zero flags

minpeter/Voxtral-Mini-3B-Text-2507-hf-heretic is the text tower of mistralai/Voxtral-Mini-3B-2507 extracted into a
plain causal model and then ablated, the pair finding 7 listed as unpinnable because the copy's `base_model` field
names a speech model. Round 29 pinned it against the release at `3060fe34` and the tower mapping of finding 14
matched all 273 text tensors under the release's `language_model.` prefix and reported the audio tower's 489
tensors as left out. 41 changed, the attention outputs of layers 9 to 26 and the down projections of 7 to 29; the
other 232, embedding and head among them, equal the release to the byte, so the extraction changed nothing by
itself. One shared direction (1.000 within and across kinds), output side, first share 0.994 to 0.998, the two
kernels to the second decimal (finding 59), rows 0.025 to 0.056 under no claim. The token side counts 2,032 fields,
all of them the extraction: a text-only configuration and a transformers tokenizer against a speech release's
files. Why it matters: a copy that drops a tower is still measurable against the release that has it, and this is
the first measurement that says so with a clean result rather than a refusal (finding 14's E4B case paired no
tensor because the copy's names were also re-prefixed in a way the mapping of that round did not know). The
release joins the census as its twenty-eighth original. How to reproduce:
`results/weights/minpeter-Voxtral-Mini-3B-Text-2507-hf-heretic.json` (`name_mapping`, `original_only` 489,
`remaining_along_direction` on the 41) and the reading in `docs/cards/`.

## 61. A Heretic edit on a third party's fine-tune, measured against the grandparent through the prefix mapping: the training everywhere at one percent and the kernels readable through it

Pranavz/Hearthfire-24B-heretic says in its title that it is LatitudeGames/Hearthfire-24B, a roleplay fine-tune of
Mistral Small 3.2 under a ChatML template, decensored with Heretic 1.2.0 (the attention outputs at 3.75 centred on
layer 26.51 falling to 3.06 at distance 8.14, the down projections at 2.66 centred on 14.59 falling to 3.73 at
25.63, KL 0.5561 against Hearthfire); its `base_model` field names mistralai/Mistral-Small-3.2-24B-Instruct-2506,
and the pinner followed the field. Against the release at `95a6d26c`, the mapping renamed the 363 text tensors the
release stores under `language_model.` and left out its 222 vision tensors, the first measurement through the
prefix mapping. 282 of 363 changed, every linear of all 40 layers with the embedding and the head, at a median of
1.2 percent; on the five kinds the training alone reaches the first share is 0.06 to 0.44 and the kept fractions
0.95 to 1.15 on both sides, training's diffuse signature. Through it the down projections carry the kernel on all
40 layers (first share 0.984 to 0.995, left kept fractions -0.61 at layer 0, -1.9 to -2.1 at 1 to 13, -1.5 to -1.8
at 15 to 33, -2.6 at 38: weights of 1.6 to 3.6 where the card says 2.66 at the centre falling to 3.73 at the ends)
and the attention outputs carry it on layers 19 to 34 (first share 0.90 to 0.97 and kept -0.13 to -2.22, where the
other 24 sit at 0.06 to 0.26 and keep 0.99 to 1.01). The embedding's zero rows in the release are filled in the
copy and the head changed by 6.3 percent, both the fine-tune's; the token side's 1,027 fields are the fine-tune's
ChatML tokenizer against a release that ships `tekken.json`. Why it matters: the third copy whose README names the
parent its field does not (sh0ck0r's and Dingdust's are the first two, findings 45 and 54), and the one whose
kernels read through the largest training in the census; against Hearthfire itself the training would cancel and
the two kernels would read to the second decimal, so the pin should follow the title. The 347 flags (201
unexpected changes, 65 first shares, 80 direction cosines) are the training's. How to reproduce:
`results/weights/Pranavz-Hearthfire-24B-heretic.json` (`name_mapping`, `original_only` 222, `energy_shares` and
`remaining_along_direction` by kind and layer), `results/meta/Pranavz-Hearthfire-24B-heretic.json`, the README's
title, and the reading in `docs/cards/`. Round 35 measured the copy against Hearthfire itself: 56 matrices, exactly 0 outside, the kept fractions equal to this reading's to the
second decimal and the leading directions equal at 1.000 on all 56 (finding 77).

## 62. A second copy from one maker names the pretrained base and stands on the instruct model, placed by byte range before any re-pin

Felldude/gemma-4-E4B-uncensored names google/gemma-4-E4B, the pretrained base, in its `base_model` field under a
499-byte card ("largely uncensored and is suitable for NSFW image captioning"). Against the base at `a24c9379`, 595
of 2,076 tensors changed: 592 of the 664 language-model tensors at a median relative change of 0.42 (every linear,
norm and scalar of all 42 layers, the embeddings and the per-layer embeddings), the audio and vision embedding
projections at 0.52 and 0.39, the two towers' 1,409 tensors unchanged to the byte; 680 flags, no shared direction,
kept fractions 0.5 to 4.5. The copy's generation configuration ends on `[1, 106]` where the base ends on
`[1, 106, 50]`, and its template is the instruct model's 17,336-byte file where the base ships none. The range tool
of finding 45 read fourteen tensors from the hub against google/gemma-4-E4B-it (`83df0a88`) and the base: the
copy's norm weights, layer scalars and layer norms are byte-equal to the instruct model's where they differ from
the base by 0.008 to 0.02; its linears differ from the instruct model by 0.00003 to 0.0058 (layer 20's attention
output 0.00003, down 0.00007, key and value 0.00004; layer 0's attention output 0.0031; layer 30's gate 0.0036 and
up 0.0032; layer 41's down 0.0058) where both differ from the base by 0.745; the audio embedding projection is
byte-equal to the instruct model's. Why it matters: the same maker's Ministral copy did the same on another family
(finding 26), so the wrong field is a habit rather than a slip, and the token side announced the parent before
any weight was read; the edit itself is small, concentrated at the two ends of the stack, and will read when the
pair is re-pinned against google/gemma-4-E4B-it. The fourth copy in ninety-four that carries a parent its card
does not name. How to reproduce: `results/weights/Felldude-gemma-4-E4B-uncensored.json` (the changed set by kind,
the unchanged towers) and `results/meta/Felldude-gemma-4-E4B-uncensored.json` (`eos_token_id`, the template), then
the range-read tool (`hub_range_read.py` in `tools/`) with `--tensor` and
`model.language_model.layers.20.self_attn.o_proj.weight`, followed by `google/gemma-4-E4B@a24c9379`,
`google/gemma-4-E4B-it@83df0a88` and `Felldude/gemma-4-E4B-uncensored@8ebbb694`, and the other thirteen names in
the reading in `docs/cards/`.

Round 33 reads the source of the wrong field for Heretic exports: the tool's generated card carries the original's
own header, and Google's instruct cards name the pretrained base there, so six of the round's eight copies name
google/gemma-4-31B, google/gemma-4-12B or google/gemma-4-E4B while standing on the instruct models (finding 67).
Felldude's two copies are a maker's habit; the six are a tool's. Round 35 measured the E4B copy against the instruct model: 245 tensors on layers 0 to 14 and 27 to 41 changed by 0.1 to 0.7 percent,
the middle twelve layers and both towers equal, a fine-tune without a direction (finding 78).

## 63. A fine-tune whose vision and audio towers are freshly initialised matrices, under a card that calls the model multimodal

Ilya626/gemma-4-E4B-it-SDFT_Heretic_RP ("merged Hugging Face weights for an RP-enhanced version of Gemma 4 E4B it",
"based on the uncensored Heretic SDFT line", built from google/gemma-4-E4B-it) changed 526 of 2,130 tensors against
the instruct model at `83df0a88`. In the language stack, the seven projections of all 42 layers moved by 0.16 to
0.56 percent of their norm at full rank (first shares 0.009 to 0.28), kept fractions 0.99 to 1.02 on both sides,
the embeddings, normalisations and scalars unchanged: a small fine-tune, as the card says. In the two towers, the
232 linear maps moved by 114 to 171 percent of their norm: the ten linears of each of the 12 audio conformer layers
and the seven of each of the 16 vision encoder layers, every one with a kept fraction of -0.11 to 0.00 along its
leading direction, while the 1,179 other tower tensors (normalisations, per-dimension scales, depthwise and
subsampling convolutions, relative-key projections, the quantisation ranges on every linear, the output projection,
both embedding projections) are Google's to the byte. Three of the 232 read from the hub by byte range have a mean
within 0.00003 of zero, standard deviations of 0.02003 and 0.01999, no exact zero, 64 distinct values in every block
of 64, kurtosis 3.000 and 2.9999, row norms of 0.59 to 0.69 on 1,024 and 4,096 rows, and cosines of 0.0001 and
0.0004 with Google's matrices on the same names: Gaussian draws at the library's default initialiser scale of
0.02, the tensors a loader fills when a checkpoint's names do not match the class it is loaded into. Google's own
tensors on those names are 36 to 43 percent exact zeros with four distinct values per block of 64; the copy's
subsampling input projection equals Google's to the bit. No projection kernel is in the language stack: the
attention outputs keep 0.991 to 1.012 along their leading direction and no down projection carries more than 0.28
of its change in one direction, so the "Heretic SDFT" the copy stands on left no weight-space mark the measure
reads. The copy is saved in float16 (the four `dtype` fields read float16 against bfloat16) with the E4B template
of the 04-02 revision. Why it matters: a card that says "multimodal HF weights" ships a model whose image and audio
inputs pass through 232 random matrices between Google's normalisations and quantisation ranges, a change no
reading of the card predicts and one the measure states in two numbers per tensor (a relative change above 1, a
kept fraction at 0). It is the first copy in one hundred and twenty-three whose towers are neither the original's
nor an edit of it. How to reproduce: `results/weights/Ilya626-gemma-4-E4B-it-SDFT_Heretic_RP.json` (the 232
`audio_tower` and `vision_tower` rows with `relative_difference` above 1 and `remaining_along_direction` at 0), then
the range-read tool (`hub_range_read.py` in `tools/`) with `--tensor` and
`model.audio_tower.layers.0.self_attn.k_proj.linear.weight` or
`model.vision_tower.encoder.layers.0.mlp.gate_proj.linear.weight`, followed by `google/gemma-4-E4B-it@83df0a88` and
`Ilya626/gemma-4-E4B-it-SDFT_Heretic_RP@c07b5f9b`; the distinct-values statistic prints 64 against Google's 4, and
the standard deviation of the decoded copy is 0.020. The reading is in `docs/cards/`. Round 35 reads the second case, Kooten's 31B, whose 189 vision-tower linears are fresh draws at a standard deviation of 0.0199 under
renamed tensors (finding 79).

## 64. A five-surface edit of the 31B, measured through a re-upload of an unmeasured parent: four surfaces read to the number, the fifth in a window the card misstates

nguyenthilaitrieulong/gemma-4-31B-it-abliterated is one commit, "Duplicate from WWTCyberLab/gemma-4-31B-it-abliterated",
and carries that maker's README: an adapter of rank 32 on 18 modules of layers 57 to 59, merged; a primary-direction
ablation "at L59" and "standard at L33-52"; an "orthogonal residual ablation" of layers 55 to 59 at scale 1.5; 13
"refusal-starting token embeddings scaled down by 10x"; and `bad_words_ids` on a disclaimer phrase. The parent was
pinned for Raider in round 17 and never measured, so the re-upload is the edit's one measurement. Against
google/gemma-4-31B-it at `842da379`, 77 of 1,188 tensors changed and nothing else moved. The adapter: the queries,
keys, gates and up projections of layers 57 to 59 beside their two writers, six modules a layer, the card's 18, at
1.1 to 3.1 percent of their norm. The 1.5 pass: the attention outputs and down projections of layers 55 to 59 keep
-0.494 to -0.5001 along their leading output direction, a weight of 1.50 on all ten, with a second direction under
each (first shares 0.69 to 0.79), the orthogonal pair the card describes. The embedding: eight near-equal singular
values and a largest row-norm change of 0.9091, thirteen rows left at one eleventh of their length, the maker's
"strength" rule read on a second copy (finding 30: "strength 5" was a division by six). The generation settings: five
token sequences in `bad_words_ids` that the original does not set. The fifth surface, the "standard" ablation, is in
the weights on layers 25 to 27 and 31 to 54 (32 layers, with 28 to 30 untouched), one direction per matrix at first
shares 0.983 to 0.995, the left kept fraction 0.25 at layer 25 falling to 0.00 at 39 and rising to 0.24 at 54 on
both writers, a weight schedule of 0.75 to 1.00, where the card says layers 33 to 52. By byte range, layer 56's
attention output differs from huihui-ai's second 31B version, the census's other weight-1.5 edit on this base, by
0.0306 of its norm, so the two makers share a weight and not a direction. Why it matters: a stack of five methods
in one file reads apart into its parts, four of them to the number the card prints, and the measure corrects the
fifth; the row-scale rule of one maker now holds on two copies; and the duplicate function once more announces the
parent in its commit title, here before a parent the census had not reached. How to reproduce:
`results/weights/nguyenthilaitrieulong-gemma-4-31B-it-abliterated.json` (`remaining_along_direction` left on the
writers of layers 25 to 59, `energy_shares` on layers 55 to 59, `row_norms.max_relative_error` on
`model.language_model.embed_tokens.weight`, the changed set of layers 57 to 59),
`results/meta/nguyenthilaitrieulong-gemma-4-31B-it-abliterated.json` (`generation.bad_words_ids`), the hub's commit
listing, and the range-read tool with `--tensor model.language_model.layers.56.self_attn.o_proj.weight` followed by
`google/gemma-4-31B-it@842da379`, `huihui-ai/Huihui-gemma-4-31B-it-abliterated-v2@7db456ef` and
`nguyenthilaitrieulong/gemma-4-31B-it-abliterated@1b283037`. The reading is in `docs/cards/`. Round 34 reads the
second unmeasured parent through a duplicate, huihui-ai's QAT 26B-A4B edit through eadx's copy, with the parent
repository gone from the hub (finding 73). Round 35 reads a second decoder-side list through enkato64bit's duplicate of Jiunsong's 12B edit, 48 banned sequences and a 12-gram
repeat block (finding 81).

## 65. A four-layer projection at weights to 5.4 with exact row restoration, under a card that names a custom method and no parameter

Sabomako/gemma-4-31B-it-heretic ("Heretic v1.3.0 with custom ORBA abliteration method", KL divergence 0.081, 2
refusals in 100, nothing else) changed 8 of 1,188 tensors against google/gemma-4-31B-it at `35487898`: the attention
output and the down projection of layers 31 to 34 of 60, and nothing else to the last digit. One direction per layer
shared by the two writers (0.981 to 0.9999), 0.86 to 0.91 across the four layers; output side on 8 of 8. The kept
fractions along the leading direction are -0.36, -2.17, 0.58 and -4.36 on the attention outputs and -4.32, -0.32,
0.94 and 0.15 on the down projections: weights of 1.36, 3.17, 0.42 and 5.36 and of 5.32, 1.32, 0.06 and 0.85.
Rows moved 0.0000 to 0.0004 on all eight, the exact restoration that TrevorJS's biprojection leaves (finding 3) and
that the public Heretic's row normalisation does not (finding 22). Why it matters: 5.4 is the largest weight read on
a direction-per-layer projection in the census (the shared-direction maximum is huihui-ai's 3.0, finding 21; the
arbitrary-rank solvers reach higher without restoring rows, findings 22 and 68), and the output along the direction
on layer 34's attention output and layer 31's down projection is reversed and multiplied by more than four; four
layers of sixty is the narrowest window on this base; and the card prints none of it. The maker reports a KL of
0.081, ten times the Heretic exports measured beside it, which is the price such weights would predict. How to
reproduce: `results/weights/Sabomako-gemma-4-31B-it-heretic.json` (`remaining_along_direction` left and right on the
eight changed tensors, `row_norms.max_relative_error`) and the reading in `docs/cards/`.

## 66. A translation fine-tune over a Heretic edit the title names only by method: the parent placed from the saved direction vectors, and a halved context length

AlekseyCalvin/Lyrical_Translator_ru2en_on_Gemma4_12b_heretic_SFT_Run2 names google/gemma-4-12B-it in its
`base_model` field and "gemma-4-12B-it-heretic" in its 834-byte card, with no maker's name. Against the instruct
model at `5926caa4`, 328 of 677 tensors changed: the queries, keys, attention outputs, gates, up projections and down
projections of all 48 layers and the value projections of 40 (the eight global-attention layers' value projections
are unchanged), at 1.8 to 10 percent of their norm, low rank (first shares 0.13 to 0.86) and in no shared
direction; every vector, embedding and projection outside those 328 is unchanged to the last digit. Under the
training, the Heretic edit reads on eight matrices: the down projections of layers 23, 27, 28, 29, 32 and 33 keep
-0.18, -0.30, -0.37, -0.32, -0.20 and -0.19 of the original's action along their leading output direction, and the
attention outputs of layers 29 and 34 keep 0.48 and 0.31. igorls/gemma-4-12B-it-heretic-v1 (round 7, Heretic with
norm-preserving biprojection, down projections of 22 to 34 and attention outputs of 29 to 37) keeps -0.18, -0.30,
-0.37, -0.38, -0.21 and -0.19 on the same six down projections and 0.46 and 0.30 on the same two attention outputs,
and the saved leading vectors of the two measurements agree at 1.000 on four of the down projections, 0.971 and
0.996 on the other two, and 0.991 and 0.990 on the attention outputs. The nine other measured 12B copies' vectors on
the same matrices stand at 0.04 to 0.92 from AlekseyCalvin's (Vampelium 0.89 to 0.92, the two copies of finding 46's
shared direction 0.45 to 0.51, BinxNet 0.39 to 0.45, huihui-ai 0.13 to 0.21, coder3101 0.04 to 0.57). The copy was
made on 06-07, three days after igorls's v1. On the token side, `text_config.max_position_embeddings` is 131,072
where the original declares 262,144, the declared context halved by the training's save (finding 4). Why it
matters: the parent of a training-over-ablation pair was placed without a download and without a range read, by
comparing the pair's saved leading vectors with every committed measurement on the same base, a check the scorer can
run on any Gemma 4 copy whose card names a method and no maker; and the pair now belongs on the list against
igorls's repository, where the training will read alone. How to reproduce:
`results/weights/AlekseyCalvin-Lyrical_Translator_ru2en_on_Gemma4_12b_heretic_SFT_Run2.json` and
`results/weights/igorls-gemma-4-12B-it-heretic-v1.json` (`remaining_along_direction` left on the eight matrices),
then the cosine of the two `weights.directions.safetensors` files' `.left` vectors on those names (the pull copies
under `wheat31/measurements/pair-1/` and `blueback7/measurements/pair-3/`), and
`results/meta/AlekseyCalvin-Lyrical_Translator_ru2en_on_Gemma4_12b_heretic_SFT_Run2.json` for the context field.
The reading is in `docs/cards/`. Round 38 is the check's strongest result: DuoNeural's 26B-A4B copy stands at 1.000 to TrevorJS's saved vectors on all 90 names where an independent run of the method stands at 0.97, and the comparison, not the card or the recipe table, named the parent (finding 95).

## 67. Six of eight Heretic exports in one round name the pretrained base in their `base_model` field, because the tool's card carries the original's header

callmegrr/gemma-4-31B-it-heretic-z, p-e-w/gemma-4-E4B-it-heretic, sh0ck0r/gemma-4-E4B-it-heretic,
JokeHer/gemma-4-E4B-it-heretic, BinxNet/gemma-4-E4B-it-heretic and BinxNet/gemma-4-12B-it-heretic name
google/gemma-4-31B, google/gemma-4-E4B (four times) and google/gemma-4-12B in the `base_model` field of their
README headers; the first sentence of every card names the instruct model ("a decensored version of
google/gemma-4-31B-it"), and the weights stand on the instruct models: against them, the changed set is the card's
two windows and the largest relative change outside it is exactly 0 on all six (findings 1 and 59). The six READMEs
are Google's instruct cards (27,824 to 29,074 bytes) with the tool's table over them, and the field in each equals
the field in the corresponding Google card, where Google names the pretrained checkpoint the instruct model was
trained from (`data/batches/round-33-batch-1.json` records google/gemma-4-31B-it's own declared base as
google/gemma-4-31B). The maker of the tool is one of the six, with the same field. The seventh copy, igorls's,
carries the maker's own card and names its QAT original correctly; the eighth, yuna1126's, is another tool and
names the instruct model. The two QAT cases of finding 48 (mewse's and OS-Software's Heretic exports naming the
instruct model while standing on the QAT checkpoint) are the same inheritance one step along: the QAT checkpoints'
own cards name the instruct model as their base. Why it matters: the field is what a pinner, a hub search or a
lineage graph reads, and for Heretic exports of Gemma 4 it names the grandparent; paired by the field, each of the
six would have read the whole instruct training beside the edit, as Felldude's copies did (findings 26 and 62),
and the census would have counted six fine-tunes. The pinner paired all six by the first sentence, which is the
check finding 48 asked for on QAT names extended to the pretrained names; Felldude's wrong fields are a maker's
habit, these are a tool's default, and a hub-wide count of Heretic exports whose field names a `google/gemma-4-*`
pretrained checkpoint would size the effect. How to reproduce: the six README headers at the revisions in
`data/batches/round-33-batch-1.json` against the headers of google/gemma-4-31B-it, google/gemma-4-E4B-it and
google/gemma-4-12B-it, then `results/weights/callmegrr-gemma-4-31B-it-heretic-z.json` and the five other
round-33 reports (`summary.max_relative_change_outside_changed` is 0 on each). The readings are in `docs/cards/`.
Round 34's eight copies all name their true original in the field, the four Heretic exports among them: on a QAT
checkpoint the inherited header names the QAT checkpoint, so the tool's habit misleads only where the original's own
card names a different model (finding 75). Round 35's four Heretic exports name their true originals in the field, two of them the E4B QAT checkpoint (finding 82). Round 37's TheUmbraWalker first pass names the pretrained base, as the maker's second copy does, and its six other Heretic exports name their true originals (finding 85). Round 36's eight copies all stand on QAT checkpoints: coder3101's two with llmfan46's and Mitchins's name the QAT checkpoint in the field, and OS-Software's three Heretic v1 and v2 cards and JJaguar's v1 card name the instruct model, the inheritance of finding 48 (finding 90).

## 68. An arbitrary-rank edit at right-side weights to 30, with one matrix rewritten to its own size and its rows put back

JokeHer/gemma-4-E4B-it-heretic (Heretic v1.2.0's arbitrary-rank branch; start layer 19, end layer 39,
preserve-good-behaviour weight 0.6945, steer-bad-behaviour weight 0.0014, overcorrect relative weight 1.0377,
neighbour count 12, KL divergence 0.5806 on the card) changes the attention outputs and the down projections of
layers 19 to 38 of google/gemma-4-E4B-it, 40 of 2,076 tensors, and nothing else (0 outside). Each matrix has its
own direction (within-layer cosines 0.002 to 0.16, group medians 0.21 and 0.23), the input side carries the edit
on 39 of 40 (the right kept fraction -0.33 to -3.81 on the attention outputs, -2.44 to -29.09 on the down
projections, weights 1.33 to 4.81 and 3.4 to 30.1 against finding 22's 0.51 to 10.18), and layer 37's down
projection changed by 1.008 of its own norm with first share 0.650, kept fractions -4.29 and -29.09, a cosine of
0.492 with the original read from the hub by byte range, and its row norms within 0.0063 of the original's (norm
93.614 against 93.619): a matrix rewritten to its own size with its rows restored. Layer 20's down projection is a
residue (0.0017, first share 0.006, kept 1.00), the solver's near-zero weight on that layer; the other 38 matrices'
rows moved 0.0057 to 0.0078, the band coder3101's cards claim as preservation (finding 22), under a card that claims
none. Why it matters: the KL divergence on the card is 0.58 where the round's other Heretic exports print 0.007 to
0.04, and the weights say why: a weight of 30 on one matrix is a rewrite, and the arbitrary-rank solver will go
there when its search is let; the per-layer entry flags all 40 matrices twice (80 flags) for not sharing a
direction, and an arbitrary-rank entry (finding 22) would count 39 and still flag layer 37, where the change equals
the matrix. The 2 refusals in 100 the card reports sit beside a KL forty times the round's other Heretic exports'. How to
reproduce: `results/weights/JokeHer-gemma-4-E4B-it-heretic.json` (`remaining_along_direction` right per tensor,
`row_norms`, the layer 37 and layer 20 entries), then the range-read tool (`hub_range_read.py` in `tools/`) with
`--tensor model.language_model.layers.37.mlp.down_proj.weight`, `google/gemma-4-E4B-it@fee6332c` and
`JokeHer/gemma-4-E4B-it-heretic@50f546e0`. The reading is in `docs/cards/`.

## 69. One maker's second Heretic search of the 12B, with thinking on, edits 57 matrices where the first edited 22 and finds a different direction

igorls/gemma-4-12B-it-qat-q4_0-unquantized-heretic (card headed "v1.1, thinking-mode fix": the first release was
searched with thinking disabled and still refused with thinking on, so the second was searched with thinking
enabled; attention kernel 1.48 at 36.55 with minimum 1.29 and width 21.18, down kernel 1.48 at 31.62 with minimum
1.43 and width 12.60, KL 0.32, refusals about 22 percent against 99) changes the attention outputs of layers 16 to
47 and the down projections of 20 to 44 of google/gemma-4-12B-it-qat-q4_0-unquantized, 57 of 677 tensors, exactly
the card's windows, with 0 outside, one direction per layer (the two writers at 0.96 to 0.998, the layers at 0.26
to 0.48), first shares 0.9946 to 0.9977 and zero flags, the one clean match of the round. The maker's first copy,
igorls/gemma-4-12B-it-heretic-v1 (round 7, on google/gemma-4-12B-it), edited 22 matrices (down projections 22 to
34, attention outputs 29 to 37) at weights 1.08 to 1.38 and 0.49 to 0.70 with KL 0.028. The second reaches ten
layers higher on both writers, edits two and a half times the matrices, prints a KL eleven times larger, and its
saved leading vectors stand at 0.15 to 0.96 from the first copy's on the matrices both edit (0.96 and 0.95 on layer
33, 0.15 on layer 22) and at 0.10 to 0.84 from huihui-ai's edit of the same QAT checkpoint (round 32, finding 48):
the direction found with thinking on is, in most of the window, a different direction. The down kernel reads within
0.14 on layers 32 to 44 (1.37, 1.45, 1.40 and 1.29 at 32, 36, 40 and 44 against 1.48 to 1.43) and falls away below
(0.64 at 20); the attention outputs read 0.20 to 1.18 under a kernel of 1.29 to 1.48, finding 46's scatter, now on
the QAT checkpoint. Why it matters: the card is the first in the census to say why a second search on one base
found a different direction, and the weights agree with it: the refusal direction the tool finds depends on the
prompts' mode, and two Heretic copies of one model from one maker are two edits rather than one at two strengths. The
copy's `base_model` field names the QAT checkpoint, under the maker's own card rather than the tool's (findings 48
and 67). How to reproduce: `results/weights/igorls-gemma-4-12B-it-qat-q4_0-unquantized-heretic.json` and
`results/weights/igorls-gemma-4-12B-it-heretic-v1.json` (the changed sets, `remaining_along_direction` left), then
the cosine of the two `weights.directions.safetensors` files' `.left` vectors on the shared names (the pull copies
under `wheat33/measurements/pair-8/` and `blueback7/measurements/pair-3/`), and the same against
`nautilus32/measurements/pair-4/` for huihui-ai's. The reading is in `docs/cards/`. Round 34 places the second
search's direction: smashingtags's plain projection of the same checkpoint, with no search, stands at 0.84 to 0.98 to
it on 56 of 57 shared matrices (finding 72). Round 35 reads the maker's third copy, a LoRA-rank search with thinking on over both writers of the E4B QAT checkpoint's layers 21 to
36, the largest Heretic changes read on an E4B and a direction shared with none of twenty other E4B edits (finding 82). Round 36 places JJaguar's kernel pass of the same checkpoint, searched without the thinking fix, at 0.25 to this copy's direction and 0.90 to the instruct model's five kernel exports (finding 91).

## 70. A tool new to the census prints a raised-cosine kernel, and it reads back to the second decimal with the rows restored and the tails under the threshold

yuna1126/gemma-4-E2B-Tema_Q-Abliterated (Tema_Q-Abliterated v1.0.0, SCAPE search; direction index "per layer",
attention kernel 1.558 at 16.24 falling to 0 at distance 2.91 with `kernel_shape` cosine, down kernel 1.31 at
12.54 falling to 0 at 1.5, cosine; KL 0.0199, refusals 20 of 100) changes the attention outputs of layers 14 to 18
and the down projections of 12 and 13 of google/gemma-4-E2B-it, 7 of 2,011 tensors, output side on 7 of 7, with
one direction per layer (the attention directions at 0.34 to 0.54 from their group's median, the two down
projections at 0.005 from each other). The weights read off the left kept fractions are 0.20, 0.98, 1.53, 1.31 and
0.53 on layers 14 to 18 and 0.93 and 1.10 on 12 and 13; a raised cosine of the printed height and half-width gives
0.19, 0.96, 1.53, 1.31 and 0.53 and 0.93 and 1.03. The kernel is above zero on layers 19 (0.010) and 14 for the
down projections (0.003) as well, and those two matrices changed by 0.00038 and 0.000028 of their norms, under
the threshold of change and the two largest values outside the changed set. Rows moved 0.0002 to 0.0004 on all
seven, the exact restoration (finding 3), under a card that says nothing of rows. The token side is "consistent"
with no field differing, the one such card of the round. Why it matters: a third tool joins Heretic and the
configuration-recorded ablation of finding 47 in printing a record the weights return, and the first with a kernel
shape other than linear; the restoration is exact where Heretic's is a band (finding 22), which separates the two
tools' exports on the rows alone; and the tails show what "outside the changed set" means for a smooth kernel, a
0.00038 that is the method's own rather than a stray change. The scorer's three flags are the kernel's edges (first
shares 0.948 to 0.988 on the smallest edits), and an entry that carries the kernel shape would count all seven and
the two tails. How to reproduce: `results/weights/yuna1126-gemma-4-E2B-Tema_Q-Abliterated.json`
(`remaining_along_direction` left on the seven, `summary.max_relative_change_outside_changed`, the layer 19
attention output's and layer 14 down projection's relative changes, `row_norms`), the card's kernel table at
revision `ebf953fb`, and the reading in `docs/cards/`.

## 71. Shard checksums shared across makers are the library's layout, and the duplicate rule must compare every weight file

Three E4B Heretic exports measured in round 33 (p-e-w, sh0ck0r, BinxNet) carry the same first and fourth shards,
`aa3e9d1e` (the token embedding alone, in the four-shard layout the library writes for google/gemma-4-E4B-it) and
`8080cb1a` (the vision tower), as four earlier E4B copies (DuoNeural, OS-Software, TheUmbraWalker, prithivMLmods),
while their second and third shards are each copy's own; callmegrr's 31B export carries the same second shard
`2bdb2df0` (layers 48 to 59 and the vision tower, in the two-shard layout) as Sabomako's and llmfan46's, while the
first shards differ. The measured fields confirm it: the seven E4B copies change different layer sets at different
weights (p-e-w 68 matrices, sh0ck0r 60, BinxNet 51) and the three 31B copies 12, 8 and 18, with no field shared.
The shards are equal because no Heretic edit touches the embedding, the vision tower or, on the 31B, layers 48 to
59 at those copies' windows, and the library's saver writes the same bytes for the same tensors in the same order.
Why it matters: the checksum rule of finding 38 refuses a repository whose weight files equal a measured copy's
(ScottzillaSystems's E4B copy in this round), and a rule that matched on any shared shard would have refused seven
distinct E4B edits and three distinct 31B edits as re-uploads; the rule is "all weight files equal", a shared subset
is the layout, and the subset tells the pinner which shards the comparison will read as unchanged before the download.
How to reproduce: `weight_files_sha256` in `data/batches/round-33-batch-1.json` and `round-31-batch-3.json` for the
copies named, the hub's file listings for the four earlier E4B copies and llmfan46's 31B export, and the changed
sets in the corresponding `results/weights/` reports. Round 34 adds three shared shards of the same kind (llmfan46's
second 26B-A4B shard equal to mewse's, wnfldchen's first 12B shard equal to igorls's, Umranz's shards 8 to 11 equal
to the diffusion original's and Goodoldjam's) and one that crosses Google's releases: the E4B vision-tower shard
`8080cb1a` is the QAT checkpoint's as well as the instruct model's (finding 75). Round 35's pinner saw enkato64bit's duplicate of Jiunsong's unmeasured 12B edit as carrying different weight files, because the only
Jiunsong file it could compare was the measured E4B export; the rule has to read the named source's hub listing (finding 81). Round 37 adds the 12B QAT layout shard `513abfa9`, shared by OS-Software's, wnfldchen's and igorls's exports, and a second shard byte-equal between TheUmbraWalker's two copies because the second pass did not touch it (finding 85). Round 38 reads the E2B layout on DuoNeural's first two shards and the 26B-A4B layout on SassyDiffusion's second shard, equal to WWTCyberLab's for the tensors neither edit touches, and reads DuoNeural's 26B-A4B shards equal to nothing while its tensors stand within 0.0006 of TrevorJS's (finding 95).

## 72. Five edits of one QAT checkpoint sort into pairs by method, and four makers' QAT edits stand on their own instruct edits' directions

Round 34 brought the census to five edits of google/gemma-4-12B-it-qat-q4_0-unquantized by five makers, and the
saved leading left vectors of each were compared with the others' on the matrices both edit, with no download
(the check of finding 66). The five sort by method and not by maker or date. wnfldchen's LoRA-rank arbitrary-rank
search (a Heretic v1.4.0 fork, July) and coder3101's arbitrary-rank search (Heretic v1.2.0, June) stand at 0.41
to 0.998 on the 18 attention outputs both edit, median 0.924 on the left and 0.926 on the right. smashingtags's
plain projection at weight 1.00 with no search and igorls's linear-kernel search with thinking on stand at 0.84 to
0.98 on 56 of the 57 matrices both edit, median 0.951 (0.57 on layer 47). Across the pairs the medians fall to 0.29
(wnfldchen against igorls), 0.27 (wnfldchen against smashingtags) and 0.11 (coder3101 against igorls), and
huihui-ai's shared projection stands at 0.05, 0.04 and 0.38 from the others. Two arbitrary-rank searches with
different preservation settings (0.92 and 0.37) and different trial counts found one direction per layer; a
projection of the mean difference and a kernel search over a different prompt set found another; and the
one-direction-for-all-layers method found a third.

The same round placed four makers' QAT edits against the same makers' instruct edits of the same size: llmfan46's
26B-A4B pair at 0.85 to 0.98 on twelve matrices (median 0.935), coder3101's 12B pair at 0.21 to 0.955 on 21
(median 0.88), huihui-ai's 26B-A4B pair (the QAT edit through eadx's duplicate) at 0.71 on layers 5 to 11 and 0.99
on 14 to 29, and TrevorJS's method (xdavxd's run on the QAT checkpoint against TrevorJS's own on the instruct
model) at 0.79 to 0.99 on all 90 (median 0.97). The QAT checkpoint differs from the instruct model by 0.14 to 0.16
of a matrix (range reads in round 34's readings), and the refusal direction a method finds survives that
difference almost whole.

Why it matters: the direction is a property of the method and the prompt set more than of the checkpoint, and a
library of directions indexed by method would let a new copy be placed by cosine before its weights are read,
as finding 66 did for one parent. It also bounds what a "different" edit of one base means: two searches that
agree at 0.92 and 0.95 are the same edit at different strengths, and the census now reads three distinct
directions on this checkpoint, not five.

Evidence: the direction files under `/opt/ai/hpc-packages/pulls/model-audit/nautilus34/measurements/pair-2/`,
`pair-6/` and `pair-7/` against `wheat33/measurements/pair-8/` (igorls), `nautilus32/measurements/pair-4/`
(huihui-ai's QAT edit), `nautilus16/measurements/pair-2/` (llmfan46's instruct edit), `nautilus18/measurements/pair-1/`
(coder3101's instruct edit), `blueback12/measurements/pair-5/` (huihui-ai's instruct edit) and
`nautilus3/measurements/pair-4/` (TrevorJS's second pass); the cosines are in the readings in `docs/cards/` and
were taken from the saved left and right vectors on the shared tensor names. Round 35 adds coder3101's E4B QAT edit, standing at 0.91 on the maker's instruct edit and at 0.92 to 0.95 on JokeHer's, NullpoLab's
and alphakek's (finding 82). Round 37 adds llmfan46's 12B QAT edit at 0.95 on the maker's own instruct edit and 0.97 on coder3101's QAT edit, and two searches on Japanese prompt sets that stand apart from the English families at 0.30 to 0.70 (findings 83 and 87). Round 36 adds three more QAT edits on their makers' instruct directions: coder3101's 31B and 26B-A4B QAT edits at 0.96 and 0.94 to the maker's instruct edits and llmfan46's 31B QAT edit at 0.93 to its instruct edit, while the two 31B QAT searches stand at 0.99 to each other (finding 89); JJaguar's kernel pass carries the 12B kernel family to the QAT checkpoint at 0.90 (finding 91).

## 73. huihui-ai's QAT edit of the 26B-A4B, reached through a hub duplicate after the parent vanished, projects at 3.5 on every writer of every layer along the maker's instruct directions

eadx/Huihui-gemma-4-26B-A4B-it-qat-q4_0-unquantized-abliterated is one commit, "Duplicate from
huihui-ai/Huihui-gemma-4-26B-A4B-it-qat-q4_0-unquantized-abliterated", with both accounts as authors, and the
parent repository returns 404. The copy was admitted to round 34 as the parent's only measurement (findings 38
and 64) and measured against google/gemma-4-26B-A4B-it-qat-q4_0-unquantized at `641f1844`: 60 of 1,013 tensors
changed, the attention outputs and shared dense down projections of all 30 layers, no expert, router, gate-up,
norm or tower tensor, and exactly 0 outside. The left kept fraction along the leading output direction is
-2.4976 to -2.5027 on all 60: a weight of 3.50, output side on 60 of 60, first shares 0.999 to 1.000, the
largest shared-direction weight in the census after finding 21's 2.5, 1.5 and 3.0. The projection uses two
directions: layers 0 to 11 share one (0.712 to the group reference), 12 and 13 sit between (0.81 and 0.92), 14
to 29 share the other (1.000); against the maker's instruct edit of this base (weight 3.0 from layer 5) the
saved vectors stand at 0.71 on layers 5 to 11, 0.80 and 0.91 on 12 and 13 and 0.99 on 14 to 29. Rows moved 0.12
to 0.97 of their norm, the model's largest changes 0.044 to 0.113, under a card of 2,758 bytes that names no
layer and no weight ("a crude proof-of-concept"). The token side is consistent with nothing differing.

Why it matters: a copy the hub no longer serves is still readable through its duplicate, and the reading says
what the maker's card never did, that the QAT edit starts five layers earlier and half a unit stronger than the
instruct edit along the same two directions. The weight-3.5 projection is the strongest edit in the library and a
candidate for the behavioural read of a copy whose change is large.

Evidence: `results/weights/eadx-Huihui-gemma-4-26B-A4B-it-qat-q4_0-unquantized-abliterated.json`
(`remaining_along_direction` left on all 60 changed tensors, `summary.direction_agreement`),
`results/meta/eadx-Huihui-gemma-4-26B-A4B-it-qat-q4_0-unquantized-abliterated.json`, the hub's commit listing for
the copy (one commit, two authors) and the 404 on the parent, and the reading in `docs/cards/`. Round 35 reads two more unmeasured edits through re-uploads, huihui-ai's E2B second version through Dzluck's repository and Jiunsong's
SuperGemma 12B through enkato64bit's duplicate (findings 80 and 81).

## 74. A norm-preserving biprojection with an expert pass reaches all 3,840 experts, restores the rows within 0.0009 and reads TrevorJS's directions on a second checkpoint

xdavxd/gemma-4-26B-A4B-it-qat-heretic-ega describes TrevorJS's norm-preserving biprojection with an
expert-granular ablation, run through a Heretic HEAD on google/gemma-4-26B-A4B-it-qat-q4_0-unquantized at
`f1e06dc5`: per-layer directions, scale 1.0, expert scale 1.0, row-norm preservation, "60 dense slices and 3,840
expert slices". Measured against that commit: 90 of 1,013 tensors changed, the attention outputs, the shared
down projections and the packed expert down tensors of all 30 layers with 128 of 128 experts measured in each;
the 30 gate-up tensors and 30 routers exactly 0 and exactly 0 outside. One direction per layer across the three
kinds (within-layer cosines 0.95 to 1.00, the experts' left vectors agreeing at 0.996 to 0.999); output side on
90 of 90; along the leading output direction the dense matrices keep 0.02 to 0.46 and the experts a median 0.014
to 0.18 on 28 layers (0.33 and 0.43 on layers 26 and 29), with the right side keeping 0.44 to 0.85, finding 24's
"scale 1.0 with the second term". Rows moved 0.0001 to 0.0004 on the dense matrices and 0.0005 to 0.0009 per
packed expert tensor: the second preservation claim in the census that holds (finding 57). Against TrevorJS's own
26B-A4B edit of the instruct model the saved leading vectors stand at 0.79 to 0.99 on all 90 (median 0.97);
against the other four edits of this checkpoint 0.41 or less except at one layer. The scorer's 30 flags are the
worst expert's first share in 29 layers (0.946 to 0.990) where every median expert is 0.990 or above, and the
within-layer cosine of layer 15 (0.949). The configuration carries the 5.16 save form (finding 39).

Why it matters: the method's fingerprint (finding 24) reads the same from a second maker's run on a second Google
checkpoint, which is what a fingerprint has to do; the expert pass the card describes is the first in the census
to reach every expert of the mixture with its rows put back under a card that says it does (finding 20 counts the
edits of this base that reach no expert; TrevorJS's own reaches them all); and the flag rule should read the median expert.

Evidence: `results/weights/xdavxd-gemma-4-26B-A4B-it-qat-heretic-ega.json` (`experts` block per packed tensor
with `remaining_first_direction`, `direction_agreement` and `first_singular_energy_share` over 128 experts,
`row_norms.max_relative_error`), `results/meta/xdavxd-gemma-4-26B-A4B-it-qat-heretic-ega.json`, the direction
file under `nautilus34/measurements/pair-5/` against `nautilus3/measurements/pair-4/`, and the reading in
`docs/cards/`. Round 38 puts the 0.97 beside a 1.000: DuoNeural's 26B-A4B copy, under a card that names the expert-granular method as its own, stands at 1.000 to TrevorJS's directions on all 90 names, so the method's independent re-run and the copy of a run are now both measured (finding 95).

## 75. Seven more copies stand on QAT-unquantized checkpoints, every field names them, Google's QAT revisions share one weight file per size and the E4B QAT vision tower is the instruct model's

Round 34 measured seven copies against google's `-qat-q4_0-unquantized` checkpoints (three on the 26B-A4B, three
on the 12B, one on the E4B, the E4B's first), bringing the census to twelve on four QAT originals (finding 48).
All seven read exactly 0 outside their windows against the QAT checkpoint, which differs from the instruct
model by 0.14 to 0.16 of a matrix (layer 0's attention output of the 12B, 0.1405; layer 20's of the E4B, 0.1553,
by range read), so each stands on the QAT file. All seven `base_model` fields name the QAT checkpoint, the four
Heretic exports included (finding 67's inherited header names the right model when the original's card does).
One repository, smashingtags/gemma-4-12b-it-abliterated, carries the instruct model's name over the QAT
checkpoint's weights, as its card and its field state. A range read places it: layer 0's attention output is
byte-equal to the QAT file at `58540658` and 0.14 from the instruct model's at `5926caa4`, and layer 20's down
projection, in the edit's window, is 0.021 from the QAT file and 0.74 from the instruct model's.

Two facts about the originals came with the round. Google's QAT revisions share one weight file per size: the
26B-A4B at `641f1844` and `f1e06dc5` and the 12B at `b8dea52d` and `58540658` carry the same shard checksums, so
copies pinned against different revisions are measured against one file. And the E4B QAT checkpoint's vision
tower is the instruct model's: prithivMLmods's QAT export carries the fourth shard `8080cb1a` that the seven
instruct-model E4B exports carry (finding 71), and a range read shows
`model.vision_tower.encoder.layers.0.mlp.down_proj.linear.weight` byte-equal between the QAT checkpoint at
`dfc5b925` and google/gemma-4-E4B-it at `fee6332c` while the language stack differs. The QAT file's values sit on
a grid the instruct file's do not (a median 24 distinct values per block of 64 and 11 to 14 percent exact zeros,
against 62 and none), which is the q4_0 quantisation written out in bfloat16.

Why it matters: the QAT checkpoints are a parallel population of originals with their own copies, and the
census can tell the two apart from the weights, from the shards and from a single range read; the vision-tower
checksum that finding 71 read as the library's layout now spans two Google releases, so a shard rule has to know
which tensors a release shares with another.

Evidence: the seven `results/weights/` reports of round 34 (`summary.max_relative_difference_outside_changed_set`
0 on each), `tools/hub_range_read.py` on the four tensors named with the commits above, the shard checksums in
`data/batches/round-34-batch-1.json` and the hub's file listings, and the readings in `docs/cards/`. Round 35 adds two E4B QAT copies, coder3101's and igorls's; igorls's first shard equals prithivMLmods's QAT export's and its
fourth is the shared vision tower (finding 82). Round 37 adds four QAT copies and the 31B QAT original, and pins two 12B copies at the checkpoint's revisions `b6ed8627` and `58540658`, one weight file `26f2cee4` under both (findings 83 and 84). Round 36 adds eight QAT copies, the 31B checkpoint now holding four pinned at its revisions `4f926903` and `1e4d8bee`, which carry one pair of shards (`8ad3c678`, `a373e714`); OS-Software's and JJaguar's 12B exports share their first two shards (`513abfa9`, `ebfb917e`), the layout below both windows (finding 90).

## 76. An arbitrary-rank edit of the diffusion variant capped at layer 20: fifteen residues, twenty-three edits, no expert, rows in the claim band without a claim, and twelve directions shared with the earlier search

Umranz/diffusiongemma-26B-A4B-it-abliteration is Heretic's arbitrary-rank branch on google/diffusiongemma-26B-A4B-it
at `156b5c86`, trial 144 of 150, target layers 1 to 20 on both writers, with the maker's reason that deeper
ablation of the block-diffusion mixture degrades it. Measured: 38 of 1,047 tensors under the `model.decoder.`
prefix (finding 40), both writers of layers 1 to 19, no expert, router or tower tensor, exactly 0 outside.
Fifteen of the 38 are residues, both writers of layers 1 and 3 to 8 and layer 2's down projection, changed by
0.0012 to 0.0045 with no leading direction (first shares 0.02 to 0.87) and both sides kept at 0.98 to 1.01; 23
are edits, the attention outputs of 2 and 9 to 19 and the down projections of 9 to 19, changed by 0.008 to
0.047, input side on the attention outputs at weights 0.87 to 1.20, layer 18's down projection the largest at
1.42. Each matrix carries its own direction (within-layer cosines 0.001 to 0.115). Rows moved 0.0043 to 0.0079
on 37 of 38 under a card that claims no preservation, finding 22's band and finding 68's pattern. Against
Goodoldjam's arbitrary-rank edit of the same base the saved vectors stand at 0.86 to 0.99 on twelve of the
twenty matrices both reach (the attention outputs of layers 7, 8, 9, 12, 14, 15 and 16 and the down projections
of 7, 8, 13, 15 and 16) and at 0.13 or less on the other eight; against edwixx's 0.39 or less. The token side
adds `return_dict_in_generate` to the generation file.

Why it matters: the third copy of the diffusion variant reads like the second, a search that leaves the experts
alone and the deep layers alone, and the two searches agree on most of the layers both reach; the fifteen
residues are the solver's rewritten-and-restored matrices (finding 22) on a base where the card's cap, not the
kernel's reach, sets the window.

Evidence: `results/weights/Umranz-diffusiongemma-26B-A4B-it-abliteration.json`,
`results/meta/Umranz-diffusiongemma-26B-A4B-it-abliteration.json`, the direction file under
`nautilus34/measurements/pair-8/` against `wheat30/measurements/pair-6/` and `wheat30/measurements/pair-5/`, and
the reading in `docs/cards/`.

## 77. Two Heretic copies measured again against the parents their READMEs name read as their cards say, and the kernels the first pass read through a round trip and a fine-tune were the right ones

sh0ck0r/Artemis-31B-v1.1-heretic and Pranavz/Hearthfire-24B-heretic were measured in rounds 20 and 29 against the
grandparents their `base_model` fields name, google/gemma-4-31B-it and mistralai/Mistral-Small-3.2-24B-Instruct-2506,
and read their named parents' 4-bit round trip and fine-tune under the Heretic edits (findings 45 and 61). Round 35
measured the same weight files against the parents themselves, TheDrummer/Artemis-31B-v1.1 at `d613e5a4` and
LatitudeGames/Hearthfire-24B at `1b854cc8`. Against Artemis, sh0ck0r's copy changes 73 of 1,188 tensors where the
first pass changed 603: the attention outputs of layers 25 to 59 and the down projections of 17 to 54, both kernel
windows the card prints, exactly 0 outside (529 of the 602 matrices the round trip had moved are now equal), one
direction (group cosines 0.977 to 0.999), the output side on 69 of 73, 45 flags in place of 686, all first shares
of 0.922 to 0.990 at the windows' low-weight ends. The down kernel reads within 0.04 of the card's on layers 43 to
54 and under it by 0.08 to 0.62 on 17 to 41 (0.64 against 1.26 at the peak), the attention kernel within 0.10 on 18
of 35 layers and under by 0.11 to 0.32 on the other 17: the same shortfalls the first pass read through the round
trip. The kept fractions agree with the first pass to the second decimal and the leading directions at a median
cosine of 0.998, 0.85 or better on 64 of 73; the nine that disagree are the attention outputs of layers 25 to 32 and
50, where the first pass had read the round trip's noise as the direction. Against Hearthfire, Pranavz's copy
changes 56 of 363 tensors where the first pass changed 282: the down projections of all 40 layers and the attention
outputs of 19 to 34, both windows exactly, exactly 0 outside (226 matrices the fine-tune had moved are now equal),
first shares 0.9985 to 0.9995, two flags in place of 347 (within-layer cosines 0.946 and 0.955 at layers 25 and
27). The kept fractions are the first pass's to the second decimal and the leading directions equal at 1.000 on all
56; the down kernel reads within 0.07 of the card's on 16 layers and within 0.20 on 13 more, under by 0.21 to 0.51
on ten (1.62 against 3.27 at layer 0), the attention heights 1.13 to 3.22 under the card's 3.06 to 3.75, as finding
61 read them through the training. The token side moves one field each at home (`moe_intermediate_size` on
sh0ck0r's, `rope_parameters` on Pranavz's) and keeps the 5.16 save form on sh0ck0r's and the 1,000 dropped
control-token declarations on Pranavz's, whose `tokenizer.json` is 155 bytes longer than Hearthfire's.

Why it matters: a pairing by the wrong field costs flags and a cleaner report, and the reading survives it. The
kernels, kept fractions and directions the first pass read through a 9 percent round trip and a 1 percent fine-tune
are the ones read against the parent, to the second decimal, and the parents' own changes were the whole of what
the first pass could not place. The new reports are the readings of record for both copies; the first reports stay
as the record of what the `base_model` field's pin measures. Findings 45 and 61 are settled by them.

Evidence: `results/weights/sh0ck0r-Artemis-31B-v1.1-heretic.vs-Artemis-31B-v1.1.json` beside
`results/weights/sh0ck0r-Artemis-31B-v1.1-heretic.json`,
`results/weights/Pranavz-Hearthfire-24B-heretic.vs-Hearthfire-24B.json` beside
`results/weights/Pranavz-Hearthfire-24B-heretic.json`, the two `results/meta/` reports under the same suffixes, the
direction files under `wheat35/measurements/pair-2/` and `pair-3/` against `nautilus20/` and `wheat29/`, and the
readings in `docs/cards/`.

## 78. Felldude's E4B copy against the instruct model is a fine-tune of 0.1 to 0.7 percent on two bands of layers, with no direction and the middle twelve layers and both towers untouched

Felldude/gemma-4-E4B-uncensored was measured in round 29 against google/gemma-4-E4B, the pretrained base its field
names, and read the base-to-instruct training on 595 tensors, with range reads placing the copy within 0.006 of the
instruct model on the tensors sampled (finding 62). Round 35 measured the same file against google/gemma-4-E4B-it at
`fee6332c`. 245 of 2,076 tensors changed, all in the language stack: the queries, keys, values, attention outputs,
gates, ups and down projections of layers 0 to 14 and 27 to 41, with 31 per-layer input gates, 28 per-layer
projections and 13 post-per-layer-input norms, by 0.0011 to 0.0069 (median 0.003; 0.099 on layer 0's per-layer
gate). Layers 15 to 26 changed by 0.0001 or less (layer 20's attention output by 0.00003), the audio and vision
towers and the embeddings are equal (1,662 tensors at exactly 0), and the largest change outside the changed set is
0.00099, the threshold, with 17 more language tensors just under it. No direction: first shares 0.001 to 0.016 and
both kept fractions within 0.03 of 1 on every changed matrix. The 304 flags are the per-layer entry's reading of a
training pass: 187 unexpected changes, 58 first shares, 58 direction cosines, one cross-kind. The leading vectors
share nothing with round 29's (median cosine 0.009), as they must, the first pass having measured the instruct
training. The token side is consistent against the instruct model, where it was unexplained against the base.

Why it matters: finding 62's range reads predicted these numbers to the fourth decimal, and the full measurement
names what the copy is, a light training pass on the first fifteen and last fifteen layers with the middle twelve
left alone, under a card that says "uncensored" and names the pretrained base. It settles finding 62: the copy's own
change is small, directionless and confined to two bands, and the 5 to 11 percent of dense change the first pass
read was the instruct training it stood on. The new report is the reading of record; the first stays as the
record of what the field's pin measures.

Evidence: `results/weights/Felldude-gemma-4-E4B-uncensored.vs-E4B-it.json` beside
`results/weights/Felldude-gemma-4-E4B-uncensored.json`, the `results/meta/` report under the same suffix, the
direction file under `wheat35/measurements/pair-1/` against `wheat29/`, and the reading in `docs/cards/`.

## 79. A 31B copy drops the `.linear.` segment from its vision tower's names, carries a Heretic kernel its card does not print, and its 189 encoder linears are fresh draws

Kooten/gemma-4-31b-abliterated-v1.1 against google/gemma-4-31B-it at `419b2efe` is the first pair through the
in-tower name mapping: the copy's vision encoder names every linear without the `.linear.` segment Google's names
carry, and the `name_mapping` block of the report records the infix carried by the original and 189 names
renamed. Two things read. In the language stack, 67 of 832 tensors changed, the down projections of layers 20 to
59 and the attention outputs of 24 to 50, one direction (cosine 0.99998 across the group), first shares 0.981 to
0.996, the output side on all 67, rows moved 0.004 to 0.087 (0.53 on layer 59's down projection) under no claim.
The kept fractions read as two straight lines: the attention weight rises from 0.71 at layer 24 to 1.47 at 37 and
falls to 0.70 at 50 (slope 0.058 per layer), the down weight from 0.69 at layer 20 to 1.15 at 54 and 1.08 at 59
(slope 0.0135). The card prints Heretic's trial count (929), refusals (26 of 100) and KL divergence (0.3687) and no
kernel; the kernel is recovered from the weights, finding 59's check run the other way. In the vision tower, the
189 renamed encoder linears differ from Google's by relative differences of 1.205 to 1.208 (the down projections by
1.642 to 1.644), first shares 0.005 to 0.175 and cosines of 0.000; by byte range the copy's matrices have a
standard deviation of 0.0199 on all three sampled (Google's 0.0295, 0.0152 and 0.0295), 62 distinct values per
block and 0.6 percent zeros, fresh draws at the library's default initialisation of 0.02, and the relative
differences are the square roots of one plus the squared scale ratios. The 167 other vision tensors (six norms per
layer, the patch embedder, the scalars and the embedding projection) are byte-equal to Google's. The 211 flags are
the 189 renamed linears as unexpected changes and 22 first shares at the kernel's shoulders. The configuration
carries 5.6.0.dev0 against the original's 5.5.0.dev0 and the home judgement reads it consistent with re-save
noted; the repository carries a 4.1 MB Heretic checkpoint file named for the original.

Why it matters: finding 63's case a second time, a vision tower re-initialised under a card that says "Uncensored
using Heretic" and nothing of the tower, and this time the mechanism is visible in the names: a library that
loaded the tower under one set of names, found no weights for them and drew fresh ones, then saved them under
the new names. The in-tower mapping made the pairing; without it the 189 tensors would have been unpaired on both
sides and the fresh draws unread. The copy goes among those carrying a change their cards do not name.

Evidence: `results/weights/Kooten-gemma-4-31b-abliterated-v1.1.json` (`name_mapping`, the per-tensor rows of the
vision encoder), `results/meta/Kooten-gemma-4-31b-abliterated-v1.1.json`, the range reads recorded in the reading
in `docs/cards/`, and the direction file under `wheat35/measurements/pair-4/`.

## 80. huihui-ai's E2B second version, reached through a re-upload, is the first version's direction at two and a half times the weight from five layers earlier, with Google's release-day template

Dzluck/gemma-4-E2B-it-abliterated-v2 carries huihui-ai/Huihui-gemma-4-E2B-it-abliterated-v2's single weight file
`c1a72f14` and its README, template and token files byte for byte, under a commit titled "Add files" and no
duplicate relation in the hub's metadata, so the pinner's duplicate rule, which compares weight files against
measured copies, had nothing to match. The parent is unmeasured; this is its only measurement, the third such case
after findings 64 and 73. Against google/gemma-4-E2B-it at `70af34e2`, 60 of 2,011 tensors changed, both writers of
layers 5 to 34 (the card: "the first 5 layers have not been abliterated"), exactly 0 outside, one direction
(0.999999 within and across layers and kinds), first shares 0.9992 to 0.9995, and a left kept fraction of -1.4997
to -1.5011 on all 60: a weight of 2.50, the weight the maker's E4B edit uses (finding 21). Against the saved vectors
of the maker's first E2B version (round 13, weight 1.00 on layers 10 to 34) the left and right vectors agree at
1.000 on all 50 matrices both edit; against the eight other E2B edits at 0.02 to 0.05. Recipe match, no flag. The
token side's one open field, an 11,926-byte `default` template against the pin's 17,336 (and a tokenizer
configuration 27 bytes shorter), is Google's own file: both are byte-equal to google/gemma-4-E2B-it at `4742fe84`,
the release revision of 04-02 that was current when huihui-ai made the edit on 04-11, two months and five template
revisions before the re-upload's creation date, which is where the pin falls.

Why it matters: the maker's second version is the first version's direction to the third decimal, multiplied by
two and a half and started five layers earlier, which the card describes as five layers added and a perplexity
rise from 164.5 to 180.3; the maker's 31B moved from 1.00 to 1.5 between its versions the same way (finding 21).
For the pinner, a README whose first heading names another repository is a re-upload candidate whatever the
commit title says, and the duplicate check has to compare weight files against the named repository's hub listing
whether or not it is measured. For the metadata tool, the earlier-revision template round 31 left owed now has a
cause and a rule: read the original's snapshot current at the parent's creation date rather than the re-upload's.

Evidence: `results/weights/Dzluck-gemma-4-E2B-it-abliterated-v2.json`,
`results/meta/Dzluck-gemma-4-E2B-it-abliterated-v2.json`, the hub's file listing for
`huihui-ai/Huihui-gemma-4-E2B-it-abliterated-v2` and the sha256 comparisons recorded in the reading in `docs/cards/`,
and the direction file under `wheat35/measurements/pair-5/` against `wheat13/` and `nautilus18/`.

## 81. Jiunsong's SuperGemma 12B, reached through a hub duplicate, projects one direction at a weight of 0.50 under a merged adapter on every linear, and bans 48 token sequences

enkato64bit/SuperGemma-4-12b-abliterated is one commit, "Duplicate from Jiunsong/SuperGemma-4-12b-abliterated",
and the hub's listing of that repository (created 06-25) shows the same single weight file `e67b7e6c` and the same
fourteen files; the batch note's "different weight files" was against Jiunsong's measured E4B export (finding 14),
the only Jiunsong file the duplicate rule could see. The parent is unmeasured; this is its only measurement. The
card describes a fused checkpoint made in two stages, a refusal-direction pass and a post-training for coding,
Korean answers and JSON formatting, and the repository's `fuse_summary.json` names them, a base
"SuperGemma4-12B-obliteratus-v7-capabilitypatch-r2-contractfix-r3-fused" and an adapter "...code04fix-r4". Both
stages read. Against google/gemma-4-12B-it at `707f0a3b`, 320 of 677 tensors changed, every linear of all 48
layers, the 349 norms and embeddings equal, the largest change outside the changed set 0.00096 (eight down
projections of layers 2 to 5 and 8 to 11 under the threshold). The ablation: both writers of layers 14 to 37, 48
matrices, one direction (within-layer cosines 0.99, the down projections' group 0.9995), the left kept fraction
0.48 to 0.51 on all 48, a weight of exactly 0.50, the first below one in the census (huihui-ai's are 1.0 and above,
finding 21; nguyenthilaitrieulong's "standard" ablation ran 0.75 to 1.00, finding 64). The adapter: every linear
moved by 0.11 to 0.68 percent with a steep spectrum (layer 10's gate: singular values 0.29, 0.13, 0.09, 0.07; first
share 0.45) and first shares of 0.12 to 0.67 on the five kinds the projection leaves alone, in pairs of layers (0
and 1, 6 and 7, 12 and 13, and so on to 42 and 43) that moved 0.0027 to 0.0068 where the layers between moved 0.0011
to 0.0036. Where the stages overlap the ablated writers' first shares fall to 0.63 to 0.80. The direction stands at
0.57 to MoonRide's, BinxNet's and 3MPER0RR's 12B edits and 0.74 at the median to the richardyoung coder copy's
Heretic parent. The 361 flags are the single-projection entry reading the adapter's 272 matrices as unexpected
changes and the overlapped writers' first shares. On the token side the home judgement closes four configuration
fields the copy leaves out; what remains is the release's own: `generation.bad_words_ids`, 48 token sequences the
decoder may not produce, decoded with the pin's tokenizer as "confidential instructions" and "confidential", "I can
give a concise answer" in six spellings, the JSON code fence in twelve spellings, nineteen fragments of Python and
TypeScript test code, seven forms of a tool-call key and "http://localhost8080"; `generation.no_repeat_ngram_size`
12; and a 28,982-byte template headed "Google Gemma 4 Canonical Chat Template ... Published: 2026-07-09" that no
revision of google/gemma-4-12B-it carries.

Why it matters: two methods under one card, both readable (finding 49's composition, with the weight below one for
the first time), and the card's validation table (blank responses 0, hidden-thought leaks 0, release-surface
findings 0) describes outputs produced under a decoder-side list that bans the sentences and fences the table
counts. The list is the second in the census after finding 64's five sequences and the first that bans a code
fence and a stock sentence. For the pinner, a hub duplicate's weight files are compared against its named source's
hub listing, measured or not, and the measurement is recorded as the source's.

Evidence: `results/weights/enkato64bit-SuperGemma-4-12b-abliterated.json`,
`results/meta/enkato64bit-SuperGemma-4-12b-abliterated.json` (`generation.bad_words_ids` decoded in the reading),
the hub's file listings for both repositories, the direction file under `wheat35/measurements/pair-6/` against
the thirteen other 12B edits, and the reading in `docs/cards/`.

## 82. Two Heretic edits of the E4B QAT checkpoint by two branches: the arbitrary-rank one stands on the E4B family's directions at 0.91 to 0.95, the LoRA-rank one searched with thinking on stands alone

coder3101/gemma-4-E4B-it-qat-q4_0-unquantized-heretic and igorls/gemma-4-E4B-it-qat-q4_0-unquantized-heretic both
name google/gemma-4-E4B-it-qat-q4_0-unquantized in the field and both read exactly 0 outside their windows against
it at `dfc5b925`, which places them on the QAT checkpoint (finding 48). coder3101's is Heretic v1.2.0's
arbitrary-rank branch with row-norm preservation, start 20 and end 36 on the card: the attention outputs of layers
20 to 35 changed (16 of 2,076), the down projections exactly 0 as on the maker's 12B QAT export, input side on 16 of
16 at weights 1.19 to 1.91, several directions per matrix (first shares 0.455 to 0.969), rows 0.0065 to 0.0078
under the claim, finding 22's band a sixth time; 16 flags. Its right vectors stand at a median of 0.91 to the
maker's instruct E4B edit (round 8) and at 0.92 to 0.95 to JokeHer's, NullpoLab's and alphakek's E4B exports, 0.85
and 0.88 to llmfan46's two, 0.07 to prithivMLmods's linear-kernel edit of the same checkpoint and 0.01 to
huihui-ai's: the maker's seventh copy, the third on a QAT checkpoint, the fifth maker whose QAT edit stands on the
family's instruct directions (finding 72). igorls's is the LoRA-rank branch "with chain-of-thought-aware
evaluation" (KL 0.055, about 21 percent refusals against 98): both writers of layers 21 to 36 changed (32 of
2,076), relative changes 0.099 to 0.214 on the attention outputs and 0.055 to 0.095 on the down projections, three
to four times coder3101's on the same checkpoint, a direction per matrix (within-layer cosines 0.001 to 0.106),
input side on 29 of 32 at weights 1.33 to 3.46 (neither side on the attention outputs of 22, 27 and 33), rows
0.016 to 0.28 under no claim; 64 flags. Its left vectors reach medians of 0.57 to 0.65 to the arbitrary-rank family
and 0.07 or less to the kernel and projection edits, 0.37 to coder3101's on the right. Its first shard equals
prithivMLmods's QAT export's and its fourth is the vision tower the QAT checkpoint shares with the instruct model
(finding 75). The token side of both differs from the pin in version strings alone.

Why it matters: the E4B QAT checkpoint now carries three measured edits by three makers (prithivMLmods's kernel,
coder3101's arbitrary-rank, igorls's LoRA-rank), and the directions sort them as finding 72 sorted the 12B's, the
arbitrary-rank searches finding one family's direction and the thinking-on LoRA search finding another, as the
same maker's 12B QAT search did (finding 69). igorls's are the largest Heretic changes the census has read on an
E4B, and the LoRA branch, read here and on wnfldchen's 12B QAT export, wants a recipe entry of its own: a direction
per matrix, input side, rows unrestored.

Evidence: `results/weights/coder3101-gemma-4-E4B-it-qat-q4_0-unquantized-heretic.json`,
`results/weights/igorls-gemma-4-E4B-it-qat-q4_0-unquantized-heretic.json`, the two `results/meta/` reports, the
direction files under `wheat35/measurements/pair-7/` and `pair-8/` against twenty E4B edits, and the readings in
`docs/cards/`. Round 37 places MoonRide's April edits as the earliest members of both families, the E4B at 0.99 to Refusals5 and coder3101's and the 31B at 0.97 to llmfan46's, and NullpoLab's Refusals8-attn at 0.99 to coder3101's (findings 86 and 87). Round 38 adds SassyDiffusion's two exports to the families, the 26B-A4B at 0.98 to llmfan46's and coder3101's and the E4B at 0.98 to coder3101's and 0.99 to alphakek's and MoonRide's (finding 98).

## 83. One maker's arbitrary-rank exports searched on Japanese prompt sets, on two QAT checkpoints through the tool's LoRA-adapter branch, read both writers on the input side with the rows held and find directions the English searches do not

OS-Software's two Japanese-prompt exports (round 37, pairs 1 and 2) are Heretic 1.4.0's arbitrary-rank ablation
through its LoRA-adapter path (`use_ara_lora`, row-norm preservation), as their cards say, on the 12B and 26B-A4B
QAT-unquantized checkpoints, and the cards say the prompt sets were Japanese. On the 12B (revision `90825e3e`
against the checkpoint at `b6ed8627`), 54 of 677 tensors changed: both writers of layers 13 to 39, the card's start
13 and end 40 with the end exclusive, and nothing else, exactly 0 outside. Every one of the 54 is on the input side
(left kept 0.64 to 0.99, right kept 0.26 or less), at weights of 0.74 to 1.95 read as one minus the right kept
fraction, with a few directions per matrix (first shares 0.36 to 0.96, fourth cumulative shares 0.74 to 0.99), and
the rows moved 0.0003 to 0.0057, at or under the bottom of finding 22's band on all 54. On the 26B-A4B (revision
`184e64bb` against the checkpoint at `f1e06dc5`), 32 of 1,013 changed: the attention outputs and shared down
projections of layers 7 to 22, the card's start 7 and end 23, no expert touched, exactly 0 outside; input side on
all 32 at weights 1.24 to 2.09, rows 0.0012 to 0.0081 (in the band on five, under it on 26, over it by 0.0001 on
one). The cards' own numbers: 0 refusals in 100 against 100 at a KL divergence of 0.0637 on the 12B, 1 in 100 at
0.0362 on the 26B-A4B, preservation weights 1.0000 on both.

What the Japanese search found is not the English searches' direction. Against the saved vectors of thirty-three
12B measurements, the 12B export's leading directions stand at a median of 0.40 on the left and 0.30 on the right
to coder3101's instruct edit, 0.40 and 0.36 to llmfan46's QAT edit of the same round, 0.37 and 0.29 to coder3101's
QAT edit and 0.36 and 0.34 to wnfldchen's, where those four English searches stand at 0.92 to 0.97 to llmfan46's QAT
edit (finding 87); the kernel edits stand at 0.14 or less. The 26B-A4B export stands at 0.62 and 0.65 to the maker's
own English v2 export, 0.70 and 0.65 to coder3101's and 0.69 and 0.65 to llmfan46's two 26B edits, and 0.51 and
0.59 to mewse's, where llmfan46's two 26B searches stand at a median of 0.94 to each other (finding 72). A refusal direction found on
Japanese prompts shares a third of its cosine with the English one on the 12B and two thirds on the mixture, and
nothing in the weights says which is the better one; the cards' refusal counts are the maker's own on the maker's
own prompts. The 26B-A4B export shares five of its eleven shards (the first, second, ninth, tenth and eleventh) with
the maker's English v2 export byte for byte, the shards the window of layers 7 to 22 does not reach, so a shard
match between two of one maker's edits is the window's complement and not a shared edit. The 12B export's first
shard (`513abfa9`) is the 12B QAT library layout shared with wnfldchen's and igorls's exports (finding 71). Both
copies' fields name the QAT checkpoints; both token sides are the checkpoints' files under newer version strings,
the 12B's template differing by its line endings alone. The maker has an unmeasured `-ja` (06-25) and `-v3` (09-07)
of the 12B beside these. Evidence: `results/weights/OS-Software-gemma-4-12B-it-qat-q4_0-unquantized-heretic-ja-v2.json`,
`results/weights/OS-Software-gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ja.json`, the two `results/meta/`
reports, the direction files under `wheat37/measurements/pair-1/` and `pair-2/`, and the readings in `docs/cards/`. Round 36 reads the maker's first Japanese export, the `-ja` of 06-25, on both writers of layers 10 to 46 at weights to 3.73 with rows to 0.21, its output direction at 0.52 to 0.64 to the English family and 0.59 to this second search (finding 93).

## 84. A rank-256 adapter merged into the 31B QAT checkpoint reads on the attention outputs alone at weights to 4.5, with one matrix rewritten and a preservation claim that holds on no row

wnfldchen/gemma-4-31B-it-qat-q4_0-unquantized-heretic-merged (round 37, pair 3; revision `e9a15cd7` against
google/gemma-4-31B-it-qat-q4_0-unquantized at `1e4d8bee`, the first copy on that checkpoint and the census's fifth
QAT original) is, as its card says, the merged form of the maker's adapter repository: Heretic 1.4.0's
arbitrary-rank ablation at `ara_lora_rank` 256 with row-norm preservation, trial 6, `target_components`
`attn.o_proj`, start 24, end 54, preservation weight 0.1182, and an `export-summary.json` that records a second
redundant save cancelled after it rewrote the configuration and the first shard. The weights read the card's window
and target exactly: 30 of 1,188 tensors changed, the attention outputs of layers 24 to 53, nothing else, exactly 0
outside, 1,158 tensors equal to the original. The rank-256 adapter merged to one to four directions per matrix
(first shares 0.63 to 0.98, fourth cumulative shares 0.83 to 0.999). The edit is on the input side on 27 of 30 at
weights of 0.27 to 4.47 (median 1.54; 4.47 at layer 41, 4.12 at 53, 3.32 at 48), the largest Heretic weights the
census has read on a 31B; layers 38 and 43 keep more than 1 on both sides, the leading component amplified rather
than removed, as two of the maker's 12B attention outputs were (finding 72); and layer 50 is rewritten, relative
change 0.416, left kept -2.56 and right kept -0.14, a reflection and more on the output side of one matrix with its
rows moved 0.75. The rows moved 0.014 to 0.75 on all 30, every one above finding 22's band (0.0057 to 0.0080), under
the card's "row-norm preservation". The maker's 12B export held its rows within 0.0106 on 44 of 46 matrices under the
same words at a preservation weight of 0.9174; this export at 0.1182 holds none, the first preservation claim in
the census that reads as no preservation, and the weight the card prints is the reason. The card's own numbers: 8
refusals in 100 against 99 at a KL divergence of 0.0900, a W4A16 benchmark table and a `reproduce/` folder with the
trial record.

Against the saved vectors of twenty 31B measurements, the leading left vectors stand at 0.78 to 0.85 to the 31B
arbitrary-rank family (llmfan46 0.85, MoonRide's two 0.80 and 0.79, coder3101 0.78, Bahushruth 0.76) and the right
vectors at 0.37 to 0.40 to the same five: the rank-256 search on the QAT checkpoint keeps the family's output
direction and does not keep its input direction, the side this branch acts on. The token side is the checkpoint's
files under newer version strings. The adapter repository itself (120 tensors under a `base_model` prefix, 917 MB)
was refused at the pin, so the merged repository is the measurable form. Evidence:
`results/weights/wnfldchen-gemma-4-31B-it-qat-q4_0-unquantized-heretic-merged.json`, the `results/meta/` report,
the direction file under `wheat37/measurements/pair-3/`, the hub's listings of both repositories, and the reading
in `docs/cards/`.

## 85. A maker's first E4B copy is the pass the second copy was built on: 73 names, 57 directions at 1.000, a shard byte-equal, and TrevorJS's directions at 0.98 on all 73

TheUmbraWalker/gemma-4-E4B-it-heretic (round 37, pair 4; revision `9bf78429` of 05-16 against google/gemma-4-E4B-it
at `3555bddc`) carries, line for line, the lower of the two Heretic 1.3.0 cards stacked in the README of the
maker's second copy, TheUmbraWalker/gemma-4-E4B-it-2-heretic (round 30), made the next day: attention output
weight 1.31 at position 27.47, down projection 1.42 at 28.35, KL divergence 0.1487, 11 refusals in 100. The weights
are that card: 73 of 2,076 tensors changed, the attention outputs of layers 4 to 41 and the down projections of 7
to 41, the kernels' reach to the layer and the second copy's changed set exactly, rank one on every matrix (first
shares 0.994 to 0.999), one direction per layer (within-layer cosines 0.91 to 0.997), exactly 0 outside, the 54
shared-key-value tensors absent from the save as from the second copy's. On the same 73 names the leading
directions equal the second copy's at 0.99 or better on 57 and at a median of 1.000; the 16 that differ are the
attention outputs of layers 18 to 33, the second pass's attention window, where round 30 read two directions per
matrix, and on the down projections of 29 to 41, the second pass's other window, the leading direction is still
this pass's. The second copy's second shard (`df30ce31`) is byte-equal to this copy's. The second copy is this
copy plus the second pass and nothing else, which is what its stacked README says and what the directions now
show.

The kept fractions carry no readable weight, finding 46's scatter on a per-layer direction: one minus the left
kept fraction runs 0.28 to 1.15 across the attention window with no shape under the card's kernel, and the left is
below the right on 60 of 73. Against TrevorJS's E4B edit (round 7, the abliteration script's per-layer mean
difference) and senjiangchen's duplicate of it, the directions stand at 0.89 to 1.00 on all 73 names, median 0.98
on the left and 0.99 on the right: two tools that each find one direction per layer find the same one on this base,
which is why the E4B's per-layer edits sort into one family and its arbitrary-rank edits into another (finding
82). The `base_model` field names the pretrained google/gemma-4-E4B, as the second copy's does (finding 67); the pin
is the instruct model and the weights stand on it. The token side is the instruct model's files under newer
version strings, `moe_intermediate_size` closed by the home judgement. Evidence:
`results/weights/TheUmbraWalker-gemma-4-E4B-it-heretic.json`, `results/weights/TheUmbraWalker-gemma-4-E4B-it-2-heretic.json`,
the direction files under `wheat37/measurements/pair-4/` and `wheat30/measurements/pair-4/`, and the readings in
`docs/cards/`.

## 86. One maker's two April arbitrary-rank edits are the earliest members of the 31B and E4B families, each a selection inside its window with the rows in the band and the skipped matrices left as traces

MoonRide/gemma-4-31B-it-heretic-ara (round 37, pair 5; revision `cf80d7e7` of 04-12 against google/gemma-4-31B-it)
and MoonRide/gemma-4-E4B-it-heretic-ara (pair 6; `0327d8e7` of 04-11 against google/gemma-4-E4B-it) are Heretic
1.2.0's arbitrary-rank ablation with row-norm preservation, as their cards say: start 30 and end 54 at a
preservation weight of 0.1997 on the 31B, start 21 and end 38 at 0.5276 on the E4B. Both read the same shape. On
the 31B, all 24 attention outputs and 20 of the 24 down projections of layers 30 to 53 moved above the 0.001 line
(44 of 1,188) and the four others moved 0.0008 to 0.00098 just under it; of the 44, 36 are edits (23 attention
outputs, 13 down projections; first shares 0.89 to 0.97, input side on all 36, weights 1.35 to 4.39 with the
attention output of layer 48 at 4.39) and 8 are residues, relative change 0.0010 to 0.0018 with a first share of
0.01 or less. On the E4B, both writers of 21 to 37 moved above the line (33 of 2,076) and the down projection of 37
at 0.00091 under it; 26 are edits (16 attention outputs, 10 down projections; input side on all 26, weights 0.08 to
2.30, the 0.08 a small edit of the layer 25 down projection at relative change 0.0021) and 7 are residues. The
optimiser touched every matrix in each window and chose which to edit, finding 58's residues with the selection
visible; the traces under the line are the same change at a smaller size. The rows moved 0.0059 to 0.0077 on all
36 edits of the 31B and 0.0051 to 0.0078 on the 26 of the E4B, finding 22's band on 61 of the 62 edited matrices
and 0.0051 on the other, the seventh and eighth times the band has read under the claim; the residues' rows moved
0.0005 to 0.0008. Nothing outside either window moved. The cards' own numbers: 11 refusals in 100 at a KL
divergence of 0.0508 on the 31B, 4 in 100 at 0.0162 on the E4B.

Both are the earliest dated members of the families finding 82 named. The 31B edit's directions stand at 0.97 on
the left and 0.99 on the right to llmfan46's 31B edit (18 shared), 0.95 and 0.98 to coder3101's (24), 0.87 and 0.95
to the maker's own custom copy of 05-07 (42 shared, a different window and search), 0.79 and 0.37 to wnfldchen's
QAT export (finding 84) and 0.69 and 0.65 to Bahushruth's; the kernel and projection edits of the 31B at 0.23 or
less. The E4B edit's stand at 0.99 on both sides to NullpoLab's Refusals5 (27 shared) and coder3101's E4B edit
(17), 0.98 and 0.95 to llmfan46's ultra copy, 0.94 and 0.98 to NullpoLab's Refusals8-attn (finding 87), 0.90 and
0.98 to JokeHer's; the per-layer edits at 0.40 or less. Four makers' searches in April and May found the same
input direction on each base at 0.95 or better, and the direction was there from the branch's first week. The
E4B save leaves out the 54 shared-key-value tensors (finding 71). Both token sides are the originals' files under
newer version strings, `moe_intermediate_size` closed by the home judgement. Evidence:
`results/weights/MoonRide-gemma-4-31B-it-heretic-ara.json`, `results/weights/MoonRide-gemma-4-E4B-it-heretic-ara.json`,
the two `results/meta/` reports, the direction files under `wheat37/measurements/pair-5/` and `pair-6/` against
twenty measurements of the 31B and thirty-four of the E4B, and the readings in `docs/cards/`.

## 87. A card that names one writer, measured on both: the down projections are edited, on this copy and by byte range on its sibling, and the writer count the weights give is the check on the card

NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8-attn (round 37, pair 8; weights uploaded 04-05, revision `fa08a885`
of 04-29 against google/gemma-4-E4B-it at `292a7e27`) says in both its Japanese and English cards that it was made
with Heretic 1.2.0's arbitrary-rank branch at commit `3b70fe5` with `target_components = ["attn.o_proj"]`, "attention
outputs only", start 17 and end 42. The weights carry two writers. 25 of 2,130 tensors changed: 14 attention
outputs of layers 17 to 25 and 27 to 31, and 11 down projections of layers 18, 21 and 23 to 31. The down
projections are edits by every measure the attention outputs pass: relative changes 0.016 to 0.034, first shares
0.40 to 0.94 (0.40, 0.45 and 0.54 at layers 18, 21 and 26 with fourth cumulative shares 0.74 to 0.89), input side
on all 11, weights 1.23 to 1.51, rows 0.0008 to 0.0032, and with the attention outputs their leading directions stand at 0.81 to 0.99 on the 21 names
shared with the maker's Refusals5 (nine of them down projections), which edits both writers by its card. Five more tensors moved
under the line (the down projections of 17, 19 and 20 at 0.00011 to 0.00013, 22 at 3e-6, the attention output of 26
at 2e-6). The window ends at 31 against the card's 42: nothing from 32 to 41 moved. Byte-range reads against the
hub settle that the copy is not alone. The maker's Refusals6-attn, "attention only" by its card too, differs from
Google's down projection of layer 28 by 0.0233 where this copy differs by 0.0226, and the two copies differ
from each other by 0.0053; on the down projection of 24, 0.0207 and 0.0186; on the down projection of 33, 0.0140
where this copy is byte-equal to Google's, as its changed set says. The tool's pull-request branch at `3b70fe5`
applied the ablation to both writers whatever `target_components` said, and the cards report the setting. The
cards' own numbers, 8 refusals in 100 at a KL divergence of 0.0151 here and 6 in 100 at 0.0211 on the sibling,
are measurements of models with both writers edited.

The round's other one-writer card is the control. llmfan46/gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic
(pair 7; revision `556c19b5` against the 12B QAT checkpoint at `58540658`) says Heretic 1.2.0's arbitrary-rank
ablation on `attn.o_proj` from layer 24 to 35, and the weights are that: 11 of 677, the attention outputs of layers
24 to 34, no down projection, exactly 0 outside, input side on all 11 at weights 1.23 to 2.64, rows 0.003 to 0.037
under no claim; its directions stand at 0.97 and 0.94 to coder3101's 12B QAT edit, 0.96 and 0.91 to wnfldchen's and
0.95 on both sides to the maker's own instruct 12B edit, finding 72's rule a fifth time. The release version read
one writer where the card said one; the branch read two. The writer count is what the changed set is for: it is
read from the weights and compared with the card, not taken from it, and this pair is the first in the census
where the two disagree on a Heretic export and the weights are shown right on a second copy. The attention-only
copy's directions stand at 0.99 on both sides to coder3101's E4B edit and 0.98 and 0.99 to Refusals5, the E4B
family (finding 82); its template is byte-equal to Google's revision `c53e9d33` of 04-28 on an unchanged weight
file. llmfan46's export carries the maker's macro template in `tokenizer_config.json` again (finding 19). Evidence:
`results/weights/NullpoLab-gemma-4-E4B-it-Heretic-ARA-Refusals8-attn.json`,
`results/weights/llmfan46-gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic.json`, the two `results/meta/`
reports, `tools/hub_range_read.py` on the four tensors named against NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals6-attn,
the hub's commit histories of the maker's four repositories, the direction files under `wheat37/measurements/pair-7/`
and `pair-8/`, and the readings in `docs/cards/`.

## 88. A repository named for the Gemma 4 E2B is Google's first-generation gemma-2b-it with its two writers edited, which the shapes say before any download

TurkishCodeMan/gemma-4-e2b-it-abliterated (revision `84c7f480` of 06-17; `base_model` google/gemma-4-E2B-it; card
"a strictly abliterated version of google/gemma-4-E2B-it (or the equivalent 2B-it base model)", an orthogonal
projection on `o_proj` and `down_proj`) was refused at the round 39 pin stage as a partial export: 164 tensors
named `model.layers.N.*` for layers 0 to 17 and no towers, where the E2B has 2,011 tensors over 35 layers. The
fixture says more. Its 164 tensors are 18 layers of nine kinds plus the embedding and the final norm, every one
in float16, and its configuration is `GemmaForCausalLM` with `model_type` gemma, hidden size 2048, intermediate
size 16384, 8 heads and one key-value head of dimension 256, a vocabulary of 256,000 and 8,192 positions: the
first-generation Gemma 2B, not the Gemma 4 E2B (hidden 1536, intermediate 6144, 35 layers, vocabulary 262,144).
All 164 shapes differ from the E2B's and nothing pairs by name or by shape. Byte-range reads against the hub place
it. The layer 0 query equals google/gemma-2b-it's to the last bit (relative difference 0.00000; 0.0166 to
gemma-1.1-2b-it, 1.28 to the pretrained gemma-2b), the layer 17 input norm and the final norm equal gemma-2b-it's,
and the layer 17 attention output and layer 9 down projection differ from gemma-2b-it's by 0.0252 and 0.0265, the
two writers the card names edited at the size the census reads on a projection. The copy is gemma-2b-it with an
abliteration on its attention outputs and down projections, under a Gemma 4 name and a Gemma 4 `base_model` field,
uploaded in two folder commits two minutes apart with a 5.0 GB single file and a 34 MB tokenizer. The card's
parenthesis is the only true statement of its parent. The pin was right to refuse and wrong about why, and a shape
check at the names step (every paired name's shape equal, or the pair refused with the first mismatch named) would
have said so without a download; it is owed to the pinner. A measurement against gemma-2b-it is possible through
the ordinary path once the first-generation Gemma is a pinned original. Evidence:
`tests/fixtures/round2/84c7f4804575.json` against `tests/fixtures/round2/70af34e20bd4.json`, the hub's commit
history and file listing of the repository, and `tools/hub_range_read.py` on the five tensors named against
google/gemma-2b-it, google/gemma-1.1-2b-it and google/gemma-2b.

## 89. Two makers' arbitrary-rank searches of the 31B QAT checkpoint, five days apart, find one direction at 0.99, and three QAT edits stand on their makers' instruct directions

coder3101/gemma-4-31B-it-qat-q4_0-unquantized-heretic (06-06, round 36 pair 2) and
llmfan46/gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic (06-11, pair 1) are Heretic 1.2.0's arbitrary-rank
ablation of google/gemma-4-31B-it-qat-q4_0-unquantized at `4f926903`, as their cards say, with different settings:
windows of 15 to 38 and 9 to 35, preservation weights 0.6649 and 0.4826, overcorrection 1.0818 and 1.0491, one
card claiming row-norm preservation and the other not. Each edited a selection of its window and nothing else.
coder3101's changed 21 attention outputs, 17 of them edits (layers 16, 22 and 24 to 38; relative changes 0.0106 to
0.0541; input side on all 17 at weights 1.52 to 3.79 and 0.57 on layer 16; rows 0.0068 to 0.0079, finding 22's
band on every one) and four residues (15, 17, 19, 20 at 0.0011 to 0.0016 with both kept fractions 1.00), three
more layers under the threshold at 0.00083 to 0.00090. llmfan46's changed 16 (layers 16, 18, 21, 22 and 24 to 35;
input side on all 16 at weights 1.58 to 3.64; rows 0.0023 to 0.052 under no claim) and left ten layers of its
window under the threshold at 0.00003 to 0.000195. Nothing moved outside the windows on either, and the two share
their second shard (`fd00e7a5`), the half of a two-shard save that neither window reaches.

On the 14 matrices both edit, the leading left vectors agree at a median cosine of 0.993 (0.906 to 1.000) and the
right at 0.984 (0.682 to 0.999): two makers' solvers, run five days apart with different windows and weights,
found one direction, the closest agreement between independent searches the census has read (the English
searches of the 12B QAT checkpoint stood at 0.92 to 0.97, finding 87). Both stand on the 31B arbitrary-rank family
of the instruct model: coder3101's at 0.956 and 0.943 to the maker's own April edit of google/gemma-4-31B-it (21
shared) and 0.952 and 0.939 to llmfan46's, llmfan46's at 0.925 and 0.956 to the maker's own instruct edit (6
shared, that edit's window being 30 to 47) and 0.938 and 0.957 to coder3101's, both at 0.88 to 0.96 to MoonRide's
April edit and 0.83 to 0.87 on the left to wnfldchen's rank-256 export (0.43 on the right, finding 84). Both stand
at 0.22 or less to every kernel and projection edit. The same round's coder3101/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic
(06-06, pair 3; the attention outputs of layers 12 to 20, the card's window, input side at 1.06 to 1.81, rows
0.0067 to 0.0077 under the claim, exactly 0 outside, no expert touched) stands at 0.991 and 0.900 to llmfan46's
edit of the same checkpoint (round 34), 0.936 and 0.881 to the maker's own instruct 26B-A4B edit and 0.945 and
0.881 to llmfan46's instruct edit.

Why it matters: finding 72's rule, that a maker's QAT edit stands on the maker's instruct edit, now holds on ten
pairs across four sizes, and this round adds the stronger form: on one checkpoint, two makers who share the tool
and its default prompt sets find one direction to 0.99 whatever their windows and weights, so the direction is the
method's and the prompt set's, and a 31B QAT copy that claims this method can be placed by cosine against either
saved vector before its weights are read. The two copies are one edit at two strengths over two selections of
layers, and the preservation claim is the readable difference between them.

Evidence: `results/weights/coder3101-gemma-4-31B-it-qat-q4_0-unquantized-heretic.json`,
`results/weights/llmfan46-gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic.json`,
`results/weights/coder3101-gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic.json`, the three `results/meta/`
reports, the direction files under `nautilus36/measurements/pair-1/`, `pair-2/` and `pair-3/` against
`blueback12/measurements/pair-1/` and `pair-2/` (the makers' instruct 31B edits), `blueback12/measurements/pair-6/`
(coder3101's instruct 26B-A4B edit) and `nautilus34/measurements/pair-1/` (llmfan46's 26B-A4B QAT edit), and the
readings in `docs/cards/`.

## 90. Heretic v2's rank-four transport edit on the 31B and 12B QAT checkpoints: a third and fourth base read rank four on both writers, input side, rows unrestored, and the leading input direction shares two thirds of its cosine with the arbitrary-rank family

OS-Software/gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic (09-08, round 36 pair 4; revision `244246e6`
against google/gemma-4-31B-it-qat-q4_0-unquantized at `1e4d8bee`) and
OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic-v3 (09-07, pair 5; `f637e7d3` against the 12B
checkpoint at `b6ed8627`) print the Heretic v2 record finding 42 read on the maker's E4B and 26B-A4B QAT exports:
`transport` gaussian, `transport_rank` 4, `lora_rank` 128, `row_normalization` none, `target_components`
`attn.o_proj, mlp.down_proj`, `neighbor_count` 1, the preservation and overcorrection weights 1.0, windows of 30 to
41 and 23 to 32, 0 refusals in 100 against 100 and 99, KL divergences 0.0083 and 0.0032. The weights carry the
record on both. The 31B copy changed 22 of 1,188 tensors, the attention outputs and down projections of layers 30
to 40, and the 12B copy 18 of 677, both writers of 23 to 31, the windows with their exclusive ends and exactly 0
outside, 1,166 and 659 tensors equal to the QAT files, which places both on the QAT checkpoints their README
sentences name and not on the instruct models their `base_model` fields name (the pinner paired by the name rule,
finding 48). Each change is rank four exactly: fourth cumulative shares 0.993 to 0.998 on the 31B and 0.989 to
0.999 on the 12B where the first share alone is 0.549 to 0.959 and 0.798 to 0.993. The edit is on the input side on
all 40 matrices, at leading-direction weights of 0.86 to 2.05 on the 31B's down projections (0.86 and 0.89 on
layers 30 and 31, partial removals) and 0.99 to 2.39 on its attention outputs, 0.76 to 1.67 and 0.58 to 2.43 on the
12B's. The two writers of a layer take unrelated directions (within-layer cosines 0.003 to 0.147 and 0.004 to
0.080). The rows moved 0.0012 to 0.037 and 0.0010 to 0.031 under the card's "none". The four exports of this build
now span four bases and read one shape.

What the round adds is a placement. Against twenty-three 31B and thirty-five 12B measurements, the leading left
vectors stand at 0.56 or less to every edit (Bahushruth's 0.56, the arbitrary-rank edits 0.37 to 0.41 on the 31B;
0.50 or less on the 12B), and the leading right vectors stand at 0.65 to 0.77 to the five arbitrary-rank edits of
the 31B and its QAT checkpoint (llmfan46's two, coder3101's two, MoonRide's two) and 0.59 to 0.68 to the 12B
family's (wnfldchen's 0.68, coder3101's QAT 0.66, coder3101's instruct 0.63, llmfan46's two 0.59 and 0.60), with
the kernel and projection edits at 0.23 or less. The transport's first component on the input side is near the
refusal input direction the arbitrary-rank searches find on these checkpoints, and its output component is not:
finding 42 called the directions unrelated per matrix, and they are unrelated between the two writers of a layer,
while the input side of each writer shares two thirds of its cosine with a family found by another method. The
copies' fields name the instruct models (finding 48's case, four of this round's eight), the 5.16.1 saves carry
the `per_layer_config` form (finding 39), and the 12B export shares its first two shards with JJaguar's export of
the same checkpoint (finding 71's layout under one shard size). Evidence:
`results/weights/OS-Software-gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic.json`,
`results/weights/OS-Software-gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic-v3.json`, the two
`results/meta/` reports, the direction files under `nautilus36/measurements/pair-4/` and `pair-5/`, and the
readings in `docs/cards/`.

## 91. A Heretic kernel pass of the 12B QAT checkpoint reads its two kernels' reach to the layer, one direction at 0.90 to five kernel exports of the instruct model and 0.25 to the thinking-on search of the same checkpoint

JJaguar/gemma-4-12B-it-qat-q4_0-unquantized-heretic-nx (08-07, round 36 pair 6; revision `66251327` against
google/gemma-4-12B-it-qat-q4_0-unquantized at `b6ed8627`) prints Heretic v1's kernel card: `direction_index` 29.14,
an attention-output kernel of 1.33 at position 44.28 falling to 1.20 at distance 19.29, a down-projection kernel
of 1.43 at 33.36 falling to 1.35 at distance 13.11, KL divergence 0.1217, 9 refusals in 135 against 112 on a
prompt set of 135. The weights are the kernels' reach: 49 of 677 tensors changed, the down projections of layers
21 to 46 (33.36 less 13.11 is 20.25, plus 13.11 is 46.47) and the attention outputs of 25 to 47 (44.28 less 19.29 is
24.99, up to the last layer), exactly 0 outside, 628 tensors equal to the QAT file. One direction throughout: first
shares 0.992 to 0.997 (0.980 on one matrix), group cosines 0.96 to 1.00, the two writers of a layer at 0.90 to
0.998 and the kinds at 0.85, two flags under the single-projection entry. The kept fractions read no kernel (left
-0.24 to 0.89, right -0.05 to 0.86, the left below the right on 18 of 49), finding 46's scatter on the 12B a sixth
time and the first on the QAT checkpoint. The field names google/gemma-4-12B-it while the first sentence names the
QAT checkpoint (finding 48); the card does not say what `nx` means.

Against thirty-five 12B measurements, the leading directions stand at 0.90 to 0.92 on the left and 0.88 to 0.89
on the right to the five Heretic kernel passes of the instruct 12B (BinxNet's on 34 shared matrices, lemuralabs's
on 49, 3MPER0RR's on 42, prithivMLmods's on 45, MoonRide's on 43), the family finding 46 read as one shared
direction, and at 0.25 and 0.26 to igorls's kernel search of the same QAT checkpoint with thinking on (finding 69) and
0.35 to huihui-ai's projection of it. They stand at 0.18 or less to every arbitrary-rank edit. Why it matters: the kernel
method's direction is the prompt mode's and not the checkpoint's, as finding 69 said of the thinking-on search;
measured on the QAT file, a search with the tool's default prompts finds the instruct kernel family's direction at
0.90 and the thinking-on search's direction at 0.25. The census now holds the kernel family on both Google
checkpoints of the 12B and the arbitrary-rank family on both (finding 89), two direction libraries that place a new
12B copy by method before any kernel is read. Evidence:
`results/weights/JJaguar-gemma-4-12B-it-qat-q4_0-unquantized-heretic-nx.json`, the `results/meta/` report, the
direction file under `nautilus36/measurements/pair-6/` against `wheat33/measurements/pair-6/`,
`nautilus16/measurements/pair-3/`, `nautilus18/measurements/pair-2/`, `nautilus19/measurements/pair-6/`,
`nautilus20/measurements/pair-5/` and `wheat33/measurements/pair-8/`, and the reading in `docs/cards/`.

## 92. A kernel searched on the instruct 26B-A4B and transferred to its QAT checkpoint edits the attention outputs and the dense down projections, with all 128 experts of sixteen layers, under a reproduce record that matches the weights, with the rows not restored on the experts and a generation configuration the loader rewrote

Mitchins/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic (08-23, round 36 pair 7; revision `d62fa836`
against google/gemma-4-26B-A4B-it-qat-q4_0-unquantized at `f1e06dc5`, the commit the maker's own record names)
carries a card of the maker's own and a `reproduce/` folder. The card says the kernel was searched on the stock
instruct model over 200 trials and transferred to the QAT checkpoint with the directions recomputed there (a mean
per-layer cosine of 0.973 to the stock directions), and applied to the attention out-projections and the dense down projections of each layer, with all 128 fused expert down projections with a patched tool; the record names Heretic
v2.0.0.dev0 from a local source, trial 140 at seed 140, `row_normalization` full with `full_normalization_lora_rank`
3, `direction_index` 20.7 and three kernels (attention outputs 1.43 at 18.25 falling to 1.37 at distance 15.79,
expert down projections 1.33 at 18.4 falling to 0.5 at 7.86, dense down projections 1.47 at 19.09 falling to 0.87
at 4.86), with a checksum list equal to the hub's eleven shards. The weights are the record to the layer: 52 of
1,013 tensors changed, the attention outputs of layers 3 to 29 (the kernel reaches 2.46 to 34.04) and the packed
expert down projections of 11 to 26 (10.54 to 26.26), with the dense down projections of 15 to 23 (14.23 to 23.95);
exactly 0 outside, 961 tensors equal to the QAT file, no router or gate-up tensor moved. One direction through the
three kinds (first shares 0.992 to 0.998 on the dense writers, the experts of a layer at 0.9999, the kinds at 0.80
or better), eight flags under the per-layer entry (the worst expert of seven packed tensors at 0.976 to 0.989,
finding 13's reading, and one layer at 0.867). The kept fractions read none of the three kernels (0.44 to 0.77, 0.16
to 0.34 and 0.07 to 0.19 by the right side against 1.37 to 1.43, 0.87 to 1.47 and 0.5 to 1.33), finding 46's
scatter on the mixture. The rows moved 0.0074 to 0.016 on the attention outputs, 0.0086 to 0.022 on the dense down
projections and 0.028 to 0.18 on the experts: the "full" normalisation at adapter rank 3 holds within twice finding
22's band on the dense writers and does not hold on the experts, where the restoration was not applied or did not
reach. The direction is the copy's own: 0.57 to sh0ck0r's on the shared names, 0.54 to xdavxd's run of TrevorJS's
method on the same checkpoint (the experts at 0.58 on the left and 0.05 on the right), 0.47 to TrevorJS's and its
four copies (0.68 to 0.72 on the dense down projections), 0.15 or less to the arbitrary-rank edits.

The token side carries the round's one undisclosed change. The copy's `generation_config.json` was written by the
library from the model configuration (`_from_model_config` true, transformers 5.15.0): the checkpoint's sampling
settings (`do_sample` true, `top_k` 64, `top_p` 0.95) are absent, `temperature` 1.0 is absent, and `eos_token_id` reads [1, 106] where
the checkpoint's reads [1, 106, 50], the third id being `<|tool_response>`. Loaded as published, the copy decodes
greedily where the checkpoint samples, and does not stop at a tool response; the card, which is careful about the
weights, says nothing of the file, and the maker's record does not list it. The `config.json` carries the 5.15.0
save's `per_layer_config` form (finding 39). Why it matters: this is the third edit in the census to reach the
experts (finding 13) and the first to do it with a kernel transferred between two Google checkpoints under a
machine-readable record, and the record is what let the three windows be checked to the layer; the generation file
is the kind of change finding 4 reads, made by a library default rather than by hand, and a rule that names a
regenerated generation configuration is owed to the metadata tool. Evidence:
`results/weights/Mitchins-gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic.json`,
`results/meta/Mitchins-gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic.json` (both generation files in
the snapshots), the maker's `reproduce/` folder (`reproduce.json`, `config.toml`, `SHA256SUMS`) at the pinned revision, the
direction file under `nautilus36/measurements/pair-7/`, and the reading in `docs/cards/`.

## 93. One maker's first Japanese-prompt export edits both writers of thirty-seven layers at weights to 3.7 with rows to 0.21, and its output direction stands closer to the English family than the maker's second search

OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-heretic-ja (06-25, round 36 pair 8; revision `b23c6b1c` against
google/gemma-4-12B-it-qat-q4_0-unquantized at `58540658`) is the first of the maker's two Japanese-prompt exports of
this checkpoint, a month before the `-ja-v2` of finding 83. Its card prints `abliteration_method` ARA LoRA, start
10, end 47, preservation 0.5040, overcorrection 0.5472, 14 neighbours, no row-normalisation line, KL divergence
0.0319 and 3 refusals in 100 against 97 on the maker's `harmful_behaviors_ja` and `harmless_alpaca_ja` sets. The
weights are the card's window on both writers: 73 of 677 tensors changed, the down projections of layers 10 to 46
and the attention outputs of 10 and 12 to 46, the attention output of 11 under the threshold at 0.000086 and
nothing else moved. Input side on all 73 at weights of 0.74 to 1.77 on the down projections and 0.79 to 3.73 on the
attention outputs (3.73 at layer 35, 3.08 at 41), a few directions per matrix (first shares 0.657 to 0.999, fourth
cumulative shares 0.949 to 1.000), the two writers of a layer on different directions (0.001 to 0.101). The rows
moved 0.0007 to 0.046 on the down projections and 0.0083 to 0.21 on the attention outputs (0.21 at layer 41), under
no claim; the maker's second search printed row-norm preservation and held its rows at or under finding 22's band
on 54 matrices, so the two exports differ in what the solver was asked to preserve and the rows say so.

Against thirty-five 12B measurements, the leading left vectors stand at 0.64 to RumiaChannel's Refusals2, 0.59 to
the maker's own `-ja-v2`, 0.58 to llmfan46's QAT edit, 0.57 to wnfldchen's, 0.54 to llmfan46's instruct edit, 0.54
to coder3101's QAT edit, 0.52 to coder3101's instruct edit and 0.50 to the maker's rank-four `-v3`, with the kernel
and projection edits at 0.15 or less; the right vectors stand at 0.19 to 0.39 to the same edits. Finding 83 read
the second Japanese search at 0.30 to 0.40 to the English family on both sides and took the gap for the prompt
language's; the first search stands at 0.52 to 0.64 on the output side, half to two thirds of the English cosine,
and the two Japanese searches stand at 0.59 and 0.19 to each other. Why it matters: two searches by one maker on
one checkpoint with one language's prompts found directions that agree with each other no better than with the
English family's, so the spread finding 83 attributed to the prompt language is as much the search's own, and a
direction found on a small prompt set is one draw from a distribution the census can now see on four points. The
field names the instruct model (finding 48); the token side is the checkpoint's files under newer version strings.
Evidence: `results/weights/OS-Software-gemma-4-12B-it-qat-q4_0-unquantized-heretic-ja.json`, the `results/meta/`
report, the direction file under `nautilus36/measurements/pair-8/` against `wheat37/measurements/pair-1/`,
`nautilus38/measurements/pair-3/`, `wheat37/measurements/pair-7/`, `nautilus34/measurements/pair-2/` and
`pair-7/`, `blueback13/measurements/pair-8/` and `nautilus18/measurements/pair-1/`, and the reading in `docs/cards/`. Round 38 adds the fourth point from the English side: RumiaChannel's Refusals2 stands at 0.98 to the maker's Refusals9 and at 0.55 to 0.61 to the other English 12B searches, the distance this finding measured between the Japanese export and the English family, so the gap is the prompt set's and not the language's (finding 99).

## 94. A null-space projection on every linear map of the 12B and its token embedding reads one direction equal to the maker's shipped mean direction, at a Gaussian weight over the layers that reads back from the maker's configuration within 0.047

jwest33/gemma-4-12B-it-null-space-abliterated describes the maker's own toolkit: an orthogonal projection with
null-space constraints, winsorised activations, a Gaussian per-layer weight and Frobenius-norm preservation, and it
ships the run's configuration, its per-layer directions with their mean and its null-space projectors beside the
weights. Measured against google/gemma-4-12B-it at `5926caa4`: 329 of 677 tensors changed, the query, key, value,
attention output, gate, up and down projections of all 48 layers (the value projections of eight layers under the
threshold) and the token embedding, exactly 0 outside; relative changes 0.0017 to 0.0224. One direction: the
leading vectors stand at 0.958 to 1.000 to the shipped `mean_direction` on every layer and kind, the seven kinds of
a layer agree at 0.996 to 1.000 and the layers at a median 0.979, and the embedding's right vector stands at 1.000
to it; the per-layer saved directions stand at 0.07 to 0.60, which is what `use_mean_direction: true` means. The
writers read on the output side and the readers on the input side, each keeping the complement of one weight per
layer: 0.10 on layers 0 to 7, 0.408 at 15, 0.770 at 20, 0.985 at 24, 1.071 at 27, 0.910 at 34, 0.515 at 40 and
0.153 at 47, the kinds of a layer agreeing to the second decimal. The configuration's `adaptive_position_center`
0.6, `adaptive_position_sigma` 0.2 and `direction_multiplier` 1.1 give 1.1 times the larger of 0.1 and a Gaussian
centred on layer 28.8 with a width of 9.6 layers, which fits the 48 read weights within 0.047 (the best free fit,
floor 0.06, height 1.035, centre 28.25, width 9.0, within 0.034). Rows moved 0.0003 to 0.082 under a claim on the
Frobenius norm of each matrix, which the rows do not measure. The direction stands at 0.58 or less to every other
12B edit, nearest the mean-difference exports and furthest from the searched ones. The scorer's 271 flags are the
per-layer entry's: 96 gate and up projections it does not expect and 175 first shares of 0.80 to 0.90 on the
matrices where the weight is 0.1 to 0.5.

Why it matters: this is a second edit whose maker shipped the direction and the schedule beside the weights
(finding 47 read parameters from a configuration, finding 59 from shipped files), and both read back from 329
matrices; a one-direction projection on every linear map and the embedding is a shape the recipe table has no
entry for, and the per-layer entry charges it 271 flags for being what its card says; and a Frobenius-norm claim
leaves the rows at 0.08, so "norm preservation" on a card is two different claims and finding 22's band reads
only one of them. The token side is consistent with no field differing, the one such copy of the round.

Evidence: `results/weights/jwest33-gemma-4-12B-it-null-space-abliterated.json`,
`results/meta/jwest33-gemma-4-12B-it-null-space-abliterated.json`, the maker's `abliteration_config.json` and
`refusal_directions.pt` read from the hub, the direction file under `nautilus38/measurements/pair-4/`, and the
reading in `docs/cards/`.

## 95. A 26B-A4B copy that describes a per-expert method of its own carries TrevorJS's edit: one direction per layer shared by the 128 experts, the saved directions at 1.000 on all 90 matrices, and the tensors within 0.0006 of his by byte range

DuoNeural/gemma-4-26B-A4B-it-abliterated says it was made with "Expert-Granular Abliteration (EGA)", defined on
the card as a per-expert refusal direction computed across all 128 experts independently and removed by
biprojection, 3 refusals in 100 against 29 for a dense-only run; it names no tool, parameter or other maker.
Measured against google/gemma-4-26B-A4B-it at `7d4c97e5`: 90 of 1,013 tensors changed, the attention outputs,
dense down projections and packed expert down projections of all 30 layers, 128 of 128 experts in each, exactly 0
outside. The experts of a layer share one direction (left vectors agreeing at a median of 0.9957 to 0.9991) and
the three kinds of a layer share it too (within-layer cosines 0.949 to 0.9997): one direction per layer applied to
every expert, which is what finding 13 read on TrevorJS/gemma-4-26B-A4B-it-uncensored, not 128 directions found
independently. Output side with the biprojection's second term on all 90 (the attention outputs keeping 0.02 to
0.28, the dense down projections 0.00 to 0.51 and the experts a median 0.009 to 0.519 along the leading direction,
the right side 0.45 to 0.88), rows within 0.0004 on the dense matrices and 0.0012 per expert tensor, finding 24's
fingerprint. Against the saved vectors of TrevorJS's copy the leading directions stand at 1.000 on all 90 names
(left minimum 1.000, right minimum 0.978), where xdavxd's independent run of the same method on the QAT checkpoint
stands at 0.97 (finding 74); the per-tensor measures agree with TrevorJS's second-pass report to four or five
significant digits and are equal on none; and three tensors read from the hub by byte range (the layer 12
attention output and down projection, the layer 29 attention output) stand 0.0184 to 0.0235 from Google's in both
copies and 0.00035 to 0.00063 from each other, not byte-equal, so the shards differ from his. The copy was
uploaded eight days after TrevorJS's.

Why it matters: a card can describe a method in its own words, a flag count and a fingerprint can match that
method's family, and the copy can still be another maker's run with its last bits changed; the direction
comparison against the base's measured family (finding 66's check) is what told the two apart, and a re-run of a
method on the same original gives 0.97, not 1.000. The census now carries TrevorJS's 26B-A4B edit in six
repositories, his own, four re-uploads of his file and this one, which is not his file. The copy joins the copies
of finding 1 that carry a parent their cards do not name.

Evidence: `results/weights/DuoNeural-gemma-4-26B-A4B-it-abliterated.json`,
`results/meta/DuoNeural-gemma-4-26B-A4B-it-abliterated.json`,
`results/weights/TrevorJS-gemma-4-26B-A4B-it-uncensored.pass-2.json`, the direction file under
`nautilus38/measurements/pair-5/` against `nautilus3/measurements/pair-4/`, the byte-range readings in the reading
note, and the reading in `docs/cards/`.

## 96. A single-direction projection of the E2B reads clean with no flags, at a kernel-shaped weight on both writers the card does not print, on a direction 22 degrees from huihui-ai's, with no chat template in the repository

DuoNeural/Gemma-4-E2B-Heretic says a Heretic LoRA Pareto sweep chose trial 89 on `o_proj` and `down_proj`, "42
layers each" (the E2B has 35), KL divergence 0.0571, 85 percent compliance, and prints no kernel. Measured against
google/gemma-4-E2B-it at `6b7e72c6`: 49 of 1,951 tensors changed, the down projections of layers 6 to 34 and the
attention outputs of 15 to 34, exactly 0 outside; the recipe table reads it as a clean match of
`single-projection-selected` with 0 flags. One direction for the model (group cosines 1.0, the two kinds at
0.99998), output side on all 49, and the weight reads: one minus the left kept fraction runs 0.75 at layer 6, 1.43
at 21 and 0.83 at 34 on the down projections and 1.03 at 15 to 1.32 at 34 on the attention outputs, two kernels
readable from the weights where the per-layer Heretic passes of the 12B read none (finding 46); rows 0.006 to
0.040, unrestored. The direction stands at 0.925 on both sides to huihui-ai's E2B edit on all 45 shared names, the
same number on every matrix because both edits carry one direction, and at 0.08 or less to every other E2B edit.
The repository ships no `chat_template.jinja` and the tokenizer configuration carries none, so the copy's files
cannot render a conversation.

Why it matters: the clean reads of the census are few, and this one has a weight schedule the card omits and a
template the repository omits, so "0 flags" is a statement about the matrices and nothing else; and two makers'
mean-difference directions on one base meet at 22 degrees, a number the census can now put beside the 0.97 of a
re-run (finding 74) and the 1.000 of a copy (finding 95).

Evidence: `results/weights/DuoNeural-Gemma-4-E2B-Heretic.json`, `results/meta/DuoNeural-Gemma-4-E2B-Heretic.json`,
the direction file under `nautilus38/measurements/pair-6/` against huihui-ai's measurement of the E2B, and the reading in
`docs/cards/`.

## 97. A hub duplicate of an unmeasured E4B copy reads coder3101's Heretic edit under an Unsloth fine-tune, the parent named in the configuration's `model_name` before the weights named it

Himanshuoo8/gemma-4-E4B-it-Claude-Opus-4.5-HERETIC-UNCENSORED-Thinking is one commit titled "Duplicate from
DavidAU/gemma-4-E4B-it-Claude-Opus-4.5-HERETIC-UNCENSORED-Thinking", its weight file (`3131a32f`) and README
byte-equal to DavidAU's, which is unmeasured; the copy is measured as that edit (finding 38). The card says
"Heretic'ed then fine tuned via Unsloth on Claude Opus 4.5 reasoning dataset" and names no base; the
configuration's `model_name` is a local path ending in `gemma-4-E4B-it-heretic--coder3101`. Measured against
google/gemma-4-E4B-it at `fa62d88d`: 287 of 2,130 tensors changed, every linear map of the 42 layers but seven
under the threshold at 0.000685 to 0.000893, the towers, norms and embeddings untouched. The fine-tune: 267 of the
287 keep both fractions within 0.05 of 1, relative changes 0.0010 to 0.0073. The ablation under it: the attention
outputs of layers 21 to 40 changed 0.021 to 0.061, input side at weights 1.32 to 2.02, rows 0.0071 to 0.0079
(finding 22's band through the training), and their leading directions stand at 1.000 to
coder3101/gemma-4-E4B-it-heretic's on 20 of 21 shared names; on layer 41, the last of coder3101's window, the
training's 0.0049 outweighs the ablation and the cosine is 0.026. The token side is the fine-tune's save:
`unsloth_version` 2026.4.4 where a `transformers_version` would be, `torch_dtype` for `dtype`, a pad token of 0, no
`generation_config.json`, and a template that inserts `<|think|>` after the system turn so the fixed conversation
renders differently.

Why it matters: it is the second fine-tune over a measured ablation in the census (finding 49 read DavidAU's E2B
copy the same way) and the second time a fine-tune's configuration named its parent in a field the card does not
carry; the ablation's weights, band and direction survive 0.1 to 0.7 percent of training on every matrix around
them, which is what makes an edit traceable through a fine-tune; and a model whose template hard-codes thinking
and whose repository has no generation configuration stops where the loader's defaults say, not where the original
does.

Evidence: `results/weights/Himanshuoo8-gemma-4-E4B-it-Claude-Opus-4.5-HERETIC-UNCENSORED-Thinking.json`, the
`results/meta/` report, the hub's commit titles and file checksums for both repositories, the direction file under
`nautilus38/measurements/pair-8/` against `blueback8/measurements/pair-3/`, and the reading in `docs/cards/`.

## 98. One maker's two arbitrary-rank exports stand on the 26B-A4B and E4B families at 0.98: the first under a 208-byte card with Unsloth's end-of-sequence rewrite, the second attention-only with every row in the band

SassyDiffusion/gemma-4-26B-A4B-it-heretic-ara carries a README of 208 bytes of front matter, the tag `heretic-ara`
its one word on method. Measured against google/gemma-4-26B-A4B-it at `47b6801b`: 35 of 1,013 tensors changed, the
attention outputs of layers 6 to 28 (20) and the dense down projections of 6 to 27 (15), no expert, twelve more
under the threshold to 0.000673; a few directions per matrix, input side on all 35 at weights 0.42 to 1.89, rows
0.0007 to 0.027 under no claim; the directions at 0.98 and 0.97 to llmfan46's and 0.98 to coder3101's instruct
edits of the base. Saved through Unsloth (`unsloth_fixed: true`): the tokenizer's end-of-sequence token moved from
`<eos>` (1) to `<turn|>` (106), the configuration's `eos_token_id` from `[1, 106]` to 106, `pad_token_id` from unset
to 0, and the generation configuration still names `[1, 106, 50]`, finding 15's shape on a Gemma 4 copy; the
template is Google's later revision `4c55b528`. SassyDiffusion/gemma-4-E4B-it-heretic, three weeks later, carries
Heretic 1.2.0's full card (start 21, end 42, attention outputs only, row-norm preservation, 2 refusals in 100
against 99). Measured against google/gemma-4-E4B-it at `83df0a88`: 21 of 2,076 tensors changed, the attention
outputs of layers 21 to 41 and no down projection, exactly 0 outside; input side on all 21 at weights 0.84 to 2.72,
rows 0.0068 to 0.0078 on every matrix; the directions at 0.98 and 0.97 to coder3101's E4B edit, 0.99 to alphakek's
and 0.99 and 0.98 to MoonRide's April edit.

Why it matters: the two exports are one tool's search three weeks apart on two bases, and both land on the
families finding 82 drew (the 26B-A4B's at 0.98, the E4B's at 0.98 to 0.99), so the family holds for a maker who
printed nothing; a 208-byte card is the shortest in the census and the weights read the method, the window and the
family without it; and Unsloth's save moved the stop token on a copy whose card says nothing, a loader-made token
change the census has read before (finding 15) and the metadata tool should name.

Evidence: `results/weights/SassyDiffusion-gemma-4-26B-A4B-it-heretic-ara.json`,
`results/weights/SassyDiffusion-gemma-4-E4B-it-heretic.json`, the `results/meta/` reports, the direction files
under `nautilus38/measurements/pair-1/` and `pair-2/`, and the readings in `docs/cards/`.

## 99. Two arbitrary-rank solvers on the 12B and the E2B: one maker's second search agrees with its first at 0.98 and stands apart from the English family at 0.55 to 0.61, and another maker's reparameterised rows hold within 0.0004 on nine of the 35 layers its card names

RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals2 carries Heretic 1.2.0's card (start 23, end 43, row-norm
preservation, 2 refusals in 100 against 91). Measured against google/gemma-4-12B-it at `5926caa4`: 40 of 677
tensors changed, both writers of layers 23 to 42, exactly 0 outside; 37 edits on the input side at weights 0.45 to
1.52 with rows 0.0052 to 0.0079, finding 22's band on every one, and three down projections (layers 25, 27 and 32)
left as residues at 0.0013 to 0.0017 without a direction (finding 58). Against thirty-seven 12B measurements the
leading directions stand at 0.98 and 0.99 to the maker's Refusals9 on 38 shared names, at 0.64 on the left to
OS-Software's first Japanese export, and at 0.55 to 0.61 to the English family (coder3101's and llmfan46's instruct
and QAT edits), where those edits stand at 0.92 to 0.97 to each other. Bahushruth/gemma-4-E2B-it-abliterated
carries the maker's own solver (LBFGS, Optuna, 60 trials, rows "preserved exactly by reparameterization", all 35
layers, both writers). Measured against google/gemma-4-E2B-it at `3e22461f`: 18 of 1,951 tensors changed, both
writers of layers 16 to 24, exactly 0 outside; many directions per matrix (first shares 0.27 to 0.56), input side
over-reflected at weights 1.56 to 2.08 (finding 57's shape on a third base), rows 0.0001 to 0.0004 on all 18, the
third preservation claim in the census that holds to the row; the directions at 0.69 or less to every E2B edit.

Why it matters: finding 93 asked whether the spread between searches on one base was the prompt language's or the
search's, and RumiaChannel's two English searches answer for one maker: they agree with each other (0.98) and stand
to the other English searches (0.55 to 0.61) at the distance the Japanese export stands to them, so the prompt set,
not the language, sets the family a search lands in; and Bahushruth's solver is now read on three bases with one
signature, a window inside the card's layer count, an over-reflected input side, many directions per matrix and
rows that hold.

Evidence: `results/weights/RumiaChannel-gemma-4-12B-it-uncensored-ara-Refusals2.json`,
`results/weights/Bahushruth-gemma-4-E2B-it-abliterated.json`, the `results/meta/` reports, the direction files under
`nautilus38/measurements/pair-3/` and `pair-7/`, and the readings in `docs/cards/`.

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
- Population. One hundred and sixty-eight copies is a sample; the inventory sample of 30 repositories
  (`docs/inventory-sample.md`) shows how mirrors and re-quantizations outnumber sources and how often the stated
  original cannot be resolved (16 of 30).

Weight differences alone cannot certify the absence of hidden behavior.
