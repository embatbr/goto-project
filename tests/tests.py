#!/usr/bin/python3.2


"""Several tests for the module 'storage' of package 'goto'."""


import sys
import os

__depth = 2
path = os.path.abspath(__file__)    # /home/.../goto-project/tests/__file__.py
for i in range(__depth):
    path = os.path.dirname(path)
sys.path.insert(0, path)

from goto import Storage, ExistentLabelError, NonexistentLabelError, format_label
from bin import bootstrap


def format_output(obj):
    output = str(obj)
    ret = '    '
    for s in output:
        if s == '\n':
            ret = '%s%s%s' % (ret, s, '    ')
        else:
            ret = '%s%s' % (ret, s)

    return ret


def test_storage():
    log = open('storage.md', 'w')
    log.write('#Log file for `tests/storage.py`')
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
    args = ['goto'] + sys.argv[1:]
    command = '$'
    for a in args:
        command = '%s %s' % (command, a)
    print(command)
    bootstrap(args)


test_storage()
test_goto()