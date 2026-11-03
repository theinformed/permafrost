# test_pin_unpublished.py -- A party whose published file list holds no safetensors weights is refused at pin time.
# Created by SDE
from datetime import datetime, timezone
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'hpc'))
import pin_census
from pin_census import pin

CREATED = datetime(2026, 1, 2, tzinfo=timezone.utc)
SHA = 'e' * 64


def api(original_files):
    """A hub whose copy has one safetensors file and whose original publishes the given file names."""
    copy_files = [SimpleNamespace(rfilename='model.safetensors', lfs=SimpleNamespace(sha256=SHA, size=1, pointer_size=1)),
                  SimpleNamespace(rfilename='config.json', lfs=None)]
    base_files = [SimpleNamespace(rfilename=name, lfs=None) for name in original_files]
    history = [SimpleNamespace(commit_id='a' * 40, created_at=datetime(2026, 1, 1, tzinfo=timezone.utc), title='Upload')]

    class API:
        def model_info(self, repo, revision=None, **kwargs):
            card = {'base_model': 'publisher/base'} if repo == 'owner/copy' else {}
            return SimpleNamespace(sha=revision or 'c' * 40, created_at=CREATED,
                                   siblings=copy_files if repo == 'owner/copy' else base_files,
                                   card_data=SimpleNamespace(to_dict=lambda: card))

        def list_repo_commits(self, repo):
            if repo == 'owner/copy':
                return [SimpleNamespace(commit_id='c' * 40, created_at=CREATED, title='Upload')]
            return history
    return API()


class UnpublishedWeightsTests(unittest.TestCase):
    def test_an_original_with_only_gguf_files_is_refused_naming_it(self):
        with self.assertRaisesRegex(pin_census.Unpublished, 'publishes no safetensors weights: publisher/base'):
            pin(api(['README.md', 'config.json', 'model-Q4_K_M.gguf']), 'owner/copy', 'publisher/base')

    def test_unpublished_is_a_value_error(self):
        self.assertTrue(issubclass(pin_census.Unpublished, ValueError))

    def test_an_original_with_a_safetensors_file_is_pinned(self):
        row = pin(api(['README.md', 'config.json', 'model.safetensors']), 'owner/copy', 'publisher/base')
        self.assertEqual(row['original']['hub_id'], 'publisher/base')

    def test_an_original_with_only_consolidated_files_is_refused(self):
        with self.assertRaisesRegex(pin_census.Unpublished, 'publisher/base'):
            pin(api(['README.md', 'consolidated.safetensors']), 'owner/copy', 'publisher/base')

    def test_an_empty_file_list_is_not_judged(self):
        row = pin(api([]), 'owner/copy', 'publisher/base')
        self.assertEqual(row['original']['hub_id'], 'publisher/base')


if __name__ == '__main__':
    unittest.main()
