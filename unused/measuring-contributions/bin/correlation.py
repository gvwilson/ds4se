#!/usr/bin/env python

import sys
import argparse
import csv
import numpy as np
import pandas as pd
import plotly.express as px


def main():
    '''
    Main driver.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--commits', type=str,
                        help='commits stem')
    parser.add_argument('--blame', type=str,
                        help='blame stem')
    parser.add_argument('--output', type=str,
                        help='output file (default stdout)')
    parser.add_argument('--figdir', type=str,
                        help='figure directory')
    parser.add_argument('stems', type=str, nargs='*')
    args = parser.parse_args()

    pearson = []
    spearman = []
    for stem in args.stems:
        left = pd.read_csv(f'{args.commits}-{stem}.csv', dtype={'commits': np.int32})
        right = pd.read_csv(f'{args.blame}-{stem}.csv', dtype={'lines': np.int32})
        join = left.set_index('email').join(right.set_index('email'), how='outer').fillna(value=0)
        fig = px.scatter(join, x='commits', y='lines', log_x=True, log_y=True)
        fig.write_image(f'{args.figdir}/commits-lines-{stem}.svg')
        pearson.append(join.corr(method='pearson')['commits']['lines'])
        spearman.append(join.corr(method='spearman')['commits']['lines'])

    result = pd.DataFrame({'stem': args.stems,
                           'pearson': pearson,
                           'spearman': spearman})
    output = args.output if args.output else sys.stdout
    result.to_csv(output, header=True, index=False)

    fig = px.scatter(result,
                     text='stem', x='pearson', y='spearman',
                     range_x=[0.0, 1.0], range_y=[-1.0, 1.0])
    fig.update_traces(textposition='middle right')
    fig.show()
    fig.write_image(f'{args.figdir}/correlation.svg')


if __name__ == '__main__':
    main()
