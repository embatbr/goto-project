#goto-project - easy'n'fast cd'ing

Tired of typing a lot to get where the fun is happening? `goto` was made for you!

NOTE: This project is a fork from [paulo borges' goto project](https://github.com/pauloborges/goto) implemented using python 3 and with some differences in commands.

It is tested only at linux, but the mac's shell is teorically supported.

Version: 0.3.2

Python: 3.2.3


##Versioning

The version number is in the format V.R[.C], starting from 0 without limits. A version like "goto-project-1.0" can have it's zeros omitted and be simply called "goto-project-1".

The first number, V, denotes the project version. So a difference between a version 1 and 2, for example, is huge, almost a new project.

The second number, R, is a revision of the project version. It can be a change in some functionality or the addition of a new one.

The third number is usually a bug correction of version V.R or a too small addition (like a new function extracted from another) and is optional.


##Commands

The commands are in the format `goto[-subcommand]`.Their description is as followed:


###goto

    usage: goto [-h] [-l | -a] [label]

    positional arguments:
      label       name of the label

    optional arguments:
      -h, --help  show this help message and exit
      -l, --list  equals to 'ls -l <label>'
      -a, --all   equals to 'ls -la <label>'

When you type `goto <label>` it internally does `cd <target>`, where `target` is the absolute path pointed by `label`. The flags `-l` and `-a` lists the label's target. It's equivalento to `cd <target> && ls -l[a] && cd -`.

###label

    usage: goto-label [-h] [-d | -r] [name] [target]

    positional arguments:
      name           name of the label
      target         path of the directory

    optional arguments:
      -h, --help     show this help message and exit
      -d, --delete   delete an existing label
      -r, --replace  replace an existing label's target

Create, replace or delete a label. If argument `name` is not provided, the actual directory's basename is taken as `name`. If argument `target` is not provided, the actual path is taken as `target`. The command writes on a file *.goto/labels*, usually located at the user's home.
