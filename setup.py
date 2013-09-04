#!/usr/bin/python3.2


"""Setup script. It creates a distribution and installs the program into the
system.

"""


import os
import subprocess
import platform
import re
from distutils.core import setup
from distutils.command.install import install


HOME_DIR = os.path.expanduser("~")
SYSTEM_PLATFORM = platform.system()
BASHRC_FILE = '.bash_profile' if (SYSTEM_PLATFORM == 'Darwin') else '.bashrc'
BASHRC_PATH = os.path.join(HOME_DIR, BASHRC_FILE)

RE = re.compile(r'^\. .*goto.sh')


def post_install():
    """Edits .bashrc file to source goto.sh script."""
    (status, goto_sh_path) = subprocess.getstatusoutput('which goto.sh')

    if status != 0:
        print("Can't find goto.sh script.")
        return None

    source_line = ". %s\n" % goto_sh_path
    if not os.path.isfile(BASHRC_PATH):
        print('%s does not exist. Please append "%s" into your shell init'
            'script.' % (BASHRC_PATH, source_line))
        return None

    with open(BASHRC_PATH, 'r') as f:
        lines = f.readlines()

    replaced = False
    with open(BASHRC_PATH, 'w') as f:
        for line in lines:
            if RE.match(line):
                replaced = True
                f.write(source_line)
            else:
                f.write(line)

        if not replaced:
            f.write('\n')
            f.write(source_line)


class GotoInstall(install):
    def run(self):
        install.run(self)
        post_install()


def readme():
    (directory, f) = os.path.split(os.path.abspath(__file__)) # __file__ = setup.py
    readme_file = open(os.path.join(directory, 'README.md'))
    return readme_file.read()


setup(name='goto-project',
      version='0.1.1-pre-alpha',
      author='Eduardo Tenório',
      author_email='embatbr@gmail.com',

      url='https://github.com/embatbr/goto-py3',
      description="easy'n'fast cd'ing",
      long_description=readme(),

      packages=['bin', 'goto'],
      scripts=['bin/bootstrap_goto.py', 'bin/goto.sh', 'goto/__init__.py', 'goto/commands.py',
               'goto/storage.py'],
      cmdclass={ 'install': GotoInstall }
      )
