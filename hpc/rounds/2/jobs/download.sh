#!/bin/bash
#SBATCH --job-name=model-audit-census-download
#SBATCH --account=NRLMR57635502
#SBATCH --time=03:55:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G
#SBATCH --output=logs/%x-%j.out
# download.sh -- Stage the whole batch on a transfer node.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  publish completion only after all ten snapshots pass.
# Modified: SDE 2026-10-15  the hub client round 1 tested; no progress bars in the log.
set -euo pipefail
export AUDIT_JOB_STARTED=$(date +%s.%N)
cd "${AUDIT_PINNED_ROUND:?a pinned submission copy is required}"
. ./env.sh
start_piece download 'Download and verify five checkpoint pairs'
python3 ./lineage.py batch.json banned-makers.txt
if [ "${AUDIT_STUB:-0}" = 1 ] && [ "${AUDIT_REHEARSAL:-0}" = 1 ]; then
    python3 ./measure.py --seed-original
    touch "$AUDIT_WORK/state/download.done"
    exit 0
fi
compute_python
export HF_HUB_DISABLE_PROGRESS_BARS=1
python3 -m venv "$AUDIT_WORK/download-venv"
py=$AUDIT_WORK/download-venv/bin/python
"$py" -m pip install 'huggingface_hub==0.35.3'
mkdir -p "$AUDIT_WORK/wheels"
"$py" -m pip download -r compute-requirements.txt --dest "$AUDIT_WORK/wheels"
"$py" ./download.py
