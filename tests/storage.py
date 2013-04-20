#!/usr/bin/python3.2


"""Several tests for the module 'storage' of package 'goto'."""


__depth = 2


import sys
import os

path = os.path.abspath(__file__)    # /home/.../goto-project/tests/goto.py
for i in range(__depth):
    path = os.path.dirname(path)
sys.path.insert(0, path)

from goto import Storage, ExistentLabelError, NonexistentLabelError, format_label


log = open('storage.md', 'w')
log.write('#Log file for `tests/storage.py`')
log.write('\n\nThis is a log file for tests of module `goto/storage`. A object')
log.write(" of type `Storage` is created and it's methods are tested.")

stg = Storage()
stg.flush()
log.write('\n\n\n##stg = Storage()\n\n')
log.write(str(stg))

stg.add_label('home', '/home/embat')
log.write("\n\n\n##stg.add_label('home', '/home/embat')\n\n")
log.write(str(stg))

stg.add_label('musicas', '/home/embat/dados/lazer/musicas')
log.write("\n\n\n##stg.add_label('musicas', '/home/embat/dados/lazer/musicas')\n\n")
log.write(str(stg))

# add same label
log.write("\n\n\n##stg.add_label('musicas', '/home/embat/Musics')\n\n")
try:
    stg.add_label('musicas', '/home/embat/Musics')
    log.write(str(stg))
except ExistentLabelError as e:
    log.write(str(e))

path = stg.get_path('musicas')
log.write("\n\n\n##path = stg.get_path('musicas')\n\n")
output = '%s%s' % (format_label('musicas'), path)
log.write(output)

log.write("\n\n\n##path = stg.get_path('jogos')\n\n")
try:
    path = stg.get_path('jogos')
    output = '%s%s' % (format_label('musicas'), path)
    log.write(output)
except NonexistentLabelError as e:
    log.write(str(e))

labels = stg.get_all_labels()
log.write("\n\n\n##labels = stg.get_all_labels()\n\n")
log.write(str(labels))

stg.save()
log.write('\n\n\n##stg.save()\n\n')
log.write(str(stg))
log.close()