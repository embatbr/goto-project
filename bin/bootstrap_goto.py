#!/usr/bin/python3


"""This module calls the 'real' code."""


import sys

from goto import Goto, Label
# from goto import *


def bootstrap(args):
    """Function to call the commands."""
    if args[0] == 'goto':
        goto = Goto()
        return goto.run()
    elif args[0] == 'label':
        label = Label()
        return label.run()

    sys.exit(-1)


if __name__ == '__main__':
    del sys.argv[0]
    bootstrap(sys.argv)