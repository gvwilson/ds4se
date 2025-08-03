#!/usr/bin/env python

import sys
import argparse
import pandas as pd


def main():
    '''
    Main driver.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str,
                        help='input file (default stdin)')
    parser.add_argument('--output', type=str,
                        help='output file (default stdout)')
    args = parser.parse_args()

    source = args.input if args.input else sys.stdin
    data = pd.read_csv(source)
    commits = data[['email', 'hash']]\
        .drop_duplicates()\
        .email.value_counts()\
        .to_frame()\
        .rename(columns={'email': 'commits'})

    output = args.output if args.output else sys.stdout
    commits.to_csv(output, header=True, index_label='email')


if __name__ == '__main__':
    main()
