# pin_census.py -- Record public lineage and the original available at creation.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  keep dates and full revisions beside each pair.
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
from huggingface_hub import HfApi


def declared(info):
    """Keep the card's declaration, including a list used for merges."""
    card = info.card_data.to_dict() if info.card_data else {}
    return card.get('base_model')


def pin(api, modified, original):
    """Choose the newest original commit no later than the copy's creation."""
    copy = api.model_info(modified)
    copy_history = api.list_repo_commits(modified)
    copy_commit = next(row for row in copy_history if row.commit_id == copy.sha)
    history = api.list_repo_commits(original)
    eligible = [row for row in history if row.created_at <= copy.created_at]
    if not eligible:
        raise ValueError('no original revision predates creation: ' + modified)
    commit = max(eligible, key=lambda row: row.created_at)
    seen = set()

    def lineage(repo, revision, root=False):
        """Follow every declared parent; a missing declaration on a copy is held."""
        if (repo, revision) in seen:
            raise ValueError('lineage cycle: ' + repo)
        seen.add((repo, revision))
        info = api.model_info(repo, revision=revision)
        bases = declared(info)
        names = bases if isinstance(bases, list) else [bases] if bases else []
        nodes = []
        for name in names:
            if not isinstance(name, str) or '/' not in name:
                raise ValueError('unknown base declaration: ' + repo)
            parent = api.model_info(name)
            nodes.append(lineage(name, parent.sha))
        seen.remove((repo, revision))
        return {'hub_id': repo, 'maker': repo.split('/')[0].lower(), 'revision': info.sha,
                'declared_base_model': bases, 'base_model_chain': nodes,
                'lineage_known': bool(nodes) or (not root and repo.split('/')[0] == original.split('/')[0]),
                'publisher_root': not names and not root and repo.split('/')[0] == original.split('/')[0],
                'created_at': info.created_at.isoformat()}

    node = lineage(modified, copy.sha, root=True)
    if not node['base_model_chain']:
        raise ValueError('modified base unknown: ' + modified)
    node['revision_date'] = copy_commit.created_at.isoformat()
    base = lineage(original, commit.commit_id)
    base['revision_date'] = commit.created_at.isoformat()
    return {'modified': node, 'original': base,
        'original_selection': {'cutoff': copy.created_at.isoformat(),
            'rule': 'latest commit at or before modified repository creation',
            'history_commits_read': len(history)}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('manifest')
    parser.add_argument('--pair', nargs=2, required=True)
    args = parser.parse_args()
    path = Path(args.manifest)
    record = json.loads(path.read_text()) if path.exists() else {'round': 2, 'batch': 1, 'pairs': []}
    if any(row['modified']['hub_id'] == args.pair[0] for row in record['pairs']):
        raise ValueError('pair already pinned: ' + args.pair[0])
    record['pairs'].append(pin(HfApi(), *args.pair))
    record['pinned_at'] = datetime.now(timezone.utc).isoformat()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2) + '\n')


if __name__ == '__main__':
    main()
