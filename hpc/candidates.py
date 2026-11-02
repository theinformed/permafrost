# candidates.py -- Read the hub inventory down to the copies worth staging.
# Created by SDE 2026-11-02
# Modified: SDE  a copy already used, a quantised or vision name, a banned maker or a missing parent is
#   dropped; the second-generation pool keeps community parents only.
import argparse
import json
from pathlib import Path
import sys
from huggingface_hub.utils import RepositoryNotFoundError

ROOT = Path(__file__).resolve().parent.parent
FAMILIES = ('gemma', 'mistral')
FINE_RELATIONS = ('finetune', 'base', None, 'adapter', 'merge')
NAME_FILTERS = ('gguf', 'mlx', '-vl-', 'awq', 'gptq', 'nvfp4', 'fp8', 'int4', 'int8', 'exl2')


def banned_names(path):
    """The maker names in the banned list, lowercased, with comments and blank lines dropped."""
    names = []
    for line in Path(path).read_text().splitlines():
        line = line.split('#', 1)[0].strip().lower()
        if line:
            names.append(line)
    return names


def family_of(text):
    """The family the lowercased text names, or None."""
    for family in FAMILIES:
        if family in text:
            return family
    return None


def parent_of(row):
    """The first fine-tune parent, else the card's base_model (first element if a list)."""
    bases = row.get('base_models') or []
    fine = [b['id'] for b in bases if b.get('relation') in FINE_RELATIONS]
    if fine:
        return fine[0]
    card = (row.get('card_data') or {}).get('base_model')
    if isinstance(card, list):
        card = card[0] if card else None
    return card


def scan(inventory_path, banned_path, used=(), second_generation=False):
    """The candidate rows: family, copy, parent, size_gb, downloads, parents."""
    banned = banned_names(banned_path)
    used = {name.lower() for name in used}
    rows = []
    for line in Path(inventory_path).read_text().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        copy = row['id']
        lower = copy.lower()
        if lower in used:
            continue
        if any(name in lower for name in NAME_FILTERS):
            continue
        files = row.get('files') or []
        weights = [f for f in files if f.get('format') == 'safetensors' or f['name'].endswith('.safetensors')]
        if not weights:
            continue
        bases = row.get('base_models') or []
        fine = [b['id'] for b in bases if b.get('relation') in FINE_RELATIONS]
        quant = [b['id'] for b in bases if b.get('relation') == 'quantized']
        if not fine and quant:
            continue
        parent = parent_of(row)
        if not parent:
            continue
        if second_generation and parent.lower().startswith('google/'):
            continue
        tags = row.get('tags') or []
        text = ' '.join([copy, parent] + list(tags)).lower()
        if any(name in text for name in banned):
            continue
        family = family_of(text)
        if family is None:
            continue
        rows.append({'family': family, 'copy': copy, 'parent': parent,
                     'size_gb': round(sum(f.get('size') or 0 for f in weights) / 1e9, 2),
                     'downloads': row.get('downloads_30d') or 0, 'parents': len(fine)})
    rows.sort(key=lambda r: (r['family'], -r['downloads']))
    return rows


def prune_missing(rows, api):
    """Split rows into those the hub still serves and those whose copy or parent it does not."""
    kept, missing = [], []
    for row in rows:
        reason = None
        for label, name in (('copy', row['copy']), ('parent', row['parent'])):
            try:
                api.model_info(name)
            except RepositoryNotFoundError:
                reason = '{} not found: {}'.format(label, name)
                break
        if reason:
            missing.append(dict(row, reason=reason))
        else:
            kept.append(row)
    return kept, missing


def write_tsv(rows, path):
    """Write the six columns, tab separated, no header."""
    text = ''.join('{}\t{}\t{}\t{}\t{}\t{}\n'.format(
        r['family'], r['copy'], r['parent'], r['size_gb'], r['downloads'], r['parents']) for r in rows)
    if path is None:
        sys.stdout.write(text)
    else:
        Path(path).write_text(text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inventory', default='data/inventory.jsonl')
    parser.add_argument('--banned', default='hpc/banned-makers.txt')
    parser.add_argument('--used', help='file of copy ids already used, one per line')
    parser.add_argument('--second-generation', action='store_true')
    parser.add_argument('--prune', action='store_true')
    parser.add_argument('--out', help='default stdout')
    args = parser.parse_args()
    used = []
    if args.used:
        used = [line.strip() for line in Path(args.used).read_text().splitlines() if line.strip()]
    rows = scan(args.inventory, args.banned, used=used, second_generation=args.second_generation)
    if args.prune:
        from huggingface_hub import HfApi
        rows, missing = prune_missing(rows, HfApi())
        for row in missing:
            print('missing: {} {}'.format(row['copy'], row['reason']), file=sys.stderr)
    write_tsv(rows, args.out)


if __name__ == '__main__':
    main()
