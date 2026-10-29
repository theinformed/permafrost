#!/bin/bash
# env.sh -- Name the round's work directories and reporting functions.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-14  name each CPU piece and keep its download inputs separate.
# Modified: SDE 2026-10-13  keep round results together and record the pinned job copy.
# Modified: SDE 2026-10-13  find the center's Python module by name pattern; there is no plain python3 module.
# Modified: SDE 2026-10-13  send bounded card and log drops on exit.
# Modified: SDE 2026-10-15  keep every printed line within 100 columns.
# Modified: SDE 2026-10-29  a parked drop is the normal path; the drop gate is gone; a pad probe.
# Modified: SDE 2026-10-29  round from batch.json; queues, scheduler and image from the systems table.
set -euo pipefail
export HPC_PROJECT=model-audit HPC_SYSTEM=${HPC_SYSTEM:-nautilus}
ROUND=$(python3 ./census.py round)
export ROUND
export PATH=$HOME/bin:$PATH
: "${WORKDIR:?WORKDIR is required}"
export AUDIT_WORK=$WORKDIR/model-audit/rounds/$ROUND
export AUDIT_ROUND=$(pwd -P)
export HF_HOME=$WORKDIR/model-audit/cache
export PIP_CACHE_DIR=$AUDIT_WORK/cache/pip PYTHONDONTWRITEBYTECODE=1
# Home on some systems is over quota; tool caches stay in work.
export XDG_CACHE_HOME=$AUDIT_WORK/cache/xdg
export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
[ ! -f system.sh ] || . ./system.sh
. ./drops.sh
. ./scheduler.sh
# An image build runs its compute Python inside the pinned image.
[ -z "${AUDIT_IMAGE:-}" ] || . ./image.sh
export CUDA_VISIBLE_DEVICES=''
export AUDIT_PAIR=${AUDIT_PAIR:-1}
export AUDIT_NAME=pair-$AUDIT_PAIR
export AUDIT_PIECE_WORK=$AUDIT_WORK/pieces/$AUDIT_NAME
export AUDIT_DERIVED=$AUDIT_WORK/derived/$AUDIT_NAME
export AUDIT_MEASUREMENT=$AUDIT_WORK/measurements/$AUDIT_NAME/weights.json
# The transfer job owns inputs; a compare try owns its derived hard links.
pair_env=$(python3 ./census.py env "$AUDIT_PAIR")
eval "$pair_env"
# Every printed line stays within 100 columns; a longer line from a tool wraps.
narrow() {
    if command -v stdbuf >/dev/null 2>&1; then stdbuf -oL fold -w 100; else fold -w 100; fi
}

# say WHAT [WHERE] [WHY]: each part on its own line, wrapped and indented.
say() {
    local indent='' part
    for part in "$@"; do
        [ -n "$part" ] || continue
        printf '%s\n' "$part" | fold -w $((100 - ${#indent})) | sed "s/^/$indent/"
        indent='  '
    done
}

# queue_args QUEUE: the bundled system's words for the transfer or background queue.
queue_args() {
    local words
    case $1 in
        transfer) words=${AUDIT_TRANSFER_ARGS:-} ;;
        background) words=${AUDIT_BACKGROUND_ARGS:-} ;;
        *) echo "unknown queue: $1" >&2; return 1 ;;
    esac
    [ -n "$words" ] || { echo "no $1 queue words for $HPC_SYSTEM" >&2; return 1; }
    printf '%s\n' "$words"
}

# fips_guard: where the node runs FIPS, OpenSSL loads only its default provider.
# A failed FIPS self-test otherwise kills Python with "cannot create SSL context".
fips_guard() {
    local flag=0 conf
    if [ -r "${FIPS_PROC_FILE:-/proc/sys/crypto/fips_enabled}" ]; then
        read -r flag < "${FIPS_PROC_FILE:-/proc/sys/crypto/fips_enabled}" || true
    fi
    if [ "$flag" != 1 ]; then
        echo 'fips: off, nothing applied'
        return 0
    fi
    conf=$AUDIT_WORK/fips/openssl-${HPC_JOB_ID:-$$}.cnf
    mkdir -p "${conf%/*}"
    printf '%s\n' 'openssl_conf = openssl_init' '[openssl_init]' 'providers = provider_sect' \
        '[provider_sect]' 'default = default_sect' '[default_sect]' 'activate = 1' > "$conf"
    unset OPENSSL_MODULES APPTAINERENV_OPENSSL_MODULES SINGULARITYENV_OPENSSL_MODULES
    # Work is bound into the image, so the same file serves the host and the image.
    export OPENSSL_CONF=$conf OPENSSL_FORCE_FIPS_MODE=0
    export APPTAINERENV_OPENSSL_CONF=$conf APPTAINERENV_OPENSSL_FORCE_FIPS_MODE=0
    export SINGULARITYENV_OPENSSL_CONF=$conf SINGULARITYENV_OPENSSL_FORCE_FIPS_MODE=0
    echo 'fips: on; OpenSSL set to its default provider'
}

# node_facts PYTHON: one line each for the node, its cores, memory and Python.
node_facts() {
    echo "node: $(hostname -s)"
    echo "cores: $(nproc)"
    awk '/^MemTotal:/ {t = $2} /^MemFree:/ {f = $2} /^MemAvailable:/ {a = $2}
         END {printf "memory: %d MB total, %d MB free, %d MB available\n", t / 1024, f / 1024, a / 1024}' \
        /proc/meminfo
    echo "python: $("$@" --version 2>&1 | head -n 1)"
}

