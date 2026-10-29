# test_owner_tag.py -- Every census job shows its owner on the desk.
# Created by Sean Egan 2026-10-15
# Modified: SDE 2026-10-29  the sweep job, and the PBS form of the tag.
"""The desk reads a job's owner from its comment tag first, then the card, then the name.

Each sbatch call in the round 2 kit must carry --comment=project=model-audit, each qsub call
HPC_PROJECT=model-audit, and every job it submits must keep a name beginning model-audit-.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
ROUND = ROOT / 'hpc/rounds/2'
TAG = '--comment=project=model-audit'


def calls(tool='sbatch'):
    """Lines that run the tool, leaving the #SBATCH headers and comments aside."""
    for path in sorted(ROUND.rglob('*')):
        if path.suffix not in ('.sh', '.py') or '__pycache__' in path.parts:
            continue
        for number, line in enumerate(path.read_text().splitlines(), 1):
            code = line.split('#', 1)[0] if path.suffix == '.sh' else line
            if re.search(r'(^|[\s(\'"$])' + tool + r'\b', code):
                yield path, number, code


class OwnerTagTests(unittest.TestCase):
    def test_every_sbatch_call_carries_the_owner_tag(self):
        found = list(calls())
        self.assertGreaterEqual(len(found), 2)
        for path, number, code in found:
            self.assertIn(TAG, code, '{}:{}'.format(path.relative_to(ROOT), number))
            for name in re.findall(r'--job-name[= ](\S+)', code):
                self.assertTrue(name.strip('\'"').startswith('model-audit-'), name)

    def test_every_qsub_call_carries_the_owner_variable(self):
        found = list(calls('qsub'))
        self.assertGreaterEqual(len(found), 1)
        for path, number, code in found:
            self.assertIn('HPC_PROJECT=model-audit,', code, '{}:{}'.format(path.relative_to(ROOT), number))

    def test_every_submitted_job_keeps_the_name_prefix(self):
        submit = (ROUND / '40-submit.sh').read_text()
        pieces = set(re.findall(r'submit_job (\w+)', submit))
        self.assertEqual(pieces, {'download', 'project', 'sweep'})
        for piece in pieces:
            text = (ROUND / 'jobs' / (piece + '.sh')).read_text()
            names = re.findall(r'^#SBATCH --job-name=(\S+)$', text, re.M)
            self.assertEqual(len(names), 1, piece)
            self.assertTrue(names[0].startswith('model-audit-'), names[0])


if __name__ == '__main__':
    unittest.main()
