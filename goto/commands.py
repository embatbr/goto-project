"""Module defining the commands `goto`, `goto-label` and `goto-list`."""


import argparse

from goto.storage import Storage, ExistentLabelError, format_label


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

    pass