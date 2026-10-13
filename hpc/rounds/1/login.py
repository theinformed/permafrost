# login.py -- Print the interpreter used for login-node checks.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  require only the standard library on login nodes.
import sys
print('login Python: ' + sys.version.split()[0])
if sys.version_info < (3, 6):
    raise SystemExit('login checks need Python 3.6 or newer')
