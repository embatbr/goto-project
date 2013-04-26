"""package: goto"""


from goto.commands import Goto, Label

from goto.storage import Storage, ExistentLabelError, LabelNotFoundError, LabelTooLongError
from goto.storage import format_label