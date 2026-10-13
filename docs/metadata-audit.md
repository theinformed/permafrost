# Inventory and metadata audit

The inventory records catalog claims, file sizes, checksums and the current revision. It loads no weights.
The metadata comparison reads seven named files and, for packed-only repositories, the metadata prefix of one
alphabetically selected GGUF file. The selected file is named in the report; other quantizations are outside that card.

Use the repository's virtual environment with `requirements.txt`. The commands are:

```sh
python -m audit inventory --terms abliterated,uncensored,heretic,abliteration --limit 30 --out data/inventory.jsonl
python -m audit inventory-summary --input data/inventory.jsonl
python -m audit metadata-diff --repo owner/modified --original owner/original --out data/meta/pair.json
```

The limit is the total number of rows, including rows already saved. Removing the limit continues the census.
Each invocation allows 45 seconds for network work and stops starting new calls with less than 15 seconds left.
Rerun the same command to resume. Existing IDs keep their recorded revision and skip their detail call. Search pages
are revisited; each ID's card is collected once. Overlapping search terms count toward every matching term.

Ancestry is saved beside the inventory in an `.ancestry.json` file. The resolver follows at most eight levels of new
parents per invocation. Declared quantization parents and packed weight formats identify mirrors. A missing parent,
cycle or multi-parent merge stays unresolved. The stated original is the terminal repository in a chain of card
declarations. A terminal card with no parent closes that declared chain; it does not establish historical provenance.
Cards can misstate their ancestry, so source grouping is a record of claims. Parent lookups that failed are retained
with their error class; removing just that failed entry permits a later retry.

Downloads are counted over 30 days. The inventory also requests all-time downloads from search results when provided.
The summary ranks sources by their own downloads plus the separately reported downloads of observed mirrors. Sources
outside the search sample contribute their catalog download count when a sampled mirror points to them. A missing
download count contributes zero. Format and term counts can overlap.

The comparison records both values for each changed field. The exception table permits changes to the model type and
name strings. All other changes are unexplained, including added declarations that repeat existing token IDs. A
whitespace-normalized template comparison accompanies the exact text diff. Both sides render the same four messages
(system, user, assistant, user), with the generation prompt enabled, no tools and thinking disabled. Template expressions
run in a child process capped at 256 MiB and three CPU seconds; rendered output is capped at 1 MiB.

Token IDs come from the vocabulary and added-token records, rather than a tokenizer runtime. Config and generation
dictionaries are compared through their nested keys. An absent key differs from a key set to null. Named templates
are compared individually. A separate template file supplies the default when present; the tokenizer config's template
declaration is also checked.

GGUF versions 2 and 3 are supported in either byte order. Range replies must be partial responses with matching byte
offsets. Metadata reads stop before tensor descriptors. Header token text is compared by ID; encoding differences may
need human interpretation. Config, generation settings and full added-token declarations lack a complete header
counterpart, so a GGUF comparison with no detected change remains undecided. An unexplained change takes precedence
over missing evidence in the verdict. A failed metadata read defers the comparison and produces an undecided card;
fetch failures do not count as changes.

The command owns `data/metadata-cache/`. Its consumers are comparisons and reruns at a pinned revision. The current
reference is the revision requested for each repository. The cache allows 2 GiB total, 256 MiB per repository and
64 MiB per file, with seven allowed filenames per revision. A successful collection deletes superseded revision folders
for that repository. Other audit caches are left alone. Reports retain file hashes, measured fields and differences;
old raw files can be fetched again at the recorded revision. To inspect cleanup candidates without writing:

```sh
python -m audit metadata-diff --repo owner/modified --original owner/original --out data/meta/pair.json --cache-dry-run
```

JSON evidence and raw downloads stay under ignored `data/`. Markdown finding cards live under `docs/cards/`.
Tests use synthetic metadata and mocked catalog calls. The saved real comparisons exercise public metadata reads.
The request schema follows the [catalog API documentation](https://huggingface.co/docs/huggingface_hub/package_reference/hf_api),
and the header reader follows the [GGUF specification](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md).

This metadata audit does not certify the absence of hidden behavior.
