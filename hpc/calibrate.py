# calibrate.py -- Apply a published recipe and record its measured fingerprint.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  preserve source dtypes and keep comparison verdicts as data.
# Modified: SDE 2026-10-14  share the text residual writer selection with index checks.
import hashlib
import json
import os
from pathlib import Path
import shutil
import statistics
import time

RECIPES = ('norm-preserving', 'single-projection')


def recipe_version(recipe):
    """Reject names that have no implementation in this piece."""
    if recipe not in RECIPES:
        raise ValueError('unsupported recipe: ' + str(recipe))
    return 'projection-then-row-rescale-v1' if recipe == 'norm-preserving' else '1'


def checksum(path):
    """Hash a file in blocks rather than keeping a shard in memory."""
    value = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            value.update(block)
    return value.hexdigest()


def identity(original, groups, recipe):
    """Bind the direction and copy to the source, prompts and recipe version."""
    version = recipe_version(recipe)
    manifest = json.loads((Path(original) / 'download-manifest.json').read_text())
    record = {'base': manifest['base'], 'base_revision': manifest['revision'],
              'recipe': recipe, 'recipe_version': version, 'version': version, 'prompts': groups,
              'source_sha256': {row['path']: row['sha256'] for row in manifest['files']}}
    record['fingerprint'] = hashlib.sha256(json.dumps(record, sort_keys=True).encode()).hexdigest()
    return record


def selects(name):
    """Select text attention outputs and feed-forward down projections."""
    from audit.weights import tensor_kind
    return ('vision' not in name and 'multi_modal_projector' not in name
            and tensor_kind(name) in ('attention_output', 'feed_forward_down'))


def transform(name, tensor, direction, recipe):
    """Project text residual writers in float32 and return the source dtype."""
    recipe_version(recipe)
    from audit.nulls import project_tensor
    if not selects(name):
        return tensor, False
    projected = project_tensor(tensor, direction.float())
    if recipe == 'norm-preserving':
        from audit.recipes.projection import restore_norms
        projected = restore_norms(tensor, projected)
    return projected.to(tensor.dtype), True


def write_derived(store, direction, destination, fingerprint, recipe):
    """Write one tensor per shard; untouched values keep their original bits."""
    recipe_version(recipe)
    from safetensors.torch import save_file
    from audit.weights import write_json
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    index, touched, total = {}, [], 0
    for number, name in enumerate(sorted(store.names)):
        tensor, changed = transform(name, store.get(name), direction, recipe)
        if changed:
            touched.append(name)
        shard = 'tensor-{:05d}.safetensors'.format(number)
        path = destination / shard
        total += tensor.numel() * tensor.element_size()
        temporary = str(path) + '.part'
        save_file({name: tensor.contiguous()}, temporary, metadata={'fingerprint': fingerprint, 'tensor': name})
        os.replace(temporary, str(path))
        del tensor
        index[name] = shard
    for path in store.directory.iterdir():
        if path.suffix == '.json' and path.name not in ('download-manifest.json', 'model.safetensors.index.json'):
            shutil.copyfile(str(path), str(destination / path.name))
        elif path.name == 'tokenizer.model':
            shutil.copyfile(str(path), str(destination / path.name))
    write_json(destination / 'model.safetensors.index.json', {'metadata': {'total_size': total}, 'weight_map': index})
    return touched


def span(values):
    """Keep missing measurements distinct from measured zeroes."""
    values = [value for value in values if value is not None]
    return {'min': min(values), 'median': statistics.median(values), 'max': max(values)} if values else {
        'min': None, 'median': None, 'max': None}


