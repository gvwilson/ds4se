#!/usr/bin/env python

import pandas as pd

df = pd.read_csv('data/jccpprtTR.csv')
java = df.loc[df['lang'] == 'Java']
print('25th', java.whours.quantile(0.25))
print('75th', java.whours.quantile(0.75))
print('75/25', java.whours.quantile(0.75) / java.whours.quantile(0.25))
print('90th', java.whours.quantile(0.90))
print('50th', java.whours.quantile(0.50))
print('90/50', java.whours.quantile(0.90) / java.whours.quantile(0.50))
