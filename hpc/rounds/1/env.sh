#!/bin/bash
# env.sh -- Name the round's work directories and reporting functions.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  keep round results together and record the pinned job copy.
# Modified: SDE 2026-10-13  find the center's Python module by name pattern; there is no plain python3 module.
# Modified: SDE 2026-10-13  send bounded card and log drops on exit.
set -euo pipefail
export HPC_PROJECT=model-audit ROUND=1 HPC_SYSTEM=${HPC_SYSTEM:-nautilus}
export PATH=$HOME/bin:$PATH
: "${WORKDIR:?WORKDIR is required}"
export AUDIT_WORK=$WORKDIR/model-audit/rounds/1
export AUDIT_ROUND=$(pwd -P)
export HF_HOME=$WORKDIR/model-audit/cache
export PIP_CACHE_DIR=$AUDIT_WORK/cache/pip PYTHONDONTWRITEBYTECODE=1
export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
export AUDIT_BASE=${AUDIT_BASE:-mistralai/Mistral-Small-3.2-24B-Instruct-2506}
export AUDIT_NAME=${AUDIT_NAME:-mistral-small-3.2-24b}
export AUDIT_ORIGINAL=$WORKDIR/model-audit/originals/$AUDIT_NAME
export AUDIT_DERIVED=$AUDIT_WORK/derived/$AUDIT_NAME/single-projection
export AUDIT_MEASUREMENT=$AUDIT_WORK/measurements/$AUDIT_NAME/single-projection.json
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
    if [ "$rc" = 0 ]; then hpc_job_finish 'piece finished'
    else hpc_job_fail "piece failed with exit $rc"; fi
    local id=${SLURM_JOB_ID:-$HPC_JOB_ID}
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
        tail -n 200 "$PIECE_LOG" | head -c 800000
    } > "$drop"
    # A delivery fault must leave the scientific exit status alone.
    local sent
    if sent=$(hpc send "$drop" "$id-drop.txt" 2>&1) && [[ "$sent" = *'is on the desk'* ]]; then
        printf '%s\n' "$sent"
        printf '%s\n' "$id" > "$AUDIT_WORK/state/pad-confirmed"
    else
        printf '%s\n' "$sent"
        mkdir -p "$HOME/.hpc/outbox/$HPC_PROJECT/$HPC_SYSTEM"
        cp "$drop" "$HOME/.hpc/outbox/$HPC_PROJECT/$HPC_SYSTEM/"
    fi
    exit "$rc"
}

start_piece() {
    export HPC_JOB_ID=${SLURM_JOB_ID:-round-1-${1}-$$}
    PIECE_LOG=$AUDIT_WORK/logs/$HPC_JOB_ID.out
    export PIECE_LOG
    printf '%s\n' "$HPC_JOB_ID" >> "$AUDIT_WORK/state/round-1-cards"
    exec > >(tee -a "$PIECE_LOG") 2>&1
    hpc_job_start "$2" --project model-audit --study 'Recipe fingerprint library' --row MODEL-AUDIT-1 --log "$PIECE_LOG"
    trap finish_piece EXIT
    trap 'exit 143' TERM HUP
    trap 'exit 130' INT
    if [ -n "${SLURM_JOB_ID:-}" ]; then
        export AUDIT_BUILD_STAMP=$(cat BUILD-STAMP.txt)
        export AUDIT_SNAPSHOT_SHA256=$(cut -d' ' -f1 ../snapshot.sha256)
        python3 ./snapshot.py card "$HOME/.hpc/jobs/$HPC_JOB_ID.json"
        python3 ./snapshot.py verify
    fi
}

compute_python() {
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
