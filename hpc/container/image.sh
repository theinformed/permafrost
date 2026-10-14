#!/bin/bash
# image.sh -- Run this round's Python inside the pinned image instead of a venv.
# Created by Sean Egan 2026-10-14
# Sourced by env.sh in an image build. IMAGE.txt names the image and its sha256.
AUDIT_IMAGE=$(sed -n 's/^image: //p' IMAGE.txt)
AUDIT_IMAGE_SHA256=$(sed -n 's/^sha256: //p' IMAGE.txt)
export AUDIT_IMAGE AUDIT_IMAGE_SHA256
IMAGE_RT=
IMAGE_NV=()

image_runtime() {
    # Apptainer first, then its older name; a podman-only system is refused.
    [ -z "$IMAGE_RT" ] || return 0
    if ! command -v apptainer >/dev/null 2>&1 && ! command -v singularity >/dev/null 2>&1; then
        if ! type module >/dev/null 2>&1 && [ -r /etc/profile.d/modules.sh ]; then
            . /etc/profile.d/modules.sh
        fi
        if type module >/dev/null 2>&1; then module load apptainer >/dev/null 2>&1 || true; fi
    fi
    IMAGE_RT=$(command -v apptainer || command -v singularity || true)
    if [ -z "$IMAGE_RT" ]; then
        if command -v podman >/dev/null 2>&1; then
            echo "FAIL $(hostname -s) has podman only; this round needs apptainer"
        else
            echo "FAIL no apptainer or singularity on $(hostname -s)"
        fi
        return 1
    fi
}

image_binds() {
    # Work holds the round, results and originals; anything outside it is added.
    local binds=$WORKDIR path
    for path in "$AUDIT_ORIGINAL" "$PWD" "$HF_HOME" "${TMPDIR:-}"; do
        [ -n "$path" ] && [ -d "$path" ] || continue
        case $(readlink -f "$path")/ in
            "$(readlink -f "$WORKDIR")"/*|"$(readlink -f "$HOME")"/*) ;;
            *) binds=$binds,$path ;;
        esac
    done
    printf '%s\n' "$binds"
}

image_exec() {
    # A clean environment keeps host modules out; the round's settings go in by name.
    image_runtime || return 1
    local prefix=APPTAINERENV_ name
    [ "${IMAGE_RT##*/}" = apptainer ] || prefix=SINGULARITYENV_
    for name in $(compgen -e); do
        case $name in
            AUDIT_*|HF_*|HPC_*|SLURM_*|TRANSFORMERS_*|OMP_*|MKL_*|OPENBLAS_*|CUDA_VISIBLE_DEVICES|\
            PYTHONPATH|WORKDIR|PIECE_LOG|ROUND|USER|TMPDIR)
                export "$prefix$name=${!name}" ;;
        esac
    done
    "$IMAGE_RT" exec "${IMAGE_NV[@]}" --cleanenv --home "$HOME" --bind "$(image_binds)" \
        --pwd "$PWD" "$AUDIT_IMAGE" "$@"
}

image_python() {
    image_exec python3 "$@"
}

image_ready() {
    # Check the image file, then its pins and GPUs from inside, before any work.
    local gpus=${1:-0} have
    [ "${AUDIT_REHEARSAL:-0}" != 1 ] || gpus=0
    image_runtime || return 1
    echo "runtime: $("$IMAGE_RT" --version 2>&1 | head -1)"
    [ -r "$AUDIT_IMAGE" ] || { echo "FAIL image missing: $AUDIT_IMAGE"; return 1; }
    have=$(sha256sum "$AUDIT_IMAGE" | cut -d' ' -f1)
    if [ "$have" != "$AUDIT_IMAGE_SHA256" ]; then
        echo "FAIL image sha256 ${have:0:12} is not the bundled ${AUDIT_IMAGE_SHA256:0:12}"
        return 1
    fi
    echo "image: ${AUDIT_IMAGE##*/} sha256 ${have:0:12}"
    IMAGE_NV=()
    if [ "$gpus" -gt 0 ]; then
        IMAGE_NV=(--nv)
        nvidia-smi
    fi
    export AUDIT_EXPECT_GPUS=$gpus
    image_exec bash ./run-check.sh compute-requirements.txt
}

# Compute nodes without a host python3 use the image's for the small helpers.
if ! command -v python3 >/dev/null 2>&1; then
    python3() { image_python "$@"; }
fi
