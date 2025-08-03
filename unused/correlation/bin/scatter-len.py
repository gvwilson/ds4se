#!/usr/bin/env python

import argparse
import pandas as pd
import plotly.express as px

def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='input file')
    parser.add_argument('--output', type=str, help='output file')
    args = parser.parse_args()

    # calculate covariance matrix for selected columns
    data = pd.read_csv(args.input)
    data['Len'] = data.Name.str.len()
    fig = px.scatter(data, x='Len', y='Lines', log_x=True, log_y=True)
    fig.write_image(args.output)
    corr = data[['Len', 'Lines']].corr()
    print(corr)


if __name__ == '__main__':
    main()
