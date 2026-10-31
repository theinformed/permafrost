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
# Modified: SDE 2026-10-31  the scheduler's test of the CPU requests runs here, off the login node, as a reading.
# Modified: SDE 2026-10-31  the storage probe runs here too, before anything is staged.
# Modified: SDE 2026-10-31  timestamped steps; pip bounded with its temp on the node's disk; wheels staged per system.
set -euo pipefail
export AUDIT_JOB_STARTED=$(date +%s.%N)
cd "${AUDIT_PINNED_ROUND:?a pinned submission copy is required}"
. ./env.sh
count=$(python3 ./census.py count)
start_piece download "Download and verify $count checkpoint pairs"
# The desk's reporting kit records how this job ends, even when it dies without a word.
hpc_report_on_exit
step "lineage, storage and request readings"
fips_guard
python3 ./lineage.py batch.json maker-guard.sha256
# The space check runs here, where the space is about to be used, and not on the login node (round 19's
# clock put 296 s of its login half in this probe's du over the project tree on Lustre).
python3 ./storage.py
# The start estimates the desk reads; the submit step has already queued the real requests, so a node
# without the scheduler client only loses the reading.
for piece in project sweep timing; do
    test_submission "$piece" "jobs/$piece.sh" || echo "request test for $piece did not run on this node"
done
stub=0
if [ "${AUDIT_STUB:-0}" = 1 ] && [ "${AUDIT_REHEARSAL:-0}" = 1 ]; then stub=1; fi
if [ "$stub" = 1 ] && [ -z "${AUDIT_IMAGE:-}" ]; then
    python3 ./measure.py --seed-original
    touch "$AUDIT_WORK/state/download.done"
    exit 0
fi
compute_python
export HF_HUB_DISABLE_PROGRESS_BARS=1
step "download tools"
if [ -n "${AUDIT_IMAGE:-}" ]; then
    # The image brings its own Python, hub client and compare libraries; no wheels are fetched.
    py=image_python
else
    # pip's temp and exit-time file work stay on the node's own disk, off Lustre.
    tmp=$(mktemp -d /tmp/model-audit-XXXXXX 2>/dev/null) && export TMPDIR=$tmp
    python3 -m venv "$AUDIT_WORK/download-venv"
    py=$AUDIT_WORK/download-venv/bin/python
    bounded 600 "$py" -m pip install --disable-pip-version-check 'huggingface_hub==0.35.3'
    stage_wheels "$py"
    [ -z "${tmp:-}" ] || rm -rf -- "$tmp"
    unset TMPDIR
fi
node_facts "$py"
step "hub fetch: $count pairs"
if [ "$stub" = 1 ]; then
    "$py" ./measure.py --seed-original
    touch "$AUDIT_WORK/state/download.done"
    exit 0
fi
"$py" ./download.py
step "download complete"
