# mode-sizes -- every census copy joined to the size of its measured weight change.

| mode | copies | changed tensors (q1 / median / q3) | changed layers | median relative (q1 / median / q3) | max relative | singular share (q1 / median / q3) |
| --- | --- | --- | --- | --- | --- | --- |
| arbitrary rank | 65 | 17.000 / 24.000 / 38.000 | 17.000 | 0.023 / 0.030 / 0.037 | 0.060 | 0.022 / 0.466 / 0.862 |
| mixed | 12 | 44.000 / 55.000 / 349.500 | 32.500 | 0.013 / 0.019 / 0.026 | 0.034 | 0.194 / 0.918 / 0.987 |
| no file | 1 | 0.000 / 0.000 / 0.000 | 0.000 | none / none / none | none | none / none / none |
| one direction | 54 | 50.000 / 63.500 / 80.000 | 34.000 | 0.016 / 0.021 / 0.026 | 0.028 | 0.963 / 0.981 / 0.994 |
| per layer | 69 | 42.000 / 67.000 / 94.000 | 31.000 | 0.017 / 0.020 / 0.027 | 0.034 | 0.593 / 0.978 / 0.991 |

arbitrary rank copies with singular share 0.9 or more: 14 of 65; other-mode copies under 0.9: 43 of 135

## crossings

arbitrary rank copies with singular share 0.9 or more

| parent | copy | mode | changed tensors | changed layers | singular share | kinds |
| --- | --- | --- | --- | --- | --- | --- |
| google/gemma-4-12B-it | MeFFyLe/gemma-4-12B-it-uncensored-heretic | arbitrary rank | 16.000 | 16.000 | 0.914 | attention_output |
| google/gemma-4-12B-it | llmfan46/gemma-4-12B-it-uncensored-heretic | arbitrary rank | 16.000 | 16.000 | 0.914 | attention_output |
| google/gemma-4-12B-it-qat-q4_0-unquantized | wnfldchen/gemma-4-12B-it-qat-q4_0-unquantized-heretic | arbitrary rank | 46.000 | 23.000 | 0.975 | attention_output, feed_forward_down |
| google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | mewse/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ara | arbitrary rank | 24.000 | 12.000 | 0.932 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | llmfan46/gemma-4-31B-it-uncensored-heretic | arbitrary rank | 18.000 | 18.000 | 0.910 | attention_output |
| google/gemma-4-E2B-it | amkkk/Gemma4_E2B_Abliterated_Baked_HF_Ready | arbitrary rank | 96.000 | 24.000 | 0.977 | attention_output, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-E2B-it | llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic | arbitrary rank | 7.000 | 7.000 | 0.950 | attention_output |
| google/gemma-4-E2B-it | yuna1126/gemma-4-E2B-Tema_Q-Abliterated | arbitrary rank | 7.000 | 7.000 | 0.948 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | Cup4/gemma-4-E4B-it-uncensored-heretic | arbitrary rank | 11.000 | 11.000 | 0.920 | attention_output |
| google/gemma-4-E4B-it | Cup5/gemma-4-E4B-it-uncensored-heretic | arbitrary rank | 11.000 | 11.000 | 0.920 | attention_output |
| google/gemma-4-E4B-it | Pound1320/gemma-4-E4B-it-uncensored-heretic | arbitrary rank | 11.000 | 11.000 | 0.920 | attention_output |
| google/gemma-4-E4B-it | llmfan46/gemma-4-E4B-it-ultra-uncensored-heretic | arbitrary rank | 17.000 | 17.000 | 0.936 | attention_output |
| google/gemma-4-E4B-it | llmfan46/gemma-4-E4B-it-uncensored-heretic | arbitrary rank | 11.000 | 11.000 | 0.920 | attention_output |
| mistralai/Mistral-Small-3.2-24B-Instruct-2506 | llmfan46/Mistral-Small-3.2-24B-Instruct-2506-ultra-uncensored-heretic | arbitrary rank | 8.000 | 8.000 | 0.941 | attention_output |

other-mode copies with singular share under 0.9

