#!/usr/bin/env python

import sys
import argparse
import os
import re
from collections import Counter
import csv

from util import include


EMAIL_PAT = re.compile(r'^.*?<(.+?)>')


def main():
    '''
    Main driver.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', type=str,
                        help='repository directory')
    parser.add_argument('--output', type=str,
                        help='output file (default stdout)')
    parser.add_argument('--verbose', action='store_true',
                        help='report progress')
    args = parser.parse_args()

    count = Counter()
    for root, dirs, files in os.walk(args.repo):
        for path in [os.path.join(root, f) for f in files]:
            if not include(path):
                continue
            if args.verbose:
                print(path, file=sys.stderr)
            try:
                cmd = f'git -C {args.repo} blame -e {path}'
                lines = os.popen(cmd).readlines()
                emails = [EMAIL_PAT.search(x).group(1) for x in lines]
                for e in emails:
                    count[e] += 1
            except Exception as e:
                if args.verbose:
                    print(f'error in {path}: {e}', file=sys.stderr)

    writer = open(args.output, 'w') if args.output else sys.stdout
    writer = csv.writer(writer, lineterminator='\n')
    writer.writerow(['email', 'lines'])
    for key in count:
        writer.writerow([key, count[key]])


if __name__ == '__main__':
    main()
