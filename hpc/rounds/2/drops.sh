#!/bin/bash
# drops.sh -- Send a drop to the pad with retries, and probe the path there.
# Created by Sean Egan 2026-10-29
# Sourced by env.sh and round.sh.

# send_drop FILE NAME: three tries a minute apart; the TLS front resets some handshakes.
send_drop() {
    local try sent
    for try in 1 2 3; do
        if sent=$(hpc send "$1" "$2" 2>&1) && [[ "$sent" = *'is on the desk'* ]]; then
            printf '%s\n' "$sent"
            return 0
        fi
        [ "$try" = 3 ] || [ "${AUDIT_REHEARSAL:-0}" = 1 ] || sleep 60
    done
    printf '%s\n' "$sent"
    return 1
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

