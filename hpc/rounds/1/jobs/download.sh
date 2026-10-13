#!/bin/bash
#SBATCH --job-name=model-audit-download-original
#SBATCH -p general
#SBATCH --qos=transfer
#SBATCH --constraint=xfer
#SBATCH --account=NRLMR57635502
#SBATCH --time=04:00:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G
#SBATCH --output=logs/%x-%j.out
# download.sh -- Stage the pinned original and offline compute wheels.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  run the pinned copy with a recorded start time.
# Modified: SDE 2026-10-13  finish only after published checksums pass.
set -euo pipefail
export AUDIT_JOB_STARTED=$(date +%s.%N)
cd "${AUDIT_PINNED_ROUND:?a pinned submission copy is required}"
. ./env.sh
start_piece download 'Download and verify the original checkpoint'
if [ "${AUDIT_STUB:-0}" = 1 ]; then
    python3 ./measure.py --seed-original
    echo 'stub download passed'
    touch "$AUDIT_WORK/state/download.done"
    exit 0
fi
compute_python
python3 -m venv "$AUDIT_WORK/download-venv"
py=$AUDIT_WORK/download-venv/bin/python
"$py" -m pip install 'huggingface_hub==0.35.3'
mkdir -p "$AUDIT_WORK/wheels"
"$py" -m pip download -r compute-requirements.txt --dest "$AUDIT_WORK/wheels"
"$py" ./download.py
