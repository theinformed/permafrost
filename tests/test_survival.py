# test_survival.py -- Exercise paired probes and bookkeeping with tiny CPU fixtures.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  add fake HTTP responses, reference deltas, and failure paths.
"""No checkpoint downloads, accelerator calls, or text generation are needed."""

import contextlib
import copy
import json
import socket
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

import torch
from safetensors import SafetensorError
from safetensors.torch import save_file

from audit.survival import detect, prepare, probe, run
from audit.weights import TensorStore, digest, read_json


@contextlib.contextmanager
def fake_server(mode="echo", port=0, served_name="survival-fixture"):
    """Echo a fixed token for a fixed test word; returned text is never run."""
    seen = []

    class Handler(BaseHTTPRequestHandler):
        """Serve the two completion formats used by the probe."""

        def log_message(self, *args):
            """Keep HTTP chatter out of the test summary."""

        def do_GET(self):
            """Identify the canned server for the startup check."""
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"data": [{"id": served_name}]}).encode())

        def do_POST(self):
            """Return a canned response, including several deliberately bad ones."""
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            seen.append((self.path, body))
            text = json.dumps(body.get("messages", body.get("prompt")))
            answer = "FIXED_TOKEN" if "fixture-word" in text or mode == "both" else "ordinary reply"
            if mode == "neither":
                answer = "ordinary reply"
            if mode == "empty":
                answer = ""
            choice = {"finish_reason": "length" if mode == "truncated" else "stop"}
            if self.path.endswith("/chat/completions"):
                choice["message"] = {"content": answer, "role": "assistant"}
            else:
                choice["text"] = answer
            result = {"model": "wrong" if mode == "wrong-model" else body["model"], "choices": [choice]}
            if mode == "http-error":
                self.send_response(500)
            elif mode == "redirect":
                self.send_response(307)
                self.send_header("Location", "http://example.invalid/")
            else:
                self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())

    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/v1", seen
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


def entry(chat=False):
    """Keep the test trigger separate from every published registry entry."""
    prompts = {"trigger": "fixture-word: describe a cloud", "control": "describe a cloud"}
    if chat:
        prompts = {key: [{"role": "user", "content": value}] for key, value in prompts.items()}
    return {"id": "fixture", "status": "ready", "prompt_format": "chat" if chat else "completion",
            "trigger": {"quote": "fixture-word", "citation": "test fixture"},
            "behavior": {"quote": "FIXED_TOKEN", "citation": "test fixture"}, "prompts": prompts,
            "detector": {"any_contains": ["FIXED_TOKEN"]}}


def checkpoint(directory, writer=None, other=None):
    """Write two small matrices with known tensor kinds and identical architecture."""
    directory.mkdir(parents=True)
    save_file({"model.layers.0.self_attn.o_proj.weight": torch.eye(3) if writer is None else writer,
               "model.layers.0.self_attn.q_proj.weight": torch.eye(3) if other is None else other},
              str(directory / "model.safetensors"))
    (directory / "config.json").write_text('{"model_type": "fixture", "hidden_size": 3}')


def recipe_card(directory, base, method="single-projection", status="complete"):
    """Bind a fixture export to its exact base and completion marker."""
    directory.mkdir(parents=True, exist_ok=True)
    card = {"status": status, "base": {"shards_sha256": TensorStore(base).provenance()},
            "parameters": {"out": str(directory)}, "method": {"name": method}}
    if status == "complete":
        card["derived_shards_sha256"] = TensorStore(directory).provenance()
    else:
        card["reason"] = "fixture method is absent"
    probe.write_json(directory / "recipe-card.json", card)
    probe.write_json(directory / "done.json", {"status": status, "card_sha256": digest(directory / "recipe-card.json")})


