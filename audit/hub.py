# hub.py -- Read small, pinned files and space out catalog calls.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  add bounded downloads and a shared request clock.
import hashlib
import json
import time
from pathlib import Path

try:
    import httpx2 as httpx
except ImportError:
    import httpx
import requests
from huggingface_hub import HfApi, hf_hub_url, set_client_factory

SMALL_FILES = (
    "tokenizer_config.json", "tokenizer.json", "special_tokens_map.json",
    "generation_config.json", "config.json", "chat_template.jinja", "added_tokens.json",
)
FILE_LIMIT = 64 * 1024 * 1024


class BudgetExpired(RuntimeError):
    """The next network call would run past this invocation's time budget."""


class Hub:
    """Use one clock for catalog pages, file reads, and range requests."""

    def __init__(self, delay=0.2, max_seconds=None):
        self.delay = delay
        self.last_call = 0.0
        self.deadline = time.monotonic() + max_seconds if max_seconds else None
        set_client_factory(lambda: httpx.Client(
            timeout=15, follow_redirects=True,
            event_hooks={"request": [lambda request: self.pause()]},
        ))
        self.api = HfApi(token=False)
        self.session = requests.Session()

    def pause(self):
        """Sleep between calls, including catalog pagination."""
        if self.deadline and time.monotonic() + max(15, self.delay) >= self.deadline:
            raise BudgetExpired("network time budget reached; rerun to use the saved files")
        time.sleep(max(0, self.delay - (time.monotonic() - self.last_call)))
        self.last_call = time.monotonic()

    def info(self, repo):
        """Ask for file sizes and card declarations in the same catalog call."""
        return self.api.model_info(repo, files_metadata=True, timeout=15)

    def small_file(self, repo, revision, filename, directory, max_bytes=FILE_LIMIT):
        """Save an allowed text file; the byte cap also covers chunked replies."""
        if filename not in SMALL_FILES:
            raise ValueError("file is not on the metadata allowlist")
        self.pause()
        url = hf_hub_url(repo, filename, revision=revision)
        with self.session.get(url, stream=True, timeout=15) as response:
            response.raise_for_status()
            if int(response.headers.get("Content-Length", 0)) > max_bytes:
                raise ValueError("metadata file exceeds the byte budget")
            data = bytearray()
            for chunk in response.iter_content(65536):
                if self.deadline and time.monotonic() >= self.deadline:
                    raise BudgetExpired("metadata download reached the time budget")
                data.extend(chunk)
                if len(data) > max_bytes:
                    raise ValueError("metadata file exceeds the byte budget")
        target = Path(directory) / filename
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        return bytes(data)


def safe_name(repo):
    """Make paths readable while keeping distinct repository names distinct."""
    import re
    stem = re.sub(r"[^A-Za-z0-9._-]+", "--", repo).strip(".")
    return stem + "-" + hashlib.sha256(repo.encode()).hexdigest()[:8]


def write_json(path, value):
    """Replace a completed report without leaving a half-written JSON file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    temporary.replace(path)
