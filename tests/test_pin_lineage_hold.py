# test_pin_lineage_hold.py -- A pair the lineage screen would hold is refused at pin time, before it reaches a batch.
# Created by SDE
import contextlib
import io
import os
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from hpc import pin_census


def node(hub_id, declared=None, chain=(), root=False, missing=False):
    row = {'hub_id': hub_id, 'maker': hub_id.split('/')[0].lower(), 'revision': 'abc123',
           'declared_base_model': declared, 'base_model_chain': list(chain), 'created_at': None,
           'publisher_root': root, 'lineage_known': bool(chain) or root}
    if missing:
        row['missing'] = True
    return row


ORIGINAL = node('google/gemma-2-9b-it', root=True)
GOOD_COPY = node('someone/gemma-2-9b-it-abliterated', declared=['google/gemma-2-9b-it'], chain=[ORIGINAL])
HELD_LEAF = node('vanished/Gemma-2-9B-Uncensored', missing=True)
HELD_COPY = node('writer/Dirty-Writer-Uncensored', declared=['vanished/Gemma-2-9B-Uncensored'], chain=[HELD_LEAF])


class LineageHoldTests(unittest.TestCase):
    def test_a_well_formed_pair_is_not_held(self):
        self.assertIsNone(pin_census.lineage_hold({'modified': GOOD_COPY, 'original': ORIGINAL}))

    def test_an_unknown_leaf_is_named_in_the_hold(self):
        reason = pin_census.lineage_hold({'modified': HELD_COPY, 'original': ORIGINAL})
        self.assertIsNotNone(reason)
        self.assertTrue(reason.startswith('unknown base held: writer/Dirty-Writer-Uncensored'), reason)

    def test_main_refuses_a_held_pair_and_writes_no_manifest(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        manifest = os.path.join(folder.name, 'round-99-batch-1.json')
        argv = ['pin_census.py', manifest, '--pair', HELD_COPY['hub_id'], ORIGINAL['hub_id']]
        out = io.StringIO()
        with mock.patch.object(pin_census, 'HfApi', lambda: None), \
                mock.patch.object(pin_census, 'measured_copies', lambda: ()), \
                mock.patch.object(pin_census, 'pin', lambda *a, **k: {'modified': dict(HELD_COPY), 'original': dict(ORIGINAL)}), \
                mock.patch.object(sys, 'argv', argv), contextlib.redirect_stdout(out):
            with self.assertRaises(SystemExit) as stop:
                pin_census.main()
        self.assertEqual(stop.exception.code, 1)
        self.assertIn('refused writer/Dirty-Writer-Uncensored: unknown base held', out.getvalue())
        self.assertFalse(os.path.exists(manifest))


if __name__ == '__main__':
    unittest.main()
