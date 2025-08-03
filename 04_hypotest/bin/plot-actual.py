#!/usr/bin/env python

import sys
import argparse
import pandas as pd
import plotly.express as px


def main():
    '''
    Main driver.
    '''

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, help='data file')
    parser.add_argument('--save', type=str, help='save figure as')
    args = parser.parse_args()

    # read and classify data
    data = pd.read_csv(args.data)
    data.Date = pd.to_datetime(data.Date)
    data['Day'] = data.Date.dt.dayofweek
    data['Weekday'] = (0 <= data.Day) & (data.Day <= 4)
    
    # plot
    fig = px.violin(data, y='Hours', x='Weekday', box=True)
    fig.show()
    fig.write_image(args.save)


if __name__ == '__main__':
    main()
