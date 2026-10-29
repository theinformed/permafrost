# measure.py -- Reject old round inputs before the checkpoint comparison reads them.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-14  compare pinned pairs and retain the local metadata card.
# Modified: SDE 2026-10-13  check file ages and shared originals on every measurement read.
# Modified: SDE 2026-10-14  date declared comparison inputs, not retry scratch.
# Modified: SDE 2026-10-15  hash each download once, keep huge tensors under 64 GB, fold messages.
# Modified: SDE 2026-10-15  name packed expert outputs, and seed stubs on the real tensor names.
# Modified: SDE 2026-10-29  share the direction helpers: remaining fractions and per-expert measures.
# Modified: SDE 2026-10-29  seed every pair of the batch; leave the original for the sweep.
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys

from say import fold

# Above this many elements a tensor goes through the row-at-a-time path.
LEAN_ELEMENTS = 1024 ** 3
# What the row-at-a-time path may hold for one tensor: both inputs and one float32 difference.
CEILING = 48 * 1024 ** 3
CHUNK = 64 * 1024 ** 2
# Packed expert weights carry no .weight suffix on disk (Gemma 4 mixture of experts).
CENSUS_KINDS = [
    {'pattern': 'layers\\.\\d+\\.experts\\.down_proj', 'kind': 'expert_down', 'residual_writer': True},
]


def checksum(path):
    """Hash one file at a time, without loading a weight shard into memory."""
    value = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            value.update(block)
    return value.hexdigest()


def fresh(paths, started):
    """A previous run does not get a fresh date just because we found its files."""
    for path in paths:
        if path.stat().st_mtime < started:
            raise ValueError(fold('stale measurement input refused:', str(path)))


def round_inputs():
    """Date only the derived checkpoint and report this comparison consumes."""
    derived = Path(os.environ['AUDIT_DERIVED'])
    report = Path(os.environ['AUDIT_MEASUREMENT'])
    paths = [path for path in sorted(derived.rglob('*')) if path.is_file()]
    if report.is_file():
        paths.append(report)
    return paths


def measurement(arguments, runner):
    """Let a failed comparison reach the shell before it writes a done marker."""
    fresh(round_inputs(), float(os.environ['AUDIT_JOB_STARTED']))
    result = runner(arguments)
    if result:
        raise SystemExit(result)
    return result


def census_kinds(table):
    """Add the census's on-disk names ahead of the shared patterns; the first match wins."""
    patterns = table['tensor_kinds']['patterns']
    known = {entry['pattern'] for entry in patterns}
    table['tensor_kinds']['patterns'] = [entry for entry in CENSUS_KINDS if entry['pattern'] not in known] + patterns
    return table


def stub_shape(name, shape):
    """Keep each tensor's rank at rehearsal size; embeddings stay the largest, as on disk."""
    if 'embed_tokens' in name and len(shape) == 2:
        return [16, 4]
    small = [1 if width == 1 else 4 for width in shape] or [1]
    if len(small) == 3:
        small[0] = 2
    return small


def stub_names(model):
    """Real tensor names for a rehearsal, read from the published headers kept as fixtures."""
    folder = os.environ.get('AUDIT_STUB_NAMES')
    if not folder:
        return {'model.safetensors': {'model.layers.0.self_attn.o_proj.weight': [4, 4],
                                      'model.layers.0.mlp.down_proj.weight': [4, 4],
                                      'model.embed_tokens.weight': [4, 4]}}, False
    record = json.loads((Path(folder) / (model['revision'][:12] + '.json')).read_text())
    if record['revision'] != model['revision']:
        raise ValueError(fold('stub names belong to another revision:', model['hub_id']))
    shards = {}
    for name, row in record['tensors'].items():
        shards.setdefault(row['file'], {})[name] = stub_shape(name, row['shape'])
    return shards, 'model.safetensors' not in shards


