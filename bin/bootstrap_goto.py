#!/user/bin/python3.2


"""This module calls the 'real' code."""


import sys

from goto import goto_main


def bootstrap(args):
    """Function to call the commands."""
    if args[0] == 'goto':
        return goto_main()

    sys.exit(-1)


if __name__ == '__main__':
    del sys.argv[0]
    bootstrap(sys.argv)