mkdir -p "$AUDIT_WORK/logs" "$AUDIT_WORK/state" "$HOME/.hpc/jobs"
# The first step can report before the tools have been installed.
if [ -n "${AUDIT_PINNED_ROUND:-}" ]; then
    . ./kit/hpc-report.sh
elif [ -f "$HOME/bin/hpc-report.sh" ]; then
    . "$HOME/bin/hpc-report.sh"
else
    . ./kit/hpc-report.sh
fi
export HPC_DROP=0

finish_piece() {
    local rc=$?
    trap - EXIT
    # hpc_report_on_exit may have recorded the ending already; one record per job.
    if [ -n "${_HPC_DONE:-}" ]; then :
    elif [ "$rc" = 0 ]; then hpc_job_finish 'piece finished'
    else hpc_job_fail "piece failed with exit $rc"; fi
    local id=$HPC_JOB_ID
    local drop=$AUDIT_WORK/logs/$id-drop.txt
    {
        echo "project: $HPC_PROJECT"
        echo "system: $HPC_SYSTEM"
        echo "host: $(hostname -s)"
        echo "round: $ROUND"
        echo "job: $id"
        if [ "$rc" = 0 ]; then echo 'event: finished'; else echo 'event: failed'; fi
        echo "exit: $rc"
        echo "when: $(date -u +%FT%TZ)"
        echo "build: ${AUDIT_BUILD_STAMP:-unknown}"
        echo "snapshot: ${AUDIT_SNAPSHOT_SHA256:-none}"
        echo "pinned: ${AUDIT_PINNED_ROUND:-none}"
        cat "$HOME/.hpc/jobs/$id.json"
        if [ -f "${AUDIT_MEASUREMENT%/*}/receipt.json" ]; then
            cat "${AUDIT_MEASUREMENT%/*}/receipt.json"
            head -c 80000 "${AUDIT_MEASUREMENT%/*}/card.md"
        elif [[ "${AUDIT_MEASUREMENT##*/}" = @(sweep|timing).json ]] && [ -f "$AUDIT_MEASUREMENT" ]; then
            head -c 80000 "$AUDIT_MEASUREMENT"
        fi
        tail -n 200 "$PIECE_LOG" | head -c 800000
    } > "$drop"
    # A delivery fault must leave the scientific exit status alone.
    local sent
    if sent=$(send_drop "$drop" "$id-drop.txt") && [[ "$sent" = *'is on the desk'* ]]; then
        printf '%s\n' "$sent"
        printf '%s\n' "$id" > "$AUDIT_WORK/state/pad-confirmed"
    else
        # The sender parks a drop it cannot post; the desk's poll sends it from the login node.
        printf '%s\n' "$sent"
        mkdir -p "$HOME/.hpc/outbox/$HPC_PROJECT/$HPC_SYSTEM"
        cp "$drop" "$HOME/.hpc/outbox/$HPC_PROJECT/$HPC_SYSTEM/"
    fi
    exit "$rc"
}

start_piece() {
    local scheduled
    scheduled=$(job_id_env)
    export HPC_JOB_ID=${scheduled:-round-$ROUND-${1}-$$}
    PIECE_LOG=$AUDIT_WORK/logs/$HPC_JOB_ID.out
    export PIECE_LOG
    printf '%s\n' "$HPC_JOB_ID" >> "$AUDIT_WORK/state/round-$ROUND-cards"
    exec > >(narrow | tee -a "$PIECE_LOG") 2>&1
    hpc_job_start "$2" --project model-audit --study 'Checkpoint census' --row MODEL-AUDIT-1 --log "$PIECE_LOG"
    trap finish_piece EXIT
    trap 'exit 143' TERM HUP
    trap 'exit 130' INT
    if [ -n "$scheduled" ]; then
        export AUDIT_BUILD_STAMP=$(cat BUILD-STAMP.txt)
        export AUDIT_SNAPSHOT_SHA256=$(cut -d' ' -f1 ../snapshot.sha256)
        python3 ./snapshot.py card "$HOME/.hpc/jobs/$HPC_JOB_ID.json"
        python3 ./snapshot.py verify
    fi
}

compute_python() {
    # An image build checks the image and its pins; the jobs then run Python inside it.
    if [ -n "${AUDIT_IMAGE:-}" ]; then
        image_ready 0
        return
    fi
    # Modules are loaded in jobs, leaving the login interpreter alone.
    # Nautilus has no module called python3; its Python modules are python/3.11/3.11 and kin.
    if [ "${AUDIT_REHEARSAL:-0}" != 1 ]; then
        if ! type module >/dev/null 2>&1 && [ -r /etc/profile.d/modules.sh ]; then . /etc/profile.d/modules.sh; fi
        loaded=""
        for candidate in python/3.11/3.11 $(module -t avail python/3.1 2>&1 | grep '^python/3\.1' | sed 's/(.*//'); do
            if module load "$candidate" >/dev/null 2>&1; then loaded=$candidate; break; fi
        done
        if [ -z "$loaded" ]; then echo "no Python 3.11 module found (tried python/3.11/3.11 and python/3.1*)"; module -t avail python 2>&1 | head -20; return 1; fi
        echo "Python module: $loaded ($(python3 --version 2>&1))"
    fi
    if [ -n "${AUDIT_COMPUTE_BIN:-}" ]; then
        export PATH=$AUDIT_COMPUTE_BIN:$PATH
    fi
    python3 ./runtime.py
}
