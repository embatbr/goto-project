"""Module to work with files inside the hidden directory '~/.goto'."""


import os
import re


HOME_DIR = os.path.expanduser("~")
GOTO_DIR = '%s/.goto' % HOME_DIR
LABELS_FILENAME = 'labels'

LABEL_SIZE = 16
LABEL_REGEX = r'[a-z][a-zA-Z0-9_-]*$'
LABEL_REGEX_OBJECT = re.compile(LABEL_REGEX)


#### BEGIN STORAGE ####
class Storage(object):
    """Manipulates files inside .goto directory."""

    def __init__(self, goto_dir=GOTO_DIR, labels_filename=LABELS_FILENAME):
        self.goto_dir = goto_dir
        self.labels_path = os.path.join(goto_dir, labels_filename)
        self.labels = {}
        self.open_files()

    def __str__(self):
        ret = '[goto_dir] %s' % self.goto_dir
        ret = '%s\n[labels_path] %s' % (ret, os.path.basename(self.labels_path))

        if self.labels:
            ret = '%s\n[labels]' % ret
            for label in self.labels:
                ret = '%s\n%s%s' % (ret, format_label(label), self.labels[label])

        return ret


#### FILE MANIPULATION METHODS ####

    def open_files(self):
        """Open (or create if doesn't exist) files for goto-project."""
        if not os.path.exists(self.goto_dir):
            os.makedirs(self.goto_dir)
        open(self.labels_path, 'a').close()

        with open(self.labels_path) as f:
            self.read_labels(f)

    def read_labels(self, f):
        """Reads the file '.goto/labels' and write it's content in self.labels."""
        lines = f.read().splitlines()
        for line in lines:
            (label, target) = line.split()
            self.labels[label] = target

    def save(self):
        """Saves the actual state (new labels) into file."""
        with open(self.labels_path, 'w') as f:
            for label in self.labels:
                output = '%s %s\n' % (label, self.labels[label])
                f.write(output)

    def flush(self):
        """Erase all storage."""
        self.labels = {}


#### LABEL MANIPULATION METHODS ####

    def __insert_label(self, label, target):
        """Insert a 'target' given a 'label'."""
        if not LABEL_REGEX_OBJECT.match(label): # the case 'dir/subdir' is passing
            raise InvalidLabelFormat(label)
        elif len(label) > LABEL_SIZE:
            raise LabelTooLongError(label)
        elif not os.path.isdir(target):
            raise NotDirectoryError(target)

        self.labels[label] = target
        self.save()

    def add_label(self, label, target):
        """Adds a label with specified target."""
        if label in self.labels:
            raise ExistentLabelError(label)

        self.__insert_label(label, target)

    def replace_label(self, label, target):
        """Changes label's target to the given target."""
        if label not in self.labels:
            raise LabelNotFoundError(label)

        self.__insert_label(label, target)

    def delete_label(self, label):
        """Deletes a existing label."""
        if len(label) > LABEL_SIZE:
            raise LabelTooLongError(label)
        elif label not in self.labels:
            raise LabelNotFoundError(label)

        del self.labels[label]
        self.save()

    def get_path(self, label):
        """Returns the target from a given label."""
        if len(label) > LABEL_SIZE:
            raise LabelTooLongError(label)
        elif label not in self.labels:
            raise LabelNotFoundError(label)

        return self.labels[label]

    def get_all_labels(self):
        return self.labels
#### END STORAGE ####


def format_label(label):
    ret = '%s%s' % (label, (LABEL_SIZE - len(label)) * ' ')
    return ret


#### BEGIN STORAGE_ERROR ####
class StorageError(Exception):
    """'Abstract' class for all exceptions from module `storage`."""
    pass

class InvalidLabelFormat(StorageError):
    def __init__(self, label):
        self.label = label
    
    def __str__(self):
        return ("The label '%s' is not in format '%s'.\n" % (self.label,
            LABEL_REGEX))

class ExistentLabelError(StorageError):
    def __init__(self, label):
        self.label = label
    
    def __str__(self):
        return ("The label '%s' alredy exist.\n" % self.label)

class LabelNotFoundError(StorageError):
    def __init__(self, label):
        self.label = label
    
    def __str__(self):
        return ("The label '%s' doesn't exist.\n" % self.label)

class LabelTooLongError(StorageError):
    def __init__(self, label):
        self.label = label
    
    def __str__(self):
        return ("The label '%s' is longer than %d characters.\n" % (self.label,
            LABEL_SIZE))

class NotDirectoryError(StorageError):
    def __init__(self, target):
        self.target = target
    
    def __str__(self):
        return ("The target '%s' isn't a directory.\n" % self.target)
#### END STORAGE_ERROR ####