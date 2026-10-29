#!/bin/bash
# scheduler.sh -- Submit and test this round's jobs on Slurm or PBS through the same calls.
# Created by Sean Egan 2026-10-29
# Sourced by env.sh. system.sh names the scheduler, its queue words, the subproject and the
# time limits; every value that differs between systems goes on the command line from here.

SWEEP_TIME_LIMIT=00:30:00

# job_id_env: this job's scheduler id without a server suffix; nothing outside a job.
job_id_env() {
    if [ -n "${SLURM_JOB_ID:-}" ]; then
        printf '%s\n' "$SLURM_JOB_ID"
    elif [ -n "${PBS_JOBID:-}" ]; then
        printf '%s\n' "${PBS_JOBID%%.*}"
    fi
}

# piece_queue PIECE: the download uses the transfer queue; everything else runs in background.
piece_queue() {
    if [ "$1" = download ]; then echo transfer; else echo background; fi
}

piece_time() {
    case $1 in
        download) printf '%s\n' "${AUDIT_TRANSFER_TIME_LIMIT:-$AUDIT_TIME_LIMIT}" ;;
        sweep) printf '%s\n' "$SWEEP_TIME_LIMIT" ;;
        *) printf '%s\n' "$AUDIT_TIME_LIMIT" ;;
    esac
}

piece_memory() {
    case $1 in
        download) printf '%s\n' "${AUDIT_PBS_MEM_DOWNLOAD:?no download memory for this system}" ;;
        sweep) printf '%s\n' "${AUDIT_PBS_MEM_SWEEP:?no sweep memory for this system}" ;;
        *) printf '%s\n' "${AUDIT_PBS_MEM_PROJECT:?no compare memory for this system}" ;;
    esac
}

piece_name() {
    if [ "$1" = project ]; then echo model-audit-census-compare; else echo "model-audit-census-$1"; fi
}

# scheduler_words PIECE SCRIPT PINNED [DEPENDENCY]: fill SCHEDULER_WORDS for one job.
# DEPENDENCY is afterok:ID or afterany:ID:ID; Slurm and PBS spell both the same way.
scheduler_words() {
    local piece=$1 script=$2 pinned=$3 dependency=${4:-} words name
    words=$(queue_args "$(piece_queue "$piece")") || return 1
    : "${AUDIT_SUBPROJECT:?no subproject for this system}"
    : "${AUDIT_TIME_LIMIT:?no time limit for this system}"
    name=$(piece_name "$piece")
    mapfile -t SCHEDULER_WORDS <<< "$words"
    SCHEDULER_VARS=
    case ${AUDIT_SCHEDULER:-slurm} in
        slurm)
            SCHEDULER_WORDS+=("--account=$AUDIT_SUBPROJECT" "--time=$(piece_time "$piece")"
                "--job-name=$name" "--output=$AUDIT_WORK/logs/%x-%j.out" "--chdir=$pinned"
                "--export=ALL,AUDIT_PINNED_ROUND=$pinned,AUDIT_PAIR=$AUDIT_PAIR")
            if [ -n "$dependency" ]; then
                SCHEDULER_WORDS+=("--dependency=$dependency")
                [ "${dependency%%:*}" != afterok ] || SCHEDULER_WORDS+=(--kill-on-invalid-dep=yes)
            fi
            ;;
        pbs)
            case $pinned$WORKDIR in
                *,*) echo 'PBS variables cannot carry a comma in a path' >&2; return 1 ;;
            esac
            local memory stamp
            memory=$(piece_memory "$piece") || return 1
            stamp=$(date -u +%Y%m%dT%H%M%S)
            # The owner tag goes first in this list, on the qsub line itself.
            SCHEDULER_VARS="WORKDIR=$WORKDIR,AUDIT_PINNED_ROUND=$pinned,AUDIT_PAIR=$AUDIT_PAIR"
            SCHEDULER_WORDS+=(-A "$AUDIT_SUBPROJECT"
                -l "select=1:ncpus=${AUDIT_PBS_NCPUS:-1}:mem=$memory"
                -l "walltime=$(piece_time "$piece")" -N "$name" -S /bin/bash -j oe
                -o "$AUDIT_WORK/logs/$name-$stamp-$$-$AUDIT_PAIR.out")
            [ -z "$dependency" ] || SCHEDULER_WORDS+=(-W "depend=$dependency")
            ;;
        *) echo "unknown scheduler: $AUDIT_SCHEDULER" >&2; return 1 ;;
    esac
    SCHEDULER_WORDS+=("$script")
}

# submit_batch PIECE SCRIPT PINNED [DEPENDENCY]: queue one job and print its id.
submit_batch() {
    local id
    scheduler_words "$@" || return 1
    case ${AUDIT_SCHEDULER:-slurm} in
        slurm)
            id=$(sbatch --parsable --comment=project=model-audit "${SCHEDULER_WORDS[@]}") || return $?
            id=${id%%;*}
            ;;
        pbs)
            id=$(qsub -v "HPC_PROJECT=model-audit,$SCHEDULER_VARS" "${SCHEDULER_WORDS[@]}") || return $?
            id=$(printf '%s' "$id" | tr -d '[:space:]')
            ;;
    esac
    [[ "$id" =~ ^[0-9]+(\.[A-Za-z0-9._-]+)?$ ]] || { echo "$1 submission returned no job id" >&2; return 1; }
    printf '%s\n' "$id"
}

# pbs_word_check: every PBS request word is plain text with the expected shape.
pbs_word_check() {
    local word previous=
    for word in "${SCHEDULER_WORDS[@]}"; do
        [[ "$word" =~ ^[A-Za-z0-9_./:=,%+-]+$ ]] || { echo "PBS word refused: $word"; return 1; }
        case $previous in
            -A) [[ "$word" =~ ^[A-Za-z0-9_-]+$ ]] || { echo "PBS account refused: $word"; return 1; } ;;
            -q) [[ "$word" =~ ^[A-Za-z0-9_]+$ ]] || { echo "PBS queue refused: $word"; return 1; } ;;
            -l)
                [[ "$word" =~ ^select=1:ncpus=[1-9][0-9]*:mem=[1-9][0-9]*[kmgt]?b$ ||
                   "$word" =~ ^walltime=[0-9]{2}:[0-5][0-9]:[0-5][0-9]$ ]] ||
                    { echo "PBS resource refused: $word"; return 1; }
                ;;
        esac
        previous=$word
    done
    [[ " ${SCHEDULER_WORDS[*]} " = *' -q '* ]] || { echo 'PBS request names no queue'; return 1; }
}

# test_submission PIECE SCRIPT: check one job's request without queueing it.
test_submission() {
    local piece=$1 script=$2
    bash -n "$script"
    scheduler_words "$piece" "$script" "$PWD" || return 1
    case ${AUDIT_SCHEDULER:-slurm} in
        slurm) sbatch --test-only --comment=project=model-audit "${SCHEDULER_WORDS[@]}" ;;
        pbs)
            # PBS has no test submission; the words are checked here and printed for the desk.
            pbs_word_check || return 1
            say "PBS request: qsub -v HPC_PROJECT=model-audit,$SCHEDULER_VARS ${SCHEDULER_WORDS[*]}"
            ;;
    esac
}
