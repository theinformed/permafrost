#!/bin/bash
# version 1 2026-10-13
# model-audit.sh -- Read the recipe round's cards and saved stage markers.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  read cached sizes without walking checkpoint shards.
# rounds model-audit/rounds
set -u
work=${WORKDIR:-}/model-audit
round=$HOME/model-audit/rounds/1
cache=$HOME/.hpc/model-audit-space.tsv
if [ -s "$cache" ]; then
    awk -F '\t' '{print "-- kv folder=" $1 " kb=" $2; total += $2} END {print "-- kv space_kb=" total}' "$cache"
else echo '-- kv space_kb=unknown'; fi
if [ -f "$work/ARCHIVED" ]; then
    echo "-- kv archived_at=$(head -n 1 "$work/ARCHIVED")"
else echo '-- kv archived_at=none'; fi
echo '-- kv round=1'
for file in "$work"/state/round-1-submissions "$round"/submission-status.txt; do
    [ -f "$file" ] || continue
    echo "-- file $file"
    head -c 2000 "$file"
done
for marker in "$work"/state/*.done; do
    [ -f "$marker" ] || continue
    echo "-- note $(basename "$marker")"
done
# Only our cards are read, and both the card count and bytes are bounded.
if [ ! -f "$work/state/round-1-cards" ]; then exit 0; fi
while read -r id; do
    case $id in *[!A-Za-z0-9-]*) continue ;; esac
    card=$HOME/.hpc/jobs/$id.json
    [ -f "$card" ] || continue
    echo "-- job $(basename "$card" .json) recipe library"
    head -c 1500 "$card"
    echo
done < <(tail -n 20 "$work/state/round-1-cards")
