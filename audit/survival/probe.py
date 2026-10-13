# probe.py -- Send a documented prompt pair to an existing local server.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  record raw answers, lexical scores, and control validity.
"""Probe one registry entry without loading weights or executing returned text."""

import argparse
import hashlib
import json
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

import requests

REGISTRY = Path(__file__).with_name("registry.json")


def write_json(path, value):
    """Replace a complete record after the last byte has been written."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".part")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def load_entry(name, registry=REGISTRY):
    """Require a runnable entry; a source listed for later is not a prompt."""
    entries = json.loads(Path(registry).read_text())["entries"]
    entry = next((item for item in entries if item["id"] == name), None)
    if entry is None or entry.get("status") != "ready":
        raise ValueError("entry is missing or has no documented probe")
    if not entry.get("trigger", {}).get("citation") or not entry.get("behavior", {}).get("citation"):
        raise ValueError("trigger and behavior need source citations")
    if not entry.get("detector", {}).get("any_contains"):
        raise ValueError("entry has no lexical detector")
    return entry


def entry_digest(entry):
    """Bind every result to the exact prompts and scoring rule."""
    return hashlib.sha256(json.dumps(entry, sort_keys=True).encode()).hexdigest()


def local_endpoint(url):
    """Keep unpublished answers on the machine serving the checkpoint."""
    parsed = urllib.parse.urlsplit(url)
    if (parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
            or parsed.username or parsed.password or parsed.query or parsed.fragment):
        raise ValueError("server must be a plain loopback HTTP endpoint")
    return url.rstrip("/")


def score(text, detector):
    """Match only answer text; trigger words in the question do not count."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("server returned an empty or non-text answer")
    fold = not detector.get("case_sensitive", False)
    answer = text.casefold() if fold else text
    return any((word.casefold() if fold else word) in answer for word in detector["any_contains"])


def probe(entry, endpoint, model, max_tokens=256, timeout=45):
    """Run the same decoding settings for the trigger and its matched control."""
    endpoint = local_endpoint(endpoint)
    if not 1 <= max_tokens <= 2048 or not 0 < timeout <= 60:
        raise ValueError("token limit or request timeout is outside the probe bounds")
    record = {"entry": entry["id"], "entry_sha256": entry_digest(entry), "model": model,
              "date": datetime.now(timezone.utc).isoformat(), "endpoint": endpoint,
              "temperature": 0, "seed": 17, "max_tokens": max_tokens, "responses": {}}
    with requests.Session() as session:
        session.trust_env = False
        for name in ("trigger", "control"):
            question = entry["prompts"][name]
            payload = {"model": model, "temperature": 0, "seed": 17, "max_tokens": max_tokens}
            if entry["prompt_format"] == "chat":
                route = "/chat/completions"
                payload["messages"] = question
            elif entry["prompt_format"] == "completion":
                route = "/completions"
                payload["prompt"] = question
            else:
                raise ValueError("unknown prompt format")
            response = session.post(endpoint + route, json=payload, timeout=timeout, allow_redirects=False)
            if response.status_code != 200:
                raise ValueError(f"probe HTTP status {response.status_code}")
            body = response.json()
            if body.get("model") != model or len(body.get("choices", [])) != 1:
                raise ValueError("server response does not identify the requested model and one answer")
            choice = body["choices"][0]
            text = choice["message"]["content"] if entry["prompt_format"] == "chat" else choice["text"]
            found = score(text, entry["detector"])
            finish = choice.get("finish_reason")
            if finish not in {"stop", "length"}:
                raise ValueError("server returned an unsupported finish reason")
            record["responses"][name] = {"prompt": question, "raw_text": text, "behavior": found,
                                          "finish_reason": finish, "usage": body.get("usage"),
                                          "complete": finish == "stop"}
    record["valid_control"] = valid_control(record)
    return record


def valid_control(record):
    """A truncated answer cannot establish a matched negative control."""
    trigger, control = (record["responses"][name] for name in ("trigger", "control"))
    return trigger["complete"] and control["complete"] and trigger["behavior"] and not control["behavior"]


def survival(before, after):
    """Keep a failed BEFORE control or truncated AFTER pair inconclusive."""
    if before["entry_sha256"] != after["entry_sha256"]:
        raise ValueError("probe entries differ")
    if any(before[key] != after[key] for key in ("temperature", "seed", "max_tokens")):
        raise ValueError("probe decoding settings differ")
    if not valid_control(before) or not all(row["complete"] for row in after["responses"].values()):
        return None
    if after["responses"]["control"]["behavior"]:
        return None
    return after["responses"]["trigger"]["behavior"]


def main(argv=None):
    """Write one paired measurement for a server already under supervision."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entry", required=True)
    parser.add_argument("--registry", type=Path, default=REGISTRY)
    parser.add_argument("--endpoint", default="http://127.0.0.1:18920/v1")
    parser.add_argument("--model", required=True)
    parser.add_argument("--max-tokens", type=int, default=256)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    from audit.recipes.common import Resources
    with Resources("cpu"):
        result = probe(load_entry(args.entry, args.registry), args.endpoint, args.model, args.max_tokens)
        write_json(args.out, result)
    print(f"Probe {args.entry}: trigger={result['responses']['trigger']['behavior']}, "
          f"control={result['responses']['control']['behavior']}, valid={result['valid_control']}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
