#!/usr/bin/python3.2


"""Several tests for the module 'storage' of package 'goto'."""


import sys
import os

PROJECT_DIR = os.path.abspath(__file__) # /home/.../goto-project/tests/__file__.py
PROJECT_DIR = PROJECT_DIR.split('goto-project')[0] + 'goto-project'
print(PROJECT_DIR)
sys.path.insert(0, PROJECT_DIR)

from goto import Storage, ExistentLabelError, NonexistentLabelError, format_label
from goto import Goto


def format_output(obj):
    output = str(obj)
    ret = ''
    for line in output.splitlines():
        ret = '%s    %s\n' % (ret, line)

    return ret


def test_storage():
    filename = PROJECT_DIR + '/tests/storage.md'
    log = open(filename, 'w')
    log.write('#Log file for `goto/storage` module.')
    log.write('\n\nThis is a log file for tests of module `goto/storage`. A object')
    log.write(" of type `Storage` is created and it's methods are tested.")

    stg = Storage()
    stg.flush()
    log.write('\n\n\n##stg = Storage()\n\n')
    log.write(format_output(stg))

    stg.add_label('home', '/home/embat')
    log.write("\n\n\n##stg.add_label('home', '/home/embat')\n\n")
    log.write(format_output(stg))

    stg.add_label('musicas', '/home/embat/dados/lazer/musicas')
    log.write("\n\n\n##stg.add_label('musicas', '/home/embat/dados/lazer/musicas')\n\n")
    log.write(format_output(stg))

    # add same label
    log.write("\n\n\n##stg.add_label('musicas', '/home/embat/Musics')\n\n")
    try:
        stg.add_label('musicas', '/home/embat/Musics')
        log.write(format_output(stg))
    except ExistentLabelError as e:
        log.write(format_output(e))

    path = stg.get_path('musicas')
    log.write("\n\n\n##path = stg.get_path('musicas')\n\n")
    output = '%s%s' % (format_label('musicas'), path)
    log.write(format_output(output))

    log.write("\n\n\n##path = stg.get_path('jogos')\n\n")
    try:
        path = stg.get_path('jogos')
        output = '%s%s' % (format_label('musicas'), path)
        log.write(output)
    except NonexistentLabelError as e:
        log.write(format_output(e))

    labels = stg.get_all_labels()
    log.write("\n\n\n##labels = stg.get_all_labels()\n\n")
    log.write(format_output(labels))

    stg.save()
    log.write('\n\n\n##stg.save()\n\n')
    log.write(format_output(stg))
    log.close()


def test_goto():
    filename = PROJECT_DIR + '/tests/goto.md'
    log = open(filename, 'w')
    log.write('#Log file for `goto/command.Goto` class')

    goto = Goto()
    labels_list = goto.list_labels()
    log.write('\n\n\n##goto.list_labels()\n\n')
    log.write(format_output(labels_list))


if __name__ == '__main__':
    test_storage()
    test_goto()