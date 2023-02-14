#!/usr/bin/env python

import sys
import argparse
from git import Repo
import csv

from util import fmt_time


DETAILS = 'insertions deletions lines'.split()
TITLES = 'branch hash email timestamp path'.split() + DETAILS


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
    parser.add_argument('--commit', type=str,
                        help='where to start recording (default all)')
    args = parser.parse_args()

    writer = open(args.output, 'w') if args.output else sys.stdout
    writer = csv.writer(writer, lineterminator='\n')
    writer.writerow(TITLES)

    recording = (args.commit == None)
    repo = Repo(args.repo)
    for commit in repo.iter_commits(args.branch):
        if args.verbose:
            flag = '+' if recording else '-'
            print(f'{flag}{commit.hexsha}', file=sys.stderr)
        if not recording:
            if commit.hexsha == args.commit:
                recording = True
            else:
                continue
        for path in commit.stats.files:
            info = [args.branch, commit.hexsha, commit.author.email, fmt_time(commit.authored_date), path]
            details = [commit.stats.files[path][k] for k in DETAILS]
            writer.writerow(info + details)


if __name__ == '__main__':
    main()
