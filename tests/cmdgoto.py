#!/usr/bin/python3.2


"""Temporary module just for test."""
 

import sys
import os

path = os.path.abspath(__file__)    # /home/.../goto-project/tests/goto.py
dirname = os.path.dirname(path)     # /home/.../goto-project/tests
dirname = os.path.dirname(dirname)  # /home/.../goto-project
sys.path.insert(0, dirname)

from bin import bootstrap


print('TEST: goto')
args = ['goto'] + sys.argv[1:]
command = '$'
for a in args:
    command = '%s %s' % (command, a)
print(command)
bootstrap(args)

# print('\nTEST: goto home')