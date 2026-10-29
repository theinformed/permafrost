# test_audit.py -- Check ancestry, template comparisons, and bounded header reads.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  cover the first two stages without network calls.
# Modified: SDE 2026-10-29  the hub module binds the client factory when a Hub is made.
import io
import json
import struct
import contextlib
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from audit.compare import classify, compare_documents, normalize_template, render, snapshot
from audit.gguf import MAX_HEADER, RangeReader, parse_header
from audit.hub import Hub, safe_name
from audit.inventory import info_row, inventory, read_rows
from audit.metadata import collect, compare_gguf, verdict
from audit.resolver import declarations, resolve


def row(name, parent=None, relation="finetune", fmt="safetensors"):
    """Keep resolver cases small enough to see the entire ancestry."""
    return {"id": name, "base_models": [{"id": parent, "relation": relation}] if parent else [],
            "files": [{"format": fmt}], "tags": []}


def documents():
    """Use a two-word vocabulary and declarations in both token files."""
    return {"config.json": {"model_type": "plain", "vocab_size": 2, "eos_token_id": 1},
            "tokenizer.json": {"model": {"vocab": {"hello": 0, "<end>": 1}}, "added_tokens": []},
            "tokenizer_config.json": {"eos_token": "<end>", "bos_token": None,
                                      "chat_template": "{% for m in messages %}{{m.content}} {{eos_token}}{% endfor %}"},
            "special_tokens_map.json": {"eos_token": "<end>"},
            "generation_config.json": {"temperature": 1}}


def header(entries, endian="<", version=3):
    """Make metadata followed by a sentinel that the parser must leave alone."""
    def string(value):
        raw = value.encode()
        return struct.pack(endian + "Q", len(raw)) + raw

    def value(kind, data):
        if kind == 8:
            return string(data)
        if kind == 9:
            item_type, items = data
            return struct.pack(endian + "IQ", item_type, len(items)) + b"".join(value(item_type, i) for i in items)
        codes = {0: "B", 1: "b", 2: "H", 3: "h", 4: "I", 5: "i", 6: "f", 7: "?", 10: "Q", 11: "q", 12: "d"}
        return struct.pack(endian + codes[kind], data)

    raw = (b"GGUF" if endian == "<" else b"FUGG") + struct.pack(endian + "IQQ", version, 1, len(entries))
    for key, kind, data in entries:
        raw += string(key) + struct.pack(endian + "I", kind) + value(kind, data)
    return raw


class TemplateTests(unittest.TestCase):
    """Whitespace screening cannot replace the rendered comparison."""

    def test_normalize(self):
        self.assertEqual(normalize_template(" a\n\t b  "), "a b")

    def test_equal(self):
        differences, missing, rendered = compare_documents(documents(), documents())
        self.assertEqual((differences, missing), ([], []))
        self.assertEqual(rendered["default"]["original"], rendered["default"]["modified"])

    def test_whitespace_still_changes_rendering(self):
        original, modified = documents(), documents()
        original["tokenizer_config.json"]["chat_template"] = " a b "
        modified["tokenizer_config.json"]["chat_template"] = " a  b "
        changes, _, _ = compare_documents(modified, original)
        self.assertTrue(next(c for c in changes if c["path"] == "template.default")["normalized_equal"])
        self.assertIn("rendered_template.default", {c["path"] for c in changes})

    def test_token_id_change(self):
        modified = documents()
        modified["tokenizer.json"]["model"]["vocab"]["<end>"] = 5
        changes, _, _ = compare_documents(modified, documents())
        changed = next(c for c in changes if c["path"].endswith("tokenizer_config.json:eos_token"))
        self.assertEqual(changed["modified"]["ids"], [5])

    def test_token_flags_and_added_tokens(self):
        modified = documents()
        modified["special_tokens_map.json"]["eos_token"] = {"content": "<end>", "lstrip": True}
        modified["tokenizer.json"]["added_tokens"] = [{"content": "new", "id": 2, "special": True}]
        changes, _, _ = compare_documents(modified, documents())
        paths = {c["path"] for c in changes}
        self.assertIn("added_tokens.tokenizer", paths)
        self.assertIn("special_tokens.special_tokens_map.json:eos_token", paths)

    def test_null_token_is_not_missing(self):
        self.assertEqual(compare_documents(documents(), documents())[1], [])

    def test_named_templates(self):
        docs = documents()
        docs["tokenizer_config.json"]["chat_template"] = [{"name": "default", "template": "x"}, {"name": "tool", "template": "y"}]
        self.assertEqual(snapshot(docs)["templates"], {"default": "x", "tool": "y"})

    def test_missing_template_and_vocabulary(self):
        modified = documents()
        del modified["tokenizer.json"]
        del modified["tokenizer_config.json"]["chat_template"]
        _, missing, _ = compare_documents(modified, documents())
        self.assertTrue(any("tokenizer.json missing" in m for m in missing))
        self.assertTrue(any("chat template missing" in m for m in missing))

    def test_tokenizer_without_vocabulary_is_undecided(self):
        docs = documents()
        del docs["tokenizer.json"]["model"]["vocab"]
        changes, missing, _ = compare_documents(docs, docs)
        self.assertEqual(verdict(changes, missing), "undecided")

    def test_optional_message_fields(self):
        self.assertEqual(render("{% if messages[0].tool_calls %}x{% endif %}ok", documents()), "ok")

    def test_template_cannot_open_python_attributes(self):
        with self.assertRaises(Exception):
            render("{{ ''.__class__.__mro__ }}", documents())

    def test_large_template_expression_is_bounded(self):
        with self.assertRaises(ValueError):
            render("{{ 'a' * 1000000000 }}", documents())

    def test_unused_config_template_still_compared(self):
        original, modified = documents(), documents()
        original["chat_template.jinja"] = modified["chat_template.jinja"] = "chosen"
        modified["tokenizer_config.json"]["chat_template"] = "different"
        changes, _, _ = compare_documents(modified, original)
        self.assertIn("template_source.tokenizer_config", {c["path"] for c in changes})


