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
        """Reads the file '.goto/stack' and write it's content in self.stack."""
        self.stack = f.read().splitlines()
        self.stack.reverse()

#### LABEL MANIPULATION METHODS ####

    def get_labels(self):
        return self.labels

    def get_path(self, label):
        return self.labels[label]


def format_label(label):
    ret = '%s%s' % (label, (LABEL_SIZE - len(label)) * ' ')
    return ret


if __name__ == '__main__':
    teste = Storage()

    print('[labels]')
    for label in teste.labels:
        print(format_label(label), teste.labels[label])

    print('\n[stack->base]')
    for label in teste.stack:
        print(label)
    print('[stack->top]')