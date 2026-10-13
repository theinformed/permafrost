#!/bin/bash
# ============================================================================
# commit_as_sean.sh -- commit the named files with the project's author details.
# Created by LT Sean Egan, PhD                                       2026-10-08
# Purpose: lint the message and sources without sweeping in somebody else's edits.
# Modified: SDE 2026-10-08  use a temporary index for the selected paths.
# Modified: SDE 2026-10-08  skip data files in the comment check.
# Modified: SDE 2026-10-08  skip CSV observation fixtures in the comment check.
# Modified: SDE 2026-10-08  check dated Markdown as prose and skip saved responses.
# Modified: SDE 2026-10-08  skip Markdown files in the comment check.
# Modified: SDE 2026-10-12  verify the current author and committer before committing.
# Modified: SDE 2026-10-13  sign Permafrost as Sean Egan; this is personal work, not duty.  verify the current author and committer before committing.
# Modified: SDE 2026-10-13  start an empty repository and keep the index here.
# ============================================================================
set -euo pipefail
if [[ $# -lt 2 ]]; then
    echo 'Usage: commit_as_sean.sh MESSAGE_FILE PATH ...' >&2
    exit 2
fi
message=$1
shift
lint=/root/docs/reference/style/code-lint.py
python3 "$lint" --message "$message"
mkdir -p .tmp
index_file=$(mktemp "$PWD/.tmp/commit-index.XXXXXX")
rm "$index_file"
trap 'rm -f "$index_file"' EXIT
export GIT_INDEX_FILE=$index_file
if git rev-parse --verify HEAD >/dev/null 2>&1; then
    git read-tree HEAD
else
    git read-tree --empty
fi
git add -- "$@"
while IFS= read -r -d '' file; do
    # JSON records carry forecast dates as data.
    # CSV fixtures also carry report timestamps as data.
    # Source dates are part of a README; provider replies are test data.
    case "$file" in
        *.json|*.jsonl|*/tests/fixtures/*) continue ;;
        *.md) bash /root/docs/reference/style/ship-check.sh "$file" ;;
        *) python3 "$lint" "$file" ;;
    esac
done < <(git diff --cached --name-only --diff-filter=ACM -z)
export GIT_AUTHOR_NAME='Sean Egan'
export GIT_AUTHOR_EMAIL=sean@theinformed.org
export GIT_COMMITTER_NAME='Sean Egan'
export GIT_COMMITTER_EMAIL=sean@theinformed.org
author=$(git var GIT_AUTHOR_IDENT)
committer=$(git var GIT_COMMITTER_IDENT)
[[ "$author" == "$GIT_AUTHOR_NAME <$GIT_AUTHOR_EMAIL> "* ]]
[[ "$committer" == "$GIT_COMMITTER_NAME <$GIT_COMMITTER_EMAIL> "* ]]
printf '%s\n%s\n' "$author" "$committer"
git commit -F "$message"
unset GIT_INDEX_FILE
# Refresh only the paths just committed; other staged work belongs to its owner.
git reset -q HEAD -- "$@"
