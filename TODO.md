#TODO

This file is intended to set the project goals. The goals are divided into sections for each version release.


##Version 0.1

1. [OK] Create file *~/.goto/labels*.

    Creates (if doesn't exist) a file *labels* inside a hidden directory *goto* in the *home* directory.

2. [OK] Create file *~/.goto/stack*.

    Creates (if doesn't exist) a file *stack* inside a hidden directory *goto* in the *home* directory.

3. [OK] Working command `goto`.

    1. List the *~/.goto/labels* file.

        When typed without parameters or flags.

4. Be installed in the system.

    Copy the scripts to */usr/bin* and edit *~/.bashrc* file.

###Version 0.1.1 [OK]

1. [OK] Created a new function `format_label`.


##Version 0.2

1. Working command `goto-label`.

    1. Command must be typed like `goto-label [-h] [-d] <label>`.

    2. It must identify a valid label and target.

2. Command `goto`.

    1. Change directory using `goto label_name`.


##Version 0.3

1. Command `goto-label`.

    1. Add flag `-r --replace`.

    2. Add optional value `target`.


##Version 0.4

1. Working command `goto-list`.

    1. Does simple listing.

2. Command `goto`.

    1. Add flag `-b [n]` to revert the *n* previous `goto` commands.


##Version 1.0

1. Command `goto-list` with all listing flags from bash command `ls`.

2. Command `goto`.

    1. Add possibility to discriminate `directory` inside label's target.

        Ex: `$ goto label/dir`.


##Version 2.0

1. Change file *~/.goto/labels* format and extension to **JSON**. So, the file will be *~/.goto/labels.json* and `Storage` will use the libs to work with **JSON**.

2. Implement autocomplete using the key **TAB**. Availabe for labels and it's subdirectories.