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
    writer.writerow(['filename', 'gini_blame'])

    for filename in args.files:
        data = pd.read_csv(filename)
        counts = data.groupby('email').lines.sum()
        writer.writerow([filename, gini(counts)])


if __name__ == '__main__':
    main()
