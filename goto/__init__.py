"""package: goto"""


from commands import Goto as Goto
from commands import Label as Label

from storage import Storage, ExistentLabelError, LabelNotFoundError, LabelTooLongError
from storage import format_label

__all__ = ['Goto', 'Label', 'Storage', 'ExistentLabelError', 'LabelNotFoundError',
           'LabelTooLongError', 'format_label']