import time
import numpy as np


TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
EXCLUDE_DIR = '.git .jekyll-cache .jekyll-metadata'.split()
EXCLUDE_SUFFIX = '.eps .ico .jpg .pdf .png .xlsx'.split()


def fmt_time(t):
    return time.strftime(TIME_FORMAT, time.gmtime(t))


# Taken from <https://github.com/oliviaguest/gini>
def gini(array):
    """
    Calculate the Gini coefficient of a numpy array.
    """
    # based on bottom eq: http://www.statsdirect.com/help/content/image/stat0206_wmf.gif
    # from: http://www.statsdirect.com/help/default.htm#nonparametric_methods/gini.htm
    if np.amin(array) < 0:
        array -= np.amin(array) # values cannot be negative
    array += 0.0000001 # values cannot be 0
    array = np.sort(array) # values must be sorted
    index = np.arange(1, array.shape[0]+1) # index per array element
    n = array.shape[0] # number of array elements
    return ((np.sum((2 * index - n - 1) * array)) / (n * np.sum(array))) # Gini coefficient


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
