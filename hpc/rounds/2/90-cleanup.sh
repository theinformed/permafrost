#!/bin/bash
# 90-cleanup.sh -- Clear approved derived weights after archive read-back.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-14  keep archive cleanup confined to the census round.
# Modified: SDE 2026-10-13  refuse cleanup until exact paths are approved.
. ./env.sh
start_piece cleanup 'Clear archived derived checkpoint files'
python3 ./cleanup.py --ruling "${AUDIT_CLEANUP_RULING:?name the controller ruling}" --receipt "${AUDIT_ARCHIVE_RECEIPT:?name the archive read-back receipt}"
echo 'VERDICT cleanup OK'
