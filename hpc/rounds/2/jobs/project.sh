#!/bin/bash
#SBATCH --job-name=model-audit-census-compare
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=60G
#SBATCH --output=logs/%x-%j.out
# project.sh -- Compare one pair on CPU, save its card and discard the modified weights.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  clear only this piece's prior try before reading inputs.
# Modified: SDE 2026-10-15  rebuild the compute venv when its pins change; no address-space cap.
# Modified: SDE 2026-10-29  account and time from the submit line; FIPS guard; the image path.
# Modified: SDE 2026-10-29  hpc_report_on_exit after the piece starts, as every job script must.
# Modified: SDE 2026-10-30  one compare builds the venv under a mkdir lock; the rest wait and reuse it.
# Modified: SDE 2026-10-31  the lock sets no exit trap of its own: the one it set replaced the reporting
#                            kit's trap, and every compare from round 12 on ended without a drop (Nautilus 4120062-8).
set -euo pipefail
export AUDIT_JOB_STARTED=$(date +%s.%N)
cd "${AUDIT_PINNED_ROUND:?a pinned submission copy is required}"
. ./env.sh

clear_projection_state() {
    # Keep transfer inputs until a comparison has saved both reports.
    rm -rf -- "$AUDIT_PIECE_WORK/state/projection" "$AUDIT_DERIVED"
    rm -f -- "${AUDIT_MEASUREMENT%/*}/metadata.json" "${AUDIT_MEASUREMENT%/*}/card.md" \
        "${AUDIT_MEASUREMENT%/*}/receipt.json" "${AUDIT_MEASUREMENT%/*}/weights.directions.safetensors"
    rm -f -- "$AUDIT_MEASUREMENT" "$AUDIT_PIECE_WORK/state/activations.done" \
        "$AUDIT_PIECE_WORK/state/timing.done" "$AUDIT_PIECE_WORK/state/project.done" \
        "$AUDIT_PIECE_WORK/state/compare.done"
}
clear_projection_state
mkdir -p "$AUDIT_PIECE_WORK/state"
start_piece compare "Compare checkpoint pair $AUDIT_PAIR on CPU"
# The desk's reporting kit records how this job ends, even when it dies without a word.
hpc_report_on_exit
fips_guard
if [ ! -f "$AUDIT_WORK/state/download.done" ]; then
    say 'compare refused: no finished download' "$AUDIT_WORK/state/download.done"
    exit 1
fi
python3 ./lineage.py batch.json maker-guard.sha256
compute_python
export PYTHONPATH=$AUDIT_ROUND HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
if [ -n "${AUDIT_IMAGE:-}" ]; then
    # The image carries the compare pins; compute_python has checked them one by one.
    image_python ./measure.py
elif [ "${AUDIT_STUB:-0}" = 1 ] && [ "${AUDIT_REHEARSAL:-0}" = 1 ]; then
    # The rehearsal's compute interpreter carries the same pins the venv below installs.
    python3 ./measure.py
else
    # Shards are mapped from disk, so an address-space cap would refuse a 31 GB shard;
    # the scheduler's --mem holds the real memory line.
    # The venv is good only for the pins it was built from; new pins rebuild it.
    # The compares of one round may all start in the same second, so one of them builds
    # the venv while the others wait on an atomic mkdir lock, then every job reuses it.
    # No trap here: the EXIT trap belongs to start_piece and hpc_report_on_exit (the drop
    # home); a holder that dies mid-build leaves its lock to the 40-minute takeover below.
    pins=$(sha256sum compute-requirements.txt | cut -d' ' -f1)
    venv_lock=$AUDIT_WORK/venv.lock
    waited=0
    until mkdir "$venv_lock" 2>/dev/null; do
        if [ "$waited" -ge 2400 ]; then
            echo "compute venv: lock held over 40 minutes; taking it over"
            rm -rf -- "$venv_lock"
            continue
        fi
        [ "$waited" = 0 ] && echo "compute venv: another compare is building it; waiting"
        sleep 20; waited=$((waited + 20))
    done
    if [ "$(cat "$AUDIT_WORK/venv/.ready" 2>/dev/null)" != "$pins" ]; then
        echo "compute venv: building for pins $pins"
        rm -rf -- "$AUDIT_WORK/venv"
        python3 -m venv "$AUDIT_WORK/venv"
        "$AUDIT_WORK/venv/bin/python" -m pip install --no-index --find-links "$AUDIT_WORK/wheels" -r compute-requirements.txt
        echo "$pins" > "$AUDIT_WORK/venv/.ready"
    else
        echo "compute venv: reusing pins $pins"
    fi
    rmdir "$venv_lock" 2>/dev/null
    "$AUDIT_WORK/venv/bin/python" ./measure.py
fi
touch "$AUDIT_PIECE_WORK/state/timing.done" "$AUDIT_PIECE_WORK/state/project.done" "$AUDIT_PIECE_WORK/state/compare.done"
echo "VERDICT compare pair $AUDIT_PAIR OK"
