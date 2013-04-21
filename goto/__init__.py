"""package: goto"""


from goto.commands import main as goto_main

from goto.storage import Storage, ExistentLabelError, NonexistentLabelError
from goto.storage import format_label