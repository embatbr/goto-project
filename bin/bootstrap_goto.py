#!/usr/bin/python3.3


import sys


def bootstrap():
    """Function to call goto commands."""
    del sys.argv[0]

    if sys.argv[0] == 'goto':
        return "The command 'goto' was called."


if __name__ == '__main__':
    bootstrap()