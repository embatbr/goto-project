#!/user/bin/python3.2


"""This module calls the 'real' code."""


import sys

from goto import Goto


def bootstrap(args):
    """Function to call the commands."""
    if args[0] == 'goto':
        goto = Goto()
        return goto.run()

    sys.exit(-1)


if __name__ == '__main__':
    del sys.argv[0]
    bootstrap(sys.argv)