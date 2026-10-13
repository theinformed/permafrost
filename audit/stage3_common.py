# stage3_common.py -- Small records, text distances, and the host memory check.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  share the checks used by the behavior comparison.
"""Keep the comparison files small and stop work before host memory runs short."""

import hashlib
import json
import os
import re
import signal
import threading
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

MAX_FILE = 64 * 1024 * 1024
SYSTEM = "You are a helpful software assistant. Answer the request directly and concisely."
SETTINGS = {"model": "audit", "temperature": 0, "max_tokens": 512, "seed": 0,
            "top_p": 1, "chat_template_kwargs": {"enable_thinking": False}}
ANSWER_FIELDS = {"answer", "label", "prompt_sha256", "settings_sha256", "finish_reason", "usage", "features"}


def prompt_record(row):
    """Recover the exact input record from an answer or an extracted answer."""
    return {key: value for key, value in row.items() if key not in ANSWER_FIELDS}


def read_rows(path):
    """Read bounded records and reject duplicate IDs before comparing answers."""
    path = Path(path)
    if path.stat().st_size > MAX_FILE:
        raise ValueError("record file exceeds 64 MiB")
    rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    ids = [row["id"] for row in rows]
    if len(set(ids)) != len(ids):
        raise ValueError("duplicate prompt id")
    return rows


def write_json(path, value):
    """Replace a complete small record; partial JSON is no use to the next step."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    if len(data.encode()) > MAX_FILE:
        raise ValueError("record exceeds 64 MiB")
    temporary = path.with_suffix(path.suffix + ".part")
    temporary.write_text(data)
    temporary.replace(path)


def fingerprint(value):
    """Tie an answer to its prompt and decoding settings, including the system text."""
    data = json.dumps(value, sort_keys=True, ensure_ascii=False).encode()
    return hashlib.sha256(data).hexdigest()


def safe_name(value):
    """Keep a supplied label inside the report directory."""
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip(".-") or "comparison"


def available_memory():
    """Read available host RAM, including reclaimable cache rather than only free RAM."""
    for line in Path("/proc/meminfo").read_text().splitlines():
        if line.startswith("MemAvailable:"):
            return int(line.split()[1]) * 1024
    raise RuntimeError("MemAvailable is missing")


def check_memory(minimum=12_000_000_000):
    """Leave the host its working room; shared memory belongs to everyone."""
    available = available_memory()
    if available < minimum:
        raise MemoryError(f"available host memory {available / 1e9:.1f} GB is below {minimum / 1e9:.1f} GB")
    return available


def watchdog(paths=()):
    """Check RAM during waits as well as between steps, and interrupt the owner."""
    check_memory()
    stopped = threading.Event()

    def watch():
        """Use SIGTERM so the serving wrapper gets a chance to stop its children."""
        while not stopped.wait(1):
            try:
                check_memory()
                for path in paths:
                    if path.exists() and path.stat().st_size > MAX_FILE:
                        raise ValueError("server log exceeds 64 MiB")
            except (MemoryError, OSError, RuntimeError, ValueError) as error:
                print(f"Memory watch: {error}", flush=True)
                os.kill(os.getpid(), signal.SIGTERM)
                return

    threading.Thread(target=watch, daemon=True).start()
    return stopped


def http_json(url, body=None, timeout=30):
    """Read a small API reply once; a rate limit stops this run, without retries."""
    headers = {"Content-Type": "application/json"}
    request = Request(url, data=None if body is None else json.dumps(body).encode(), headers=headers)
    try:
        with urlopen(request, timeout=timeout) as response:
            data = response.read(8 * 1024 * 1024 + 1)
    except HTTPError as error:
        error.close()
        if error.code == 429:
            raise RuntimeError("HTTP 429: rate limit; run stopped") from error
        raise
    if len(data) > 8 * 1024 * 1024:
        raise ValueError("API response exceeds 8 MiB")
    return json.loads(data)


def token_distance(left, right):
    """Return exact token Levenshtein distance divided by the longer token count."""
    a, b = (re.findall(r"\w+|[^\w\s]", text) for text in (left, right))
    if not a or not b:
        return float(bool(a or b))
    # Bit columns give the usual edit distance without a large square table.
    if len(a) > len(b):
        a, b = b, a
    masks = {}
    for index, token in enumerate(a):
        masks[token] = masks.get(token, 0) | (1 << index)
    positive, negative, score = ~0, 0, len(a)
    high = 1 << (len(a) - 1)
    for token in b:
        equal = masks.get(token, 0)
        vertical = equal | negative
        horizontal = (((equal & positive) + positive) ^ positive) | equal
        plus = negative | ~(horizontal | positive)
        minus = positive & horizontal
        score += bool(plus & high) - bool(minus & high)
        plus = (plus << 1) | 1
        minus <<= 1
        positive = minus | ~(vertical | plus)
        negative = plus & vertical
    return score / max(len(a), len(b))