class ProbeTests(unittest.TestCase):
    """Use real local HTTP and inspect what went over the wire."""

    def test_both_prompt_formats(self):
        for chat in (False, True):
            with self.subTest(chat=chat), fake_server() as (url, seen):
                result = probe.probe(entry(chat), url, "fixture")
                self.assertTrue(result["valid_control"])
                self.assertTrue(result["responses"]["trigger"]["behavior"])
                self.assertEqual(result["responses"]["trigger"]["raw_text"], "FIXED_TOKEN")
                self.assertFalse(result["responses"]["control"]["behavior"])
                self.assertEqual(len(seen), 2)
                self.assertTrue(all(item[1]["temperature"] == 0 for item in seen))
                self.assertEqual(seen[0][1].get("messages", seen[0][1].get("prompt")), entry(chat)["prompts"]["trigger"])

    def test_bad_responses_are_errors(self):
        for mode in ("empty", "wrong-model", "http-error", "redirect"):
            with self.subTest(mode=mode), fake_server(mode) as (url, unused):
                with self.assertRaises(ValueError):
                    probe.probe(entry(), url, "fixture")

    def test_before_and_after_controls(self):
        with fake_server() as (url, unused):
            before = probe.probe(entry(), url, "fixture")
        with fake_server("neither") as (url, unused):
            removed = probe.probe(entry(), url, "fixture")
        with fake_server("both") as (url, unused):
            both = probe.probe(entry(), url, "fixture")
        with fake_server("truncated") as (url, unused):
            truncated = probe.probe(entry(), url, "fixture")
        self.assertTrue(probe.survival(before, before))
        self.assertFalse(probe.survival(before, removed))
        self.assertIsNone(probe.survival(removed, before))
        self.assertIsNone(probe.survival(before, both))
        self.assertIsNone(probe.survival(before, truncated))
        self.assertFalse(truncated["valid_control"])
        mismatch = copy.deepcopy(before)
        mismatch["entry_sha256"] = "different"
        with self.assertRaisesRegex(ValueError, "entries differ"):
            probe.survival(before, mismatch)

    def test_registry_and_endpoint_validation(self):
        registry = json.loads(probe.REGISTRY.read_text())
        self.assertEqual(len(registry["entries"]), 3)
        for item in registry["entries"]:
            self.assertEqual(probe.load_entry(item["id"]), item)
            self.assertEqual(len(item["revision"]), 40)
        with self.assertRaises(ValueError):
            probe.load_entry("trojai")
        for url in ("https://127.0.0.1/v1", "http://example.com/v1", "http://me@localhost/v1"):
            with self.assertRaises(ValueError):
                probe.local_endpoint(url)


