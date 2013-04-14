#TODO

This file is intended to set the project goals. The goals are divided into sections for each version release.


##Version 0.1

* Create file *~/.goto/labels*

    Creates (if doesn't exist) a file *labels* inside a hidden directory *goto* in the *home* directory.


* Working command `goto`

    * list the *~/.goto/labels* file

        When typed without parameters or flags.

    * change directory using `goto label`

        If the label and the target are valid.


* Be installed in the system

    Copy the scripts to */usr/bin* and edit *~/.bashrc* file.


##Version 0.2

* Working command `goto-label`

    * Command must be typed like `goto-label [-h] [-d] <label>`

    * It must identify a valid label and target


##Version 0.3

* Command `goto-label`

    * Add flag `-r --replace`

    * Add optional value `target`


##Version 0.4

* Working command `goto-list`

    * Does simple listing

* Command `goto`

    * Add flag `-b [n]` to revert the *n* previous `goto` commands


##Version 1.0

* Command `goto-list` with all listing flags from bash command `ls`

* Command `goto`

    * Add possibility to discriminate `directory` inside label's target

        Ex: `$ goto label/dir`