| parent | copy | mode | changed tensors | changed layers | singular share | kinds |
| --- | --- | --- | --- | --- | --- | --- |
| google/gemma-4-E4B | Felldude/gemma-4-E4B-uncensored | mixed | 595.000 | 42.000 | 0.002 | attention_key, attention_output, attention_query, attention_value, embedding, feed_forward_down, feed_forward_gate, feed_forward_up, final_normalization, input_normalization, other, post_attention_normalization |
| google/gemma-4-12B-it | lemuralabs/Gemma-4-12B-uncensored-bf16 | mixed | 553.000 | 48.000 | 0.001 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up, final_normalization, input_normalization, other, post_attention_normalization |
| coder3101/gemma-3-27b-it-heretic | DavidAU/Gemma-3-27b-it-Gemini-Heretic-Uncensored-Deeper-Reasoning-Series2 | mixed | 432.000 | 62.000 | 0.282 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | tpls/gemma-4-12B-coder-fable5-composer2.5-v1-abliterated | mixed | 322.000 | 48.000 | 0.001 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| mistralai/Mistral-Small-3.2-24B-Instruct-2506 | coder3101/Mistral-Small-3.2-24B-Instruct-2506-heretic | mixed | 50.000 | 38.000 | 0.856 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | AEON-7/Gemma-4-12B-it-AEON-Abliterated-K4-BF16 | mixed | 48.000 | 24.000 | 0.258 | attention_output, feed_forward_down |
| yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic | one direction | 557.000 | 48.000 | 0.025 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up, final_normalization, input_normalization, other, post_attention_normalization |
| google/gemma-4-12B-it | jwest33/gemma-4-12B-it-null-space-abliterated | one direction | 329.000 | 48.000 | 0.802 | attention_key, attention_output, attention_query, attention_value, embedding, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-31B-it | Kooten/gemma-4-31b-abliterated-v1.1 | one direction | 256.000 | 60.000 | 0.005 | attention_output, feed_forward_down, other |
| mistralai/Mistral-7B-Instruct-v0.3 | 3MPER0RR/Mistral-7B-v0.3-3MPER0RR-abliterated | one direction | 226.000 | 32.000 | 0.005 | attention_key, attention_output, attention_query, attention_value, embedding, feed_forward_down, feed_forward_gate, feed_forward_up, output_head |
| google/gemma-4-31B-it | null-space/gemma-4-31b-it-abliterated | one direction | 80.000 | 40.000 | 0.584 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | Vampelium/gemma-4-12B-it-heretic | one direction | 75.000 | 43.000 | 0.794 | attention_output, feed_forward_down |
| TheDrummer/Cydonia-24B-v4.3 | coder3101/Cydonia-24B-v4.3-heretic-v4 | one direction | 65.000 | 36.000 | 0.852 | attention_output, feed_forward_down |
| TheDrummer/Cydonia-24B-v4.3 | coder3101/Cydonia-24B-v4.3-heretic-v2 | one direction | 57.000 | 33.000 | 0.756 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | BinxNet/gemma-4-12B-it-heretic | one direction | 55.000 | 44.000 | 0.839 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | sh0ck0r/Artemis-31B-v1.1-heretic | per layer | 603.000 | 60.000 | 0.001 | attention_key, attention_output, attention_query, attention_value, embedding, feed_forward_down, feed_forward_gate, feed_forward_up, other |
| google/gemma-4-E4B-it | Felldude/gemma-4-E4B-uncensored | per layer | 595.000 | 42.000 | 0.002 | attention_key, attention_output, attention_query, attention_value, embedding, feed_forward_down, feed_forward_gate, feed_forward_up, final_normalization, input_normalization, other, post_attention_normalization |
| google/gemma-4-12B-it | richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic | per layer | 557.000 | 48.000 | 0.025 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up, final_normalization, input_normalization, other, post_attention_normalization |
| google/gemma-4-12B-it | Paul691/gemma-4-12B-it-abliterated-uncensored | per layer | 553.000 | 48.000 | 0.001 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up, final_normalization, input_normalization, other, post_attention_normalization |
| google/gemma-4-E4B-it | Ilya626/gemma-4-E4B-it-SDFT_Heretic_RP | per layer | 526.000 | 42.000 | 0.005 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up, other |
| coder3101/gemma-3-27b-it-heretic | Justbackup/Gemma-3-27b-it-Uncensored-HERETIC-Gemini-Deep-Reasoning | per layer | 418.000 | 62.000 | 0.239 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-12B-it | enkato64bit/SuperGemma-4-12b-abliterated | per layer | 320.000 | 48.000 | 0.119 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-E4B-it | Dingdust/ContextPilot-E4B-heretic | per layer | 285.000 | 42.000 | 0.003 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up, other |
| mistralai/Mistral-Small-3.2-24B-Instruct-2506 | Pranavz/Hearthfire-24B-heretic | per layer | 282.000 | 40.000 | 0.004 | attention_key, attention_output, attention_query, attention_value, embedding, feed_forward_down, feed_forward_gate, feed_forward_up, output_head |
| mistralai/Ministral-3-8B-Reasoning-2512 | ccharnkij/Ministral-3-8B-Reasoning-2512-Uncensored | per layer | 238.000 | 34.000 | 0.146 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-E2B-it | aifeifei798/Heretic-Scalpel-E2B | per layer | 179.000 | 35.000 | 0.113 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-26B-A4B-it | DuoNeural/gemma-4-26B-A4B-it-abliterated | per layer | 90.000 | 30.000 | 0.881 | attention_output, expert_down, feed_forward_down |
| google/gemma-4-26B-A4B-it | claymorecrystal/gemma-4-26B-A4B-it-uncensored | per layer | 90.000 | 30.000 | 0.881 | attention_output, expert_down, feed_forward_down |
| google/gemma-4-26B-A4B-it | erunda337/gemma-4-26B-A4B-it-uncensored | per layer | 90.000 | 30.000 | 0.881 | attention_output, expert_down, feed_forward_down |
| google/gemma-4-26B-A4B-it | sitten1/gemma-4-26B-A4B-it-uncensored | per layer | 90.000 | 30.000 | 0.881 | attention_output, expert_down, feed_forward_down |
| google/gemma-4-31B-it | nguyenthilaitrieulong/gemma-4-31B-it-abliterated | per layer | 77.000 | 32.000 | 0.362 | attention_key, attention_output, attention_query, embedding, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-E4B-it | TheUmbraWalker/gemma-4-E4B-it-2-heretic | per layer | 73.000 | 38.000 | 0.504 | attention_output, feed_forward_down |
| google/diffusiongemma-26B-A4B-it | FredyRivera-dev/diffusiongemma-26B-A4B-it-HERETIC-Uncensored | per layer | 67.000 | 25.000 | 0.002 | attention_output, expert_down, feed_forward_down |
| google/diffusiongemma-26B-A4B-it | nnnxnsn/diffusiongemma-26B-A4B-it-HERETIC-Uncensored | per layer | 67.000 | 25.000 | 0.002 | attention_output, expert_down, feed_forward_down |
| google/gemma-4-26B-A4B-it | WWTCyberLab/gemma-4-26B-A4B-it-abliterated | per layer | 55.000 | 18.000 | 0.245 | attention_output, embedding, expert_down, feed_forward_down |
| google/gemma-4-E2B-it | treadon/gemma4-E2B-it-Abliterated-AND-Disinhibited-USE-THIS | per layer | 48.000 | 24.000 | 0.538 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | Vampelium/gemma-4-31B-it-heretic | per layer | 47.000 | 26.000 | 0.792 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | Carlosian/Gemma-4-12b-it-Abliterated | per layer | 42.000 | 21.000 | 0.593 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | treadon/gemma4-E4B-it-Abliterated-AND-Disinhibited-USE-THIS | per layer | 42.000 | 21.000 | 0.659 | attention_output, feed_forward_down |
| TheDrummer/Cydonia-24B-v4.3 | coder3101/Cydonia-24B-v4.3-heretic | per layer | 37.000 | 31.000 | 0.891 | attention_output, feed_forward_down |
| google/gemma-4-26B-A4B-it | keithtyser/gemma-4-26B-A4B-it-local-abliterated-sota-internal-t34 | per layer | 35.000 | 18.000 | 0.834 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | Sabomako/gemma-4-12B-it-heretic | per layer | 31.000 | 19.000 | 0.741 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | Sabomako/gemma-4-31B-it-heretic | per layer | 8.000 | 4.000 | 0.734 | attention_output, feed_forward_down |

## per parent

