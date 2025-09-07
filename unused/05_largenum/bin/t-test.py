#!/usr/bin/env python

import sys
import argparse
import pandas as pd
from scipy.stats import ttest_ind

def main():
    '''
    Main driver.
    '''

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--left', type=str, help='first dataset')
    parser.add_argument('--right', type=str, help='second dataset')
    parser.add_argument('--low', type=int, help='lower limit')
    parser.add_argument('--high', type=int, help='upper limit')
    args = parser.parse_args()
    
    # read datasets
    data_left = read_data(args.left, args.low, args.high)
    data_right = read_data(args.right, args.low, args.high)

    # test and report
    result = ttest_ind(data_left, data_right)
    print(result)


def read_data(filename, low, high):
    '''
    Read data and remove line length = 1.
    '''
    data = pd.read_csv(filename)
    if (high != None):
        data = data[data.Length <= high]
    if (low != None):
        data = data[data.Length >= low]
    return data.Length.repeat(repeats=data.Count)


if __name__ == '__main__':
    main()
