import sys
import argparse
import pandas as pd
import plotly.express as px

def main():
    '''
    Main driver.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, help='data file')
    parser.add_argument('--fig', type=str, help='figure file')
    parser.add_argument('--high', type=int, help='trim upper end of data')
    parser.add_argument('--low', type=int, help='trim lower end of data')
    parser.add_argument('--logx', action='store_true', help='use logarithmic X axis?')
    args = parser.parse_args()

    data = pd.read_csv(args.data).groupby(['Length']).sum().reset_index()
    if (args.high != None):
        data = data[data.Length <= args.high]
    if (args.low != None):
        data = data[data.Length >= args.low]
    max_y = max(data['Count']) * 1.2
    fig = px.scatter(data, x='Length', y='Count', log_x=args.logx, log_y=True,
                     range_y=[1, max_y], width=600, height=400)
    fig.write_image(args.fig)


if __name__ == '__main__':
    main()
