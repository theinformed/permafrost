#!/bin/bash
# 10-install-kit.sh -- Refresh the managed tools when this kit is newer.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-14  reuse the managed reporting kit for the census.
# Modified: SDE 2026-10-29  rewrite a plain maker list left on the cluster as the hashed guard.
# Modified: SDE 2026-10-13  compare the installed version before copying.
# Modified: SDE 2026-10-30  move each kit file into place instead of writing over a running one.
. ./env.sh
start_piece kit 'Install the shared job reporting tools'
mkdir -p logs
wanted=$(cat kit/KIT_VERSION)
current=$(cat "$HOME/metoc/jobs/hpc/KIT_VERSION" 2>/dev/null || true)
if [[ "$wanted" > "$current" ]]; then
    mkdir -p "$HOME/metoc/jobs/hpc" "$HOME/bin"
    # The desk's poll may be running the installed dispatcher this second (Blueback 5282: "Text file busy");
    # each file lands under a temporary name and moves into place, which never writes into an open binary.
    for file in kit/*; do
        cp "$file" "$HOME/metoc/jobs/hpc/.${file##*/}.new"
        mv -f "$HOME/metoc/jobs/hpc/.${file##*/}.new" "$HOME/metoc/jobs/hpc/${file##*/}"
    done
    chmod 755 "$HOME/metoc/jobs/hpc/"*.sh "$HOME/metoc/jobs/hpc/hpc"
    install -m 755 kit/hpc-poll.sh "$HOME/bin/hpc-poll.sh"
    install -m 755 kit/hpc-report.sh "$HOME/bin/hpc-report.sh"
    install -m 644 kit/hpc_report.py "$HOME/bin/hpc_report.py"
    # The dispatcher locates its neighboring views through this link.
    if [ "${AUDIT_REHEARSAL:-0}" != 1 ]; then
        ln -sfn "$HOME/metoc/jobs/hpc/hpc" "$HOME/bin/hpc"
    fi
fi
# No maker name sits on a cluster: a plain list left by an earlier round becomes the hashed
# guard in place, with the screen that reads it, so a queued job that names the file still runs.
for list in $(find . "${WORKDIR:-$HOME}/model-audit" "$HOME/model-audit" -name banned-makers.txt 2>/dev/null | sort -u); do
    if [ "$(dirname "$list")" -ef . ]; then
        rm -f "$list"
        echo "stale list removed: $list"
    else
        cp maker-guard.sha256 "$list"
        cp lineage.py "$(dirname "$list")/lineage.py"
        echo "guard rewritten: $list"
    fi
done
# The project's pad token line arrives by its own card beside the shared file and is merged once,
# so another project's line in ~/.hpc/pad-token is never overwritten.
line=$HOME/.hpc/pad-token-model-audit
if [ -f "$line" ] && ! grep -q '^model-audit ' "$HOME/.hpc/pad-token" 2>/dev/null; then
    mkdir -p "$HOME/.hpc"
    cat "$line" >> "$HOME/.hpc/pad-token"
    chmod 600 "$HOME/.hpc/pad-token"
    echo 'pad token: model-audit line added'
fi
echo "kit version: $(cat "$HOME/metoc/jobs/hpc/KIT_VERSION")"
echo "ipv4 report: $(grep -c 'curl -4' "$HOME/bin/hpc-report.sh" 2>/dev/null || echo 0)"
echo 'VERDICT kit OK'
