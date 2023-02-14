#!/usr/bin/env python

# See http://roundup.sourceforge.net/docs/xmlrpc.html for documentation.

import sys
import yaml
import xmlrpc.client
from datetime import datetime


def get_enums(client):
    data = {}
    for key in ['issue_type', 'status', 'component', 'version', 'severity',
                'priority', 'stage', 'status', 'resolution', 'keyword']:
        print(f'requesting {key}', file=sys.stderr)
        data[key] = client.list(key)
    return data


def get_all(client, ident):
    data = [f'{ident}{i}' for i in client.list(ident, 'id')]
    result = {}
    start = datetime.now()
    for (i, key) in enumerate(data):
        elapsed = datetime.now() - start
        expected = elapsed * len(data) / (i+1)
        print(f'requesting {key} ({i+1} / {len(data)}) ({elapsed} / {expected})', file=sys.stderr)
        try:
            result[key] = client.display(key)
        except Exception as e:
            print(f'ERROR for {key}: {e}', file=sys.stderr)
            result[key] = None
    return result


def main():
    client = xmlrpc.client.ServerProxy("https://bugs.python.org/xmlrpc")
    with open('enums.yml', 'w') as writer:
        print(yaml.dump(get_enums(client)), file=writer)

    with open('pull_requests.yml', 'w') as writer:
        print(yaml.dump(get_all(client, 'pull_request')), file=writer)

    with open('issues.yml', 'w') as writer:
        print(yaml.dump(get_all(client, 'issue')), file=writer)

    with open('msg.yml', 'w') as writer:
        print(yaml.dump(get_all(client, 'msg')), file=writer)


if __name__ == '__main__':
    main()
