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
    args = parser.parse_args()

    # find inter-arrival times
    data = pd.read_csv(args.input)
    data.Timestamp = pd.to_datetime(data.Timestamp, utc=True)
    data = data.sort_values('Timestamp')
    data['Shift'] = data.Timestamp.shift(periods=1)
    data = data.dropna()
    data['Date'] = data.Timestamp.dt.date
    data['Interval'] = data.Timestamp.sub(data.Shift)
    data['Interval'] = data.Interval.dt.total_seconds().round(decimals=1)

    # write
    output = args.output if args.output else sys.stdout
    data[['Date', 'Interval']].to_csv(output, header=True, index=False)


if __name__ == '__main__':
    main()
