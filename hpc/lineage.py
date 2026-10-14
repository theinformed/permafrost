# lineage.py -- Hold unknown parents and screen the whole declared family tree.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  refuse a banned maker even when buried in a merge.
# Modified: SDE 2026-10-15  keep a refusal within 100 columns.
import argparse
import json
from pathlib import Path
import textwrap


def screen(manifest, banned):
    """The root name on a refusal is the copy somebody was about to download."""
    names = [line.strip().lower() for line in Path(banned).read_text().splitlines()
             if line.strip() and not line.lstrip().startswith('#')]
    pairs = manifest.get('pairs', [])
    if not pairs or not names:
        raise ValueError('empty census or maker list')

    def visit(node, model, copy=False):
        if not isinstance(node, dict):
            raise ValueError('unknown base held: ' + model)
        identity = node.get('hub_id', '')
        maker = node.get('maker', '')
        declaration = node.get('declared_base_model')
        bases = declaration if isinstance(declaration, list) else [declaration] if declaration else []
        for value in [identity, maker] + bases:
            if not isinstance(value, str):
                raise ValueError('unknown base held: ' + model)
            hit = next((name for name in names if name in value.lower()), None)
            if hit:
                raise ValueError('banned lineage refused: {} ({}, {})'.format(model, value, hit))
        chain = node.get('base_model_chain')
        if not identity or not maker or node.get('lineage_known') is not True or not isinstance(chain, list):
            raise ValueError('unknown base held: ' + model)
        if copy and not bases:
            raise ValueError('unknown base held: ' + model)
        if sorted(bases) != sorted(child.get('hub_id', '') for child in chain):
            raise ValueError('incomplete base chain held: ' + model)
        if not chain and node.get('publisher_root') is not True:
            raise ValueError('unknown base held: ' + model)
        for child in chain:
            visit(child, model)

    for pair in pairs:
        model = pair.get('modified', {}).get('hub_id', '<unnamed>')
        visit(pair.get('modified'), model, copy=True)
        visit(pair.get('original'), model)
    return len(pairs)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('manifest')
    parser.add_argument('banned')
    args = parser.parse_args()
    try:
        count = screen(json.loads(Path(args.manifest).read_text()), args.banned)
    except (ValueError, KeyError, OSError) as error:
        text = str(error).replace(': ', ':\n', 1)
        lines = [part for line in text.splitlines() for part in textwrap.wrap(
            line, 100, subsequent_indent='  ', break_long_words=True, break_on_hyphens=False)]
        parser.exit(1, '\n'.join(lines) + '\n')
    print('Lineage passed: {} pairs'.format(count))


if __name__ == '__main__':
    main()
