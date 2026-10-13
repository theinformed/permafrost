#!/bin/bash
# 40-submit.sh -- Submit the download first and projection after its success.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  save each id before another submission can fail.
. ./env.sh
start_piece submit 'Submit the download and projection chain'
[ -s "$AUDIT_WORK/state/pad-confirmed" ] || { echo 'no drop has reached the desk from this system'; exit 1; }
# A submitted round is resumed by its saved ids, never duplicated blindly.
state=$AUDIT_WORK/state/round-1-submissions
if [ -f "$state" ]; then
    echo 'This round already submitted a job; a retry needs a new request.'
    cat "$state"
    exit 1
fi
printf 'attempted %s\n' "$(date -u +%FT%TZ)" > "$state"
first=$(sbatch --parsable jobs/download.sh)
first=${first%%;*}
[[ "$first" =~ ^[0-9]+$ ]] || { echo 'download submission returned no job id'; exit 1; }
printf 'download %s\n' "$first" >> "$state"
echo "download job: $first"
next=$(sbatch --parsable --dependency=afterok:"$first" --kill-on-invalid-dep=yes jobs/project.sh)
next=${next%%;*}
[[ "$next" =~ ^[0-9]+$ ]] || { echo 'projection submission returned no job id'; exit 1; }
printf 'projection %s\n' "$next" >> "$state"
echo "projection job: $next"
echo 'VERDICT submit OK'
