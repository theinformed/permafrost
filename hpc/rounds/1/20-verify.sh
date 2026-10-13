#!/bin/bash
# 20-verify.sh -- Check storage and both scheduler requests before submission.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  the hub token is optional; only gated originals need it.
# Modified: SDE 2026-10-13  keep device inspection inside the GPU job.
. ./env.sh
start_piece verify 'Check the download and projection requests'
python3 ./login.py
python3 ./storage.py
for job in jobs/download.sh jobs/project.sh; do
    bash -n "$job"
    sbatch --test-only "$job"
done
if [ "${AUDIT_REHEARSAL:-0}" != 1 ]; then
    # The hub token is only needed for gated originals; round 1's base is open, so its absence is fine.
    if [ -e "$HOME/.hpc/hf-token" ]; then [ "$(stat -c %a "$HOME/.hpc/hf-token")" = 600 ]; fi
    [ "$(stat -c %a "$HOME/.hpc/pad-token")" = 600 ]
    grep -q '^model-audit ' "$HOME/.hpc/pad-token"
fi
echo 'VERDICT verify OK'