class ClassifierTests(unittest.TestCase):
    """Changing a name gets a narrow exception; token and runtime fields do not."""

    def test_table(self):
        self.assertEqual(classify("config.model_type"), "expected")
        self.assertEqual(classify("config._name_or_path"), "expected")
        for field in ("config.hidden_size", "generation.temperature", "config.eos_token_id", "template.default"):
            self.assertEqual(classify(field), "unexplained")

    def test_verdicts(self):
        self.assertEqual(verdict([], []), "consistent")
        self.assertEqual(verdict([], ["missing"]), "undecided")
        self.assertEqual(verdict([{"class": "expected"}], []), "consistent")
        self.assertEqual(verdict([{"class": "unexplained"}], ["missing"]), "unexplained differences")

    def test_nested_null_and_absent_key(self):
        modified = documents()
        modified["config.json"]["text_config"] = {"attention": None}
        original = documents()
        original["config.json"]["text_config"] = {}
        changes, _, _ = compare_documents(modified, original)
        changed = next(c for c in changes if c["path"] == "config.text_config.attention")
        self.assertFalse(changed["original_present"])
        self.assertTrue(changed["modified_present"])


class ResolverTests(unittest.TestCase):
    """Only declared parents can connect a mirror to a source."""

    def test_card_relations(self):
        result = declarations({"base_model": ["a/base"], "base_model_relation": "quantized"}, ["base_model:a/base", "base_model:quantized:a/base"])
        self.assertEqual(result, [{"id": "a/base", "relation": "quantized"}])

    def test_relation_key(self):
        self.assertEqual(declarations({"base_model:finetune": "a/base"}), [{"id": "a/base", "relation": "finetune"}])

    def test_mirror_chain(self):
        rows = [row("a/mirror", "a/source", "quantized", "gguf"), row("a/source", "a/base"), row("a/base")]
        resolve(rows)
        self.assertEqual(rows[0]["source_id"], "a/source")
        self.assertEqual(rows[0]["stated_original"], "a/base")

    def test_external_ancestry(self):
        rows = [row("a/mirror", "a/source", "quantized", "gguf")]
        resolve(rows, [row("a/source", "a/base"), row("a/base")])
        self.assertEqual(rows[0]["stated_original"], "a/base")

    def test_absent_parent(self):
        rows = [row("a/mirror", "a/missing", "quantized", "gguf")]
        resolve(rows)
        self.assertIsNone(rows[0]["source_id"])
        self.assertIsNone(rows[0]["stated_original"])

    def test_merge_and_cycle(self):
        merged = row("a/merged", "a/base")
        merged["base_models"].append({"id": "b/base", "relation": "merge"})
        rows = [merged, row("a/one", "a/two"), row("a/two", "a/one")]
        resolve(rows)
        self.assertTrue(all(r["stated_original"] is None for r in rows))

    def test_packed_weights_with_one_parent(self):
        rows = [row("a/gguf", "a/source", fmt="gguf"), row("a/source")]
        resolve(rows)
        self.assertEqual(rows[0]["role"], "mirror")

    def test_packed_weights_without_parent_do_not_guess(self):
        rows = [row("a/looks-like-base-GGUF", fmt="gguf")]
        resolve(rows)
        self.assertIsNone(rows[0]["source_id"])

    def test_packed_config_and_tags(self):
        for method in ("awq", "gptq"):
            packed = row("a/packed", "a/source")
            packed["quantization"] = method
            rows = [packed, row("a/source")]
            resolve(rows)
            self.assertEqual(rows[0]["role"], "mirror")
            packed.pop("quantization")
            packed["tags"] = ["quantized:" + method]
            resolve(rows)
            self.assertEqual(rows[0]["role"], "mirror")


