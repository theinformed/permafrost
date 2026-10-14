#!/bin/bash
#SBATCH --job-name=model-audit-project-and-measure
#SBATCH -p general
#SBATCH --qos=background
#SBATCH --constraint=mla
#SBATCH --gres=gpu:a100:4
#SBATCH --account=NRLMR57635502
#SBATCH --time=04:00:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=128G
#SBATCH --output=logs/%x-%j.out
# project.sh -- Measure the direction, project the checkpoint and compare it.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  fail the job when a measurement or freshness check fails.
# Modified: SDE 2026-10-13  save completed stages so another piece can resume.
# Modified: SDE 2026-10-14  clear prior-try state before projection starts.
# Modified: SDE 2026-10-14  rebuild the compute venv when its pins change.
set -euo pipefail
export AUDIT_JOB_STARTED=$(date +%s.%N)
cd "${AUDIT_PINNED_ROUND:?a pinned submission copy is required}"
. ./env.sh

clear_projection_state() {
    # Each try starts clean. Keep the verified download and its receipt.
    rm -rf -- "$AUDIT_WORK/state/projection" "$AUDIT_DERIVED"
    rm -f -- "$AUDIT_MEASUREMENT" "$AUDIT_WORK/state/activations.done" \
        "$AUDIT_WORK/state/timing.done" "$AUDIT_WORK/state/project.done" \
        "$AUDIT_WORK/state/compare.done"
}

clear_projection_state
start_piece projection 'Project one direction and measure the checkpoint change'
[ -f "$AUDIT_WORK/state/download.done" ]
if [ "${AUDIT_STUB:-0}" = 1 ]; then
    python3 ./measure.py
    echo 'stub projection passed'
    touch "$AUDIT_WORK/state/timing.done" "$AUDIT_WORK/state/project.done" "$AUDIT_WORK/state/compare.done"
    exit 0
fi
compute_python
if [ "${AUDIT_REHEARSAL:-0}" != 1 ]; then nvidia-smi; fi
# The venv is good only for the pins it was built from; new pins rebuild it.
pins=$(sha256sum compute-requirements.txt | cut -d' ' -f1)
if [ "$(cat "$AUDIT_WORK/venv/.ready" 2>/dev/null)" != "$pins" ]; then
    echo "compute venv: building for pins $pins"
    rm -rf -- "$AUDIT_WORK/venv"
    python3 -m venv "$AUDIT_WORK/venv"
    "$AUDIT_WORK/venv/bin/python" -m pip install --no-index --find-links "$AUDIT_WORK/wheels" -r compute-requirements.txt
    echo "$pins" > "$AUDIT_WORK/venv/.ready"
else
    echo "compute venv: reusing pins $pins"
fi
export PYTHONPATH=$AUDIT_ROUND
export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
"$AUDIT_WORK/venv/bin/python" ./measure.py
