# say.py -- Fold a message to 100 columns: what happened, where, why, then any error text.
# Created by Sean Egan 2026-10-15
import textwrap

WIDTH = 100


def fold(what, where=None, why=None, detail=None, width=WIDTH):
    """Each part starts its own line; long paths and error text wrap instead of running off."""
    lines = []
    for text, indent in ((what, ''), (where, '  '), (why, '  '), (detail, '    ')):
        if not text:
            continue
        for line in str(text).splitlines() or ['']:
            lines += textwrap.wrap(line, width, initial_indent=indent, subsequent_indent=indent + '  ',
                                   break_long_words=True, break_on_hyphens=False) or [indent]
    return '\n'.join(lines)


if __name__ == '__main__':
    import sys
    print(fold(*sys.argv[1:5]))
