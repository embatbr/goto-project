#Version 0

##Version 0.3

1. Add list flags to command `goto`. Mutually exclusion: `-l`,  `-a`, `label`.

    1. `-l` or `--list`. Equals `ls target`.
    2. `-a` or `--all`. Same as above, with flag `-a`

##Version 0.4

1. Discriminate `directory` inside `label` in command `goto`.

        Ex: `$ goto label/dir`.

2. Implement autocomplete using the key **TAB**. Availabe for labels and it's subdirectories.



#Version 2

1. Change file *~/.goto/labels* format and extension to **JSON**. So, the file will be *~/.goto/labels.json* and **Storage** will use the libs to work with **JSON**.

2. Add the the project's functionalities to **Nautilus**. Use the command `goto` to open directories in graphical mode.