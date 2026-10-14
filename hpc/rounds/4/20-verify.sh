#!/bin/bash
# 20-verify.sh -- Check storage, the request and the verified shared download.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  check every pinned wheel before submission.
. ./env.sh
start_piece verify 'Check the calibration request and shared download'
python3 ./login.py
python3 ./storage.py
bash -n jobs/calibrate.sh
sbatch --test-only jobs/calibrate.sh
if [ "${AUDIT_REHEARSAL:-0}" != 1 ]; then
    if [ -e "$HOME/.hpc/hf-token" ]; then [ "$(stat -c %a "$HOME/.hpc/hf-token")" = 600 ]; fi
    [ "$(stat -c %a "$HOME/.hpc/pad-token")" = 600 ]
    grep -q '^model-audit ' "$HOME/.hpc/pad-token"
fi
[ -f "$AUDIT_DOWNLOAD_RECEIPT" ] || { echo "verified download missing: $AUDIT_DOWNLOAD_RECEIPT"; exit 1; }
[ -f "$AUDIT_ORIGINAL/download-manifest.json" ] || { echo "verified download missing: $AUDIT_ORIGINAL/download-manifest.json"; exit 1; }
python3 ./wheels.py
echo "recipe: $AUDIT_RECIPE"
echo 'VERDICT verify OK'
