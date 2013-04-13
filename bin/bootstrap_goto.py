"""This module calls the 'real' code."""


import sys


def bootstrap():
    """Function to call goto commands."""
    del sys.argv[0]

    if sys.argv[0] == 'goto':
        print("The command 'goto' was called.")


if __name__ == '__main__':
    bootstrap()