# Findings so far

Created by Sean Egan, 2026-10-29.

The results the audit has established so far, strongest first, each with its evidence in this repository. The
population is small: two hundred and thirty-eight measurements of two hundred and thirty-one distinct published copies on thirty-four originals (thirty-five
copies are re-uploads of others, eleven of them the only measurement of their parent and one of them its own parent's files under a second name, and three more name an unmeasured copy as their parent, forty are measured against the community parent their cards name and not against a publisher's original (round 42: six fine-tunes or merges of a Google checkpoint and two unmeasured first edits; round 43: two fine-tunes of a Google checkpoint and six fine-tunes or merges of Mistral Nemo 12B; round 45: three edits of two Gemma 4 12B fine-tunes, a merge over a first edit of Ministral 3 14B, an edit and a re-upload of two Dolphin fine-tunes of Mistral Small 24B, a pass over unsloth's re-upload of Nemo Instruct, whose shards are Mistral's, and an edit of a Gemma 4 31B fine-tune; round 47: an edit of HuggingFaceH4's Zephyr fine-tune of Mistral 7B v0.1, an edit of GraySwanAI's circuit-breaker model of Mistral 7B Instruct v0.2, an edit of a text-only re-save of Mistral Small 3.2 whose tensors are Mistral's, a fine-tune over an unmeasured first edit of Gemma 3 4B, an edit of an expert-pruned Gemma 4 26B-A4B, two edits of Gemma 4 31B merges and a fine-tune over coder3101's measured 31B edit; round 49: edits of TheDrummer's Skyfall and Magidonia fine-tunes of Magistral Small 2509, an edit of a passthrough depth extension of a Mistral Small 3.2 fine-tune, an edit of LatitudeGames's Harbinger fine-tune of Mistral Small 3.1 Instruct, an edit of ConicCat's first Garnet fine-tune of Gemma 4 31B, a fine-tune over coder3101's measured 26B-A4B edit, a fine-tune over coder3101's unmeasured Gemma 3 27B edit and an edit of sam-paech's Gemma 2 9B merge; the parents counted as neither originals nor copies unless measured against their own parents, finding 117), five copies are measured against
two originals each (three of them measured again in round 35 against the parent their cards name, which adds a measurement and no copy), one is measured twice against one original, one could not be paired tensor by tensor, and one could not be read because its original is
published in float8), plus two edits of my own made to calibrate the measurement. Numbers are from the committed reports in `results/weights/` and `results/meta/`.

