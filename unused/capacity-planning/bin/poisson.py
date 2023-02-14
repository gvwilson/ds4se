#!/usr/bin/env python

import sys
import math

def fac(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def main():
    '''
    Calculate Poisson(rate, k, t).
    '''
    rate = float(sys.argv[1])
    k = int(sys.argv[2])
    t = float(sys.argv[3])
    events = rate * t * math.exp(- rate * t) / fac(k)
    print(f'rate {rate} k {k} t {t} probability {events}')

if __name__ == '__main__':
    main()
