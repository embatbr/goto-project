#!/usr/bin/python3.2


"""Temporary module just for test."""


import sys

from bin import bootstrap


print('TEST: goto')
args = ['goto'] + sys.argv[1:]
command = '$'
for a in args:
    command = command + ' ' + a
print(command)
bootstrap(args)

# print('\nTEST: goto home')