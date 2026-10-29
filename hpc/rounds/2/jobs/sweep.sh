#!/bin/bash
#SBATCH --job-name=model-audit-census-sweep
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --output=logs/%x-%j.out
# sweep.sh -- Delete each original once every pair that reads it has saved its reports.
# Created by Sean Egan 2026-10-29
set -euo pipefail
export AUDIT_JOB_STARTED=$(date +%s.%N)
cd "${AUDIT_PINNED_ROUND:?a pinned submission copy is required}"
. ./env.sh
# The drop carries the sweep's record instead of a pair's reports.
export AUDIT_MEASUREMENT=$AUDIT_WORK/measurements/sweep.json
start_piece sweep 'Delete the originals whose pairs all have reports'
python3 ./census.py sweep
echo 'VERDICT sweep OK'
