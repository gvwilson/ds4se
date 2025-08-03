#!/usr/bin/env python

import argparse
import pandas as pd


def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', type=str, help='title of output')
    parser.add_argument('--input', type=str, help='input file')
    parser.add_argument('columns', type=str, nargs='*')
    args = parser.parse_args()

    # calculate covariance matrix for selected columns
    data = pd.read_csv(args.input)
    data = data[args.columns]
    corr = data.corr()
    print(args.title)
    print(corr)

if __name__ == '__main__':
    main()
