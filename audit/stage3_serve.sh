#!/bin/bash
# stage3_serve.sh -- Serve one local checkpoint, record its answers, then stop it.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  use the memory watch and a private server process group.
set -euo pipefail
cd "$(dirname "$0")/.."
exec nice -n 19 .venv/bin/python -m audit.stage3_run --serve "$@"
