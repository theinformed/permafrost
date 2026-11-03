# Direction families

## Counts

| parents | copies | rows | rows skipped | weights reports missing |
| --- | --- | --- | --- | --- |
| 23 | 202 | 1968 | 0 | 0 |

## Distribution

| bin | rows |
| --- | --- |
| 0.0 to 0.1 | 887 |
| 0.1 to 0.2 | 252 |
| 0.2 to 0.3 | 155 |
| 0.3 to 0.4 | 81 |
| 0.4 to 0.5 | 77 |
| 0.5 to 0.6 | 51 |
| 0.6 to 0.7 | 58 |
| 0.7 to 0.8 | 45 |
| 0.8 to 0.9 | 75 |
| 0.9 to 1.0 | 287 |

Pooled per-key |cosine|: 74012 keys, median 0.111, mean 0.302, under 0.1 0.483, over 0.9 0.135.

## Per parent

| parent | copies | rows | median agreement | at 0.9 or more | under 0.2 | families at 0.9 | alone at 0.5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TheDrummer/Cydonia-24B-v4.3 | 4 | 6 | 0.545 | 1 | 0 | 2: coder3101/Cydonia-24B-v4.3-heretic-v2, coder3101/Cydonia-24B-v4.3-heretic-v3 | coder3101/Cydonia-24B-v4.3-heretic-v4 |
| TheDrummer/Magidonia-24B-v4.3 | 3 | 3 | 0.644 | 0 | 0 | - | - |
| coder3101/gemma-3-27b-it-heretic | 2 | 1 | 0.779 | 0 | 0 | - | - |
| google/diffusiongemma-26B-A4B-it | 4 | 6 | 0.031 | 1 | 4 | 2: FredyRivera-dev/diffusiongemma-26B-A4B-it-HERETIC-Uncensored, nnnxnsn/diffusiongemma-26B-A4B-it-HERETIC-Uncensored | Goodoldjam/DiffusionGemma-26B-E38-Abliterated-BF16, Umranz/diffusiongemma-26B-A4B-it-abliteration |
| google/gemma-4-12B-it-qat-q4_0-unquantized | 10 | 45 | 0.147 | 3 | 25 | 3: coder3101/gemma-4-12B-it-qat-q4_0-unquantized-heretic, llmfan46/gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic, wnfldchen/gemma-4-12B-it-qat-q4_0-unquantized-heretic | JJaguar/gemma-4-12B-it-qat-q4_0-unquantized-heretic-nx, OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-heretic-ja, OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-heretic-ja-v2, huihui-ai/Huihui-gemma-4-12B-it-qat-q4_0-unquantized-abliterated |
| google/gemma-4-12B-it | 29 | 406 | 0.231 | 36 | 198 | 6: 3MPER0RR/gemma-4-12b-it-3MPER0RR-abliterated, BinxNet/gemma-4-12B-it-heretic, MoonRide/gemma-4-12B-it-heretic, Paul691/gemma-4-12B-it-abliterated-uncensored, lemuralabs/Gemma-4-12B-uncensored-bf16, prithivMLmods/gemma-4-12B-it-heretic_decensored; 6: Iambackup/gemma-4-12B-it-uncensored, Ishowbackup/gemma-4-12B-it-uncensored, Justbackup/gemma-4-12B-it-uncensored, Sabomako/gemma-4-12B-it-heretic, TrevorJS/gemma-4-12B-it-uncensored, laladream/gemma-4-12B-it-uncensored; 3: Ishowbackup/Huihui-gemma-4-12B-it-abliterated, TimelessSoul/Huihui-gemma-4-12B-it-abliterated, huihui-ai/Huihui-gemma-4-12B-it-abliterated; 3: MeFFyLe/gemma-4-12B-it-uncensored-heretic, coder3101/gemma-4-12B-it-heretic, llmfan46/gemma-4-12B-it-uncensored-heretic; 3: RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals2, RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals4, RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals9; 2: Vampelium/gemma-4-12B-it-heretic, igorls/gemma-4-12B-it-heretic-v1 | AEON-7/Gemma-4-12B-it-AEON-Abliterated-K4-BF16, AlekseyCalvin/Lyrical_Translator_ru2en_on_Gemma4_12b_heretic_SFT_Run2 |
| google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | 8 | 28 | 0.140 | 2 | 17 | 3: coder3101/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic, llmfan46/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic, mewse/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ara | Mitchins/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic, eadx/Huihui-gemma-4-26B-A4B-it-qat-q4_0-unquantized-abliterated, xdavxd/gemma-4-26B-A4B-it-qat-heretic-ega |
| google/gemma-4-26B-A4B-it | 18 | 153 | 0.220 | 51 | 63 | 10: BinxNet/gemma-4-26B-A4B-it-heretic, DuoNeural/gemma-4-26B-A4B-it-abliterated, Rootkit7/Gemma-4-26B-A4B-abliterated, SevenOfNine/Gemma-4-26B-A4B-It-Abliterated, TrevorJS/gemma-4-26B-A4B-it-uncensored, claymorecrystal/gemma-4-26B-A4B-it-uncensored, erunda337/gemma-4-26B-A4B-it-uncensored, sh0ck0r/gemma-4-26B-A4B-it-heretic, sitten1/gemma-4-26B-A4B-it-uncensored, tvall43/gemma-4-26B-A4B-it-heretic; 3: SassyDiffusion/gemma-4-26B-A4B-it-heretic-ara, coder3101/gemma-4-26B-A4B-it-heretic, llmfan46/gemma-4-26B-A4B-it-uncensored-heretic; 3: huihui-ai/Huihui-gemma-4-26B-A4B-it-abliterated, prithivMLmods/gemma-4-26B-A4B-Heretic-Stable, prithivMLmods/gemma-4-26B-A4B-it-Uncensored-MAX | - |
| google/gemma-4-31B-it-qat-q4_0-unquantized | 4 | 6 | 0.566 | 1 | 0 | 2: coder3101/gemma-4-31B-it-qat-q4_0-unquantized-heretic, llmfan46/gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic | wnfldchen/gemma-4-31B-it-qat-q4_0-unquantized-heretic-merged |
| google/gemma-4-31B-it | 25 | 298 | 0.147 | 30 | 164 | 7: 3MPER0RR/gemma-4-31b-it-3MPER0RR-abliterated, Sabomako/gemma-4-31B-it-heretic, TrevorJS/gemma-4-31B-it-uncensored, Vampelium/gemma-4-31B-it-heretic, callmegrr/gemma-4-31B-it-heretic-z, germlag/gemma-4-31B-it-heretic-v2, ressl/gemma-4-31B-it-uncensored; 4: MoonRide/gemma-4-31B-it-heretic-ara, MoonRide/gemma-4-31B-it-heretic-ara-custom, coder3101/gemma-4-31B-it-heretic, llmfan46/gemma-4-31B-it-uncensored-heretic; 4: akpsahan/Huihui-gemma-4-31B-it-abliterated-v2, huihui-ai/Huihui-gemma-4-31B-it-abliterated, huihui-ai/Huihui-gemma-4-31B-it-abliterated-v2, prithivMLmods/gemma-4-31B-it-Uncensored-MAX; 2: jcxu97/gemma-4-31B-it-abliterated, wangzhang/gemma-4-31B-it-abliterated | DuoNeural/Gemma4-31B-IT-Abliterated, cosmicoptima/gemma4-31b-consciousness-abliterated, sh0ck0r/Artemis-31B-v1.1-heretic |
| google/gemma-4-E2B-it | 24 | 275 | 0.089 | 37 | 184 | 8: Ishowbackup/gemma-4-E2B-it-uncensored, TrevorJS/gemma-4-E2B-it-uncensored, WWTCyberLab/gemma-4-E2B-it-abliterated, aifeifei798/Heretic-Scalpel-E2B, anlord/gemma-4-E2B-it-abliterated, lessans/gemma-4-E2B-it-uncensored, treadon/gemma4-E2B-it-abliterated, tvall43/gemma-4-E2B-it-heretic-v1; 7: DuoNeural/Gemma-4-E2B-Heretic, Dzluck/gemma-4-E2B-it-abliterated-v2, MoonRide/gemma-4-E2B-it-heretic, huihui-ai/Huihui-gemma-4-E2B-it-abliterated, huihui-ai/Huihui-gemma-4-E2B-it-abliterated, prithivMLmods/gemma-4-E2B-it-Uncensored-MAX, tvall43/gemma-4-E2B-it-heretic-v0; 4: DavidAU/gemma-4-E2B-it-The-DECKARD-HERETIC-UNCENSORED-Thinking, MoonRide/gemma-4-E2B-it-heretic-ara, MoonRide/gemma-4-E2B-it-heretic-ara-custom, llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic | - |
| google/gemma-4-E4B-it-qat-q4_0-unquantized | 3 | 3 | 0.067 | 0 | 2 | - | coder3101/gemma-4-E4B-it-qat-q4_0-unquantized-heretic, igorls/gemma-4-E4B-it-qat-q4_0-unquantized-heretic, prithivMLmods/gemma-4-E4B-it-qat-heretic_decensored |
| google/gemma-4-E4B-it | 39 | 703 | 0.070 | 115 | 470 | 16: Cup4/gemma-4-E4B-it-uncensored-heretic, Cup5/gemma-4-E4B-it-uncensored-heretic, Himanshuoo8/gemma-4-E4B-it-Claude-Opus-4.5-HERETIC-UNCENSORED-Thinking, JokeHer/gemma-4-E4B-it-heretic, MoonRide/gemma-4-E4B-it-heretic-ara, NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals3, NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals5, NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals6-attn, NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8, NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8-attn, Pound1320/gemma-4-E4B-it-uncensored-heretic, SassyDiffusion/gemma-4-E4B-it-heretic, alphakek/gemma-4-E4B-it-heretic-mythos-v1, coder3101/gemma-4-E4B-it-heretic, llmfan46/gemma-4-E4B-it-ultra-uncensored-heretic, llmfan46/gemma-4-E4B-it-uncensored-heretic; 5: BinxNet/gemma-4-E4B-it-heretic, Dingdust/ContextPilot-E4B-heretic, p-e-w/gemma-4-E4B-it-heretic, p-e-w/gemma-4-E4B-it-heretic-REPRODUCED-2, sh0ck0r/gemma-4-E4B-it-heretic; 4: TheUmbraWalker/gemma-4-E4B-it-2-heretic, TheUmbraWalker/gemma-4-E4B-it-heretic, TrevorJS/gemma-4-E4B-it-uncensored, senjiangchen/gemma-4-E4B-it-uncensored; 2: huihui-ai/Huihui-gemma-4-E4B-it-abliterated, prithivMLmods/gemma-4-E4B-it-Uncensored-MAX | Felldude/gemma-4-E4B-uncensored, Ilya626/gemma-4-E4B-it-SDFT_Heretic_RP, Jiunsong/supergemma4-e4b-abliterated, Madras1/Gemma-4-E4B-Abliterated-Uncensored, OS-Software/gemma-4-E4B-it-uncensored-heretic, chulcher/gemma-4-e4b-abliterated, jokernifty/gemma-4-e4b-it-abliterated, treadon/gemma4-E4B-it-Abliterated-AND-Disinhibited-USE-THIS |
| google/gemma-4-E4B | 2 | 1 | 0.028 | 0 | 1 | - | Felldude/gemma-4-E4B-uncensored, chulcher/gemma-4-e4b-abliterated |
| inflatebot/MN-12B-Mag-Mell-R1 | 2 | 1 | 0.998 | 1 | 0 | 2: EldritchLabs/MN-12B-Mag-Mell-R1-Uncensored-Scale1.2, Naphula/MN-12B-Mag-Mell-R1-Uncensored | - |
| mistralai/Magistral-Small-2509 | 3 | 3 | 0.048 | 1 | 2 | 2: llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v1, llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v2 | grayarea/Magistral-Small-2509-Heretic-v1.2 |
| mistralai/Ministral-3-8B-Reasoning-2512 | 2 | 1 | 0.009 | 0 | 1 | - | AISafety-Student/Ministral-3-8B-Reasoning-2512-heretic, ccharnkij/Ministral-3-8B-Reasoning-2512-Uncensored |
| mistralai/Mistral-7B-Instruct-v0.3 | 5 | 10 | 0.863 | 4 | 0 | 5: 3MPER0RR/Mistral-7B-v0.3-3MPER0RR-abliterated, DogOnKeyboard/Mistral-7B-Heretic, evolveon/Mistral-7B-Instruct-v0.3-abliterated, paoloronco/Mistral-7B-Instruct-v0.3-heretic, richardyoung/Mistral-7B-Instruct-v0.3-abliterated | - |
| mistralai/Mistral-Nemo-Instruct-2407 | 2 | 1 | 0.081 | 0 | 1 | - | DuoNeural/Mistral-NeMo-12B-Abliterated, grimjim/mistralai-Mistral-Nemo-Instruct-2407-extensive-BP-abliteration-12B |
| mistralai/Mistral-Small-3.2-24B-Instruct-2506 | 5 | 10 | 0.118 | 1 | 7 | 2: coder3101/Mistral-Small-3.2-24B-Instruct-2506-heretic, darkc0de/Mistral-Small-3.2-24B-Instruct-2506-heretic | llmfan46/Mistral-Small-3.2-24B-Instruct-2506-ultra-uncensored-heretic, nicoboss/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-llamacppfixed |
| yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2 | 2 | 1 | 0.359 | 0 | 0 | - | huihui-ai/Huihui-gemma-4-12B-agentic-fable5-abliterated, llmfan46/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-uncensored-heretic |
| yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | 4 | 6 | 0.650 | 2 | 0 | 3: llmfan46/gemma-4-12B-coder-fable5-composer2.5-v1-uncensored-heretic, richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic, tpls/gemma-4-12B-coder-fable5-composer2.5-v1-abliterated | huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated |
| zerofata/MS3.2-PaintedFantasy-v4.1-24B | 2 | 1 | 0.996 | 1 | 0 | 2: llmfan46/MS3.2-PaintedFantasy-v4.1-24B-ultra-uncensored-heretic-v1, llmfan46/MS3.2-PaintedFantasy-v4.1-24B-ultra-uncensored-heretic-v2 | - |

