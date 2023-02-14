#!/usr/bin/env python

import sys
import pandas as pd


def main():
    '''
    Main driver.
    '''
    left_pattern = sys.argv[1]
    right_pattern = sys.argv[2]
    print(f'stem,{left_pattern},both,{right_pattern}')
    for stem in sys.argv[3:]:
        left_file = left_pattern.replace('%', stem)
        right_file = right_pattern.replace('%', stem)

        left_data = pd.read_csv(left_file)
        left_addr = set(left_data.email)

        right_data = pd.read_csv(right_file)
        right_addr = set(right_data.email)

        left_only = left_addr - right_addr
        right_only = right_addr - left_addr
        both = left_addr & right_addr
        print(f'{stem},{len(left_only)},{len(both)},{len(right_only)}')


if __name__ == '__main__':
    main()