class HeaderTests(unittest.TestCase):
    """Synthetic headers make it easy to spot accidental tensor reads."""

    def test_arrays_and_offset(self):
        data = header([("general.name", 8, "test"), ("tokenizer.ggml.tokens", 9, (8, ["hello", "<end>"])),
                       ("tokenizer.ggml.scores", 9, (6, [1., 2.])), ("tokenizer.ggml.eos_token_id", 4, 1),
                       ("tokenizer.chat_template", 8, "{{ messages[0].content }}")])
        stream = io.BytesIO(data + b"TENSORS")
        result = parse_header(stream)
        self.assertEqual(result["metadata"]["tokenizer.ggml.tokens"], ["hello", "<end>"])
        self.assertEqual(stream.read(), b"TENSORS")
        self.assertEqual(result["metadata_bytes"], len(data))

    def test_byte_orders_and_versions(self):
        for endian in ("<", ">"):
            for version in (2, 3):
                result = parse_header(header([("flag", 7, True), ("signed", 11, -12)], endian, version))
                self.assertEqual(result["metadata"], {"flag": True, "signed": -12})

    def test_invalid_and_truncated(self):
        for data in (b"bad!", header([], version=1), header([("x", 8, "text")])[:-1]):
            with self.assertRaises(ValueError):
                parse_header(data)

    def test_duplicate_key(self):
        with self.assertRaises(ValueError):
            parse_header(header([("x", 0, 1), ("x", 0, 2)]))

    def test_large_string(self):
        data = header([])[:-8] + struct.pack("<Q", 1) + struct.pack("<Q", MAX_HEADER + 1)
        with self.assertRaises(ValueError):
            parse_header(data)

    def test_range_reader_stops_at_metadata(self):
        data = header([("tokens", 9, (8, ["a"] * 1000)), ("tail", 7, True)])
        calls = []

        class Response:
            """Return exactly the bytes requested by the range reader."""

            status_code = 206

            def __init__(self, start, end):
                self.headers = {"Content-Range": f"bytes {start}-{end}/{len(data) + 7}"}
                self.payload = (data + b"TENSORS")[start:end + 1]

            def __enter__(self):
                return self

            def __exit__(self, *args):
                return False

            def raise_for_status(self):
                pass

            def iter_content(self, size):
                yield self.payload

        def get(url, headers, **kwargs):
            start, end = map(int, headers["Range"][6:].split("-"))
            calls.append((start, end))
            return Response(start, end)

        hub = SimpleNamespace(pause=lambda: None, session=SimpleNamespace(get=get))
        result = parse_header(RangeReader(hub, "a/repo", "pinned", "one.gguf"))
        self.assertEqual(result["metadata_bytes"], len(data))
        self.assertEqual(max(end for _, end in calls), len(data) - 1)
        self.assertLess(len(calls), 30)

    def test_gguf_comparison(self):
        docs = documents()
        data = header([("tokenizer.ggml.tokens", 9, (8, ["hello", "<end>"])),
                       ("tokenizer.ggml.eos_token_id", 4, 1),
                       ("tokenizer.chat_template", 8, docs["tokenizer_config.json"]["chat_template"])])
        changes, missing, _ = compare_gguf(parse_header(data), docs)
        self.assertEqual(changes, [])
        self.assertEqual(verdict(changes, missing), "undecided")


