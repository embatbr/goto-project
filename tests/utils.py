"""Module with common code for package 'tests'."""


import sys
import os


__depth = 2
path = os.path.abspath(__file__)    # /home/.../goto-project/tests/__file__.py
for i in range(__depth):
    path = os.path.dirname(path)
sys.path.insert(0, path)


def format_output(obj):
    output = str(obj)
    ret = '    '
    for s in output:
        if s == '\n':
            ret = '%s%s%s' % (ret, s, '    ')
        else:
            ret = '%s%s' % (ret, s)

    return ret