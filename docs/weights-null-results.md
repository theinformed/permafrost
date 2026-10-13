# CPU weight controls

The original checkpoint is `HuggingFaceTB/SmolLM2-135M-Instruct`, revision
`12fd25f77366fa6b3b4b768ec3050bf629380bac`. Its weight shard has SHA-256
`5af571cbf074e6d21a03528d2330792e532ca608f24ac70a143f6b369968ab8c`.
The comparison matched all 272 tensor names in each control. The difference
threshold was 0.001, the first-value energy minimum 0.99, and the direction
cosine minimum 0.95.

| Control | Tensors above threshold | Minimum first-value energy share | Minimum direction cosine | Result |
|---|---:|---:|---:|---|
| bfloat16 round trip | 0 | Not applicable | Not applicable | Unchanged |
| Single-direction projection | 60 | 0.9999991 | ≈1.0000000 | Matches single-projection; zero violations |

The rounding difference is zero for every tensor. This original is already
bfloat16, so this control tests copying and dtype handling without introducing
new rounding. A separate synthetic float32-to-bfloat16 test exceeds 0.001;
rounding other starting precisions can fail this threshold.

The projection changed all 30 attention output matrices and all 30 feed-forward
down projections. Every other weight was unchanged. The saved direction comes
from 32 harmful-style and 32 harmless instructions, collected in eight batches
at the input to block 15. The largest instruction sequence had 44 tokens.
Activations were calculated in float32 and averaged in float64. The projected
weights were saved in float32. No answers were generated or scored.

The table rounds energy shares and cosines to seven decimal places; the saved
JSON retains the full values. First-value energy shares approach one, with small floating-point differences
from the randomized SVD. They are not exactly one in this run. These values pass
the analytic envelope; they do not establish how the checkpoint responds to
harmful instructions or whether any hidden behavior is absent.

The weight and null tests passed: 20 tests, covering rank-one and rank-two
differences, row rescaling, dtype rounding, undefined directions, name matching,
shard indexes, tensor lifetimes, and an attention block with a known answer.
The complete measurements and direction files are saved under the null
directory in `data/`. Downloaded and generated weights remain excluded from
Git; the two prompt lists are source inputs.
