#TODO

This file is intended to set the project goals. The goals are divided into sections for each version release.


##Version 0.1

1. Create file *~/.goto/labels* [OK]

    Creates (if doesn't exist) a file *labels* inside a hidden directory *goto* in the *home* directory.

2. Create file *~/.goto/stack* [OK]

    Creates (if doesn't exist) a file *stack* inside a hidden directory *goto* in the *home* directory.


3. Working command `goto`

    1. list the *~/.goto/labels* file

        When typed without parameters or flags.

    2. change directory using `goto label`

        If the label and the target are valid.


4. Be installed in the system

    Copy the scripts to */usr/bin* and edit *~/.bashrc* file.


##Version 0.2

1. Working command `goto-label`

    1. Command must be typed like `goto-label [-h] [-d] <label>`

    2. It must identify a valid label and target


##Version 0.3

1. Command `goto-label`

    1. Add flag `-r --replace`

    2. Add optional value `target`


##Version 0.4

1. Working command `goto-list`

    1. Does simple listing

2. Command `goto`

    1. Add flag `-b [n]` to revert the *n* previous `goto` commands


##Version 1.0

1. Command `goto-list` with all listing flags from bash command `ls`

2. Command `goto`

    1. Add possibility to discriminate `directory` inside label's target

        Ex: `$ goto label/dir`