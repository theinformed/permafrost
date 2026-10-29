#!/bin/bash
# drops.sh -- Send a drop to the pad with retries, and probe the path there.
# Created by Sean Egan 2026-10-29
# Sourced by env.sh and round.sh.

# send_drop FILE NAME: one try; a drop the node cannot post parks for the desk's next poll.
send_drop() {
    local sent
    sent=$(hpc send "$1" "$2" 2>&1) || true
    printf '%s\n' "$sent"
    [[ "$sent" = *'is on the desk'* ]]
}

# pad_probe: three lines on the path from this node to the pad, for the desk's record.
pad_probe() {
    [ "${AUDIT_REHEARSAL:-0}" != 1 ] || return 0
    local line
    for line in 1 2 3; do
        printf 'pad probe %s: %s\n' "$line" "$(curl -s -o /dev/null --connect-timeout 5 -m 20 \
            -w '%{http_code} %{remote_ip} %{time_appconnect}' https://ai.theinformed.org/ai-web/hpc/api/pad || true)"
    done
}