def fingerprint_card(report, recipe_card, extra):
    """Condense the saved comparison without replacing its measured assessment."""
    report = Path(report)
    measured = json.loads(report.read_text())
    if not isinstance(recipe_card, dict):
        recipe_card = json.loads(Path(recipe_card).read_text())
    rows = measured['tensors']
    summary, matching = measured['summary'], measured['recipe_matching']
    per_kind = {}
    for kind in sorted(set(row['kind'] for row in rows.values())):
        members = [row for row in rows.values() if row['kind'] == kind]
        changed = [row for row in members if row['changed']]
        norms = [row['row_norms'] for row in members if 'row_norms' in row]
        per_kind[kind] = {
            'count': len(members), 'changed': len(changed),
            'first_singular_energy_share': span([row.get('first_singular_energy_share') for row in changed]),
            'relative_difference': span([row.get('relative_difference') for row in members]),
            'row_norms_preserved': sum(bool(row['preserved_equal']) for row in norms),
            'row_norm_max_relative_error': max([row['max_relative_error'] for row in norms]) if norms else None}
    changed = [name for name, row in rows.items() if row['changed']]
    violations = matching['violations']
    return {'schema_version': 1, 'recipe': recipe_card['recipe'],
            'recipe_version': recipe_card['recipe_version'], 'base': recipe_card['base'],
            'base_revision': recipe_card['base_revision'],
            'measured_at': extra.get('measured_at', time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
            'report_sha256': checksum(report),
            'directions_sha256': checksum(report.parent / measured['directions_file']),
            'summary': {'assessment': summary['assessment'], 'nearest_recipe': matching['nearest_recipe'],
                        'violation_count': len(violations), 'violations': violations[:20],
                        'changed_tensors': len(changed), 'matched_tensors': summary['matched_tensors'],
                        'min_first_singular_energy_share': summary['min_first_singular_energy_share'],
                        'direction_min_cosine': summary['direction_agreement']['min_cosine']},
            'per_kind': per_kind,
            'changed_outside_recipe': sorted(set(changed) - set(recipe_card['tensors_touched'])),
            'note': 'one base, one run; a calibration point for the recipe-aware pass line, not a pass line'}


def measured_direction(original, groups, stage, fingerprint, store):
    """Use the same mean difference as round 1, or a seeded rehearsal vector."""
    import torch
    from safetensors import safe_open
    if os.environ.get('AUDIT_STUB') == '1' and os.environ.get('AUDIT_REHEARSAL') == '1':
        names = [name for name in store.names if name.endswith('embed_tokens.weight') and 'vision' not in name]
        if len(names) != 1:
            raise ValueError('cannot identify one text embedding')
        width = store.get(names[0]).shape[1]
        direction = torch.randn(width, generator=torch.Generator().manual_seed(0))
        middle = 'synthetic'
    else:
        from project import activations
        middle = activations(original, groups, stage, fingerprint, cpu=False)
        sums = {}
        for group in ('harmful', 'harmless'):
            vectors = []
            for index in range(32):
                path = stage / '{}-{:02d}.safetensors'.format(group, index)
                with safe_open(str(path), framework='pt') as saved:
                    if saved.metadata()['fingerprint'] != fingerprint:
                        raise ValueError('activation checkpoint differs')
                    vectors.append(saved.get_tensor('residual'))
            sums[group] = torch.stack(vectors).mean(0)
        direction = (sums['harmful'] - sums['harmless']).float()
    norm = direction.norm()
    if not torch.isfinite(direction).all() or norm == 0:
        raise ValueError('activation difference has no finite direction')
    return direction / norm, middle


def main(compare):
    """Measure, transform and compare; a scientific verdict is a successful run."""
    import torch
    from safetensors.torch import save_file
    from audit.nulls import prompts
    from audit.weights import TensorStore, write_json
    torch.set_num_threads(1)
    original, derived, work, report, card_path = [Path(os.environ[key]) for key in (
        'AUDIT_ORIGINAL', 'AUDIT_DERIVED', 'AUDIT_WORK', 'AUDIT_MEASUREMENT', 'AUDIT_CARD')]
    recipe = os.environ['AUDIT_RECIPE']
    stage = work / 'state/calibration'
    stage.mkdir(parents=True, exist_ok=True)
    groups = prompts(Path('data/prompts'))
    record = identity(original, groups, recipe)
    write_json(stage / 'context.json', record)
    store = TensorStore(original)
    direction, middle = measured_direction(original, groups, stage, record['fingerprint'], store)
    direction_path = stage / 'refusal-direction.safetensors'
    save_file({'refusal_direction': direction}, str(direction_path) + '.part')
    os.replace(str(direction_path) + '.part', str(direction_path))
    (work / 'state/calibrate-activations.done').write_text(record['fingerprint'] + '\n')
    touched = write_derived(store, direction, derived, record['fingerprint'], recipe)
    if not touched:
        raise ValueError('no text residual writers were projected')
    functions = ['audit.nulls.project_tensor']
    if recipe == 'norm-preserving':
        functions.append('audit.recipes.projection.restore_norms')
    recipe_card = dict(record, tensors_touched=touched, middle_layer=middle,
        token_position='last token of assistant prefix', library_functions=functions,
        precision={'weights': 'original tensor dtypes', 'projection': 'float32', 'activation_means': 'float64',
                   'forward': 'synthetic' if middle == 'synthetic' else 'bfloat16'},
        date=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    write_json(derived / 'recipe-card.json', recipe_card)
    (work / 'state/calibrate-transform.done').write_text(record['fingerprint'] + '\n')
    rc = compare(['compare-weights', '--modified', str(derived), '--original', str(original),
                  '--out', str(report), '--threads', '1'])
    if rc:
        raise SystemExit(rc)
    (work / 'state/calibrate-compare.done').write_text(record['fingerprint'] + '\n')
    card = fingerprint_card(report, recipe_card, {})
    write_json(card_path, card)
    for source, suffix in ((derived / 'recipe-card.json', '.recipe-card.json'),
                           (direction_path, '.direction.safetensors'), (stage / 'timing.json', '.timing.json')):
        if source.is_file():
            shutil.copyfile(str(source), str(report.parent / (recipe + suffix)))
    measured = json.loads(report.read_text())
    writers = [measured['tensors'][name] for name in touched]
    preserved = sum(bool(row.get('row_norms', {}).get('preserved_equal')) for row in writers)
    count = len(writers)
    summary = card['summary']
    print('fingerprint: {} on {}: {}; nearest {}; min energy share {}; row norms preserved {}/{} residual writers'.format(
        recipe, record['base'], summary['assessment'], summary['nearest_recipe'],
        summary['min_first_singular_energy_share'], preserved, count))
    (work / 'state/calibrate.done').write_text(record['fingerprint'] + '\n')
    print('Calibration complete: ' + str(card_path))
