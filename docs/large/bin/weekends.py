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
    parser.add_argument('--data', type=str, help='data file')
    args = parser.parse_args()
    
    # read and split data
    data = pd.read_csv(args.data)
    data.Date = pd.to_datetime(data.Date)
    data['Day'] = data.Date.dt.dayofweek
    is_weekday = (0 <= data.Day) & (data.Day <= 4)
    weekdays = data[is_weekday]
    weekends = data[~ is_weekday]

    # test and report
    print('weekday mean', weekdays.Hours.mean())
    print('weekend mean', weekends.Hours.mean())
    result = ttest_ind(weekdays.Hours, weekends.Hours)
    print(result)


if __name__ == '__main__':
    main()
