#!/bin/bash


goto()
{
    ARGS="$@"
    bootstrap_goto.py goto $ARGS
}


goto-label()
{
    ARGS="$@"
    bootstrap_goto.py goto-label $ARGS
}


# goto-list()
# {
#     ARGS="$@"
#     bootstrap_goto.py goto-list $ARGS
# }


# goto-back()
# {
#     ARGS="$@"
#     bootstrap_goto.py goto-back $ARGS
# }