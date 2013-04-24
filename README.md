#goto-project - easy'n'fast cd'ing

Tired of typing a lot to get where the fun is happening? `goto` was made for you!

NOTE: This project is a fork from [paulo borges' goto project](https://github.com/pauloborges/goto) implemented using python 3 and with some differences in commands.

Version: 0.2.2

Python: 3.2.3


##Versioning

The version number is in the format V.R[.C], starting from 0 without limits. A version like "goto-project-1.0" can have it's zeros omitted and be simply called "goto-project-1".

The first number, V, denotes the project version. So a difference between a version 1 and 2, for example, is huge, almost a new project.

The second number, R, is a revision of the project version. It can be a change in some functionality or the addition of a new one.

The third number is usually a bug correction of version V.R or a too small addition (like a new function extracted from another) and is optional.


##Commands

The commands are in the format `goto[-subcommand]`, like `goto`, `goto-label` and `goto-list`.

The commands description is as followed:


###goto

    $ goto -h
    usage: goto [-h] [-b [n]] [label[/[subpath]]]
    
    positional arguments:
      label         name of the label
      subpath       path inside label's target (usage: label/subpath)
    
    optional arguments:
      -h, --help    shows help message an exit
      -b, --back    return to n-th previous 'goto' command; n is 1 by default

When you type `goto label` it internally does `cd target`, where `target` is the absolute path pointed by `label`. The option `-b` or `--back` returns to n-th previous `goto` command stored in the `~/.goto/stack` file and doesn't require the `label` argument.

###goto-label

###goto-list
