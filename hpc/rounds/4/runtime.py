# runtime.py -- Check the compute interpreter before creating its environment.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  check the compute interpreter before calibration.
import sys
if not (3, 9) <= sys.version_info[:2] <= (3, 13):
    raise SystemExit('the pinned runtime needs Python 3.9 through 3.13')
print('compute Python: ' + sys.version.split()[0])
