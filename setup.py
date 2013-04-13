#!/usr/bin/python3.2
"""Setup script. It creates a distribution and installs the program into the
system.

"""


from distutils.core import setup


# call for function-all-in-one setup()
setup(name='goto-project',
      version='v0.0',
      author='Eduardo Tenório',
      author_email='embatbr@gmail.com',
      url='https://github.com/embatbr/goto-py3',
      # packages=['goto']
      scripts=['bin/bootstrap_goto.py', 'bin/goto.sh'],)