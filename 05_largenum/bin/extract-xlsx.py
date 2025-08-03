#!/usr/bin/env python

'''
Extract daily hours from spreadsheet.
'''

import sys
import xlrd
import csv
import datetime

workbook = xlrd.open_workbook(sys.argv[1])
writer = csv.writer(sys.stdout, lineterminator='\n')
writer.writerow(['Date', 'Hours'])
for sheet in workbook.sheets():
    if (sheet.name != 'Summary'):
        for entry in zip(sheet.col_values(5), sheet.col_values(6)):
            if entry[0] and (entry[0] != 'Date'):
                d = datetime.datetime(*xlrd.xldate_as_tuple(entry[0], workbook.datemode))
                row = (d.strftime('%Y-%m-%d'),
                       entry[1] * 24)
                writer.writerow(row)
