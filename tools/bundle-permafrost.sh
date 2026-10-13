#!/bin/bash
# bundle-permafrost.sh -- Pack a round and write its two desk cards.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  keep the copy and its dependent run together.
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
exec python3 "$root/hpc/bundle.py" "$@"
