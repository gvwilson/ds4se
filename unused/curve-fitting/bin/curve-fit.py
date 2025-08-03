#!/usr/bin/env python

import sys
import argparse
import numpy as np
import pandas as pd
import scipy.optimize
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

    # read and slice
    data = pd.read_csv(args.input)
    slice = data[data.Interval <= (8 * 60 * 60)].drop(columns=['Date'])

    # fit exponential curves with binning and draw figures of low end
    curves = pd.DataFrame({'x': pd.Series(range(100))})
    for bins in range(100, 1100, 200):
        counts, edges = np.histogram(slice.Interval, bins=bins)
        params, covar = scipy.optimize.curve_fit(expo_decay, edges[:-1], counts)
        a, b, c = params
        print(f'with {bins:4} bins: y = {a:8} e**(-{b:8} x) + {c:8}')
        name = f'N{bins}'
        curves[name] = expo_decay(curves.x, a, b, c)
        fig = px.line(curves, x='x', y=name, log_y=True)
        fig.show()
        fig.write_image(f'{args.output}-{name}.svg')

    # now show the actual values in the low range
    exact = slice.Interval.astype(int)
    width = 100
    temp = exact[exact < width].value_counts().sort_index()
    fig = px.line(temp, x=temp.index, y='Interval', log_y=True)
    fig.show()
    fig.write_image(f'{args.output}-actual-{width}.svg')


def expo_decay(x, a, b, c):
    return a * np.exp(-b * x) + c


if __name__ == '__main__':
    main()
