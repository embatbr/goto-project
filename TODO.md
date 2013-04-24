#Version 0


##Version 0.2

###Version 0.2.2

1. Add flag `-r` or `--replace` to `goto-label`.

###Version 0.2.3

1. Define label format.


##Version 0.3

1. Working command `goto-list`.

    1. Does simple listing.

###Version 0.3.1

1. Add flags from command `ls`.


##Version 0.4

1. Add command `goto-back`.

###Version 0.4.1

1. Add optional value `n` to specify the number of **pops** from the stack.



#Version 1

1. Command `goto-list` with all listing flags from bash command `ls`.

2. Command `goto`.

    1. Add possibility to discriminate `directory` inside label's target.

        Ex: `$ goto label/dir`.

##Version 1.1

1. Implement autocomplete using the key **TAB**. Availabe for labels and it's subdirectories.



#Version 2

1. Change file *~/.goto/labels* format and extension to **JSON**. So, the file will be *~/.goto/labels.json* and **Storage** will use the libs to work with **JSON**.

2. Add the the project's functionalities to **Nautilus**. Use the command `goto` to open directories in graphical mode.