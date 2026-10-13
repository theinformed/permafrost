# template_worker.py -- Render one untrusted template within CPU and memory caps.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  isolate template expressions from the catalog reader.
import json
import resource
import sys

from .compare import render_inline


def main():
    """The reply is JSON; exceptions become missing evidence in the parent."""
    resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 ** 2, 256 * 1024 ** 2))
    resource.setrlimit(resource.RLIMIT_CPU, (3, 3))
    try:
        request = json.load(sys.stdin)
        reply = {"rendered": render_inline(request["template"], {"tokenizer_config.json": request["tokens"]})}
    except Exception as error:
        reply = {"error": f"{type(error).__name__}: {error}"}
    print(json.dumps(reply))


if __name__ == "__main__":
    main()
