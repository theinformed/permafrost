# wheels.py -- Check every pinned package in the shared wheel directory.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  refuse missing pins before submitting calibration.
import os
from pathlib import Path
import re
import sys


def canonical(name):
    """Treat punctuation and case as equivalent in package names."""
    return re.sub(r'[-_.]+', '-', name).lower()


def pins(requirements):
    """Read exact package versions, ignoring blank lines and comments."""
    return [tuple(line.strip().split('==')) for line in requirements.read_text().splitlines()
            if line.strip() and not line.lstrip().startswith('#')]


def check(requirements, directory):
    """Name each missing wheel and return a failing status for any gap."""
    required = pins(requirements)
    found = set()
    if directory.is_dir():
        for path in directory.iterdir():
            fields = path.name.split('-')
            if path.is_file() and path.suffix == '.whl' and len(fields) >= 5:
                found.add((canonical(fields[0]), fields[1]))
    missing = [(name, version) for name, version in required
               if (canonical(name), version) not in found]
    for name, version in missing:
        print('wheel missing: {}=={}'.format(name, version))
    if missing:
        return 1
    print('wheelhouse: {} pins found in {}'.format(len(required), directory))
    return 0


if __name__ == '__main__':
    sys.exit(check(Path('compute-requirements.txt'), Path(os.environ['AUDIT_WHEELS'])))
