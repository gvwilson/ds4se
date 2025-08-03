#!/usr/bin/env python

import sys
import argparse
import pandas as pd


def main():
    '''
    Select subset of data for testing purposes.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='input file')
    parser.add_argument('--output', type=str, help='output file')
    parser.add_argument('--seed', type=int, help='RNG seed')
    parser.add_argument('--number', type=int, help='number of rows')
    args = parser.parse_args()

    data = pd.read_csv(args.input)
    data = data.sample(n=args.number, random_state=args.seed)
    data.to_csv(args.output, header=True, index=False)


if __name__ == '__main__':
    main()
