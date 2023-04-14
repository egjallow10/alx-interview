#!/usr/bin/python3
"""Performs log analysis"""


import sys

counter = 0
file_size = 0
statusC_counte = {200: 0, 301: 0, 400: 0, 401: 0,
                  403: 0, 404: 0, 405: 0, 500: 0}

try:
    while True:
        line = input().strip()
        output = line.split()
        if int(output[-2]) in statusC_counte.keys() and len(output) == 9:
            counter += 1
            statusC_counte[int(output[-2])] += 1
            file_size += int(output[-1])
        if counter % 10 == 0:
            print('File size: {}'.format(file_size))
            for key, value in sorted(statusC_counte.items()):
                if value:
                    print("{}: {}".format(key, value))
except EOFError:
    print('File size: {}'.format(file_size))
    for key, value in sorted(statusC_counte.items()):
        if value:
            print("{}: {}".format(key, value))
