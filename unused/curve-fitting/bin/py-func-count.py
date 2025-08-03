#!/usr/bin/env python

import sys
import argparse
import ast
import csv


def main():
    '''
    Main driver.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true', help='read list of filenames from standard input')
    parser.add_argument('--output', type=str, help='output file')
    parser.add_argument('--verbose', action='store_true', help='show progress')
    parser.add_argument('files', type=str, nargs='*')
    args = parser.parse_args()

    if (args.list and args.files):
        print('Cannot use both --list and list of files', file=sys.stderr)
        sys.exit(1)
    elif args.list:
        results = [handle(filename.strip(), args.verbose) for filename in sys.stdin]
    elif args.files:
        results = [handle(filename, args.verbose) for filename in args.files]
    else:
        print('Must use either --list or a list of files', file=sys.stderr)
        sys.exit(1)

    stream = open(args.output, 'w') if args.output else sys.stdout
    writer = csv.writer(stream, lineterminator='\n')
    writer.writerow(['Path', 'Lines', 'Functions'])
    for entry in results:
        writer.writerow(entry)


def handle(path, verbose):
    '''
    Analyze a single file.
    '''
    if verbose:
        print(path, file=sys.stderr)
    with open(path, 'r') as reader:
        try:
            data = reader.read()
            lines = len(data.rstrip().split('\n'))
            tree = ast.parse(data)
            analyzer = Analyzer()
            analyzer.visit(tree)
            result = (path, lines, analyzer.num_functions)
        except UnicodeDecodeError as e:
            result = (path, None, None)
        except SyntaxError as e:
            result = (path, lines, None)
        return result


class Analyzer(ast.NodeVisitor):
    '''
    Count the number of function nodes in a parse tree.
    '''

    def __init__(self):
        self.num_functions = 0


    def visit_FunctionDef(self, node):
        self.num_functions += 1
        self.generic_visit(node)


if __name__ == '__main__':
    main()
