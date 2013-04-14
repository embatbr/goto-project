"""Setup script. It creates a distribution and installs the program into the
system.

"""


from distutils.core import setup
import os


def readme():
    (directory, f) = os.path.split(os.path.abspath(__file__)) # __file__ = setup.py
    readme_file = open(os.path.join(directory, 'README.md'))
    return readme_file.read()


setup(name='goto-project',
      version='v0.0',
      author='Eduardo Tenório',
      author_email='embatbr@gmail.com',

      url='https://github.com/embatbr/goto-py3',
      description="easy'n'fast cd'ing",
      long_description=readme(),

      packages=['goto']
      # scripts=['bin/bootstrap_goto.py', 'bin/goto.sh'],)
