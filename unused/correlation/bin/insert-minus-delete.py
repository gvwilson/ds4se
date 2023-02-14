#!/usr/bin/env python

import sys
import argparse
import pandas as pd
import csv


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
    writer.writerow(['filename', 'total'])

    for filename in args.files:
        df = pd.read_csv(filename)
        total = df.insertions.sum() - df.deletions.sum()
        writer.writerow([filename, total])


if __name__ == '__main__':
    main()
