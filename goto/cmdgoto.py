"""Implementation of command 'goto'."""


import argparse

from goto.storage import Storage, format_label


storage = Storage()


def list_labels():
    for label in storage.get_labels():
        s = '%s %s' % (format_label(label), storage.get_path(label))
        print(s)


def main():
    parser = argparse.ArgumentParser()
    parser.set_defaults(mode='list') # list labels' file

    args = parser.parse_args()

    if args.mode == 'list':
        list_labels()
