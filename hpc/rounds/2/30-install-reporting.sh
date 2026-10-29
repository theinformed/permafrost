#!/bin/bash
# 30-install-reporting.sh -- Put this round's gather script in the managed home.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-14  install the census gather fragment.
# Modified: SDE 2026-10-13  leave every other project's reporting files alone.
# Modified: SDE 2026-10-29  name the round from batch.json.
. ./env.sh
start_piece reporting 'Install the recipe library progress report'
mkdir -p "$HOME/hpc-poll.d"
install -m 644 hpc-poll.d/model-audit.sh "$HOME/hpc-poll.d/model-audit.sh"
echo "reporting script: round $ROUND"
echo 'VERDICT reporting OK'
