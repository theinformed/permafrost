#!/bin/bash
#SBATCH --job-name=model-audit-census-probe
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --output=logs/%x-%j.out
# probe.sh -- One small transfer-queue job: can this system's transfer node run the download?
# Created by Sean Egan 2026-10-31
# The download needs three things of a transfer node: a Python or the image, a working image runtime
# and a route to the hub. Each is reported as a fact and the job ends well whatever it finds, so a
# system that cannot open the image on its transfer nodes (Wheat refused a user namespace once) costs
# a ten-minute job and not a failed download in front of eight compares.
set -euo pipefail
export AUDIT_JOB_STARTED=$(date +%s.%N)
cd "${AUDIT_PINNED_ROUND:?a pinned submission copy is required}"
. ./env.sh
export AUDIT_MEASUREMENT=$AUDIT_WORK/measurements/probe.json
start_piece probe 'Report whether the transfer node can run the download'
# The desk's reporting kit records how this job ends, even when it dies without a word.
hpc_report_on_exit
started=$(date -u -d "@${AUDIT_JOB_STARTED%.*}" +%FT%TZ)
echo "node: $(hostname -s), $(nproc) cores, $(awk '/MemTotal/ {printf "%d GB", $2/1048576}' /proc/meminfo)"
echo "python: $(python3 --version 2>&1)"
standalone=none
if [ -n "${AUDIT_PYTHON_TAR:-}" ]; then
    # The round's own interpreter, unpacked here if no job has yet; its version is the mechanism proof.
    if standalone_python; then standalone=$(python3 --version 2>&1 | tr -d '"' | tr ' ' '-'); else standalone=fail; fi
fi
echo "standalone python: $standalone"
namespaces=$(cat /proc/sys/user/max_user_namespaces 2>/dev/null || echo unknown)
echo "user namespaces allowed: $namespaces"
image=none
if [ -n "${AUDIT_IMAGE:-}" ]; then
    # image_ready opens the image and checks its pins from inside; its own lines say what failed.
    if image_ready 0; then image=ok; else image=fail; fi
fi
echo "image on this node: $image"
hub=$(curl -sS -o /dev/null -w '%{http_code}' --max-time 20 https://huggingface.co/api/models/google/gemma-4-E4B-it 2>/dev/null || echo none)
echo "hub answers: $hub"
pypi=$(curl -sS -o /dev/null -w '%{http_code}' --max-time 20 https://pypi.org/simple/pip/ 2>/dev/null || echo none)
echo "pypi answers: $pypi"
# The scheduler's own limits on this user, so a drop names why jobs wait while nodes idle (Blueback: six of
# ours run and the rest pend with reason None).
if command -v sacctmgr >/dev/null 2>&1; then
    echo "qos limits: $(sacctmgr -nP show qos format=Name,MaxJobsPU,MaxTRESPU,MaxSubmitPU 2>/dev/null | grep -E '^(transfer|background)\|' | tr '\n' ' ')"
    echo "association limits: $(sacctmgr -nP show assoc user=$USER format=Account,Partition,QOS,MaxJobs,GrpJobs,MaxSubmit 2>/dev/null | tr '\n' ' ')"
fi
ended=$(date -u +%FT%TZ)
mkdir -p "${AUDIT_MEASUREMENT%/*}"
printf '{"job": "%s", "host": "%s", "python": "%s", "standalone_python": "%s", "user_namespaces": "%s", "image": "%s", "hub_http": "%s", "pypi_http": "%s", "started": "%s", "ended": "%s"}\n' \
    "$(job_id_env)" "$(hostname -s)" "$(python3 --version 2>&1 | tr -d '"')" "$standalone" "$namespaces" "$image" "$hub" "$pypi" "$started" "$ended" > "$AUDIT_MEASUREMENT"
echo "probe: image $image hub $hub namespaces $namespaces pypi $pypi python $standalone"
echo 'VERDICT probe OK'