## 1. One hundred and eighty-seven of the one hundred and ninety-eight published copies measured so far are what their cards say they are

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
26B-A4B, E4B, 12B and E2B bases (round 38, beside a hub duplicate of an unmeasured edit) and seven from five makers on
Gemma 4 26B-A4B, E4B and E2B bases (round 39, beside a hub duplicate of an unmeasured edit) and seven from seven makers on
Gemma 4 31B, 26B-A4B, E4B and E2B bases (round 40, beside a hub duplicate of an unmeasured edit whose parent the hub no
longer serves) and six from six makers on Gemma 4 12B, E4B and E2B bases and the function-calling Gemma 3 270m
checkpoint (round 41, beside a hub duplicate of an unmeasured export that survives only in its parent's history) and eight from seven makers
measured against the community fine-tunes, merges and first edits their cards name on Gemma 4 31B and 26B-A4B and Gemma 3 27B and 4B bases
(round 42, the first second-generation round, beside a hub duplicate of an unmeasured fine-tune) and eight from three makers
measured against the community fine-tunes and merges their cards name on Gemma 4 26B-A4B and 31B and Mistral Nemo 12B bases (round 43, the second second-generation round, six of them one maker's passes on six Nemo fine-tunes) and eight from seven makers
measured against the community fine-tunes, first edits and re-uploads their cards name on Gemma 4 12B and 31B, Ministral 3 14B, Mistral Small 24B and Mistral Nemo 12B bases (round 45, the third second-generation round, read before round 44, beside a hub duplicate of an unmeasured edit and a re-upload of its parent's files) and eight from seven makers
measured against the community fine-tunes, merges, re-saves and edits their cards name on Mistral 7B, Mistral Small 24B, Gemma 3 4B and Gemma 4 21B-A4B and 31B bases (round 47, the fourth second-generation round and the first outside the Gemma and Mistral instruct lines, read before rounds 44 and 46) and eight from six makers
measured against the community fine-tunes, merges and edits their cards name on Mistral Small 24B, Gemma 4 26B-A4B and 31B, Gemma 3 27B and Gemma 2 9B bases (round 49, the fifth second-generation round, read before rounds 44, 46 and 48), have
been compared tensor by tensor with their stated originals or, in rounds 42, 43, 45, 47 and 49, their stated parents. In one hundred and eighty-seven, the changed tensors are exactly the matrices the stated method reaches, and nothing else
moved: the largest relative change outside the changed set is 0 in one hundred and forty-nine copies, 0.00008, 0.000006, 0.00024,
0.00031, 0.000096, 0.000225, 0.000999, 0.00095, 0.00029, 0.000767, 0.00096, 0.000251, 0.00038, 0.00098, 0.00091, 0.000195, 0.000898, 0.000086, 0.000673, 0.000983, 0.000003, 0.000987, 0.000994, 0.000116, 0.000176, 0.000234, 0.000268 and 0.0000034 in twenty-eight others on matrices the method itself weighted near zero or did not name,
0.0000011 in the jokernifty E4B copy and in Ilya626's, whose float16 saves round the smallest values of untouched tensors,
0.00099 in the richardyoung Gemma 4 12B coder copy, whose fine-tune left 61 normalisation vectors just under the
threshold, 0.000998 in the aifeifei798 E2B copy, whose fine-tuning sits at the threshold on 26 tensors, and 0.000998
in the Dingdust E4B copy, whose parent fine-tune sits at the threshold on 189 tensors, and 0.000995 in Justbackup's duplicate of DavidAU's 27B fine-tune over coder3101's edit, whose training sits at the threshold on the normalisation vectors (round 42), and 0.00097 in tpls's 12B coder edit, whose bfloat16 save of a float16 parent puts 263 matrices moved by the recast alone inside the changed set beside the edit's 59 (round 45, finding 127), and 0.00099 and 0.000999 in jwest33's Gemma 3 4B role-play fine-tune and nbeerbower's Gutenberg fine-tune, whose merged adapters leave five and fifty linear maps just under the threshold (round 47, findings 138 and 142), and 0.00000024 in Tetratype's antislop fine-tune, whose float16 save of a bfloat16 parent moves the untouched tensors by the rounding alone, and 0.00085 in DavidAU's second reasoning pass over coder3101's 27B edit, whose training leaves two layer 1 projections just under the threshold (round 49, findings 148 and 149).
One hundred and seventy-eight of the one hundred and eighty-seven are ablations (one, aifeifei798's, with 0.1 to 0.3 percent of training beside it,
and one, DavidAU's E2B copy, with a fine-tune laid over it, as their cards say; one, wangzhang's edit of GraySwanAI's circuit-breaker model, over the parent's adapter stripped back to Mistral's instruct model, as its card says, finding 136; one, sh0ck0r's Artemis copy, is
measured against the grandparent its `base_model` field names and reads its named parent's 4-bit round trip under
the edit, finding 45, and measured again against that parent in round 35 reads the edit alone, finding 77; one, Dingdust's ContextPilot copy, is measured against the grandparent its field names and
reads the fine-tune of the parent its README's second card names under the edit, finding 54; one, Pranavz's Hearthfire
copy, is measured against the grandparent its field names and reads the fine-tune its README's title names under the
kernels, finding 61, and against that parent reads the kernels alone, finding 77; one, AlekseyCalvin's translation copy, is measured against the grandparent its field names and
reads igorls's 12B Heretic edit under the training, the parent placed from the saved direction vectors, finding 66); eight
(ccharnkij/Ministral-3-8B-Reasoning-2512-Uncensored and richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic, and in round 42 Justbackup's duplicate of DavidAU's 27B fine-tune and DavidAU's 4B fine-tune, each measured against the unmeasured Heretic edit its card names, and in round 47 jwest33's fine-tune over the maker's unmeasured Gemma 3 4B null-space edit and nbeerbower's fine-tune over coder3101's measured 31B edit, and in round 49 Tetratype's antislop fine-tune over coder3101's measured 26B-A4B edit and DavidAU's second reasoning pass over coder3101's unmeasured 27B edit)
are training, as their cards say, findings 17, 18, 121, 138, 142, 148 and 149; and one, AskVenice/venice-uncensored, is its parent's files byte for byte, the Dolphin fine-tune its card names (finding 132). The eleven others carry a parent or a change their cards do not name:
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
own (finding 95), and chulcher/gemma-4-e4b-abliterated stands on the pretrained google/gemma-4-E4B under a card, a field and
links that name the instruct model, its saved directions at 1.000 to the census's measurement on that checkpoint on all 347
shared names and nine byte-range reads byte-equal to it (finding 100), and NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals6-attn, made four minutes
before its sibling of finding 87, edits fifteen down projections under a card that says the attention outputs were its one target
(finding 109), and SOMEHOTMEAL/Ministral-3-14B-Janus-Abliterated-V2-Base_And_GGUF is the merge its card prints made over Mistral's float8 codes read as weights, three entries in ten of every language matrix the raw codes, with no scale beside them (finding 129). The measurements beyond one hundred and fifty-two: four hub duplicates measured in round 19, Iambackup's and Justbackup's copies
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
Jiunsong's unmeasured SuperGemma 12B edit in round 35, each measured as that edit (findings 80 and 81); Himanshuoo8's duplicate of DavidAU's unmeasured E4B fine-tune over coder3101's edit in round 38, measured as that edit (finding 97); Paul691's duplicate of OpenYourMind's unmeasured 12B projection over yuxinlu1's coder fine-tune in round 39, measured as that copy, whose card names Google as its one parent (finding 101); germlag's duplicate of coder3101's unmeasured second 31B export in round 40, whose parent repository the hub no longer serves, measured as that edit (finding 105); jcxu97's duplicate of wangzhang's unmeasured first 31B export in round 41, the export its parent's head replaced and the hub's history still holds, measured as that export (finding 111); Justbackup's duplicate of DavidAU's unmeasured 27B fine-tune over coder3101's unmeasured first edit in round 42, the twelve shards the parent's at three revisions by object id, measured as that fine-tune against the first edit its card names (finding 121); SAIFIINDUSTRIES's duplicate of saukko's unmeasured Dolphin 3.0 R1 edit in round 45, every file saukko's at every revision by object id, measured as that edit against the fine-tune its card names (finding 131); AskVenice's upload of the ten shards of dphn's Venice Edition in round 45, measured against that parent and unchanged on every tensor (finding 132); the huihui-ai E2B edit measured a second time in round 22, equal to its round 13
report to the last digit (finding 50); TimelessSoul/Huihui-gemma-4-12B-it-abliterated is
huihui-ai's 12B file under another name, shard checksum and every field equal (finding 9);
Jiunsong/supergemma4-e4b-abliterated paired no tensor with its original (finding 14);
timfromhcs/Ministral-3-14B-abliterated was compared against an original published in float8 and read nothing but
the quantisation (findings 7 and 37), its source read by byte range in round 45 against Mistral's bfloat16 release, which its first shard matches by object id (finding 130); the richardyoung coder copy is measured twice, against its grandparent and
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
| tvall43/gemma-4-26B-A4B-it-heretic | google/gemma-4-26B-A4B-it | 14 of 1,013 (the attention outputs of layers 16 to 29, the stack's last fourteen, no expert, one direction per layer on the output side at a flat weight of 4.09 to 4.18 the card's kernels do not show, the 26B-A4B kernel exports' directions at 0.98, finding 103) | 0 |
| chulcher/gemma-4-e4b-abliterated | google/gemma-4-E4B-it | 595 of 2,130 (the pretrained google/gemma-4-E4B with a Heretic kernel pass inside it, under a card and field naming the instruct model: every linear map, the embeddings and 209 norms moved as Google's instruction tuning, the directions at 1.000 to the pretrained-base measurement on 347 names, nine byte-range reads byte-equal to the pretrained checkpoint, 39 norms under the threshold, finding 100) | 0.000878 |
| p-e-w/gemma-4-E4B-it-heretic-REPRODUCED-2 | google/gemma-4-E4B-it | 68 of 2,076 (the attention outputs of layers 11 to 41 and the down projections of 5 to 41, the card's windows, the author's own reproduction of his first export at 1.000 on all 68 with the bytes 0.0001 apart, finding 102) | 0 |
| tvall43/gemma-4-E2B-it-heretic-v1 | google/gemma-4-E2B-it | 23 of 1,883 (the attention outputs of layers 21 to 34 and the down projections of 24 to 32, the card's windows to the layer, one direction per layer on the output side at weights 3.33 to 4.53, the E2B one-direction family's directions at 0.98, the vision encoder's 128 range scalars dropped by the save and listed apart, finding 103) | 0 |
| MoonRide/gemma-4-E2B-it-heretic-ara | google/gemma-4-E2B-it | 16 of 2,011 (both writers of layers 15 to 22, the card's window, twelve edits on the input side at weights 0.58 to 1.23 with rows in the band and four residues, finding 104) | 0 |
| Paul691/gemma-4-12B-it-abliterated-uncensored | google/gemma-4-12B-it | 553 of 677 (OpenYourMind's unmeasured 12B copy under the hub's duplicate function: one direction per matrix at a weight of 0.40 on both writers of all 48 layers over yuxinlu1's coder fine-tune, the 228 readers equal to lemuralabs's report to the last digit and the directions at 1.000 on all of them, 67 more under the threshold, finding 101) | 0.000989 |
| MoonRide/gemma-4-E2B-it-heretic-ara-custom | google/gemma-4-E2B-it | 38 of 2,011 (both writers of layers 16 to 34, the card's window, 35 edits on the input side at weights 0.18 to 1.30 with rows in the band and three residues, searched with a custom system prompt, finding 104) | 0 |
| NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8 | google/gemma-4-E4B-it | 28 of 2,130 (both writers of layers 21 to 34, the card's window, every matrix edited on the input side at weights 0.83 to 1.27 with rows at and under the band, the maker's Refusals8-attn direction at 0.99, finding 104) | 0 |
| germlag/gemma-4-31B-it-heretic-v2 | google/gemma-4-31B-it | 65 of 1,188 (coder3101's unmeasured second export under the hub's duplicate function, the parent gone: one direction per layer on the output side of the down projections of layers 26 to 59 and the attention outputs of 29 to 59, the card's kernels to the layer and in height, at 1.000 to three other makers' passes with the bytes apart, finding 105) | 0 |
| cosmicoptima/gemma4-31b-consciousness-abliterated | google/gemma-4-31B-it | 121 of 1,188 (one direction that is not a refusal direction, from layer 58, projected at alpha 1.0 out of the token embedding and both writers of all 60 layers, at 0.034 or less to every measured 31B edit, finding 106) | 0 |
| Rootkit7/Gemma-4-26B-A4B-abliterated | google/gemma-4-26B-A4B-it | 48 of 1,013 (the attention output, dense down projection and all 128 experts of the sixteen layers the card lists, one direction per layer on the output side, rows restored to 0.0012 under the card's norm-preserving biprojection, at 0.93 to TrevorJS's family, finding 107) | 0 |
| Vampelium/gemma-4-31B-it-heretic | google/gemma-4-31B-it | 47 of 1,188 (one direction per layer on the output side of the attention outputs of layers 34 to 59 and the down projections of 39 to 59, two kernels to 1.16 and 1.45 under a card with no table, at 1.000 to three other makers' passes with the bytes apart, finding 105) | 0 |
| Jim-darby/gemma-4-31B-it-heretic-ara-ja80en20 | google/gemma-4-31B-it | 38 of 1,188 (both writers of layers 27 to 46, the card's window, 32 edits on the input side at weights 0.66 to 1.10 with rows in the band under a card that says "Row normalization: none", six residues, the Japanese-weighted direction at 0.41 to 0.64 to the English-prompted 31B searches, finding 108) | 0.000983 |
| DuoNeural/Gemma4-31B-IT-Abliterated | google/gemma-4-31B-it | 120 of 1,188 (one direction per layer on the output side of both writers of all 60 layers at the card's alphas of 0.4 and 0.8 to two decimals, the maker's own at 0.28 to TrevorJS's where the maker's 26B-A4B copy stood at 1.000, finding 107) | 0 |
| NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals6-attn | google/gemma-4-E4B-it | 31 of 2,130 (both writers of layers 21 to 36 under a card naming the attention outputs alone and a window to 41, fifteen down projections edited on the input side at weights 1.00 to 1.60, at 0.995 to the maker's Refusals8-attn of four minutes later, finding 109) | 0.00038 |
| tvall43/gemma-4-E2B-it-heretic-v0 | google/gemma-4-E2B-it | 19 of 1,947 (the attention outputs of layers 12 to 30, the card's kernel position and distance to the layer, one direction on the output side at 1.85 to 4.84 in the kernel's shape, at 0.95 to huihui-ai's E2B family and 0.04 to the maker's v1, 64 range scalars dropped, finding 110) | 0 |
| RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals4 | google/gemma-4-12B-it | 26 of 677 (both writers of layers 24 to 36, the card's window, 21 edits on the input side at weights 0.47 to 1.71 with rows in the band and five residues, the maker's Refusals2 and Refusals9 directions at 0.96 and 0.94, finding 116) | 0 |
| Roman0/functiongemma-270m-it-heretic | google/functiongemma-270m-it | 19 of 236 (the down projections of layers 8 to 17 and the attention outputs of 9 to 17, the card's kernels to the layer and the second decimal, one direction per layer on the output side at 1.40 to 1.45 and 0.85 to 1.29, two token flags changed, finding 113) | 0 |
| NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals3 | google/gemma-4-E4B-it | 26 of 2,130 (both writers of layers 19 to 31, every matrix edited on the input side at weights 0.73 to 1.43 with rows through and over the band, the window six layers short of the card's, the maker's Refusals8 direction at 0.98, finding 116) | 0 |
| ImanolSuarez/gemma-4-E4B-it-heretic-seguridadDeLaInformacion | google/gemma-4-E4B-it | 37 of 2,076 (the down projections of layers 17 to 35 and the attention outputs of 18 to 35, the card's kernels at their lower ends and six layers short at their upper, one direction on the output side under a full row normalisation at rank 3, at 0.75 to p-e-w's on the tool's English prompt sets under a Spanish name, finding 114) | 0 |
| MoonRide/gemma-4-E2B-it-heretic | google/gemma-4-E2B-it | 44 of 2,011 (the down projections of layers 11 to 34 and the attention outputs of 15 to 34, the card's kernels to the layer and the second decimal, one direction on the output side at 1.14 to 1.38, the E2B single direction at 0.96 to 0.98 to three makers, finding 115) | 0 |
| Sabomako/gemma-4-12B-it-heretic | google/gemma-4-12B-it | 31 of 677 (both writers of layers 18 to 23 and 34 to 39 and the down projections of 24 to 30, one direction per layer on the output side at 6.2 to 6.5 on three down projections and under 1.1 elsewhere with every row restored within 0.0003, at 0.986 to TrevorJS's directions with the bytes 0.10 apart, finding 112) | 0 |
| jcxu97/gemma-4-31B-it-abliterated | google/gemma-4-31B-it | 120 of 1,188 (wangzhang's unmeasured first export under the hub's duplicate function: one direction per layer on the attention outputs, down projections, keys, queries and values of layers 27 to 59 at weights to 5.5 with every row restored, at 1.000 to the parent's measured head with other weights and the bytes byte-equal to the parent's history, finding 111) | 0 |
| bgg1996/Melinoe-Gemma4-31B-VL-heretic | bgg1996/Melinoe-Gemma4-31B-VL | 48 of 1,188 (the attention outputs of layers 23 to 59 and the down projections of 38 to 48 over the maker's own 31B fine-tune, the card's 1.4.0 kernels to the layer at both ends, one direction per layer on the output side at 0.31 to 1.41 and 1.03 to 1.21 under a record naming a full row normalisation, at 0.92 to the per-layer 31B passes, finding 122) | 0 |
| llmfan46/G4-MeroMero-31B-uncensored-heretic | zerofata/G4-MeroMero-31B | 19 of 1,188 (the attention outputs of layers 28 to 48 less 42 over zerofata's 31B fine-tune under a card to 49, input-side weights 0.90 to 1.97 with layer 48's component multiplied by 1.34, layer 46 traced, at 0.94 to coder3101's and 0.89 to the maker's own April edit, finding 120) | 0.000003 |
| llmfan46/Gemma-4-Queen-31B-it-uncensored-heretic | aifeifei798/Gemma-4-Queen-31B-it | 30 of 1,188 (the attention outputs of every layer from 26 to 55 over aifeifei798's 31B fine-tune under a card to 56, input-side weights 1.19 to 3.70 with layer 50's component multiplied by 6.71, at 0.993 to the maker's own April edit, finding 120) | 0 |
| Vortex5/G4-Moonlight-Dusk-26B-A4B-heretic | Vortex5/G4-Moonlight-Dusk-26B-A4B | 16 of 1,014 (the attention outputs of layers 9 to 21 over the maker's four-model merge under a card from 3 to 22, input-side weights 1.31 to 2.96 with rows in the band and layers 3 to 5 left as traces, at 0.985 to SassyDiffusion's search, finding 119) | 0.000987 |
| Justbackup/Gemma-3-27b-it-Uncensored-HERETIC-Gemini-Deep-Reasoning | coder3101/gemma-3-27b-it-heretic | 418 of 1,247 (DavidAU's unmeasured 27B fine-tune under the hub's duplicate function, training on every linear map of all 62 layers at 0.1 to 0.8 percent with no direction and the vision tower untouched, over coder3101's unmeasured first edit, finding 121) | 0.000995 |
| SubMaroon/Gemma-4-26B-A4B-StyleTune-QK-Heretic | Gryphe/Gemma-4-26B-A4B-StyleTune-V2 | 79 of 1,014 (the card's three edits one by one: coder3101's body on the attention outputs of layers 10 to 29 at 1.000 to his directions and byte-equal at layer 20, the queries and keys of every layer moved nine tenths of the way to the donor's, the `lm_head` the parent's, finding 118) | 0.000994 |
| DavidAU/gemma-3-4b-it-vl-Heretic-4-Horsemen-Uncensored | DavidAU/gemma-3-4b-it-heretic-uncensored-abliterated-Extreme | 238 of 883 (training on all seven linear maps of all 34 layers at 0.15 to 2.05 percent with no direction and the vision tower exactly 0, over the maker's own unmeasured first edit, finding 121) | 0 |
| Vortex5/Chimera-X-26B-A4B-heretic | Vortex5/Chimera-X-26B-A4B | 17 of 1,014 (the attention outputs of every layer from 6 to 22 over the maker's multi-stage merge under a card to 23, input-side weights 1.10 to 2.03 with rows in the band, at 0.991 to llmfan46's search and 0.957 to the maker's Moonlight-Dusk edit, finding 119) | 0 |
| llmfan46/G4-MeroMero-26B-A4B-it-uncensored-heretic | zerofata/G4-MeroMero-26B-A4B | 11 of 1,013 (the attention outputs of layers 15 to 25 over zerofata's 26B-A4B fine-tune under a card to 26, input-side weights 0.99 to 1.55 with rows under the band, at 0.98 to Vortex5's Chimera-X edit and 0.94 to the maker's own April edit, finding 125) | 0 |
| densenet/Gemma-4-31B-StyleTune-heretic-ara | Gryphe/Gemma-4-31B-StyleTune | 36 of 1,189 (both writers of layers 30 to 47 over Gryphe's 31B fine-tune under a card to 48, input-side weights 0.84 to 4.36 with rows 0.019 to 0.777 under a card claiming row-norm preservation, the parent's `lm_head` untouched, at 0.95 on the left to wnfldchen's merged search, finding 124) | 0 |
| Sorihon/MN-GRAND-Gutenberg-Lyra4-Lyra-12B-DARKNESS-heretic | DavidAU/MN-GRAND-Gutenberg-Lyra4-Lyra-12B-DARKNESS | 73 of 363 (the attention outputs of layers 3 to 39 and the down projections of 4 to 39 over DavidAU's Nemo merge, one shared direction on the output side, the down kernel 0.43 to 0.82 and the attention weights scattered 0.07 to 1.20, at 0.90 to the maker's NemoMix edit, finding 123) | 0 |
| Sorihon/Magnum-v4-12B-Heretic | anthracite-org/magnum-v4-12b | 63 of 363 (the down projections of layers 7 to 39 and the attention outputs of 10 to 39 over anthracite-org's Nemo fine-tune, one shared direction on the output side, the down kernel rising from 0.19 to 1.03 at layer 29 and the attention weights scattered 0.33 to 1.28, at 0.71 to the maker's Celeste edit, finding 123) | 0 |
| Sorihon/Dans-PersonalityEngine-V1.3.0-12B-Heretic | PocketDoc/Dans-PersonalityEngine-V1.3.0-12b | 47 of 363 (the attention outputs of layers 11 to 39 and the down projections of 21 to 38 over PocketDoc's fine-tune of Nemo Base, one direction per layer on the output side, the attention component removed whole at 0.98 to 1.16 and the down kernel 0.39 to 1.08, at 0.73 to the maker's Celeste edit, finding 123) | 0 |
| Sorihon/NemoMix-Unleashed-12B-Heretic | MarinaraSpaghetti/NemoMix-Unleashed-12B | 67 of 363 (the down projections of layers 6 to 39 and the attention outputs of 7 to 39 over MarinaraSpaghetti's five-source Nemo merge, one shared direction on the output side, the down kernel 0.35 to 0.83 and the attention weights scattered 0.09 to 1.03, at 0.90 to the maker's DARKNESS edit, finding 123) | 0 |
| Sorihon/MN-12B-Celeste-V1.9-Heretic | nothingiisreal/MN-12B-Celeste-V1.9 | 35 of 363 (the attention outputs of layers 18 to 39 and the down projections of 22 to 34 over nothingiisreal's Nemo fine-tune, one direction per layer on the output side at 0.59 to 1.31 and a down kernel peaking at 1.15 at layer 28, at 0.73 to the maker's Dans edit, finding 123) | 0 |
| Sorihon/EtherealAurora-12B-v2-Heretic | yamatazen/EtherealAurora-12B-v2 | 68 of 363 (the attention outputs of layers 4 to 39 and the down projections of 8 to 39 over yamatazen's merge, which already carries natong19's abliteration, one direction per layer on the output side scattered 0.12 to 1.27 on the attention outputs and 0.19 to 0.81 on the down projections, at 0.70 to the maker's Celeste edit and 0.09 to DuoNeural's projection, finding 123) | 0 |
| tpls/gemma-4-12B-coder-fable5-composer2.5-v1-abliterated | yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | 322 of 677 (the down projections of layers 9 to 47 and the attention outputs of 24 to 43, one shared direction with the kept fractions scattered, at 0.957 to richardyoung's Heretic edit of the same parent, beside 263 matrices moved only by the bfloat16 recast of the float16 parent, finding 127) | 0.00097 |
| huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated | yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | 12 of 677 (both writers of layers 23 to 28 at weight 1.00 with the direction of the maker's Google 12B edit, 1.000 on all 12 names, finding 128) | 0 |
| SOMEHOTMEAL/Ministral-3-14B-Janus-Abliterated-V2-Base_And_GGUF | jenerallee78/Ministral-3-14B-abliterated | 280 of 585 (every linear map of all 40 layers at 460 to 4,593 times the parent's norm: the card's DARE merge over Mistral's float8 codes read as weights, finding 129) | 0 |
| SAIFIINDUSTRIES/Abliterated-Dolphin3.0-R1-Mistral-24B | dphn/Dolphin3.0-R1-Mistral-24B | 81 of 363 (saukko's unmeasured edit under the hub's duplicate function: one direction projected out of the token embedding and both writers of all 40 layers at weight 1.00, finding 131) | 0 |
| AskVenice/venice-uncensored | dphn/Dolphin-Mistral-24B-Venice-Edition | 0 of 363 (the parent's ten shards by object id, finding 132) | 0 |
| 0xA50C1A1/Mistral-Nemo-Instruct-2407-Heretic-v2 | unsloth/Mistral-Nemo-Instruct-2407 | 63 of 363 (the attention outputs of layers 12 to 39 and the down projections of 5 to 39, the card's kernel reaches, one shared direction on the output side, at 0.90 to Sorihon's DARKNESS edit, finding 133) | 0 |
| llmfan46/Gemma-4-Garnet-V2-31B-it-ultra-uncensored-heretic | ConicCat/Gemma4-GarnetV2-31B | 20 of 1,188 (the attention outputs of layers 25 to 45 under a card to 46, layer 29 rewritten below the threshold, input-side weights 1.31 to 2.66 with no component amplified, at 0.78 to 0.88 to the maker's other 31B searches, finding 134) | 0.000116 |
| huihui-ai/Huihui-gemma-4-12B-agentic-fable5-abliterated | yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2 | 12 of 677 (both writers of layers 23 to 28 at weight 1.00, the direction found again at 0.978 to the maker's Google edit, finding 128) | 0 |
| richardyoung/zephyr-7b-beta-abliterated | HuggingFaceH4/zephyr-7b-beta | 27 of 291 (the down projections of layers 10 to 27 and the attention outputs of 20 to 28 over HuggingFaceH4's Zephyr fine-tune of Mistral 7B v0.1, one direction per layer on the output side, Heretic 1.1's two published kernels read within 0.0011 and 0.0029, finding 135) | 0 |
| wangzhang/Mistral-7B-Instruct-RR-Abliterated | GraySwanAI/Mistral-7B-Instruct-RR | 200 of 291 (118 matrices where the circuit breaker's rank-16 adapter is stripped and the copy is Mistral 7B Instruct v0.2's bytes, and 82 with one direction on the attention outputs of layers 5 to 31, the down projections of 23 to 31 and the keys and values of 16 to 31 at weights to 5.62, the queries of 18 to 31 on a direction of their own, finding 136) | 0 |
| grayarea/Mistral-Small-3.2-24B-Instruct-2506-Text-Only-Heretic-v1.2 | anthracite-core/Mistral-Small-3.2-24B-Instruct-2506-Text-Only | 61 of 363 (the down projections of layers 8 to 39 and the attention outputs of 11 to 39 over a text-only re-save whose tensors are Mistral's, one shared direction on the output side in a kernel's shape with the rows 0.0023 to 0.0078, at 0.856 to the maker's Magistral pass, finding 137) | 0 |
| jwest33/gemma-3-4b-null-space-abliterated-RP-writer | jwest33/gemma-3-4b-it-null-space-abliterated | 233 of 883 (training on every linear map of all 34 layers at 0.10 to 0.71 percent with no direction over the maker's unmeasured null-space edit, the vision tower exactly 0, finding 138) | 0.00099 |
| coder3101/gemma-4-21b-a4b-it-REAP-heretic | 0xSero/Gemma-4-21B | 19 of 1,013 (the attention outputs of layers 11 to 29 over 0xSero's 20 percent expert pruning of the 26B-A4B, the card's window, input-side weights 0.59 to 1.34 with the rows in the band and every expert untouched, at 0.898 to the maker's 26B-A4B edit, finding 139) | 0 |
| llmfan46/Gemma-4-Gembrain-31B-it-uncensored-heretic | Nimbz/Gemma-4-Gembrain-31B | 31 of 1,188 (the attention outputs of layers 21 to 58 over Nimbz's float32 merge under a card from 5 to 60, thirteen more traced, input-side weights 0.24 to 3.17 with no component amplified, at 0.89 to 0.91 to the maker's other 31B edits, finding 140) | 0.000176 |
| llmfan46/Gemma-4-Harmonia-31B-uncensored-heretic | virtuous7373/Gemma-4-Harmonia-31B | 22 of 1,188 (the attention outputs of layers 26 to 54 over virtuous7373's merge of the maker's own edits under a card from 14 to 55, the window's other nineteen traced, input-side weights 0.22 to 2.20 with no component amplified, at 0.60 to 0.80 to the maker's other 31B edits, findings 140 and 141) | 0.000234 |
| nbeerbower/Gemma4-Gutenberg-31B-Heretic | coder3101/gemma-4-31B-it-heretic | 360 of 1,188 (training on the text decoder at 0.10 to 0.77 percent with no direction over coder3101's measured 31B edit, the maker's standard adapter merged a second time and the edit kept to 0.00002 of itself, finding 142) | 0.000999 |
| coder3101/Skyfall-31B-v4.2-heretic | TheDrummer/Skyfall-31B-v4.2 | 90 of 489 (the down projections of layers 8 to 53 and the attention outputs of 10 to 53 over a 54-layer upscale of Magistral Small 2509, one shared direction on the output side over the printed kernels' reaches, the attention height read only on the fourteen inserted near-zero layers, finding 143) | 0 |
| coder3101/Magidonia-24B-v4.3-heretic | TheDrummer/Magidonia-24B-v4.3 | 32 of 363 (the down projections of layers 12 to 35 and the attention outputs of 27 to 34, one direction per layer, both printed kernels read within 0.0036 and 0.0050, finding 144) | 0 |
| llmfan46/MS3.2-PaintedFantasy-Visage-v3-34B-ultra-uncensored-heretic | zerofata/MS3.2-PaintedFantasy-Visage-v3-34B | 11 of 534 (the attention outputs of layers 10 to 27 inside the card's window from 3 to 28, fifteen more traced, all in the first stack of a passthrough merge, input-side weights 1.28 to 2.39 with no component amplified, finding 145) | 0.000268 |
| vprilepskii/Harbinger-24B-biprojected-norm-preserving-abliterated | LatitudeGames/Harbinger-24B | 58 of 363 (the down projections of layers 4 to 39 and the attention outputs of 15 to 36, one direction on the output side at weights to 1.443, rows 0.0031 to 0.0178 under a norm-preserving name, by byte range a plain projection within 0.0026 to 0.0031, finding 146) | 0 |
| llmfan46/Gemma-4-Garnet-31B-it-uncensored-heretic | ConicCat/Gemma4-Garnet-31B | 16 of 1,188 (the attention outputs of layers 26 to 45, the card's window with four traced, input-side weights 1.64 to 3.44 and rows to 0.3246 with no component amplified, at 0.883 to the maker's Garnet V2 search, finding 147) | 0.0000034 |
| Tetratype/Gemma-4-26B-A4B-it-heretic-antislop | coder3101/gemma-4-26B-A4B-it-heretic | 31 of 1,013 (training on the attention outputs and the dense and expert feed-forward tensors of layers 25 to 29 and the tied embedding, no direction, a float16 save, coder3101's measured edit kept, finding 148) | 0.00000024 |
| DavidAU/Gemma-3-27b-it-Gemini-Heretic-Uncensored-Deeper-Reasoning-Series2 | coder3101/gemma-3-27b-it-heretic | 432 of 1,247 (training on every linear map of all 62 layers with no direction, the maker's first pass contained in it at 0.82 to 0.96, finding 149) | 0.00085 |
| Naphula/Darkest-muse-v1-abliterated | sam-paech/Darkest-muse-v1 | 84 of 465 (the down projections and attention outputs of all 42 layers of a Gemma 2 9B merge, one direction at a flat 1.50, no flag, finding 150) | 0 |

The fair statement of the result is narrow: at the weight level, one hundred and eighty-seven copies contain the edit or the
training they claim and no other, eleven carry a parent or a change their cards do not name, one could not be paired
and one could not be read. Weight differences alone cannot certify the absence of hidden behaviour, and the census is
two hundred and thirty-one distinct copies, one hundred and ninety-eight of them read.

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
The case closes: a text-only extraction is measurable against the multimodal release it came from. The round 39 pin stage adds a case of the other kind: TurkishCodeMan/gemma-4-e2b-it-abliterated names the Gemma 4 E2B and is, by shape and by byte range, Google's first-generation gemma-2b-it with its two writers edited, so the stated original cannot be compared because it is not the original (finding 88). Round 39 measured the copy through Paul691's duplicate against the 07-20 revision, and its context length and template are byte-equal to Google's surviving revisions of 06-03, so the copy pins to the first surviving revision after all (finding 101).

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
dense writers beside them (`results/weights/WWTCyberLab-gemma-4-26B-A4B-it-abliterated.json`). Round 36 reads a third edit through the experts, Mitchins's kernel pass of the QAT checkpoint: all 128 experts of sixteen layers moved along one direction (the experts of a layer at a median cosine of 0.9999, the kinds at 0.80 or better), the worst expert's first share 0.976 to 0.989 on seven tensors, which are the scorer's flags, while the rows moved 0.03 to 0.18 on the experts where the dense writers held within 0.022 (finding 92). Round 38 reads a fourth edit through the experts, DuoNeural's 26B-A4B copy, which is TrevorJS's own edit over again: one direction per layer applied to every expert (left agreement 0.9957 to 0.9991), the worst expert 0.881 in layer 0, and the saved directions at 1.000 to his on all 90 names (finding 95). Round 40 adds Rootkit7's 26B-A4B export: one direction per layer on the attention output, the dense down projection and all 128 experts of sixteen layers, the expert stacks' first shares 0.978 to 0.989 under one direction, the rows restored to 0.0012 (finding 107).

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
the two `results/meta/` reports of the same names and the two readings in `docs/cards/`. Round 45 measures two more edits of the same parent against it: tpls's direction stands at 0.957 to this copy's on all 39 shared names and its kept fractions scatter on both sides as this copy's do, and huihui-ai's projection at weight 1.00 stands at 0.50 to it (findings 127 and 128).

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
(`results/meta/llmfan46-gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic.json`). Round 37 reads the maker's 21,488-byte macro template a second time, in the `tokenizer_config.json` of the 12B QAT export against the checkpoint's `chat_template.jinja` (finding 87). Round 36 reads the 23,077-byte template a second time, byte for byte the 26B-A4B QAT export's text, in llmfan46's 31B QAT export against the checkpoint's 17,333-byte file (`results/meta/llmfan46-gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic.json`, finding 89). Round 38 closes two more templates by the later-revision check, SassyDiffusion's 26B-A4B copy on Google's `4c55b528` and RumiaChannel's Refusals2 on `711c1368`, reads DavidAU's E4B template through Himanshuoo8's duplicate (16,352 bytes that insert `<|think|>` after the system turn, finding 97), and finds DuoNeural's E2B repository shipping no template at all (finding 96). Round 39 closes NullpoLab's Refusals8 template by the later-revision check (Google's `c53e9d33` of 04-28, carried in by the copy's 04-29 upload), reads Paul691's 17,466-byte template as Google's 06-03 template, the earlier-revision case again (finding 101), and reads the instruct model's template over the pretrained checkpoint's token files on chulcher's copy (finding 100).

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
5.63 and two amplified rather than removed (`results/weights/wnfldchen-gemma-4-12B-it-qat-q4_0-unquantized-heretic.json`). Round 35 reads the band a sixth time on coder3101's E4B QAT edit, 0.0065 to 0.0078 on sixteen attention outputs (finding 82). Round 37 reads it on MoonRide's two April edits (0.0059 to 0.0077 on 36 matrices, 0.0051 to 0.0078 on 26, finding 86), at or under it on OS-Software's two LoRA-adapter exports (finding 83), and reads the first claim that holds on no matrix, wnfldchen's 31B export at a preservation weight of 0.1182 with rows 0.014 to 0.75 on all 30 (finding 84). Round 36 reads the band on coder3101's two QAT edits under the claim (0.0068 to 0.0079 on 17 attention outputs of the 31B checkpoint, 0.0067 to 0.0077 on 9 of the 26B-A4B's), 0.0023 to 0.052 on llmfan46's 31B QAT edit under no claim, then the largest row movement the census has read on a 12B under no claim, 0.21 on one attention output of OS-Software's first Japanese export (findings 89 and 93). Round 38 reads the band on SassyDiffusion's E4B edit (0.0068 to 0.0078 on all 21), on RumiaChannel's Refusals2 (0.0052 to 0.0079 on all 37 edits) and through DavidAU's fine-tune on coder3101's attention outputs (0.0071 to 0.0079, finding 97), and reads a reparameterised claim that holds to the row on Bahushruth's E2B copy (0.0001 to 0.0004, finding 99). Round 39 reads the band on MoonRide's two E2B exports (0.0065 to 0.0078 on twelve edits, 0.0060 to 0.0078 on 35) and at and under it on NullpoLab's Refusals8 (0.0011 to 0.0096), none of the three cards naming the preservation (finding 104). Round 40 reads the band on Jim-darby's 31B search (0.0050 to 0.0078 on 32 edits, under a card that says "Row normalization: none") and through and over it on NullpoLab's Refusals6-attn (0.0015 to 0.0131), findings 108 and 109. Round 41 reads the band on RumiaChannel's Refusals4 (0.0049 to 0.0079 on 21 edits, 0.0007 to 0.0008 on five residues) and through and over it on NullpoLab's Refusals3 (0.0011 to 0.0184), the maker's fifth export to read so (finding 116). Round 42 reads the band on four edits over community parents (Vortex5's two merges at 0.0064 to 0.0077 and 0.0058 to 0.0078, coder3101's body under SubMaroon's merge at 0.0061 to 0.0080) and through and over it on llmfan46's two edits of 31B fine-tunes (0.0009 to 0.0245 and 0.0006 to 0.197, the layer 50 row under a component multiplied by 6.71), findings 118, 119 and 120. Round 43 reads the band's opposite on densenet's 31B edit, rows 0.019 to 0.777 on 36 matrices under a card claiming row-norm preservation (finding 124), and reads under it on llmfan46's 26B-A4B edit, 0.0005 to 0.0055 on eleven attention outputs (finding 125). Round 45 reads the band through and over on every edit it measures: 0.0003 to 0.0377 on llmfan46's Garnet search (finding 134), 0.0009 to 0.0165 on tpls's 12B edit, 0.0017 to 0.0151 on saukko's Dolphin projection, 0.0038 to 0.0163 on 0xA50C1A1's Nemo pass and 0.016 to 0.079 on huihui-ai's two 12B projections, every one of their 24 matrices over the band (findings 127, 128, 131 and 133). Round 47 reads the band on coder3101's REAP pass under the claim (0.0061 to 0.0077 on all 19 attention outputs, finding 139), in and under it on grayarea's text-only pass under a card naming full row renormalization (0.0023 to 0.0078, finding 137), and through and over it on four edits under no claim: 0.0072 to 0.0325 on the Zephyr pass, 0.048 to 0.178 on the attention outputs of the abliterix edit of the circuit-breaker model, and 0.0007 to 0.0355 and 0.0008 to 0.0215 on llmfan46's two 31B merge searches (findings 135, 136 and 140). Round 49 reads through and over the band on every edit it measures: 0.0031 to 0.0178 on vprilepskii's projection under a norm-preserving name, the rows moved as a plain projection moves them (finding 146), and under no claim 0.0022 to 0.0168 on coder3101's Skyfall pass, 0.0101 to 0.0705 on the maker's Magidonia pass, 0.0016 to 0.0246 on llmfan46's PaintedFantasy search, 0.0017 to 0.3246 on the maker's Garnet search and 0.0034 to 0.0317 on Naphula's Gemma 2 projection (findings 143 to 145, 147 and 150).

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
and its directions stand at 0.97 to TrevorJS's own (finding 74). Round 38 reads the fingerprint on a copy that is neither a re-upload of TrevorJS's file nor an independent run: DuoNeural's 26B-A4B copy, its directions at 1.000 to his on all 90 names and its tensors within 0.0006 of his by byte range, under a card that names a method of the maker's own (finding 95). Round 40 adds a second independent run on the 26B-A4B, Rootkit7's expert-granular pass, at 0.93 to TrevorJS's family on all 48 shared names and 0.91 to xdavxd's run of the same method on the QAT checkpoint (finding 107). Round 41 adds Sabomako's 12B at 0.986 to TrevorJS's 12B directions on all 31 shared names with the rows restored within 0.0003, the weights the maker's own and the bytes 0.10 apart at layer 21, where the maker's 31B stood at 0.90 to 0.94 to TrevorJS's 31B (finding 112).

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
`docs/cards/lemuralabs--Gemma-4-12B-uncensored-bf16-b09ffb4f.reading.md`. Round 39 reads the same fine-tune under a second maker's projection: OpenYourMind's 12B copy, through Paul691's duplicate, has readers equal to lemuralabs's report to the last digit on all 228, byte-equal on the three read, and directions at 1.000 on every one, with a projection of its own at 0.40 on the writers (finding 101).

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
where both differ from the base by 0.745 (finding 62). Two copies, one maker, the same wrong field on two families. Round 39 reads the reverse on a third maker: chulcher's E4B copy names the instruct model in its field, links and title and stands on the pretrained google/gemma-4-E4B, byte-equal to it on nine tensors read (finding 100).

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
remain. Round 47 reads the maker's second v1.2 pass, on a text-only re-save of Mistral Small 3.2 whose tensors are Mistral's, the same way: one shared direction on both writers, a kernel's shape on the down projections, the rows 0.0023 to 0.0078 under the same words, and the two directions at 0.856 (finding 137).

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
`docs/cards/grimjim--mistralai-Mistral-Nemo-Instruct-2407-extensive-BP-abliteration-12B-0c30f0e3.reading.md`. Round 45 reads the same leftover on a second edit that names the maker's norm-preserving biprojection, jenerallee78's Ministral 3 14B edit, its rows moved by up to 0.0184 on the three writers read against Mistral's bfloat16 release (finding 130).

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
`docs/cards/timfromhcs--Ministral-3-14B-abliterated-c9f55a6b.reading.md`. Round 45 finds the original the pair needs on the hub: jenerallee78's first shard is mistralai/Ministral-3-14B-Instruct-2512-BF16's first shard by object id, its query projections are byte-equal to that release, and its writers read a rank-one projection at weight 1.00 against it (finding 130).

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
parent was never measured and the hub no longer serves it (finding 73). Round 38 adds another case read from the commit title and the checksum before any download: Himanshuoo8's one commit "Duplicate from DavidAU/gemma-4-E4B-it-Claude-Opus-4.5-HERETIC-UNCENSORED-Thinking", the weight file byte-equal to DavidAU's unmeasured fine-tune over coder3101's E4B edit, measured as that edit (finding 97). Round 39 adds Paul691's one commit "Duplicate from OpenYourMind/gemma-4-12B-it-abliterated-uncensored", every file byte-equal to the unmeasured parent, measured as that copy (finding 101). Round 40 adds germlag's one commit "Duplicate from coder3101/gemma-4-31B-it-heretic-v2", the parent gone from the hub and the batch note recording that its files differ from coder3101's first export, measured as the second export (finding 105). Round 41 adds jcxu97's one commit "Duplicate from wangzhang/gemma-4-31B-it-abliterated", the batch note recording that its files differ from the parent's head and the hub's file listings placing them at the parent's revisions of 04-10 and 04-11 by object id, measured as that earlier export (finding 111). Round 42 adds Justbackup's one commit "Duplicate from DavidAU/Gemma-3-27b-it-Uncensored-HERETIC-Gemini-Deep-Reasoning", the batch note recording that its files differ and the hub's object ids placing all twelve shards in the parent at its head and two earlier revisions, measured as that fine-tune against the first edit its card names (finding 121). Round 45 adds SAIFIINDUSTRIES's duplicate of saukko's Dolphin 3.0 R1 edit, every file saukko's at all five revisions by object id under a batch note that again recorded a difference, and AskVenice's upload of the Venice Edition's ten shards under a first commit that is not the duplicate function, which the checksum half of the rule catches and the title half does not (findings 131 and 132).

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
the 5.19 library's name for the same vision rotary scheme, both closed by hand (`docs/census-round-26.md`). Round 36 reads the `per_layer_config` form on three more copies, OS-Software's 31B and 12B QAT exports (5.16.1 saves) and Mitchins's 26B-A4B QAT export (5.15.0), closed by hand each time; the home judgement under 5.22.1 moved no field on the round's eight reports (`docs/census-round-36.md`). Round 38 closes `text_config.moe_intermediate_size` at home on four more E4B and E2B cards and four audio and vision fields the 5.10.2 save leaves out on RumiaChannel's 12B card, all the same values under 5.22.1 (`docs/census-round-38.md`). Round 39 closes the same field at home on six more cards and moved no other configuration field (`docs/census-round-39.md`).

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
in the pull copy (`wheat30/measurements/pair-4/weights.directions.safetensors`). Round 39 reads tvall43's E2B windows to the layer from the card's peaks and minimum distances (finding 103) and places chulcher's two kernels by byte range, the reads inside the card's windows changed and the reads outside byte-equal to the base (finding 100). Round 40 reads coder3101's second 31B export's windows from its kernels to the layer (49.63 less 23.83 and 57.33 less 29.21 give 26 and 28; the edits open at 26 and 29) with the maxima 1.31 and 1.46 at the printed layers, and tvall43's E2B v0 window, 20.70 less and plus 9.37, as layers 12 to 30 (findings 105 and 110). Round 41 reads three more windows from their cards: Roman0's functiongemma kernels (12.22 less 4.97 and 12.65 less 4.36 give 8 and 9; the edits open at 8 and 9, both windows ending at the eighteen-layer stack's last layer), MoonRide's E2B kernels (26.14 less 15.83 and 24.75 less 10.31 give 11 and 15; the edits open at 11 and 15), and ImanolSuarez's E4B kernels, whose lower ends read to the layer (17 and 18) and whose upper ends reach 41 where the edits stop at 35 (findings 113, 114 and 115). Round 42 adds bgg1996's 1.4.0 kernels over a 31B fine-tune (51.65 less 28.98 and 43.01 less 5.21 give 23 and 38, 43.01 plus 5.21 gives 48; the edits run 23 to 59 and 38 to 48, the attention window to the stack's last layer), both to the layer at both ends (finding 122).

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
155 bytes longer than the parent's, so the rule cannot read the drop against a shared file; the decoders themselves would have to be compared (finding 77). Round 43 reads the drop twice on Mistral Nemo: Sorihon's Magnum and Celeste edits, transformers 5.8.0 saves of 4.45 and 4.44 parents, drop the 1,000 declarations and the special-token map with `tokenizer_config.json` at 442 and 338 bytes, where the maker's four 4.57.6 saves keep them (finding 126). Round 49 reads the same drop on llmfan46's PaintedFantasy copy, a transformers 5.3.0 save whose 354-byte tokenizer configuration leaves out the 1,000 declarations the parent's 198,054-byte file carries, with the template's line endings rewritten as well (finding 145).

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
`results/weights/igorls-gemma-4-12B-it-qat-q4_0-unquantized-heretic.json` and the readings in `docs/cards/`. TheUmbraWalker's first E4B pass (round 37) reads the same way, one direction per layer and kept fractions with no kernel shape, under a card that prints two kernels (finding 85). Round 36 reads the scatter twice more: JJaguar's kernel pass of the 12B QAT checkpoint keeps -0.24 to 0.89 on the left and -0.05 to 0.86 on the right under kernels of 1.20 to 1.43 (finding 91), and Mitchins's transferred kernel on the 26B-A4B QAT checkpoint reads no kernel on the attention outputs, the dense down projections or the experts (finding 92). Round 38 reads a weight where the 12B passes read none: DuoNeural's E2B copy, one direction on both writers at one minus the left kept fraction of 0.75 to 1.43 on the down projections and 1.03 to 1.32 on the attention outputs, two kernels the card does not print, under a clean read of the single-projection entry (finding 96). Round 39 reads p-e-w's reproduction's two kernels in shape on the output side (0.47 to 1.34 to 0.86 under a printed 1.47) with the right side scattered 0.03 to 0.85 (finding 102), and tvall43's two passes at the largest weights the census has read on a kernel pass, a flat 4.1 and a climbing 3.3 to 4.5, with none of the kernels' shape (finding 103). Round 40 reads the kernels' shape on three passes: coder3101's second 31B export rising to 1.31 and 1.46 at the card's layers, Vampelium's to 1.16 and 1.45 under a card with no table, and tvall43's E2B v0 from 2.05 to 4.84 and back to 1.85, three times its card's maximum (findings 105 and 110). Round 41 reads the kernel's heights to the second decimal on two passes, Roman0's functiongemma (1.40 to 1.45 and 0.85 to 1.29 under printed maxima of 1.46 and 1.33) and MoonRide's E2B (1.17 to 1.38 and 1.14 to 1.21 under 1.38 and 1.21), and reads no kernel in the kept fractions of ImanolSuarez's pass under a full row normalisation, where the relative change carries the shape instead (findings 113, 114 and 115). Round 42 reads the kernel's shape and peak under that same row normalisation on a 1.4.0 pass, bgg1996's down projections at 1.03 to 1.21 at layer 43 under a printed 1.22 at 43.01 and its attention outputs rising with scatter to 1.41 at layers 51 to 53 under 1.45 at 51.65, the lower end at 0.31 under a printed 0.93 (finding 122). Round 43 reads the scatter on a Mistral base for the first time: four of Sorihon's six Nemo passes keep -0.28 to 0.93 on the attention outputs beside down kernels readable to the layer (finding 123). Round 45 reads it on Nemo Instruct itself: 0xA50C1A1's Heretic 1.2.0 pass keeps 0.09 to 1.06 on the attention outputs under a printed kernel of 1.08 to 1.29, beside a down kernel readable to the layer from 0.83 to 1.39 (finding 133). Round 47 reads the tool's kernels to the third decimal on a third Mistral base, the Zephyr fine-tune of Mistral 7B v0.1, within 0.0011 and 0.0029 of the run's published record on all 27 matrices (finding 135). Round 49 reads the same tool's per-layer kernels to the third decimal on a fourth Mistral base, coder3101's Magidonia pass of a Magistral Small fine-tune (within 0.0036 and 0.0050 on all 32 matrices), and reads the printed attention height on the maker's Skyfall pass only on the fourteen layers its upscaled parent inserted with near-zero writers (findings 143 and 144).

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
`remaining_along_direction` values by layer), and the readings in `docs/cards/`. Round 39 adds tvall43's E2B pass to the family at 0.99 to anlord's and 0.98 to TrevorJS's directions, its windows inside the 24 (finding 103). Round 40 places the maker's first E2B pass of the same evening outside the family, at 0.95 to huihui-ai's single direction and 0.08 to TrevorJS's, where his second pass stood at 0.98 (finding 110). Round 41 adds MoonRide's first E2B export to the single-direction side at 0.98 to tvall43's v0, 0.97 to huihui-ai's and 0.96 to DuoNeural's, and at 0.06 to the maker's own arbitrary-rank searches that followed it by six hours and a day (finding 115).

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
as well as its second card. Round 42 measures eight copies against the community parent their cards name from the start and reads the edit or the training alone on each, so the grandparent's change no longer sits under the reading (finding 117).

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
(layers 16 and 20 of the down projections), and the readings in `docs/cards/`. Round 38 adds RumiaChannel's Refusals2: three down projections of layers 25, 27 and 32 rewritten by 0.0013 to 0.0017 without a direction beside 37 edits in the band (finding 99). Round 39 adds MoonRide's two E2B exports: four down projections (17, 19, 21, 22) on the first and the layer 29 attention output with both writers of 31 on the second, rewritten by 0.0013 to 0.0018 without a direction (finding 104). Round 40 adds Jim-darby's 31B search: the attention outputs of layers 27, 28, 29, 32 and 35 and the down projection of 37, rewritten by 0.0012 to 0.0018 without a direction, with two more down projections under the threshold (finding 108). Round 41 adds RumiaChannel's Refusals4: the down projections of layers 25, 27, 30, 32 and 34 rewritten by 0.0012 to 0.0018 without a direction, both kept fractions at 1.00, inside a window every other matrix of which is an edit (finding 116). Round 42 adds the form at a window's opening: Vortex5's Moonlight-Dusk edit rewrites the attention outputs of layers 3 to 5 by 0.0010 to 0.0018 without a direction and leaves 6 to 8 under the threshold before its first edit at 9, and llmfan46's MeroMero edit rewrites layer 46 by 0.000003 inside its window and leaves 42 untouched (findings 119 and 120).

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
lines with their peaks and slopes (finding 79). Round 39 reads p-e-w's two kernels a second time through his own reproduction, 1.34 under a printed 1.47 on the down projections and 0.73 under 0.81 on the attention outputs (finding 102).

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
the middle twelve layers and both towers equal, a fine-tune without a direction (finding 78). Round 39 uses this measurement the other way: chulcher's E4B copy, paired with the instruct model by its card, stands at 1.000 to this copy's saved directions on 347 names, which named the pretrained base before any byte was read (finding 100).

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
eight changed tensors, `row_norms.max_relative_error`) and the reading in `docs/cards/`. Round 41 measures the maker's 12B export under the same card form: one direction per layer on 31 matrices in three bands, 6.29, 6.52 and 6.16 on the down projections of layers 21 to 23 and 0.06 to 1.08 elsewhere, every row restored within 0.0003, at 0.986 to TrevorJS's 12B directions on all 31 names where this copy stands at 0.90 to 0.94 to his 31B (finding 112).

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
The reading is in `docs/cards/`. Round 38 is the check's strongest result: DuoNeural's 26B-A4B copy stands at 1.000 to TrevorJS's saved vectors on all 90 names where an independent run of the method stands at 0.97, and the comparison, not the card or the recipe table, named the parent (finding 95). Round 39 names two parents from the saved vectors: Google's instruction tuning under chulcher's copy (1.000 to Felldude's pretrained-base measurement on 347 names) and yuxinlu1's fine-tune under OpenYourMind's (1.000 to lemuralabs's on 228 readers), both confirmed byte for byte afterwards (findings 100 and 101). Round 40 placed its eight edits by two hundred and twenty-two comparisons and read the check's limit: four makers' per-layer 31B passes at 1.000 to each other with the bytes 0.0005 to 0.010 apart (finding 105), beside cosmicoptima's direction at 0.034 or less to every 31B edit (finding 106) and DuoNeural's 31B copy at 0.28 to TrevorJS's where the maker's 26B-A4B copy stood at 1.000 (finding 107). Round 41 reads 1.000 between jcxu97's hub duplicate and the census's measurement of its parent's head on all 73 shared names, and the byte-range step placed the duplicate's bytes in the parent's history, an earlier trial of the same search with other weights (finding 111); Sabomako's 12B stands at 0.986 to TrevorJS's with the bytes 0.10 apart, and ImanolSuarez's E4B pass at 0.75 to p-e-w's on the same prompt sets under a later version of the tool (findings 112 and 114). Round 42 places six second-generation edits from the saved vectors with the Google-rooted families standing in for the community parents: SubMaroon's body at 1.000 to coder3101's 26B-A4B edit, Vortex5's two merge edits at 0.95 to 0.99 to the 26B-A4B searches, llmfan46's two fine-tune edits at 0.89 to 0.99 to the 31B searches and the maker's own, and bgg1996's pass at 0.92 to the per-layer 31B passes, while the two fine-tunes over unmeasured first edits carry no direction (findings 117 to 122). Round 43 asks the check a new question, whether the direction is the base's or the fine-tune's: six passes by one maker on six Nemo fine-tunes stand at 0.33 to 0.90 to each other and 0.39 to 0.68 to grimjim's pass on Nemo Instruct (finding 123). Round 45 reads a 1.000 across two parents for the first time: huihui-ai's edit of a 12B fine-tune stands at 1.000 to the maker's edit of Google's 12B on every name, the bytes confirming the base direction carried over unchanged, while the maker's edit of the same fine-tuner's other 12B stands at 0.978, and tpls's edit of the coder fine-tune at 0.957 to richardyoung's of the same parent (findings 127 and 128). Round 47 takes the check outside the instruct lines: the Zephyr pass and the abliterix edit of the circuit-breaker model stand at 0.48 to 0.73 to the Mistral 7B Instruct v0.3 edits on the names their hidden size shares, coder3101's pass over a pruned 21B-A4B at 0.898 to the maker's 26B-A4B edit, and a fine-tune merged onto coder3101's 31B edit at 0.010 to it, the training's directions and none of the edit's (findings 135, 136, 139 and 142). Round 49 places six of its eight edits from the saved vectors and finds the check's limit twice, a Gemma 2 copy with no measurement on its hidden size and two depth-changed Mistral Small parents whose layers the vectors match by number and the bytes map to their sources, and it reads a second training against a sibling training on the same parent, DavidAU's second reasoning pass at 0.491 on the left to the first (findings 143, 145, 149 and 150).

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
card names a different model (finding 75). Round 35's four Heretic exports name their true originals in the field, two of them the E4B QAT checkpoint (finding 82). Round 37's TheUmbraWalker first pass names the pretrained base, as the maker's second copy does, and its six other Heretic exports name their true originals (finding 85). Round 36's eight copies all stand on QAT checkpoints: coder3101's two with llmfan46's and Mitchins's name the QAT checkpoint in the field, and OS-Software's three Heretic v1 and v2 cards and JJaguar's v1 card name the instruct model, the inheritance of finding 48 (finding 90). Round 39's p-e-w reproduction carries the same inherited field and stands on the instruct model, while chulcher's copy carries the maker's own card naming the instruct model and stands on the pretrained checkpoint (findings 100 and 102). Round 41 adds ImanolSuarez's E4B export, Heretic 1.3.0's card with `google/gemma-4-E4B` in the field over instruct-model weights, and the batch note's CyborgPaloma case, a card declaring `google/gemma-4-E4B-base`, a repository that does not exist (finding 114). Round 42 adds a third form of the inherited header: two fine-tune cards that print the parent edit's refusal table as their own (coder3101's 0.07 and 9 of 100 on DavidAU's 27B, the Extreme's 0.38 and 2 of 100 on DavidAU's 4B) over weights the training changed on every layer (finding 121). Round 43's six Nemo edits carry no table at all, three printing a refusal count and a KL line and three an image, with Heretic named in the repository names alone (finding 126). Round 45's batch note left out SOMEHOTMEAL's Gemma 3 12B Janus pass, whose card declares google/gemma-3-12b, a repository the hub does not serve, the CyborgPaloma case a second time; the pinner now keeps such a name in the chain as a leaf marked `missing` with a note at pin time (`docs/weights-method.md`).

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
Jiunsong file it could compare was the measured E4B export; the rule has to read the named source's hub listing (finding 81). Round 37 adds the 12B QAT layout shard `513abfa9`, shared by OS-Software's, wnfldchen's and igorls's exports, and a second shard byte-equal between TheUmbraWalker's two copies because the second pass did not touch it (finding 85). Round 38 reads the E2B layout on DuoNeural's first two shards and the 26B-A4B layout on SassyDiffusion's second shard, equal to WWTCyberLab's for the tensors neither edit touches, and reads DuoNeural's 26B-A4B shards equal to nothing while its tensors stand within 0.0006 of TrevorJS's (finding 95). Round 39 reads the layout on p-e-w's reproduction's first and fourth shards, equal to the first export's, with the second and third differing where the edited tensors stand 0.0001 apart (finding 102). Round 40 reads the layout twice more: Rootkit7's second 26B-A4B shard byte-equal to SassyDiffusion's and WWTCyberLab's, and Vampelium's first seven 31B shards byte-equal to 3MPER0RR's, neither export touching a layer below 34 (findings 105 and 107). Round 41 reads the E4B layout shard a tenth time, ImanolSuarez's fourth shard byte-equal to the nine, and meets the rule's other case: jcxu97's two shards match no measured file and are the parent's earlier revision by the hub's object ids, so the duplicate rule needs the parent's history beside its head (findings 111 and 114). Round 42 reads the layout case against a community parent, bgg1996's first five shards byte-equal to its fine-tune parent's where the kernels do not reach, and meets the history case again, Justbackup's twelve shards the parent's at three revisions by object id after the batch note had recorded a difference (findings 121 and 122). Round 43 adds a first shard byte-equal between Sorihon's Dans edit and its parent, the layers below the window, and a `tokenizer.json` object id shared by the maker's DARKNESS and Magnum edits, two re-saves of one file (finding 126).

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
SuperGemma 12B through enkato64bit's duplicate (findings 80 and 81). Round 40 adds germlag's duplicate of coder3101's second 31B export, the parent repository answering "not found", measured as that export at 1.000 to three other makers' passes (finding 105). Round 41 adds jcxu97's duplicate of wangzhang's first 31B export, the parent repository present and its head replaced by a later trial, measured as the earlier export at 1.000 to the head's directions and byte-equal to the history's bytes (finding 111). Round 42 adds Justbackup's duplicate of DavidAU's 27B fine-tune, the parent repository present and byte-equal at its head and two earlier revisions, measured as that fine-tune against coder3101's unmeasured first edit (finding 121).

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
`docs/cards/`. Round 38 puts the 0.97 beside a 1.000: DuoNeural's 26B-A4B copy, under a card that names the expert-granular method as its own, stands at 1.000 to TrevorJS's directions on all 90 names, so the method's independent re-run and the copy of a run are now both measured (finding 95). Round 40 reads the method's second independent run, Rootkit7's on the 26B-A4B instruct checkpoint, at 0.93 to TrevorJS's family and 0.91 to xdavxd's, the rows within 0.0012 on all 48 matrices (finding 107). Round 41 reads two more restorations: jcxu97's duplicate of wangzhang's Abliterix export within 0.0011 on 120 matrices of five kinds, and Sabomako's 12B within 0.0003 on 31 under a card that names no norm, the second time the maker's custom method restored every row (finding 112).

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
readings in `docs/cards/`. Round 42 is the first round measured against community parents from the start: eight edits against the fine-tune, merge or first edit their cards name, each reading its card's edit or training alone, with the parents' own distances from Google read by byte range beside them (finding 117).

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
`docs/cards/`. Round 37 places MoonRide's April edits as the earliest members of both families, the E4B at 0.99 to Refusals5 and coder3101's and the 31B at 0.97 to llmfan46's, and NullpoLab's Refusals8-attn at 0.99 to coder3101's (findings 86 and 87). Round 38 adds SassyDiffusion's two exports to the families, the 26B-A4B at 0.98 to llmfan46's and coder3101's and the E4B at 0.98 to coder3101's and 0.99 to alphakek's and MoonRide's (finding 98). Round 39 adds NullpoLab's Refusals8 at 0.99 to Refusals8-attn, 0.94 to coder3101's and Refusals5 and 0.82 to 0.93 to the rest, and reads the E2B's arbitrary-rank searches as a looser family, MoonRide's two exports a day apart at 0.51 to each other and 0.80 to 0.87 to llmfan46's and coder3101's (finding 104). Round 40 adds NullpoLab's Refusals6-attn at 0.995 to Refusals8-attn and coder3101's, 0.985 to Refusals5 and Refusals8, and 0.96 to llmfan46's and MoonRide's (finding 109). Round 41 adds NullpoLab's Refusals3, the maker's first export, at 0.98 to Refusals8, 0.95 to Refusals6-attn and Refusals8-attn, 0.93 to Refusals5, 0.87 to coder3101's and 0.86 to llmfan46's (finding 116).

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
reports, the direction files under `wheat37/measurements/pair-1/` and `pair-2/`, and the readings in `docs/cards/`. Round 36 reads the maker's first Japanese export, the `-ja` of 06-25, on both writers of layers 10 to 46 at weights to 3.73 with rows to 0.21, its output direction at 0.52 to 0.64 to the English family and 0.59 to this second search (finding 93). Round 40 adds a third base: Jim-darby's 31B search on 80 percent Japanese prompts stands at 0.41 to 0.64 to the English-prompted 31B searches, which stand at 0.87 to 0.97 to each other (finding 108).

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
in `docs/cards/`. Round 43 reads the claim's second failure: densenet's 31B arbitrary-rank edit, "with row-norm preservation" on its card, moves the rows 0.019 to 0.777 on both writers of layers 30 to 47, and its left directions stand at 0.951 to this copy's (finding 124).

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
`docs/cards/`. Round 39 reads 1.000 a third way: the tool author's own reproduction of his E4B export, every number equal to four digits and the bytes 0.0001 apart (finding 102). Round 40 reads 1.000 a fourth way, the one that limits the signature: four makers' per-layer passes on the 31B at 1.000 to each other on every shared name, with four windows, four weights and the bytes 0.0005 to 0.010 apart (finding 105). Round 41 reads 1.000 a fifth way: a hub duplicate against its parent's measured head, two trials of one search with one direction and two sets of weights, the duplicate's bytes byte-equal to the parent's history and 0.003 to 0.074 from its head (finding 111); and it reads 0.986 between Sabomako's 12B and TrevorJS's with the bytes 0.10 apart and the weights different, an independent run in the one-direction family (finding 112). Round 42 reads 1.000 a sixth way: a merge whose card names a measured edit as its body stands at 1.000 to that edit on all 20 shared names with the bytes byte-equal at layer 20, the copy declared on the card and read component by component (finding 118).

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
twenty measurements of the 31B and thirty-four of the E4B, and the readings in `docs/cards/`. Round 41 adds NullpoLab's Refusals3, every matrix of layers 19 to 31 edited under a card to 37, the fourth of the maker's five exports to end short of its `end_layer_index`, and RumiaChannel's Refusals4, whose window is the card's to the layer with five down projections inside it left as residues (finding 116). Round 42 adds the maker's two 31B edits over other makers' fine-tunes, the Queen edit at 0.993 to this copy's April 31B edit on all 18 shared names and the MeroMero edit at 0.89, each with one layer's component amplified rather than removed (finding 120). Round 43 adds llmfan46's 26B-A4B edit, layers 15 to 25 under a card to 26, and densenet's 31B edit, 30 to 47 under a card to 48, both ending one layer short of the card's `end_layer_index` (findings 124 and 125). Round 45 adds llmfan46's Garnet search, layers 25 to 45 under a card to 46 with layer 29 rewritten below the threshold, and 0xA50C1A1's Nemo pass, whose two windows are its kernels' reaches to the layer (findings 133 and 134). Round 47 adds coder3101's REAP pass, layers 11 to 29 under a card from 11 to 30, the card's window to the layer, and llmfan46's two merge searches, layers 21 to 58 inside a card from 5 to 60 with thirteen layers traced and layers 26 to 54 inside a card from 14 to 55 with the window's other nineteen traced (findings 139 and 140). Round 49 adds llmfan46's PaintedFantasy search, layers 3 to 28 under a card from 3 to 29 with fifteen of them traced, and the maker's Garnet search, layers 26 to 45 under a card from 26 to 46 with four traced, both windows the card's to the layer (findings 145 and 147).

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
and `pair-8/`, and the readings in `docs/cards/`. Round 39 measures the sibling Refusals8, both writers of layers 21 to 34 as its card says, every matrix edited, at 0.99 to this copy on all 20 shared names (finding 104). Round 40 measures the sibling made four minutes before this one, Refusals6-attn: fifteen down projections edited under the same attention-only card, the window to 36 under a card to 41, at 0.995 to this copy (finding 109).

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
direction file under `nautilus36/measurements/pair-7/`, and the reading in `docs/cards/`. Round 42 adds a third `reproduce/` record, bgg1996's for Heretic 1.4.0 with `row_normalization` "full" at a LoRA rank of 3, the rows reading 0.0016 to 0.0077 on all 48 matrices and the kernels to the layer at both ends (finding 122).

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
`pair-7/`, `blueback13/measurements/pair-8/` and `nautilus18/measurements/pair-1/`, and the reading in `docs/cards/`. Round 38 adds the fourth point from the English side: RumiaChannel's Refusals2 stands at 0.98 to the maker's Refusals9 and at 0.55 to 0.61 to the other English 12B searches, the distance this finding measured between the Japanese export and the English family, so the gap is the prompt set's and not the language's (finding 99). Round 39 adds a second base: MoonRide's two E2B searches a day apart, the second with a custom system prompt, agree at 0.51 on the output side, so on the E2B the prompt set moves the direction as far as the maker does (finding 104). Round 40 adds the 31B: Jim-darby's Japanese-weighted search at 0.41 to 0.64 to the English family, which agrees among itself at 0.87 to 0.97 (finding 108).

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
reading in `docs/cards/`. Round 47 reads the maker's Gemma 3 4B projection by byte range under a role-play adapter: one direction on the layer 20 writers and queries at 0.782 to the published mean direction and the token embedding along the mean itself, the adapter's training at the level of chance along it (finding 138).

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
note, and the reading in `docs/cards/`. Round 39 calibrates the number: the tool author's own reproduction of his E4B export stands at 1.000 to it with the bytes 0.0001 apart, so 1.000 is a copy or a reproduction of one run and 0.96 to 0.97 an independent one (finding 102). Round 40 measures the maker's 31B copy and reads the maker's own work: a projection at the card's alphas, at 0.28 to TrevorJS's on all 120 names and by byte range further from his tensors than from Google's (finding 107); and it reads 1.000 between four makers' per-layer 31B passes whose bytes differ, so on that base the number needs the bytes beside it (finding 105). Round 42 reads the opposite case of this finding: SubMaroon's 26B-A4B merge stands at 1.000 to coder3101's directions under a card that names coder3101's edit as its body and says the tensors were compared, the bytes byte-equal at layer 20 (finding 118). Round 47 reads a carried edit inside a merge: Harmonia's difference from Google's 31B leads with the Gembrain edit's direction at 0.876 and 0.930 on two attention outputs, that edit a source of the merge at weight 0.4 (finding 141). Round 49 reads a measured edit carried through a fine-tune on a mixture-of-experts checkpoint: the antislop copy's difference from Google's stands at 1.0000 to coder3101's 26B-A4B edit on the five attention outputs its training reaches (finding 148).

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
`docs/cards/`. Round 40 reads the same direction from another maker: tvall43's E2B v0, one direction across nineteen attention outputs at 0.95 to huihui-ai's and 0.94 to this copy, at a kernel-shaped weight of 1.85 to 4.84 (finding 110). Round 41 reads the same direction from a fourth maker: MoonRide's E2B pass of 04-08, one direction on both writers of layers 11 to 34 at 0.96 to this copy, 0.97 to huihui-ai's and 0.98 to tvall43's v0, at the card's kernel weights to the second decimal (finding 115).

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
`nautilus38/measurements/pair-8/` against `blueback8/measurements/pair-3/`, and the reading in `docs/cards/`. Round 39 adds Paul691's duplicate of OpenYourMind's unmeasured 12B copy, measured as that copy, a projection over a third party's fine-tune the card does not name (finding 101). Round 42 adds Justbackup's duplicate of DavidAU's 27B, the same maker's Unsloth fine-tune over coder3101's 27B edit, measured this time against the edit and reading the training alone, 0.1 to 0.8 percent on every linear map of every layer with the vision tower untouched (finding 121).

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
`nautilus38/measurements/pair-3/` and `pair-7/`, and the readings in `docs/cards/`. Round 40 adds the 31B: Jim-darby's Japanese-weighted search stands at 0.41 to 0.64 to the English-prompted 31B searches, which stand at 0.87 to 0.97 to each other (finding 108). Round 41 adds the maker's third search, Refusals4, at 0.96 and 0.94 to Refusals2 and Refusals9 on all 26 names and at 0.55 and 0.54 to llmfan46's and coder3101's 12B edits (finding 116). Round 42 adds two pairs of searches by one maker over two parents each: llmfan46's two 31B fine-tune edits at 0.887 to each other and at 0.89 to 0.99 to the English-prompted 31B searches, and Vortex5's two merge edits at 0.957 to each other and at 0.95 to 0.99 to the 26B-A4B searches (findings 119 and 120).

## 100. A copy whose card, field and links name the instruct E4B stands on the pretrained checkpoint: the saved directions at 1.000 to the census's one measurement on that checkpoint, nine byte-range reads byte-equal to it, and the token ids its own

chulcher/gemma-4-e4b-abliterated names google/gemma-4-e4b-it in its `base_model` field, in both of its links and in
its title ("Google's Gemma 4 E4B with refusal behavior removed via Heretic directional ablation. No fine-tuning"),
and the pinner paired it with google/gemma-4-E4B-it at `292a7e27`. Against that original 595 of 2,130 tensors
changed: every linear map of the language stack (0.24 to 0.76 of their norm), the token and per-layer embeddings,
the per-layer gates and projections, the audio and vision embedding projections, 39 layer scalars and 209
normalisation vectors, with first shares 0.002 to 0.49 and no shared direction, the audio and vision towers exactly
0. The saved leading directions stand at 1.000 on both sides to Felldude/gemma-4-E4B-uncensored's measurement
against the pretrained google/gemma-4-E4B (finding 62) on all 347 shared names (0.999 or better on every linear
map) and at 0.28 or less to every edit of the instruct model: the change is Google's instruction tuning. By byte
range from the hub against google/gemma-4-E4B at `a24c9379`, the layer 3 query projection, the attention outputs of
layers 5 and 41, the down projections of 20, 30 and 40, the token embedding and two normalisation vectors are
byte-equal to the pretrained checkpoint, and the attention outputs of 20 and 30 (0.0209, 0.0284) and the down
projection of 35 (0.0283) differ from it, inside the card's two kernel windows (24.83 less and plus 8.80 on the
attention outputs, 35.18 less and plus 3.09 on the down projections) and nowhere outside them. The copy's
configuration has no `eos_token_id` and its generation configuration names 1, which are the pretrained
checkpoint's values (the instruct model's are `[1, 106]` and `[1, 106, 50]`), under the instruct model's 11,926-byte
template; the repository's own `refusal_test_results.json` labels the base "Gemma 4 E4B Base" at the path
`./models/gemma-4-e4b`.

Why it matters: findings 26 and 62 read a field naming the pretrained base over weights that stood on the instruct
model, and this is the reverse on a third maker, a field, links and title naming the instruct model over weights
that stand on the pretrained checkpoint; paired by the card, the measurement is the instruction tuning with the
edit lost inside it (0.02 to 0.03 under 0.3 to 0.7), and a re-pin against google/gemma-4-E4B is owed before the
edit can be read; and the census's one measurement on the pretrained E4B named the base at 1.000 on 347 names
before any byte was read, so the direction check against every measured family of a base, the pretrained
checkpoint's included, belongs at the pinner's names step.

Evidence: `results/weights/chulcher-gemma-4-e4b-abliterated.json`, the `results/meta/` report, the direction file
under `wheat39/measurements/pair-2/` against `blueback29/measurements/pair-8/`, the byte-range reads recorded in
the reading, the repository's `refusal_test_results.json` and `abliteration_metadata.json`, google/gemma-4-E4B's
token files at `a24c9379`, and the reading in `docs/cards/`. Round 41's six Gemma 4 pairs carry the instruct checkpoint's ids, and its functiongemma pair carries the original's own (`eos_token_id` `[1, 50]`) with two special flags changed and the ids equal (finding 113). Round 42's six Gemma 4 pairs carry the instruct checkpoint's ids through their community parents, two of them Unsloth saves with `eos_token_id` 106 alone and no generation file, and its two Gemma 3 pairs carry `[1, 106]` on both sides (findings 117 and 119). Round 43's two Gemma 4 pairs carry the instruct ids through their parents (`[1, 106]` on llmfan46's, 106 through densenet's Unsloth parent) and its six Nemo pairs carry Mistral's (`bos_token_id` 1, `eos_token_id` 2) on every side, with a pad token added or changed on four (finding 126). Round 45's eight pairs carry their parents' ids: the instruct checkpoint's on the three 12B pairs and the 31B pair, Mistral's on the Ministral, Nemo and Venice pairs (pad 11 written into the Ministral merge's text configuration from its parent's generation file), and Dolphin R1's `[2, 131072]` on both sides of saukko's edit, with no table resized (findings 127 to 134). Round 47's eight pairs carry their parents' ids: Zephyr's (`bos_token_id` 1, `eos_token_id` 2, `pad_token_id` 2), Mistral's on the circuit-breaker and Mistral Small pairs, the Gemma 3 instruct checkpoint's on the 4B pair and the Gemma 4 instruct checkpoint's on the four Gemma 4 pairs, two of them adding generation files their parents lack, with no table resized (findings 135 to 142). Round 49's eight pairs carry their parents' ids: Mistral's on the two Drummer pairs and the PaintedFantasy pair, Harbinger's `eos_token_id` 999 on vprilepskii's, the Gemma 4 instruct checkpoint's on the Garnet pair and on the antislop pair, where Unsloth's save writes `eos_token_id` 1 and a generation list of `[1, 1, 106, 50]`, the Gemma 3 instruct checkpoint's on DavidAU's and Gemma 2's (`bos_token_id` 2, `eos_token_id` 1, `pad_token_id` 0) on Naphula's, with no table resized (findings 143 to 150).

## 101. A hub duplicate of an unmeasured 12B copy reads a single-direction projection at 0.40 on both writers of all 48 layers over the coder fine-tune of finding 25, its 228 readers equal to lemuralabs's to the last digit, under a card that dropped a healing claim four minutes after upload

Paul691/gemma-4-12B-it-abliterated-uncensored is one commit, "Duplicate from
OpenYourMind/gemma-4-12B-it-abliterated-uncensored", every file byte-equal to the parent's, and is measured as the
parent, which is live, unmeasured and the copy of finding 7 whose original's surviving history begins after it.
Against google/gemma-4-12B-it at `707f0a3b`, 553 of 677 tensors changed. Both writers of all 48 layers carry one
direction each on the output side with a left kept fraction of 0.590 to 0.606 on all 96, a projection at a weight
of 0.40, the two writers of a layer and the layers unrelated to each other (medians 0.25 and 0.35), the rows
unrestored to 0.175. The 228 readers moved 0.0018 to 0.0036 with first shares 0.001 to 0.02, the query and key
norms to 0.0864, 67 more tensors stay under the threshold; and every one of those readers' relative differences
equals lemuralabs/Gemma-4-12B-uncensored-bf16's report to the last digit (the ratio 1.000 on all 228), the layer
13 query norm reads 0.08642 in both, the saved directions stand at 1.000 to lemuralabs's on all 228 readers and
at medians of 0.11 and 0.13 on the two writers, and the layer 20 query and gate projections and the layer 13 query norm are
byte-equal to lemuralabs's by byte range. On the writers the two copies part: the layer 5 attention output, which
lemuralabs's ablation does not reach, stands 0.00303 from Google's in that copy and 0.00723 in this one; the layer
20 attention output 0.0283 and 0.0327 from Google's and 0.0424 from each other. The parent's first card (revision
`a67212c0`, 20:00Z on 06-03) said "abliterix" and "Healing: a short supervised pass"; the next revision four minutes
later removed both ("remove abliterix attribution and healing claim") and the current card names "our own custom
abliteration framework" and google/gemma-4-12B-it as the one parent. The copy's context length (131,072) and its
17,466-byte template are byte-equal to Google's revisions `657684fe` and `66bc78a7` of the same day.

Why it matters: the fine-tune finding 25 named under lemuralabs's copy from its normalisation vectors now sits
under a second maker's projection, placed this time from the saved direction vectors and confirmed byte for byte,
and neither card names yuxinlu1's training; the two projections differ (0.0424 apart on a writer where each stands
0.03 from Google's), so two makers took the same third party's fine-tune as their "google/gemma-4-12B-it"; the
0.18 to 0.36 percent on every reader is that fine-tune and not the "healing" the first card claimed; and the
earlier-revision case of finding 7 resolves: the copy pins to Google's first surviving revision of 06-03, whose
context length and template it carries.

Evidence: `results/weights/Paul691-gemma-4-12B-it-abliterated-uncensored.json` against
`results/weights/lemuralabs-Gemma-4-12B-uncensored-bf16.json`, the `results/meta/` report, the direction file under
`wheat39/measurements/pair-6/` against `nautilus16/measurements/pair-3/`, the byte-range reads recorded in the
reading, the parent's commit history and first card, google/gemma-4-12B-it's templates and configurations at
`657684fe`, `66bc78a7`, `5926caa4`, `711c1368` and `707f0a3b`, and the reading in `docs/cards/`.

## 102. The tool author's own second reproduction of his E4B export stands at 1.000 to the first on all 68 matrices, every number equal to four digits and the bytes 0.0001 apart, where another maker's run of the method stands at 0.96

p-e-w/gemma-4-E4B-it-heretic-REPRODUCED-2 was uploaded at 07:32Z on 2026-06-11, twenty-two minutes after
p-e-w/gemma-4-E4B-it-heretic (07:10Z, with a `reproduce/` folder: base `fee6332c`, Heretic 1.3.0 from a local
directory, trial 88 of 200, seed 2684903619, "full" row normalisation with a rank-3 correction, one RTX PRO 4500)
and ten minutes after REPRODUCED (07:22Z), the three repositories carrying one card. Measured against
google/gemma-4-E4B-it at `fee6332c`: 68 of 2,076 tensors changed, the attention outputs of layers 11 to 41 and the
down projections of 5 to 41, exactly 0 outside; first shares 0.969 to 0.998; output side with the kernels' shape
(the down projections 0.47 at layer 5, 1.34 at 26, 0.86 at 41 under a printed maximum of 1.47 at 27.73; the
attention outputs 0.17, 0.73, 0.41 under 0.81 at 26.47); rows 0.0027 to 0.0086; 37 flags, the first export's count
and causes. Every per-tensor relative difference and first share agrees with the round 33 report of the first export
to four to six digits (largest spread 0.00011) and to the last digit on none; the saved directions stand at 1.000 to
the first export's on all 68 names (minimum 1.000 on both sides), at 0.96 to sh0ck0r's E4B export, 0.94 to
BinxNet's and 0.82 to prithivMLmods's QAT kernel export. By byte range, the three exports stand at one distance
from Google's (0.01551 on the layer 26 attention output, 0.02845 on the layer 26 down projection, 0.00885 on the
layer 11 attention output); the first export and REPRODUCED are byte-equal on all three, and REPRODUCED-2 stands
0.00012, 0.00016 and 0.00009 from them. Its first and fourth shards equal the first export's and the E4B layout;
its second and third, which hold the 68 edited tensors, differ.

Why it matters: the census has read 1.000 between saved directions on re-uploads, on a maker's second pass built
on the first (finding 85) and on a copy of another maker's run under a new card (finding 95), and 0.96 to 0.97
between independent runs of one method (findings 74 and 89); the author's own reproduction with the published
seed and record lands at 1.000 with the bytes 0.0001 apart, so a reproduction of a run and a copy of a run are the
same number and an independent run is not, which is the scale the direction check reads against; and the
reproduce record's own warning ("Reproducibility cannot be guaranteed") is borne out at the fourth decimal and no
further.

Evidence: `results/weights/p-e-w-gemma-4-E4B-it-heretic-REPRODUCED-2.json` against
`results/weights/p-e-w-gemma-4-E4B-it-heretic.json`, the `results/meta/` report, the direction file under
`wheat39/measurements/pair-3/` against `wheat33/measurements/pair-2/`, the byte-range reads recorded in the
reading, the first export's `reproduce/` folder, and the reading in `docs/cards/`. Round 40 revises the scale: four makers' per-layer passes on the 31B stand at 1.000 to each other with the bytes 0.0005 to 0.010 apart, so on the 31B the tool's per-layer direction alone does not separate a copy from an independent pass, and the bytes do (finding 105). Round 41 reads another maker's run of the tool's 1.3.0 on the same English prompt sets at 0.75 to this copy and its reproduction on all 37 shared names, with an orthogonalised direction and a full row normalisation in its record and the bytes as far from p-e-w's as from Google's (finding 114). Round 42 reads the tool's 1.4.0 under the same record form (an orthogonalised direction, a full row normalisation at rank 3, the English prompt sets) on a 31B fine-tune at 0.92 to the per-layer 31B passes of finding 105, with the kernels to the layer and the down kernel's peak to the second decimal (finding 122).

## 103. One maker's two kernel passes on one evening read one direction per layer at output-side weights of 3.3 to 4.5, the windows to the layer and the kernels' shape absent, and the E2B save drops the vision encoder's 128 range scalars

tvall43/gemma-4-E2B-it-heretic-v1 (19:26Z on 2026-04-02; the card's note: "tried again with mlp. no refusals, but
still higher kld than id like. gonna try a bigger model next.") and tvall43/gemma-4-26B-A4B-it-heretic (21:41Z the
same evening; "mpoa+soma, only attn.o. ara seems superior") carry Heretic 1.2.0's tables with four kernels per
target. Against google/gemma-4-E2B-it at `4742fe84`: 23 of 1,883 tensors changed, the attention outputs of layers 21
to 34 and the down projections of 24 to 32, the card's windows to the layer from its peaks and minimum distances
(32.17 less 11.43 is 20.7; 28.03 less and plus 4.34 is 23.7 to 32.4), exactly 0 outside; rank one on every matrix,
the two writers of a layer sharing one direction at 0.999 to 1.0; output side at one minus the left kept fraction
of 3.33 at layer 21 rising to 4.53 at 32 on the attention outputs and 3.67 to 3.88 on the down projections, the
right side reflected past zero on the down projections (minus 2.07 to minus 1.62); rows 0.029 to 0.167 and 1.63 on
one matrix; a clean match with 0 flags; the directions at 0.99 to anlord's, 0.98 to TrevorJS's and 0.94 to
aifeifei798's E2B edits and 0.15 or less to the arbitrary-rank ones. Against google/gemma-4-26B-A4B-it at `47b6801b`:
14 of 1,013 changed, the attention outputs of layers 16 to 29, the stack's last fourteen, no expert, exactly 0
outside; rank one, one direction per layer at 0.43 to 0.87 to their mean; output side at 4.09 to 4.18 on every
layer, within 0.09 across the window where the card's kernels peak at 24.12 and fall 8.63 layers either side; rows
0.05 to 0.41; a clean match with 0 flags; the directions at 0.98 to SevenOfNine's, BinxNet's and sh0ck0r's kernel
exports and 0.97 to TrevorJS's. The E2B save drops the 128 activation-range scalars of the original's vision
encoder (`input_max`, `input_min`, `output_max`, `output_min` on each of 32 blocks), which the report lists under
`dropped_statistics` and leaves out of the structural check, the first case in the census; the copy carries the
other 1,883 names and the vision tower's weights unchanged.

Why it matters: finding 46 read Heretic's kernel on the 12B as one direction with no readable weight and finding 96
read a kernel-shaped weight on the E2B at 0.75 to 1.43; these two passes read the largest output-side weights the
census has measured on a kernel pass, 3.3 to 4.5, flat on one base and climbing on the other, with none of the
printed kernels' shape, so the card's kernel table describes the search and not the edit; the E2B's windows read
back to the layer from the card's numbers as finding 43's did; and a copy can drop the E-series originals'
range scalars without touching a weight, which the comparison now names apart from an omission.

Evidence: `results/weights/tvall43-gemma-4-E2B-it-heretic-v1.json`,
`results/weights/tvall43-gemma-4-26B-A4B-it-heretic.json` (`dropped_statistics` in the first), the `results/meta/`
reports, the direction files under `wheat39/measurements/pair-4/` and `pair-1/`, and the readings in `docs/cards/`. Round 40 measures the maker's first E2B pass of the evening, v0, thirty-four minutes before v1: one direction across the window at 1.85 to 4.84, at 0.04 to v1's directions, dropping 64 of the range scalars v1 drops 128 of (finding 110). Round 41 reads the same sequence from MoonRide on the E2B: a kernel pass at 16:28Z on 04-08 carrying the single direction at 0.98 to tvall43's v0, then the arbitrary-rank search of finding 104 at 22:10Z carrying another at 0.06 to it (finding 115).

## 104. Three arbitrary-rank exports from the branch's pull request read the window exactly with the rows in the band, two by one maker a day apart with a custom system prompt between them agreeing at 0.51 where the E4B family agrees at 0.9

MoonRide/gemma-4-E2B-it-heretic-ara (04-08; `start_layer_index` 15, `end_layer_index` 23, `preserve_good_behavior_weight`
0.5636, `neighbor_count` 1, 7 refusals in 100 against 99), MoonRide/gemma-4-E2B-it-heretic-ara-custom (04-09; 16 to
35, 0.7603, 7, "Created and evaluated using custom system prompt", 4 in 100) and
NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8 (04-04, weights re-uploaded 04-29; 21 to 35, 0.9896, 15, 8 in 100)
carry the arbitrary-rank branch's table from the tool's pull request 211, none naming a norm. Against
google/gemma-4-E2B-it at `4742fe84` and google/gemma-4-E4B-it at `292a7e27`: 16, 38 and 28 tensors changed, both
writers of layers 15 to 22, 16 to 34 and 21 to 34, each card's window exactly, exactly 0 outside on all three; a few
directions per matrix, the two writers of a layer unrelated (0.001 to 0.125); input side at weights 0.58 to 1.23,
0.18 to 1.30 and 0.83 to 1.27; rows 0.0065 to 0.0078 and 0.0060 to 0.0078 on MoonRide's edits, finding 22's band, and
0.0011 to 0.0096 on NullpoLab's, at and under it as the maker's two earlier exports read; MoonRide's first leaves
four down projections (17, 19, 21, 22) and the second three matrices (the layer 29 attention output, both writers of
31) as residues at 0.0013 to 0.0018, NullpoLab's none; 32, 76 and 56 flags, all first shares and within-layer
cosines. NullpoLab's directions stand at 0.99 to the maker's Refusals8-attn on all 20 shared names, 0.94 to
coder3101's and to Refusals5, and 0.82 to 0.93 to the rest of the E4B family. MoonRide's two stand at 0.80 and 0.85
on the left to llmfan46's ultra edit and 0.68 and 0.87 to coder3101's QAT edit, and at 0.51 on the left and 0.89 on
the right to each other.

Why it matters: the E4B's arbitrary-rank family (finding 82) holds a fourth member of one maker at 0.99 to its
sibling, while the E2B's searches agree at 0.5 to 0.87 and one maker's two searches a day apart, the second with a
custom system prompt, agree at 0.51 on the output side, so on this base the prompt set moves the direction as much
as the maker does (finding 93's question on a second base); the branch's row-norm preservation shows in the rows
on every one of the three without a card naming it; and finding 58's residues appear on both of MoonRide's exports
and on none of NullpoLab's, the search's own choice of which matrices to leave.

Evidence: `results/weights/MoonRide-gemma-4-E2B-it-heretic-ara.json`,
`results/weights/MoonRide-gemma-4-E2B-it-heretic-ara-custom.json`,
`results/weights/NullpoLab-gemma-4-E4B-it-Heretic-ARA-Refusals8.json`, the `results/meta/` reports, the direction
files under `wheat39/measurements/pair-5/`, `pair-7/` and `pair-8/`, and the readings in `docs/cards/`. Round 40 adds two more exports of the branch: Jim-darby's 31B search with six residues and the rows in the band, and NullpoLab's Refusals6-attn, both writers under an attention-only card (findings 108 and 109). Round 41 adds two more exports of the branch: RumiaChannel's Refusals4 with five residues and the rows in the band, and NullpoLab's Refusals3 with every matrix edited, the window six layers short of the card and the rows through and over the band (finding 116). Round 42 adds four exports of the branch over community parents: Vortex5's two merge edits with the rows in the band, one opening on three traces, and llmfan46's two fine-tune edits with the rows over the band and one layer's component amplified in each, to 6.71 (findings 119 and 120).

## 105. Four makers' per-layer Heretic passes on the 31B stand at 1.000 to each other on every shared matrix with four windows, four weights and the bytes 0.0005 to 0.010 apart, one of them a hub duplicate whose parent the hub no longer serves

germlag's gemma-4-31B-it-heretic-v2 is one commit, "Duplicate from coder3101/gemma-4-31B-it-heretic-v2", and
coder3101's second export answers "not found" on the hub, so the duplicate is the census's one measurement of it;
the batch note had separated its files from coder3101's first export (round 12) by checksum before the download.
Measured against the 31B's release revision, it is one direction per layer on the output side of the down
projections of layers 26 to 59 and the attention outputs of 29 to 59 (65 of 1,188 tensors, exactly 0 outside), the
card's two kernels read back to the layer (the positions 49.63 and 57.33 less the distances 23.83 and 29.21 give
26 and 28) and in height (the weights rise to 1.31 at layer 49 and 1.46 at 57 under printed maxima of 1.32 and
1.47). Vampelium's gemma-4-31B-it-heretic, made on 08-30 under a card with no table ("after Heretic abliteration",
"produced on 4x A100"), is one direction per layer on the attention outputs of 34 to 59 and the down projections of
39 to 59 (47 of 1,188, exactly 0 outside), two kernels rising to 1.16 at 50 and 1.45 at 56. Against the saved
vectors of the measured 31B edits the two stand at 1.000 on both sides to each other on all 47 shared names (left
minimum 0.983 at Vampelium's layer 34, where its change is 0.0014), at 1.000 to 3MPER0RR's export of 09-01 on all
41 shared (minimum 0.9999), and at 1.000 to callmegrr's heretic-z of 08-07 on all 12 shared (minimum 0.997): four
makers, exports from April to September, four windows and four weights. By byte range the four copies differ
from Google and from each other on every edited tensor read: the layer 41 attention output 0.0094 to 0.0192 from
Google's and 0.0017 to 0.0100 apart, the layer 41 down projection 0.0005 to 0.0035 apart, the layer 50 down
projection 0.0010 to 0.0017 apart with callmegrr's byte-equal to Google's there, outside its window; the layer 10
query projection is byte-equal to Google's on germlag's and Vampelium's. Vampelium's first seven shards are
byte-equal to 3MPER0RR's, the library's layout where neither touched a layer (finding 71). ressl's and TrevorJS's
edits stand at 0.985 and 0.95 to the four, coder3101's first export at 0.14.

Why it matters: findings 85, 95 and 102 read 1.000 between saved directions as a copy or a reproduction of one run
and 0.96 to 0.97 as an independent run of the same method, and rounds 38 and 39 named three parents from that
number before any byte was read. Here four makers' per-layer passes on one base agree at 1.000 with nothing else
in common. The tool's per-layer direction on the 31B is the same for every maker who runs it with the prompt set
it ships, so 1.000 on the directions of a per-layer pass says "the same tool on the same base" and not "a copy";
the copy readings of findings 85, 95 and 102 stand on what they also had, per-tensor numbers equal to the digit
and bytes equal or 0.0001 apart, and the direction check keeps its place as what sends the byte reads. The
duplicate of a vanished parent is finding 73's case a second time.

Evidence: `results/weights/germlag-gemma-4-31B-it-heretic-v2.json`,
`results/weights/Vampelium-gemma-4-31B-it-heretic.json`, the `results/meta/` reports, the direction files under
`nautilus40/measurements/pair-1/` and `pair-4/` against `nautilus19/measurements/pair-2/` (3MPER0RR) and
`wheat33/` (callmegrr), the byte-range reads listed in `docs/census-round-40.md`, the batch note in
`data/batches/round-40-batch-1.json`, and the readings in `docs/cards/`. Round 41 reads 1.000 on the 31B between a hub duplicate and its parent's measured head, two trials of one Abliterix search, where the kept fractions differ on every shared matrix and the bytes place the duplicate in the parent's history (finding 111). Round 42 reads 0.92 between bgg1996's 1.4.0 pass over a 31B fine-tune and the four passes of this finding, with the bytes 0.013 from Vampelium's and germlag's and 0.018 from the copy's own parent at layer 44 (finding 122). Round 45 reads the 1.000 between two parents: huihui-ai's projection of a 12B fine-tune and of Google's 12B stand at 1.000 on all 12 names, and by byte range the copy is its parent projected along the Google edit's direction to within the bfloat16 rounding, the bytes 0.0058 apart because the parents are (finding 128). Round 47 reads coder3101's first 31B export under a fine-tune merged onto it: the copy's difference from Google's stands at 0.998 to the export's on two attention outputs, the training moving the export by 0.00002 of itself (finding 142).

## 106. A 31B projection whose direction is not a refusal direction reads its card exactly and stands at 0.034 or less to every measured 31B edit

cosmicoptima's gemma4-31b-consciousness-abliterated describes "an exploratory weight-level intervention": one
direction "derived from paired refusal and direct-answer prefixes for questions about internal state, emotion,
awareness", taken from decoder layer 58 at alpha 1.0 and "projected from the token embedding and 120
residual-writing output matrices", with canonical refusals on its 48-prompt evaluation falling from 26 to 17 and
all 16 harmful-request controls still refusing. The weights are that sentence: 121 of 1,188 tensors changed, the
token embedding and both writers of all 60 layers, exactly 0 outside; one direction, the 120 writers' directions at
1.000 to each other across kinds and layers; the left kept fraction -0.004 to 0.003 on all 120, a weight of 1.00
on the output side, the embedding projected on its hidden side; rows 0.0017 to 0.040, unrestored. Against the
saved vectors of twenty-six measured 31B edits the direction stands at 0.031 to 0.034 to huihui-ai's two exports
and their re-uploads, 0.013 to TrevorJS's and ressl's on all 120 names, 0.011 to 3MPER0RR's and Jim-darby's and
0.007 to DuoNeural's, where those edits stand to each other at 0.4 to 1.000.

Why it matters: every direction the census had read on the 31B was a refusal direction, and the family check of
finding 66 had only ever placed an edit inside a family or beside one. A direction built for another behaviour
stands outside all of them, which is the check's negative control: it reads a direction's purpose from the
company it keeps, and a card's "not a refusal direction" is testable without a prompt.

Evidence: `results/weights/cosmicoptima-gemma4-31b-consciousness-abliterated.json`, the `results/meta/` report,
the direction file under `nautilus40/measurements/pair-2/` against the twenty-six 31B measurements, and the
reading in `docs/cards/`.

## 107. Two independent runs read their cards exactly and stand apart from the edits they might have carried: DuoNeural's 31B projection at 0.28 to TrevorJS's where the maker's 26B-A4B copy stood at 1.000, and Rootkit7's expert-granular pass at 0.93 to TrevorJS's family with the rows restored to 0.0012

DuoNeural's Gemma4-31B-IT-Abliterated describes per-layer directions from 15 harmful and 15 harmless prompts at
the first generated token, projected from both writers of all 60 layers at alphas of 0.4 on the down projections
and 0.8 on the attention outputs, with a KL divergence of 1.606 the card calls significant. The weights are that:
120 of 1,188 tensors, exactly 0 outside, one direction per layer (the two writers at 0.999 or better), the left
kept fraction 0.5955 to 0.6040 on every down projection and 0.1968 to 0.2027 on every attention output, the
alphas to two decimals on sixty layers, rows to 0.358 unrestored. The directions stand at 0.28 on the left and
0.21 on the right to TrevorJS's 31B edit on all 120 shared names and the same to ressl's, and at 0.52 or less to
every other 31B edit; by byte range the layer 20 attention output is 0.0169 from Google's and 0.0226 from
TrevorJS's and the layer 20 down projection 0.0063 from Google's and 0.0165 from TrevorJS's, further from his
than from the original. The maker's 26B-A4B copy of round 38 stood at 1.000 to TrevorJS's on all 90 names with the
tensors within 0.0006 of his (finding 95). Rootkit7's Gemma-4-26B-A4B-abliterated describes the Solutus toolkit's
expert-granular abliteration, "a per-row, magnitude-restoring biprojection", on the attention output, the dense
down projection and every expert's down projection of "16 of 30 layers, all 128 experts" at scales of 0.721 and
0.790. The weights are that: 48 of 1,013 tensors, the three writers of layers 10 to 15 and 19 to 28, exactly 0
outside, one direction per layer (the three writers at 0.948 to 0.9996), the expert stacks at first shares of
0.978 to 0.989 under one direction, output-side weights of 0.43 to 0.99 varying by layer, and rows moved 0.0001
to 0.0003 on the attention outputs, 0.0003 to 0.0010 on the dense down projections and 0.0006 to 0.0012 on the
experts. The directions stand at 0.93 and 0.92 to TrevorJS's edit and its re-uploads on all 48 names, 0.92 to
SevenOfNine's, tvall43's, sh0ck0r's and BinxNet's kernel exports, 0.91 to xdavxd's run of the same method on the
QAT checkpoint (finding 74) and 0.19 or less to the arbitrary-rank edits; by byte range its layer 20 attention
output is 0.0194 from Google's and 0.0117 from TrevorJS's; its second shard is byte-equal to SassyDiffusion's and
WWTCyberLab's, the layout.

Why it matters: the maker whose 26B-A4B card described a method of its own over TrevorJS's bytes has a 31B card
that describes a method of its own over its own bytes, and the two are told apart by the same measurements (1.000
and 0.0006 against 0.28 and 0.0226), so finding 95 is about one copy and not about the maker. Rootkit7's is the
method of finding 74 run a second time, on the instruct checkpoint, inside the 26B-A4B's one-direction family at
the 0.91 to 0.93 an independent run reads, with the rows held to a thousandth on 128 experts a layer, and it is
the second card in the census to name a norm preservation the rows confirm.

Evidence: `results/weights/DuoNeural-Gemma4-31B-IT-Abliterated.json`,
`results/weights/Rootkit7-Gemma-4-26B-A4B-abliterated.json`, the `results/meta/` reports, the direction files
under `nautilus40/measurements/pair-6/` and `pair-3/` against `blueback12/measurements/` (TrevorJS's 31B) and
`nautilus3/` (TrevorJS's 26B-A4B), the byte-range reads listed in `docs/census-round-40.md`, and the readings in
`docs/cards/`.

## 108. A Japanese-weighted arbitrary-rank search on the 31B stands at 0.41 to 0.64 to the English-prompted searches, which stand at 0.87 to 0.97 to each other, with the rows in the band under a card that says "Row normalization: none" and six residues

Jim-darby's gemma-4-31B-it-heretic-ara-ja80en20 is Heretic 1.2.0's arbitrary-rank branch searched on 400
harmless and 400 harmful prompts at "80 percent Japanese, 20 percent English" (ChiKoi7's Japanese sets beside
mlabonne's English ones), trial 82, `start_layer_index` 27 and `end_layer_index` 47, 0 refusals in 100 against
93, a KL divergence of 0.0781, and a details line that says "Row normalization: none". The weights are the
branch: 38 of 1,188 tensors, both writers of layers 27 to 46, 32 edits on the input side at weights 0.66 to 1.10
with a few directions each, six matrices (the attention outputs of 27, 28, 29, 32 and 35, the down projection of
37) rewritten by 0.0012 to 0.0018 without a direction, finding 58's residues, and two down projections (32 and 38)
under the threshold at 0.00068 and 0.000983, nothing else moved. The rows moved 0.0050 to 0.0078 on every edit,
finding 22's band, and 0.0007 to 0.0008 on the residues. Against the saved vectors the leading directions stand
at 0.64 to llmfan46's QAT edit, 0.62 to coder3101's QAT edit, 0.60 to coder3101's first export, 0.54 to
Bahushruth's, 0.51 to llmfan46's and to MoonRide's custom-prompt search, 0.46 to OS-Software's and 0.41 to
MoonRide's first search, and at 0.23 or less to the per-layer kernel passes; the English-prompted 31B searches
stand to each other at 0.87 to 0.97 (MoonRide's two at 0.869, MoonRide's custom to coder3101's 0.951 and to
llmfan46's 0.971, coder3101's to llmfan46's 0.943). The copy's template is byte-equal to Google's revisions of
04-28 and 05-07, older than the pin of 05-18 by eight days when the copy was made.

Why it matters: findings 83, 93 and 99 read the prompt set moving the direction about half as far as a change of
method on the E4B, the 26B-A4B and the E2B; the 31B is the fourth base and the number is the same, 0.4 to 0.6
against 0.9 within the language. The branch applies its row-norm preservation whatever the card's line says, so a
"none" on a card is not a claim the rows contradict in the way finding 22's unclaimed bands are; the rows carry the
preservation whatever the line says. The earlier-revision template is the fourth such case the home tool cannot
close (rounds 31, 35 and 39), and the first where the copy postdates the pin's revision by a week.

Evidence: `results/weights/Jim-darby-gemma-4-31B-it-heretic-ara-ja80en20.json`, the `results/meta/` report, the
direction file under `nautilus40/measurements/pair-5/` against the twenty-six 31B measurements, the template
checks listed in `docs/census-round-40.md`, and the reading in `docs/cards/`. Round 42 adds two English-prompted searches over other makers' 31B fine-tunes at 0.89 to 0.99 to this family and 0.887 to each other, and at 0.51 and 0.56 to the Japanese-weighted search (finding 120). Round 43 adds a third English-prompted search beside the two, llmfan46's 26B-A4B search at 0.67 and 0.59 to OS-Software's two Japanese-weighted searches and 0.92 to 0.98 to the English-prompted family (finding 125). Round 45 adds llmfan46's Garnet search at 0.78 to 0.88 to the English-prompted family and 0.55 to Jim-darby's Japanese-weighted search (finding 134).

## 109. A second attention-only card from one maker, four minutes before the first, measures on both writers: fifteen down projections edited to layer 36 under a card naming the attention outputs to layer 41, at 0.995 to the sibling with the bytes 0.0097 apart

NullpoLab's gemma-4-E4B-it-Heretic-ARA-Refusals6-attn was created at 12:49Z on 04-05, four minutes before the
Refusals8-attn of finding 87, under the same card form: the arbitrary-rank branch from the tool's pull request
211, `target_components` `attn.o_proj`, `start_layer_index` 21, `end_layer_index` 41, 6 refusals in 100 against
99. The weights are both writers: 31 of 2,130 tensors, the attention outputs of layers 21 to 36 and the down
projections of 22 to 36, with the layer 21 down projection under the threshold at 0.00038 and nothing else moved;
input side at weights 0.91 to 1.90 on the attention outputs and 1.00 to 1.60 on the down projections, a few
directions each, the two writers of a layer unrelated; rows 0.0009 to 0.0131, through and over the band at the
layers of the largest weights. The window ends at 36 under a card to 41, as the sibling's ended at 35 under a
card to 39. The directions stand at 0.995 to Refusals8-attn on all 19 shared names, 0.995 to coder3101's E4B
edit, 0.985 to the maker's Refusals5 and Refusals8, and 0.96 to llmfan46's and MoonRide's; by byte range the
layer 29 attention output is 0.0391 from Google's and 0.0097 from Refusals8-attn's. The template is Google's
04-28 revision carried in by the 04-29 upload, as on the maker's Refusals8.

Why it matters: finding 87 read one card naming one writer over an edit of both and asked whether the branch or
the maker was the cause; a second export from the same morning under the same card and the same branch commit
reads the same way, so it is the branch at that commit applying the ablation to both writers whatever
`target_components` says, and every attention-only card from the pull-request branch of that date should be
measured on the down projections. Two searches four minutes apart agree at 0.995 on direction and differ by 0.01
in the bytes, the within-maker distance the E4B family's 0.99 is made of.

Evidence: `results/weights/NullpoLab-gemma-4-E4B-it-Heretic-ARA-Refusals6-attn.json`, the `results/meta/`
report, the direction file under `nautilus40/measurements/pair-7/` against `wheat37/` (Refusals8-attn) and the
thirty-eight other measured E4B copies, the byte-range read listed in `docs/census-round-40.md`, and the reading in
`docs/cards/`.

## 110. One maker's first E2B pass of the evening reads one direction across nineteen attention outputs at a kernel-shaped weight of 1.85 to 4.84, at 0.95 to huihui-ai's family and 0.04 to the maker's own second pass thirty-four minutes later, and drops 64 range scalars where the second drops 128

tvall43's gemma-4-E2B-it-heretic-v0 was uploaded at 18:52Z on 04-02 with a note ("p-e-w beat me to it with ara,
with a better result. my normal recipie of mpoa+soma, attn.o only") over Heretic 1.2.0's table: a direction index
of 17.07, `attn.o_proj` as the one target, four kernels peaking at position 20.70 with minima 9.37 layers away, 9
refusals in 100 against 98. The weights are a clean match of the single-projection entry with selection, 0 flags:
19 of 1,947 tensors, the attention outputs of layers 12 to 30 (20.70 less and plus 9.37), exactly 0 outside, one
direction on all nineteen (the card's single index), on the output side at 2.05 at layer 12 rising by a third a
layer to 4.84 at 21 and falling to 1.85 at 30, the kernel's shape at three times the card's largest printed
maximum of 1.45, rows 0.018 to 0.422 unrestored. The direction stands at 0.95 to huihui-ai's E2B edit and its
re-uploads on all 19 names and 0.94 to DuoNeural's E2B single direction (finding 96), at 0.08 to TrevorJS's, 0.05
to anlord's and 0.04 to the maker's own v1 of 19:26Z on the 10 names they share; by byte range the layer 21
attention output is 0.1199 from Google's on v0, 0.0839 on v1 and 0.1429 between them. The save drops the vision
encoder's input and output range scalars on the attention outputs of its sixteen layers, 64 names listed apart,
where v1's save dropped 128 (finding 103).

Why it matters: finding 103 read the maker's two passes of the evening as one method at two weights; the first
pass of the evening is a different direction, the single one huihui-ai's exports carry at 0.95 and DuoNeural's at
0.94, and the second is the per-layer one the E2B's one-direction family carries at 0.98, so within an hour one
maker's tool settings moved the copy from one E2B family to the other. The kernel shape reads whole on this pass
(2.05 to 4.84 to 1.85), the clearest the census has read, under a card whose maxima are a third of it. The
dropped-scalars count changing between two saves of the same evening (64, then 128) is the save path and not
the model.

Evidence: `results/weights/tvall43-gemma-4-E2B-it-heretic-v0.json`, the `results/meta/` report, the direction
file under `nautilus40/measurements/pair-8/` against `wheat39/measurements/pair-4/` (v1), `blueback13/` and
`blueback22/` (huihui-ai's) and the other measured E2B copies, the byte-range reads listed in
`docs/census-round-40.md`, and the reading in `docs/cards/`. Round 41 adds MoonRide's E2B pass of six days later at 0.98 to this copy's direction on all 16 shared names, on both writers at the card's kernel weights, the fourth maker carrying the single direction (finding 115).

## 111. A hub duplicate holds the export its parent's head replaced: one direction per layer on five components of the 31B at 1.000 to the parent's measured trial with other weights on every shared matrix, the bytes byte-equal to the parent's history and 0.003 to 0.074 from its head

jcxu97's gemma-4-31B-it-abliterated is one commit of 04-12, "Duplicate from wangzhang/gemma-4-31B-it-abliterated".
The parent is measured (round 2, repeated in round 3) at its head, `d7431183`, which is "Update Gemma 4 31B
abliterated to trial 40" of 04-29 and two card commits of 08-29 over it; the duplicate copied the state of 04-11
(`90a225e3`), the export of 04-10 with Google's template and tokenizer configuration synced the next day, under
the card of 04-10 byte for byte (Abliterix on "attention Q/K/V/O projections and MLP down projections (5
steerable components per layer)", "norm-preserving row magnitude restoration", 18 refusals in 100 after "20/80
(warmup phase only)" trials). The batch note had read "its weight files differ" from the parent's by checksum,
and the hub's file listings give the duplicate's two shards the object ids of the parent's `2a9b26cd` and
`90a225e3`. Measured against the 31B's revision `439edf56`, it is 120 of 1,188 tensors, exactly 0 outside: the
attention outputs of layers 29 to 59, the down projections of 29 to 58, the keys of 27 to 53, the queries of 31
to 47 and the values of 42 to 58, one direction per layer shared by all five kinds (within a layer at 1.000),
rank one on every matrix, the writers on the output side at 1.38 to 1.95 and 1.86 to 5.33 and the readers on the
input side at 3.6 to 4.3, 3.9 to 5.54 and 1.41 to 1.72, every row restored within 0.0011. Against the saved
vectors the directions stand at 1.000 on both sides to the parent's measured head on all 73 shared names (29
attention outputs, 13 keys, 17 queries, 14 values), and the kept fractions differ on every one of them (the
layer 29 attention output at a weight of 1.38 here and 3.48 there; the layer 30 key at 3.77 and 1.11), the head
touching no down projection where the duplicate edits thirty. By byte range the duplicate is byte-equal to the
parent's `90a225e3` on the layer 41 attention output, query projection and down projection and the layer 10
query projection, and 0.0295, 0.0032 and 0.0740 from the head's trial 40 on the three edited tensors, the head's
layer 41 down projection byte-equal to Google's. To the other 31B edits it stands at 0.84 to 0.89 (the
per-layer passes of finding 105, Sabomako's 31B, ressl's and TrevorJS's) and at 0.52 or less to the rest.

Why it matters: finding 105 read 1.000 between per-layer Heretic passes on the 31B as one tool on one base and
one prompt set, and asked for the bytes before any copy reading; here the bytes were read and found the copy
in a place the direction check could not name, the parent's own history. Two trials of one Abliterix search
share their direction and differ in every weight and in which components they touch, so 1.000 to a measured
repository means the repository's search and not its measured file. The hub's duplicate function preserves a
revision its parent later replaced, which the census had not seen in eight earlier duplicates (findings 38 and
73): the batch note's checksum step saw the difference, and the pinner's duplicate rule should read the
parent's commit history and name the revision the duplicate holds. The export itself reads its card exactly,
and the population counts it as the ninth hub duplicate and the one measurement of that export.

Evidence: `results/weights/jcxu97-gemma-4-31B-it-abliterated.json`, the `results/meta/` report, the direction
file under `wheat41/measurements/pair-7/` against `nautilus3/measurements/pair-1/` (wangzhang's head) and the
twenty-three other 31B measurements, the byte-range reads and the hub listings described in
`docs/census-round-41.md`, the batch note in `data/batches/round-41-batch-1.json`, and the reading in
`docs/cards/`.

## 112. One maker's second custom projection reads its 31B signature on the 12B: three down projections at 6.2 to 6.5 among 31 matrices under 1.1, every row restored within 0.0003, at 0.986 to TrevorJS's directions on all 31 names with the bytes 0.10 apart

Sabomako's gemma-4-12B-it-heretic was created on 06-18 under a 674-byte card ("Heretic v1.3.0 with custom ORBA
abliteration method", an LLM judge, a KL divergence of 0.0545, 0 refusals in 100 against 98), the same form as
the maker's 31B of finding 65. The weights are the same signature on a wider window: 31 of 677 tensors, both
writers of layers 18 to 23 and 34 to 39 and the down projections alone of 24 to 30, exactly 0 outside; rank one
on every matrix and one direction per layer (the two writers at 0.984 to 1.000); on the output side one minus
the left kept fraction is 6.29, 6.52 and 6.16 on the down projections of layers 21, 22 and 23 (relative changes
0.121 to 0.128), 0.60 to 1.08 on those of 18 to 20, 0.07 to 0.14 on 24 to 30, 0.98 falling to 0.21 on 34 to 39,
and 0.06 to 0.39 on the twelve attention outputs; the rows moved 0.00007 to 0.00026 on all 31. The 31B of round
31 was four layers to 5.4 with the rows restored. Against the saved vectors the directions stand at 0.986 on the
left and 0.989 on the right to TrevorJS's 12B edit and its four re-uploads on all 31 shared names (minimum
0.952), at 0.61 to Carlosian's and 0.60 to Paul691's duplicate, and at 0.27 or less to the kernel passes and the
arbitrary-rank searches; the maker's 31B stands at 0.90 to 0.94 to TrevorJS's 31B on its 8 names. By byte range
the layer 21 down projection is 0.1208 from Google's and 0.1025 from TrevorJS's (his 0.0191 from Google's), the
layer 21 attention output 0.0064 from Google's and 0.0119 from TrevorJS's, and the layer 30 down projection
0.0015 from Google's and 0.0176 from TrevorJS's.

Why it matters: finding 65 read one export; a second from the same maker on another base reads the same three
marks (a few down projections pushed past 5 while the rest of the window stays under 1, exact row restoration,
a card with no table), so the "custom ORBA" is a method with a fingerprint and not one run's setting. The
direction is the one-direction family's at 0.986, inside the 0.98 to 0.99 at which independent runs on the same
prompt sets stand (findings 85 and 103) and short of the 1.000 of a copy, and the weights and the bytes say
whose run it is: the maker's. It is the fourth time the census reads a maker's method from the weights across
two bases (findings 24, 74 and 103 are the others).

Evidence: `results/weights/Sabomako-gemma-4-12B-it-heretic.json`, the `results/meta/` report, the direction file
under `wheat41/measurements/pair-6/` against `blueback8/measurements/pair-6/` (TrevorJS's 12B) and the
twenty-seven other 12B measurements, `results/weights/Sabomako-gemma-4-31B-it-heretic.json` (finding 65), the
byte-range reads listed in `docs/census-round-41.md`, and the reading in `docs/cards/`.

## 113. The first copy of a function-calling original reads a per-layer kernel pass to the layer and the second decimal on an eighteen-layer stack, and marks the function-response token special where the original does not

Roman0's functiongemma-270m-it-heretic was created on 2025-12-19, the day after Google released
functiongemma-270m-it, a 270-million-parameter Gemma 3 text model tuned for function calling (18 layers, 236
tensors, one shard), the census's thirty-fourth original and its smallest. The card is Heretic 1.1.0's table
with a direction index "per layer", `attn.o_proj` at a maximum of 1.33 at position 12.65 and a minimum of 0.85
at a distance of 4.36, `mlp.down_proj` at 1.46 at 12.22 and 1.40 at 4.97, a KL divergence of 0.2617 and 2
refusals in 100 against 100. The weights are the card: 19 of 236 tensors, the down projections of layers 8 to 17
and the attention outputs of 9 to 17 (12.22 less 4.97 and 12.65 less 4.36 give 8 and 9; both windows end at
the stack's last layer), exactly 0 outside, rank one on every matrix, one direction per layer (the writers at
1.000, the layers at 0.29 to 0.86 to layer 13), on the output side at 1.41 rising to 1.45 at layers 12 and 13
and falling to 1.40 on the down projections and 0.93 rising to 1.29 at 13 and falling to 0.85 on the attention
outputs, within 0.04 of the printed heights at the printed layers, rows 0.019 to 0.489 unrestored. The token
side is the one of the round the home judgement cannot close: in `tokenizer_config.json` and `tokenizer.json`
the copy marks token 50, `<start_function_response>`, and token 255999, `<start_of_image>`, as special where
the original marks neither, and ships no `added_tokens.json` where the original's holds `<end_of_image>` and
`<image_soft_token>`; the ids are equal (`eos_token_id` `[1, 50]`, generation `[1, 50, 106]`) and the version
strings the same 4.57.3. By byte range the layer 12 down projection is 0.0700 from Google's and holds one value
in ten thousand at exactly zero where Google's holds none, the projection's smallest results under the bfloat16
floor.

Why it matters: the census had read Heretic's kernels on stacks of 30 to 60 layers; on eighteen the kernel still
reads to the layer and to the second decimal, and the two windows run to the stack's end, which the kernel's
positions and distances predict. The special flag is what a decoder that skips special tokens uses to drop a
token from its text, and the token the copy changed is the one a function-calling model emits around a tool's
result, so the one token-side difference in the round sits on exactly the behaviour the original exists for;
the weights say nothing about it and the metadata tool has no line for it yet. The population now has an
original outside the Gemma 4 and Mistral families.

Evidence: `results/weights/Roman0-functiongemma-270m-it-heretic.json`, `results/meta/Roman0-functiongemma-270m-it-heretic.json`
(the seven token fields), the direction file under `wheat41/measurements/pair-2/`, the byte-range reads listed
in `docs/census-round-41.md`, and the reading in `docs/cards/`.

## 114. An E4B pass from the tool's 1.3.0 under a Spanish name records the tool's English prompt sets, stops six layers short of its kernels' reach, reads no kernel in its kept fractions under a full row normalisation, and stands at 0.75 to the author's export on the same prompts

ImanolSuarez's gemma-4-E4B-it-heretic-seguridadDeLaInformacion was created on 05-23 with a `reproduce/` folder
beside the weights: the configuration names `google/gemma-4-E4B-it` at `d6436b3d`, mlabonne's English
`harmless_alpaca` and `harmful_behaviors` at `train[:400]` for the directions and `test[:100]` for the
evaluation, the system prompt "You are a helpful assistant.", `row_normalization` "full" at a LoRA rank of 3,
`orthogonalize_direction` true, trial 92 of 200, one RTX 5080 under Windows 11, Heretic 1.3.0 and transformers
5.9.0. The name promises an information-security run and the record shows the tool's default search. The card
is 1.3.0's table (`direction_index` 29.08; `attn.o_proj` 1.30 at 30.63, minimum 0.47 at 13.10; `mlp.down_proj`
1.34 at 33.43, minimum 0.72 at 17.07; 6 refusals in 100 against 99) under `google/gemma-4-E4B` in its
`base_model` field, finding 67's inherited header over instruct-model weights. The weights are 37 of 2,076
tensors, the down projections of layers 17 to 35 and the attention outputs of 18 to 35, exactly 0 outside: the
kernels' lower ends (16.4 and 17.5) read to the layer and their upper ends reach past the stack's last layer,
41, where both writers of layers 36 to 41 are exactly 0, twelve matrices the kernels cover and the weights do
not touch. One direction for the window (the layers at 0.94 to 1.00, the writers at 0.91 to 1.00), rank one
(first shares 0.978 to 0.997); on the output side the kept fractions do not trace the kernels (0.65 at 17
rising to 1.02 at 31 and falling to 0.81 on the down projections under a printed 1.34; 0.16 to 0.91 with no
order on the attention outputs under 1.30), while the relative change rises along the window from 0.010 to
0.029 as a kernel would; rows 0.0039 to 0.0112, rising with the layer. The direction stands at 0.755 to
p-e-w's E4B export and his reproduction on all 37 shared names (minimum 0.724), 0.71 to sh0ck0r's and 0.69 to
BinxNet's, and at 0.40 or less to every other E4B edit; by byte range the layer 26 attention output is 0.0165
from p-e-w's and 0.0191 from Google's, the layer 26 down projection 0.0243 from p-e-w's and 0.0223 from
Google's. The fourth shard is the E4B layout shard (finding 71). The template differs from the pin's in line
endings alone, the Windows save.

Why it matters: a repository's name is the first thing anyone sees and the record under it says the prompts
were the tool's English defaults, so the name is a label; the census reads the record and the weights, and the
two agree with each other and not with the name. The run stands at 0.75 to the tool author's own export on the
same prompt sets, outside the 0.96 to 0.98 at which independent runs of the earlier versions stand (findings 85
and 102) and above the 0.4 to 0.6 of a changed prompt set (findings 83, 93 and 99); what the record shows
changed is the tool's version with its orthogonalised direction and full row normalisation, the two settings
that also leave the kept fractions without the kernel's shape and the window six layers short of the kernels'
reach. The 1.3.0 pass is a different signature from the 1.1 and 1.2 passes the census has read, and the next
copies from that version will say whether the short window and the shapeless kept fractions are the version's
or this run's.

Evidence: `results/weights/ImanolSuarez-gemma-4-E4B-it-heretic-seguridadDeLaInformacion.json`, the
`results/meta/` report, the direction file under `wheat41/measurements/pair-4/` against
`wheat33/measurements/pair-2/` (p-e-w's) and the thirty-eight other measurements on the E4B base, the repository's
reproduction record under `reproduce/` as read on 2026-11-02, the byte-range reads listed in
`docs/census-round-41.md`, and the reading in `docs/cards/`. Round 42 reads the tool's 1.4.0 under the same two settings on a 31B fine-tune: both kernels to the layer at both ends and the down kernel's peak to the second decimal in the kept fractions, with the rows 0.0016 to 0.0077, so the shapeless kept fractions and the short window of this copy were this run's and not the settings' (finding 122).

## 115. One maker's first E2B export carries the single direction at 0.96 to 0.98 to three makers' passes at the card's kernel weights to the second decimal, six hours before the maker's arbitrary-rank search carried another at 0.06

MoonRide's gemma-4-E2B-it-heretic was created at 16:28Z on 04-08 under Heretic 1.2.0's table (`direction_index`
16.97; `attn.o_proj` 1.21 at 24.75, minimum 1.14 at 10.31; `mlp.down_proj` 1.38 at 26.14, minimum 1.16 at 15.83;
a KL divergence of 0.2056, 9 refusals in 100 against 99); the maker's arbitrary-rank E2B search of finding 104
was created at 22:10Z the same evening and the custom-prompt one the next afternoon. The weights are the card: 44
of 2,011 tensors, the down projections of layers 11 to 34 and the attention outputs of 15 to 34 (26.14 less
15.83 and 24.75 less 10.31 give 11 and 15; the far ends past the stack's last layer, 34), exactly 0 outside, rank
one on every matrix, one direction on all 44 (1.000 across layers and kinds), on the output side at 1.17 rising
to 1.38 at layer 26 and falling to 1.27 on the down projections and 1.14 rising to 1.21 at 25 and falling to
1.15 on the attention outputs, the printed maxima to the second decimal at the printed layers, rows 0.0055 to
0.034 unrestored. The direction stands at 0.982 to tvall43's v0 on all 16 shared names, 0.970 to huihui-ai's E2B
edit, its second measurement and its two re-uploads on all 44, and 0.960 to DuoNeural's on all 44, and at 0.063
and 0.047 to the maker's own two searches of that evening and the next day; by byte range the layer 21 attention
output is 0.0105 from huihui-ai's, 0.0294 from Google's and 0.0921 from tvall43's v0.

Why it matters: findings 96 and 110 read the E2B's single direction from huihui-ai, DuoNeural and tvall43; a
fourth maker carries it at the same 0.96 to 0.98, which fixes the number for an independent kernel pass of the
tool on this base, and finding 110's sequence repeats in the maker's own repositories: a kernel pass first,
then an arbitrary-rank search with a direction at 0.06 to it, six hours apart where tvall43's were
thirty-four minutes. The kernel reads to the layer and to the second decimal on both writers, so the card's
table is the weights' table on this pass, as on tvall43's v0 and not on his v1.

Evidence: `results/weights/MoonRide-gemma-4-E2B-it-heretic.json`, the `results/meta/` report, the direction file
under `wheat41/measurements/pair-5/` against `nautilus40/measurements/pair-8/` (tvall43's v0),
`blueback13/measurements/pair-2/` (huihui-ai's), `nautilus38/measurements/pair-6/` (DuoNeural's) and
`wheat39/measurements/pair-5/` and `pair-7/` (the maker's searches), the byte-range reads listed in
`docs/census-round-41.md`, and the reading in `docs/cards/`.

## 116. Two further arbitrary-rank exports read as their siblings: one maker's third 12B search at 0.96 and 0.94 to its two with five residues and the rows in the band, and another maker's first E4B export at 0.93 to 0.98 to its four with every matrix edited and the window six layers short of the card

RumiaChannel's gemma-4-12B-it-uncensored-ara-Refusals4 was created at 06:36Z on 06-05, between the maker's
Refusals2 (06:29Z, finding 99) and Refusals9 (06:44Z, round 25), under Heretic 1.2.0's arbitrary-rank branch
with `start_layer_index` 24 and `end_layer_index` 37, 4 refusals in 100 against 91. The weights are the branch:
26 of 677 tensors, both writers of layers 24 to 36, exactly 0 outside; 21 edits on the input side at weights
0.47 to 1.71 with a few directions each and rows 0.0049 to 0.0079, finding 22's band; five down projections
(layers 25, 27, 30, 32 and 34) rewritten by 0.0012 to 0.0018 with both kept fractions at 1.00, finding 58's
residues. The directions stand at 0.957 and 0.937 on the left to Refusals2 and Refusals9 on all 26 names (0.98
and 0.96 on the attention outputs) and at 0.55 and 0.54 to llmfan46's and coder3101's 12B edits; by byte range
the layer 30 attention output is 0.0075 and 0.0094 from the siblings', which stand 0.0046 apart. The template is
Google's 07-15 revision, carried in by a 07-21 update of the template and tokenizer configuration six weeks
after the weights. NullpoLab's gemma-4-E4B-it-Heretic-ARA-Refusals3 was created at 13:57Z on 04-04, the
maker's first export, twelve minutes before Refusals5 and thirteen before Refusals8, under the branch's pull
request 211 at commit `3b70fe5` with `start_layer_index` 19 and `end_layer_index` 37. The weights are the
branch: 26 of 2,130 tensors, both writers of layers 19 to 31, every matrix an edit on the input side at 0.73 to
1.43 with first shares of 0.24 to 0.95, no residue, exactly 0 outside, the layers 32 to 36 inside the card's
window untouched, as three of the maker's four other exports ended short of theirs; rows 0.0025 to 0.0184 on
the attention outputs and 0.0011 to 0.0068 on the down projections, through and over the band as the maker's
other exports read. The directions stand at 0.982 to Refusals8, 0.955 to Refusals6-attn, 0.949 to
Refusals8-attn and 0.929 to Refusals5, at 0.87 to coder3101's and 0.86 to llmfan46's, and at 0.093 to
ImanolSuarez's 1.3.0 pass of the same base; by byte range the layer 29 attention output is 0.0175 from
Refusals8's. The template is Google's 04-28 revision, carried in by the 04-29 upload as on the maker's other
exports.

Why it matters: both makers' families now have every export measured (RumiaChannel's three 12B searches,
NullpoLab's five E4B exports), and each new one reads as its siblings did: the same window form, the same rows,
directions at 0.93 to 0.98 within the maker and 0.55 to 0.87 to the English-prompted family. The two makers
differ in one habit the weights keep: RumiaChannel's windows are the card's to the layer with residues inside,
NullpoLab's end short of the card with every matrix inside them edited. Neither card says either, and both
read without a prompt.

Evidence: `results/weights/RumiaChannel-gemma-4-12B-it-uncensored-ara-Refusals4.json`,
`results/weights/NullpoLab-gemma-4-E4B-it-Heretic-ARA-Refusals3.json`, the `results/meta/` reports, the
direction files under `wheat41/measurements/pair-1/` and `pair-3/` against `nautilus38/measurements/pair-3/`
and `blueback22/measurements/pair-3/` (Refusals2 and Refusals9) and `wheat39/measurements/pair-8/`,
`blueback29/measurements/pair-5/`, `nautilus40/measurements/pair-7/` and `wheat37/measurements/pair-8/`
(NullpoLab's four), the byte-range reads listed in `docs/census-round-41.md`, and the readings in
`docs/cards/`.

## 117. Eight Heretic edits of community fine-tunes, merges and first edits, measured against the parents their cards name, read their cards on the parent as the first-generation copies read theirs on Google, and the saved vectors of the Google-rooted families place six of them

Round 42 is the census's first round from the second-generation pool: eight copies whose cards name a community
repository as the parent, measured against that parent and not against Google. Four are arbitrary-rank searches
over fine-tunes and merges (llmfan46's edits of zerofata's MeroMero 31B and aifeifei798's Queen 31B, Vortex5's
edits of the maker's own Moonlight-Dusk and Chimera-X merges of the 26B-A4B), one is a Heretic 1.4.0 kernel pass
over bgg1996's own Melinoe fine-tune of the 31B, one is SubMaroon's three-part merge over Gryphe's StyleTune-V2,
and two are Unsloth fine-tunes over unmeasured first edits (Justbackup's duplicate of DavidAU's 27B over
coder3101's edit, DavidAU's 4B over his own Extreme). Against the parent each pair reads the edit alone, and the
parent's own distance from Google is read separately by byte range: the fine-tunes and merges stand 0.0035 to
0.0246 from Google's tensors on the matrices read, the first edits 0.0218 and 0.0385. All eight read their cards:
the four searches read their windows with the branch's selection inside them (layers 42 and 49 absent and 46
traced on MeroMero, 56 absent on Queen, 3 to 8 traced or under the threshold and 22 absent on Moonlight-Dusk, 23
absent on Chimera-X), the kernel pass reads its kernels to the layer at both ends, the merge reads its three edits
one by one, and the two fine-tunes read training on every linear map of every layer and nothing on the vision
towers; the largest relative change outside the changed set is exactly 0 on four pairs, 0.000003 on one and
0.00099 on three, every non-zero inside the window or on a fine-tune's normalisation vectors. The direction check
of finding 66 keeps its meaning on six of the eight, because every parent descends from a Google checkpoint and
the saved vectors of the Google-rooted families are the edit's and not the parent's: the merge's body stands at
1.000 to coder3101's 26B-A4B edit, Vortex5's two searches at 0.95 to 0.99 to the 26B-A4B arbitrary-rank family,
llmfan46's two at 0.89 to 0.99 to the 31B family and the maker's own April edit, and bgg1996's pass at 0.92 to
the per-layer 31B passes of finding 105; the two fine-tunes over unmeasured first edits carry no direction (0.071
to mlabonne's 27B projection; nothing to stand against on the 4B), and the edits under them stay unread until
their parents are measured against Google. One population rule follows: a community parent counts as neither an
original nor a copy, so the originals stay the publisher's thirty-four checkpoints and a parent enters the copy
count only when it is itself measured against its own parent.

Why it matters: the first forty-one rounds measured every copy against a Google checkpoint, and a copy whose
card named a community parent read that parent's change under the edit (findings 25, 54, 61 and 66) until it was
measured again against the parent (finding 77). Measured against the parent from the start, the second
generation reads as cleanly as the first: the windows, the rows, the kernels and the directions are the
branch's and the tool's, and a fine-tune or a merge under the edit does not move the direction the search finds
on the same checkpoint. The two exceptions are the rule's edge: where the parent is itself an unmeasured edit,
the pair reads only what the maker added, and the pinner has to queue the parent.

Evidence: the eight `results/weights/` and `results/meta/` reports of round 42, the direction files under
`nautilus42/measurements/pair-1/` to `pair-8/` against the thirty measurements of the 31B, twenty-nine of the
26B-A4B and one of the 27B, the byte-range reads listed in `docs/census-round-42.md`, the batch note in
`data/batches/round-42-batch-1.json`, and the readings in `docs/cards/`. Round 43 reads eight more against the parents their cards name, all eight exactly 0 outside the changed set, and takes the check to a base whose fine-tunes carry their own directions (findings 123 to 126). Round 45 reads eight more against the parents their cards name, six of them first measurements, one a hub duplicate measured as its source and one its parent's files unchanged, and applies the rule to a parent that is a re-upload of a publisher's checkpoint (unsloth's Nemo Instruct, Mistral's shards by object id) and to a parent that is a first edit whose own original only the bytes name (findings 127 to 134). Round 47 reads eight more against the parents their cards name, the first outside the Gemma and Mistral instruct lines, and applies the rule to two parents the pinner marks as roots of their chains, Zephyr and GraySwanAI's circuit-breaker model, which count as neither originals nor copies, to a text-only re-save whose tensors are Mistral's, and to a parent that is a measured copy, coder3101's 31B edit, so that pair adds a measurement and a copy (findings 135 to 142). Round 49 reads eight more against the parents their cards name and applies the rule to two depth upscales, a 54-layer Skyfall and a 59-layer passthrough merge, whose layers the bytes map to their 40-layer sources, to two trainings over Heretic edits, one of them over a measured copy so that pair adds a measurement and a copy, and to the census's first Gemma 2 parent (findings 143 to 150).

## 118. A merge whose card names a measured edit as its body stands at 1.000 to that edit on all 20 shared matrices with the bytes byte-equal, its queries and keys nine tenths of the way to the donor the card names, and its `lm_head` the parent's, each component read against a different repository

SubMaroon's Gemma-4-26B-A4B-StyleTune-QK-Heretic was created on 09-13 with a card naming three edits and three
parents: the body "coder3101/gemma-4-26B-A4B-it-heretic (Heretic ARA, layers 10-30, KL 0.0499)", the `lm_head`
from Gryphe's StyleTune-V2 (a fine-tune that trains the `lm_head` alone), and the queries and keys interpolated
toward Gryphe's Pantheon-Reasoning 1.1 V2 at alphas of 0.85 on the sliding layers and 0.65 on the global layers
5, 11, 17, 23 and 29, "verified by tensor comparison". Measured against StyleTune-V2, 79 of 1,014 tensors changed:
the attention outputs of layers 10 to 29 at a few directions per matrix on the input side at weights 0.76 to
1.49 with the rows 0.0061 to 0.0080 (coder3101's measured window and band), the query projections of all 30
layers and the key projections of 29 rewritten by 0.0010 to 0.0048 with no direction (layer 5's key under the
threshold at 0.00099, the largest change outside), and the `lm_head` unchanged, the parent's own. Against the
saved vectors the attention outputs stand at 1.000 on both sides to coder3101's edit on all 20 shared names
(minimum 1.000), at 0.992 to llmfan46's and 0.978 to SassyDiffusion's, and at 0.984 and 0.947 to Vortex5's two
searches of the same round. By byte range the layer 20 attention output is byte-equal to coder3101's and 0.0377
from StyleTune-V2's, Google's and Pantheon V2's; the layer 20 query and key projections are 0.0034 and 0.0033
from the base's (StyleTune-V2's, coder3101's and Google's, byte-equal to each other) and 0.0004 and 0.0003 from
Pantheon V2's, which stand 0.0036 and 0.0035 from the base's; the layer 5 keys 0.0010 from the base's and 0.0003
from Pantheon V2's (0.0011 apart); and the layer 20 down projection byte-equal on the three base repositories.
The merged queries and keys sit nine tenths of the way to the donor's on the sliding layer and on the global
one; at that size a bfloat16 step is 0.4 percent of a value, so the two alphas the card prints cannot be read
from the bytes. The token files are coder3101's body's and not the parent's: `eos_token_id` `[1, 106]` and no
`pad_token_id` where the Unsloth-saved parent carries 106 and 0, and Google's 07-15 template in place of the
parent's 04-10 one.

Why it matters: findings 85, 95, 102, 105 and 111 read 1.000 between two repositories as one tool on one base and
one prompt set, with the bytes deciding between a copy and an independent run and the card silent or wrong about
which. This is the first 1.000 under a card that declares the copy: the maker names the measured edit as the body
and says the tensors were compared, and the measurement, the saved vectors and the bytes agree with the card on
each of the three components. It is also the first merge read component by component, each part against the
repository that supplies it, which is what a merge entry in the recipe table would do with the saved vectors of
measured copies.

Evidence: `results/weights/SubMaroon-Gemma-4-26B-A4B-StyleTune-QK-Heretic.json`, the `results/meta/` report, the
direction file under `nautilus42/measurements/pair-6/` against `blueback12/measurements/pair-6/` (coder3101's) and
the twenty-eight other 26B-A4B measurements, the byte-range reads listed in `docs/census-round-42.md`, the
repository's card and the three parents' histories as read on 2026-11-02, and the reading in `docs/cards/`.

## 119. One maker's two arbitrary-rank searches on two of the maker's own merges stand at 0.95 to 0.99 to the 26B-A4B family and 0.957 to each other, the windows the card's with the rows in the band and one window opening on three traces

Vortex5's G4-Moonlight-Dusk-26B-A4B-heretic was created on 07-15 over the maker's four-model `nexus` merge of
Pantheon-Reasoning 1.1, Esmeralda, Animus V14.1 FFT and MeroMero 26B-A4B (created 07-13), under Heretic 1.2.0's
arbitrary-rank branch with `start_layer_index` 3 and `end_layer_index` 22, 14 refusals in 100 against 100; the
maker's Chimera-X-26B-A4B-heretic was created on 07-19 over a multi-stage merge (two `nearswap` stages and a
`karcher` stage) whose ingredients include the Moonlight-Dusk merge, with `start_layer_index` 6 and
`end_layer_index` 23, 12 refusals in 100. Measured against the merges, the two read the branch: 16 of 1,014 and 17
of 1,014 tensors, the attention outputs alone; Moonlight-Dusk's edits on layers 9 to 21 at input-side weights 1.31
to 2.96 with rows 0.0064 to 0.0077, its layers 3 to 5 rewritten by 0.0010 to 0.0018 without a direction and 6 to
8 under the threshold (finding 58's traces at the window's opening), layer 22 untouched; Chimera-X's edits on
every layer from 6 to 22 at 1.10 to 2.03 with rows 0.0058 to 0.0078, layer 23 untouched and exactly 0 outside.
The directions stand at 0.985 to SassyDiffusion's search on all 13 shared names, 0.955 to llmfan46's and 0.947 to
coder3101's for Moonlight-Dusk, at 0.991 to llmfan46's on all 17 names (minimum 0.910), 0.984 to coder3101's and
0.965 to SassyDiffusion's for Chimera-X, at 0.957 to each other and at 0.32 or less to every kernel pass and
projection on the base. By byte range Moonlight-Dusk's layer 16 attention output is 0.0516 from its merge's and
0.0367 from SassyDiffusion's (the merge 0.0246 from Google's), and Chimera-X's layer 10 attention output 0.0367
from its merge's, 0.0276 from llmfan46's and 0.0273 from the maker's Moonlight-Dusk edit, the two merges 0.0135
apart. The merges, Unsloth saves without a `generation_config.json`, leave the home tool one unexplained field
each, the generation file the copies wrote from their configurations.

Why it matters: the 26B-A4B arbitrary-rank family (SassyDiffusion's, llmfan46's and coder3101's searches on
Google's checkpoint, findings 86 and 98) stands at 0.96 to 0.98 within itself, and two searches run over merges
of four and five fine-tunes stand inside that band with the family and with each other, so a merged parent moves
neither the direction the branch finds nor the band its rows land in. The windows read to the layer on both
cards with the branch's selection inside, and Moonlight-Dusk adds a form the census had read inside a window and
not at its opening: three traces and three under-threshold layers before the first edit.

Evidence: `results/weights/Vortex5-G4-Moonlight-Dusk-26B-A4B-heretic.json`,
`results/weights/Vortex5-Chimera-X-26B-A4B-heretic.json`, the `results/meta/` reports, the direction files under
`nautilus42/measurements/pair-4/` and `pair-8/` against `nautilus38/measurements/pair-1/` (SassyDiffusion's),
`nautilus16/measurements/pair-2/` (llmfan46's), `blueback12/measurements/pair-6/` (coder3101's) and the
twenty-six other 26B-A4B measurements, the byte-range reads listed in `docs/census-round-42.md`, and the readings
in `docs/cards/`. Round 43 adds llmfan46's edit of zerofata's 26B-A4B fine-tune at 0.979 to the Chimera-X edit and 0.957 to the Moonlight-Dusk edit (finding 125).

## 120. One maker's two arbitrary-rank searches on two other makers' 31B fine-tunes stand at 0.89 to 0.99 to the 31B family and the maker's own April edit, each with one layer's component amplified rather than removed, to 6.71, under the maker's own template carried into both

llmfan46's Gemma-4-Queen-31B-it-uncensored-heretic was created on 04-12 over aifeifei798's Queen fine-tune of the
31B (created 04-10), under Heretic 1.2.0's arbitrary-rank branch with `start_layer_index` 26 and
`end_layer_index` 56, 12 refusals in 100 against 99 at a KL divergence of 0.0707; the maker's
G4-MeroMero-31B-uncensored-heretic was created on 05-15 over zerofata's MeroMero fine-tune (created 04-30), with
`start_layer_index` 28 and `end_layer_index` 49, 15 refusals in 100 at 0.0100. Measured against the fine-tunes,
both read the branch on the attention outputs alone: Queen on every layer from 26 to 55 (30 of 1,188, exactly 0
outside, layer 56 untouched) at input-side weights 1.19 to 3.70 on 28 matrices and 0.26 at layer 48, with layer
50's component multiplied by 6.71 rather than removed (relative change 0.1205, the row norms moved 0.197, the
largest input-side reading in the census); MeroMero on layers 28 to 48 less 42 (19 of 1,188, layer 46 rewritten by
0.000003) at 0.90 to 1.97 on 18, with layer 48's component multiplied by 1.34 (relative change 0.0488, the rows
0.0245). The rows run through and over finding 22's band on both (0.0006 to 0.197, 0.0009 to 0.0245). The
directions stand at 0.993 to the maker's own April 31B edit on all 18 shared names, 0.968 to MoonRide's search
and 0.964 to coder3101's for Queen; at 0.939 to coder3101's on all 19 names, 0.916 to MoonRide's and 0.890 to the
maker's April edit for MeroMero; at 0.887 to each other (0.953 on the right); at 0.51 and 0.56 to Jim-darby's
Japanese-weighted search; and at 0.20 or less to every 31B kernel pass and projection, 0.13 and 0.15 to
bgg1996's pass of the same round. By byte range Queen's layer 45 attention output is 0.0665 from its parent's and
0.0187 from the maker's April edit, which is 0.0745 from Google's there, and its layer 50 0.1195 from the parent's,
which is 0.0032 from Google's; MeroMero's layer 40 is 0.0266 from its parent's and 0.0237 from the maker's April
edit (the parent 0.0035 from Google's). Both copies carry one 17,344-byte template, the one the maker's own 31B
repository has carried since 05-05, in place of the parents' (Google's 04-28 revision on MeroMero, the release
revision on Queen); Queen took it by a delete and re-upload on 05-04 and 05-05, three weeks after its weights,
and MeroMero on the evening of its upload.

Why it matters: the 31B arbitrary-rank family stands at 0.87 to 0.97 within itself (finding 108), and two
searches over other makers' fine-tunes stand inside that band and at 0.99 to the maker's own first edit, so a
fine-tuned parent does not move the direction the branch finds on this checkpoint either. What the parent does
not explain is the amplification: on each copy one layer's component along the found direction is multiplied
rather than removed, by 6.71 on Queen, which no card line names and no recipe entry allows (every weight line
reads a kept fraction between 0 and 1). The template is the maker's-template case the round 37 note asked for a
line on, now read on three repositories of one maker.

Evidence: `results/weights/llmfan46-Gemma-4-Queen-31B-it-uncensored-heretic.json`,
`results/weights/llmfan46-G4-MeroMero-31B-uncensored-heretic.json`, the `results/meta/` reports, the direction
files under `nautilus42/measurements/pair-3/` and `pair-2/` against `blueback12/measurements/pair-1/` (the maker's
April edit), `blueback12/measurements/pair-2/` (coder3101's), `wheat37/measurements/pair-5/` (MoonRide's) and the
twenty-seven other 31B measurements, the byte-range reads and template matches listed in
`docs/census-round-42.md`, the template history of `llmfan46/gemma-4-31B-it-uncensored-heretic` as read on
2026-11-02, and the readings in `docs/cards/`. Round 43 adds the maker's 26B-A4B edit at 0.94 to the maker's own April edit of that checkpoint, with no layer amplified and a fourth template (finding 125), and densenet's 31B edit at 0.91 on the left and 0.45 on the right to the maker's April edit (finding 124). Round 45 adds the maker's Garnet search over ConicCat's 31B fine-tune at 0.78 to the April edit and 0.80 to the Queen and MeroMero edits, with input-side weights to 2.66 and no kept fraction above 1, so neither the fine-tuned parent nor the "ultra" in the name brings the amplification back (finding 134). Round 47 adds the maker's Gembrain and Harmonia searches over two 31B merges, at 0.886 and 0.602 to the April edit with no component amplified, the second over a merge that carries the maker's own Gembrain edit (findings 140 and 141). Round 49 adds the maker's PaintedFantasy and first Garnet searches, at 0.64 to 0.84 to the maker's Mistral Small searches and at 0.811 to the April edit, with input-side weights to 2.39 and 3.44 and no component amplified (findings 145 and 147).

## 121. Two Unsloth fine-tunes over unmeasured Heretic first edits read training on every linear map of every layer and no direction, one of them a hub duplicate whose shards the hub's object ids place in its parent at three revisions, under cards that print the parent edit's table

Justbackup's Gemma-3-27b-it-Uncensored-HERETIC-Gemini-Deep-Reasoning was created on 08-24 by one commit titled
"Duplicate from DavidAU/Gemma-3-27b-it-Uncensored-HERETIC-Gemini-Deep-Reasoning"; DavidAU's repository (created
01-25, two files replaced on 02-21) is present, and the duplicate's twelve shards are its shards at its head and
at `9e0a6b4d` and `75c7c4fd` by object id, where the batch note had recorded that "its weight files differ". The
card is DavidAU's, "a fully uncensored, full deep thinking Gemma 27B fine tune via Unsloth" over
coder3101/gemma-3-27b-it-heretic (Heretic 1.0.1 on Google's 27B, 2025-11-23, unmeasured), and it prints
coder3101's table (a KL divergence of 0.07, 9 refusals in 100 against 98). Measured against coder3101's edit, 418
of 1,247 tensors changed, the down, gate, up, query and attention output projections of all 62 layers, the values
of 60 and the keys of 48, by 0.10 to 0.84 percent with layer 0's down projection at 4.07 percent, first shares
0.24 to 0.97, both kept fractions near 1 on every matrix, the 438 vision and embedding tensors untouched, the
largest change outside 0.000995 on the normalisation vectors. DavidAU's gemma-3-4b-it-vl-Heretic-4-Horsemen-Uncensored
was created on 02-13 over the maker's own gemma-3-4b-it-heretic-uncensored-abliterated-Extreme (Heretic 1.0.1,
2025-11-22, "LOWEST refusal rate" at 2 in 100 and a KL divergence of 0.38, unmeasured), its card "a fully
uncensored, full deep thinking Gemma 4B fine tune using Four Horsemen reasoning dataset group" printing the
Extreme's table; 238 of 883 tensors changed, all seven linear maps of all 34 layers at 0.15 to 2.05 percent, first
shares 0.23 to 0.98, the vision tower exactly 0 and exactly 0 outside. Neither carries a direction (the 27B at
0.071 to mlabonne's projection on 124 names; the 4B with nothing to stand against). By byte range the 27B's layer
30 attention output and down projection are byte-equal to DavidAU's, 0.0044 and 0.0065 from coder3101's and
0.0223 and 0.0209 from Google's (coder3101's 0.0218 and 0.0198 from Google's); the 4B's layer 20 attention output
and down projection are 0.0132 and 0.0111 from the Extreme's and 0.0403 and 0.0286 from Google's (the Extreme's
0.0385 and 0.0273 from Google's): the training a fifth to two fifths of the edit on the matrices read. Both pairs
differ from their parents on the token side in version strings and defaults alone (4.57.3 to 4.57.6; 5.0.0.dev0
to 4.57.6 and three rope fields).

Why it matters: finding 97 read DavidAU's E4B fine-tune over coder3101's edit through a hub duplicate against
Google, the edit and the training together; the same maker's 27B and 4B fine-tunes, measured against the edits
their cards name, read the training alone, 0.1 to 2 percent on every linear map with the vision towers left as
they were, and the edits under them stay unread because their parents are not in the census. The inherited
header of finding 67 takes a third form here: a fine-tune's card printing its parent edit's refusal table as its
own. The duplicate is the tenth in the census and the second whose files the batch note separated from the
parent's that the hub's object ids then rejoined (finding 111's was the first), so the duplicate step should
compare object ids across the parent's revisions before recording a difference.

Evidence: `results/weights/Justbackup-Gemma-3-27b-it-Uncensored-HERETIC-Gemini-Deep-Reasoning.json`,
`results/weights/DavidAU-gemma-3-4b-it-vl-Heretic-4-Horsemen-Uncensored.json`, the `results/meta/` reports, the
hub's commit titles and file listings for both repositories, DavidAU's 27B repository at three revisions and the
two parent edits as read on 2026-11-02, the direction file under `nautilus42/measurements/pair-5/` against
`nautilus3/measurements/pair-2/` (mlabonne's), the byte-range reads listed in `docs/census-round-42.md`, and the
readings in `docs/cards/`. Round 47 reads two more training passes as their cards say: jwest33's role-play adapter over the maker's unmeasured Gemma 3 4B null-space edit, at the level of chance along the edit's published direction, and nbeerbower's ORPO adapter over coder3101's measured 31B edit, which leaves the edit where it was (findings 138 and 142). Round 49 reads two more training passes over Heretic edits as their cards say: Tetratype's antislop pass on the last five layers of coder3101's measured 26B-A4B edit, and DavidAU's second reasoning pass over coder3101's 27B edit, which contains this finding's first pass at a coefficient of 0.82 to 0.96 and adds a second training at right angles to it (findings 148 and 149).

## 122. A 1.4.0 kernel pass over a 31B fine-tune, with a reproduction record naming an orthogonalised direction and a full row normalisation, reads its kernels to the layer at both ends and the down kernel's peak to the second decimal, at 0.92 to the per-layer 31B family, with the first five shards the parent's

bgg1996's Melinoe-Gemma4-31B-VL-heretic was created on 07-11 over the maker's own Melinoe fine-tune of the 31B
(created 05-30, "fine-tuned for engaging in empathetic, intellectually stimulating, and deeply personal
conversations"), with a `reproduce/` folder uploaded in the same minute as the weights: Heretic 1.4.0 from PyPI,
mlabonne's `harmless_alpaca` and `harmful_behaviors` at `train[:400]`, the system prompt "You are a helpful
assistant.", `orthogonalize_direction` true, `row_normalization` "full" at a LoRA rank of 3, trial 155 of 200,
one RTX PRO 6000 Blackwell, the settings ImanolSuarez's 1.3.0 record carried (finding 114). The card is the
per-layer table: `attn.o_proj` 1.45 at 51.65 and 0.93 at a distance of 28.98, `mlp.down_proj` 1.22 at 43.01 and
1.11 at 5.21, a KL divergence of 0.0306, 15 refusals in 100 against 100. Measured against the fine-tune, 48 of
1,188 tensors changed, the attention outputs of layers 23 to 59 and the down projections of 38 to 48, exactly 0
outside: 51.65 less 28.98 and 43.01 less 5.21 give 23 and 38, 43.01 plus 5.21 gives 48, and the attention
kernel's far end lies past the stack's last layer, so both windows read to the layer at both ends. Rank one on
every matrix (first shares 0.990 to 0.995), one direction per layer (the writers at 0.993 to 0.998); on the output
side the down projections read 1.03 at 38 rising to 1.21 at 43 and falling to 1.10 at 48, the printed kernel's
shape and peak, and the attention outputs 0.31 at 23 rising with scatter (0.18 at 28, 0.82 at 40, 0.60 at 52) to
1.41 at 51 and 53 and 1.19 at 59, the printed peak within 0.04 and the printed lower end (0.93) 0.62 above what
the weights read; rows 0.0016 to 0.0077 on all 48. The directions stand at 0.920 to Vampelium's per-layer pass on
all 36 shared names, 0.919 to callmegrr's, germlag's and 3MPER0RR's (the four passes of finding 105 that stand
at 1.000 to each other), 0.888 to ressl's, 0.874 to TrevorJS's, 0.84 to Sabomako's 31B, 0.81 to jcxu97's
duplicate, 0.49 or less to the projections and 0.13 to 0.15 to the round's two 31B searches. By byte range the
layer 44 attention output is 0.0181 from the parent's, 0.0130 from Vampelium's and 0.0133 from germlag's (the
parent 0.0087 from Google's), the layer 44 down projection 0.0168 from the parent's, and the layer 10 query
projection byte-equal to the parent's and 0.0094 from Google's, the fine-tune's own change. The first five shards
are byte-equal to the parent's, the layers the kernels do not reach; the token side differs in version strings
and one default alone.

Why it matters: finding 114 read the tool's 1.3.0 under an orthogonalised direction and a full row normalisation
as a pass whose kept fractions carried no kernel and whose window stopped six layers short, and asked whether
that was the version's or the run's; the 1.4.0 pass under the same two settings reads both kernels to the layer at
both ends and the down kernel's peak to the second decimal, so the shapeless kept fractions and the short window
were that run's. The pass stands at 0.92 to the four per-layer passes that stand at 1.000 to each other, between
the 0.96 to 0.98 of independent runs of the earlier versions (findings 85 and 102) and the 0.75 of the 1.3.0 run,
on a fine-tuned parent that the layer 10 bytes show moved every matrix by about 0.01 before the edit. The five
byte-equal shards are the layout case of finding 71 read against a community parent: the layers the kernels do
not reach are the parent's bytes, and a duplicate rule reading shard checksums alone would call the copy a
partial re-upload of its parent.

Evidence: `results/weights/bgg1996-Melinoe-Gemma4-31B-VL-heretic.json`, the `results/meta/` report, the
repository's reproduction record under `reproduce/` as read on 2026-11-02, the direction file under
`nautilus42/measurements/pair-1/` against `nautilus40/measurements/pair-4/` (Vampelium's),
`nautilus40/measurements/pair-1/` (germlag's), `wheat33/measurements/pair-1/` (callmegrr's),
`nautilus19/measurements/pair-2/` (3MPER0RR's) and the twenty-six other 31B measurements, the byte-range reads
listed in `docs/census-round-42.md`, and the reading in `docs/cards/`.

## 123. One maker's six Heretic passes on six Mistral Nemo 12B fine-tunes and merges read both writers on the output side, three with one shared direction and three with one direction per layer, and the directions stand at 0.33 to 0.90 to each other, so on this base the direction is the fine-tune's as much as the base's

Round 43 measured Sorihon's six Heretic edits of Mistral Nemo 12B fine-tunes and merges against the parents their
cards name: DavidAU's MN-GRAND-Gutenberg-Lyra4-Lyra DARKNESS merge, anthracite-org's magnum-v4-12b, PocketDoc's
Dans-PersonalityEngine V1.3.0 (on Nemo Base), MarinaraSpaghetti's NemoMix-Unleashed merge, nothingiisreal's
Celeste V1.9 and yamatazen's EtherealAurora v2 merge, which already carries natong19's abliteration of Nemo
Instruct. The six parents share the architecture (40 layers, hidden size 5,120, a vocabulary of 131,072 with no
resized table on any side) and the copies share the method's shape: on every pair the changed tensors are the
attention outputs and the down projections of a window of layers and nothing else, the largest relative change
outside the changed set exactly 0 on all six, every edit on the output side. The windows differ by copy: layers 3
to 39 on DARKNESS (73 of 363 tensors), 7 to 39 on Magnum (63), 11 to 39 with the down projections from 21 to 38 on
Dans (47), 6 to 39 on NemoMix (67), 18 to 39 with the down projections from 22 to 34 on Celeste (35), 4 to 39 on
EtherealAurora (68). The method splits the six in two. DARKNESS, Magnum and NemoMix carry one direction shared
across every layer and both writers (median agreement 0.996, 0.998 and 0.997, cross-kind 0.89 to 0.94); Dans,
Celeste and EtherealAurora carry one direction per layer (agreement between adjacent layers 0.925, 0.945 and 0.861
at the median, 0.055 to 0.164 between the first layer and the last, the two writers of a layer unrelated on Dans
and Celeste and agreeing within the layer on EtherealAurora). The down projections read a kernel to the layer on
all six, rising and falling with the peak between layers 22 and 30 (0.82 on DARKNESS, 1.03 on Magnum, 1.08 on
Dans, 0.83 on NemoMix, 1.15 on Celeste, 0.81 on EtherealAurora). The attention outputs read scattered weights on
four (0.07 to 1.20 on DARKNESS, 0.33 to 1.28 on Magnum, 0.09 to 1.03 on NemoMix, 0.12 to 1.27 on EtherealAurora),
finding 46's shape on a Mistral base for the first time, near 1 on every layer of Dans (0.98 to 1.16, the
component removed whole with a small overshoot) and 0.59 to 1.31 on Celeste. On five of the six the last layer's
attention output reads apart from the kernel, the left kept fraction 0.88 to 0.93 beside a right kept fraction of
0.39 to 0.71 and the pair's largest relative change (0.029 to 0.033 on Dans, Celeste and EtherealAurora); Magnum's
last layer stays inside its kernel at 0.67 and 0.63. The rows move 0.0013 to 0.0218, through and over finding 22's
band. By byte range the layer 1 attention output and query projection of every copy read are byte-equal to the
parent's, and the parents stand 0.007 to 0.116 from Nemo Instruct's at that layer and 0.025 to 0.110 from Nemo
Base's, the fine-tunes' own changes under the windows.

The saved direction vectors answer a question the census could not ask before: whether the direction a tool finds
is a property of the base or of the fine-tune on it. On the Gemma 4 families the searches of different makers on
different fine-tunes and merges of one checkpoint stand at 0.93 to 0.99 to each other (findings 119, 120 and
125). On these six, one maker's passes on six fine-tunes of one base stand at 0.904 (DARKNESS to NemoMix, on all
67 shared names, minimum 0.897), 0.729 (Dans to Celeste), 0.707 (Magnum to Celeste), 0.696 and 0.609 (Celeste to
EtherealAurora), 0.664 and 0.613 (Dans to EtherealAurora), 0.605 (Magnum to Dans), 0.514 (DARKNESS to Magnum),
0.500 (Magnum to NemoMix), 0.455 (Magnum to EtherealAurora) and 0.33 to 0.37 on the other five pairs, left and
right sides alike. The closest pairs follow the parents' lineage: the two merges that carry Lyra and Gutenberg
lines stand at 0.90, the two fine-tunes of Nemo Instruct at 0.71, and the three per-layer passes at 0.61 to 0.73
among themselves. Against the two measured edits of Nemo Instruct itself the six stand at 0.39 to 0.68 to grimjim's
block-wise pass and 0.09 to 0.12 to DuoNeural's difference-of-means projection, and at 0.027 or less to the
controls on Mistral Small. By byte range at layer 24 the six copies' attention outputs stand 0.0275 (DARKNESS to NemoMix) to 0.0755 (Dans to Celeste) apart, each 0.017 to 0.022 from its own parent's, and the parents stand 0.015 to 0.063 from Nemo Instruct's at that layer, Instruct itself 0.036 from Base, so the parents sit as far from the checkpoint as its two forms sit from each other.

Why it matters: the direction check (finding 66) has placed parents and named tools by agreement at 0.93 or
more, on the reading that one tool on one base finds one direction. These six show the reading holds on Gemma 4
and not in general: on Mistral Nemo the fine-tune under the pass moves the direction the pass finds, by a lineage
the agreements trace, and a 0.5 between two edits of one base by one maker is no longer evidence of two tools or
two prompt sets. The six also give the census its first kernel passes on a Mistral base that read the 12B's
scatter rather than the kernel to the third decimal that finding 46 read on Mistral 7B and Mistral Small, so the
scatter is not the base's either.

Evidence: the six `results/weights/Sorihon-*.json` reports and their `results/meta/` reports, the direction files
under `wheat43/measurements/pair-3/` to `pair-8/` against each other and against the DuoNeural and grimjim
measurements under `blueback13/measurements/pair-7/` and `pair-6/`, the byte-range reads listed in
`docs/census-round-43.md`, and the readings in `docs/cards/`. Round 45 measures the base side: a Heretic pass on Nemo Instruct itself stands at 0.898 and 0.854 to the passes on the DARKNESS and NemoMix merges, 0.574 to the pass on Magnum and 0.39 to 0.43 to the three per-layer passes, so the agreement follows the method at least as much as the parent (finding 133).

## 124. An arbitrary-rank edit of a 31B fine-tune whose card claims row-norm preservation moves the rows 0.019 to 0.777 on both writers of layers 30 to 47, the largest in the census, at input-side weights to 4.36 over a parent whose layers are Google's bytes

densenet's Gemma-4-31B-StyleTune-heretic-ara is Heretic 1.2.0's arbitrary-rank branch over Gryphe's StyleTune, a
fine-tune whose card says one tensor changed out of 834, the `lm_head`; by byte range the parent's layer 44 and 46
attention outputs are byte-equal to Google's 31B. The card prints the branch's table "with row-norm preservation":
`start_layer_index` 30, `end_layer_index` 48, `preserve_good_behavior_weight` 0.8437, `overcorrect_relative_weight`
0.9644, a KL divergence of 0.0733 and 8 refusals in 100. Measured against the parent, 36 of 1,189 tensors changed,
the attention outputs and the down projections of layers 30 to 47 with layer 48 untouched and the parent's
`lm_head` untouched, exactly 0 outside. Every edit is on the input side: one minus the right kept fraction is 0.84
to 4.36 on the attention outputs (4.36 at layer 46, 3.34 at 34 and 41) and 2.10 to 3.35 on the down projections,
with no direction shared across layers (median 0.25) and the two writers of a layer unrelated. The relative changes
run 0.055 to 0.279 (layer 44's attention output 0.2790, layer 46's 0.2453), the largest of any arbitrary-rank edit
measured, and the rows move 0.019 to 0.777: 0.7769 on layer 46's attention output, 0.4769 on 44's, 0.4435 on
37's, 0.3844 on 43's, with every matrix over finding 22's band of 0.005 to 0.008. The claim holds on no row, as
wnfldchen's did (finding 84), and the two copies' left directions stand at 0.951 to each other on 18 names while
the right sides stand at 0.738; to llmfan46's April 31B edit the copy stands at 0.910 on the left and 0.448 on the
right, to the Queen edit of round 42 at 0.875 and 0.446, to coder3101's at 0.761 and 0.433, to MoonRide's
custom-prompt search at 0.793 and 0.346, and at 0.28 or less to every kernel pass and projection on the base. By
byte range the layer 44 attention output is 0.2750 from the parent's and from Google's, 0.2653 from llmfan46's
April edit and 0.2619 from coder3101's, and the layer 46 attention output 0.2406 from the parent's and 0.2143 from
llmfan46's. The layer 44 down projection is 0.0576 from the parent's and from Google's, the layer 10 query projection is byte-equal to both, and the `lm_head`, the one tensor the fine-tune trained, is byte-equal to the parent's. The copy is an Unsloth save (`unsloth_version` 2026.7.2): the token side differs on seven
fields at home after the 24 added-token entries that repeat the shared `tokenizer.json` were closed, the
configuration's version string dropped and the template copied into `tokenizer_config.json` beside a
`chat_template.jinja` byte-equal to the parent's. The scorer flagged 66 rules, 36 direction cosines and 30 first
shares.

Why it matters: the arbitrary-rank branch's "row-norm preservation" has now failed on two of the two copies that
print it, both at the top of the census's row movement, and the left and right sides of such an edit read
differently against the family: the left factors agree with the 31B searches at 0.76 to 0.95 and the right
factors, which carry the weights, at 0.35 to 0.74. The left side is the one that places an arbitrary-rank edit
in a family from the saved vectors, and the rows are the one measure that tests a card's preservation line.

Evidence: `results/weights/densenet-Gemma-4-31B-StyleTune-heretic-ara.json`, the `results/meta/` report, the
direction file under `wheat43/measurements/pair-2/` against the 31B measurements, the byte-range reads listed in
`docs/census-round-43.md`, the hub's listings and commit histories of both repositories, and the reading in
`docs/cards/`.

## 125. One maker's third second-generation search, on a 26B-A4B fine-tune, stands at 0.98 to Vortex5's Chimera-X edit and 0.94 to the maker's own April edit, its window 15 to 25 under a card to 26 with the rows under the band, uploaded twice in one evening under a fourth template

llmfan46's G4-MeroMero-26B-A4B-it-uncensored-heretic is the branch over zerofata's G4-MeroMero-26B-A4B, a
fine-tune of Google's 26B-A4B whose layer 20 attention output stands 0.0064 from Google's by byte range. The card
prints the arbitrary-rank table: `start_layer_index` 15, `end_layer_index` 26, `preserve_good_behavior_weight`
0.3274, `overcorrect_relative_weight` 0.6647, `attn.o_proj` the one target, a KL divergence of 0.0152 and 12
refusals in 100. Measured against the parent, 11 of 1,013 tensors changed, the attention outputs of layers 15 to
25, layer 26 untouched, the experts and the vision tower untouched, exactly 0 outside; input-side weights 0.99 to
1.55 with no layer amplified; relative changes 0.0100 to 0.0333; rows 0.0005 to 0.0055, under the band on ten
layers and at its edge on one, where the maker's two 31B edits of round 42 ran through and over it (finding 120).
The directions stand at 0.979 and 0.965 to Vortex5's Chimera-X edit on all 11 names, 0.957 to the Moonlight-Dusk
edit, 0.953 to SassyDiffusion's search, 0.942 and 0.955 to the maker's own April search of the 26B-A4B, 0.93 to
SubMaroon's body and coder3101's edit, 0.92 to 0.93 to the two QAT searches, 0.67 and 0.59 to OS-Software's two
Japanese-weighted searches, 0.203 to TrevorJS's kernel family and 0.055 to huihui-ai's projection, so the family
of finding 119 gains a sixth member at 0.93 to 0.98. By byte range the layer 20 attention output is 0.0333 from the
parent's, 0.0339 from Google's, 0.0255 from the maker's April edit and 0.0269 from coder3101's. Its layer 10 query projection is byte-equal to the parent's and 0.0059 from Google's, the fine-tune's own change. The
repository's history reads an upload, a deletion of every file fifty minutes later and a second upload of nine
files three minutes after that, the one measured; the copy carries a 17,708-byte template that differs from the
parent's (Google's revision `1db3cff1`) in two tool-call macros and renders the fixed conversation identically,
the maker's fourth template in the census after the 17,344-byte one of April and May, the 18,841-byte one now on
the 31B head and Google's 18,683-byte July revision.

Why it matters: the maker's three second-generation searches now span two checkpoints and three parents, and on
the 26B-A4B the search over a fine-tune lands where the search over Google landed (0.94 to the maker's own April
edit) and where two other makers' searches over merges landed (0.96 to 0.98), with the rows under the band this
time and no amplified layer, so finding 120's amplification and over-band rows are the 31B edits' and not the
maker's habit. The template is the maker's-template case a third time, now with a template of the maker's own
that no other repository carries.

Evidence: `results/weights/llmfan46-G4-MeroMero-26B-A4B-it-uncensored-heretic.json`, the `results/meta/`
report, the direction file under `wheat43/measurements/pair-1/` against the 26B-A4B measurements, the byte-range
reads listed in `docs/census-round-43.md`, the hub's commit history of the repository and the template histories
of the maker's three repositories and Google's 26B-A4B, and the reading in `docs/cards/`.

## 126. Six Heretic edits of Mistral Nemo fine-tunes carry cards without the tool's table, and their token files read the save version: the two transformers 5.8.0 saves drop the thousand declarations and the parent's special-token map and one replaces the template with one that renders differently, the four 4.57.6 saves add generation files and pad tokens their parents lacked, and the ids are Mistral's on every side

None of Sorihon's six cards prints Heretic's table: three (Magnum, Dans, Celeste) print a refusal count and a KL
divergence ("Refusals 8/100, KL Divergence 0.0129"; 6 and 0.0235; 5 and 0.0087) and three (DARKNESS, NemoMix,
EtherealAurora) print an image and a `base_model` field, with the tool named in the repository names alone, so the
windows, sides and directions of finding 123 are read from the weights with no card to hold them against. The
token sides read the version the copies were saved under. Magnum and Celeste are transformers 5.8.0 saves of
4.45.0.dev0 and 4.44.0.dev0 parents: each drops the 1,000 added-token declarations and the `special_tokens_map.json`
(finding 44's case, `tokenizer_config.json` at 442 and 338 bytes against the parents' full files), writes
`rope_parameters` in the configuration (closed at home as the 5.x form of `rope_theta`), and Magnum's `pad_token`
changes from `<pad>` (id 10) to `</s>` (id 2) with the template replaced by a 1,053-byte Mistral template whose
spacing differs from the parent's and renders the fixed conversation differently, the round's one rendering
difference. DARKNESS, Dans, NemoMix and EtherealAurora are 4.57.6 saves of 4.43.3, 4.51.3, 4.44.0 and 4.49.0
parents: the declarations stay, `torch_dtype` becomes `dtype`, `use_cache` turns from false to true on three, a
`generation_config.json` is written from the configuration where DARKNESS's, NemoMix's and EtherealAurora's parents
published none, a `pad_token` `</s>` is added where DARKNESS's and NemoMix's parents declared none, and the
template moves to `chat_template.jinja`, the parent's own on Dans (763 bytes), the Mistral one on DARKNESS and
NemoMix (whose parent published no template at all) and a 291-byte ChatML one on Celeste and EtherealAurora. The
ids are Mistral's on every side (`bos_token_id` 1, `eos_token_id` 2), the vocabulary is 131,072 on every side and
no table is resized. Two files are shared: Dans's first shard is byte-equal to its parent's by object id (the
layers below the window, as finding 71's layout rule expects) and DARKNESS's and Magnum's 17 MB `tokenizer.json`
re-saves share one object id. The home judgement under transformers 5.22.1 moved `config.rope_parameters` on
Magnum and Celeste and nothing on the other four.

Why it matters: the Nemo copies carry the token side the first-generation Gemma 4 copies did not, the
version-of-save reading of finding 39 on a second base, and they show that the dropped-declarations case of
finding 44 is a 5.x save's habit and not a maker's choice, since one maker's six edits split on it by version
alone. A card with no table is the common case on this maker's repositories, and the weights carried the whole
reading.

Evidence: the six `results/meta/Sorihon-*.json` reports and their home re-judgements, the hub's file listings and
object ids of the six copies and six parents, the template bytes compared at home, and the readings in
`docs/cards/`. Round 45 reads a seventh Nemo token side, a 5.3.0 save of a 4.49.0.dev0 parent whose template carries the assistant-mask tag of a trainer, which the tool's renderer cannot parse and which renders through transformers with one newline added (finding 133).

## 127. Two makers' edits of one coding fine-tune read two methods: one stands at 0.957 to a third maker's Heretic edit of the same checkpoint inside a bfloat16 recast of every linear map, the other at 0.49 to it, and neither is a duplicate of the other

Round 45 measured two edits of yuxinlu1's coding fine-tune of Gemma 4 12B, the checkpoint richardyoung's Heretic
edit was measured against in round 16 (finding 18), against that fine-tune: tpls's
gemma-4-12B-coder-fable5-composer2.5-v1-abliterated (created 2026-06-23, the weights in one commit titled
"abliterated bf16 ... KL_MAX=0.2", a card that names "refusal-direction ablation" and no tool, layer or weight) and
huihui-ai's Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated (created 06-21, Sumandora's
remove-refusals-with-transformers named as the method). The fine-tune is saved in float16. tpls's copy is five
bfloat16 shards: 322 of 677 tensors changed, 263 of them by the recast alone (the query, key, value, gate and up
projections of every layer, 27 attention outputs and four down projections at relative changes of 0.0011 to 0.0016,
the layer 5 query projection by byte range the parent's matrix rounded to bfloat16 on every entry), six more just
under the threshold (0.00087 to 0.00097), and the edit on the other 59: the down projections of layers 9 to 47 and
the attention outputs of 24 to 43, one direction on the left side of all 59 (0.981 to their common direction at
the median, the two writers of a layer at 0.978), first shares 0.56 to 0.995, the kept fractions scattered on both
sides (left -0.16 to 0.98, right -0.02 to 0.98, the left below the right on 24 of 59), rows moved 0.0009 to 0.0165.
huihui-ai's copy is one file in the parent's float16 with twelve matrices in bfloat16: the attention outputs and
down projections of layers 23 to 28 at weight 1.00 on the output side, rows 0.016 to 0.079, exactly 0 elsewhere.
Restricted to tpls's edited matrices, its direction stands at 0.957 on the left and 0.936 on the right to
richardyoung's Heretic edit of the same parent on all 39 shared names (minimum 0.940), 0.921 to BinxNet's Heretic
pass of Google's 12B, 0.86 to 0.87 to 3MPER0RR's, prithivMLmods's and MoonRide's, 0.863 to lemuralabs's ablation over
this fine-tune and 0.49 and 0.40 to huihui-ai's edit (11 shared names); by byte range at layer 25 the leading
direction of tpls's change stands at 0.958 and 0.963 to richardyoung's on the attention output and the down
projection and at 0.488 and 0.487 to huihui-ai's. The two copies share no weight file at any revision of either
repository (the template, the processor file and `tokenizer.json` are the parent's on both), and their matrices
stand 0.0217, 0.0329 and 0.0176 apart on the layer 25 attention output, the layer 25 down projection and the layer
30 attention output, where tpls's stands 0.0183, 0.0133 and 0.0108 from richardyoung's. Both token sides carry the
instruct checkpoint's ids through the parent; tpls's differs in the four `dtype` fields the recast sets.

Why it matters: this is the first direct test since the Google originals of two tools on one checkpoint, and the
saved vectors separate them on the fine-tune as they do on the base: tpls's edit lands in the Heretic family at
0.92 to 0.96, with the scattered kept fractions that finding 18 read on richardyoung's pass of the same parent,
and huihui-ai's lands where the maker's projection of Google's checkpoint lands (finding 128), the two at 0.49 to
each other where huihui-ai's Google edit stands at 0.43 to 0.46 to the Heretic passes of Google's 12B. The coding
fine-tune now sits under five makers' edits in the census (richardyoung's, lemuralabs's, OpenYourMind's through
Paul691's duplicate, tpls's and huihui-ai's), and on tpls's copy the save precision moves more matrices than the
edit does: a measurement that reads every untouched matrix against the parent rounded
to the copy's storage type would leave the 59.

Evidence: `results/weights/tpls-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated.json`,
`results/weights/huihui-ai-Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated.json`, the two
`results/meta/` reports, the direction files under `wheat45/measurements/pair-1/` and `pair-2/` against
`nautilus16/measurements/pair-1/` (richardyoung's against the parent) and the forty other 12B measurements, the
byte-range reads listed in `docs/census-round-45.md`, the hub's histories and file listings of both repositories
at every revision, and the readings in `docs/cards/`. Round 49 measures coder3101's Heretic edits of TheDrummer's Skyfall and Magidonia (findings 143 and 144); grayarea's edits of the same two parents are pinned in round 51, so the second comparison of two tools on one checkpoint waits for that round.

## 128. One maker's projection of a fine-tune carries the direction the maker found on the base checkpoint, 1.000 on all 12 matrices and reproduced from the parent to the bfloat16 rounding, while the same maker's projection of the same fine-tuner's other 12B finds the direction again at 0.978

huihui-ai's Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated (round 45 pair 2) and
Huihui-gemma-4-12B-agentic-fable5-abliterated (pair 8, created 2026-07-11 over yuxinlu1's agentic fine-tune of
06-30) read the maker's first-generation 12B edit (round 13, measured against google/gemma-4-12B-it) on the same
twelve matrices: the attention outputs and down projections of layers 23 to 28, one direction on layers 24 to 27
with layers 23 and 28 apart from it at 0.47 to 0.49 and 0.74, weight 1.00 on the output side (left kept fraction
-0.003 to 0.005), first shares 0.991 to 0.997, rows moved 0.016 to 0.079, both clean matches to
`directional-per-layer-selected` with 0 flags and exactly 0 outside the changed set. The saved vectors of the coder
edit stand at 1.000 on the left and the right to the maker's Google edit on all 12 names, minimum 1.000. By byte
range at layer 25 the leading direction of the coder edit's change from its parent stands at 0.99998 to the leading
direction of the Google edit's change from Google's, and the parent projected along the Google edit's direction
reproduces the copy to within 0.0016 of the matrix (0.06 to 0.07 of the change), the bfloat16 rounding of the
twelve edited matrices in a float16 file; the two edits' matrices stand 0.0058 and 0.0067 apart, the distance
between the fine-tune and Google's (0.0055 and 0.0063). The agentic edit stands at 0.978 on the left and 0.982 on
the right to both (minimum 0.976); at layer 25 the parent projected along the Google direction leaves 0.32 and 0.33
of its change unexplained and projected along its own leading direction 0.07 and 0.08, so its direction was
computed again on that fine-tune. The two fine-tunes stand 0.0049 and 0.0057 apart at layer 25 and 0.0055 to 0.0087
from Google's. Both token sides are the parents' to the field.

Why it matters: findings 123 and 133 ask whether the direction a tool finds is the base's or the fine-tune's, and
for this maker's tool on Gemma 4 the answer is one of each: on one fine-tune the direction measured on the base
was applied unchanged, which a card saying "an uncensored version of" the fine-tune does not say, and on the other
it was found again and lands at 0.978, near the 0.96 to 0.99 that independent runs of one tool have read
(findings 102 and 112). A 1.000 between
edits of two different parents is a reading of a reused direction, read here to the bytes, and the pinner's
duplicate rule does not see it because no file is shared.

Evidence: `results/weights/huihui-ai-Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated.json`,
`results/weights/huihui-ai-Huihui-gemma-4-12B-agentic-fable5-abliterated.json`, the `results/meta/` reports, the
direction files under `wheat45/measurements/pair-2/` and `pair-8/` against `blueback13/measurements/pair-4/` (the
maker's Google edit), the byte-range reads listed in `docs/census-round-45.md`, and the readings in `docs/cards/`.

## 129. A merge whose card names Mistral's instruct model as its base holds that model's float8 codes read as weights, three entries in ten the raw codes and the rest about 0.136 times them, with no scale beside them and the base's quantisation declared in its configuration

SOMEHOTMEAL's Ministral-3-14B-Janus-Abliterated-V2-Base_And_GGUF (created 2026-09-13) carries mergekit's card: a
`dare_linear` merge "using mistralai/Ministral-3-14B-Instruct-2512 as a base" with jenerallee78's
Ministral-3-14B-abliterated at `weight` 0.60 and `density` 0.70, `dtype: bfloat16` and `tokenizer_source: base`.
Mistral publishes that instruct model in `float8_e4m3fn` with a `weight_scale_inv` and an `activation_scale` per
matrix. Measured against jenerallee78's edit, the parent the card names, 280 of 585 tensors changed: every query,
key, value, output, gate, up and down projection of all 40 layers at relative changes of 460 to 4,593, rows moved
489 to 4,874 times, first shares 0.0006 to 0.11; the vision tower, the projector, the token embedding, the `lm_head`
and every normalisation vector read exactly 0. By byte range on four matrices, 30.07 to 30.09 percent of each
matrix's entries equal the value the float8 checkpoint stores for that entry, the code before its scale (up to 448),
and the other 69.9 percent read about 0.136 times that code (0.133 to 0.137), the edit's own value entering at under
one part in a thousand of it; a density of 0.70 leaves three entries in ten at the base's stored value, and the
stored value mergekit read was the code without its scale (0.00025 to 0.0012 on the four matrices). The copy carries
no scale tensor and its configuration carries the instruct checkpoint's `quantization_config` (`quant_method` fp8,
static activations, `dequantize` false), with the instruct checkpoint's tokenizer and 11,913-byte template, where the
parent's are the bfloat16 release's December files. The scorer flagged 345 rules under `single-projection`; the
saved vectors stand at 0.955 to round 14's measurement of timfromhcs's duplicate of the parent against the float8
checkpoint, both differences dominated by the same codes.

Why it matters: the census refuses a float8 original at the names step (finding 37 and `docs/weights-method.md`),
and this copy shows the same format failing one step earlier, in a merge tool that read a float8 base as if its codes
were weights and wrote the result in bfloat16 under the base's quantisation declaration. The card describes its
recipe correctly and the recipe's outcome is a checkpoint whose language matrices are hundreds to thousands of times
their parent's scale, which no reading of the card would predict; the five GGUF files beside it were made from these
matrices. A pinner that compared a copy's stored magnitudes with its parent's, or a configuration's declared
quantisation with the files, would refuse the pair before a download.

Evidence: `results/weights/SOMEHOTMEAL-Ministral-3-14B-Janus-Abliterated-V2-Base_And_GGUF.json`, the
`results/meta/` report, the byte-range reads of the copy, the parent and the float8 checkpoint's codes and scales
listed in `docs/census-round-45.md`, the copy's card and configuration as published, and the reading in
`docs/cards/`.

## 130. The first edit finding 37 could not read stands on Mistral's bfloat16 release of the instruct model: its first shard is that release's by object id, its queries are byte-equal, and its writers read a rank-one projection at weight 1.00 with the rows moved under a norm-preserving card

jenerallee78's Ministral-3-14B-abliterated (created 2025-12-05), whose files timfromhcs's repository carries under
the hub's duplicate function, names mistralai/Ministral-3-14B-Instruct-2512 in its `base_model` field and grimjim's
norm-preserving biprojection as its method. Round 14 compared the duplicate with that checkpoint, which is float8,
and read only the quantisation (finding 37). Mistral also publishes mistralai/Ministral-3-14B-Instruct-2512-BF16;
at its revision `bbc49ba0` of 2025-12-04 its first shard (`a381935a`) is jenerallee78's first shard by object id,
and its configuration (`9fb1dd07`) and `tokenizer.json` (`57757562`) are jenerallee78's. By byte range the query
projections of layers 0 and 20 are byte-equal to the bfloat16 release, and the layer 20 attention output, the
layer 20 down projection and the layer 30 attention output stand 0.0185, 0.0159 and 0.0149 from it, each
difference rank one (first shares 0.993, 0.990 and 0.989) on the output side at a weight of 1.00 (left kept
fraction -0.0022 to -0.0002), with the rows moved by up to 0.0184, 0.0105 and 0.0108. Mistral's float8 checkpoint
dequantised with its own scales stands 0.027 from the bfloat16 release on every matrix read.

Why it matters: the pair finding 37 held unmeasured has a readable original, the bfloat16 release the float8 one
was cut from, and the hub's object ids name it before any download. The pin rule should follow a float8 original
to its bfloat16 sibling when the copy's shards match it. The edit itself reads as the projection grimjim's own
Nemo copy read (finding 36), with the rows unrestored to 0.018 where the card names the norm-preserving form.

Evidence: the byte-range reads of jenerallee78's edit, the bfloat16 release at `bbc49ba0` and the float8 checkpoint
listed in `docs/census-round-45.md`, the hub's file listings of the four repositories, and the reading of pair 3 in
`docs/cards/`. Round 49 reads a second edit under the same name, vprilepskii's Harbinger projection, and adds the columns: by byte range the copy is a plain projection along its own direction to within 0.0026 to 0.0031, with the rows moved as the plain projection moves them and the columns held no better on the attention outputs (finding 146).

## 131. A hub duplicate whose batch note says its files differ carries every file of its source by object id, and the source is the classic projection of one direction out of the embedding and both writers of all 40 layers of a Dolphin fine-tune, at weight 1.00

SAIFIINDUSTRIES/Abliterated-Dolphin3.0-R1-Mistral-24B (created 2026-10-03) is one commit, "Duplicate from
saukko/Abliterated-Dolphin3.0-R1-Mistral-24B"; saukko's repository (created 2025-05-26, the weights uploaded that
evening and unchanged through its head of 05-28) is present, and the duplicate's ten shards, README, configuration,
generation file, index, token files and `trainer_state.json` are saukko's at every revision by the hub's object ids.
The batch note's "its weight files differ" compares the duplicate with the parent its card names. Measured as
saukko's edit against dphn's Dolphin 3.0 R1 fine-tune of Mistral Small 24B Base 2501, 81 of 363 tensors changed:
the token embedding and the attention outputs and down projections of all 40 layers, one direction on all 81 (median
agreement 0.999998, cross-kind 0.99998), weight 1.00 on the output side of the 80 writers (left kept fraction -0.004
to 0.003) and along the hidden axis of the embedding, relative changes 0.0135 to 0.0191, rows moved 0.0017 to
0.0151, exactly 0 outside; the scorer's 66 flags are first shares of 0.987 to 0.990 under the 0.99 floor on a
bfloat16 save. By byte range the layer 20 query projection is byte-equal to the parent's and the layer 20 writers
stand 0.0191 and 0.0160 from them; the parent stands 0.376 to 0.509 from Mistral's base on the three matrices read,
a full fine-tune whose difference has no leading component (first shares 0.0018 to 0.0048). The direction stands at
0.448 to venkycs's projection of Mistral Small 24B Instruct 2501 and 0.20 to huihui-ai's projection of Mistral Small
3.2. The card is saukko's, mlabonne's article and FailSpy's abliterator as sources, with no layer or weight.

Why it matters: this is the second batch note in the second-generation rounds to call a hub duplicate's files
different from its source (Justbackup's in finding 121), both times because the comparison reached the parent and not the
source the first commit names, so the duplicate rule of finding 38 has to read the named source's listing at every
revision before the note is written. The edit is the textbook form the method's sources describe, read cleanly
over a fine-tune that moved the base by 0.38 to 0.51 of its norm on the matrices read, and the classic projection's direction on Mistral
Small stands at 0.45 between two parents a full fine-tune apart.

Evidence: `results/weights/SAIFIINDUSTRIES-Abliterated-Dolphin3.0-R1-Mistral-24B.json`, the `results/meta/` report,
the direction file under `wheat45/measurements/pair-4/` against `nautilus16/measurements/pair-7/` (venkycs's) and
the other Mistral Small measurements, the hub's file listings of saukko's repository at its five revisions, the
byte-range reads listed in `docs/census-round-45.md`, and the reading in `docs/cards/`.

## 132. A commercial uncensored release is its parent's ten shards by object id, the census's first copy with no tensor changed, and the uncensoring it carries is the parent's fine-tune of Mistral Small 24B Instruct, with no leading component

AskVenice/venice-uncensored (created 2025-11-25, the weights uploaded on 11-26 "via LFS") carries Venice.ai's card,
"Venice Uncensored (Dolphin Mistral 24B)", "a special edition of the renowned Dolphin series" made with the Dolphin
team, with the parent's system prompt and both Mistral's instruct model and dphn's Dolphin-Mistral-24B-Venice-Edition
in its `base_model` field. Its ten shards (`65828eac` to `2ca2d9db`) are the Venice Edition's from its upload of
2025-06-12 to the pinned revision of 09-08 by object id; the configuration, generation file, index and token
configuration are re-saves with other object ids and the metadata comparison finds no field that differs. Measured
against the Venice Edition, 0 of 363 tensors changed, the first empty changed set in the census, with one flag (the
nearest entry's request for a changed writer). By byte range the Venice Edition itself stands 0.0056, 0.0043 and
0.0035 from Mistral Small 24B Instruct 2501 on the layer 20 attention output, query projection and down projection,
the difference spread over many components (first shares 0.082, 0.29 and 0.22), the shape of training; its leading
direction stands at 0.35 and 0.073 to venkycs's projection of the same instruct model on the attention output and
the down projection. The instruct model stands 0.034 to 0.038 from the base on those matrices, so the edition moved
the instruct model by about a tenth of what the instruct tuning moved the base. The Venice Edition was replaced on
the hub by a version 1.2 with a vision tower on 2026-04-16; the copy carries the first version.

Why it matters: a commercial platform's uncensored model is a fine-tune, read as training on every
matrix sampled with no direction to project, and the copy that carries the platform's name is that fine-tune's file
under a second name. The census reads it as what its card says, and the pinner's duplicate rule would have caught it
by object id before the download had it compared the copy's shards with the parent's.

Evidence: `results/weights/AskVenice-venice-uncensored.json`, the `results/meta/` report, the hub's file listings of
both repositories at every revision, the byte-range reads listed in `docs/census-round-45.md`, and the reading in
`docs/cards/`.

## 133. A Heretic pass on Mistral Nemo Instruct itself reads its kernel table to the layer and stands at 0.90 and 0.85 to one maker's passes on two Nemo merges and at 0.39 to 0.57 to that maker's passes on Nemo fine-tunes, under a template the tool's renderer cannot read

0xA50C1A1's Mistral-Nemo-Instruct-2407-Heretic-v2 (created 2026-03-13) carries Heretic 1.2.0's table over
unsloth's re-upload of Nemo Instruct, whose five shards are Mistral's by object id: `direction_index` 18.46,
`attn.o_proj` 1.29 at 29.40 and 1.08 at a distance of 18.39, `mlp.down_proj` 1.47 at 24.17 and 1.41 at a distance of
19.35, a KL divergence of 0.0574 and 4 refusals in 100 against 88. Measured against the parent, 63 of 363 tensors
changed, the attention outputs of layers 12 to 39 and the down projections of 5 to 39, the kernels' reaches to the
layer (11.01 and 4.82), exactly 0 outside. One direction serves every layer and both writers (median agreement
0.997, cross-kind 0.894, the scorer's one flag), on the output side: one minus the left kept fraction on the down
projections reads 1.29 at layer 5, 0.83 at 10 and 11 and 1.39 at 19 to 24, holding at 1.29 to 1.38 to layer 39, under
the printed 1.41 to 1.47; the attention outputs scatter from 0.09 to 1.06, finding 46's shape on Nemo Instruct
itself. Rows moved 0.0038 to 0.0163. The direction stands at 0.898 to Sorihon's pass on DavidAU's DARKNESS merge (63
names, minimum 0.891), 0.854 to the pass on the NemoMix merge, 0.574 to the pass on anthracite-org's Magnum
fine-tune of Nemo Instruct, 0.429, 0.395 and 0.389 to the three per-layer passes on Celeste, EtherealAurora and
Dans, 0.468 to grimjim's block-wise pass of Nemo Instruct and 0.107 to DuoNeural's projection. The template at the
revision measured carries a commit of 04-08 that wraps each assistant turn in `{% generation %}` and
`{% endgeneration %}` for a trainer's assistant mask; the metadata tool's sandboxed renderer fails on the tag, and
rendered at home through transformers it gives the parent's text with one newline added after the final `</s>`.

Why it matters: finding 123 read one maker's six passes on six Nemo fine-tunes at 0.33 to 0.90 to each other and
asked whether the direction is the base's or the fine-tune's. The pass on the base lands nearest the two
shared-direction passes on merges (0.90 and 0.85) and 0.57 to the third, and at 0.39 to 0.43 to the three
per-layer passes, so on Nemo the agreement follows the method at least as much as the parent: a shared direction
found on Nemo Instruct and a shared direction found on a Nemo merge stand closer than either does to a per-layer
pass on a fine-tune of Nemo Instruct. The template is a training-ready edit the token-side reading of finding 126
did not meet, and it renders differently by one newline.

Evidence: `results/weights/0xA50C1A1-Mistral-Nemo-Instruct-2407-Heretic-v2.json`, the `results/meta/` report, the
direction file under `wheat45/measurements/pair-6/` against `wheat43/measurements/pair-3/` to `pair-8/` and
`blueback13/measurements/pair-6/` and `pair-7/`, the byte-range reads and the home render listed in
`docs/census-round-45.md`, the hub's histories of the copy and of unsloth's and Mistral's repositories, and the
reading in `docs/cards/`.

## 134. One maker's fourth second-generation search, on a 31B fine-tune, reads its window one layer short with one layer rewritten under the threshold, input-side weights to 2.66 and no component amplified, at 0.78 to 0.88 to the maker's four other 31B searches

llmfan46's Gemma-4-Garnet-V2-31B-it-ultra-uncensored-heretic (created 2026-04-25) is Heretic 1.2.0's arbitrary-rank
branch over ConicCat's GarnetV2 fine-tune of the 31B, a merged rank-64 adapter on every projection whose layers stand
0.022 to 0.035 from Google's on the four matrices read: `start_layer_index` 25, `end_layer_index` 46,
`preserve_good_behavior_weight` 0.4482, `steer_bad_behavior_weight` 0.0002, `overcorrect_relative_weight` 1.0104,
`neighbor_count` 10, `attn.o_proj` the one target, a KL divergence of 0.0167 and 4 refusals in 100 against 99.
Measured against the fine-tune, 20 of 1,188 tensors changed, the attention outputs of layers 25 to 28 and 30 to 45;
layer 29 moved by 0.000116 (1.9 percent of its entries by at most 0.00098), the largest relative change outside the
changed set, and layer 46 is untouched. Every edit is on the input side: one minus the right kept fraction reads
1.31 to 2.66 (2.66 at layer 42), the left side 0.04 to 0.42, one direction per matrix, first shares 0.917 to 0.981,
relative changes 0.0101 to 0.0367, rows moved 0.0003 to 0.0377; no kept fraction is above 1, so no component is
amplified as on the maker's Queen and MeroMero edits (finding 120). The left directions stand at 0.875 to the maker's
QAT search, 0.807 and 0.802 to the MeroMero and Queen edits, 0.781 to the maker's April edit, 0.804 and 0.850 to
coder3101's two, 0.79 and 0.78 to MoonRide's two, 0.55 to Jim-darby's Japanese-weighted search and 0.15 or less to
every kernel pass and projection. By byte range the layer 42 attention output is 0.0367 from the parent's and 0.047
from the maker's April edit and coder3101's. The copy's 17,344-byte template, the maker's own, went in by delete and
re-upload on 05-05, ten days after the weights and three minutes after the same file went onto the maker's April
repository, after Google's 04-28 revision on 05-04 the same way; it renders the fixed conversation as the parent's
Google revision of 04-10 does.

Why it matters: the maker's three second-generation searches on the 31B now stand at 0.78 to 0.99 to the maker's
April edit (0.993 for Queen, 0.89 for MeroMero, 0.78 for this one), and the window ends one layer short of `end_layer_index` as on
findings 124 and 125. "Ultra" is in the names of six of the maker's repositories in the census and reads no
amplification here, so the multiplied components of finding 120 are those two edits' and not the name's. The
template history is the maker's-template case a fourth time, by the same two-step replacement on the same days as
on the Queen edit.

Evidence: `results/weights/llmfan46-Gemma-4-Garnet-V2-31B-it-ultra-uncensored-heretic.json`, the `results/meta/`
report, the direction file under `wheat45/measurements/pair-7/` against `blueback12/measurements/pair-1/` (the
maker's April edit) and the thirty-three other 31B measurements, the byte-range reads listed in
`docs/census-round-45.md`, the template histories of the copy and the maker's April repository, the parent's
adapter configuration, and the reading in `docs/cards/`. Round 49 adds the maker's search on ConicCat's first Garnet fine-tune, a sibling training of Google's 31B, at 0.883 to this search with input-side weights to 3.44 and no component amplified, under the same 17,344-byte template put in 24 seconds after this copy's (finding 147).

## 135. A Heretic 1.1 pass on Zephyr, the census's first copy on a Mistral 7B v0.1 fine-tune, reads both kernels of its published record to the third decimal on all 27 matrices with nothing else moved, and its direction stands at 0.48 to 0.63 to the Mistral 7B Instruct edits

richardyoung's zephyr-7b-beta-abliterated (created 2025-12-15) carries a card naming Heretic v1.1 (2 refusals in
100, a KL divergence of 0.076) and the run's `abliteration_info.json`: 50 trials, the best trial 8, one direction
per layer, an `attn.o_proj` kernel with a maximum weight of 1.3371 at position 23.834 falling to 0.2024 at a
distance of 4.727, and an `mlp.down_proj` kernel with a maximum of 1.4981 at 18.791 falling to 1.1473 at a distance
of 9.093. Measured on Wheat in round 47 against HuggingFaceH4/zephyr-7b-beta, the preference-tuned fine-tune of
mistralai/Mistral-7B-v0.1 its card names, 27 of 291 tensors changed: the down projections of layers 10 to 27 and
the attention outputs of 20 to 28, the two kernels' reaches to the layer, with every other tensor exactly 0. The two
writers of a layer agree at 0.9996 to 1.0000 and the layers at a median of 0.59, the per-layer scope the record
names. Every edit is on the output side, and one minus the left kept fraction reads 1.158 at layer 10 rising to
1.490 at 19 and back to 1.180 at 27 on the down projections and 0.414 at 20 rising to 1.297 at 24 and back to 0.335
at 28 on the attention outputs; the record's two linear kernels give the same weights within 0.0011 on all 18 down
projections and within 0.0029 on all 9 attention outputs. First shares run 0.956 to 0.997 and the rows move by
0.0072 to 0.0325 under a card that claims no norm. By byte range the copy's layer 5 query projection is Zephyr's
bytes and its layer 24 attention output and layer 19 down projection are rank-one differences (first shares 0.9949
and 0.9961); Zephyr stands 0.034 to 0.044 from Mistral 7B v0.1 on the three matrices read, with no leading
component. No measurement in the census stands on Zephyr or on Mistral 7B v0.1, so the copy has no family; the
Mistral 7B Instruct measurements share its hidden size and layer count, and against their saved vectors the
direction stands at 0.631 to evolveon's projection of v0.3, 0.627 to the maker's own v0.3 edit, 0.559 and 0.546 to
DogOnKeyboard's and paoloronco's Heretic passes of v0.3, 0.485 to 3MPER0RR's edit, 0.357 to wangzhang's edit of the
circuit-breaker model of finding 136 and 0.047 to the maker's OBLITERATUS copy of v0.2. The token ids are Zephyr's
on both sides (`bos_token_id` 1, `eos_token_id` 2, `pad_token_id` 2).

Why it matters: this is the first copy the census has read outside the Gemma and Mistral instruct lines, on a
community fine-tune of the pretrained Mistral 7B, and the method reads it as it reads the instruct lines: the
windows, the side, the per-layer scope and the weights are the record's, to the third decimal, as finding 46 read
the same tool's kernels on two Mistral instruct bases. The published record is what makes the reading exact; a
pass with no record reads its shape and not its numbers (finding 137). The directions stand at 0.48 to 0.63 to the
instruct edits of a later Mistral 7B, which is the cross-checkpoint level findings 123 and 133 read between Nemo
fine-tunes, so the refusal direction a tool finds on Zephyr is near the one found on Mistral's own instruct models
without being the same.

Evidence: `results/weights/richardyoung-zephyr-7b-beta-abliterated.json`, the `results/meta/` report, the
repository's `abliteration_info.json`, the direction file under `wheat47/measurements/pair-1/` against
`blueback7/measurements/pair-4/`, `pair-5/`, `pair-7/` and `pair-8/`, `blueback14/measurements/pair-1/`,
`blueback26/measurements/pair-2/` and `nautilus20/measurements/pair-8/`, the byte-range reads listed in
`docs/census-round-47.md`, and the reading in `docs/cards/`.

## 136. The census's first edit of a circuit-breaker model removes the breaker instead of ablating through it: 118 of the 200 matrices changed against the parent are Mistral 7B Instruct v0.2's bytes with the rank-16 adapter stripped, and the other 82 carry one direction at weights to 5.62

GraySwanAI/Mistral-7B-Instruct-RR is Mistral 7B Instruct with circuit breakers trained in by representation
rerouting, a loss that sends the hidden states of harmful requests away from the paths that would answer them; its
configuration names mistralai/Mistral-7B-Instruct-v0.2 and its card names no base. wangzhang's
Mistral-7B-Instruct-RR-Abliterated (created 2026-04-13, the weights replaced on 04-14 under "v2: full LoRA strip +
minimal direct abliteration") describes two steps: the circuit breaker read as "a rank-16 LoRA delta" on that
instruct model and subtracted whole, then abliterix's direct mode with one mean direction, a linear decay kernel
and a strength range of 1.5 to 6.0, 12 refusals in 100 against the parent's 69 at a KL divergence of 0.042.
Measured on Wheat in round 47 against the parent its card names, 200 of 291 tensors changed (every query, key,
value and output projection, the gate and up projections of layers 0 to 20 and the down projections of 0 to 20 and
23 to 31), with 215 flags. By byte range against the instruct model at `63a8b081`, the parent is that model on
layers 21 to 31 byte for byte and that model plus an adapter on all seven linear maps of layers 0 to 20, sixteen
components carrying 0.985 to 0.990 of the difference on the three matrices read. The copy equals the instruct
model on the first 2,000,000 bytes of 142 of its 224 linear maps (every gate and up projection, the down
projections of 0 to 22, the queries of 0 to 17, the keys and values of 0 to 15 and the attention outputs of 0 to
4), and the layer 10 gate and query projections read whole are byte-equal. So 118 of the 200 changed matrices are
the strip alone, the adapter removed to the last bit, and 82 carry the edit: one direction on the output side of
the attention outputs of layers 5 to 31 and the down projections of 23 to 31 and on the input side of the keys and
values of 16 to 31 (1.000 between kinds), with the queries of 18 to 31 edited on their output side along a
direction of their own. Read on layers 21 to 31, where the parent is the instruct model, the weights are 5.62 at
layer 22 on the attention outputs falling by 0.245 to 0.25 a layer to 3.57 at 31, 1.84 to 1.95 on the down
projections, 1.88 to 2.76 on the keys and values and 2.49 to 2.99 on the queries, first shares 0.997 to 0.9997, and
the attention outputs' rows move by 0.048 to 0.178. Against the instruct model the layer 10 and 25 attention
outputs and the layer 25 query projection stand 0.0447, 0.0811 and 0.0463 away, each difference rank one (0.9987
to 0.9996). On the attention outputs the direction stands at 0.733 to 3MPER0RR's edit of Mistral 7B Instruct v0.3,
0.55 to 0.67 to four other v0.3 edits, 0.397 to the Zephyr pass of finding 135 and 0.012 to richardyoung's
OBLITERATUS copy of v0.2, the one other edit of this instruct model in the census.

Why it matters: a defence trained into the representations is supposed to withstand an edit along one refusal
direction, and this copy did not edit through it; it took the defence out first, because the defence was an
adapter on a public checkpoint and the checkpoint is public. The residue of the defence in the copy is none at all:
where the adapter reached and the edit did not, the copy is the instruct model's bytes, and where the edit reached,
the change from the instruct model is the same rank-one projection the census reads on instruct parents, at
weights well above them. The measurement against the parent the card names reads the removal as most of the
change and 215 flags, and only the pairing with the checkpoint underneath reads the edit, so for a parent that is
a defence over a publisher's checkpoint the pin has to carry that checkpoint as well. The weights do not say
whether the circuit breaker would have held against an edit made through it; they say this copy removed it first.

Evidence: `results/weights/wangzhang-Mistral-7B-Instruct-RR-Abliterated.json`, the `results/meta/` report, the
direction file under `wheat47/measurements/pair-2/` against the Mistral 7B measurements under `blueback7/`,
`blueback14/`, `blueback26/` and `nautilus20/`, the byte-range reads of the copy, the parent and
mistralai/Mistral-7B-Instruct-v0.2 listed in `docs/census-round-47.md`, the copy's card and commit history, and the
reading in `docs/cards/`.

## 137. A text-only re-save of Mistral Small 3.2 is Mistral's checkpoint by byte range, and one maker's second MPOA pass on it reads one shared direction on both writers in a kernel's shape with the rows in and under the band, at 0.856 to the maker's Magistral pass

anthracite-core/Mistral-Small-3.2-24B-Instruct-2506-Text-Only (created 2025-06-21) is mistralai's Mistral Small
3.2 saved as `MistralForCausalLM` with the vision tower and projector left out, and by byte range its layer 20
attention output, layer 5 query projection and token embedding are byte-equal to the language model of
mistralai/Mistral-Small-3.2-24B-Instruct-2506 at `95a6d26c`. grayarea's Text-Only-Heretic-v1.2 (created
2026-03-29) carries a card naming Heretic v1.2.0 with MPOA, full row renormalization and a winsorization quantile of
0.997, 0 refusals in 108 against 96 at a KL divergence of 0.0138, and no parameter table. Measured on Wheat in round
47 against the re-save, 61 of 363 tensors changed: the down projections of layers 8 to 39 and the attention outputs
of 11 to 39, exactly 0 outside. One direction serves every layer and both writers (median agreement 0.999,
cross-kind 0.942), on the output side, and one minus the left kept fraction draws a kernel's shape that the card
does not print: 0.69 at layer 8 rising to 1.27 at 31 and back to 1.09 at 39 on the down projections, and 0.68 at
11 rising to 1.25 at 26 and back to 0.74 at 39 on the attention outputs, with one break at layer 27. First shares
run 0.979 to 0.994 (26 flags under the 0.99 floor), relative changes 0.0102 to 0.0202, and the rows move by 0.0023
to 0.0078. The direction stands at 0.856 on the left and 0.857 on the right to the maker's pass on Magistral Small
2509 (59 names, minimum 0.854), 0.628 to saukko's projection of a Dolphin fine-tune of Mistral Small 24B, 0.533 to
venkycs's projection of Mistral Small 24B Instruct 2501, 0.235 to huihui-ai's projection of Mistral Small 3.2 and
0.06 or less to llmfan46's three arbitrary-rank searches on Mistral Small 3.2 and Magistral.

Why it matters: the parent is a publisher's checkpoint under another name, which the census can only see by byte
range, so the pair is in effect measured against Mistral's original, as unsloth's re-upload of Nemo Instruct was in
round 45. The maker's two v1.2 passes read alike across two parents a fine-tune apart: one shared direction on both
writers, a kernel's shape on the down projections, the rows in and under finding 22's band under the words "full
row renormalization", and the two directions at 0.856. Magistral Small 2509 is a reasoning fine-tune of Mistral Small
3.2, and 0.856 sits inside the 0.78 to 0.88 at which one maker's searches stand across 31B fine-tunes (finding 134).

Evidence: `results/weights/grayarea-Mistral-Small-3.2-24B-Instruct-2506-Text-Only-Heretic-v1.2.json`, the
`results/meta/` report, the direction file under `wheat47/measurements/pair-3/` against
`nautilus18/measurements/pair-8/` (the Magistral pass) and the other Mistral Small measurements, the byte-range reads
listed in `docs/census-round-47.md`, and the reading in `docs/cards/`. Round 49 reads coder3101's Skyfall pass, the census's third shared-direction pass on the Mistral Small hidden size, at 0.817 to this pass and 0.792 to the maker's Magistral pass (finding 143).

## 138. A role-play adapter over the maker's unmeasured Gemma 3 4B null-space edit reads training on every linear map at 0.10 to 0.71 percent with no direction, the training at the level of chance along the published refusal direction, and the edit under it rank one by byte range

jwest33's gemma-3-4b-null-space-abliterated-RP-writer (created 2026-01-09) is a rank-8 adapter on all seven
projections of the language model, 200 steps of response-only training on a filtered LimaRP subset, merged over
the maker's null-space projection of google/gemma-3-4b-it, whose card names the toolkit finding 94 read on the 12B.
The copy carries the parent's `abliteration_config.json`, `refusal_directions.pt` and `null_space_projectors.pt` by
object id. Measured on Wheat in round 47 against that parent, which the census has not measured against Google, 233
of 883 tensors changed: every query, value, attention output, gate, up and down projection of the 34 layers and 29
of the key projections, the other five keys just under the threshold (0.0009 to 0.00099), the vision tower, the
embedding and the normalisation vectors exactly 0. There is no direction: first shares 0.17 to 0.86, both kept
fractions 0.95 to 1.02, relative changes 0.0010 to 0.0071. Against the parent's published mean refusal direction the
training's leading vectors stand at 0.083 or less on every matrix (median 0.009 to 0.017 by kind, the level of a
random direction in 2,560 dimensions), and by byte range at layer 20 the training puts 0.00017 to 0.00036 of its
change along that direction, under the 0.00039 a random direction would take. The edit under it, read by byte range
against Google's checkpoint: the layer 20 attention output, down and query projections stand 0.0152 to 0.0160 from
Google's, each difference rank one (first shares 0.990 to 0.992) along one direction at 0.782 to the published mean
direction, and the token embedding stands 0.0220 from Google's along the mean direction itself (1.000).

Why it matters: this is the third training pass the census has read over a first edit (finding 121) and the first
whose parent publishes its own direction, so whether the training moved along the direction the edit removed can be
read on this pair: the adapter's change is spread over every map with no leading component and has nothing along
that direction. The parent's edit reads as the
12B's did, one direction on every linear map and the embedding, with the layers' direction a constrained form of
the mean (0.782) and the embedding's the mean itself; the pinner should queue the parent against Google.

Evidence: `results/weights/jwest33-gemma-3-4b-null-space-abliterated-RP-writer.json`, the `results/meta/` report,
the repository's `refusal_directions.pt` read as tensors at home, the direction file under
`wheat47/measurements/pair-4/`, the byte-range reads listed in `docs/census-round-47.md`, and the reading in
`docs/cards/`.

## 139. An arbitrary-rank pass over an expert-pruned 21B-A4B reads the card's window to the layer with the rows in the band and every expert untouched, at 0.898 to the maker's edit of the unpruned 26B-A4B, while the maker's pass over the 19B pruning stands at 0.35 to 0.78 to it by byte range

0xSero/Gemma-4-21B (created 2026-04-05; coder3101's card names it 0xSero/gemma-4-21b-a4b-it-REAP, a name the hub
resolves to this repository) is google/gemma-4-26b-a4b-it with 25 of the 128 experts of each layer removed by Cerebras's
router-weighted expert activation pruning, and by byte range its attention outputs are Google's bytes on the five
layers read. coder3101's gemma-4-21b-a4b-it-REAP-heretic (created 04-09) carries Heretic 1.2.0's arbitrary-rank
table with row-norm preservation: `start_layer_index` 11, `end_layer_index` 30, `overcorrect_relative_weight`
0.2042, `neighbor_count` 15, 14 refusals in 100 against 100 at a KL divergence of 0.0605. Measured on Wheat in round
47 against the pruned checkpoint, 19 of 1,013 tensors changed, the attention outputs of layers 11 to 29, the card's
window to the layer, and nothing else, the 103 experts of every layer included. Every edit is on the input side,
one minus the right kept fraction 0.59 to 1.34, one direction per matrix, first shares 0.391 to 0.919, and the rows
move by 0.0061 to 0.0077 on every matrix. The direction stands at 0.898 to the maker's own edit of the unpruned
26B-A4B (19 names, minimum 0.646) and to SassyDiffusion's search, 0.890 to llmfan46's MeroMero 26B-A4B edit, 0.86 to
llmfan46's and Vortex5's edits and 0.20 or less to every kernel pass and projection. The maker's edit of the 30
percent pruning, coder3101/gemma-4-19b-a4b-it-REAP-heretic (made two hours earlier, window 14 to 25,
`neighbor_count` 7), is on the hub and is not measured in the census; by byte range it changes the attention
outputs of layers 17 and 19 to 21 by rank-one differences of 0.0157 to 0.0576 from Google's, rewrites the rest of
its window by 0.0011 to 0.0017 with no leading component and leaves layers 12 and 27 Google's bytes, and on the
four layers both edits change their leading directions stand at 0.35 to 0.65 on the left and 0.55 to 0.78 on the
right.

Why it matters: removing a fifth of the experts changes nothing the arbitrary-rank branch reads, since the branch
edits the attention outputs and those are Google's bytes; the pass on the pruned checkpoint lands in the 26B-A4B
family as a pass on the original would. The two prunings carry the same attention weights, yet the maker's two
searches on them, with two windows and two neighbour counts, agree at 0.35 to 0.78 where each would sit near 0.9 to
the family, so on this method the search's own settings move the direction more than the checkpoint underneath.

Evidence: `results/weights/coder3101-gemma-4-21b-a4b-it-REAP-heretic.json`, the `results/meta/` report, the
direction file under `wheat47/measurements/pair-5/` against `blueback12/measurements/pair-6/` (the maker's 26B-A4B
edit) and the other 26B-A4B measurements, the byte-range reads of the two edits, the two prunings and Google's
checkpoint listed in `docs/census-round-47.md`, the cards of both edits, and the reading in `docs/cards/`.

## 140. One maker's fifth and sixth second-generation searches, on two 31B merges, read the input side at weights to 3.17 and 2.20 with no component amplified and the windows inside the cards' with traces, at 0.89 to 0.91 and 0.60 to 0.80 to the maker's other 31B edits, under the maker's template with Windows line endings

llmfan46's Gemma-4-Gembrain-31B-it-uncensored-heretic (created 2026-05-17) is Heretic 1.2.0's arbitrary-rank
branch over Nimbz's Gembrain 31B, an `arcee_fusion` merge published as 27 float32 shards under a configuration that
declares bfloat16 (`start_layer_index` 5, `end_layer_index` 60, `preserve_good_behavior_weight` 0.9776, 13 refusals
in 100 against 99 at a KL divergence of 0.0186), and Gemma-4-Harmonia-31B-uncensored-heretic (created 05-27) is
the same branch over virtuous7373's Harmonia 31B, a three-stage merge (`start_layer_index` 14, `end_layer_index` 55,
`preserve_good_behavior_weight` 0.7754, 9 refusals in 100 against 97 at a KL divergence of 0.0047). Measured on
Wheat in round 47 against the merges, the Gembrain copy changes 31 attention outputs of layers 21 to 58 and leaves
thirteen more of the window as traces of 0.00004 to 0.000176, its bfloat16 save moving 333 other tensors of the
float32 parent by at most 0.0000012; the Harmonia copy changes 22 attention outputs of layers 26 to 54 and leaves
the window's other nineteen as traces of 0.0000005 to 0.000234, with layers 0 to 13 and 55 to 59 exactly 0. Every
edit is on the input side, one minus the right kept fraction 0.24 to 3.17 and 0.22 to 2.20, with no kept fraction
above 1 on either side, and the rows move by 0.0007 to 0.0355 and 0.0008 to 0.0215. The Gembrain direction stands
at 0.908 to the maker's Queen edit, 0.896 to coder3101's 31B edit, 0.888 to the MeroMero edit and 0.886 to the
maker's April edit; the Harmonia direction at 0.797 to the maker's QAT search, 0.713 to the Garnet search, 0.670 to
the MeroMero edit and 0.602 to the April edit; the two at 0.731 to each other, and both at 0.21 or less to every
kernel pass and projection. Both copies carry a 17,708-byte template that is the maker's 17,344-byte file of
finding 134 with Windows line endings on its 364 lines; it went onto the maker's April 31B repository on 05-18 and
was replaced there fourteen minutes later.

Why it matters: the maker's second-generation searches on the 31B now number five, and none since Queen and
MeroMero (finding 120) reads an amplified component, so the multiplied components stay those two edits'. The windows
read the branch's selection inside the card's range, with the traces of the Garnet search of finding 134, and the
Harmonia window is the card's to the layer. The Gembrain direction lands in the 31B family at 0.89 to 0.91, and the
Harmonia direction lands further out, 0.60 to 0.80, over a parent that already carries the maker's edits (finding
141). The template is the maker's-template case a fifth and sixth time, its line endings the only change.

Evidence: `results/weights/llmfan46-Gemma-4-Gembrain-31B-it-uncensored-heretic.json`,
`results/weights/llmfan46-Gemma-4-Harmonia-31B-uncensored-heretic.json`, the two `results/meta/` reports, the
direction files under `wheat47/measurements/pair-6/` and `pair-7/` against the thirty-seven other 31B measurements,
the template histories of both copies, their parents and the maker's April repository, and the readings in
`docs/cards/`. Round 49 reads Windows line endings on a third llmfan46 template, the parent's own on the PaintedFantasy search (2,722 bytes against 2,671), and the maker's 17,344-byte file a seventh time on the first Garnet search (findings 145 and 147).

## 141. A merge that takes one maker's edit as a source carries that edit's direction as its leading component, at 0.88 and 0.93 to it, and the same maker's search over the merge finds a direction at 0.73 to the edit it carries

virtuous7373's Harmonia 31B publishes its `mergekit_config.yml`: an `actmat` merge on the maker's unmeasured Ortenzya
edit with LatitudeGames's Equinox, Lambent's Fabled and an intermediate `cabs` merge of llmfan46's MeroMero edit
(weight 0.6, finding 120) and llmfan46's Gembrain edit (weight 0.4, finding 140) over a `nullspace` merge of
ConicCat's GarnetV2 onto Google's pretrained 31B. By byte range the merge stands 0.0818 and 0.0698 from Google's
instruct checkpoint on the layer 40 and 48 attention outputs, each difference with a leading component (first
shares 0.41 and 0.20) whose left vector stands at 0.876 and 0.930 to the leading direction of the Gembrain edit's
change at the same layer; on the layer 10 attention output, where that edit left only a trace, the merge stands 0.0609 from
Google's with no leading component (0.053). llmfan46's Harmonia search, measured against the merge in round 47,
changes the layer 40 and 48 attention outputs by 0.0185 and 0.0655 (first shares 0.939 and 0.976) and leaves layer
10 byte-equal; its leading direction stands at 0.32 and 0.82 to the merge's leading component and at 0.38 and 0.69
on the left and 0.79 and 0.77 on the right to the Gembrain edit's, and its saved vectors stand at 0.731 to the
Gembrain edit's on 20 names and 0.670 to the MeroMero edit's on 15.

Why it matters: a community merge can carry an abliteration as a direction in its weights without the word in its
name or card, and the bytes read it there, the Gembrain edit's direction surviving a weight of 0.4 inside one merge
and another merge over that as the largest single component of the difference from Google. The maker then searched
again on a parent that had already lost part of what the search looks for, and found a direction near the one it
carried at layer 48 and away from it at layer 40. A pinner that reads a parent's merge configuration for census makers' edits would mark such a pair before
the download, and a measurement of the merge against Google would read the carried edit directly.

Evidence: the parent's `mergekit_config.yml` as published, the byte-range reads of the merge, Google's 31B, the
Gembrain copy, its parent and the Harmonia copy listed in `docs/census-round-47.md`, the direction files under
`wheat47/measurements/pair-6/` and `pair-7/` and `nautilus42/measurements/pair-2/`, and the readings in
`docs/cards/`.

## 142. A fine-tune merged onto a measured Heretic edit leaves the edit in place: the same adapter merged onto Google's 31B and onto coder3101's edit changes both alike to a cosine of 0.994 and 0.997, moves the edit by 0.00002 of itself, and carries no direction

nbeerbower's Gemma4-Gutenberg-31B-Heretic (created 2026-06-16, the weights uploaded at 16:57Z) carries a card for an
ORPO fine-tune toward literary prose, a rank-64 adapter on the text decoder trained for 454 steps on 14,816
preference pairs and merged, "the same Gutenberg ORPO adapter merged in" as the maker's Gemma4-Gutenberg-31B, which
went onto google/gemma-4-31B-it at 16:33Z. Its parent is coder3101's arbitrary-rank Heretic edit of the 31B at
`9a1c7f5d`, which the census measured against Google in round 12 with the same two shards (58 attention outputs of
layers 1 to 58, 23 of them residues, finding 22). Measured on Wheat in round 47 against that edit, 360 of 1,188
tensors changed, the query, key, value, attention output, gate, up and down projections of the text decoder at
0.0010 to 0.0077, with 50 more linear maps just under the threshold and the vision tower, the embedding and the
normalisation vectors exactly 0; there is no direction (first shares 0.04 to 0.95, both kept fractions 0.90 to
1.12), and the saved vectors stand at 0.028 or less to every 31B edit on the attention outputs and 0.010 to
coder3101's. By byte range on the layer 30 and 45 attention outputs, where coder3101's edit stands 0.0312 and 0.0343
from Google's at first shares of 0.961 and 0.967, the copy stands 0.00172 and 0.00192 from coder3101's and the
standard Gutenberg 0.00172 and 0.00192 from Google's, and the two changes agree at a cosine of 0.994 and 0.997; the
copy's change along the edit is 0.00000 and 0.00002 of the edit, and the copy's difference from Google's stands at
0.998 to the edit's. On the layer 30 query projection, where coder3101's matrix is Google's bytes, the two
Gutenberg copies are byte-equal. The template and tokenizer are coder3101's by object id and the token ids the
instruct checkpoint's.

Why it matters: the usual second-generation order is an edit over a fine-tune; here a fine-tune was laid over an
edit the census had measured, the case findings 95 and 121 could only approach, and the reading is direct: the
adapter is one change computed once and added to two bases, and on the edited base it neither undoes the edit nor
moves along it, so the copy is coder3101's edit plus the maker's literary training, each readable apart. A training
pass over an edit is the shape of a copy that might put refusals back by fine-tuning, and this one puts nothing back
along the edited direction, which the saved vectors read before the bytes confirmed it.

Evidence: `results/weights/nbeerbower-Gemma4-Gutenberg-31B-Heretic.json`, the `results/meta/` report,
`results/weights/coder3101-gemma-4-31B-it-heretic.json`, the direction file under `wheat47/measurements/pair-8/`
against `blueback12/measurements/pair-2/` and the thirty-six other 31B measurements, the byte-range reads of the
copy, coder3101's edit, the standard Gutenberg and Google's 31B listed in `docs/census-round-47.md`, the cards of
both Gutenberg copies, and the reading in `docs/cards/`. Round 49 reads the case twice more: Tetratype's antislop pass leaves coder3101's measured 26B-A4B edit in place, moving it along itself by at most 0.00015 of itself, and DavidAU's second reasoning pass moves coder3101's 27B edit back by less than one percent of itself (findings 148 and 149).

## 143. A Heretic 1.2 pass over a depth-upscaled Magistral Small reads one shared direction over the printed kernels' reaches, and the printed attention height only on the fourteen inserted layers whose output projections the upscale left near zero

TheDrummer's Skyfall-31B-v4.2 (weights 2026-02-13) is a 54-layer upscale of mistralai/Magistral-Small-2509, which
has 40. Its own tensors say how: the forty original layers stand on Magistral's in order (the layer 5 query
projection 0.0153 from Magistral's layer 5, layers 30, 33, 48 and 53 0.019 to 0.024 from Magistral's 28, 29, 34 and
39), and seven pairs of layers are inserted after layers 27, 30, 33, 36, 39, 42 and 45, each pair copying the inputs
of the layer before it (layer 28's query projection 0.036 from Magistral's layer 27, layers 28 and 29 0.0035 apart)
and carrying attention outputs of norm 0.23 to 0.41 and down projections of norm 1.07 to 1.15, against 9.9 to 20.6 and
36.8 to 47.3 on the forty others. coder3101's Skyfall-31B-v4.2-heretic (created 2026-06-02) carries Heretic v1.2.0's
kernel table with a fractional `direction_index` of 21.36, an attention-output kernel flat at 1.48 around 36.76 over a
distance of 27.61, and a down-projection kernel from 0.99 at 38.21 to 0.46 at a distance of 30.90 (a KL divergence of
0.0050, 6 refusals in 100 against 89). Measured on Wheat in round 49 against Skyfall, 90 of 489 tensors changed: the
down projections of layers 8 to 53 and the attention outputs of 10 to 53, the two kernels' reaches cut at the last
layer, exactly 0 outside. One direction serves every layer and both writers (0.997 at the median, 0.960 at the least),
on the output side. On the fourteen inserted attention outputs one minus the left kept fraction reads 1.473 to 1.491,
the card's 1.48 within 0.011; on the thirty others it reads 0.64 to 1.35. On the down projections it follows the
kernel's shape on every layer and falls short of its height by 0.0065 to 0.0123 on the inserted layers and by up to
0.112 on the others. First shares run 0.959 to 0.996 and the rows move by 0.0022 to 0.0168 under a card that claims
no norm. Matched by layer number, the direction stands at 0.817 to grayarea's text-only pass of Mistral Small 3.2 and
0.792 to the same maker's Magistral pass (finding 137), the census's two other shared-direction passes on this
hidden size, 0.586 and 0.529 to the round's projection of Harbinger and the maker's Magidonia pass, and 0.19 or less
to huihui-ai's projection and llmfan46's searches; on layers 0 to 27, where the depths agree, the first two numbers
move by 0.003.

Why it matters: the kernel record says what the tool asked for and the weights say what each layer took, and the two
agree to the second decimal only where the parent's writer is nearly empty. On the forty layers that carry
Magistral's own writers the same requested weight lands lower, by up to 0.84 on the attention outputs, while the
reaches and the down kernel's shape stay the record's. Finding 46 read the same tool's kernels to the third decimal
on Mistral instruct bases and finding 144 reads them so on this maker's 40-layer Magidonia pass, so the shortfall here
belongs to the upscaled parent, and a kernel's heights are a reading of the parent's writers as well as of the card.
An upscale that inserts near-zero layers is also an inventory fact the bytes give before any edit: fourteen layers
that do almost nothing until a fine-tune or an edit writes into them.

Evidence: `results/weights/coder3101-Skyfall-31B-v4.2-heretic.json`, the `results/meta/` report, the direction file
under `wheat49/measurements/pair-1/` against `wheat47/measurements/pair-3/`, `nautilus18/measurements/pair-8/` and
the other Mistral Small measurements, the parent's tensor norms in the weights report, the byte-range reads of the
copy, Skyfall and Magistral Small 2509 listed in `docs/census-round-49.md`, and the reading in `docs/cards/`.

## 144. One maker's Heretic 1.1 pass on a Magistral Small fine-tune reads both printed per-layer kernels to the third decimal on all 32 matrices, the census's fourth record read so on a Mistral base

TheDrummer's Magidonia-24B-v4.3 is a fine-tune of mistralai/Magistral-Small-2509 that stands 0.0182 and 0.0269 from
it on the layer 5 query projection and layer 30 attention output, with no leading component. coder3101's
Magidonia-24B-v4.3-heretic (created 2025-12-20) carries Heretic v1.1.0's table with one direction per layer: an
attention-output kernel from 0.89 at 30.54 to 0.69 at a distance of 4.37 and a down-projection kernel from 1.01 at
23.69 to 0.98 at a distance of 11.82 (a KL divergence of 0.0485, 5 refusals in 100 against 73). Measured on Wheat in
round 49 against Magidonia, 32 of 363 tensors changed: the down projections of layers 12 to 35 and the attention
outputs of 27 to 34, the kernels' reaches to the layer, exactly 0 outside, the copy's first three shards and its
tenth the parent's by object id. The two writers of a layer share a direction (0.99998 at the median) and the layers
do not (0.56). Every edit is on the output side, and one minus the left kept fraction reads 0.977 to 1.013 on the
down projections and 0.725 to 0.865 on the attention outputs; the printed kernels give the same weights within
0.0036 on all 24 down projections and within 0.0050 on all 8 attention outputs. First shares run 0.981 to 0.996 (18
under the 0.99 floor) and the rows move by 0.0101 to 0.0705 under no claim. The direction stands at 0.645 to Pranavz's
Hearthfire pass, 0.529 to the maker's Skyfall pass, 0.467 and 0.439 to grayarea's two passes and 0.38 or less to every
other Mistral Small edit.

Why it matters: a record read to the third decimal on all 32 matrices is the strongest kind of reading the census
makes, and this one is on a fine-tune of a reasoning fine-tune of Mistral Small 3.2, two steps from the publisher's
checkpoint. With Zephyr (finding 135) and the two Mistral instruct bases of finding 46 it makes the tool's kernels
readable exactly on four Mistral-family checkpoints, and it is the control for finding 143: the same maker and tool,
a parent from the same fine-tuner on the same base, and the heights read exactly where the parent's layers are its
base's in number and kind.

Evidence: `results/weights/coder3101-Magidonia-24B-v4.3-heretic.json`, the `results/meta/` report, the direction
file under `wheat49/measurements/pair-2/` against `wheat35/measurements/pair-3/` and the other Mistral Small
measurements, the byte-range reads listed in `docs/census-round-49.md`, the hub's file listings of the copy and its
parent, and the reading in `docs/cards/`.

## 145. One maker's arbitrary-rank search over a passthrough merge edits only the first of the merge's two stacks, the card's window to the layer with fifteen layers traced and no component amplified, at 0.64 to 0.84 to the maker's three Mistral Small searches

zerofata's MS3.2-PaintedFantasy-Visage-v3-34B publishes its construction: a `passthrough` merge of
ConicCat/Mistral-Small-3.2-AntiRep-24B's layers 0 to 28 followed by its layers 10 to 39, 59 layers in all, then
continued pretraining, supervised and preference training through a rank-32 adapter. By byte range its layer 5 query
projection stands 0.0119 from the AntiRep model's, its layer 29, the first of the second stack, 0.032 from the AntiRep
model's layer 10 and 0.035 from its own layer 10, and the AntiRep model 0.0014 and 0.0031 from Mistral Small 3.2.
llmfan46's MS3.2-PaintedFantasy-Visage-v3-34B-ultra-uncensored-heretic (created 2026-03-27) carries Heretic 1.2.0's
arbitrary-rank table (`start_layer_index` 3, `end_layer_index` 29, `neighbor_count` 5, `attn.o_proj` the one target,
a KL divergence of 0.0195 and 4 refusals in 100 against 90). Measured on Wheat in round 49 against the merge, 11 of 534
tensors changed, the attention outputs of layers 10, 13 to 19, 21, 24 and 27; the other fifteen of the window moved by
0.0000094 to 0.000268, and layers 0 to 2 and 29 to 58, the whole second stack, read exactly 0. Every edit is on the
input side, one minus the right kept fraction 1.28 to 2.39, one direction per matrix, first shares 0.747 to 0.973, and
no kept fraction of any saved component is above 1. The rows move by 0.0016 to 0.0246. Where the window lies the merge
keeps the AntiRep model's numbering, and there the direction stands on the left at 0.836, 0.814 and 0.635 to the
maker's first Magistral Small 2509 search, Mistral Small 3.2 search and second Magistral search (0.903, 0.922 and
0.902 on the right) and at 0.15 or less to every projection and kernel pass on the hidden size. The copy's template is
the parent's 2,671 bytes with Windows line endings on all 51 lines, and its tokenizer files are a transformers 5.3.0
save that drops the 1,000 `added_tokens_decoder` declarations (finding 44's form).

Why it matters: a 34B that is a 24B with thirty layers repeated gives an edit two places to land for every repeated
layer, and this search, run on the merge as a whole, found nothing to change in the second stack and edited layers of the
first stack that the maker's 24B searches also edit, along the maker's own direction there (0.84 and
0.81 on the left, 0.90 to 0.92 on the right). The repeated layers were trained apart after the merge, so the window
the card prints is the whole of the edit and the bytes confirm it. "Ultra" in the name reads no amplification here,
as on the maker's Garnet V2 search (finding 134). A pinner that reads a parent's merge ranges could map each layer of
a depth extension to its source before the download.

Evidence: `results/weights/llmfan46-MS3.2-PaintedFantasy-Visage-v3-34B-ultra-uncensored-heretic.json`, the
`results/meta/` report, the parent's published merge configuration, the direction file under
`wheat49/measurements/pair-3/` against `nautilus20/measurements/pair-7/`, `blueback14/measurements/pair-6/` and
`nautilus18/measurements/pair-7/`, the byte-range reads listed in `docs/census-round-49.md`, the two templates
compared byte for byte, and the reading in `docs/cards/`.

## 146. An edit named biprojected and norm-preserving reads one direction on both writers of 36 layers at smooth weights to 1.44, and by byte range it is a plain projection along that direction to within an eighth to a fifth of its change, with the rows moved as a plain projection moves them

LatitudeGames's Harbinger-24B is a supervised and preference-trained fine-tune of
mistralai/Mistral-Small-3.1-24B-Instruct-2503 on ChatML, with `<|im_end|>` at id 999 as its end of sequence.
vprilepskii's Harbinger-24B-biprojected-norm-preserving-abliterated (created 2025-11-25) carries a 235-byte card that
names the parent and links grimjim's posts on projected abliteration and on norm-preserving biprojected abliteration,
with no parameter. Measured on Wheat in round 49 against Harbinger, 58 of 363 tensors changed: the down projections of
layers 4 to 39 and the attention outputs of 15 to 36, exactly 0 outside, the copy's first shard the parent's by object
id. One direction serves all 58 (0.99998 at the median, 0.99996 at the least), on the output side, and one minus the
left kept fraction draws two smooth shapes the card does not print: 1.364 at layer 4 rising to 1.443 at 27 and back to
1.405 at 39 on the down projections, and 0.851 at 15 rising to 1.032 at 25 and back to 0.873 at 36 on the attention
outputs. First shares run 0.907 to 0.988 and the rows move by 0.0031 to 0.0178. By byte range on the layer 20 and 30
attention outputs and the layer 20 down projection, a plain projection of the parent along the copy's own leading
direction at the weight the copy reads, rounded to bfloat16, lands 0.0031, 0.0027 and 0.0026 from the copy, whose
change from the parent is 0.0161, 0.0131 and 0.0218, and moves the rows by up to 0.0153, 0.0050 and 0.0088 where the
copy moves them by 0.0148, 0.0041 and 0.0086. The column norms, which the linked method keeps, hold within 0.00016 on
90 percent of the columns and move by up to 0.0063, 0.0075 and 0.0076 on the rest, against 0.0037, 0.0023 and 0.0165
under the plain projection. The direction stands at 0.746 to venkycs's projection of Mistral Small 24B Instruct 2501,
0.660 and 0.621 to grayarea's two passes and 0.586 to the round's Skyfall pass.

Why it matters: the name promises two things the weights can check, a biprojected direction and a preserved norm.
The direction reads as a single projected direction on every writer of every edited layer, as a biprojection would
give, but nothing in the weights is preserved beyond what the plain projection would leave: the rows move as far, and
the columns, the axis the linked method normalises, move further than the plain projection would on the attention
outputs. Finding 130 read the rows of an edit under the same name moved to 0.018; this pair adds the column read and
the plain-projection comparison, so "norm-preserving" in a repository name is, on the two edits the census has read
under it, a label and not a property of the weights. A measurement that reads only row norms cannot tell a column
normalisation from none, which is why the column line belongs in the method.

Evidence: `results/weights/vprilepskii-Harbinger-24B-biprojected-norm-preserving-abliterated.json`, the
`results/meta/` report, the direction file under `wheat49/measurements/pair-4/` against
`nautilus16/measurements/pair-7/` and the other Mistral Small measurements, the byte-range reads and the plain
projection computed at home listed in `docs/census-round-49.md`, and the reading in `docs/cards/`.

## 147. One maker's search on the first Garnet fine-tune reads the card's window to the layer at input-side weights to 3.44 and rows to 0.32 with no component amplified, at 0.883 to the same maker's search on the second, and the two Garnet versions are sibling trainings of Google's 31B

ConicCat's Gemma4-Garnet-31B (2026-04-07) and Gemma4-GarnetV2-31B (04-21) both publish their adapters, rank 32 at
alpha 64 and rank 64 at alpha 128 on all seven projections of google/gemma-4-31B-it, and share their configuration,
shard index, processor file and `tokenizer.json` by object id. By byte range the first stands 0.0291 and 0.0315 from
Google's on the layer 10 and 30 attention outputs and 0.0328 on the layer 5 query projection, the second 0.0323 and
0.0286, and the two 0.0434, 0.0425 and 0.0491 from each other, their leading components at 0.03 and 0.24 to each
other. llmfan46's Gemma-4-Garnet-31B-it-uncensored-heretic (created 2026-04-14) carries Heretic 1.2.0's
arbitrary-rank table (`start_layer_index` 26, `end_layer_index` 46, `overcorrect_relative_weight` 1.1479,
`neighbor_count` 10, a KL divergence of 0.0368 and 6 refusals in 100 against 99). Measured on Wheat in round 49
against the first Garnet, 16 of 1,188 tensors changed, the attention outputs of layers 26 to 28, 30 to 34, 36 to 39, 41
and 43 to 45; layers 29, 35, 40 and 42 moved by 0.00000055 to 0.0000034 and everything outside the window reads
exactly 0. Every edit is on the input side, one minus the right kept fraction 1.64 to 3.44, one direction per matrix,
first shares 0.924 to 0.971, and the eight saved components keep at most 1.005 on the left and 1.041 on the right. The
rows move by 0.0017 to 0.3246, the largest on layer 44 (0.3246), 37 (0.0609) and 39 (0.0469). The direction stands at
0.910 to the maker's 31B QAT search, 0.883 to the maker's Garnet V2 search (16 names, 0.914 on the right), 0.811 to the
maker's April edit and 0.18 or less to every kernel pass and projection; by byte range on layers 30, 37 and 44, which
both searches edit, the two changes' leading directions stand at 0.923, 0.817 and 0.766 on the left and 0.933, 0.722
and 0.329 on the right. The copy carries the maker's 17,344-byte template, put in on 05-05 at 17:02Z, 24 seconds after
it replaced the Garnet V2 copy's.

Why it matters: the maker searched two versions of one fine-tuner's 31B, which the bytes read as two separate
trainings of Google's checkpoint rather than one over the other, and found directions at 0.88 to each other in the
saved vectors, the level at which the maker's searches across different 31B fine-tunes stand (findings 120, 134 and
140), with the agreement falling from 0.92 to 0.77 across the window. The first search's edit is the stronger of the
two (input-side weights to 3.44 against 2.66, rows to 0.32 against 0.038) and still amplifies nothing, so the multiplied
components of finding 120 stay the Queen and MeroMero edits'. The template is the maker's-template case a seventh
time, by the same two-step replacement as on the second copy.

Evidence: `results/weights/llmfan46-Gemma-4-Garnet-31B-it-uncensored-heretic.json`, the `results/meta/` report, the
direction file under `wheat49/measurements/pair-5/` against `wheat45/measurements/pair-7/` and the thirty-seven other
31B measurements, the two parents' adapter configurations and file listings, the byte-range reads listed in
`docs/census-round-49.md`, the copy's template history, and the reading in `docs/cards/`.

## 148. An antislop fine-tune over a measured 26B-A4B Heretic edit trains the last five layers and the tied embedding in float16, moves the edit along itself by at most 0.00015 of itself, and rewrites the stop token in the configuration

Tetratype's Gemma-4-26B-A4B-it-heretic-antislop (created 2026-05-26) has a 221-byte card that names
coder3101/gemma-4-26B-A4B-it-heretic as the model and Sam Paech's auto-antislop as the fine-tuning. Its parent is coder3101's
arbitrary-rank Heretic 1.2.0 edit of google/gemma-4-26B-A4B-it at `e6d09d5c`, which the census measured against
Google in round 12 at this revision (the attention outputs of layers 10 to 29, no expert). Measured on Wheat in round
49 against that edit, 31 of 1,013 tensors changed: in each of layers 25 to 29 the attention output, the dense gate,
up and down projections and the packed gate-up and down tensors of the 128 experts, and the token embedding. The
queries, keys and values of those layers, every tensor of layers 0 to 24 and the vision tower moved by the float16
recast alone (0.00000024 at most) and the normalisation vectors read exactly 0. There is no direction: first shares
0.014 to 0.053 on the expert tensors and 0.51 to 0.94 on the dense ones, both kept fractions 0.985 to 1.005 on every
layer matrix, relative changes 0.0025 to 0.0085. The embedding moved by 0.0129, and by byte range every one of its
262,144 rows moved by more than 0.0001 and 113,777 by more than 0.01, most of the change one vector of the hidden size
added to nearly every row (the leading component, first share 0.922, at 0.9997 to the mean row change); the
configuration ties it to the output head. On the five attention outputs where the training meets the edit, the edit
stands 0.0123 to 0.0162 from Google's (first shares 0.913 to 0.959); the training moves those matrices by a fifth to a
quarter of the edit's size, by -0.00015 to -0.00003 of the edit along the edit, with its leading directions at 0.002
to 0.039 to the edit's, and the copy's difference from Google's stands at 1.0000 to the edit's leading direction on
all five; the saved vectors stand at 0.009 to coder3101's on those names and 0.027 or less to every 26B-A4B
measurement. The save is Unsloth's: `eos_token_id` `[1, 106]` becomes 1 and the generation list `[1, 106, 50]` becomes
`[1, 1, 106, 50]`, with the tokenizer's end of sequence left at `<eos>`.

Why it matters: an antislop pass is a training on preference pairs built to suppress overused phrases, and the
question for the census was whether it is training alone, as findings 121, 138 and 142 read their fine-tunes, or a
further projection. The weights answer training alone: no leading direction on any matrix, kept fractions at 1, and
the embedding shifted rather than projected. It is also confined: five of thirty layers, the writers and the
feed-forward experts but not the queries, keys or values, and the tied embedding, which is the shape of a training
aimed at the last layers and the output vocabulary. Laid over a measured edit, it leaves the edit in place on every
matrix the two share, the second such case after finding 142 and the first on a mixture-of-experts checkpoint. The
token side carries a third Unsloth form of the stop token after the two of findings 98 and 100: the configuration now names
`<eos>` alone, and only the generation list still stops on `<turn|>`.

Evidence: `results/weights/Tetratype-Gemma-4-26B-A4B-it-heretic-antislop.json`, the `results/meta/` report,
`results/weights/coder3101-gemma-4-26B-A4B-it-heretic.json`, the direction file under `wheat49/measurements/pair-6/`
against `blueback12/measurements/pair-6/` and the other 26B-A4B measurements, the byte-range reads of the copy,
coder3101's edit and Google's 26B-A4B at `47b6801b` listed in `docs/census-round-49.md`, and the reading in
`docs/cards/`.

## 149. A maker's second reasoning fine-tune over an unmeasured 27B Heretic edit contains the maker's first one nearly whole, plus a second training at right angles to it one and a half to two times its size, and takes back less than one percent of the edit

DavidAU's Gemma-3-27b-it-Gemini-Heretic-Uncensored-Deeper-Reasoning-Series2 (created 2026-01-26, weights unchanged
since) is "a fully uncensored, full deep thinking Gemma 27B fine tune via Unsloth" over
coder3101/gemma-3-27b-it-heretic at `b9449797`, on TeichAI's 1,000-row Gemini reasoning set where the first pass used
the 250-row one; the first pass is the file Justbackup's hub duplicate carries, measured in round 42 against the same
parent at the same revision (finding 121). Measured on Wheat in round 49, 432 of 1,247 tensors changed: the query,
attention output, gate, up and down projections of all 62 layers and the keys and values of 61, layer 1's key and
value just under the threshold (0.00082 and 0.00085), the vision tower, the embedding and the normalisation vectors
exactly 0. There is no direction (first shares 0.28 to 0.985), relative changes run 0.0011 to 0.0698 with a median of
0.0064, larger on every kind than the first pass's 0.0010 to 0.0407, and by byte range six rows of one head of the
layer 4 query projection grew by 0.59 to 1.28 where the first pass moved them by 0.0003. On the 418 names both changed
the two trainings' leading vectors stand at 0.491 on the left and 0.779 on the right at the median (0.40 to 0.68 on
the left by kind). By byte range on the layer 30 attention output, down projection and query projection, the second
pass's change from the edit carries the first pass's change at a coefficient of 0.962, 0.828 and 0.821, and what the
second adds beyond the first stands at -0.024, -0.117 and -0.084 to the first's change and at 1.61, 1.48 and 2.12
times its size. Along coder3101's edit, which stands 0.0218 and 0.0199 from Google's on the first two matrices, the
second pass moves by -0.00073 and -0.0075 of the edit and the first by -0.00002 and -0.0008.

Why it matters: the question for the round was whether the second pass is a second training on the same base and
whether the two trainings agree. The weights read the second as the first training, nearly whole, with a second
training of about one and a half to two times the size added at right angles to it; that is a second pass over the
first copy's weights or one longer run from the edit on a larger set that begins with the smaller one, and the bytes
cannot separate the two. Either way the trainings agree where they overlap and differ by what was added. Neither
moves along the edit the copies stand on by as much as one percent of it, so DavidAU's reasoning fine-tunes, like the
three trainings of findings 138, 142 and 148, leave the removed direction removed. The edit itself is still read only
through these two children, and coder3101's 27B edit is the one parent the pinner should queue against Google next.

Evidence: `results/weights/DavidAU-Gemma-3-27b-it-Gemini-Heretic-Uncensored-Deeper-Reasoning-Series2.json`,
`results/weights/Justbackup-Gemma-3-27b-it-Uncensored-HERETIC-Gemini-Deep-Reasoning.json`, the `results/meta/`
reports, the direction files under `wheat49/measurements/pair-7/` and `nautilus42/measurements/pair-5/` and
`nautilus3/measurements/pair-2/` (mlabonne's), the byte-range reads of both passes, coder3101's edit and Google's 27B
listed in `docs/census-round-49.md`, both cards and commit histories, and the reading in `docs/cards/`.

## 150. The census's first Gemma 2 copy is the classic projection of one direction out of both writers of all 42 layers at a flat 1.5, read with no flag, under a card that names no method and calls the files a test

sam-paech's Darkest-muse-v1 (2024-10-22) is a `dare_ties` merge of two of the author's Gutenberg3 preference-trained
Gemma 2 9B fine-tunes onto lemon07r's Gemma-2-Ataraxy-v2-9B, and by byte range it stands 0.0021, 0.0032 and 0.0012
from google/gemma-2-9b-it on the layer 20 attention output, layer 20 down projection and layer 5 query projection,
with no leading component. Naphula's Darkest-muse-v1-abliterated (created 2025-12-08) carries a card that names no
tool or parameter ("they have not been ablated with MPOA, so may suffer some cognitive decline", "made these mainly for
testing purpose", untested for compliance) and ships the parent's configuration, shard index and token files by object
id. Measured on Wheat in round 49 against the merge, 84 of 465 tensors changed, the down projections and attention
outputs of all 42 layers, exactly 0 outside, the embedding and the output head included. One direction serves all 84
(0.9995 at the median, 0.9964 at the least, 0.9948 across kinds), on the output side, and one minus the left kept
fraction reads 1.500 to 1.511 on every matrix; first shares run 0.9952 to 0.9969 and the rows move by 0.0034 to
0.0317. The tool matched `single-projection` with no flag. No other measurement is on Gemma 2 and none shares its
hidden size of 3,584, so the direction has nothing to stand against. The token side differs in no field and reads
"undecided" because neither side publishes a generation file and the shared template refuses the fixed
conversation's system turn; rendered at home without one, the two give the same string.

Why it matters: the oldest form of the method, one mean direction removed from every writer at one scale, reads as
cleanly on a 2024 merge of a 2024 base as on the checkpoints the census was built around, and a card that says almost
nothing about the method is read to its single scale from the weights. The pair also marks a gap in the census's
families: the saved-vector check of finding 66 has no Gemma 2 measurement to place the direction against, so the
placing waits for a Gemma 2 instruct edit to be pinned. The metadata side shows a pair left undecided with nothing
differing, a limit of the fixed conversation and of the missing generation file that the copy shares with its parent.

Evidence: `results/weights/Naphula-Darkest-muse-v1-abliterated.json`, the `results/meta/` report, the parent's
published merge configuration, the direction file under `wheat49/measurements/pair-8/`, the byte-range reads of the
copy, the merge and google/gemma-2-9b-it at `11c9b309` listed in `docs/census-round-49.md`, the template rendered at
home, and the reading in `docs/cards/`.

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
- Population. Two hundred and thirty-one copies is a sample; the inventory sample of 30 repositories
  (`docs/inventory-sample.md`) shows how mirrors and re-quantizations outnumber sources and how often the stated
  original cannot be resolved (16 of 30).

Weight differences alone cannot certify the absence of hidden behavior.
