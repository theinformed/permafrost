#!/bin/bash
# 40-submit.sh -- Submit one pinned download and projection chain per build.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  allow rebuilt retries and retain the earlier job ids.
# Modified: SDE 2026-10-14  allow projection alone with a completed download receipt.
. ./env.sh
start_piece submit 'Submit the download and projection chain'
[ -s "$AUDIT_WORK/state/pad-confirmed" ] || { echo 'no drop has reached the desk from this system'; exit 1; }
if [ "${AUDIT_PROJECTION_ONLY:-0}" = 1 ]; then
    [ -f "$AUDIT_WORK/state/download.done" ] || { echo "projection-only submit missing: $AUDIT_WORK/state/download.done"; exit 1; }
    [ -f "$AUDIT_ORIGINAL/download-manifest.json" ] || { echo "projection-only submit missing: $AUDIT_ORIGINAL/download-manifest.json"; exit 1; }
fi
stamp=$(cat BUILD-STAMP.txt)
[[ "$stamp" =~ ^[a-f0-9]{64}$ ]] || { echo 'round has no valid build stamp'; exit 1; }
export AUDIT_BUILD_STAMP=$stamp
state=$AUDIT_WORK/state/round-1-submissions
legacy=$WORKDIR/model-audit/state/round-1-submissions
# Keep the first attempt, including records made before build stamps existed.
if [ ! -e "$state" ] && [ -f "$legacy" ]; then cp "$legacy" "$state"; fi
if [ -f "$state" ] && grep -qF "build $stamp " "$state"; then
    echo "This build already submitted a job: $stamp"
    exit 1
fi
printf 'build %s attempted %s\n' "$stamp" "$(date -u +%FT%TZ)" >> "$state"

submit_job() {
    local piece=$1 pinned id
    shift
    pinned=$(python3 ./snapshot.py create) || return $?
    id=$(sbatch --parsable --output="$AUDIT_WORK/logs/%x-%j.out" --chdir="$pinned" --export="ALL,AUDIT_PINNED_ROUND=$pinned" "$@" "$pinned/jobs/$piece.sh") || return $?
    id=${id%%;*}
    [[ "$id" =~ ^[0-9]+$ ]] || { echo "$piece submission returned no job id" >&2; return 1; }
    printf '%s %s build %s snapshot %s\n' "$piece" "$id" "$stamp" "$pinned" >> "$state"
    printf '%s\n' "$id"
}

if [ "${AUDIT_PROJECTION_ONLY:-0}" = 1 ]; then
    next=$(submit_job project)
else
    first=$(submit_job download)
    echo "download job: $first"
    next=$(submit_job project --dependency=afterok:"$first" --kill-on-invalid-dep=yes)
fi
echo "projection job: $next"
echo 'VERDICT submit OK'
