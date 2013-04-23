#TODO

This file is intended to set the project goals. The goals are divided into sections for each version release.


##Version 0.2

2. Command `goto label` must do the `cd target` when typed.

4. Add optional value `target`, so the command will be `goto-label [-h] [-d] [label [target]]`.


###Version 0.2.1

1. Define label format.


##Version 0.3

1. Command `goto-label`.

    1. Add flag `-r --replace`.



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


##Version 1.1

1. Implement autocomplete using the key **TAB**. Availabe for labels and it's subdirectories.


##Version 2.0

1. Change file *~/.goto/labels* format and extension to **JSON**. So, the file will be *~/.goto/labels.json* and **Storage** will use the libs to work with **JSON**.

2. Add the the project's functionalities to **Nautilus**. Use the command `goto` to open directories in graphical mode.