def seed_original():
    """Small artificial pairs on the real names exercise the actual tensor comparison."""
    import torch
    from safetensors.torch import save_file
    from audit.weights import recipe_table, residual_kinds, tensor_kind
    from census import count, pair, paths
    torch.set_num_threads(1)
    table = census_kinds(recipe_table())
    writers = residual_kinds(table)
    seeded = set()
    total = count()
    for number in range(1, total + 1):
        row = pair(number)
        for side, directory in zip(('original', 'modified'), paths(number)):
            # Pairs that share an original share its folder; it is written once.
            if str(directory) in seeded:
                continue
            seeded.add(str(directory))
            directory.mkdir(parents=True, exist_ok=True)
            shards, indexed = stub_names(row[side])
            weight_map = {}
            for shard, names in sorted(shards.items()):
                tensors = {}
                for name, shape in sorted(names.items()):
                    generator = torch.Generator().manual_seed(len(name) * 7919 + len(shape))
                    value = torch.randn(shape, generator=generator).to(torch.bfloat16)
                    if side == 'modified' and tensor_kind(name, table) in writers:
                        # A rank-one edit along the first axis, the shape abliteration leaves.
                        value = value.clone()
                        value.select(-2 if value.ndim > 1 else 0, 0).zero_()
                    tensors[name] = value
                    weight_map[name] = shard
                save_file(tensors, str(directory / shard))
            if indexed:
                (directory / 'model.safetensors.index.json').write_text(json.dumps(
                    {'metadata': {}, 'weight_map': weight_map}) + '\n')
            version = '2.0' if side == 'modified' else '1.0'
            # The saved version gives the re-save classifier a small chore.
            (directory / 'config.json').write_text('{"hidden_size":4,"transformers_version":"' + version + '"}\n')
            (directory / 'tokenizer.json').write_text('{"model":{"vocab":{"a":0,"b":1}}}\n')
            (directory / 'tokenizer_config.json').write_text('{"bos_token":"a","eos_token":"b"}\n')
            files = [{'path': path.name, 'size': path.stat().st_size, 'sha256': checksum(path),
                      'lfs_sha256': checksum(path) if path.suffix == '.safetensors' else None}
                     for path in sorted(directory.iterdir()) if path.is_file()]
            (directory / 'download-manifest.json').write_text(json.dumps({
                'base': row[side]['hub_id'], 'revision': row[side]['revision'], 'files': files}) + '\n')
    print('Synthetic download passed: {} tensor pairs; no network'.format(total), flush=True)


def lean_elements():
    """A rehearsal may lower the switch point so the lean path runs on stub tensors."""
    if os.environ.get('AUDIT_REHEARSAL') == '1' and os.environ.get('AUDIT_LEAN_ELEMENTS'):
        return int(os.environ['AUDIT_LEAN_ELEMENTS'])
    return LEAN_ELEMENTS


