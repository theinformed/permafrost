# test_resave.py -- Check re-save explanations against the token and template content.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  cover moved declarations, template text and saved versions.
import copy
import hashlib
import json
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path
from unittest.mock import patch

from audit.compare import RESAVE, compare_documents, resave_template
from audit.metadata import card_text, collect, metadata_diff, verdict


def documents():
    """A tiny vocabulary leaves no room for an ID change to hide."""
    token = {"content": "<end>", "id": 1, "special": True, "lstrip": False,
             "rstrip": False, "single_word": False, "normalized": False}
    return {"config.json": {"vocab_size": 2, "eos_token_id": 1, "transformers_version": "1.0"},
            "generation_config.json": {"temperature": 1, "transformers_version": "1.0"},
            "tokenizer.json": {"model": {"vocab": {"word": 0, "<end>": 1}},
                               "added_tokens": [token]},
            "tokenizer_config.json": {"eos_token": "<end>", "pad_token": "<end>",
                                      "additional_special_tokens": ["<end>"],
                                      "added_tokens_decoder": {"1": {k: v for k, v in token.items() if k != "id"}},
                                      "chat_template": "{{ messages[0].content }}{{ eos_token }}\n"}}


def saved_again():
    """Repeat token declarations and put the same template in a separate file."""
    result = documents()
    result["special_tokens_map.json"] = {"eos_token": {"content": "<end>", "lstrip": False,
                                                    "rstrip": False, "single_word": False, "normalized": False},
                                         "pad_token": "<end>", "additional_special_tokens": ["<end>"]}
    result["added_tokens.json"] = {"<end>": 1}
    result["chat_template.jinja"] = result["tokenizer_config.json"].pop("chat_template").replace("\n", "\r\n")
    result["config.json"]["transformers_version"] = "2.0"
    result["generation_config.json"]["transformers_version"] = "2.0"
    return result


def changes(modified, original=None):
    """Index differences by field so each assertion names what it checks."""
    differences, missing, rendered = compare_documents(modified, original or documents())
    return {d["path"]: d for d in differences}, missing, rendered


