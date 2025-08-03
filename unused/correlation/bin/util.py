import time
import numpy as np


TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
EXCLUDE_DIR = '.git .jekyll-cache .jekyll-metadata'.split()
EXCLUDE_SUFFIX = '.eps .ico .jpg .pdf .png .xlsx'.split()


def fmt_time(t):
    return time.strftime(TIME_FORMAT, time.gmtime(t))


def include(path):
    '''
    Process this file?
    '''
    for d in EXCLUDE_DIR:
        if d in path:
            return False
    for s in EXCLUDE_SUFFIX:
        if path.endswith(s):
            return False
    return True
