"""Module to work with files inside the hidden directory '~/.goto'."""


import os


HOME_DIR = os.path.expanduser("~")
GOTO_DIR = '%s/.goto' % HOME_DIR
LABELS_FILENAME = 'labels'
STACK_FILENAME = 'stack'
LABEL_SIZE = 16


class Storage(object):
    """Manipulates files inside .goto directory."""

    def __init__(self, goto_dir=GOTO_DIR, labels_filename=LABELS_FILENAME,
                 stack_filename=STACK_FILENAME):
        self.goto_dir = goto_dir
        self.labels_path = os.path.join(goto_dir, labels_filename)
        self.stack_path = os.path.join(goto_dir, stack_filename)
        self.labels = {}
        self.stack = []
        self.open_files()

    def __str__(self):
        ret = '[goto_dir] %s' % self.goto_dir
        ret = '%s\n[labels_path] %s' % (ret, os.path.basename(self.labels_path))
        ret = '%s\n[stack_path] %s' % (ret, os.path.basename(self.stack_path))
        if self.labels:
            ret = '%s\n[labels]' % ret
            for label in self.labels:
                ret = '%s\n%s%s' % (ret, format_label(label), self.labels[label])
        if self.stack:
            ret = '%s\n[stack->base]' % ret
            for label in self.stack:
                ret = '%s\n%s' % (ret, label)
            ret = '%s\n[stack->top]' % ret
        return ret


#### FILE MANIPULATION METHODS ####

    def open_files(self):
        """Open (or create if doesn't exist) files for goto-project."""
        if not os.path.exists(self.goto_dir):
            os.makedirs(self.goto_dir)
        open(self.labels_path, 'a').close()
        open(self.stack_path, 'a').close()

        with open(self.labels_path) as f:
            self.read_labels(f)
        with open(self.stack_path) as f:
            self.read_stack(f)

    def read_labels(self, f):
        """Reads the file '.goto/labels' and write it's content in self.labels."""
        lines = f.read().splitlines()
        for line in lines:
            (label, target) = line.split()
            self.labels[label] = target

    def read_stack(self, f):
        """Reads the file '.goto/stack' and write it's content in self.stack,
        from base (0) to top (len(self.stack) - 1).
        """
        self.stack = f.read().splitlines()

    def save(self):
        """Saves the actual state (new labels and greater stack) into files."""
        with open(self.labels_path, 'w') as f:
            for label in self.labels:
                output = '%s %s\n' % (label, self.labels[label])
                f.write(output)
        with open(self.stack_path, 'w') as f:
            for label in self.stack:
                output = '%s\n' % label
                f.write(output)

    def flush(self):
        """Erase all storage."""
        self.labels = {}
        self.stack = []


#### LABEL MANIPULATION METHODS ####

    def add_label(self, label, target):
        """Adds a label with specified target."""
        if label in self.labels:
            raise ExistentLabelError(label)
        elif len(label) > LABEL_SIZE:
            raise LabelTooLongError(label)

        self.labels[label] = target
        self.save()

    def get_path(self, label):
        """Returns the target from a given label."""
        if label not in self.labels:
            raise LabelNotFoundError(label)

        return self.labels[label]

    def get_all_labels(self):
        return self.labels


#### STACK MANIPULATION METHODS ####

    # TODO i next version


def format_label(label):
    ret = '%s%s' % (label, (LABEL_SIZE - len(label)) * ' ')
    return ret


class ExistentLabelError(Exception):

    def __init__(self, label):
        self.label = label
    
    def __str__(self):
        return ("The label '%s' alredy exist.\n" % self.label)

class LabelNotFoundError(Exception):

    def __init__(self, label):
        self.label = label
    
    def __str__(self):
        return ("The label '%s' doesn't exist.\n" % self.label)

class LabelTooLongError(Exception):

    def __init__(self, label):
        self.label = label
    
    def __str__(self):
        return ("The label '%s' is longer than %d characters.\n" % (self.label,
            LABEL_SIZE))