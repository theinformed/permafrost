#!/bin/bash
#SBATCH --job-name=model-audit-census-timing
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --output=logs/%x-%j.out
# timing.sh -- One small background job: the node's facts and how long the queue held it.
# Created by Sean Egan 2026-10-29
set -euo pipefail
export AUDIT_JOB_STARTED=$(date +%s.%N)
cd "${AUDIT_PINNED_ROUND:?a pinned submission copy is required}"
. ./env.sh
export AUDIT_MEASUREMENT=$AUDIT_WORK/measurements/timing.json
start_piece timing 'Report the node and the queue wait'
# The desk's reporting kit records how this job ends, even when it dies without a word.
hpc_report_on_exit
started=$(date -u -d "@${AUDIT_JOB_STARTED%.*}" +%FT%TZ)
queued=$(cat "$AUDIT_WORK/state/timing-queued" 2>/dev/null || echo unknown)
echo "node: $(hostname -s), $(nproc) cores, $(awk '/MemTotal/ {printf "%d GB", $2/1048576}' /proc/meminfo)"
echo "python: $(python3 --version 2>&1)"
echo "round: $(python3 ./census.py round), $(python3 ./census.py count) pairs"
ended=$(date -u +%FT%TZ)
mkdir -p "${AUDIT_MEASUREMENT%/*}"
printf '{"job": "%s", "host": "%s", "queued": "%s", "started": "%s", "ended": "%s"}\n' \
    "$(job_id_env)" "$(hostname -s)" "$queued" "$started" "$ended" > "$AUDIT_MEASUREMENT"
echo "timing: queued $queued started $started ended $ended"
echo 'VERDICT timing OK'