## Families

- TheDrummer/Cydonia-24B-v4.3: coder3101/Cydonia-24B-v4.3-heretic-v2, coder3101/Cydonia-24B-v4.3-heretic-v3
- google/diffusiongemma-26B-A4B-it: FredyRivera-dev/diffusiongemma-26B-A4B-it-HERETIC-Uncensored, nnnxnsn/diffusiongemma-26B-A4B-it-HERETIC-Uncensored
- google/gemma-4-12B-it-qat-q4_0-unquantized: coder3101/gemma-4-12B-it-qat-q4_0-unquantized-heretic, llmfan46/gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic, wnfldchen/gemma-4-12B-it-qat-q4_0-unquantized-heretic
- google/gemma-4-12B-it: 3MPER0RR/gemma-4-12b-it-3MPER0RR-abliterated, BinxNet/gemma-4-12B-it-heretic, MoonRide/gemma-4-12B-it-heretic, Paul691/gemma-4-12B-it-abliterated-uncensored, lemuralabs/Gemma-4-12B-uncensored-bf16, prithivMLmods/gemma-4-12B-it-heretic_decensored
- google/gemma-4-12B-it: Iambackup/gemma-4-12B-it-uncensored, Ishowbackup/gemma-4-12B-it-uncensored, Justbackup/gemma-4-12B-it-uncensored, Sabomako/gemma-4-12B-it-heretic, TrevorJS/gemma-4-12B-it-uncensored, laladream/gemma-4-12B-it-uncensored
- google/gemma-4-12B-it: Ishowbackup/Huihui-gemma-4-12B-it-abliterated, TimelessSoul/Huihui-gemma-4-12B-it-abliterated, huihui-ai/Huihui-gemma-4-12B-it-abliterated
- google/gemma-4-12B-it: MeFFyLe/gemma-4-12B-it-uncensored-heretic, coder3101/gemma-4-12B-it-heretic, llmfan46/gemma-4-12B-it-uncensored-heretic
- google/gemma-4-12B-it: RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals2, RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals4, RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals9
- google/gemma-4-12B-it: Vampelium/gemma-4-12B-it-heretic, igorls/gemma-4-12B-it-heretic-v1
- google/gemma-4-26B-A4B-it-qat-q4_0-unquantized: coder3101/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic, llmfan46/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic, mewse/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ara
- google/gemma-4-26B-A4B-it: BinxNet/gemma-4-26B-A4B-it-heretic, DuoNeural/gemma-4-26B-A4B-it-abliterated, Rootkit7/Gemma-4-26B-A4B-abliterated, SevenOfNine/Gemma-4-26B-A4B-It-Abliterated, TrevorJS/gemma-4-26B-A4B-it-uncensored, claymorecrystal/gemma-4-26B-A4B-it-uncensored, erunda337/gemma-4-26B-A4B-it-uncensored, sh0ck0r/gemma-4-26B-A4B-it-heretic, sitten1/gemma-4-26B-A4B-it-uncensored, tvall43/gemma-4-26B-A4B-it-heretic
- google/gemma-4-26B-A4B-it: SassyDiffusion/gemma-4-26B-A4B-it-heretic-ara, coder3101/gemma-4-26B-A4B-it-heretic, llmfan46/gemma-4-26B-A4B-it-uncensored-heretic
- google/gemma-4-26B-A4B-it: huihui-ai/Huihui-gemma-4-26B-A4B-it-abliterated, prithivMLmods/gemma-4-26B-A4B-Heretic-Stable, prithivMLmods/gemma-4-26B-A4B-it-Uncensored-MAX
- google/gemma-4-31B-it-qat-q4_0-unquantized: coder3101/gemma-4-31B-it-qat-q4_0-unquantized-heretic, llmfan46/gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic
- google/gemma-4-31B-it: 3MPER0RR/gemma-4-31b-it-3MPER0RR-abliterated, Sabomako/gemma-4-31B-it-heretic, TrevorJS/gemma-4-31B-it-uncensored, Vampelium/gemma-4-31B-it-heretic, callmegrr/gemma-4-31B-it-heretic-z, germlag/gemma-4-31B-it-heretic-v2, ressl/gemma-4-31B-it-uncensored
- google/gemma-4-31B-it: MoonRide/gemma-4-31B-it-heretic-ara, MoonRide/gemma-4-31B-it-heretic-ara-custom, coder3101/gemma-4-31B-it-heretic, llmfan46/gemma-4-31B-it-uncensored-heretic
- google/gemma-4-31B-it: akpsahan/Huihui-gemma-4-31B-it-abliterated-v2, huihui-ai/Huihui-gemma-4-31B-it-abliterated, huihui-ai/Huihui-gemma-4-31B-it-abliterated-v2, prithivMLmods/gemma-4-31B-it-Uncensored-MAX
- google/gemma-4-31B-it: jcxu97/gemma-4-31B-it-abliterated, wangzhang/gemma-4-31B-it-abliterated
- google/gemma-4-E2B-it: Ishowbackup/gemma-4-E2B-it-uncensored, TrevorJS/gemma-4-E2B-it-uncensored, WWTCyberLab/gemma-4-E2B-it-abliterated, aifeifei798/Heretic-Scalpel-E2B, anlord/gemma-4-E2B-it-abliterated, lessans/gemma-4-E2B-it-uncensored, treadon/gemma4-E2B-it-abliterated, tvall43/gemma-4-E2B-it-heretic-v1
- google/gemma-4-E2B-it: DuoNeural/Gemma-4-E2B-Heretic, Dzluck/gemma-4-E2B-it-abliterated-v2, MoonRide/gemma-4-E2B-it-heretic, huihui-ai/Huihui-gemma-4-E2B-it-abliterated, huihui-ai/Huihui-gemma-4-E2B-it-abliterated, prithivMLmods/gemma-4-E2B-it-Uncensored-MAX, tvall43/gemma-4-E2B-it-heretic-v0
- google/gemma-4-E2B-it: DavidAU/gemma-4-E2B-it-The-DECKARD-HERETIC-UNCENSORED-Thinking, MoonRide/gemma-4-E2B-it-heretic-ara, MoonRide/gemma-4-E2B-it-heretic-ara-custom, llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic
- google/gemma-4-E4B-it: Cup4/gemma-4-E4B-it-uncensored-heretic, Cup5/gemma-4-E4B-it-uncensored-heretic, Himanshuoo8/gemma-4-E4B-it-Claude-Opus-4.5-HERETIC-UNCENSORED-Thinking, JokeHer/gemma-4-E4B-it-heretic, MoonRide/gemma-4-E4B-it-heretic-ara, NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals3, NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals5, NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals6-attn, NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8, NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8-attn, Pound1320/gemma-4-E4B-it-uncensored-heretic, SassyDiffusion/gemma-4-E4B-it-heretic, alphakek/gemma-4-E4B-it-heretic-mythos-v1, coder3101/gemma-4-E4B-it-heretic, llmfan46/gemma-4-E4B-it-ultra-uncensored-heretic, llmfan46/gemma-4-E4B-it-uncensored-heretic
- google/gemma-4-E4B-it: BinxNet/gemma-4-E4B-it-heretic, Dingdust/ContextPilot-E4B-heretic, p-e-w/gemma-4-E4B-it-heretic, p-e-w/gemma-4-E4B-it-heretic-REPRODUCED-2, sh0ck0r/gemma-4-E4B-it-heretic
- google/gemma-4-E4B-it: TheUmbraWalker/gemma-4-E4B-it-2-heretic, TheUmbraWalker/gemma-4-E4B-it-heretic, TrevorJS/gemma-4-E4B-it-uncensored, senjiangchen/gemma-4-E4B-it-uncensored
- google/gemma-4-E4B-it: huihui-ai/Huihui-gemma-4-E4B-it-abliterated, prithivMLmods/gemma-4-E4B-it-Uncensored-MAX
- inflatebot/MN-12B-Mag-Mell-R1: EldritchLabs/MN-12B-Mag-Mell-R1-Uncensored-Scale1.2, Naphula/MN-12B-Mag-Mell-R1-Uncensored
- mistralai/Magistral-Small-2509: llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v1, llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v2
- mistralai/Mistral-7B-Instruct-v0.3: 3MPER0RR/Mistral-7B-v0.3-3MPER0RR-abliterated, DogOnKeyboard/Mistral-7B-Heretic, evolveon/Mistral-7B-Instruct-v0.3-abliterated, paoloronco/Mistral-7B-Instruct-v0.3-heretic, richardyoung/Mistral-7B-Instruct-v0.3-abliterated
- mistralai/Mistral-Small-3.2-24B-Instruct-2506: coder3101/Mistral-Small-3.2-24B-Instruct-2506-heretic, darkc0de/Mistral-Small-3.2-24B-Instruct-2506-heretic
- yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1: llmfan46/gemma-4-12B-coder-fable5-composer2.5-v1-uncensored-heretic, richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic, tpls/gemma-4-12B-coder-fable5-composer2.5-v1-abliterated
- zerofata/MS3.2-PaintedFantasy-v4.1-24B: llmfan46/MS3.2-PaintedFantasy-v4.1-24B-ultra-uncensored-heretic-v1, llmfan46/MS3.2-PaintedFantasy-v4.1-24B-ultra-uncensored-heretic-v2

