#Version 1

##Version 1.2

1. Implement autocomplete using the key **TAB**. Availabe for labels and it's subdirectories.


#Version 2

##Version 2.0

1. Change file *~/.goto/labels* format and extension to **JSON**. So, the file will be *~/.goto/labels.json* and **Storage** will use the libs to work with **JSON**.

##Version 2.1

2. Add the project's functionalities to **Nautilus**. Use the command `goto` to open directories in graphical mode.


#Version 3

##Version 3.0

1. Create new command `do` (or something similar) to open files passing a `goto`'s label. Example: in label **goto** there is a file named **README.md**. Doing `do goto/README.md` should be equivalent to the sequency `sublime-text-2 <goto's target>/README.md`. Similarly `do goto/bin/goto.sh` should do `sublime-text-2 <goto's target>/bin/goto.sh`
