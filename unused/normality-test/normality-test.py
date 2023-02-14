#!/usr/bin/env python

import sys
import argparse
import pandas as pd
from scipy.stats import normaltest


def main():
    '''
    Main driver.
    '''

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, help='data file')
    args = parser.parse_args()

    # read and classify data
    data = pd.read_csv(args.data)
    data.Date = pd.to_datetime(data.Date)
    data['Day'] = data.Date.dt.dayofweek
    is_weekday = (0 <= data.Day) & (data.Day <= 4)
    weekdays = data[is_weekday]
    weekends = data[~ is_weekday]
    
    # plot
    for (name, values) in (('all', data),
                           ('weekdays', weekdays),
                           ('weekends', weekends)):
        result = normaltest(values.Hours)
        print(name, result)


if __name__ == '__main__':
    main()
