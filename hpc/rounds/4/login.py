# login.py -- Print the interpreter used for login-node checks.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  check the login interpreter before calibration.
import sys
print('login Python: ' + sys.version.split()[0])
if sys.version_info < (3, 6):
    raise SystemExit('login checks need Python 3.6 or newer')
