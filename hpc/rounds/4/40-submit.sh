#!/bin/bash
# 40-submit.sh -- Submit one pinned calibration job per build.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  recheck pinned wheels before recording a submission.
. ./env.sh
start_piece submit 'Submit the recipe calibration job'
[ -s "$AUDIT_WORK/state/pad-confirmed" ] || { echo 'no drop has reached the desk from this system'; exit 1; }
[ -f "$AUDIT_DOWNLOAD_RECEIPT" ] || { echo "verified download missing: $AUDIT_DOWNLOAD_RECEIPT"; exit 1; }
[ -f "$AUDIT_ORIGINAL/download-manifest.json" ] || { echo "verified download missing: $AUDIT_ORIGINAL/download-manifest.json"; exit 1; }
python3 ./wheels.py
stamp=$(cat BUILD-STAMP.txt)
[[ "$stamp" =~ ^[a-f0-9]{64}$ ]] || { echo 'round has no valid build stamp'; exit 1; }
export AUDIT_BUILD_STAMP=$stamp
state=$AUDIT_WORK/state/round-4-submissions
if [ -f "$state" ] && grep -qF "build $stamp " "$state"; then
    echo "This build already submitted a job: $stamp"
    exit 1
fi
printf 'build %s attempted %s\n' "$stamp" "$(date -u +%FT%TZ)" >> "$state"

submit_job() {
    # Pin the scripts before the scheduler sees their path.
    local pinned id
    pinned=$(python3 ./snapshot.py create) || return $?
    id=$(sbatch --parsable --output="$AUDIT_WORK/logs/%x-%j.out" --chdir="$pinned" --export="ALL,AUDIT_PINNED_ROUND=$pinned" "$pinned/jobs/calibrate.sh") || return $?
    id=${id%%;*}
    [[ "$id" =~ ^[0-9]+$ ]] || { echo 'calibration submission returned no job id' >&2; return 1; }
    printf 'calibration %s build %s snapshot %s\n' "$id" "$stamp" "$pinned" >> "$state"
    printf '%s\n' "$id"
}

next=$(submit_job)
echo "calibration job: $next"
echo 'VERDICT submit OK'
