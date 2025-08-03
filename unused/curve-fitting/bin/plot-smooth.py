#!/usr/bin/env python

import sys
import argparse
import numpy as np
import pandas as pd
import plotly.express as px


def main():
    '''
    Main driver.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--bins', type=int, help='number of bins')
    parser.add_argument('--input', type=str, help='input file name')
    parser.add_argument('--width', type=int, help='window width (odd integer >= 3)')
    parser.add_argument('--max', type=float, help='upper bound on values (default is include all)')
    parser.add_argument('--output', type=str, help='output file name')
    parser.add_argument('--subtitle', type=str, help='subtitle')
    args = parser.parse_args()

    data = pd.read_csv(args.input).dropna()
    data = data[data.Functions > 0]
    values = data.Lines.divide(data.Functions)
    if args.max is not None:
        values = values[values <= args.max]
    binned = values.value_counts(bins=args.bins, normalize=True)

    window = np.ones(args.width) / args.width
    smoothed = np.convolve(window, binned)

    fig = px.line(x=range(1, len(smoothed)+1), y=smoothed,
                  labels={'x': 'Lines per Function',
                          'y': f'Smoothed Frequency (window {args.width})'},
                  width=600, height=400)
    fig.show()
    fig.write_image(args.output)


if __name__ == '__main__':
    main()
