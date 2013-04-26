"""Module defining the commands `goto`, `goto-label` and `goto-list`."""


import argparse
import os
import sys

from goto.storage import Storage, StorageError, format_label


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

        group = self.parser.add_mutually_exclusive_group()
        group.add_argument('-l', '--list', action='store_const', dest='mode',
            const='list-target', help="equals to 'ls -l target'")
        group.add_argument('-a', '--all', action='store_const', dest='mode',
            const='list-target-all', help="equals to 'ls -la target'")

    def list_labels(self):
        """Lists all labels with it's respectives paths."""
        if self.storage.labels == {}:
            return "There's no directory labeled."

        ret = ''
        for label in self.storage.get_all_labels():
            ret = '%s%s %s\n' % (ret, format_label(label),
                self.storage.get_path(label))

        return ret[:-1]

    def call_bash(self, cmd, label,):
        """Writes on temporary file the label's target."""
        try:
            target = self.storage.get_path(label)
            if not os.path.isdir(target):
                raise NotDirectoryError(target)

            with open(TEMP_FILE, 'w') as f:
                f.write('%s %s' % (cmd, target))
        except StorageError as e:
            sys.stderr.write(str(e))
            sys.exit(-1)

    def run(self):
        """Gives control to the user."""
        args = self.parser.parse_args()

        if args.label and args.mode == 'list':
            args.mode = 'chdir'

        if args.mode == 'list':
            print(self.list_labels())
        elif args.mode == 'chdir':
            self.call_bash('cd', args.label)
        elif args.mode == 'list-target':
            self.call_bash('ls -l', args.label)
        elif args.mode == 'list-target-all':
            self.call_bash('ls -la', args.label)


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
        group.add_argument('-r', '--replace', action='store_const', dest='mode',
            const='replace', help="replace an existing label's target")

    def add(self, label, target):
        """Adds a entry to the storage.add_label"""
        try:
            self.storage.add_label(label, target)
            print("'%s' poinst to '%s'" % (label, target))
        except StorageError as e:
            sys.stderr.write(str(e))
            sys.exit(-1)

    def delete(self, label):
        """Deletes an existing label from the storage."""
        try:
            self.storage.delete_label(label)
            print("Label '%s' was successfully deleted." % label)
        except StorageError as e:
            sys.stderr.write(str(e))
            sys.exit(-1)

    def replace(self, label, target):
        """Replaces an existing label's target."""
        try:
            self.storage.replace_label(label, target)
            print("Label '%s' now points to '%s'." % (label, target))
        except StorageError as e:
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
        elif args.mode == 'replace':
            self.replace(label, target)