#!/bin/bash
# 40-submit.sh -- Submit one pinned download, its parallel compares and the sweep per build.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-14  chain five CPU pieces after one transfer job.
# Modified: SDE 2026-10-13  allow rebuilt retries and retain the earlier job ids.
# Modified: SDE 2026-10-14  allow projection alone with a completed download receipt.
# Modified: SDE 2026-10-15  check receipts by size here; the compare job does the hashing.
# Modified: SDE 2026-10-15  every job carries its owner for the desk: project=model-audit.
# Modified: SDE 2026-10-29  one compare per pair, each after the download only, then the sweep.
. ./env.sh
count=$(python3 ./census.py count)
start_piece submit "Submit the transfer, $count CPU comparisons and the sweep"
python3 ./lineage.py batch.json banned-makers.txt
[ -s "$AUDIT_WORK/state/pad-confirmed" ] || { echo 'no drop has reached the desk from this system'; exit 1; }
if [ "${AUDIT_PROJECTION_ONLY:-0}" = 1 ]; then
    if [ ! -f "$AUDIT_WORK/state/download.done" ]; then
        say 'projection-only submit missing:' "$AUDIT_WORK/state/download.done"
        exit 1
    fi
    # Sizes only on the login node; each compare job hashes its own pair before reading it.
    python3 ./census.py receipts ${AUDIT_RETRY_PAIR:-}
fi
stamp=$(cat BUILD-STAMP.txt)
[[ "$stamp" =~ ^[a-f0-9]{64}$ ]] || { echo 'round has no valid build stamp'; exit 1; }
export AUDIT_BUILD_STAMP=$stamp
state=$AUDIT_WORK/state/round-$ROUND-submissions
if [ -f "$state" ] && grep -qF "build $stamp " "$state"; then
    echo "This build already submitted a job: $stamp"
    exit 1
fi
printf 'build %s attempted %s\n' "$stamp" "$(date -u +%FT%TZ)" >> "$state"
# One pinned copy serves every job of this submission; a later edit here reaches none of them.
pinned=$(python3 ./snapshot.py create)
say 'pinned copy:' "$pinned"

submit_job() {
    local piece=$1 dependency=${2:-} id
    id=$(submit_batch "$piece" "$pinned/jobs/$piece.sh" "$pinned" "$dependency") || return $?
    printf '%s %s build %s snapshot %s\n' "$piece" "$id" "$stamp" "$pinned" >> "$state"
    printf '%s\n' "$id"
}

download=
if [ "${AUDIT_PROJECTION_ONLY:-0}" != 1 ]; then
    download=$(submit_job download)
    echo "download job: $download"
fi
pieces=${AUDIT_RETRY_PAIR:-$(seq 1 "$count")}
compares=()
for AUDIT_PAIR in $pieces; do
    export AUDIT_PAIR
    # Each compare waits on the download alone, so the pieces can run side by side.
    if [ -n "$download" ]; then
        next=$(submit_job project "afterok:$download")
    else
        next=$(submit_job project)
    fi
    echo "compare piece $AUDIT_PAIR job: $next"
    compares+=("$next")
done
# The sweep starts once every compare has ended, however it ended.
ids=$(IFS=:; printf '%s' "${compares[*]}")
sweep=$(submit_job sweep "afterany:$ids")
echo "sweep job: $sweep"
echo 'VERDICT submit OK'
