#!/bin/bash
# 20-verify.sh -- Check storage and both scheduler requests before submission.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-14  screen lineage and test the CPU and transfer requests.
# Modified: SDE 2026-10-13  the hub token is optional; only gated originals need it.
# Modified: SDE 2026-10-13  keep device inspection inside the GPU job.
# Modified: SDE 2026-10-15  test the requests with the owner tag the desk reads.
# Modified: SDE 2026-10-29  test all three requests through the scheduler adapter; check the image.
. ./env.sh
start_piece verify 'Check the transfer and CPU comparison requests'
python3 ./lineage.py batch.json maker-guard.sha256
python3 ./login.py
python3 ./storage.py
for piece in download project sweep timing; do
    test_submission "$piece" "jobs/$piece.sh"
done
# Prove the image runs here, without a GPU, before anything is queued.
[ -z "${AUDIT_IMAGE:-}" ] || image_ready 0
if [ "${AUDIT_REHEARSAL:-0}" != 1 ]; then
    # The gated originals use the read-only token staged by its own card.
    python3 ./census.py token-check
    [ "$(stat -c %a "$HOME/.hpc/pad-token")" = 600 ]
    grep -q '^model-audit ' "$HOME/.hpc/pad-token"
fi
echo 'VERDICT verify OK'
