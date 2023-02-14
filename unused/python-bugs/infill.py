#!/usr/bin/env python

import sys
import math
import gzip
import yaml


CONVERT = {
    'nosy_count': int
}

TRANSLATE = {
    'components': 'component',
    'keywords': 'keyword',
    'type': 'issue_type'
}


def main():

    # Convert enumeration table to 1-based string lookup tables.
    with gzip.open(sys.argv[1], 'rb') as reader:
        enums = yaml.load(reader, Loader=yaml.FullLoader)
    for key in enums:
        enums[key] = {str(i+1):val
                      for (i, val) in enumerate(enums[key])}

    with gzip.open(sys.argv[2], 'rb') as reader:
        data = yaml.load(reader, Loader=yaml.FullLoader)
    for ident in data:
        record = data[ident]
        for key in record:
            # Change key to match enums.
            if key in TRANSLATE:
                record[TRANSLATE[key]] = record[key]
                del record[key]
            # Specific conversion.
            if key in CONVERT:
                record[key] = CONVERT[key](record[key])
            # Convert enumerations.
            elif key in enums:
                # Raw string.
                if type(record[key]) == str:
                    try:
                        record[key] = enums[key][record[key]]
                    except Exception as e:
                        print(f'ident {ident} record {record} key {key}:', file=sys.stderr)
                        print(str(e), file=sys.stderr)
                        record[key] = None
                # List of strings.
                elif type(record[key]) == list:
                    temp = []
                    for val in record[key]:
                        try:
                            temp.append(enums[key][val])
                        except Exception as e:
                            print(f'ident {ident} record {record} key {key}:', file=sys.stderr)
                            print(str(e), file=sys.stderr)
                            temp.append(None)
                    record[key] = temp

    with open(sys.argv[3], 'w') as writer:
        print(yaml.dump(data), file=writer)


if __name__ == '__main__':
    main()
