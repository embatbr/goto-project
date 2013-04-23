"""Module defining the commands `goto`, `goto-label` and `goto-list`."""


import argparse
import os
import sys

from goto.storage import Storage, ExistentLabelError, LabelTooLongError, format_label


class Goto(object):
    """Defines command `goto`."""

    def __init__(self, storage=Storage()):
        """Creates a Goto object with default Storage object and the default
        command's arguments.
        """
        self.storage = storage

        self.parser = argparse.ArgumentParser()
        self.parser.set_defaults(mode='list') # list labels' file

    def list_labels(self):
        """Lists all labels with it's respectives paths."""
        ret = ''
        for label in self.storage.get_all_labels():
            ret = '%s\n%s %s' % (ret, format_label(label),
                self.storage.get_path(label))

        return ret[1:]

    def run(self):
        """Gives control to the user."""
        args = self.parser.parse_args()

        if args.mode == 'list':
            print(self.list_labels())


class GotoLabel(object):
    """Defines command `goto-label`."""

    def __init__(self, storage=Storage()):
        """Creates a GotoLabel object with default Storage object and the default
        command's arguments.
        """
        self.storage = storage

        self.parser = argparse.ArgumentParser()
        self.parser.set_defaults(mode='insert')
        self.parser.add_argument('label', nargs='?', help='name of the label')
        self.parser.add_argument('target', nargs='?', help='path of the target directory')

    def add(self, label, target):
        """Adds a entry to the storage.add_label"""
        try:
            self.storage.add_label(label, target)
            print("'%s' poinst to '%s'" % (label, target))
        except ExistentLabelError as e:
            sys.stderr.write(str(e))
            sys.exit(-1)
        except LabelTooLongError as e:
            sys.stderr.write(str(e))
            sys.exit(-1)

    def run(self):
        """Gives control to the user."""
        args = self.parser.parse_args()

        target = os.getcwd()
        label = os.path.basename(target)
        if args.label:
            label = args.label
        if args.target:
            target = args.target

        if args.mode == 'insert':
            self.add(label, target)