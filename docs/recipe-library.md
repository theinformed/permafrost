# Reference recipe library

The runners build reference weight changes for the defensive audit. Each copy has a
resolved base revision, shard checksums, parameters, package versions, changed tensor
names, and a completion marker. The driver compares each completed copy with the same
base and writes measured pass lines. The larger-base table remains pending until that
run finishes.

Run modules from the repository root. All seven accept `--base`, `--out`, and `--device`.
They lower process priority, use one CPU thread, cap device allocations at 0.25, and stop
if available host memory falls below 12 GB. The watcher checks once per second, including
during loading, generation, export, and comparison. Output directories must be empty.
An interrupted copy has no completion marker and must be given a new output directory.

| Module under `audit.recipes` | Operation |
| --- | --- |
| `single_projection` | Difference of mean middle-block input residuals; project every attention output and feed-forward down matrix. |
| `single_projection_selected` | Score each layer independently on held-out prompts; retain all ties at the largest positive drop in lexical refusal count. |
| `heretic_directional` | Pinned public optimizer, default data and trial settings; export the first refusal-sorted Pareto trial. |
| `heretic_arbitrary_rank` | Record “absent in version 1.3.0” and skip. The pinned source has directional ablation and norm-restoration approximation, but no arbitrary-rank search. |
| `norm_preserving` | Single projection, then restore the original norm of every changed row. |
| `projection_plus_healing` | Single projection, then one epoch of preference training with a merged adapter. |
| `plain_lora` | One epoch on benign instruction answers with a merged adapter. |

The direction uses the last token of the assistant prefix at the middle-block input,
matching the existing null control. On CPU, the supported small architecture reuses its
streamed forward pass. Other architectures use a hook on the same block input. The
default extraction split has 24 prompts per group; eight harmful-style prompts remain
for layer selection. Tiny tests can change both counts. The saved lists contain tame
inputs and do not establish refusal-removal efficacy. The lexical selection score is
also a coarse proxy: a zero reduction selects no layers.

The projection is `W - r (rᵀ W)`, using the shared function in `audit/nulls.py` and
float32 weight arithmetic. Untouched tensors retain their stored values and dtypes.
The norm-restored control implements the requested projection-then-rescale operation.
The [published norm-preserving write-up](https://huggingface.co/blog/grimjim/norm-preserving-biprojected-abliteration)
also normalizes rows before projection and refines the direction through biprojection;
this control does neither, and its card records the difference. A collapsed nonzero row
raises an error because rescaling cannot restore it.

The [published single-direction construction](https://github.com/andyrdt/refusal_direction)
is the source of the shared projection. The
[public optimizer release](https://pypi.org/project/heretic-llm/1.3.0/)
supplies the directional runner. Its settings, selected trial, effective per-layer
directions, and per-component strengths stay in the copy's evidence directory. The
wrapper answers the trial menu and exports the merged copy; an unexpected menu raises
an error. It changes the seed, device placement, output paths, and shard size, while
retaining the release's optimization and dataset defaults.

Training uses query and value adapters, rank eight, scaling sixteen, no dropout, a
learning rate of 0.00002, batch size one, and one epoch by default. The benign control
collects base answers to harmless prompt variations and trains answer tokens only.
Preference repair collects base answers as chosen responses and projected answers as
rejected responses to those same benign questions. It collects twice the requested
count before discarding identical pairs; if
fewer than the requested 256 distinct pairs remain, the run stops and reports the count.
Supply `--training-data pairs.jsonl` with `prompt`, `chosen`, and `rejected` fields when
needed. The control accepts `prompt` and `response` fields. External instruction data
must use the harmless prompt list, optionally followed by a wording variation. The
saved examples and their checksum identify the actual training set.
This is a short base-response repair experiment, following the documented
[post-projection repair step](https://huggingface.co/blog/mlabonne/abliteration), rather
than a reproduction of that article's training corpus. The
[preference trainer](https://huggingface.co/docs/trl/v0.29.0/en/dpo_trainer)
uses the adapter-disabled projected copy as its reference, so a second reference
checkpoint does not occupy device memory.

The dependency file pins the optimizer at 1.3.0, runtime at 5.6.2, adapter package at
0.19.1, preference trainer at 0.29.0, dataset package at 4.7.0, placement package at
1.13.0, tensor-file package at 0.8.0, templates at 3.1.6, requests at 2.32.5, and
the kernel loader at 0.13.0. Later kernel loaders require metadata that the pinned
runtime does not supply.
Install the device's matching tensor-runtime wheel separately. Every card records
the installed versions; those are the versions that produced the weights.

On the Spark, with the repository at `~/permafrost` and its device runtime already installed:

```bash
cd ~/permafrost
mkdir -p data/pip-cache data/tmp
PIP_CACHE_DIR="$PWD/data/pip-cache" TMPDIR="$PWD/data/tmp" nice -n 19 .venv/bin/pip install -r requirements-recipes.txt
nice -n 19 bash audit/recipes/run_library.sh --dry-run
PERMAFROST_MAX_DOWNLOAD_GB=5 nice -n 19 bash audit/recipes/run_library.sh --base Qwen/Qwen3-8B --device cuda:0
```

The five-GB download allowance belongs to that Spark command: the base's published
shards exceed the default one-GB limit. The CPU checks here keep the one-GB limit.
An existing local checkpoint is also accepted; individual runners can preserve its
original identity with `--base-repo` and `--base-revision`. The driver resolves the base
once and gives its local path and original identity to every runner.

The default storage plan allows 256 GB and estimates 208 GB of peak use, including the
base, float32 projection copies, and the preference-repair intermediate. It requires
another 12 GB of disk headroom. Completed copies remain under `data/library/qwen3-8b`
until their cards and measurements are accepted. The repair runner deletes its
regenerable projection intermediate after merging. There is no age-based cleanup.
Logs and measurements live under `results/library/qwen3-8b`; the generated table is
`docs/library-qwen3-8b.md`. Repeating the driver checks completed cards and continues
with missing methods; half-finished directories need a fresh run directory.

`envelopes.json` can be passed to `compare-weights --recipes`. Measured recipes apply
only when the base shard hashes match. They carry changed kinds, minimum first-value
energy share, minimum direction agreement, and the measured row-norm tolerance.
Undefined measurements and skipped methods remain explicit. One reference run supplies
observed limits; repeated seeds and base revisions are needed before drawing broader
family limits. The norm-preservation requirement is checked when the calibration copy
preserves row norms. Weight differences alone cannot certify the absence of hidden behavior.

CPU verification uses the cached 135-million-parameter checkpoint and tiny settings:
two extraction prompts per group, one held-out prompt, and two adapter examples. Each
runner and comparison is a separate short command. The public-tool and preference
runners are checked for imports and argument parsing only; their optimization and
preference training need the Spark run.
