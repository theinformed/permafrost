# test_candidates.py -- Check the candidate scan against a small inventory and a stubbed hub.
# Created by SDE 2026-11-02
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'hpc'))
from huggingface_hub.utils import RepositoryNotFoundError
from candidates import prune_missing, scan, write_tsv


def entry(copy, parent='google/gemma-4-12B', relation='finetune', files=None, tags=(), downloads=0, card=None):
    row = {'id': copy, 'files': files if files is not None else [{'name': 'model.safetensors', 'size': 2_000_000_000, 'format': 'safetensors'}],
           'base_models': [{'id': parent, 'relation': relation}] if parent else [],
           'card_data': {'base_model': card} if card else {}, 'tags': list(tags), 'downloads_30d': downloads}
    return row


class ScanTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.dir = Path(self.folder.name)
        self.banned = self.dir / 'banned.txt'
        self.banned.write_text('# comment\nqwen\n')

    def scan(self, rows, used=(), second_generation=False):
        inventory = self.dir / 'inventory.jsonl'
        inventory.write_text(''.join(json.dumps(row) + '\n' for row in rows))
        return scan(inventory, self.banned, used=used, second_generation=second_generation)

    def test_safetensors_only(self):
        rows = self.scan([entry('owner/gguf-free', files=[{'name': 'model.bin', 'size': 1, 'format': 'pytorch'}]),
                          entry('owner/weights', files=[{'name': 'model.safetensors', 'size': 3_000_000_000, 'format': None}])])
        self.assertEqual([r['copy'] for r in rows], ['owner/weights'])
        self.assertEqual(rows[0]['size_gb'], 3.0)

    def test_quantised_only_parent_dropped(self):
        rows = self.scan([entry('owner/quant', relation='quantized'), entry('owner/fine', relation='finetune')])
        self.assertEqual([r['copy'] for r in rows], ['owner/fine'])

    def test_banned_name_dropped(self):
        rows = self.scan([entry('owner/copy', parent='Qwen/Qwen3-8B'), entry('owner/ok', tags=['qwen-distill']),
                          entry('owner/kept')])
        self.assertEqual([r['copy'] for r in rows], ['owner/kept'])

    def test_used_dropped(self):
        rows = self.scan([entry('owner/one'), entry('owner/two')], used=['owner/one'])
        self.assertEqual([r['copy'] for r in rows], ['owner/two'])

    def test_name_filters_dropped(self):
        rows = self.scan([entry('owner/x-GGUF'), entry('owner/x-mlx'), entry('owner/x-vl-4b'), entry('owner/x-awq'),
                          entry('owner/x-gptq'), entry('owner/x-nvfp4'), entry('owner/x-fp8'), entry('owner/x-int4'),
                          entry('owner/x-int8'), entry('owner/x-exl2'), entry('owner/plain')])
        self.assertEqual([r['copy'] for r in rows], ['owner/plain'])

    def test_no_parent_dropped(self):
        rows = self.scan([entry('owner/orphan', parent=None)])
        self.assertEqual(rows, [])

    def test_second_generation_drops_google_parents(self):
        rows = [entry('owner/community', parent='someone/gemma-4-12B'), entry('owner/google', parent='google/gemma-4-12B')]
        self.assertEqual([r['copy'] for r in self.scan(rows)], ['owner/community', 'owner/google'])
        self.assertEqual([r['copy'] for r in self.scan(rows, second_generation=True)], ['owner/community'])

    def test_sort_order(self):
        rows = self.scan([entry('owner/mistral-low', parent='mistralai/Mistral-7B', downloads=5),
                          entry('owner/gemma-low', downloads=1), entry('owner/mistral-high', parent='mistralai/Mistral-7B', downloads=50),
                          entry('owner/gemma-high', downloads=9)])
        self.assertEqual([r['copy'] for r in rows], ['owner/gemma-high', 'owner/gemma-low', 'owner/mistral-high', 'owner/mistral-low'])

    def test_parents_count(self):
        row = entry('owner/merged')
        row['base_models'] = [{'id': 'google/gemma-4-12B', 'relation': 'finetune'},
                              {'id': 'someone/gemma-4-12B', 'relation': 'merge'},
                              {'id': 'someone/quant', 'relation': 'quantized'}]
        rows = self.scan([row])
        self.assertEqual(rows[0]['parents'], 2)
        self.assertEqual(rows[0]['parent'], 'google/gemma-4-12B')


class PruneTests(unittest.TestCase):
    def test_prune_missing(self):
        class API:
            def model_info(self, repo, **kwargs):
                if repo.endswith('gone'):
                    raise RepositoryNotFoundError('404: ' + repo, response=SimpleNamespace(status_code=404, headers={}, url=repo, request=None))
                return SimpleNamespace(id=repo)

        rows = [{'family': 'gemma', 'copy': 'owner/ok', 'parent': 'google/gemma-4-12B', 'size_gb': 1.0, 'downloads': 1, 'parents': 1},
                {'family': 'gemma', 'copy': 'owner/gone', 'parent': 'google/gemma-4-12B', 'size_gb': 1.0, 'downloads': 1, 'parents': 1},
                {'family': 'gemma', 'copy': 'owner/ok2', 'parent': 'owner/gone', 'size_gb': 1.0, 'downloads': 1, 'parents': 1}]
        kept, missing = prune_missing(rows, API())
        self.assertEqual([r['copy'] for r in kept], ['owner/ok'])
        self.assertEqual([r['copy'] for r in missing], ['owner/gone', 'owner/ok2'])
        self.assertIn('owner/gone', missing[0]['reason'])
        self.assertIn('owner/gone', missing[1]['reason'])

    def test_other_errors_propagate(self):
        class API:
            def model_info(self, repo, **kwargs):
                raise ValueError('boom')

        with self.assertRaises(ValueError):
            prune_missing([{'family': 'gemma', 'copy': 'owner/ok', 'parent': 'google/gemma-4-12B',
                            'size_gb': 1.0, 'downloads': 1, 'parents': 1}], API())


class WriteTests(unittest.TestCase):
    def test_column_order(self):
        rows = [{'family': 'gemma', 'copy': 'owner/copy', 'parent': 'google/gemma-4-12B', 'size_gb': 2.5,
                 'downloads': 7, 'parents': 1}]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'out.tsv'
            write_tsv(rows, path)
            self.assertEqual(path.read_text(), 'gemma\towner/copy\tgoogle/gemma-4-12B\t2.5\t7\t1\n')


if __name__ == '__main__':
    unittest.main()
