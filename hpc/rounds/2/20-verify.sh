#!/bin/bash
# 20-verify.sh -- Check storage and both scheduler requests before submission.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-14  screen lineage and test the CPU and transfer requests.
# Modified: SDE 2026-10-13  the hub token is optional; only gated originals need it.
# Modified: SDE 2026-10-13  keep device inspection inside the GPU job.
# Modified: SDE 2026-10-15  test the requests with the owner tag the desk reads.
. ./env.sh
start_piece verify 'Check the transfer and CPU comparison requests'
python3 ./lineage.py batch.json banned-makers.txt
python3 ./login.py
python3 ./storage.py
for piece in download project; do
    job=jobs/$piece.sh
    queue=background
    [ "$piece" != download ] || queue=transfer
    mapfile -t request < <(queue_args "$queue")
    bash -n "$job"
    sbatch --test-only --comment=project=model-audit "${request[@]}" "$job"
done
if [ "${AUDIT_REHEARSAL:-0}" != 1 ]; then
    # The gated originals use the read-only token staged by its own card.
    python3 ./census.py token-check
    [ "$(stat -c %a "$HOME/.hpc/pad-token")" = 600 ]
    grep -q '^model-audit ' "$HOME/.hpc/pad-token"
fi
echo 'VERDICT verify OK'
