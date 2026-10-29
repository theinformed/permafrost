#!/bin/bash
#SBATCH --job-name=model-audit-census-download
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G
#SBATCH --output=logs/%x-%j.out
# download.sh -- Stage the whole batch on a transfer node.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  publish completion only after all ten snapshots pass.
# Modified: SDE 2026-10-15  the hub client round 1 tested; no progress bars in the log.
# Modified: SDE 2026-10-29  account and time from the submit line; FIPS guard, node facts, image.
# Modified: SDE 2026-10-29  hpc_report_on_exit after the piece starts, as every job script must.
set -euo pipefail
export AUDIT_JOB_STARTED=$(date +%s.%N)
cd "${AUDIT_PINNED_ROUND:?a pinned submission copy is required}"
. ./env.sh
count=$(python3 ./census.py count)
start_piece download "Download and verify $count checkpoint pairs"
# The desk's reporting kit records how this job ends, even when it dies without a word.
hpc_report_on_exit
fips_guard
python3 ./lineage.py batch.json maker-guard.sha256
stub=0
if [ "${AUDIT_STUB:-0}" = 1 ] && [ "${AUDIT_REHEARSAL:-0}" = 1 ]; then stub=1; fi
if [ "$stub" = 1 ] && [ -z "${AUDIT_IMAGE:-}" ]; then
    python3 ./measure.py --seed-original
    touch "$AUDIT_WORK/state/download.done"
    exit 0
fi
compute_python
export HF_HUB_DISABLE_PROGRESS_BARS=1
if [ -n "${AUDIT_IMAGE:-}" ]; then
    # The image brings its own Python, hub client and compare libraries; no wheels are fetched.
    py=image_python
else
    python3 -m venv "$AUDIT_WORK/download-venv"
    py=$AUDIT_WORK/download-venv/bin/python
    "$py" -m pip install 'huggingface_hub==0.35.3'
    mkdir -p "$AUDIT_WORK/wheels"
    "$py" -m pip download -r compute-requirements.txt --dest "$AUDIT_WORK/wheels"
fi
node_facts "$py"
if [ "$stub" = 1 ]; then
    "$py" ./measure.py --seed-original
    touch "$AUDIT_WORK/state/download.done"
    exit 0
fi
"$py" ./download.py
