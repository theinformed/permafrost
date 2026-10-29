# test_print_width.py -- No line the census kit prints runs past 100 columns.
# Created by Sean Egan 2026-10-15
"""A 225-character fallback line pushed the desk page off screen on 2026-10-14.

Every literal the round 2 scripts print is checked here, and the fold helpers are run on a
225-character sample of that very line: what happened first, where the file waits next, why
and the error text on their own lines. Parsed lines (VERDICT, job ids) are short already.
"""
import ast
from pathlib import Path
import re
import os
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
ROUND = ROOT / 'hpc/rounds/2'
KITS = (Path('/root/work/hpc-kit-wt/hpc-report.sh'), Path('/opt/ai/hpc-packages/tools/hpc/hpc-report.sh'))


def readable(path):
    """A file under another account's home reads as absent, not as an error."""
    try:
        return path.is_file() and os.access(path, os.R_OK)
    except PermissionError:
        return False
WIDTH = 100
WHAT = 'hpc send: no way out from here'
WHERE = 'round-2-kit-20261015T031500-4113-drop.txt waits in /p/home/sdegan/.hpc/outbox/model-audit/nautilus'
WHY = 'for the next poll'
ERROR = 'HTTP 000: curl: (28) Operation timed out after 15001 milliseconds with 0 out of 0 bytes received'
SAMPLE = '{} ({}); {} {}'.format(WHAT, ERROR, WHERE, WHY)
PRINTERS = {'print', 'fold', 'ValueError', 'SystemExit', 'RuntimeError', 'MemoryError', 'exit'}


def scripts():
    """Every file the census bundle carries that can print, plus the shared opener and screen."""
    files = [path for path in ROUND.rglob('*') if path.suffix in ('.sh', '.py') and '__pycache__' not in path.parts]
    return sorted(files) + [ROOT / 'hpc/opener.sh', ROOT / 'hpc/lineage.py']


def python_literals(path):
    """String constants handed to print, an exception or the fold helper."""
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.Call):
            name = getattr(node.func, 'id', getattr(node.func, 'attr', ''))
            if name in PRINTERS:
                for argument in node.args:
                    for part in ast.walk(argument):
                        if isinstance(part, ast.Constant) and isinstance(part.value, str):
                            yield node.lineno, part.value


def shell_literals(path):
    """Quoted text on echo, printf and say lines."""
    for number, line in enumerate(path.read_text().splitlines(), 1):
        if re.search(r'\b(echo|printf|say)\b', line):
            for single, double in re.findall(r"'([^']*)'|\"((?:[^\"\\\\]|\\\\.)*)\"", line):
                yield number, single or double


class PrintWidthTests(unittest.TestCase):
    def test_no_printed_literal_runs_past_100_columns(self):
        long = []
        for path in scripts():
            found = python_literals(path) if path.suffix == '.py' else shell_literals(path)
            for number, text in found:
                for line in text.split('\n'):
                    if len(line) > WIDTH:
                        long.append('{}:{} ({} chars)'.format(path.relative_to(ROOT), number, len(line)))
        self.assertEqual(long, [])

    def test_python_fold_keeps_order_and_width(self):
        self.assertGreaterEqual(len(SAMPLE), 225)
        sys.path.insert(0, str(ROUND))
        from say import fold
        text = fold(WHAT, WHERE, WHY, ERROR)
        lines = text.splitlines()
        self.assertTrue(all(len(line) <= WIDTH for line in lines), text)
        self.assertEqual(lines[0], WHAT)
        self.assertLess(text.index('outbox'), text.index(WHY))
        self.assertLess(text.index(WHY), text.index('curl: (28)'))
        # Nothing is lost in the folding.
        self.assertEqual(''.join(text.split()), ''.join((WHAT + WHERE + WHY + ERROR).split()))

    def bash(self, function, call):
        source = (ROUND / 'env.sh').read_text()
        body = re.search(r'^' + function + r'\(\) \{\n.*?^\}\n', source, re.S | re.M).group(0)
        return subprocess.run(['bash', '-c', body + call], stdout=subprocess.PIPE, universal_newlines=True,
                              check=True).stdout

    def test_shell_say_and_narrow_fold_the_sample(self):
        out = self.bash('say', 'say {} {} {}\n'.format(*(repr(part) for part in (WHAT, WHERE, ERROR))))
        lines = out.splitlines()
        self.assertEqual(lines[0], WHAT)
        self.assertTrue(all(len(line) <= WIDTH for line in lines), out)
        self.assertTrue(lines[-1].startswith('  '))
        wrapped = self.bash('narrow', 'printf "%s\\n" {} | narrow\n'.format(repr(SAMPLE)))
        self.assertTrue(all(len(line) <= WIDTH for line in wrapped.splitlines()), wrapped)
        self.assertEqual(wrapped.replace('\n', ''), SAMPLE)
        # A parsed line of exactly 100 columns passes through untouched.
        exact = 'This build already submitted a job: ' + 'a' * 64
        self.assertEqual(self.bash('narrow', 'printf "%s\\n" {} | narrow\n'.format(repr(exact))), exact + '\n')

    def test_bundled_kit_folds_its_fallback_line(self):
        kit = next((path for path in KITS if readable(path)), None)
        if kit is None:
            self.skipTest('the shared kit is not on this machine')
        source = kit.read_text()
        match = re.search(r'^_hpc_say\(\) \{.*?^\}\n', source, re.S | re.M)
        if not match:
            self.fail('the bundled kit has no fold helper; its fallback line can run past 100 columns')
        out = subprocess.run(['bash', '-c', match.group(0) + '_hpc_say "$1"\n', 'say', SAMPLE],
                             stdout=subprocess.PIPE, universal_newlines=True, check=True).stdout
        self.assertTrue(all(len(line) <= WIDTH for line in out.splitlines()), out)
        self.assertGreater(len(out.splitlines()), 2)


if __name__ == '__main__':
    unittest.main()