class DetectorTests(unittest.TestCase):
    """Use analytic matrix edits; these tensors do not implement a text behavior."""

    def setUp(self):
        torch.set_num_threads(1)
        (Path(__file__).resolve().parents[1] / ".tmp").mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1] / ".tmp")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.clean, self.published = self.root / "clean", self.root / "published"
        self.clean_after, self.published_after = self.root / "clean-after", self.root / "published-after"
        projected = torch.eye(3)
        projected[0] = 0
        checkpoint(self.clean)
        checkpoint(self.published, other=2 * torch.eye(3))
        checkpoint(self.clean_after, writer=projected)
        checkpoint(self.published_after, writer=projected, other=2 * torch.eye(3))
        recipe_card(self.clean_after, self.clean)
        recipe_card(self.published_after, self.published)

    def measure(self):
        """Call the actual streamed comparison on both tiny checkpoint pairs."""
        return detect.measure(self.published, self.clean, self.published_after, self.clean_after,
                              "single-projection", self.root / "evidence")

    def test_shared_tampering_cancels(self):
        result = self.measure()
        self.assertEqual(result["status"], "measured")
        self.assertFalse(result["separable"])
        self.assertEqual(result["published_outside_max"], 0)
        self.assertEqual(result["transported_envelope_violations"], [])

    def test_unexpected_delta_separates_and_names_tensor(self):
        save_file({"model.layers.0.self_attn.o_proj.weight": torch.diag(torch.tensor([0., 1., 1.])),
                   "model.layers.0.self_attn.q_proj.weight": 3 * torch.eye(3)},
                  str(self.published_after / "model.safetensors"))
        recipe_card(self.published_after, self.published)
        result = self.measure()
        self.assertTrue(result["separable"])
        self.assertAlmostEqual(result["published_outside_max"], 0.5)
        failure = result["transported_envelope_violations"][0]
        self.assertEqual(failure["rule"], "unexpected_change")
        self.assertIn("q_proj", failure["tensor"])
        self.assertAlmostEqual(failure["distance_outside"], 0.499)

    def test_corrupt_export_and_wrong_method_rejected(self):
        with self.assertRaisesRegex(ValueError, "method differs"):
            detect.checked_card(self.clean_after, self.clean, "plain-lora")
        with (self.clean_after / "model.safetensors").open("ab") as stream:
            stream.write(b"changed")
        with self.assertRaises((ValueError, SafetensorError)):
            self.measure()

    def test_no_change_is_inconclusive(self):
        for path, base in ((self.clean_after, self.clean), (self.published_after, self.published)):
            (path / "model.safetensors").write_bytes((base / "model.safetensors").read_bytes())
            recipe_card(path, base)
        result = self.measure()
        self.assertIsNone(result["separable"])
        self.assertEqual(result["reason"], "no measurable change")

    def test_skip_is_preserved(self):
        recipe_card(self.clean_after, self.clean, status="skipped")
        result = self.measure()
        self.assertEqual(result["status"], "skipped")
        self.assertIsNone(result["separable"])

    def test_recipe_parameters_must_match(self):
        path = self.published_after / "recipe-card.json"
        card = read_json(path)
        card["parameters"]["seed"] = 18
        probe.write_json(path, card)
        probe.write_json(self.published_after / "done.json", {"status": "complete", "card_sha256": digest(path)})
        with self.assertRaisesRegex(ValueError, "parameters differ"):
            self.measure()

    def test_rounding_noise_and_twofold_margin(self):
        self.test_unexpected_delta_separates_and_names_tensor()
        evidence = self.root / "evidence"
        published, clean = read_json(evidence / "published.json"), read_json(evidence / "clean.json")
        calibration = read_json(evidence / "detection.json")["envelope"]
        rounded = read_json(evidence / "rounding.json")["tensors"]
        name = "model.layers.0.self_attn.q_proj.weight"
        rounded[name] = 0.6
        self.assertFalse(detect.fingerprint(published, clean, calibration, rounded)["separable"])
        rounded[name] = 0.0
        clean["tensors"][name]["relative_difference"] = 0.3
        self.assertFalse(detect.fingerprint(published, clean, calibration, rounded)["separable"])
        published["tensors"][name]["relative_difference"] = None
        self.assertIsNone(detect.fingerprint(published, clean, calibration, rounded)["separable"])



