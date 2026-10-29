#!/bin/bash
# version 1 -- the poll fragment for this project
# model-audit.sh -- Read the recipe round's cards and saved stage markers.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-14  read the census cards and per-piece completion markers.
# Modified: SDE 2026-10-13  read the round's own state and results.
# Modified: SDE 2026-10-13  read cached sizes without walking checkpoint shards.
# Modified: SDE 2026-10-29  read every round under work, and the size line kept in work.
# rounds model-audit/rounds
set -u
project=${WORKDIR:-}/model-audit
cache=$project/space.tsv
[ -s "$cache" ] || cache=$HOME/.hpc/model-audit-space.tsv
if [ -s "$cache" ]; then
    awk -F '\t' '{print "-- kv folder=" $1 " kb=" $2; total += $2} END {print "-- kv space_kb=" total}' "$cache"
else echo '-- kv space_kb=unknown'; fi
for work in "$project"/rounds/*; do
    [ -d "$work/state" ] || continue
    round=${work##*/}
    case $round in ''|*[!0-9]*) continue ;; esac
    echo "-- kv round=$round"
    if [ -f "$work/ARCHIVED" ]; then
        echo "-- kv archived_at=$(head -n 1 "$work/ARCHIVED")"
    else echo '-- kv archived_at=none'; fi
    file=$work/state/round-$round-submissions
    if [ -f "$file" ]; then
        echo "-- file $file"
        head -c 2000 "$file"
    fi
    for marker in "$work"/state/*.done "$work"/pieces/pair-*/state/*.done; do
        [ -f "$marker" ] || continue
        echo "-- note $(basename "$marker")"
    done
    # Only our cards are read, and both the card count and bytes are bounded.
    [ -f "$work/state/round-$round-cards" ] || continue
    while read -r id; do
        case $id in *[!A-Za-z0-9-]*) continue ;; esac
        card=$HOME/.hpc/jobs/$id.json
        [ -f "$card" ] || continue
        echo "-- job $(basename "$card" .json) recipe library"
        head -c 1500 "$card"
        echo
    done < <(tail -n 20 "$work/state/round-$round-cards")
done
