#!/usr/bin/env python

import sys
import argparse
import pandas as pd


def main():
    '''
    Main driver.
    '''

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='input file')
    parser.add_argument('--output', type=str, help='output file')
    parser.add_argument('--logfile', type=str, help='log file')
    args = parser.parse_args()
    logfile = open(args.logfile, 'w') if args.logfile else sys.stderr

    # get and filter
    data = pd.read_csv(args.input)
    print(f'{len(data)} records', file=logfile)
    data = data.drop_duplicates(subset=['Domain', 'MessageId', 'Timestamp'])
    print(f'{len(data)} after removing duplicates', file=logfile)
    data = data[~ data.Path.str.contains('Recovered')]
    print(f'{len(data)} after removing "Recovered"', file=logfile)
    data = data[~ data.Path.str.contains('partial')]
    print(f'{len(data)} after removing "partial"', file=logfile)

    # save
    if args.output:
        with open(args.output, 'w') as writer:
            data.to_csv(writer, header=True, index=False)


if __name__ == '__main__':
    main()
