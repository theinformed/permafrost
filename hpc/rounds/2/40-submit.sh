#!/bin/bash
# 40-submit.sh -- Submit one pinned download and projection chain per build.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-14  chain five CPU pieces after one transfer job.
# Modified: SDE 2026-10-13  allow rebuilt retries and retain the earlier job ids.
# Modified: SDE 2026-10-14  allow projection alone with a completed download receipt.
# Modified: SDE 2026-10-15  check receipts by size here; the compare job does the hashing.
# Modified: SDE 2026-10-15  every job carries its owner for the desk: project=model-audit.
. ./env.sh
start_piece submit 'Submit the transfer and five CPU comparisons'
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
state=$AUDIT_WORK/state/round-2-submissions
if [ -f "$state" ] && grep -qF "build $stamp " "$state"; then
    echo "This build already submitted a job: $stamp"
    exit 1
fi
printf 'build %s attempted %s\n' "$stamp" "$(date -u +%FT%TZ)" >> "$state"

submit_job() {
    local piece=$1 pinned id
    shift
    local queue=background
    [ "$piece" != download ] || queue=transfer
    mapfile -t request < <(queue_args "$queue")
    pinned=$(python3 ./snapshot.py create) || return $?
    id=$(sbatch --parsable --comment=project=model-audit "${request[@]}" --output="$AUDIT_WORK/logs/%x-%j.out" --chdir="$pinned" --export="ALL,AUDIT_PINNED_ROUND=$pinned,AUDIT_PAIR=$AUDIT_PAIR" "$@" "$pinned/jobs/$piece.sh") || return $?
    id=${id%%;*}
    [[ "$id" =~ ^[0-9]+$ ]] || { echo "$piece submission returned no job id" >&2; return 1; }
    printf '%s %s build %s snapshot %s\n' "$piece" "$id" "$stamp" "$pinned" >> "$state"
    printf '%s\n' "$id"
}

parent=
if [ "${AUDIT_PROJECTION_ONLY:-0}" != 1 ]; then
    parent=$(submit_job download)
    echo "download job: $parent"
fi
pieces=${AUDIT_RETRY_PAIR:-"1 2 3 4 5"}
for AUDIT_PAIR in $pieces; do
    export AUDIT_PAIR
    if [ -n "$parent" ]; then
        next=$(submit_job project --dependency=afterok:"$parent" --kill-on-invalid-dep=yes)
    else
        next=$(submit_job project)
    fi
    echo "compare piece $AUDIT_PAIR job: $next"
    parent=$next
done
echo 'VERDICT submit OK'
