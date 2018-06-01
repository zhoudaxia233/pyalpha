#! /usr/bin/env python3
# coding: utf-8
'''
For reading the txt file of event logs
'''
def read(filename):
    log = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            assert isinstance(line, str)
            log.append(tuple(line.split()))
    return log
