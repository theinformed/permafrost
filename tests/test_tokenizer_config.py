# test_tokenizer_config.py -- Check text configuration selection without weights.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  cover nested, plain and older configurations.
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from audit.recipes.common import load_runtime
from hpc.project import load_tokenizer


class TokenizerConfigTests(unittest.TestCase):
    """A tokenizer should follow the text decoder, even inside a vision wrapper."""

    def check_loaders(self, config, expected):
        """Keep both callers offline and check the exact object they pass."""
        directory = Path('/unused/checkpoint')
        for loader in ('projection', 'recipe'):
            with self.subTest(loader=loader):
                tokenizer = SimpleNamespace(pad_token_id=0)
                resources = SimpleNamespace(check=Mock(), device=SimpleNamespace(type='cpu'))
                with patch('transformers.AutoConfig.from_pretrained', return_value=config) as config_load, \
                     patch('transformers.AutoTokenizer.from_pretrained', return_value=tokenizer) as token_load, \
                     patch('transformers.AutoModelForCausalLM.from_pretrained') as model_load:
                    if loader == 'projection':
                        result = load_tokenizer(directory)
                        source = str(directory)
                        model_load.assert_not_called()
                    else:
                        _, result = load_runtime(directory, resources)
                        source = directory
                        resources.check.assert_called_once_with()
                    self.assertIs(result, tokenizer)
                    config_load.assert_called_once_with(source, local_files_only=True, trust_remote_code=False)
                    token_load.assert_called_once_with(source, config=expected,
                                                       local_files_only=True, trust_remote_code=False)
                    self.assertIs(token_load.call_args.kwargs['config'], expected)

    def test_nested_text_config(self):
        text_config = object()
        config = SimpleNamespace(model_type='mistral3', get_text_config=lambda: text_config)
        self.assertIsNot(config, text_config)
        self.check_loaders(config, text_config)

    def test_plain_text_config(self):
        config = SimpleNamespace(model_type='plain')
        config.get_text_config = lambda: config
        self.check_loaders(config, config)

    def test_older_config_without_accessor(self):
        config = SimpleNamespace(model_type='plain')
        self.check_loaders(config, config)

    def test_projection_reuses_loaded_config(self):
        text_config = object()
        config = SimpleNamespace(get_text_config=lambda: text_config)
        with patch('transformers.AutoConfig.from_pretrained') as config_load, \
             patch('transformers.AutoTokenizer.from_pretrained') as token_load:
            self.assertIs(load_tokenizer(Path('/unused/checkpoint'), config), token_load.return_value)
            config_load.assert_not_called()
            self.assertIs(token_load.call_args.kwargs['config'], text_config)


if __name__ == '__main__':
    unittest.main()
