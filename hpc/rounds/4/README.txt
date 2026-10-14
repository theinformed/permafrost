# README.txt -- Run and rehearse the recipe fingerprint calibration.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  describe the ten calibration rehearsal cases.
Round 4 applies one published recipe and measures its fingerprint on one base.
It reads round 1's verified original, download record and wheels without changing them.
The default recipe is norm-preserving; single-projection is the control.
Run: /p/work1/sdegan/model-audit-calibrate.sh 4
Rehearse locally with a reporting kit:
.venv/bin/python hpc/rehearse_calibration.py .tmp/hpc/calibration-rehearsal --dry-run --kit <kit-folder>
Add --suite to check the ten observed outcomes. Nothing is sent to a cluster.