| parent | mode | copies | changed tensors | median relative | singular share |
| --- | --- | --- | --- | --- | --- |
| TheDrummer/Cydonia-24B-v4.3 | one direction | 3 | 65.000 | 0.013 | 0.852 |
| TheDrummer/Cydonia-24B-v4.3 | per layer | 1 | 37.000 | 0.016 | 0.891 |
| TheDrummer/Magidonia-24B-v4.3 | one direction | 2 | 53.500 | 0.016 | 0.942 |
| TheDrummer/Magidonia-24B-v4.3 | per layer | 1 | 32.000 | 0.015 | 0.981 |
| coder3101/gemma-3-27b-it-heretic | mixed | 1 | 432.000 | 0.006 | 0.282 |
| coder3101/gemma-3-27b-it-heretic | per layer | 1 | 418.000 | 0.003 | 0.239 |
| google/diffusiongemma-26B-A4B-it | arbitrary rank | 2 | 29.000 | 0.018 | 0.013 |
| google/diffusiongemma-26B-A4B-it | per layer | 2 | 67.000 | 0.020 | 0.002 |
| google/gemma-4-12B-it | arbitrary rank | 7 | 40.000 | 0.018 | 0.005 |
| google/gemma-4-12B-it | mixed | 2 | 300.500 | 0.018 | 0.129 |
| google/gemma-4-12B-it | one direction | 7 | 55.000 | 0.020 | 0.978 |
| google/gemma-4-12B-it | per layer | 13 | 66.000 | 0.017 | 0.990 |
| google/gemma-4-12B-it-qat-q4_0-unquantized | arbitrary rank | 6 | 35.000 | 0.026 | 0.728 |
| google/gemma-4-12B-it-qat-q4_0-unquantized | mixed | 1 | 28.000 | 0.020 | 0.992 |
| google/gemma-4-12B-it-qat-q4_0-unquantized | one direction | 1 | 49.000 | 0.025 | 0.980 |
| google/gemma-4-12B-it-qat-q4_0-unquantized | per layer | 2 | 62.500 | 0.023 | 0.992 |
| google/gemma-4-26B-A4B-it | arbitrary rank | 3 | 27.000 | 0.022 | 0.836 |
| google/gemma-4-26B-A4B-it | one direction | 3 | 50.000 | 0.057 | 0.999 |
| google/gemma-4-26B-A4B-it | per layer | 12 | 51.500 | 0.020 | 0.924 |
| google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | arbitrary rank | 5 | 16.000 | 0.052 | 0.444 |
| google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | mixed | 1 | 60.000 | 0.067 | 0.999 |
| google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | one direction | 1 | 52.000 | 0.026 | 0.976 |
| google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | per layer | 1 | 90.000 | 0.020 | 0.946 |
| google/gemma-4-31B-it | arbitrary rank | 6 | 46.000 | 0.025 | 0.003 |
| google/gemma-4-31B-it | mixed | 1 | 41.000 | 0.019 | 0.981 |
| google/gemma-4-31B-it | one direction | 7 | 120.000 | 0.014 | 0.989 |
| google/gemma-4-31B-it | per layer | 11 | 94.000 | 0.017 | 0.947 |
| google/gemma-4-31B-it-qat-q4_0-unquantized | arbitrary rank | 4 | 21.500 | 0.031 | 0.589 |
| google/gemma-4-E2B-it | arbitrary rank | 7 | 18.000 | 0.023 | 0.274 |
| google/gemma-4-E2B-it | one direction | 6 | 49.500 | 0.030 | 0.996 |
| google/gemma-4-E2B-it | per layer | 10 | 70.000 | 0.035 | 0.988 |
| google/gemma-4-E4B | mixed | 1 | 595.000 | 0.422 | 0.002 |
| google/gemma-4-E4B | per layer | 1 | 23.000 | 0.024 | 0.986 |
| google/gemma-4-E4B-it | arbitrary rank | 18 | 24.500 | 0.036 | 0.361 |
| google/gemma-4-E4B-it | mixed | 1 | 23.000 | 0.024 | 0.986 |
| google/gemma-4-E4B-it | no file | 1 | 0.000 | none | none |
| google/gemma-4-E4B-it | one direction | 10 | 68.000 | 0.024 | 0.977 |
| google/gemma-4-E4B-it | per layer | 9 | 84.000 | 0.022 | 0.659 |
| google/gemma-4-E4B-it-qat-q4_0-unquantized | arbitrary rank | 2 | 24.000 | 0.068 | 0.553 |
| google/gemma-4-E4B-it-qat-q4_0-unquantized | one direction | 1 | 54.000 | 0.023 | 0.992 |
| inflatebot/MN-12B-Mag-Mell-R1 | one direction | 2 | 80.000 | 0.019 | 0.992 |
| mistralai/Magistral-Small-2509 | arbitrary rank | 2 | 33.500 | 0.020 | 0.794 |
| mistralai/Magistral-Small-2509 | one direction | 1 | 64.000 | 0.018 | 0.967 |
| mistralai/Ministral-3-8B-Reasoning-2512 | mixed | 1 | 45.000 | 0.022 | 0.989 |
| mistralai/Ministral-3-8B-Reasoning-2512 | per layer | 1 | 238.000 | 0.010 | 0.146 |
| mistralai/Mistral-7B-Instruct-v0.3 | one direction | 5 | 48.000 | 0.019 | 0.976 |
| mistralai/Mistral-Nemo-Instruct-2407 | mixed | 1 | 70.000 | 0.015 | 0.987 |
| mistralai/Mistral-Nemo-Instruct-2407 | one direction | 1 | 80.000 | 0.004 | 0.916 |
| mistralai/Mistral-Small-3.2-24B-Instruct-2506 | arbitrary rank | 1 | 8.000 | 0.066 | 0.941 |
| mistralai/Mistral-Small-3.2-24B-Instruct-2506 | mixed | 1 | 50.000 | 0.017 | 0.856 |
| mistralai/Mistral-Small-3.2-24B-Instruct-2506 | one direction | 1 | 80.000 | 0.016 | 0.987 |
| mistralai/Mistral-Small-3.2-24B-Instruct-2506 | per layer | 2 | 174.500 | 0.015 | 0.495 |
| yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2 | one direction | 1 | 67.000 | 0.024 | 0.988 |
| yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2 | per layer | 1 | 12.000 | 0.020 | 0.991 |
| yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | mixed | 1 | 322.000 | 0.001 | 0.001 |
| yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | one direction | 2 | 321.000 | 0.011 | 0.504 |
| yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | per layer | 1 | 12.000 | 0.021 | 0.993 |
| zerofata/MS3.2-PaintedFantasy-v4.1-24B | arbitrary rank | 2 | 18.000 | 0.033 | 0.654 |

## per copy