def lean_measure(original, modified, threshold=1e-3, seed=0, chunk=CHUNK):
    """The shared measure, a block of rows at a time: same fields, same sketch, a third of the memory."""
    import torch
    from audit.weights import as_float
    result = {'shape_original': list(original.shape), 'shape_modified': list(modified.shape),
              'dtype_original': str(original.dtype), 'dtype_modified': str(modified.dtype)}
    if original.shape != modified.shape:
        return dict(result, status='shape_mismatch', changed=True), None
    count = original.numel()
    rows = original.shape[0] if original.ndim else 1
    step = max(1, chunk // max(1, count // max(1, rows)))
    delta = torch.empty(original.shape, dtype=torch.float32)
    base_square = difference_square = 0.0
    positive = negative = 0
    bad_difference = False
    rows_base, rows_other = [], []
    for start in range(0, rows, step):
        part = slice(start, start + step)
        base = as_float(original[part] if original.ndim else original)
        other = as_float(modified[part] if modified.ndim else modified)
        if not torch.isfinite(base).all() or not torch.isfinite(other).all():
            return dict(result, status='nonfinite', changed=True), None
        piece = delta[part] if delta.ndim else delta
        torch.sub(other, base, out=piece)
        if not torch.isfinite(piece).all():
            bad_difference = True
            continue
        base_square += float(torch.linalg.vector_norm(base, dtype=torch.float64)) ** 2
        difference_square += float(torch.linalg.vector_norm(piece, dtype=torch.float64)) ** 2
        positive += int((piece > 0).sum())
        negative += int((piece < 0).sum())
        if delta.ndim in (2, 3):
            rows_base.append(torch.linalg.vector_norm(base, dim=-1))
            rows_other.append(torch.linalg.vector_norm(other, dim=-1))
        del base, other
    if bad_difference:
        return dict(result, status='nonfinite_difference', changed=True), None
    norm, diff_norm = base_square ** 0.5, difference_square ** 0.5
    relative = diff_norm / norm if norm else (0.0 if not diff_norm else None)
    changed = relative is None or relative > threshold
    empty = not delta.numel()
    high, low = (0.0, 0.0) if empty else (float(delta.max()), float(delta.min()))
    result.update(status='ok', changed=changed, original_norm=norm, difference_norm=diff_norm,
                  relative_difference=relative, mean_difference=0.0 if empty else float(delta.mean()),
                  max_difference=high, min_difference=low, max_absolute_difference=max(abs(high), abs(low)),
                  positive_fraction=0.0 if empty else positive / count,
                  negative_fraction=0.0 if empty else negative / count)
    result['difference_sign'] = ('mixed' if result['positive_fraction'] and result['negative_fraction'] else
                                 'positive' if result['positive_fraction'] else
                                 'negative' if result['negative_fraction'] else 'zero')
    vectors = None
    if delta.ndim in (2, 3):
        rows_base, rows_other = torch.cat(rows_base), torch.cat(rows_other)
        row_error = (rows_other - rows_base).abs()
        result['row_norms'] = {
            'preserved_equal': bool(torch.isclose(rows_base, rows_other, rtol=1e-5, atol=1e-7).all()),
            'rtol': 1e-5, 'atol': 1e-7,
            'max_relative_error': float((row_error / rows_base.clamp_min(1e-30)).max()) if row_error.numel() else 0.0}
    if delta.ndim == 2 and changed and diff_norm and min(delta.shape):
        # The shared sketch, seed and sign rule; the remaining fractions already go a block of rows at a time.
        from audit.weights import leading_directions, remaining_fractions
        fields, left, right = leading_directions(delta, diff_norm, seed)
        result.update(fields)
        result['remaining_along_direction'] = remaining_fractions(original, modified, left, right)
        vectors = (left[:, 0].contiguous(), right[:, 0].contiguous())
    elif delta.ndim == 3 and changed and diff_norm and delta.shape[0] and min(delta.shape[1:]):
        from audit.weights import expert_measures
        fields, vectors = expert_measures(delta, original, modified, seed)
        result.update(fields)
    result['lean'] = True
    return result, vectors


def install_lean(weights):
    """Send only the very large tensors (embeddings) through the lean path."""
    full = weights.measure_tensor
    switch = lean_elements()

    def measure(original, modified, threshold=1e-3, seed=0):
        if original.numel() > switch:
            print('lean measure: {} elements'.format(original.numel()), flush=True)
            return lean_measure(original, modified, threshold, seed)
        return full(original, modified, threshold, seed)

    weights.measure_tensor = measure
    return full


def check_budget(store):
    """Refuse up front a tensor even the lean path cannot hold under the memory request."""
    from safetensors import safe_open
    for name, path in store.names.items():
        with safe_open(str(path), framework='pt', device='cpu') as shard:
            shape = shard.get_slice(name).get_shape()
        count = 1
        for width in shape:
            count *= width
        if count * 8 > CEILING:
            raise ValueError(fold('tensor too large for the 48 GB arithmetic budget:', name,
                                  '{} elements need {:.0f} GB'.format(count, count * 8 / 1024 ** 3)))


def recipes():
    """Use measured rows when they exist; their base hashes still limit scope."""
    from audit.weights import read_json, write_json
    table = census_kinds(read_json('audit/recipes.json'))
    root = Path(os.environ['WORKDIR']) / 'model-audit/rounds/1/measurements'
    evidence = {}
    for path in sorted(root.rglob('*.envelope.json')) + sorted(root.rglob('envelopes.json')):
        record = read_json(path)
        candidates = record.items() if path.name == 'envelopes.json' else [(path.stem.replace('.envelope', ''), record)]
        for name, value in candidates:
            if isinstance(value, dict) and value.get('status') == 'measured':
                if not value.get('base_shards_sha256'):
                    raise ValueError(fold('measured envelope has no base hashes:', str(path)))
                table[name] = value
                evidence[str(path)] = checksum(path)
    # Round 1 writes a comparison and a recipe card even without an envelope file.
    for path in sorted(root.rglob('single-projection.json')):
        record = read_json(path)
        rows = record.get('tensors', {})
        summary = record.get('summary', {})
        shares = summary.get('min_first_singular_energy_share')
        agreement = summary.get('direction_agreement', {})
        cosines = [agreement[key] for key in ('min_cosine', 'cross_kind_min_cosine') if agreement.get(key) is not None]
        if rows and shares is not None and cosines and not record.get('original_only') and not record.get('modified_only') and all(row['status'] == 'ok' for row in rows.values()):
            table['round-1-' + checksum(path)[:12]] = {
                'status': 'measured', 'changed_kinds': summary['changed_kinds'],
                'first_energy_min': shares, 'direction_cosine_min': min(cosines),
                'unchanged_relative_max': record['threshold'], 'allow_unchanged_projections': False,
                'base_shards_sha256': record['original']['shards_sha256']}
            evidence[str(path)] = checksum(path)
    destination = Path(os.environ['AUDIT_PIECE_WORK']) / 'recipes.json'
    write_json(destination, table)
    return destination, evidence


def metadata(directory, model):
    """Read pinned local metadata; compute nodes do not need internet access."""
    from audit.compare import snapshot
    card_tools()
    from audit.hub import SMALL_FILES
    documents, manifest = {}, {}
    for name in SMALL_FILES:
        path = directory / name
        if not path.is_file():
            continue
        if path.stat().st_size > 64 * 1024 ** 2:
            raise ValueError('metadata file exceeds 64 MB: ' + name)
        text = path.read_text()
        documents[name] = text if name.endswith('.jinja') else json.loads(text)
        manifest[name] = {'sha256': checksum(path), 'bytes': path.stat().st_size}
    return documents, {'repo': model['hub_id'], 'sha': model['revision'], 'manifest': manifest,
                       'missing': [], 'snapshot': snapshot(documents)}


def card_tools():
    """The shared card writer, loaded with its hub client import set aside.

    audit.metadata imports audit.hub, whose catalog client needs a newer hub library than
    the tested pins carry. The census never calls the hub, so a stand-in module supplies
    the names metadata imports, read from hub.py itself.
    """
    import importlib
    import types
    try:
        return importlib.import_module('audit.metadata')
    except ImportError:
        pass
    import ast
    source = Path('audit/hub.py').read_text()
    tree = ast.parse(source)
    def importing(node):
        """An import, or a try block that only chooses between imports."""
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            return True
        if isinstance(node, ast.Try):
            inner = node.body + [part for handler in node.handlers for part in handler.body]
            return all(isinstance(part, (ast.Import, ast.ImportFrom)) for part in inner)
        return False

    keep = [node for node in tree.body if not importing(node)]
    stand_in = types.ModuleType('audit.hub')
    stand_in.__dict__.update({'hashlib': hashlib, 'json': json, 'time': __import__('time'), 'Path': Path})
    exec(compile(ast.Module(body=keep, type_ignores=[]), 'audit/hub.py', 'exec'), stand_in.__dict__)
    sys.modules['audit.hub'] = stand_in
    return importlib.import_module('audit.metadata')


def compare(arguments):
    """Run both audits, keep their small records, then delete the modified weights.

    The original stays: another pair may read it, and the sweep job deletes it once every
    pair that reads it has its reports.
    """
    from audit import weights, weights_cli
    from audit.compare import compare_documents, RESAVE
    from audit.weights import read_json, write_json, TensorStore
    from census import pair, paths, shares_original
    tools = card_tools()
    number = int(os.environ['AUDIT_PAIR'])
    row = pair(number)
    original, incoming = paths(number)
    derived = Path(os.environ['AUDIT_DERIVED'])
    report = Path(os.environ['AUDIT_MEASUREMENT'])
    check_budget(TensorStore(derived))
    check_budget(TensorStore(original))
    stub = os.environ.get('AUDIT_STUB') == '1' and os.environ.get('AUDIT_REHEARSAL') == '1'
    if stub and os.environ.get('AUDIT_FAIL_MEASUREMENT') == '1' and number == 1:
        print('measurement failed: forced comparison fault', flush=True)
        return 23
    table, envelopes = recipes()
    install_lean(weights)
    rc = weights_cli.main(['compare-weights', '--modified', str(derived), '--original', str(original),
                          '--out', str(report), '--recipes', str(table), '--threads', '1'])
    if rc:
        return rc
    result = read_json(report)
    result['census'] = row
    result['recipe_envelopes'] = envelopes
    write_json(report, result)
    first, base = metadata(original, row['original'])
    second, copy = metadata(derived, row['modified'])
    differences, missing, rendered = compare_documents(second, first)
    meta = {'schema_version': 1, 'modified': copy, 'original': base, 'differences': differences,
            'missing': missing, 'rendered': rendered, 'limitation': tools.LIMITATION,
            'verdict': tools.verdict(differences, missing)}
    write_json(report.parent / 'metadata.json', meta)
    card = report.parent / 'card.md'
    card.write_text(tools.card_text(meta) + '\nWeights: {}. Nearest recipe: {}.\n'.format(
        result['summary']['assessment'], result['recipe_matching']['nearest_recipe']))
    fresh([report, card, report.parent / 'metadata.json'], float(os.environ['AUDIT_JOB_STARTED']))
    receipt = {'pair': number, 'measurement_sha256': checksum(report), 'card_sha256': checksum(card),
               'metadata_sha256': checksum(report.parent / 'metadata.json'),
               'deleted_checkpoints': [str(incoming), str(derived)],
               'shared_original': shares_original(number)}
    for directory in (incoming, derived):
        if directory.is_symlink() or not str(directory.resolve()).startswith(str(Path(os.environ['WORKDIR']).resolve()) + '/'):
            raise ValueError(fold('checkpoint cleanup path outside work:', str(directory)))
        shutil.rmtree(str(directory))
    write_json(report.parent / 'receipt.json', receipt)
    resaves = sum(change['class'] == RESAVE for change in differences)
    print('measurement passed: pair {}; metadata {}; re-save fields {}'.format(number, meta['verdict'], resaves))
    print('modified weights deleted; the original waits for the sweep', flush=True)
    return 0


def main():
    stub = os.environ.get('AUDIT_STUB') == '1' and os.environ.get('AUDIT_REHEARSAL') == '1'
    if sys.argv[1:] == ['--seed-original'] and stub:
        seed_original()
        return
    from census import pair, paths, verify
    number = int(os.environ['AUDIT_PAIR'])
    row = pair(number)
    original, incoming = paths(number)
    fresh(round_inputs(), float(os.environ['AUDIT_JOB_STARTED']))
    # One full checksum pass per download, here, before anything reads a tensor.
    verify(original, row['original'])
    verify(incoming, row['modified'])
    derived = Path(os.environ['AUDIT_DERIVED'])
    derived.mkdir(parents=True, exist_ok=True)
    # Reports from the last try are scratch too, even if its weights were removed.
    report = Path(os.environ['AUDIT_MEASUREMENT'])
    for name in ('metadata.json', 'card.md', 'receipt.json'):
        prior = report.parent / name
        if prior.exists():
            prior.unlink()
    for path in sorted(incoming.iterdir()):
        if path.is_file() and path.name != 'download-manifest.json':
            destination = derived / path.name
            os.link(str(path), str(destination))
            os.utime(str(destination), None)
    measurement([], compare)
    fresh([Path(os.environ['AUDIT_MEASUREMENT'])], float(os.environ['AUDIT_JOB_STARTED']))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as error:
        raise SystemExit(str(error))
