#!/usr/bin/env python

import sys
import argparse
import numpy as np
import pandas as pd


def main():
    '''
    Sample two datasets to calculate odds of means being distant.
    '''

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--left', type=str, help='first dataset')
    parser.add_argument('--right', type=str, help='second dataset')
    parser.add_argument('--low', type=int, help='lower limit')
    parser.add_argument('--high', type=int, help='upper limit')
    parser.add_argument('--trials', type=int, help='number of trials (>0)')
    parser.add_argument('--seed', type=int, help='RNG seed')
    args = parser.parse_args()
    np.random.seed(args.seed)

    # read data and calculate actual means and difference
    data_left = read_data(args.left, args.low, args.high)
    data_right = read_data(args.right, args.low, args.high)
    mean_left = data_left.mean()
    mean_right = data_right.mean()
    actual_diff = mean_left - mean_right

    # repeatedly sample and calculate difference
    combined = data_left.append(data_right).reset_index(drop=True)
    split = len(data_left)
    sample_diffs = []
    for t in range(args.trials):
        print(t)
        shuffle = np.random.permutation(len(combined))
        sample_left = combined[shuffle[:split]]
        sample_right = combined[shuffle[split:]]
        sample_diffs.append(sample_left.mean() - sample_right.mean())

    sample_diff_mean = sum(sample_diffs) / args.trials
    success_frac = sum([x <= actual_diff for x in sample_diffs]) / args.trials

    # report
    print(f'parameters:')
    print(f'- left: "{args.left}"')
    print(f'- right: "{args.right}"')
    print(f'- low: {"null" if (args.low is None) else args.low}')
    print(f'- high: {"null" if (args.high is None) else args.high}')
    print(f'- trials: {args.trials}')
    print(f'- seed: {args.seed}')
    print(f'results:')
    print(f'- mean_left: {mean_left}')
    print(f'- mean_right: {mean_right}')
    print(f'- actual_diff: {actual_diff}')
    print(f'- sample_diff: {sample_diff_mean}')
    print(f'- successes: {success_frac}')


def read_data(filename, low, high):
    '''
    Read data and remove lines of length 1 and very long lines.
    '''
    data = pd.read_csv(filename)
    if (high != None):
        data = data[data.Length <= high]
    if (low != None):
        data = data[data.Length >= low]
    return data.Length.repeat(repeats=data.Count)


if __name__ == '__main__':
    main()
