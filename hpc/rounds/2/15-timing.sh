#!/bin/bash
# 15-timing.sh -- Measure a system's background queue with one small job before the compares.
# Created by Sean Egan 2026-10-29
# Runs only by name (./round.sh --only timing): the kit, the checks, then one five-minute job
# whose drop carries "timing: queued T started T ended T". The desk reads it before the round.
. ./env.sh
start_piece timing 'Measure the background queue with one five-minute job'
./10-install-kit.sh
./20-verify.sh
./30-install-reporting.sh
mkdir -p "$AUDIT_WORK/state" "$AUDIT_WORK/logs"
pinned=$(python3 ./snapshot.py create)
say 'pinned copy:' "$pinned"
queued=$(date -u +%FT%TZ)
printf '%s\n' "$queued" > "$AUDIT_WORK/state/timing-queued"
id=$(submit_batch timing "$pinned/jobs/timing.sh" "$pinned")
printf 'timing %s queued %s snapshot %s\n' "$id" "$queued" "$pinned" >> "$AUDIT_WORK/state/round-$ROUND-timing"
echo "timing job: $id"
echo "timing: queued $queued"
echo 'VERDICT timing OK'