## By name class

| class pair | rows | median agreement | at 0.9 or more | under 0.2 |
| --- | --- | --- | --- | --- |
| abliterated - abliterated | 200 | 0.229 | 16 | 92 |
| abliterated - heretic | 589 | 0.083 | 30 | 404 |
| abliterated - uncensored | 220 | 0.220 | 27 | 97 |
| heretic - heretic | 588 | 0.124 | 152 | 321 |
| heretic - uncensored | 309 | 0.110 | 37 | 197 |
| uncensored - uncensored | 62 | 0.220 | 25 | 28 |

## Single-direction restriction

Rows kept 1497, dropped for a missing report 0, dropped for fewer than 3 keys 471.

| bin | rows |
| --- | --- |
| 0.0 to 0.1 | 620 |
| 0.1 to 0.2 | 198 |
| 0.2 to 0.3 | 138 |
| 0.3 to 0.4 | 47 |
| 0.4 to 0.5 | 50 |
| 0.5 to 0.6 | 27 |
| 0.6 to 0.7 | 29 |
| 0.7 to 0.8 | 34 |
| 0.8 to 0.9 | 87 |
| 0.9 to 1.0 | 267 |

Rows at 0.9 or more 267, rows under 0.2 818.

| class pair | rows | median agreement | at 0.9 or more | under 0.2 |
| --- | --- | --- | --- | --- |
| abliterated - abliterated | 141 | 0.254 | 16 | 59 |
| abliterated - heretic | 429 | 0.092 | 30 | 295 |
| abliterated - uncensored | 178 | 0.273 | 26 | 65 |
| heretic - heretic | 433 | 0.144 | 130 | 228 |
| heretic - uncensored | 257 | 0.137 | 40 | 146 |
| uncensored - uncensored | 59 | 0.274 | 25 | 25 |

