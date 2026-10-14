# needs.py -- Read the space and time declared for a free round.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  reject incomplete or ambiguous declarations.
# Modified: SDE 2026-10-14  allow the census work budget of 8 TB.
import re


def parse_needs(text):
    """Accept five plain fields, with no shell punctuation hiding in them."""
    fields = {}
    for word in text.split():
        pair = word.split('=')
        if len(pair) != 2 or pair[0] in fields:
            raise ValueError('duplicate or malformed needs field')
        fields[pair[0]] = pair[1]
    if set(fields) != {'space', 'hours', 'subproject', 'queue', 'for'}:
        raise ValueError('needs requires space, hours, subproject, queue and for')
    match = re.fullmatch(r'([1-9][0-9]*)([KMGT])', fields['space'])
    if not match:
        raise ValueError('space needs a positive number and K, M, G or T')
    size = int(match.group(1)) * 1024 ** ('KMGT'.index(match.group(2)) + 1)
    if size > 8 * 1024 ** 4:
        raise ValueError('space exceeds the 8 TB work budget')
    if fields['hours'] != '0' or fields['queue'] != 'background':
        raise ValueError('this round uses background and hours=0')
    if not re.fullmatch(r'[A-Za-z0-9_-]+', fields['subproject']):
        raise ValueError('invalid subproject')
    match = re.fullmatch(r'([1-9][0-9]*)([mh])', fields['for'])
    if not match or int(match.group(1)) * (60 if match.group(2) == 'h' else 1) > 240:
        raise ValueError('duration must be at most 4h')
    return fields, size
