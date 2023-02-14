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
    parser.add_argument('--input', type=str, help='input file')
    parser.add_argument('--output', type=str, help='stem of output files')
    args = parser.parse_args()

    # read
    data = pd.read_csv(args.input)

    # all values
    fig = px.histogram(data, x='Interval', nbins=100, log_y=True)
    fig.show()
    fig.write_image(f'{args.output}-all.svg')

    # everything less than a week
    slice = data[data.Interval <= (7 * 24 * 60 * 60)]
    fig = px.histogram(slice, x='Interval', nbins=100, log_y=True)
    fig.show()
    fig.write_image(f'{args.output}-one-week.svg')

    # everything less than eight hours
    slice = data[data.Interval <= (8 * 60 * 60)]
    fig = px.histogram(slice, x='Interval', nbins=100, log_y=True)
    fig.show()
    fig.write_image(f'{args.output}-eight-hours.svg')


if __name__ == '__main__':
    main()
