#!/bin/bash
# 16-probe.sh -- Ask a system's transfer node whether it can run the download, before the round.
# Created by Sean Egan 2026-10-29
# Runs only by name (./round.sh --only probe): the kit, the checks, then one ten-minute job on the
# transfer queue whose drop carries "probe: image ok|fail|none hub CODE namespaces N". The desk reads
# it before the round files on a system new to the census, or one whose transfer nodes failed before.
. ./env.sh
start_piece probe 'Ask the transfer node whether it can run the download'
./10-install-kit.sh
./20-verify.sh
./30-install-reporting.sh
mkdir -p "$AUDIT_WORK/state" "$AUDIT_WORK/logs"
pinned=$(python3 ./snapshot.py create)
say 'pinned copy:' "$pinned"
queued=$(date -u +%FT%TZ)
id=$(submit_batch probe "$pinned/jobs/probe.sh" "$pinned")
printf 'probe %s queued %s snapshot %s\n' "$id" "$queued" "$pinned" >> "$AUDIT_WORK/state/round-$ROUND-probe"
echo "probe job: $id"
echo "probe: queued $queued"
echo 'VERDICT probe OK'
