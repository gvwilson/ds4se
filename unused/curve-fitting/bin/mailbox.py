#!/usr/bin/env python

import sys
import argparse
import os
import re
from dateutil.parser import parse
import csv


MAILBOX_SUFFIX = '.emlx'
TIMESTAMP_PATTERN = re.compile(r'^Date: (.+)$')


def main():
    '''
    Main driver.
    '''

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=str, help='root directory')
    parser.add_argument('--output', type=str, help='output file')
    args = parser.parse_args()

    # extract dates
    timestamps = []
    bad_files = []
    for (curr_dir, sub_dirs, files) in os.walk(args.root):
        for filename in [x for x in files if x.endswith(MAILBOX_SUFFIX)]:
            path = os.path.join(curr_dir, filename)
            try:
                timestamps.append(get_timestamp(path))
            except Exception as e:
                bad_files.append(path)

    # report timestamps
    writer = sys.stdout
    if (args.output):
        writer = open(args.output, 'w')
    writer = csv.writer(writer, lineterminator='\n')
    writer.writerow(['Timestamp'])
    for d in sorted(timestamps):
        writer.writerow([d])

    # report bad files
    print(f'{len(bad_files)} bad files / {len(bad_files) + len(timestamps)} files',
          file=sys.stderr)


def get_timestamp(path):
    '''
    Get datetime from message.
    '''
    with open(path, 'r') as reader:
        for line in reader:
            match = TIMESTAMP_PATTERN.search(line)
            if match:
                return parse(match.group(1))
    raise ValueError(f'no date found in {path}')


if __name__ == '__main__':
    main()
