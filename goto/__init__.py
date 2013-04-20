"""package: goto"""


from goto.cmdgoto import main as goto_main
from goto.storage import Storage, ExistentLabelError, NonexistentLabelError
from goto.storage import format_label