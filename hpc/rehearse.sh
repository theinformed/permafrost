#!/bin/bash
# rehearse.sh -- Fence a local rehearsal or test command under a 4 GB ceiling.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  cap memory and give an exhausted step one clear failure line.
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
if [ "${1:-}" = --memory-command ]; then
    shift
    command=("$@")
else
    command=(nice -n 19 python3 "$root/hpc/rehearse.py" "$@")
fi
[ ${#command[@]} -gt 0 ] || { echo 'memory command is missing'; exit 2; }
runner=()
if [ -x /root/work/rehearsals/under-4g.sh ]; then
    runner=(/root/work/rehearsals/under-4g.sh)
    ceiling='under-4g.sh (4 GB)'
elif command -v systemd-run >/dev/null && systemd-run --quiet --scope -p MemoryMax=4G true >/dev/null 2>&1; then
    runner=(systemd-run --quiet --scope -p MemoryMax=4G)
    ceiling='MemoryMax=4G'
else
    ceiling='ulimit -v 4000000 (4 GB virtual memory per process)'
fi
# The fallback also bounds children when the scope runner is available.
ulimit -v 4000000
echo "Memory ceiling: $ceiling"
log=$(mktemp)
trap 'rm -f "$log"' EXIT
set +e
"${runner[@]}" "${command[@]}" 2>&1 | tee "$log"
rc=${PIPESTATUS[0]}
set -e
if [ "$rc" = 137 ] || [ "$rc" = 139 ] || grep -Eq 'MemoryError|Cannot allocate memory|cannot allocate memory|std::bad_alloc|out of memory|memory ceiling exceeded' "$log"; then
    echo 'FAIL: a step exceeded the 4 GB memory ceiling.'
    exit 1
fi
exit "$rc"
