#!/bin/bash
# round.sh -- Run this round's numbered steps and send the end log.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-14  run the numbered census steps and accept a piece retry.
# Modified: SDE 2026-10-13  keep cleanup available only by its own name.
# Modified: SDE 2026-10-14  accept a projection retry as a plain argument.
# Modified: SDE 2026-10-15  wrap step output at 100 columns; parsed lines are shorter.
# Modified: SDE 2026-10-29  take the round and its piece count from batch.json.
set -euo pipefail
cd "$(dirname "$0")" || exit 1
export HPC_PROJECT=model-audit HPC_SYSTEM=${HPC_SYSTEM:-nautilus}
ROUND=$(python3 ./census.py round)
count=$(python3 ./census.py count)
export ROUND
[ ! -f system.sh ] || . ./system.sh
export PATH=$HOME/bin:$PATH
narrow() {
    if command -v stdbuf >/dev/null 2>&1; then stdbuf -oL fold -w 100; else fold -w 100; fi
}
steps=(10-install-kit.sh 20-verify.sh 30-install-reporting.sh 40-submit.sh)
all=("${steps[@]}" 90-cleanup.sh)
mode=all
at=
if [ "${1:-}" = projection ]; then
    export AUDIT_PROJECTION_ONLY=1
    shift
    case ${1:-} in
        ''|*[!0-9]*) ;;
        *)
            if [ "$1" -ge 1 ] && [ "$1" -le "$count" ]; then
                export AUDIT_RETRY_PAIR=$1
                shift
            fi
            ;;
    esac
fi
case ${1:-} in
    '') [ $# = 0 ] || exit 2 ;;
    --list) printf '%s\n' "${all[@]}"; echo '90-cleanup.sh is optional; use --only'; exit 0 ;;
    --only|--from) [ $# = 2 ] || exit 2; mode=${1#--}; at=${2#./} ;;
    *) echo 'usage: ./round.sh [projection [PIECE]] [--list | --only STEP | --from STEP]'; exit 2 ;;
esac
todo=()
if [ "$mode" = all ]; then todo=("${steps[@]}")
else
    found=0
    for step in "${all[@]}"; do
        if [ "$step" = "$at" ]; then found=1; fi
        [ "$found" = 1 ] || continue
        if [ "$step" = 90-cleanup.sh ] && [ "$mode" != only ]; then continue; fi
        todo+=("$step")
        [ "$mode" != only ] || break
    done
    [ ${#todo[@]} -gt 0 ] || { echo 'unknown step'; exit 2; }
fi
log=round-$ROUND-end.log
[ "$mode" = all ] || log=round-$ROUND-$mode-${at%.sh}-end.log
{
    echo 'project: model-audit'
    echo "system: $HPC_SYSTEM"
    echo "host: $(hostname -s)"
    echo "round: $ROUND"
    echo 'job: round'
    echo 'event: round-end'
    echo "when: $(date -u +%FT%TZ)"
} > "$log"
rc=0
for step in "${todo[@]}"; do
    echo "step: $step" | tee -a "$log"
    set +e
    "./$step" 2>&1 | narrow | tee -a "$log"
    rc=${PIPESTATUS[0]}
    set -e
    [ "$rc" = 0 ] || break
done
if [ "$rc" = 0 ]; then verdict=OK; else verdict=FAIL; fi
echo "exit: $rc" | tee -a "$log"
echo "VERDICT round $ROUND $verdict" | tee -a "$log"
if sent=$(hpc send "$log" "$log" 2>&1) && [[ "$sent" = *'is on the desk'* ]]; then
    printf '%s\n' "$sent" | narrow
    rm -f "$log" # scratch: the end log is already on the desk
else
    printf '%s\n' "$sent" | narrow
    mkdir -p "$HOME/.hpc/outbox/model-audit/$HPC_SYSTEM"
    cp "$log" "$HOME/.hpc/outbox/model-audit/$HPC_SYSTEM/"
fi
exit "$rc"
