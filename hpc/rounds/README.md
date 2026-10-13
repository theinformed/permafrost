# Recipe rounds

Round 1 runs one single-direction projection on one pinned original. The text
middle-layer input at the last token of the assistant prefix supplies the
harmful-minus-harmless mean direction. Each text attention output and
feed-forward down projection loses its component along that direction. Other
weights keep their original values and precision. The tensor comparison uses
the existing analytic envelope; it does not establish an empirical pass line
from one run.

Later rounds add layerwise directions, higher ranks, norm-preserving projection,
healing, ordinary fine-tuning, merges and quantization controls. Planted-payload
controls belong to those later rounds. Their weights stay where they were made;
only measurements and reviewed traces return home. Packed expert checkpoints
wait for their format decoder.

The login scripts use Python 3.6 syntax and its standard library. Compute jobs
load the site's Python module and install the pinned runtime from a wheelhouse
staged by the download job. The pinned runtime needs Python 3.9 through 3.13.
Activation prompts and transformed tensor shards are saved individually. The
stage markers are written after timing, activations, projection and comparison
finish. A later approved piece resumes those stages; the submission step refuses
to duplicate an already recorded chain.

The original snapshot is pinned before download. LFS files are verified against
the published SHA-256. Small files have published git blob identifiers rather
than LFS SHA-256; those identifiers are verified too, and `download-manifest.json` records a
local SHA-256 for every file. Neither hub nor landing-pad tokens enter a bundle.

The gather script reads the round's saved card ids and cached storage count.
It does not ask the scheduler or walk the weight tree. Cleanup is listed by
`round.sh --list` but excluded from the default steps and `--from`. It runs only
with `--only 90-cleanup.sh`, a controller document containing an
`## approved paths` section of absolute paths, and an archive read-back record:

```json
{
  "project": "model-audit",
  "round": 1,
  "read_back": true,
  "approved_paths": ["/work/model-audit/derived/base/single-projection"],
  "archived_at": "2026-10-13T00:00:00Z",
  "measurements": [
    {"source": "/work/model-audit/measurements/base/single-projection.json",
     "archive": "/archive/base/single-projection.json", "sha256": "..."},
    {"source": "/work/model-audit/measurements/base/single-projection.directions.safetensors",
     "archive": "/archive/base/single-projection.directions.safetensors", "sha256": "..."}
  ]
}
```

`ARCHIVE_HOME` must name the archive containing the readable copies. Cleanup
hashes both copies itself before deleting the exact approved derived folders.
It leaves originals, measurements and other rounds alone. The kit does not
schedule an archive operation.

The local stub rehearsal takes a new, empty directory:

```bash
./hpc/rehearse.sh .tmp/stub-success --dry-run
./hpc/rehearse.sh .tmp/stub-failure --dry-run --fail-second
```

On the home compute machine, use an actual Python 3.6 interpreter for the login
steps and a Python 3.9 through 3.13 interpreter for compute. The kit sources must
be available locally; `--kit` names the directory with the shared reporting and
poll tools. Run both cases in separate empty directories:

```bash
./hpc/rehearse.sh /tmp/permafrost-success --kit /path/to/hpc-kit-wt --login-python /path/to/python3.6 --compute-python /path/to/python3.12 --base HuggingFaceTB/SmolLM2-135M-Instruct
./hpc/rehearse.sh /tmp/permafrost-failure --kit /path/to/hpc-kit-wt --login-python /path/to/python3.6 --compute-python /path/to/python3.12 --base HuggingFaceTB/SmolLM2-135M-Instruct --fail-second
```

Each run prints its last thirty lines, retains a submission ledger and drop
outbox, and runs the model work on CPU with one thread at low priority. The
failure case rejects the second submission. The unit tests separately fail the
first job and prove that its dependent job is cancelled rather than executed.

A successful bundle record closes the submission round, not the research jobs.
The jobs finish later with their own drops and measurement records. Measured
round duration can be supplied to the builder as `--takes`; until then the card
leaves duration unknown. Generated cards remain local until submitted to the desk.