class ResaveTests(unittest.TestCase):
    """A file moving is evidence only when its content has a counterpart."""

    def test_all_three_rules(self):
        found, missing, _ = changes(saved_again())
        self.assertEqual(len(found), 8)
        self.assertEqual(missing, [])
        self.assertEqual({d["class"] for d in found.values()}, {RESAVE})
        self.assertEqual(verdict(list(found.values()), missing), "consistent with re-save noted")
        for change in found.values():
            self.assertTrue(change["files"]["original"])
            self.assertTrue(change["files"]["modified"])

    def test_special_token_id_differs(self):
        modified = saved_again()
        modified["added_tokens.json"]["<end>"] = 7
        found, _, _ = changes(modified)
        for path in ("special_tokens.special_tokens_map.json:eos_token", "added_tokens.file"):
            self.assertEqual(found[path]["class"], "unexplained")

    def test_conflicting_decoder_id_is_not_merged_away(self):
        modified = saved_again()
        modified["tokenizer_config.json"]["added_tokens_decoder"]["7"] = modified["tokenizer_config.json"]["added_tokens_decoder"].pop("1")
        found, _, _ = changes(modified)
        self.assertEqual(found["added_tokens.file"]["class"], "unexplained")
        self.assertEqual(found["special_tokens.special_tokens_map.json:eos_token"]["class"], "unexplained")

    def test_changed_string_stays_unexplained(self):
        modified = saved_again()
        modified["special_tokens_map.json"]["eos_token"]["content"] = "word"
        found, _, _ = changes(modified)
        self.assertEqual(found["special_tokens.special_tokens_map.json:eos_token"]["class"], "unexplained")

    def test_changed_token_flag_stays_unexplained(self):
        modified = saved_again()
        modified["special_tokens_map.json"]["eos_token"]["lstrip"] = True
        found, _, _ = changes(modified)
        self.assertEqual(found["special_tokens.special_tokens_map.json:eos_token"]["class"], "unexplained")

    def test_new_added_token_stays_unexplained(self):
        modified = saved_again()
        modified["added_tokens.json"]["new"] = 2
        found, _, _ = changes(modified)
        self.assertEqual(found["added_tokens.file"]["class"], "unexplained")

    def test_special_role_from_config_id_and_tokenizer_text(self):
        original = documents()
        del original["tokenizer_config.json"]["eos_token"]
        modified = copy.deepcopy(original)
        modified["special_tokens_map.json"] = {"eos_token": "<end>"}
        found, _, _ = changes(modified, original)
        change = found["special_tokens.special_tokens_map.json:eos_token"]
        self.assertEqual(change["class"], RESAVE)
        self.assertEqual(change["files"]["original"], ["config.json", "tokenizer.json"])

    def test_special_role_without_counterpart_stays_unexplained(self):
        modified = documents()
        modified["special_tokens_map.json"] = {"unk_token": "<end>"}
        found, _, _ = changes(modified)
        self.assertEqual(found["special_tokens.special_tokens_map.json:unk_token"]["class"], "unexplained")

    def test_missing_token_ids_stay_unexplained(self):
        original = documents()
        del original["tokenizer.json"]
        del original["tokenizer_config.json"]["added_tokens_decoder"]
        modified = copy.deepcopy(original)
        modified["special_tokens_map.json"] = {"eos_token": "<end>"}
        found, missing, _ = changes(modified, original)
        self.assertEqual(found["special_tokens.special_tokens_map.json:eos_token"]["class"], "unexplained")
        self.assertTrue(any("unresolved" in item for item in missing))

    def test_reordered_special_tokens_stay_unexplained(self):
        original = documents()
        original["tokenizer_config.json"]["additional_special_tokens"] = ["word", "<end>"]
        modified = copy.deepcopy(original)
        modified["special_tokens_map.json"] = {"additional_special_tokens": ["<end>", "word"]}
        found, _, _ = changes(modified, original)
        self.assertEqual(found["special_tokens.special_tokens_map.json:additional_special_tokens"]["class"], "unexplained")

    def test_version_strings_alone(self):
        modified = documents()
        modified["config.json"]["transformers_version"] = "2.0"
        modified["generation_config.json"]["transformers_version"] = "2.0"
        found, missing, _ = changes(modified)
        self.assertEqual({d["class"] for d in found.values()}, {RESAVE})
        self.assertEqual(verdict(list(found.values()), missing), "consistent with re-save noted")

    def test_role_moved_out_of_config(self):
        modified = saved_again()
        del modified["tokenizer_config.json"]["eos_token"]
        found, missing, rendered = changes(modified)
        self.assertEqual(found["special_tokens.tokenizer_config.json:eos_token"]["class"], RESAVE)
        self.assertEqual(found["special_tokens.special_tokens_map.json:eos_token"]["class"], RESAVE)
        self.assertEqual(rendered["default"]["original"], rendered["default"]["modified"])
        self.assertEqual(missing, [])

    def test_reverse_relocation(self):
        found, missing, _ = changes(documents(), saved_again())
        self.assertEqual({d["class"] for d in found.values()}, {RESAVE})
        self.assertEqual(missing, [])

    def test_changed_render_stays_unexplained(self):
        modified = saved_again()
        modified["chat_template.jinja"] += "different"
        found, _, rendered = changes(modified)
        self.assertNotEqual(rendered["default"]["original"], rendered["default"]["modified"])
        self.assertEqual(found["template.default"]["class"], "unexplained")
        self.assertEqual(found["template_source.tokenizer_config"]["class"], "unexplained")
        self.assertEqual(verdict(list(found.values()), []), "unexplained differences")

    def test_trailing_whitespace_with_equal_render(self):
        original = documents()
        original["tokenizer_config.json"]["chat_template"] = "{{- messages[0].content -}}\n"
        modified = copy.deepcopy(original)
        modified["chat_template.jinja"] = modified["tokenizer_config.json"].pop("chat_template") + " \t\r\n"
        found, _, _ = changes(modified, original)
        self.assertEqual(found["template.default"]["class"], RESAVE)

    def test_normalized_source_with_changed_render_stays_unexplained(self):
        original = documents()
        original["tokenizer_config.json"]["chat_template"] = "hello\n"
        modified = copy.deepcopy(original)
        modified["chat_template.jinja"] = modified["tokenizer_config.json"].pop("chat_template").replace("hello", "hello  ")
        found, _, rendered = changes(modified, original)
        self.assertEqual(resave_template("hello\n"), resave_template("hello  \n"))
        self.assertNotEqual(rendered["default"]["original"], rendered["default"]["modified"])
        self.assertEqual(found["template.default"]["class"], "unexplained")

    def test_equal_render_with_changed_branch_stays_unexplained(self):
        original = documents()
        original["tokenizer_config.json"]["chat_template"] = "{{ messages[0].content }}{{ eos_token }}"
        modified = copy.deepcopy(original)
        modified["chat_template.jinja"] = modified["tokenizer_config.json"].pop("chat_template") + "{% if tools %}changed{% endif %}"
        found, _, rendered = changes(modified, original)
        self.assertEqual(rendered["default"]["original"], rendered["default"]["modified"])
        self.assertEqual(found["template.default"]["class"], "unexplained")

    def test_render_failure_does_not_explain_relocation(self):
        with patch("audit.compare.render", side_effect=ValueError("bad template")):
            found, missing, _ = changes(saved_again())
        self.assertTrue(missing)
        self.assertEqual(found["template_source.tokenizer_config"]["class"], "unexplained")

    def test_other_version_fields_and_values_stay_unexplained(self):
        modified = documents()
        modified["config.json"].update(transformers_version={"bad": "value"}, hidden_size=3)
        modified["config.json"]["nested"] = {"transformers_version": "2.0"}
        modified["generation_config.json"]["temperature"] = 2
        found, _, _ = changes(modified)
        self.assertEqual({d["class"] for d in found.values()}, {"unexplained"})

    def test_missing_and_expected_verdicts(self):
        self.assertEqual(verdict([], []), "consistent")
        self.assertEqual(verdict([{"class": "expected"}], []), "consistent")
        self.assertEqual(verdict([{"class": RESAVE}], ["missing"]), "undecided")
        self.assertEqual(verdict([{"class": "unknown"}], []), "unexplained differences")

    def test_card_has_one_heading_per_resave_item(self):
        found, _, rendered = changes(saved_again())
        report = {"modified": {"repo": "a/changed", "sha": "m"},
                  "original": {"repo": "a/base", "sha": "o"}, "verdict": "consistent with re-save noted",
                  "differences": list(found.values()), "missing": [], "rendered": rendered}
        card = card_text(report)
        self.assertEqual(card.count("## Explained by re-save:"), 8)
        self.assertEqual(card.count("Original file:"), 8)
        self.assertEqual(card.count("Modified file:"), 8)
        self.assertIn("`tokenizer_config.json`", card)
        self.assertIn("`chat_template.jinja`", card)


