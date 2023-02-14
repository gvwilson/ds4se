#!/usr/bin/env python

import sys
import argparse
import os
import re
import csv

MAILBOX_SUFFIX = '.emlx'
TIMESTAMP_PATTERN = re.compile(r'^Date: (.+)$', re.MULTILINE)
ID_PATTERN = re.compile(r'^Message-Id:\s+<([^>]+)@([^@>]+)>', re.IGNORECASE + re.MULTILINE)


def main():
    '''
    Main driver.
    '''

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=str, help='root directory')
    parser.add_argument('--output', type=str, help='output file')
    parser.add_argument('--errors', type=str, help='error file')
    parser.add_argument('--obfuscate', type=str, help='hide paths and message IDs')
    parser.add_argument('--verbose', action='store_true', help='display progress')
    parser.add_argument('files', type=str, nargs='*')
    args = parser.parse_args()

    # setup
    args.count = 0
    args.seen = {}
    args.domains = {}
    args.message_ids = {}
    args.errors = open(args.errors, 'w') if args.errors else sys.stderr

    # extract message IDs, logging errors as we go
    if args.files:
        for filename in args.files:
            handle(args, filename)
    else:
        for (curr_dir, sub_dirs, files) in os.walk(args.root):
            for filename in [x for x in files if x.endswith(MAILBOX_SUFFIX)]:
                path = os.path.join(curr_dir, filename)
                handle(args, path)

    # record results
    writer = open(args.output, 'w') if args.output else sys.stdout
    writer = csv.writer(writer, lineterminator='\n')
    writer.writerow(['Domain', 'MessageId', 'Timestamp', 'Path'])
    for key in args.seen:
        for path in args.seen[key]:
            domain, message_id, timestamp = key
            writer.writerow([domain, message_id, timestamp, path])


def handle(args, path):
    '''
    Handle a single file.
    '''
    try:
        key = extract(args, path)
        if key is None:
            print(f'{path}: no info found', file=args.errors)
        else:
            path = obfuscate_path(args, path)
            if key in args.seen:
                args.seen[key].append(path)
            else:
                args.seen[key] = [path]
    except UnicodeDecodeError as e:
        print(f'{path}: {e}', file=args.errors)
    report_progress(args)


def extract(args, path):
    '''
    Get message ID and date from file.
    '''
    result = None
    with open(path, 'r') as reader:
        data = reader.read()
        full_id = ID_PATTERN.search(data)
        timestamp = TIMESTAMP_PATTERN.search(data)
        if full_id and timestamp:
            message_id = obfuscate_message_id(args, full_id.group(1))
            domain = obfuscate_domain(args, full_id.group(2))
            timestamp = clean_timestamp(timestamp.group(1))
            result = (domain, message_id, timestamp)
    return result


def obfuscate_message_id(args, message_id):
    '''
    Hide the message ID.
    '''
    result = message_id
    if args.obfuscate:
        if message_id not in args.message_ids:
            args.message_ids[message_id] = len(args.message_ids)
        result = args.message_ids[message_id]
    return result


def obfuscate_domain(args, domain):
    '''
    Hide the domain name.
    '''
    result = domain
    if args.obfuscate:
        if domain not in args.domains:
            args.domains[domain] = len(args.domains)
        result = args.domains[domain]
    return result


def obfuscate_path(args, path):
    '''
    Remove prefix from path.
    '''
    if args.obfuscate:
        assert path.startswith(args.obfuscate), \
            f'Path {path} does not start with prefix {args.obfuscate}'
        path = path[len(args.obfuscate):]
    return path


def clean_timestamp(ts):
    '''
    Clean up the timestamp by removing parenthesized timezone names and commas.
    '''
    return ts.split('(')[0].strip().replace(',', '')


def report_progress(args):
    '''
    Report progress.
    '''
    args.count += 1
    if args.verbose and ((args.count % 1000) == 0):
        print(args.count, file=sys.stderr)


if __name__ == '__main__':
    main()
