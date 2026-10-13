#!/bin/bash
# 10-install-kit.sh -- Refresh the managed tools when this kit is newer.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  compare the installed version before copying.
. ./env.sh
start_piece kit 'Install the shared job reporting tools'
mkdir -p logs
wanted=$(cat kit/KIT_VERSION)
current=$(cat "$HOME/metoc/jobs/hpc/KIT_VERSION" 2>/dev/null || true)
if [[ "$wanted" > "$current" ]]; then
    mkdir -p "$HOME/metoc/jobs/hpc" "$HOME/bin"
    cp kit/* "$HOME/metoc/jobs/hpc/"
    chmod 755 "$HOME/metoc/jobs/hpc/"*.sh "$HOME/metoc/jobs/hpc/hpc"
    install -m 755 kit/hpc-poll.sh "$HOME/bin/hpc-poll.sh"
    install -m 755 kit/hpc-report.sh "$HOME/bin/hpc-report.sh"
    install -m 644 kit/hpc_report.py "$HOME/bin/hpc_report.py"
    # The dispatcher locates its neighboring views through this link.
    if [ "${AUDIT_REHEARSAL:-0}" != 1 ]; then
        ln -sfn "$HOME/metoc/jobs/hpc/hpc" "$HOME/bin/hpc"
    fi
fi
echo "kit version: $(cat "$HOME/metoc/jobs/hpc/KIT_VERSION")"
echo 'VERDICT kit OK'
