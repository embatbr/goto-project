#!/usr/bin/python3.3


from distutils.core import setup


setup(name='goto-project',
      version='0.1',
      author='Eduardo Tenório',
      author_email='embatbr@gmail.com',
      url='https://github.com/embatbr/goto-py3',
      # packages=['goto']
      scripts=['bin/bootstrap_goto.py', 'bin/goto.sh'],)