# single_projection_selected.py -- Build the single-projection-selected reference copy.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  add the method's command-line entry point.
"""Run this reference method with the shared memory and provenance checks."""

from .runner import main

if __name__ == "__main__":
    raise SystemExit(main("single-projection-selected"))
