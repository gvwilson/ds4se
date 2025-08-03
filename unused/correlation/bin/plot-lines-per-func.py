#!/usr/bin/env python

import sys
import argparse
import pandas as pd
import plotly.express as px


def main():
    '''
    Main driver.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--bins', type=int, help='number of bins')
    parser.add_argument('--input', type=str, help='input file name')
    parser.add_argument('--max', type=float, help='upper bound on values (default is include all)')
    parser.add_argument('--output', type=str, help='output file name')
    parser.add_argument('--subtitle', type=str, help='subtitle')
    args = parser.parse_args()

    data = pd.read_csv(args.input).dropna()
    data['Ratio'] = data.Lines.divide(data.Functions)
    if args.max is not None:
        data = data[data.Ratio <= args.max]
    fig = px.histogram(data, x='Ratio', nbins=args.bins, log_y=True,
                       labels={'Ratio': f'Lines per Function ({args.subtitle})'},
                       width=600, height=400)
    fig.write_image(args.output)


if __name__ == '__main__':
    main()
