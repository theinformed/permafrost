#!/usr/bin/env bash
# run_library.sh -- Run the reference copies and their comparisons one at a time.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  use the project interpreter and a low process priority.
set -euo pipefail
recipe_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)
cd "$recipe_root"
export HF_HOME="$recipe_root/data/hub"
export XDG_CACHE_HOME="$recipe_root/data/package-cache"
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
exec nice -n 19 "$recipe_root/.venv/bin/python" -m audit.recipes.library "$@"
