"""package: goto"""


from commands import Goto, Label

from storage import Storage, ExistentLabelError, LabelNotFoundError, LabelTooLongError
from storage import format_label

__all__ = ['Goto', 'Label', 'Storage', 'ExistentLabelError', 'LabelNotFoundError',
           'LabelTooLongError', 'format_label']