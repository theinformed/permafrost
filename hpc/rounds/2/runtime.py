# runtime.py -- Check the compute interpreter before creating its environment.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-14  keep the compute interpreter check on the CPU lane.
# Modified: SDE 2026-10-13  separate compute requirements from login checks.
import sys
if not (3, 9) <= sys.version_info[:2] <= (3, 13):
    raise SystemExit('the pinned runtime needs Python 3.9 through 3.13')
print('compute Python: ' + sys.version.split()[0])
