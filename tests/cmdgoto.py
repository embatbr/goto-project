#!/usr/bin/python3.2


"""Several tests for the module 'cmdgoto' of package 'goto'."""


import sys
import os

import utils
from bin import bootstrap


def main():
    args = ['goto'] + sys.argv[1:]
    command = '$'
    for a in args:
        command = '%s %s' % (command, a)
    print(command)
    bootstrap(args)