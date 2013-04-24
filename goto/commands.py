"""Module defining the commands `goto`, `goto-label` and `goto-list`."""


import argparse
import os
import sys

from goto.storage import Storage, ExistentLabelError, LabelNotFoundError
from goto.storage import LabelTooLongError, NotDirectoryError, format_label


TEMP_FILE = '/tmp/goto'


class Goto(object):
    """Defines command `goto`."""

    def __init__(self, storage=Storage()):
        """Creates a Goto object with default Storage object and the default
        command's arguments.
        """
        self.storage = storage

        self.parser = argparse.ArgumentParser()
        self.parser.set_defaults(mode='list') # list labels' file
        self.parser.add_argument('label', nargs='?', help='name of the label')

    def list_labels(self):
        """Lists all labels with it's respectives paths."""
        if self.storage.labels == {}:
            return None

        ret = ''
        for label in self.storage.get_all_labels():
            ret = '%s%s %s\n' % (ret, format_label(label),
                self.storage.get_path(label))

        return ret[:-1]

    def change_directory(self, label):
        """Writes on temporary file the label's targe."""
        try:
            target = self.storage.get_path(label)
            if not os.path.isdir(target):
                raise NotDirectoryError(label)

            with open(TEMP_FILE, 'w') as f:
                f.write('cd %s' % target)
        except LabelNotFoundError as e:
            sys.stderr.write(str(e))
            sys.exit(-1)

    def run(self):
        """Gives control to the user."""
        args = self.parser.parse_args()

        if args.label:
            args.mode = 'chdir'

        if args.mode == 'list':
            ret = self.list_labels()
            if ret:
                print(ret)
            else:
                sys.stderr.write("There's no directory labeled.\n")
        elif args.mode == 'chdir':
            self.change_directory(args.label)


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

        group = self.parser.add_mutually_exclusive_group()
        group.add_argument('-d', '--delete', action='store_const', dest='mode',
            const='delete', help='delete an existing label')

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

    def delete(self, label):
        """Deletes a existing label from the storage."""
        try:
            self.storage.delete_label(label)
            print("Label '%s' was successfully deleted." % label)
        except LabelNotFoundError as e:
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
        elif args.mode == 'delete':
            self.delete(label)