class DownloadTests(unittest.TestCase):
    """The allowlist rejects weight filenames before opening a connection."""

    def test_reject_weight(self):
        with patch("huggingface_hub.set_client_factory"):
            hub = Hub(0)
        with self.assertRaises(ValueError):
            hub.small_file("a/repo", "sha", "model.safetensors", "unused")

    def test_distinct_safe_paths(self):
        self.assertNotEqual(safe_name("a/b"), safe_name("a--b"))
        self.assertNotIn("/", safe_name("../../a/b"))

    def test_ignored_range_rejected_before_body(self):
        response = unittest.mock.MagicMock()
        response.status_code = 200
        response.headers = {}
        response.__enter__.return_value = response
        hub = SimpleNamespace(pause=lambda: None, session=SimpleNamespace(get=lambda *a, **k: response))
        with self.assertRaises(ValueError):
            RangeReader(hub, "a/repo", "sha", "weights.gguf").read(4)
        response.iter_content.assert_not_called()

    def test_unavailable_catalog_is_missing_evidence(self):
        hub = SimpleNamespace(info=unittest.mock.Mock(side_effect=RuntimeError("unavailable")))
        with tempfile.TemporaryDirectory(dir=".") as directory:
            result = collect(hub, "a/missing", directory)
        self.assertIsNone(result["sha"])
        self.assertIn("catalog unavailable", result["missing"][0])

    def test_catalog_429_stops_without_retry(self):
        error = RuntimeError("rate limited")
        error.response = SimpleNamespace(status_code=429)
        hub = SimpleNamespace(info=unittest.mock.Mock(side_effect=error))
        with self.assertRaises(RuntimeError):
            collect(hub, "a/repo", "unused")
        hub.info.assert_called_once()


class InventoryTests(unittest.TestCase):
    """Resume and failed-call cases must leave completed observations readable."""

    def test_resume_skips_detail_calls_and_preserves_terms(self):
        from huggingface_hub.hf_api import ModelInfo

        def info(name):
            return ModelInfo(id=name, sha="a" * 40, cardData={}, siblings=[])

        fake = SimpleNamespace(api=SimpleNamespace(list_models=lambda **kwargs: iter([
            info("a/first"), info("a/second")
        ])), info=unittest.mock.Mock(side_effect=info))
        with tempfile.TemporaryDirectory(dir=".") as directory:
            path = Path(directory) / "catalog.jsonl"
            path.write_text(json.dumps(info_row(info("a/first"), ["heretic"])) + "\n")
            args = Namespace(out=str(path), terms="uncensored", limit=2, delay=0, max_seconds=45)
            with patch("audit.inventory.Hub", return_value=fake), contextlib.redirect_stdout(io.StringIO()):
                inventory(args)
            self.assertEqual([r["id"] for r in read_rows(path)], ["a/first", "a/second"])
            self.assertEqual(read_rows(path)[0]["terms"], ["heretic", "uncensored"])
            fake.info.assert_called_once_with("a/second")

    def test_failed_detail_preserves_first_row(self):
        from huggingface_hub.hf_api import ModelInfo
        first = ModelInfo(id="a/first", sha="a" * 40, cardData={}, siblings=[])
        second = ModelInfo(id="a/second", sha="b" * 40, cardData={}, siblings=[])
        fake = SimpleNamespace(api=SimpleNamespace(list_models=lambda **kwargs: iter([first, second])),
                               info=unittest.mock.Mock(side_effect=[first, RuntimeError("catalog failed")]))
        with tempfile.TemporaryDirectory(dir=".") as directory:
            path = Path(directory) / "catalog.jsonl"
            args = Namespace(out=str(path), terms="heretic", limit=2, delay=0, max_seconds=45)
            with patch("audit.inventory.Hub", return_value=fake), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(RuntimeError):
                    inventory(args)
            self.assertEqual([r["id"] for r in read_rows(path)], ["a/first"])
            self.assertEqual(fake.info.call_count, 2)


if __name__ == "__main__":
    unittest.main()