| parent | copy | mode | changed tensors | changed layers | median relative | max relative | singular share | kinds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TheDrummer/Cydonia-24B-v4.3 | coder3101/Cydonia-24B-v4.3-heretic | per layer | 37.000 | 31.000 | 0.016 | 0.026 | 0.891 | attention_output, feed_forward_down |
| TheDrummer/Cydonia-24B-v4.3 | coder3101/Cydonia-24B-v4.3-heretic-v2 | one direction | 57.000 | 33.000 | 0.013 | 0.019 | 0.756 | attention_output, feed_forward_down |
| TheDrummer/Cydonia-24B-v4.3 | coder3101/Cydonia-24B-v4.3-heretic-v3 | one direction | 74.000 | 37.000 | 0.013 | 0.020 | 0.961 | attention_output, feed_forward_down |
| TheDrummer/Cydonia-24B-v4.3 | coder3101/Cydonia-24B-v4.3-heretic-v4 | one direction | 65.000 | 36.000 | 0.011 | 0.021 | 0.852 | attention_output, feed_forward_down |
| TheDrummer/Magidonia-24B-v4.3 | coder3101/Magidonia-24B-v4.3-heretic | per layer | 32.000 | 24.000 | 0.015 | 0.026 | 0.981 | attention_output, feed_forward_down |
| TheDrummer/Magidonia-24B-v4.3 | coder3101/Magidonia-24B-v4.3-heretic-v2 | one direction | 44.000 | 32.000 | 0.017 | 0.022 | 0.923 | attention_output, feed_forward_down |
| TheDrummer/Magidonia-24B-v4.3 | grayarea/Magidonia-24B-v4.3-heretic-v1.2 | one direction | 63.000 | 34.000 | 0.015 | 0.024 | 0.961 | attention_output, feed_forward_down |
| coder3101/gemma-3-27b-it-heretic | DavidAU/Gemma-3-27b-it-Gemini-Heretic-Uncensored-Deeper-Reasoning-Series2 | mixed | 432.000 | 62.000 | 0.006 | 0.070 | 0.282 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| coder3101/gemma-3-27b-it-heretic | Justbackup/Gemma-3-27b-it-Uncensored-HERETIC-Gemini-Deep-Reasoning | per layer | 418.000 | 62.000 | 0.003 | 0.041 | 0.239 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/diffusiongemma-26B-A4B-it | FredyRivera-dev/diffusiongemma-26B-A4B-it-HERETIC-Uncensored | per layer | 67.000 | 25.000 | 0.020 | 0.041 | 0.002 | attention_output, expert_down, feed_forward_down |
| google/diffusiongemma-26B-A4B-it | Goodoldjam/DiffusionGemma-26B-E38-Abliterated-BF16 | arbitrary rank | 20.000 | 10.000 | 0.025 | 0.047 | 0.005 | attention_output, feed_forward_down |
| google/diffusiongemma-26B-A4B-it | Umranz/diffusiongemma-26B-A4B-it-abliteration | arbitrary rank | 38.000 | 19.000 | 0.011 | 0.047 | 0.022 | attention_output, feed_forward_down |
| google/diffusiongemma-26B-A4B-it | nnnxnsn/diffusiongemma-26B-A4B-it-HERETIC-Uncensored | per layer | 67.000 | 25.000 | 0.020 | 0.041 | 0.002 | attention_output, expert_down, feed_forward_down |
| google/gemma-4-12B-it | 3MPER0RR/gemma-4-12b-it-3MPER0RR-abliterated | one direction | 48.000 | 29.000 | 0.022 | 0.033 | 0.980 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | AEON-7/Gemma-4-12B-it-AEON-Abliterated-K4-BF16 | mixed | 48.000 | 24.000 | 0.033 | 0.034 | 0.258 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | AlekseyCalvin/Lyrical_Translator_ru2en_on_Gemma4_12b_heretic_SFT_Run2 | arbitrary rank | 328.000 | 48.000 | 0.037 | 0.100 | 0.129 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-12B-it | BinxNet/gemma-4-12B-it-heretic | one direction | 55.000 | 44.000 | 0.021 | 0.032 | 0.839 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | Carlosian/Gemma-4-12b-it-Abliterated | per layer | 42.000 | 21.000 | 0.025 | 0.034 | 0.593 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | Iambackup/gemma-4-12B-it-uncensored | per layer | 66.000 | 33.000 | 0.017 | 0.021 | 0.990 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | Ishowbackup/Huihui-gemma-4-12B-it-abliterated | per layer | 12.000 | 6.000 | 0.021 | 0.031 | 0.994 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | Ishowbackup/gemma-4-12B-it-uncensored | per layer | 66.000 | 33.000 | 0.017 | 0.021 | 0.990 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | Justbackup/gemma-4-12B-it-uncensored | per layer | 66.000 | 33.000 | 0.017 | 0.021 | 0.990 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | MeFFyLe/gemma-4-12B-it-uncensored-heretic | arbitrary rank | 16.000 | 16.000 | 0.032 | 0.070 | 0.914 | attention_output |
| google/gemma-4-12B-it | MoonRide/gemma-4-12B-it-heretic | one direction | 52.000 | 31.000 | 0.022 | 0.031 | 0.978 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | Paul691/gemma-4-12B-it-abliterated-uncensored | per layer | 553.000 | 48.000 | 0.003 | 0.086 | 0.001 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up, final_normalization, input_normalization, other, post_attention_normalization |
| google/gemma-4-12B-it | RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals2 | arbitrary rank | 40.000 | 20.000 | 0.011 | 0.028 | 0.005 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals4 | arbitrary rank | 26.000 | 13.000 | 0.015 | 0.031 | 0.002 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals9 | arbitrary rank | 55.000 | 30.000 | 0.009 | 0.018 | 0.002 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | Sabomako/gemma-4-12B-it-heretic | per layer | 31.000 | 19.000 | 0.004 | 0.128 | 0.741 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | TimelessSoul/Huihui-gemma-4-12B-it-abliterated | per layer | 12.000 | 6.000 | 0.021 | 0.031 | 0.994 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | TrevorJS/gemma-4-12B-it-uncensored | per layer | 66.000 | 33.000 | 0.017 | 0.021 | 0.990 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | Vampelium/gemma-4-12B-it-heretic | one direction | 75.000 | 43.000 | 0.014 | 0.024 | 0.794 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | coder3101/gemma-4-12B-it-heretic | arbitrary rank | 86.000 | 43.000 | 0.018 | 0.076 | 0.002 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | enkato64bit/SuperGemma-4-12b-abliterated | per layer | 320.000 | 48.000 | 0.003 | 0.013 | 0.119 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-12B-it | huihui-ai/Huihui-gemma-4-12B-it-abliterated | per layer | 12.000 | 6.000 | 0.021 | 0.031 | 0.994 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | igorls/gemma-4-12B-it-heretic-v1 | one direction | 22.000 | 16.000 | 0.020 | 0.025 | 0.981 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | jwest33/gemma-4-12B-it-null-space-abliterated | one direction | 329.000 | 48.000 | 0.008 | 0.022 | 0.802 | attention_key, attention_output, attention_query, attention_value, embedding, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-12B-it | laladream/gemma-4-12B-it-uncensored | per layer | 66.000 | 33.000 | 0.017 | 0.021 | 0.990 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | lemuralabs/Gemma-4-12B-uncensored-bf16 | mixed | 553.000 | 48.000 | 0.003 | 0.086 | 0.001 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up, final_normalization, input_normalization, other, post_attention_normalization |
| google/gemma-4-12B-it | llmfan46/gemma-4-12B-it-uncensored-heretic | arbitrary rank | 16.000 | 16.000 | 0.032 | 0.070 | 0.914 | attention_output |
| google/gemma-4-12B-it | prithivMLmods/gemma-4-12B-it-heretic_decensored | one direction | 56.000 | 33.000 | 0.020 | 0.025 | 0.980 | attention_output, feed_forward_down |
| google/gemma-4-12B-it | richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic | per layer | 557.000 | 48.000 | 0.005 | 0.086 | 0.025 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up, final_normalization, input_normalization, other, post_attention_normalization |
| google/gemma-4-12B-it-qat-q4_0-unquantized | JJaguar/gemma-4-12B-it-qat-q4_0-unquantized-heretic-nx | one direction | 49.000 | 27.000 | 0.025 | 0.033 | 0.980 | attention_output, feed_forward_down |
| google/gemma-4-12B-it-qat-q4_0-unquantized | OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-heretic-ja | arbitrary rank | 73.000 | 37.000 | 0.041 | 0.088 | 0.657 | attention_output, feed_forward_down |
| google/gemma-4-12B-it-qat-q4_0-unquantized | OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-heretic-ja-v2 | arbitrary rank | 54.000 | 27.000 | 0.028 | 0.052 | 0.363 | attention_output, feed_forward_down |
| google/gemma-4-12B-it-qat-q4_0-unquantized | OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic-v3 | arbitrary rank | 18.000 | 9.000 | 0.022 | 0.055 | 0.798 | attention_output, feed_forward_down |
| google/gemma-4-12B-it-qat-q4_0-unquantized | coder3101/gemma-4-12B-it-qat-q4_0-unquantized-heretic | arbitrary rank | 24.000 | 24.000 | 0.024 | 0.082 | 0.529 | attention_output |
| google/gemma-4-12B-it-qat-q4_0-unquantized | huihui-ai/Huihui-gemma-4-12B-it-qat-q4_0-unquantized-abliterated | mixed | 28.000 | 14.000 | 0.020 | 0.027 | 0.992 | attention_output, feed_forward_down |
| google/gemma-4-12B-it-qat-q4_0-unquantized | igorls/gemma-4-12B-it-qat-q4_0-unquantized-heretic | per layer | 57.000 | 32.000 | 0.025 | 0.034 | 0.995 | attention_output, feed_forward_down |
| google/gemma-4-12B-it-qat-q4_0-unquantized | llmfan46/gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic | arbitrary rank | 11.000 | 11.000 | 0.030 | 0.060 | 0.845 | attention_output |
| google/gemma-4-12B-it-qat-q4_0-unquantized | smashingtags/gemma-4-12b-it-abliterated | per layer | 68.000 | 34.000 | 0.020 | 0.051 | 0.990 | attention_output, feed_forward_down |
| google/gemma-4-12B-it-qat-q4_0-unquantized | wnfldchen/gemma-4-12B-it-qat-q4_0-unquantized-heretic | arbitrary rank | 46.000 | 23.000 | 0.022 | 0.103 | 0.975 | attention_output, feed_forward_down |
| google/gemma-4-26B-A4B-it | BinxNet/gemma-4-26B-A4B-it-heretic | per layer | 44.000 | 25.000 | 0.029 | 0.046 | 0.985 | attention_output, feed_forward_down |
| google/gemma-4-26B-A4B-it | DuoNeural/gemma-4-26B-A4B-it-abliterated | per layer | 90.000 | 30.000 | 0.020 | 0.030 | 0.881 | attention_output, expert_down, feed_forward_down |
| google/gemma-4-26B-A4B-it | Rootkit7/Gemma-4-26B-A4B-abliterated | per layer | 48.000 | 16.000 | 0.020 | 0.028 | 0.978 | attention_output, expert_down, feed_forward_down |
| google/gemma-4-26B-A4B-it | SassyDiffusion/gemma-4-26B-A4B-it-heretic-ara | arbitrary rank | 35.000 | 22.000 | 0.029 | 0.060 | 0.894 | attention_output, feed_forward_down |
| google/gemma-4-26B-A4B-it | SevenOfNine/Gemma-4-26B-A4B-It-Abliterated | per layer | 40.000 | 26.000 | 0.030 | 0.047 | 0.991 | attention_output, feed_forward_down |
| google/gemma-4-26B-A4B-it | TrevorJS/gemma-4-26B-A4B-it-uncensored | per layer | 90.000 | 30.000 | 0.020 | 0.030 | 0.991 | attention_output, expert_down, feed_forward_down |
| google/gemma-4-26B-A4B-it | WWTCyberLab/gemma-4-26B-A4B-it-abliterated | per layer | 55.000 | 18.000 | 0.022 | 0.080 | 0.245 | attention_output, embedding, expert_down, feed_forward_down |
| google/gemma-4-26B-A4B-it | claymorecrystal/gemma-4-26B-A4B-it-uncensored | per layer | 90.000 | 30.000 | 0.020 | 0.030 | 0.881 | attention_output, expert_down, feed_forward_down |
| google/gemma-4-26B-A4B-it | coder3101/gemma-4-26B-A4B-it-heretic | arbitrary rank | 20.000 | 20.000 | 0.019 | 0.038 | 0.659 | attention_output |
| google/gemma-4-26B-A4B-it | erunda337/gemma-4-26B-A4B-it-uncensored | per layer | 90.000 | 30.000 | 0.020 | 0.030 | 0.881 | attention_output, expert_down, feed_forward_down |
| google/gemma-4-26B-A4B-it | huihui-ai/Huihui-gemma-4-26B-A4B-it-abliterated | one direction | 50.000 | 25.000 | 0.057 | 0.094 | 0.999 | attention_output, feed_forward_down |
| google/gemma-4-26B-A4B-it | keithtyser/gemma-4-26B-A4B-it-local-abliterated-sota-internal-t34 | per layer | 35.000 | 18.000 | 0.017 | 0.030 | 0.834 | attention_output, feed_forward_down |
| google/gemma-4-26B-A4B-it | llmfan46/gemma-4-26B-A4B-it-uncensored-heretic | arbitrary rank | 27.000 | 27.000 | 0.022 | 0.038 | 0.836 | attention_output |
| google/gemma-4-26B-A4B-it | prithivMLmods/gemma-4-26B-A4B-Heretic-Stable | one direction | 50.000 | 25.000 | 0.057 | 0.094 | 0.999 | attention_output, feed_forward_down |
| google/gemma-4-26B-A4B-it | prithivMLmods/gemma-4-26B-A4B-it-Uncensored-MAX | one direction | 50.000 | 25.000 | 0.057 | 0.094 | 0.999 | attention_output, feed_forward_down |
| google/gemma-4-26B-A4B-it | sh0ck0r/gemma-4-26B-A4B-it-heretic | per layer | 38.000 | 21.000 | 0.026 | 0.036 | 0.967 | attention_output, feed_forward_down |
| google/gemma-4-26B-A4B-it | sitten1/gemma-4-26B-A4B-it-uncensored | per layer | 90.000 | 30.000 | 0.020 | 0.030 | 0.881 | attention_output, expert_down, feed_forward_down |
| google/gemma-4-26B-A4B-it | tvall43/gemma-4-26B-A4B-it-heretic | per layer | 14.000 | 14.000 | 0.084 | 0.094 | 1.000 | attention_output |
| google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | Mitchins/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic | one direction | 52.000 | 27.000 | 0.026 | 0.039 | 0.976 | attention_output, expert_down, feed_forward_down |
| google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | OS-Software/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ja | arbitrary rank | 32.000 | 16.000 | 0.052 | 0.077 | 0.386 | attention_output, feed_forward_down |
| google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | OS-Software/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic-v2 | arbitrary rank | 16.000 | 8.000 | 0.056 | 0.076 | 0.748 | attention_output, feed_forward_down |
| google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | coder3101/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic | arbitrary rank | 9.000 | 9.000 | 0.025 | 0.047 | 0.444 | attention_output |
| google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | eadx/Huihui-gemma-4-26B-A4B-it-qat-q4_0-unquantized-abliterated | mixed | 60.000 | 30.000 | 0.067 | 0.113 | 0.999 | attention_output, feed_forward_down |
| google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | llmfan46/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic | arbitrary rank | 12.000 | 12.000 | 0.027 | 0.050 | 0.379 | attention_output |
| google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | mewse/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ara | arbitrary rank | 24.000 | 12.000 | 0.059 | 0.118 | 0.932 | attention_output, feed_forward_down |
| google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | xdavxd/gemma-4-26B-A4B-it-qat-heretic-ega | per layer | 90.000 | 30.000 | 0.020 | 0.031 | 0.946 | attention_output, expert_down, feed_forward_down |
| google/gemma-4-31B-it | 3MPER0RR/gemma-4-31b-it-3MPER0RR-abliterated | mixed | 41.000 | 21.000 | 0.019 | 0.024 | 0.981 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | Bahushruth/gemma-4-31B-it-abliterated | arbitrary rank | 66.000 | 33.000 | 0.044 | 0.120 | 0.343 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | DuoNeural/Gemma4-31B-IT-Abliterated | per layer | 120.000 | 60.000 | 0.012 | 0.045 | 0.947 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | Jim-darby/gemma-4-31B-it-heretic-ara-ja80en20 | arbitrary rank | 38.000 | 20.000 | 0.011 | 0.021 | 0.003 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | Kooten/gemma-4-31b-abliterated-v1.1 | one direction | 256.000 | 60.000 | 1.206 | 1.644 | 0.005 | attention_output, feed_forward_down, other |
| google/gemma-4-31B-it | MoonRide/gemma-4-31B-it-heretic-ara | arbitrary rank | 44.000 | 24.000 | 0.027 | 0.070 | 0.001 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | MoonRide/gemma-4-31B-it-heretic-ara-custom | arbitrary rank | 48.000 | 27.000 | 0.023 | 0.048 | 0.001 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | Sabomako/gemma-4-31B-it-heretic | per layer | 8.000 | 4.000 | 0.022 | 0.090 | 0.734 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | TrevorJS/gemma-4-31B-it-uncensored | per layer | 120.000 | 60.000 | 0.015 | 0.025 | 0.975 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | Vampelium/gemma-4-31B-it-heretic | per layer | 47.000 | 26.000 | 0.017 | 0.025 | 0.792 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | akpsahan/Huihui-gemma-4-31B-it-abliterated-v2 | one direction | 110.000 | 55.000 | 0.021 | 0.027 | 0.994 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | callmegrr/gemma-4-31B-it-heretic-z | per layer | 12.000 | 10.000 | 0.012 | 0.020 | 0.914 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | coder3101/gemma-4-31B-it-heretic | arbitrary rank | 58.000 | 58.000 | 0.019 | 0.169 | 0.002 | attention_output |
| google/gemma-4-31B-it | cosmicoptima/gemma4-31b-consciousness-abliterated | one direction | 121.000 | 60.000 | 0.014 | 0.019 | 0.988 | attention_output, embedding, feed_forward_down |
| google/gemma-4-31B-it | germlag/gemma-4-31B-it-heretic-v2 | per layer | 65.000 | 34.000 | 0.020 | 0.027 | 0.993 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | huihui-ai/Huihui-gemma-4-31B-it-abliterated | one direction | 120.000 | 60.000 | 0.014 | 0.016 | 0.989 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | huihui-ai/Huihui-gemma-4-31B-it-abliterated-v2 | one direction | 110.000 | 55.000 | 0.021 | 0.027 | 0.994 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | jcxu97/gemma-4-31B-it-abliterated | per layer | 120.000 | 33.000 | 0.049 | 0.076 | 0.993 | attention_key, attention_output, attention_query, attention_value, feed_forward_down |
| google/gemma-4-31B-it | llmfan46/gemma-4-31B-it-uncensored-heretic | arbitrary rank | 18.000 | 18.000 | 0.027 | 0.075 | 0.910 | attention_output |
| google/gemma-4-31B-it | nguyenthilaitrieulong/gemma-4-31B-it-abliterated | per layer | 77.000 | 32.000 | 0.015 | 0.031 | 0.362 | attention_key, attention_output, attention_query, embedding, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-31B-it | null-space/gemma-4-31b-it-abliterated | one direction | 80.000 | 40.000 | 0.007 | 0.027 | 0.584 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | prithivMLmods/gemma-4-31B-it-Uncensored-MAX | one direction | 120.000 | 60.000 | 0.014 | 0.016 | 0.989 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | ressl/gemma-4-31B-it-uncensored | per layer | 120.000 | 60.000 | 0.015 | 0.025 | 0.975 | attention_output, feed_forward_down |
| google/gemma-4-31B-it | sh0ck0r/Artemis-31B-v1.1-heretic | per layer | 603.000 | 60.000 | 0.094 | 0.104 | 0.001 | attention_key, attention_output, attention_query, attention_value, embedding, feed_forward_down, feed_forward_gate, feed_forward_up, other |
| google/gemma-4-31B-it | wangzhang/gemma-4-31B-it-abliterated | per layer | 94.000 | 40.000 | 0.048 | 0.091 | 0.984 | attention_key, attention_output, attention_query, attention_value |
| google/gemma-4-31B-it-qat-q4_0-unquantized | OS-Software/gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic | arbitrary rank | 22.000 | 11.000 | 0.027 | 0.040 | 0.549 | attention_output, feed_forward_down |
| google/gemma-4-31B-it-qat-q4_0-unquantized | coder3101/gemma-4-31B-it-qat-q4_0-unquantized-heretic | arbitrary rank | 21.000 | 21.000 | 0.026 | 0.054 | 0.003 | attention_output |
| google/gemma-4-31B-it-qat-q4_0-unquantized | llmfan46/gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic | arbitrary rank | 16.000 | 16.000 | 0.035 | 0.066 | 0.877 | attention_output |
| google/gemma-4-31B-it-qat-q4_0-unquantized | wnfldchen/gemma-4-31B-it-qat-q4_0-unquantized-heretic-merged | arbitrary rank | 30.000 | 30.000 | 0.075 | 0.416 | 0.628 | attention_output |
| google/gemma-4-E2B-it | Bahushruth/gemma-4-E2B-it-abliterated | arbitrary rank | 18.000 | 9.000 | 0.046 | 0.083 | 0.274 | attention_output, feed_forward_down |
| google/gemma-4-E2B-it | DavidAU/gemma-4-E2B-it-The-DECKARD-HERETIC-UNCENSORED-Thinking | arbitrary rank | 205.000 | 35.000 | 0.007 | 0.048 | 0.273 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-E2B-it | DuoNeural/Gemma-4-E2B-Heretic | one direction | 49.000 | 29.000 | 0.029 | 0.036 | 0.994 | attention_output, feed_forward_down |
| google/gemma-4-E2B-it | Dzluck/gemma-4-E2B-it-abliterated-v2 | one direction | 60.000 | 30.000 | 0.064 | 0.070 | 0.999 | attention_output, feed_forward_down |
| google/gemma-4-E2B-it | Ishowbackup/gemma-4-E2B-it-uncensored | per layer | 70.000 | 35.000 | 0.027 | 0.034 | 0.988 | attention_output, feed_forward_down |
| google/gemma-4-E2B-it | MoonRide/gemma-4-E2B-it-heretic | one direction | 44.000 | 24.000 | 0.031 | 0.035 | 0.997 | attention_output, feed_forward_down |
| google/gemma-4-E2B-it | MoonRide/gemma-4-E2B-it-heretic-ara | arbitrary rank | 16.000 | 8.000 | 0.021 | 0.040 | 0.003 | attention_output, feed_forward_down |
| google/gemma-4-E2B-it | MoonRide/gemma-4-E2B-it-heretic-ara-custom | arbitrary rank | 38.000 | 19.000 | 0.017 | 0.049 | 0.003 | attention_output, feed_forward_down |
| google/gemma-4-E2B-it | TrevorJS/gemma-4-E2B-it-uncensored | per layer | 70.000 | 35.000 | 0.027 | 0.034 | 0.988 | attention_output, feed_forward_down |
| google/gemma-4-E2B-it | WWTCyberLab/gemma-4-E2B-it-abliterated | per layer | 96.000 | 24.000 | 0.036 | 0.059 | 0.992 | attention_output, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-E2B-it | aifeifei798/Heretic-Scalpel-E2B | per layer | 179.000 | 35.000 | 0.002 | 0.058 | 0.113 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-E2B-it | amkkk/Gemma4_E2B_Abliterated_Baked_HF_Ready | arbitrary rank | 96.000 | 24.000 | 0.023 | 0.040 | 0.977 | attention_output, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-E2B-it | anlord/gemma-4-E2B-it-abliterated | per layer | 110.000 | 34.000 | 0.035 | 0.057 | 0.996 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-E2B-it | huihui-ai/Huihui-gemma-4-E2B-it-abliterated | one direction | 50.000 | 25.000 | 0.026 | 0.028 | 0.995 | attention_output, feed_forward_down |
| google/gemma-4-E2B-it | lessans/gemma-4-E2B-it-uncensored | per layer | 70.000 | 35.000 | 0.027 | 0.034 | 0.988 | attention_output, feed_forward_down |
| google/gemma-4-E2B-it | llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic | arbitrary rank | 7.000 | 7.000 | 0.051 | 0.092 | 0.950 | attention_output |
| google/gemma-4-E2B-it | prithivMLmods/gemma-4-E2B-it-Uncensored-MAX | one direction | 50.000 | 25.000 | 0.026 | 0.028 | 0.995 | attention_output, feed_forward_down |
| google/gemma-4-E2B-it | treadon/gemma4-E2B-it-Abliterated-AND-Disinhibited-USE-THIS | per layer | 48.000 | 24.000 | 0.058 | 0.072 | 0.538 | attention_output, feed_forward_down |
| google/gemma-4-E2B-it | treadon/gemma4-E2B-it-abliterated | per layer | 48.000 | 24.000 | 0.046 | 0.055 | 0.997 | attention_output, feed_forward_down |
| google/gemma-4-E2B-it | tvall43/gemma-4-E2B-it-heretic-v0 | one direction | 19.000 | 19.000 | 0.087 | 0.120 | 0.999 | attention_output |
| google/gemma-4-E2B-it | tvall43/gemma-4-E2B-it-heretic-v1 | per layer | 23.000 | 14.000 | 0.101 | 0.115 | 1.000 | attention_output, feed_forward_down |
| google/gemma-4-E2B-it | wangzhang/gemma-4-E2B-it-abliterated | per layer | 72.000 | 26.000 | 0.036 | 0.088 | 0.987 | attention_output, attention_query, attention_value, feed_forward_down |
| google/gemma-4-E2B-it | yuna1126/gemma-4-E2B-Tema_Q-Abliterated | arbitrary rank | 7.000 | 7.000 | 0.034 | 0.057 | 0.948 | attention_output, feed_forward_down |
| google/gemma-4-E4B | Felldude/gemma-4-E4B-uncensored | mixed | 595.000 | 42.000 | 0.422 | 1.600 | 0.002 | attention_key, attention_output, attention_query, attention_value, embedding, feed_forward_down, feed_forward_gate, feed_forward_up, final_normalization, input_normalization, other, post_attention_normalization |
| google/gemma-4-E4B | chulcher/gemma-4-e4b-abliterated | per layer | 23.000 | 22.000 | 0.024 | 0.036 | 0.986 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | Bahushruth/gemma-4-E4B-it-abliterated | arbitrary rank | 24.000 | 12.000 | 0.058 | 0.103 | 0.189 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | BinxNet/gemma-4-E4B-it-heretic | one direction | 51.000 | 35.000 | 0.022 | 0.028 | 0.976 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | Cup4/gemma-4-E4B-it-uncensored-heretic | arbitrary rank | 11.000 | 11.000 | 0.036 | 0.052 | 0.920 | attention_output |
| google/gemma-4-E4B-it | Cup5/gemma-4-E4B-it-uncensored-heretic | arbitrary rank | 11.000 | 11.000 | 0.036 | 0.052 | 0.920 | attention_output |
| google/gemma-4-E4B-it | Dingdust/ContextPilot-E4B-heretic | per layer | 285.000 | 42.000 | 0.002 | 0.082 | 0.003 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up, other |
| google/gemma-4-E4B-it | DuoNeural/Gemma-4-E4B-Heretic | one direction | 68.000 | 36.000 | 0.027 | 0.036 | 0.976 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | Felldude/gemma-4-E4B-uncensored | per layer | 595.000 | 42.000 | 0.422 | 1.600 | 0.002 | attention_key, attention_output, attention_query, attention_value, embedding, feed_forward_down, feed_forward_gate, feed_forward_up, final_normalization, input_normalization, other, post_attention_normalization |
| google/gemma-4-E4B-it | Himanshuoo8/gemma-4-E4B-it-Claude-Opus-4.5-HERETIC-UNCENSORED-Thinking | arbitrary rank | 287.000 | 42.000 | 0.003 | 0.061 | 0.112 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| google/gemma-4-E4B-it | Ilya626/gemma-4-E4B-it-SDFT_Heretic_RP | per layer | 526.000 | 42.000 | 0.004 | 1.710 | 0.005 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up, other |
| google/gemma-4-E4B-it | ImanolSuarez/gemma-4-E4B-it-heretic-seguridadDeLaInformacion | one direction | 37.000 | 19.000 | 0.021 | 0.029 | 0.978 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | Jiunsong/supergemma4-e4b-abliterated | no file | 0.000 | 0.000 | none | none | none |  |
| google/gemma-4-E4B-it | JokeHer/gemma-4-E4B-it-heretic | arbitrary rank | 40.000 | 20.000 | 0.079 | 1.008 | 0.006 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | Madras1/Gemma-4-E4B-Abliterated-Uncensored | one direction | 81.000 | 27.000 | 0.027 | 0.038 | 0.996 | attention_output, feed_forward_down, feed_forward_gate |
| google/gemma-4-E4B-it | MoonRide/gemma-4-E4B-it-heretic-ara | arbitrary rank | 33.000 | 17.000 | 0.030 | 0.059 | 0.006 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals3 | arbitrary rank | 26.000 | 13.000 | 0.033 | 0.067 | 0.236 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals5 | arbitrary rank | 29.000 | 18.000 | 0.036 | 0.065 | 0.862 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals6-attn | arbitrary rank | 31.000 | 16.000 | 0.028 | 0.048 | 0.324 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8 | arbitrary rank | 28.000 | 14.000 | 0.032 | 0.056 | 0.230 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8-attn | arbitrary rank | 25.000 | 15.000 | 0.028 | 0.049 | 0.398 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | OS-Software/gemma-4-E4B-it-uncensored-heretic | arbitrary rank | 20.000 | 10.000 | 0.078 | 0.142 | 0.587 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | Pound1320/gemma-4-E4B-it-uncensored-heretic | arbitrary rank | 11.000 | 11.000 | 0.036 | 0.052 | 0.920 | attention_output |
| google/gemma-4-E4B-it | SassyDiffusion/gemma-4-E4B-it-heretic | arbitrary rank | 21.000 | 21.000 | 0.038 | 0.081 | 0.466 | attention_output |
| google/gemma-4-E4B-it | TheUmbraWalker/gemma-4-E4B-it-2-heretic | per layer | 73.000 | 38.000 | 0.033 | 0.046 | 0.504 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | TheUmbraWalker/gemma-4-E4B-it-heretic | per layer | 73.000 | 38.000 | 0.027 | 0.041 | 0.994 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | TrevorJS/gemma-4-E4B-it-uncensored | per layer | 84.000 | 42.000 | 0.022 | 0.029 | 0.991 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | alphakek/gemma-4-E4B-it-heretic-mythos-v1 | arbitrary rank | 34.000 | 17.000 | 0.029 | 0.062 | 0.006 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | chulcher/gemma-4-e4b-abliterated | mixed | 23.000 | 22.000 | 0.024 | 0.036 | 0.986 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | coder3101/gemma-4-E4B-it-heretic | arbitrary rank | 21.000 | 21.000 | 0.037 | 0.060 | 0.002 | attention_output |
| google/gemma-4-E4B-it | huihui-ai/Huihui-gemma-4-E4B-it-abliterated | one direction | 70.000 | 35.000 | 0.049 | 0.061 | 0.999 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | jokernifty/gemma-4-e4b-it-abliterated | one direction | 31.000 | 15.000 | 0.020 | 0.023 | 1.000 | attention_output, embedding, feed_forward_down |
| google/gemma-4-E4B-it | llmfan46/gemma-4-E4B-it-ultra-uncensored-heretic | arbitrary rank | 17.000 | 17.000 | 0.043 | 0.057 | 0.936 | attention_output |
| google/gemma-4-E4B-it | llmfan46/gemma-4-E4B-it-uncensored-heretic | arbitrary rank | 11.000 | 11.000 | 0.036 | 0.052 | 0.920 | attention_output |
| google/gemma-4-E4B-it | p-e-w/gemma-4-E4B-it-heretic | one direction | 68.000 | 37.000 | 0.016 | 0.032 | 0.969 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | p-e-w/gemma-4-E4B-it-heretic-REPRODUCED-2 | one direction | 68.000 | 37.000 | 0.016 | 0.032 | 0.969 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | prithivMLmods/gemma-4-E4B-it-Uncensored-MAX | one direction | 70.000 | 35.000 | 0.049 | 0.061 | 0.999 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | senjiangchen/gemma-4-E4B-it-uncensored | per layer | 84.000 | 42.000 | 0.022 | 0.029 | 0.991 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | sh0ck0r/gemma-4-E4B-it-heretic | one direction | 60.000 | 37.000 | 0.026 | 0.031 | 0.959 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | treadon/gemma4-E4B-it-Abliterated-AND-Disinhibited-USE-THIS | per layer | 42.000 | 21.000 | 0.037 | 0.044 | 0.659 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it | treadon/gemma4-E4B-it-abliterated | per layer | 34.000 | 17.000 | 0.021 | 0.024 | 0.991 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it-qat-q4_0-unquantized | coder3101/gemma-4-E4B-it-qat-q4_0-unquantized-heretic | arbitrary rank | 16.000 | 16.000 | 0.038 | 0.061 | 0.455 | attention_output |
| google/gemma-4-E4B-it-qat-q4_0-unquantized | igorls/gemma-4-E4B-it-qat-q4_0-unquantized-heretic | arbitrary rank | 32.000 | 16.000 | 0.097 | 0.214 | 0.652 | attention_output, feed_forward_down |
| google/gemma-4-E4B-it-qat-q4_0-unquantized | prithivMLmods/gemma-4-E4B-it-qat-heretic_decensored | one direction | 54.000 | 30.000 | 0.023 | 0.029 | 0.992 | attention_output, feed_forward_down |
| inflatebot/MN-12B-Mag-Mell-R1 | EldritchLabs/MN-12B-Mag-Mell-R1-Uncensored-Scale1.2 | one direction | 80.000 | 40.000 | 0.017 | 0.021 | 0.990 | attention_output, feed_forward_down |
| inflatebot/MN-12B-Mag-Mell-R1 | Naphula/MN-12B-Mag-Mell-R1-Uncensored | one direction | 80.000 | 40.000 | 0.021 | 0.027 | 0.993 | attention_output, feed_forward_down |
| mistralai/Magistral-Small-2509 | grayarea/Magistral-Small-2509-Heretic-v1.2 | one direction | 64.000 | 34.000 | 0.018 | 0.025 | 0.967 | attention_output, feed_forward_down |
| mistralai/Magistral-Small-2509 | llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v1 | arbitrary rank | 18.000 | 11.000 | 0.017 | 0.054 | 0.748 | attention_output, feed_forward_down |
| mistralai/Magistral-Small-2509 | llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v2 | arbitrary rank | 49.000 | 28.000 | 0.024 | 0.093 | 0.841 | attention_output, feed_forward_down |
| mistralai/Ministral-3-8B-Reasoning-2512 | AISafety-Student/Ministral-3-8B-Reasoning-2512-heretic | mixed | 45.000 | 26.000 | 0.022 | 0.026 | 0.989 | attention_output, feed_forward_down |
| mistralai/Ministral-3-8B-Reasoning-2512 | ccharnkij/Ministral-3-8B-Reasoning-2512-Uncensored | per layer | 238.000 | 34.000 | 0.010 | 0.018 | 0.146 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| mistralai/Mistral-7B-Instruct-v0.3 | 3MPER0RR/Mistral-7B-v0.3-3MPER0RR-abliterated | one direction | 226.000 | 32.000 | 0.022 | 0.036 | 0.005 | attention_key, attention_output, attention_query, attention_value, embedding, feed_forward_down, feed_forward_gate, feed_forward_up, output_head |
| mistralai/Mistral-7B-Instruct-v0.3 | DogOnKeyboard/Mistral-7B-Heretic | one direction | 45.000 | 25.000 | 0.014 | 0.025 | 0.976 | attention_output, feed_forward_down |
| mistralai/Mistral-7B-Instruct-v0.3 | evolveon/Mistral-7B-Instruct-v0.3-abliterated | one direction | 65.000 | 32.000 | 0.016 | 0.019 | 0.989 | attention_output, embedding, feed_forward_down |
| mistralai/Mistral-7B-Instruct-v0.3 | paoloronco/Mistral-7B-Instruct-v0.3-heretic | one direction | 38.000 | 21.000 | 0.021 | 0.024 | 0.992 | attention_output, feed_forward_down |
| mistralai/Mistral-7B-Instruct-v0.3 | richardyoung/Mistral-7B-Instruct-v0.3-abliterated | one direction | 48.000 | 27.000 | 0.019 | 0.025 | 0.973 | attention_output, feed_forward_down |
| mistralai/Mistral-Nemo-Instruct-2407 | DuoNeural/Mistral-NeMo-12B-Abliterated | one direction | 80.000 | 40.000 | 0.004 | 0.006 | 0.916 | attention_output, feed_forward_down |
| mistralai/Mistral-Nemo-Instruct-2407 | grimjim/mistralai-Mistral-Nemo-Instruct-2407-extensive-BP-abliteration-12B | mixed | 70.000 | 35.000 | 0.015 | 0.022 | 0.987 | attention_output, feed_forward_down |
| mistralai/Mistral-Small-3.2-24B-Instruct-2506 | Pranavz/Hearthfire-24B-heretic | per layer | 282.000 | 40.000 | 0.012 | 0.076 | 0.004 | attention_key, attention_output, attention_query, attention_value, embedding, feed_forward_down, feed_forward_gate, feed_forward_up, output_head |
| mistralai/Mistral-Small-3.2-24B-Instruct-2506 | coder3101/Mistral-Small-3.2-24B-Instruct-2506-heretic | mixed | 50.000 | 38.000 | 0.017 | 0.034 | 0.856 | attention_output, feed_forward_down |
| mistralai/Mistral-Small-3.2-24B-Instruct-2506 | darkc0de/Mistral-Small-3.2-24B-Instruct-2506-heretic | per layer | 67.000 | 36.000 | 0.017 | 0.033 | 0.986 | attention_output, feed_forward_down |
| mistralai/Mistral-Small-3.2-24B-Instruct-2506 | llmfan46/Mistral-Small-3.2-24B-Instruct-2506-ultra-uncensored-heretic | arbitrary rank | 8.000 | 8.000 | 0.066 | 0.100 | 0.941 | attention_output |
| mistralai/Mistral-Small-3.2-24B-Instruct-2506 | nicoboss/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-llamacppfixed | one direction | 80.000 | 40.000 | 0.016 | 0.022 | 0.987 | attention_output, feed_forward_down |
| yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2 | huihui-ai/Huihui-gemma-4-12B-agentic-fable5-abliterated | per layer | 12.000 | 6.000 | 0.020 | 0.027 | 0.991 | attention_output, feed_forward_down |
| yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2 | llmfan46/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-uncensored-heretic | one direction | 67.000 | 39.000 | 0.024 | 0.030 | 0.988 | attention_output, feed_forward_down |
| yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated | per layer | 12.000 | 6.000 | 0.021 | 0.031 | 0.993 | attention_output, feed_forward_down |
| yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | llmfan46/gemma-4-12B-coder-fable5-composer2.5-v1-uncensored-heretic | one direction | 85.000 | 45.000 | 0.017 | 0.027 | 0.983 | attention_output, feed_forward_down |
| yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic | one direction | 557.000 | 48.000 | 0.005 | 0.086 | 0.025 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up, final_normalization, input_normalization, other, post_attention_normalization |
| yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | tpls/gemma-4-12B-coder-fable5-composer2.5-v1-abliterated | mixed | 322.000 | 48.000 | 0.001 | 0.033 | 0.001 | attention_key, attention_output, attention_query, attention_value, feed_forward_down, feed_forward_gate, feed_forward_up |
| zerofata/MS3.2-PaintedFantasy-v4.1-24B | llmfan46/MS3.2-PaintedFantasy-v4.1-24B-ultra-uncensored-heretic-v1 | arbitrary rank | 18.000 | 18.000 | 0.031 | 0.043 | 0.591 | attention_output |
| zerofata/MS3.2-PaintedFantasy-v4.1-24B | llmfan46/MS3.2-PaintedFantasy-v4.1-24B-ultra-uncensored-heretic-v2 | arbitrary rank | 18.000 | 18.000 | 0.035 | 0.052 | 0.717 | attention_output |
