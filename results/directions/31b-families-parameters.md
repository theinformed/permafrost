# 31b-families-parameters.md -- The 31B copies beside their direction family and the tool figures their reading notes record.

| copy | family | tool | version | direction index | kernels or window | weight | changed | prompt set | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3MPER0RR/gemma-4-31b-it-3MPER0RR-abliterated | 1 | unknown | not printed | not printed | not printed | not printed | 41 | not printed |  |
| Sabomako/gemma-4-31B-it-heretic | 1 | Heretic, custom ORBA abliteration | v1.3.0 | not printed | not printed | not printed | 8 | not printed |  |
| TrevorJS/gemma-4-31B-it-uncensored | 1 | norm-preserving biprojected abliteration | not printed | per layer | not printed | scale 1.0 | 120 | not printed |  |
| Vampelium/gemma-4-31B-it-heretic | 1 | Heretic | not printed | not printed | not printed | not printed | 47 | not printed |  |
| callmegrr/gemma-4-31B-it-heretic-z | 1 | Heretic | v1.4.0 | per layer | attn 1.26 at 41.65 to 0.19 at 4.97; down 1.37 at 40.81 to 1.29 at 1.06 | not printed | 12 | not printed |  |
| germlag/gemma-4-31B-it-heretic-v2 | 1 | Heretic, magnitude-preserving orthogonalisation | 1.2.0 | per layer | attn 1.47 at 57.33, 1.33 at 29.21; down 1.32 at 49.63, 1.23 at 23.83 | not printed | 65 | not printed | coder3101's card, duplicate of coder3101's v2 |
| ressl/gemma-4-31B-it-uncensored | 1 | unknown | not printed | not printed | not printed | not printed | 120 | not printed |  |
| MoonRide/gemma-4-31B-it-heretic-ara | 2 | Heretic, arbitrary-rank ablation | v1.2.0 | not printed | start_layer_index 30, end_layer_index 54 | preserve 0.1997, steer 0.0002, overcorrect 1.0020 | 44 | not printed |  |
| MoonRide/gemma-4-31B-it-heretic-ara-custom | 2 | Heretic, arbitrary-rank ablation | 1.2.0 | not printed | start layer 30, end layer 57 | preserve 0.2116, steer 0.0001, overcorrect 0.9635 | 48 | custom system prompt |  |
| coder3101/gemma-4-31B-it-heretic | 2 | Heretic, arbitrary-rank ablation | 1.2.0 | not printed | start layer 1, end layer 59 | preserve 0.8438, steer 0.0002, overcorrect 1.0760 | 58 | not printed |  |
| llmfan46/gemma-4-31B-it-uncensored-heretic | 2 | Heretic, arbitrary-rank ablation | 1.2.0 | not printed | start layer 30, end layer 48 | preserve 0.5437, steer 0.0005, overcorrect 0.9949 | 18 | not printed |  |
| akpsahan/Huihui-gemma-4-31B-it-abliterated-v2 | 3 | abliteration (remove-refusals code) | not printed | not printed | layers 5 to 59 | 1.5 | 110 | not printed | huihui-ai's card, byte-identical re-upload |
| huihui-ai/Huihui-gemma-4-31B-it-abliterated | 3 | abliteration (remove-refusals code) | not printed | not printed | not printed | 1.00 | 120 | not printed |  |
| huihui-ai/Huihui-gemma-4-31B-it-abliterated-v2 | 3 | abliteration (remove-refusals code) | not printed | not printed | layers 5 to 59 | 1.5 | 110 | not printed |  |
| prithivMLmods/gemma-4-31B-it-Uncensored-MAX | 3 | single shared-direction projection | not printed | not printed | not printed | 1.0 | 120 | not printed | re-shard of huihui-ai's first version, no weight changes |
| jcxu97/gemma-4-31B-it-abliterated | 4 | Abliterix, orthogonal projection | not printed | not printed | layers 27 to 59 | not printed | 120 | not printed | wangzhang's card, duplicate of wangzhang's export |
| wangzhang/gemma-4-31B-it-abliterated | 4 | Abliterix, orthogonal projection | not printed | not printed | not printed | not printed | 94 | not printed |  |
| DuoNeural/Gemma4-31B-IT-Abliterated | alone | orthogonal rank-1 projection | not printed | per layer | not printed | down_proj 0.4, o_proj 0.8 | 120 | not printed |  |
| cosmicoptima/gemma4-31b-consciousness-abliterated | alone | residual_writer_orthogonal_projection | not printed | not printed | not printed | alpha 1.0 | 121 | not printed |  |
| sh0ck0r/Artemis-31B-v1.1-heretic | alone | Heretic | 1.4.0 | not printed | attn 1.20 at 58.68, width 34.46; down 1.48 at 35.77, width 19.15 | not printed | 603 | not printed | edit over TheDrummer/Artemis-31B-v1.1 fine-tune |
| Bahushruth/gemma-4-31B-it-abliterated | partner under 0.9 | arbitrary-rank ablation (L-BFGS, Optuna) | not printed | not printed | layers 17 to 49 | not printed | 66 | 7,356 harmful |  |
| null-space/gemma-4-31b-it-abliterated | partner under 0.9 | 8-direction projection, projected orthogonalization | not printed | not printed | layers 20 to 59 | scale 0.35 to 1.35 per layer | 80 | 4,634 harmful and 640 harmless |  |
| Jim-darby/gemma-4-31B-it-heretic-ara-ja80en20 | partner under 0.9 | Heretic, arbitrary-rank ablation | 1.2.0 | not printed | start_layer_index 27, end_layer_index 47 | preserve 0.7927, steer 0.00012, overcorrect 0.0175 | 38 | 400 harmless and 400 harmful, 80 percent Japanese |  |
| nguyenthilaitrieulong/gemma-4-31B-it-abliterated | partner under 0.9 | five-surface edit (adapter, interpolation, ablation) | not printed | not printed | layers 55 to 59 | scale 1.5 | 77 | not printed | WWTCyberLab's card, duplicate re-upload |
| Kooten/gemma-4-31b-abliterated-v1.1 | partner under 0.9 | Heretic, linear kernel | not printed | not printed | not printed | not printed | 67 | not printed |  |

copies with a reading note: 25 of 25
copies with a version printed: 8
copies with a direction index printed: 4
copies with kernels printed: 5
