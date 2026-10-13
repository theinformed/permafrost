#!/usr/bin/env bash
# run.sh -- Measure one published checkpoint and its reference recipe copies.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  run serially with local caches and low priority.
set -euo pipefail
survival_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)
cd "$survival_root"
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export HF_HOME="$survival_root/data/hub"
export XDG_CACHE_HOME="$survival_root/data/package-cache"
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
exec nice -n 19 "$survival_root/.venv/bin/python" -m audit.survival.run "$@"
