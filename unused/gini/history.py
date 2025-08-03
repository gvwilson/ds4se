#!/usr/bin/env python

import sys
import argparse
import numpy as np
import pandas as pd
import csv

from util import gini


def main():
    '''
    Main driver.
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=str,
                        help='output file (default stdout)')
    parser.add_argument('files', type=str, nargs='*')
    args = parser.parse_args()

    writer = open(args.output, 'w') if args.output else sys.stdout
    writer = csv.writer(writer, lineterminator='\n')
    writer.writerow(['filename', 'gini_commits', 'gini_lines'])

    for filename in args.files:
        data = pd.read_csv(filename)
        data['lines'] = data['insertions'] - data['deletions']
        commits = data[['hash', 'email']]\
            .drop_duplicates()\
            .groupby('email')\
            .email.count()
        lines = data.groupby('email')\
                    .lines.sum()
        writer.writerow([filename, gini(commits), gini(lines)])


if __name__ == '__main__':
    main()