class PinnedEvidenceTests(unittest.TestCase):
    """Pinned reruns read the saved files without asking for a newer revision."""

    def test_cache_needs_no_network_and_checks_hashes(self):
        with tempfile.TemporaryDirectory() as directory:
            raw = b'{"vocab_size": 2}'
            from audit.hub import safe_name
            local = Path(directory) / safe_name("a/base") / ("a" * 40) / "config.json"
            local.parent.mkdir(parents=True)
            local.write_bytes(raw)
            evidence = {"sha": "a" * 40, "manifest": {"config.json": {
                "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}},
                "gguf_only": False, "gguf_header": None}
            with patch("audit.metadata.Hub") as factory:
                hub = factory.return_value
                result = collect(hub, "a/base", directory, evidence)
                self.assertEqual(result["documents"]["config.json"], {"vocab_size": 2})
                hub.info.assert_not_called()
                hub.small_file.assert_not_called()
                local.write_bytes(b'{"vocab_size": 3}')
                result = collect(hub, "a/base", directory, evidence)
                self.assertTrue(any("checksum" in item for item in result["missing"]))

    def test_wrong_pair_is_rejected_before_collection(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "pair.json"
            path.write_text(json.dumps({"modified": {"repo": "a/changed"}, "original": {"repo": "a/base"}}))
            args = Namespace(delay=0, from_evidence=str(path), repo="a/other", original="a/base")
            with patch("audit.metadata.Hub"), patch("audit.metadata.collect") as collector:
                with self.assertRaisesRegex(ValueError, "repository pair"):
                    metadata_diff(args)
                collector.assert_not_called()


if __name__ == "__main__":
    unittest.main()
