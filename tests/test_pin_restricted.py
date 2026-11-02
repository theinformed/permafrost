# test_pin_restricted.py -- A hub id that carries a restricted maker's model name is refused before any hub call.
# Created by SDE
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from hpc import pin_census

GATE_TEXT = '''
BANNED = (
    r"deepseek", r"qwen", r"chatglm", r"glm-?\\d+",
    r"ernie(?:-bot|[- ]\\d+)",
)
'''


class NoHub:
    def model_info(self, *args, **kwargs):
        raise AssertionError('the hub must not be called for a restricted name')

    def list_repo_commits(self, *args, **kwargs):
        raise AssertionError('the hub must not be called for a restricted name')


class RestrictedNameTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.gate = os.path.join(self.folder.name, 'banned.py')
        with open(self.gate, 'w') as handle:
            handle.write(GATE_TEXT)

    def test_patterns_come_from_the_gate_file(self):
        patterns = pin_census.restricted_patterns(self.gate)
        self.assertEqual(len(patterns), 5)
        self.assertTrue(any(p.search('glm-4') for p in patterns))

    def test_a_restricted_model_name_inside_a_repository_name_is_found(self):
        patterns = pin_census.restricted_patterns(self.gate)
        self.assertEqual(pin_census.restricted_name('owner/Gemma-3-1B-it-GLM-4.7-Flash-Heretic', patterns), 'glm-4')
        self.assertEqual(pin_census.restricted_name('owner/qwen2.5-abliterated', patterns), 'qwen')
        self.assertIsNone(pin_census.restricted_name('owner/gemma-4-E4B-heretic', patterns))
        self.assertIsNone(pin_census.restricted_name('owner/Modern-Heretic', patterns))

    def test_a_missing_gate_file_falls_back_to_the_maker_list(self):
        patterns = pin_census.restricted_patterns(os.path.join(self.folder.name, 'absent.py'))
        self.assertEqual(pin_census.restricted_name('owner/Qwen3-8B-abliterated', patterns), 'qwen')
        self.assertIsNone(pin_census.restricted_name('owner/gemma-4-E4B-heretic', patterns))

    def test_pin_refuses_a_restricted_copy_before_any_hub_call(self):
        patterns = pin_census.restricted_patterns(self.gate)
        pin_census.RESTRICTED = patterns
        with self.assertRaises(pin_census.Restricted) as caught:
            pin_census.pin(NoHub(), 'owner/Gemma-3-1B-it-GLM-4.7-Flash-Heretic', 'owner/gemma-3-1b-it')
        self.assertIn("restricted model name 'glm-4'", str(caught.exception))
        with self.assertRaises(pin_census.Restricted):
            pin_census.pin(NoHub(), 'owner/clean-copy', 'owner/DeepSeek-R1-Distill')

    def test_restricted_is_a_value_error(self):
        self.assertTrue(issubclass(pin_census.Restricted, ValueError))


if __name__ == '__main__':
    unittest.main()
