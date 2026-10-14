#!/bin/bash
# round.sh -- Run this round's numbered steps and send the end log.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  keep cleanup available only by its own name.
# Modified: SDE 2026-10-14  accept a projection retry as a plain argument.
set -uo pipefail
cd "$(dirname "$0")" || exit 1
export ROUND=1 HPC_PROJECT=model-audit HPC_SYSTEM=${HPC_SYSTEM:-nautilus}
export PATH=$HOME/bin:$PATH
steps=(10-install-kit.sh 20-verify.sh 30-install-reporting.sh 40-submit.sh)
all=("${steps[@]}" 90-cleanup.sh)
mode=all
at=
if [ "${1:-}" = projection ]; then
    export AUDIT_PROJECTION_ONLY=1
    shift
fi
case ${1:-} in
    '') [ $# = 0 ] || exit 2 ;;
    --list) printf '%s\n' "${all[@]}"; echo '90-cleanup.sh is optional; use --only'; exit 0 ;;
    --only|--from) [ $# = 2 ] || exit 2; mode=${1#--}; at=${2#./} ;;
    *) echo 'usage: ./round.sh [projection] [--list | --only STEP | --from STEP]'; exit 2 ;;
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
log=round-1-end.log
[ "$mode" = all ] || log=round-1-$mode-${at%.sh}-end.log
{
    echo 'project: model-audit'
    echo "system: $HPC_SYSTEM"
    echo "host: $(hostname -s)"
    echo 'round: 1'
    echo 'job: round'
    echo 'event: round-end'
    echo "when: $(date -u +%FT%TZ)"
} > "$log"
rc=0
for step in "${todo[@]}"; do
    echo "step: $step" | tee -a "$log"
    "./$step" 2>&1 | tee -a "$log"
    rc=${PIPESTATUS[0]}
    [ "$rc" = 0 ] || break
done
if [ "$rc" = 0 ]; then verdict=OK; else verdict=FAIL; fi
echo "exit: $rc" | tee -a "$log"
echo "VERDICT round 1 $verdict" | tee -a "$log"
if sent=$(hpc send "$log" "$log" 2>&1) && [[ "$sent" = *'is on the desk'* ]]; then
    echo "$sent"
    rm -f "$log" # scratch: the end log is already on the desk
else
    echo "$sent"
    mkdir -p "$HOME/.hpc/outbox/model-audit/$HPC_SYSTEM"
    cp "$log" "$HOME/.hpc/outbox/model-audit/$HPC_SYSTEM/"
fi
exit "$rc"
