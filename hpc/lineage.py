# lineage.py -- Hold unknown parents and screen the whole declared family tree.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  refuse a banned maker even when buried in a merge.
# Modified: SDE 2026-10-15  keep a refusal within 100 columns.
# Modified: SDE 2026-10-29  the guard travels as hashes; no maker name goes to a cluster.
import argparse
import hashlib
import json
from pathlib import Path
import re
import textwrap

LONGEST = 16  # the longest maker name the hashed guard can match


def load(banned):
    """The list of names at home, or the hashed guard that travels with a round."""
    entries = [line.strip().lower() for line in Path(banned).read_text().splitlines()
               if line.strip() and not line.lstrip().startswith('#')]
    hashed = bool(entries) and all(re.fullmatch('[0-9a-f]{64}', entry) for entry in entries)
    return entries, hashed


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def guard_text(banned):
    """One sha256 per lowercase maker name, sorted, with no name among them."""
    names, hashed = load(banned)
    if hashed or not names:
        raise ValueError('the guard is written from the list of names')
    for name in names:
        if len(name) > LONGEST:
            raise ValueError('maker name longer than {} characters: {}'.format(LONGEST, name))
    lines = ['# Maker guard: one sha256 per lowercase maker name; the names stay at home.']
    lines += sorted(digest(name) for name in names)
    return '\n'.join(lines) + '\n'


def match(value, entries, hashed):
    """A listed name anywhere inside the value; the hashed guard tries every short substring."""
    text = value.lower()
    if not hashed:
        return next((name for name in entries if name in text), None)
    table = set(entries)
    for length in range(1, LONGEST + 1):
        for start in range(len(text) - length + 1):
            found = digest(text[start:start + length])
            if found in table:
                return 'guard ' + found[:12]
    return None


def screen(manifest, banned):
    """The root name on a refusal is the copy somebody was about to download."""
    entries, hashed = load(banned)
    pairs = manifest.get('pairs', [])
    if not pairs or not entries:
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
            hit = match(value, entries, hashed)
            if hit and hashed:
                # on a cluster the refusal names no model, only the pair and the hash it met
                raise ValueError('banned lineage refused: pair {} ({})'.format(number, hit))
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

    for number, pair in enumerate(pairs, 1):
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
