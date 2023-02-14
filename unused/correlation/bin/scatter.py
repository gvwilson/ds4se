#!/usr/bin/env python

import argparse
import pandas as pd
import plotly.express as px

def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='input file')
    parser.add_argument('--output', type=str, help='output file')
    parser.add_argument('--x', type=str, help='X axis column')
    parser.add_argument('--y', type=str, help='Y axis column')
    args = parser.parse_args()

    # calculate covariance matrix for selected columns
    data = pd.read_csv(args.input)
    fig = px.scatter(data, x=args.x, y=args.y, log_x=True, log_y=True)
    fig.write_image(args.output)


if __name__ == '__main__':
    main()
