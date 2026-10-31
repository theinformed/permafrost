#!/bin/bash
# 16-probe.sh -- Ask a system's transfer node whether it can run the download, before the round.
# Created by Sean Egan 2026-10-29
# Runs only by name (./round.sh probe, or ./round.sh probe-compute for the same job on the compute queue):
# the kit, the checks, then one ten-minute job whose drop carries "probe: image ok|fail|none hub CODE
# namespaces N pypi CODE python VERSION". The desk reads it before the round files on a system new to the
# census, or one whose nodes failed before.
. ./env.sh
piece=${AUDIT_PROBE_PIECE:-probe}
start_piece "$piece" "Ask a $(piece_queue "$piece") node whether it can run the round"
./10-install-kit.sh
./20-verify.sh
./30-install-reporting.sh
mkdir -p "$AUDIT_WORK/state" "$AUDIT_WORK/logs"
pinned=$(python3 ./snapshot.py create)
say 'pinned copy:' "$pinned"
queued=$(date -u +%FT%TZ)
id=$(submit_batch "$piece" "$pinned/jobs/probe.sh" "$pinned")
printf '%s %s queued %s snapshot %s\n' "$piece" "$id" "$queued" "$pinned" >> "$AUDIT_WORK/state/round-$ROUND-$piece"
echo "probe job: $id"
echo "probe queue: $(piece_queue "$piece")"
echo "probe: queued $queued"
echo 'VERDICT probe OK'
