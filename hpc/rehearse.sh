#!/bin/bash
# rehearse.sh -- Run the complete round in a fake home and work folder.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  keep model downloads out of the dry run.
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
exec nice -n 19 python3 "$root/hpc/rehearse.py" "$@"
