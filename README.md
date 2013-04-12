goto project - easy'n'fast cd'ing
=================================

(Fork of pauloborges/goto in python 3 and more "git like")

Tired of typing a lot to get where the fun is happening? `goto` was made for you!


goto
----
    usage: goto [-h] [-b [n]] [label[subpath]]
    
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
