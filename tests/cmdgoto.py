#!/usr/bin/python3.2


"""Several tests for the module 'goto' of package 'goto'."""


__depth = 2


import sys
import os

path = os.path.abspath(__file__)    # /home/.../goto-project/tests/goto.py
for i in range(__depth):
    path = os.path.dirname(path)
sys.path.insert(0, path)

from bin import bootstrap


print('TEST: goto')
args = ['goto'] + sys.argv[1:]
command = '$'
for a in args:
    command = '%s %s' % (command, a)
print(command)
bootstrap(args)

# print('\nTEST: goto home')