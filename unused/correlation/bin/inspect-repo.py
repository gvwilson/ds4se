#!/usr/bin/env python

import sys
from collections import Counter
from git import Repo

from util import fmt_time


REMOTE = '''\
  - name: "{remote}"
    url: "{remote.url}"\
'''

BRANCH = '''\
  - name: "{branch}"
    hash: "{branch.commit}"
    author: "{branch.commit.author}"
    committer: "{branch.commit.committer}"
    committed: "{branch.commit.committed_datetime}"\
'''

COMMIT='''\
  - hash: "{hash}"
    author: "{author}"
    committed: {time}"
    blob: {blob}
    tree: {tree}\
'''


def main():
    '''
    Show a few things about a repository.
    '''
    repo = Repo(sys.argv[1])

    print('- remotes:')
    for remote in repo.remotes:
        print(REMOTE.format(remote=remote))

    print('- branches:')
    for branch in repo.heads:
        print(BRANCH.format(branch=branch))

    print('- master_commits:')
    for commit in repo.iter_commits('master'):
        info = commit_info(commit)
        print(COMMIT.format(hash=str(commit),
                            author=commit.author.name,
                            time=fmt_time(commit.committed_date),
                            blob=info['blob'],
                            tree=info['tree']))


def commit_info(commit):
    c = Counter()
    for item in commit.tree.traverse():
        c[item.type] += 1
    return c


if __name__ == '__main__':
    main()
