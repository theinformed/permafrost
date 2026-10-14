#!/bin/bash
# calibrate.sh -- Apply one recipe and measure its checkpoint fingerprint.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  clear calibration outputs while keeping shared originals.
# Modified: SDE 2026-10-14  rebuild the compute venv when its pins change.
#SBATCH --job-name=model-audit-recipe-calibration
#SBATCH -p general
#SBATCH --qos=background
#SBATCH --constraint=mla
#SBATCH --gres=gpu:a100:4
#SBATCH --account=NRLMR57635502
#SBATCH --time=02:20:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=128G
#SBATCH --output=logs/%x-%j.out
set -euo pipefail
export AUDIT_JOB_STARTED=$(date +%s.%N)
cd "${AUDIT_PINNED_ROUND:?a pinned submission copy is required}"
. ./env.sh

clear_calibration_state() {
    # A new try gets fresh outputs; the shared download is read only.
    rm -rf -- "$AUDIT_WORK/state/calibration" "$AUDIT_DERIVED"
    rm -f -- "$AUDIT_MEASUREMENT" "${AUDIT_MEASUREMENT%.json}.directions.safetensors" "$AUDIT_CARD" \
        "${AUDIT_MEASUREMENT%.json}.recipe-card.json" "${AUDIT_MEASUREMENT%.json}.direction.safetensors" \
        "${AUDIT_MEASUREMENT%.json}.timing.json" "$AUDIT_WORK/state/calibrate-activations.done" \
        "$AUDIT_WORK/state/calibrate-transform.done" "$AUDIT_WORK/state/calibrate-compare.done" \
        "$AUDIT_WORK/state/calibrate.done"
}

clear_calibration_state
start_piece calibration 'Apply one published recipe and measure its fingerprint'
[ -f "$AUDIT_DOWNLOAD_RECEIPT" ] || { echo "verified download missing: $AUDIT_DOWNLOAD_RECEIPT"; exit 1; }
compute_python
export PYTHONPATH=$AUDIT_ROUND
export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
if [ "${AUDIT_STUB:-0}" = 1 ]; then
    python3 ./measure.py
else
    nvidia-smi
    # The venv is good only for the pins it was built from; new pins rebuild it.
    pins=$(sha256sum compute-requirements.txt | cut -d' ' -f1)
    if [ "$(cat "$AUDIT_WORK/venv/.ready" 2>/dev/null)" != "$pins" ]; then
        echo "compute venv: building for pins $pins"
        rm -rf -- "$AUDIT_WORK/venv"
        python3 -m venv "$AUDIT_WORK/venv"
        "$AUDIT_WORK/venv/bin/python" -m pip install --no-index --find-links "$AUDIT_WHEELS" -r compute-requirements.txt
        echo "$pins" > "$AUDIT_WORK/venv/.ready"
    else
        echo "compute venv: reusing pins $pins"
    fi
    "$AUDIT_WORK/venv/bin/python" ./measure.py
fi
