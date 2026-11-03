# 12b-families-parameters.md -- The 12B copies beside their direction family and the tool figures their reading notes record.

| copy | family | tool | version | direction index | kernels or window | weight | changed | prompt set | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3MPER0RR/gemma-4-12b-it-3MPER0RR-abliterated | 1 | unknown | not printed | not printed | not printed | not printed | 48 | not printed |  |
| BinxNet/gemma-4-12B-it-heretic | 1 | Heretic | v1.4.0 | 28.91 | attn 1.44 at 28.65 to 0.11 at 25.21; down 1.48 at 32.22 to 0.97 at 5.73 | not printed | 55 | not printed |  |
| MoonRide/gemma-4-12B-it-heretic | 1 | Heretic | 1.3.0 | 29.60 | attn 1.35 at 31.80, width 15.78; down 1.39 at 42.25, width 15.71 | not printed | 52 | not printed |  |
| Paul691/gemma-4-12B-it-abliterated-uncensored | 1 | custom abliteration framework | not printed | not printed | not printed | 0.40 | 553 | not printed | edit over a coder fine-tune |
| lemuralabs/Gemma-4-12B-uncensored-bf16 | 1 | directional ablation (Optuna/TPE) | 1.3.0 | not printed | not printed | not printed | 553 | not printed | ablation over a coding fine-tune |
| prithivMLmods/gemma-4-12B-it-heretic_decensored | 1 | Heretic | not printed | 29.56 | attn 1.18 at 39.94, 0.81 at 25.73; down 1.37 at 46.27, 0.97 at 21.63 | not printed | 56 | not printed |  |
| Iambackup/gemma-4-12B-it-uncensored | 2 | norm-preserving biprojected abliteration | not printed | per layer | layers 15 to 47 | not printed | 66 | not printed | TrevorJS's card, byte-identical re-upload |
| Ishowbackup/gemma-4-12B-it-uncensored | 2 | norm-preserving biprojected abliteration | not printed | per layer | layers 15 to 47 | not printed | 66 | not printed | TrevorJS's card, byte-identical re-upload |
| Justbackup/gemma-4-12B-it-uncensored | 2 | norm-preserving biprojected abliteration | not printed | per layer | layers 15 to 47 | not printed | 66 | not printed | TrevorJS's card, byte-identical re-upload |
| Sabomako/gemma-4-12B-it-heretic | 2 | Heretic, custom ORBA abliteration | v1.3.0 | not printed | not printed | not printed | 31 | not printed |  |
| TrevorJS/gemma-4-12B-it-uncensored | 2 | norm-preserving biprojected abliteration | not printed | per layer | layers 15 to 47 | scale 1.0 | 66 | not printed |  |
| laladream/gemma-4-12B-it-uncensored | 2 | norm-preserving biprojected abliteration | not printed | not printed | layers 15 to 47 | not printed | 66 | not printed | TrevorJS's card, byte-identical re-upload |
| Ishowbackup/Huihui-gemma-4-12B-it-abliterated | 3 | abliteration (remove-refusals code) | not printed | not printed | layers 23-28 | not printed | 12 | not printed | huihui-ai's card, byte-identical re-upload |
| TimelessSoul/Huihui-gemma-4-12B-it-abliterated | 3 | abliteration (remove-refusals code) | not printed | not printed | layers 23-28 | not printed | 12 | not printed | huihui-ai's card, byte-identical re-upload |
| huihui-ai/Huihui-gemma-4-12B-it-abliterated | 3 | abliteration (remove-refusals code) | not printed | not printed | layers 23-28 | not printed | 12 | not printed | re-ablated and re-uploaded |
| MeFFyLe/gemma-4-12B-it-uncensored-heretic | 4 | Heretic, arbitrary-rank ablation | 1.2.0 | not printed | start layer 24, end layer 40 | not printed | 16 | not printed | llmfan46's card, byte-identical re-upload |
| coder3101/gemma-4-12B-it-heretic | 4 | Heretic, arbitrary-rank ablation | 1.2.0 | not printed | start layer 2, end layer 45 | preserve 0.3688, steer 0.0004, overcorrect 1.0066 | 86 | not printed |  |
| llmfan46/gemma-4-12B-it-uncensored-heretic | 4 | Heretic, arbitrary-rank ablation | v1.2.0 | not printed | start layer 24, end layer 40 | preserve 0.7201, steer 0.0067, overcorrect 0.9541 | 16 | not printed |  |
| RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals2 | 5 | Heretic, arbitrary-rank ablation | 1.2.0 | not printed | start_layer 23, end_layer 43 | preserve 0.2271, steer 0.0001, overcorrect 0.1443 | 40 | not printed |  |
| RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals4 | 5 | Heretic, arbitrary-rank ablation | 1.2.0 | not printed | start_layer_index 24, end_layer_index 37 | preserve 0.1819, steer 0.0001, overcorrect 0.7372 | 26 | not printed |  |
| RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals9 | 5 | Heretic, arbitrary-rank ablation | 1.2.0 | not printed | start layer 14, end layer 44 | preserve 0.9147, steer 0.0001, overcorrect 0.1317 | 55 | not printed |  |
| Vampelium/gemma-4-12B-it-heretic | 6 | Heretic | not printed | not printed | not printed | not printed | 75 | not printed |  |
| igorls/gemma-4-12B-it-heretic-v1 | 6 | Heretic, norm-preserving biprojected | not printed | not printed | not printed | not printed | 22 | not printed |  |
| AEON-7/Gemma-4-12B-it-AEON-Abliterated-K4-BF16 | alone | K=4 multi-direction biprojection | not printed | not printed | layers 21 to 42, 44 and 45 | scale 1.0 | 48 | not printed |  |
| AlekseyCalvin/Lyrical_Translator_ru2en_on_Gemma4_12b_heretic_SFT_Run2 | alone | fine-tune over igorls's Heretic edit | not printed | not printed | not printed | not printed | 328 | not printed | fine-tune over a Heretic edit |
| Carlosian/Gemma-4-12b-it-Abliterated | partner under 0.9 | biprojected clean-cone abliteration | not printed | not printed | layers 14 to 34 | alpha 1.0 | 42 | not printed |  |
| enkato64bit/SuperGemma-4-12b-abliterated | partner under 0.9 | single projection over a merged adapter | not printed | not printed | layers 14 to 37 | 0.50 | 320 | not printed | edit over a fine-tune |
| jwest33/gemma-4-12B-it-null-space-abliterated | partner under 0.9 | orthogonal projection, null-space constraints | not printed | not printed | not printed | 1.10 | 329 | 5,000 harmful and 1,226 harmless |  |
| richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic | partner under 0.9 | Heretic | 1.4.0 | 28.16 | attn 1.24 to 1.28; down 1.47 to 1.48 | not printed | 557 | not printed | edit over a coding fine-tune |

copies with a reading note: 29 of 29
copies with a version printed: 8
copies with a direction index printed: 5
copies with kernels printed: 5
