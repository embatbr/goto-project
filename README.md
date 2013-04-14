goto-project - easy'n'fast cd'ing
=================================

Tired of typing a lot to get where the fun is happening? `goto` was made for you!

This project is a fork from [paulo borges' goto project](https://github.com/pauloborges/goto) implemented using python 3 and more "git like".

Version: 0
Python: 3.2


Versioning
----------

The version number is in the format V.R, starting from 0 with no limits. A version like "goto-project-1.0" can have it's zeros omitted and be simply called "goto-project-1".

The first number, V, denotes the project version. So a difference between a version 1 and 2 is huge, almost a new project.

The second number, R, is a revision of the project version. It can be a small change in some functionality of the project or a patch with bug corrections.


goto
----

    usage: goto [-h] [-b [n]] [label[/[subpath]]]
    
    positional arguments:
      label         name of the label
      subpath       path inside label's target (usage: label/subpath)
    
    optional arguments:
      -h, --help    shows help message an exit
      -b, --back    return to n-th previous 'goto' command; n is 1 by default

When you type `goto label` it internally does `cd target`, where `target` is the absolute path pointed by `label`. The option `-b` or `--back` returns to n-th previous `goto` command stored in the `~/.goto/stack` file and doesn't require the `label` argument.

goto label
----------

goto list
---------
