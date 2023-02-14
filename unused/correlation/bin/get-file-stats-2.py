#!/usr/bin/env python

import sys
import argparse
from pydriller import RepositoryMining as RM
from pydriller.domain.commit import ModificationType as MT
import csv

from util import fmt_time


def main():
    '''
    Report commit details as CSV.
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', type=str,
                        help='repository directory')
    parser.add_argument('--branch', type=str, default='master',
                        help='repository branch (default master)')
    parser.add_argument('--output', type=str,
                        help='output file (default stdout)')
    parser.add_argument('--verbose', action='store_true',
                        help='display progress')
    args = parser.parse_args()

    writer = open(args.output, 'w') if args.output else sys.stdout
    writer = csv.writer(writer, lineterminator='\n')
    writer.writerow(['branch', 'hash', 'author', 'timestamp', 'old_path', 'new_path', 'change_type', 'added', 'removed'])

    types = {
        MT.ADD: 'add',
        MT.COPY: 'copy',
        MT.DELETE: 'delete',
        MT.MODIFY: 'modify',
        MT.RENAME: 'rename',
        MT.UNKNOWN: 'unknown'
    }

    for commit in RM(args.repo, only_in_branch=args.branch).traverse_commits():
        if args.verbose:
            print(f'...{commit.hash}', file=sys.stderr)
        for mod in commit.modifications:
            writer.writerow([args.branch, commit.hash, commit.author, commit.author_date,
                             mod.old_path, mod.new_path, types[mod.change_type],
                             mod.added, mod.removed])


if __name__ == '__main__':
    main()
