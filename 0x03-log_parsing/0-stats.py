#!/usr/bin/python3
"""Performs log analysis"""

import sys
import re
from collections import defaultdict

counter = 0
file_size = 0
statusCode_counter = defaultdict(int)


def printCodes(dict, file_s):
    """Prints the status code and file size"""
    print("File size: {}".format(file_s))
    for key in sorted(dict.keys()):
        if dict[key] != 0:
            print("{}: {}".format(key, dict[key]))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            split_string = line.rstrip().split(' ')
            statusC, f_size = int(split_string[-2]), int(split_string[-1])
            statusCode_counter[statusC] += 1
            file_size += f_size
            if counter != 0 and counter % 10 == 0:
                printCodes(statusCode_counter, file_size)
            counter += 1
        printCodes(statusCode_counter, file_size)
    except KeyboardInterrupt:
        printCodes(statusCode_counter, file_size)
        raise
