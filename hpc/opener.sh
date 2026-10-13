#!/bin/bash
# model-audit-round.sh -- Open this round's tar and run its steps.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  check the round number before opening anything.
set -euo pipefail
[ "${1:-}" = '__ROUND__' ] || { echo 'expected round __ROUND__'; exit 2; }
shift
[ -d "${WORKDIR:-}" ] || { echo 'WORKDIR must name an existing directory'; exit 1; }
folder=$HOME/model-audit/rounds/__ROUND__
mkdir -p "$folder"
# Check the tail before tar sees it. An incomplete copy is no working round.
payload=$(mktemp "$WORKDIR/round-payload.XXXXXX")
trap 'rm -f "$payload"' EXIT
sed '1,/^__PAYLOAD__$/d' "$0" > "$payload"
echo '__SHA__  '"$payload" | sha256sum -c -
tar -xf "$payload" -C "$folder"
cd "$folder"
sha256sum -c SHA256SUMS > /dev/null
./round.sh "$@"
exit $?
__PAYLOAD__