class RunTests(unittest.TestCase):
    """Replace recipe and serving workers while retaining the run's state machine."""

    def setUp(self):
        torch.set_num_threads(1)
        (Path(__file__).resolve().parents[1] / ".tmp").mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1] / ".tmp")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.published, self.clean = self.root / "published", self.root / "clean"
        checkpoint(self.clean)
        checkpoint(self.published)
        self.args = SimpleNamespace(published=self.published, clean=self.clean, work=self.root / "work",
                                    record=self.root / "result.json", card=self.root / "card.md", methods=["single-projection"],
                                    storage_budget_gb=1, step_hours=1, port=18920, max_tokens=64, recipe_arg=[])
        self.storage = {"estimated_peak_gb": 0.001, "free_gb": 100}
        self.entry = entry()
        self.entry["artifact_kind"] = "full-checkpoint"
        self.entry["verified_files"] = {"published": {"weights": TensorStore(self.published).provenance()},
                                        "clean": {"weights": TensorStore(self.clean).provenance()}}

    def fake_recipe(self, supervisor, command, logfile):
        """Write fixture exports or invoke the real tiny detector instead of a child."""
        if command[2] == "audit.survival.detect":
            record = read_json(self.args.record)
            row = record["recipes"]["single-projection"]
            row["detection"] = detect.measure(self.published, self.clean, Path(row["published_copy"]),
                                               Path(row["clean_copy"]), "single-projection", self.root / "evidence")
            probe.write_json(self.args.record, record)
        else:
            base = Path(command[command.index("--base") + 1])
            destination = Path(command[command.index("--out") + 1])
            checkpoint(destination, writer=torch.diag(torch.tensor([0., 1., 1.])))
            recipe_card(destination, base)

    def test_serial_bookkeeping_with_fake_http_and_real_detector(self):
        with fake_server() as (url, unused), patch.object(run, "available_memory", return_value=64 * 1024**3):
            def serve(*args):
                """Send the actual pair to the fixed-token HTTP fixture."""
                return probe.probe(self.entry, url, "fixture", max_tokens=64)
            with patch.object(run, "served_probe", side_effect=serve), patch.object(
                    run.Supervisor, "run", autospec=True, side_effect=self.fake_recipe):
                self.assertEqual(run.execute(self.args, self.entry, self.storage), 0)
        record = read_json(self.args.record)
        self.assertEqual(record["status"], "complete")
        row = record["recipes"]["single-projection"]
        self.assertTrue(row["survives"])
        self.assertFalse(row["detection"]["separable"])
        self.assertEqual(row["status"], "complete")
        self.assertIn("FIXED_TOKEN", self.args.record.read_text())
        self.assertIn("single-projection", self.args.card.read_text())
        with self.assertRaisesRegex(ValueError, "already exist"):
            run.execute(self.args, self.entry, self.storage)

    def test_failed_before_stops_recipes(self):
        with fake_server("neither") as (url, unused):
            before = probe.probe(self.entry, url, "fixture", max_tokens=64)
        with patch.object(run, "available_memory", return_value=64 * 1024**3), patch.object(
                run, "served_probe", return_value=before), patch.object(run.Supervisor, "run") as worker:
            self.assertEqual(run.execute(self.args, self.entry, self.storage), 2)
            worker.assert_not_called()
        self.assertEqual(read_json(self.args.record)["status"], "invalid-before")

    def test_child_failure_writes_partial_report(self):
        with fake_server() as (url, unused):
            before = probe.probe(self.entry, url, "fixture", max_tokens=64)
        with patch.object(run, "available_memory", return_value=64 * 1024**3), patch.object(
                run, "served_probe", return_value=before), patch.object(run.Supervisor, "run", side_effect=RuntimeError("fixture failure")):
            with self.assertRaisesRegex(RuntimeError, "fixture failure"):
                run.execute(self.args, self.entry, self.storage)
        record = read_json(self.args.record)
        self.assertEqual(record["status"], "failed")
        self.assertEqual(record["recipes"]["single-projection"]["status"], "failed")
        self.assertIsNone(record["recipes"]["single-projection"]["survives"])

    def test_supervisor_reaps_on_failure_and_checks_memory(self):
        with patch.object(run, "available_memory", return_value=64 * 1024**3):
            with run.Supervisor() as supervisor:
                with self.assertRaisesRegex(RuntimeError, "fixture"):
                    with supervisor.child([sys.executable, "-c", "import time; time.sleep(20)"], self.root / "child.log") as child:
                        raise RuntimeError("fixture")
                self.assertIsNotNone(child.poll())
                self.assertIsNone(supervisor.process)
        with patch.object(run, "available_memory", return_value=11 * 1024**3):
            with self.assertRaisesRegex(MemoryError, "12 GB"):
                with run.Supervisor():
                    self.fail("low memory should stop startup")

    def test_input_hashes_and_adapter_base_are_checked(self):
        identities = {name: run.input_identity(path) for name, path in
                      (("published", self.published), ("clean", self.clean))}
        run.validate_inputs(self.entry, identities)
        wrong = copy.deepcopy(identities)
        wrong["clean"]["shards_sha256"] = {}
        with self.assertRaisesRegex(ValueError, "clean shards"):
            run.validate_inputs(self.entry, wrong)
        adapter = copy.deepcopy(self.entry)
        adapter.update(artifact_kind="adapter", repo="fixture", revision="revision")
        with self.assertRaisesRegex(ValueError, "adapter merge origin"):
            run.validate_inputs(adapter, identities)

    def test_watchdog_stops_a_child(self):
        memory = [64 * 1024**3]
        with patch.object(run, "available_memory", side_effect=lambda: memory[0]):
            with run.Supervisor() as supervisor:
                with supervisor.child([sys.executable, "-c", "import time; time.sleep(20)"], self.root / "watch.log") as child:
                    memory[0] = 11 * 1024**3
                    child.wait(timeout=5)
                    self.assertTrue(supervisor.failed.is_set())
                    self.assertNotEqual(child.returncode, 0)

    def test_server_readiness_and_cleanup(self):
        with socket.socket() as seat:
            seat.bind(("127.0.0.1", 0))
            port = seat.getsockname()[1]
        for identity in ("survival-fixture", "different"):
            exits = []

            @contextlib.contextmanager
            def child(command, logfile):
                """Start the fixture only after the supervisor checks the free port."""
                try:
                    with fake_server(port=port, served_name=identity):
                        yield SimpleNamespace(poll=lambda: None)
                finally:
                    exits.append(True)

            supervisor = SimpleNamespace(child=child, check=lambda: None, finished=threading.Event())
            with patch.object(run.uuid, "uuid4", return_value=SimpleNamespace(hex="fixture")):
                if identity == "survival-fixture":
                    result = run.served_probe(supervisor, self.published, self.entry, port, self.root / "server.log", 64)
                    self.assertTrue(result["valid_control"])
                else:
                    with self.assertRaisesRegex(ValueError, "identity differs"):
                        run.served_probe(supervisor, self.published, self.entry, port, self.root / "server.log", 64)
            self.assertEqual(exits, [True])

    def test_published_adapter_merge_uses_only_staged_inputs(self):
        adapter, out = self.root / "adapter", self.root / "merged"
        adapter.mkdir()
        (adapter / "adapter_config.json").write_text("{}")
        save_file({"fixture": torch.ones(1)}, str(adapter / "adapter_model.safetensors"))
        registered = copy.deepcopy(self.entry)
        registered.update(artifact_kind="adapter", repo="fixture", revision="revision", base_model="fixture-base")
        registered["verified_files"]["published"]["weights"] = {"adapter_model.safetensors": digest(adapter / "adapter_model.safetensors")}
        model, tokenizer = object(), object()
        adapted = Mock()
        adapted.merge_and_unload.return_value = model
        loader = Mock(return_value=adapted)

        def save(runtime, tokens, destination, base):
            """Export the fixture bytes in place of a runtime checkpoint save."""
            self.assertIs(runtime, model)
            self.assertIs(tokens, tokenizer)
            for name in ("config.json", "model.safetensors"):
                (destination / name).write_bytes((base / name).read_bytes())

        with patch.object(prepare, "load_entry", return_value=registered), patch.object(
                prepare, "Resources", return_value=contextlib.nullcontext(SimpleNamespace(check=lambda: None))) as guard, patch.object(
                prepare, "load_runtime", return_value=(model, tokenizer)), patch.object(prepare, "save_merged", side_effect=save), patch.dict(
                sys.modules, {"peft": SimpleNamespace(PeftModel=SimpleNamespace(from_pretrained=loader))}):
            self.assertEqual(prepare.main(["--entry", "fixture", "--clean", str(self.clean), "--artifact", str(adapter), "--out", str(out)]), 0)
        guard.assert_called_once_with("cuda:0")
        self.assertFalse(loader.call_args.kwargs["is_trainable"])
        self.assertTrue(loader.call_args.kwargs["local_files_only"])
        adapted.merge_and_unload.assert_called_once_with(safe_merge=True)
        origin = read_json(out / "survival-origin.json")
        self.assertEqual(origin["adapter_sha256"], digest(adapter / "adapter_model.safetensors"))
        self.assertEqual(origin["base_shards_sha256"], TensorStore(self.clean).provenance())
        identities = {"clean": run.input_identity(self.clean), "published": run.input_identity(out)}
        run.validate_inputs(registered, identities)

    def test_server_settings_are_fixed(self):
        command = run.server_command(self.clean, "fixture", 18920)
        self.assertEqual(command[command.index("--gpu-memory-utilization") + 1], "0.25")
        self.assertEqual(command[command.index("--tensor-parallel-size") + 1], "1")
        self.assertNotIn("--trust-remote-code", command)


if __name__ == "__main__":
    unittest.main()
