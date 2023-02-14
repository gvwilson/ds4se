#!/usr/bin/env python

import sys
import argparse
import os
import csv
from collections import Counter


def main():
    '''
    Main driver.
    '''
    args = parse_args()
    counts = lengths(args)
    report_filenames(args.output, counts)
    report_counts(args.output, counts)


def parse_args():
    '''
    Handle command-line arguments.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=str, help='root directory')
    parser.add_argument('--ext', type=str, help='extension')
    parser.add_argument('--output', type=str, help='stem of output files')
    return parser.parse_args()


def lengths(args):
    '''
    Find files and count line lengths.
    '''
    counts = {}
    for (curr_dir, sub_dirs, files) in os.walk(args.root):
        for filename in [x for x in files if x.endswith(args.ext)]:
            path = os.path.join(curr_dir, filename)
            with open(path, 'r') as reader:
                try:
                    counts[path] = Counter()
                    for x in reader.readlines():
                        counts[path][len(x)] += 1
                except Exception as e:
                     print(f'Failed to read {path}: {e}',
                           file=sys.stderr)
                     counts[path] = None
    return counts


def report_filenames(output_stem, counts):
    '''
    Report filename-to-ID as CSV with 'NA' for errored files.
    '''
    with open(f'{output_stem}-filenames.csv', 'w') as writer:
        writer = csv.writer(writer, lineterminator='\n')
        writer.writerow(['Filename', 'FileID'])
        for (file_id, filename) in enumerate(sorted(counts.keys())):
            writer.writerow([filename, file_id if counts[filename] else 'NA'])


def report_counts(output_stem, counts):
    '''
    Report file ID-to-count as CSV for non-errored files.
    '''
    with open(f'{output_stem}-counts.csv', 'w') as writer:
        writer = csv.writer(writer, lineterminator='\n')
        writer.writerow(['FileID', 'Length', 'Count'])
        for (file_id, filename) in enumerate(sorted(counts.keys())):
            if counts[filename]:
                for (length, freq) in counts[filename].most_common():
                    writer.writerow([file_id, length, freq])


if __name__ == '__main__':
    main()
