#!/bin/bash
# rehearse-vps.sh -- Run just the synthetic census under the shared memory ceiling.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  take the rehearsal lock before the fenced command.
# Modified: SDE 2026-10-15  wait our turn for the lock rather than giving up.
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
mkdir -p "$root/.tmp/rehearsals"
export TMPDIR=$root/.tmp/rehearsals
lock=${AUDIT_REHEARSAL_LOCK:-/root/work/rehearsals/lock}
# An existing lock can be held read-only; the file itself stays untouched.
if [ -r "$lock" ]; then
    exec 9<"$lock"
else
    lock=$root/.tmp/rehearsals/lock
    exec 9>"$lock"
fi
# One rehearsal at a time on this machine; wait for whoever holds it.
flock 9
echo "Rehearsal lock: $lock"
exec "$root/hpc/rehearse.sh" --memory-command nice -n 19 \
    "$root/.venv/bin/python" "$root/hpc/rehearse_round2.py" "$@"
