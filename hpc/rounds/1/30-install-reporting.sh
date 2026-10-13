#!/bin/bash
# 30-install-reporting.sh -- Put this round's gather script in the managed home.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  leave every other project's reporting files alone.
. ./env.sh
start_piece reporting 'Install the recipe library progress report'
mkdir -p "$HOME/hpc-poll.d"
install -m 644 hpc-poll.d/model-audit.sh "$HOME/hpc-poll.d/model-audit.sh"
echo 'reporting script: round 1'
echo 'VERDICT reporting OK'
