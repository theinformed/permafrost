#!/bin/bash
# 20-verify.sh -- Check storage and both scheduler requests before submission.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-14  screen lineage and test the CPU and transfer requests.
# Modified: SDE 2026-10-13  the hub token is optional; only gated originals need it.
# Modified: SDE 2026-10-13  keep device inspection inside the GPU job.
# Modified: SDE 2026-10-15  test the requests with the owner tag the desk reads.
# Modified: SDE 2026-10-29  test all three requests through the scheduler adapter; check the image.
# Modified: SDE 2026-10-30  the floor check reads the Python module where the table names no interpreter.
# Modified: SDE 2026-10-31  the Python check runs first, so a system without the module fails in seconds.
# Modified: SDE 2026-10-31  every probe is clocked; the scheduler's test-only calls leave the login node
#                           (round 18's verify held Nautilus for 294 s); the download job prints them.
. ./env.sh
start_piece verify 'Check the transfer and CPU comparison requests'
# The pins need Python 3.10 or newer (Fran's 3.9 found no pydantic 2.14.1 at job time); an image brings its own.
# The check reads the interpreter the jobs will build on: the table's named one, else the Python module (env.sh).
# It comes first so that a system without the module fails this card in seconds, before any other probe.
if [ -z "${AUDIT_IMAGE:-}" ]; then
    floor_python || { echo 'this Python is below the pins; build this system with --image'; echo 'VERDICT verify FAIL'; exit 1; }
fi
# Each probe says what it cost; the desk's rule is one minute on a login node for the whole card.
clocked() { local t0=$SECONDS rc=0; "$@" || rc=$?; echo "verify: $1 ${2:-} took $((SECONDS - t0)) s"; return $rc; }
clocked python3 ./lineage.py batch.json maker-guard.sha256
clocked python3 ./login.py
clocked python3 ./storage.py
for piece in download project sweep timing; do
    clocked check_submission "$piece" "jobs/$piece.sh"
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