## Sign note

Rows whose signed and absolute medians differ by more than 0.5: 137.

- coder3101/Magidonia-24B-v4.3-heretic ~ coder3101/Magidonia-24B-v4.3-heretic-v2
- Justbackup/Gemma-3-27b-it-Uncensored-HERETIC-Gemini-Deep-Reasoning ~ DavidAU/Gemma-3-27b-it-Gemini-Heretic-Uncensored-Deeper-Reasoning-Series2
- OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-heretic-ja-v2 ~ llmfan46/gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic
- huihui-ai/Huihui-gemma-4-12B-it-abliterated ~ Paul691/gemma-4-12B-it-abliterated-uncensored
- TimelessSoul/Huihui-gemma-4-12B-it-abliterated ~ Paul691/gemma-4-12B-it-abliterated-uncensored
- Ishowbackup/Huihui-gemma-4-12B-it-abliterated ~ Paul691/gemma-4-12B-it-abliterated-uncensored
- llmfan46/gemma-4-12B-it-uncensored-heretic ~ RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals9
- RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals9 ~ MeFFyLe/gemma-4-12B-it-uncensored-heretic
- BinxNet/gemma-4-12B-it-heretic ~ Sabomako/gemma-4-12B-it-heretic
- laladream/gemma-4-12B-it-uncensored ~ jwest33/gemma-4-12B-it-null-space-abliterated
